---
name: indices-judiciais
description: >-
  Use esta skill sempre que a pergunta for sobre o VALOR de um índice, sobre a SEMÂNTICA de um
  indexador, ou sobre a QUALIDADE de uma tabela de séries. Gatilhos típicos: "qual o IPCA-E de
  março de 2019", "quanto valeu o INPC em nov/2021", "essa tabela de índices está completa",
  "falta mês na série", "de onde vem esse fator de 1,0253", "o perito usou IPCA ou IPCA-E",
  "IPCA-E é a mesma coisa que IPCA", "a série de SELIC serve de correção monetária", "índice
  nominal ou percentual", "Ufir, OTN, BTN, ORTN, IRSM, URV, IPC-R, IGP-DI, IPC/FGV", "expurgo
  de jan/1989", "como calcular a taxa legal do Bacen", "série 29541 do SGS", "Tabela Única do
  CSJT", "que formato a tabela de índices precisa ter", "qual a versão da série usada neste
  cálculo", "posso interpolar mês faltante". NÃO use para decidir QUAL índice incide em cada
  período (é `calculo-judicial-atualizacao`), nem para apurar verbas.
---

# Índices judiciais — semântica e contrato de séries

Esta skill é a camada **(B)**: **o dado que muda quando o governo publica portaria, não quando muda a lei.**

> A distinção que organiza o projeto inteiro: **regra (A)** muda com lei ou jurisprudência;
> **série (B)** muda com portaria. *"Uma tabela de IRRF desatualizada é série a atualizar; uma
> alíquota mudada por emenda é regra a bifurcar."* — `consolidado/01-dominio-e-invariantes.md` § 1.1.

**Ela responde a três perguntas, e só a essas três:** (1) o que este indexador **significa**, e
como se aplica; (2) que **contrato** uma série cumpre para ser consumível; (3) a série recebida
é **válida** — e o que fazer quando não é.

---

## Quando usar / quando não usar

**Use quando** a pergunta for sobre o **valor**, a **identidade** ou a **integridade** de uma
série: distinguir IPCA de IPCA-E, classificar um indexador como nominal ou percentual, conferir
se uma tabela recebida tem buraco, decidir se um fator pode alimentar a conta, ou rastreá-lo.

**Não use — e carregue a skill indicada:**

| Pergunta | Skill |
|---|---|
| Qual índice vale de 2015 a 2024; onde fica o corte; qual cadeia por jurisdição | `calculo-judicial-atualizacao` |
| Invariantes R1–R24 na íntegra, aritmética decimal, ordem das operações | `calculo-judicial-core` |
| Horas extras, 13º, férias, RSR, INSS, IRRF — apuração de verbas | `calculo-trabalhista-liquidacao` |

**A fronteira que importa, nos dois sentidos:** `calculo-judicial-atualizacao` diz *"IPCA-E"* e
**não sabe quanto o IPCA-E valeu**; esta skill sabe **o que é** o IPCA-E e **que forma** a série
dele precisa ter, e **não decide se ele incide no seu caso**.

**E esta skill não carrega série** — é o ponto inteiro dela (`README.md`, "O que não entra"):
descreve o **contrato**, não o dado. Os CSV de `docs/calculo/extracao/trabalhista/` abrem com o
cabeçalho `# OUT_OF_SCOPE — série de valores, não entra na skill` e existem como **evidência de
conferência**, não como fonte de consulta.

---

## Modelo de domínio

| Termo | Significado exato |
|---|---|
| **série (B)** | sequência `competência → valor`, mantida fora da skill. **Dado externo, não regra** |
| **indexador** | o identificador do que a série mede — `IPCA-E`, `Ufir`, `INPC` |
| **`tipo` (nominal · percentual)** | **o campo que não pode faltar** — R3. Decide a defasagem |
| **englobante** | índice que **cobre correção e juros** — SELIC e taxa legal (R1) |
| **derivado** | índice que **não é publicado**: resulta de operação sobre outras séries — a taxa legal (R11) |
| **fator** | número multiplicativo acumulado, **6 decimais, truncamento** (R12) |
| **`aplicacao`** | a defasagem — **vive na cadeia (A), não na série (B)** |
| **cobertura** | intervalo `[primeira competência, última competência]` efetivamente presente |
| **proveniência** | `documento`, `item`, `pagina_pdf` — de onde cada linha veio |

