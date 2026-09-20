# Tributário federal — e as demais cadeias do CJF

**Manual de Orientação de Procedimentos para os Cálculos na Justiça Federal, CJF, Res.
990/2026.** **Única fonte do corpus cuja edição está vigente.** Governa o tributário federal.
**Não governa o contencioso cível estadual.**

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 5;
`02-atualizacao-detalhe.md` §§ 5.1 a 5.6 e 10; `00-base-normativa.md` §§ 5 e 6;
`extracao/justica-federal/bloco-08-jf.md` e `bloco-08-jf-detalhe.md`;
JSON em `docs/calculo/tabelas-normativas/cjf.*.json`.

**Escopo deste arquivo:** **repetição de indébito** (§ 2) e **dívida fiscal** (§ 3) — as duas
cadeias **tributárias** do Manual. Mais **três seções transversais** a todas as cadeias federais,
que vivem aqui porque não pertencem a nenhuma delas em particular: as **quatro fórmulas de
`aplicacao`** (§ 4), as **ECs 113/2021 e 136/2025** (§ 6), o **precatório** (§ 7) e a
**consolidação de dez/2021 nos cinco lugares** (§ 8).

**Escopo declarado de "cinco ramos do CJF":** o Manual tem **sete cadeias** extraídas (78
segmentos) — **cinco de correção monetária** (condenatórias gerais, previdenciário, repetição de
indébito, desapropriação direta, dívida fiscal) e **duas de juros** autônomas (condenatórias
gerais e trabalhista-JF). Fonte: `bloco-08-jf.md` § 4, `pagina_pdf` 48, 54, 57, 63, 66, 78 e 23.
**Cada um dos demais ramos tem arquivo próprio** — ver o quadro da § 5.

---

## 1. O tronco comum — 1964 a fev/1991

**Quatro cadeias de correção compartilham este tronco, palavra por palavra:** condenatórias
gerais, previdenciário, repetição de indébito e desapropriação.

| Período | Indexador | Observação do manual |
|---|---|---|
| **1964** a fev/1986 | **ORTN** | Lei 4.357/1964 |
| mar/1986 a jan/1989 | **OTN** | débitos anteriores a jan/1989 multiplicados, **neste mês, por 6,17** |
| **jan/1989** | **IPC/IBGE 42,72%** | *"Expurgo, em substituição ao BTN"* |
| **fev/1989** | **IPC/IBGE 10,14%** | idem |
| mar/1989 a mar/1990 | **BTN** | — |
| mar/1990 a fev/1991 | **IPC/IBGE** | *"Expurgo, em substituição ao BTN e ao INPC de fev./1991"* |

**O expurgo SUBSTITUI, não soma** — item 4.1.2.1, `pagina_pdf` 42.

> **A DÍVIDA FISCAL (cap. 2) NÃO TEM ESTE TRONCO.** Ver § 3, e o campo `SEM_EXPURGO` do JSON.

**`R-08-04` e `R3`** — o manual justifica **expressamente** uma sobreposição aparente
(item 2.3.1.3, `pagina_pdf` 25):

> *"O mês de janeiro de 1989 marca o termo final da OTN e o início da BTN. Entretanto, por serem
> indexadores nominais, este fato não implica duplicidade de correção monetária, pois a OTN de
> janeiro serve para definir a inflação de dez./1988, e a BTN de janeiro, comparada com a de
> fevereiro, para fixar a inflação de jan./1989."*

**Vale para todas as cadeias com indexador nominal.** E é a razão de `tipo: nominal | percentual`
ser campo obrigatório.

**A ponta inicial é `ponta_materializada`:** o manual abre com *"De 1964"*, **sem mês**. `1964-01`
é materialização para permitir a checagem de R1/R2 — **pendência `P8-07`**.

---

## 2. Repetição de indébito tributário — `TRIB-FED-REPETICAO`

Item 4.4. **Nunca bifurca por devedor.**

| Período | Indexador |
|---|---|
| 1964-01 .. 1991-02 | **tronco comum** (§ 1) |
| 1991-03 .. 1991-11 | INPC/IBGE |
| 1991-12 | IPCA **série especial** |
| 1992-01 .. 1996-01 | **Ufir** |
| **1996-01 → ** | **SELIC — engloba correção E juros** |

