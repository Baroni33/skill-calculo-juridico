# Extração — Manual TRT-3 (julho/2016, 471 páginas)

**Fase do pipeline:** Fase 2 — Extração bifurcada por tipo de conteúdo.

## Propósito

Um arquivo por bloco de páginas da seção "Triagem do corpus" de `01-plano-extracao.md`.
Nomenclatura: `NNN-NNN-assunto.md`, onde `NNN` é índice de PDF.

## O que entra

- Conteúdo dos blocos de páginas, extraído conforme o tipo declarado na triagem:
  prosa vira prosa com validação adversarial; tabular vira CSV/JSON com validação
  determinística.
- Proveniência em todo registro: `documento`, `pagina_pdf`, item numerado.

## O que não entra

- **Norma vigente inferida deste manual.** Ele é anterior à Reforma Trabalhista
  (Lei 13.467/2017), à ADC 58, à EC 113/2021, à Lei 14.905/2024 e à EC 136/2025.
  Os capítulos 7, 10, 12, 14 e parte do 8 não servem como fonte normativa — seguem
  para `../../confronto-normativo/`.
- Séries de valores mensais de índices (regra 4 do plano).
- Dado tabular convertido em prosa (regra 2 do plano).
- Jurisprudência embutida — vira índice de referência, não conteúdo.

## Paginação

Offset **0**. `pagina_pdf` = número impresso. Ver `../../fontes.md`.

## Estado

Vazio. Sem conteúdo até a Fase 2. Um bloco por sessão, contexto limpo entre blocos.
