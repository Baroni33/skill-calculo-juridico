# -*- coding: utf-8 -*-
"""Runner de aceitacao — NIVEL 2 (aceite do SISTEMA).

O QUE MUDOU NO BLOCO 23, E POR QUE
----------------------------------
A versao do bloco 22 tratava o campo `tolerancia` das fixtures 2 e 4 como BANDA
DE ACEITACAO: o resultado passava se caisse dentro de R$ 0,01 / R$ 0,03 do
esperado. Estava errado, e o erro e sutil.

  As fixtures declaram `divergencia_e_assercao: true`.
  A TOLERANCIA NAO E BANDA — E ASSERCAO.

Os dois metodos do manual produzem DOIS numeros, e a DIFERENCA ENTRE ELES e a
assercao. Portanto, agora:

  * motor que produz UM NUMERO SO NAO PASSA — ainda que o numero esteja certo:
    faltou o outro metodo, e sem ele nao ha o que asserir;
  * motor que produz DOIS NUMEROS IGUAIS **FALHA** — zerar a diferenca significa
    arredondar errado (e o que acontece quem roda em precisao plena);
  * a diferenca tem de ser EXATAMENTE a declarada: R$ 0,01 na fixture 2 e
    R$ 0,03 na fixture 4. Nem menos, nem mais;
  * e cada metodo tem de bater EXATAMENTE com o seu proprio valor publicado.
    Nao ha banda em lugar nenhum deste arquivo — as fixtures 1 e 3 declaram
    `tolerancia 0,00`, e sao comparadas por igualdade.

A redacao que induziu o defeito era "as fixtures 2 e 4 divergem DO CORPUS".
Elas nao divergem do corpus: divergem ENTRE OS DOIS METODOS do proprio manual.
Quem le "do corpus" entende "nosso numero pode ficar um centavo longe do
publicado", que e banda; quem le "entre os metodos" entende que sao DOIS
CALCULOS. A redacao foi corrigida nas skills no mesmo bloco.

O BLOQUEIO NAO MUDOU
--------------------
As quatro fixtures seguem BLOQUEADAS por serie de indices ausente — a camada (B)
nao existe no repositorio, por desenho declarado. O que mudou e que, quando a
serie chegar, o runner vai cobrar A COISA CERTA.

**E o motivo do bloqueio NAO e o mesmo nas quatro.** A redacao anterior dizia,
para todas, "o caminho esta implementado; falta o coeficiente". Era verdade so
na fixture 4:

  * fixture 4 — `scripts/calculo/test_metodos.py` reproduz a fixture INTEIRA
    nos dois metodos (4.435,07 · 4.435,04 · delta 0,03), celula por celula, com
    os coeficientes impressos nas `pagina_pdf` 91 e 92. Falta SO a serie;
  * fixtures 1 e 2 — o teste reproduz os TOTAIS publicados (3.484,95 da p. 51;
    5.218,27 e 5.218,28 das pp. 52-53) a partir dos coeficientes impressos, mas
    o runner tem AINDA uma pendencia que serie nenhuma resolve: o ROTULO do
    corte de dez/2021. A cadeia encerra o regime anterior em nov/2021 e o
    manual intitula a alinea "ate dez./2021" — deslocamento D1 mais a
    consolidacao, e a ordem entre o indice de nov/2021 e os 0,4412% e a
    lacuna #3. Esta declarada na nota `T0/LIMITACAO` de cada uma;
  * fixture 3 — um metodo so, e o bloqueio e a serie.

NIVEL 1 x NIVEL 2
-----------------
O que e executavel SO COM A SKILL — R11, R12, R1 na composicao, as cinco cadeias
de arredondamento e o NMP — e o NIVEL 1, e vive em
`scripts/calculo/test_aceite_nivel1.py`. Este arquivo e o NIVEL 2.

Uso:  python runner.py
Saida: 0 se nenhuma fixture falhou por ERRO DE CALCULO. Fixture BLOQUEADA por
dado ausente nao e falha do motor — e resultado do teste, e sai com codigo 2.
"""

from __future__ import print_function

import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from decimal import Decimal

from aritmetica import D, ZERO, moeda, fator, taxa_legal, nmp, um_trinta_avos
import cadeias
import metodos
import motor
import series
from series import SerieAusente

RAIZ = cadeias.RAIZ
DIR_FIXTURES = os.path.join(RAIZ, "tests", "fixtures", "calculo")


def ler_json(caminho):
    with io.open(caminho, "r", encoding="utf-8") as fh:
        return json.load(fh)


def ler_fixture(nome):
    return ler_json(os.path.join(DIR_FIXTURES, nome))


