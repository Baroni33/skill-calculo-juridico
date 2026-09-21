# Tabelas normativas

**Fase do pipeline:** Fase 2 (produção) e Fase 3 (consolidação).

> ## BLOCO 25 — OS `.json` NÃO MORAM MAIS AQUI
>
> **A regra foi para dentro da skill que a consome.** Este diretório guarda
> agora **só este README** — o contrato de campo, a proveniência e o histórico
> das decisões, que são **base de conhecimento** e continuam no repositório.
> **Os 32 arquivos de regra migraram**, por CONSUMO, e o `git` registra
> renomeação, não reescrita:
>
> | O que | Para onde | Quem consome |
> |---|---|---|
> | as **cadeias temporais** `cjf.*` e `trab.hist.*`, **`cadeias-manifesto.json`** e **`indexadores-tipo-catalogo.json`** (a contagem vive em `../consolidado/00-numeros.md`) | `skills/calculo-judicial-atualizacao/regras/` | `valida_cobertura.py`, `valida_cadeias.py` e as `references/` de atualização |
> | **`regimes-temporais-catalogo.json`** + **`camada-regime-temporal-schema.json`** | `skills/calculo-judicial-core/regras/` | `valida_regimes.py` — presets e invariantes |
> | **`camada-norma-coletiva-catalogo.json`**, **`camada-norma-coletiva-schema.json`** e os **6 `trt3-18.*`** | `skills/calculo-trabalhista-liquidacao/regras/` | `valida_parametros.py` e as `references/` de liquidação |
>
> **`indexadores-tipo-catalogo.json` tem UM dono: `calculo-judicial-atualizacao`.**
> É a skill que mais o cita, e é lá que mora `valida_cobertura.py`, o validador
> de **R3** que lê o catálogo. `indices-judiciais` e `calculo-judicial-core`
> **apontam** para ele pelo caminho novo; nenhuma das duas guarda cópia.
>
> **NENHUM `serie-*.csv` MIGROU.** Os 21 de `docs/calculo/extracao/trabalhista/`
> continuam onde estão, marcados `OUT_OF_SCOPE` no cabeçalho.
>
> > **CORREÇÃO — o bloco 25 tinha publicado aqui um absoluto que não valia.**
> > A frase era *"A SÉRIE DE VALOR NÃO MIGROU"*, e ela **não fora medida**: a
> > varredura que a sustentaria não existia. Ela existe agora, e **achou dois
> > casos** dentro das regras migradas. **Escopo, contado antes de declarado:**
> > os **32 arquivos `.json`** de `skills/*/regras/` — os mesmos 32 que
> > migraram —, lidos com `json.load` e `encoding='utf-8'`, percorridos em
> > profundidade atrás de **qualquer objeto com duas ou mais chaves na forma
> > `AAAA-MM`**. Três objetos casaram; **dois são valor por competência**, e o
> > terceiro é prosa:
> >
> > | Onde | O quê | Veredito |
> > |---|---|---|
> > | `trab.hist.fazenda-publica.juros-mora.json` → `percentuais_por_competencia` | **15** percentuais de juros, jun/12 a ago/13 | **fica, reclassificado** — ver abaixo |
> > | `cjf.previdenciario.correcao-monetaria.json` → `segmentos[8].valores_fixos_pct` | **4** percentuais de conversão em URV, mar a jun/94 | **fica, e a dúvida tem dono** — ver abaixo |
> > | `cjf.fgts.correcao-monetaria.json` → `notas[1].contraste_com_o_capitulo_4_geral` | 3 chaves de competência cujo valor é **frase** (*"42,72% nos dois — mesmo percentual"*) | **não é série**: é o contraste narrado da pendência `N-5`, e nenhum consumidor o lê como dado |
> >
> > **O defeito não foi o arquivo ter viajado; foi proclamar o absoluto sem
> > varrer.** Os dois primeiros ficam, e a razão é a mesma nos dois: **não são
> > série (B), são conjunto fechado por norma e exaurido.** O teste que este
> > projeto usa para separar as camadas é *"série (B) muda quando o governo
> > publica portaria"* — e nenhum destes dezenove números pode mudar.
> >
> > * **os quinze da fazenda pública** existem porque a meta anual da Selic
> >   ficou igual ou inferior a 8,5% (art. 12, II, `b`, da Lei 8.177/91), e isso
> >   **só ocorreu de jun/12 a ago/13**. O conjunto fechou em set/13. O
> >   `atalho_do_manual` do próprio arquivo **não os dispensa**: ele vale sob a
> >   condição de uso que declara — data final de atualização **posterior a
> >   31/08/13** —, e cálculo que termine **dentro** da janela não tem outra
> >   resposta senão os quinze;
> > * **os quatro da URV** não são índice, e o segmento já o dizia:
> >   `tipo_indexador: "nao-indexador"`, porque conversão de padrão monetário é
> >   **operação**, não medida de inflação. E o item 4.2.3.1 do Manual CJF
> >   **não enuncia fórmula**: enumera os quatro. **Não há regra a extrair além
> >   dos números.** Sem eles a cadeia diria *que* converte e não *como*.
> >
> > **A decisão está gravada nos dois arquivos**, em `DECISAO_BLOCO_25`, e o
> > rótulo errado foi trocado: `natureza` dizia *"série (B) — percentuais
> > cravados, mês a mês"* e passou a dizer o que o conjunto é. A chave `serie`
> > virou `percentuais_por_competencia`, com o nome antigo registrado ao lado
> > em `chave_anterior` para que a busca continue achando o caso.
> >
> > **Regra e valor continuam sendo coisas diferentes.** O que este bloco
> > aprendeu é que *"conjunto fechado por norma"* é uma **terceira coisa**, e
> > que ela pertence à regra.

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

