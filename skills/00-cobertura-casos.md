# Cobertura dos 33 casos difíceis pelas quatro skills

**Tarefa 4 do bloco 16.** Para cada caso de [`../docs/calculo/03-casos-dificeis.md`](../docs/calculo/03-casos-dificeis.md),
**em qual skill e seção** está a resposta. Linha de base:
[`../docs/calculo/consolidado/00-validacao-casos.md`](../docs/calculo/consolidado/00-validacao-casos.md)
— 31 respondidos, 2 parciais, 0 não respondidos.

> **Caso que o consolidado respondia e nenhuma skill responde é perda na transposição.**

**Método.** Li a pergunta de cada caso, abri a seção apontada e perguntei *"a resposta está ali,
ou só o tema está?"*. Nenhum ponteiro foi aceito por rótulo. Escopo das buscas negativas no fim.

---

## Nota de atualização — segunda passagem

**Este arquivo foi reescrito depois de duas correções nas skills.** O histórico fica:

| Caso | 1ª passagem | Agora | O que mudou nas skills |
|---|---|---|---|
| **C22** | `PARCIAL` | **`COBERTO`** | nasceu `### R8 e R16 — Precedência` em `calculo-judicial-core/SKILL.md` |
| **C24** | `PARCIAL` | **`COBERTO`** | nasceu `### Parâmetros negociáveis (R14–R18) — a direção vem do art. 611-B` em `calculo-trabalhista-liquidacao/SKILL.md` |

**C22 e C24 abriram como `PARCIAL` na primeira passagem e foram fechados no mesmo bloco.** Não é
ruído: é a verificação funcionando. A primeira passagem apontou **onde deveria entrar**; as duas
seções entraram ali, e a segunda passagem conferiu o texto, não o rótulo.

**Correção de contagem própria, independente das skills.** A 1ª passagem declarava *core 16 · liq
11*; a soma das listas dava **15 e 12**. A tabela de distribuição abaixo está recontada.

**As demais correções do bloco** (rótulos `RG1`–`RG15` na prosa regional, `TRT-3, TRT-4 e TJMG`,
`B04-F7` `VIGENTE`, sete limitações bloqueantes + três menores) foram conferidas contra as linhas
deste arquivo; **as que tocam ponteiros estão refletidas em C18, C27, C30, C32 e C33.**

> **Pendência observada, NÃO corrigida aqui** (este arquivo não corrige skills): a contagem de
> regimes temporais está **28** em `liq/references/cortes-e-bifurcacoes.md` (linha 236) e ainda
> **26** na espinha `liq/SKILL.md` (linhas 323 e 485). C18 **não depende do número** — depende dos
> eixos —, então segue `COBERTO`, com a divergência registrada.

---

## Placar

| | Casos |
|---|---|
| **COBERTO** | **33** |
| **PARCIAL** | **0** |
| **PERDIDO** | **0** |

**C31 e C33, os dois parciais do consolidado, FECHARAM.** **C22 e C24**, os dois parciais que
abriram na transposição, **também fecharam**. Ver § "Os quatro que fecharam".

Abreviações: **core** = `calculo-judicial-core`; **atu** = `calculo-judicial-atualizacao`;
**liq** = `calculo-trabalhista-liquidacao`; **idx** = `indices-judiciais`.

---

## Grupo 1 — Cumulação e composição

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C1** | Englobamento | **core** (+ atu, idx) | `## Invariantes` → `### R1` — *"aplicar correção junto … é erro material"*, literal | **COBERTO** |
| **C2** | Taxa legal é razão | **idx** (+ atu) | `## Invariantes` → `### R11` — fórmula, 6 decimais, IPCA-15 de `m−1`, **e a tabela de validação**: set/2025 `1,377047%` × `1,374156%` | **COBERTO** |
| **C3** | Deflação e piso nominal | **core** (+ idx) | `### R5 e R6 — Pisos`: piso **por parcela**, e *"dividir pelo índice negativo"* como **redação defeituosa que não se implementa** | **COBERTO** |
| **C4** | Nominal × percentual | **idx** (+ core R3, atu R3) | `### R3` — tabela nominal/percentual, fonte item 4.1.2.4, *"desloca o cálculo em um mês"* | **COBERTO** |