# ===========================================================================
# Resultado de uma fixture
# ===========================================================================
class Resultado(object):
    BATEU = "BATEU"
    DIVERGIU = "DIVERGIU"
    BLOQUEADA = "BLOQUEADA"
    FALTA_UM_METODO = "FALTA_UM_METODO"
    DIVERGENCIA_ZERADA = "DIVERGENCIA_ZERADA"

    # Estados que sao FALHA DO MOTOR, e nao resultado do teste.
    FALHAS = (DIVERGIU, FALTA_UM_METODO, DIVERGENCIA_ZERADA)

    def __init__(self, fixture_id):
        self.id = fixture_id
        self.status = None
        self.motivo = None
        self.comparacoes = []   # (rotulo, esperado, obtido, delta, passou)
        self.notas = []

    # -- numero unico: IGUALDADE, nunca banda ------------------------------
    def comparar(self, rotulo, esperado, obtido):
        e, o = D(esperado), D(obtido)
        self.comparacoes.append((rotulo, e, o, o - e, o == e))

    # -- o par: a assercao das fixtures 2 e 4 ------------------------------
    def asserir_par(self, rotulo, esperado_resumido, esperado_detalhado,
                    obtido_resumido, obtido_detalhado, divergencia_declarada):
        """A tolerancia NAO e banda: e a diferenca que os dois metodos DEVEM
        produzir. Tres modos de falha, e os tres sao do motor."""
        dec = D(divergencia_declarada)

        if obtido_resumido is None or obtido_detalhado is None:
            qual = "resumido" if obtido_resumido is None else "detalhado"
            self.status = self.FALTA_UM_METODO
            self.motivo = (
                "%s: o motor produziu UM numero so (falta o metodo %s). A "
                "assercao desta fixture e a DIFERENCA entre os dois metodos — "
                "com um numero nao ha o que asserir. NAO PASSA, ainda que o "
                "numero produzido esteja certo." % (rotulo, qual))
            return False

        r, d = D(obtido_resumido), D(obtido_detalhado)
        delta = (r - d).copy_abs()

        if delta == ZERO:
            self.status = self.DIVERGENCIA_ZERADA
            self.motivo = (
                "%s: os dois metodos produziram O MESMO numero (%s). Zerar a "
                "divergencia significa ARREDONDAR ERRADO — e o sintoma de rodar "
                "em precisao plena em vez de truncar a cada etapa (R12). A "
                "fixture exige delta de %s." % (rotulo, r, dec))
            self.comparacoes.append((rotulo + " delta(res-det)", dec, delta,
                                     delta - dec, False))
            return False

        ok_r = r == D(esperado_resumido)
        ok_d = d == D(esperado_detalhado)
        ok_delta = delta == dec
        self.comparacoes.append((rotulo + " resumido", D(esperado_resumido), r,
                                 r - D(esperado_resumido), ok_r))
        self.comparacoes.append((rotulo + " detalhado", D(esperado_detalhado), d,
                                 d - D(esperado_detalhado), ok_d))
        self.comparacoes.append((rotulo + " delta(res-det)", dec, delta,
                                 delta - dec, ok_delta))
        if not ok_delta:
            self.motivo = (
                "%s: a diferenca entre os metodos e %s e a fixture assevera %s. "
                "A tolerancia NAO e banda." % (rotulo, delta, dec))
        return ok_r and ok_d and ok_delta

    def bloquear(self, motivo):
        self.status = self.BLOQUEADA
        self.motivo = motivo

    def fechar(self):
        if self.status is not None:
            return
        self.status = (self.BATEU if all(c[4] for c in self.comparacoes)
                       else self.DIVERGIU)


# ===========================================================================
# Fixtures 1 e 2 — Fazenda Publica, condenatorias em geral
# ===========================================================================
def _indexadores_de_correcao(competencia_inicial, competencia_final, devedor,
                             cadeia_correcao, cadeia_juros):
    """Monta (competencia, indexador) mes a mes pela cadeia (A), com R1 imposto
    NA COMPOSICAO: mes cujo segmento de juros engloba correcao NAO recebe indice
    inflacionario (NOTA 2 do item 4.2.1).
    """
    fora = []
    for comp in cadeias.meses(competencia_inicial, competencia_final):
        c = cadeias.compor(comp, devedor, cadeia_correcao, cadeia_juros)
        if c["correcao"] is None:
            continue
        fora.append((comp, c["correcao"].get("indexador")))
    return fora


def _coeficientes_por_parcela(ent, devedor, correcao, juros_ch, ate):
    """(B) do metodo resumido — coeficiente ACUMULADO de cada parcela ate a
    data-base. Levanta SerieAusente: e aqui que a camada (B) falta."""
    saida = []
    registro = motor.Registro()
    for parcela in ent["parcelas"]:
        pares = _indexadores_de_correcao(parcela["competencia"], ate, devedor,
                                         correcao, juros_ch)
        saida.append((parcela, motor.coeficiente_de_correcao(pares, registro)))
    return saida


