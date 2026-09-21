#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador não sobrescreve o que a curadoria escreveu depois dele — BLOCO 25.

O DEFEITO, E POR QUE ELE É DE CLASSE
-------------------------------------
`gera_cadeias_bloco18.py`, `gera_cadeias_bloco19.py`, `migra_bloco19_tipos.py` e
`extrai_bloco_01.py` são **geradores one-shot**: rodaram uma vez, no bloco que
lhes dá nome, e o que produziram **foi curado depois, à mão, por outros blocos**.
O bloco 23 tokenizou `aplicacao` em cinco segmentos, guardando a prosa do manual
em `aplicacao_literal` e nomeando a fórmula em `aplicacao_formula`; um bloco
anterior acrescentou aos `serie-*.csv` as linhas de proveniência de **R3**.

**Nenhum dos geradores sabe disso, e todos escreviam por cima sem perguntar.**
Rodar `gera_cadeias_bloco19.py` desfazia a tokenização e derrubava a suíte;
rodar `extrai_bloco_01.py` apagava 20 linhas de proveniência em 6 CSV. Nada
avisava: os dois retornavam 0 e imprimiam "escrito".

**O bloco 25 AGRAVOU a consequência sem ter criado a causa.** Antes, o gerador
estragava `docs/`. Depois da migração ele estraga `skills/*/regras/` — o
**artefato empacotado**, o que o usuário instala.

O DESENHO, E POR QUE NÃO FOI "EXIGIR `--forcar` SEMPRE"
--------------------------------------------------------
Três saídas foram pesadas:

  (a) **`--forcar` obrigatório para escrever.** Rejeitado: pune o caso inocente.
      `gera_cadeias_bloco18.py` reproduz HOJE, byte a byte, dois dos quatro
      arquivos que gera — rodá-lo é seguro e deveria continuar sendo trivial;

  (b) **tornar o gerador idempotente reaplicando a curadoria.** Rejeitado: põe
      no gerador o conhecimento de todas as curadorias futuras. É a mesma
      dívida, adiada;

  (c) **ESCOLHIDA — comparar antes de escrever.** Idêntico: não escreve, e diz
      `nada-a-fazer`. Inexistente: escreve. **Divergente: RECUSA, nomeia o
      arquivo, e sai com código 2.** `--forcar` continua existindo, para o dia
      em que a intenção for mesmo regerar.

**A recusa é ATÔMICA, e isso é o ponto que (c) só cumpre com `grava_lote`.** O
lote inteiro é conferido antes de qualquer `write_text`. Recusa arquivo a
arquivo deixaria o diretório meio regerado — exatamente o que aconteceu na
medição deste bloco, em que `extrai_bloco_01.py` danificou seis CSV antes de
alguém olhar.

`encoding='utf-8'` explícito em toda leitura e escrita, como o resto do módulo.
"""

from __future__ import annotations

from pathlib import Path

#: Código de saída da recusa. **Não é 1**: 1 é "o validador achou violação", e
#: confundir os dois faz um script de CI tratar recusa como divergência de
#: norma.
EXIT_RECUSA = 2


class ArtefatoCurado(Exception):
    """O destino existe, diverge do que o gerador produz, e `--forcar` não veio."""

    def __init__(self, divergentes: list[Path]) -> None:
        self.divergentes = divergentes
        super().__init__(
            f"{len(divergentes)} artefato(s) divergente(s): "
            + ", ".join(p.name for p in divergentes)
        )


def _le(destino: Path) -> str | None:
    if not destino.exists():
        return None
    return destino.read_text(encoding="utf-8")


def grava_lote(pares: list[tuple[Path, str]], forcar: bool = False) -> dict[Path, str]:
    """Confere o lote INTEIRO e só então escreve. Devolve destino → estado.

    Estados: ``"criado"``, ``"nada-a-fazer"``, ``"sobrescrito"`` (só com
    `forcar`). Levanta `ArtefatoCurado` se algum destino divergir sem `forcar`
    — e, nesse caso, **nada é escrito**.
    """
    atual = {destino: _le(destino) for destino, _ in pares}
    if not forcar:
        divergentes = [
            destino for destino, conteudo in pares
            if atual[destino] is not None and atual[destino] != conteudo
        ]
        if divergentes:
            raise ArtefatoCurado(divergentes)

    estados: dict[Path, str] = {}
    for destino, conteudo in pares:
        anterior = atual[destino]
        if anterior is None:
            estados[destino] = "criado"
        elif anterior == conteudo:
            estados[destino] = "nada-a-fazer"
            continue
        else:
            estados[destino] = "sobrescrito"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(conteudo, encoding="utf-8")
    return estados


def explica_recusa(erro: ArtefatoCurado, raiz: Path, script: str) -> str:
    """A mensagem que o gerador imprime ao recusar. Tem de dizer o que fazer."""
    linhas = [
        "",
        "RECUSADO — artefato já curado divergiria do que este gerador produz.",
        "",
        f"  gerador: {script}",
        "  arquivos que seriam sobrescritos, e o que se perderia neles:",
    ]
    for p in erro.divergentes:
        try:
            rel = p.relative_to(raiz).as_posix()
        except ValueError:
            rel = str(p)
        linhas.append(f"    - {rel}")
    linhas += [
        "",
        "  Estes arquivos foram EDITADOS DEPOIS de terem sido gerados — é o caso",
        "  da tokenização de `aplicacao` (bloco 23) e das linhas de proveniência",
        "  de R3 nos `serie-*.csv`. Regerar por cima desfaz a curadoria e, desde",
        "  o bloco 25, estraga o ARTEFATO EMPACOTADO, não mais só `docs/`.",
        "",
        "  Se a intenção é mesmo regerar, rode com --forcar e confira o diff",
        "  antes de comitar. Nada foi escrito.",
        "",
    ]
    return "\n".join(linhas)


def quer_forcar(argv: list[str]) -> bool:
    """`--forcar` no `argv`. Não é `argparse` de propósito: estes geradores não

    têm outra opção, e um `argparse` por gerador seria quatro cópias da mesma
    decisão."""
    return "--forcar" in argv