---

## Grupo 2 — Ordem de operações e imputação

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C5** | Imputação proporcional sem norma | **liq** (+ core R10) | `references/imputacao-e-amortizacao.md § 3` (tabela de escopo: 101 × 0 × 0 em 471 páginas) e `§ 3.1` (direção do delta, `pr.imputacao` sem default); `## Limitações declaradas` **item 3 das sete que bloqueiam a conta** | **COBERTO** |
| **C6** | Descarregar antes dos juros | **core** (+ liq) | core `### R23`; liq `## Invariantes` → bloco `R23` com a **minuta da p. 328** e o `anatocismo` zero no cap. 10 | **COBERTO** |
| **C7** | A amortização parte a linha do tempo | **liq** | `### Passo 7` + `references/imputacao-e-amortizacao.md § 2` (roteiro A–J; G/H levam ao marco final) e `§ 3.1` (amplitude com `índice_residual × pct_juros_residual`) | **COBERTO** |
| **C8** | Base contra ordem | **core** (+ liq) | core `## Comparador` → *"a ordem … é indiferente — distributividade, delta 0,00"* + tabela com −2,48%, −3,15%, −R$ 285,83; liq `references/imputacao-e-amortizacao.md § 1` com a aritmética dos dois caminhos | **COBERTO** |
| **C9** | Amplitude tem forma fechada | **core** (+ liq) | core `## Comparador` (fórmula + *"qual das três grandezas limita muda de caso para caso"*); liq `references/imputacao-e-amortizacao.md § 3.1` com os quatro casos e o **Exemplo 5 limitado pelo abatimento** | **COBERTO** |
| **C10** | Data de referência da dedução | **liq** (+ atu) | `references/imputacao-e-amortizacao.md § 6` — **três** posições, `16.4.11` com **duas teses**, e o cap. 10 adotando o levantamento **sem citar a Súmula 15**; atu `references/trabalhista-regional-trt3.md`, verbete **`RG1`** | **COBERTO** |

---

## Grupo 3 — Arredondamento e precisão

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C11** | Cinco cadeias de arredondamento | **core** (+ idx R12, liq Passo 6) | `## Aritmética — as cinco cadeias de arredondamento` — tabela por etapa com casas e fonte, e o NMP de três ramos divergindo de `ROUND_HALF_UP` em `x,y50`–`x,y54` | **COBERTO** |
| **C12** | Precisão plena na cadeia interna | **core** (+ idx) | `## Aritmética` → `### Três regras que o motor não pode violar`, item 1 — *"valor exibido nunca realimenta cálculo — mesmo que parte dos exemplos do corpus o faça"* | **COBERTO** |

---

## Grupo 4 — Capitalização

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C13** | Exceção histórica à R4 | **atu** (+ core) | atu `### R4-EXCEÇÃO` — 27/02/1987 a 03/03/1991, DL 2.322/87, três registros independentes; core `### R4` grava **dentro do invariante** | **COBERTO** |
| **C14** | Acumulação por soma | **core** (+ liq) | core `### R23`, nota final — *"juros acumulam por soma, nunca por multiplicação — Súmula 121 do STF"*, **duas regras anti-anatocismo distintas**. *A parte "o regime vem da lei que institui a taxa" também não está no consolidado — não é perda de transposição* | **COBERTO** |

---

