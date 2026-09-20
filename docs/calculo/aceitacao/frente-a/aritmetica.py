# -*- coding: utf-8 -*-
"""Aritmetica decimal do motor — R12.

Fonte de cada criterio: skills/calculo-judicial-core/SKILL.md, secao
"Aritmetica — as cinco cadeias de arredondamento", e a tabela identica em
skills/indices-judiciais/SKILL.md (R12).

NENHUM float em lugar nenhum. Toda entrada entra como str e vira Decimal.
"""

from decimal import Decimal, getcontext, ROUND_DOWN, localcontext

# "Precisao plena encadeada": o corpus nao declara um numero de digitos.
# 50 digitos e escolha DESTE modulo, registrada em registro-de-lacunas.md (#9).
getcontext().prec = 50

CASAS_FATOR = 6       # fator de indice e taxa legal — truncamento, 6 casas
CASAS_MOEDA = 2       # valor monetario intermediario e final — truncamento, 2 casas

ZERO = Decimal("0")
UM = Decimal("1")
CEM = Decimal("100")


def D(valor):
    """Converte para Decimal sem jamais passar por float."""
    if isinstance(valor, Decimal):
        return valor
    if isinstance(valor, int):
        return Decimal(valor)
    if isinstance(valor, str):
        return Decimal(valor.strip().replace(".", "").replace(",", ".")
                       if ("," in valor) else valor.strip())
    raise TypeError("float e tipo proibido neste motor (R12): %r" % (valor,))


def truncar(valor, casas):
    """Truncamento (ROUND_DOWN = em direcao a zero), nunca half-up."""
    q = Decimal(1).scaleb(-casas)
    return D(valor).quantize(q, rounding=ROUND_DOWN)


def fator(valor):
    """Fator de indice / taxa legal: 6 casas, truncamento (CJF 4.2.1.1, Nota 6)."""
    return truncar(valor, CASAS_FATOR)


def moeda(valor):
    """Valor monetario intermediario e final: 2 casas, truncamento (CJF)."""
    return truncar(valor, CASAS_MOEDA)


def grandeza_fisica(valor):
    """Hora centesimal, numero de HE: half-up, 2 casas (TRT-3, item 5.3)."""
    from decimal import ROUND_HALF_UP
    return D(valor).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def nmp(valor):
    """NMP (numero de meses do RRA) — TRES RAMOS, 1 casa.

    IN 1500/14, art. 45, paragrafo unico, conforme a skill:
    2a casa < 5 mantem; > 5 sobe; == 5 manda olhar a 3a casa (0-4 mantem, 5-9 sobe).
    NAO e ROUND_HALF_UP: difere na faixa x,y50 a x,y54.
    """
    v = D(valor)
    negativo = v < 0
    v = -v if negativo else v
    inteiro_decimo = truncar(v, 1)
    resto = (v - inteiro_decimo) * CEM          # "casas 2 e 3 em diante"
    segunda = int(truncar(resto, 0))            # 0..9
    if segunda < 5:
        r = inteiro_decimo
    elif segunda > 5:
        r = inteiro_decimo + Decimal("0.1")
    else:
        terceira = int(truncar((resto - segunda) * Decimal(10), 0))
        r = inteiro_decimo + (Decimal("0.1") if terceira >= 5 else ZERO)
    return -r if negativo else r


def um_trinta_avos():
    """1/30 e dizima. Decimal(1)/Decimal(30), nunca o truncamento impresso."""
    return UM / Decimal(30)


def taxa_legal(fator_selic_m, fator_deflator_m_menos_1):
    """R11 — razao entre fatores, NUNCA subtracao de percentuais.

        TL_m = (Fator_Selic_m / Fator_Deflator_{m-1} - 1) * 100

    Seis decimais, truncamento. Piso zero por R6 (CC art. 406, par. 3).
    O deflator e IPCA-15 na regra geral e INPC na variante previdenciaria —
    QUAL deles usar e decisao do chamador, nao desta funcao.
    """
    fs = D(fator_selic_m)
    fd = D(fator_deflator_m_menos_1)
    bruta = (fs / fd - UM) * CEM
    truncada = fator(bruta)
    return piso_zero_taxa_legal(truncada)


def piso_zero_taxa_legal(taxa):
    """R6 — resultado negativo vira zero, nunca negativo."""
    t = D(taxa)
    return ZERO if t < ZERO else t


def piso_nominal_parcela(valor_corrigido, valor_nominal):
    """R5 — piso nominal POR PARCELA.

    Indices negativos ENTRAM no calculo, mas nenhuma parcela do principal fica
    abaixo do nominal. O piso e por parcela, nao sobre o total.
    A instrucao de "dividir pelo indice negativo" NAO se implementa.
    """
    vc, vn = D(valor_corrigido), D(valor_nominal)
    return vn if vc < vn else vc


def juros_simples(base, taxa_pct_acumulada):
    """R4 — juros simples: base * taxa. Acumulacao de taxas por SOMA (Sumula 121/STF)."""
    return D(base) * (D(taxa_pct_acumulada) / CEM)


def acumular_simples(taxas_pct):
    """Soma de percentuais — nunca produto. Sumula 121 do STF."""
    total = ZERO
    for t in taxas_pct:
        total += D(t)
    return total


def acumular_composto(taxas_pct):
    """R4-EXCECAO — juros COMPOSTOS de 27/02/1987 a 03/03/1991 (DL 2.322/87, art. 3).

    Mecanica literal do manual: "1,0% ao mes, c/ taxa capitalizada.
    Ex.: 3 meses = 3,03%".
    ATENCAO (registro-de-lacunas #8): a granularidade diverge entre as fontes —
    TRT-3 ao dia (27/02/1987-03/03/1991), CJF ao mes (mar/87-mar/91). O corpus
    NAO harmoniza. Esta funcao nao decide a fronteira; so a mecanica.
    """
    f = UM
    for t in taxas_pct:
        f = f * (UM + D(t) / CEM)
    return (f - UM) * CEM
