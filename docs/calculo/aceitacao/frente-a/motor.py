# -*- coding: utf-8 -*-
"""Motor de atualizacao — o que as skills permitem implementar.

Ordem minima operacional (calculo-judicial-core, secao Procedimento):
    0 CLASSIFICAR -> 1 REGIME -> 2 PARAMETRO -> 3 APURAR -> 4 ATUALIZAR -> 5 REGISTRAR

O que este modulo NAO faz, por falta de dado declarado:
  - nao inventa valor de indice: pede a series.py e propaga SerieAusente;
  - nao arbitra preset sem default (R20-EXCECAO);
  - nao "conserta" divergencia declarada de fixture.
"""

from decimal import Decimal

from aritmetica import (D, ZERO, UM, CEM, fator, moeda, piso_nominal_parcela,
                        piso_zero_taxa_legal, acumular_simples, truncar)
import series
from series import SerieAusente
from cadeias import meses, ErroDeDados


class Registro(object):
    """R13 — reprodutibilidade: preset, overrides com justificativa, versoes."""

    def __init__(self):
        self.preset = None
        self.overrides = []
        self.versao_normativa = "docs/calculo/tabelas-normativas @ arvore de trabalho"
        self.versao_series = "NAO EXISTE — series.py nao tem campo `versao` "\
                             "(indices-judiciais, Limitacoes 3: bloqueia R13)"
        self.marcas = []
        self.linhas = []

    def marcar(self, texto):
        if texto not in self.marcas:
            self.marcas.append(texto)

    def linha(self, texto):
        self.linhas.append(texto)


# ---------------------------------------------------------------------------
# Correcao monetaria
# ---------------------------------------------------------------------------
def coeficiente_de_correcao(indexadores_por_mes, registro=None):
    """Acumula fatores mensais de correcao.

    `indexadores_por_mes`: lista de (competencia, nome_do_indexador).
    Cada valor vem de series.indice_mensal — que levanta SerieAusente quando o
    dado nao existe no escopo lido. Nao ha fallback: R5 manda o indice negativo
    ENTRAR, nao manda inventar o ausente.

    ATENCAO R3: a defasagem (`aplicacao`) vive na CADEIA, nao na serie. Quem
    monta `indexadores_por_mes` ja deve ter deslocado. Este motor nao desloca
    sozinho porque o corpus nao declara o eixo do par 13 (30/08/2024).
    """
    f = UM
    for competencia, indexador in indexadores_por_mes:
        pct = series.indice_mensal(indexador, competencia)
        f = f * (UM + pct / CEM)
        if registro is not None:
            registro.linha("correcao %s %s = %s%%" % (competencia, indexador, pct))
    return fator(f)


def corrigir(valor_nominal, coeficiente):
    """Aplica o coeficiente e honra R5 — piso nominal POR PARCELA."""
    bruto = D(valor_nominal) * D(coeficiente)
    return moeda(piso_nominal_parcela(bruto, D(valor_nominal)))


# ---------------------------------------------------------------------------
# Juros de mora — R4 (simples), Sumula 121/STF (acumulacao por SOMA)
# ---------------------------------------------------------------------------
def percentual_de_juros(taxas_mensais_pct):
    """Soma de percentuais. NUNCA produto (R4 + Sumula 121/STF)."""
    return acumular_simples(taxas_mensais_pct)


def juros(base, percentual_acumulado):
    return moeda(D(base) * D(percentual_acumulado) / CEM)


# ---------------------------------------------------------------------------
# As formulas de `aplicacao` do CJF — D1 e D2 (civel-federal.md S5)
# ---------------------------------------------------------------------------
def d1_competencias(competencia_inicial, mes_de_pagamento):
    """D1 — Selic/taxa legal NO MES POSTERIOR ao de sua competencia,
    INCLUSIVE para o mes de pagamento. Fazenda a partir de dez/2021.
    Ex. do manual: a Selic de dez/2021 e computada em jan/2022.
    Devolve as competencias DA SERIE que alimentam o intervalo.
    """
    todos = meses(competencia_inicial, mes_de_pagamento)
    # o mes de pagamento e alimentado pela competencia anterior; e a serie do
    # proprio mes de pagamento NAO entra (ela seria computada no mes seguinte).
    return todos[:-1] if len(todos) > 1 else []


def d2_competencias(termo_inicial_juros, mes_de_pagamento):
    """D2 — Selic do mes SEGUINTE ao termo inicial dos juros ate o mes ANTERIOR
    ao pagamento, e 1% no mes do pagamento. Nao-Fazenda; e Fazenda jan/2003 a
    jun/2009. Devolve (competencias_da_serie, acrescimo_fixo_pct).
    """
    todos = meses(termo_inicial_juros, mes_de_pagamento)
    return todos[1:-1], D("1")


