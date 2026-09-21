#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Roda R1 e R2 sobre as cadeias extraídas dos manuais — blocos 8 e 9.

Este script é um **CLI sobre `valida_cobertura.py`**, não uma implementação
paralela. A lógica de tronco-e-ramo, que na primeira versão vivia aqui, foi
movida para o validador (bloco 9, tarefa 0): segmento sem `condicao` vale para
todos os ramos, e a cobertura de cada ramo é avaliada como tronco ∪ ramo.

O que sobra aqui é o que é de apresentação:

1. **Componente próprio.** R2 é cobrada apenas do componente que a cadeia
   declara. Uma tabela de correção monetária não deve ser cobrada de cobrir
   juros de mora ao longo de toda a linha do tempo — a SELIC declara
   `engloba: [correcao-monetaria, juros-mora]`, o que criaria um universo de
   juros dentro de uma tabela de correção. R1 roda sobre todos os componentes,
   porque é ali que o englobamento precisa ser vigiado.

2. **A janela** vem do campo `janela_de_analise` de cada cadeia.

As violações que sobram são do manual, não da modelagem. Nenhuma foi
harmonizada.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

# O console do Windows usa cp1252 e engasga com travessões. R12 manda encoding
# explícito; aqui é a saída.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

# BLOCO 25 — `valida_cobertura.py` virou script DE SKILL e mora em
# `skills/calculo-judicial-atualizacao/scripts/`. Importar `caminhos_de_skill`
# registra esse diretório no `sys.path`; o `import` abaixo não mudou.
import caminhos_de_skill  # noqa: E402,F401

from valida_cobertura import Segmento, valida_cobertura  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
# As 20 cadeias migraram para dentro da skill que as consome (bloco 25).
TABELAS = caminhos_de_skill.CADEIAS

# --------------------------------------------------------------------------
# Manifesto de cadeias
# --------------------------------------------------------------------------
# ONDE: sidecar em `skills/calculo-judicial-atualizacao/regras/`, ao lado do
# que descreve — para lá foram as cadeias no bloco 25, e o manifesto foi junto.
# É o mesmo lugar e o mesmo argumento de `indexadores-tipo-catalogo.json`
# (bloco 17): um inventário do diretório mora com o diretório, e os dois
# consumidores — este CLI e `test_valida_cobertura.py`, que vivem em
# scripts/ — leem UMA fonte em vez de cada um manter a sua.
#
# POR QUE NÃO ENVELHECE: a contagem cravada em constante envelheceu porque só
# uma edição manual a fazia crescer. Este manifesto cresce SOZINHO — quem
# encontra cadeia que ele não conhece a GRAVA e avisa. O que ele nunca faz é
# remover: cadeia que some exige edição deliberada, com o porquê no commit.
# Assimetria proposital, e é toda a tese da tarefa: cadeia a mais é crescimento
# normal; cadeia a menos é regressão. Foi assim que a renomeação do bloco 17
# derrubou o validador de 11 para 7 em silêncio, seguindo a imprimir "OK".
#
# A CHAVE É O `id`, NÃO O NOME DO ARQUIVO. Renomear `trt3.hist.*.json` para
# `trab.hist.*.json` não pode acusar ausência — o arquivo mudou de nome, a
# cadeia não deixou de existir. Só a perda do `id` é regressão.
MANIFESTO = TABELAS / "cadeias-manifesto.json"


def descobre_cadeias(diretorio: Path | None = None) -> dict[str, dict]:
    """Todas as cadeias do diretório, por `id`, com o que o manifesto vigia."""
    diretorio = TABELAS if diretorio is None else diretorio
    achadas: dict[str, dict] = {}
    for caminho in sorted(diretorio.glob("*.json")):
        if not e_cadeia(caminho):
            continue
        dados = json.loads(caminho.read_text(encoding="utf-8"))
        ident = dados.get("id") or caminho.stem
        achadas[ident] = {
            "arquivo": caminho.name,
            "componente": dados.get("componente"),
            "segmentos": len(dados["segmentos"]),
        }
    return achadas


