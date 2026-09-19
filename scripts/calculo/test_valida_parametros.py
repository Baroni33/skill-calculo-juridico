"""Testes da camada de resolução de parâmetros negociáveis.

Cobre os seis casos pedidos no bloco 5, a consistência do catálogo consolidado, as
invariantes R14 a R18 e a classificação pelo art. 611-B da CLT.

O caso 6 — cadeia temporal do adicional de HE — é exercitado em duas frentes: o
mecanismo, com a fixture sintética de três faixas; e o ACT Gasmig, com os valores
reais que `02-base-normativa-verbas.md` traz. Os intervalos de competência das três
faixas do ACT não constam do documento, e o teste correspondente afirma essa lacuna
em vez de escondê-la.
"""

from __future__ import annotations

import json
import unittest
from decimal import Decimal
from pathlib import Path

from valida_parametros import (
    COBERTURA_COM,
    COBERTURA_CONFLITO,
    COBERTURA_REJEITADO,
    COBERTURA_SEM,
    COBERTURA_SEM_DEFAULT,
    ORIGEM_COLETIVA,
    ORIGEM_DEFAULT,
    ORIGEM_TITULO,
    ORIGEM_USUARIO,
    Catalogo,
    ErroDeDados,
    Instrumentos,
    competencia_para_indice,
    resolve,
    resolve_serie,
)

RAIZ = Path(__file__).resolve().parents[2]
FIXTURES = RAIZ / "tests" / "fixtures" / "calculo"
SINTETICO = FIXTURES / "instrumentos-sinteticos.json"
GASMIG = FIXTURES / "instrumentos-act-gasmig.json"


def gasmig() -> Instrumentos:
    return Instrumentos.de_arquivos(GASMIG)


def catalogo() -> Catalogo:
    return Catalogo.de_arquivo()


def instrumentos() -> Instrumentos:
    return Instrumentos.de_arquivos(SINTETICO)


# --------------------------------------------------------------------------

class TestCatalogo(unittest.TestCase):
    def test_catalogo_carrega_e_e_consistente(self):
        cat = catalogo()
        self.assertGreater(len(cat.parametros), 0)
        self.assertEqual(cat.valida(), [], "catálogo com inconsistência interna")

    def test_todo_parametro_com_piso_e_apenas_elevacao(self):
        """R18 só faz sentido se piso e regime de alteração andarem juntos."""
        for p in catalogo().parametros.values():
            if p.alteracao == "apenas-elevacao":
                self.assertIsNotNone(p.piso_legal, f"{p.id}: apenas-elevacao sem piso")

    def test_derivado_nao_e_parametro_negociavel(self):
        """O divisor sai da jornada; aceitá-lo avulso permite par inconsistente."""
        divisor = catalogo()["pn.jornada.divisor"]
        self.assertEqual(divisor.alteracao, "derivado")
        self.assertIn("pn.jornada.semanal", divisor.derivado_de)

    def test_parametro_desconhecido_levanta(self):
        with self.assertRaises(ErroDeDados):
            catalogo()["pn.inexistente"]


class TestCompetencia(unittest.TestCase):
    def test_indice_e_monotonico(self):
        self.assertEqual(
            competencia_para_indice("2025-02") - competencia_para_indice("2025-01"), 1
        )
        self.assertEqual(
            competencia_para_indice("2026-01") - competencia_para_indice("2025-12"), 1
        )

    def test_forma_invalida_levanta(self):
        for ruim in ("2025/01", "2025-13", "202501", "", "jan/2025"):
            with self.assertRaises(ErroDeDados, msg=ruim):
                competencia_para_indice(ruim)


# --------------------------------------------------------------------------
# Caso 1 — resolução com instrumento vigente encontrado
# --------------------------------------------------------------------------

