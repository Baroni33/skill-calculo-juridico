# skill: calculo-judicial-atualizacao

**Fase do pipeline:** Fase 5 — Build das skills.
**Eixo de mudança:** a cada mudança legislativa.

## Propósito

Cadeias período→indexador e período→juros, por jurisdição. É a skill que muda
quando o STF, o STJ, o TST ou o Congresso mexem na regra.

## O que entra

- Cadeias de correção monetária e juros, segmentadas por período e condição.
- Presets do "Catálogo de critérios" de `docs/calculo/01-plano-extracao.md`
  (`TRAB-ADC58-LEI14905`, `CIVEL-CC-TEMA1368`, `TRIB-FED-REPETICAO` etc.).
- Um arquivo por variante em `references/`.

## O que não entra

- Invariantes e aritmética — estão em `calculo-judicial-core`.
- Séries de valores mensais — contrato em `indices-judiciais`.
- **Segmento solto exposto ao usuário.** O usuário escolhe preset; o motor compõe
  segmentos. É montando bloco a bloco que se produz combinação inválida.

## references/

O agente carrega só o arquivo da jurisdição em questão:

```
trabalhista-nacional.md        cadeia nacional, Tabela Única CSJT
trabalhista-regional-trt3.md   os verbetes regionais que o manual invoca
civel-cc-nacional.md           Tema 1368, Lei 14.905, taxa legal
civel-regional-tjmg.md         tabela da CGJ/TJMG, histórico pré-2003
civel-federal.md               condenatórias em geral do CJF — correção + juros autônomos
desapropriacao.md              as TRÊS cadeias, com os juros compensatórios
tributario-federal.md          repetição, dívida fiscal, ECs 113/136, precatório
previdenciario.md
```

> **ACRESCENTADOS NO BLOCO 17:** `civel-federal.md` e `desapropriacao.md`. A lista de seis do
> bloco 16 **não fechava o domínio** — as duas matérias estavam hospedadas em
> `tributario-federal.md` § 5 por falta de lugar. **O conteúdo mudou de lugar, não de teor.**

> **RENOMEADO NO BLOCO 16.** A lista anterior separava por qualidade do devedor e por
> precedente; a nova separa por **alcance da norma — NACIONAL × REGIONAL**, porque a
> atualização trabalhista é nacional desde a Res. CSJT 8/2005 e o que o manual do TRT-3
> tem de regional são **os verbetes que ele invoca**, não sua aritmética. Razões arquivo a
> arquivo em [`references/README.md`](references/README.md).

## Armadilhas que esta skill precisa cobrir

- IPCA-**E** na fase pré-judicial trabalhista; IPCA (sem E) a partir de 30/08/2024.
  Fontes secundárias erram isso.
- Marco inicial dos juros trabalhistas é o **ajuizamento**, não a citação (R7).
- SELIC e taxa legal **englobam** correção e juros — cumular com índice
  inflacionário é erro (R1).
- Taxa legal é **razão entre fatores**, nunca subtração de percentuais (R11).

## Estado

**Escrito no bloco 16, fase 5.** `SKILL.md` e os seis arquivos de `references/` existem.

## `regras/` e `scripts/` — BLOCO 25

**A regra mora aqui, não em `docs/`.** As cadeias temporais `cjf.*` e `trab.hist.*`, o
**manifesto** que as inventaria e o **catálogo de tipos de indexador** vieram de
`docs/calculo/tabelas-normativas/` para `regras/`. O critério foi **CONSUMO**: quem lê
essas cadeias é `valida_cobertura.py`, as `references/` desta skill e os relatórios de
atualização. Migração **não reescreve conteúdo normativo** — texto e proveniência estão
como estavam, e o `git` registra renomeação.

**Esta skill é a DONA de `indexadores-tipo-catalogo.json`.** Havia três candidatas:
`indices-judiciais` (é semântica de índice), `calculo-judicial-core` (é vocabulário) e
esta. **Ganhou esta** por duas razões que não são de arrumação: **(1)** o catálogo é o que
o validador de **R3** lê, e `valida_cobertura.py` mora aqui; **(2)** as cadeias temporais
apontam para ele no campo `tipo_indexador_catalogo`, e sidecar vive com o diretório que
descreve. As outras duas skills **apontam** pelo caminho novo — **nenhuma guarda cópia**,
porque catálogo duplicado diverge e `test_classes_de_indice.py` existe para acusar isso.

| Diretório | O que é | Quem lê |
|---|---|---|
| `references/` | prosa por variante | o modelo |
| `regras/` | as cadeias, o manifesto e o catálogo de tipos | script, por caminho |
| `scripts/` | `valida_cobertura.py` (R1, R2, R3) e `valida_taxa_legal.py` (R6, R11, R12) | o agente |

**Os dois scripts são autocontidos** — não abrem arquivo de configuração e não dependem
de `docs/`. Eram assim antes de migrar, e continuam.
