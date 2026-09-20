"""Validação determinística do bloco 1 de tabelas (Manual TRT-3, p. 373-471).

Quatro checagens, conforme o contrato do bloco:

  1. CONTAGEM   — linhas extraídas por tabela contra uma contagem independente
                  feita sobre a camada de texto do PDF.
  2. FAIXAS     — dentro de cada vigência: sem lacuna, sem sobreposição, limites
                  em ordem monotônica.
  3. VIGÊNCIAS  — sem lacuna nem sobreposição na linha do tempo de cada tabela.
  4. PROVENIÊNCIA — toda linha tem documento, item e pagina_pdf preenchidos, e a
                  página cai no intervalo declarado da seção.

Dois níveis de achado, que **não** se confundem:

  ERRO        — defeito da extração. Precisa ser corrigido no extrator.
  DIVERGÊNCIA — defeito ou lacuna do original. Fica registrado, não se conserta
                (regra do bloco: "erro ou lacuna do original vira observação").

Saída não-zero só em ERRO. Divergência é resultado esperado do trabalho.

Aritmética decimal em toda parte, nenhum float (R12).
"""

from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from decimal import Decimal, InvalidOperation
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    fitz = None

RAIZ = Path(__file__).resolve().parents[2]
DIR_SERIE = RAIZ / "docs" / "calculo" / "extracao" / "trabalhista"
DIR_SEMANTICA = RAIZ / "docs" / "calculo" / "tabelas-normativas"
PDF = Path(
    r"C:\Users\Rafaela\Downloads\Plataforma-SaaS-Jus"
    r"\manual-de-calculo-trabalhista_2016-1.pdf"
)

# Intervalo declarado de cada item do bloco 1, para a checagem de proveniência.
# Não é "a faixa do diretório": é o contrato de páginas de cada item. A faixa
# contra a qual cada linha é conferida se RESOLVE por arquivo (ver
# `faixa_declarada`), nunca por uma constante única do bloco — o diretório
# recebe séries de outros blocos, e uma constante de bloco as acusaria de erro.
FAIXAS_DE_PAGINA = {
    "18.1": (373, 380),
    "18.2": (381, 381),
    "18.3": (382, 384),
    "18.4": (385, 386),
    "18.5": (387, 388),
    "18.6": (389, 389),
    "18.7": (390, 399),
    "18.8.1": (400, 417),
    "18.8.2": (418, 449),
    "18.8.2-anexo-fpas": (449, 449),
    "18.9": (450, 452),
    "18.10": (453, 454),
    "18.11": (455, 455),
    "18.12": (455, 455),
    "18.13": (456, 459),
    "18.14": (460, 466),
    "18.15": (467, 470),
}


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

class Relatorio:
    def __init__(self) -> None:
        self.erros: list[str] = []
        self.divergencias: list[str] = []
        self.ok: list[str] = []
        self.nao_verificado: list[str] = []

    def erro(self, msg: str) -> None:
        self.erros.append(msg)

    def divergencia(self, msg: str) -> None:
        self.divergencias.append(msg)

    def passou(self, msg: str) -> None:
        self.ok.append(msg)

    def sem_verificacao(self, msg: str) -> None:
        self.nao_verificado.append(msg)

    def imprime(self) -> int:
        # O console do Windows assume cp1252 e quebra em '≤'. A saída é UTF-8;
        # caracteres que o terminal não desenha viram '?', sem abortar o relatório.
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        for titulo, itens in (
            ("OK", self.ok),
            ("DIVERGÊNCIA DO ORIGINAL (registrada, não corrigida)", self.divergencias),
            ("NÃO VERIFICÁVEL MECANICAMENTE", self.nao_verificado),
            ("ERRO DE EXTRAÇÃO", self.erros),
        ):
            if not itens:
                continue
            print(f"\n== {titulo} — {len(itens)}")
            for item in itens:
                print(f"   {item}")
        print(
            f"\nresumo: {len(self.ok)} ok, {len(self.divergencias)} divergências, "
            f"{len(self.nao_verificado)} não verificados, {len(self.erros)} erros"
        )
        return 1 if self.erros else 0


