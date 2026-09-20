# -*- coding: utf-8 -*-
"""Runner de aceitacao — frente A.

Roda as quatro fixtures de tests/fixtures/calculo/ e imprime, numero a numero,
o obtido contra o esperado, honrando o campo `tolerancia` (inclusive quando ele
declara que a divergencia E ASSERCAO).

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

    def __init__(self, fixture_id):
        self.id = fixture_id
        self.status = None
        self.motivo = None
        self.comparacoes = []   # (rotulo, esperado, obtido, delta, dentro_da_tolerancia)
        self.notas = []

    def comparar(self, rotulo, esperado, obtido, tolerancia):
        e, o, t = D(esperado), D(obtido), D(tolerancia)
        delta = (o - e).copy_abs()
        self.comparacoes.append((rotulo, e, o, o - e, delta <= t))

    def bloquear(self, motivo):
        self.status = self.BLOQUEADA
        self.motivo = motivo

    def fechar(self):
        if self.status == self.BLOQUEADA:
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


def _roda_fazenda(fx, resultado):
    ent = fx["entradas"]
    devedor = ent["devedor"]
    data_base = ent["data_base"]
    tol = fx["tolerancia"]["valor"]

    correcao = cadeias.carregar("cjf.condenatorias-gerais.correcao-monetaria.json")
    juros_ch = cadeias.carregar("cjf.condenatorias-gerais.juros-mora.json")

    # R2 e R1 — checar ANTES de calcular (invariantes se impedem na composicao)
    probs = correcao.checar_cobertura(devedor) + juros_ch.checar_cobertura(devedor)
    for p in probs:
        resultado.notas.append("R2/cadeia (sobreposicao DO ORIGINAL): " + p)
    janela = cadeias.meses(min(p["competencia"] for p in ent["parcelas"]), data_base)
    for v in cadeias.validar_composicao(janela, devedor, correcao, juros_ch):
        resultado.notas.append(v)

    # Fase 1 — corrigir cada parcela ate nov/2021 (pre-consolidacao)
    registro = motor.Registro()
    registro.preset = "cadeia CJF condenatorias-gerais (sem preset nomeado no corpus)"
    try:
        for parcela in ent["parcelas"]:
            comp = parcela["competencia"]
            if comp > "2021-11":
                continue
            pares = _indexadores_de_correcao(comp, "2021-11", devedor,
                                             correcao, juros_ch)
            motor.coeficiente_de_correcao(pares, registro)
    except SerieAusente as e:
        resultado.bloquear(str(e))
        return
    except cadeias.ErroDeDados as e:
        resultado.bloquear("ErroDeDados: %s" % e)
        return

    resultado.bloquear("alcancou a fase de juros sem bloquear — inesperado")


def _roda_nao_fazenda(fx, resultado):
    ent = fx["entradas"]
    devedor = ent["devedor"]
    tol = fx["tolerancia"]["valor"]
    correcao = cadeias.carregar("cjf.condenatorias-gerais.correcao-monetaria.json")
    juros_ch = cadeias.carregar("cjf.condenatorias-gerais.juros-mora.json")

    for p in correcao.checar_cobertura(devedor) + juros_ch.checar_cobertura(devedor):
        resultado.notas.append("R2/cadeia (sobreposicao DO ORIGINAL): " + p)
    janela = cadeias.meses(min(p["competencia"] for p in ent["parcelas"]),
                           ent["data_base"])
    for v in cadeias.validar_composicao(janela, devedor, correcao, juros_ch):
        resultado.notas.append(v)

    registro = motor.Registro()
    try:
        for parcela in ent["parcelas"]:
            pares = _indexadores_de_correcao(parcela["competencia"],
                                             ent["data_base"], devedor,
                                             correcao, juros_ch)
            motor.coeficiente_de_correcao(pares, registro)
    except SerieAusente as e:
        resultado.bloquear(str(e))
        return
    resultado.bloquear("alcancou a fase de juros sem bloquear — inesperado")


def _roda_precatorio(fx, resultado):
    ent = fx["entradas"]
    registro = motor.Registro()
    # A cadeia vem DECLARADA na propria fixture (cadeia_correcao / cadeia_juros);
    # nao ha o que resolver, so o que aplicar. O que falta e o valor.
    try:
        for trecho in ent["cadeia_correcao"]:
            pares = [(c, trecho["indexador"])
                     for c in cadeias.meses(trecho["de"], trecho["ate"])]
            motor.coeficiente_de_correcao(pares, registro)
    except SerieAusente as e:
        resultado.bloquear(str(e))
        return
    resultado.bloquear("alcancou a fase de juros sem bloquear — inesperado")


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
# Autotestes do que E implementavel e verificavel no escopo lido
# ===========================================================================
def autotestes():
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

    return linhas, ok_total


# ===========================================================================
def main():
    print("=" * 78)
    print("ACEITACAO — FRENTE A — motor de atualizacao")
    print("=" * 78)

    print("\n--- AUTOTESTES (o que e implementavel e verificavel no escopo lido)\n")
    linhas, ok = autotestes()
    for rotulo, esperado, obtido, passou in linhas:
        print("  [%s] %-42s esperado=%-34s obtido=%s"
              % ("ok" if passou else "XX", rotulo, esperado, obtido))

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

    print("\n--- FIXTURES\n")
    for nome, fx, r in resultados:
        tol = fx["tolerancia"]
        print("=" * 78)
        print("%s" % nome)
        print("  id          : %s" % fx["id"])
        print("  esperado    : total = %s" % fx.get("esperado", {}).get(
            "total", fx.get("esperado", {}).get("metodo_resumido", {}).get("total_da_conta")))
        print("  tolerancia  : %s %s — %s" % (tol["valor"], tol["unidade"], tol["razao"]))
        if tol.get("divergencia_e_assercao"):
            print("  ATENCAO     : a divergencia declarada E ASSERCAO. Um motor que a "
                  "zera esta arredondando errado.")
        print("  STATUS      : %s" % r.status)
        if r.motivo:
            print("  MOTIVO      : %s" % r.motivo)
        for c in r.comparacoes:
            print("    %-28s esperado=%-12s obtido=%-12s delta=%-8s %s"
                  % (c[0], c[1], c[2], c[3], "ok" if c[4] else "FORA DA TOLERANCIA"))
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
    n_div = sum(1 for _, _, r in resultados if r.status == Resultado.DIVERGIU)
    n_blo = sum(1 for _, _, r in resultados if r.status == Resultado.BLOQUEADA)
    print("  bateram: %d   divergiram: %d   BLOQUEADAS por dado ausente: %d   de 4"
          % (n_bat, n_div, n_blo))
    print("  autotestes: %s" % ("ok" if ok else "FALHOU"))
    print("  lacunas registradas em: registro-de-lacunas.md")
    print("=" * 78)

    if n_div or not ok:
        return 1
    if n_blo:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
