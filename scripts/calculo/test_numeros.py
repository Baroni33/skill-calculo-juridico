"""Número de resultado digitado fora de `00-numeros.md` — e o gerador que o substitui.

O bloco 19 publicou *"R1 e R2 não se moveram"* em quatro arquivos depois de R1
ter ido a 21. O bloco 18 deixou *"14 ok, 10 erros"* num runbook depois de os
erros sumirem. O bloco 17 deixou *"97 de 97 segmentos"* depois de virarem 126.
**Número de resultado digitado é cópia sem dono, e cópia sem dono envelhece em
silêncio.** `gera_numeros.py` dá um dono ao número; este arquivo impede que a
cópia volte.

ESCOPO DECLARADO DA VARREDURA — CONTADO ANTES DE DECLARADO
-----------------------------------------------------------
  árvores: `README.md` da raiz, `docs/`, `skills/`, `scripts/`
  extensões lidas: `.md` e `.json` (`.json` entrou no bloco 20 — ver a nota de
      `EXTENSOES_LIDAS`, com a medição que sustenta a decisão)
  fora, e cada um com razão escrita:
    * `docs/calculo/consolidado/00-numeros.md` — é o dono. É ali que o número
      DEVE estar;
    * `docs/calculo/extracao/**` — **relatório de bloco é registro datado**.
      Os `bloco-NN-relatorio.md` DEVEM manter os números que tinham quando
      foram escritos; um relatório que se atualiza sozinho deixa de ser
      registro. Exemção de ÁRVORE, e não entrada de ledger, porque a razão
      vale para a árvore inteira por natureza — pôr 90 entradas de ledger para
      dizer 90 vezes a mesma coisa é como se destrói um ledger;
    * `.py` — **os três casos-limite do enunciado, decididos:**
      **(i) número em teste.** A asserção É a fonte: `assertEqual(x, 21)` falha
      no minuto em que 21 deixa de valer. Não é cópia — é o mecanismo que
      impede a cópia. Fica.
      **(ii) número em docstring de script.** Documenta o CÓDIGO e o que ele
      decidiu, junto do código que decidiu: `valida_cadeias.py` narra a queda
      "de 11 cadeias para 7" para explicar por que a descoberta deixou de ser
      por prefixo. É narrativa histórica colada ao seu objeto, da mesma
      espécie do relatório de bloco. Fica — mas **só enquanto for narrativa**:
      docstring que publique o placar corrente é o mesmo defeito do runbook do
      bloco 18, e a revisão de código é o lugar de pegá-lo, não o regex.
      **(iii) número em `pendencias.md`.** Decidido caso a caso, no ledger
      abaixo: quando a contagem **É a pendência** (*"32 segmentos seguem
      `indeterminado`"* — o tamanho do problema é o problema), fica; quando é
      **placar de validador** (*"fecha em R1: 21 | R2: 1"*), virou ponteiro.

O QUE O DETECTOR PROCURA, E O QUE ELE DELIBERADAMENTE NÃO PROCURA
------------------------------------------------------------------
Procura **vocabulário de resultado AGREGADO** — a grandeza que só o estado do
repositório inteiro responde:

    N testes · N cadeias · R1:N / R2:N / R3:N · N rótulos
    N ok, N divergências (o placar de valida_bloco_tabelas)
    N de N segmentos · N segmentos em N cadeias

**NÃO procura `N segmentos` solto, nem `N violações` solto.** Não é descuido, é
a decisão mais importante deste arquivo. Medido antes de decidir: com os dois
dentro, a varredura devolve **64** pares em 15 arquivos; sem eles, **21** em 6.
As 43 diferenças são quase todas legítimas:

  * `N segmentos` é, na prática, **contagem POR CADEIA** — *"`cjf.fgts.
    correcao-monetaria.json` (11 segmentos)"*, em `references/`. Esse número
    tem dono adjacente: o arquivo que ele conta está citado na mesma linha, e
    ele só muda quando aquele arquivo muda. **E é auditável**, porque
    `00-numeros.md` § 1.1 publica a contagem cadeia a cadeia — foi para isso
    que a § 1.1 existe;
  * `N violações` é, na prática, **delta narrado** — *"as 21 violações novas de
    R3, uma a uma"*, seguido da tabela com as 21. Número cuja lista está
    imediatamente abaixo não envelhece em silêncio: envelhece junto com a
    lista, à vista.

Pô-los no detector jogaria ~43 menções legítimas num ledger, e ledger que
ninguém consegue manter vira ruído, o teste passa a ser ignorado, e **validador
ignorado é pior que validador ausente** — o argumento da tarefa 4 do bloco 17.
O custo aceito, declarado: uma contagem AGREGADA de segmentos escrita como
*"156 segmentos"* nu passa. Foi por isso que `N de N segmentos` e
`N segmentos em N cadeias` entraram: são as formas em que o agregado costuma
aparecer, e uma delas é literalmente a frase que o bloco 17 deixou envelhecer.

**Número de CONTEÚDO NORMATIVO não é alcançado pelo detector, por construção.**
*42,72% em jan./1989*, *6,17*, *0,5% a.m.*, *art. 457*, `pagina_pdf 42` não têm
nenhum dos substantivos de resultado ao lado. O detector não olha "número"; ele
olha **número seguido do substantivo de uma grandeza que o repositório conta**.
É o que torna o falso positivo raro sem heurística de contexto.

POR QUE O LEDGER DO BLOCO 18 SERVE AQUI — E ONDE ELE PRECISOU MUDAR
--------------------------------------------------------------------
`test_ponteiros.py` resolveu problema da mesma família com **ledger chaveado
pelo par `(alvo, arquivo)`, autolimpante, que falha em exceção órfã**. O padrão
**serve**, e pelo mesmo motivo: a alternativa — heurística de contexto,
procurar *"era"*, *"virou"*, *"à época"* perto do número — erra dos dois lados e
treina o leitor a ignorar o resultado.

Uma mudança, e é de chave. Lá a chave era o **alvo** (um nome de arquivo).
Aqui a chave é o par **(arquivo, achado)**, onde `achado` é o FRAGMENTO casado
— `"11 cadeias"` —, nunca a linha inteira. Linha inteira parece mais preciso e
é pior: qualquer reflow de parágrafo orfanaria a entrada e o teste falharia sem
que número algum tivesse mudado. **Autolimpante tem de morder o fato, não a
formatação.** Com o fragmento como chave, reescrever a prosa em volta não
quebra nada, e trocar `11` por `12` quebra — que é exatamente o momento em que
se quer a fricção.
"""

