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
- Aritmética decimal exata, ponto flutuante binário proibido no caminho de cálculo,
  critério de truncamento definido e consistente por etapa. O tipo concreto é
  escolha do implementador — `references/linguagem-alvo-e-aritmetica.md`.
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

## `regras/` e `scripts/` — BLOCO 25

**Os presets de regime temporal são regra, e regra mora na skill que a consome.**
`regimes-temporais-catalogo.json` e `camada-regime-temporal-schema.json` vieram de
`docs/calculo/tabelas-normativas/` para `regras/`, porque quem os lê é
`scripts/valida_regimes.py` — e regime temporal decide **qual regra se aplica**, que é
matéria de invariante, não de liquidação nem de atualização.

`scripts/valida_regimes.py` resolve o catálogo a partir do **próprio `__file__`**:
`regras/` é irmão de `scripts/`. Antes o caminho atravessava o repositório até `docs/`,
e a instrução de instalação — *não copie `docs/`* — o quebrava no instante em que a skill
saía daqui. **É essa a armadilha que o bloco 24 registrou e o 25 desarmou.**

**O catálogo de tipos de indexador NÃO está aqui.** Esta skill o cita; o dono é
`calculo-judicial-atualizacao`, e o que existe aqui é ponteiro.
