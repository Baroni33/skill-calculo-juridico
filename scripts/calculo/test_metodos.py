"""Confronta `metodos.py` com as CÉLULAS PUBLICADAS do Manual CJF.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
Até o bloco 23, **nenhum teste do repositório confrontava `metodos.py`**.
`grep -l metodos scripts/calculo/test_*.py` devolvia **vazio**. O único
"teste" era um `hasattr(metodos, "detalhado")` dentro do runner — que é
verificar que a função EXISTE, não que ela está CERTA. E estava errada: a
regra `T3` proibia, em prosa, a célula `55,75 × 43,89% = 24,46` que o próprio
manual publica na `pagina_pdf` 52 e que a § 10-A.8 do consolidado já listava
como prova de truncamento.

**ESTE TESTE NÃO PRECISA DE SÉRIE.** Os coeficientes estão IMPRESSOS no PDF
(10 casas) e transcritos no consolidado. O que se afere aqui é **o
procedimento**: dado o coeficiente publicado, a sequência de operações e de
truncamentos reproduz — ou não — o número publicado. Nenhum índice mensal é
consultado; `series.py` não é importado.

FONTE, com `pagina_pdf` (offset 1: `numero_impresso = pagina_pdf − 1`):
  * **51** — 4.2.1.1, 1º Exemplo, cálculo **detalhado** até jun/2022
  * **52** — 4.2.1.1, 1º Exemplo **resumido**; 2º Exemplo **detalhado** até jun/2026
  * **53** — 4.2.1.1, 2º Exemplo **resumido**
  * **91** — 5.2.1.1, precatório complementar, **resumido**
  * **92** — 5.2.1.2, precatório complementar, **detalhado**

ORDEM: começa pela **fixture 4**, que reproduz inteira nos dois métodos. Depois
as demais. **O que não fecha fica DECLARADO aqui, com `skipTest` explicando** —
nunca silenciado, nunca ajustado para caber.

NENHUM `float`. `Decimal` em tudo, e o módulo se auto-varre por AST no fim.
"""

from __future__ import annotations

import ast
import sys
import unittest
from decimal import Decimal, ROUND_DOWN, localcontext
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FRENTE_A = RAIZ / "docs" / "calculo" / "aceitacao" / "frente-a"
if str(FRENTE_A) not in sys.path:
    sys.path.insert(0, str(FRENTE_A))

import metodos  # noqa: E402  — depende do sys.path acima


def D(x):
    return Decimal(str(x))


# ===========================================================================
# 1 — FIXTURE 4 · precatório complementar. Reproduz INTEIRA, nos dois métodos.
# ===========================================================================
#: Coeficientes impressos. Nada aqui é calculado a partir de série.
K_RESUMIDO_ORIGEM = D("1.1883716656")   # jan/2016 → maio/2020  (p. 91)
K_RESUMIDO_PAGTO = D("1.0567647130")    # ago/2018 → maio/2020  (p. 91)
K1 = D("1.0777734324")                  # jan/2016 → jul/2017   (p. 92)
K2 = D("1.0520636054")                  # jul/2017 → jan/2019   (p. 92)
K3 = D("1.0083132766")                  # ago/2018 → jan/2019   (p. 92)
K4 = D("1.0480519672")                  # jan/2019 → maio/2020  (p. 92)


def _linhas_fixture_04():
    """As quatro linhas da tabela da `pagina_pdf` 91."""
    return [
        {"valor": "20000.00", "coeficiente": K_RESUMIDO_ORIGEM,
         "d_pct": D("14.15"), "conta": "principal", "sinal": 1},
        {"valor": "3000.00", "coeficiente": K_RESUMIDO_ORIGEM,
         "so_correcao": True, "conta": "juros", "sinal": 1},
        {"valor": "21000.00", "coeficiente": K_RESUMIDO_PAGTO,
         "d_pct": D("5.15"), "conta": "principal", "sinal": -1},
        {"valor": "3150.00", "coeficiente": K_RESUMIDO_PAGTO,
         "so_correcao": True, "conta": "juros", "sinal": -1},
    ]


