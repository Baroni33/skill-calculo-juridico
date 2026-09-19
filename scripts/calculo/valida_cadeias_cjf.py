#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Roda R1 e R2 sobre as cadeias do Manual CJF — bloco 8.

Por que este script existe, e não apenas `valida_cobertura.py` direto:

1. **Tronco e ramo.** As cadeias do CJF são incondicionais até nov./2021 e só
   então bifurcam por qualidade do devedor. O `valida_cobertura` trata cada
   `condicao` como universo separado — corretamente, porque tabelas que
   bifurcam por devedor, data da sentença ou fato gerador não devem ser
   comparadas entre si. Mas isso faz o tronco incondicional aparecer como
   lacuna em cada ramo. Aqui o tronco é **replicado** em cada ramo antes da
   checagem, que é o que a leitura do manual manda: o ramo herda o tronco.

2. **Componente próprio.** Uma cadeia de correção monetária não deve ser
   cobrada de cobrir juros de mora ao longo de toda a linha do tempo. A SELIC
   declara `engloba: [correcao-monetaria, juros-mora]`, o que cria um universo
   de juros dentro de uma tabela de correção. A checagem de R2 roda **apenas
   sobre o componente próprio da cadeia**; R1 roda sobre todos, porque é
   exatamente ali que o englobamento precisa ser vigiado.

As violações que sobram são do manual, não da modelagem. Nenhuma foi
harmonizada.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

# O console do Windows usa cp1252 e engasga com as setas e travessões que o
# relatório imprime. R12 do projeto manda encoding explícito; aqui é a saída.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

from valida_cobertura import (  # noqa: E402
    Segmento,
    competencia_para_indice,
    valida_cobertura,
)

RAIZ = Path(__file__).resolve().parents[2]
TABELAS = RAIZ / "docs/calculo/tabelas-normativas"


def expande_tronco(brutos: list[dict]) -> list[dict]:
    """Replica os segmentos incondicionais em cada ramo condicionado.

    O tronco continua existindo no universo sem condição — um cálculo que não
    precise distinguir o devedor o usa direto.
    """
    condicoes = {
        json.dumps(s.get("condicao") or {}, sort_keys=True, ensure_ascii=False)
        for s in brutos
    }
    condicoes.discard("{}")
    if not condicoes:
        return list(brutos)

    saida = list(brutos)
    for c in sorted(condicoes):
        cond = json.loads(c)
        for s in brutos:
            if s.get("condicao"):
                continue
            copia = dict(s)
            copia["condicao"] = cond
            copia["id"] = f"{s.get('indexador') or s.get('taxa') or 'seg'} [tronco>ramo]"
            copia["_replicado"] = True
            saida.append(copia)
    return saida


def carrega(caminho: Path) -> tuple[dict, list[Segmento]]:
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    brutos = expande_tronco(dados["segmentos"])
    return dados, [Segmento.de_dict(s, i) for i, s in enumerate(brutos)]


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    alvos = sorted(TABELAS.glob("cjf.*.json"))
    if not alvos:
        print("nenhuma cadeia cjf.*.json encontrada")
        return 1

    total_r1 = total_r2 = 0
    for caminho in alvos:
        dados, segmentos = carrega(caminho)
        janela = dados.get("janela_de_analise", {})
        proprio = dados["componente"]

        relatorio = valida_cobertura(
            segmentos, janela.get("inicio"), janela.get("fim")
        )
        r1 = [v for v in relatorio.violacoes if v.regra == "R1"]
        # R2 no universo SEM CONDIÇÃO num período em que os ramos
        # condicionados cobrem tudo não é lacuna: é a bifurcação. O manual é
        # incondicional até nov./2021 e só então separa por devedor.
        cobertos = [
            (competencia_para_indice(s.inicio), competencia_para_indice(s.fim))
            for s in segmentos
            if s.condicao and s.fornece(proprio)
        ]

        def e_bifurcacao(v) -> bool:
            if v.condicao != "(sem condição)":
                return False
            i, f = competencia_para_indice(v.inicio), competencia_para_indice(v.fim)
            return all(
                any(a <= m <= b for a, b in cobertos) for m in range(i, f + 1)
            )

        r2, bifurcacoes = [], []
        for v in relatorio.violacoes:
            if v.regra != "R2" or v.componente != proprio:
                continue
            (bifurcacoes if e_bifurcacao(v) else r2).append(v)
        total_r1 += len(r1)
        total_r2 += len(r2)

        marca = "OK" if not (r1 or r2) else f"R1={len(r1)} R2={len(r2)}"
        print(f"\n{caminho.stem}  [{len(segmentos)} segmentos, {marca}]")
        print(f"  item {dados['fonte']['item']}, pagina_pdf {dados['fonte']['pagina_pdf']}")
        for v in r1 + r2:
            print(f"  {v}")
        for v in bifurcacoes:
            janela_v = v.inicio if v.inicio == v.fim else f"{v.inicio}..{v.fim}"
            print(f"  [bifurcação] {v.componente} | {janela_v}: "
                  f"o tronco encerra e os ramos condicionados cobrem — não é lacuna")

    print(f"\n{'=' * 70}")
    print(f"{len(alvos)} cadeias | R1: {total_r1} violações | R2: {total_r2} violações")
    print(
        "Toda violação acima é do MANUAL, transcrita como está.\n"
        "Ver bloco-08-relatorio.md § 5 para a leitura de cada uma."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