from __future__ import annotations

import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import gera_numeros  # noqa: E402

ARVORES = ("docs", "skills", "scripts")

#: **BLOCO 20 — `.json` ENTROU, e a decisão foi MEDIDA antes de tomada.**
#: O detector lia só `.md`, e o escopo nem mencionava `.json`. O custo disso
#: apareceu em `indexadores-tipo-catalogo.json`, que afirmava **em presente**
#: *"ausentes das 15 cadeias"*, *"os 34 rótulos … nas 15 cadeias"* e
#: *"varrendo … dos 126 segmentos"* quando já eram **20 cadeias, 156 segmentos e
#: 35 rótulos nomeados** — exatamente o defeito que este arquivo existe para
#: matar, fora do alcance dele.
#:
#: **O risco alegado era falso positivo**, porque JSON é cheio de número de
#: conteúdo. **Medido:** rodando o detector sobre os **39** `.json` de `docs/`,
#: `skills/`, `scripts/` e `tests/`, os achados são **8, todos em UM arquivo** —
#: o catálogo. Nos outros 38, **zero**. O detector não olha "número": olha
#: número **seguido do substantivo de uma grandeza que o repositório conta**, e
#: `pagina_pdf`, percentual e ano não têm esse substantivo ao lado. **Estender
#: custa um ledger de poucas linhas; não estender deixava um buraco do tamanho
#: do diretório de tabelas.**
EXTENSOES_LIDAS = (".md", ".json")

FORA_DA_VARREDURA = (
    "docs/calculo/extracao/",
    "docs/calculo/consolidado/00-numeros.md",
)

PADROES = (
    r"\d+\s+testes\b",
    r"\d+\s+cadeias\b",
    r"R[123]\s*[:=]\s*\d+",
    r"\d+\s+ok,\s*\d+\s+divergências",
    r"\d+\s+rótulos\b",
    r"\d+\s+de\s+\d+\s+segmentos\b",
    r"\d+\s+segmentos\s+em\s+\d+\s+cadeias",
)
RE_RESULTADO = re.compile("|".join(f"(?:{p})" for p in PADROES))

