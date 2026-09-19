# Extração — Manual CJF, Res. 990/2026 (93 páginas)

**Fase do pipeline:** Fase 2 — Extração bifurcada por tipo de conteúdo.

## Propósito

Extração do manual vigente da Justiça Federal. Diferente do trabalhista, cabe em
contexto: **passada única, sem map-reduce**.

## O que entra

- Cap. 1 custas, cap. 2 dívida fiscal, cap. 3 dívidas diversas,
  cap. 4 liquidação de sentença (núcleo), cap. 5 requisições de pagamento.
- Tabelas de indexadores dentro dos cap. 2 e 4 → tabular (CSV/JSON).
- O restante → prosa.
- Proveniência em todo registro: `documento`, `pagina_pdf`, item numerado.

## O que não entra

- Séries de valores mensais de índices (regra 4 do plano).
- Dado tabular convertido em prosa (regra 2 do plano).
- Regra do contencioso cível estadual — este manual **não governa** esse ramo.

## Paginação

Offset **1**. A página 1 do PDF é folha em branco; `numero_impresso = pagina_pdf - 1`.
Grave `pagina_pdf`. Ver `../../fontes.md`.

## Lacuna conhecida

O item 2.8 remete a um quadro de multas administrativas "anexado a este manual"
que não existe no PDF. Registrar como lacuna, não tentar suprir.

## Estado

Vazio. Sem conteúdo até a Fase 2.