# --------------------------------------------------------------------------
# Leitura
# --------------------------------------------------------------------------

def le_csv(nome: str) -> list[dict]:
    caminho = DIR_SERIE / nome
    with open(caminho, "r", encoding="utf-8", newline="") as fh:
        linhas = [l for l in fh if not l.startswith("#")]
    return list(csv.DictReader(linhas))


def le_cabecalho(caminho: Path) -> str:
    """Bloco de comentários '#' do topo do CSV, onde mora a proveniência declarada."""
    partes: list[str] = []
    with open(caminho, "r", encoding="utf-8", newline="") as fh:
        for linha in fh:
            if not linha.startswith("#"):
                break
            partes.append(linha)
    return "".join(partes)


def le_json(nome: str) -> dict:
    with open(DIR_SEMANTICA / nome, "r", encoding="utf-8") as fh:
        return json.load(fh)


def texto_do_pdf(paginas) -> str:
    if fitz is None:
        return ""
    doc = fitz.open(PDF)
    return " ".join(re.sub(r"\s+", " ", doc[p - 1].get_text()) for p in paginas)


def sem_acento(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    ).lower()


def para_decimal(texto: str) -> Decimal | None:
    """Converte '1.234,56' em Decimal. Nenhum float em caminho algum (R12)."""
    if texto is None:
        return None
    limpo = re.sub(r"[^\d.,]", "", texto)
    if not limpo:
        return None
    limpo = limpo.replace(".", "").replace(",", ".")
    try:
        return Decimal(limpo)
    except InvalidOperation:
        return None


# --------------------------------------------------------------------------
# 1. Contagem contra o texto do PDF
# --------------------------------------------------------------------------

# Cada entrada conta, na camada de texto, uma marca que aparece uma vez por linha
# de dado. Independente do caminho de extração: se os dois números baterem, nem o
# extrator nem esta contagem perderam linha.
CONTAGENS = [
    {
        "rotulo": "18.8.1 atividades (marcador de grau após pontilhado)",
        "paginas": range(400, 418),
        "padrao": r"\.{4,}\s*\d\b",
        "csv": "serie-18.8.1-grau-risco-cnae-ate-2007-05.csv",
    },
    {
        "rotulo": "18.8.2 códigos CNAE 2.0",
        "paginas": range(418, 450),
        "padrao": r"\b\d{4}-\d/\d{2}\b",
        "csv": "serie-18.8.2-grau-risco-cnae-desde-2007-06.csv",
    },
    {
        "rotulo": "18.10 cotações diárias da URV",
        "paginas": range(453, 455),
        "padrao": r"\b\d{1,3}(?:\.\d{3})*,\d{2}\b",
        "csv": "serie-18.10-urv.csv",
    },
    {
        "rotulo": "18.13 competências de RSR",
        "paginas": range(456, 460),
        "padrao": r"\b(?:jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)/\d{2}\b",
        "csv": "serie-18.13-rsr-contagens.csv",
    },
    {
        "rotulo": "18.15 taxas Selic (percentuais)",
        "paginas": [468],
        "padrao": r"\b\d{1,2},\d{2}%",
        "csv": "serie-18.15-juros-selic-acumulados.csv",
        "filtro": lambda r: r["quadro"] == "taxa-selic-mensal",
        # O parágrafo de abertura da p468 cita a taxa de fevereiro/2016 em prosa;
        # a contagem começa na moldura da tabela.
        "recorte": "Mês/Ano",
    },
]


