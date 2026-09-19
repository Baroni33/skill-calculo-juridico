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

## Nomenclatura

- `bloco-NN-assunto.md` — relatório do bloco: o que saiu, contagens, divergências.
- `serie-18.X-assunto.csv` — série de valores, cabeçalho `OUT_OF_SCOPE`. Não é
  conteúdo de skill; fica como evidência de conferência contra a tabela mantida à parte.

A regra da triagem continua valendo: um bloco por sessão, contexto limpo entre blocos.

## Estado

| Bloco | Páginas | Tipo | Situação |
|---|---|---|---|
| 1 — Tabelas (item 18) | 373–471 | Tabular | **Fechado.** `bloco-01-tabelas.md` |
| 2 — Critérios e estrutura (itens 1, 3, 4, 5) | 9–17 (+6.1, p. 18) | Prosa | **Fechado.** `bloco-02-relatorio.md` |
| demais | 18–372 | Misto | Não iniciados |

Do bloco 1: 20 CSV de série aqui, 6 JSON semânticos em `../../tabelas-normativas/`.
Validação determinística: `python scripts/calculo/valida_bloco_tabelas.py`.

Do bloco 2: espinha, detalhe e relatório. Validação adversarial — dois revisores
independentes, um caçando omissões e outro afirmações sem respaldo; resultado e achados
aceitos/rejeitados no relatório.