## Grupo 5 — Regimes temporais

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C15** | OJ 394 / Tema 9 | **liq** | `references/cortes-e-bifurcacoes.md`, linha **20/03/2023** da tabela de bifurcações — eixo **data em que a HE foi trabalhada**, `F4-01`, com as duas versões; `## Armadilhas` → ficha do Tema 9 **omite a modulação** | **COBERTO** |
| **C16** | Item "i" da ADC 58 | **liq** (+ atu armadilha 11) | `references/imputacao-e-amortizacao.md § 5` — tabela i.1 × i.2, **alcance da proteção** (§ "Alcance da proteção dentro de i.1"), **default i.1**, ordem por R22 (`pr.adc58-item-i` antes de `pr.imputacao`) | **COBERTO** |
| **C17** | Intertemporal, Tema 23 | **atu** (+ liq) | atu `## Limitações declaradas` item 4 (Tema 23, modulação negada, ultratividade vencida); liq `references/cortes-e-bifurcacoes.md`, linha `pr.intertemporal` — **`R20-EXCEÇÃO` cai de cinco para quatro** | **COBERTO** |
| **C18** | Eixos não intercambiáveis | **liq** (+ core, atu Passo 0) | `### Passo 0` (tabela de eixos por preset) e `## Catálogo de critérios` → `references/cortes-e-bifurcacoes.md` (**28 regimes, catorze eixos**; a espinha ainda diz 26 — ver Nota de atualização); os três exemplos do caso: multa 467 → data da sentença, divisor bancário → estado processual, OJ 394 → data da HE | **COBERTO** |
| **C19** | Súmula 124, modulação | **liq** | `references/cortes-e-bifurcacoes.md`, bloco *"A Súmula 124 SOBREVIVEU"* (`JR-01`, `VIGENTE`) — alcança **sentenças transitadas ainda em liquidação, desde que silentes quanto ao divisor**, *"exatamente o caso de uso de conferência"* | **COBERTO** |
| **C20** | Consolidação de dez/2021 | **atu** (+ idx armadilha 4) | `references/tributario-federal.md § 6` — tabela dos **cinco** ramos (IPCA-E 1,17% · INPC 0,84% · TR 0,00%, juros 0,4412% nos cinco); `references/previdenciario.md` repete o ramo INPC | **COBERTO** |
| **C21** | Desapropriação | **atu** | `references/tributario-federal.md § 5.5`, linha **dez./2021** da tabela de cortes: *"Já incluídos na SELIC aplicada aos juros de mora"* — **sem taxa adicional** (`D8-C11`); mais o corte de **ago./2017** e a contradição `N-6` | **COBERTO** |

> **C21 era o caso que passou por rótulo no bloco 15.** Desta vez a afirmação foi lida na linha
> da tabela, não no título da seção. **Está lá, literal** — reconferido na 2ª passagem (§ Amostragem).

---

## Grupo 6 — Norma coletiva e parâmetros

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C22** | Precedência | **core** (+ liq) | **`### R8 e R16 — Precedência`** — **as duas escadas**, R16 especializando R8 na camada de parâmetro, mais as três consequências e a distinção **R16 × R18** | **COBERTO — fechou** |
| **C23** | Ausência de norma coletiva | **core** (+ liq) | `### R14 a R18` — default legal, marca `sem cobertura coletiva`, **e a exceção da ajuda-alimentação**: *"não existe"*, terceiro estado | **COBERTO** |
| **C24** | Art. 611-B decide a direção | **liq** | **`### Parâmetros negociáveis (R14–R18) — a direção vem do art. 611-B`** — anti-heurística literal, tabela de três vias com **insalubridade/periculosidade (XVIII)** e **noturno (VI)**, o derivado (ƒ) e a lacuna dos 27 incisos | **COBERTO — fechou** |
| **C25** | Divisor é derivado | **liq** (+ core) | liq `## Modelo de domínio` (par `(44h, 200)`, 210 como atributo do regime, teste que impede reintrodução); `references/verbas-catalogo.md` — *"o sábado como RSR não altera o divisor"* (teses do IRR-849) | **COBERTO** |
| **C26** | Norma coletiva é do contrato | **core** (+ liq) | core `### R14 a R18` → **R17**, com os dois empregados da mesma empresa no mesmo processo | **COBERTO** |

---

