"""Testes de valida_cobertura.py — invariantes R1, R2 e R3."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from valida_cadeias import confere_manifesto, descobre_cadeias, le_manifesto
from valida_cobertura import (
    TIPOS_DE_INDEXADOR,
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
TABELAS = RAIZ / "docs" / "calculo" / "tabelas-normativas"
CATALOGO = TABELAS / "indexadores-tipo-catalogo.json"


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
         engloba=()):
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

    def test_dominio_tem_exatamente_cinco_valores(self):
        self.assertEqual(
            TIPOS_DE_INDEXADOR,
            {"nominal", "percentual", "englobante", "nao-indexador", "indeterminado"},
        )


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

    def test_classificado_tem_fonte_e_indeterminado_tem_pendencia(self):
        idx = self.catalogo()["indexadores"]
        for chave, e in idx.items():
            if e["tipo"] == "indeterminado":
                self.assertIsNone(e.get("fonte"), chave)
                self.assertTrue(
                    e.get("pendencia"), f"{chave}: indeterminado sem pendência"
                )
            else:
                self.assertTrue(e.get("fonte"), f"{chave}: classificado sem fonte")

    def test_ipca_e_continua_indeterminado(self):
        """A regra dura do bloco 17. 'IPCA-E é percentual porque IPCA é
        percentual' é a dedução proibida: o item 4.1.2.4 não nomeia nem um
        nem outro."""
        idx = self.catalogo()["indexadores"]
        for chave in ("IPCA-E/IBGE", "IPCA-15/IBGE", "IPCA série especial"):
            self.assertEqual(idx[chave]["tipo"], "indeterminado", chave)

    def test_selic_e_taxa_legal_sao_englobantes(self):
        idx = self.catalogo()["indexadores"]
        self.assertEqual(idx["Selic"]["tipo"], "englobante")
        self.assertEqual(idx["taxa-legal"]["tipo"], "englobante")

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
