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
trabalhista-privado.md
trabalhista-fazenda.md
civel-cc-tema1368.md
civel-mg-cgj.md
tributario-federal.md
previdenciario.md
```

## Armadilhas que esta skill precisa cobrir

- IPCA-**E** na fase pré-judicial trabalhista; IPCA (sem E) a partir de 30/08/2024.
  Fontes secundárias erram isso.
- Marco inicial dos juros trabalhistas é o **ajuizamento**, não a citação (R7).
- SELIC e taxa legal **englobam** correção e juros — cumular com índice
  inflacionário é erro (R1).
- Taxa legal é **razão entre fatores**, nunca subtração de percentuais (R11).

## Estado

Vazio, inclusive `references/`.