## Grupo 7 — Leitura do corpus

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C27** | Regra mora no exemplo | **liq** | `## Como este corpus se lê` § 1 — contagem por capítulo (**cap. 9 → 7 · 10.1 → 12 · 11 → 17 · 16 → 6**) e três regras estruturais (mês comercial inclusivo, precisão plena encadeada, base da multa do art. 467); o 13º como base autônoma no INSS em `references/descontos-inss-irrf.md` (`P7-04`) | **COBERTO** |
| **C28** | Fundamento fora do capítulo | **liq** | `## Como este corpus se lê` § 2 — **seis em trinta e seis**, IN SRF 15/2001 com **1 ocorrência em 471 páginas**, e os outros cinco nomeados | **COBERTO** |
| **C29** | Escopo declarado | **liq** (+ core, idx, atu na prática) | `## Como este corpus se lê` § 6 — *"zero no segmento"* × *"zero em 471 páginas"*, com a origem (NMP, duas rodadas) | **COBERTO** |

---

## Grupo 8 — Defeitos do original

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C30** | O comparador precisa conhecer os erros | **core** (+ liq, idx, atu) | core `## Comparador` → a tabela das **três classes** (erro material × delta de método × comportamento do original) e `## Armadilhas conhecidas`; liq `## Armadilhas` com A11, A1, A4, A7, A12; **os dois bloqueios aritméticos** em liq `## Limitações` **item 2** (deltas de 10,00 e 2.036,51, com a propagação) e idx `## Limitações` 2; dez/10 em idx armadilha 5 | **COBERTO** |
| **C31** | Divergências esperadas não são erros | **core** (+ atu) | core `## Fixtures de aceite` — *"As fixtures 2 e 4 divergem do corpus em R$ 0,01 e R$ 0,03. É esperado"*; atu `## Fixtures de aceite` — *"um motor que zera essas diferenças está arredondando errado"* | **COBERTO — fechou** |

---

## Grupo 9 — O que o corpus não resolve

| # | Assunto | Skill (primária) | Seção | Estado |
|---|---|---|---|---|
| **C32** | Fazenda Pública | **core** (+ liq, atu) | core `### R9` — os **dois testes incompatíveis**, *"pergunta ao jurídico"*; liq `## Limitações` **item 6** (cap. 8 *"não explore atividade econômica"* × cap. 14 *"direta e indireta"*, **"não harmonizo"**) e `references/encargos-processuais.md` com `economia mista` | **COBERTO** |
| **C33** | Dados externos bloqueantes | **core** (+ idx) | core `## Limitações declaradas` — as três numa **só tabela** (Tabela Única do CSJT `P9-02`; art. 85, § 3º, do CPC; série histórica de normas coletivas); idx `## Limitações` § 4 repete as três em tabela `extraído × a integrar`; consequências: idx § 1 (bloqueia o motor trabalhista), liq `## Limitações` **item 4** (não calcula honorários por faixa; `pr.planos-economicos` bloqueado, `P19`), core `R14` (default legal, marcado) | **COBERTO — fechou** |

---

## Os quatro que fecharam

| # | Estado anterior | Onde fechou |
|---|---|---|
| **C31** | Parcial no bloco 15 — fixtures 2 e 4 **não nomeadas** na espinha | core `## Fixtures de aceite`, deltas **R$ 0,01 e R$ 0,03** nomeados por fixture; atu `## Fixtures de aceite`, teste invertido |
| **C33** | Parcial no bloco 15 — três dependências **dispersas** | core `## Limitações declaradas`, as três na mesma tabela. **Ressalva honesta mantida:** a *consequência da ausência* só está completa para a Tabela Única do CSJT; para as outras duas é preciso ir a idx § 4 e a liq `## Limitações` 4 |
| **C22** | **Parcial na 1ª passagem deste arquivo** — `R16` com zero ocorrências; o core só trazia a escada de três | core **`### R8 e R16 — Precedência`**. Fechou **acima do pedido**: a 1ª passagem pedia "um quarto degrau em R8"; a resolução foi **duas escadas** — R16 especializa R8 na camada de parâmetro, inserindo a norma coletiva **acima da escolha do usuário**. Fonte do enunciado de R16 declarada (`camada-norma-coletiva-schema.json`, que prevalece sobre a leitura humana — `parametros-negociaveis.md` § 1), o que explica por que o consolidado dizia três: **ele enuncia R8, não R16.** A seção ainda separa **R16 de R18** — *"o título vence o piso; a cláusula, não"* |
| **C24** | **Parcial na 1ª passagem deste arquivo** — faltavam a anti-heurística e os parâmetros concretos | liq **`### Parâmetros negociáveis (R14–R18) — a direção vem do art. 611-B`**: *"A âncora é o artigo, NÃO a presença de 'no mínimo'"*, tabela de três vias com **insalubridade e periculosidade (inciso XVIII)** e **adicional noturno (inciso VI)** → `apenas-elevacao`; parágrafo único → `qualquer`; demais → `qualquer` sob o **Tema 1046**; mais o **derivado (ƒ)** (divisor, não se sobrescreve) e as lacunas declaradas |