### Onde mora a defasagem — e por que isso importa para o contrato

Nos JSON de `docs/calculo/tabelas-normativas/`, **`aplicacao` está no segmento da cadeia**, nunca
na série. Consequência para o contrato: **a série é indexada por competência de publicação,
crua.** Quem desloca é o consumidor.

> **Uma série já defasada na origem é uma série corrompida.** Entregue uma tabela "já com a
> Súmula 381 aplicada" e o motor a desloca de novo, errando **um mês** — sem que nenhuma
> checagem de integridade acuse, porque a série continua contígua e monotônica.

---

## Invariantes

**Não reproduzidas aqui.** Enunciado integral de **R1 a R24** em
`docs/calculo/consolidado/01-dominio-e-invariantes.md` § 2, e em `calculo-judicial-core`.
**As seis que mordem nesta skill:**

### `R3` — nominal × percentual. A armadilha mais silenciosa da camada de séries

| Classe | Índices | O que a série reflete |
|---|---|---|
| **nominal** | **Ufir, BTN, OTN, ORTN** | a inflação do mês **anterior** |
| **percentual** | **INPC, IGP-DI** — e só os nomeados | a inflação do **próprio** mês |

Fonte: item 4.1.2.4 do Manual CJF (`pagina_pdf` 42), via `02-atualizacao.md` § 11, R3.

> **Trocar entre tipos sem ajustar a defasagem desloca o cálculo em um mês** — sem sinal de
> alarme: a conta roda, o total é plausível, e o erro atravessa a cadeia inteira.

**Corolário de R2 que só faz sentido aqui** — `R-08-04`: em cadeia de índices **nominais**, fim
e início no **mesmo mês** (OTN/BTN em jan/1989) **não é dupla contagem**, e o manual o diz
expressamente. Um validador de sobreposição que não conheça `tipo` acusa falso positivo.

### `R1` — SELIC e taxa legal **englobam** correção e juros

**Uma série de SELIC não é uma série de correção monetária.** Consumi-la como tal **conta a
inflação duas vezes** — **erro material**, não escolha de critério. Vale para o dado concreto do
repositório: `serie-18.15-juros-selic-acumulados.csv` (528 linhas, 264 no quadro
`taxa-selic-mensal`) **não alimenta coluna de correção**.

### `R11` — a taxa legal é **razão entre fatores**, e é **derivada, não publicada**

```
TL_m = (Fator_Selic_m / Fator_Deflator_{m-1} − 1) × 100
```

**Seis decimais, truncamento. IPCA-15 do mês anterior** na regra geral (Res. CMN 5.171/2024);
**INPC** na variante previdenciária (Manual CJF, item 4.3.2, Nota 3). **Piso zero por `R6`**
(CC art. 406, § 3º): resultado negativo vira **zero**, nunca negativo.

> A lei e o acórdão descrevem *"SELIC deduzido o IPCA"*. **Isso é descrição do efeito, não a
> operação.** A subtração literal erra ~**0,003 p.p./mês**, e **acumula**.

Conferido nos dois pares publicados (`pendencias.md` §§ 2 e 3, variante INPC) — e ali o
truncamento também se resolveu empiricamente: `1,3770478004` → **`1,377047`**, não `1,377048`.

| Competência | Fator Selic | Fator deflator | Razão | Subtração |
|---|---|---|---|---|
| Set/2025 | 1,01164156 | 0,9979 | **1,377047%** ✓ | 1,374156% ✗ |
| Mai/2026 | 1,01090058 | 1,0081 | **0,277807%** ✓ | 0,280058% ✗ |

### `R5` — piso nominal: índice negativo **entra**

Índice negativo **entra no cálculo**; o piso é **por parcela**, não sobre o total (REsp
1.265.580; Manual CJF item 4.1.2.2). **A instrução do manual TRT-3 de "dividir pelo índice
negativo" é redação defeituosa e NÃO se implementa** — `pendencias.md` § 9-B a classifica como
ambígua. O que se implementa é R5.

### `R12` — as cinco cadeias de arredondamento. **O critério é POR ETAPA, não global**