**Fundamento da SELIC:** art. 39, § 4º, da **Lei 9.250/1995**.

**Juros:** **1% simples até 31/12/1995**; **SELIC a partir de 1º/01/1996**.

**Termo inicial dos juros: TRÂNSITO EM JULGADO** — CTN art. 167, § único. **`R7`: não é a citação
nem o ajuizamento.**

**`aplicacao` = D3** — do mês seguinte ao **recolhimento indevido** até o mês anterior à
repetição, **e 1% no mês**. **O eixo é o recolhimento indevido**, não a competência da parcela.

**`R-08-13` — a repetição de indébito NÃO consolida em dez/2021.** Literal, `pagina_pdf` 64:
*"não altera o cálculo [...] sendo, portanto, desnecessário consolidar"* — porque **já observa a
SELIC desde jan/1996**. É a **única dispensa** entre os seis ramos (ver § 8).

**Defeito do original registrado:** o manual escreve *"A partir de jan./1996"* enquanto a linha
anterior termina **em jan./1996** — **sobreposição de um mês no impresso**, preservada no JSON.

---

## 3. Dívida fiscal — `TRIB-FED-DIVIDA-ATIVA`

Item 2.3.1.2, `pagina_pdf` 23–24. **A cadeia mais atípica do manual.**

| Período | Indexador | Nota |
|---|---|---|
| 1964-01 .. 1986-02 | **ORTN** | `ponta_materializada` no início |
| 1986-03 .. 1989-01 | **OTN** | multiplicador de transição em jan/1989: **6,92 para o IR**, **6,17 para o II** |
| 1989-01 .. 1991-01 | **BTN** | *"O último BTN corresponde a **126,8621**"*. **`SEM_EXPURGO`** |
| **1991-02 .. 1991-12** | **nenhum** | *"Não há correção monetária, somente juros de mora equivalentes à **TRD**"* (item 2.3.2.2) |
| 1992-01 → | **Ufir → SELIC, bifurcado pelo `data-do-fato-gerador`** | ver abaixo |

### 3.1 Os dois desvios em relação às demais cadeias

**(a) Sem tronco e sem expurgo.** *"Ao contrário do capítulo 4, a dívida fiscal **NÃO** substitui
o BTN pelos expurgos de jan./1989 e fev./1989."* — atrito **N-4**. E o multiplicador de jan/1989
é **duplo** (6,92 / 6,17), contra o **6,17 único** das demais.

**(b) Uma janela inteira sem correção monetária** — `1991-02 .. 1991-12`, só juros pela TRD.

### 3.2 A bifurcação por **fato gerador** — regra literal

> *"Para fatos geradores ocorridos: a) **Até 31/12/1994**: I. Até jan./1997: Ufir; II. A partir de
> jan./97: taxa Selic, até o mês anterior ao pagamento; 1% no mês do pagamento. b) **A partir de
> jan./1995**: I. De jan./95 a mar./1995: **TMMCTN**; II. A partir de abr./1995: taxa Selic até o
> mês anterior ao pagamento; 1% no mês do pagamento."*

**O eixo é `data-do-fato-gerador`**, declarado em `dominio_condicoes`. **Não é a competência da
parcela, não é o ajuizamento.** Dois débitos do mesmo devedor, atualizados no mesmo mês, seguem
indexadores diferentes conforme o fato gerador.

`dominio_condicoes` **declara que os dois ramos ESGOTAM o eixo** — sem essa declaração o
validador cobraria o universo *"nenhuma condição se aplica"*, porque **exaustividade se declara,
não se presume** (**R2**).

**`aplicacao` = D4** — do mês seguinte à **competência da parcela** até o mês anterior ao
pagamento, e 1% no mês.

### 3.3 Duas especificidades da contribuição previdenciária **na dívida fiscal**

Item 2.4.2, `pagina_pdf` 30–33. **Não confundir com `previdenciario.md`**, que é a cadeia de
**benefícios**.

- **o IR entra na SELIC em jan./1997; a contribuição previdenciária, em abr./1997**, com **dois
  meses de vácuo**: *"II. De fev./1997 a mar./1997: **sem correção monetária**; III. A partir de
  abr./1997: taxa Selic..."*;
