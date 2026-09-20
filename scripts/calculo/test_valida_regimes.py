"""Testes da camada de presets de regime temporal — bloco 6.

Cobre os cinco cenários pedidos no enunciado, as invariantes R19 a R22, a
consistência do catálogo e a separação entre eixos.

O caso que mais importa é o c10 da fixture: uma competência, quatro regimes,
quatro eixos, quatro datas distintas. Se o motor tivesse um eixo só, daria
quatro respostas erradas de uma vez.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from valida_regimes import (
    EIXOS_DECLARADOS,
    MOTIVO_ATRAVESSA,
    MOTIVO_EIXO_NAO_DECLARADO,
    MOTIVO_SEM_DEFAULT,
    ORIGEM_DATA,
    ORIGEM_DEFAULT,
    ORIGEM_USUARIO,
    AvaliacaoDeRegimes,
    CatalogoRegimes,
    Data,
    ErroDeDados,
    Escolha,
    Fatos,
    RegimesNaoAvaliados,
    avalia_regimes,
    parametro_consultavel,
    resolve_regime,
)

RAIZ = Path(__file__).resolve().parents[2]
FIXTURES = RAIZ / "tests/fixtures/calculo"
CASOS = FIXTURES / "regimes-casos.json"


# Desde o bloco 15 pr.intertemporal TEM default (tempus regit actum, Tema 23 do
# TST). Escolher a ultratividade passou a ser DIVERGÊNCIA, e R21 exige
# justificativa. Não é afrouxamento: é a invariante fazendo o que promete.
JUST_ULTRATIVA = (
    "título judicial adotou expressamente a ultratividade — posição vencida no "
    "Tema 23 do TST, mas prevalente por R8 quando o título a acolhe"
)


def catalogo() -> CatalogoRegimes:
    return CatalogoRegimes.de_arquivo()


def casos() -> dict:
    return json.loads(CASOS.read_text(encoding="utf-8"))


def fatos_do_caso(caso: dict, dados: dict) -> Fatos:
    contrato = dados["contratos"][caso["contrato"]]
    campos = {"competencia": caso["competencia"], "admissao": contrato["admissao"]}
    campos.update(caso.get("fatos_extras", {}))
    return Fatos(**campos)


def escolhas_do_caso(caso: dict) -> dict[str, Escolha]:
    """Aceita as duas formas da fixture.

    `"pr.x": "variante"` — escolha sem justificativa, válida quando não há
    divergência do default. `"pr.x": {"variante": ..., "justificativa": ...}` —
    necessária desde que `pr.intertemporal` ganhou default (bloco 15): divergir
    exige justificar, por R21.
    """
    out: dict[str, Escolha] = {}
    for k, v in caso.get("escolhas", {}).items():
        if isinstance(v, dict):
            out[k] = Escolha(v["variante"], v.get("justificativa"))
        else:
            out[k] = Escolha(v)
    return out


# --------------------------------------------------------------------------
# Datas de granularidade variável
# --------------------------------------------------------------------------


class TestData(unittest.TestCase):
    def test_competencia_mensal_antes_de_corte_diario(self):
        self.assertTrue(Data.de("2017-10").antes_de(Data.de("2017-11-11")))
        self.assertFalse(Data.de("2017-12").antes_de(Data.de("2017-11-11")))

    def test_competencia_que_contem_o_corte_atravessa(self):
        """Novembro de 2017 fica dos dois lados de 11/11/2017."""
        self.assertTrue(Data.de("2017-11").atravessa(Data.de("2017-11-11")))
        self.assertFalse(Data.de("2017-10").atravessa(Data.de("2017-11-11")))
        self.assertFalse(Data.de("2017-12").atravessa(Data.de("2017-11-11")))

    def test_dia_exato_nao_atravessa(self):
        for dia, esperado_antes in (("2017-11-10", True), ("2017-11-11", False),
                                    ("2017-11-12", False)):
            with self.subTest(dia=dia):
                d = Data.de(dia)
                self.assertFalse(d.atravessa(Data.de("2017-11-11")))
                self.assertEqual(d.antes_de(Data.de("2017-11-11")), esperado_antes)

    def test_borda_do_corte_e_inclusiva(self):
        """'a partir de 20.03.2023' inclui o próprio dia 20."""
        self.assertTrue(Data.de("2023-03-20").desde(Data.de("2023-03-20")))

    def test_ano_sem_mes_atravessa_qualquer_corte_interno(self):
        self.assertTrue(Data.de("2017").atravessa(Data.de("2017-11-11")))

    def test_data_invalida_quebra(self):
        for ruim in ("2017-13", "abril/2018", "11/11/2017", "2017-11-32"):
            with self.subTest(valor=ruim):
                with self.assertRaises(ErroDeDados):
                    Data.de(ruim)


# --------------------------------------------------------------------------
# Catálogo
# --------------------------------------------------------------------------


class TestCatalogo(unittest.TestCase):
    def test_catalogo_e_consistente(self):
        self.assertEqual(catalogo().valida(), [])

    def test_toda_variante_tem_fundamento_e_fonte(self):
        for r in catalogo().regimes.values():
            for v in r.variantes:
                with self.subTest(regime=r.id, variante=v.id):
                    self.assertTrue(v.fundamento, "variante sem fundamento é palpite")
                    self.assertTrue(v.fonte, "variante sem fonte não é auditável")

    def test_o_corpus_tem_mais_de_um_eixo(self):
        """A tese do bloco, em forma de teste."""
        em_uso = {e for e in catalogo().eixos_em_uso() if e in EIXOS_DECLARADOS}
        self.assertGreaterEqual(len(em_uso), 11)
        # E os dois eixos que o enunciado nomeou como distintos estão lá.
        self.assertIn("competencia-do-fato", em_uso)
        self.assertIn("determinacao-judicial-na-execucao", em_uso)

    def _conta_eixo(self, eixo: str) -> int:
        """Conta um eixo pela MESMA régua: primário, componente e alternativo.

        A primeira versão deste teste contava o título de um jeito e a
        competência de outro, e com isso "provava" uma dominância que não
        existia. A régua simétrica é o teste; o resultado é o que for.
        """
        n = 0
        for r in catalogo().regimes.values():
            if r.eixo == eixo or eixo in r.eixos_componentes:
                n += 1
            elif (r.bruto.get("eixo_alternativo") or {}).get("eixo") == eixo:
                n += 1
        return n

    def test_o_titulo_comparece_tanto_quanto_a_competencia(self):
        """O que a contagem simétrica sustenta — e só isso.

        A afirmação forte da primeira redação, "o título é o eixo MAIS
        FREQUENTE do corpus", não se sustentava e foi retirada do catálogo. O
        que resta, e é suficiente para a tese do bloco: a precedência R8 não é
        uma exceção rara — o título comparece tanto quanto a data do fato.
        """
        titulo = self._conta_eixo("conteudo-do-titulo")
        competencia = self._conta_eixo("competencia-do-fato")
        self.assertGreaterEqual(titulo, 5)
        self.assertLessEqual(abs(titulo - competencia), 1)

    def test_a_correcao_da_afirmacao_forte_esta_registrada(self):
        c = catalogo().dados["eixos"]
        self.assertIn("CORRECAO", c)
        self.assertIn("não se sustentava", c["CORRECAO"])

    def test_a_maioria_dos_eixos_nao_e_temporal(self):
        """Dos catorze, só dois são de competência ou fato."""
        declarados = set(catalogo().dados["eixos"]["declarados_no_corpus"])
        self.assertEqual(len(declarados), 14)
        temporais = {"competencia-do-fato", "fato-gerador"}
        self.assertTrue(temporais <= declarados)
        self.assertEqual(len(declarados - temporais), 12)

    def test_eixo_nao_declarado_implica_eixo_declarado_false(self):
        for r in catalogo().regimes.values():
            with self.subTest(regime=r.id):
                if r.eixo == "NAO-DECLARADO":
                    self.assertFalse(r.eixo_declarado)
                    self.assertTrue(r.bruto.get("fonte_do_eixo"))

    def test_eixo_origem_tem_quatro_estados_e_todos_estao_em_uso(self):
        """Declarado, inferido, herdado, não declarado. Um booleano não bastava."""
        cat = catalogo()
        origens = {r.eixo_origem for r in cat.regimes.values()}
        self.assertEqual(
            origens, {"declarado", "inferido", "herdado", "nao-declarado"})
        self.assertTrue(cat.inferidos())
        self.assertTrue(cat.provisorios())

    def test_inferido_exige_justificativa_e_resolve_com_rastro(self):
        cat = catalogo()
        for r in cat.inferidos():
            with self.subTest(regime=r.id):
                self.assertTrue(r.bruto["justificativa_da_inferencia"])
                self.assertFalse(r.eixo_declarado)
                self.assertNotEqual(r.eixo, "NAO-DECLARADO")

    def test_a_resolucao_de_eixo_inferido_marca_a_inferencia(self):
        r = resolve_regime(
            "pr.seguro-desemprego-regime",
            Fatos(competencia="2015-06", dispensa="2015-01-20"), {}, catalogo())
        self.assertTrue(r.calculavel)
        self.assertTrue(r.eixo_inferido)
        self.assertTrue(any("eixo INFERIDO" in a for a in r.avisos))
        self.assertIs(r.registro()["eixo_inferido"], True)

    def test_todo_regime_diz_de_onde_vem_o_eixo(self):
        for r in catalogo().regimes.values():
            with self.subTest(regime=r.id):
                self.assertTrue(r.bruto.get("fonte_do_eixo"))

    def test_o_porque_dos_tres_estados_esta_registrado(self):
        e = catalogo().dados["eixo_origem"]
        self.assertIn("booleano", e["por_que_nao_um_booleano"])
        self.assertIn("o rastro", e["diferenca_pratica"])

    def test_sem_default_exige_justificativa(self):
        cat = catalogo()
        sem = [r for r in cat.regimes.values() if r.sem_default]
        self.assertEqual(
            {r.id for r in sem},
            # Bloco 15: pr.intertemporal SAIU — o Tema 23 do TST fixou tese
            # vinculante e o regime ganhou default. Restam quatro.
            {"pr.tema1046-validade-clausula",
             "pr.he-adicional-cf88", "pr.sumula17-salario-profissional",
             # Bloco 12 — de natureza distinta: não é o corpus deixando a
             # questão aberta, é a prática não ter norma.
             "pr.imputacao"},
        )
        # E o catálogo nomeia todos, não um número desatualizado.
        texto = catalogo().dados["invariantes"]["R20-EXCECAO"]
        for rid in (r.id for r in sem):
            self.assertIn(rid, texto)
        for r in sem:
            with self.subTest(regime=r.id):
                self.assertTrue(r.bruto["por_que_sem_default"])
                self.assertIsNone(r.default)

    def test_regime_herdado_aponta_para_regime_existente(self):
        cat = catalogo()
        herdados = cat.herdados()
        self.assertTrue(herdados)
        for r in herdados:
            with self.subTest(regime=r.id):
                self.assertIn(r.herda_de, cat.regimes)
                self.assertEqual(cat[r.herda_de].eixo, "meta")

    def test_prescricao_intercorrente_esta_fora_do_motor_de_verbas(self):
        r = catalogo()["pr.prescricao-intercorrente"]
        self.assertEqual(r.escopo, "liquidacao-execucao")
        self.assertEqual(r.afeta_verbas, ())
        self.assertIn("não de apuração", r.bruto["fora_do_motor_de_verbas"])

    def test_regime_bloqueado_diz_por_que(self):
        r = catalogo()["pr.planos-economicos"]
        self.assertTrue(r.bloqueado)
        self.assertIn("P19", r.bruto["por_que_bloqueado"])


# --------------------------------------------------------------------------
# Os casos da fixture
# --------------------------------------------------------------------------


class TestCasosDaFixture(unittest.TestCase):
    def test_todos_os_casos_da_fixture(self):
        dados = casos()
        for caso in dados["casos"]:
            fatos = fatos_do_caso(caso, dados)
            escolhas = escolhas_do_caso(caso)
            for rid, esperado in caso["espera"].items():
                with self.subTest(caso=caso["id"], regime=rid):
                    r = resolve_regime(rid, fatos, escolhas, catalogo())
                    self.assertEqual(r.calculavel, esperado["calculavel"])
                    for campo in ("variante", "motivo", "eixo_efetivo",
                                  "origem", "data_aplicada"):
                        if campo in esperado:
                            self.assertEqual(getattr(r, campo), esperado[campo])
                    if "efeito" in esperado:
                        self.assertEqual(r.efeito, esperado["efeito"])

    def test_a_fixture_cobre_os_cinco_cenarios_do_enunciado(self):
        ids = {c["id"] for c in casos()["casos"]}
        exigidos = {
            "c2.tempus-antes-do-corte", "c3.tempus-depois-do-corte",
            "c4.ultratividade-nunca-consulta-a-regra-nova",
            "c7.he-antes-do-tema-9", "c8.he-depois-do-tema-9",
            "c10.eixos-distintos-mesma-competencia",
        }
        self.assertTrue(exigidos <= ids, exigidos - ids)

    def test_a_fixture_se_declara_sintetica(self):
        d = casos()
        self.assertIn("SINTÉTICO", d["natureza"])
        self.assertTrue(any("Não usar como fonte normativa" in a for a in d["aviso"]))


# --------------------------------------------------------------------------
# Cenário 1 — contrato atravessando 11/11/2017 nas duas correntes
# --------------------------------------------------------------------------


class TestIntertemporal(unittest.TestCase):
    ANTIGO = Fatos(admissao="2015-03-02", competencia="2024-05")

    def test_sem_escolha_resolve_pelo_default_e_marca_a_conta(self):
        """Inverteu no bloco 15 — e o teste antigo virou o de baixo.

        Até o bloco 14 este regime era R20-EXCECAO e não calculava sem escolha. Com o
        Tema 23, tem default. R20 continua valendo: a conta fica marcada `default`.
        """
        r = resolve_regime("pr.intertemporal", self.ANTIGO, {}, catalogo())
        self.assertTrue(r.calculavel)
        self.assertEqual(r.variante, "tempus-regit-actum")
        self.assertEqual(r.origem, ORIGEM_DEFAULT)

    def test_o_mecanismo_de_bloqueio_continua_existindo(self):
        """O default do intertemporal não desligou R20-EXCECAO — restam quatro casos."""
        cat = catalogo()
        sem = {r.id for r in cat.regimes.values() if r.sem_default}
        self.assertEqual(
            sem,
            {"pr.tema1046-validade-clausula", "pr.he-adicional-cf88",
             "pr.sumula17-salario-profissional", "pr.imputacao"},
        )
        r = resolve_regime("pr.imputacao", self.ANTIGO, {}, cat)
        self.assertFalse(r.calculavel)
        self.assertEqual(r.motivo, MOTIVO_SEM_DEFAULT)

    def test_o_bloqueio_NAO_se_propaga_mais_a_partir_do_intertemporal(self):
        """Inverteu no bloco 15. O intertemporal deixou de bloquear os dependentes.

        Até o bloco 14, `pr.intrajornada-71-4` e os demais herdeiros ficavam
        `calculavel: false` porque o meta-regime não resolvia. Com o default do
        Tema 23, resolvem. O mecanismo de propagação segue testado em
        `test_o_mecanismo_de_bloqueio_continua_existindo`.
        """
        a = avalia_regimes("2024-05", self.ANTIGO, {}, catalogo())
        self.assertTrue(a["pr.intrajornada-71-4"].calculavel)
        self.assertEqual(a["pr.intertemporal"].origem, ORIGEM_DEFAULT)

    def _antigo_bloqueio_se_propagava(self):
        r = resolve_regime("pr.intrajornada-71-4", self.ANTIGO, {}, catalogo())
        self.assertFalse(r.calculavel)
        self.assertIn("pr.intertemporal", r.avisos[0])

    def test_mesma_competencia_duas_correntes_dois_resultados(self):
        """O ponto inteiro da camada, num teste."""
        cat = catalogo()
        tempus = resolve_regime(
            "pr.intrajornada-71-4", self.ANTIGO,
            {"pr.intertemporal": Escolha("tempus-regit-actum")}, cat)
        ultra = resolve_regime(
            "pr.intrajornada-71-4", self.ANTIGO,
            {"pr.intertemporal": Escolha("ultratividade", JUST_ULTRATIVA)}, cat)

        self.assertEqual(tempus.variante, "redacao-reforma")
        self.assertEqual(ultra.variante, "redacao-anterior")
        self.assertEqual(tempus.eixo_efetivo, "competencia-do-fato")
        self.assertEqual(ultra.eixo_efetivo, "data-de-admissao")
        self.assertNotEqual(tempus.efeito, ultra.efeito)

    def test_contrato_dividido_sob_tempus(self):
        """Uma conta, dois regimes — e a R19 grava cada competência."""
        cat = catalogo()
        escolha = {"pr.intertemporal": Escolha("tempus-regit-actum")}
        antes = resolve_regime(
            "pr.intrajornada-71-4",
            Fatos(admissao="2015-03-02", competencia="2016-08"), escolha, cat)
        depois = resolve_regime(
            "pr.intrajornada-71-4",
            Fatos(admissao="2015-03-02", competencia="2018-08"), escolha, cat)
        self.assertEqual(antes.variante, "redacao-anterior")
        self.assertEqual(depois.variante, "redacao-reforma")

    def test_escolher_a_ultratividade_agora_EXIGE_justificativa(self):
        """Inverteu no bloco 15. Antes não havia default, logo não havia de que divergir.

        O Tema 23 do TST fixou tese vinculante e o regime ganhou default. Escolher a
        ultratividade — posição dos dez vencidos — passou a ser **divergência**, e R21
        a rejeita sem justificativa. É a invariante fazendo o que promete.
        """
        with self.assertRaises(ErroDeDados) as ctx:
            resolve_regime(
                "pr.intertemporal", self.ANTIGO,
                {"pr.intertemporal": Escolha("ultratividade")}, catalogo())
        self.assertIn("R21", str(ctx.exception))

    def test_com_justificativa_a_ultratividade_resolve_e_fica_registrada(self):
        """R8: título que a adote expressamente prevalece — mas o rastro fica."""
        r = resolve_regime(
            "pr.intertemporal", self.ANTIGO,
            {"pr.intertemporal": Escolha("ultratividade", JUST_ULTRATIVA)}, catalogo())
        self.assertTrue(r.calculavel)
        self.assertEqual(r.origem, ORIGEM_USUARIO)
        self.assertEqual(len(r.divergencias), 1)
        self.assertEqual(r.divergencias[0]["valor_do_default"], "tempus-regit-actum")


# --------------------------------------------------------------------------
# Cenário 2 — horas extras antes e depois de 20/03/2023
# --------------------------------------------------------------------------


class TestTema9(unittest.TestCase):
    def _resolve(self, competencia: str):
        return resolve_regime(
            "pr.oj394-reflexo-rsr",
            Fatos(admissao="2015-03-02", competencia=competencia),
            {}, catalogo())

    def test_antes_do_corte_nao_repercute(self):
        r = self._resolve("2023-02")
        self.assertEqual(r.variante, "sem-repercussao")
        self.assertIs(r.efeito["repercute_em_ferias_13_aviso_fgts"], False)
        self.assertIn("OJ 394", r.fundamento)

    def test_depois_do_corte_repercute(self):
        r = self._resolve("2023-04")
        self.assertEqual(r.variante, "com-repercussao")
        self.assertIs(r.efeito["repercute_em_ferias_13_aviso_fgts"], True)
        self.assertIn("Tema Repetitivo 9", r.fundamento)

    def test_o_eixo_nega_nominalmente_os_rivais(self):
        r = catalogo()["pr.oj394-reflexo-rsr"]
        fonte = r.bruto["fonte_do_eixo"]
        self.assertIn("não pela data do ajuizamento nem do julgamento", fonte)
        self.assertEqual(r.eixo, "competencia-do-fato")

    def test_ninguem_escolhe_uma_cadeia_temporal(self):
        """A data decide. A origem registra isso, e não 'escolha'."""
        self.assertEqual(self._resolve("2023-04").origem, ORIGEM_DATA)

    def test_o_reflexo_do_rsr_e_a_verba_alcancada(self):
        r = catalogo()["pr.oj394-reflexo-rsr"]
        self.assertIn("reflexo-he-rsr", r.afeta_verbas)
        for v in ("ferias", "decimo-terceiro", "aviso-previo", "fgts"):
            self.assertIn(v, r.afeta_verbas)
        # A tese alcança também as contribuições previdenciárias.
        self.assertIn("contribuicao-previdenciaria", r.afeta_verbas)

    def test_corrige_o_caso_dificil_6_e_a_lista_do_bloco_03(self):
        r = catalogo()["pr.oj394-reflexo-rsr"]
        self.assertIn("caso difícil nº 6", r.bruto["corrige"])
        self.assertIn("Não marcado, porque não muda", r.bruto["corrige"])

    def test_marco_de_2023_atravessa_o_corte(self):
        r = self._resolve("2023-03")
        self.assertFalse(r.calculavel)
        self.assertEqual(r.motivo, MOTIVO_ATRAVESSA)

    def test_com_precisao_de_dia_marco_resolve(self):
        cat = catalogo()
        for dia, esperado in (("2023-03-19", "sem-repercussao"),
                              ("2023-03-20", "com-repercussao")):
            with self.subTest(dia=dia):
                r = resolve_regime(
                    "pr.oj394-reflexo-rsr",
                    Fatos(admissao="2015-03-02", competencia=dia), {}, cat)
                self.assertEqual(r.variante, esperado)


# --------------------------------------------------------------------------
# Cenário 3 — intervalo intrajornada: extensão E natureza
# --------------------------------------------------------------------------


class TestIntrajornada(unittest.TestCase):
    ESCOLHA = {"pr.intertemporal": Escolha("tempus-regit-actum")}

    def _resolve(self, competencia: str):
        return resolve_regime(
            "pr.intrajornada-71-4",
            Fatos(admissao="2015-03-02", competencia=competencia),
            self.ESCOLHA, catalogo())

    def test_redacao_anterior_integral_e_salarial(self):
        e = self._resolve("2016-08").efeito
        self.assertEqual(e["extensao"], "integral")
        self.assertEqual(e["natureza"], "salarial")
        self.assertIs(e["tem_reflexos"], True)

    def test_redacao_da_reforma_suprimido_e_indenizatorio(self):
        e = self._resolve("2018-08").efeito
        self.assertEqual(e["extensao"], "periodo-suprimido")
        self.assertEqual(e["natureza"], "indenizatoria")
        self.assertIs(e["tem_reflexos"], False)

    def test_sao_duas_mudancas_e_o_catalogo_diz_isso(self):
        r = catalogo()["pr.intrajornada-71-4"]
        self.assertIn("EXTENSÃO e NATUREZA", r.bruto["duas_mudancas"])
        a = r.variante("redacao-anterior").efeito
        b = r.variante("redacao-reforma").efeito
        self.assertNotEqual(a["extensao"], b["extensao"])
        self.assertNotEqual(a["natureza"], b["natureza"])

    def test_a_natureza_arrasta_a_cadeia_de_reflexos(self):
        r = catalogo()["pr.intrajornada-71-4"]
        for v in ("decimo-terceiro", "ferias", "aviso-previo", "fgts", "rsr"):
            self.assertIn(v, r.afeta_verbas)

    def test_o_terceiro_regime_de_1994_esta_declarado_como_lacuna(self):
        """Lei 8.923/94 criou o § 4º; antes dela não havia consequência."""
        lac = catalogo()["pr.intrajornada-71-4"].bruto["lacuna_anterior"]
        self.assertIn("8.923", lac["evento"])
        self.assertIn("NÃO o enuncia como regime", lac["situacao"])


# --------------------------------------------------------------------------
# Cenário 4 — a interação que o enunciado mandou modelar
# --------------------------------------------------------------------------


class TestInteracaoComOIntertemporal(unittest.TestCase):
    def test_contrato_de_2015_sob_ultratividade_nunca_ve_a_regra_nova(self):
        cat = catalogo()
        escolha = {"pr.intertemporal": Escolha("ultratividade", JUST_ULTRATIVA)}
        for competencia in ("2016-08", "2019-01", "2024-05", "2026-09"):
            with self.subTest(competencia=competencia):
                r = resolve_regime(
                    "pr.intrajornada-71-4",
                    Fatos(admissao="2015-03-02", competencia=competencia),
                    escolha, cat)
                self.assertEqual(r.variante, "redacao-anterior")
                self.assertEqual(r.eixo_efetivo, "data-de-admissao")

    def test_a_verba_suprimida_torna_o_parametro_inconsultavel(self):
        """in itinere: sob tempus e competência nova, a verba não existe.

        E o parâmetro não é consultado — nem consultado-e-descartado, que
        deixaria rastro de uma consulta que não houve.
        """
        cat = catalogo()
        a = avalia_regimes(
            "2024-05", Fatos(admissao="2015-03-02"),
            {"pr.intertemporal": Escolha("tempus-regit-actum")}, cat)
        ok, motivo = parametro_consultavel("pn.in-itinere.prefixacao", a, cat)
        self.assertFalse(ok)
        self.assertIn("a verba não existe", motivo)

    def test_sob_ultratividade_a_mesma_verba_continua_existindo(self):
        cat = catalogo()
        a = avalia_regimes(
            "2024-05", Fatos(admissao="2015-03-02"),
            {"pr.intertemporal": Escolha("ultratividade", JUST_ULTRATIVA)}, cat)
        r = a["pr.in-itinere"]
        self.assertTrue(r.calculavel)
        self.assertIs(r.efeito["verba_existe"], True)

    def test_o_catalogo_declara_a_interacao(self):
        i = catalogo().dados["interacao_com_o_intertemporal"]
        self.assertIn("NUNCA SÃO CONSULTADOS", i["regra"])
        self.assertIn("consultado: false", i["consequencia_pratica"])


# --------------------------------------------------------------------------
# Cenário 5 — eixos distintos resolvendo a mesma competência
# --------------------------------------------------------------------------


class TestEixosDistintos(unittest.TestCase):
    FATOS = Fatos(
        competencia="2015-06",
        admissao="2015-03-02",
        dispensa="2015-01-20",
        sentenca="2001-06-30",
        inicio_do_aviso="2011-09-01",
        ciencia_da_lesao="2014-11-13",
    )

    def test_quatro_regimes_quatro_eixos_quatro_datas(self):
        cat = catalogo()
        esperado = {
            "pr.seguro-desemprego-regime": ("data-da-dispensa", "2015-01-20"),
            "pr.multa467-base": ("data-da-sentenca", "2001-06-30"),
            "pr.aviso-proporcional": ("inicio-do-aviso", "2011-09-01"),
            "pr.fgts-prescricao": ("ciencia-da-lesao", "2014-11-13"),
        }
        vistos = set()
        for rid, (eixo, data) in esperado.items():
            with self.subTest(regime=rid):
                r = resolve_regime(rid, self.FATOS, {}, cat)
                self.assertTrue(r.calculavel)
                self.assertEqual(r.eixo_efetivo, eixo)
                self.assertEqual(r.data_aplicada, data)
                vistos.add(r.data_aplicada)
        # Quatro datas distintas, uma competência só.
        self.assertEqual(len(vistos), 4)

    def test_a_multa_467_corta_pela_sentenca_nao_pela_competencia(self):
        """Competência de 2015, sentença de 2001 → regime de 2001."""
        r = resolve_regime("pr.multa467-base", self.FATOS, {}, catalogo())
        self.assertEqual(r.variante, "dobro-dos-salarios")

    def test_a_mesma_competencia_com_outra_sentenca_muda_a_multa(self):
        fatos = Fatos(**{**self.FATOS.__dict__, "sentenca": "2019-04-10"})
        r = resolve_regime("pr.multa467-base", fatos, {}, catalogo())
        self.assertEqual(r.variante, "cinquenta-por-cento")

    def test_eletricitario_corta_pela_admissao(self):
        cat = catalogo()
        antigo = resolve_regime(
            "pr.periculosidade-eletricitarios",
            Fatos(competencia="2024-05", admissao="2010-05-17"), {}, cat)
        novo = resolve_regime(
            "pr.periculosidade-eletricitarios",
            Fatos(competencia="2024-05", admissao="2019-06-01"), {}, cat)
        self.assertEqual(antigo.variante, "totalidade-das-parcelas")
        self.assertEqual(novo.variante, "salario-base")

    def test_a_data_da_lei_12740_nao_esta_no_corpus_e_nao_foi_suposta(self):
        """O corpus diz 'antes da Lei 12.740/2012'. Sem dia, sem mês.

        A primeira versão deste catálogo cravou 08/12/2012 — historicamente
        correto e mesmo assim invenção, porque não está em arquivo nenhum do
        repositório. A consequência de não supor é dura e é o ponto: admissão
        ocorrida EM 2012 não resolve.
        """
        cat = catalogo()
        r = cat["pr.periculosidade-eletricitarios"]
        self.assertEqual(str(r.corte), "2012")
        self.assertIn("NÃO FOI SUPOSTA", r.bruto["lacuna_de_data"])

        indefinido = resolve_regime(
            r.id, Fatos(competencia="2024-05", admissao="2012-06-15"), {}, cat)
        self.assertFalse(indefinido.calculavel)
        self.assertEqual(indefinido.motivo, "nenhuma-variante-cobre-a-data")

    def test_fato_do_eixo_ausente_nao_vira_default_silencioso(self):
        r = resolve_regime(
            "pr.multa467-base", Fatos(competencia="2015-06"), {}, catalogo())
        self.assertFalse(r.calculavel)
        self.assertEqual(r.motivo, "fato-do-eixo-nao-informado")

    def test_eixo_nao_declarado_recusa(self):
        r = resolve_regime(
            "pr.tema1046-validade-clausula", self.FATOS, {}, catalogo())
        self.assertFalse(r.calculavel)
        self.assertEqual(r.motivo, MOTIVO_EIXO_NAO_DECLARADO)
        self.assertIn("plausível", r.avisos[0])


# --------------------------------------------------------------------------
# Invariantes R19 a R22
# --------------------------------------------------------------------------


class TestInvariantes(unittest.TestCase):
    FATOS = Fatos(admissao="2015-03-02")
    ESCOLHA = {"pr.intertemporal": Escolha("tempus-regit-actum")}

    def test_R19_o_registro_e_por_competencia(self):
        cat = catalogo()
        a = avalia_regimes("2016-08", self.FATOS, self.ESCOLHA, cat)
        b = avalia_regimes("2024-05", self.FATOS, self.ESCOLHA, cat)
        ra = a["pr.intrajornada-71-4"].registro()
        rb = b["pr.intrajornada-71-4"].registro()
        self.assertNotEqual(ra["variante"], rb["variante"])
        for r in (ra, rb):
            for campo in ("regime", "variante", "eixo", "origem", "fundamento"):
                self.assertIn(campo, r)
        self.assertEqual(a.registro()["competencia"], "2016-08")

    def test_R19_o_registro_da_competencia_traz_todos_os_regimes(self):
        cat = catalogo()
        a = avalia_regimes("2024-05", self.FATOS, self.ESCOLHA, cat)
        de_apuracao = [r for r in cat.regimes.values() if r.escopo == "apuracao"]
        self.assertEqual(len(a.registro()["regimes"]), len(de_apuracao))

    def test_R20_default_marca_a_conta(self):
        r = resolve_regime("pr.fgts-indice-jam", self.FATOS, {}, catalogo())
        self.assertTrue(r.calculavel)
        self.assertEqual(r.origem, ORIGEM_DEFAULT)
        self.assertEqual(r.variante, "sem-jam")
        self.assertTrue(r.avisos, "default sem marca é default escondido")

    def test_R21_divergir_do_default_exige_justificativa(self):
        with self.assertRaises(ErroDeDados) as ctx:
            resolve_regime(
                "pr.fgts-indice-jam", self.FATOS,
                {"pr.fgts-indice-jam": Escolha("jam")}, catalogo())
        self.assertIn("R21", str(ctx.exception))

    def test_R21_com_justificativa_registra_a_divergencia(self):
        r = resolve_regime(
            "pr.fgts-indice-jam", self.FATOS,
            {"pr.fgts-indice-jam": Escolha(
                "jam", "a sentença determinou expressamente o JAM")},
            catalogo())
        self.assertTrue(r.calculavel)
        self.assertEqual(len(r.divergencias), 1)
        d = r.divergencias[0]
        self.assertEqual(d["valor_do_default"], "sem-jam")
        self.assertEqual(d["valor_aplicado"], "jam")
        self.assertIn("sentença", d["justificativa"])

    def test_R21_escolher_o_proprio_default_nao_e_divergencia(self):
        r = resolve_regime(
            "pr.fgts-indice-jam", self.FATOS,
            {"pr.fgts-indice-jam": Escolha("sem-jam")}, catalogo())
        self.assertEqual(r.divergencias, [])
        self.assertEqual(r.origem, ORIGEM_USUARIO)

    def test_R22_parametro_antes_da_avaliacao_quebra(self):
        with self.assertRaises(RegimesNaoAvaliados):
            parametro_consultavel("pn.he.adicional", None, catalogo())

    def test_R22_o_parametro_continua_bloqueado_mas_por_outra_razao(self):
        """Inverteu no bloco 15, e a razão nova é mais forte que a antiga.

        Antes: `pn.in-itinere.prefixacao` não se consultava porque o intertemporal
        não resolvia. Agora resolve — por `tempus regit actum`, competência de 2024 —
        e o resultado é que **a verba não existe nessa competência**: o art. 58, § 2º
        deixou de computar o deslocamento na jornada. O parâmetro segue inconsultável,
        e agora com um motivo de mérito em vez de um bloqueio de modelagem.
        """
        cat = catalogo()
        a = avalia_regimes("2024-05", self.FATOS, {}, cat)
        ok, motivo = parametro_consultavel("pn.in-itinere.prefixacao", a, cat)
        self.assertFalse(ok)
        self.assertIn("pr.in-itinere", motivo)
        self.assertIn("não existe nesta competência", motivo)

    def test_R22_o_tema1046_bloqueia_todos_os_parametros(self):
        """Ele decide a validade de qualquer cláusula coletiva."""
        cat = catalogo()
        self.assertIn("TODOS",
                      cat["pr.tema1046-validade-clausula"].afeta_parametros)
        a = avalia_regimes("2024-05", self.FATOS, self.ESCOLHA, cat)
        ok, motivo = parametro_consultavel("pn.ferias.particao", a, cat)
        self.assertFalse(ok)
        self.assertIn("pr.tema1046", motivo)

    def test_as_quatro_invariantes_estao_no_catalogo(self):
        inv = catalogo().dados["invariantes"]
        for r in ("R19", "R20", "R20-EXCECAO", "R21", "R22"):
            self.assertIn(r, inv)
        self.assertIn("CADA COMPETÊNCIA", inv["R19"])
        self.assertIn("ANTES", inv["R22"])


# --------------------------------------------------------------------------
# Separação entre as duas camadas
# --------------------------------------------------------------------------


class TestSeparacaoDeCamadas(unittest.TestCase):
    def test_o_catalogo_distingue_regime_de_parametro(self):
        d = catalogo().dados["a_distincao_que_governa_tudo"]
        self.assertIn("NÃO é negociável por sindicato", d["preset_de_regime"])
        self.assertIn("AVALIADO ANTES", d["ordem"])

    def test_nao_confunde_com_os_presets_de_atualizacao(self):
        d = catalogo().dados["nao_confundir_com_os_presets_de_atualizacao"]
        self.assertIn("TRAB-ADC58-LEI14905", d["o_que_sao"])
        self.assertIn("TRAB-INTERTEMP-TEMPUS", d["o_unico_cruzamento"])

    def test_os_presets_nomeados_no_corpus_estao_no_catalogo(self):
        """TRAB-INTERTEMP-* eram os únicos presets sem catálogo."""
        presets = {
            v.preset for r in catalogo().regimes.values()
            for v in r.variantes if v.preset
        }
        self.assertEqual(
            presets, {"TRAB-INTERTEMP-TEMPUS", "TRAB-INTERTEMP-ULTRATIVO"})

    def test_todo_parametro_citado_existe_no_catalogo_de_parametros(self):
        pn = json.loads(
            (RAIZ / "docs/calculo/tabelas-normativas"
                    "/camada-norma-coletiva-catalogo.json").read_text(encoding="utf-8"))
        ids = {p["id"] for p in pn["parametros"]}
        for r in catalogo().regimes.values():
            for p in r.afeta_parametros:
                if p == "TODOS":
                    continue
                with self.subTest(regime=r.id, parametro=p):
                    self.assertIn(p, ids)


# --------------------------------------------------------------------------
# Lacuna do eixo não declarado
# --------------------------------------------------------------------------


class TestLacunaDoEixo(unittest.TestCase):
    def test_a_lacuna_esta_declarada_e_quantificada(self):
        lac = catalogo().dados["LACUNA_EIXO_NAO_DECLARADO"]
        self.assertIn("F1–F9", lac["as_marcas_F"])
        self.assertIn("marcas de Fase 4", lac["quantos"])
        self.assertIn("plausível", lac["por_que_nao_foi_suposto"])

    def test_a_excecao_da_marca_F6_esta_registrada(self):
        """Nem todas as dezesseis marcas F são da Lei 13.467/2017."""
        m = catalogo().dados["LACUNA_EIXO_NAO_DECLARADO"]["as_marcas_F"]
        self.assertIn("13.419/2017", m)
        self.assertIn("EXCEÇÃO", m)

    def test_o_numero_sem_lastro_foi_retirado(self):
        lac = catalogo().dados["LACUNA_EIXO_NAO_DECLARADO"]
        self.assertNotIn("Quinze pontos", lac["quantos"])
        self.assertIn("CORRECAO", lac)

    def test_nenhum_regime_com_eixo_nao_declarado_resolve(self):
        cat = catalogo()
        fatos = Fatos(competencia="2020-01", admissao="2015-03-02",
                      dispensa="2020-01-10", sentenca="2020-02-01")
        for r in cat.provisorios():
            with self.subTest(regime=r.id):
                res = resolve_regime(r.id, fatos, {}, cat)
                self.assertFalse(res.calculavel)

    def test_a_variante_removida_do_salario_basico_esta_explicada(self):
        r = catalogo()["pr.insalubridade-base-sumula228"]
        vr = r.bruto["variante_removida"]
        self.assertEqual(vr["id"], "salario-basico")
        self.assertIn("CASSADA DEFINITIVAMENTE", vr["por_que"])
        self.assertIn("VARIANTE DE REGIME", vr["cuidado"])


# --------------------------------------------------------------------------
# Higiene
# --------------------------------------------------------------------------


class TestHigiene(unittest.TestCase):
    def test_nenhum_float_nos_arquivos_deste_bloco(self):
        import ast

        for caminho in (Path(__file__).with_name("valida_regimes.py"),
                        Path(__file__)):
            with self.subTest(arquivo=caminho.name):
                arvore = ast.parse(caminho.read_text(encoding="utf-8"))
                floats = [
                    n for n in ast.walk(arvore)
                    if isinstance(n, ast.Constant) and isinstance(n.value, float)
                ]
                self.assertEqual(floats, [], "R12: nenhum float")

    def test_o_catalogo_nao_tem_float(self):
        def varre(o, caminho="raiz"):
            if isinstance(o, float):
                self.fail(f"float em {caminho}")
            if isinstance(o, dict):
                for k, v in o.items():
                    varre(v, f"{caminho}.{k}")
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    varre(v, f"{caminho}[{i}]")

        varre(json.loads(
            (RAIZ / "docs/calculo/tabelas-normativas"
                    "/regimes-temporais-catalogo.json").read_text(encoding="utf-8")))

    def test_todo_regime_tem_id_estavel(self):
        for rid in catalogo().regimes:
            self.assertRegex(rid, r"^pr\.[a-z0-9-]+$")


class TestRegimesDoBloco12(unittest.TestCase):
    """pr.adc58-item-i e pr.imputacao, acrescentados na consolidação."""

    def test_adc58_item_i_nao_crava_data_de_corte(self):
        """O corte é um EVENTO. Cravar data seria inventar a que o corpus não dá."""
        r = catalogo()["pr.adc58-item-i"]
        self.assertIsNone(r.corte)
        self.assertIn("não é uma data", r.bruto["corte_observacao"].lower())

    def test_adc58_item_i_declara_origem_externa_ao_corpus(self):
        """Pesquisa externa tem de vir declarada, como o art. 611-B no bloco 5."""
        r = catalogo()["pr.adc58-item-i"]
        self.assertIn("EXTERNA AO CORPUS", r.bruto["fonte_do_eixo"])
        self.assertIn("NÃO foi lido", r.bruto["fonte_do_eixo"])
        self.assertEqual(len(r.bruto["precedentes"]), 3)

    def test_i1_nao_recalcula_o_pago_e_i2_recalcula(self):
        """É a distinção que resolve o atrito marcado no bloco 11B."""
        v = {x["id"]: x for x in catalogo()["pr.adc58-item-i"].bruto["variantes"]}
        self.assertFalse(v["i1-pagamento-consolidado"]["efeito"]["recalcula_pago_pelo_criterio_novo"])
        self.assertTrue(v["i2-execucao-questionada"]["efeito"]["recalcula_pago_pelo_criterio_novo"])

    def test_i1_protege_pagamento_mas_nao_deposito_recursal(self):
        v = {x["id"]: x for x in catalogo()["pr.adc58-item-i"].bruto["variantes"]}
        i1 = v["i1-pagamento-consolidado"]
        self.assertIn("pagamento", i1["alcanca"])
        self.assertIn("incontroverso-liberado", i1["alcanca"])
        self.assertIn("recursal", i1["nao_alcanca"])
        self.assertIn("controverso-em-garantia", i1["nao_alcanca"])

    def test_imputacao_nao_tem_default(self):
        r = catalogo()["pr.imputacao"]
        self.assertTrue(r.sem_default)
        self.assertIsNone(r.default)

    def test_imputacao_registra_que_a_pratica_nao_tem_norma(self):
        """O achado que decide R10: 101 aplicações, zero fundamentos."""
        r = catalogo()["pr.imputacao"]
        prop = next(x for x in r.bruto["variantes"] if x["id"] == "proporcional")
        self.assertIn("SEM NORMA CITADA", prop["fundamento"])
        self.assertIn("101", prop["fundamento"])

    def test_imputacao_registra_a_direcao_do_delta(self):
        """Sem a direção, o número não diz a quem a escolha favorece."""
        direcao = catalogo()["pr.imputacao"].bruto["amplitude_medida"]["direcao_do_delta"].lower()
        self.assertIn("devedor", direcao)
        self.assertIn("credor", direcao)
        variantes = {x["id"]: x for x in catalogo()["pr.imputacao"].bruto["variantes"]}
        self.assertEqual(variantes["proporcional"]["efeito"]["favorece"], "devedor")
        self.assertEqual(variantes["art-354-cc"]["efeito"]["favorece"], "credor")

    def test_imputacao_nao_tem_eixo_temporal(self):
        """Distinto de NAO-DECLARADO: aqui não há o que faltar."""
        self.assertEqual(catalogo()["pr.imputacao"].eixo, "sem-eixo-temporal")


if __name__ == "__main__":
    unittest.main()