| Etapa | Critério | Casas | Fonte |
|---|---|---|---|
| **Fator de índice e taxa legal** | **truncamento** | **6** | CJF 4.2.1.1, Nota 6 |
| Grandeza física (hora centesimal, nº de HE) | **half-up** | 2 | TRT-3, item 5.3 |
| Valor monetário intermediário e final | **truncamento** | 2 | CJF |
| **NMP** (nº de meses do RRA) | **três ramos** — IN 1500/14, art. 45, § único | 1 | TRT-3, pp. 226 e 230 |
| Cadeias do capítulo 6 | **quatro práticas não enunciadas** | — | armadilha |

**A regra do NMP NÃO é half-up:** 2ª casa `<5` mantém, `>5` sobe, **`=5` manda olhar a 3ª casa**
(0–4 mantém, 5–9 sobe). Difere de `ROUND_HALF_UP` na faixa `x,y50` a `x,y54`.

**Nenhum float, em caminho algum.** `valida_bloco_tabelas.py` converte toda célula por `Decimal`
(`para_decimal`): *"Aritmética decimal em toda parte, nenhum float (R12)"*.

### Precisão plena encadeada — e o que isso faz com o comparador

**A cadeia interna roda em precisão plena. Os valores impressos com 2 casas NÃO são os
operandos.** O truncamento é só na **emissão**, e **valor exibido nunca realimenta cálculo** —
mesmo que parte dos exemplos do manual o faça. **Duas consequências operacionais:** (1) **as
colunas impressas do manual não somam os totais impressos**, por 0,01 a 0,02; (2) **o limiar de
alarme do comparador não deve ser o centavo.**

**`1/30` é dízima.** Usar `Decimal(1)/Decimal(30)`, **nunca** o truncamento impresso: o manual
grafa **`0,0333%`** na regra e **`0,03333%`** no exemplo **duas linhas abaixo**
(`02-atualizacao.md` § 7, régua 4). Em contagens longas de dias, muda.

### `R13` — reprodutibilidade: a série entra na conta com **versão**

Toda conta grava **a versão das séries consumidas**. **Uma série revisada pelo órgão emissor
não pode alterar silenciosamente um cálculo já emitido.** Ver "Limitações declaradas" — a
infraestrutura não existe.

---

## Procedimento

### Passos 1 e 2 — identificar pelo nome **exato**, depois classificar

`IPCA`, `IPCA-E` e `IPCA-15` são **três índices diferentes** (ver "Catálogo"). Recusar o
identificador ambíguo é mais barato que descobrir a troca no total. Da classificação saem três
decisões: **a defasagem** (R3), **se pode conviver com uma linha de juros** (R1) e **se o valor é
publicado ou derivado** (R11).

**São cinco classes, não três**, e a quarta é a que mais governa o motor:

| Classe | O que afirma |
|---|---|
| `nominal` · `percentual` | reflete o mês **anterior** · o **próprio** mês |
| `englobante` | cobre correção **e** juros (R1) — **neutro em R3** |
| **`indeterminado`** | **o conceito se aplica, e não há fonte.** A virada **bloqueia** sob `R3-INDETERMINADO` |
| `nao-indexador` | **verificado, e o conceito não se aplica** — moeda, paridade, conversão |

> **`indeterminado` e `nao-indexador` afirmam coisas diferentes:** *"não se sabe"* × *"não se
> pergunta"*. **Ausência do campo não é nenhum dos dois** — é indistinguível de esquecimento.

### Passo 3 — validar a série recebida, nesta ordem

Ordem e critérios derivados de `scripts/calculo/valida_bloco_tabelas.py`:

| # | Checagem | Como | Falha é |
|---|---|---|---|
| 1 | **Proveniência** | toda linha tem `documento`, `item` e `pagina_pdf`, e a página cai no intervalo declarado da seção | **ERRO** |
| 2 | **Contagem** | linhas extraídas contra contagem independente sobre a fonte | **ERRO** |
| 3 | **Vigências** | sem lacuna nem sobreposição na linha do tempo | **DIVERGÊNCIA** |
| 4 | **Faixas** | dentro de cada vigência: sem lacuna, sem sobreposição, limites monotônicos | **DIVERGÊNCIA** |
| 5 | **Calendários** | contiguidade dos dias do mês | **DIVERGÊNCIA** |

### Passo 4 — separar **erro de extração** de **divergência do original**