- **base dos juros sobre multas** (item 2.4.1, `pagina_pdf` 30): *"As multas assim calculadas são
  acrescidas de juros de 1% **sobre o valor originário**. A partir do **Decreto-Lei n.
  2.323/1987** (art. 16), calculam-se os juros **sobre o valor corrigido**."*

**FGTS na dívida fiscal** (item 2.4.4.1, `pagina_pdf` 35–36) — cadeia **em forma de lista, não de
tabela**: conversão em **BTNF em 1º/11/1989**, juros de 1% simples e multa de 20%; conversão dos
BTN em cruzeiros em **1º/2/1991, multiplicando por 126,8621**; índices mensais aplicados **de
forma trimestral**, multiplicados por **1,0075** (taxa mínima, capitalização de 3% ao ano).

**`D8-C6` — um mês sem juros por falta de lei:** **3 a 31 de janeiro de 1992**. **Declarado, não
inferido.**

**`D8-C7` — pendência:** a abreviação **"cor/mon."** aparece **treze vezes** (`pagina_pdf` 26, 32,
33, 91 e 92) e **nunca é definida**.

---

## 4. As quatro fórmulas de `aplicacao`

| # | Regra | Onde |
|---|---|---|
| **D1** | Selic **no mês posterior ao de sua competência, inclusive no mês de pagamento**. *Ex.: a Selic de dez./2021 é computada em jan./2022* | Fazenda, a partir de dez/2021. **A taxa legal segue D1** (item 4.2.2, NOTA 7) |
| **D2** | Selic **do mês seguinte ao termo inicial dos juros até o mês anterior ao pagamento, e 1% no mês do pagamento** | não-Fazenda; e Fazenda de jan/03 a jun/09 |
| **D3** | do mês seguinte ao **recolhimento indevido** até o mês anterior à repetição, e 1% no mês | repetição de indébito |
| **D4** | do mês seguinte à **competência da parcela** até o mês anterior ao pagamento, e 1% no mês | dívida fiscal |

> **D1 e D2 dão resultados diferentes sobre a MESMA série.** D2 ignora a Selic do mês de
> pagamento e a substitui por **1% fixo**. A mesma Selic, dois números.

---

## 5. As demais cadeias do CJF — **cada uma tem arquivo próprio**

**Migradas no bloco 17.** As cadeias de **condenatórias gerais** e de **desapropriação** estavam
alojadas aqui por falta de arquivo na divisão de seis fixada pelo bloco 16. **A lacuna foi
fechada** — `bloco-16-relatorio.md` § 6. **Não há mais conteúdo normativo dessas matérias neste
arquivo.**

| Cadeia | Item do Manual | Onde está agora |
|---|---|---|
| **Condenatórias em geral** — correção (15 segmentos) e **juros autônomos** (11 segmentos); tronco comum; bifurca em **dez/2021** (correção) e **jul/2009** (juros), **reconverge em set/2025** nos dois; o **ramo paralelo `N-8`** dos servidores e empregados públicos | 4.2.1.1 · 4.2.2 | **`references/civel-federal.md`** §§ 2 e 3 |
| **Desapropriação** direta e indireta — **três cadeias autônomas**: correção (com o **IPC/FGV** exclusivo), juros de mora (eixo na **data da sentença**) e **juros compensatórios** (`D8-C10`, os três cortes, `N-6`, `N-10`, `R-08-19`) | 4.5 · 4.6 | **`references/desapropriacao.md`** §§ 2, 3 e 4 |
| **Benefícios previdenciários** — 15 segmentos, **nunca bifurca**, taxa legal com deflator **INPC** | 4.3 | `references/previdenciario.md` |
| **Trabalhista da Justiça Federal** — `cjf.trabalhista.juros-mora`, com a **`R4-EXCEÇÃO`** | 4.7.2 | `references/trabalhista-nacional.md` § 6, e § 5.1 abaixo |

> **O benefício ASSISTENCIAL não segue a cadeia previdenciária:** segue a das **condenatórias em
> geral** (item 4.2.1.1) — e **aquela bifurca por devedor**, enquanto a previdenciária não.
> `previdenciario.md` § 5; `civel-federal.md` § 6.

### 5.1 A cadeia trabalhista **da Justiça Federal**