# ---------------------------------------------------------------------------
# Consolidacao de dez/2021 — R-08-12 e R-08-14
# ---------------------------------------------------------------------------
def consolidar_dez_2021(principal_corrigido_ate_nov_2021, juros_ate_nov_2021,
                        indice_nov_2021_pct, registro=None):
    """NOTA 5 do item 4.2.1, literal:
      a) credito consolidado com base em dez/2021 pelos criterios ate entao
         aplicaveis, considerando o indice de nov/2021 e os juros de dez/2021
         (0,4412%);
      b) sobre o consolidado, SEM EXCLUSAO DE QUALQUER PARCELA, incide a Selic
         a partir de jan/2022;
      c) o resultado ('Juros Selic') e INTEGRALMENTE somado a 'Juros ate 12/2021'.

    LACUNA REGISTRADA (#3): o corpus da o indice de nov/2021 e os juros de
    dez/2021, mas NAO da a ordem exata entre aplicar 1,17% e aplicar 0,4412%,
    nem sobre que base incidem os 0,4412%. Aqui se implementa a leitura literal
    da alinea (a): corrige o principal por nov/2021 e soma 0,4412% ao
    percentual de juros do principal corrigido. Isso e COMPOSICAO, nao citacao.
    """
    p = moeda(D(principal_corrigido_ate_nov_2021) * (UM + D(indice_nov_2021_pct) / CEM))
    j = moeda(D(juros_ate_nov_2021))
    consolidado = moeda(p + j)
    if registro is not None:
        registro.linha("consolidado dez/2021 = principal %s + juros %s = %s"
                       % (p, j, consolidado))
        registro.marcar("consolidacao dez/2021 aplicada (R-08-14: sem exclusao "
                        "de qualquer parcela)")
    return {"principal": p, "juros": j, "consolidado": consolidado}


def juros_selic_sobre_consolidado(principal, juros_ate_12_2021, selic_pct_acumulada):
    """R-08-14 — a Selic incide sobre o consolidado INTEIRO, principal E juros.
    O resultado vai INTEGRALMENTE para a parcela 'Juros ate 12/2021'.
    """
    sp = moeda(D(principal) * D(selic_pct_acumulada) / CEM)
    sj = moeda(D(juros_ate_12_2021) * D(selic_pct_acumulada) / CEM)
    return {"sobre_principal": sp, "sobre_juros": sj, "juros_selic": moeda(sp + sj)}


# ---------------------------------------------------------------------------
# Honorarios (fixture 4) — incidem sobre principal e juros SEPARADAMENTE
# ---------------------------------------------------------------------------
def honorarios(subtotal_principal, subtotal_juros, pct):
    hp = moeda(D(subtotal_principal) * D(pct) / CEM)
    hj = moeda(D(subtotal_juros) * D(pct) / CEM)
    return {"principal": hp, "juros": hj, "total": moeda(hp + hj)}


# ---------------------------------------------------------------------------
# R23 / R10 — descarregar e imputar
# ---------------------------------------------------------------------------
def descarregar(saldo_total, juros_contidos):
    """R23 — antes de aplicar juros sobre saldo remanescente, os juros ja
    contidos nesse saldo devem ser EXCLUIDOS. Nao descarregar produz anatocismo
    (delta medido de +R$ 30.452,43 — o maior do corpus).
    """
    return moeda(D(saldo_total) - D(juros_contidos))


def imputar(abatimento, principal, juros_, preset=None):
    """R10 — pagamentos parciais.

    O preset `pr.imputacao` NAO TEM DEFAULT (R20-EXCECAO). Escolher seria o
    motor tomar posicao juridica: `art. 354` tem ZERO ocorrencias em 471
    paginas; `proporcional` ocorre 101 vezes so no segmento que o aplica.
    Este motor recusa arbitrar.
    """
    if preset is None:
        raise ErroDeDados(
            "pr.imputacao sem default (R20-EXCECAO): o motor nao arbitra a "
            "ordem de imputacao. Informe 'civel-art-354' ou 'trabalhista-proporcional'.")
    a, p, j = D(abatimento), D(principal), D(juros_)
    if preset == "civel-art-354":            # juros primeiro
        em_juros = j if a >= j else a
        em_principal = a - em_juros
    elif preset == "trabalhista-proporcional":
        d = p + j
        if d == ZERO:
            raise ErroDeDados("divisao por zero na imputacao proporcional")
        em_principal = moeda(p / d * a)
        em_juros = moeda(j / d * a)
    else:
        raise ErroDeDados("preset de imputacao desconhecido: %s" % preset)
    return {"em_principal": moeda(em_principal), "em_juros": moeda(em_juros)}
