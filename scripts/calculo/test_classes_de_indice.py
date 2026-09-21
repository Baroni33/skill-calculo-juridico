"""Classe de índice (`R3`) afirmada numa skill e divergente do catálogo.

O bloco 19 moveu **IPCA-E/IBGE** e **IPCA-15/IBGE** de `indeterminado` para
`janela-deslocada` no catálogo. Quatro blocos depois, `calculo-judicial-core/
SKILL.md` ainda publicava *"IPCA-E, IPCA-15 … são `indeterminado`"* e
`references/civel-federal.md` repetia a mesma frase — e a aceitação da frente A
**citou os dois lados no mesmo item sem notar que se contradizem**. As fixtures
1 a 3 são cadeias de IPCA-E: a divergência morde exatamente onde dói.

**É a mesma doença de `test_numeros.py`** — o valor com dono copiado para um
lugar sem dono —, com uma diferença que muda o desenho: lá o número pode ter
razão legítima para ficar desatualizado (registro datado, narrativa histórica),
e por isso existe um ledger. **Aqui não pode.** A classe de R3 não tem versão
histórica publicável numa skill: ou é a do catálogo, ou está errada.
**Este arquivo não tem ledger de exceções, e isso é decisão, não esquecimento.**

A FONTE É O CATÁLOGO, E A SKILL APONTA
---------------------------------------
`skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json`, cuja própria
`REGRA_DESTE_CATALOGO` diz *"o valor SAI DA FONTE … NUNCA classificado por
dedução a partir do nome"*. Este teste não julga se a classe está **certa** —
isso é matéria da fonte normativa. Ele julga se a skill **diz o mesmo que o
catálogo**, rótulo a rótulo.

ESCOPO DECLARADO DA VARREDURA — CONTADO ANTES DE DECLARADO
-----------------------------------------------------------
  árvore: `skills/`, extensão `.md` — **todas**, `SKILL.md` e `references/`
  fora: nada. Não há exclusão, e `TestEscopoContado` prova a identidade
        `varridos == tudo que a árvore tem`, para que "os N arquivos" seja
        sempre uma CONTA e nunca um rótulo.
  `docs/` fica fora **por competência, não por descuido**: lá o dono é o
        catálogo e o consolidado, e quem os audita é `valida_cadeias.py` /
        `valida_cobertura.py`, que leem o JSON diretamente. O defeito que este
        arquivo mata é **a cópia na skill**.

O QUE O DETECTOR PROCURA — DOIS IDIOMAS, NENHUMA JANELA DE PROXIMIDADE
-----------------------------------------------------------------------
**(1) `R-TABELA`.** Linha de tabela markdown com **exatamente uma** célula
marcada por classe. Duas formas, e a direção do vizinho muda com a forma:

  * célula que é **só** o token (`| **ORTN** | nominal | nota |`) → o índice
    está na célula **anterior**. É o idioma de `fgts.md` e `poupanca.md`;
  * célula que **começa** pelo token e descreve a classe
    (`| **nominal** — inflação do mês anterior | ORTN, OTN, … | fonte |`) → os
    índices estão na célula **seguinte**. É o idioma das tabelas de classe.

**(2) `R-PRED`.** O predicado em prosa: `X e Y são <classe>`, e a variante
invertida `são <classe> — entre eles X, Y`. Foi nesta forma que as duas
divergências reais estavam escritas, nas duas.

**NÃO procura por proximidade** — nome de índice e token de classe a N
caracteres um do outro. Não é descuido: é a decisão mais importante deste
arquivo, e foi **MEDIDA antes de tomada**, sobre o repositório no estado em que
a tarefa o encontrou:

  janela ±40 →  77 pares,  28 "divergências"
  janela ±60 → 114 pares,  52 "divergências"
  janela ±80 → 149 pares,  75 "divergências"
  janela ±120 → 190 pares, 103 "divergências"
  **R-TABELA + R-PRED → 73 pares, 4 divergências, TODAS reais**
  (as 4 são as duas frases defeituosas × os dois índices de cada uma)

Medido **de novo depois das correções desta tarefa**, e o par de números é o
argumento inteiro da decisão editorial: **45 pares, 0 divergências**. Caíram 28
afirmações — não porque o detector piorou, mas porque as listas copiadas
viraram ponteiro. **Menos afirmação de classe numa skill é menos superfície
para envelhecer**, e o piso de `test_a_varredura_enxerga_o_repositorio` é o que
impede que essa queda vá longe demais e o detector fique cego.

Das 52 da janela ±60, **48 eram falso positivo**, e sempre pela mesma causa: a
prosa que ENSINA R3 põe as classes lado a lado — *"nominal (Ufir, BTN, OTN,
ORTN) reflete o mês anterior; percentual (INPC, IGP-DI), o próprio"* —, de modo
que qualquer janela larga o bastante para pegar a afirmação pega também a
classe vizinha. Pô-las num ledger custaria ~48 entradas para dizer 48 vezes
*"aqui está certo"*, **e ledger que ninguém consegue manter vira ruído, o teste
passa a ser ignorado, e validador ignorado é pior que validador ausente** — o
argumento da tarefa 4 do bloco 17, o mesmo que `test_ponteiros.py` e
`test_numeros.py` usaram para recusar heurística de contexto.

O CUSTO ACEITO, DECLARADO
--------------------------
**Passa ileso:** a classe afirmada em prosa fora dos dois idiomas — a
enumeração entre parênteses (*"nominal (Ufir, BTN, OTN, ORTN)"*), o rótulo em
lista com travessão, a afirmação partida entre dois parágrafos. **É cobertura
parcial, e assumida.** Em troca, o detector **não tem ledger**: qualquer achado
divergente é defeito, a mensagem já diz onde, e não existe a categoria
"exceção declarada" para alguém pendurar um erro.

**A mitigação do custo não é regex maior, é editorial** — e foi feita nesta
mesma tarefa: as skills deixaram de **copiar** as listas por classe e passaram
a **apontar** para o catálogo. Onde a lista permaneceu por clareza pedagógica,
permaneceu **na forma de tabela**, que é justamente a que este detector lê.
Cada enumeração que vira ponteiro é uma afirmação a menos para envelhecer.

**O segundo modo de falha, e o pior:** passar por vacuidade. Regex quebrada
acha zero e aprova tudo em silêncio. `test_a_varredura_enxerga_o_repositorio`
exige piso de achados, e `test_detecta_divergencia_plantada` prova nos dois
idiomas que o detector ainda morde.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
# BLOCO 25 — o catálogo migrou para dentro de `calculo-judicial-atualizacao`.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import caminhos_de_skill  # noqa: E402
CATALOGO = caminhos_de_skill.CATALOGO_INDEXADORES
SKILLS = RAIZ / "skills"

#: As cinco classes do vocabulário fechado de `tipo_indexador`. `englobante`
#: **não entra**: foi RETIRADO no bloco 19, e uma skill que ainda o use está
#: falando de R1 no campo de R3 — outro defeito, de outro teste.
CLASSES = ("janela-deslocada", "nao-indexador", "indeterminado", "percentual", "nominal")

#: Grafias com que as skills nomeiam o rótulo do catálogo. **Só apelido de
#: GRAFIA, nunca de identidade:** `IPCA-E` é como a prosa escreve
#: `IPCA-E/IBGE`. O que NÃO entra aqui é o par que a fonte trata como índices
#: diferentes — `IPC` nu × `IPC/IBGE` é a ambiguidade registrada em `D8-C21`, e
#: unificá-los seria o próprio erro que o catálogo proíbe.
APELIDOS = {
    "IPCA-E/IBGE": ("IPCA-E",),
    "IPCA-15/IBGE": ("IPCA-15",),
    "taxa-legal": ("taxa legal",),
    "Selic": ("SELIC",),
}

_CL = "(" + "|".join(CLASSES) + ")"
RE_CLASSE_PURA = re.compile("^" + _CL + "$")
RE_CLASSE_INICIAL = re.compile("^" + _CL + r"\b")
RE_PREDICADO = re.compile(
    r"([^.;|>\n]{0,120}?)"
    r"(?:são|é|ficam|fica|seguem|segue|permanecem|permanece|continuam|continua)\s+"
    r"[`*\"“ ]{0,3}" + _CL + r"\b"
    r"(?:[`*\"” ]{0,3}[—\-]{0,2}\s*(?:entre eles|entre elas|a saber|:)?([^.;|>\n]{0,120})?)?"
)


def classes_do_catalogo() -> dict[str, str]:
    """`{grafia da skill: classe}`. Rótulo composto e sentinela ficam fora.

    `Ufir → Selic` e `UPC → índices básicos…` são **segmentos compostos**: o
    rótulo não é um índice, é uma bifurcação, e casá-lo por substring pegaria
    as duas pontas com a classe do composto. `(segmento sem indexador)` não é
    nome que prosa alguma escreva.
    """
    dados = json.loads(CATALOGO.read_text(encoding="utf-8"))
    fora: dict[str, str] = {}
    for rotulo, corpo in dados["indexadores"].items():
        if rotulo.startswith("(") or "→" in rotulo:
            continue
        for grafia in (rotulo,) + APELIDOS.get(rotulo, ()):
            fora[grafia] = corpo["tipo"]
    return fora


def arquivos_varridos() -> list[Path]:
    return sorted(p for p in SKILLS.rglob("*.md") if p.is_file())


def _desmarca(texto: str) -> str:
    return re.sub(r"[`*_~]", "", texto).strip()


def _nomes_em(texto: str, nomes: dict[str, str]) -> list[str]:
    """Rótulos citados no trecho, do mais longo para o mais curto.

    A fronteira exclui `/` e `-` além de `\\w`: sem isso, `IPC` casaria dentro
    de `IPC/IBGE` e `IPCA-E`, e `BTN` dentro de `BTNF` — que é literalmente a
    dedução por semelhança de nome que `P19-02` proíbe.
    """
    limpo = _desmarca(texto)
    achados = []
    for nome in sorted(nomes, key=len, reverse=True):
        if re.search(r"(?<![\w/\-])" + re.escape(nome) + r"(?![\w/\-])", limpo):
            achados.append(nome)
    return achados


def afirmacoes(raiz_skills: Path, nomes: dict[str, str]) -> list[tuple[str, int, str, str]]:
    """`(arquivo, linha, rótulo, classe afirmada)`, ordenado e sem repetição."""
    fora: set[tuple[str, int, str, str]] = set()
    for caminho in sorted(p for p in raiz_skills.rglob("*.md") if p.is_file()):
        rel = caminho.relative_to(raiz_skills.parent).as_posix()
        for n, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), 1):
            for rotulo, classe in _r_tabela(linha, nomes) + _r_predicado(linha, nomes):
                fora.add((rel, n, rotulo, classe))
    return sorted(fora)


def _r_tabela(linha: str, nomes: dict[str, str]) -> list[tuple[str, str]]:
    if not linha.lstrip().startswith("|"):
        return []
    celulas = linha.strip().strip("|").split("|")
    marcadas = []
    for j, celula in enumerate(celulas):
        limpa = _desmarca(celula)
        inicio = RE_CLASSE_INICIAL.match(limpa)
        # Célula que cita DUAS classes é vocabulário — `| nominal · percentual
        # | reflete … |` —, não afirmação sobre um índice. Adivinhar qual token
        # vale para qual nome seria a heurística que este arquivo recusa.
        if not inicio or len(re.findall(_CL, limpa)) != 1:
            continue
        marcadas.append((j, inicio.group(1), bool(RE_CLASSE_PURA.match(limpa))))
    # Mesma razão, agora entre células: duas classes na linha, nenhuma afirmação.
    if len(marcadas) != 1:
        return []
    j, classe, pura = marcadas[0]
    alvo = j - 1 if (pura and j > 0) else j + 1
    if not 0 <= alvo < len(celulas):
        return []
    return [(nome, classe) for nome in _nomes_em(celulas[alvo], nomes)]


def _r_predicado(linha: str, nomes: dict[str, str]) -> list[tuple[str, str]]:
    achados = []
    for m in RE_PREDICADO.finditer(linha):
        classe = m.group(2)
        for lado in (m.group(1), m.group(3) or ""):
            achados += [(nome, classe) for nome in _nomes_em(lado, nomes)]
    return achados


def divergencias(raiz_skills: Path, nomes: dict[str, str]) -> list[str]:
    return [
        f"{arq}:{lin}: a skill diz que `{rotulo}` é `{classe}`; "
        f"o catálogo diz `{nomes[rotulo]}`"
        for arq, lin, rotulo, classe in afirmacoes(raiz_skills, nomes)
        if classe != nomes[rotulo]
    ]


# --------------------------------------------------------------------------
class TestSkillNaoDivergeDoCatalogo(unittest.TestCase):

    def setUp(self):
        self.nomes = classes_do_catalogo()

    def test_nenhuma_skill_afirma_classe_diferente_da_do_catalogo(self):
        self.assertEqual(
            divergencias(SKILLS, self.nomes), [],
            "classe de R3 divergente do catálogo. **Não conserte o catálogo "
            "para o texto passar**: o valor sai da fonte. Corrija a skill — e, "
            "de preferência, troque a lista copiada por um ponteiro para "
            "`skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json`.",
        )

    def test_a_varredura_enxerga_o_repositorio(self):
        """Contra o pior modo de falha: passar por vacuidade."""
        self.assertGreater(len(arquivos_varridos()), 25, "a varredura perdeu skills/")
        self.assertGreater(len(self.nomes), 25, "o catálogo não foi lido")
        self.assertGreater(
            len(afirmacoes(SKILLS, self.nomes)), 30,
            "o detector parou de achar afirmação de classe — regex quebrada "
            "acha zero e aprova tudo em silêncio",
        )

    def test_o_catalogo_so_usa_o_vocabulario_fechado(self):
        """Se o catálogo ganhar uma classe nova, este arquivo fica cego a ela —
        e falhar aqui é mais barato que aprovar por desconhecimento."""
        for rotulo, classe in classes_do_catalogo().items():
            self.assertIn(classe, CLASSES, rotulo)

    def test_todo_apelido_aponta_para_rotulo_que_existe(self):
        """Apelido órfão é escopo mentiroso: o nome some do catálogo e o
        detector continua jurando que o cobre."""
        rotulos = json.loads(CATALOGO.read_text(encoding="utf-8"))["indexadores"]
        for rotulo in APELIDOS:
            self.assertIn(rotulo, rotulos, f"apelido sem rótulo: {rotulo}")


class TestEscopoContado(unittest.TestCase):
    """Escopo é CONTA, não rótulo — a regra que o bloco 20 pagou para aprender.

    Aqui a identidade é trivial porque não há exclusão nenhuma, e é isso que o
    teste publica: **varridos == todo `.md` sob `skills/`**. No dia em que
    alguém acrescentar uma exclusão, ela terá de aparecer aqui.
    """

    def test_varre_tudo_que_a_arvore_tem(self):
        tudo = sorted(p for p in SKILLS.rglob("*.md") if p.is_file())
        self.assertEqual(arquivos_varridos(), tudo)
        self.assertTrue(tudo, "skills/ não tem .md — árvore errada")

    def test_alcanca_espinha_e_references(self):
        rels = {p.relative_to(RAIZ).as_posix() for p in arquivos_varridos()}
        self.assertTrue(any(r.endswith("/SKILL.md") for r in rels))
        self.assertTrue(any("/references/" in r for r in rels))


class TestDeteccao(unittest.TestCase):
    """Os dois idiomas, plantados; e o que deve passar ileso."""

    def setUp(self):
        self.nomes = {"IPCA-E": "janela-deslocada", "ORTN": "nominal", "INPC": "percentual"}

    def _sobre(self, texto: str):
        with tempfile.TemporaryDirectory() as d:
            alvo = Path(d) / "skills" / "x"
            alvo.mkdir(parents=True)
            (alvo / "SKILL.md").write_text(texto, encoding="utf-8")
            return divergencias(Path(d) / "skills", self.nomes)

    def test_detecta_divergencia_plantada_no_predicado(self):
        """A forma exata das duas divergências reais desta tarefa."""
        self.assertEqual(len(self._sobre("**IPCA-E e IPCA-15 são `indeterminado`**\n")), 1)
        self.assertEqual(
            len(self._sobre("Dez indexadores são `indeterminado` — entre eles IPCA-E e a TR.\n")), 1
        )

    def test_detecta_divergencia_plantada_na_tabela(self):
        self.assertEqual(
            len(self._sobre("| mar/1986 | **IPCA-E** | percentual | nota |\n")), 1
        )
        self.assertEqual(
            len(self._sobre("| **percentual** — o próprio mês | **INPC, IPCA-E** | fonte |\n")), 1
        )

    def test_o_que_confere_com_o_catalogo_passa(self):
        self.assertEqual(self._sobre("| jan/1965 | **ORTN** | nominal | ponta |\n"), [])
        self.assertEqual(self._sobre("O **IPCA-E** é `janela-deslocada` desde o bloco 19.\n"), [])

    def test_a_prosa_que_ENSINA_a_regra_passa_ilesa(self):
        """O custo aceito, virado teste: sem isto, o ledger teria ~48 entradas.

        A frase abaixo põe as duas classes lado a lado e está CERTA; qualquer
        detector por proximidade a acusaria."""
        self.assertEqual(
            self._sobre(
                "Nominal (ORTN) reflete a inflação do mês anterior; percentual "
                "(INPC), a do próprio mês, e o IPCA-E não é nenhum dos dois.\n"
            ),
            [],
        )

    def test_tabela_de_vocabulario_com_duas_classes_nao_afirma_nada(self):
        self.assertEqual(
            self._sobre("| `nominal` · `percentual` | mês anterior · próprio — ORTN, INPC |\n"), []
        )

    def test_fronteira_de_nome_nao_deduz_por_semelhanca(self):
        """`BTNF` não herda do `BTN`, `IPC` não é `IPC/IBGE` — `P19-02`."""
        nomes = {"BTN": "nominal", "IPC": "indeterminado"}
        with tempfile.TemporaryDirectory() as d:
            alvo = Path(d) / "skills" / "x"
            alvo.mkdir(parents=True)
            (alvo / "SKILL.md").write_text(
                "| 1990 | **BTNF** | percentual | x |\n"
                "| 1986 | **IPC/IBGE** | percentual | y |\n",
                encoding="utf-8",
            )
            self.assertEqual(divergencias(Path(d) / "skills", nomes), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
