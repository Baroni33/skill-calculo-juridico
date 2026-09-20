"""NÍVEL 1 — o critério de aceite DA SKILL, executável sem série de índices.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
O conjunto de skills **declara não carregar série de índices** — `indices-judiciais`
diz, literal, "esta skill não carrega série — é o ponto inteiro dela" — e, até o
bloco 23, usava como critério de aceite quatro fixtures do CJF que consomem série
(a fixture 1 sozinha, 23 meses de IPCA-E). **As duas afirmações não podem ser
verdadeiras ao mesmo tempo.**

A resolução do bloco 23 NÃO foi popular série. Foi declarar o nível:

  NÍVEL 1  invariantes e aritmética — R11 pelos dois pares publicados, R12 por AST,
           R1 na composição, as cinco cadeias de arredondamento e o NMP de três
           ramos.                                  EXECUTÁVEL SÓ COM A SKILL.
  NÍVEL 2  as quatro fixtures de tests/fixtures/calculo/.
                                                   EXIGE SÉRIE CARREGADA.

  => NÍVEL 1 é o aceite DA SKILL. NÍVEL 2 é o aceite do SISTEMA, não da skill.

O conteúdo do NÍVEL 1 não é lista idealizada: é o que a Frente A do bloco 22 de
fato acertou lendo só as skills, enumerado em
`docs/calculo/aceitacao/bloco-22-relatorio.md` § 1.

POR QUE EM scripts/calculo/ E NÃO NOS OUTROS DOIS CANDIDATOS
------------------------------------------------------------
  * `tests/fixtures/calculo/` é DADO, não código. Um arquivo a mais ali seria
    prosa que ninguém roda — e critério de aceite que ninguém roda envelhece, que
    é exatamente o defeito que este bloco veio corrigir;
  * uma seção de skill declara, não verifica. A seção existe e APONTA para cá;
  * `scripts/calculo/` é o único diretório do repositório que roda inteiro em toda
    varredura (`python -m unittest discover -s scripts/calculo -p "test_*.py"`), e
    já hospeda os validadores de R1, R2, R3, R6, R11 e R12 que o NÍVEL 1 invoca.

ISTO NÃO É UM MOTOR DE CÁLCULO. A restrição de scripts/calculo/README.md segue
valendo: aqui se afere aritmética normativa e invariante sobre cadeia, cada
asserção ancorada em NÚMERO PUBLICADO pelo corpus. Não se liquida condenação e não
se consulta série de valores.

NENHUM float, em lugar nenhum (R12) — inclusive neste arquivo, que se auto-varre.
"""

from __future__ import annotations

import ast
import json
import unittest
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP, localcontext
from pathlib import Path

from valida_cobertura import valida_cobertura
from valida_taxa_legal import (
    PARES_VALIDACAO_INPC,
    Deflator,
    taxa_legal,
    taxa_legal_por_subtracao,
)

RAIZ = Path(__file__).resolve().parents[2]
TABELAS = RAIZ / "docs" / "calculo" / "tabelas-normativas"
FIXTURES = RAIZ / "tests" / "fixtures" / "calculo"
SKILLS = RAIZ / "skills"

CEM = Decimal("100")


# --------------------------------------------------------------------------
# As cinco cadeias de arredondamento — calculo-judicial-core, seção
# "Aritmética — as cinco cadeias de arredondamento".
# --------------------------------------------------------------------------

def truncar(valor: Decimal, casas: int) -> Decimal:
    """ROUND_DOWN — truncamento, nunca half-up."""
    return valor.quantize(Decimal(1).scaleb(-casas), rounding=ROUND_DOWN)


def fator(valor: Decimal) -> Decimal:
    """Fator de índice e taxa legal: 6 casas, truncamento (CJF 4.2.1.1, Nota 6)."""
    return truncar(valor, 6)


def moeda(valor: Decimal) -> Decimal:
    """Valor monetário intermediário e final: 2 casas, truncamento (CJF)."""
    return truncar(valor, 2)


