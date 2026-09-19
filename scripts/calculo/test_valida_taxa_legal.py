"""Testes de valida_taxa_legal.py — R6, R11 e R12.

Inclui os casos NEGATIVOS que dão sentido ao validador: half-up deve falhar,
subtração literal deve falhar, float deve ser recusado.
"""

from __future__ import annotations

import ast
import json
import os
import pathlib
import tempfile
import unittest
from decimal import Decimal, ROUND_HALF_UP, localcontext

from valida_taxa_legal import (
    PARES_VALIDACAO_INPC,
    SEIS_DECIMAIS,
    Deflator,
    carrega_fatores,
    taxa_legal,
    taxa_legal_por_subtracao,
    verifica_pares_validacao,
)


class TestParesDeValidacao(unittest.TestCase):
    """Seção 4 da base normativa — taxa legal previdenciária, deflator INPC."""

    def test_set_2025(self):
        self.assertEqual(
            taxa_legal(Decimal("1.01164156"), Decimal("0.9979"), Deflator.INPC),
            Decimal("1.377047"),
        )

    def test_mai_2026(self):
        self.assertEqual(
            taxa_legal(Decimal("1.01090058"), Decimal("1.0081"), Deflator.INPC),
            Decimal("0.277807"),
        )

    def test_helper_nao_reporta_falhas(self):
        self.assertEqual(verifica_pares_validacao(), [])

    def test_ambos_os_pares_sao_do_caso_inpc(self):
        """Guarda contra alguém reclassificar os pares como IPCA-15."""
        self.assertEqual(len(PARES_VALIDACAO_INPC), 2)
        for par in PARES_VALIDACAO_INPC:
            obtido = taxa_legal(par["fator_selic"], par["fator_deflator"], Deflator.INPC)
            self.assertEqual(obtido, par["esperado"], par["rotulo"])


class TestTruncamentoVersusArredondamento(unittest.TestCase):
    """R12 — os pares publicados SÓ fecham com truncamento."""

    def _half_up(self, selic, defl):
        with localcontext() as ctx:
            ctx.prec = 40
            exato = (Decimal(selic) / Decimal(defl) - 1) * 100
        return exato.quantize(SEIS_DECIMAIS, rounding=ROUND_HALF_UP)

    def test_half_up_diverge_em_set_2025(self):
        obtido = self._half_up("1.01164156", "0.9979")
        self.assertEqual(obtido, Decimal("1.377048"))
        self.assertNotEqual(obtido, Decimal("1.377047"))

    def test_half_up_diverge_em_mai_2026(self):
        obtido = self._half_up("1.01090058", "1.0081")
        self.assertEqual(obtido, Decimal("0.277808"))
        self.assertNotEqual(obtido, Decimal("0.277807"))

    def test_half_up_falharia_nos_dois_pares(self):
        """Se alguém trocar ROUND_DOWN por half-up, os dois pares quebram."""
        for par in PARES_VALIDACAO_INPC:
            with self.subTest(par=par["rotulo"]):
                self.assertNotEqual(
                    self._half_up(par["fator_selic"], par["fator_deflator"]),
                    par["esperado"],
                )

    def test_truncamento_nao_arredonda_para_cima(self):
        # 1.0000005 → exatamente 0.00005% na 7ª casa; truncar não promove a 6ª.
        self.assertEqual(taxa_legal(Decimal("1.00000059"), Decimal("1")), Decimal("0.000059"))


class TestSubtracaoLiteralFalha(unittest.TestCase):
    """R11 — a operação é razão entre fatores, nunca subtração de percentuais."""

    def test_subtracao_reproduz_os_valores_erroneos_documentados(self):
        self.assertEqual(
            taxa_legal_por_subtracao(Decimal("1.01164156"), Decimal("0.9979")),
            Decimal("1.374156"),
        )
        self.assertEqual(
            taxa_legal_por_subtracao(Decimal("1.01090058"), Decimal("1.0081")),
            Decimal("0.280058"),
        )

    def test_subtracao_diverge_do_manual_nos_dois_pares(self):
        for par in PARES_VALIDACAO_INPC:
            with self.subTest(par=par["rotulo"]):
                errado = taxa_legal_por_subtracao(par["fator_selic"], par["fator_deflator"])
                self.assertEqual(errado, par["subtracao_erronea"])
                self.assertNotEqual(errado, par["esperado"])

    def test_divergencia_e_da_ordem_de_tres_milesimos_de_pp(self):
        """~0,003 p.p./mês, conforme a seção 4. Acumula."""
        for par in PARES_VALIDACAO_INPC:
            with self.subTest(par=par["rotulo"]):
                delta = abs(
                    taxa_legal(par["fator_selic"], par["fator_deflator"], Deflator.INPC)
                    - taxa_legal_por_subtracao(par["fator_selic"], par["fator_deflator"])
                )
                self.assertGreater(delta, Decimal("0.0005"))
                self.assertLess(delta, Decimal("0.005"))


class TestPisoZero(unittest.TestCase):
    """R6 — resultado negativo vira zero, nunca negativo (CC art. 406, § 3º)."""

    def test_deflator_maior_que_selic_resulta_zero(self):
        self.assertEqual(taxa_legal(Decimal("1.001"), Decimal("1.010")), Decimal("0.000000"))

    def test_resultado_zero_e_admitido(self):
        self.assertEqual(taxa_legal(Decimal("1.0"), Decimal("1.0")), Decimal("0.000000"))

    def test_nunca_retorna_negativo(self):
        for selic, defl in [("1.00", "1.50"), ("0.99", "1.01"), ("1.000001", "1.2")]:
            with self.subTest(selic=selic):
                self.assertGreaterEqual(taxa_legal(Decimal(selic), Decimal(defl)), 0)

    def test_piso_zero_tem_seis_casas(self):
        self.assertEqual(taxa_legal(Decimal("1.0"), Decimal("1.5")).as_tuple().exponent, -6)


