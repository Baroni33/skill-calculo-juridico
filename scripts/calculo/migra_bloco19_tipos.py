#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bloco 19 — reescreve `tipo_indexador` nas cadeias, a partir do catálogo.

Roda UMA VEZ e é idempotente: reaplicar não muda mais nada. Mantido no
repositório porque a alteração que ele faz tem de ser auditável por quem vier
depois — qual segmento mudou, de que valor para qual, e com que fonte.

O que muda, e SÓ isto:

* **Selic** — `englobante` → `percentual`. Englobamento é fato de R1 e vive no
  campo `engloba`, que NÃO é tocado aqui;
* **taxa-legal** — `englobante` → `indeterminado`, pendência `P19-01`. A fonte
  externa não a alcança, e `percentual` por analogia com a SELIC seria dedução;
* **IPCA-E/IBGE** e **IPCA-15/IBGE** — `indeterminado` → `janela-deslocada`;
* **TR** e **remuneração básica da caderneta de poupança (TR)** — seguem
  `indeterminado`, mas trocam `tipo_indexador_pendencia` por
  `tipo_indexador_razao`: agora HÁ fonte, e ela diz que o índice não cabe.

`encoding='utf-8'` explícito na leitura e na escrita. Nenhum float em caminho
algum — aqui não há aritmética, e é assim que fica.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TABELAS = RAIZ / "docs" / "calculo" / "tabelas-normativas"

SELIC_FONTE = (
    "FONTE EXTERNA AO CORPUS (tabela do bloco 19, verificada fora do agente) — "
    "'SELIC acumulada' é classe `percentual`: reflete M, o próprio mês de "
    "competência. Era 'englobante', e 'englobante' era ERRO DE CATEGORIA — "
    "englobamento é fato de R1 e quem o grava é o campo 'engloba', que não "
    "mudou. O efeito do erro era deixar a SELIC cega para R3."
)

LEGAL_POR_QUE = (
    "A tabela externa do bloco 19 NÃO alcança a taxa legal: ela nomeia 'SELIC "
    "acumulada' e mais nada do gênero. Classificá-la 'percentual' por analogia "
    "com a SELIC é a dedução proibida — e a analogia é frágil por fonte, "
    "porque R11 registra a taxa legal como DERIVADA por razão entre fatores "
    "(TL = Fator_Selic / Fator_Deflator − 1), não índice publicado. No corpus, "
    "nenhuma linha lhe atribui tipo com citação de item e pagina_pdf (ver "
    "ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_19). Perdeu 'englobante' porque "
    "'englobante' era fato de R1 no campo de R3; o englobamento em si segue "
    "intacto no campo 'engloba'."
)

IPCA_E_FONTE = (
    "FONTE EXTERNA AO CORPUS (IBGE, verificada fora do agente) — o IPCA-E "
    "mensal das tabelas judiciais É o IPCA-15, cujo período de coleta vai do "
    "dia 16 do mês anterior ao dia 15 do mês de referência: metade da janela "
    "em M−1, metade em M. Identificação declarada pela própria fonte, não por "
    "semelhança de nome."
)

IPCA_15_FONTE = (
    "FONTE EXTERNA AO CORPUS (IBGE, verificada fora do agente) — o IPCA-15 "
    "difere do IPCA apenas no PERÍODO DE COLETA, do dia 16 do mês anterior ao "
    "dia 15 do mês de referência, e na abrangência geográfica."
)

TR_FONTE = (
    "FONTE EXTERNA AO CORPUS (BCB, verificada fora do agente) — TBF, Redutor-R "
    "e TR são divulgados para PERÍODO ENTRE DATAS DE ANIVERSÁRIO, não para mês "
    "calendário (17/02 a 17/03, 03/05 a 03/06, 05/10 a 05/11); e a TR é "
    "PREFIXADA, com variação divulgada para o mês seguinte."
)

TR_RAZAO = "período entre datas de aniversário e prefixação"

TR_FECHAMENTO = (
    "NÃO se fecha esperando fonte. A fonte chegou, e o que ela diz é que a TR "
    "não cabe em mês calendário — logo não há classe a atribuir. Fecharia só "
    "se a modelagem ganhar classe para período entre datas de aniversário, ou "
    "se a cadeia declarar a conversão para competência em 'aplicacao'. Era "
    "'tipo_indexador_pendencia: P17-02', que afirmava 'não há fonte' e passou "
    "a ser falso."
)