def grandeza_fisica(valor: Decimal) -> Decimal:
    """Hora centesimal, nº de HE: half-up, 2 casas (TRT-3, item 5.3)."""
    return valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def nmp(valor: Decimal) -> Decimal:
    """NMP do RRA — TRÊS RAMOS, 1 casa (IN 1500/14, art. 45, § único).

    2ª casa < 5 mantém; > 5 sobe; == 5 manda olhar a 3ª casa (0-4 mantém, 5-9
    sobe). NÃO é ROUND_HALF_UP: difere na faixa x,y50 a x,y54.
    """
    negativo = valor < 0
    v = -valor if negativo else valor
    decimo = truncar(v, 1)
    resto = (v - decimo) * CEM
    segunda = int(truncar(resto, 0))
    if segunda < 5:
        r = decimo
    elif segunda > 5:
        r = decimo + Decimal("0.1")
    else:
        terceira = int(truncar((resto - segunda) * Decimal(10), 0))
        r = decimo + (Decimal("0.1") if terceira >= 5 else Decimal("0"))
    return -r if negativo else r


class TestCincoCadeiasDeArredondamento(unittest.TestCase):
    """Cada asserção ancorada em célula PUBLICADA pelo manual (D8-D33).

    Seis células em que ROUND_HALF_UP daria outro número e o manual publica o
    truncado — a refutação medida que sustenta R12 nos itens 4.2.1.1 e 5.2.1.
    """

    CELULAS_D8_D33 = [
        ("4.2.1.1 fev/2020 principal", "1133.9588923", "1133.95", "1133.96"),
        ("4.2.1.1 jan/2020 juros 2,45%", "27.979245", "27.97", "27.98"),
        ("4.2.1.1 SELIC 43,89% s/ juros", "24.468675", "24.46", "24.47"),
        ("5.2.1 resumido, pago 8/2018", "22192.058973", "22192.05", "22192.06"),
        ("5.2.1 detalhado, 3º passo", "1575.368833977", "1575.36", "1575.37"),
        ("5.2.1 detalhado, juros pagos", "3176.18682129", "3176.18", "3176.19"),
    ]

    def test_moeda_trunca_em_2_e_nao_arredonda(self):
        for rotulo, exato, truncado, half_up in self.CELULAS_D8_D33:
            with self.subTest(rotulo):
                self.assertEqual(moeda(Decimal(exato)), Decimal(truncado))
                self.assertNotEqual(Decimal(truncado), Decimal(half_up),
                                    "a célula deixou de discriminar os critérios")

    def test_fator_trunca_em_6(self):
        """1,3770478004 -> 1,377047. Truncamento, não half-up (o par de set/2025)."""
        self.assertEqual(fator(Decimal("1.3770478004")), Decimal("1.377047"))

    def test_grandeza_fisica_e_half_up_e_nao_truncamento(self):
        """A quarta cadeia existe porque NÃO é a mesma das outras três."""
        self.assertEqual(grandeza_fisica(Decimal("1.005")), Decimal("1.01"))
        self.assertEqual(moeda(Decimal("1.005")), Decimal("1.00"))

    def test_um_trinta_avos_e_dizima_e_nao_o_truncamento_impresso(self):
        """O corpus grafa 0,0333% na regra e 0,03333% no exemplo duas linhas
        abaixo. Nenhum dos dois é o operando: 1/30 é dízima."""
        um_trinta = Decimal(1) / Decimal(30)
        self.assertNotEqual(um_trinta, Decimal("0.0333"))
        self.assertNotEqual(um_trinta, Decimal("0.03333"))
        self.assertEqual(truncar(um_trinta, 6), Decimal("0.033333"))