class TestResolucaoComInstrumento(unittest.TestCase):
    def test_encontra_clausula_vigente(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2024-08",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "60")
        self.assertEqual(r.origem, ORIGEM_COLETIVA)
        self.assertEqual(r.cobertura, COBERTURA_COM)
        self.assertTrue(r.tem_cobertura)

    def test_R15_proveniencia_completa(self):
        """Toda parcela grava qual instrumento governou o parâmetro."""
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2024-08",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        p = r.proveniencia
        self.assertEqual(p["instrumento"], "sintetico.cct-alfa.2024-2026")
        self.assertEqual(p["clausula"], "10.1")
        self.assertEqual(p["vigencia"], ("2024-05", "2025-04"))
        self.assertTrue(p["texto"])

    def test_R15_proveniencia_tambem_no_default(self):
        """Quando cai no default, a proveniência aponta a fonte legal."""
        r = resolve(
            "pn.he.adicional", "categoria-sem-instrumento", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertIn("CF art. 7º", r.proveniencia["fonte"])

    def test_extensao_de_categoria_e_marcada(self):
        """Instrumento que alcança categoria cujo sindicato não negociou."""
        r = resolve(
            "pn.he.adicional", "beta-administrativo", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "75")
        self.assertTrue(
            r.proveniencia["por_extensao"],
            "extensão precisa ser sinalizada: sua força vinculante é mais discutível",
        )

    def test_categoria_signataria_nao_e_marcada_como_extensao(self):
        r = resolve(
            "pn.he.adicional", "beta-operacao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "75")
        self.assertFalse(r.proveniencia["por_extensao"])

    def test_R17_categoria_separa_resolucoes(self):
        """Mesma competência, categorias distintas, resultados distintos."""
        alfa = resolve("pn.he.adicional", "alfa-producao", "2024-08",
                       instrumentos=instrumentos(), catalogo=catalogo())
        beta = resolve("pn.he.adicional", "beta-operacao", "2025-06",
                       instrumentos=instrumentos(), catalogo=catalogo())
        self.assertNotEqual(alfa.valor, beta.valor)

    def test_variante_resolve_como_variante(self):
        r = resolve(
            "pn.insalubridade.base", "alfa-producao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "base-convencional")
        self.assertIn(r.valor, catalogo()["pn.insalubridade.base"].variantes)

    def test_rsr_ampliado_por_autonomia_sindical(self):
        """IRR-849, tese 1 — ampliação do número de dias de RSR."""
        r = resolve(
            "pn.rsr.dias", "beta-operacao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "2")
        self.assertEqual(r.cobertura, COBERTURA_COM)


# --------------------------------------------------------------------------
# Caso 2 — sem instrumento → fallback com marcação (R14)
# --------------------------------------------------------------------------

class TestFallback(unittest.TestCase):
    def test_R14_sem_instrumento_nao_e_erro(self):
        r = resolve(
            "pn.he.adicional", "categoria-inexistente", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "50")
        self.assertEqual(r.origem, ORIGEM_DEFAULT)
        self.assertEqual(r.cobertura, COBERTURA_SEM)
        self.assertFalse(r.tem_cobertura)
        self.assertTrue(r.calculavel, "fallback é calculável, só não tem cobertura")

    def test_R14_sem_camada_alguma_tambem_resolve(self):
        """Nenhum instrumento cadastrado no sistema inteiro."""
        r = resolve("pn.he.adicional", "qualquer", "2025-06", catalogo=catalogo())
        self.assertEqual(r.valor, "50")
        self.assertEqual(r.cobertura, COBERTURA_SEM)

    def test_parametro_sem_default_legal_nao_cai_em_lugar_nenhum(self):
        """pn.ajuda-alimentacao.valor não tem default: a verba fica pendente de dado."""
        r = resolve(
            "pn.ajuda-alimentacao.valor", "categoria-inexistente", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertIsNone(r.valor)
        self.assertEqual(r.cobertura, COBERTURA_SEM_DEFAULT)
        self.assertFalse(r.calculavel)

    def test_mesmo_parametro_com_instrumento_resolve(self):
        r = resolve(
            "pn.ajuda-alimentacao.valor", "alfa-producao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "32.50")
        self.assertEqual(r.cobertura, COBERTURA_COM)


# --------------------------------------------------------------------------
# Caso 3 — competência anterior ao instrumento mais antigo
# --------------------------------------------------------------------------

class TestForaDaVigencia(unittest.TestCase):
    def test_competencia_anterior_cai_no_default(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2019-03",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "50")
        self.assertEqual(r.cobertura, COBERTURA_SEM)

    def test_competencia_posterior_cai_no_default(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2030-01",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.cobertura, COBERTURA_SEM)

    def test_bordas_da_vigencia_sao_inclusivas(self):
        for competencia in ("2024-05", "2025-04"):
            r = resolve("pn.he.adicional", "alfa-manutencao", competencia,
                        instrumentos=instrumentos(), catalogo=catalogo())
            self.assertEqual(r.valor, "60", f"borda {competencia}")

    def test_um_mes_antes_da_borda_ja_esta_fora(self):
        r = resolve("pn.he.adicional", "alfa-manutencao", "2024-04",
                    instrumentos=instrumentos(), catalogo=catalogo())
        self.assertEqual(r.cobertura, COBERTURA_SEM)

    def test_contrato_atravessa_vigencia_mes_a_mes(self):
        """R17 — cada competência resolve com o instrumento vigente naquela data."""
        serie = resolve_serie(
            "pn.he.adicional", "alfa-manutencao",
            ["2024-03", "2024-05", "2025-06", "2026-05"],
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual([r.valor for r in serie], ["50", "60", "70", "50"])
        self.assertEqual(
            [r.cobertura for r in serie],
            [COBERTURA_SEM, COBERTURA_COM, COBERTURA_COM, COBERTURA_SEM],
        )


# --------------------------------------------------------------------------
# Caso 4 — valor abaixo do piso legal (R18)
# --------------------------------------------------------------------------

class TestPisoLegal(unittest.TestCase):
    def test_R18_clausula_abaixo_do_piso_e_rejeitada(self):
        r = resolve(
            "pn.he.adicional", "delta-servicos", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertTrue(r.rejeicoes, "a rejeição tem de aparecer")
        self.assertEqual(r.rejeicoes[0]["valor_negociado"], "40")
        self.assertEqual(r.rejeicoes[0]["piso_legal"], "50")

    def test_R18_nao_corrige_silenciosamente_para_o_piso(self):
        """Rejeita e reporta. Corrigir esconderia defeito do cadastro."""
        r = resolve(
            "pn.he.adicional", "delta-servicos", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.valor, "50")
        self.assertEqual(r.origem, ORIGEM_DEFAULT)
        self.assertEqual(
            r.cobertura, COBERTURA_SEM,
            "cláusula inválida não produz cobertura coletiva",
        )

    def test_R18_vale_para_o_adicional_noturno(self):
        r = resolve(
            "pn.noturno.adicional", "delta-servicos", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertTrue(r.rejeicoes)
        self.assertEqual(r.valor, "20")

    def test_R18_valor_igual_ao_piso_e_aceito(self):
        r = resolve(
            "pn.he.adicional", "qualquer", "2025-06",
            catalogo=catalogo(), escolha_usuario="50",
        )
        self.assertEqual(r.rejeicoes, [])
        self.assertEqual(r.valor, "50")

    def test_R18_escolha_do_usuario_abaixo_do_piso_e_rejeitada(self):
        r = resolve(
            "pn.he.adicional", "qualquer", "2025-06",
            catalogo=catalogo(), escolha_usuario="30",
        )
        self.assertEqual(r.cobertura, COBERTURA_REJEITADO)
        self.assertIsNone(r.valor)

    def test_R18_titulo_judicial_nao_e_barrado_pelo_piso(self):
        """R16 põe o título acima; cabe ao juízo, não ao motor, aplicar a lei."""
        r = resolve(
            "pn.he.adicional", "qualquer", "2025-06",
            catalogo=catalogo(), titulo_judicial="40",
        )
        self.assertEqual(r.valor, "40")
        self.assertEqual(r.origem, ORIGEM_TITULO)
        self.assertEqual(r.rejeicoes, [])

    def test_piso_nao_se_aplica_a_parametro_de_alteracao_qualquer(self):
        r = resolve(
            "pn.comissoes.periodo-da-media", "qualquer", "2025-06",
            catalogo=catalogo(), escolha_usuario="6",
        )
        self.assertEqual(r.valor, "6")
        self.assertEqual(r.rejeicoes, [])


# --------------------------------------------------------------------------
# Caso 5 — dois instrumentos aplicáveis → conflito reportado
# --------------------------------------------------------------------------

class TestConflito(unittest.TestCase):
    def test_dois_instrumentos_geram_conflito(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.cobertura, COBERTURA_CONFLITO)
        self.assertEqual(len(r.conflitos), 2)

    def test_conflito_nao_escolhe_por_heuristica(self):
        """Nem o mais recente, nem o mais favorável, nem o mais específico."""
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertIsNone(r.valor)
        self.assertFalse(r.calculavel)
        instrumentos_no_conflito = {c["instrumento"] for c in r.conflitos}
        self.assertEqual(
            instrumentos_no_conflito,
            {"sintetico.cct-alfa.2024-2026", "sintetico.cct-gama.2025-2026"},
        )

    def test_conflito_lista_valores_para_decisao_humana(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual({c["valor"] for c in r.conflitos}, {"70", "65"})

    def test_fora_do_periodo_de_sobreposicao_nao_ha_conflito(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2024-08",
            instrumentos=instrumentos(), catalogo=catalogo(),
        )
        self.assertEqual(r.cobertura, COBERTURA_COM)

    def test_clausulas_sobrepostas_no_mesmo_instrumento_sao_erro_de_dados(self):
        """Defeito de cadastro, não conflito normativo — precisa quebrar."""
        dados = json.loads(SINTETICO.read_text(encoding="utf-8"))
        inst = dados["instrumentos"][0]
        inst["clausulas"].append(
            {
                "clausula": "10.1-bis",
                "parametro": "pn.he.adicional",
                "valor": "99",
                "forma": "percentual",
                "vigencia_propria": {"inicio": "2024-05", "fim": "2025-04"},
                "texto": "SINTÉTICO — sobreposição proposital",
            }
        )
        with self.assertRaises(ErroDeDados):
            resolve(
                "pn.he.adicional", "alfa-producao", "2024-08",
                instrumentos=Instrumentos(dados), catalogo=catalogo(),
            )


# --------------------------------------------------------------------------
# Precedência (R16)
# --------------------------------------------------------------------------

class TestPrecedencia(unittest.TestCase):
    def test_titulo_vence_norma_coletiva(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2024-08",
            instrumentos=instrumentos(), catalogo=catalogo(),
            titulo_judicial="100",
        )
        self.assertEqual(r.valor, "100")
        self.assertEqual(r.origem, ORIGEM_TITULO)

    def test_norma_coletiva_vence_escolha_do_usuario(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2024-08",
            instrumentos=instrumentos(), catalogo=catalogo(),
            escolha_usuario="55",
        )
        self.assertEqual(r.valor, "60")
        self.assertEqual(r.origem, ORIGEM_COLETIVA)

    def test_escolha_do_usuario_vence_default(self):
        r = resolve(
            "pn.he.adicional", "sem-instrumento", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
            escolha_usuario="55",
        )
        self.assertEqual(r.valor, "55")
        self.assertEqual(r.origem, ORIGEM_USUARIO)

    def test_R16_divergencia_e_registrada_nao_silenciada(self):
        r = resolve(
            "pn.he.adicional", "alfa-producao", "2024-08",
            instrumentos=instrumentos(), catalogo=catalogo(),
            titulo_judicial="100", escolha_usuario="55",
        )
        self.assertEqual(r.valor, "100")
        niveis = {d["nivel_divergente"] for d in r.divergencias}
        self.assertEqual(niveis, {ORIGEM_COLETIVA, ORIGEM_USUARIO, ORIGEM_DEFAULT})

    def test_sem_divergencia_quando_niveis_coincidem(self):
        r = resolve(
            "pn.he.adicional", "sem-instrumento", "2025-06",
            instrumentos=instrumentos(), catalogo=catalogo(),
            escolha_usuario="50",
        )
        self.assertEqual(r.divergencias, [])


# --------------------------------------------------------------------------
# Caso 6 — cadeia temporal de adicional de HE
# --------------------------------------------------------------------------

class TestCadeiaTemporal(unittest.TestCase):
    def test_tres_faixas_no_mesmo_instrumento(self):
        """Mecanismo das faixas temporais internas — com fixture sintética.

        É o mesmo caminho que o ACT Gasmig exercitaria; os dados é que são outros.
        A categoria alfa-manutencao é alcançada só pela CCT Alfa, de modo que a
        cadeia se resolve sem cair no conflito com a Gama.
        """
        casos = [
            ("2024-06", "60", "10.1"),
            ("2025-04", "60", "10.1"),
            ("2025-05", "70", "10.2"),
            ("2025-12", "70", "10.2"),
            ("2026-01", "80", "10.3"),
            ("2026-04", "80", "10.3"),
        ]
        for competencia, esperado, clausula in casos:
            with self.subTest(competencia=competencia):
                r = resolve(
                    "pn.he.adicional", "alfa-manutencao", competencia,
                    instrumentos=instrumentos(), catalogo=catalogo(),
                )
                self.assertEqual(r.cobertura, COBERTURA_COM)
                self.assertEqual(r.valor, esperado)
                self.assertEqual(r.proveniencia["clausula"], clausula)

    def test_a_mesma_competencia_muda_de_faixa_conforme_a_categoria(self):
        """R17 na prática: alfa-manutencao resolve, alfa-producao entra em conflito."""
        livre = resolve("pn.he.adicional", "alfa-manutencao", "2025-06",
                        instrumentos=instrumentos(), catalogo=catalogo())
        disputada = resolve("pn.he.adicional", "alfa-producao", "2025-06",
                            instrumentos=instrumentos(), catalogo=catalogo())
        self.assertEqual(livre.valor, "70")
        self.assertEqual(disputada.cobertura, COBERTURA_CONFLITO)

    def test_faixas_nao_deixam_buraco_dentro_da_vigencia(self):
        """As três faixas da CCT Alfa cobrem a vigência inteira, sem lacuna."""
        dados = json.loads(SINTETICO.read_text(encoding="utf-8"))
        alfa = dados["instrumentos"][0]
        faixas = [
            (c["vigencia_propria"]["inicio"], c["vigencia_propria"]["fim"])
            for c in alfa["clausulas"]
            if c["parametro"] == "pn.he.adicional"
        ]
        faixas.sort(key=lambda f: competencia_para_indice(f[0]))
        self.assertEqual(faixas[0][0], alfa["vigencia"]["inicio"])
        self.assertEqual(faixas[-1][1], alfa["vigencia"]["fim"])
        for anterior, seguinte in zip(faixas, faixas[1:]):
            self.assertEqual(
                competencia_para_indice(seguinte[0]),
                competencia_para_indice(anterior[1]) + 1,
                f"lacuna ou sobreposição entre {anterior} e {seguinte}",
            )

    def test_act_gasmig_resolve_os_parametros_cadastrados(self):
        """Caso 6 com dados reais: o que a base normativa traz, resolve."""
        casos = [
            ("pn.jornada.semanal", "40"),
            ("pn.he.adicional-domingos-feriados", "100"),
            ("pn.jornada.turno-ininterrupto", "enquadrado"),
            ("pn.turno.setima-e-oitava-horas", "normais"),
            ("pn.ferias.particao", "3"),
            ("pn.he.banco-de-horas", "banco-convencional"),
        ]
        for parametro, esperado in casos:
            with self.subTest(parametro=parametro):
                r = resolve(parametro, "gasmig-sitramico", "2026-03",
                            instrumentos=gasmig(), catalogo=catalogo())
                self.assertEqual(r.valor, esperado)
                self.assertEqual(r.cobertura, COBERTURA_COM)
                self.assertEqual(r.proveniencia["instrumento"], "act.gasmig.2025-2027")

    def test_act_gasmig_jornada_de_40h_implica_divisor_200(self):
        """O divisor é derivado, não cadastrado: 40/6 × 30 = 200 (Súmula 431)."""
        jornada = resolve("pn.jornada.semanal", "gasmig-sitramico", "2026-03",
                          instrumentos=gasmig(), catalogo=catalogo())
        self.assertEqual(jornada.valor, "40")

        divisor = catalogo()["pn.jornada.divisor"]
        self.assertEqual(divisor.alteracao, "derivado")
        self.assertFalse(divisor.sobrescrevivel)
        self.assertEqual(
            (Decimal(jornada.valor) / 6 * 30).to_integral_value(), Decimal(200)
        )

        # E não está cadastrado como cláusula: derivado nunca é valor cadastrável.
        cadastrados = {
            c["parametro"]
            for i in json.loads(GASMIG.read_text(encoding="utf-8"))["instrumentos"]
            for c in i["clausulas"]
        }
        self.assertNotIn("pn.jornada.divisor", cadastrados)

    def test_act_gasmig_setima_e_oitava_horas_e_o_ponto_de_litigio(self):
        """A cláusula é aplicada; a nulidade é do juízo, não do motor."""
        r = resolve("pn.turno.setima-e-oitava-horas", "gasmig-sitramico", "2026-03",
                    instrumentos=gasmig(), catalogo=catalogo())
        self.assertEqual(r.valor, "normais")
        self.assertEqual(catalogo()["pn.turno.setima-e-oitava-horas"].default_legal,
                         "extras")
        # Divergência com o default é registrada, não silenciada (R16).
        self.assertTrue(any(d["nivel_divergente"] == ORIGEM_DEFAULT
                            for d in r.divergencias))

    def test_act_gasmig_tres_faixas_de_he_declaradas_sem_datas(self):
        """A lacuna que resta do caso 6, afirmada em vez de escondida.

        `02-base-normativa-verbas.md` § 10 dá os três percentuais — 80, 75 e 60 —
        e a palavra "por período", sem os intervalos. Cadastrar três cláusulas do
        mesmo parâmetro sem `vigencia_propria` produziria sobreposição, que o
        resolvedor trata como defeito de cadastro. Supor as datas seria pior.
        """
        dados = json.loads(GASMIG.read_text(encoding="utf-8"))
        pendentes = {
            d["parametro"]: d for d in dados["parametros_declarados_sem_valor_completo"]
        }
        he = pendentes["pn.he.adicional"]
        self.assertEqual(he["valores_conhecidos"], ["80", "75", "60"])

        cadastrados = {c["parametro"] for i in dados["instrumentos"]
                       for c in i["clausulas"]}
        self.assertNotIn("pn.he.adicional", cadastrados)

        # Consequência prática: cai no default legal, muito abaixo do real.
        r = resolve("pn.he.adicional", "gasmig-sitramico", "2026-03",
                    instrumentos=gasmig(), catalogo=catalogo())
        self.assertEqual(r.valor, "50")
        self.assertEqual(r.cobertura, COBERTURA_SEM)

    def test_act_gasmig_he_noturna_e_derivado_sobrescrevivel(self):
        """O ACT fixa percentual direto; o default compõe 1,20 × 1,50 = 80."""
        p = catalogo()["pn.he.adicional-noturna"]
        self.assertTrue(p.sobrescrevivel)
        self.assertEqual(p.default_legal, "80")
        self.assertEqual(
            ((Decimal("1.20") * Decimal("1.50") - 1) * 100).to_integral_value(),
            Decimal(80),
        )
        # Valor do ACT desconhecido: não cadastrado, resolve pelo derivado.
        r = resolve("pn.he.adicional-noturna", "gasmig-sitramico", "2026-03",
                    instrumentos=gasmig(), catalogo=catalogo())
        self.assertEqual(r.valor, "80")
        self.assertEqual(r.cobertura, COBERTURA_SEM)


# --------------------------------------------------------------------------
# Classificação pelo art. 611-B da CLT
# --------------------------------------------------------------------------

class TestClassificacao611B(unittest.TestCase):
    def test_inciso_XVIII_torna_insalubridade_e_periculosidade_apenas_elevacao(self):
        """A âncora é a vedação de redução, não a redação 'no mínimo'."""
        for pid in ("pn.insalubridade.base", "pn.insalubridade.percentual",
                    "pn.periculosidade.base", "pn.periculosidade.percentual"):
            with self.subTest(parametro=pid):
                p = catalogo()[pid]
                self.assertEqual(p.fundamento_611b, "inciso-XVIII")
                self.assertEqual(p.alteracao, "apenas-elevacao")
                self.assertFalse(p.classificacao_provisoria)

    def test_periculosidade_entrou_apesar_de_nao_ter_no_minimo_no_texto(self):
        """Dúvida 1 do bloco 5, resolvida pelo inciso XVIII."""
        p = catalogo()["pn.periculosidade.percentual"]
        self.assertEqual(p.default_legal, "30")
        self.assertEqual(p.piso_legal, "30")
        self.assertIn("dúvida 1", p.bruto["duvida_resolvida"].lower())

    def test_inciso_VI_alcanca_o_trabalho_noturno(self):
        for pid in ("pn.noturno.adicional", "pn.he.adicional-noturna"):
            with self.subTest(parametro=pid):
                p = catalogo()[pid]
                self.assertEqual(p.fundamento_611b, "inciso-VI")
                self.assertEqual(p.alteracao, "apenas-elevacao")

    def test_paragrafo_unico_libera_duracao_do_trabalho_e_intervalos(self):
        """Duração e intervalos NÃO são normas de saúde para este fim."""
        for pid in ("pn.jornada.semanal", "pn.he.regime-de-compensacao",
                    "pn.he.banco-de-horas", "pn.jornada.turno-ininterrupto",
                    "pn.turno.setima-e-oitava-horas", "pn.sobreaviso.fator",
                    "pn.prontidao.fator"):
            with self.subTest(parametro=pid):
                p = catalogo()[pid]
                self.assertEqual(p.fundamento_611b, "paragrafo-unico")
                self.assertEqual(p.alteracao, "qualquer")

    def test_sobreaviso_e_prontidao_sao_duracao_do_trabalho(self):
        """Dúvida 2 do bloco 5, resolvida pelo parágrafo único."""
        self.assertEqual(catalogo()["pn.sobreaviso.fator"].default_legal, "1/3")
        self.assertEqual(catalogo()["pn.prontidao.fator"].default_legal, "2/3")

    def test_ressalva_do_inciso_XVII_nao_muda_o_calculo(self):
        """O corte não é absoluto, mas a nulidade é do juízo."""
        cat = catalogo()
        com_ressalva = [p for p in cat.parametros.values()
                        if p.bruto.get("ressalva_611b_xvii")]
        self.assertTrue(com_ressalva, "a ressalva precisa estar marcada em algum lugar")
        for p in com_ressalva:
            self.assertEqual(
                p.alteracao, "qualquer",
                "a ressalva não muda a classificação — só alerta para o mérito",
            )
        ressalva = cat.dados["classificacao_611b"]["ressalva_do_paragrafo_unico"]
        self.assertIn("NENHUM", ressalva["efeito_no_motor"])

    def test_os_27_incisos_nao_lidos_estao_declarados_como_lacuna(self):
        lacuna = catalogo().dados["classificacao_611b"]["LACUNA"]
        self.assertIn("trinta incisos", lacuna["descricao"])
        self.assertIn("NÃO ESTÁ NO CORPUS", lacuna["descricao"])

    def test_a_origem_da_classificacao_611b_e_declarada(self):
        """O fundamento veio de instrução, não do corpus. Dizer isso não é opcional.

        Quem auditar o catálogo contra o corpus não vai achar o art. 611-B. Se o
        catálogo dissesse "conferido", a auditoria concluiria que foi inventado —
        e estaria certa quanto à forma.
        """
        c = catalogo().dados["classificacao_611b"]
        origem = c["ORIGEM_DESTE_BLOCO"]
        self.assertIn("INSTRUÇÃO DIRETA DO USUÁRIO", origem["de_onde_vem"])
        self.assertIn("SEM transcrição", origem["o_que_o_corpus_tem"])
        # A chave não pode voltar a chamar-se "conferidos".
        self.assertNotIn("incisos_conferidos", c)
        self.assertEqual(
            set(c["incisos_fornecidos_por_instrucao"]), {"VI", "XVII", "XVIII"}
        )
        # A ressalva do TST também é instrução, e sem referência.
        self.assertIn(
            "INSTRUÇÃO DO USUÁRIO",
            c["ressalva_do_paragrafo_unico"]["origem"],
        )

    def test_nao_mapeado_implica_classificacao_provisoria(self):
        cat = catalogo()
        for p in cat.por_fundamento_611b("nao-mapeado"):
            self.assertTrue(
                p.classificacao_provisoria,
                f"{p.id}: sem inciso conferido, a classificação é provisória",
            )
        self.assertEqual(len(cat.provisorios()), len(cat.por_fundamento_611b("nao-mapeado")))


# --------------------------------------------------------------------------
# Parâmetros derivados
# --------------------------------------------------------------------------

class TestDerivados(unittest.TestCase):
    def test_nenhuma_variante_embute_um_derivado(self):
        """Divisor dentro do nome de uma variante contradiz a derivação.

        A variante do turno chamava-se 'enquadrado-sexta-diaria-divisor-180' e
        afirmava, para a Gasmig, um divisor que o próprio corpus contradiz: 40h
        semanais dão 200 pela Súmula 431.
        """
        derivados = {p.id.rsplit(".", 1)[-1] for p in catalogo().parametros.values()
                     if p.derivado}
        for p in catalogo().parametros.values():
            for v in p.bruto.get("variantes", ()):
                for nome in derivados:
                    self.assertNotIn(
                        nome, v, f"{p.id}: variante {v!r} embute o derivado {nome!r}"
                    )

    def test_todo_derivado_tem_formula(self):
        for p in catalogo().parametros.values():
            if p.derivado_de:
                self.assertTrue(
                    p.derivacao.get("formula"),
                    f"{p.id}: derivado sem fórmula — nunca como valor cadastrável",
                )

    def test_divisor_nao_e_sobrescrevivel(self):
        p = catalogo()["pn.jornada.divisor"]
        self.assertFalse(p.sobrescrevivel)
        self.assertEqual(p.fundamento_611b, "derivado-nao-se-negocia")

    def test_he_noturna_e_o_unico_derivado_sobrescrevivel(self):
        sobrescreviveis = [p.id for p in catalogo().parametros.values()
                           if p.sobrescrevivel]
        self.assertEqual(sobrescreviveis, ["pn.he.adicional-noturna"])

    def test_consolidacao_nao_duplicou_parametros(self):
        cat = catalogo()
        self.assertEqual(len(cat.parametros), len(set(cat.parametros)))
        origens = {
            o for p in cat.parametros.values()
            for o in p.bruto.get("origem_consolidacao", [])
        }
        self.assertTrue({"varredura", "secao-10", "adendo-secao-18"} <= origens)


# --------------------------------------------------------------------------
# Higiene
# --------------------------------------------------------------------------

class TestAritmetica(unittest.TestCase):
    def test_nenhum_float_no_modulo(self):
        """R12 — nenhum literal float em caminho algum."""
        import ast

        for nome in ("valida_parametros.py", "test_valida_parametros.py"):
            caminho = Path(__file__).with_name(nome)
            arvore = ast.parse(caminho.read_text(encoding="utf-8"))
            floats = [
                no for no in ast.walk(arvore)
                if isinstance(no, ast.Constant) and isinstance(no.value, float)
            ]
            self.assertEqual(floats, [], f"{nome}: literal float encontrado")

    def test_float_em_clausula_e_rejeitado(self):
        dados = json.loads(SINTETICO.read_text(encoding="utf-8"))
        dados["instrumentos"][3]["clausulas"][0]["valor"] = float("40")
        with self.assertRaises(ErroDeDados):
            resolve(
                "pn.he.adicional", "delta-servicos", "2025-06",
                instrumentos=Instrumentos(dados), catalogo=catalogo(),
            )

    def test_comparacao_de_piso_e_decimal(self):
        from valida_parametros import _para_decimal

        self.assertEqual(_para_decimal("50", "x"), Decimal("50"))
        self.assertTrue(_para_decimal("49.99", "x") < _para_decimal("50", "x"))


class TestFixtures(unittest.TestCase):
    def test_fixture_sintetica_declara_que_e_sintetica(self):
        dados = json.loads(SINTETICO.read_text(encoding="utf-8"))
        self.assertIn("SINTÉTICO", dados["natureza"])

    def test_fixture_gasmig_e_real_e_parcial(self):
        dados = json.loads(GASMIG.read_text(encoding="utf-8"))
        self.assertEqual(dados["status"], "parcial")
        self.assertIn("REAL", dados["natureza"])
        inst = dados["instrumentos"][0]
        self.assertTrue(inst["clausulas"], "a fixture real precisa ter cláusulas")
        self.assertTrue(inst["parcial"])
        self.assertTrue(dados["parametros_declarados_sem_valor_completo"])

    def test_fixture_gasmig_marca_o_que_e_rotulo_desta_extracao(self):
        """A categoria é um provisório declarado, não um dado do documento."""
        dados = json.loads(GASMIG.read_text(encoding="utf-8"))
        inst = dados["instrumentos"][0]
        self.assertEqual(inst["categorias_abrangidas"], ["gasmig-sitramico"])
        self.assertIn("RÓTULO DESTA EXTRAÇÃO", inst["categorias_fonte"])

    def test_fixture_gasmig_registra_a_divergencia_de_referencia(self):
        """O enunciado apontou a seção 3; os valores estão nas seções 7 a 10."""
        dados = json.loads(GASMIG.read_text(encoding="utf-8"))
        div = dados["divergencia_de_referencia"]
        self.assertIn("seção 3", div["o_que_o_enunciado_disse"])
        self.assertIn("Horas in itinere", div["o_que_o_arquivo_tem"])

    def test_fixture_gasmig_preserva_os_achados_que_nao_viraram_clausula(self):
        """Dado concreto do ACT que não cabe no catálogo não pode evaporar.

        A contribuição negocial é desconto, e não há camada de descontos. O
        sábado a base manda expressamente registrar como ponto a confirmar, não
        como conclusão. Nenhum dos dois vira cláusula; ambos ficam declarados.
        """
        dados = json.loads(GASMIG.read_text(encoding="utf-8"))
        declarados = dados["parametros_declarados_sem_valor_completo"]
        blob = json.dumps(declarados, ensure_ascii=False)
        self.assertIn("contribuição negocial", blob)
        self.assertIn("ponto a confirmar", blob)

        cadastrados = {c["parametro"] for i in dados["instrumentos"]
                       for c in i["clausulas"]}
        self.assertNotIn("pn.jornada.sabado-como-rsr", cadastrados)

        # Sem cláusula, resolve pelo default — mas a cobertura diz a verdade.
        r = resolve("pn.jornada.sabado-como-rsr", "gasmig-sitramico", "2026-03",
                    instrumentos=gasmig(), catalogo=catalogo())
        self.assertEqual(r.valor, "sabado-nao-e-rsr")
        self.assertEqual(r.cobertura, COBERTURA_SEM)

    def test_fixture_gasmig_nao_inventa_vigencia_nem_extensao(self):
        inst = json.loads(GASMIG.read_text(encoding="utf-8"))["instrumentos"][0]
        self.assertIsNone(inst["vigencia"]["inicio"])
        self.assertIsNone(inst["vigencia"]["fim"])
        self.assertIsNone(inst["categorias_por_extensao"][0]["categoria"])


if __name__ == "__main__":
    unittest.main()
