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

from valida_cobertura import Segmento, valida_cobertura  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
TABELAS = RAIZ / "docs/calculo/tabelas-normativas"
PREFIXOS = ("cjf.", "trt3.hist.")


def carrega(caminho: Path) -> tuple[dict, list[Segmento]]:
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    return dados, [Segmento.de_dict(s, i) for i, s in enumerate(dados["segmentos"])]


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    alvos = sorted(
        p for p in TABELAS.glob("*.json") if p.name.startswith(PREFIXOS)
    )
    if not alvos:
        print("nenhuma cadeia encontrada")
        return 1

    total_r1 = total_r2 = 0
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
        total_r1 += len(r1)
        total_r2 += len(r2)

        marca = "OK" if not (r1 or r2) else f"R1={len(r1)} R2={len(r2)}"
        print(f"\n{caminho.stem}  [{len(segmentos)} segmentos, {marca}]")
        print(f"  item {dados['fonte']['item']}, pagina_pdf {dados['fonte']['pagina_pdf']}")
        for v in r1 + r2:
            print(f"  {v}")

    print(f"\n{'=' * 70}")
    print(f"{len(alvos)} cadeias | R1: {total_r1} violações | R2: {total_r2} violações")
    print(
        "Toda violação acima é do MANUAL, transcrita como está.\n"
        "Leitura de cada uma nos relatórios dos blocos 8 e 9."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