`cjf.trabalhista.juros-mora` (item 4.7.2) **bifurca em ago/2001 e NUNCA reconverge** — o ramo
**empresa pública / prestador de serviços** segue em **1,0% a.m.** até o fim da janela. Traz a
**`R4-EXCEÇÃO`**: **1,0% COMPOSTA, mar/1987 a mar/1991** (DL 2.322/87). Quadro completo em
`references/trabalhista-nacional.md` § 6.

**`R-08-08` — a bifurcação por devedor NÃO é universal:** **três cadeias nunca bifurcam** —
previdenciário, repetição de indébito e **desapropriação direta**. **A dívida fiscal bifurca, mas
por `data-do-fato-gerador`, não por devedor** (§ 3.2) — e é a única assim.

---

## 6. EC 113/2021 e EC 136/2025 — `C14-01`, `SUPERADO`

### 6.1 A redação original da EC 113/2021 NÃO era "só federal"

> *"Nas discussões e nas condenações que envolvam a Fazenda Pública, **independentemente de sua
> natureza** e para fins de atualização monetária, de remuneração do capital e de compensação da
> mora, inclusive do precatório, haverá a incidência, **uma única vez**, até o efetivo pagamento,
> do índice da taxa referencial do Sistema Especial de Liquidação e de Custódia (Selic),
> acumulado mensalmente."*

> **Refutação registrada, e a fonte do erro é INTERNA.**
> `bloco-13c-sindical-precatorios.md` § 7 afirma que a EC 113/2021 alcançava **apenas
> requisitórios federais**. **Está errado** — a redação original **não tem a palavra "federal"**.
> **A restrição é criação da EC 136/2025.** Não corrigido na base; registrado aqui. **Não repetir
> o erro.**

### 6.2 A redação nova — EC 136/2025, promulgada em **09/09/2025**

> *"Nos **requisitórios** que envolvam a Fazenda Pública **federal**, **a partir da sua
> expedição** até o efetivo pagamento, a atualização monetária será feita pela variação do
> **IPCA**, e, para fins de compensação da mora, incidirão **juros simples de 2% a.a.**"*

**Trava:** se a soma da atualização com os juros **superar a SELIC** no mesmo período, **aplica-se
a SELIC** em substituição.

**Três estreitamentos simultâneos — e é por isso que o eixo é triplo:**

| Eixo | Antes | Depois |
|---|---|---|
| **Objeto** | discussões e condenações | **só requisitórios** |
| **Ente** | toda Fazenda Pública | **só Fazenda Pública federal** |
| **Período** | do início até o pagamento | **da expedição** até o pagamento |

**Regra de incidência — CNJ, Provimento 207/2025 — ASSIMÉTRICA:** o **IPCA** incide sobre
**principal e juros somados**; os **2% a.a.** incidem sobre o **principal, excluídos os juros já
apurados**. **É especificação de implementação e NÃO decorre da leitura da emenda.**

### 6.3 Fase pré-requisitório — vácuo preenchido pelo CC

- **STJ, REsp 2.236.270/SP** (Rel. Min. Gurgel de Faria, pub. 02/03/2026): a nova redação
  restringe-se **exclusivamente aos requisitórios**; na fase de conhecimento aplica-se o **art.
  406 do CC**;
- **STF, ARE 1.557.312/SP** (Tema 1.419);
- **CJF, Res. 990/2026** encerra a SELIC na fase pré-requisitório **a partir de set/2025**,
  aplicando **IPCA** para correção e **taxa legal** para juros. **Previdenciário mantém INPC e
  taxa legal com dedução do INPC.**

### 6.4 Instabilidades — registradas, não resolvidas

- **ADI 7873** questiona a emenda. **Pendente**;
- **TJ-SP, 2ª Câmara de Direito Público** (AI 3001155-79.2026.8.26.0000) **mantém a SELIC** para
  débitos não submetidos à fase de precatório, aplicando a EC 136 **apenas após a expedição do
  requisitório** — **contra** a Res. CJF 990/2026 e o STJ. **As duas posições entram**;
- **Fazenda estadual e municipal:** ficam **sem a regra antiga** (revogada) e **sem a nova** (que
  não as alcança). **Vácuo normativo — lacuna de LEGISLAÇÃO, não de pesquisa.**

---

## 7. Precatório — `C14-02`, `BIFURCADO`, e `C14-03`, `INAPLICÁVEL`