def _marcos_fixture_04():
    """Os três passos da `pagina_pdf` 92.

    O bloco de juros leva o COEFICIENTE e NÃO a taxa — INPC e IPCA-E não
    englobam juros de mora. É a célula `(juros cor/mon.)`.
    """
    return [
        {"ate": "2017-07", "coeficiente": K1, "taxa_pct": D("9.00"),
         "taxa_engloba_correcao": False,
         "entradas": [
             {"valor": "20000.00", "coeficiente": K1, "conta": "principal"},
             {"valor": "3000.00", "coeficiente": K1, "conta": "juros"}]},
        {"ate": "2019-01", "coeficiente": K2, "taxa_pct": D("0.00"),
         "taxa_engloba_correcao": False,
         "pagamentos": [
             {"valor": "21000.00", "coeficiente": K3, "conta": "principal"},
             {"valor": "3150.00", "coeficiente": K3, "conta": "juros"}]},
        {"ate": "2020-05", "coeficiente": K4, "taxa_pct": D("5.15"),
         "taxa_engloba_correcao": False},
    ]


class TestFixture04Resumido(unittest.TestCase):
    """`pagina_pdf` 91 — célula por célula."""

    def setUp(self):
        self.r = metodos.resumido(_linhas_fixture_04(), honorarios_pct=D("10"))

    def test_celulas_publicadas(self):
        esperado = [
            # (C publicado, juros publicado, TOTAL publicado)
            ("23767.43", "3363.09", "27130.52"),
            ("3565.11", "0.00", "3565.11"),
            ("22192.05", "1142.89", "23334.94"),
            ("3328.80", "0.00", "3328.80"),
        ]
        for det, (c, j, total) in zip(self.r["detalhe"], esperado):
            self.assertEqual(det["C"], D(c))
            self.assertEqual(det["J"], D(j))
            self.assertEqual(det["L"], D(total))

    def test_subtotais_e_total_da_conta(self):
        self.assertEqual(self.r["subtotal_principal"], D("1575.38"))
        self.assertEqual(self.r["subtotal_juros"], D("2456.51"))
        self.assertEqual(self.r["subtotal"], D("4031.89"))
        self.assertEqual(self.r["honorarios_principal"], D("157.53"))
        self.assertEqual(self.r["honorarios_juros"], D("245.65"))
        self.assertEqual(self.r["total_da_conta"], D("4435.07"))

    def test_pagamento_truncado_no_subtraendo_empurra_para_cima(self):
        """§ 10-A.7, correção 2. `21.000 × 1,0567647130 = 22.192,058973`, e o
        manual publica **22.192,05**: os `0,008973` desprezados estão no
        SUBTRAENDO, e o resumido fica ACIMA do exato."""
        exato = D("21000.00") * K_RESUMIDO_PAGTO
        self.assertEqual(exato, D("22192.058973"))
        self.assertEqual(self.r["detalhe"][2]["C"], D("22192.05"))
        self.assertGreater(self.r["subtotal_principal"],
                           D("20000.00") * K_RESUMIDO_ORIGEM - exato)


class TestFixture04Detalhado(unittest.TestCase):
    """`pagina_pdf` 92 — os três passos, `TOTAL` por `TOTAL`."""

    def setUp(self):
        self.r = metodos.detalhado(_marcos_fixture_04(),
                                   honorarios_pct=D("10"))

    def test_os_tres_passos(self):
        esperado = [
            ("2017-07", "21555.46", "5173.31", "26728.77"),
            ("2019-01", "1503.14", "2266.47", "3769.61"),
            ("2020-05", "1575.36", "2456.50", "4031.86"),
        ]
        for passo, (ate, p, j, t) in zip(self.r["passos"], esperado):
            self.assertEqual(passo["ate"], ate)
            self.assertEqual(passo["principal"], D(p))
            self.assertEqual(passo["juros"], D(j))
            self.assertEqual(passo["total"], D(t))

    def test_primeiro_passo_corrige_os_valores_ORIGINARIOS(self):
        """O 1º passo NÃO recebe os originários pelo nominal: `20.000,00 ×
        1,0777734324 = 21.555,46` e `3.000,00 × 1,0777734324 = 3.233,32`. A
        versão anterior somava nominal e produzia 20.000,00 no principal."""
        self.assertEqual(self.r["passos"][0]["principal"], D("21555.46"))
        self.assertEqual(self.r["passos"][0]["juros"],
                         D("1939.99") + D("3233.32"))

    def test_total_da_conta(self):
        self.assertEqual(self.r["honorarios_principal"], D("157.53"))
        self.assertEqual(self.r["honorarios_juros"], D("245.65"))
        self.assertEqual(self.r["total_da_conta"], D("4435.04"))


