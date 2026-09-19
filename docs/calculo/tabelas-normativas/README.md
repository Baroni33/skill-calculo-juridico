# Tabelas normativas

**Fase do pipeline:** Fase 2 (produção) e Fase 3 (consolidação).

## Propósito

Artefato central do módulo. Representa **regra**, não série de valores.

Um JSON por regra, validado por script — não por revisão de LLM (regra 2 do plano).
O schema canônico está na seção "Schema das tabelas normativas" de
`../01-plano-extracao.md`. Não duplicar o schema aqui; ele evolui lá.

## O que entra

JSON com `id`, `jurisdicao`, `tipo_acao`, `componente`, `fonte`, `vigencia_norma`
e `segmentos`. Campos que não podem faltar, e por quê:

| Campo | Razão |
|---|---|
| `engloba` | torna a checagem de cumulação (R1) mecânica |
| `condicao` | tabelas bifurcam por devedor, data da sentença e data do fato gerador |
| `aplicacao` | a defasagem é fonte silenciosa de divergência |
| `multiplicador_transicao` | conversões de moeda e indexador |
| `valor_fixo_pct` | expurgos com percentual cravado |
| `base_incidencia` | só para juros — valor originário vs. corrigido |
| `tipo: nominal \| percentual` | só para o catálogo de índices; ver R3 |

## O que não entra

- **Séries de valores mensais.** Só a semântica de aplicação e o contrato com a
  tabela mantida à parte (regra 4 do plano).
- Regra sem proveniência (regra 3 do plano).

## Validação

`scripts/calculo/valida_cobertura.py` verifica R1 e R2 sobre os `segmentos`.
Toda tabela deve passar antes de entrar.

## Estado

Vazio. Sem conteúdo até a Fase 2.