**É a distinção que governa a camada inteira**, literal no cabeçalho do script: **ERRO** é
*"defeito da extração, precisa ser corrigido no extrator"*; **DIVERGÊNCIA** é *"defeito ou
lacuna do original, fica registrado, não se conserta"*. E: *"saída não-zero só em ERRO.
Divergência é resultado esperado do trabalho."*

### Passo 5 — o que fazer com buraco no meio

Quatro comportamentos, todos observados no validador, **nenhum deles interpolação**:

| Situação | Conduta |
|---|---|
| **Lacuna entre vigências** | registra divergência com as competências das duas pontas (`lacuna de AAAA-MM a AAAA-MM`). **Não preenche.** |
| **Sobreposição** | registra divergência. **Não desempata** — pode ser real: jan/10 tem dois quadros vigentes no original |
| **Célula ilegível** | **suspende a análise daquela vigência** em vez de reportar a lacuna aparente — *"o vão seria artefato da leitura, não do original"* |
| **Rótulo em forma livre** | vai para `NÃO VERIFICÁVEL MECANICAMENTE`. Fica como **texto literal**; normalizar seria interpretar |

> **A conduta padrão diante do buraco é registrar e parar, nunca costurar.** O CSV guarda a
> **string literal do original**; a normalização convive com ela em coluna separada
> (`competencia` ao lado de `competencia_original`).

### Passo 6 — registrar a versão consumida (R13)

Sem versão, a conta não é reproduzível. Ver "Limitações declaradas", item 3.

---

## Catálogo de critérios

**Contrato de série — os campos.** Derivado do formato efetivamente extraído
(`bloco-01-tabelas.md` § 1) e das checagens de `valida_bloco_tabelas.py`. **Nenhum campo
inventado:** a última coluna diz se o campo existe hoje.

| Campo | Papel | Existe hoje? |
|---|---|---|
| `documento` | arquivo-fonte | **sim** — cabeçalho `# documento=…` e coluna por linha |
| `emissor` | quem publicou | **sim** — cabeçalho `# emissor=…` |
| `item` | seção da fonte | **sim** — coluna |
| `pagina_pdf` | página, com `offset_paginacao` declarado | **sim** — coluna |
| `serie` | identificador do quadro (ano, nome do índice) | **sim** — coluna |
| `chave` | competência, na forma do original | **sim** — coluna (`jan`, `Janeiro`, `JAN`) |
| `competencia` + `competencia_original` | competência **normalizada** `AAAA-MM` **ao lado** da string literal | **sim, no formato novo** — `serie-9.2.11` |
| `valor` | o dado, como string decimal do original | **sim** — coluna |
| `quadro` | discrimina quadros distintos no mesmo item | **sim** — usado em `serie-18.15-juros-selic-acumulados.csv` |
| **`tipo`** (nominal/percentual) | **R3** | **só como `tipo_indexador` em UM JSON de cadeia**, e ali marcado como **inferência** |
| **`versao`** / **`data_de_coleta`** | **R13** | **NÃO EXISTE** — ver "Limitações declaradas" |

**Cobertura** não é campo: **é derivada** da varredura de vigências (checagem 3) — quem precisa
de "início e fim" lê as pontas da série validada, não um metadado.

### Os índices, com a classificação que decide tudo

**Catálogo completo — 28 indexadores, com o que cada um é, onde entra e a fonte da
classificação — em [`references/catalogo-de-indices.md`](references/catalogo-de-indices.md).**
A classificação normativa é `docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json`,
**que é o que o validador lê**.

**Quatro classes, e a terceira é a que este bloco tornou visível:**

| Classe | Quais | Fonte |
|---|---|---|
| **nominal** — inflação do mês **anterior** | **ORTN, OTN, BTN, Ufir** | item 4.1.2.4, letra a, `pagina_pdf` 42 — **nomeados literalmente** |
| **percentual** — inflação do **próprio** mês | **INPC, IGP-DI** (item 4.1.2.4, letra b) e **IPC/IBGE** (por **D8-C21**) | idem |
| **indeterminado** — o conceito se aplica, **e não há fonte** | IPCA, IPCA-E, IPCA-15, IPCA série especial, IPC/FGV, IPC-R, IRSM, MVR, **TR** e remuneração básica da poupança | **nenhuma** — `P17-01`, `P17-02` |
| **englobante** — cobre correção **e** juros (R1) | **SELIC**, **taxa legal** | D8-C22: *"Selic não é índice de inflação"* |