**Eixo: expedição do requisitório ⊕ ente devedor.**

**Sobrevivem QUATRO regras estruturais do cap. 14**, independentes da EC 62/2009 e não tocadas
pelas ECs 113 e 136:

1. **suspensão dos juros** no prazo constitucional de pagamento;
2. **juros de 0,5% a.m. desde ago/2001**;
3. **exclusão de juros compensatórios**;
4. **exceção à precedência do título**.

**NÃO sobrevive o índice.**

**Data de apresentação do precatório:** **1º de julho até 2021**; **2 de abril a partir de 2022**.

**`R-08-17` — no requisitório complementar o indexador troca TRÊS vezes:** original até a
apresentação → **administrativo** no prazo constitucional → **novamente o original** depois.
**Governada pelo ESTADO DA REQUISIÇÃO, não pela competência** (`pagina_pdf` 89).

**`C14-03` — `INAPLICÁVEL` por prejudicialidade, razão declarada:** depende de **classificar a
devedora como Fazenda Pública**, que é **determinação jurídica do usuário do módulo**, não
matéria de cálculo. **`C14-01` e `C14-02` são condicionais a ela.** **Busca declarada:**
`economia mista` tem **zero ocorrências nas 471 páginas** do manual trabalhista; a única
equiparação nominada é a **ECT**, e só *"para efeito de execução e do DL 779/1969"*.

---

## 8. Consolidação de dez/2021 — **cinco lugares, três valores de fechamento**

Literal, `pagina_pdf` 50 (repetido com redação quase idêntica em **59, 67, 74 e 79**):

> *"a) o crédito será consolidado tendo por base o mês de dez./2021 pelos critérios de juros e
> correção monetária até então aplicáveis, considerando, para esse fim, o [índice] de nov./2021
> ([x]%) e os **juros de dez./2021 (0,4412%)**; b) sobre o valor consolidado do crédito em
> dez./2021, **sem exclusão de qualquer parcela**, incidirá a taxa Selic a partir de jan./2022
> (competência dez./2021) (§ 1º do art. 22 da Res. CNJ n. 303/2019, com redação dada pelo art. 6º
> da Res. CNJ n. 448/2022); c) o valor resultante [...] denominado 'Juros Selic', deve ser
> **integralmente somado à parcela denominada 'Juros até 12/2021'**."*

| Ramo | Índice de nov/2021 | Valor | Juros de dez/2021 | Item | `pagina_pdf` |
|---|---|---|---|---|---|
| Condenatórias em geral | IPCA-E | **1,17%** | 0,4412% | 4.2.1, NOTA 5 | **50** |
| Benefícios previdenciários | INPC | **0,84%** | 0,4412% | 4.3.1, NOTA 5 | **59** |
| Desapropriação **direta** | IPCA-E | **1,17%** | 0,4412% | 4.5.1.1, NOTA 2 | **67** |
| Desapropriação **indireta** | IPCA-E | **1,17%** | 0,4412% | 4.6.1.1, NOTA 2 | **74** |
| Ações trabalhistas (JF) | **TR** | **0,00%** | 0,4412% | 4.7.2, NOTA 2 | **79** |
| **Repetição de indébito** | — | **não consolida** | — | 4.4.1.1, NOTA 4 | 64 |

**`R-08-12`** — os juros de dez/2021 são os **mesmos (0,4412%) nos cinco**; **o índice assume três
valores**. **A TR trabalhista de 0,00% significa que, nesse ramo, o principal não se move em
nov/2021.**

**`R-08-14` — "sem exclusão de qualquer parcela":** a SELIC incide sobre o consolidado **inteiro,
principal E juros**. Nos exemplos da `pagina_pdf` 51 há duas linhas de dez/2021 — principal
corrigido **R$ 2.275,96** e juros **R$ 55,75** — **ambas recebendo 5,05% de Selic**.

> **Verificação por varredura:** `0,4412` ocorre nas páginas **50, 59, 67, 74 e 79**. A primeira
> redação do bloco 08 listava **quatro** lugares e três ramos; **são cinco** — as duas
> desapropriações ficaram de fora.

---

## 9. Invariantes que mordem com força nesta jurisdição

- **`R1`** — SELIC e taxa legal **englobam**. A repetição de indébito é o caso extremo: **um único
  segmento desde jan/1996** cobrindo correção e juros. Não há o que somar;