def le_manifesto(caminho: Path | None = None) -> dict:
    caminho = MANIFESTO if caminho is None else caminho
    if not caminho.exists():
        return {"cadeias": {}}
    return json.loads(caminho.read_text(encoding="utf-8"))


def confere_manifesto(achadas: dict[str, dict],
                      manifesto: dict | None = None) -> tuple[list[str], list[str]]:
    """(regressões, crescimento). Regressão é o que FALTA; nunca o que sobra.

    Duas espécies de regressão, ambas silenciosas antes deste manifesto:
      * `id` declarado que não aparece mais em arquivo algum;
      * cadeia que aparece com MENOS segmentos do que já teve — encolhimento
        de linha do tempo não é crescimento, é perda de cobertura.
    """
    manifesto = le_manifesto() if manifesto is None else manifesto
    declaradas = manifesto.get("cadeias", {})
    regressoes: list[str] = []
    crescimento: list[str] = []
    for ident, esperado in sorted(declaradas.items()):
        atual = achadas.get(ident)
        if atual is None:
            regressoes.append(
                f"cadeia SUMIU: '{ident}' (era {esperado.get('arquivo')}) — "
                f"o manifesto a declara e nenhum arquivo a contém"
            )
        elif atual["segmentos"] < esperado.get("segmentos", 0):
            regressoes.append(
                f"cadeia ENCOLHEU: '{ident}' tem {atual['segmentos']} segmentos, "
                f"o manifesto declara {esperado['segmentos']}"
            )
    for ident in sorted(set(achadas) - set(declaradas)):
        crescimento.append(ident)
    return regressoes, crescimento