> **As listas do item 4.1.2.4 são exemplificativas — e isso NÃO autoriza estendê-las por
> semelhança de nome.** Classificar o IPCA-E como percentual *"porque IPCA soa percentual"* é a
> dedução que o bloco 17 removeu. **Dez dos vinte e oito ficaram `indeterminado`**, e é resultado
> correto.

**Moeda não é indexador.** Cruzado, cruzeiro, cruzeiro real, real e a conversão em URV entram
como **`nao-indexador`** — que afirma *verificado, e o conceito não se aplica*, fato diferente de
`indeterminado` (*aplica-se, sem fonte*). **Ausência de campo seria indistinguível de esquecimento.**

### Divulgação e oráculos

**Bacen** divulga mensalmente a **taxa legal**, o **Fator Selic_m** e o **Fator IPCA_m**; no
**SGS**, a **série 29541** é o *Fator da Taxa Selic mensal para cálculo da Taxa Legal*. Primeira
taxa legal em **30/08/2024** (aplicável aos dias 30 e 31/08); a partir de set/2024, **primeiro
dia útil** de cada mês. A **Calculadora do Cidadão** do BCB tem módulo de taxa legal e serve como
**oráculo de teste**. **IBGE** para INPC, IPCA, IPCA-E e IPCA-15.
Fonte: `docs/calculo/00-base-normativa.md` § 4, "Divulgação".

---

## Armadilhas conhecidas

**1 — `R3`: trocar nominal por percentual sem ajustar a defasagem.** Desloca **um mês**, sem
sintoma. É por isso que `tipo` é o campo que **não pode faltar**.

**2 — IPCA-E × IPCA: fontes secundárias escrevem "IPCA" nos dois lugares, e estão erradas.**
No trabalhista, **IPCA-E** na fase pré-judicial e **IPCA (sem E)** a partir de 30/08/2024 — a
distinção é do **dispositivo do acórdão** (`calculo-judicial-atualizacao`, Armadilha 5). Um
terceiro nome, **IPCA-15**, é o deflator da taxa legal. **Três índices, três séries.**

**3 — consumir SELIC como correção monetária** (`R1`: conta a inflação duas vezes — observado em
produção, `CalculosService.cs` soma juros à base, `pendencias.md` § 4 itens a–d, **quatro
invariantes no mesmo trecho**) **e implementar a taxa legal por subtração** (`selic − ipca`;
`R11`, e o deflator é o do mês **`m−1`**, não o corrente).

**4 — pedir "o IPCA de nov/2021" e receber 1,17%.** `1,17%` é o **IPCA-E** de nov/2021 na
consolidação de dez/2021; o **INPC** do mesmo mês é **0,84%** e a **TR** trabalhista é
**0,00%**. **Três ramos, três valores, um só mês** (`02-atualizacao-detalhe.md` § 10).

**5 — `A5`, e é o inverso do caso usual:** índice de **dez/10** (`pagina_pdf` 96) impresso como
`1,012012029` **quebra a monotonicidade** da série — é **menor** que o de jan/11. O somatório
do manual fecha com o índice **implícito** (`1,012945924`), não com o impresso. **O erro está no
índice publicado; o valor está certo.** Assinatura para o validador: monotonicidade quebrada em
série de fator acumulado é **suspeita de defeito do publicador**, não de erro de leitura.

**6 — `DEFEITO_DO_ORIGINAL` das moedas:** em `trab.hist.moedas-e-paridades`, a primeira linha
termina em **12/02/70** e a segunda começa em **13/02/67** — **três anos de sobreposição**; quase
certamente era 12/02/67. **Registrado, não corrigido.**

**7 — a Tabela Única do CSJT extraída é a versão baseada na TR.**
`serie-18.15-tabela-unica-trabalhista.csv` traz a tabela com base na **TR**, **declarada
inconstitucional para débitos trabalhistas pela ADC 58**: **registro histórico**, não série
vigente (`bloco-01-tabelas.md` § 7).

**8 — o calendário de 18.14 não serve para contar dias úteis.** **Treze meses impressos com
menos dias do que têm** — conferido na imagem da página. Março de 2017 imprime **27 dias num mês
de 31**, com a coluna inteira de segunda-feira vazia. `dia_da_semana` vem da coluna sob o
cabeçalho do original, **não de cálculo de calendário**, e diverge do real em **42 dias**.