class TestFixture04Divergencia(unittest.TestCase):
    """A asserção da fixture 4: R$ 0,03, EXATOS — e os honorários IGUAIS."""

    def test_delta_e_exatamente_tres_centavos(self):
        r = metodos.resumido(_linhas_fixture_04(), honorarios_pct=D("10"))
        d = metodos.detalhado(_marcos_fixture_04(), honorarios_pct=D("10"))
        self.assertEqual(r["total_da_conta"], D("4435.07"))
        self.assertEqual(d["total_da_conta"], D("4435.04"))
        self.assertEqual(r["total_da_conta"] - d["total_da_conta"], D("0.03"))

    def test_honorarios_identicos_isolam_a_divergencia(self):
        r = metodos.resumido(_linhas_fixture_04(), honorarios_pct=D("10"))
        d = metodos.detalhado(_marcos_fixture_04(), honorarios_pct=D("10"))
        self.assertEqual(r["honorarios_total"], d["honorarios_total"])
        self.assertEqual(r["honorarios_total"], D("403.18"))


# ===========================================================================
# 2 — FIXTURE 1 · 4.2.1.1, 1º Exemplo, data-base jun/2022
# ===========================================================================
#: Coeficientes até dez/2021, IMPRESSOS na `pagina_pdf` 51 (e repetidos na 52).
C_JAN2020_ATE_DEZ2021 = D("1.1420100005")
C_FEV2020_ATE_DEZ2021 = D("1.1339588923")
#: Coeficientes até jun/2026, IMPRESSOS na `pagina_pdf` 53.
C_JAN2020_ATE_JUN2026 = D("1.1896586348")
C_FEV2020_ATE_JUN2026 = D("1.1812716064")
C_FEV2022_ATE_JUN2026 = D("1.0417234826")
#: set/2025 → jun/2026, IMPRESSO na `pagina_pdf` 52.
K_SET2025_JUN2026 = D("1.0417234826")


def _marco_a():
    """`a) Atualização dos valores até dez./2021` — comum aos dois Exemplos.

    Coeficiente **POR PARCELA** e truncamento **POR LINHA**. `TestMarcoA`
    prova que sobre o agregado o número é outro.
    """
    return {"ate": "2021-12", "entradas": [
        {"valor": "1000.00", "coeficiente": C_JAN2020_ATE_DEZ2021,
         "taxa_pct": D("2.45")},
        {"valor": "1000.00", "coeficiente": C_FEV2020_ATE_DEZ2021,
         "taxa_pct": D("2.45")}]}


class TestMarcoA(unittest.TestCase):
    """O marco `a)` das `pagina_pdf` 51 e 52 — e por que o coeficiente NÃO
    pode ser um só por marco."""

    def test_celulas(self):
        r = metodos.detalhado([_marco_a()])
        p = r["passos"][0]
        self.assertEqual(p["principal"], D("2275.96"))
        self.assertEqual(p["juros"], D("55.75"))
        self.assertEqual(p["total"], D("2331.71"))

    def test_por_linha_da_5575_e_sobre_o_agregado_daria_5576(self):
        """`27,97 + 27,78 = 55,75`. Um coeficiente só sobre o agregado daria
        `2.275,96 × 2,45% = 55,76102 → 55,76`, e o manual publica **55,75**.
        É a refutação medida da regra antiga."""
        por_linha = (D("1142.01") * D("2.45") / D("100")).quantize(
            D("0.01"), rounding=ROUND_DOWN) + (
            D("1133.95") * D("2.45") / D("100")).quantize(
            D("0.01"), rounding=ROUND_DOWN)
        sobre_agregado = (D("2275.96") * D("2.45") / D("100")).quantize(
            D("0.01"), rounding=ROUND_DOWN)
        self.assertEqual(por_linha, D("55.75"))
        self.assertEqual(sobre_agregado, D("55.76"))
        self.assertNotEqual(por_linha, sobre_agregado)