TRD_POR_QUE = (
    "Taxa Referencial Diária. A fonte externa do bloco 19 nomeia TBF, "
    "Redutor-R e TR — e NÃO nomeia a TRD. Estender a razão da TR à TRD por "
    "semelhança de nome é a dedução proibida, e aqui não há o parêntese do "
    "manual que sustenta a costura da 'remuneração básica da caderneta de "
    "poupança (TR)'. Continua SEM FONTE. As únicas ocorrências de 'TRD' com "
    "vocabulário de tipo no corpus são o texto 'nao-indexador' dos segmentos "
    "de JUROS DE MORA, que não a classifica como indexador de correção."
)

# indexador -> (tipo novo, chaves a gravar, chaves a remover)
REGRAS: dict[str, tuple[str, dict[str, object], tuple[str, ...]]] = {
    "Selic": ("percentual", {"tipo_indexador_fonte": SELIC_FONTE}, ()),
    "taxa-legal": (
        "indeterminado",
        {
            "tipo_indexador_fonte": None,
            "tipo_indexador_por_que": LEGAL_POR_QUE,
            "tipo_indexador_pendencia": "P19-01",
        },
        ("tipo_indexador_razao", "tipo_indexador_fechamento"),
    ),
    "IPCA-E/IBGE": (
        "janela-deslocada",
        {"tipo_indexador_fonte": IPCA_E_FONTE},
        ("tipo_indexador_pendencia", "tipo_indexador_por_que",
         "tipo_indexador_razao", "tipo_indexador_fechamento"),
    ),
    "IPCA-15/IBGE": (
        "janela-deslocada",
        {"tipo_indexador_fonte": IPCA_15_FONTE},
        ("tipo_indexador_pendencia", "tipo_indexador_por_que",
         "tipo_indexador_razao", "tipo_indexador_fechamento"),
    ),
    "TR": (
        "indeterminado",
        {
            "tipo_indexador_fonte": TR_FONTE,
            "tipo_indexador_razao": TR_RAZAO,
            "tipo_indexador_fechamento": TR_FECHAMENTO,
        },
        ("tipo_indexador_pendencia", "tipo_indexador_por_que"),
    ),
    "remuneração básica da caderneta de poupança (TR)": (
        "indeterminado",
        {
            "tipo_indexador_fonte": TR_FONTE,
            "tipo_indexador_razao": TR_RAZAO,
            "tipo_indexador_fechamento": TR_FECHAMENTO,
            "tipo_indexador_identificacao_declarada": (
                "O rótulo é do PRÓPRIO manual e já traz '(TR)' entre "
                "parênteses: a identificação é ROTULAGEM DA FONTE, não "
                "semelhança de nome. Sem esse parêntese, a razão da TR não "
                "seria estendida a este rótulo."
            ),
        },
        ("tipo_indexador_pendencia", "tipo_indexador_por_que"),
    ),
    "TRD": (
        "indeterminado",
        {"tipo_indexador_por_que": TRD_POR_QUE, "tipo_indexador_pendencia": "P18-01"},
        ("tipo_indexador_razao", "tipo_indexador_fechamento"),
    ),
}


def reescreve(seg: dict) -> tuple[dict, bool]:
    """Devolve o segmento reescrito e se mudou. Ordem das chaves preservada."""
    regra = REGRAS.get(seg.get("indexador", ""))
    if regra is None:
        return seg, False
    tipo, grava, remove = regra
    novo: dict = {}
    for chave, valor in seg.items():
        if chave in remove:
            continue
        if chave == "tipo_indexador":
            novo[chave] = tipo
            continue
        novo[chave] = grava[chave] if chave in grava else valor
    # Chaves novas entram logo depois de `tipo_indexador_fonte`, se houver.
    faltando = [k for k in grava if k not in novo]
    if faltando:
        ordenado: dict = {}
        for chave, valor in novo.items():
            ordenado[chave] = valor
            if chave == "tipo_indexador_fonte":
                for k in faltando:
                    ordenado[k] = grava[k]
        for k in faltando:
            ordenado.setdefault(k, grava[k])
        novo = ordenado
    return novo, novo != seg


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    so_conferir = "--conferir" in argv
    mudancas = 0
    for caminho in sorted(TABELAS.glob("*.json")):
        dados = json.loads(caminho.read_text(encoding="utf-8"))
        if dados.get("tipo") != "cadeia-temporal":
            continue
        novos, mudou_arquivo = [], False
        for seg in dados["segmentos"]:
            novo, mudou = reescreve(seg)
            novos.append(novo)
            if mudou:
                mudancas += 1
                mudou_arquivo = True
                print(f"{caminho.name}: {seg.get('indexador')} "
                      f"{seg.get('tipo_indexador')} -> {novo['tipo_indexador']}")
        if mudou_arquivo and not so_conferir:
            dados["segmentos"] = novos
            caminho.write_text(
                json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    print(f"{mudancas} segmento(s) reescrito(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