**9 — ruído tipográfico que o validador acusa, e que é do original.** Dígito a mais ou ponto no
lugar da vírgula nos limites de faixa (`De 2.2347,86 até 3.130,51`, `Até 1.1710,78`,
`De 478.78 até 957,56` — **nove ocorrências**, `bloco-01-tabelas.md` § 5.1); e **chamada de nota
de rodapé colada na data** (`04/04/9116`, `Dez/1017`), que faz o validador acusar lacuna de
**1018-01 a 2010-12**. O CSV guarda a **string literal**.

**10 — tolerância do comparador.** Diferenças de **0,01 a 0,03** entre recalculado e impresso
são **esperadas**. **O limiar de alarme não deve ser o centavo.**
Índice completo dos defeitos: `docs/calculo/armadilhas-comparador.md`.

---

## Fixtures de aceite

**1 — taxa legal por razão, variante INPC** — os dois pares da tabela de `R11`
(`pendencias.md` § 2, `PARES_VALIDACAO_INPC`): set/2025 → **1,377047%**; mai/2026 →
**0,277807%**. **A subtração falha nos dois.** **Truncamento, não half-up:** `1,3770478004` →
`1,377047`. Teste em `scripts/calculo/test_valida_taxa_legal.py`.

**2 — soma de série contra atalho do manual** (cadeia da Fazenda trabalhista, `pagina_pdf` 92):
a série (B) de **jun/12 a ago/13** soma **6,5760%**; o atalho do manual é `15 × 0,5% = 7,5%`,
com diferença de **0,9240%**. **Conferido em `Decimal`: fecha exato.**

**3 — integridade do bloco 1**, `python scripts/calculo/valida_bloco_tabelas.py`
(`encoding='utf-8'` explícito em toda leitura). Estado atual reproduzido:
`15 ok, 31 divergências, 1 não verificados, **0 erros**`, exit 0. **Os dez erros eram de
escopo do validador, não de dado, e sumiram no bloco 17** — ver § 5.

**4 — contagens que devem bater exatamente** (`bloco-01-tabelas.md` § 4): 18.8.1 → 560 = 560;
18.8.2 → 1.412 = 1.412; 18.10 URV → 546 = 546; 18.13 → 768 = 768; 18.15 Selic → 264 = 264.

**5 — a contagem que NÃO deve bater, e é fixture disso:** 18.1 grava **149 segmentos** contra
**171** ocorrências de "sim"/"não" no texto, porque a palavra aparece também nas observações em
prosa. **Um validador que force a igualdade aqui está errado.**

---

## Limitações declaradas

**Não é rodapé. É o que impede usar esta skill fora do que ela sustenta.**

### 1. A Tabela Única do CSJT não está integrada — `P9-02`

**É a fonte nacional da cadeia trabalhista, e bloqueia o motor trabalhista.** O capítulo 7 do
Manual TRT-3 **não tem mapa período → indexador de correção**, e diz por quê, literal
(`pagina_pdf` 85):

> *"A tabela mensal de correção está escalonada em meses e anos, já computa as conversões e
> paridades da moeda nacional e não contém juros."*

**A cadeia vive numa série — categoria (B) — e não numa regra.** O segmento
`1942-11 .. 1991-02` grava `indexador: "NAO-DECLARADO-PELO-MANUAL"`, **não "TR"**. **A ponte
para o tronco do CJF não é inferida:** o tronco cobre o período, **mas o corpus não faz a
remissão**.

**Busca negativa, com escopo declarado:** varredura das **dezessete páginas do capítulo 7**
(`pagina_pdf` 83–99) por `IPC`, `IGP`, `INPC`, `expurgo`, `ORTN`, `OTN`, `BTN`, `Ufir`, `42,72`,
`10,14`, `6,17`, `6,92`, `126,8621` — **nenhuma ocorrência**. "IPC" só aparece dentro de
"IPCA-E". **Isto vale para o capítulo 7, não para as 471 páginas.**

### 2. Os dois bloqueios aritméticos — **nenhum é arredondamento**