class TestFixture01(unittest.TestCase):
    """1º Exemplo — os dois métodos convergem em **3.484,95**
    (`tolerancia 0,00`; o manual não registra divergência)."""

    def test_detalhado_pagina_51(self):
        r = metodos.detalhado([
            _marco_a(),
            {"ate": "2022-06", "taxa_pct": D("5.05"),
             "taxa_engloba_correcao": True,
             "entradas": [{"valor": "1000.00", "taxa_pct": D("3.55")}]},
        ])
        b = r["passos"][1]
        self.assertEqual(b["principal"], D("3275.96"))
        self.assertEqual(b["juros"], D("208.99"))     # 55,75 + 153,24
        self.assertEqual(r["total_da_conta"], D("3484.95"))

    def test_resumido_pagina_52(self):
        """Legenda da p. 52: `(F) = C x D%` · `(G) = (C + F) x E%` ·
        `(H) = F + G` · `(I) = C + H`. Três colunas de taxa não existem aqui."""
        linhas = [
            {"valor": "1000.00", "coeficiente": C_JAN2020_ATE_DEZ2021,
             "d_pct": D("2.45"), "e_pct": D("5.05")},
            {"valor": "1000.00", "coeficiente": C_FEV2020_ATE_DEZ2021,
             "d_pct": D("2.45"), "e_pct": D("5.05")},
            {"valor": "1000.00", "coeficiente": D("1.0000000000"),
             "e_pct": D("3.55")},
        ]
        r = metodos.resumido(linhas)
        esperado = [("1142.01", "27.97", "59.08", "1229.06"),
                    ("1133.95", "27.78", "58.66", "1220.39"),
                    ("1000.00", "0.00", "35.50", "1035.50")]
        for det, (c, g, h, l) in zip(r["detalhe"], esperado):
            self.assertEqual(det["C"], D(c))
            self.assertEqual(det["G"], D(g))
            self.assertEqual(det["H"], D(h))
            self.assertEqual(det["L"], D(l))
        self.assertEqual(r["subtotal_principal"], D("3275.96"))
        self.assertEqual(r["subtotal_juros"], D("208.99"))
        self.assertEqual(r["total_da_conta"], D("3484.95"))

    def test_os_dois_convergem(self):
        det = metodos.detalhado([
            _marco_a(),
            {"ate": "2022-06", "taxa_pct": D("5.05"),
             "taxa_engloba_correcao": True,
             "entradas": [{"valor": "1000.00", "taxa_pct": D("3.55")}]}])
        res = metodos.resumido([
            {"valor": "1000.00", "coeficiente": C_JAN2020_ATE_DEZ2021,
             "d_pct": D("2.45"), "e_pct": D("5.05")},
            {"valor": "1000.00", "coeficiente": C_FEV2020_ATE_DEZ2021,
             "d_pct": D("2.45"), "e_pct": D("5.05")},
            {"valor": "1000.00", "coeficiente": D("1.0000000000"),
             "e_pct": D("3.55")}])
        self.assertEqual(det["total_da_conta"], res["total_da_conta"])
        self.assertEqual(det["total_da_conta"], D("3484.95"))


# ===========================================================================
# 3 — FIXTURE 2 · 4.2.1.1, 2º Exemplo, data-base jun/2026. Δ = R$ 0,01
# ===========================================================================
def _marcos_fixture_02():
    return [
        _marco_a(),
        # b) de dez./2021 até set./2025 — SELIC. Engloba correção: a taxa é a
        #    ÚNICA correção que o bloco de juros recebe neste trecho, e por
        #    isso incide sobre ele (55,75 × 43,89% = 24,46, p. 52).
        #    DUAS taxas no mesmo marco: 43,89% no agregado, 42,39% em fev/2022.
        {"ate": "2025-09", "taxa_pct": D("43.89"),
         "taxa_engloba_correcao": True,
         "entradas": [{"valor": "1000.00", "taxa_pct": D("42.39")}]},
        # c) de set./2025 a jun./2026 — IPCA-15 + taxa legal. NÃO engloba: o
        #    bloco de juros leva o COEFICIENTE e não a taxa.
        {"ate": "2026-06", "coeficiente": K_SET2025_JUN2026,
         "taxa_pct": D("7.03"), "taxa_engloba_correcao": False},
    ]


