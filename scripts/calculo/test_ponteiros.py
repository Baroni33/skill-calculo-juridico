"""Ponteiros mortos — referência a caminho que não existe.

O bloco 17 achou ponteiros mortos em 14 arquivos, dois deles CRIADOS naquele
mesmo bloco. Foram corrigidos **sem teste**, e o que se corrige sem teste volta.
Este é o teste.

ESCOPO DECLARADO DA VARREDURA (regra: afirmação de ausência exige escopo)
------------------------------------------------------------------------
  árvores: `README.md` da raiz, `docs/`, `skills/`, `scripts/`
  extensões lidas: `.md` e `.json` (`__pycache__` e `.git` fora)
  extensões procuradas: .json .md .py .csv .pdf .txt .yaml .yml
  o que conta como ponteiro:
     1. link markdown `[texto](alvo)` cujo alvo termine em uma das extensões;
     2. em `.md`, vão de código craseado — `` `algo.json` `` — cujo conteúdo
        inteiro seja um nome de arquivo ou caminho;
     3. em `.json`, valor de string que seja um nome de arquivo ou caminho.
  o que NÃO é verificado, e por quê:
     * âncoras (`#secao`) — o alvo é o arquivo, não a seção;
     * URL e `mailto:` — rede, e a regra do bloco é não pesquisar na web;
     * nome de arquivo solto em prosa, fora de crase e fora de link. Este
       repositório escreve caminho entre crases; aceitar prosa nua trazia
       `-detalhe.md` (sufixo abreviado) e `\\.\\d+` (regex) como se fossem
       ponteiros, e **validador com falso positivo é ignorado, e validador
       ignorado é pior que validador ausente** — o argumento da tarefa 4 do
       bloco 17.

COMO SE DISTINGUE NARRATIVA HISTÓRICA DE PONTEIRO MORTO
-------------------------------------------------------
`bloco-16-relatorio.md`, `01-plano-extracao.md` e os relatórios dos blocos 8 e 9
**devem** citar `trt3.hist.*` e `valida_cadeias_cjf.py`: eles DESCREVEM a
renomeação. Um teste que os acuse é um teste ruim.

Três desenhos foram pesados:

  (a) **contexto** — procurar 'era', 'virou', 'renomeado' perto da menção.
      Rejeitado: heurística erra dos dois lados. Deixa passar o ponteiro morto
      escrito em tom de história e acusa a referência viva que por acaso vizinha
      um verbo no passado. Heurística é exatamente o que treina o leitor a
      ignorar o relatório.

  (b) **marca no próprio texto** — um sufixo tipo `<!-- historico -->`.
      Rejeitado: obriga a editar documento narrativo para agradar a um teste, e
      a marca é auto-atribuída — quem escreve o ponteiro morto escreve a marca.

  (c) **LEDGER DECLARADO, E AUTOLIMPANTE.** Escolhido. `EXCECOES` abaixo é
      explícito, aparece no diff, e cada entrada carrega o porquê. A chave é o
      **par (alvo, arquivo)**, não o alvo sozinho: `valida_cadeias_cjf.py` é
      tolerado nos três documentos que narram a renomeação e em nenhum outro —
      se amanhã um arquivo novo o citar como se fosse script vivo, o teste
      dispara.

      O defeito óbvio de um ledger é envelhecer. Curado por
      `TestLedgerNaoEnvelhece.test_toda_excecao_ainda_corresponde_a_uma_mencao_real`:
      entrada cujo par não aparece mais no texto, ou cujo alvo passou a existir,
      **falha**. A exceção não sobrevive ao fato que a justificava.

`test_a_varredura_enxerga_o_repositorio` existe para que um erro de regex não
faça este arquivo passar por vacuidade, achando zero ponteiros e aprovando tudo.

A VÁLVULA DE NOME-BASE, E POR QUE ELA FOI APERTADA NO BLOCO 25
---------------------------------------------------------------
Havia uma válvula: *se o nome-base existe em algum lugar, não é morte, é
imprecisão de caminho relativo*. **Ela tem razão de existir** — este repositório
cita `consolidado/00-numeros.md` de vários diretórios, e acusar isso é ruído que
treina o leitor a ignorar o teste.

**Mas ela foi desenhada contra RENOMEAÇÃO, e o bloco 25 fez MUDANÇA DE
DIRETÓRIO.** 32 `.json` saíram de `docs/calculo/tabelas-normativas/` para
`skills/*/regras/` e 4 validadores saíram de `scripts/calculo/` para
`skills/*/scripts/`. O basename sobreviveu a todos, e **a válvula imunizou todo
ponteiro antigo** — inclusive 8 links markdown clicáveis sob o rótulo *"Fonte de
verdade executável"*. O teste passava.

**O aperto, em `alcancavel_por_nome`:** o nome-base ainda salva, mas só se
**todo diretório citado no alvo for diretório REAL** de algum arquivo com esse
nome. `consolidado/00-numeros.md` continua salvo; `tabelas-normativas/x.json`
não, porque `tabelas-normativas` deixou de ser diretório de `x.json`.

**O CUSTO FOI MEDIDO ANTES DE A DECISÃO SER TOMADA** — a régua do bloco 20.
Com a válvula larga: **728** ponteiros dependiam só dela. Com o aperto:
**18 ponteiros, em 11 arquivos**, deixaram de ser imunizados. Classificados um
a um:

  * **13 eram defeito de verdade** — endereço de artefato que a migração moveu.
    **Corrigidos**, não excepcionados;
  * **5 eram abreviação de nome de skill em prosa** (`liq/SKILL.md`,
    `core/SKILL.md`, `atualizacao/SKILL.md`). São o falso positivo genuíno do
    aperto, e foram **escritos por extenso**: custa menos que uma entrada de
    ledger, e o documento fica melhor;
  * **5 entraram no ledger**, classe `registro datado de bloco` — relatório que
    cita o endereço que o artefato tinha no dia em que foi escrito.

**Custo declarado:** 5 abreviações deixaram de ser escrevíveis; quem quiser
abreviar diretório de skill em prosa terá de tirar as crases ou declarar a
exceção. Foi julgado barato diante de 13 ponteiros mortos que o teste aprovava.
"""