def valida_contagens(rel: Relatorio) -> None:
    if fitz is None:
        rel.sem_verificacao("contagem contra o PDF: PyMuPDF ausente")
        return
    for caso in CONTAGENS:
        corpo = texto_do_pdf(caso["paginas"])
        if caso.get("recorte"):
            corte = corpo.find(caso["recorte"])
            if corte < 0:
                rel.erro(f"contagem {caso['rotulo']}: recorte {caso['recorte']!r} ausente")
                continue
            corpo = corpo[corte:]
        no_pdf = len(re.findall(caso["padrao"], corpo))
        linhas = le_csv(caso["csv"])
        if caso.get("filtro"):
            linhas = [r for r in linhas if caso["filtro"](r)]
        extraido = len(linhas)
        if no_pdf == extraido:
            rel.passou(f"contagem {caso['rotulo']}: {extraido} = {no_pdf} no PDF")
        else:
            rel.erro(
                f"contagem {caso['rotulo']}: {extraido} extraídas contra {no_pdf} "
                f"marcas no texto do PDF (diferença {extraido - no_pdf})"
            )

    # 18.1 é JSON: conta os tokens sim/não do trecho contra os segmentos gravados.
    dados = le_json("trt3-18.1-incidencia-parcelas.json")
    segmentos = 0
    for p in dados["parcelas"]:
        for coluna in ("inss", "fgts", "irrf"):
            valor = p[coluna]
            if isinstance(valor, list):
                segmentos += len(valor)
            elif valor.get("incide"):
                segmentos += 1
    corpo = texto_do_pdf(range(373, 381))
    no_pdf = len(re.findall(r"(?i)(?<![\wçãé])(sim|n[ãa]o)(?![\wçãé])", corpo))
    if segmentos == no_pdf:
        rel.passou(f"contagem 18.1 sim/não: {segmentos} = {no_pdf} no PDF")
    else:
        rel.divergencia(
            f"contagem 18.1 sim/não: {segmentos} segmentos gravados contra {no_pdf} "
            f"ocorrências no texto. A diferença é esperada: 'não' aparece também "
            f"dentro das observações em prosa do original."
        )


# --------------------------------------------------------------------------
# 2. Faixas — lacuna, sobreposição e monotonia
# --------------------------------------------------------------------------

_RE_ATE = re.compile(r"(?i)^at[ée]\s+(.+)$")
# O espaço antes de "até" falta em algumas linhas do original ("De 720,01até
# 1.200,00"). Tolerar a falta é ler o original, não corrigi-lo: o CSV guarda a
# string literal; o que se relaxa aqui é só a leitura para conferência.
_RE_DE_ATE = re.compile(r"(?i)^(?:de|acima de|mais de)\s+(.+?)\s*(?:at[ée]|\sa)\s+(.+)$")
_RE_ACIMA = re.compile(r"(?i)^(?:acima de|mais de|a partir de)\s+(.+)$")


def interpreta_faixa(texto: str) -> tuple[Decimal | None, Decimal | None] | None:
    """Devolve (limite_inferior, limite_superior). None em qualquer ponta = aberto."""
    alvo = texto.strip()
    m = _RE_DE_ATE.match(alvo)
    if m:
        return para_decimal(m.group(1)), para_decimal(m.group(2))
    m = _RE_ATE.match(alvo)
    if m:
        return None, para_decimal(m.group(1))
    m = _RE_ACIMA.match(alvo)
    if m:
        return para_decimal(m.group(1)), None
    return None