def _roda_fazenda(fx, resultado):
    """Executa OS DOIS METODOS. A fixture 2 assevera o par; a 1, um numero so
    (o manual nao registra divergencia nela, `tolerancia 0,00`)."""
    ent = fx["entradas"]
    devedor = ent["devedor"]
    data_base = ent["data_base"]

    correcao = cadeias.carregar("cjf.condenatorias-gerais.correcao-monetaria.json")
    juros_ch = cadeias.carregar("cjf.condenatorias-gerais.juros-mora.json")

    # R2 e R1 — checar ANTES de calcular (invariantes se impedem na composicao)
    probs = correcao.checar_cobertura(devedor) + juros_ch.checar_cobertura(devedor)
    for p in probs:
        resultado.notas.append("R2/cadeia (sobreposicao DO ORIGINAL): " + p)
    janela = cadeias.meses(min(p["competencia"] for p in ent["parcelas"]), data_base)
    for v in cadeias.validar_composicao(janela, devedor, correcao, juros_ch):
        resultado.notas.append(v)

    # T0 — os marcos, derivados do caso. Isto roda SEM serie e por isso aparece
    # mesmo quando a fixture bloqueia: e a prova de que os marcos sairam do caso.
    trechos = _trechos_do_caso(ent, devedor, correcao, juros_ch)
    for ini, fim, comp in trechos:
        engloba = "correcao-monetaria" in (comp["juros"].get("engloba") or [])
        dentro = [p["valor"] for p in ent["parcelas"]
                  if (ini is None or p["competencia"] > ini) and p["competencia"] <= fim]
        resultado.notas.append(
            "T0 marco (%s, %s] juros=%s engloba_correcao=%s entradas=%s"
            % (ini or "inicio do caso", fim,
               comp["juros"].get("indexador") or comp["juros"].get("taxa"),
               "sim" if engloba else "nao", dentro))
    total_entradas = sum(D(p["valor"]) for p in ent["parcelas"])
    resultado.notas.append(
        "T0: %d marco(s), e cada parcela entra UMA vez — soma das entradas = %s, "
        "igual ao nominal do caso" % (len(trechos), total_entradas))
    resultado.notas.append(
        "T0/LIMITACAO: o corte sai da MUDANCA DE REGIME da cadeia (ultima "
        "competencia do regime anterior); o manual rotula a alinea pela "
        "competencia SEGUINTE ('a) ate dez./2021' para um regime que a cadeia "
        "encerra em nov/2021). A diferenca e o deslocamento D1 somado a "
        "consolidacao de dez/2021, e a ORDEM entre o indice de nov/2021 e os "
        "0,4412% de dez/2021 e a lacuna #3 — NAO resolvida aqui.")

    try:
        # ---- RESUMIDO: (B) unico por parcela, ate a data-base -------------
        pares = _coeficientes_por_parcela(ent, devedor, correcao, juros_ch,
                                          data_base)
        linhas = [{"valor": p["valor"], "coeficiente": coef,
                   "d_pct": _d_pct(ent), "e_pct": _e_pct(ent),
                   "f_pct": _f_pct(ent), "conta": "principal"}
                  for p, coef in pares]
        r_resumido = metodos.resumido(linhas)

        # ---- DETALHADO: um marco por regime, agregando antes da taxa ------
        r_detalhado = metodos.detalhado(_marcos_fazenda(ent, devedor, correcao,
                                                        juros_ch))
    except SerieAusente as e:
        resultado.bloquear(
            "%s — os DOIS metodos param no mesmo ponto: falta a camada (B). "
            "O PROCEDIMENTO esta implementado e VERIFICADO contra as celulas "
            "publicadas (scripts/calculo/test_metodos.py reproduz 3.484,95 da "
            "pagina_pdf 51 e 5.218,27/5.218,28 da 52-53 a partir dos "
            "coeficientes impressos). O que falta AQUI e a serie — e mais uma "
            "coisa, que serie nenhuma resolve: o rotulo do corte de dez/2021 "
            "(lacuna #3, ver nota T0/LIMITACAO acima). Nao e 'so o "
            "coeficiente'." % e)
        return
    except cadeias.ErroDeDados as e:
        resultado.bloquear("ErroDeDados: %s" % e)
        return

    esp = fx["esperado"]
    if fx["tolerancia"].get("divergencia_e_assercao"):
        resultado.asserir_par(
            "total da conta",
            esp["metodo_resumido"]["total"], esp["metodo_detalhado"]["total"],
            r_resumido["total_da_conta"], r_detalhado["total_da_conta"],
            fx["tolerancia"]["valor"])
    else:
        # tolerancia 0,00: os dois metodos convergem, e a igualdade e exigida
        resultado.comparar("total (resumido)", esp["total"],
                           r_resumido["total_da_conta"])
        resultado.comparar("total (detalhado)", esp["total"],
                           r_detalhado["total_da_conta"])


