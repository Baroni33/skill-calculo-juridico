# skill: calculo-judicial-core

**Fase do pipeline:** Fase 5 — Build das skills.
**Eixo de mudança:** raro.

## Propósito

Modelo de domínio, invariantes, aritmética decimal, memória de cálculo,
comparador/diff e catálogo de critérios. É a base sobre a qual as outras três
skills assentam.

## O que entra

- Entidades e vocabulário mínimo do domínio.
- As invariantes R1–R13 da seção 7 de `docs/calculo/00-base-normativa.md`.
- Aritmética decimal: nenhum float, critério de truncamento definido e consistente
  por etapa.
- **Comparador.** Fica aqui, não na skill trabalhista: "recalcular pelo critério
  correto e produzir o diff parcela a parcela" é a mesma operação nas três
  jurisdições.
- Fixtures de aceite (`tests/fixtures/calculo/`).

## O que não entra

- Cadeias período→indexador — vão para `calculo-judicial-atualizacao`.
- Apuração de verbas — vai para `calculo-trabalhista-liquidacao`.
- Séries de valores de índices.

## Estrutura obrigatória do SKILL.md

Espinha fixa para toda skill do conjunto, conforme
`docs/calculo/01-plano-extracao.md`:

```
frontmatter: name, description (explícita e "pushy" sobre quando disparar)
## Quando usar / quando não usar
## Modelo de domínio
## Invariantes
## Procedimento
## Catálogo de critérios
## Armadilhas conhecidas
## Fixtures de aceite
## Ponteiros
```

Abaixo de 500 linhas. Passando disso, mais uma camada de hierarquia com ponteiro
explícito.

## Estado

Vazio. A estrutura se escreve a partir do conteúdo consolidado, não antes.