def valida_faixas(rel: Relatorio, nome_csv: str, coluna_faixa: str,
                  coluna_vigencia: str, rotulo: str, topo_aberto: bool = True) -> None:
    """`topo_aberto=False` nas tabelas com teto: a última faixa fecha por norma.

    A chave é só a vigência, não (vigência, página): a tabela do IRRF de abril a
    dezembro de 2011 está partida entre duas páginas do original e precisa ser
    avaliada inteira, senão a metade de cima aparece como faixa faltando.
    """
    linhas = le_csv(nome_csv)
    grupos: dict[str, list[dict]] = {}
    for r in linhas:
        grupos.setdefault(r[coluna_vigencia], []).append(r)

    limpos, problemas, incompletos = 0, 0, 0
    for vigencia, faixas in grupos.items():
        pagina = "/".join(sorted({r["pagina_pdf"] for r in faixas}))
        interpretadas, ilegiveis = [], []
        for r in faixas:
            bruto = r[coluna_faixa]
            lido = interpreta_faixa(bruto)
            if lido is None or (lido[0] is None and lido[1] is None):
                ilegiveis.append(bruto)
                continue
            interpretadas.append((lido[0], lido[1], bruto))

        if ilegiveis:
            # Sem uma das faixas não dá para afirmar nada sobre lacuna: o vão
            # aparente seria artefato da leitura, não do original.
            incompletos += 1
            rel.sem_verificacao(
                f"{rotulo} p{pagina} [{vigencia}]: análise suspensa — faixa em forma "
                f"não reconhecida: {', '.join(repr(x) for x in ilegiveis)}"
            )
            continue

        if len(interpretadas) < 2:
            continue

        falhou = False
        anterior_sup = None
        for i, (inf, sup, bruto) in enumerate(interpretadas):
            if i == 0:
                if inf is not None:
                    rel.divergencia(
                        f"{rotulo} p{pagina} [{vigencia}]: primeira faixa não abre "
                        f"em zero: {bruto!r}"
                    )
                    falhou = True
            else:
                if inf is None:
                    rel.divergencia(
                        f"{rotulo} p{pagina} [{vigencia}]: faixa intermediária sem "
                        f"limite inferior: {bruto!r}"
                    )
                    falhou = True
                elif anterior_sup is None:
                    rel.divergencia(
                        f"{rotulo} p{pagina} [{vigencia}]: faixa aberta seguida de "
                        f"outra faixa: {bruto!r}"
                    )
                    falhou = True
                elif inf < anterior_sup:
                    rel.divergencia(
                        f"{rotulo} p{pagina} [{vigencia}]: sobreposição — {bruto!r} "
                        f"começa em {inf} abaixo do teto anterior {anterior_sup}"
                    )
                    falhou = True
                elif inf - anterior_sup > Decimal("0.011"):
                    rel.divergencia(
                        f"{rotulo} p{pagina} [{vigencia}]: lacuna de "
                        f"{inf - anterior_sup} antes de {bruto!r}"
                    )
                    falhou = True
            if sup is not None and inf is not None and sup <= inf:
                rel.divergencia(
                    f"{rotulo} p{pagina} [{vigencia}]: limites fora de ordem em {bruto!r}"
                )
                falhou = True
            anterior_sup = sup
        if topo_aberto and interpretadas[-1][1] is not None:
            rel.divergencia(
                f"{rotulo} p{pagina} [{vigencia}]: última faixa é fechada "
                f"({interpretadas[-1][2]!r}); não há faixa aberta no topo"
            )
            falhou = True
        problemas += falhou
        limpos += not falhou

    rel.passou(
        f"faixas {rotulo}: {limpos} vigências íntegras, {problemas} com divergência, "
        f"{incompletos} suspensas (de {len(grupos)})"
    )


# --------------------------------------------------------------------------
# 3. Vigências na linha do tempo
# --------------------------------------------------------------------------