| | **A3 — p. 266** | **A2 — pp. 269 e 271** |
|---|---|---|
| Delta | **−10,00 exatos** na coluna K (e −0,99 na H) | **−2.036,51** na linha (−11,00 no total) |
| Impresso | total `43.077,24` | `53.199,50`; total `154.874,90` |
| Correto | `43.088,23` | `55.236,01`; total `156.911,41` |
| Por que não é arredondamento | **10,00 exatos não é absorvível**; fechar K exigiria `H = 1.350,52`, que não resulta de operação alguma do exemplo | `53.063,01 × 1,04095137 = 55.236,01`; o índice implícito **`1,00257222` não corresponde a índice algum do exemplo** |

> **O segundo é justamente um índice que não se sabe de onde vem.** `55.236,01` **não existe em
> nenhuma das 471 páginas**; `53.199,50` ocorre **só** nas pp. 269 e 271. Não é cópia de outro
> exemplo, não é transposição, não é arredondamento. **Origem desconhecida.**

### 3. Versionamento de séries — **ausente. Bloqueia R13**

`IndicesSyncService` faz **upsert destrutivo** sobre `IndicesMonetarios`
(`existente.Valor = valor;`). **Sem histórico, sem versão, sem data de coleta.** Hoje, uma
série revisada pelo emissor **altera silenciosamente cálculos já emitidos**, e uma conta não
pode ser reproduzida (`pendencias.md` § 5). **O contrato precisa suportar leitura por versão,
não só por competência** — daí `versao` e `data_de_coleta` marcados `NÃO EXISTE` no Catálogo.

### 4. O que está extraído × o que é dado externo a integrar

| Extraído (evidência de conferência) | Dado externo, **a integrar** |
|---|---|
| OTN/BTN/MVR (18.11), Ufir (18.12), URV (18.10) | **Tabela Única do CSJT vigente** — `P9-02` |
| Tabela Única do CSJT **base TR** (18.15, histórica) | séries correntes de **INPC, IPCA, IPCA-E, IPCA-15** |
| SELIC acumulada (18.15) | **Fator Selic e Fator IPCA do SGS** para a taxa legal |
| faixas de IRRF (até 2015/2017) e de contribuição (até 2017) | **as faixas do art. 85, § 3º, do CPC** — `P8-F4-02` |
| calendários (18.14) — **com os defeitos** | **série histórica de normas coletivas** |

**As faixas do art. 85, § 3º, do CPC são externas.** Busca declarada em toda a árvore `docs/` por
`200 salários`, `1.000 salários`, `2.000 salários`, `20.000 salários`, `100.000 salários` →
**zero**; só existe a regra de progressividade (`pendencias.md`, `P8-F4-02`). **E a série
histórica de normas coletivas também é externa:** o catálogo do repositório guarda **defaults
legais e pisos, não cláusulas de instrumentos** — as cláusulas ficam em `tests/fixtures/calculo/`
e, no uso real, **em dados do cliente** (`tabelas-normativas/README.md`, "Terceira família").

### 5. O que as "31 divergências" significam (e o que foram os "10 erros")

**O script separa erro de extração de divergência do original. Divergência é RESULTADO
ESPERADO.** Não apresentar como falha da skill.

**As 31 divergências são o original:** 13 calendários com dias faltando, 9 limites de faixa com
erro de digitação, sobreposições reais de vigência (jan/10 tem **dois quadros vigentes**;
jun/99, jun/00 e jun/11 mudam de tabela **no meio do mês**, e a checagem trabalha em competência
mensal), rótulos com nota de rodapé colada, e a contagem de 18.1 que **não deve** fechar.

**Os 10 erros eram de ESCOPO, não de dado, e estão corrigidos (bloco 17, tarefa 4).** Todos
apontavam para o mesmo arquivo — `serie-9.2.11-ufir-juros-ate-dez79.csv`, linhas 2 a 11,
*"página 178"*. O validador conferia a proveniência contra `PAGINAS_DO_BLOCO =
range(373, 472)`, constante do bloco 1, enquanto varria `DIR_SERIE.glob("serie-*.csv")` —
**todos** os CSV do diretório. Uma série de bloco posterior caiu no mesmo lugar e foi acusada
de estar fora de 373–471. **`bloco-01-tabelas.md` registra "0 erros de extração"**, e o
registro estava certo **para o escopo dele**. **O dado nunca regrediu; o escopo do validador é
que estava estreito.**