def grava_manifesto(achadas: dict[str, dict], caminho: Path | None = None) -> None:
    """Cresce o manifesto. NUNCA remove `id` nem reduz contagem de segmentos."""
    caminho = MANIFESTO if caminho is None else caminho
    anterior = le_manifesto(caminho)
    manifesto = {
        "id": "cadeias-manifesto",
        "titulo": "Manifesto das cadeias temporais — PISO de inventário, não retrato",
        "tipo": "manifesto",
        "REGRA_DESTE_MANIFESTO": REGRA,
        "MANTIDO_POR": "scripts/calculo/valida_cadeias.py (cresce sozinho; nunca encolhe sozinho)",
        "CONSUMIDO_POR": [
            "scripts/calculo/valida_cadeias.py — aborta com exit 1 em regressão",
            "scripts/calculo/test_valida_cobertura.py — guardas de tipo_indexador",
        ],
    }
    declaradas = dict(anterior.get("cadeias", {}))
    for ident, atual in achadas.items():
        antes = declaradas.get(ident)
        if antes is None:
            declaradas[ident] = dict(atual)
        else:
            antes["arquivo"] = atual["arquivo"]
            antes["componente"] = atual["componente"]
            antes["segmentos"] = max(antes.get("segmentos", 0), atual["segmentos"])
    manifesto["cadeias"] = dict(sorted(declaradas.items()))
    caminho.write_text(
        json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


REGRA = (
    "PISO, NÃO RETRATO. O validador falha se encontrar MENOS cadeias do que "
    "este arquivo declara, ou cadeia com MENOS segmentos do que ele registra. "
    "Cadeia a mais é crescimento normal e é GRAVADA AQUI AUTOMATICAMENTE por "
    "valida_cadeias.py — manifesto que precisa de edição manual a cada cadeia "
    "nova envelhece igual à constante que ele veio substituir. Remover um id "
    "ou baixar uma contagem é EDIÇÃO MANUAL DELIBERADA, e o porquê vai no "
    "commit. A chave é o campo 'id' da cadeia, nunca o nome do arquivo: a "
    "renomeação trt3.hist.* -> trab.hist.* do bloco 17 derrubou a descoberta "
    "de 11 para 7 em silêncio, e o id é o que sobrevive a renomeação."
)


def e_cadeia(caminho: Path) -> bool:
    """Cadeia se reconhece pelo CONTEUDO, nunca pelo nome do arquivo.

    A descoberta era por prefixo (`cjf.`, `trt3.hist.`) — o mesmo defeito que o
    bloco 17 veio corrigir nos identificadores. Renomear os quatro arquivos
    `trt3.hist.*` para `trab.hist.*` fez o validador cair de 11 cadeias para 7
    **em silêncio**, seguindo a imprimir "OK" sobre as sete restantes.

    Ler `tipo` e `segmentos` torna a renomeacao inocua, que e o ponto: o
    identificador nao carrega semantica que o campo ja expressa.
    """
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return False
    return dados.get("tipo") == "cadeia-temporal" and isinstance(
        dados.get("segmentos"), list
    )


def carrega(caminho: Path) -> tuple[dict, list[Segmento]]:
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    return dados, [Segmento.de_dict(s, i) for i, s in enumerate(dados["segmentos"])]


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    congelar = "--sem-atualizar-manifesto" in argv
    alvos = sorted(p for p in TABELAS.glob("*.json") if e_cadeia(p))
    if not alvos:
        print("nenhuma cadeia encontrada")
        return 1

    achadas = descobre_cadeias()
    regressoes, crescimento = confere_manifesto(achadas)
    if regressoes:
        print("REGRESSÃO CONTRA O MANIFESTO — " + str(MANIFESTO))
        for r in regressoes:
            print(f"  {r}")
        print(
            "\nCadeia a mais é crescimento normal; cadeia a menos é regressão.\n"
            "Se a remoção foi deliberada, edite o manifesto à mão e diga por quê."
        )
        return 1
    if crescimento and not congelar:
        grava_manifesto(achadas)
        print(
            f"manifesto atualizado: +{len(crescimento)} cadeia(s) — "
            + ", ".join(crescimento)
        )
    elif crescimento:
        print(f"fora do manifesto (não gravado): {', '.join(crescimento)}")

    total_r1 = total_r2 = total_r3 = 0
    for caminho in alvos:
        dados, segmentos = carrega(caminho)
        janela = dados.get("janela_de_analise", {})
        proprio = dados["componente"]

        relatorio = valida_cobertura(
            segmentos,
            janela.get("inicio"),
            janela.get("fim"),
            dominio_condicoes=dados.get("dominio_condicoes"),
        )
        r1 = [v for v in relatorio.violacoes if v.regra == "R1"]
        r2 = [
            v for v in relatorio.violacoes
            if v.regra == "R2" and v.componente == proprio
        ]
        # R3, como R2, é cobrada do componente PRÓPRIO da cadeia: a virada que
        # interessa é a da linha do tempo que a tabela declara.
        r3 = [
            v for v in relatorio.violacoes
            if v.regra.startswith("R3") and v.componente == proprio
        ]
        total_r1 += len(r1)
        total_r2 += len(r2)
        total_r3 += len(r3)

        marca = (
            "OK" if not (r1 or r2 or r3)
            else f"R1={len(r1)} R2={len(r2)} R3={len(r3)}"
        )
        print(f"\n{caminho.stem}  [{len(segmentos)} segmentos, {marca}]")
        print(f"  item {dados['fonte']['item']}, pagina_pdf {dados['fonte']['pagina_pdf']}")
        for v in r1 + r2 + r3:
            print(f"  {v}")

    print(f"\n{'=' * 70}")
    print(
        f"{len(alvos)} cadeias | R1: {total_r1} violações | "
        f"R2: {total_r2} violações | R3: {total_r3} violações"
    )
    print(
        "Toda violação acima é do MANUAL, transcrita como está.\n"
        "Leitura de cada uma nos relatórios dos blocos 8 e 9."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
