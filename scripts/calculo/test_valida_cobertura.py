"""Testes de valida_cobertura.py — invariantes R1, R2 e R3."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

import caminhos_de_skill  # noqa: F401  (registra os scripts/ de skill no path)
import valida_cobertura as _mod_cobertura
from valida_cadeias import confere_manifesto, descobre_cadeias, le_manifesto
from valida_cobertura import (
    APLICACOES_QUE_AJUSTAM_DEFASAGEM,
    TIPOS_COM_DEFASAGEM,
    TIPOS_DE_INDEXADOR,
    TIPOS_FORA_DO_ALCANCE_DE_R3,
    TIPOS_QUE_BLOQUEIAM_R3,
    TIPOS_RETIRADOS,
    Segmento,
    carrega_segmentos,
    competencia_para_indice,
    indice_para_competencia,
    valida_cobertura,
)

CM = "correcao-monetaria"
JM = "juros-mora"
PM = "padrao-monetario"

RAIZ = Path(__file__).resolve().parents[2]
# BLOCO 25 — as cadeias e o catálogo migraram para dentro da skill.
TABELAS = caminhos_de_skill.CADEIAS
CATALOGO = caminhos_de_skill.CATALOGO_INDEXADORES


def seg(inicio, fim, componente, engloba=(), condicao=None, id=None):
    return Segmento(
        inicio=inicio,
        fim=fim,
        componente=componente,
        engloba=tuple(engloba),
        condicao=tuple(sorted((k, v) for k, v in (condicao or {}).items())),
        id=id or f"{componente}:{inicio}..{fim}",
    )


def segt(inicio, fim, indexador, tipo, aplicacao="", componente=CM, condicao=None,
         engloba=(), razao=""):
    """Segmento com tipo de indexador declarado — o material de R3."""
    return Segmento(
        inicio=inicio,
        fim=fim,
        componente=componente,
        engloba=tuple(engloba),
        condicao=tuple(sorted((k, v) for k, v in (condicao or {}).items())),
        id=indexador,
        indexador=indexador,
        tipo_indexador=tipo,
        aplicacao=aplicacao,
        tipo_indexador_razao=razao,
    )


def carrega_cadeia(nome):
    """Lê uma cadeia real do repositório. utf-8 explícito (Windows é cp1252)."""
    with open(TABELAS / nome, "r", encoding="utf-8") as fh:
        dados = json.load(fh)
    segmentos = [Segmento.de_dict(s, i) for i, s in enumerate(dados["segmentos"])]
    return dados, segmentos


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
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
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
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
        )
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1)
        self.assertEqual((lacunas[0].inicio, lacunas[0].fim), ("2022-07", "2022-07"))
        self.assertIn("fazenda-publica", lacunas[0].condicao)


class TestExaustividadeNaoSePresume(unittest.TestCase):
    """O conserto da tarefa 0 do bloco 9, na primeira versão, trocou falso
    positivo por falso negativo: tronco + um único ramo passava como íntegro
    mesmo sem cobrir o outro ramo. Nenhum dos 199 testes de então pegou."""

    TRONCO_E_UM_RAMO = [
        seg("1964-01", "2000-12", CM, id="ORTN"),
        seg("2001-01", "2025-12", CM, condicao={"devedor": "fazenda-publica"}, id="SELIC"),
    ]

    def test_ramo_nao_exaustivo_sem_dominio_declarado_acusa_lacuna(self):
        r = valida_cobertura(self.TRONCO_E_UM_RAMO, inicio="1964-01", fim="2025-12")
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1, "25 anos descobertos não podem passar")
        self.assertEqual((lacunas[0].inicio, lacunas[0].fim), ("2001-01", "2025-12"))

    def test_dominio_declarado_nomeia_o_ramo_que_falta(self):
        r = valida_cobertura(
            self.TRONCO_E_UM_RAMO, inicio="1964-01", fim="2025-12",
            dominio_condicoes={"devedor": ["fazenda-publica", "nao-fazenda-publica"]},
        )
        lacunas = [v for v in r.por_regra("R2") if "lacuna" in v.mensagem]
        self.assertEqual(len(lacunas), 1)
        self.assertIn("nao-fazenda-publica", lacunas[0].condicao)

    def test_bifurcacao_exaustiva_declarada_passa_limpa(self):
        """O caso do bloco 8: tronco longo, depois dois ramos que esgotam o eixo."""
        r = valida_cobertura(
            [
                seg("1964-01", "2021-11", CM, id="tronco"),
                seg("2021-12", "2025-12", CM, condicao={"devedor": "fazenda-publica"}, id="FP"),
                seg("2021-12", "2025-12", CM, condicao={"devedor": "privado"}, id="PRIV"),
            ],
            inicio="1964-01", fim="2025-12",
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
        )
        self.assertTrue(r.ok, str(r))

    def test_tronco_cobre_o_ramo_sem_aparecer_como_lacuna(self):
        """O falso positivo original da tarefa 0: o ramo herda o tronco."""
        r = valida_cobertura(
            [
                seg("1964-01", "2021-11", CM, id="tronco"),
                seg("2021-12", "2025-12", CM, condicao={"devedor": "fazenda-publica"}, id="FP"),
                seg("2021-12", "2025-12", CM, condicao={"devedor": "privado"}, id="PRIV"),
            ],
            inicio="1964-01", fim="2025-12",
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
        )
        self.assertEqual(
            [v for v in r.por_regra("R2") if "lacuna" in v.mensagem], [],
            "o tronco de 1964 a 2021 vale para os dois ramos",
        )

    def test_colisao_tronco_x_tronco_conta_uma_vez_so(self):
        """Dois segmentos de tronco que se sobrepõem são UM fato, não um por ramo."""
        r = valida_cobertura(
            [
                seg("1964-01", "1989-01", CM, engloba=[CM, JM], id="OTN"),
                seg("1989-01", "2021-11", CM, id="IPC"),
                seg("2021-12", "2025-12", CM, condicao={"devedor": "fazenda-publica"}, id="FP"),
                seg("2021-12", "2025-12", CM, condicao={"devedor": "privado"}, id="PRIV"),
            ],
            inicio="1964-01", fim="2025-12",
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
        )
        colisoes = [v for v in r.por_regra("R1") if v.inicio == "1989-01"]
        self.assertEqual(len(colisoes), 1, "contada uma vez por ramo infla o total")
        self.assertEqual(colisoes[0].condicao, "(tronco)")


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
            "id": "trab.correcao-monetaria.privado",
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
        # A tabela cobre UM ramo só. Isso agora se declara — antes era presumido,
        # e a presunção escondia lacuna (ver TestExaustividadeNaoSePresume).
        self.assertTrue(
            valida_cobertura(
                segmentos, dominio_condicoes={"devedor": ["fazenda-pública"]}
            ).ok
        )

    def test_campo_obrigatorio_ausente(self):
        with self.assertRaises(ValueError) as ctx:
            Segmento.de_dict({"inicio": "2020-01", "fim": "2020-12"}, 3)
        self.assertIn("componente", str(ctx.exception))


class TestConjuntoVazio(unittest.TestCase):
    def test_sem_segmentos_nao_quebra(self):
        self.assertTrue(valida_cobertura([]).ok)


# --------------------------------------------------------------------------
# R3 — tipo do indexador na virada
# --------------------------------------------------------------------------

class TestR3ViradaDeTipo(unittest.TestCase):
    """Item 4.1.2.4 do Manual CJF, `pagina_pdf` 42: nominal reflete a inflação do
    mês ANTERIOR, percentual a do PRÓPRIO mês. Virar sem ajustar a defasagem
    desloca o cálculo em um mês — e nada mais o detecta."""

    def r3(self, relatorio):
        return [v for v in relatorio.violacoes if v.regra == "R3"]

    def indet(self, relatorio):
        return [v for v in relatorio.violacoes if v.regra == "R3-INDETERMINADO"]

    # --- caso POSITIVO: a virada que viola -------------------------------

    def test_nominal_para_percentual_sem_aplicacao_viola(self):
        r = valida_cobertura(
            [
                segt("1989-03", "1990-02", "BTN", "nominal"),
                segt("1990-03", "1991-02", "IPC/IBGE", "percentual"),
            ],
            inicio="1989-03", fim="1991-02",
        )
        v = self.r3(r)
        self.assertEqual(len(v), 1, str(r))
        self.assertEqual((v[0].inicio, v[0].fim), ("1990-03", "1991-02"))
        self.assertEqual(v[0].segmentos, ["BTN", "IPC/IBGE"])
        self.assertIn("nominal → percentual", v[0].mensagem)
        self.assertFalse(r.ok)

    def test_percentual_para_nominal_tambem_viola(self):
        r = valida_cobertura(
            [
                segt("1989-01", "1989-02", "IPC/IBGE", "percentual"),
                segt("1989-03", "1990-03", "BTN", "nominal"),
            ],
            inicio="1989-01", fim="1990-03",
        )
        self.assertEqual(len(self.r3(r)), 1, "a virada é simétrica")
        self.assertIn("percentual → nominal", self.r3(r)[0].mensagem)

    # --- caso NEGATIVO: a virada com ajuste declarado --------------------

    def test_virada_com_aplicacao_declarada_no_segmento_que_entra_nao_viola(self):
        r = valida_cobertura(
            [
                segt("1989-03", "1990-02", "BTN", "nominal"),
                segt(
                    "1990-03", "1991-02", "IPC/IBGE", "percentual",
                    aplicacao="mes-posterior-a-competencia",
                ),
            ],
            inicio="1989-03", fim="1991-02",
        )
        self.assertEqual(self.r3(r), [], str(r))
        self.assertTrue(r.ok, str(r))

    def test_aplicacao_so_no_segmento_que_SAI_nao_salva(self):
        """O ajuste tem de estar declarado em quem entra: é o índice novo que
        muda de régua."""
        r = valida_cobertura(
            [
                segt("1989-03", "1990-02", "BTN", "nominal",
                     aplicacao="mes-posterior-a-competencia"),
                segt("1990-03", "1991-02", "IPC/IBGE", "percentual"),
            ],
            inicio="1989-03", fim="1991-02",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))

    def test_aplicacao_so_de_espacos_nao_conta_como_declaracao(self):
        r = valida_cobertura(
            [
                Segmento.de_dict({"inicio": "1989-03", "fim": "1990-02",
                                  "componente": CM, "indexador": "BTN",
                                  "tipo_indexador": "nominal"}, 0),
                Segmento.de_dict({"inicio": "1990-03", "fim": "1991-02",
                                  "componente": CM, "indexador": "IPC/IBGE",
                                  "tipo_indexador": "percentual",
                                  "aplicacao": "   "}, 1),
            ],
            inicio="1989-03", fim="1991-02",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))

    # --- o que NÃO é virada ----------------------------------------------

    def test_mesmo_tipo_dos_dois_lados_nao_e_virada(self):
        r = valida_cobertura(
            [
                segt("1964-01", "1986-02", "ORTN", "nominal"),
                segt("1986-03", "1989-01", "OTN", "nominal"),
            ],
            inicio="1964-01", fim="1989-01",
        )
        self.assertTrue(r.ok, str(r))

    def test_mesmo_indexador_dos_dois_lados_nao_e_virada(self):
        """Trocar fundamento ou condição não move a régua de defasagem."""
        r = valida_cobertura(
            [
                segt("2021-12", "2024-08", "INPC", "percentual"),
                segt("2024-09", "2025-08", "INPC", "nominal"),  # tipo absurdo de propósito
            ],
            inicio="2021-12", fim="2025-08",
        )
        self.assertEqual(self.r3(r), [], "mesmo indexador não é virada")

    def test_englobante_nao_entra_em_r3(self):
        """Selic não é índice de inflação (D8-C22). Quem governa é R1, não R3."""
        r = valida_cobertura(
            [
                segt("1992-01", "1995-12", "Ufir", "nominal"),
                segt("1996-01", "2021-11", "Selic", "englobante"),
                segt("2021-12", "2024-08", "INPC", "percentual"),
            ],
            inicio="1992-01", fim="2024-08",
        )
        self.assertEqual(self.r3(r), [], str(r))
        self.assertEqual(self.indet(r), [], str(r))

    def test_nao_indexador_nao_entra_em_r3(self):
        """Moeda não é indexador: não há defasagem a alinhar."""
        r = valida_cobertura(
            [
                segt("1990-03", "1993-07", "Cruzeiro (Cr$)", "nao-indexador",
                     componente=PM),
                segt("1993-08", "1994-06", "Cruzeiro real (CR$)", "nao-indexador",
                     componente=PM),
            ],
            inicio="1990-03", fim="1994-06",
        )
        self.assertEqual(self.r3(r), [], str(r))
        self.assertEqual(self.indet(r), [], str(r))

    def test_sem_o_campo_tipo_nao_acusa_nada(self):
        """Retrocompatibilidade: R3 não inventa tipo para quem não o declara."""
        r = valida_cobertura(
            [seg("1989-03", "1990-02", CM, id="BTN"), seg("1990-03", "1991-02", CM, id="IPC")],
            inicio="1989-03", fim="1991-02",
        )
        self.assertTrue(r.ok, str(r))

    # --- o caso INDETERMINADO: decidido BLOQUEIA --------------------------

    def test_indeterminado_numa_ponta_bloqueia(self):
        """DECISÃO do bloco 17: bloqueia, com rótulo próprio.

        Passar converteria "não se sabe" em "está certo". Num validador cuja
        razão de existir é que o erro de R3 não tem sintoma, o falso negativo
        é o pior resultado possível — é a mesma troca que a nota sobre
        exaustividade, no módulo, já condena uma vez."""
        r = valida_cobertura(
            [
                segt("1992-01", "2000-12", "Ufir", "nominal"),
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "indeterminado"),
            ],
            inicio="1992-01", fim="2021-11",
        )
        self.assertFalse(r.ok, "indeterminado numa ponta não pode passar limpo")
        self.assertEqual(self.r3(r), [], "não é virada CONFIRMADA")
        v = self.indet(r)
        self.assertEqual(len(v), 1, str(r))
        self.assertEqual(v[0].segmentos, ["Ufir", "IPCA-E/IBGE"])
        self.assertIn("NÃO PODE SER VERIFICADA", v[0].mensagem)

    def test_indeterminado_dos_dois_lados_tambem_bloqueia(self):
        r = valida_cobertura(
            [
                segt("2001-01", "2024-08", "IPCA-E/IBGE", "indeterminado"),
                segt("2024-09", "2025-08", "IPCA-15/IBGE", "indeterminado"),
            ],
            inicio="2001-01", fim="2025-08",
        )
        self.assertEqual(len(self.indet(r)), 1, str(r))

    def test_aplicacao_declarada_NAO_salva_o_indeterminado(self):
        """Declarar a defasagem não supre a falta de classificação: sem saber o
        tipo, não se sabe se a defasagem declarada é a certa."""
        r = valida_cobertura(
            [
                segt("1992-01", "2000-12", "Ufir", "nominal"),
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "indeterminado",
                     aplicacao="mes-posterior-a-competencia"),
            ],
            inicio="1992-01", fim="2021-11",
        )
        self.assertEqual(len(self.indet(r)), 1, str(r))

    def test_indeterminado_contra_englobante_nao_acusa(self):
        r = valida_cobertura(
            [
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "indeterminado"),
                segt("2021-12", "2025-08", "Selic", "englobante"),
            ],
            inicio="2001-01", fim="2025-08",
        )
        self.assertEqual(self.indet(r), [], str(r))

    # --- fronteiras de universo ------------------------------------------

    def test_r3_nao_cruza_ramos_de_condicao_distinta(self):
        """Fazenda e privado são linhas do tempo separadas: a 'virada' entre
        elas não existe."""
        r = valida_cobertura(
            [
                segt("2021-12", "2024-08", "Selic", "englobante",
                     condicao={"devedor": "fazenda-publica"}, engloba=[CM, JM]),
                segt("2021-12", "2024-08", "INPC", "percentual",
                     condicao={"devedor": "privado"}),
            ],
            inicio="2021-12", fim="2024-08",
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
        )
        self.assertEqual(self.r3(r), [], str(r))

    def test_tronco_entra_na_linha_do_ramo(self):
        """Tronco nominal seguido de ramo percentual É virada, uma por ramo."""
        r = valida_cobertura(
            [
                segt("1964-01", "2021-11", "Ufir", "nominal"),
                segt("2021-12", "2025-08", "INPC", "percentual",
                     condicao={"devedor": "fazenda-publica"}),
                segt("2021-12", "2025-08", "IGP-DI", "percentual",
                     condicao={"devedor": "privado"}),
            ],
            inicio="1964-01", fim="2025-08",
            dominio_condicoes={"devedor": ["fazenda-publica", "privado"]},
        )
        self.assertEqual(len(self.r3(r)), 2, str(r))
        self.assertEqual(
            {v.condicao for v in self.r3(r)},
            {"devedor=fazenda-publica", "devedor=privado"},
        )

    # --- domínio do campo -------------------------------------------------

    def test_tipo_fora_do_dominio_e_rejeitado(self):
        with self.assertRaises(ValueError) as ctx:
            Segmento.de_dict({
                "inicio": "2020-01", "fim": "2020-12", "componente": CM,
                "tipo_indexador": "real",
            }, 7)
        self.assertIn("tipo_indexador", str(ctx.exception))

    def test_dominio_e_fechado_e_tem_os_seis_valores(self):
        """Bloco 19: entra `janela-deslocada`. `englobante` fica legível, mas
        RETIRADO — nenhuma cadeia o usa, e há teste separado que o cobra."""
        self.assertEqual(
            TIPOS_DE_INDEXADOR,
            {"nominal", "percentual", "janela-deslocada", "englobante",
             "nao-indexador", "indeterminado"},
        )
        self.assertEqual(TIPOS_RETIRADOS, {"englobante"})
        self.assertTrue(TIPOS_RETIRADOS <= TIPOS_DE_INDEXADOR)

    def test_janela_deslocada_esta_no_dominio_e_e_aceita(self):
        s = Segmento.de_dict({
            "inicio": "2001-01", "fim": "2021-11", "componente": CM,
            "indexador": "IPCA-E/IBGE", "tipo_indexador": "janela-deslocada",
        }, 0)
        self.assertEqual(s.tipo_indexador, "janela-deslocada")

    def test_grafia_aproximada_de_janela_deslocada_e_rejeitada(self):
        """Domínio FECHADO: 'janela deslocada' com espaço não passa."""
        for errado in ("janela deslocada", "janela_deslocada", "Janela-Deslocada"):
            with self.assertRaises(ValueError, msg=errado):
                Segmento.de_dict({
                    "inicio": "2001-01", "fim": "2001-12", "componente": CM,
                    "tipo_indexador": errado,
                }, 0)

    def test_as_tres_classes_com_defasagem(self):
        self.assertEqual(
            TIPOS_COM_DEFASAGEM,
            {"nominal", "percentual", "janela-deslocada"},
        )


class TestParticaoDoDominioDeTipo(unittest.TestCase):
    """BLOCO 20 — o buraco em `derivado`, e ele era real.

    `_valida_r3` acusava só quando **as duas pontas** estavam em
    `TIPOS_COM_DEFASAGEM`. Valor de `tipo_indexador` fora dos três conjuntos
    caía no fim da função **sem violação e sem `R3-INDETERMINADO`** — silêncio.
    Num validador cuja razão de existir é que o erro de R3 não tem sintoma,
    silêncio é o pior resultado possível: é a mesma troca de falso positivo por
    falso negativo que a nota sobre exaustividade já condena.

    O conserto tem duas metades, e as duas estão aqui: **os conjuntos amarrados**
    (nenhum valor do domínio sem destino) e **o fall-through que grita**.
    """

    def test_os_tres_conjuntos_particionam_o_dominio(self):
        cobertos = (
            TIPOS_COM_DEFASAGEM
            | TIPOS_FORA_DO_ALCANCE_DE_R3
            | TIPOS_QUE_BLOQUEIAM_R3
        )
        self.assertEqual(
            TIPOS_DE_INDEXADOR - cobertos, set(),
            "valor de tipo_indexador sem destino em R3: ou tem defasagem, ou "
            "está declarado fora de alcance, ou bloqueia. Silêncio não é opção.",
        )
        self.assertEqual(
            cobertos - TIPOS_DE_INDEXADOR, set(),
            "conjunto de R3 nomeia tipo que não está no domínio",
        )

    def test_os_tres_conjuntos_sao_disjuntos(self):
        """Dois destinos para o mesmo valor é ambiguidade, e a ordem dos `if`
        decidiria em silêncio qual vale."""
        pares = (
            (TIPOS_COM_DEFASAGEM, TIPOS_FORA_DO_ALCANCE_DE_R3),
            (TIPOS_COM_DEFASAGEM, TIPOS_QUE_BLOQUEIAM_R3),
            (TIPOS_FORA_DO_ALCANCE_DE_R3, TIPOS_QUE_BLOQUEIAM_R3),
        )
        for a, b in pares:
            self.assertEqual(a & b, set(), f"{sorted(a)} × {sorted(b)}")

    def test_valor_fora_dos_tres_conjuntos_GRITA_em_vez_de_passar(self):
        """A prova de que o silêncio acabou. `Segmento.de_dict` barra o valor
        desconhecido na leitura; este teste constrói o `Segmento` direto, que é
        o caminho por onde um valor novo entraria sem revalidação."""
        estranho = Segmento(
            inicio="2010-01", fim="2019-12", componente=CM,
            id="X", indexador="X", tipo_indexador="derivado",
        )
        normal = segt("2000-01", "2009-12", "Ufir", "nominal")
        with self.assertRaises(ValueError) as ctx:
            valida_cobertura([normal, estranho], inicio="2000-01", fim="2019-12")
        self.assertIn("R3 sem regra para o par de tipos", str(ctx.exception))
        self.assertIn("derivado", str(ctx.exception))

    def test_nao_indexador_isenta_tres_viradas_e_a_caracterizacao_esta_certa(self):
        """L-a do bloco 20 — a isenção se sustenta; a caracterização não estava.

        Dizia-se *"+3, todas moeda × índice"*. **Duas** são `Conversão em URV`;
        a terceira é `cjf.divida-fiscal.correcao-monetaria` segmento 4, com
        `indexador: null` e a observação *"Não há correção monetária, somente
        juros"* — **não é moeda, é janela sem correção**. Índice classificado por
        dedução é proibido, e chamar de moeda o que é ausência de índice era
        justamente isso.
        """
        dados, _ = carrega_cadeia("cjf.divida-fiscal.correcao-monetaria.json")
        s = dados["segmentos"][3]
        self.assertIsNone(s["indexador"])
        self.assertEqual(s["tipo_indexador"], "nao-indexador")
        self.assertIn("Não há correção monetária", s["observacao"])
        self.assertEqual((s["inicio"], s["fim"]), ("1991-02", "1991-12"))

        # As duas que SÃO moeda, e são as únicas.
        dados, _ = carrega_cadeia("cjf.previdenciario.correcao-monetaria.json")
        urv = [x for x in dados["segmentos"] if x.get("indexador") == "Conversão em URV"]
        self.assertEqual(len(urv), 1, "a URV é um segmento só; as viradas são duas")
        self.assertEqual(urv[0]["tipo_indexador"], "nao-indexador")


class TestR3JanelaDeslocada(unittest.TestCase):
    """Bloco 19 — a terceira classe.

    `janela-deslocada` mede metade de M−1 e metade de M. Não é `nominal` (M−1
    inteiro) nem `percentual` (M inteiro): a virada contra QUALQUER das duas
    desloca o cálculo tanto quanto a virada entre elas. São TRÊS pares, não um.
    """

    def r3(self, relatorio):
        return relatorio.por_regra("R3")

    def indet(self, relatorio):
        return relatorio.por_regra("R3-INDETERMINADO")

    def test_nominal_para_janela_deslocada_e_virada(self):
        r = valida_cobertura(
            [
                segt("1992-01", "2000-12", "Ufir", "nominal"),
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada"),
            ],
            inicio="1992-01", fim="2021-11",
        )
        v = self.r3(r)
        self.assertEqual(len(v), 1, str(r))
        self.assertIn("nominal → janela-deslocada", v[0].mensagem)
        self.assertEqual(v[0].segmentos, ["Ufir", "IPCA-E/IBGE"])

    def test_janela_deslocada_para_nominal_tambem_e_virada(self):
        r = valida_cobertura(
            [
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada"),
                segt("2021-12", "2025-08", "Ufir", "nominal"),
            ],
            inicio="2001-01", fim="2025-08",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))

    def test_percentual_para_janela_deslocada_e_virada(self):
        """É a virada que a reclassificação da SELIC tornou visível."""
        r = valida_cobertura(
            [
                segt("2021-12", "2025-08", "Selic", "percentual"),
                segt("2025-09", "2026-06", "IPCA-15/IBGE", "janela-deslocada"),
            ],
            inicio="2021-12", fim="2026-06",
        )
        v = self.r3(r)
        self.assertEqual(len(v), 1, str(r))
        self.assertIn("percentual → janela-deslocada", v[0].mensagem)

    def test_janela_deslocada_para_percentual_tambem_e_virada(self):
        r = valida_cobertura(
            [
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada"),
                segt("2021-12", "2025-08", "INPC", "percentual"),
            ],
            inicio="2001-01", fim="2025-08",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))

    def test_janela_deslocada_contra_janela_deslocada_NAO_e_virada(self):
        """IPCA-E mensal É o IPCA-15 (fonte externa, IBGE). Mesma classe, mesma
        régua: rótulos diferentes não fazem virada."""
        r = valida_cobertura(
            [
                segt("2021-12", "2024-08", "IPCA-E/IBGE", "janela-deslocada"),
                segt("2024-09", "2025-08", "IPCA-15/IBGE", "janela-deslocada"),
            ],
            inicio="2021-12", fim="2025-08",
        )
        self.assertEqual(self.r3(r), [], str(r))
        self.assertTrue(r.ok, str(r))

    def test_aplicacao_salva_a_virada_para_janela_deslocada(self):
        """Mesmo remédio das outras duas classes: declarar em 'aplicacao'."""
        r = valida_cobertura(
            [
                segt("1992-01", "2000-12", "Ufir", "nominal"),
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada",
                     aplicacao="mes-posterior-a-competencia"),
            ],
            inicio="1992-01", fim="2021-11",
        )
        self.assertEqual(self.r3(r), [], str(r))
        self.assertTrue(r.ok, str(r))

    def test_aplicacao_salva_tambem_a_virada_percentual_para_janela(self):
        r = valida_cobertura(
            [
                segt("2021-12", "2025-08", "Selic", "percentual"),
                segt("2025-09", "2026-06", "IPCA-15/IBGE", "janela-deslocada",
                     aplicacao="primeiro-dia-do-mes-subsequente-a-prestacao"),
            ],
            inicio="2021-12", fim="2026-06",
        )
        self.assertEqual(self.r3(r), [], str(r))

    def test_aplicacao_no_segmento_que_SAI_nao_salva(self):
        """O ajuste tem de ser declarado por quem ENTRA. Simétrico ao que já
        valia para nominal × percentual."""
        r = valida_cobertura(
            [
                segt("1992-01", "2000-12", "Ufir", "nominal",
                     aplicacao="mes-posterior-a-competencia"),
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada"),
            ],
            inicio="1992-01", fim="2021-11",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))

    def test_tres_classes_produzem_tres_pares_de_virada(self):
        """A regra não enumera pares: exige que os dois lados estejam em
        TIPOS_COM_DEFASAGEM e sejam diferentes. Prova exaustiva."""
        classes = sorted(TIPOS_COM_DEFASAGEM)
        pares = [(a, b) for a in classes for b in classes if a != b]
        self.assertEqual(len(pares), 6, "três classes, seis viradas ordenadas")
        for a, b in pares:
            r = valida_cobertura(
                [
                    segt("2000-01", "2009-12", f"X-{a}", a),
                    segt("2010-01", "2019-12", f"Y-{b}", b),
                ],
                inicio="2000-01", fim="2019-12",
            )
            self.assertEqual(len(self.r3(r)), 1, f"{a} → {b}: {r}")

    def test_janela_deslocada_contra_indeterminado_bloqueia(self):
        r = valida_cobertura(
            [
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada"),
                segt("2021-12", "2025-08", "TR", "indeterminado"),
            ],
            inicio="2001-01", fim="2025-08",
        )
        self.assertEqual(len(self.indet(r)), 1, str(r))

    def test_janela_deslocada_contra_nao_indexador_nao_acusa(self):
        r = valida_cobertura(
            [
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada"),
                segt("2021-12", "2025-08", "Real (R$)", "nao-indexador"),
            ],
            inicio="2001-01", fim="2025-08",
        )
        self.assertTrue(r.ok, str(r))


class TestRazaoNaoEPendencia(unittest.TestCase):
    """Bloco 19 — `indeterminado` tem duas razões, e elas se fecham diferente.

    Pendência diz *"não há fonte"* e fecha quando a fonte chegar. Razão diz
    *"há fonte, e ela diz que o índice não cabe em mês calendário"* — e não
    fecha esperando fonte. As duas BLOQUEIAM, porque o efeito sobre o cálculo é
    o mesmo; o que muda é o que a mensagem diz a quem audita.
    """

    def test_razao_aparece_na_mensagem_e_a_virada_segue_bloqueando(self):
        r = valida_cobertura(
            [
                segt("1964-01", "1993-04", "ORTN", "nominal"),
                segt("1993-05", "2026-06", "TR", "indeterminado",
                     razao="período entre datas de aniversário e prefixação"),
            ],
            inicio="1964-01", fim="2026-06",
        )
        v = r.por_regra("R3-INDETERMINADO")
        self.assertEqual(len(v), 1, str(r))
        self.assertIn("NÃO CABE", v[0].mensagem)
        self.assertIn("datas de aniversário", v[0].mensagem)
        self.assertIn("NÃO se fecha esperando fonte", v[0].mensagem)

    def test_sem_razao_a_mensagem_continua_dizendo_sem_fonte(self):
        r = valida_cobertura(
            [
                segt("1964-01", "1986-02", "ORTN", "nominal"),
                segt("1986-03", "1987-01", "IPC", "indeterminado"),
            ],
            inicio="1964-01", fim="1987-01",
        )
        v = r.por_regra("R3-INDETERMINADO")
        self.assertEqual(len(v), 1, str(r))
        self.assertIn("sem fonte é pendência", v[0].mensagem)
        self.assertNotIn("NÃO CABE", v[0].mensagem)

    def test_razao_em_tipo_que_nao_e_indeterminado_e_rejeitada(self):
        with self.assertRaises(ValueError) as ctx:
            Segmento.de_dict({
                "inicio": "2020-01", "fim": "2020-12", "componente": CM,
                "tipo_indexador": "percentual",
                "tipo_indexador_razao": "qualquer coisa",
            }, 3)
        self.assertIn("só cabe em 'indeterminado'", str(ctx.exception))

    def test_razao_e_pendencia_juntas_sao_rejeitadas(self):
        """São afirmações INCOMPATÍVEIS sobre o estado do conhecimento: uma diz
        que não há fonte, a outra que há."""
        with self.assertRaises(ValueError) as ctx:
            Segmento.de_dict({
                "inicio": "2020-01", "fim": "2020-12", "componente": CM,
                "tipo_indexador": "indeterminado",
                "tipo_indexador_razao": "período entre datas de aniversário",
                "tipo_indexador_pendencia": "P17-02",
            }, 4)
        self.assertIn("mutuamente excludentes", str(ctx.exception))


class TestR3NasCadeiasDoBloco9(unittest.TestCase):
    """As cadeias históricas do TRT-3. O relatório do bloco 9 (§ 5.3) afirma que
    NÃO há virada entre nominal e percentual neste capítulo — "porque não há
    cadeia de índices: o único indexador nomeado é a TR". O validador confirma:
    zero R3 confirmadas. O que ele acrescenta é o que o bloco 9 não tinha campo
    para dizer — as duas pontas indeterminadas."""

    def test_correcao_monetaria_tem_zero_r3_confirmada_e_duas_indeterminadas(self):
        _, segmentos = carrega_cadeia("trab.hist.correcao-monetaria.json")
        r = valida_cobertura(
            segmentos, "1942-11", "2016-05",
            dominio_condicoes={"devedor": ["fazenda-publica", "nao-fazenda-publica"]},
        )
        confirmadas = [v for v in r.violacoes if v.regra == "R3"]
        indeterminadas = [v for v in r.violacoes if v.regra == "R3-INDETERMINADO"]
        self.assertEqual(confirmadas, [], "bloco-09-relatorio.md § 5.3: não há virada")
        self.assertEqual(len(indeterminadas), 2, str(r))
        self.assertTrue(
            all("NAO-DECLARADO-PELO-MANUAL" in v.segmentos for v in indeterminadas)
        )

    def test_tr_esta_rebaixada_a_indeterminado(self):
        """Era `percentual` por inferência DECLARADA (critério formal do 4.1.2.4).
        Inferência declarada não é fonte — logo, indeterminado."""
        _, segmentos = carrega_cadeia("trab.hist.correcao-monetaria.json")
        tr = [s for s in segmentos if "TR" in s.indexador]
        self.assertEqual(len(tr), 2)
        for s in tr:
            self.assertEqual(s.tipo_indexador, "indeterminado", s.indexador)

    def test_moedas_nao_produzem_r3(self):
        _, segmentos = carrega_cadeia("trab.hist.moedas-e-paridades.json")
        r = valida_cobertura(segmentos, "1942-11", "2016-05")
        self.assertEqual([v for v in r.violacoes if v.regra.startswith("R3")], [])

    def test_juros_trabalhistas_sem_indexador_nao_produzem_r3(self):
        _, segmentos = carrega_cadeia("trab.hist.juros-mora.json")
        r = valida_cobertura(segmentos, "1942-11", "2016-05")
        self.assertEqual([v for v in r.violacoes if v.regra.startswith("R3")], [])


class TestAplicacaoEVocabularioFechado(unittest.TestCase):
    """BLOCO 20 — `aplicacao` deixou de ser um teste de truthiness.

    O padrão auditado é o de `englobante`: valor que duplica o que outro campo
    já expressa e cuja presença DESLIGA uma checagem. Aqui não era um valor de
    enum — era a AUSÊNCIA de enum: qualquer string não-vazia em `aplicacao`
    desligava R3, inclusive prosa que fala de outro componente (a regra de
    incidência dos JUROS, transcrita dentro de uma cadeia de CORREÇÃO).

    Estes testes impedem o retorno, como `test_nenhuma_constante_de_faixa_do_
    bloco_sobrou` do bloco 17 impediu o da constante.
    """

    def r3(self, r):
        return [v for v in r.violacoes if v.regra == "R3"]

    def test_prosa_em_aplicacao_nao_salva_a_virada(self):
        """Prosa NÃO casa com token, mesmo prosa que descreve uma defasagem real.

        Este é exatamente o mecanismo do falso positivo que o bloco 20 corrigiu
        em seguida: a prosa abaixo É a fórmula **D3**, do próprio componente do
        segmento que a carrega — e era rejeitada pela GRAFIA. O conserto não foi
        reabrir o vocabulário: foi **tokenizar D2, D3 e D4** e guardar o literal
        em `aplicacao_literal`. O teste segue aqui para provar que a régua
        continua sendo o token, nunca o texto.
        """
        r = valida_cobertura(
            [
                segt("1992-01", "1995-12", "Ufir", "nominal"),
                segt("1996-01", "2026-06", "Selic", "percentual",
                     aplicacao=("a partir do mês seguinte ao recolhimento indevido "
                                "até o mês anterior à repetição, e 1% no mês da "
                                "repetição")),
            ],
            inicio="1992-01", fim="2026-06",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))
        self.assertIn("PROSA fora do vocabulário", str(r))

    def test_o_token_D3_salva_a_mesma_virada_que_a_prosa_nao_salvava(self):
        """A metade que faltava: tokenizada, a MESMA regra passa a valer."""
        r = valida_cobertura(
            [
                segt("1992-01", "1995-12", "Ufir", "nominal"),
                segt("1996-01", "2026-06", "Selic", "percentual",
                     aplicacao=("mes-seguinte-ao-recolhimento-indevido-e-1pct-"
                                "no-mes-da-repeticao")),
            ],
            inicio="1992-01", fim="2026-06",
        )
        self.assertEqual(self.r3(r), [], str(r))

    def test_regra_de_qual_valor_usar_tambem_nao_salva(self):
        """A prosa literal de `cjf.condenatorias-gerais.correcao-monetaria`:
        diz QUAL valor do IPCA-E usar em jan./2001, não QUANDO ele incide."""
        r = valida_cobertura(
            [
                segt("1992-01", "2000-12", "Ufir", "nominal"),
                segt("2001-01", "2021-11", "IPCA-E/IBGE", "janela-deslocada",
                     aplicacao=("O percentual a ser utilizado em janeiro de 2001 "
                                "deverá ser o IPCA-E acumulado no período de "
                                "janeiro a dezembro de 2000.")),
            ],
            inicio="1992-01", fim="2021-11",
        )
        self.assertEqual(len(self.r3(r)), 1, str(r))

    def test_o_vocabulario_e_fechado_e_tem_as_quatro_formulas_mais_a_trabalhista(self):
        """Eram DOIS tokens para QUATRO fórmulas declaradas no consolidado.

        `02-atualizacao-detalhe.md` § 5.3 enuncia `D1`–`D4`; o domínio só tinha
        `D1`. `D2`, `D3` e `D4` estavam gravadas em prosa e eram rejeitadas pela
        GRAFIA — não por não serem declaração de defasagem.
        """
        self.assertEqual(
            APLICACOES_QUE_AJUSTAM_DEFASAGEM,
            frozenset({
                "mes-posterior-a-competencia",                                    # D1
                "mes-seguinte-ao-termo-inicial-dos-juros-e-1pct-no-mes-do-pagamento",   # D2
                "mes-seguinte-ao-recolhimento-indevido-e-1pct-no-mes-da-repeticao",     # D3
                "mes-seguinte-a-competencia-da-parcela-e-1pct-no-mes-do-pagamento",     # D4
                "primeiro-dia-do-mes-subsequente-a-prestacao",
            }),
        )

    def test_todo_valor_de_aplicacao_do_repositorio_e_token_ou_literal(self):
        """`aplicacao` é campo de TOKEN. Prosa mora em `aplicacao_literal`.

        Uma única exceção, e ela é o achado que se sustenta: a de jan./2001 em
        `cjf.condenatorias-gerais.correcao-monetaria`, que diz **qual** valor do
        IPCA-E usar, não **quando** ele incide — não é regra de defasagem, e por
        isso NÃO foi tokenizada e segue produzindo violação de R3.
        """
        prosa = []
        for ident, c in sorted(descobre_cadeias(TABELAS).items()):
            with open(TABELAS / c["arquivo"], "r", encoding="utf-8") as fh:
                dados = json.load(fh)
            for i, s in enumerate(dados["segmentos"]):
                valor = (s.get("aplicacao") or "").strip()
                if valor and valor not in APLICACOES_QUE_AJUSTAM_DEFASAGEM:
                    prosa.append((ident, i, valor[:40]))
        self.assertEqual(len(prosa), 1, prosa)
        self.assertEqual(prosa[0][0], "cjf.condenatorias-gerais.correcao-monetaria")
        self.assertTrue(prosa[0][2].startswith("O percentual a ser utilizado"), prosa)

    def test_os_cinco_tokenizados_preservam_o_literal_e_nomeiam_a_formula(self):
        """Tokenizar não pode perder o literal do manual. `aplicacao_literal` é
        onde a prosa foi guardada, e `aplicacao_formula` diz qual `D` é."""
        esperado = {
            ("cjf.condenatorias-gerais.juros-mora.json", 1): "D2",
            ("cjf.repeticao-indebito.correcao-monetaria.json", 9): "D3",
            ("cjf.fgts.juros-mora.json", 1): "D4",
            ("cjf.poupanca.juros-mora.json", 1): "D4",
            ("cjf.divida-fiscal.juros-mora.json", 7): "D4",
        }
        for (arquivo, i), formula in esperado.items():
            with open(TABELAS / arquivo, "r", encoding="utf-8") as fh:
                s = json.load(fh)["segmentos"][i]
            self.assertIn(s["aplicacao"], APLICACOES_QUE_AJUSTAM_DEFASAGEM, arquivo)
            self.assertEqual(s.get("aplicacao_formula"), formula, arquivo)
            literal = s.get("aplicacao_literal", "")
            self.assertIn("a partir do mês seguinte", literal, arquivo)
            self.assertIn("1% no mês", literal, arquivo)

    def test_a_virada_da_repeticao_de_indebito_era_falso_positivo_e_sumiu(self):
        """`cjf.repeticao-indebito.correcao-monetaria`, `Ufir → Selic`.

        A justificativa escrita no validador dizia que a prosa era *"de outro
        componente — a regra dos JUROS"*. **Era falsa**: o segmento declara
        `componente: correcao-monetaria` e `engloba` os dois. É o `D3` do
        próprio componente, e a violação que dali saía era de modelagem.
        """
        dados, segmentos = carrega_cadeia(
            "cjf.repeticao-indebito.correcao-monetaria.json")
        alvo = dados["segmentos"][9]
        self.assertEqual(alvo["componente"], CM)
        self.assertEqual(sorted(alvo["engloba"]), [CM, JM])
        r = valida_cobertura(segmentos, "1964-01", "2026-06")
        pares = {tuple(sorted(v.segmentos)) for v in self.r3(r)}
        self.assertNotIn(("Selic", "Ufir"), pares, str(r))

    def test_nenhum_escape_por_truthiness_sobrou_no_codigo(self):
        """Guarda literal: o teste `if seguinte.aplicacao:` não pode voltar."""
        # BLOCO 25 — a fonte sai do MÓDULO, não de um irmão de diretório: o script
        # virou script de skill e a guarda tinha de ir junto.
        fonte = Path(_mod_cobertura.__file__).read_text(encoding="utf-8")
        self.assertNotIn("if seguinte.aplicacao:", fonte)
        self.assertIn("in APLICACOES_QUE_AJUSTAM_DEFASAGEM", fonte)

    def test_a_virada_que_a_prosa_escondia_e_que_se_sustenta(self):
        """`Ufir → IPCA-E`, em `cjf.condenatorias-gerais.correcao-monetaria`.

        Das DUAS viradas que o fechamento do vocabulário revelou, **uma era
        falso positivo de modelagem** (a de `repeticao-indebito` — teste acima) e
        **esta se sustenta**: o `aplicacao` do segmento que entra diz qual valor
        do IPCA-E usar em jan./2001, e não quando o índice incide. Violação DO
        MANUAL: ele troca de classe de janela e não declara ajuste de defasagem.
        """
        _, segmentos = carrega_cadeia("cjf.condenatorias-gerais.correcao-monetaria.json")
        r = valida_cobertura(
            segmentos, "1964-01", "2026-06",
            dominio_condicoes={"devedor": ["fazenda-publica", "nao-fazenda-publica"]},
        )
        pares = {tuple(sorted(v.segmentos)) for v in self.r3(r) if v.componente == CM}
        self.assertIn(("IPCA-E/IBGE", "Ufir"), pares, str(r))


class TestCatalogoDeTipos(unittest.TestCase):
    """O catálogo é a única fonte do campo. Nenhuma cadeia pode carregar
    indexador que ele não classifique, nem tipo fora do domínio."""

    def catalogo(self):
        with open(CATALOGO, "r", encoding="utf-8") as fh:
            return json.load(fh)

    def cadeias(self):
        """Descoberta pelo CONTEUDO, nunca pelo prefixo do nome do arquivo.

        A versao anterior filtrava por `("cjf.", "trt3.hist.")`. Quando o bloco
        17 renomeou os quatro `trt3.hist.*` para `trab.hist.*`, ela passou a
        achar 7 de 11 — e as guardas de `tipo_indexador` teriam dado OK sem
        inspecionar quatro cadeias. O teste falhou, e estava certo.

        A contagem NÃO é mais constante. `assertEqual(len(nomes), 11)` estava
        certa quando quebrou com as quatro cadeias do bloco 18 — mas trocar 11
        por 15 reintroduz o defeito daqui a quatro meses. O piso vem do
        manifesto, que cresce sozinho e só encolhe por edição deliberada.
        """
        achadas = descobre_cadeias(TABELAS)
        regressoes, _ = confere_manifesto(achadas)
        self.assertEqual(regressoes, [], "regressão contra cadeias-manifesto.json")
        return [c["arquivo"] for c in achadas.values()]

    def test_todo_segmento_de_toda_cadeia_tem_tipo(self):
        """Cada cadeia tem de trazer PELO MENOS os segmentos que o manifesto
        registra. `assertEqual(total, 97)` tinha o mesmo defeito da contagem de
        cadeias: cravava um número que o crescimento normal invalida, e ainda
        agregava tudo num só total, onde uma cadeia que encolhe some por
        compensação com outra que cresce. O manifesto guarda POR CADEIA."""
        declarado = le_manifesto().get("cadeias", {})
        achadas = descobre_cadeias(TABELAS)
        for nome in self.cadeias():
            _, segmentos = carrega_cadeia(nome)
            for s in segmentos:
                self.assertIn(s.tipo_indexador, TIPOS_DE_INDEXADOR, f"{nome}: {s.id}")
        for ident, piso in declarado.items():
            self.assertIn(ident, achadas, f"cadeia '{ident}' sumiu")
            self.assertGreaterEqual(
                achadas[ident]["segmentos"], piso["segmentos"],
                f"{ident}: encolheu de {piso['segmentos']} segmentos",
            )

    def test_todo_indexador_esta_no_catalogo_com_o_mesmo_tipo(self):
        idx = self.catalogo()["indexadores"]
        for nome in self.cadeias():
            _, segmentos = carrega_cadeia(nome)
            for s in segmentos:
                chave = s.indexador or "(segmento sem indexador)"
                self.assertIn(chave, idx, f"{nome}: indexador fora do catálogo")
                self.assertEqual(idx[chave]["tipo"], s.tipo_indexador, chave)

    def test_classificado_tem_fonte_e_indeterminado_tem_pendencia_OU_razao(self):
        """Bloco 19 — `indeterminado` fecha de duas formas, e o catálogo tem de
        dizer QUAL. Sem fonte → `pendencia`, com `fonte: null`. Fonte diz que
        não cabe → `razao`, com `fonte` preenchida. NUNCA as duas."""
        idx = self.catalogo()["indexadores"]
        for chave, e in idx.items():
            if e["tipo"] != "indeterminado":
                self.assertTrue(e.get("fonte"), f"{chave}: classificado sem fonte")
                self.assertFalse(
                    e.get("razao"), f"{chave}: razão só cabe em indeterminado"
                )
                continue
            tem_razao, tem_pend = bool(e.get("razao")), bool(e.get("pendencia"))
            self.assertNotEqual(
                tem_razao, tem_pend,
                f"{chave}: indeterminado precisa de EXATAMENTE um entre "
                f"'razao' e 'pendencia' (razao={tem_razao}, pendencia={tem_pend})",
            )
            if tem_razao:
                self.assertTrue(
                    e.get("fonte"),
                    f"{chave}: razão afirma que a fonte EXISTE e diz que não cabe",
                )
                self.assertTrue(e.get("fechamento"), f"{chave}: razão sem fechamento")
            else:
                self.assertIsNone(e.get("fonte"), chave)

    def test_ipca_e_e_ipca_15_sao_janela_deslocada(self):
        """Bloco 19. Não por dedução a partir do nome — por FONTE EXTERNA AO
        CORPUS (IBGE), declarada como externa no próprio catálogo: o período de
        coleta vai do dia 16 de M−1 ao dia 15 de M."""
        idx = self.catalogo()["indexadores"]
        for chave in ("IPCA-E/IBGE", "IPCA-15/IBGE"):
            self.assertEqual(idx[chave]["tipo"], "janela-deslocada", chave)
            self.assertIn("FONTE EXTERNA AO CORPUS", idx[chave]["fonte"], chave)

    def test_ipca_serie_especial_continua_indeterminado(self):
        """A fonte externa alcança IPCA-15 e IPCA-E. NÃO diz que a 'série
        especial' seja um ou outro — e o manual a grava como segmento próprio.
        Identificá-la por semelhança de nome é a dedução proibida."""
        idx = self.catalogo()["indexadores"]
        e = idx["IPCA série especial"]
        self.assertEqual(e["tipo"], "indeterminado")
        self.assertEqual(e["pendencia"], "P17-01")

    def test_selic_e_percentual_e_taxa_legal_e_indeterminado(self):
        """`englobante` era fato de R1 dentro do campo de R3, e deixava a SELIC
        cega. A taxa legal NÃO vem junto: a fonte externa não a alcança, e
        `percentual` por analogia com a SELIC seria a dedução proibida."""
        idx = self.catalogo()["indexadores"]
        self.assertEqual(idx["Selic"]["tipo"], "percentual")
        self.assertEqual(idx["taxa-legal"]["tipo"], "indeterminado")
        self.assertEqual(idx["taxa-legal"]["pendencia"], "P19-01")

    def test_nenhum_indexador_do_catalogo_e_englobante(self):
        idx = self.catalogo()["indexadores"]
        self.assertEqual(
            [k for k, e in idx.items() if e["tipo"] == "englobante"], []
        )

    def test_nenhum_segmento_de_cadeia_alguma_usa_englobante(self):
        """O valor segue LEGÍVEL para que dado antigo não estoure; o que não
        pode é voltar. Sem esta prova, `englobante` é um convite a reintroduzir
        o erro de categoria — e o sintoma dele é o silêncio de R3."""
        for nome in self.cadeias():
            _, segmentos = carrega_cadeia(nome)
            for s in segmentos:
                self.assertNotIn(
                    s.tipo_indexador, TIPOS_RETIRADOS,
                    f"{nome}: {s.id} voltou a usar valor retirado",
                )

    def test_englobamento_da_selic_e_da_taxa_legal_segue_no_campo_engloba(self):
        """O que se retirou foi o fato de R1 gravado no campo de R3. R1 em si —
        § 7 de 00-base-normativa.md, NÃO alterada — continua lendo `engloba`."""
        selic = legal = 0
        for nome in self.cadeias():
            _, segmentos = carrega_cadeia(nome)
            for s in segmentos:
                if s.indexador == "Selic":
                    selic += 1
                    self.assertIn("correcao-monetaria", s.engloba, f"{nome}: {s.id}")
                    self.assertIn("juros-mora", s.engloba, f"{nome}: {s.id}")
                elif s.indexador == "taxa-legal":
                    legal += 1
                    self.assertIn("juros-mora", s.engloba, f"{nome}: {s.id}")
        self.assertGreaterEqual(selic, 14)
        self.assertGreaterEqual(legal, 5)

    def test_tres_segmentos_de_taxa_legal_nao_englobam_correcao(self):
        """ACHADO DO BLOCO 19, registrado e NÃO harmonizado.

        `engloba` não foi tocado — e é por não ter sido tocado que a assimetria
        aparece: dois segmentos de taxa legal declaram
        `['correcao-monetaria', 'juros-mora']` e três declaram só
        `['juros-mora']`, embora a § 7 trate a taxa legal como englobante dos
        dois. Não é efeito desta mudança; é dado pré-existente que o campo
        `tipo_indexador: englobante` encobria, porque o rótulo dizia
        'englobante' onde o `engloba` não englobava. Harmonizar exigiria fonte
        que diga qual das duas gravações está certa, e ela não foi localizada.
        """
        so_juros = []
        for nome in self.cadeias():
            _, segmentos = carrega_cadeia(nome)
            for s in segmentos:
                if s.indexador == "taxa-legal" and "correcao-monetaria" not in s.engloba:
                    so_juros.append((nome, s.inicio, s.fim))
        self.assertEqual(len(so_juros), 3, so_juros)

    def test_moedas_sao_nao_indexador(self):
        idx = self.catalogo()["indexadores"]
        for chave in ("Cruzado (Cz$)", "Cruzeiro novo (NCr$)", "Real (R$)",
                      "Conversão em URV"):
            self.assertEqual(idx[chave]["tipo"], "nao-indexador", chave)

    def test_os_quatro_nominais_literais_da_fonte(self):
        idx = self.catalogo()["indexadores"]
        for chave in ("Ufir", "BTN", "OTN", "ORTN"):
            self.assertEqual(idx[chave]["tipo"], "nominal", chave)
            self.assertIn("4.1.2.4", idx[chave]["fonte"])

    def test_os_percentuais_literais_da_fonte(self):
        idx = self.catalogo()["indexadores"]
        for chave in ("INPC", "IGP-DI"):
            self.assertEqual(idx[chave]["tipo"], "percentual", chave)
            self.assertIn("4.1.2.4", idx[chave]["fonte"])

    def test_igp_di_permanece_percentual_contra_a_tabela_externa(self):
        """A tabela externa do bloco 19 NÃO nomeia o IGP-DI; o item 4.1.2.4,
        letra b, o nomeia LITERALMENTE. 'Salvo se a fonte extraída disser o
        contrário' — e aqui ela diz. Divergência registrada, não harmonizada."""
        cat = self.catalogo()
        self.assertIn("IGP-DI", cat["fonte"]["literal"])
        self.assertEqual(cat["indexadores"]["IGP-DI"]["tipo"], "percentual")
        self.assertTrue(cat["indexadores"]["IGP-DI"].get("CONFERIDO_NO_BLOCO_19"))

    def test_ipc_nu_permanece_indeterminado_com_a_ambiguidade_registrada(self):
        """D8-C21 sustenta o IPC/IBGE. Classificar o 'IPC' nu por herança do
        irmão é a dedução proibida — o manual usa DOIS IPC, de emissores
        distintos, e o rótulo nu não diz qual."""
        idx = self.catalogo()["indexadores"]
        self.assertEqual(idx["IPC"]["tipo"], "indeterminado")
        self.assertEqual(idx["IPC"]["pendencia"], "P18-01")
        self.assertTrue(idx["IPC"].get("ambiguidade"))
        self.assertEqual(idx["IPC/IBGE"]["tipo"], "percentual")
        self.assertEqual(idx["IPC/FGV"]["tipo"], "indeterminado")

    def test_trd_nao_herda_a_razao_da_tr(self):
        """A fonte externa nomeia TBF, Redutor-R e TR — e NÃO a TRD. Herdar por
        nome parecido é exatamente o que a regra proíbe."""
        idx = self.catalogo()["indexadores"]
        self.assertEqual(idx["TRD"]["tipo"], "indeterminado")
        self.assertEqual(idx["TRD"]["pendencia"], "P18-01")
        self.assertFalse(idx["TRD"].get("razao"))
        self.assertIn("TRD", idx["TRD"]["por_que"])

    def test_segmento_composto_segue_registrado_como_tal(self):
        """`Ufir → Selic (bifurcado por fato gerador)` NÃO é índice e não se
        classifica: a cura é partir o segmento (P17-03)."""
        idx = self.catalogo()["indexadores"]
        e = idx["Ufir → Selic (bifurcado por fato gerador)"]
        self.assertEqual(e["tipo"], "indeterminado")
        self.assertEqual(e["pendencia"], "P17-03")
        self.assertEqual(idx["NAO-DECLARADO-PELO-MANUAL"]["pendencia"], "P9-02")