---

## Amostragem de verificação — cinco `COBERTO` reconferidos na 2ª passagem

**Critério: a resposta do caso está no texto da seção, ou só o tema está?** Abri a seção e li a
afirmação. **Nenhum foi rebaixado.**

| # | O que fui procurar | O que encontrei | Veredito |
|---|---|---|---|
| **C16** | o **default** entre i.1 e i.2, e a **ordem de avaliação** | `imputacao-e-amortizacao.md § 5`: *"Tem default — i.1, que é a regra; i.2 é declarada exceção"* e *"Ordem de avaliação, por R22: `pr.adc58-item-i` **antes** de `pr.imputacao`"*. **Alcance da proteção** tem subtítulo próprio | **confirmado** |
| **C19** | se a **modulação** está, e não só a súmula | `cortes-e-bifurcacoes.md`: *"alcança sentenças transitadas ainda em liquidação, desde que silentes quanto ao divisor, que é exatamente o caso de uso"* — com `JR-01`, `VIGENTE`, conferido por script | **confirmado** |
| **C21** | a frase da linha dez./2021, **literal** | `tributario-federal.md § 5.5`: *"o regime autônomo acaba — literal: 'Já incluídos na SELIC aplicada aos juros de mora'. **Sem taxa adicional**"*, `D8-C11` | **confirmado** |
| **C27** | as **quatro contagens por capítulo**, não um total agregado | liq `## Como este corpus se lê` § 1: **cap. 9 → 7; cap. 10.1 → 12; cap. 11 → 17; cap. 16 → 6**, com as três regras estruturais nomeadas | **confirmado** |
| **C32** | os **dois testes incompatíveis**, e que a skill **não escolhe** | liq `## Limitações` 6 dá os dois textos (cap. 8 × cap. 14) e fecha com *"Não harmonizo"*; core `### R9` remete ao jurídico | **confirmado** |

> **A armadilha deste projeto é o rótulo que bate e o conteúdo que não.** Os cinco passaram pela
> leitura do texto. O único desvio achado na amostragem foi **numérico e fora do caso** — os 26/28
> regimes de C18 —, registrado na Nota de atualização e **não corrigido aqui**.

---

## Cobertura por skill

Contagem pela skill **primária** de cada caso. **Recontada** — a 1ª passagem publicou totais que
não batiam com as próprias listas.

| Skill | Primária em | Quais |
|---|---|---|
| **calculo-judicial-core** | **15** | C1, C3, C6, C8, C9, C11, C12, C14, C22, C23, C26, C30, C31, C32, C33 |
| **calculo-trabalhista-liquidacao** | **12** | C5, C7, C10, C15, C16, C18, C19, C24, C25, C27, C28, C29 |
| **calculo-judicial-atualizacao** | **4** | C13, C17, C20, C21 |
| **indices-judiciais** | **2** | C2, C4 |
| **Total** | **33** | — |