Inventário **das cadeias**, e não conteúdo normativo. **Bloco 25: migrou junto com elas**,
para `skills/calculo-judicial-atualizacao/regras/` — o argumento não mudou, só o endereço:
um sidecar que descreve um diretório vive **com** esse diretório, e os dois consumidores
(`valida_cadeias.py` e `test_valida_cobertura.py`) leem UMA fonte.

É **piso, não retrato**: declara o conjunto mínimo de cadeias, por `id`, e o mínimo de
segmentos de cada uma. Cadeia a menos, ou cadeia que encolhe, é **regressão** e derruba o
validador; cadeia a mais é crescimento e é **gravada automaticamente** por
`valida_cadeias.py`. **Arquivo mantido por script — não o edite à mão para fazê-lo crescer.**
Edição manual só para *baixar* um número ou remover um `id`, e o porquê vai no commit.

A chave é o `id`, nunca o nome do arquivo: foi a renomeação `trt3.hist.*` → `trab.hist.*`
que derrubou a descoberta de 11 cadeias para 7 em silêncio, no bloco 17.

## Validação

**Bloco 25 — os validadores também se dividiram, e por CONSUMO.** Quem valida
regra de skill virou **script de skill** e mora ao lado da regra; quem afere o
repositório continua em `scripts/calculo/`. A tabela abaixo dá o caminho de
**hoje** — os antigos `scripts/calculo/valida_{regimes,parametros,cobertura,taxa_legal}.py`
**não existem mais**, e o ponteiro único para eles é
`scripts/calculo/caminhos_de_skill.py`.

| Validador | Onde mora | O que cobra |
|---|---|---|
| `skills/calculo-judicial-atualizacao/scripts/valida_cobertura.py` | script de skill | R1 e R2 sobre `segmentos`, e R3. Vale para a família de cadeias período → indexador; toda tabela dessa família deve passar antes de entrar |
| `skills/calculo-judicial-atualizacao/scripts/valida_taxa_legal.py` | script de skill | R11 — taxa legal sobre um par que o usuário passa |
| `skills/calculo-judicial-core/scripts/valida_regimes.py` | script de skill | presets e invariantes da camada de regime temporal |
| `skills/calculo-trabalhista-liquidacao/scripts/valida_parametros.py` | script de skill | R14 a R18, precedência, conflito e piso legal. `--catalogo-ok` verifica a consistência interna do catálogo |
| `scripts/calculo/valida_cadeias.py` | ferramenta de pipeline | R1/R2/R3 sobre **todas** as cadeias deste repositório e a conferência contra `cadeias-manifesto.json` |
| `scripts/calculo/valida_bloco_tabelas.py` | ferramenta de pipeline | contagem, faixas, vigências e proveniência do bloco 1 |

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