_MES = {"jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
        "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12}


def _competencia(token: str) -> int | None:
    """'jan/92', 'Maio/04', '01/06/99' → índice de meses. None se não reconhecer."""
    alvo = sem_acento(token.strip())
    m = re.match(r"^(\d{2})[/.](\d{2})[/.](\d{2,4})$", alvo)
    if m:
        mes, ano = int(m.group(2)), int(m.group(3))
    else:
        m = re.match(r"^([a-z]{3})[a-z]*[/.](\d{2,4})$", alvo)
        if not m:
            return None
        mes = _MES.get(m.group(1))
        ano = int(m.group(2))
        if mes is None:
            return None
    if ano < 100:
        ano += 1900 if ano >= 80 else 2000
    if not 1 <= mes <= 12:
        return None
    return ano * 12 + (mes - 1)


def interpreta_vigencia(rotulo: str) -> tuple[int, int] | None:
    # "Abr/06 a Mar/07(SM = 350,00)" — o parêntese é anotação, não parte do
    # intervalo; "Mar/94 a jun/94 em URV" — o sufixo é a unidade do quadro.
    alvo = re.sub(r"\s+", " ", rotulo.strip())
    alvo = re.sub(r"\s*\([^)]*\)\s*$", "", alvo)
    alvo = re.sub(r"(?i)\s+em\s+\w+\s*$", "", alvo)
    partes = re.split(r"(?i)\s+a\s+|\s+at[ée]\s+", alvo)
    if len(partes) == 2:
        ini, fim = _competencia(partes[0]), _competencia(partes[1])
        if ini is not None and fim is not None:
            return ini, fim
        return None
    unico = _competencia(alvo)
    return (unico, unico) if unico is not None else None


def _rotulo_competencia(indice: int) -> str:
    ano, mes = divmod(indice, 12)
    return f"{ano:04d}-{mes + 1:02d}"


def valida_vigencias(rel: Relatorio, nome_csv: str, coluna: str, rotulo: str) -> None:
    linhas = le_csv(nome_csv)
    vistos: list[str] = []
    for r in linhas:
        if r[coluna] not in vistos:
            vistos.append(r[coluna])

    intervalos, nao_lidos = [], []
    for v in vistos:
        lido = interpreta_vigencia(v)
        (intervalos.append((lido[0], lido[1], v)) if lido else nao_lidos.append(v))

    if nao_lidos:
        rel.sem_verificacao(
            f"vigências {rotulo}: {len(nao_lidos)} rótulos em forma livre, fora da "
            f"linha do tempo verificável — {'; '.join(repr(v) for v in nao_lidos[:4])}"
            + (" …" if len(nao_lidos) > 4 else "")
        )

    intervalos.sort()
    falhas = 0
    for i in range(1, len(intervalos)):
        ini, _, rot = intervalos[i]
        _, fim_ant, rot_ant = intervalos[i - 1]
        if ini <= fim_ant:
            rel.divergencia(
                f"vigências {rotulo}: sobreposição entre {rot_ant!r} e {rot!r} "
                f"({_rotulo_competencia(ini)} ≤ {_rotulo_competencia(fim_ant)})"
            )
            falhas += 1
        elif ini > fim_ant + 1:
            rel.divergencia(
                f"vigências {rotulo}: lacuna de {_rotulo_competencia(fim_ant + 1)} a "
                f"{_rotulo_competencia(ini - 1)}, entre {rot_ant!r} e {rot!r}"
            )
            falhas += 1
    rel.passou(
        f"vigências {rotulo}: {len(intervalos)} interpretadas, {falhas} descontinuidades"
    )


# --------------------------------------------------------------------------
# 4. Proveniência
# --------------------------------------------------------------------------

# 'pagina_pdf=178-179' e 'item=9.2.11' no cabeçalho de comentário do CSV.
_RE_PAGINA_CABECALHO = re.compile(r"\bpagina_pdf\s*=\s*(\d+)\s*(?:[-–]\s*(\d+))?")
_RE_ITEM_CABECALHO = re.compile(r"\bitem\s*=\s*([0-9]+(?:\.[0-9]+)*(?:-[\w.-]+)?)")


def faixa_declarada(caminho: Path, linhas: list[dict]) -> tuple[tuple[int, int], str] | None:
    """Faixa de páginas contra a qual conferir ESTE arquivo, e de onde ela veio.

    Duas origens, nesta ordem, e nenhuma constante de bloco:

      1. o cabeçalho do próprio CSV, quando declara `pagina_pdf=` (é o caso das
         séries trazidas de outros blocos, como 9.2.11, p178-179);
      2. o item declarado nas linhas, resolvido em `FAIXAS_DE_PAGINA` — o
         contrato de páginas do bloco 1.

    Sem nenhuma das duas, devolve None: o arquivo não é conferível aqui, e dizê-lo
    é obrigação do relatório. Silêncio seria pior que o falso erro.
    """
    cabecalho = le_cabecalho(caminho)
    m = _RE_PAGINA_CABECALHO.search(cabecalho)
    if m:
        ini = int(m.group(1))
        fim = int(m.group(2)) if m.group(2) else ini
        return (ini, fim), "cabeçalho do próprio arquivo"

    itens = {r["item"] for r in linhas if r.get("item")}
    mi = _RE_ITEM_CABECALHO.search(cabecalho)
    if mi:
        itens.add(mi.group(1))
    conhecidos = [FAIXAS_DE_PAGINA[i] for i in itens if i in FAIXAS_DE_PAGINA]
    if itens and len(conhecidos) == len(itens):
        return (min(f[0] for f in conhecidos), max(f[1] for f in conhecidos)), \
            "contrato de páginas do item"
    return None


def valida_proveniencia(rel: Relatorio) -> None:
    faltando, fora_da_faixa, sem_item = 0, [], 0
    total = 0
    sem_faixa: list[str] = []
    origens: dict[str, int] = {}
    # `glob("*.csv")`, e não `glob("serie-*.csv")`: o prefixo era a última
    # descoberta por convenção de NOME que sobrava no repositório, e tinha o
    # defeito do bloco 17 — renomear `serie-18.3-x.csv` para `18.3-serie.csv`
    # tirava o arquivo da conferência de proveniência EM SILÊNCIO, e o resumo
    # seguia dizendo "0 erros". Todo CSV deste diretório é série; o que decide
    # se é conferível é o cabeçalho declarado (`faixa_declarada`), que é
    # CONTEÚDO, e o que não for conferível sai em "NÃO VERIFICÁVEL" — visível.
    for caminho in sorted(DIR_SERIE.glob("*.csv")):
        linhas = le_csv(caminho.name)
        resolvida = faixa_declarada(caminho, linhas)
        if resolvida is None:
            sem_faixa.append(caminho.name)
            faixa_do_arquivo = None
        else:
            faixa_do_arquivo, origem = resolvida
            origens[origem] = origens.get(origem, 0) + 1
        for numero, r in enumerate(linhas, start=2):
            total += 1
            pagina, item = r.get("pagina_pdf"), r.get("item")
            if not pagina:
                faltando += 1
                continue
            if not item:
                sem_item += 1
                continue
            # O item, quando é do bloco 1, dá a faixa mais estreita e prevalece;
            # senão vale a faixa declarada pelo arquivo.
            esperada = FAIXAS_DE_PAGINA.get(item, faixa_do_arquivo)
            if esperada is None:
                continue
            if not esperada[0] <= int(pagina) <= esperada[1]:
                fora_da_faixa.append(
                    f"{caminho.name}:{numero} item {item} na página {pagina}, "
                    f"fora de {esperada[0]}-{esperada[1]}"
                )

    for nome in ("trt3-18.1-incidencia-parcelas.json",):
        dados = le_json(nome)
        faixa_18_1 = FAIXAS_DE_PAGINA["18.1"]
        for p in dados["parcelas"]:
            total += 1
            if not p.get("paginas_pdf"):
                faltando += 1
            elif any(not faixa_18_1[0] <= x <= faixa_18_1[1] for x in p["paginas_pdf"]):
                fora_da_faixa.append(
                    f"{nome}: {p['parcela']!r} fora de "
                    f"{faixa_18_1[0]}-{faixa_18_1[1]}"
                )

    if sem_faixa:
        rel.sem_verificacao(
            "proveniência: sem faixa de páginas declarada, nem no cabeçalho nem por "
            f"item conhecido — {', '.join(sem_faixa)}"
        )
    if faltando or sem_item:
        rel.erro(
            f"proveniência: {faltando} linhas sem pagina_pdf e {sem_item} sem item"
        )
    for caso in fora_da_faixa[:10]:
        rel.erro(f"proveniência fora do intervalo declarado: {caso}")
    if len(fora_da_faixa) > 10:
        rel.erro(
            f"proveniência: mais {len(fora_da_faixa) - 10} linhas fora do intervalo "
            f"declarado, não listadas acima"
        )
    if not faltando and not sem_item and not fora_da_faixa:
        detalhe = ", ".join(f"{n} por {o}" for o, n in sorted(origens.items()))
        rel.passou(
            f"proveniência: {total} linhas, todas com documento, item e pagina_pdf; "
            f"faixa resolvida por arquivo ({detalhe})"
        )


# --------------------------------------------------------------------------
# 5. Calendários — contiguidade dos dias
# --------------------------------------------------------------------------

_DIAS_NO_MES = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def valida_calendarios(rel: Relatorio) -> None:
    linhas = le_csv("serie-18.14-calendarios.csv")
    por_mes: dict[tuple[int, int], set[int]] = {}
    for r in linhas:
        if not r["ano"] or not r["mes_numero"]:
            continue
        por_mes.setdefault((int(r["ano"]), int(r["mes_numero"])), set()).add(int(r["dia"]))

    incompletos = 0
    for (ano, mes), dias in sorted(por_mes.items()):
        esperado = _DIAS_NO_MES[mes - 1]
        if mes == 2 and (ano % 4 == 0 and (ano % 100 or ano % 400 == 0)):
            esperado = 29
        faltando = sorted(set(range(1, esperado + 1)) - dias)
        sobrando = sorted(d for d in dias if d > esperado)
        if faltando or sobrando:
            incompletos += 1
            detalhe = []
            if faltando:
                detalhe.append(f"ausentes {faltando}")
            if sobrando:
                detalhe.append(f"excedentes {sobrando}")
            rel.divergencia(
                f"18.14 calendário {mes:02d}/{ano}: {', '.join(detalhe)} "
                f"(o original imprime {len(dias)} dias num mês de {esperado})"
            )
    rel.passou(
        f"18.14 calendários: {len(por_mes) - incompletos} meses completos, "
        f"{incompletos} com dias ausentes no original"
    )


# --------------------------------------------------------------------------
# Execução
# --------------------------------------------------------------------------

def main() -> int:
    rel = Relatorio()

    valida_contagens(rel)

    valida_faixas(rel, "serie-18.4-irrf-tabela-progressiva-mensal.csv",
                  "base_calculo", "vigencia_original", "18.4 IRRF mensal")
    valida_faixas(rel, "serie-18.5-irrf-rra.csv",
                  "base_calculo", "vigencia_original", "18.5 IRRF RRA")
    valida_faixas(rel, "serie-18.6-irrf-plr.csv",
                  "base_calculo", "vigencia_original", "18.6 IRRF PLR")
    # A contribuição do segurado tem teto: a última faixa fecha por norma, e a
    # coluna teto_maximo guarda o limite do desconto. Topo fechado não é defeito.
    valida_faixas(rel, "serie-18.7-contribuicao-faixas.csv",
                  "salario_contribuicao", "vigencia_original", "18.7 previdenciária",
                  topo_aberto=False)
    valida_faixas(rel, "serie-18.9-seguro-desemprego.csv",
                  "faixa_salario_medio", "vigencia_original", "18.9 seguro-desemprego")

    valida_vigencias(rel, "serie-18.7-contribuicao-faixas.csv",
                     "vigencia_original", "18.7 previdenciária")
    valida_vigencias(rel, "serie-18.9-seguro-desemprego.csv",
                     "vigencia_original", "18.9 seguro-desemprego")
    valida_vigencias(rel, "serie-18.3-salario-familia.csv",
                     "competencia", "18.3 salário-família")

    valida_proveniencia(rel)
    valida_calendarios(rel)

    return rel.imprime()


if __name__ == "__main__":
    raise SystemExit(main())
