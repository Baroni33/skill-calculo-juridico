"""Testes de valida_cobertura.py — invariantes R1 e R2."""

from __future__ import annotations

import json
import os
import tempfile
import unittest

from valida_cobertura import (
    Segmento,
    carrega_segmentos,
    competencia_para_indice,
    indice_para_competencia,
    valida_cobertura,
)

CM = "correcao-monetaria"
JM = "juros-mora"


def seg(inicio, fim, componente, engloba=(), condicao=None, id=None):
    return Segmento(
        inicio=inicio,
        fim=fim,
        componente=componente,
        engloba=tuple(engloba),
        condicao=tuple(sorted((k, v) for k, v in (condicao or {}).items())),
        id=id or f"{componente}:{inicio}..{fim}",
    )


class TestAritmeticaCompetencia(unittest.TestCase):
    def test_ida_e_volta(self):
        for c in ("2020-01", "2021-12", "1996-06", "2026-05"):
            self.assertEqual(indice_para_competencia(competencia_para_indice(c)), c)

    def test_meses_consecutivos_diferem_de_um(self):
        self.assertEqual(
            competencia_para_indice("2022-01") - competencia_para_indice("2021-12"), 1
        )

    def test_rejeita_formato_invalido(self):
        for ruim in ("2020-1", "2020/01", "20-01", "2020-13", "abc", "2020-00"):
            with self.subTest(ruim=ruim):
                with self.assertRaises(ValueError):
                    competencia_para_indice(ruim)

    def test_rejeita_nao_string(self):
        with self.assertRaises(TypeError):
            competencia_para_indice(202001)

    def test_rejeita_inicio_posterior_ao_fim(self):
        with self.assertRaises(ValueError):
            Segmento.de_dict({"inicio": "2022-05", "fim": "2022-01", "componente": CM})


class TestR2Cobertura(unittest.TestCase):
    def test_cobertura_valida_sem_violacao(self):
        r = valida_cobertura(
            [seg("2020-01", "2021-11", CM), seg("2021-12", "2024-08", CM)],
            inicio="2020-01",
            fim="2024-08",
        )
        self.assertTrue(r.ok, str(r))

    def test_fronteiras_adjacentes_nao_sao_sobreposicao(self):
        """fim de um = mês imediatamente anterior ao início do próximo."""
        r = valida_cobertura(
            [seg("2021-01", "2021-12", CM), seg("2022-01", "2022-12", CM)],
            inicio="2021-01",
            fim="2022-12",
        )
        self.assertTrue(r.ok, str(r))

    def test_lacuna_de_um_mes(self):
        r = valida_cobertura(
            [seg("2020-01", "2021-11", CM), seg("2022-01", "2024-08", CM)],
            inicio="2020-01",
            fim="2024-08",
        )
        self.assertFalse(r.ok)
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1)
        self.assertEqual(lacunas[0].inicio, "2021-12")
        self.assertEqual(lacunas[0].fim, "2021-12")

    def test_lacuna_de_varios_meses_colapsa_em_um_intervalo(self):
        r = valida_cobertura(
            [seg("2020-01", "2020-06", CM), seg("2021-01", "2021-12", CM)],
            inicio="2020-01",
            fim="2021-12",
        )
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1)
        self.assertEqual((lacunas[0].inicio, lacunas[0].fim), ("2020-07", "2020-12"))

    def test_sobreposicao_de_um_mes(self):
        r = valida_cobertura(
            [seg("2020-01", "2021-12", CM), seg("2021-12", "2024-08", CM)],
            inicio="2020-01",
            fim="2024-08",
        )
        self.assertFalse(r.ok)
        sobr = [v for v in r.por_regra("R2") if "sobreposição" in v.mensagem]
        self.assertEqual(len(sobr), 1)
        self.assertEqual((sobr[0].inicio, sobr[0].fim), ("2021-12", "2021-12"))
        self.assertEqual(len(sobr[0].segmentos), 2)

    def test_lacuna_na_borda_final_ate_a_data_base(self):
        """A união deve cobrir até a data-base, não apenas até o último segmento."""
        r = valida_cobertura([seg("2020-01", "2024-08", CM)], inicio="2020-01", fim="2026-06")
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1)
        self.assertEqual((lacunas[0].inicio, lacunas[0].fim), ("2024-09", "2026-06"))

    def test_janela_inferida_nao_inventa_lacuna_de_borda(self):
        r = valida_cobertura([seg("2020-01", "2024-08", CM)])
        self.assertTrue(r.ok, str(r))


