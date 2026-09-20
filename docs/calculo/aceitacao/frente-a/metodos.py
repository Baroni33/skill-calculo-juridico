# -*- coding: utf-8 -*-
"""Os DOIS procedimentos do Manual CJF — resumido e detalhado.

No bloco 22 este modulo NAO EXISTIA, e por isso nao podia existir: "metodo
resumido" e "metodo detalhado" nunca eram definidos em lugar algum do escopo
lido. O motor produzia UM numero, e a assercao das fixtures 2 e 4 e a DIFERENCA
ENTRE DOIS.

Agora existe o que implementar. Fonte, em ordem de precedencia:
  skills/calculo-judicial-atualizacao/references/metodos-resumido-e-detalhado.md
  docs/calculo/consolidado/02-atualizacao.md          SS 10-A.1 e 10-A.2
  docs/calculo/consolidado/02-atualizacao-detalhe.md  SS 10-A.0 a 10-A.9

A DIFERENCA ESTRUTURAL, e e a unica: o DETALHADO agrega por coluna antes de
aplicar a taxa do marco seguinte; o RESUMIDO nunca agrega antes do fim. Tudo o
mais decorre de QUANDO se trunca.

O QUE O BLOCO 23 CORRIGIU NO `detalhado` — tres defeitos, todos medidos contra
celula PUBLICADA (pagina_pdf 51 e 52):

  1. UM coeficiente por marco sobre o agregado. O marco `a)` tem coeficiente
     POR PARCELA (1,1420100005 e 1,1339588923) e truncamento POR LINHA:
     27,97 + 27,78 = 55,75. Sobre o agregado (2.275,96 x 2,45%) daria 55,76, e
     o manual publica 55,75. Por isso `entradas` levam `coeficiente` proprio;
  2. "T3 sem nova taxa". O manual APLICA a taxa sobre o bloco de juros nos dois
     exemplos de 4.2.1.1: `Dez./2021 R$ 55,75 (juros) 5,05 -> R$ 2,81` (p. 51) e
     `Dez./2021 R$ 55,75 (juros) 43,89 -> R$ 24,46` (p. 52). A propria
     SS 10-A.8 do consolidado ja listava `55,75 x 43,89% = 24,468675 -> 24,46`
     como prova de truncamento. O discriminante NAO e "juros nunca rendem
     juros": e R1 — quando o indexador de juros do trecho ENGLOBA a correcao
     (SELIC, taxa legal), a taxa e a UNICA correcao que o bloco de juros recebe
     naquele trecho, e por isso incide sobre ele; quando o trecho tem
     coeficiente proprio (INPC, IPCA-E), o bloco leva o COEFICIENTE e NAO a
     taxa — celula `(juros correção monetária)` da p. 52 e `(juros cor/mon.)`
     da p. 92. E EXATAMENTE a assimetria que o RESUMIDO ja imprime na legenda:
     `(H) = (C + G) x E%` (SELIC sobre principal E juros) contra
     `(I) = C x F%` (taxa legal so sobre o principal);
  3. UMA `taxa_pct` por marco. O marco `b)` aplica 43,89% ao agregado de
     dez/2021 E 42,39% a parcela de fev/2022, no mesmo passo. Por isso cada
     `entrada` pode trazer a sua taxa, e so herda a do marco quando cala.

Com os tres, `detalhado` reproduz 3.484,95 (p. 51), 5.218,27 (p. 52) e
4.435,04 (p. 92) CELULA POR CELULA, a partir dos coeficientes impressos.
`scripts/calculo/test_metodos.py` e onde isso e cobrado.

R12 vale nos dois itens: TRUNCAMENTO a cada celula, 2 casas para valor. A obs.
da pagina_pdf 92 escreve "arredondamento" e a aritmetica faz truncamento
(D8-D33). Rodar em precisao plena FAZ OS DOIS CONVERGIREM e zera a divergencia
que as fixtures asseveram — por isso o truncamento por etapa e obrigatorio aqui,
e e a excecao declarada da regra de "precisao plena encadeada".

Nenhum float. Coeficiente algum e inventado: quem os fornece e o chamador, e a
serie ausente sobe como SerieAusente.
"""

from decimal import Decimal

from aritmetica import D, ZERO, CEM, moeda

CASAS_COEFICIENTE = 10   # (B) e impresso com 10 casas (paginas 52, 53, 91 e 92)