def _linhas_fixture_02():
    return [
        {"valor": "1000.00", "coeficiente": C_JAN2020_ATE_JUN2026,
         "d_pct": D("2.45"), "e_pct": D("43.89"), "f_pct": D("7.03")},
        {"valor": "1000.00", "coeficiente": C_FEV2020_ATE_JUN2026,
         "d_pct": D("2.45"), "e_pct": D("43.89"), "f_pct": D("7.03")},
        {"valor": "1000.00", "coeficiente": C_FEV2022_ATE_JUN2026,
         "e_pct": D("42.39"), "f_pct": D("7.03")},
    ]


class TestFixture02Detalhado(unittest.TestCase):
    """`pagina_pdf` 52 — as três sub-tabelas."""

    def setUp(self):
        self.r = metodos.detalhado(_marcos_fixture_02())

    def test_os_tres_marcos(self):
        esperado = [("2275.96", "55.75", "2331.71"),
                    ("3275.96", "1503.02", "4778.98"),
                    ("3412.64", "1805.63", "5218.27")]
        for passo, (p, j, t) in zip(self.r["passos"], esperado):
            self.assertEqual(passo["principal"], D(p))
            self.assertEqual(passo["juros"], D(j))
            self.assertEqual(passo["total"], D(t))

    def test_a_celula_que_a_regra_antiga_proibia(self):
        """`Dez./2021 · R$ 55,75 · (juros) · 43,89 · R$ 24,46 · R$ 80,21`
        (`pagina_pdf` 52). A § 10-A.8 do consolidado já a listava como prova
        de truncamento (`24,468675 → 24,46`, half-up daria 24,47) — e a `T3`
        dizia, ao mesmo tempo, que ela não existe."""
        celula = (D("55.75") * D("43.89") / D("100"))
        self.assertEqual(celula, D("24.468675"))
        self.assertEqual(celula.quantize(D("0.01"), rounding=ROUND_DOWN),
                         D("24.46"))
        # 55,75 + 998,91 + 24,46 + 423,90 = 1.503,02
        self.assertEqual(self.r["passos"][1]["juros"],
                         D("55.75") + D("998.91") + D("24.46") + D("423.90"))

    def test_duas_taxas_no_mesmo_marco(self):
        """43,89% no agregado de dez/2021 E 42,39% na parcela de fev/2022,
        simultaneamente. Uma `taxa_pct` por marco não expressa isto."""
        self.assertEqual((D("2275.96") * D("43.89") / D("100")).quantize(
            D("0.01"), rounding=ROUND_DOWN), D("998.91"))
        self.assertEqual((D("1000.00") * D("42.39") / D("100")).quantize(
            D("0.01"), rounding=ROUND_DOWN), D("423.90"))

    def test_bloco_de_juros_leva_coeficiente_e_nao_taxa_no_marco_c(self):
        """`Set./2025 (A + C) · R$ 1.503,02 · 1,0417234826 · (juros correção
        monetária) · R$ 1.565,73` — sem coluna `% Juros`. É a mesma assimetria
        que a legenda do resumido imprime: `(H) = (C + G) × E%` contra
        `(I) = C × F%`."""
        self.assertEqual((D("1503.02") * K_SET2025_JUN2026).quantize(
            D("0.01"), rounding=ROUND_DOWN), D("1565.73"))
        self.assertEqual(self.r["passos"][2]["juros"],
                         D("1565.73") + D("239.90"))

    def test_total_5218_27(self):
        self.assertEqual(self.r["total_da_conta"], D("5218.27"))