class TestR1Englobamento(unittest.TestCase):
    def test_selic_englobando_com_juros_concorrente(self):
        """SELIC engloba correção e juros; segmento de juros no mesmo intervalo viola R1."""
        r = valida_cobertura(
            [
                seg("2021-12", "2024-08", CM, engloba=[CM, JM], id="SELIC"),
                seg("2021-12", "2024-08", JM, id="juros-1pct"),
            ],
            inicio="2021-12",
            fim="2024-08",
        )
        self.assertFalse(r.ok)
        r1 = r.por_regra("R1")
        self.assertTrue(r1, f"esperava violação de R1, veio: {r}")
        self.assertEqual(r1[0].componente, JM)
        self.assertEqual((r1[0].inicio, r1[0].fim), ("2021-12", "2024-08"))
        self.assertIn("SELIC", r1[0].segmentos)
        self.assertIn("juros-1pct", r1[0].segmentos)

    def test_taxa_legal_englobando_com_juros_concorrente(self):
        r = valida_cobertura(
            [
                seg("2024-09", "2026-06", JM, engloba=[JM], id="taxa-legal"),
                seg("2025-01", "2025-06", JM, id="juros-extra"),
            ],
            inicio="2024-09",
            fim="2026-06",
        )
        r1 = r.por_regra("R1")
        self.assertTrue(r1)
        self.assertEqual((r1[0].inicio, r1[0].fim), ("2025-01", "2025-06"))

    def test_selic_sozinha_cobre_ambos_sem_violacao(self):
        """A SELIC englobando os dois componentes satisfaz R2 sem violar R1."""
        r = valida_cobertura(
            [seg("2021-12", "2024-08", CM, engloba=[CM, JM], id="SELIC")],
            inicio="2021-12",
            fim="2024-08",
        )
        self.assertTrue(r.ok, str(r))

    def test_englobamento_fora_do_intervalo_nao_viola(self):
        r = valida_cobertura(
            [
                seg("2021-12", "2024-08", CM, engloba=[CM, JM], id="SELIC"),
                seg("2024-09", "2026-06", JM, id="taxa-legal"),
                seg("2024-09", "2026-06", CM, id="IPCA"),
            ],
            inicio="2021-12",
            fim="2026-06",
        )
        self.assertTrue(r.ok, str(r))


class TestCondicoesBifurcadas(unittest.TestCase):
    def test_ramos_com_condicao_distinta_nao_colidem(self):
        """Fazenda Pública e privado cobrem o mesmo período sem sobreposição."""
        r = valida_cobertura(
            [
                seg("2021-12", "2024-08", CM, condicao={"devedor": "fazenda-publica"}, id="FP"),
                seg("2021-12", "2024-08", CM, condicao={"devedor": "privado"}, id="PRIV"),
            ],
            inicio="2021-12",
            fim="2024-08",
        )
        self.assertTrue(r.ok, str(r))

    def test_lacuna_dentro_de_um_ramo_e_reportada_com_a_condicao(self):
        r = valida_cobertura(
            [
                seg("2021-12", "2022-06", CM, condicao={"devedor": "fazenda-publica"}, id="FP-a"),
                seg("2022-08", "2024-08", CM, condicao={"devedor": "fazenda-publica"}, id="FP-b"),
                seg("2021-12", "2024-08", CM, condicao={"devedor": "privado"}, id="PRIV"),
            ],
            inicio="2021-12",
            fim="2024-08",
        )
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1)
        self.assertEqual((lacunas[0].inicio, lacunas[0].fim), ("2022-07", "2022-07"))
        self.assertIn("fazenda-publica", lacunas[0].condicao)


class TestCadeiaRealTrabalhista(unittest.TestCase):
    """Cadeia trabalhista privada da seção 1 da base normativa."""

    def cadeia(self):
        return [
            seg("2018-01", "2021-11", CM, id="IPCA-E-prejudicial"),
            seg("2018-01", "2021-11", JM, id="TRD-art39"),
            seg("2021-12", "2024-08", CM, engloba=[CM, JM], id="SELIC"),
            seg("2024-09", "2026-06", CM, id="IPCA"),
            seg("2024-09", "2026-06", JM, id="taxa-legal"),
        ]

    def test_cadeia_integra(self):
        r = valida_cobertura(self.cadeia(), inicio="2018-01", fim="2026-06")
        self.assertTrue(r.ok, str(r))

    def test_cumular_ipca_sobre_selic_viola_R1(self):
        cadeia = self.cadeia()
        cadeia.append(seg("2021-12", "2024-08", CM, id="IPCA-indevido"))
        r = valida_cobertura(cadeia, inicio="2018-01", fim="2026-06")
        self.assertFalse(r.ok)
        self.assertTrue(r.por_regra("R1"), f"esperava R1, veio: {r}")


class TestCarregamentoArquivo(unittest.TestCase):
    def test_le_json_utf8_com_acentuacao(self):
        tabela = {
            "id": "trt3.trabalhista.correcao-monetaria.privado",
            "segmentos": [
                {
                    "inicio": "2021-12",
                    "fim": "2024-08",
                    "componente": CM,
                    "indexador": "SELIC",
                    "engloba": [CM, JM],
                    "condicao": {"devedor": "fazenda-pública"},
                    "fundamento": "EC 113/2021, art. 3º — atualização monetária",
                }
            ],
        }
        caminho = os.path.join(tempfile.mkdtemp(), "tabela.json")
        with open(caminho, "w", encoding="utf-8") as fh:
            json.dump(tabela, fh, ensure_ascii=False)

        segmentos = carrega_segmentos(caminho)
        self.assertEqual(len(segmentos), 1)
        self.assertIn(("devedor", "fazenda-pública"), segmentos[0].condicao)
        self.assertTrue(valida_cobertura(segmentos).ok)

    def test_campo_obrigatorio_ausente(self):
        with self.assertRaises(ValueError) as ctx:
            Segmento.de_dict({"inicio": "2020-01", "fim": "2020-12"}, 3)
        self.assertIn("componente", str(ctx.exception))


class TestConjuntoVazio(unittest.TestCase):
    def test_sem_segmentos_nao_quebra(self):
        self.assertTrue(valida_cobertura([]).ok)


if __name__ == "__main__":
    unittest.main(verbosity=2)