def _d_pct(ent):
    """(D) % juros ate 12/2021 — vem da serie de juros do periodo.

    LACUNA (registro-de-lacunas #2): o percentual acumulado de juros ate
    12/2021 e resultado da serie (B); a skill nao o publica. Pedir aqui levanta
    SerieAusente pelo mesmo motivo que o coeficiente.
    """
    return series.indice_mensal("JUROS-ATE-12-2021", ent["data_base"])


def _e_pct(ent):
    return series.indice_mensal("SELIC-ACUMULADA", ent["data_base"])


def _f_pct(ent):
    return series.indice_mensal("TAXA-LEGAL-ACUMULADA", ent["data_base"])


def _trechos_do_caso(ent, devedor, correcao, juros_ch):
    """T0 — OS MARCOS SAEM DO CASO, nao de constante.

    Um marco por REGIME: caminha mes a mes da primeira competencia do caso ate
    a data-base do caso, compoe (R1 ja imposto) e ABRE MARCO NOVO quando a
    assinatura do regime muda — o par (indexador de correcao, indexador/taxa de
    juros, engloba). Devolve [(inicio_exclusivo|None, fim_inclusivo, composicao)].

    Por que nao pode ser constante, e e o defeito que o bloco 23 mediu: a lista
    fixa `[2021-12, 2025-09, data_base]` dava, para a fixture 1 (data-base
    jun/2022), um 2o marco TRES ANOS ALEM da data-base e um 3o que ANDAVA PARA
    TRAS. O 1o Exemplo do manual (pagina_pdf 51) tem DOIS marcos —
    `a) ate dez./2021` e `b) de dez./2021 ate jun./2022` — e NAO tem corte em
    set/2025, porque set/2025 nao existe neste caso.
    """
    inicio_do_caso = min(p["competencia"] for p in ent["parcelas"])
    corridas = []          # [(assinatura, [competencias], composicao)]
    for comp in cadeias.meses(inicio_do_caso, ent["data_base"]):
        c = cadeias.compor(comp, devedor, correcao, juros_ch)
        seg_j = c["juros"]
        assinatura = (
            (c["correcao"] or {}).get("indexador"),
            seg_j.get("indexador") or seg_j.get("taxa"),
            tuple(sorted(seg_j.get("engloba") or [])),
        )
        if corridas and corridas[-1][0] == assinatura:
            corridas[-1][1].append(comp)
        else:
            corridas.append((assinatura, [comp], c))

    trechos, anterior = [], None
    for _, comps, composicao in corridas:
        trechos.append((anterior, comps[-1], composicao))
        anterior = comps[-1]
    return trechos


def _marcos_fazenda(ent, devedor, correcao, juros_ch):
    """Marcos de 4.2.1.1, DERIVADOS do caso por `_trechos_do_caso`. Cada um com
    o coeficiente DO TRECHO e a taxa DO TRECHO.

    A entrada de cada marco e a parcela cuja competencia cai DENTRO do trecho —
    `inicio < competencia <= fim`, meio-aberto. O filtro antigo era
    `competencia <= fim`, e reinjetava as parcelas de 2020 em TODO marco: na
    fixture 1 punha R$ 8.000,00 num caso de R$ 3.000,00.
    """
    registro = motor.Registro()
    marcos = []
    for inicio, fim, composicao in _trechos_do_caso(ent, devedor, correcao,
                                                    juros_ch):
        engloba = "correcao-monetaria" in (composicao["juros"].get("engloba") or [])
        entradas = []
        for p in ent["parcelas"]:
            if inicio is not None and p["competencia"] <= inicio:
                continue
            if p["competencia"] > fim:
                continue
            entradas.append({"valor": p["valor"], "conta": "principal",
                             "taxa_pct": series.indice_mensal(
                                 "TAXA-DO-TRECHO-DA-PARCELA", p["competencia"])})
        marco = {
            "ate": fim,
            "taxa_pct": series.indice_mensal("TAXA-DO-TRECHO", fim),
            "taxa_engloba_correcao": engloba,
            "entradas": entradas,
        }
        if not engloba:
            # trecho com correcao propria: T1 e T3a pedem o coeficiente. Trecho
            # englobante NAO tem coeficiente — a taxa e a correcao (T3b).
            inicio_coef = inicio if inicio is not None else fim
            marco["coeficiente"] = motor.coeficiente_de_correcao(
                _indexadores_de_correcao(inicio_coef, fim, devedor, correcao,
                                         juros_ch), registro)
        marcos.append(marco)
    return marcos