class TestFixture02Resumido(unittest.TestCase):
    """`pagina_pdf` 53 — a legenda de 11 colunas, e só ela."""

    def setUp(self):
        self.r = metodos.resumido(_linhas_fixture_02())

    def test_celulas_publicadas(self):
        esperado = [("1189.65", "29.14", "534.92", "83.63", "647.69", "1837.34"),
                    ("1181.27", "28.94", "531.16", "83.04", "643.14", "1824.41"),
                    ("1041.72", "0.00", "441.58", "73.23", "514.81", "1556.53")]
        for det, (c, g, h, i, j, l) in zip(self.r["detalhe"], esperado):
            self.assertEqual(det["C"], D(c))
            self.assertEqual(det["G"], D(g))
            self.assertEqual(det["H"], D(h))
            self.assertEqual(det["I"], D(i))
            self.assertEqual(det["J"], D(j))
            self.assertEqual(det["L"], D(l))

    def test_total_5218_28(self):
        self.assertEqual(self.r["subtotal_principal"], D("3412.64"))
        self.assertEqual(self.r["total_da_conta"], D("5218.28"))


class TestFixture02Divergencia(unittest.TestCase):
    def test_delta_e_exatamente_um_centavo(self):
        res = metodos.resumido(_linhas_fixture_02())
        det = metodos.detalhado(_marcos_fixture_02())
        self.assertEqual(res["total_da_conta"], D("5218.28"))
        self.assertEqual(det["total_da_conta"], D("5218.27"))
        self.assertEqual(res["total_da_conta"] - det["total_da_conta"],
                         D("0.01"))

    def test_principal_e_taxa_pos_set2025_sao_IGUAIS_nos_dois(self):
        """A divergência está ISOLADA no bloco de juros."""
        res = metodos.resumido(_linhas_fixture_02())
        det = metodos.detalhado(_marcos_fixture_02())
        self.assertEqual(res["subtotal_principal"], D("3412.64"))
        self.assertEqual(det["subtotal_principal"], D("3412.64"))
        self.assertEqual(res["subtotal_juros"] - det["subtotal_juros"],
                         D("0.01"))


# ===========================================================================
# 4 — A HIPÓTESE DO TRUNCAMENTO, e a correção da EVIDÊNCIA da § 10-A.5
# ===========================================================================
class TestComutatividade(unittest.TestCase):
    """A tese da § 10-A.5 é VERDADEIRA; a evidência que ela imprimia, não.

    `564.08027018950592144500596500` e `560.10353505864666529780513900` não
    são "os dois lados" — são **jan/2020 e fev/2020**, duas parcelas. O que
    prova comutatividade é cada número ser igual **em si mesmo** dos dois
    lados, e é isto que este teste mede: parcela por parcela.
    """

    FATOR_JUROS = D("0.0245") + (D("1") + D("0.0245")) * D("0.4389")

    def test_cada_parcela_e_identica_dos_dois_lados(self):
        with localcontext() as ctx:
            ctx.prec = 60
            for coef, esperado in (
                (C_JAN2020_ATE_DEZ2021, "564.08027018950592144500596500"),
                (C_FEV2020_ATE_DEZ2021, "560.10353505864666529780513900"),
            ):
                resumido = (D("1000") * coef * K_SET2025_JUN2026
                            * self.FATOR_JUROS)
                detalhado = (D("1000") * coef * self.FATOR_JUROS
                             * K_SET2025_JUN2026)
                self.assertEqual(resumido, detalhado)
                self.assertEqual(resumido, D(esperado))

    def test_os_dois_numeros_sao_parcelas_diferentes_e_NAO_os_dois_lados(self):
        self.assertNotEqual(D("564.08027018950592144500596500"),
                            D("560.10353505864666529780513900"))

    def test_sem_truncamento_os_dois_metodos_convergem(self):
        """Por isso o truncamento por etapa é OBRIGATÓRIO: rodar em precisão
        plena ZERA a divergência que as fixtures asseveram."""
        with localcontext() as ctx:
            ctx.prec = 60
            soma = sum((D("1000") * c * K_SET2025_JUN2026 * self.FATOR_JUROS)
                       for c in (C_JAN2020_ATE_DEZ2021,
                                 C_FEV2020_ATE_DEZ2021))
            self.assertGreater(soma, D("1124"))