from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

ARVORES = ("docs", "skills", "scripts")
EXTENSOES_LIDAS = (".md", ".json")
_EXT = r"(?:json|md|py|csv|pdf|txt|yaml|yml)"

RE_LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]+)")
RE_CRASE = re.compile(r"`([^`\n]+)`")
RE_STRING = re.compile(r'"([^"\n]*)"')
RE_ALVO = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_./-]*\." + _EXT + r"$")


# --------------------------------------------------------------------------
# Ledger de exceções. Par (alvo, arquivo) — nunca alvo solto.
# --------------------------------------------------------------------------
EXCECOES: list[dict] = [
    # ---- BLOCO 25 — o endereço de ANTES da migração -----------------------
    # A válvula de nome-base foi apertada (ver `alcancavel_por_nome`) e passou
    # a enxergar MUDANÇA DE DIRETÓRIO. O custo foi medido antes de a decisão
    # ser tomada: **18 ponteiros, em 11 arquivos**, deixaram de ser imunizados.
    # Treze eram defeito de verdade — ponteiro para `tabelas-normativas/` ou
    # para `scripts/calculo/valida_*.py`, que já não existem — e **foram
    # corrigidos**. Cinco eram abreviação de nome de skill em prosa
    # (`liq/SKILL.md`, `core/SKILL.md`) e **foram escritos por extenso**, que
    # custa menos que uma entrada de ledger e melhora o documento.
    # Sobram estas cinco: registro DATADO que cita o caminho de então. O
    # caminho velho É o fato registrado, e atualizá-lo apagaria o registro.
    {
        "alvo": "scripts/calculo/valida_parametros.py",
        "classe": "registro datado de bloco",
        "por_que": (
            "Relatório do bloco 5: 'o validador ficou em scripts/calculo/'. "
            "O bloco 25 o promoveu a script de skill — hoje mora em "
            "skills/calculo-trabalhista-liquidacao/scripts/. O relatório "
            "registra onde ele nasceu, e não se atualiza."
        ),
        "arquivos": ["docs/calculo/extracao/bloco-05-relatorio.md"],
    },
    {
        "alvo": "scripts/calculo/valida_regimes.py",
        "classe": "registro datado de bloco",
        "por_que": (
            "Idem, bloco 6. Hoje em skills/calculo-judicial-core/scripts/."
        ),
        "arquivos": ["docs/calculo/extracao/bloco-06-relatorio.md"],
    },
    {
        "alvo": "docs/calculo/tabelas-normativas/cadeias-manifesto.json",
        "classe": "registro datado de bloco",
        "por_que": (
            "Relatório do bloco 18, que CRIOU o manifesto e diz onde o criou. "
            "O bloco 25 o levou para skills/calculo-judicial-atualizacao/"
            "regras/, junto das cadeias que ele inventaria."
        ),
        "arquivos": ["docs/calculo/extracao/bloco-18-relatorio.md"],
    },
    {
        "alvo": "tabelas-normativas/trt3-18.1-incidencia-parcelas.json",
        "classe": "registro datado de bloco",
        "por_que": (
            "Bloco 3: 'a tabela 18.1 do manual — extraída no bloco 1, em "
            "tabelas-normativas/…'. É a frase que diz ONDE o bloco 1 a pôs. "
            "Hoje em skills/calculo-trabalhista-liquidacao/regras/."
        ),
        "arquivos": ["docs/calculo/extracao/trabalhista/bloco-03-verbas.md"],
    },
    {
        "alvo": "tabelas-normativas/indexadores-tipo-catalogo.json",
        "classe": "registro datado de bloco",
        "por_que": (
            "Avaliação da frente B, escrita no bloco 22 sobre o estado de "
            "então. Hoje o catálogo mora em skills/calculo-judicial-"
            "atualizacao/regras/ e tem um dono declarado."
        ),
        "arquivos": ["docs/calculo/aceitacao/frente-b-avaliacao.md"],
    },
    {
        "alvo": "manual_de_calculos_2026.pdf",
        "classe": "fonte externa",
        "por_que": (
            "PDF do corpus. Vive FORA do repositório por decisão declarada em "
            "docs/calculo/fontes.md — é material de terceiro, não artefato "
            "versionado. Citá-lo é proveniência, não navegação."
        ),
        "arquivos": "*",
    },
    {
        "alvo": "manual-de-calculo-trabalhista_2016-1.pdf",
        "classe": "fonte externa",
        "por_que": (
            "PDF do corpus, idem. docs/calculo/fontes.md declara onde vive "
            "e com que emissor e data foi conferido."
        ),
        "arquivos": "*",
    },
    {
        "alvo": "cap10_1.json",
        "classe": "insumo efêmero de extração",
        "por_que": (
            "Recorte intermediário do PDF, consumido por script de extração e "
            "não versionado. A menção é a PROVENIÊNCIA do documento gerado "
            "('gerado por script a partir de …'), não ponteiro para navegar."
        ),
        "arquivos": ["docs/calculo/extracao/trabalhista/bloco-11a-imputacao-detalhe.md"],
    },
    {
        "alvo": "cap10_2b.json",
        "classe": "insumo efêmero de extração",
        "por_que": "Recorte intermediário não versionado, idem cap10_1.json.",
        "arquivos": [
            "docs/calculo/extracao/trabalhista/bloco-13a-descontos-proporcionais-detalhe.md"
        ],
    },
    {
        "alvo": "cap10_3c.json",
        "classe": "insumo efêmero de extração",
        "por_que": "Recorte intermediário não versionado, idem cap10_1.json.",
        "arquivos": ["docs/calculo/extracao/trabalhista/bloco-11b-amortizacao-detalhe.md"],
    },
    {
        "alvo": "cap10_3d.json",
        "classe": "insumo efêmero de extração",
        "por_que": "Recorte intermediário não versionado, idem cap10_1.json.",
        "arquivos": ["docs/calculo/extracao/trabalhista/bloco-11c-vincendos-detalhe.md"],
    },
    {
        "alvo": "cap16.json",
        "classe": "insumo efêmero de extração",
        "por_que": "Recorte intermediário não versionado, idem cap10_1.json.",
        "arquivos": [
            "docs/calculo/extracao/trabalhista/bloco-13a-descontos-proporcionais-detalhe.md"
        ],
    },
    {
        "alvo": "cap8_12_14.json",
        "classe": "insumo efêmero de extração",
        "por_que": "Recorte intermediário não versionado, idem cap10_1.json.",
        "arquivos": [
            "docs/calculo/extracao/trabalhista/bloco-13a-descontos-proporcionais-detalhe.md"
        ],
    },
    {
        "alvo": "cap17.json",
        "classe": "insumo efêmero de extração",
        "por_que": "Recorte intermediário não versionado, idem cap10_1.json.",
        "arquivos": ["docs/calculo/jurisprudencia-indice.md"],
    },
    {
        "alvo": "valida_cadeias_cjf.py",
        "classe": "narrativa histórica",
        "por_que": (
            "Nome ANTIGO de scripts/calculo/valida_cadeias.py. Os três "
            "documentos abaixo narram a fusão do validador — 'à época', 'foi "
            "apagado e virou'. Apagar a menção apagaria o registro da mudança."
        ),
        "arquivos": [
            "docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md",
            "docs/calculo/extracao/justica-federal/bloco-08-relatorio.md",
            "docs/calculo/extracao/trabalhista/bloco-09-relatorio.md",
        ],
    },
    {
        "alvo": "08-ordem-de-calculo.md",
        "classe": "narrativa histórica",
        "por_que": (
            "O próprio 09-ordem-de-calculo.md explica por que NÃO se chama 08: "
            "'o número 08 já estava ocupado'. A menção é a justificativa do "
            "nome do arquivo que a contém."
        ),
        "arquivos": ["docs/calculo/consolidado/09-ordem-de-calculo.md"],
    },
    {
        "alvo": "trabalhista-privado.md",
        "classe": "narrativa histórica",
        "por_que": (
            "Nome que a divisão de `references/` teve ANTES do bloco 16. A "
            "tabela do README é justamente a tabela de-para da reorganização."
        ),
        "arquivos": ["skills/calculo-judicial-atualizacao/references/README.md"],
    },
    {
        "alvo": "trabalhista-fazenda.md",
        "classe": "narrativa histórica",
        "por_que": (
            "Nome anterior ao bloco 16, fundido em trabalhista-nacional.md: "
            "privado e Fazenda são dois ramos da mesma cadeia nacional."
        ),
        "arquivos": ["skills/calculo-judicial-atualizacao/references/README.md"],
    },
    {
        "alvo": "civel-cc-tema1368.md",
        "classe": "narrativa histórica",
        "por_que": (
            "Nome anterior ao bloco 16, renomeado para civel-cc-nacional.md: "
            "o Tema 1368 é um fundamento, não o recorte."
        ),
        "arquivos": ["skills/calculo-judicial-atualizacao/references/README.md"],
    },
    {
        "alvo": "civel-mg-cgj.md",
        "classe": "narrativa histórica",
        "por_que": (
            "Nome anterior ao bloco 16, renomeado para civel-regional-tjmg.md: "
            "o nome passa a declarar alcance, não sigla de órgão."
        ),
        "arquivos": ["skills/calculo-judicial-atualizacao/references/README.md"],
    },
    {
        "alvo": "federal-condenatorias-desapropriacao.md",
        "classe": "narrativa histórica",
        "por_que": (
            "Arquivo único que o bloco 16 CANDIDATOU e não criou — o README "
            "registra a alternativa recusada, com o porquê. Recusa registrada "
            "não é ponteiro morto; é a decisão."
        ),
        "arquivos": ["skills/calculo-judicial-atualizacao/references/README.md"],
    },
    {
        "alvo": "NNN-NNN-assunto.md",
        "classe": "molde de nomenclatura",
        "por_que": (
            "`NNN` é metavariável, não nome: o README declara a CONVENÇÃO de "
            "nomes do diretório, e o molde não aponta para arquivo algum."
        ),
        "arquivos": ["docs/calculo/extracao/trabalhista/README.md"],
    },
    {
        "alvo": "bloco-NN-assunto.md",
        "classe": "molde de nomenclatura",
        "por_que": "Molde do README, `NN` é metavariável. Idem NNN-NNN-assunto.md.",
        "arquivos": ["docs/calculo/extracao/trabalhista/README.md"],
    },
    {
        "alvo": "serie-18.X-assunto.csv",
        "classe": "molde de nomenclatura",
        "por_que": "Molde do README, `X` é metavariável. Idem NNN-NNN-assunto.md.",
        "arquivos": ["docs/calculo/extracao/trabalhista/README.md"],
    },
    {
        "alvo": "bloco-13a-...-detalhe.md",
        "classe": "molde de nomenclatura",
        "por_que": (
            "Reticências no meio do nome: abreviação de "
            "bloco-13a-descontos-proporcionais-detalhe.md em texto corrido."
        ),
        "arquivos": [
            "docs/calculo/consolidado/04-descontos.md",
            "docs/calculo/consolidado/09-ordem-de-calculo.md",
        ],
    },
]