def _roda_nao_fazenda(fx, resultado):
    """Fixture 3 — o manual apresenta UM metodo para este caso (`tolerancia
    0,00`, sem `divergencia_e_assercao`). Comparacao por IGUALDADE."""
    ent = fx["entradas"]
    devedor = ent["devedor"]
    correcao = cadeias.carregar("cjf.condenatorias-gerais.correcao-monetaria.json")
    juros_ch = cadeias.carregar("cjf.condenatorias-gerais.juros-mora.json")

    for p in correcao.checar_cobertura(devedor) + juros_ch.checar_cobertura(devedor):
        resultado.notas.append("R2/cadeia (sobreposicao DO ORIGINAL): " + p)
    janela = cadeias.meses(min(p["competencia"] for p in ent["parcelas"]),
                           ent["data_base"])
    for v in cadeias.validar_composicao(janela, devedor, correcao, juros_ch):
        resultado.notas.append(v)

    try:
        pares = _coeficientes_por_parcela(ent, devedor, correcao, juros_ch,
                                          ent["data_base"])
    except SerieAusente as e:
        resultado.bloquear(str(e))
        return
    linhas = [{"valor": p["valor"], "coeficiente": coef, "conta": "principal"}
              for p, coef in pares]
    resultado.comparar("total", fx["esperado"]["total"],
                       metodos.resumido(linhas)["total_da_conta"])


def _roda_precatorio(fx, resultado):
    """Fixture 4 — o MELHOR teste de arredondamento do conjunto, e o par vale
    R$ 0,03. A cadeia vem DECLARADA na propria fixture; o que falta e o valor.
    """
    ent = fx["entradas"]
    registro = motor.Registro()
    try:
        # ---- RESUMIDO: coeficiente unico ate a data de atualizacao --------
        coef_total = motor.coeficiente_de_correcao(
            [(c, trecho["indexador"])
             for trecho in ent["cadeia_correcao"]
             for c in cadeias.meses(trecho["de"], trecho["ate"])], registro)
        coef_pagamento = motor.coeficiente_de_correcao(
            [(c, trecho["indexador"])
             for trecho in ent["cadeia_correcao"]
             for c in cadeias.meses(max(trecho["de"],
                                        ent["pagamento"]["competencia"]),
                                    trecho["ate"])
             if trecho["ate"] >= ent["pagamento"]["competencia"]], registro)
        pct_juros = series.indice_mensal("JUROS-PRECATORIO-ACUMULADO",
                                         ent["data_atualizacao"])
        linhas = [
            {"valor": ent["principal"], "coeficiente": coef_total,
             "d_pct": pct_juros, "conta": "principal", "sinal": 1},
            {"valor": ent["juros"], "coeficiente": coef_total,
             "so_correcao": True, "conta": "juros", "sinal": 1},
            {"valor": ent["pagamento"]["principal"],
             "coeficiente": coef_pagamento, "d_pct": pct_juros,
             "conta": "principal", "sinal": -1},
            {"valor": ent["pagamento"]["juros"], "coeficiente": coef_pagamento,
             "so_correcao": True, "conta": "juros", "sinal": -1},
        ]
        r_resumido = metodos.resumido(
            linhas, honorarios_pct=ent["honorarios_advocaticios_pct"])

        # ---- DETALHADO: os TRES passos declarados no item 5.2.1.2 ---------
        r_detalhado = metodos.detalhado(
            _marcos_precatorio(ent, registro),
            honorarios_pct=ent["honorarios_advocaticios_pct"])
    except SerieAusente as e:
        resultado.bloquear(
            "%s — os DOIS metodos param no mesmo ponto: falta a camada (B). "
            "Aqui, e SO isso: `scripts/calculo/test_metodos.py` reproduz esta "
            "fixture INTEIRA nos dois metodos — 4.435,07 · 4.435,04 · delta "
            "0,03 — celula por celula, com os coeficientes das paginas_pdf 91 "
            "e 92. Chegando a serie, este caminho fecha." % e)
        return
    except cadeias.ErroDeDados as e:
        resultado.bloquear("ErroDeDados: %s" % e)
        return

    esp = fx["esperado"]
    resultado.asserir_par(
        "TOTAL DA CONTA",
        esp["metodo_resumido"]["total_da_conta"],
        esp["metodo_detalhado"]["total_da_conta"],
        r_resumido["total_da_conta"], r_detalhado["total_da_conta"],
        fx["tolerancia"]["valor"])


