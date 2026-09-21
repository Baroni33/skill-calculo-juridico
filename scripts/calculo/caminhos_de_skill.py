#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Onde as regras e os scripts de skill passaram a morar — BLOCO 25.

**Um lugar só para o caminho novo.** Até o bloco 24 as regras viviam em
`docs/calculo/tabelas-normativas/` e todos os validadores em `scripts/calculo/`;
o bloco 25 levou **a regra para dentro da skill que a consome** e promoveu
quatro validadores a **script de skill**, ao lado da regra que validam.

As **ferramentas de pipeline** continuam em `scripts/calculo/` — e várias delas
precisam ler a regra migrada ou importar o script promovido. Cravar o caminho
novo em cada uma repetiria a decisão nove vezes e a faria envelhecer nove vezes.
Este módulo é o ponteiro único. Importá-lo **também** põe os `scripts/` das
skills no `sys.path`, que é o que permite a `test_valida_regimes.py` e às
irmãs continuarem fazendo `from valida_regimes import ...` sem saber onde o
arquivo foi parar.

Não há lógica de cálculo aqui, e não pode haver: é tabela de caminhos.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SKILLS = RAIZ / "skills"

#: As quatro skills que o plugin empacota.
CORE = SKILLS / "calculo-judicial-core"
ATUALIZACAO = SKILLS / "calculo-judicial-atualizacao"
LIQUIDACAO = SKILLS / "calculo-trabalhista-liquidacao"
INDICES = SKILLS / "indices-judiciais"

#: `regras/` — dado normativo lido por máquina. Irmão de `references/`, que é
#: prosa lida pelo modelo, e de `scripts/`, que é código.
REGRAS_CORE = CORE / "regras"
REGRAS_ATUALIZACAO = ATUALIZACAO / "regras"
REGRAS_LIQUIDACAO = LIQUIDACAO / "regras"

#: Onde vivem as 20 cadeias, o manifesto e o catálogo de tipos de indexador.
CADEIAS = REGRAS_ATUALIZACAO
MANIFESTO_CADEIAS = REGRAS_ATUALIZACAO / "cadeias-manifesto.json"
CATALOGO_INDEXADORES = REGRAS_ATUALIZACAO / "indexadores-tipo-catalogo.json"
CATALOGO_REGIMES = REGRAS_CORE / "regimes-temporais-catalogo.json"
CATALOGO_NORMA_COLETIVA = REGRAS_LIQUIDACAO / "camada-norma-coletiva-catalogo.json"

#: `scripts/` de skill — os quatro validadores promovidos no bloco 25.
SCRIPTS_DE_SKILL = (
    CORE / "scripts",
    ATUALIZACAO / "scripts",
    LIQUIDACAO / "scripts",
)


def registra_no_path() -> None:
    """Põe os `scripts/` das skills no `sys.path`, sem duplicar."""
    for d in SCRIPTS_DE_SKILL:
        s = str(d)
        if s not in sys.path:
            sys.path.insert(0, s)


registra_no_path()