class TestNMPTresRamos(unittest.TestCase):
    """O ramo que mais se erra: `= 5` na 2ª casa manda olhar a 3ª."""

    def test_os_tres_ramos(self):
        self.assertEqual(nmp(Decimal("12.44")), Decimal("12.4"))   # < 5 mantém
        self.assertEqual(nmp(Decimal("12.46")), Decimal("12.5"))   # > 5 sobe
        self.assertEqual(nmp(Decimal("12.450")), Decimal("12.4"))  # = 5, 3ª = 0
        self.assertEqual(nmp(Decimal("12.455")), Decimal("12.5"))  # = 5, 3ª = 5

    def test_a_faixa_em_que_difere_de_round_half_up(self):
        """x,y50 a x,y54 — é a faixa inteira, e é onde a regra ganha sentido."""
        divergiram = []
        for centesimo in range(0, 5):
            v = Decimal("12.45") + Decimal(centesimo).scaleb(-3)
            half = v.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
            self.assertEqual(nmp(v), Decimal("12.4"), str(v))
            self.assertEqual(half, Decimal("12.5"), str(v))
            divergiram.append(str(v))
        self.assertEqual(len(divergiram), 5)

    def test_fora_da_faixa_os_dois_criterios_coincidem(self):
        for bruto in ("12.455", "12.459", "12.46", "12.44", "12.40"):
            v = Decimal(bruto)
            self.assertEqual(nmp(v), v.quantize(Decimal("0.1"),
                                                rounding=ROUND_HALF_UP), bruto)


class TestR11TaxaLegalPorRazao(unittest.TestCase):
    """R11 — os DOIS pares publicados, e a demonstração ativa de que a subtração
    de percentuais diverge. Variante INPC (previdenciária)."""

    def test_os_dois_pares_publicados_fecham_pela_razao(self):
        self.assertEqual(len(PARES_VALIDACAO_INPC), 2)
        for par in PARES_VALIDACAO_INPC:
            with self.subTest(par["rotulo"]):
                self.assertEqual(
                    taxa_legal(par["fator_selic"], par["fator_deflator"],
                               Deflator.INPC),
                    par["esperado"],
                )

    def test_a_subtracao_de_percentuais_DIVERGE_nos_dois(self):
        """Não basta a razão acertar: a alternativa tem de falhar, senão o par
        não discrimina método nenhum."""
        for par in PARES_VALIDACAO_INPC:
            with self.subTest(par["rotulo"]):
                self.assertNotEqual(
                    taxa_legal_por_subtracao(par["fator_selic"],
                                             par["fator_deflator"]),
                    par["esperado"],
                )

    def test_half_up_nao_reproduz_o_par_de_set_2025(self):
        with localcontext() as ctx:
            ctx.prec = 40
            exato = (Decimal("1.01164156") / Decimal("0.9979") - 1) * CEM
        half = exato.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
        self.assertEqual(fator(exato), Decimal("1.377047"))
        self.assertNotEqual(half, Decimal("1.377047"))


# --------------------------------------------------------------------------
# R12 por AST — zero literais float
# --------------------------------------------------------------------------
class TestR12ZeroFloatPorAST(unittest.TestCase):
    """'Nenhum float. Em lugar nenhum.' — verificado por árvore sintática, não
    por grep.

    ESCOPO DECLARADO: todo `.py` de `scripts/calculo/` e de
    `docs/calculo/aceitacao/frente-a/`, EXCETO os `test_*.py`. A exceção é
    necessária e não é anistia: `test_valida_taxa_legal.py` e
    `test_valida_parametros.py` PLANTAM float de propósito, para provar que o
    caminho aritmético o RECUSA. Varrer o teste negativo junto acusaria
    exatamente a prova de que R12 está implementado.
    """

    ARVORES = (
        RAIZ / "scripts" / "calculo",
        RAIZ / "docs" / "calculo" / "aceitacao" / "frente-a",
    )

    def _fontes(self):
        for arvore in self.ARVORES:
            for p in sorted(arvore.rglob("*.py")):
                if "__pycache__" in p.parts or p.name.startswith("test_"):
                    continue
                yield p

    def test_nenhum_literal_float(self):
        achados = []
        vistos = 0
        for p in self._fontes():
            vistos += 1
            arvore = ast.parse(p.read_text(encoding="utf-8"))
            for no in ast.walk(arvore):
                if isinstance(no, ast.Constant) and isinstance(no.value, float):
                    achados.append(f"{p.relative_to(RAIZ).as_posix()}:{no.lineno}")
        self.assertEqual(achados, [], "literal float — R12 é absoluto")
        self.assertGreater(vistos, 8, "a varredura perdeu as árvores")

    def test_nenhuma_chamada_a_float(self):
        achados = []
        for p in self._fontes():
            arvore = ast.parse(p.read_text(encoding="utf-8"))
            for no in ast.walk(arvore):
                if (isinstance(no, ast.Call) and isinstance(no.func, ast.Name)
                        and no.func.id == "float"):
                    achados.append(f"{p.relative_to(RAIZ).as_posix()}:{no.lineno}")
        self.assertEqual(achados, [], "conversão para float — R12 é absoluto")

    def test_a_varredura_detecta_um_float_plantado(self):
        """Contra o pior modo de falha: passar por vacuidade."""
        arvore = ast.parse("x = 1.5\n")
        self.assertTrue(any(isinstance(n, ast.Constant) and isinstance(n.value, float)
                            for n in ast.walk(arvore)))