class TestMapeamentoBloco19(unittest.TestCase):
    """Os rótulos, mapeados UM A UM, e a contagem que o catálogo declara.

    Contagem cravada em prosa envelhece em silêncio — é a lição do manifesto de
    cadeias. Aqui ela é RECOMPUTADA do próprio repositório e conferida contra o
    que o catálogo afirma. Se o repositório crescer, este teste falha, e a
    falha é o pedido de atualizar o mapeamento.

    **Eram 34 rótulos em 15 cadeias** (bloco 19, tarefa 2). **São 36 em 20
    cadeias** desde a tarefa 3, que gerou cinco das oito cadeias de `P18-02` e
    trouxe dois rótulos novos, **ambos `indeterminado`**: `BTNF` (sem fonte,
    `P19-02`) e `UPC → índices básicos de atualização dos saldos da poupança`
    (segmento composto, `P17-03`). **O teste falhou, e foi assim que se soube.**
    """

    def catalogo(self):
        with open(CATALOGO, "r", encoding="utf-8") as fh:
            return json.load(fh)

    def rotulos(self):
        """Levantados do REPOSITÓRIO, não da tabela do enunciado."""
        achados = {}
        for ident, c in descobre_cadeias(TABELAS).items():
            _, segmentos = carrega_cadeia(c["arquivo"])
            for s in segmentos:
                achados[s.indexador or "(segmento sem indexador)"] = s.tipo_indexador
        return achados

    def test_sao_36_rotulos_e_todos_estao_no_catalogo(self):
        rot = self.rotulos()
        self.assertEqual(len(rot), 36, sorted(rot))
        idx = self.catalogo()["indexadores"]
        for chave, tipo in rot.items():
            self.assertIn(chave, idx, f"rótulo fora do catálogo: {chave}")
            self.assertEqual(idx[chave]["tipo"], tipo, chave)

    def test_totais_declarados_batem_com_o_repositorio(self):
        from collections import Counter
        contagem = Counter(self.rotulos().values())
        totais = self.catalogo()["MAPEAMENTO_BLOCO_19"]["totais"]
        self.assertEqual(totais["rotulos"], sum(contagem.values()))
        for classe in ("nominal", "percentual", "janela-deslocada",
                       "nao-indexador", "indeterminado", "englobante"):
            self.assertEqual(
                totais[classe], contagem.get(classe, 0),
                f"MAPEAMENTO_BLOCO_19.totais['{classe}'] não bate",
            )

    def test_a_contagem_de_segmentos_sem_indexador_bate_com_o_repositorio(self):
        """A contagem do '(segmento sem indexador)' SAIU do texto replicado.

        O campo `fonte` desse rótulo é copiado literalmente para dentro de cada
        segmento, em `tipo_indexador_fonte`. Enquanto a contagem morava lá, um
        número que envelhece ficava replicado dezenas de vezes nos JSON que o
        validador lê — e envelheceu: dizia '21 segmentos, em 6 cadeias' quando
        já eram 37 em 10. Agora `fonte` só carrega o que NÃO envelhece, a
        contagem vive em `quantos`, num lugar só, e este teste a confere.
        """
        entrada = self.catalogo()["indexadores"]["(segmento sem indexador)"]
        self.assertNotIn("segmentos, em", entrada["fonte"],
                         "contagem voltou para dentro do texto replicado")
        segmentos, cadeias = 0, set()
        for ident, c in descobre_cadeias(TABELAS).items():
            _, segs = carrega_cadeia(c["arquivo"])
            sem = [s for s in segs if not s.indexador]
            if sem:
                cadeias.add(ident)
                segmentos += len(sem)
        self.assertEqual(
            entrada["quantos"], f"{segmentos} segmentos, em {len(cadeias)} cadeias.",
            "'(segmento sem indexador)'.quantos não bate com o repositório",
        )

    def test_indeterminados_somam_por_razao(self):
        """13 sem fonte + 2 com razão + 2 segmentos compostos = 17."""
        mapa = self.catalogo()["MAPEAMENTO_BLOCO_19"]["indeterminado_por_razao"]
        sem_fonte = mapa["sem-fonte (fecha quando a fonte chegar)"]
        nao_cabe = mapa["fonte-diz-que-nao-cabe (NÃO fecha esperando fonte)"]
        composto = mapa["segmento-composto (P17-03)"]
        listados = sum(len(v) for v in sem_fonte["quais"].values())
        self.assertEqual(listados, sem_fonte["quantos"])
        self.assertEqual(len(nao_cabe["quais"]), nao_cabe["quantos"])
        total = sem_fonte["quantos"] + nao_cabe["quantos"] + composto["quantos"]
        self.assertEqual(
            total,
            self.catalogo()["MAPEAMENTO_BLOCO_19"]["totais"]["indeterminado"],
        )

    def test_cada_indeterminado_do_repositorio_esta_listado_em_alguma_razao(self):
        mapa = self.catalogo()["MAPEAMENTO_BLOCO_19"]["indeterminado_por_razao"]
        listados = set()
        for v in mapa["sem-fonte (fecha quando a fonte chegar)"]["quais"].values():
            listados.update(v)
        listados.update(
            mapa["fonte-diz-que-nao-cabe (NÃO fecha esperando fonte)"]["quais"]
        )
        listados.update(mapa["segmento-composto (P17-03)"]["quais"])
        no_repo = {k for k, t in self.rotulos().items() if t == "indeterminado"}
        self.assertEqual(no_repo - listados, set(), "indeterminado sem razão declarada")
        self.assertEqual(listados - no_repo, set(), "razão declarada sem rótulo no repo")

    def test_a_fonte_externa_esta_declarada_como_externa(self):
        """Disciplina do projeto: afirmação sem lastro no material extraído
        aparece como tal."""
        cat = self.catalogo()
        ext = cat["FONTE_EXTERNA_AO_CORPUS"]
        self.assertIn("NÃO foi extraído do corpus", ext["DECLARACAO"])
        for chave in ("IPCA-E/IBGE", "IPCA-15/IBGE", "TR",
                      "remuneração básica da caderneta de poupança (TR)", "Selic"):
            self.assertIn(
                "FONTE EXTERNA AO CORPUS", cat["indexadores"][chave]["fonte"], chave
            )