def _marcos_precatorio(ent, registro):
    """1o) ate a apresentacao do precatorio; 2o) ate o fim do prazo
    constitucional; 3o) ate a data final de atualizacao (5.2.1.2, p. 91)."""
    marcos = []
    for i, trecho in enumerate(ent["cadeia_correcao"]):
        marco = {
            "ate": trecho["ate"],
            "coeficiente": motor.coeficiente_de_correcao(
                [(c, trecho["indexador"])
                 for c in cadeias.meses(trecho["de"], trecho["ate"])], registro),
            "taxa_pct": series.indice_mensal("JUROS-DO-TRECHO", trecho["ate"]),
            # INPC/IPCA-E nao englobam juros: o bloco de juros leva o
            # COEFICIENTE e nao a taxa — celula `(juros cor/mon.)`, p. 92.
            "taxa_engloba_correcao": False,
        }
        if i == 0:
            # 1o passo, p. 92: os valores ORIGINARIOS entram no proprio marco e
            # recebem o coeficiente DELE (20.000,00 x 1,0777734324 = 21.555,46;
            # 3.000,00 x 1,0777734324 = 3.233,32). Entravam pelo nominal, e por
            # isso o 1o passo nao fechava.
            marco["entradas"] = [
                {"valor": ent["principal"], "conta": "principal",
                 "coeficiente": marco["coeficiente"]},
                {"valor": ent["juros"], "conta": "juros",
                 "coeficiente": marco["coeficiente"]},
            ]
        pg = ent["pagamento"]
        if trecho["de"] <= pg["competencia"] <= trecho["ate"]:
            marco["pagamentos"] = [
                {"valor": pg["principal"], "conta": "principal",
                 "coeficiente": marco["coeficiente"]},
                {"valor": pg["juros"], "conta": "juros",
                 "coeficiente": marco["coeficiente"]},
            ]
        marcos.append(marco)
    return marcos


# ===========================================================================
# Verificacao de montagem da fixture 3 (CIRCULAR — declarada)
# ===========================================================================
def montagem_fixture_03(fx):
    """Confere a ARITMETICA DE MONTAGEM da fixture 3 a partir dos coeficientes
    e percentuais que a PROPRIA fixture publica no bloco `esperado`.

    ISTO E CIRCULAR e esta declarado como tal: os coeficientes
    (1,4590697197 e 1,0953927279) e os percentuais de juros (209,65% e 14,57%)
    sao produto da serie (B), que este motor nao tem. O que se verifica aqui e
    apenas o criterio de truncamento por etapa (R12) e a soma das colunas —
    NAO a cadeia, NAO os indices, NAO o resultado.
    """
    esperado = fx["esperado"]
    linhas = []
    soma_p, soma_j = ZERO, ZERO
    for det in esperado["detalhe_por_parcela"]:
        principal = moeda(D(det["valor"]) * D(det["coeficiente_correcao"]))
        j = moeda(principal * D(det["percentual_juros"]) / D("100"))
        total = moeda(principal + j)
        linhas.append({
            "competencia": det["competencia"],
            "principal_obtido": principal, "principal_esperado": D(det["principal_corrigido"]),
            "juros_obtido": j, "juros_esperado": D(det["juros"]),
            "total_obtido": total, "total_esperado": D(det["total"]),
        })
        soma_p += principal
        soma_j += j
    return {
        "linhas": linhas,
        "principal_obtido": moeda(soma_p), "principal_esperado": D(esperado["principal_corrigido"]),
        "juros_obtido": moeda(soma_j), "juros_esperado": D(esperado["juros"]),
        "total_obtido": moeda(soma_p + soma_j), "total_esperado": D(esperado["total"]),
    }


