# -*- coding: utf-8 -*-
"""Camada (A) — cadeias temporais periodo -> regra.

Le os JSON de docs/calculo/tabelas-normativas/, que sao ponteiro declarado de
`calculo-judicial-atualizacao` ("Cadeias em schema", secao Ponteiros) e de
`references/civel-federal.md` S12.

Faz TRES coisas e so essas: resolver o segmento de uma competencia, checar R2
(sem lacuna nem sobreposicao) e checar R1 (englobamento exclusivo).
NAO sabe quanto vale indice nenhum — isso e (B), em series.py.
"""

import io
import json
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DIR_TABELAS = os.path.join(RAIZ, "docs", "calculo", "tabelas-normativas")


class ErroDeDados(Exception):
    """R21 / R2 / R1 — violacao que o motor recusa, nao contorna."""


def _comp_para_int(comp):
    ano, mes = comp.split("-")
    return int(ano) * 12 + int(mes) - 1


def _int_para_comp(n):
    return "%04d-%02d" % (n // 12, n % 12 + 1)


def meses(inicio, fim):
    """Lista de competencias AAAA-MM, inclusive nas duas pontas."""
    a, b = _comp_para_int(inicio), _comp_para_int(fim)
    return [_int_para_comp(n) for n in range(a, b + 1)]


class Cadeia(object):
    def __init__(self, dados, arquivo):
        self.arquivo = arquivo
        self.id = dados.get("id")
        self.componente = dados.get("componente")
        self.segmentos = dados.get("segmentos", [])
        self.dominio_condicoes = dados.get("dominio_condicoes")
        self.termo_inicial = dados.get("termo_inicial")
        self.notas = dados.get("notas", [])

    # --- R2 -----------------------------------------------------------------
    def checar_cobertura(self, condicao=None):
        """R2 — exaustividade se DECLARA, nao se presume.

        Ramos condicionados so esgotam o dominio se a cadeia declarar
        `dominio_condicoes`. Sem a declaracao, o universo 'nenhuma condicao se
        aplica' continua sendo cobrado.
        """
        segs = self._do_ramo(condicao)
        if not segs:
            raise ErroDeDados("ramo sem segmento: %s / %s" % (self.id, condicao))
        ordenados = sorted(segs, key=lambda s: _comp_para_int(s["inicio"]))
        problemas = []
        for anterior, atual in zip(ordenados, ordenados[1:]):
            fim_ant = _comp_para_int(anterior["fim"])
            ini_atu = _comp_para_int(atual["inicio"])
            if ini_atu > fim_ant + 1:
                problemas.append(
                    "lacuna de %s a %s" % (_int_para_comp(fim_ant + 1),
                                           _int_para_comp(ini_atu - 1)))
            elif ini_atu <= fim_ant:
                # R-08-04: em cadeia de indices NOMINAIS, fim e inicio no mesmo
                # mes NAO e dupla contagem, e o manual o diz expressamente.
                nominais = (anterior.get("tipo_indexador") == "nominal"
                            and atual.get("tipo_indexador") == "nominal")
                if not (nominais and ini_atu == fim_ant):
                    problemas.append(
                        "sobreposicao de %s a %s (%s x %s)"
                        % (atual["inicio"], anterior["fim"],
                           anterior.get("indexador") or anterior.get("taxa"),
                           atual.get("indexador") or atual.get("taxa")))
        if condicao is not None and not self.dominio_condicoes:
            problemas.append(
                "dominio_condicoes NAO declarado — R2 cobra o universo "
                "'nenhuma condicao se aplica'")
        return problemas

    def _do_ramo(self, condicao):
        """Filtra por ramo com igualdade EXATA de valor.

        `in` sobre a string seria bug silencioso: "fazenda-publica" e substring
        de "nao-fazenda-publica" e traria os dois ramos.
        """
        out = []
        for s in self.segmentos:
            cond = s.get("condicao") or s.get("condicoes")
            if cond is None:
                out.append(s)
            elif condicao is not None and cond.get("devedor") == condicao:
                out.append(s)
        return out

    # --- resolucao ----------------------------------------------------------
    def segmento(self, competencia, condicao=None):
        n = _comp_para_int(competencia)
        achados = [s for s in self._do_ramo(condicao)
                   if _comp_para_int(s["inicio"]) <= n <= _comp_para_int(s["fim"])]
        if not achados:
            raise ErroDeDados(
                "R2: competencia %s sem segmento em %s (ramo %s)"
                % (competencia, self.id, condicao))
        return achados


def carregar(nome_arquivo):
    caminho = os.path.join(DIR_TABELAS, nome_arquivo)
    with io.open(caminho, "r", encoding="utf-8") as fh:
        return Cadeia(json.load(fh), nome_arquivo)


# --- R1 ---------------------------------------------------------------------
def compor(competencia, devedor, cadeia_correcao, cadeia_juros):
    """Compoe os componentes aplicaveis a UMA competencia, com R1 ja imposto.

    "Devem ser impedidas NA COMPOSICAO, nao detectadas no resultado"
    (calculo-judicial-core, Invariantes).

    Regra de supressao — NOTA 2 do item 4.2.1, `pagina_pdf` 49, literal:
      "Se os juros de mora corresponderem a taxa Selic, o IPCA-E deixa de ser
       aplicado como indexador de correcao monetaria, a partir da incidencia da
       Selic (que engloba juros e correcao monetaria)."
    Generalizada para 'taxa legal' pelo mesmo fundamento de R1.

    Devolve dict com `correcao` (segmento ou None) e `juros` (segmento).
    """
    seg_j = cadeia_juros.segmento(competencia, devedor)[0]
    segs_c = cadeia_correcao.segmento(competencia, devedor)
    engloba_correcao = "correcao-monetaria" in (seg_j.get("engloba") or [])
    if engloba_correcao:
        return {"correcao": None, "juros": seg_j,
                "r1_suprimiu": [s.get("indexador") for s in segs_c]}
    return {"correcao": segs_c[0], "juros": seg_j, "r1_suprimiu": []}


def validar_composicao(competencias, devedor, cadeia_correcao, cadeia_juros):
    """R1 sobre a composicao efetiva. Zero violacoes e o resultado correto —
    a sobreposicao bruta das duas cadeias e do ORIGINAL e resolvida pela NOTA 2.
    """
    violacoes = []
    for comp in competencias:
        c = compor(comp, devedor, cadeia_correcao, cadeia_juros)
        if c["correcao"] is not None and \
                "correcao-monetaria" in (c["juros"].get("engloba") or []):
            violacoes.append("R1 em %s: %s + %s" % (
                comp, c["correcao"].get("indexador"),
                c["juros"].get("taxa") or "englobante"))
    return violacoes


def checar_englobamento(segmentos_de_correcao, segmentos_de_juros):
    """R1 — segmento cujo `engloba` cobre correcao E juros nao admite outro do
    mesmo componente no mesmo intervalo. SELIC e taxa legal englobam os dois.
    """
    violacoes = []
    for j in segmentos_de_juros:
        if "correcao-monetaria" not in (j.get("engloba") or []):
            continue
        ij, fj = _comp_para_int(j["inicio"]), _comp_para_int(j["fim"])
        for c in segmentos_de_correcao:
            ic, fc = _comp_para_int(c["inicio"]), _comp_para_int(c["fim"])
            if max(ij, ic) <= min(fj, fc):
                violacoes.append(
                    "R1: %s (juros, engloba correcao) x %s (correcao) em %s..%s"
                    % (j.get("taxa") or j.get("indexador"), c.get("indexador"),
                       _int_para_comp(max(ij, ic)), _int_para_comp(min(fj, fc))))
    return violacoes