**A distribuição é coerente com o desenho das skills**, não sinal de desvio: os 33 casos são
majoritariamente sobre **invariantes, ordem de operações e leitura do corpus** — matéria do
núcleo — e sobre **liquidação trabalhista**, que é o corpus extraído. O fechamento de C22 (core) e
C24 (liq) **manteve** as duas primárias onde já estavam: cada seção nova nasceu na skill que a 1ª
passagem indicara.

> **`indices-judiciais` com apenas duas primárias merece leitura, e não é alarme.** Ela é
> **secundária em seis** — C2, C3, C4, C11, C20, C33 — e em C2 é a **única** que traz os números
> de validação do caso (`1,377047%` × `1,374156%`), sem os quais o caso não fecha. A skill
> responde à camada (B), e os casos difíceis quase não perguntam por (B). **Nenhum conteúdo de
> caso foi parar nela por engano.**

---

## Escopo das buscas — afirmação de ausência exige universo E data

**As buscas da 1ª passagem foram DESCARTADAS, não reaproveitadas.** Elas registravam zeros que
hoje são falsos (`R16` → 0, `no mínimo` → 0): eram verdadeiras no estado anterior das skills e
deixaram de ser quando as duas seções entraram. **Toda negativa precisa do universo em que foi
feita e do estado em que foi feita** — é a regra que a própria liq enuncia (`## Como este corpus
se lê` § 6), aplicada a este arquivo.

**Universo (estado de 2ª passagem).** `grep -rn -i --include=*.md --exclude=00-cobertura-casos.md`
sobre `C:\projetos\skill-calculo-juridico\skills\` — **23 arquivos**: **4 `SKILL.md`**,
**13 `references/*.md`** e **6 `README.md`** (4 de skill + 2 de `references/`). **Este arquivo de
cobertura é excluído do universo**, para que citar um termo aqui não fabrique a ocorrência dele.
Buscas em `docs/` **não** foram feitas — nenhuma afirmação abaixo alcança o corpus.

| Termo | 1ª passagem | **Agora** | Onde / consequência |
|---|---|---|---|
| `R16` | 0 | **6** | todas em `core/SKILL.md`, `### R8 e R16`. **Derruba o PARCIAL de C22** |
| `no mínimo` | 0 | **2** | `liq/SKILL.md`, § 611-B — a anti-heurística. **Derruba o PARCIAL de C24** |
| `apenas-elevacao` | 1, sem exemplo | **2** | `liq/SKILL.md` (com parâmetros concretos) + `cortes-e-bifurcacoes.md`. C24 |
| `XVIII` · `inciso VI` | 0 | **1 · 1** | ambas na tabela de três vias de `liq/SKILL.md`. C24 |
| `norma coletiva da competência` | 0 | **1** | degrau 2 da escada R16, `core/SKILL.md`. C22 |
| `TRT-4` | *não buscado* | **18**, em **7 arquivos** | confirma que o TRT-4 deixou de sumir da cobertura regional |
| `RG14` | *não buscado* | **4** | o verbete SEE/TRT-4 (RSR sobre comissões) existe nos dois `references/` regionais. C10 |
| `economia mista` | 6 | **6** | estável. C32 |
| `dia 20` · `vencimento do IR` | 0 | **0** | **ressalva menor mantida em C27**: dos dois casos estruturais do enunciado, só o 13º como base autônoma foi transposto |
| `0,4412` · `1,17` · `0,84` | 13, em atu e idx | *não rebuscado* | C20 — **afirmação positiva**, verificada por leitura da tabela de `tributario-federal.md § 6` |
| `compensat` · `Súmula 124` · `IRR-849` · `23,83` · `art. 354` · `Súmula 121` | presentes | *não rebuscadas* | C5, C9, C14, C19, C21 — **positivas**, confirmadas por leitura da seção |

> **Só as negativas exigem recontagem.** Uma afirmação positiva se confirma abrindo a seção, e foi
> assim que as cinco da amostragem foram tratadas. **As duas negativas que sustentavam PARCIAL
> foram refeitas e caíram** — por isso o placar mudou.

**Nenhum caso foi marcado COBERTO por proximidade de título.** Em todos, a afirmação do caso foi
lida no texto da seção apontada.
