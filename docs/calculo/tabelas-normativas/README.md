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

## Conflito aberto: uma segunda família de tabelas não cabe neste schema

O schema acima descreve **cadeia período → indexador**: linha do tempo partida em
`segmentos`, cada um com um indexador e o que ele engloba.

A extração do bloco 1 (tabelas do Manual TRT-3) produziu regras de outra natureza, que
não têm linha do tempo de indexador nenhuma:

| Arquivo | Forma |
|---|---|
| `trt3-18.1-incidencia-parcelas.json` | matriz parcela × tributo, com fundamento por célula |
| `trt3-18.4-18.6-irrf-estrutura.json` | estrutura de faixa progressiva com parcela a deduzir |
| `trt3-18.7-contribuicao-estrutura.json` | estrutura de faixa com teto, sem parcela a deduzir |
| `trt3-18.8-grau-de-risco-estrutura.json` | enquadramento por atividade → alíquota |
| `trt3-18.10-urv-conversao.json` | conteúdo e lacuna de uma tabela de cotação |
| `trt3-18.13-rsr-criterios.json` | critérios de contagem, quatro variantes |

Não têm `segmentos`, `engloba` nem `aplicacao`, e `valida_cobertura.py` não as alcança.
Foram gravadas com um shape próprio, declarado em `categoria: "A-semantica"`, em vez de
forçadas no schema canônico.

**É conflito a resolver na Fase 3, não decisão tomada.** As duas saídas aparentes: um
schema canônico com `tipo` discriminando as famílias, ou dois diretórios distintos.
Definir antes que a Fase 5 leia daqui.

## Terceira família: a camada de norma coletiva

`camada-norma-coletiva-schema.json` e `camada-norma-coletiva-catalogo.json` não são tabelas
de regra nem séries: são o **contrato de uma camada de resolução**. Dado
`(parametro, categoria, competencia)`, devolvem valor mais proveniência, sustentando as
invariantes R14 a R18.

Entram aqui porque representam **regra**, não valor — o catálogo guarda defaults legais e
pisos, não cláusulas de instrumentos. As cláusulas ficam em `tests/fixtures/calculo/` e, no
uso real, em dados do cliente.

Inventário dos parâmetros em `../parametros-negociaveis.md`. Está **parcial**: faltam os 13
parâmetros da seção 10 de `02-base-normativa-verbas.md`, arquivo ausente do repositório.

## Validação

- `scripts/calculo/valida_parametros.py` — R14 a R18, precedência, conflito e piso legal.
  `--catalogo-ok` verifica a consistência interna do catálogo.
- `scripts/calculo/valida_cobertura.py` — R1 e R2 sobre `segmentos`. Vale para a família
  de cadeias período → indexador; toda tabela dessa família deve passar antes de entrar.
- `scripts/calculo/valida_bloco_tabelas.py` — contagem, faixas, vigências e proveniência
  do bloco 1.

## Estado

Seis tabelas da família (A) do bloco 1, item 18 do Manual TRT-3. Ver
`../extracao/trabalhista/bloco-01-tabelas.md`.

Dois artefatos da camada de norma coletiva, do bloco 5. Ver
`../extracao/bloco-05-relatorio.md`.

Nenhuma tabela da família período → indexador ainda: essas vêm do capítulo 7, que é outro
bloco e passa obrigatoriamente pela Fase 4.