# --------------------------------------------------------------------------
# Varredura
# --------------------------------------------------------------------------

def arquivos_varridos(raiz: Path) -> list[Path]:
    achados: list[Path] = []
    raiz_readme = raiz / "README.md"
    if raiz_readme.exists():
        achados.append(raiz_readme)
    for arvore in ARVORES:
        base = raiz / arvore
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix not in EXTENSOES_LIDAS:
                continue
            if "__pycache__" in p.parts or ".git" in p.parts:
                continue
            achados.append(p)
    return achados


def nomes_do_repositorio(raiz: Path) -> dict[str, list[tuple[str, ...]]]:
    """Nome-base → os diretórios REAIS de cada arquivo com esse nome.

    **Bloco 25 — era um `set` de nomes, e o `set` era cego.** A válvula que
    usava esse conjunto foi desenhada contra **RENOMEAÇÃO de diretório-pai
    inexistente**: o documento cita `consolidado/00-numeros.md` de um diretório
    onde o caminho relativo não bate, o arquivo existe, e acusar isso é ruído.
    Mas o bloco 25 fez **MUDANÇA DE DIRETÓRIO** — `tabelas-normativas/x.json`
    virou `skills/…/regras/x.json` —, e aí o nome-base sobrevive e **imuniza
    todo ponteiro antigo**. Guardar os diretórios reais é o que permite separar
    os dois casos.
    """
    onde: dict[str, list[tuple[str, ...]]] = {}
    for p in raiz.rglob("*"):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        if p.is_file():
            rel = p.relative_to(raiz)
            onde.setdefault(p.name, []).append(rel.parts[:-1])
    return onde


