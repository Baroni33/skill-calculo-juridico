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
| `tipo_indexador` | **R3.** Seis valores: `nominal`, `percentual`, **`janela-deslocada`**, `nao-indexador`, `indeterminado` — e `englobante`, **RETIRADO no bloco 19**, sem nenhum uso. Acompanha `tipo_indexador_fonte` e, quando indeterminado, **`tipo_indexador_pendencia` OU `tipo_indexador_razao`, nunca os dois** |
| `tipo_indexador_razao` | **bloco 19.** *A fonte existe e diz que o índice NÃO CABE em mês calendário* — a da TR é *"período entre datas de aniversário e prefixação"*. **Não é pendência:** pendência diz *"não há fonte"* e fecha quando a fonte chegar; razão **não se fecha esperando fonte** |

> **`tipo_indexador` tem catálogo próprio: `indexadores-tipo-catalogo.json`.** O nome do
> campo **não** é `tipo` porque `tipo` já é chave de topo em toda cadeia, com valor
> `"cadeia-temporal"`. O valor **sai da fonte** (item 4.1.2.4 do Manual CJF, `pagina_pdf`
> 42, e o apoio de `bloco-08-jf-detalhe.md`); **sem fonte é `indeterminado` e vira
> pendência** — `pendencias.md` § 23 —, **nunca classificado por dedução a partir do nome**.

> **Bloco 19 — `janela-deslocada` é a terceira classe COM DEFASAGEM.** O período de coleta
> não coincide com o mês calendário: cai **metade em M−1 e metade em M** (do dia 16 do mês
> anterior ao dia 15 do mês de referência). É a classe do **IPCA-15** e do **IPCA-E**, e a
> fonte que a sustenta é **externa ao corpus** (IBGE), declarada como tal no catálogo.
> Com três classes há **três pares** de virada, não um. Pendências em `pendencias.md` § 25.

> **`englobante` saiu porque era erro de categoria.** Englobamento é fato de **R1**, e quem
> o grava é **`engloba`** — que **não mudou**. Gravá-lo também em `tipo_indexador` deixava a
> **SELIC cega para R3**: ela nunca entrava em comparação de defasagem, embora tenha
> defasagem. A SELIC é **`percentual`**; a **taxa legal**, que a fonte não alcança, é
> **`indeterminado`** (`P19-01`) — e **não** `percentual` por analogia com a SELIC.

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

Inventário dos parâmetros em `../parametros-negociaveis.md` — **32 parâmetros**, com os 13
da § 10 de `02-base-normativa-verbas.md` já consolidados (v2.0).

A classificação `apenas-elevacao` × `qualquer` ancora-se no **art. 611-B da CLT**, cujo texto
integral não está no corpus: só os incisos VI, XVII e XVIII foram conferidos. Os parâmetros
que nenhum deles alcança carregam `fundamento_611b: "nao-mapeado"` e
`classificacao_provisoria: true` — 16 dos 32. Lista via `Catalogo.provisorios()`.

## Manifesto: `cadeias-manifesto.json`

Inventário **desta pasta**, e não conteúdo normativo — mora aqui pela mesma razão que
`indexadores-tipo-catalogo.json`: um sidecar que descreve o diretório vive com o diretório,
e os dois consumidores (`valida_cadeias.py` e `test_valida_cobertura.py`) leem UMA fonte.

É **piso, não retrato**: declara o conjunto mínimo de cadeias, por `id`, e o mínimo de
segmentos de cada uma. Cadeia a menos, ou cadeia que encolhe, é **regressão** e derruba o
validador; cadeia a mais é crescimento e é **gravada automaticamente** por
`valida_cadeias.py`. **Arquivo mantido por script — não o edite à mão para fazê-lo crescer.**
Edição manual só para *baixar* um número ou remover um `id`, e o porquê vai no commit.

A chave é o `id`, nunca o nome do arquivo: foi a renomeação `trt3.hist.*` → `trab.hist.*`
que derrubou a descoberta de 11 cadeias para 7 em silêncio, no bloco 17.

## Validação

- `scripts/calculo/valida_cadeias.py` — R1/R2/R3 sobre todas as cadeias e a conferência
  contra `cadeias-manifesto.json`.
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

---

## Camada de regime temporal (bloco 6)

`regimes-temporais-catalogo.json` e `camada-regime-temporal-schema.json` são de uma
**terceira família**, que não segue o schema de segmentos acima.

Enquanto as tabelas normativas dizem **como se atualiza** um valor e a camada de
norma coletiva diz **quanto vale** um parâmetro, esta diz **qual regra de apuração**
vale na competência — e é avaliada **antes** das outras duas (R22).

**26 regimes, catorze eixos de corte distintos.** O eixo não é o mesmo entre
regimes: a OJ 394 corta pela data da hora extra trabalhada; a multa do art. 467,
pela data da sentença; a prescrição intercorrente, pela data da determinação
judicial. Dos catorze, apenas dois são de competência ou fato; os outros doze são
processuais, documentais ou contratuais, e o **conteúdo do título** comparece tanto
quanto a competência.

O campo `eixo_origem` tem quatro estados: **declarado** (13), **inferido** (5, o
corpus sustenta o eixo para uma pergunta vizinha), **herdado** (3) e
**não declarado** (5, inaplicáveis). Quatro regimes estão **sem default** porque o
corpus manda não resolver. Em ambos os casos o resolvedor devolve
`calculavel: false` com o motivo, em vez de um número plausível.

Leitura humana em `../presets-regime.md`.