class TestManifestoDeCadeias(unittest.TestCase):
    """O manifesto tem de PEGAR a cadeia que some. Sem esta prova, ele é
    apenas um arquivo que concorda com o repositório."""

    def manifesto(self, **cadeias):
        return {"cadeias": cadeias}

    def test_cadeia_que_some_e_regressao(self):
        regressoes, _ = confere_manifesto(
            {"cjf.a": {"arquivo": "a.json", "componente": "cm", "segmentos": 3}},
            self.manifesto(
                **{
                    "cjf.a": {"arquivo": "a.json", "segmentos": 3},
                    "cjf.b": {"arquivo": "b.json", "segmentos": 4},
                }
            ),
        )
        self.assertEqual(len(regressoes), 1)
        self.assertIn("cjf.b", regressoes[0])
        self.assertIn("SUMIU", regressoes[0])

    def test_cadeia_a_mais_e_crescimento_nao_regressao(self):
        regressoes, novas = confere_manifesto(
            {
                "cjf.a": {"arquivo": "a.json", "componente": "cm", "segmentos": 3},
                "cjf.b": {"arquivo": "b.json", "componente": "jm", "segmentos": 4},
            },
            self.manifesto(**{"cjf.a": {"arquivo": "a.json", "segmentos": 3}}),
        )
        self.assertEqual(regressoes, [])
        self.assertEqual(novas, ["cjf.b"])

    def test_cadeia_que_encolhe_e_regressao(self):
        regressoes, _ = confere_manifesto(
            {"cjf.a": {"arquivo": "a.json", "componente": "cm", "segmentos": 2}},
            self.manifesto(**{"cjf.a": {"arquivo": "a.json", "segmentos": 5}}),
        )
        self.assertEqual(len(regressoes), 1)
        self.assertIn("ENCOLHEU", regressoes[0])

    def test_renomear_o_arquivo_nao_e_regressao(self):
        """A chave é o `id`. Foi renomeação que derrubou o bloco 17 de 11 para
        7; um manifesto indexado por nome de arquivo repetiria o erro com o
        sinal trocado — acusaria regressão onde houve só troca de rótulo."""
        regressoes, novas = confere_manifesto(
            {"trab.hist.juros-mora": {
                "arquivo": "OUTRO-NOME.json", "componente": "jm", "segmentos": 4}},
            self.manifesto(
                **{"trab.hist.juros-mora": {
                    "arquivo": "trt3.hist.juros-mora.json", "segmentos": 4}}
            ),
        )
        self.assertEqual(regressoes, [])
        self.assertEqual(novas, [])

    def test_manifesto_real_cobre_todas_as_cadeias_do_repositorio(self):
        achadas = descobre_cadeias(TABELAS)
        declarado = le_manifesto()["cadeias"]
        self.assertEqual(sorted(declarado), sorted(achadas),
                         "rode valida_cadeias.py para gravar o crescimento")

    def test_grava_manifesto_nunca_reduz(self):
        import tempfile
        from valida_cadeias import grava_manifesto
        with tempfile.TemporaryDirectory() as d:
            alvo = Path(d) / "m.json"
            grava_manifesto(
                {"cjf.a": {"arquivo": "a.json", "componente": "cm", "segmentos": 9}},
                alvo,
            )
            grava_manifesto(
                {"cjf.a": {"arquivo": "a.json", "componente": "cm", "segmentos": 2}},
                alvo,
            )
            with open(alvo, "r", encoding="utf-8") as fh:
                d2 = json.load(fh)
            self.assertEqual(d2["cadeias"]["cjf.a"]["segmentos"], 9)


