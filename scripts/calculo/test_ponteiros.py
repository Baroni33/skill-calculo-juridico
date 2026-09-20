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
"""

from __future__ import annotations

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


def nomes_do_repositorio(raiz: Path) -> set[str]:
    """Todo nome-base de arquivo existente. Menção por nome nu resolve aqui."""
    nomes: set[str] = set()
    for p in raiz.rglob("*"):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        if p.is_file():
            nomes.add(p.name)
    return nomes


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
    nomes = nomes_do_repositorio(raiz)
    mortos: list[tuple[str, str]] = []
    total = 0
    for p in arquivos_varridos(raiz):
        rel = p.relative_to(raiz).as_posix()
        for alvo in sorted(ponteiros(p)):
            total += 1
            if (p.parent / alvo).exists() or (raiz / alvo).exists():
                continue
            if alvo.split("/")[-1] in nomes:
                # Nome-base existe em outro diretório: o alvo é alcançável, e
                # o que sobra é imprecisão de caminho relativo, não morte.
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
                 "narrativa histórica", "molde de nomenclatura"},
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