def alcancavel_por_nome(alvo: str, onde: dict[str, list[tuple[str, ...]]]) -> bool:
    """A válvula, **apertada no bloco 25**. Vale quando as duas valem:

      1. **o nome-base existe** em algum lugar do repositório; e
      2. **todo diretório citado no alvo é diretório REAL** de algum arquivo
         com esse nome. Alvo sem diretório nenhum — `` `00-numeros.md` `` —
         passa direto: é menção por nome, e nome nu não promete caminho.

    O item 2 é o aperto. `consolidado/00-numeros.md` passa porque o arquivo
    mora mesmo dentro de um `consolidado/`; `tabelas-normativas/x.json` **não
    passa mais**, porque `tabelas-normativas` deixou de ser diretório de `x.json`.
    **Imprecisão de caminho relativo continua sendo perdoada; movimentação de
    diretório passa a doer.**

    `..` e `.` são descartados antes da comparação: são navegação relativa, não
    afirmação sobre onde o arquivo mora.
    """
    partes = alvo.split("/")
    reais = onde.get(partes[-1])
    if reais is None:
        return False
    citados = [d for d in partes[:-1] if d not in ("..", ".")]
    if not citados:
        return True
    return any(all(d in dirs for d in citados) for dirs in reais)


def ponteiros(caminho: Path) -> set[str]:
    """Alvos citados por ESTE arquivo, já sem âncora, URL nem sobra de linha."""
    texto = caminho.read_text(encoding="utf-8")
    brutos: set[str] = set()
    for m in RE_LINK.finditer(texto):
        brutos.add(m.group(1))
    padrao = RE_CRASE if caminho.suffix == ".md" else RE_STRING
    for m in padrao.finditer(texto):
        brutos.add(m.group(1).strip())
    alvos: set[str] = set()
    for bruto in brutos:
        alvo = bruto.split("#")[0].split(" ")[0].strip().strip("<>")
        if not alvo or alvo.startswith(("http://", "https://", "mailto:")):
            continue
        if RE_ALVO.match(alvo):
            alvos.add(alvo)
    return alvos