# ===========================================================================
# RESUMIDO — 5.2.1.1 e a legenda de colunas de 4.2.1.1 (pp. 52 e 53)
# ===========================================================================
def resumido(linhas, honorarios_pct=None):
    """Uma linha por parcela devida e uma por pagamento, UM coeficiente ate a
    data-base, taxas aplicadas sobre o principal ja corrigido.

    `linhas`: lista de dicts
        valor            (str/Decimal)  — (A), nominal
        coeficiente      (Decimal)      — (B), acumulado ate a DATA-BASE, 10 casas
        d_pct            juros ate 12/2021           -> (G) = C x D%
        e_pct            SELIC                        -> (H) = (C + G) x E%
        f_pct            taxa a partir de out./2025   -> (I) = C x F%
        sinal            +1 parcela devida, -1 pagamento (S8)
        so_correcao      True na parcela de JUROS do calculo original: ela leva
                         so correcao monetaria, celula "(juros cor/mon.)" (S8)
        conta            "principal" | "juros" — a coluna em que o (L) entra

    Devolve dict com subtotais e total, tudo em Decimal truncado a 2 casas.
    """
    soma = {"principal": ZERO, "juros": ZERO}
    detalhe = []
    for ln in linhas:
        sinal = D(ln.get("sinal", 1))
        a = D(ln["valor"])
        b = D(ln["coeficiente"])
        c = moeda(a * b)                                     # S3
        if ln.get("so_correcao"):
            g = h = i = ZERO                                 # S8
        else:
            g = moeda(c * D(ln.get("d_pct", 0)) / CEM)       # S4
            h = moeda((c + g) * D(ln.get("e_pct", 0)) / CEM)  # S5
            i = moeda(c * D(ln.get("f_pct", 0)) / CEM)       # S6
        j = g + h + i                                        # S7 — soma de coluna
        conta = ln.get("conta", "principal")
        if conta == "principal":
            soma["principal"] += sinal * c
            soma["juros"] += sinal * j
        else:
            # linha de JUROS do calculo original: (C) ja e coluna de juros
            soma["juros"] += sinal * (c + j)
        detalhe.append({"C": c, "G": g, "H": h, "I": i, "J": j, "L": c + j,
                        "sinal": sinal, "conta": conta})

    subtotal_principal = moeda(soma["principal"])
    subtotal_juros = moeda(soma["juros"])
    saida = {
        "metodo": "resumido",
        "detalhe": detalhe,
        "subtotal_principal": subtotal_principal,
        "subtotal_juros": subtotal_juros,
        "subtotal": moeda(subtotal_principal + subtotal_juros),
    }
    _aplica_honorarios(saida, honorarios_pct)                # S9
    return saida


# ===========================================================================
# DETALHADO — 5.2.1.2, com os marcos de 4.2.1.1
# ===========================================================================
def detalhado(marcos, honorarios_pct=None):
    """Passo a passo, um marco por vez, AGREGANDO por coluna antes do marco
    seguinte.

    `marcos`: lista de dicts, EM ORDEM
        coeficiente   (Decimal) — do TRECHO so, sobre o AGREGADO (T1 e T3a).
                      Ausente = 1: trecho cujo indexador de juros engloba a
                      correcao nao tem coeficiente proprio.
        taxa_pct      (Decimal) — a taxa DO TRECHO, sobre o agregado (T2)
        taxa_engloba_correcao  (bool) — R1: o indexador de juros do trecho
                      engloba correcao monetaria (SELIC, taxa legal). Se SIM, a
                      taxa incide TAMBEM sobre o bloco de juros (T3b), porque e
                      a unica correcao que esse bloco recebe no trecho.
        entradas      lista de {valor, conta, coeficiente, taxa_pct} que entram
                      NESTE marco (T5). `coeficiente` ausente = 1 (nominal);
                      `taxa_pct` ausente = a taxa do proprio marco. Entrada de
                      conta "juros" NAO recebe taxa (sem juros sobre juros).
        pagamentos    lista de {valor, conta, coeficiente} subtraidos DENTRO do
                      passo do marco (T6)

    Devolve dict com a mesma forma de `resumido`, mais `passos`.
    """
    principal, juros = ZERO, ZERO
    passos = []
    for marco in marcos:
        coef = D(marco.get("coeficiente", 1))
        taxa = D(marco.get("taxa_pct", 0))
        principal = moeda(principal * coef)                  # T1
        juros = moeda(juros * coef)                          # T3a
        novos = ZERO                                         # juros do trecho
        if taxa != ZERO:
            novos = moeda(novos + moeda(principal * taxa / CEM))         # T2
            if marco.get("taxa_engloba_correcao"):
                novos = moeda(novos + moeda(juros * taxa / CEM))         # T3b
        for e in marco.get("entradas", []):                  # T5
            c = moeda(D(e["valor"]) * D(e.get("coeficiente", 1)))
            if e.get("conta", "principal") == "juros":
                juros = moeda(juros + c)       # (juros cor/mon.): sem taxa
                continue
            principal = moeda(principal + c)
            t_e = D(e["taxa_pct"]) if "taxa_pct" in e else taxa
            if t_e != ZERO:
                novos = moeda(novos + moeda(c * t_e / CEM))
        juros = moeda(juros + novos)
        for p in marco.get("pagamentos", []):                # T6
            pago = moeda(D(p["valor"]) * D(p["coeficiente"]))
            if p.get("conta", "principal") == "juros":
                juros = moeda(juros - pago)
            else:
                principal = moeda(principal - pago)
        passos.append({"ate": marco.get("ate"), "principal": principal,
                       "juros": juros, "total": moeda(principal + juros)})   # T4

    saida = {
        "metodo": "detalhado",
        "passos": passos,
        "subtotal_principal": principal,
        "subtotal_juros": juros,
        "subtotal": moeda(principal + juros),
    }
    _aplica_honorarios(saida, honorarios_pct)                # T7 == S9
    return saida


def _aplica_honorarios(saida, pct):
    """Honorarios incidem sobre principal e sobre juros SEPARADAMENTE (5.2.1,
    p. 90: 'separam-se as parcelas que compoem o total do debito'). Sao
    identicos nos dois metodos na fixture 4 — e isso ISOLA a divergencia na
    atualizacao."""
    if pct is None:
        saida["total_da_conta"] = saida["subtotal"]
        return saida
    p = D(pct)
    hp = moeda(saida["subtotal_principal"] * p / CEM)
    hj = moeda(saida["subtotal_juros"] * p / CEM)
    saida["honorarios_principal"] = hp
    saida["honorarios_juros"] = hj
    saida["honorarios_total"] = moeda(hp + hj)
    saida["total_da_conta_principal"] = moeda(saida["subtotal_principal"] + hp)
    saida["total_da_conta_juros"] = moeda(saida["subtotal_juros"] + hj)
    saida["total_da_conta"] = moeda(saida["total_da_conta_principal"]
                                    + saida["total_da_conta_juros"])
    return saida
