"""Extração determinística do bloco 1 — tabelas do Manual TRT-3 (2016), p. 373-471.

Fase 2 do pipeline (`docs/calculo/01-plano-extracao.md`). Conteúdo tabular sai como
JSON/CSV e é validado por `valida_bloco_tabelas.py`, não por revisão de LLM
(regra 2 das "Regras de trabalho para os agentes").

Duas categorias, destinos diferentes:

  (A) SEMÂNTICA → docs/calculo/tabelas-normativas/*.json
      Regra estrutural que não muda com o tempo.

  (B) SÉRIE → docs/calculo/extracao/trabalhista/*.csv, marcada OUT_OF_SCOPE
      Valor que muda periodicamente e tem manutenção separada.

O script **não corrige, não harmoniza e não completa**. Lacuna ou erro do original
vira campo `observacao` ou linha marcada, nunca conserto.

Uso:
    python extrai_bloco_01.py [secao ...]      # default: todas
    python extrai_bloco_01.py --listar

Requer PyMuPDF. `pdftotext` não está instalado no ambiente de referência; a camada
de texto é lida diretamente do PDF, sempre decodificada como UTF-8.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    sys.exit("PyMuPDF não instalado: pip install pymupdf")

# --------------------------------------------------------------------------
# Localização
# --------------------------------------------------------------------------

PDF = Path(
    r"C:\Users\Rafaela\Downloads\Plataforma-SaaS-Jus"
    r"\manual-de-calculo-trabalhista_2016-1.pdf"
)
DOCUMENTO = "manual-de-calculo-trabalhista_2016-1.pdf"
EMISSOR = "TRT-3, Secretaria de Cálculos Judiciais, julho/2016"
OFFSET_PAGINACAO = 0  # numero_impresso == pagina_pdf neste manual (docs/calculo/fontes.md)

RAIZ = Path(__file__).resolve().parents[2]
DIR_SEMANTICA = RAIZ / "docs" / "calculo" / "tabelas-normativas"
DIR_SERIE = RAIZ / "docs" / "calculo" / "extracao" / "trabalhista"

CABECALHO_SERIE = (
    "# OUT_OF_SCOPE — série de valores, não entra na skill.",
    "# Manutenção separada (regra 4 de 01-plano-extracao.md). Aqui só como",
    "# evidência de conferência contra a tabela mantida à parte.",
    f"# documento={DOCUMENTO} emissor={EMISSOR} offset_paginacao={OFFSET_PAGINACAO}",
)


# --------------------------------------------------------------------------
# Utilitários
# --------------------------------------------------------------------------

def abre() -> "fitz.Document":
    if not PDF.exists():
        sys.exit(f"PDF não encontrado: {PDF}\nVer docs/calculo/fontes.md")
    return fitz.open(PDF)


def tabelas(doc, pagina_pdf: int) -> list[list[list[str]]]:
    """Devolve as tabelas de uma página como matriz de strings (nunca None)."""
    achadas = doc[pagina_pdf - 1].find_tables().tables
    return [[[c or "" for c in linha] for linha in t.extract()] for t in achadas]


def texto(doc, pagina_pdf: int) -> str:
    return doc[pagina_pdf - 1].get_text()


def limpa(s: str) -> str:
    """Normaliza espaços e travessões sem alterar o conteúdo."""
    s = s.replace("­", "").replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", s).strip()


def uma_linha(s: str) -> str:
    return limpa(re.sub(r"\s*\n\s*", " ", s))


def sem_acento(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    ).lower()


def grava_json(nome: str, dados: dict) -> Path:
    destino = DIR_SEMANTICA / nome
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(dados, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    return destino


def grava_csv(nome: str, colunas: list[str], linhas: list[dict], notas=()) -> Path:
    destino = DIR_SERIE / nome
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "w", encoding="utf-8", newline="") as fh:
        for linha in (*CABECALHO_SERIE, *notas):
            fh.write(linha.rstrip() + "\n")
        w = csv.DictWriter(fh, fieldnames=colunas, extrasaction="raise")
        w.writeheader()
        w.writerows(linhas)
    return destino


def _fonte(item: str, paginas: list[int], **extra) -> dict:
    d = {
        "documento": DOCUMENTO,
        "emissor": EMISSOR,
        "item": item,
        "paginas_pdf": paginas,
        "offset_paginacao": OFFSET_PAGINACAO,
    }
    d.update(extra)
    return d


# --------------------------------------------------------------------------
# 18.1 — incidência de INSS, FGTS e IRRF por parcela  (categoria A)
# --------------------------------------------------------------------------

P_181 = list(range(373, 381))

_RE_VALOR = re.compile(r"^(sim|n[ãa]o|isento)\s*$", re.IGNORECASE)
_RE_MARCADOR_DETALHE = re.compile(
    r"^\s*(?:[a-z]\)|\(\s*\*\s*\)|\*|notas?\b|observa[çc][õo]es?\b|\d+\s*[º°]?\s*-)",
    re.IGNORECASE,
)


def _parte_valor(celula: str) -> list[dict]:
    """Quebra uma célula em segmentos `sim|não` + fundamento.

    O fundamento legal é parte do dado: cada coluna do original traz o valor e a
    norma que o sustenta. Célula sem token de valor é continuação de página ou
    lacuna do original — devolve lista vazia, e quem chama decide.
    """
    segmentos: list[dict] = []
    atual: dict | None = None
    for linha in celula.split("\n"):
        alvo = limpa(linha)
        if not alvo:
            continue
        m = _RE_VALOR.match(alvo)
        if m:
            bruto = m.group(1)
            atual = {
                "incide": "sim" if sem_acento(bruto) == "sim" else "nao",
                "valor_original": bruto,
                "fundamento": [],
            }
            segmentos.append(atual)
        elif atual is not None:
            atual["fundamento"].append(alvo)
        else:
            segmentos.append({"incide": None, "valor_original": None, "fundamento": [alvo]})
            atual = segmentos[-1]
    for s in segmentos:
        s["fundamento"] = limpa(" ".join(s["fundamento"])) or None
    return [s for s in segmentos if s["incide"] is not None or s["fundamento"]]


def _rotula_parcela(celula: str) -> tuple[str, str | None, str]:
    """Separa o nome da parcela do detalhamento (alíneas, notas, observações).

    Devolve `(nome, detalhamento, heuristica)`. A heurística fica gravada porque
    o original quebra o nome em várias linhas sem marcador em alguns casos, e
    isso não é distinguível de um detalhamento por regra mecânica.
    """
    linhas = [limpa(x) for x in celula.split("\n")]
    linhas = [x for x in linhas if x]
    if not linhas:
        return "", None, "celula-vazia"
    corte = next(
        (i for i, x in enumerate(linhas) if _RE_MARCADOR_DETALHE.match(x)),
        len(linhas),
    )
    if corte == 0:  # a célula começa já no detalhamento
        return limpa(linhas[0]), limpa(" ".join(linhas[1:])) or None, "sem-nome-marcador-na-linha-1"
    nome = limpa(" ".join(linhas[:corte]))
    detalhe = limpa(" ".join(linhas[corte:])) or None
    if corte == 1:
        heuristica = "linha-unica" if detalhe is None else "ate-marcador"
    elif corte == len(linhas):
        heuristica = "celula-inteira-multilinha"  # nome quebrado OU detalhe sem marcador
    else:
        heuristica = "ate-marcador"
    return nome, detalhe, heuristica


def extrai_18_1(doc) -> dict:
    colunas = ("inss", "fgts", "irrf")
    parcelas: list[dict] = []
    continuacoes: list[dict] = []
    cabecalhos = 0

    for pagina in P_181:
        for tabela in tabelas(doc, pagina):
            for linha in tabela:
                if len(linha) != 4:
                    raise AssertionError(f"p{pagina}: linha com {len(linha)} colunas, esperado 4")
                celula_parcela, *celulas_valor = linha
                if uma_linha(celula_parcela).lower() == "parcela":
                    cabecalhos += 1
                    continue

                partes = {c: _parte_valor(v) for c, v in zip(colunas, celulas_valor)}
                tem_valor = any(
                    any(s["incide"] is not None for s in partes[c]) for c in colunas
                )

                if not tem_valor:
                    # Quebra de página: a linha anterior continua aqui.
                    if not parcelas:
                        raise AssertionError(f"p{pagina}: continuação sem linha anterior")
                    alvo = parcelas[-1]
                    registro = {
                        "pagina_pdf": pagina,
                        "parcela_continuada": alvo["parcela"],
                        "fragmentos": {},
                    }
                    if limpa(celula_parcela):
                        fragmento = uma_linha(celula_parcela)
                        alvo["detalhamento"] = limpa(
                            f"{alvo.get('detalhamento') or ''} {fragmento}"
                        )
                        registro["fragmentos"]["parcela"] = fragmento
                    for c, segmentos in partes.items():
                        fragmento = limpa(" ".join(s["fundamento"] or "" for s in segmentos))
                        if not fragmento:
                            continue
                        registro["fragmentos"][c] = fragmento
                        alvo_col = alvo[c]
                        destino = alvo_col[-1] if isinstance(alvo_col, list) else alvo_col
                        destino["fundamento"] = limpa(
                            f"{destino.get('fundamento') or ''} {fragmento}"
                        )
                    alvo["paginas_pdf"].append(pagina)
                    alvo["observacao"] = limpa(
                        (alvo.get("observacao") or "")
                        + f" Linha dividida pela quebra de página: fundamento continua na p.{pagina}."
                    )
                    continuacoes.append(registro)
                    continue

                nome, detalhe, heuristica = _rotula_parcela(celula_parcela)
                registro = {
                    "parcela": nome,
                    "detalhamento": detalhe,
                    "heuristica_nome": heuristica,
                    "paginas_pdf": [pagina],
                    "parcela_texto_bruto": limpa(celula_parcela.replace("\n", " | ")),
                }
                faltando = []
                for c in colunas:
                    segmentos = partes[c]
                    if not segmentos:
                        registro[c] = {"incide": None, "fundamento": None}
                        faltando.append(c.upper())
                    elif len(segmentos) == 1:
                        registro[c] = {
                            "incide": segmentos[0]["incide"],
                            "fundamento": segmentos[0]["fundamento"],
                        }
                    else:
                        registro[c] = [
                            {"ordem": i + 1, "incide": s["incide"], "fundamento": s["fundamento"]}
                            for i, s in enumerate(segmentos)
                        ]
                if faltando:
                    registro["observacao"] = (
                        "Lacuna do original: coluna(s) "
                        + ", ".join(faltando)
                        + " sem valor. Não preenchida."
                    )
                parcelas.append(registro)

    return {
        "id": "trab.incidencia.parcelas",
        "categoria": "A-semantica",
        "titulo": "Incidência de INSS, FGTS e IRRF por parcela",
        "jurisdicao": "justica-do-trabalho",
        "componente": "descontos-e-encargos",
        "fonte": _fonte("18.1", P_181),
        "colunas": {
            "inss": "Contribuição previdenciária — integra o salário de contribuição?",
            "fgts": "FGTS — integra a base de incidência do depósito?",
            "irrf": "Imposto de renda retido na fonte — é rendimento tributável?",
        },
        "notas_de_leitura": [
            "O fundamento legal é parte do dado, não anotação: a mesma parcela muda "
            "de tratamento conforme a norma invocada e a data.",
            "Quando a coluna traz mais de um valor, a parcela tem alíneas no original "
            "e a lista preserva a ordem das alíneas.",
            "Manual de 2016: anterior à Lei 13.467/2017. Toda incidência aqui é "
            "hipótese a confrontar na Fase 4, não norma vigente.",
        ],
        "estatisticas": {
            "parcelas": len(parcelas),
            "linhas_cabecalho_descartadas": cabecalhos,
            "linhas_de_continuacao_reunidas": len(continuacoes),
        },
        "continuacoes_de_pagina": continuacoes,
        "parcelas": parcelas,
    }


# --------------------------------------------------------------------------
# Auxiliares comuns às seções tabulares
# --------------------------------------------------------------------------

def matriz(doc, pagina: int, indice: int = 0, colapsa=True) -> list[list[str]]:
    """Tabela `indice` da página, com células em linha única.

    `colapsa` remove colunas vazias em todas as linhas — artefato da detecção de
    tabela, não do original.
    """
    todas = doc[pagina - 1].find_tables().tables
    if indice >= len(todas):
        raise AssertionError(f"p{pagina}: tabela {indice} inexistente ({len(todas)} detectadas)")
    linhas = [[uma_linha(c or "") for c in linha] for linha in todas[indice].extract()]
    if not colapsa:
        return linhas
    manter = [i for i in range(len(linhas[0])) if any(l[i] for l in linhas)]
    return [[l[i] for i in manter] for l in linhas]


def quantas_tabelas(doc, pagina: int) -> int:
    return len(doc[pagina - 1].find_tables().tables)


def titulos_no_texto(doc, pagina: int, prefixo: str) -> list[str]:
    """Títulos que ficam fora da moldura da tabela, na ordem de leitura."""
    achados = []
    for linha in texto(doc, pagina).split("\n"):
        alvo = limpa(linha)
        if alvo.lower().startswith(prefixo.lower()):
            achados.append(alvo)
    return achados


# --------------------------------------------------------------------------
# 18.2 — salário mínimo, moedas e paridades  (categoria B)
# --------------------------------------------------------------------------

_RE_ESPECIE = re.compile(r"^(PNS|SMR)\s+(.*)$")


def extrai_18_2(doc):
    linhas = matriz(doc, 381, 0)
    if len(linhas[0]) != 12:
        raise AssertionError(f"p381: esperadas 12 colunas colapsadas, vieram {len(linhas[0])}")

    minimos: list[dict] = []
    moedas: list[dict] = []
    paridades: list[dict] = []
    ordem = 0
    modo_g3 = "salario-minimo"

    for i, linha in enumerate(linhas):
        if i == 0:  # cabeçalho Data/valor repetido três vezes
            continue
        for g, inicio in enumerate((0, 4, 8), start=1):
            celulas = [c for c in linha[inicio:inicio + 4] if c]
            if not celulas:
                continue
            if g == 3 and celulas[0] in ("MOEDAS", "PARIDADES"):
                modo_g3 = celulas[0].lower()
                continue
            if g == 3 and modo_g3 != "salario-minimo":
                if celulas[0] in ("período", "Proporção"):  # cabeçalho interno
                    continue
                if len(celulas) < 2:
                    continue
                destino = moedas if modo_g3 == "moedas" else paridades
                destino.append({
                    "pagina_pdf": 381,
                    "item": "18.2",
                    "ordem": len(destino) + 1,
                    "campo_1": celulas[0],
                    "campo_2": celulas[1],
                })
                continue

            if len(celulas) == 2:
                data, valor = celulas
            elif len(celulas) == 1:
                data, valor = "", celulas[0]  # PNS/SMR do mesmo marco, sem data própria
            else:
                raise AssertionError(f"p381 linha {i} grupo {g}: {celulas}")
            m = _RE_ESPECIE.match(valor)
            especie, valor_num = (m.group(1), m.group(2)) if m else ("", valor)
            ordem += 1
            minimos.append({
                "pagina_pdf": 381,
                "item": "18.2",
                "ordem": ordem,
                "coluna_do_original": g,
                "data_vigencia": data,
                "especie": especie,
                "valor": valor_num,
                "observacao": "" if data else "sem data no original: mesmo marco da linha anterior",
            })

    a = grava_csv(
        "serie-18.2-salario-minimo.csv",
        ["pagina_pdf", "item", "ordem", "coluna_do_original", "data_vigencia",
         "especie", "valor", "observacao"],
        minimos,
        notas=("# especie: PNS = Piso Nacional de Salários, SMR = Salário Mínimo de Referência",
               "# (coexistiram entre 09/1987 e 07/1989). Vazio = salário mínimo único."),
    )
    b = grava_csv(
        "serie-18.2-moedas-e-paridades.csv",
        ["pagina_pdf", "item", "ordem", "campo_1", "campo_2"],
        [{**r, "bloco": None} and r for r in moedas + paridades],
        notas=("# Dois quadros sem numeração própria no original, impressos na margem",
               "# direita da tabela 18.2: MOEDAS (período/nomenclatura) e PARIDADES",
               "# (proporção/data). Fora do escopo declarado do bloco — ver relatório."),
    )
    return [
        f"{a.relative_to(RAIZ)}: {len(minimos)} marcos",
        f"{b.relative_to(RAIZ)}: {len(moedas)} moedas + {len(paridades)} paridades",
    ]


# --------------------------------------------------------------------------
# 18.3 — salário-família  (categoria B)
# --------------------------------------------------------------------------

_RE_FUNDAMENTO = re.compile(
    r"(?i)\b(portaria|o\.?\s?s\.?|i\.?\s?n\.?|in/|mp\b|medida provis|decreto|lei\b|resolu|dou)\b"
)
_RE_FAIXA = re.compile(r"(?i)^(at[ée]|acima|de)\b")
_RE_COMPETENCIA = re.compile(
    r"(?i)^(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)[a-zç]*/\d{2,4}|^\d{2}/\d{2}/\d{2,4}"
)


def _classifica_18_3(celula: str) -> str:
    if _RE_FUNDAMENTO.search(celula):
        return "fundamentacao"
    if _RE_FAIXA.match(celula):
        return "remuneracao"
    if _RE_COMPETENCIA.match(celula) or celula.lower().endswith(" a"):
        return "competencia"
    return "valor"


def extrai_18_3(doc):
    grupos: list[dict] = []
    for pagina in (382, 383, 384):
        for linha in matriz(doc, pagina, 0)[2:]:  # duas linhas de cabeçalho
            campos = {"competencia": [], "remuneracao": [], "valor": [], "fundamentacao": []}
            for celula in (c for c in linha if c):
                campos[_classifica_18_3(celula)].append(celula)
            if not any(campos.values()):
                continue
            if campos["fundamentacao"]:
                grupos.append({"pagina_pdf": pagina, "competencia": [], "remuneracao": [],
                               "valor": [], "fundamentacao": campos["fundamentacao"][0]})
            if not grupos:
                raise AssertionError(f"p{pagina}: linha órfã antes do primeiro grupo: {linha}")
            for chave in ("competencia", "remuneracao", "valor"):
                grupos[-1][chave].extend(campos[chave])

    saida, desalinhados = [], 0
    for ordem, g in enumerate(grupos, start=1):
        faixas = g["remuneracao"] or [""] * len(g["valor"])
        if len(faixas) != len(g["valor"]):
            desalinhados += 1
        for i in range(max(len(faixas), len(g["valor"]))):
            saida.append({
                "pagina_pdf": g["pagina_pdf"],
                "item": "18.3",
                "grupo": ordem,
                "competencia": limpa(" ".join(g["competencia"])),
                "remuneracao": faixas[i] if i < len(faixas) else "",
                "valor_salario_familia": g["valor"][i] if i < len(g["valor"]) else "",
                "fundamentacao_legal": g["fundamentacao"],
                "observacao": "" if len(faixas) == len(g["valor"])
                              else "faixas e valores em quantidade diferente no original",
            })

    destino = grava_csv(
        "serie-18.3-salario-familia.csv",
        ["pagina_pdf", "item", "grupo", "competencia", "remuneracao",
         "valor_salario_familia", "fundamentacao_legal", "observacao"],
        saida,
        notas=("# 'extinto' no valor é do original: acima do teto não há direito à cota.",
               "# Erros de digitação do original foram preservados (ver relatório)."),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} linhas em {len(grupos)} vigências"
            + (f", {desalinhados} com desalinhamento faixa/valor" if desalinhados else "")]


# --------------------------------------------------------------------------
# 18.4 / 18.5 / 18.6 — imposto de renda  (categoria B: faixas por vigência)
# --------------------------------------------------------------------------

def _faixas_ir(linhas, pagina, item, vigencia):
    """Converte (base de cálculo, alíquota, parcela a deduzir) em linhas de faixa."""
    saida, dependente = [], ""
    for linha in linhas:
        base = linha[0]
        if not base:
            continue
        chave = sem_acento(base)
        if chave.startswith("base de calculo") or chave.startswith("valor do plr"):
            continue
        if chave.startswith("dependente"):
            dependente = base
            continue
        if chave.startswith("tabela imposto"):
            continue
        saida.append({
            "pagina_pdf": pagina,
            "item": item,
            "vigencia_original": vigencia,
            "ordem": len(saida) + 1,
            "base_calculo": base,
            "aliquota_pct": linha[1] if len(linha) > 1 else "",
            "parcela_deduzir": linha[2] if len(linha) > 2 else "",
            "deducao_por_dependente": "",
        })
    if dependente and saida:
        for linha in saida:
            linha["deducao_por_dependente"] = dependente
    return saida


_COLS_IR = ["pagina_pdf", "item", "vigencia_original", "ordem", "base_calculo",
            "aliquota_pct", "parcela_deduzir", "deducao_por_dependente"]


def extrai_18_4(doc):
    saida = []
    for pagina in (385, 386):
        for i in range(quantas_tabelas(doc, pagina)):
            linhas = matriz(doc, pagina, i)
            vigencia = linhas[0][0]
            if not sem_acento(vigencia).startswith("tabela imposto"):
                raise AssertionError(f"p{pagina} t{i}: título inesperado {vigencia!r}")
            saida += _faixas_ir(linhas, pagina, "18.4", vigencia)
    destino = grava_csv(
        "serie-18.4-irrf-tabela-progressiva-mensal.csv", _COLS_IR, saida,
        notas=("# A tabela 'abril/11 a dezembro/11' está partida entre p385 e p386;",
               "# as duas partes ficam como vigências homônimas, sem junção."),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} faixas"]


def extrai_18_5(doc):
    saida = []
    for pagina in (387, 388):
        titulos = titulos_no_texto(doc, pagina, "Tabela imposto de renda - RRA")
        n = quantas_tabelas(doc, pagina)
        if len(titulos) != n:
            raise AssertionError(f"p{pagina}: {n} tabelas e {len(titulos)} títulos")
        for i in range(n):
            saida += _faixas_ir(matriz(doc, pagina, i), pagina, "18.5", titulos[i])
    destino = grava_csv(
        "serie-18.5-irrf-rra.csv", _COLS_IR, saida,
        notas=("# NM = número de meses a que se refere o pagamento acumulado",
               "# (legenda do original, p388). Os limites e a parcela a deduzir são",
               "# multiplicados por NM — o multiplicador é variável, não fixo em 12."),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} faixas"]


def extrai_18_6(doc):
    titulos = titulos_no_texto(doc, 389, "Tabela imposto de renda PLR")
    n = quantas_tabelas(doc, 389)
    if len(titulos) != n:
        raise AssertionError(f"p389: {n} tabelas e {len(titulos)} títulos")
    saida = []
    for i in range(n):
        saida += _faixas_ir(matriz(doc, 389, i), 389, "18.6", titulos[i])
    destino = grava_csv("serie-18.6-irrf-plr.csv", _COLS_IR, saida)
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} faixas"]


# --------------------------------------------------------------------------
# 18.7 — contribuição previdenciária  (categoria B)
# --------------------------------------------------------------------------

_RE_TETO = re.compile(r"(?i)^teto\s*m[áa]ximo\s*:?\s*([\d.,]+)\s*(.*)$")
# Os rótulos das colunas às vezes caem dentro da célula de vigência, e a ordem das
# palavras vem embaralhada pela extração. Removem-se as duas frases onde estiverem;
# "em URV" / "em Real" fica, porque é a unidade do quadro, não rótulo de coluna.
_RE_ROTULO_COLUNA = re.compile(
    r"(?i)sal[áa]rio de contribui[çc][ãa]o|al[íi]quota\s*\(\s*%\s*\)"
)


def _matriz_aliquotas(linhas, pagina, rotulo):
    """Shape antigo (jan/82 a dez/91): competência nas linhas, alíquota nas colunas."""
    aliquotas = [c for c in linhas[0] if c.endswith("%")]
    saida = []
    for linha in linhas[2:]:
        comp = linha[0]
        if not comp:
            continue
        valores = linha[1:]
        # Cada alíquota ocupa um par (De, Até), menos a primeira, que só tem Até.
        i, ordem = 0, 0
        for aliquota in aliquotas:
            largura = 1 if ordem == 0 else 2
            bloco = valores[i:i + largura]
            i += largura
            if not any(bloco):
                continue
            de, ate = ("", bloco[0]) if largura == 1 else (bloco[0], bloco[1] if len(bloco) > 1 else "")
            saida.append({
                "pagina_pdf": pagina, "item": "18.7", "quadro": rotulo,
                "competencia": comp, "aliquota_pct": aliquota.rstrip("%"),
                "limite_de": de, "limite_ate": ate,
            })
            ordem += 1
    return saida


def extrai_18_7(doc):
    matrizes = []
    matrizes += _matriz_aliquotas(matriz(doc, 390, 0), 390, "jan/82 a mai/89")
    matrizes += _matriz_aliquotas(matriz(doc, 391, 0), 391, "jul/89 a ago/89")
    matrizes += _matriz_aliquotas(matriz(doc, 391, 1), 391, "set/89 a dez/91")

    faixas = []
    for pagina in range(391, 400):
        primeira = 2 if pagina == 391 else 0
        for i in range(primeira, quantas_tabelas(doc, pagina)):
            linhas = matriz(doc, pagina, i, colapsa=False)
            largura = len(linhas[0])
            # O quadro é uma grade de sub-tabelas lado a lado, de duas colunas cada.
            for base in range(0, largura, 2):
                atual, vigencia = None, ""
                for linha in linhas:
                    esquerda = uma_linha(linha[base] or "")
                    direita = uma_linha(linha[base + 1] or "") if base + 1 < largura else ""
                    if not esquerda:
                        continue  # só rótulo de coluna solto na direita

                    # Em p392 o original funde numa única célula o teto do quadro
                    # anterior, a vigência do seguinte e o rótulo das colunas.
                    m = _RE_TETO.match(esquerda)
                    if m:
                        for f in faixas:
                            if f["_grupo"] is atual:
                                f["teto_maximo"] = m.group(1)
                        esquerda = limpa(m.group(2))
                        if not esquerda:
                            continue
                    esquerda = limpa(_RE_ROTULO_COLUNA.sub("", esquerda))
                    if not esquerda:
                        continue
                    if not re.search(r"\d", esquerda):
                        # Resto do rótulo de coluna, como "em Real" ou "em URV":
                        # é a unidade do quadro. Complementa a vigência corrente,
                        # não abre uma nova.
                        if atual is not None and not vigencia.endswith(esquerda):
                            vigencia = limpa(f"{vigencia} {esquerda}")
                            for f in faixas:
                                if f["_grupo"] is atual:
                                    f["vigencia_original"] = vigencia
                        continue

                    # "De 22/01/97 a abr/97" é vigência, "De 287,28 até 478,78" é faixa.
                    # O que separa os dois é a alíquota na coluna da direita: o
                    # cabeçalho de vigência ocupa as duas colunas e deixa a direita vazia.
                    if not (direita and _RE_FAIXA.match(esquerda)):
                        atual = object()
                        vigencia = esquerda
                        continue
                    if atual is None:
                        raise AssertionError(f"p{pagina} t{i}: faixa sem vigência: {esquerda!r}")
                    faixas.append({
                        "_grupo": atual, "pagina_pdf": pagina, "item": "18.7",
                        "vigencia_original": vigencia, "ordem": 0,
                        "salario_contribuicao": esquerda, "aliquota_pct": direita,
                        "teto_maximo": "",
                    })
    por_grupo: dict[int, int] = {}
    for f in faixas:
        chave = id(f.pop("_grupo"))
        por_grupo[chave] = por_grupo.get(chave, 0) + 1
        f["ordem"] = por_grupo[chave]

    a = grava_csv(
        "serie-18.7-contribuicao-matriz-1982-1991.csv",
        ["pagina_pdf", "item", "quadro", "competencia", "aliquota_pct", "limite_de", "limite_ate"],
        matrizes,
    )
    b = grava_csv(
        "serie-18.7-contribuicao-faixas.csv",
        ["pagina_pdf", "item", "vigencia_original", "ordem",
         "salario_contribuicao", "aliquota_pct", "teto_maximo"],
        faixas,
        notas=("# p398 traz dois quadros para jan/10: o da Portaria 350/09 (revogada,",
               "# usado nos cálculos de jan a jun/10) e o da Portaria 333/10. Os dois",
               "# constam do original e ficam ambos aqui — sobreposição real, não erro."),
    )
    return [
        f"{a.relative_to(RAIZ)}: {len(matrizes)} pares competência×alíquota",
        f"{b.relative_to(RAIZ)}: {len(faixas)} faixas",
    ]


# --------------------------------------------------------------------------
# 18.8.1 — grau de risco até 31/05/2007  (categoria B: relação CNAE → grau)
# --------------------------------------------------------------------------

P_1881 = list(range(400, 418))
# O código vem com espaço espúrio em pelo menos um caso ("74 .13-6"); o padrão
# tolera, e a forma exata do original fica gravada.
_RE_ATIVIDADE = re.compile(r"(\d{2}\s?\.\s?\d{2}\s?-\s?\d)\s+(.*?)\.{4,}\s*(\d)\b")
_RE_LEADER = re.compile(r"\.{4,}\s*\d\b")


def _texto_continuo(doc, paginas):
    """Texto das páginas concatenado, com um mapa posição→página.

    Necessário porque entradas da relação de atividades atravessam a quebra de
    página: a descrição fica numa página e o grau de risco na seguinte.
    """
    pedacos, marcos, total = [], [], 0
    for pagina in paginas:
        bruto = re.sub(r"\s+", " ", texto(doc, pagina))
        pedacos.append(bruto)
        marcos.append((total, pagina))
        total += len(bruto) + 1
    return " ".join(pedacos), marcos


def _pagina_de(marcos, posicao: int) -> int:
    pagina = marcos[0][1]
    for inicio, p in marcos:
        if posicao >= inicio:
            pagina = p
        else:
            break
    return pagina


def extrai_18_8_1(doc):
    corpo, marcos = _texto_continuo(doc, P_1881)
    achados = list(_RE_ATIVIDADE.finditer(corpo))
    leaders = len(_RE_LEADER.findall(corpo))

    saida = []
    for m in achados:
        codigo_bruto = m.group(1)
        codigo = re.sub(r"\s+", "", codigo_bruto)
        saida.append({
            "pagina_pdf": _pagina_de(marcos, m.start()),
            "item": "18.8.1",
            "codigo_cnae": codigo,
            "codigo_no_original": codigo_bruto if codigo != codigo_bruto else "",
            "descricao_atividade": limpa(m.group(2)),
            "grau_risco": m.group(3),
            "aliquota_pct": {"1": "1,00", "2": "2,00", "3": "3,00"}.get(m.group(3), ""),
        })

    destino = grava_csv(
        "serie-18.8.1-grau-risco-cnae-ate-2007-05.csv",
        ["pagina_pdf", "item", "codigo_cnae", "codigo_no_original",
         "descricao_atividade", "grau_risco", "aliquota_pct"],
        saida,
        notas=("# RPS (Dec. 3048/99), Anexo V, vigente até 31/05/2007. Códigos CNAE 1.0.",
               "# grau 1 = risco leve (1%), 2 = médio (2%), 3 = grave (3%) — do próprio",
               "# cabeçalho do original, p400. Os títulos de divisão e grupo (sem grau)",
               "# não entram: a linha de dado é a que tem grau de risco."),
    )
    aviso = ""
    if leaders != len(achados):
        aviso = f" [{leaders} marcadores de grau no texto contra {len(achados)} entradas]"
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} atividades{aviso}"]


# --------------------------------------------------------------------------
# 18.8.2 / Anexo I — grau de risco a partir de 01/06/2007  (categoria B)
# --------------------------------------------------------------------------

_RE_CNAE2 = re.compile(r"^\d{4}-\d/\d{2}$")


def _linhas_anexo_i(doc, paginas, rotulo):
    saida, descartadas = [], 0
    for pagina in paginas:
        for i in range(quantas_tabelas(doc, pagina)):
            for linha in matriz(doc, pagina, i, colapsa=False):
                celulas = [uma_linha(c or "") for c in linha]
                if not celulas or not _RE_CNAE2.match(celulas[0]):
                    descartadas += 1
                    continue
                if len(celulas) < 5:
                    raise AssertionError(f"p{pagina}: linha com {len(celulas)} colunas: {celulas}")
                saida.append({
                    "pagina_pdf": pagina,
                    "item": "18.8.2",
                    "tabela": rotulo,
                    "codigo_cnae": celulas[0],
                    "gilrat_fg_ate_2009_12": celulas[1],
                    "gilrat_fg_desde_2010_01": celulas[2],
                    "fpas": celulas[3],
                    "descricao_atividade": celulas[4],
                })
    return saida, descartadas


def extrai_18_8_2(doc):
    t1, d1 = _linhas_anexo_i(doc, range(418, 448), "ANEXO I - TABELA 1")
    t2, d2 = _linhas_anexo_i(doc, [448], "ANEXO I - TABELA 2")
    # p449 traz o fim da Tabela 2 e, logo abaixo, a tabela de alíquotas por FPAS.
    t2b, _ = _linhas_anexo_i(doc, [], "")
    for i in range(quantas_tabelas(doc, 449)):
        linhas = matriz(doc, 449, i, colapsa=False)
        if any(_RE_CNAE2.match(uma_linha(l[0] or "")) for l in linhas):
            parte, _ = [], 0
            for linha in linhas:
                celulas = [uma_linha(c or "") for c in linha]
                if celulas and _RE_CNAE2.match(celulas[0]):
                    parte.append({
                        "pagina_pdf": 449, "item": "18.8.2", "tabela": "ANEXO I - TABELA 2",
                        "codigo_cnae": celulas[0], "gilrat_fg_ate_2009_12": celulas[1],
                        "gilrat_fg_desde_2010_01": celulas[2], "fpas": celulas[3],
                        "descricao_atividade": celulas[4],
                    })
            t2b += parte
            indice_fpas = None
        else:
            indice_fpas = i

    fpas = []
    for i in range(quantas_tabelas(doc, 449)):
        linhas = matriz(doc, 449, i, colapsa=False)
        if any(_RE_CNAE2.match(uma_linha(l[0] or "")) for l in linhas):
            continue
        for linha in linhas:
            celulas = [uma_linha(c or "") for c in linha]
            codigo = celulas[0] if celulas else ""
            if not codigo or sem_acento(codigo).startswith(("codigo", "c digo")):
                continue
            fpas.append({
                "pagina_pdf": 449, "item": "18.8.2-anexo-fpas",
                "codigo_fpas": codigo,
                "aliquota_previdencia_social_pct": celulas[1] if len(celulas) > 1 else "",
                "aliquota_gilrat": celulas[2] if len(celulas) > 2 else "",
            })

    a = grava_csv(
        "serie-18.8.2-grau-risco-cnae-desde-2007-06.csv",
        ["pagina_pdf", "item", "tabela", "codigo_cnae", "gilrat_fg_ate_2009_12",
         "gilrat_fg_desde_2010_01", "fpas", "descricao_atividade"],
        t1 + t2 + t2b,
        notas=("# Anexo I da IN/RFB 1027/10. Códigos CNAE 2.0 — codificação distinta da",
               "# usada em 18.8.1, que é CNAE 1.0. As duas tabelas NÃO são versões de um",
               "# mesmo arquivo: são normas sucessivas com chave diferente. Ver o JSON",
               "# semântico trt3-18.8-grau-de-risco-estrutura.json.",
               "# A coluna GILRAT está dividida por momento do fato gerador (Dec. 6.957/09)."),
    )
    b = grava_csv(
        "serie-18.8.2-aliquotas-por-fpas.csv",
        ["pagina_pdf", "item", "codigo_fpas", "aliquota_previdencia_social_pct", "aliquota_gilrat"],
        fpas,
        notas=("# Anexo I da IN/RFB 1238/2012, impresso ao final da p449 sem numeração",
               "# 18.x própria. Fora do escopo declarado do bloco — ver relatório."),
    )
    return [
        f"{a.relative_to(RAIZ)}: {len(t1)} (tabela 1) + {len(t2) + len(t2b)} (tabela 2)"
        f"; {d1 + d2} linhas sem código CNAE descartadas",
        f"{b.relative_to(RAIZ)}: {len(fpas)} códigos FPAS",
    ]


# --------------------------------------------------------------------------
# 18.9 — seguro-desemprego  (categoria B)
# --------------------------------------------------------------------------

_RE_VIGENCIA_SD = re.compile(r"(?i)^[a-zç]{3}/\d{2}\s+a\s+[a-zç]{3}/\d{2}\s*\(SM")


def extrai_18_9(doc):
    saida, pendentes = [], []
    for pagina in (450, 451, 452):
        titulos = [l for l in (limpa(x) for x in texto(doc, pagina).split("\n"))
                   if _RE_VIGENCIA_SD.match(l)]
        tabelas_pg = quantas_tabelas(doc, pagina)
        # p452 abre com a continuação da última vigência da p451.
        fila = pendentes + titulos
        if len(fila) != tabelas_pg:
            raise AssertionError(f"p{pagina}: {tabelas_pg} tabelas e {len(fila)} vigências")
        pendentes = []
        for i in range(tabelas_pg):
            vigencia = fila[i]
            for linha in matriz(doc, pagina, i)[1:]:
                if not linha[0]:
                    continue
                saida.append({
                    "pagina_pdf": pagina, "item": "18.9",
                    "vigencia_original": vigencia,
                    "ordem": sum(1 for r in saida if r["vigencia_original"] == vigencia) + 1,
                    "faixa_salario_medio": linha[0],
                    "valor_da_parcela": linha[1] if len(linha) > 1 else "",
                })
        if pagina == 451:
            pendentes = [titulos[-1]] if len(titulos) < tabelas_pg + 1 else []
    destino = grava_csv(
        "serie-18.9-seguro-desemprego.csv",
        ["pagina_pdf", "item", "vigencia_original", "ordem",
         "faixa_salario_medio", "valor_da_parcela"],
        saida,
        notas=("# 'Parcela mínima equivalente a um salário mínimo' é regra de piso do",
               "# original, impressa fora da moldura da tabela — ver o relatório."),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} faixas"]


# --------------------------------------------------------------------------
# 18.10 / 18.11 / 18.12 — URV, BTN e Ufir  (categoria B)
# --------------------------------------------------------------------------

def _matriz_por_mes(doc, pagina, indice, item, rotulo_linha):
    linhas = matriz(doc, pagina, indice)
    cabecalho = next(l for l in linhas if sem_acento(l[0]) == sem_acento(rotulo_linha))
    colunas = cabecalho[1:]
    saida = []
    for linha in linhas[linhas.index(cabecalho) + 1:]:
        chave = linha[0]
        if not chave:
            continue
        for coluna, valor in zip(colunas, linha[1:]):
            if not valor or not coluna or sem_acento(coluna) == sem_acento(rotulo_linha):
                continue
            saida.append({
                "pagina_pdf": pagina, "item": item,
                "serie": coluna, "chave": chave, "valor": valor,
            })
    return saida


_COLS_MATRIZ = ["pagina_pdf", "item", "serie", "chave", "valor"]


def _matriz_intercalada(doc, pagina, indice, item, rotulo_linha):
    """Como `_matriz_por_mes`, para tabelas cujas linhas alternam de coluna.

    Na tabela da URV as linhas pares e ímpares são impressas com um deslocamento
    de uma coluna. Compactar as células vazias desalinharia os meses sem valor
    (fevereiro não tem dia 30); o deslocamento é tratado como passo fixo.
    """
    linhas = matriz(doc, pagina, indice, colapsa=False)
    bruta_cabecalho = next(l for l in linhas if uma_linha(l[0] or "") == rotulo_linha)
    cabecalho = [uma_linha(c or "") for c in bruta_cabecalho]
    cheias = [i for i, c in enumerate(cabecalho) if c]
    passo = (cheias[1] - cheias[0]) if len(cheias) > 1 else 1
    colunas = cabecalho[cheias[0]::passo]
    saida = []
    for bruta in linhas[linhas.index(bruta_cabecalho) + 1:]:
        celulas = [uma_linha(c or "") for c in bruta]
        if not any(celulas):
            continue
        # O deslocamento sai de onde caem os valores, não de onde cai o rótulo da
        # linha: numa das linhas da p454 o dia está numa faixa e os valores noutra.
        deslocamento = max(
            range(passo), key=lambda o: sum(1 for c in celulas[o::passo] if c)
        )
        valores = celulas[deslocamento::passo]
        chave = next(c for c in celulas if c)
        for coluna, valor in zip(colunas[1:], valores[1:]):
            if not valor or not coluna or coluna == rotulo_linha:
                continue
            saida.append({"pagina_pdf": pagina, "item": item,
                          "serie": coluna, "chave": chave, "valor": valor})
    return saida


def extrai_18_10(doc):
    saida = _matriz_intercalada(doc, 453, 0, "18.10", "DIA") + \
            _matriz_intercalada(doc, 454, 0, "18.10", "DIA")
    destino = grava_csv(
        "serie-18.10-urv.csv", _COLS_MATRIZ, saida,
        notas=("# 'serie' = mês, 'chave' = dia do mês, 'valor' = URV em CR$ naquele dia.",
               "# O método de conversão NÃO consta deste bloco — ver relatório e",
               "# tabelas-normativas/trt3-18.10-urv-conversao.json."),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} cotações diárias"]


def extrai_18_11(doc):
    saida = _matriz_por_mes(doc, 455, 0, "18.11", "Mês/Ano")
    for r in saida:
        r["serie"] = f"BTN {r['serie']}"
    avulsos = []
    for linha in texto(doc, 455).split("\n"):
        alvo = limpa(linha)
        m = re.match(r"(?i)^[úu]ltimo valor (OTN|MVR) em (\S+)\s+([\d.,]+)$", alvo)
        if m:
            avulsos.append({"pagina_pdf": 455, "item": "18.11", "serie": m.group(1),
                            "chave": m.group(2), "valor": m.group(3)})
    destino = grava_csv(
        "serie-18.11-otn-btn-mvr.csv", _COLS_MATRIZ, saida + avulsos,
        notas=("# BTN: 'serie' = ano, 'chave' = mês. OTN e MVR: só o último valor consta",
               "# do original. '-' é do original: mês sem valor publicado.",
               "# Indexadores nominais — ver invariante R3 em 00-base-normativa.md."),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} valores BTN + {len(avulsos)} avulsos"]


def extrai_18_12(doc):
    # A moldura tem duas linhas de topo: o título "UFIR" e, abaixo, os anos com a
    # primeira célula vazia. O cabeçalho útil é o segundo.
    saida = _matriz_por_mes(doc, 455, 1, "18.12", "")
    notas = [limpa(l) for l in texto(doc, 455).split("\n")
             if limpa(l).startswith(("*", "UFIR extinta", ". Fatos", "Para a reconvers"))]
    destino = grava_csv(
        "serie-18.12-ufir.csv", _COLS_MATRIZ, saida,
        notas=("# 'serie' = ano, 'chave' = mês.",
               *[f"# {n}" for n in notas]),
    )
    return [f"{destino.relative_to(RAIZ)}: {len(saida)} valores, {len(notas)} notas do original"]


# --------------------------------------------------------------------------
# 18.13 — RSR sobre dias úteis, quatro variantes  (A: critério; B: contagens)
# --------------------------------------------------------------------------

P_1813 = {456: None, 457: None, 458: None, 459: None}


def _rsr_de(doc, pagina):
    linhas = matriz(doc, pagina, 0)
    criterio = linhas[0][0]
    if not sem_acento(criterio).startswith("tabela de rsr"):
        raise AssertionError(f"p{pagina}: título inesperado {criterio!r}")
    saida = []
    for linha in linhas[2:]:
        for base in range(0, len(linha), 4):
            bloco = linha[base:base + 4]
            if len(bloco) < 4 or not bloco[0]:
                continue
            saida.append({
                "pagina_pdf": pagina, "item": "18.13", "criterio": criterio,
                "competencia": bloco[0], "rsr": bloco[1],
                "dias_uteis": bloco[2], "percentual": bloco[3],
            })
    return criterio, saida


def extrai_18_13(doc):
    saida, criterios = [], []
    for pagina in P_1813:
        criterio, linhas = _rsr_de(doc, pagina)
        criterios.append({"pagina_pdf": pagina, "criterio": criterio, "linhas": len(linhas)})
        saida += linhas

    destino = grava_csv(
        "serie-18.13-rsr-contagens.csv",
        ["pagina_pdf", "item", "criterio", "competencia", "rsr", "dias_uteis", "percentual"],
        saida,
        notas=("# Quatro variantes, uma por página. O critério de contagem é o título da",
               "# tabela e está isolado em tabelas-normativas/trt3-18.13-rsr-criterios.json.",
               "# As contagens dependem do calendário e do rol de feriados — série."),
    )

    semantica = {
        "id": "trab.rsr.criterios-de-contagem",
        "categoria": "A-semantica",
        "titulo": "RSR sobre dias úteis — critérios de contagem",
        "jurisdicao": "justica-do-trabalho",
        "componente": "repouso-semanal-remunerado",
        "fonte": _fonte("18.13", sorted(P_1813)),
        "o_que_muda_entre_as_variantes": (
            "O que varia é o conjunto de dias contados como repouso e, por "
            "consequência, o divisor de dias úteis. O percentual é RSR ÷ dias úteis."
        ),
        "variantes": [
            {
                "pagina_pdf": c["pagina_pdf"],
                "criterio": c["criterio"],
                "competencias_tabeladas": c["linhas"],
                "serie": "docs/calculo/extracao/trabalhista/serie-18.13-rsr-contagens.csv",
            }
            for c in criterios
        ],
        "armadilha_registrada": (
            "OJ 394 da SDI-I: o reflexo de horas extras no RSR não repercute em "
            "férias, 13º, aviso prévio e FGTS. Regra de propagação, não de contagem; "
            "não está neste bloco e precisa vir do capítulo de verbas."
        ),
        "observacao": (
            "O original não declara qual variante é a default nem em que hipótese "
            "cada uma se aplica. A escolha depende da norma coletiva e da "
            "jornada — não foi inferida aqui."
        ),
    }
    caminho = grava_json("trt3-18.13-rsr-criterios.json", semantica)
    return [
        f"{destino.relative_to(RAIZ)}: {len(saida)} competências em 4 variantes",
        f"{caminho.relative_to(RAIZ)}: 4 critérios",
    ]


# --------------------------------------------------------------------------
# 18.14 — calendários 2007 a 2020  (categoria B)
# --------------------------------------------------------------------------

P_1814 = list(range(460, 467))
_MESES = ("JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
          "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO")
_DIAS_SEMANA = ("D", "S", "T", "Q", "Q", "S", "S")
_NOME_DIA = ("domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado")


def extrai_18_14(doc):
    """Os calendários não têm moldura: a coluna de cada dia sai da posição x.

    Cada mês ocupa sete colunas. O cabeçalho `D S T Q Q S S` fixa as sete faixas;
    cada número abaixo pertence à faixa mais próxima em x e ao mês cujo bloco
    de sete faixas o contém.
    """
    saida, avisos = [], []
    for pagina in P_1814:
        palavras = doc[pagina - 1].get_text("words")
        anos = sorted(
            ((p[1], p[4]) for p in palavras if re.fullmatch(r"20[0-2]\d", p[4])),
            key=lambda t: t[0],
        )
        cabecalhos = sorted(
            (p for p in palavras if p[4] in ("D", "S", "T", "Q")),
            key=lambda p: (round(p[1], 1), p[0]),
        )
        # agrupa cabeçalhos por linha (y) e, dentro da linha, em blocos de sete
        linhas_cab: dict[float, list] = {}
        for p in cabecalhos:
            linhas_cab.setdefault(round(p[1], 0), []).append(p)

        titulos = [p for p in palavras if p[4].upper().rstrip(",") in _MESES]
        blocos = []
        for y, grupo in sorted(linhas_cab.items()):
            grupo.sort(key=lambda p: p[0])
            if len(grupo) % 7:
                avisos.append(f"p{pagina}: linha de cabeçalho com {len(grupo)} colunas em y={y}")
                continue
            for k in range(0, len(grupo), 7):
                sete = grupo[k:k + 7]
                if [p[4] for p in sete] != list(_DIAS_SEMANA):
                    avisos.append(f"p{pagina}: sequência inesperada {[p[4] for p in sete]}")
                    continue
                mes = min(
                    (t for t in titulos if abs(t[1] - y) < 40 and sete[0][0] - 12 <= t[0] <= sete[-1][2] + 12),
                    key=lambda t: abs(t[0] - sete[0][0]),
                    default=None,
                )
                ano = next((a for yy, a in reversed(anos) if yy < y - 5), None)
                blocos.append({"y": y, "mes": mes[4].upper() if mes else "",
                               "ano": ano, "colunas": sete,
                               "bruto0": sete[0][0], "bruto1": sete[-1][2]})

        # As faixas de x dos quatro meses de uma linha se tocam. Sem fronteira
        # explícita, a coluna de segunda-feira de um mês cai também na faixa do
        # mês anterior e some na deduplicação. A fronteira fica no meio do vão.
        for y in {b["y"] for b in blocos}:
            fila = sorted((b for b in blocos if b["y"] == y), key=lambda b: b["bruto0"])
            for k, b in enumerate(fila):
                folga = (b["bruto1"] - b["bruto0"]) / 12
                esquerda = folga if k == 0 else min(folga, (b["bruto0"] - fila[k - 1]["bruto1"]) / 2)
                direita = folga if k == len(fila) - 1 else min(folga, (fila[k + 1]["bruto0"] - b["bruto1"]) / 2)
                b["x0"] = b["bruto0"] - esquerda
                b["x1"] = b["bruto1"] + direita

        blocos.sort(key=lambda b: (b["y"], b["x0"]))
        # Cada número vai para o bloco cujo cabeçalho é o mais próximo acima dele,
        # dentro da faixa de x do bloco. Dividir por limite superior perderia a
        # última semana dos meses de seis semanas, onde as molduras se aproximam.
        for p in palavras:
            if not re.fullmatch(r"\d{1,2}", p[4]):
                continue
            centro = (p[0] + p[2]) / 2
            candidatos = [
                b for b in blocos
                if b["x0"] <= centro <= b["x1"] and 4 < p[1] - b["y"] < 120
            ]
            if not candidatos:
                continue
            # Empate em y acontece entre meses vizinhos, cujas faixas de x se
            # tocam: desempata a coluna mais próxima do número.
            bloco = max(candidatos, key=lambda b: (
                b["y"],
                -min(abs(centro - (c[0] + c[2]) / 2) for c in b["colunas"]),
            ))
            coluna = min(range(7), key=lambda i: abs(
                centro - (bloco["colunas"][i][0] + bloco["colunas"][i][2]) / 2))
            saida.append({
                "pagina_pdf": pagina, "item": "18.14",
                "ano": bloco["ano"], "mes": bloco["mes"],
                "mes_numero": _MESES.index(bloco["mes"]) + 1 if bloco["mes"] in _MESES else "",
                "dia": int(p[4]), "dia_da_semana": _NOME_DIA[coluna],
                "_y": round(p[1], 1), "_x": round(centro, 1),
            })

    vistos, unicos = set(), []
    for r in sorted(saida, key=lambda r: (r["ano"] or 0, r["mes_numero"] or 0, r["dia"])):
        chave = (r["ano"], r["mes_numero"], r["dia"])
        if chave in vistos:
            continue
        vistos.add(chave)
        r.pop("_y"), r.pop("_x")
        unicos.append(r)

    destino = grava_csv(
        "serie-18.14-calendarios.csv",
        ["pagina_pdf", "item", "ano", "mes", "mes_numero", "dia", "dia_da_semana"],
        unicos,
        notas=("# Os calendários do original não têm moldura de tabela: cada dia foi",
               "# atribuído a um mês e a um dia da semana pela posição x/y na página.",
               "# 'dia_da_semana' vem da coluna sob o cabeçalho D S T Q Q S S do original,",
               "# não de cálculo de calendário. Divergência é do original — ver relatório."),
    )
    anos = sorted({r["ano"] for r in unicos if r["ano"]})
    resumo = f"{destino.relative_to(RAIZ)}: {len(unicos)} dias, anos {anos[0]}–{anos[-1]}" if anos else str(destino)
    return [resumo] + [f"aviso: {a}" for a in avisos[:5]]


# --------------------------------------------------------------------------
# 18.15 — tabela única, tabela prática e juros Selic acumulados  (categoria B)
# --------------------------------------------------------------------------

def extrai_18_15(doc):
    unica = _matriz_por_mes(doc, 467, 0, "18.15", "")
    # A p468 tem dois quadros distintos, não repetidos: a taxa Selic mensal e a
    # Selic acumulada de cada competência até a vigência da tabela (maio/16).
    selic = _matriz_por_mes(doc, 468, 0, "18.15", "Mês/Ano")
    for r in selic:
        r["quadro"] = "taxa-selic-mensal"
    acumulada = _matriz_por_mes(doc, 468, 1, "18.15", "Mês/Ano")
    for r in acumulada:
        r["quadro"] = "selic-acumulada-ate-maio-2016"
    selic += [r for r in acumulada if not sem_acento(r["chave"]).startswith("fonte")]

    pratica = []
    for pagina in (469, 470):
        linhas = matriz(doc, pagina, 0)
        cabecalho = linhas[0]
        for linha in linhas[1:]:
            i = 0
            while i < len(cabecalho):
                rotulo = sem_acento(cabecalho[i])
                if not rotulo.startswith("comp"):
                    i += 1
                    continue
                largura = 1
                while i + largura < len(cabecalho) and not sem_acento(cabecalho[i + largura]).startswith("comp"):
                    largura += 1
                bloco = linha[i:i + largura]
                i += largura
                if not bloco or not bloco[0]:
                    continue
                campos = dict(zip((sem_acento(c) for c in cabecalho[i - largura:i]), bloco))
                pratica.append({
                    "pagina_pdf": pagina, "item": "18.15",
                    "competencia": bloco[0],
                    "coeficiente_ufir": campos.get("coefic. ufir", ""),
                    "juros_pct": campos.get("juros%", ""),
                })
    a = grava_csv(
        "serie-18.15-tabela-unica-trabalhista.csv", _COLS_MATRIZ, unica,
        notas=("# CSJT, Tabela Única para atualização de débitos trabalhistas, até",
               "# 31/05/2016 para 1º/06/2016. Base TR — SUPERADA pela ADC 58 do STF.",
               "# 'serie' = ano, 'chave' = mês, 'valor' = coeficiente de atualização.",
               "# Não use como fonte normativa: ver 00-base-normativa.md, seção 1."),
    )
    b = grava_csv(
        "serie-18.15-juros-selic-acumulados.csv", _COLS_MATRIZ + ["quadro"], selic,
        notas=("# 'serie' = ano, 'chave' = mês. Dois quadros na mesma página:",
               "#   taxa-selic-mensal            — taxa do mês, tributos federais",
               "#   selic-acumulada-ate-maio-2016 — acumulado da competência à vigência",
               "# Zeros em meses posteriores à edição (maio/2016) são do original."),
    )
    c = grava_csv(
        "serie-18.15-tabela-pratica-contribuicoes-em-atraso.csv",
        ["pagina_pdf", "item", "competencia", "coeficiente_ufir", "juros_pct"],
        pratica,
        notas=("# Vigência maio/16. Coeficiente Ufir só nas competências até jun/1994;",
               "# a partir daí o original traz apenas o percentual de juros.",),
    )
    return [
        f"{a.relative_to(RAIZ)}: {len(unica)} coeficientes",
        f"{b.relative_to(RAIZ)}: {len(selic)} taxas mensais",
        f"{c.relative_to(RAIZ)}: {len(pratica)} competências",
    ]


# --------------------------------------------------------------------------
# Semântica derivada das seções de faixas e do grau de risco  (categoria A)
# --------------------------------------------------------------------------

def escreve_semantica(doc):
    ir = {
        "id": "trab.irrf.estrutura-das-tabelas",
        "categoria": "A-semantica",
        "titulo": "IRRF — estrutura das tabelas progressivas e regimes especiais",
        "jurisdicao": "justica-do-trabalho",
        "componente": "desconto-fiscal",
        "fonte": _fonte("18.4 a 18.6", [385, 386, 387, 388, 389]),
        "estrutura_da_faixa": {
            "campos": ["base_calculo", "aliquota_pct", "parcela_deduzir"],
            "descricao": (
                "Tabela progressiva com parcela a deduzir: a alíquota da faixa incide "
                "sobre a base inteira e a parcela a deduzir devolve o excesso das faixas "
                "inferiores. Só é equivalente à progressividade por faixas se a parcela "
                "vier da mesma vigência."
            ),
            "deducao_por_dependente": (
                "Valor por dependente vem impresso no rodapé de cada tabela mensal "
                "(18.4) e está gravado em cada linha da série correspondente."
            ),
            "nao_consta_deste_bloco": (
                "A fórmula de aplicação, o tratamento das deduções (INSS, pensão, "
                "dependentes) e o momento da retenção não estão nas tabelas. Vêm do "
                "capítulo de descontos fiscais, p107-208 — outro bloco."
            ),
        },
        "regimes": [
            {
                "item": "18.4",
                "nome": "Tabela progressiva mensal",
                "base": "rendimento do mês",
                "serie": "docs/calculo/extracao/trabalhista/serie-18.4-irrf-tabela-progressiva-mensal.csv",
            },
            {
                "item": "18.5",
                "nome": "Rendimentos recebidos acumuladamente (RRA)",
                "base": "total acumulado",
                "multiplicador": "NM",
                "definicao_do_multiplicador": (
                    "NM = número de meses a que se refere o pagamento acumulado "
                    "(legenda do original, pagina_pdf 388). Limites de faixa e parcela "
                    "a deduzir são multiplicados por NM."
                ),
                "atencao": (
                    "NM é variável, igual ao número de meses do pagamento. O original "
                    "NÃO fixa doze avos: qualquer implementação que grave 12 como "
                    "constante diverge da fonte."
                ),
                "fundamento_no_original": "IN/RFB 1500/14 (rodapé da pagina_pdf 388)",
                "serie": "docs/calculo/extracao/trabalhista/serie-18.5-irrf-rra.csv",
            },
            {
                "item": "18.6",
                "nome": "Participação nos lucros ou resultados (PLR)",
                "base": "valor do PLR anual",
                "tabela_propria": True,
                "atencao": (
                    "Tabela anual e exclusiva: a tributação do PLR é separada da do "
                    "salário, não se soma à base mensal. Primeira faixa com alíquota zero."
                ),
                "serie": "docs/calculo/extracao/trabalhista/serie-18.6-irrf-plr.csv",
            },
        ],
        "observacao": (
            "Manual de 2016. As faixas das três séries param em 2015/2017 e estão "
            "superadas. Só a estrutura entra na skill; os valores têm manutenção "
            "separada (regra 4 de 01-plano-extracao.md)."
        ),
    }

    previdencia = {
        "id": "trab.contribuicao-previdenciaria.estrutura",
        "categoria": "A-semantica",
        "titulo": "Contribuição previdenciária do segurado — estrutura das tabelas",
        "jurisdicao": "justica-do-trabalho",
        "componente": "desconto-previdenciario",
        "fonte": _fonte("18.7", list(range(390, 400))),
        "formatos_encontrados": [
            {
                "quadro": "jan/82 a dez/91",
                "paginas_pdf": [390, 391],
                "forma": "matriz competência × alíquota, com o limite de cada alíquota",
                "serie": "docs/calculo/extracao/trabalhista/serie-18.7-contribuicao-matriz-1982-1991.csv",
            },
            {
                "quadro": "jan/92 em diante",
                "paginas_pdf": list(range(391, 400)),
                "forma": "faixas de salário de contribuição × alíquota, com teto por vigência",
                "serie": "docs/calculo/extracao/trabalhista/serie-18.7-contribuicao-faixas.csv",
            },
        ],
        "estrutura_da_faixa": {
            "campos": ["salario_contribuicao", "aliquota_pct", "teto_maximo"],
            "atencao": (
                "Não há parcela a deduzir: a alíquota da faixa incide sobre o salário "
                "de contribuição inteiro, e o desconto é limitado pelo teto da vigência. "
                "Estrutura diferente da do IRRF (18.4) — não são intercambiáveis."
            ),
        },
        "sobreposicao_registrada": {
            "competencia": "jan/10 a jun/10",
            "descricao": (
                "O original traz dois quadros vigentes para o mesmo período: o da "
                "Portaria Interministerial MPS/MF 350/09, revogada, e o da 333/10. "
                "Mantidos ambos, sem escolha — a seleção depende da data do cálculo."
            ),
            "pagina_pdf": 398,
        },
        "observacao": (
            "As vigências do original são rótulos em português, não intervalos "
            "normalizados. A conversão para competências exige leitura caso a caso "
            "e não foi feita aqui: normalizar seria interpretar."
        ),
    }

    grau_risco = {
        "id": "trab.gilrat.grau-de-risco",
        "categoria": "A-semantica",
        "titulo": "GILRAT/SAT — grau de risco por atividade preponderante",
        "jurisdicao": "justica-do-trabalho",
        "componente": "encargo-previdenciario-patronal",
        "fonte": _fonte("18.8", list(range(400, 450))),
        "regra": {
            "criterio_de_enquadramento": "atividade econômica preponderante da empresa",
            "periodicidade": "mensal (IN/RFB 1027/10, pagina_pdf 418)",
            "graus": [
                {"grau": 1, "risco": "leve", "aliquota_pct": "1,00"},
                {"grau": 2, "risco": "médio", "aliquota_pct": "2,00"},
                {"grau": 3, "risco": "grave", "aliquota_pct": "3,00"},
            ],
            "fundamento": "art. 22, II, da Lei 8.212/1991; RPS (Dec. 3048/99), Anexo V",
        },
        "duas_versoes_normativas": {
            "sao_a_mesma_tabela": False,
            "verificacao": (
                "Confrontadas antes de extrair, como pedido. 18.8.1 usa CNAE 1.0 "
                "(formato NN.NN-N) e dá o grau de risco como dígito 1/2/3. 18.8.2, que "
                "é o Anexo I da IN/RFB 1027/10, usa CNAE 2.0 (formato NNNN-N/NN) e dá "
                "a alíquota GILRAT em percentual, mais o código FPAS. Chave diferente, "
                "colunas diferentes, vigências que não se sobrepõem: são normas "
                "sucessivas, não duas impressões do mesmo arquivo. As duas foram "
                "extraídas, em arquivos separados."
            ),
            "versoes": [
                {
                    "item": "18.8.1",
                    "vigencia": "até 31/05/2007",
                    "codificacao": "CNAE 1.0",
                    "fundamento": "RPS (Dec. 3048/99), Anexo V",
                    "paginas_pdf": [400, 417],
                    "serie": "docs/calculo/extracao/trabalhista/serie-18.8.1-grau-risco-cnae-ate-2007-05.csv",
                },
                {
                    "item": "18.8.2",
                    "vigencia": "a partir de 01/06/2007",
                    "codificacao": "CNAE 2.0",
                    "fundamento": (
                        "RPS, Anexo V, alterado pelo Dec. 6.042/2007 (efeitos de "
                        "01/06/2007) e pelo Dec. 6.957/2009 (efeitos de 01/01/2010); "
                        "Anexo I da IN/RFB 1027/10"
                    ),
                    "paginas_pdf": [418, 449],
                    "serie": "docs/calculo/extracao/trabalhista/serie-18.8.2-grau-risco-cnae-desde-2007-06.csv",
                },
            ],
        },
        "corte_por_fato_gerador": {
            "descricao": (
                "Dentro de 18.8.2 a alíquota GILRAT se divide em duas colunas pelo "
                "momento do fato gerador: até 31/12/2009 e a partir de 01/01/2010. "
                "O marco é o art. 4º do Dec. 6.957/2009."
            ),
            "atencao": (
                "É o fato gerador que manda, não a data do cálculo nem a do ajuizamento. "
                "Confundir os três produz alíquota errada em toda a competência."
            ),
            "pagina_pdf": 448,
        },
        "tabela_2_quando_se_aplica": (
            "Se o código CNAE não for encontrado na Tabela 1, ou se a descrição "
            "atribuída não corresponder ao objeto social, o enquadramento é feito pela "
            "Tabela 2 (IN/RFB 1027/10, pagina_pdf 418)."
        ),
        "substituicao_de_aliquota": (
            "Marca (*) no FPAS: contribuinte sujeito à contribuição substitutiva dos "
            "arts. 22-A e 25 da Lei 8.212/91 ou art. 25 da Lei 8.870/94 tem a alíquota "
            "GILRAT substituída por 0,1% sobre a receita da comercialização da produção "
            "(pagina_pdf 449)."
        ),
        "nao_consta_deste_bloco": (
            "O FAP (Fator Acidentário de Prevenção), que multiplica a alíquota GILRAT "
            "entre 0,5 e 2,0, não aparece em nenhuma tabela deste bloco."
        ),
    }

    urv = {
        "id": "trab.urv.conversao",
        "categoria": "A-semantica",
        "titulo": "URV — o que o bloco de tabelas contém e o que não contém",
        "jurisdicao": "justica-do-trabalho",
        "componente": "conversao-monetaria",
        "fonte": _fonte("18.10", [453, 454]),
        "conteudo_da_tabela": {
            "unidade": "CR$ por URV",
            "granularidade": "diária",
            "abrangencia": "jan/1993 a jun/1994",
            "serie": "docs/calculo/extracao/trabalhista/serie-18.10-urv.csv",
        },
        "metodo_de_conversao": None,
        "lacuna_registrada": (
            "O método de conversão NÃO está neste bloco. As páginas 453 a 455 trazem "
            "apenas o título '18.10 Tabela URV' e as cotações. Sem texto de "
            "procedimento, sem fundamento legal, sem nota de rodapé. Não foi inferido: "
            "o critério (data-base da conversão, arredondamento, tratamento de dia não "
            "útil) precisa vir do capítulo de critérios matemáticos, p9-17."
        ),
        "por_que_importa": (
            "URV é indexador nominal do período de transição para o Real. A invariante "
            "R3 de 00-base-normativa.md trata da defasagem entre nominal e percentual; "
            "aplicar a cotação do dia errado desloca o cálculo."
        ),
    }

    caminhos = [
        grava_json("trt3-18.4-18.6-irrf-estrutura.json", ir),
        grava_json("trt3-18.7-contribuicao-estrutura.json", previdencia),
        grava_json("trt3-18.8-grau-de-risco-estrutura.json", grau_risco),
        grava_json("trt3-18.10-urv-conversao.json", urv),
    ]
    return [str(c.relative_to(RAIZ)) for c in caminhos]


# --------------------------------------------------------------------------
# Registro de seções
# --------------------------------------------------------------------------

SECOES: dict[str, dict] = {}


def registra(chave: str, titulo: str, fn):
    SECOES[chave] = {"titulo": titulo, "fn": fn}


def _roda_18_1(doc) -> list[str]:
    dados = extrai_18_1(doc)
    destino = grava_json("trt3-18.1-incidencia-parcelas.json", dados)
    e = dados["estatisticas"]
    return [
        f"{destino.relative_to(RAIZ)}: {e['parcelas']} parcelas, "
        f"{e['linhas_de_continuacao_reunidas']} continuações reunidas, "
        f"{e['linhas_cabecalho_descartadas']} cabeçalhos descartados"
    ]


registra("18.1", "Incidência de INSS, FGTS e IRRF por parcela (A)", _roda_18_1)
registra("18.2", "Salário mínimo, moedas e paridades (B)", extrai_18_2)
registra("18.3", "Salário-família (B)", extrai_18_3)
registra("18.4", "IRRF — tabela progressiva mensal (B)", extrai_18_4)
registra("18.5", "IRRF — rendimentos recebidos acumuladamente (B)", extrai_18_5)
registra("18.6", "IRRF — participação nos lucros (B)", extrai_18_6)
registra("18.7", "Contribuição previdenciária (B)", extrai_18_7)
registra("18.8.1", "Grau de risco até 31/05/2007 — CNAE 1.0 (B)", extrai_18_8_1)
registra("18.8.2", "Grau de risco desde 01/06/2007 — Anexo I, CNAE 2.0 (B)", extrai_18_8_2)
registra("18.9", "Seguro-desemprego (B)", extrai_18_9)
registra("18.10", "URV (B)", extrai_18_10)
registra("18.11", "OTN, BTN e MVR (B)", extrai_18_11)
registra("18.12", "Ufir (B)", extrai_18_12)
registra("18.13", "RSR sobre dias úteis (A + B)", extrai_18_13)
registra("18.14", "Calendários 2007-2020 (B)", extrai_18_14)
registra("18.15", "Tabela única, prática e Selic acumulada (B)", extrai_18_15)
registra("semantica", "Tabelas normativas derivadas (A)", escreve_semantica)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--listar" in argv:
        for chave, s in SECOES.items():
            print(f"{chave:8} {s['titulo']}")
        return 0
    alvos = [a for a in argv if not a.startswith("-")] or list(SECOES)
    desconhecidas = [a for a in alvos if a not in SECOES]
    if desconhecidas:
        sys.exit(f"seção desconhecida: {', '.join(desconhecidas)} (use --listar)")
    doc = abre()
    for chave in alvos:
        print(f"== {chave} — {SECOES[chave]['titulo']}")
        for linha in SECOES[chave]["fn"](doc):
            print("   " + linha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