def varre(raiz: Path) -> tuple[list[tuple[str, str]], int]:
    """(mortos, total_de_ponteiros). `mortos` são pares (arquivo, alvo)."""
    onde = nomes_do_repositorio(raiz)
    mortos: list[tuple[str, str]] = []
    total = 0
    for p in arquivos_varridos(raiz):
        rel = p.relative_to(raiz).as_posix()
        for alvo in sorted(ponteiros(p)):
            total += 1
            if (p.parent / alvo).exists() or (raiz / alvo).exists():
                continue
            if alcancavel_por_nome(alvo, onde):
                continue
            mortos.append((rel, alvo))
    return mortos, total


def excecao_de(arquivo: str, alvo: str) -> dict | None:
    for e in EXCECOES:
        if e["alvo"] != alvo:
            continue
        if e["arquivos"] == "*" or arquivo in e["arquivos"]:
            return e
    return None


class TestPonteirosMortos(unittest.TestCase):

    def test_nenhum_ponteiro_morto(self):
        mortos, _ = varre(RAIZ)
        sobrando = [
            f"{arq} -> {alvo}"
            for arq, alvo in mortos
            if excecao_de(arq, alvo) is None
        ]
        self.assertEqual(
            sobrando, [],
            "ponteiro morto: o alvo não existe. Corrija o caminho ou, se for "
            "narrativa histórica, declare em EXCECOES com o porquê.",
        )

    def test_a_varredura_enxerga_o_repositorio(self):
        """Contra o pior modo de falha deste arquivo: passar por vacuidade.

        Regex quebrada acha zero ponteiros e aprova tudo em silêncio — que é o
        defeito que o bloco 17 pagou para aprender."""
        arquivos = arquivos_varridos(RAIZ)
        self.assertGreater(len(arquivos), 50, "a varredura perdeu as árvores")
        _, total = varre(RAIZ)
        self.assertGreater(total, 200, "a extração de ponteiros parou de achar")

    def test_detecta_ponteiro_morto_plantado(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "docs").mkdir()
            (raiz / "docs" / "vivo.md").write_text("ok\n", encoding="utf-8")
            (raiz / "docs" / "a.md").write_text(
                "vivo: [x](vivo.md)\nmorto: [y](sumiu.md)\ncrase: `tambem-sumiu.json`\n",
                encoding="utf-8",
            )
            mortos, total = varre(raiz)
            self.assertEqual(
                sorted(mortos),
                [("docs/a.md", "sumiu.md"), ("docs/a.md", "tambem-sumiu.json")],
            )
            self.assertEqual(total, 3)

    def test_a_valvula_perdoa_caminho_relativo_e_acusa_mudanca_de_diretorio(self):
        """**BLOCO 25 — os dois casos que a válvula tem de separar.**

        Ela foi desenhada contra RENOMEAÇÃO e imprecisão de caminho relativo; o
        bloco 25 fez MUDANÇA DE DIRETÓRIO, o nome-base sobreviveu, e todo
        ponteiro antigo ficou imune. Este teste planta os dois lado a lado no
        MESMO repositório sintético — sem ele, apertar a regra e afrouxá-la de
        volta passa despercebido.
        """
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "docs" / "consolidado").mkdir(parents=True)
            (raiz / "docs" / "sub").mkdir()
            (raiz / "docs" / "consolidado" / "x.json").write_text("{}\n", encoding="utf-8")
            (raiz / "docs" / "sub" / "a.md").write_text(
                # (1) caminho relativo impreciso: o arquivo MORA mesmo num
                #     `consolidado/`, só não a partir deste diretório. PERDOA.
                "impreciso: `consolidado/x.json`\n"
                # (2) nome nu, sem diretório: não promete caminho. PERDOA.
                "nome nu: `x.json`\n"
                # (3) diretório que NÃO é diretório deste arquivo — o caso que
                #     o bloco 25 criou e a válvula larga escondia. ACUSA.
                "mudou de casa: `tabelas-normativas/x.json`\n",
                encoding="utf-8",
            )
            mortos, total = varre(raiz)
            self.assertEqual(total, 3)
            self.assertEqual(mortos, [("docs/sub/a.md", "tabelas-normativas/x.json")])

    def test_url_externa_nao_e_ponteiro(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "docs").mkdir()
            (raiz / "docs" / "a.md").write_text(
                "[a](https://exemplo.gov.br/x.pdf) e `https://y/z.md`\n",
                encoding="utf-8",
            )
            self.assertEqual(varre(raiz), ([], 0))