# ===========================================================================
# Autotestes — NIVEL 1: o que E implementavel e verificavel so com a skill
# ===========================================================================
def autotestes():
    """Duplicado, de proposito, em scripts/calculo/test_aceite_nivel1.py, que e
    onde o NIVEL 1 vive como criterio de aceite versionado. Aqui ele fica
    porque este runner tem de dizer, na mesma saida, o que PASSA sem serie."""
    linhas = []
    ok_total = True

    # 1 — taxa legal por razao, variante INPC (dois pares publicados)
    for comp, fs, fd, esperado in series.PARES_TAXA_LEGAL_INPC:
        obtido = taxa_legal(fs, fd)
        ok = obtido == D(esperado)
        ok_total = ok_total and ok
        linhas.append(("taxa legal %s (razao, trunc 6)" % comp, esperado, str(obtido), ok))
        # e a subtracao literal, que a skill diz que FALHA
        sub = fator((D(fs) - D(fd)) * D("100"))
        linhas.append(("  subtracao literal %s (deve DIVERGIR)" % comp,
                       esperado, str(sub), sub != D(esperado)))

    # 2 — NMP: tres ramos, e a faixa em que difere de ROUND_HALF_UP
    from decimal import ROUND_HALF_UP
    for v in ("12.44", "12.46", "12.450", "12.454", "12.455", "12.459"):
        obtido = nmp(v)
        half = D(v).quantize(D("0.1"), rounding=ROUND_HALF_UP)
        linhas.append(("NMP(%s)" % v, "regra dos tres ramos", str(obtido),
                       True))
        if obtido != half:
            linhas.append(("  NMP(%s) difere de HALF_UP" % v, str(half), str(obtido), True))

    # 3 — 1/30 e dizima: nao usar o truncamento impresso
    d = um_trinta_avos()
    linhas.append(("1/30 em Decimal", "0.0333... (dizima)", str(d)[:12], True))

    # 4 — R1/R2 sobre as duas cadeias do CJF, nos dois ramos
    c = cadeias.carregar("cjf.condenatorias-gerais.correcao-monetaria.json")
    j = cadeias.carregar("cjf.condenatorias-gerais.juros-mora.json")
    janela = cadeias.meses("1964-01", "2026-06")
    for ramo in ("fazenda-publica", "nao-fazenda-publica"):
        probs = c.checar_cobertura(ramo) + j.checar_cobertura(ramo)
        viol = cadeias.validar_composicao(janela, ramo, c, j)
        linhas.append(("R2 cobertura [%s]" % ramo,
                       "so as sobreposicoes DO ORIGINAL",
                       ("; ".join(probs) if probs else "ok"), True))
        linhas.append(("R1 na composicao [%s]" % ramo, "zero cumulacoes",
                       ("; ".join(viol) if viol else "ok (NOTA 2 suprime a correcao)"),
                       not viol))
        ok_total = ok_total and not viol

    # 5 — pr.imputacao sem default: o motor DEVE recusar
    try:
        motor.imputar("100", "1000", "300")
        linhas.append(("pr.imputacao sem default", "recusa (R20-EXCECAO)",
                       "NAO RECUSOU", False))
        ok_total = False
    except cadeias.ErroDeDados:
        linhas.append(("pr.imputacao sem default", "recusa (R20-EXCECAO)",
                       "recusou", True))

    # 6 — os dois metodos EXISTEM como procedimento: motor que produz um numero
    #     so nao passa nas fixtures 2 e 4, e o runner tem de saber disso.
    tem_os_dois = hasattr(metodos, "resumido") and hasattr(metodos, "detalhado")
    linhas.append(("os DOIS procedimentos implementados",
                   "resumido E detalhado",
                   "sim" if tem_os_dois else "NAO — um numero so nao passa",
                   tem_os_dois))
    ok_total = ok_total and tem_os_dois

    return linhas, ok_total


# ===========================================================================
# PROVA DA ASSERCAO — roda SEM serie, e e o que garante que o runner cobra a
# coisa certa quando a serie chegar.
# ===========================================================================
def prova_da_assercao():
    """As quatro fixtures estao bloqueadas, logo `asserir_par` nunca e exercida
    por elas. Sem esta prova, a correcao do bloco 23 seria uma AFIRMACAO sobre
    codigo que ninguem roda — exatamente o defeito que o bloco veio corrigir.

    Entradas sinteticas, nenhum indice: so o comparador.
    """
    casos = [
        # (rotulo, obtido_resumido, obtido_detalhado, status_esperado)
        ("motor que produz UM numero so", "5218.28", None,
         Resultado.FALTA_UM_METODO),
        ("motor que produz DOIS numeros IGUAIS", "5218.28", "5218.28",
         Resultado.DIVERGENCIA_ZERADA),
        ("motor que produz o par CERTO", "5218.28", "5218.27", None),
        ("motor cujo delta e maior que o declarado", "5218.28", "5218.25",
         Resultado.DIVERGIU),
    ]
    linhas, ok_total = [], True
    for rotulo, r_res, r_det, esperado in casos:
        res = Resultado("prova")
        res.asserir_par("total", "5218.28", "5218.27", r_res, r_det, "0.01")
        res.fechar()
        obtido = res.status
        alvo = esperado or Resultado.BATEU
        ok = obtido == alvo
        ok_total = ok_total and ok
        linhas.append((rotulo, alvo, obtido, ok))
    return linhas, ok_total


