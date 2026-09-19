# tests/fixtures/calculo — fixtures de aceite

**Fase do pipeline:** Fase 6 — Aceitação.

## Propósito

Casos com resultado numérico conhecido, transcritos da seção 8 de
`docs/calculo/00-base-normativa.md` e conferidos contra o Manual CJF
(Res. 990/2026). São o critério de aceite do motor: um agente novo lê a skill,
implementa, e o resultado bate aqui.

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

Elas decorrem do critério de truncamento aplicado a cada etapa, e o próprio manual
as declara desprezíveis. **Um motor que zera essas diferenças está arredondando
errado.** Não "corrija" a fixture para fazer os métodos convergirem: a convergência
forçada é o sintoma que estes casos existem para detectar.

## O que não entra

- Caso sem resultado numérico publicado.
- Número inventado para fechar conta.
- Valores extraídos do manual trabalhista de 2016 (defasado) — a estrutura dos
  casos daquele manual serve, os números não.