class TestLedgerNaoEnvelhece(unittest.TestCase):
    """A exceção não pode sobreviver ao fato que a justificava."""

    def setUp(self):
        self.mortos, _ = varre(RAIZ)
        self.pares = {(a, t) for a, t in self.mortos}

    def test_toda_excecao_ainda_corresponde_a_uma_mencao_real(self):
        orfas = []
        for e in EXCECOES:
            if e["arquivos"] == "*":
                if not any(t == e["alvo"] for _, t in self.pares):
                    orfas.append(e["alvo"])
                continue
            for arq in e["arquivos"]:
                if (arq, e["alvo"]) not in self.pares:
                    orfas.append(f"{arq} -> {e['alvo']}")
        self.assertEqual(
            orfas, [],
            "exceção órfã: o alvo passou a existir ou a menção sumiu. "
            "Remova a entrada de EXCECOES.",
        )

    def test_toda_excecao_declara_classe_e_por_que(self):
        for e in EXCECOES:
            self.assertIn(
                e["classe"],
                {"fonte externa", "insumo efêmero de extração",
                 "narrativa histórica", "molde de nomenclatura",
                 # BLOCO 25. Distinta de "narrativa histórica": lá o texto
                 # DESCREVE a mudança ('era X, virou Y'); aqui ele apenas
                 # registrou, na data em que foi escrito, o endereço que o
                 # artefato tinha então — e relatório de bloco não se atualiza.
                 "registro datado de bloco"},
                e["alvo"],
            )
            self.assertGreater(len(e["por_que"]), 30, e["alvo"])

    def test_excecao_por_par_e_nao_por_alvo_solto(self):
        """O curinga '*' é só para fonte externa. Nas demais classes a exceção
        vale nos arquivos que narram o fato, e em nenhum outro — senão o ledger
        vira anistia geral para o nome."""
        for e in EXCECOES:
            if e["arquivos"] == "*":
                self.assertEqual(e["classe"], "fonte externa", e["alvo"])
            else:
                self.assertIsInstance(e["arquivos"], list)
                self.assertTrue(e["arquivos"], e["alvo"])