CLASSES = {
    "registro datado de bloco",
    "narrativa histórica",
    "a contagem É a pendência",
    "enunciado da própria regra",
    # BLOCO 20. Número que **um teste recomputa do repositório** e confere. Não
    # é cópia sem dono: o dono é a asserção, e ela falha no minuto em que o
    # número deixa de valer — mesmo argumento do caso-limite (i) do escopo.
    "guardada por teste que a recomputa",
}


# --------------------------------------------------------------------------
# Ledger. Chave: o par (arquivo, achado). Nunca o achado sozinho, nunca a
# linha inteira. Cada entrada carrega o porquê, e a entrada órfã FALHA.
# --------------------------------------------------------------------------
EXCECOES: list[dict] = [
    # ---- docs/calculo/aceitacao/bloco-23-relatorio.md --------------------
    # Relatório de bloco é REGISTRO DATADO: fixa o estado do fechamento e
    # NÃO se atualiza. `docs/calculo/extracao/` está fora da varredura por
    # árvore exatamente por isso; `aceitacao/` não está, e os relatórios de
    # bloco que moram ali entram aqui, um a um.
    {
        "arquivo": "docs/calculo/aceitacao/bloco-23-relatorio.md",
        "achado": "20 testes",
        "classe": "registro datado de bloco",
        "por_que": (
            "Tamanho de `test_aceite_nivel1.py` no fechamento do bloco 23, "
            "citado para dizer que o NÍVEL 1 é executável e não prosa. "
            "Atualizar apagaria o que o bloco entregou."
        ),
    },
    {
        "arquivo": "docs/calculo/aceitacao/bloco-23-relatorio.md",
        "achado": "32 testes",
        "classe": "registro datado de bloco",
        "por_que": (
            "Tamanho de `test_metodos.py` no fechamento. É a resposta ao G3 "
            "da auditoria — 'nenhum teste confrontava metodos.py' —, e o "
            "número é a medida da correção."
        ),
    },
    {
        "arquivo": "docs/calculo/aceitacao/bloco-23-relatorio.md",
        "achado": "36 rótulos",
        "classe": "registro datado de bloco",
        "por_que": (
            "CITAÇÃO da divergência corrigida: a skill dizia 'Catálogo "
            "completo — 28 indexadores' e o catálogo tinha 36 rótulos. "
            "Apagá-la apagaria o defeito que o bloco 23 consertou."
        ),
    },
    # ---- README.md ------------------------------------------------------
    {
        "arquivo": "README.md",
        "achado": '97 de 97 segmentos',
        "classe": "enunciado da própria regra",
        "por_que": (
            "É a CITAÇÃO do defeito que esta regra existe para impedir — o "
            "bloco 17 publicou '97 de 97' e virou 126. Apagá-la apagaria o "
            "exemplo que ensina a regra."
        ),
    },
    {
        "arquivo": "README.md",
        "achado": "11 cadeias",
        "classe": "narrativa histórica",
        "por_que": (
            "'o validador caía de 11 cadeias para 7 em silêncio' — é a "
            "descrição do BUG do bloco 17, a justificativa de a descoberta ter "
            "deixado de ser por prefixo. Atualizá-la destruiria o argumento."
        ),
    },
    {
        "arquivo": "README.md",
        "achado": "15 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "'Ao fim do bloco 18: 15 cadeias, 267 testes' — estado daquele "
            "bloco, marcado como registro datado no próprio texto, com "
            "ponteiro para 00-numeros.md ao lado."
        ),
    },
    {
        "arquivo": "README.md",
        "achado": "267 testes",
        "classe": "registro datado de bloco",
        "por_que": "Idem: fecho do bloco 18, na mesma frase marcada como datada.",
    },
    {
        "arquivo": "README.md",
        "achado": "20 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "'Ao fim do bloco 19: 20 cadeias, 156 segmentos, 311 testes' — "
            "marcado como registro datado, com ponteiro ao lado."
        ),
    },
    {
        "arquivo": "README.md",
        "achado": "311 testes",
        "classe": "registro datado de bloco",
        "por_que": "Idem: fecho do bloco 19, na mesma frase marcada como datada.",
    },
    {
        "arquivo": "README.md",
        "achado": "36 rótulos",
        "classe": "registro datado de bloco",
        "por_que": (
            "Duas ocorrências, ambas do bloco 19: a frase de fecho datada e a "
            "linha 19 da tabela de blocos, que descreve o CONTEÚDO daquele "
            "bloco — 'Terceira classe de R3; 36 rótulos mapeados'."
        ),
    },
    {
        "arquivo": "README.md",
        "achado": "5 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "'5 cadeias novas' na linha 19 da tabela de blocos. É a ENTREGA "
            "daquele bloco, não o inventário de hoje."
        ),
    },
    # ---- docs/ ----------------------------------------------------------
    {
        "arquivo": "docs/calculo/01-plano-extracao.md",
        "achado": "11 cadeias",
        "classe": "narrativa histórica",
        "por_que": (
            "'a renomeação fez o validador cair de 11 cadeias para 7' — o "
            "mesmo bug do bloco 17, registrado no plano porque foi ele que "
            "criou a regra do identificador neutro."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/README.md",
        "achado": "11 cadeias",
        "classe": "narrativa histórica",
        "por_que": (
            "'derrubou a descoberta de 11 cadeias para 7 em silêncio, no bloco "
            "17' — justifica o manifesto existir. Idem acima."
        ),
    },
    {
        "arquivo": "docs/calculo/consolidado/02-atualizacao-detalhe.md",
        "achado": "11 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "'segmentos sem fundamento, em 11 cadeias, quase todos anteriores "
            "ao bloco 19' — medição feita naquele bloco, sobre o estado "
            "daquele bloco, e usada para dizer o que o bloco NÃO fez."
        ),
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "11 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "§ 23.4 (bloco 17): 'valida_cadeias.py sobre as 11 cadeias' — o "
            "escopo do que foi auditado NAQUELE bloco. A auditoria não se "
            "refaz sozinha, e o escopo dela também não."
        ),
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "15 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "§ 25.4: 'Eram 34 rótulos em 15 cadeias na tarefa 2; são 36 em 20 "
            "desde a tarefa 3'. Ponta ANTES de uma variação narrada — as duas "
            "pontas têm de ficar como estavam ou a variação deixa de ser "
            "auditável."
        ),
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "20 cadeias",
        "classe": "registro datado de bloco",
        "por_que": "§ 25.4, ponta DEPOIS da mesma variação do bloco 19.",
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "34 rótulos",
        "classe": "registro datado de bloco",
        "por_que": "§ 25.4, ponta ANTES da variação de rótulos do bloco 19.",
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "36 rótulos",
        "classe": "registro datado de bloco",
        "por_que": (
            "§ 25.4, ponta DEPOIS da mesma variação de rótulos do bloco 19, e "
            "título da subseção que a narra."
        ),
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "156 segmentos em 20 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "§ 25.4 declara o UNIVERSO sobre o qual o mapeamento um a um "
            "daquele bloco foi levantado. É o escopo da varredura, e escopo de "
            "varredura feita é fato datado."
        ),
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "5 cadeias",
        "classe": "registro datado de bloco",
        "por_que": "§ 25.5, tabela de baselines: '+5 cadeias novas' no bloco 19.",
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "17 rótulos",
        "classe": "a contagem É a pendência",
        "por_que": (
            "§ 26.1: '32 segmentos indeterminado, em 17 rótulos distintos'. O "
            "TAMANHO do problema é o problema: a seção seguinte trata os doze "
            "um a um, com a fonte que fecharia cada um. Transformar isso em "
            "ponteiro esvaziaria a pendência. 00-numeros.md § 2 publica a "
            "mesma contagem por segmento, e as duas conferem — a diferença é "
            "que lá ela é inventário e aqui é o enunciado do que falta."
        ),
    },
    {
        "arquivo": "docs/calculo/pendencias.md",
        "achado": "12 rótulos",
        "classe": "a contagem É a pendência",
        "por_que": (
            "§ 26.1 e § 26.2: 'os doze' são a pendência, nomeados um a um na "
            "tabela logo abaixo. E a § 26.1 EXISTE para registrar a colisão "
            "entre 12 e 13 e explicá-la — apagar o número apagaria a colisão."
        ),
    },
    # ---- tabelas-normativas/ (.json entrou no escopo no bloco 20) --------
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "10 cadeias",
        "classe": "guardada por teste que a recomputa",
        "por_que": (
            "`(segmento sem indexador)`.`quantos` = '37 segmentos, em 10 "
            "cadeias'. É o ÚNICO número vivo do catálogo, e existe porque o "
            "bloco 19 o tirou de dentro do texto replicado em cada segmento. "
            "`test_valida_cobertura.py::TestMapeamentoBloco19::test_a_contagem_"
            "de_segmentos_sem_indexador_bate_com_o_repositorio` o recomputa e "
            "compara string a string — envelhecer aqui QUEBRA a suíte."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "6 cadeias",
        "classe": "narrativa histórica",
        "por_que": (
            "'dizia 21 segmentos, em 6 cadeias quando já eram 37 em 10' — é a "
            "descrição do DEFEITO que fez a contagem sair do texto replicado. "
            "Atualizá-la destruiria o exemplo que justifica a regra vizinha."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "15 cadeias",
        "classe": "narrativa histórica",
        "por_que": (
            "Resto declarado das três afirmações de PRESENTE que o bloco 20 "
            "corrigiu ('ausentes das 15 cadeias', '34 rótulos nas 15 cadeias', "
            "'126 segmentos'). O que sobrou é a frase que NARRA a correção — "
            "'dizia as 15 cadeias quando já eram 20' —, e é ela que ensina por "
            "que .json entrou no escopo do detector."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "34 rótulos",
        "classe": "narrativa histórica",
        "por_que": (
            "`MAPEAMENTO_BLOCO_19.o_que_e`: 'Eram 34 em 15 cadeias na tarefa 2; "
            "são 36 em 20 cadeias depois da tarefa 3'. Variação narrada, com os "
            "dois extremos e a causa — e a ponta viva é conferida por "
            "`TestMapeamentoBloco19`."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "20 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "Ponta da mesma variação narrada, e também o `contagem_FINAL_DO_"
            "BLOCO`, que abre declarando-se resultado DO BLOCO 19. Registro "
            "datado não se reescreve."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "R1: 21",
        "classe": "registro datado de bloco",
        "por_que": (
            "`contagem_FINAL_DO_BLOCO`: 'O número publicado como resultado do "
            "bloco 19 … 20 cadeias | R1: 21 | R2: 1 | R3: 62', seguido da "
            "decomposição das 6 novas de R1 uma a uma. Registro datado."
        ),
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "R2: 1",
        "classe": "registro datado de bloco",
        "por_que": "Mesma linha de `contagem_FINAL_DO_BLOCO`. Registro datado do bloco 19.",
    },
    {
        "arquivo": "docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json",
        "achado": "R3: 62",
        "classe": "registro datado de bloco",
        "por_que": (
            "Mesma linha. **E é o exemplo do próprio ponto:** R3 foi a 64 com o "
            "fechamento do vocabulário de `aplicacao` e voltou a 63 com a "
            "tokenização de D2/D3/D4 no bloco 20. O 62 é o que o bloco 19 "
            "publicou, e continua sendo — o corrente vive em 00-numeros.md § 3."
        ),
    },
    # ---- scripts/ -------------------------------------------------------
    {
        "arquivo": "scripts/calculo/README.md",
        "achado": "20 cadeias",
        "classe": "registro datado de bloco",
        "por_que": (
            "'Tarefa 3 — cinco cadeias novas: 15 → 20 cadeias' — ponta de uma "
            "variação narrada do bloco 19, sob o aviso explícito de REGISTRO "
            "DATADO que abre o trecho. O runbook logo acima perdeu o placar "
            "digitado e ganhou ponteiro."
        ),
    },
]


# --------------------------------------------------------------------------
# Varredura
# --------------------------------------------------------------------------

def arquivos_varridos(raiz: Path) -> list[Path]:
    achados: list[Path] = []
    readme = raiz / "README.md"
    if readme.exists():
        achados.append(readme)
    for arvore in ARVORES:
        base = raiz / arvore
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix not in EXTENSOES_LIDAS:
                continue
            if "__pycache__" in p.parts or ".pytest_cache" in p.parts:
                continue
            if ".git" in p.parts:
                continue
            achados.append(p)
    return [p for p in achados if not _fora(p.relative_to(raiz).as_posix())]


def arquivos_das_arvores(raiz: Path) -> list[Path]:
    """Tudo o que as ÁRVORES declaradas contêm, **antes** das exclusões.

    Existe para que o escopo seja uma CONTA, e não um rótulo: a diferença entre
    esta lista e `arquivos_varridos` é exatamente `FORA_DA_VARREDURA`, e o teste
    abaixo prova a subtração. Ver `TestEscopoContado`.
    """
    achados: list[Path] = []
    readme = raiz / "README.md"
    if readme.exists():
        achados.append(readme)
    for arvore in ARVORES:
        base = raiz / arvore
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix not in EXTENSOES_LIDAS:
                continue
            if "__pycache__" in p.parts or ".pytest_cache" in p.parts:
                continue
            if ".git" in p.parts:
                continue
            achados.append(p)
    return achados


def _fora(rel: str) -> bool:
    return any(rel.startswith(x) or rel == x for x in FORA_DA_VARREDURA)


def varre(raiz: Path) -> list[tuple[str, str]]:
    """Pares (arquivo, achado), ordenados e sem repetição.

    O texto é normalizado em espaço único antes de casar: o repositório quebra
    linha no meio de '11\\ncadeias', e um achado que some por causa de reflow de
    parágrafo é falso negativo gratuito.
    """
    pares: set[tuple[str, str]] = set()
    for p in arquivos_varridos(raiz):
        rel = p.relative_to(raiz).as_posix()
        texto = re.sub(r"\s+", " ", p.read_text(encoding="utf-8"))
        for m in RE_RESULTADO.finditer(texto):
            pares.add((rel, m.group(0)))
    return sorted(pares)


def e_excecao(arquivo: str, achado: str) -> dict | None:
    for e in EXCECOES:
        if e["arquivo"] == arquivo and e["achado"] == achado:
            return e
    return None


# --------------------------------------------------------------------------
class TestNumeroDeResultadoDigitado(unittest.TestCase):

    def test_nenhum_numero_de_resultado_fora_de_00_numeros(self):
        sobrando = [
            f"{arq}: '{achado}'"
            for arq, achado in varre(RAIZ)
            if e_excecao(arq, achado) is None
        ]
        self.assertEqual(
            sobrando, [],
            "número de RESULTADO digitado fora de 00-numeros.md. Troque por "
            "ponteiro para docs/calculo/consolidado/00-numeros.md; se for "
            "registro datado de bloco ou narrativa histórica, declare em "
            "EXCECOES com o porquê.",
        )

    def test_a_varredura_enxerga_o_repositorio(self):
        """Contra o pior modo de falha deste arquivo: passar por vacuidade.

        Regex quebrada acha zero e aprova tudo em silêncio — o defeito que o
        bloco 17 pagou para aprender."""
        self.assertGreater(
            len(arquivos_varridos(RAIZ)), 40, "a varredura perdeu as árvores"
        )
        self.assertGreater(
            len(varre(RAIZ)), 15, "o detector de resultado parou de achar"
        )

    def test_detecta_resultado_plantado(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "docs").mkdir()
            (raiz / "docs" / "a.md").write_text(
                "Hoje são 311 testes e 20 cadeias.\n"
                "O validador fecha em R1: 21 e sai com 15 ok, 31 divergências.\n",
                encoding="utf-8",
            )
            self.assertEqual(
                varre(raiz),
                [
                    ("docs/a.md", "15 ok, 31 divergências"),
                    ("docs/a.md", "20 cadeias"),
                    ("docs/a.md", "311 testes"),
                    ("docs/a.md", "R1: 21"),
                ],
            )

    def test_conteudo_normativo_nao_e_alcancado(self):
        """A linha que mais erraria, e a razão de o detector exigir o
        substantivo da grandeza: número de DADO tem de passar ileso."""
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            (raiz / "docs").mkdir()
            (raiz / "docs" / "a.md").write_text(
                "IPC/IBGE de 42,72% em jan./1989; multiplicador 6,17; juros de "
                "0,5% a.m.; art. 457, § 2º; `pagina_pdf` 42; item 4.1.2.4; "
                "Resolução CJF n. 990/2026; 32 parâmetros negociáveis; "
                "26 regimes temporais; 50 vereditos; 19 passos.\n",
                encoding="utf-8",
            )
            self.assertEqual(varre(raiz), [])

    def test_relatorio_de_bloco_fica_fora_da_varredura(self):
        """Relatório que se atualiza sozinho deixa de ser registro."""
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            alvo = raiz / "docs" / "calculo" / "extracao"
            alvo.mkdir(parents=True)
            (alvo / "bloco-18-relatorio.md").write_text(
                "O bloco fechou com 15 cadeias e 267 testes.\n", encoding="utf-8"
            )
            self.assertEqual(varre(raiz), [])

    def test_00_numeros_e_o_unico_isento_por_ser_o_dono(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            alvo = raiz / "docs" / "calculo" / "consolidado"
            alvo.mkdir(parents=True)
            (alvo / "00-numeros.md").write_text(
                "20 cadeias, 316 testes, R1: 21\n", encoding="utf-8"
            )
            (alvo / "02-atualizacao.md").write_text(
                "20 cadeias\n", encoding="utf-8"
            )
            self.assertEqual(
                varre(raiz), [("docs/calculo/consolidado/02-atualizacao.md",
                               "20 cadeias")]
            )


class TestEscopoContado(unittest.TestCase):
    """**BLOCO 20 — escopo de varredura é CONTADO antes de declarado.**

    O relatório do bloco disse *"111 arquivos `.md` varridos"*, e **111 não é
    nenhum dos universos que existem**: `arquivos_varridos()` devolve um número,
    as árvores declaradas devolvem outro, e o repositório inteiro, um terceiro.
    A tarefa que existe para matar número não contado violou a própria regra.

    **O conserto não é cravar o número** — cravá-lo o faria envelhecer no
    primeiro arquivo novo, que é o defeito original com outra roupa. O conserto é
    publicar a **identidade** entre os universos e deixar o teste conferi-la:

        varridos  +  excluídos por FORA_DA_VARREDURA  ==  árvores declaradas

    **Qual universo esta suíte declara:** o do meio — as árvores `README.md`,
    `docs/`, `skills/`, `scripts/`, extensões `.md` e `.json`, **menos**
    `FORA_DA_VARREDURA`. Não é o repositório inteiro: `tests/` fica de fora, e
    fica declarado abaixo.
    """

    def test_o_escopo_e_a_subtracao_declarada_e_ela_fecha(self):
        arvores = arquivos_das_arvores(RAIZ)
        varridos = arquivos_varridos(RAIZ)
        excluidos = [
            p for p in arvores if _fora(p.relative_to(RAIZ).as_posix())
        ]
        self.assertEqual(
            len(varridos) + len(excluidos), len(arvores),
            "a conta do escopo não fecha: varridos + excluídos ≠ árvores",
        )
        self.assertEqual(
            sorted(varridos + excluidos), sorted(arvores),
            "há arquivo nas árvores que não está nem varrido nem excluído",
        )
        self.assertTrue(excluidos, "nenhuma exclusão aplicada — FORA_DA_VARREDURA morreu")

    def test_toda_exclusao_tem_alcance_real(self):
        """Prefixo de exclusão que não alcança arquivo algum é letra morta, e
        letra morta num escopo declarado é escopo mentiroso."""
        for prefixo in FORA_DA_VARREDURA:
            alcancados = [
                p for p in arquivos_das_arvores(RAIZ)
                if p.relative_to(RAIZ).as_posix().startswith(prefixo)
            ]
            self.assertTrue(alcancados, f"exclusão sem alvo: {prefixo}")

    def test_o_que_o_repositorio_tem_e_esta_suite_NAO_varre(self):
        """A terceira contagem, nomeada. Fora das árvores há `tests/` — fixtures
        e o seu README. Declarar isso é o que impede que `111` volte."""
        das_arvores = {p.resolve() for p in arquivos_das_arvores(RAIZ)}
        fora = sorted(
            p.relative_to(RAIZ).as_posix()
            for p in RAIZ.rglob("*")
            if p.is_file()
            and p.suffix in EXTENSOES_LIDAS
            and ".git" not in p.parts
            and "__pycache__" not in p.parts
            and ".pytest_cache" not in p.parts
            and p.resolve() not in das_arvores
        )
        self.assertTrue(
            all(x.startswith("tests/") for x in fora),
            f"árvore nova no repositório, fora do escopo declarado: {fora}",
        )


class TestLedgerNaoEnvelhece(unittest.TestCase):
    """A exceção não sobrevive ao fato que a justificava."""

    def setUp(self):
        self.pares = set(varre(RAIZ))

    def test_toda_excecao_ainda_corresponde_a_um_achado_real(self):
        orfas = [
            f"{e['arquivo']}: '{e['achado']}'"
            for e in EXCECOES
            if (e["arquivo"], e["achado"]) not in self.pares
        ]
        self.assertEqual(
            orfas, [],
            "exceção órfã: o número mudou ou a menção sumiu. Remova ou "
            "atualize a entrada de EXCECOES — ledger que sobrevive ao fato "
            "vira anistia.",
        )

    def test_toda_excecao_declara_classe_e_por_que(self):
        for e in EXCECOES:
            self.assertIn(e["classe"], CLASSES, e["achado"])
            self.assertGreater(len(e["por_que"]), 40, e["achado"])

    def test_a_chave_e_o_par_arquivo_achado(self):
        """Sem curinga. Tolerar '11 cadeias' em toda parte seria anistiar o
        número; a exceção vale no arquivo que narra o fato e em nenhum outro."""
        chaves = [(e["arquivo"], e["achado"]) for e in EXCECOES]
        self.assertEqual(len(chaves), len(set(chaves)), "entrada duplicada")
        for arquivo, achado in chaves:
            self.assertNotIn("*", arquivo)
            self.assertTrue(RE_RESULTADO.fullmatch(achado), achado)


# --------------------------------------------------------------------------
# O gerador
# --------------------------------------------------------------------------
EM_SUBPROCESSO = os.environ.get(gera_numeros.MARCA_RECURSAO) == "1"
MOTIVO = (
    "rodando dentro do próprio gerador (ele executa a suíte); a regeneração "
    "aqui recursaria sem fim"
)


class TestGerador(unittest.TestCase):

    def test_o_arquivo_gerado_existe_e_se_declara_gerado(self):
        texto = gera_numeros.DESTINO.read_text(encoding="utf-8")
        self.assertIn("ARQUIVO GERADO", texto.splitlines()[0])
        self.assertIn(gera_numeros.COMANDO, texto)

    def test_sem_timestamp_automatico(self):
        """`Date.now()` em arquivo versionado gera diff a cada rodada e polui o
        histórico. A ausência é verificada no CÓDIGO, não só na saída: é o
        import que traria o defeito de volta."""
        fonte = Path(gera_numeros.__file__).read_text(encoding="utf-8")
        for proibido in ("import datetime", "import time", "from datetime",
                         "time.time(", "datetime.now", "date.today"):
            self.assertNotIn(proibido, fonte, f"timestamp automático: {proibido}")

    def test_data_so_entra_por_argumento_e_validada(self):
        self.assertNotIn("Estado de referência declarado",
                         gera_numeros.DESTINO.read_text(encoding="utf-8"))
        with self.assertRaises(SystemExit):
            gera_numeros.main(["--data", "ontem"])

    @unittest.skipIf(EM_SUBPROCESSO, MOTIVO)
    def test_deterministico_e_em_dia(self):
        """As duas exigências na mesma rodada, porque custam a mesma coisa.

        DETERMINISMO — duas montagens seguidas, sem mudar nada, têm de dar
        bytes idênticos. Gerador não determinístico polui o histórico tanto
        quanto o timestamp que a § anterior proíbe.

        EM DIA — gerado e esquecido também envelhece; o defeito só muda de
        arquivo. O conteúdo em disco tem de ser o conteúdo do estado real.

        As duas juntas num teste só porque cada montagem executa os três
        validadores: separá-las dobraria o custo da suíte para provar o mesmo.
        """
        primeira = gera_numeros.monta(None)
        segunda = gera_numeros.monta(None)
        self.assertEqual(
            primeira, segunda,
            "o gerador NÃO é determinístico: duas rodadas seguidas, sem "
            "nenhuma mudança no repositório, produziram conteúdos diferentes.",
        )
        self.assertEqual(
            gera_numeros.DESTINO.read_text(encoding="utf-8"), primeira,
            f"00-numeros.md está desatualizado. Rode `{gera_numeros.COMANDO}`.",
        )

    def test_toda_skill_cabe_no_limite_de_linhas(self):
        """O limite de 500 que a § 7 publica é verificável — e aqui é verificado.
        Publicar limite sem teste é publicar promessa."""
        for caminho, linhas in gera_numeros.skills_md():
            self.assertLessEqual(linhas, gera_numeros.LIMITE_SKILL, caminho)

    def test_parse_que_nao_acha_aborta_em_vez_de_publicar_zero(self):
        """O pior modo de falha de um gerador: não achar e publicar zero, que
        vira número digitado com cara de medido. `_exige` morre alto."""
        with self.assertRaises(SystemExit):
            gera_numeros._exige(r"R9: (\d+)", "saída sem R9", "coisa nenhuma")


if __name__ == "__main__":
    unittest.main(verbosity=2)