class TestCoeficientesCompostos(unittest.TestCase):
    """LEVE — o décimo dígito de `k1 × k2 × k4`, registrado e não resolvido."""

    def test_k3_k4_trunca_exato(self):
        with localcontext() as ctx:
            ctx.prec = 60
            self.assertEqual((K3 * K4).quantize(D("1E-10"),
                                                rounding=ROUND_DOWN),
                             K_RESUMIDO_PAGTO)

    def test_k1_k2_k4_NAO_reproduz_o_decimo_digito_publicado(self):
        """`k1 × k2 × k4 = 1,188371665734…`; truncado a 10 casas dá
        **1,1883716657** e o manual publica **1,1883716656**. Half-up daria o
        mesmo `…657`: **nenhum critério de arredondamento produz o `…656`**.

        Logo o publicado NÃO é o produto dos três coeficientes publicados —
        ou o original tem defeito, ou os coeficientes intermediários das pp. 91
        e 92 não são truncamentos exatos da mesma cadeia mensal. **Não é
        decidível pelo que o manual imprime, e fica declarado.**

        Consequência medida: NENHUMA. `1 × 10⁻¹⁰` sobre R$ 20.000,00 vale
        `R$ 0,000002`, **oito ordens de grandeza abaixo do centavo** — a
        § 10-A.6 já media 7 × 10⁻⁷ no resultado e concluía o mesmo.
        """
        with localcontext() as ctx:
            ctx.prec = 60
            exato = K1 * K2 * K4
            truncado = exato.quantize(D("1E-10"), rounding=ROUND_DOWN)
            self.assertEqual(truncado, D("1.1883716657"))
            self.assertNotEqual(truncado, K_RESUMIDO_ORIGEM)
            self.assertEqual(truncado - K_RESUMIDO_ORIGEM, D("1E-10"))
            self.assertLess((exato - K_RESUMIDO_ORIGEM) * D("20000"),
                            D("0.01"))


# ===========================================================================
# 5 — O QUE **NÃO** FECHA. Declarado, com a razão. Nunca silenciado.
# ===========================================================================
class TestLimitesDeclarados(unittest.TestCase):

    def test_rotulo_do_corte_de_dez2021_nao_sai_da_cadeia(self):
        self.skipTest(
            "NÃO FECHA, e não é série. O manual intitula o marco "
            "'a) até dez./2021' e a cadeia de fazenda-pública encerra o regime "
            "anterior em nov/2021 (SELIC entra em 2021-12). O runner deriva o "
            "corte da MUDANÇA DE REGIME e rotula 2021-11. Reconciliar exige "
            "decidir a ORDEM entre o índice de nov/2021 (1,17%) e os 0,4412% "
            "de dez/2021 sobre que base — que é a LACUNA #3 do registro, e o "
            "corpus não a resolve. Este teste reproduz os totais a partir dos "
            "coeficientes IMPRESSOS até dez/2021, e por isso não depende do "
            "rótulo; o runner depende, e fica bloqueado também por isto.")

    def test_coeficiente_a_partir_da_serie_mensal(self):
        self.skipTest(
            "NÃO FECHA por falta da camada (B), por desenho declarado. Este "
            "arquivo consome os coeficientes IMPRESSOS (10 casas); reproduzir "
            "o próprio coeficiente a partir dos índices mensais exigiria série, "
            "que nenhuma skill carrega. É o bloqueio das 4 fixtures no runner.")

    def test_fixture_03_um_metodo_so(self):
        self.skipTest(
            "A fixture 3 (`pagina_pdf` 53, devedor não-Fazenda) tem UMA tabela "
            "e UM percentual agregado por parcela (209,65% e 14,57%), ambos "
            "produto da série. O manual não publica a decomposição, logo não "
            "há procedimento a confrontar aqui — só a montagem, que o runner "
            "já verifica e declara CIRCULAR.")


# ===========================================================================
# 6 — R12: nenhum float neste arquivo
# ===========================================================================
class TestSemFloat(unittest.TestCase):

    def test_o_proprio_arquivo_nao_tem_literal_float(self):
        arvore = ast.parse(Path(__file__).read_text(encoding="utf-8"))
        achados = [no.value for no in ast.walk(arvore)
                   if isinstance(no, ast.Constant)
                   and isinstance(no.value, float)]
        self.assertEqual(achados, [])

    def test_metodos_py_nao_tem_literal_float(self):
        arvore = ast.parse((FRENTE_A / "metodos.py").read_text(
            encoding="utf-8"))
        achados = [no.value for no in ast.walk(arvore)
                   if isinstance(no, ast.Constant)
                   and isinstance(no.value, float)]
        self.assertEqual(achados, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