# ===========================================================================
def main():
    print("=" * 78)
    print("ACEITACAO — motor de atualizacao")
    print("  NIVEL 1 (aceite DA SKILL): abaixo, e em scripts/calculo/test_aceite_nivel1.py")
    print("  NIVEL 2 (aceite do SISTEMA): as quatro fixtures — EXIGEM SERIE")
    print("=" * 78)

    print("\n--- NIVEL 1 — AUTOTESTES (executavel so com a skill)\n")
    linhas, ok = autotestes()
    for rotulo, esperado, obtido, passou in linhas:
        print("  [%s] %-42s esperado=%-34s obtido=%s"
              % ("ok" if passou else "XX", rotulo, esperado, obtido))

    print("\n--- PROVA DA ASSERCAO (o comparador, sem serie)\n")
    provas, ok_prova = prova_da_assercao()
    for rotulo, alvo, obtido, passou in provas:
        print("  [%s] %-42s deve dar=%-22s deu=%s"
              % ("ok" if passou else "XX", rotulo, alvo, obtido))
    ok = ok and ok_prova

    fixtures = [
        ("fixture-01-fazenda-publica-jun2022.json", _roda_fazenda),
        ("fixture-02-fazenda-publica-jun2026.json", _roda_fazenda),
        ("fixture-03-nao-fazenda-publica-jun2026.json", _roda_nao_fazenda),
        ("fixture-04-precatorio-complementar.json", _roda_precatorio),
    ]

    resultados = []
    for nome, roda in fixtures:
        fx = ler_fixture(nome)
        r = Resultado(fx["id"])
        try:
            roda(fx, r)
        except Exception as e:           # nada de mascarar: o erro aparece
            r.bloquear("%s: %s" % (type(e).__name__, e))
        r.fechar()
        resultados.append((nome, fx, r))

    print("\n--- NIVEL 2 — FIXTURES\n")
    for nome, fx, r in resultados:
        tol = fx["tolerancia"]
        print("=" * 78)
        print("%s" % nome)
        print("  id          : %s" % fx["id"])
        print("  esperado    : total = %s" % fx.get("esperado", {}).get(
            "total", fx.get("esperado", {}).get("metodo_resumido", {}).get("total_da_conta")))
        if tol.get("divergencia_e_assercao"):
            print("  ASSERCAO    : delta(resumido - detalhado) = %s %s, EXATO."
                  % (tol["valor"], tol["unidade"]))
            print("                NAO e banda. Um numero so NAO PASSA; dois numeros")
            print("                iguais FALHAM (zerar = arredondar errado).")
        else:
            print("  comparacao  : IGUALDADE (tolerancia %s — %s)"
                  % (tol["valor"], tol["razao"]))
        print("  STATUS      : %s" % r.status)
        if r.motivo:
            print("  MOTIVO      : %s" % r.motivo)
        for c in r.comparacoes:
            print("    %-28s esperado=%-12s obtido=%-12s delta=%-8s %s"
                  % (c[0], c[1], c[2], c[3], "ok" if c[4] else "FALHOU"))
        for n in r.notas:
            print("  nota        : %s" % n)

    # Montagem da fixture 3 — circular, declarada
    print("=" * 78)
    print("VERIFICACAO DE MONTAGEM DA FIXTURE 03 (CIRCULAR — DECLARADA)")
    print("  Consome os coeficientes e percentuais publicados no bloco `esperado`")
    print("  da propria fixture. Nao reproduz a cadeia nem os indices. Verifica")
    print("  apenas o truncamento por etapa (R12) e a soma das colunas.")
    fx3 = ler_fixture("fixture-03-nao-fazenda-publica-jun2026.json")
    m = montagem_fixture_03(fx3)
    for l in m["linhas"]:
        print("    %s principal esp=%s obt=%s | juros esp=%s obt=%s | total esp=%s obt=%s"
              % (l["competencia"], l["principal_esperado"], l["principal_obtido"],
                 l["juros_esperado"], l["juros_obtido"],
                 l["total_esperado"], l["total_obtido"]))
    print("    TOTAIS principal esp=%s obt=%s | juros esp=%s obt=%s | TOTAL esp=%s obt=%s"
          % (m["principal_esperado"], m["principal_obtido"],
             m["juros_esperado"], m["juros_obtido"],
             m["total_esperado"], m["total_obtido"]))
    montagem_ok = (m["total_obtido"] == m["total_esperado"]
                   and m["principal_obtido"] == m["principal_esperado"]
                   and m["juros_obtido"] == m["juros_esperado"])
    print("    montagem confere: %s  (NAO conta como fixture reproduzida)"
          % ("sim" if montagem_ok else "NAO"))

    print("\n" + "=" * 78)
    print("PLACAR")
    n_bat = sum(1 for _, _, r in resultados if r.status == Resultado.BATEU)
    n_fal = sum(1 for _, _, r in resultados if r.status in Resultado.FALHAS)
    n_blo = sum(1 for _, _, r in resultados if r.status == Resultado.BLOQUEADA)
    print("  bateram: %d   FALHARAM: %d   BLOQUEADAS por dado ausente: %d   de 4"
          % (n_bat, n_fal, n_blo))
    for _, _, r in resultados:
        if r.status in Resultado.FALHAS:
            print("    %-22s %s" % (r.status, r.id))
    print("  NIVEL 1 (autotestes): %s" % ("ok" if ok else "FALHOU"))
    print("  lacunas registradas em: registro-de-lacunas.md")
    print("=" * 78)

    if n_fal or not ok:
        return 1
    if n_blo:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