class TestProibicaoDeFloat(unittest.TestCase):
    """R12 — nenhum float em nenhum caminho."""

    def test_float_na_selic_e_recusado(self):
        with self.assertRaises(TypeError) as ctx:
            taxa_legal(1.01164156, Decimal("0.9979"))
        self.assertIn("float", str(ctx.exception))

    def test_float_no_deflator_e_recusado(self):
        with self.assertRaises(TypeError):
            taxa_legal(Decimal("1.01164156"), 0.9979)

    def test_str_e_int_sao_aceitos(self):
        self.assertEqual(
            taxa_legal("1.01164156", "0.9979", Deflator.INPC), Decimal("1.377047")
        )
        self.assertEqual(taxa_legal(1, 1), Decimal("0.000000"))

    def test_resultado_e_sempre_decimal(self):
        self.assertIsInstance(taxa_legal(Decimal("1.01"), Decimal("1.00")), Decimal)

    def test_codigo_fonte_nao_contem_literal_float(self):
        """Varre a AST dos dois validadores atrás de constantes float."""
        base = pathlib.Path(__file__).parent
        for nome in ("valida_taxa_legal.py", "valida_cobertura.py"):
            caminho = base / nome
            with open(caminho, "r", encoding="utf-8") as fh:
                arvore = ast.parse(fh.read(), filename=str(caminho))
            floats = [
                no for no in ast.walk(arvore)
                if isinstance(no, ast.Constant) and isinstance(no.value, float)
            ]
            with self.subTest(arquivo=nome):
                self.assertEqual(
                    floats, [], f"{nome} contém literal float na(s) linha(s) "
                    f"{[n.lineno for n in floats]}"
                )


class TestValidacaoDeEntrada(unittest.TestCase):
    def test_deflator_zero_ou_negativo(self):
        for ruim in ("0", "-1.01"):
            with self.subTest(ruim=ruim):
                with self.assertRaises(ValueError):
                    taxa_legal(Decimal("1.01"), Decimal(ruim))

    def test_selic_zero_ou_negativa(self):
        with self.assertRaises(ValueError):
            taxa_legal(Decimal("0"), Decimal("1.01"))

    def test_tipo_nao_suportado(self):
        with self.assertRaises(TypeError):
            taxa_legal(None, Decimal("1.0"))


class TestDeflatorParametrico(unittest.TestCase):
    """O deflator muda por ramo, não por preferência."""

    def test_os_dois_deflatores_existem(self):
        self.assertEqual(Deflator.IPCA15.value, "IPCA-15")
        self.assertEqual(Deflator.INPC.value, "INPC")

    def test_padrao_e_ipca15(self):
        self.assertEqual(
            taxa_legal(Decimal("1.01164156"), Decimal("0.9979")),
            taxa_legal(Decimal("1.01164156"), Decimal("0.9979"), Deflator.IPCA15),
        )

    def test_deflator_nao_altera_aritmetica_so_a_semantica(self):
        """Mesmos fatores, deflatores distintos → mesmo número.

        A escolha do deflator determina QUAL série alimenta `fator_deflator`;
        não muda a fórmula. Guarda contra alguém ramificar a aritmética por índice.
        """
        self.assertEqual(
            taxa_legal(Decimal("1.01"), Decimal("1.00"), Deflator.IPCA15),
            taxa_legal(Decimal("1.01"), Decimal("1.00"), Deflator.INPC),
        )

    def test_cada_deflator_declara_fundamento(self):
        self.assertIn("5.171", Deflator.IPCA15.fundamento)
        self.assertIn("990/2026", Deflator.INPC.fundamento)


class TestCarregamentoArquivo(unittest.TestCase):
    def test_le_json_utf8_sem_produzir_float(self):
        conteudo = {
            "fatores": [
                {
                    "competencia": "2025-09",
                    "fator_selic": "1.01164156",
                    "fator_deflator": "0.9979",
                    "nota": "competência de referência — dedução do INPC",
                }
            ]
        }
        caminho = os.path.join(tempfile.mkdtemp(), "fatores.json")
        with open(caminho, "w", encoding="utf-8") as fh:
            json.dump(conteudo, fh, ensure_ascii=False)

        fatores = carrega_fatores(caminho)
        self.assertEqual(len(fatores), 1)
        self.assertIn("competência", fatores[0]["nota"])
        self.assertEqual(
            taxa_legal(fatores[0]["fator_selic"], fatores[0]["fator_deflator"], Deflator.INPC),
            Decimal("1.377047"),
        )

    def test_numero_solto_no_json_vira_decimal_nao_float(self):
        caminho = os.path.join(tempfile.mkdtemp(), "fatores2.json")
        with open(caminho, "w", encoding="utf-8") as fh:
            fh.write('{"fatores": [{"fator_selic": 1.01164156, "fator_deflator": 0.9979}]}')
        fatores = carrega_fatores(caminho)
        self.assertIsInstance(fatores[0]["fator_selic"], Decimal)
        self.assertNotIsInstance(fatores[0]["fator_selic"], float)


if __name__ == "__main__":
    unittest.main(verbosity=2)