# --------------------------------------------------------------------------
# R1 na composição, sobre as cadeias reais do CJF
# --------------------------------------------------------------------------
CADEIA_CORRECAO = "cjf.condenatorias-gerais.correcao-monetaria.json"
CADEIA_JUROS = "cjf.condenatorias-gerais.juros-mora.json"
RAMOS = ("fazenda-publica", "nao-fazenda-publica")


def _comp_int(competencia: str) -> int:
    ano, mes = competencia.split("-")
    return int(ano) * 12 + int(mes) - 1


def _carrega(nome: str) -> dict:
    return json.loads((TABELAS / nome).read_text(encoding="utf-8"))


def _do_ramo(cadeia: dict, ramo: str) -> list[dict]:
    """Filtro por igualdade EXATA: `in` traria 'nao-fazenda-publica' em
    'fazenda-publica'."""
    out = []
    for s in cadeia["segmentos"]:
        cond = s.get("condicao") or s.get("condicoes")
        if cond is None or cond.get("devedor") == ramo:
            out.append(s)
    return out


class TestR1NaComposicao(unittest.TestCase):
    """'Devem ser impedidas NA COMPOSIÇÃO, não detectadas no resultado.'

    Mês a mês, de 1964-01 a 2026-06, nos dois ramos de devedor: quando o
    segmento de juros engloba correção monetária (SELIC, taxa legal), a linha de
    correção NÃO entra — NOTA 2 do item 4.2.1. Zero cumulações é o resultado
    correto; a sobreposição bruta das duas cadeias é DO ORIGINAL e a NOTA 2 a
    resolve.
    """

    JANELA = ("1964-01", "2026-06")

    def _compor(self, competencia, ramo, correcao, juros):
        n = _comp_int(competencia)
        segs_j = [s for s in _do_ramo(juros, ramo)
                  if _comp_int(s["inicio"]) <= n <= _comp_int(s["fim"])]
        segs_c = [s for s in _do_ramo(correcao, ramo)
                  if _comp_int(s["inicio"]) <= n <= _comp_int(s["fim"])]
        if not segs_j:
            return None
        engloba = "correcao-monetaria" in (segs_j[0].get("engloba") or [])
        return None if engloba else (segs_c[0] if segs_c else None)

    def test_zero_cumulacoes_nos_dois_ramos(self):
        correcao, juros = _carrega(CADEIA_CORRECAO), _carrega(CADEIA_JUROS)
        inicio, fim = (_comp_int(c) for c in self.JANELA)
        for ramo in RAMOS:
            violacoes, meses_vistos = [], 0
            for n in range(inicio, fim + 1):
                comp = "%04d-%02d" % (n // 12, n % 12 + 1)
                meses_vistos += 1
                segs_j = [s for s in _do_ramo(juros, ramo)
                          if _comp_int(s["inicio"]) <= n <= _comp_int(s["fim"])]
                if not segs_j:
                    continue
                engloba = "correcao-monetaria" in (segs_j[0].get("engloba") or [])
                tem_correcao = self._compor(comp, ramo, correcao, juros) is not None
                if engloba and tem_correcao:
                    violacoes.append(comp)
            with self.subTest(ramo):
                self.assertEqual(violacoes, [])
                self.assertGreater(meses_vistos, 700, "a janela encolheu")

    def test_a_supressao_da_NOTA_2_de_fato_ocorre(self):
        """Se nada fosse suprimido, o teste acima passaria por vacuidade."""
        correcao, juros = _carrega(CADEIA_CORRECAO), _carrega(CADEIA_JUROS)
        suprimidos = 0
        inicio, fim = (_comp_int(c) for c in self.JANELA)
        for n in range(inicio, fim + 1):
            segs_j = [s for s in _do_ramo(juros, "fazenda-publica")
                      if _comp_int(s["inicio"]) <= n <= _comp_int(s["fim"])]
            if segs_j and "correcao-monetaria" in (segs_j[0].get("engloba") or []):
                suprimidos += 1
        self.assertGreater(suprimidos, 0,
                           "nenhum segmento engloba correção — R1 ficaria vazia")


class TestR2CoberturaDasCadeiasDoCJF(unittest.TestCase):
    """R2 sobre as mesmas duas cadeias: o que sobrar tem de ser sobreposição DO
    ORIGINAL — jan/1989, que o manual justifica, e mar/1990, que ele não."""

    def test_as_violacoes_restantes_sao_as_do_original(self):
        for nome in (CADEIA_CORRECAO, CADEIA_JUROS):
            cadeia = _carrega(nome)
            relatorio = valida_cobertura(
                cadeia["segmentos"],
                dominio_condicoes=cadeia.get("dominio_condicoes"),
            )
            with self.subTest(nome):
                r2 = relatorio.por_regra("R2")
                self.assertLessEqual(
                    len(r2), 2,
                    "R2 além das sobreposições conhecidas do original:\n"
                    + "\n".join(str(v) for v in r2),
                )


# --------------------------------------------------------------------------
# A declaração do NÍVEL 2 não pode regredir em silêncio
# --------------------------------------------------------------------------
class TestNivel2EstaDeclaradoComoBloqueado(unittest.TestCase):
    """O defeito que o bloco 23 corrigiu foi de AFIRMAÇÃO, não de código. Uma
    afirmação corrigida sem teste volta — é o argumento de test_ponteiros.py."""

    def test_o_readme_das_fixtures_nao_as_chama_de_aceite_da_skill(self):
        texto = (FIXTURES / "README.md").read_text(encoding="utf-8")
        self.assertIn("critério de aceite do SISTEMA", texto)
        self.assertIn("NÍVEL 1", texto)
        self.assertIn("NÍVEL 2", texto)
        self.assertNotIn(
            "São o critério de aceite do motor: um agente novo lê a skill", texto,
            "a afirmação falsa voltou: um agente que só tem a skill não roda estas "
            "fixtures, porque falta a série",
        )

    def test_as_skills_que_citam_as_fixtures_declaram_a_dependencia_de_serie(self):
        for skill in ("calculo-judicial-core", "calculo-judicial-atualizacao"):
            texto = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill):
                self.assertIn("NÍVEL 2", texto)
                self.assertIn("Limitações declaradas", texto)
                self.assertTrue(
                    "série" in texto and "não a carrega por desenho" in texto
                    or "não carrega por desenho" in texto,
                    "a Limitação sobre a série ausente sumiu",
                )

    def test_a_redacao_divergem_do_corpus_nao_voltou_as_skills(self):
        """A redação induziu o defeito do runner: 'do corpus' se lê como banda de
        tolerância; 'entre os métodos' se lê como dois cálculos. Relatório de
        bloco é registro datado e fica fora deste escopo."""
        for p in sorted(SKILLS.rglob("*.md")):
            with self.subTest(p.relative_to(RAIZ).as_posix()):
                self.assertNotIn("fixtures 2 e 4 divergem do corpus",
                                 p.read_text(encoding="utf-8"))

    def test_as_duas_fixtures_seguem_declarando_a_assercao(self):
        """Guarda contra 'ajustar a fixture para passar'."""
        esperado = {"fixture-02-fazenda-publica-jun2026.json": "0.01",
                    "fixture-04-precatorio-complementar.json": "0.03"}
        for nome, valor in esperado.items():
            fx = json.loads((FIXTURES / nome).read_text(encoding="utf-8"))
            with self.subTest(nome):
                self.assertTrue(fx["tolerancia"]["divergencia_e_assercao"])
                self.assertEqual(fx["tolerancia"]["valor"], valor)


if __name__ == "__main__":
    unittest.main(verbosity=2)