**A constante não existe mais.** A faixa se resolve **por arquivo**, em duas origens: o
`pagina_pdf=` declarado no cabeçalho do próprio CSV, ou o item da linha resolvido no contrato
de páginas do bloco. Arquivo sem nenhuma das duas sai como **não verificável**, nunca como erro
e nunca em silêncio. Saída atual: **15 ok, 31 divergências, 1 não verificado, 0 erros.**
**Consequência para o contrato:** proveniência **exige o intervalo de páginas declarado junto
com a série** — validador com intervalo fixo global não escala para múltiplos blocos.

### 6. Pontos que repousam em fonte secundária ou em inferência

- **A TR foi REBAIXADA a `indeterminado` no bloco 17.** Era `percentual` pelo critério
  **formal** do item 4.1.2.4 — não é unidade monetária, logo é percentual —, mas o critério
  **material** daquele item (*"refletem a inflação do próprio mês"*) **não a alcança**: é taxa
  apurada **prospectivamente** (art. 12, I, da Lei 8.177/91). **Nenhum dos dois manuais a
  classifica.** **Inferência declarada não é fonte** — `P17-02`;
- **Nove índices seguem sem classificação em fonte alguma** (`P17-01`): IPCA, IPCA-E, IPCA-15,
  IPCA série especial, IPC/FGV, IPC-R, IRSM, MVR, e a remuneração básica da poupança. **Não se
  fecha relendo os PDFs** — exige o ato de instituição de cada índice, ou decisão de estender a
  lista do item 4.1.2.4. Até lá, **o validador bloqueia a virada em vez de aprová-la**;
- **a variante IPCA-15 da taxa legal — a regra geral e a de maior uso — está implementada mas SEM
  verificação contra valor publicado.** Os dois pares validados são do caso **INPC**; a
  aritmética é compartilhada e está coberta, falta confirmar que a **série correta** alimenta
  `fator_deflator`. Fecha-se extraindo dois meses do SGS e acrescentando
  `PARES_VALIDACAO_IPCA15` (`pendencias.md` § 2). A tabela de fatores do Bacen reproduzida no
  Manual CJF **não foi extraída como série** — é *"ilustração de método"*;
- **o método de conversão da URV não está no bloco.** As pp. 453–455 trazem título e cotações
  diárias, **e nada mais**: sem procedimento, sem fundamento legal, sem nota. Data-base,
  arredondamento e tratamento de dia não útil **não foram inferidos**.

### 7. O que esta skill NÃO resolve

Cinco pendências abertas, **todas viradas limitação, nenhuma virada regra**: `P9-02` (item 1),
**A2 e A3** (item 2), `pendencias.md` § 5 (item 3), `P8-F4-02` (item 4) e `pendencias.md` § 2
(item 6). **Nenhuma se resolve inventando dado.**

---

## Ponteiros

| Assunto | Onde |
|---|---|
| **R3, R5, R6, R11, R12, R13 — íntegra**; e a distinção (A) × (B) em § 1.1 | `docs/calculo/consolidado/01-dominio-e-invariantes.md` §§ 1.1 e 2 |
| **Quais índices existem, por cadeia**; `P9-02` (§ 6); as réguas de defasagem (§ 7) | `docs/calculo/consolidado/02-atualizacao.md` |
| **Tronco CJF 1964–fev/1991; as quatro `aplicacao` D1–D4** | `docs/calculo/consolidado/02-atualizacao-detalhe.md` §§ 5.1–5.3 |
| **Divulgação, SGS 29541, Calculadora do Cidadão** | `docs/calculo/00-base-normativa.md` § 4 |
| **Formato das séries extraídas, contagens, defeitos do original** | `docs/calculo/extracao/trabalhista/bloco-01-tabelas.md` |
| **O validador — quatro checagens, erro × divergência** | `scripts/calculo/valida_bloco_tabelas.py`; taxa legal em `test_valida_taxa_legal.py` |
| **Defeitos (A1–A15)** · **pendências** · **cadeias em schema** | `armadilhas-comparador.md` · `pendencias.md` · `tabelas-normativas/*.json` |
| **Período → indexador** · **invariantes e aritmética** | `skills/calculo-judicial-atualizacao/` · `skills/calculo-judicial-core/` |

**Sem `references/`:** o arquivo cabe abaixo do limite, e partir a semântica dos índices em dois lugares é exatamente o erro que produz "IPCA" onde deveria estar "IPCA-E".
