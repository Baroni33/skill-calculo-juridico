# tests/fixtures/calculo — fixtures de aceite

**Fase do pipeline:** Fase 6 — Aceitação.

## Propósito

Casos com resultado numérico conhecido, transcritos da seção 8 de
`docs/calculo/00-base-normativa.md` e conferidos contra o Manual CJF
(Res. 990/2026).

## Critério de aceite de QUEM — a correção do bloco 23

**Estas fixtures são o critério de aceite do SISTEMA — o motor com a série de
índices plugada —, e NÃO o critério de aceite da skill.**

Até o bloco 23 este arquivo afirmava que *"são o critério de aceite do motor: um
agente novo lê a skill, implementa, e o resultado bate aqui"*. **Isso é falso
para um agente que só tem a skill,** e o bloco 22 mediu o quanto: **as quatro
pararam antes de produzir número**, por falta de série. A **fixture 1 sozinha
consome 23 meses de IPCA-E**, e as skills publicam **cinco valores de índice ao
todo** — porque `indices-judiciais` declara, literalmente, que *"esta skill não
carrega série — é o ponto inteiro dela"*.

| Nível | O que é | Executável |
|---|---|---|
| **NÍVEL 1** — aceite **da skill** | invariantes e aritmética: R11 pelos dois pares publicados, R12 por AST, R1 na composição, as cinco cadeias de arredondamento, o NMP de três ramos | **só com a skill** — `scripts/calculo/test_aceite_nivel1.py` |
| **NÍVEL 2** — aceite **do sistema** | as **quatro fixtures deste diretório** | **exige série carregada** (camada B) |

**As fixtures não mudaram, e não devem mudar.** O que mudou é o que se afirma
sobre o papel delas. Os dois níveis, com a justificativa da escolha:
`skills/calculo-judicial-core/references/aceite-em-dois-niveis.md`.

## Conteúdo

| Arquivo | Caso | Esperado |
|---|---|---|
| `fixture-01-fazenda-publica-jun2022.json` | devedor FP, data-base jun/2022 | R$ 3.484,95 |
| `fixture-02-fazenda-publica-jun2026.json` | mesmo caso, jun/2026 | R$ 5.218,28 |
| `fixture-03-nao-fazenda-publica-jun2026.json` | devedor não-FP, jun/2026 | R$ 5.772,95 |
| `fixture-04-precatorio-complementar.json` | resíduo de precatório complementar | R$ 4.435,07 / R$ 4.435,04 |

## Schema

`id`, `fonte` (`documento`, `item`, `pagina_pdf`), `entradas`, `esperado`,
`tolerancia`, `observacao`.

`pagina_pdf` é índice de PDF. O manual do CJF tem offset de 1 — ver
`docs/calculo/fontes.md`.

## As divergências são a asserção, não o defeito

Duas fixtures carregam divergência **esperada** entre o método resumido e o
detalhado:

- **Fixture 2** — R$ 0,01
- **Fixture 4** — R$ 0,03

**A divergência é entre os dois métodos do próprio manual — nunca do corpus.** Ela
decorre do critério de truncamento aplicado a cada etapa, e o próprio manual a
declara desprezível. **A `tolerancia` destes dois arquivos NÃO é banda de
aceitação: é asserção** (`divergencia_e_assercao: true`). Portanto:

- motor que produz **um número só não passa**, ainda que o número esteja certo —
  faltou o outro método;
- motor que produz **dois números iguais FALHA**: zerar a diferença significa
  arredondar errado;
- a diferença tem de ser **exatamente** a declarada — R$ 0,01 e R$ 0,03.

Não "corrija" a fixture para fazer os métodos convergirem: a convergência forçada
é o sintoma que estes casos existem para detectar. Os dois procedimentos estão em
`skills/calculo-judicial-atualizacao/references/metodos-resumido-e-detalhado.md`.

## O que não entra

- Caso sem resultado numérico publicado.
- Número inventado para fechar conta.
- Valores extraídos do manual trabalhista de 2016 (defasado) — a estrutura dos
  casos daquele manual serve, os números não.