class TestCadeiasBloco19Tarefa3(unittest.TestCase):
    """As cinco cadeias de `P18-02` geradas na tarefa 3 — e as três que NÃO.

    O que estes testes vigiam é a disciplina, não o conteúdo: que taxa ausente
    permaneça ausente, que `JCM` não vire rótulo de indexador, e que as três
    cadeias bloqueadas sigam com a razão declarada em lugar legível. Todo o
    resto já é coberto por R1/R2/R3 e pelo manifesto.
    """

    GERADAS = {
        "cjf.desapropriacao-indireta.correcao-monetaria.json": 11,
        "cjf.divida-fiscal.juros-mora.json": 8,
        "cjf.fgts-divida-fiscal.correcao-monetaria.json": 5,
        "cjf.desapropriacao-direta.juros-compensatorios.json": 3,
        "cjf.desapropriacao-indireta.juros-compensatorios.json": 3,
    }

    def test_as_cinco_existem_com_a_contagem_de_segmentos(self):
        for nome, n in self.GERADAS.items():
            dados, segmentos = carrega_cadeia(nome)
            self.assertEqual(len(segmentos), n, nome)
            self.assertEqual(dados["tipo"], "cadeia-temporal", nome)

    def test_todo_segmento_tem_pagina_pdf(self):
        """Regra da tarefa: todo segmento sai da fonte, com `pagina_pdf`."""
        for nome in self.GERADAS:
            dados, _ = carrega_cadeia(nome)
            for i, s in enumerate(dados["segmentos"]):
                self.assertIn("pagina_pdf", s, f"{nome} #{i}")

    def test_taxa_nao_extraida_continua_nula(self):
        """O buraco é o achado. Preenchê-lo com número seria inventar dado."""
        achados = 0
        for nome in ("cjf.desapropriacao-direta.juros-compensatorios.json",
                     "cjf.desapropriacao-indireta.juros-compensatorios.json"):
            dados, _ = carrega_cadeia(nome)
            for s in dados["segmentos"]:
                self.assertIsNone(s.get("taxa"), nome)
                if "taxa_nao_extraida" in s:
                    achados += 1
        self.assertEqual(achados, 4, "duas linhas por cadeia, duas cadeias")

    def test_ago_2017_nao_virou_segmento(self):
        """`D8-C25` — a taxa é o percentual dos TDAs de oferta inicial, valor
        do CASO. Não é tabulável, e a decisão fica gravada na cadeia."""
        for nome in ("cjf.desapropriacao-direta.juros-compensatorios.json",
                     "cjf.desapropriacao-indireta.juros-compensatorios.json"):
            dados, _ = carrega_cadeia(nome)
            self.assertIn("DECISAO_2_O_CORTE_DE_AGO_2017_NAO_E_TABULAVEL", dados)
            for s in dados["segmentos"]:
                self.assertNotIn(s["inicio"], ("2017-08", "2017-07"), nome)

    def test_n6_grava_a_tabela_e_registra_o_texto(self):
        """`N-6` — texto diz 'Até dez. 2021'; a tabela encerra em nov./2021.
        Grava-se a TABELA, e a contradição fica legível. Não se escolhe lado."""
        for nome in ("cjf.desapropriacao-direta.juros-compensatorios.json",
                     "cjf.desapropriacao-indireta.juros-compensatorios.json"):
            dados, _ = carrega_cadeia(nome)
            self.assertEqual(dados["segmentos"][1]["fim"], "2021-11", nome)
            self.assertIn("DECISAO_3_N_6_A_CONTRADICAO_DE_UM_MES", dados)

    def test_base_incidencia_esta_nos_segmentos_da_divida_fiscal(self):
        """`D8-C5` — a base alterna QUATRO vezes, e só a dívida fiscal a
        exercita. O schema a acomoda sem alteração do validador."""
        dados, _ = carrega_cadeia("cjf.divida-fiscal.juros-mora.json")
        bases = [s.get("base_incidencia") for s in dados["segmentos"]]
        self.assertEqual(
            [b for b in bases if b],
            ["valor-base trimestral do débito cor/mon.",
             "valor originário",
             "valor do débito cor/mon.",
             "valor originário",
             "valor do débito cor/mon.",
             "valor do débito cor/mon."],
        )

    def test_jcm_e_criterio_e_nao_rotulo_de_indexador(self):
        """Mesmo desenho do `JAM`: nome do critério vive em campo da cadeia."""
        dados, segmentos = carrega_cadeia(
            "cjf.fgts-divida-fiscal.correcao-monetaria.json")
        self.assertEqual(dados["criterio"], "JCM")
        for s in segmentos:
            self.assertNotIn("JCM", s.indexador)

    def test_o_fgts_fiscal_e_outra_cadeia_que_a_do_item_4_8(self):
        fiscal, _ = carrega_cadeia("cjf.fgts-divida-fiscal.correcao-monetaria.json")
        fundiario, _ = carrega_cadeia("cjf.fgts.correcao-monetaria.json")
        self.assertNotEqual(fiscal["id"], fundiario["id"])
        self.assertEqual(fiscal["fonte"]["item"], "2.4.4.1")
        self.assertEqual(fundiario["fonte"]["item"], "4.8.1.1")
        # O corte da ORTN difere: set./1983 aqui, fev./1986 lá.
        self.assertEqual(fiscal["segmentos"][0]["fim"], "1983-09")
        self.assertEqual(fundiario["segmentos"][0]["fim"], "1986-02")
        # E o corte de maio/2000 é DESTA cadeia; não alcança a de 4.8.
        self.assertIn("2000-05", [s["inicio"] for s in fiscal["segmentos"]])
        self.assertNotIn("2000-05", [s["inicio"] for s in fundiario["segmentos"]])

    def test_a_indireta_de_correcao_e_derivada_da_direta(self):
        """Duas cadeias, e a duplicação é DERIVADA — é o que impede divergirem."""
        ind, seg_i = carrega_cadeia("cjf.desapropriacao-indireta.correcao-monetaria.json")
        dir_, seg_d = carrega_cadeia("cjf.desapropriacao-direta.correcao-monetaria.json")
        self.assertIn("DERIVADA_DE", ind)
        self.assertIn("DECISAO_1_DUAS_CADEIAS_E_NAO_UMA_COM_DOIS_ESCOPOS", ind)
        self.assertEqual([(s.inicio, s.fim, s.indexador) for s in seg_i],
                         [(s.inicio, s.fim, s.indexador) for s in seg_d])
        self.assertNotEqual(ind["termo_inicial"], dir_["termo_inicial"])
        self.assertTrue(all(s["pagina_pdf"] == 73 for s in ind["segmentos"]))

    def test_as_tres_bloqueadas_tem_razao_declarada(self):
        from gera_cadeias_bloco19 import BLOQUEADAS
        self.assertEqual(len(BLOQUEADAS), 3)
        for chave, v in BLOQUEADAS.items():
            self.assertTrue(v["veredito"], chave)
            self.assertGreater(len(v["por_que"]), 200, chave)
        # 4.7.1 NÃO é lacuna: o manual DELEGA ao TST. Registra-se a delegação.
        quatro_sete = [k for k in BLOQUEADAS if k.startswith("4.7.1")][0]
        self.assertIn("DELEGA", BLOQUEADAS[quatro_sete]["por_que"])
        self.assertIn("NÃO É LACUNA", BLOQUEADAS[quatro_sete]["veredito"])

    def test_nenhum_float_nos_arquivos_gerados(self):
        """R12 — nenhum `float` em caminho algum."""
        def varre(o, onde):
            if isinstance(o, float):
                self.fail(f"float em {onde}")
            if isinstance(o, dict):
                for k, v in o.items():
                    varre(v, f"{onde}.{k}")
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    varre(v, f"{onde}[{i}]")
        for nome in self.GERADAS:
            with open(TABELAS / nome, "r", encoding="utf-8") as fh:
                varre(json.load(fh), nome)


if __name__ == "__main__":
    unittest.main(verbosity=2)