class TestManifestoDePlugin(unittest.TestCase):
    """O manifesto de plugin aponta para o que existe — BLOCO 24.

    Um manifesto é ponteiro como qualquer outro, e falha mais caro: quando o
    caminho de `skills` não resolve, o plugin instala e **carrega zero skills**,
    em silêncio. E a `description` dele carrega uma contagem em prosa — "Quatro
    skills" — que é exatamente a espécie de número que envelhece sozinho.
    """

    MANIFESTO = RAIZ / ".claude-plugin"
    NUMERAL = {1: "uma", 2: "duas", 3: "três", 4: "quatro",
               5: "cinco", 6: "seis", 7: "sete", 8: "oito"}

    def setUp(self):
        if not self.MANIFESTO.is_dir():
            self.skipTest("sem .claude-plugin/ — repositório não empacotado")
        self.plugin = json.loads(
            (self.MANIFESTO / "plugin.json").read_text(encoding="utf-8"))
        self.market = json.loads(
            (self.MANIFESTO / "marketplace.json").read_text(encoding="utf-8"))
        self.skills = sorted(
            d.name for d in (RAIZ / "skills").iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file())

    def test_o_caminho_de_skills_resolve_e_tem_skill(self):
        rel = self.plugin.get("skills")
        self.assertTrue(rel, "plugin.json sem campo `skills`")
        alvo = (RAIZ / rel.lstrip("./")).resolve()
        self.assertTrue(alvo.is_dir(), f"`skills` não resolve: {rel}")
        self.assertTrue(
            self.skills,
            f"{rel} existe e não tem nenhum <dir>/SKILL.md — o plugin "
            "instalaria carregando zero skills, em silêncio.",
        )

    def test_a_contagem_em_prosa_bate_com_as_skills_que_existem(self):
        """'Quatro skills' é contagem do repositório dentro do manifesto.

        O manifesto está FORA da varredura de `test_numeros.py`, por decisão
        declarada. Esta é a contrapartida dessa decisão: o número não fica sem
        dono só porque o detector não o alcança.
        """
        esperado = self.NUMERAL.get(len(self.skills))
        self.assertIsNotNone(esperado, f"{len(self.skills)} skills — amplie NUMERAL")
        for nome, doc in (("plugin.json", self.plugin),
                          ("marketplace.json", self.market)):
            textos = [doc.get("description", "")]
            textos += [p.get("description", "") for p in doc.get("plugins", [])]
            for texto in textos:
                achados = [n for n in self.NUMERAL.values()
                           if f"{n} skills" in texto.lower()]
                for achado in achados:
                    self.assertEqual(
                        achado, esperado,
                        f"{nome} diz '{achado} skills' e existem "
                        f"{len(self.skills)}: {self.skills}",
                    )

    def test_o_frontmatter_das_skills_so_usa_campos_aceitos(self):
        """Campo fora dos seis aceitos dá ERRO DE CARREGAMENTO — a skill some."""
        aceitos = {"name", "description", "allowed-tools",
                   "compatibility", "license", "metadata"}
        for nome in self.skills:
            texto = (RAIZ / "skills" / nome / "SKILL.md").read_text(encoding="utf-8")
            bloco = texto.split("---")[1]
            chaves = {l.split(":", 1)[0].strip()
                      for l in bloco.splitlines()
                      if l and not l[0].isspace() and ":" in l}
            self.assertLessEqual(
                chaves, aceitos,
                f"{nome}: campo fora dos seis aceitos: {chaves - aceitos}",
            )

    #: Teto de `description` fixado pela spec de Agent Skills. Acima dele o
    #: cliente **derruba a skill no carregamento** — não trunca, não avisa.
    LIMITE_DESCRIPTION = 1024

    @staticmethod
    def _description(texto: str) -> str:
        """A `description` do frontmatter, inclusive quando ocupa várias linhas.

        YAML dobra valor continuado por indentação, e as quatro `description`
        deste repositório são todas dobradas — ler só a primeira linha mediria
        um oitavo do que o cliente mede. O valor conferido é o texto COLADO,
        que é o que conta para o limite.
        """
        bloco = texto.split("---")[1]
        partes: list[str] = []
        dentro = False
        for linha in bloco.splitlines():
            if linha.startswith("description:"):
                dentro = True
                cabeca = linha.split(":", 1)[1].strip()
                # `>-`, `>`, `|` e `|-` são o INDICADOR de bloco do YAML, não
                # conteúdo. Contá-los inflaria a medida em dois caracteres e
                # faria a guarda mentir para os dois lados.
                if cabeca not in (">", ">-", ">+", "|", "|-", "|+"):
                    partes.append(cabeca)
                continue
            if dentro:
                if linha and not linha[0].isspace():
                    break
                partes.append(linha.strip())
        return " ".join(p for p in partes if p)

    def test_nenhuma_description_passa_de_1024(self):
        """BLOCO 25 — a guarda contra a regressão que só aparece no cliente.

        **O modo de falha é silencioso e caro.** A spec de Agent Skills fixa
        `description` em **1024 caracteres no máximo**, e cliente real **recusa
        a skill inteira** quando o limite estoura: não há mensagem no
        repositório, no teste ou no diff — a skill simplesmente não carrega na
        máquina de quem instalou. É exatamente o mesmo feitio do defeito que
        `test_o_caminho_de_skills_resolve_e_tem_skill` existe para matar.

        **Fica aqui, ao lado da guarda de campos aceitos**, porque as duas
        aferem a MESMA coisa — o frontmatter que o cliente lê no startup — e
        pela mesma razão: campo inválido e `description` longa demais têm o
        mesmo efeito, a skill some. Separá-las em arquivos diferentes obrigaria
        a redescobrir o parse do frontmatter duas vezes.

        A `description` é o único gatilho destas skills: elas são
        *model-invoked*, sem comando de invocação. Perdê-la é perder a skill.
        """
        for nome in self.skills:
            texto = (RAIZ / "skills" / nome / "SKILL.md").read_text(encoding="utf-8")
            desc = self._description(texto)
            with self.subTest(skill=nome):
                self.assertTrue(desc, f"{nome}: SKILL.md sem `description`")
                self.assertLessEqual(
                    len(desc), self.LIMITE_DESCRIPTION,
                    f"{nome}: description com {len(desc)} caracteres, acima do "
                    f"teto de {self.LIMITE_DESCRIPTION}. O cliente NÃO trunca: "
                    "derruba a skill no carregamento, em silêncio.",
                )

    def test_a_guarda_de_1024_reprova_uma_description_longa_demais(self):
        """Contra o pior modo de falha de uma guarda: passar por vacuidade.

        Se o parse do frontmatter quebrar, `_description` devolve string curta
        ou vazia e o teto nunca é atingido — a guarda aprovaria tudo. Aqui ela
        é exercida contra um frontmatter sintético que ESTOURA o limite, e
        contra um que fica logo abaixo dele.
        """
        def fabrica(tamanho: int) -> str:
            corpo = "x" * (tamanho - 40)
            return (
                "---\n"
                "name: teste\n"
                "description: >-\n"
                f"  {corpo}\n"
                f"  {'y' * 39}\n"
                "---\n\nprosa\n"
            )

        curta = self._description(fabrica(self.LIMITE_DESCRIPTION))
        longa = self._description(fabrica(self.LIMITE_DESCRIPTION + 200))
        self.assertLessEqual(len(curta), self.LIMITE_DESCRIPTION)
        self.assertGreater(len(longa), self.LIMITE_DESCRIPTION)
        # E a leitura multilinha é a parte que pode regredir sem barulho:
        self.assertGreater(len(curta), 200, "o parse parou na primeira linha")

    def test_as_quatro_descriptions_sao_lidas_inteiras(self):
        """A guarda só vale se `_description` enxergar o valor dobrado.

        Medido no fechamento do bloco 25, uma a uma: **794** (atualização),
        **802** (core), **870** (liquidação) e **890** (índices) caracteres,
        contra o limite de 1024. A prosa dizia *"entre 797 e 893"* e **nenhum
        dos dois extremos era uma medição** — a faixa não continha o menor dos
        quatro. Folga real, e nenhuma delas caberia numa linha só. Não se
        crava o número aqui (ele muda com a prosa); crava-se que o valor lido é
        substancialmente maior que a primeira linha do YAML, que é o sintoma de
        parse truncado.
        """
        for nome in self.skills:
            texto = (RAIZ / "skills" / nome / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=nome):
                self.assertGreater(
                    len(self._description(texto)), 300,
                    f"{nome}: description lida com menos de 300 caracteres — "
                    "ou ela encolheu de verdade, ou o parse truncou.",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