- **`R2`** — a exaustividade dos ramos da dívida fiscal é **declarada** em `dominio_condicoes`.
  Sem a declaração, o validador cobra o universo *"nenhuma condição se aplica"*;
- **`R3`** — o tronco é quase todo de índices **nominais** (ORTN, OTN, BTN, Ufir); as pontas são
  **percentuais** (INPC, IPCA). **Cada virada entre tipos exige ajuste de defasagem**;
- **`R5`** — **o piso nominal é POR PARCELA**, não sobre o total: *"considerada cada parcela do
  principal"* (item 4.1.2.2, `pagina_pdf` 42). Fundamento: **REsp 1.265.580**;
- **`R7`** — repetição de indébito: **trânsito em julgado**;
- **`R8`** — **única exceção registrada** (`R-08-01`, NOTA 2): **mudança superveniente de
  legislação sobre o indexador passa por cima do título**;
- **`R12`** — **truncamento**, não arredondamento: *"são inerentes ao critério de truncamento de
  casas decimais aplicado em cada etapa do cálculo"* (`pagina_pdf` 53).

---

## 10. Limitações declaradas

1. **`D8-C7`** — *"cor/mon."* nunca definida, **treze ocorrências** (`pagina_pdf` 26, 32, 33, 91
   e 92);
2. **`D8-C6`** — **um mês sem juros por falta de lei**: 3 a 31 de janeiro de 1992. **Declarado,
   não inferido**;
3. **`D8-C8`** — no FGTS da dívida fiscal, **maio/2000 pertence a dois intervalos** (*"De
   fev./1991 a maio/2000"* × *"A partir de maio/2000"*), **sem regra de desempate**, e o item
   2.4.4.2 usa fronteira diferente para o mesmo tema;
4. **`D8-D03`/`N-3`** — os rótulos **ORTN/OTN estão invertidos** nos itens 2.3.1.1 e 4.4.1 em
   relação às tabelas. **Registrado, não corrigido**;
5. **Fazenda estadual e municipal pós-EC 136/2025** — **lacuna normativa**, não de pesquisa;
6. **ADI 7873** pendente; **divergência do TJ-SP** registrada e **não arbitrada**;
7. **A classificação da devedora como Fazenda Pública é pergunta ao jurídico do usuário do
   módulo.** Se a resposta for negativa, **somem do escopo** o ramo FP das três jurisdições, o
   precatório, as ECs 113/136 e a consolidação de dez/2021;
8. **As pendências das cadeias migradas seguem abertas nos arquivos que as receberam** — `N-8`
   (ramo paralelo dos servidores) em `civel-federal.md` § 11; **`P8-09`** (dez/2021 dos juros
   compensatórios), **`N-10`** (remissão errada em 4.6.3) e os **honorários de perito de 4.5.6**
   em `desapropriacao.md` § 10. **Migraram de lugar, não de estado: continuam pendências**;
9. **As séries (Ufir, BTN, OTN, ORTN, IPCA-E, IPCA-15, TMMCTN) não estão aqui.** São
   dado (B) — `skills/indices-judiciais/`. A única tabela numérica que o manual **reproduz** é o
   quadro da **taxa legal previdenciária** de set./2025 a jun./2026 (`pagina_pdf` 61), e **não foi
   extraída como série** porque é **ilustração de metodologia**, não a série em si.

---

## 11. Ponteiros

- `docs/calculo/consolidado/02-atualizacao-detalhe.md` §§ 5.1–5.6 e 10 — segmento a segmento
- `docs/calculo/extracao/justica-federal/bloco-08-jf.md` e `bloco-08-jf-detalhe.md` — as sete
  cadeias linha a linha, notas × linhas, defeitos do original
- `docs/calculo/tabelas-normativas/cjf.*.json` — as cadeias em schema `cadeia-temporal`
- **`references/civel-federal.md`** — **condenatórias em geral** (correção e juros autônomos),
  migrada no bloco 17
- **`references/desapropriacao.md`** — **desapropriação direta e indireta**, com as **três
  cadeias** e os **juros compensatórios**, migrada no bloco 17
- `references/previdenciario.md` — benefícios previdenciários
- `references/trabalhista-nacional.md` § 6 — `cjf.trabalhista.juros-mora`
