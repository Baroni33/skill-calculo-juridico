# Desapropriação — direta e indireta, cadeia do CJF

Correção monetária, juros de mora e **juros compensatórios** nas desapropriações na Justiça
Federal. Itens **4.5** (direta) e **4.6** (indireta) do **Manual de Orientação de Procedimentos
para os Cálculos na Justiça Federal, CJF, Res. 990/2026**.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 5;
`consolidado/02-atualizacao-detalhe.md` §§ 5.1, 5.2, **5.3.1** e 10;
`docs/calculo/extracao/justica-federal/bloco-08-jf.md` §§ 4, 5, 6 e 7 e
`bloco-08-jf-detalhe.md` §§ 3.1, 3.1.1, 4, 5 e 6;
`docs/calculo/consolidado/06-encargos.md` § 8.1;
`skills/calculo-judicial-atualizacao/regras/cjf.desapropriacao-direta.correcao-monetaria.json` (11 segmentos),
`cjf.desapropriacao-indireta.correcao-monetaria.json` (11), `cjf.desapropriacao-direta.juros-compensatorios.json` (3)
e `cjf.desapropriacao-indireta.juros-compensatorios.json` (3) — as três últimas **geradas no bloco 19,
tarefa 3**; ver `consolidado/02-atualizacao-detalhe.md` **§ 5.3.6**.

---

## 0. A advertência que justifica este arquivo existir

> ### **SÃO TRÊS CADEIAS AUTÔNOMAS, NÃO UMA.**
>
> **Correção monetária** (§ 2) · **juros de mora** (§ 3) · **juros compensatórios** (§ 4).
>
> **Quem tratar a desapropriação só pela linha de correção monetária PERDE UMA CADEIA INTEIRA.**
> Foi exatamente o que aconteceu no **bloco 15**: a espinha consolidada listou a desapropriação
> entre os cinco ramos de correção e **os compensatórios ficaram de fora**, recuperados só no
> detalhe (`02-atualizacao-detalhe.md` § 5.3.1).

E há um segundo alerta da mesma família: na **consolidação de dez/2021**, a primeira redação do
bloco 08 listava **quatro** lugares e três ramos; **são cinco** — **as duas desapropriações
ficaram de fora** e foram recuperadas por varredura de `0,4412` (§ 6). **A desapropriação é a
matéria que este corpus mais vezes esqueceu.**

---

## 1. O tronco comum — 1964 a fev/1991

**Quatro cadeias de correção compartilham este tronco, palavra por palavra:** condenatórias
gerais, previdenciário, repetição de indébito e **desapropriação**.

| Período | Indexador | Observação do manual |
|---|---|---|
| **1964** a fev/1986 | **ORTN** | Lei 4.357/1964 |
| mar/1986 a jan/1989 | **OTN** | débitos anteriores a jan/1989 multiplicados, **neste mês, por 6,17** |
| **jan/1989** | **IPC/IBGE 42,72%** | *"Expurgo, em substituição ao BTN"* |
| **fev/1989** | **IPC/IBGE 10,14%** | idem |
| mar/1989 a mar/1990 | **BTN** | — |
| mar/1990 a fev/1991 | **IPC/IBGE** | *"Expurgo, em substituição ao BTN e ao INPC de fev./1991"* |

**O expurgo SUBSTITUI, não soma** — item 4.1.2.1, `pagina_pdf` 42 (`R-08-05`).
**A dívida fiscal (cap. 2) NÃO tem este tronco** — `references/tributario-federal.md` § 3.

**`ponta_materializada` no início:** o manual abre com *"De 1964"*, **sem mês**. `1964-01` é
materialização de janela, **não afirmação do manual** — **`P8-07`**.

---

## 2. Primeira cadeia — CORREÇÃO MONETÁRIA (itens 4.5.1.1 e 4.6.1.1)

**As tabelas de 4.5.1.1 (`pagina_pdf` 66) e 4.6.1.1 (`pagina_pdf` 72–73) são IDÊNTICAS.**
O que muda entre direta e indireta é o **termo inicial** e os **juros**.

**Nunca bifurca por qualidade do devedor** — `R-08-08`.

| Período | Indexador |
|---|---|
| 1964-01 .. 1991-02 | **tronco comum** (§ 1) |
| **1991-03 .. 1991-12** | **IPC/FGV** — **índice EXCLUSIVO desta cadeia** |
| 1992-01 .. 2000-12 | **Ufir** |
| 2001-01 .. **2021-11** | **IPCA-E/IBGE** |
| **2021-12 .. 2025-08** | **SELIC** — art. 3º da EC 113/2021. **Engloba correção E juros** (R1) |
| **a partir de 2025-09** | **IPCA-15/IBGE** — ARE 1.557.312/SP (Tema 1.419 do STF), CC art. 389, § único |

### 2.1 O IPC/FGV é o único índice exclusivo de uma cadeia em todo o capítulo 4

`bloco-08-jf.md` § 4.1, literal: a desapropriação *"diverge com um índice que nenhuma outra cadeia
usa: **IPC/FGV**, de mar./1991 a dez./1991 (`pagina_pdf: 66`, e a gêmea 4.6.1.1 na `73`). É o único
índice exclusivo de uma cadeia em todo o capítulo 4, e **a primeira extração o gravou como INPC** —
erro corrigido pela validação adversarial."*

> **Um motor que resolva a cadeia por "o que as outras fazem depois de fev/1991" grava INPC aqui e
> erra dez meses.** O erro já aconteceu uma vez neste repositório.

### 2.2 Termo inicial da correção — e a assimetria `N-12`

| | Direta (4.5) | Indireta (4.6) |
|---|---|---|
| **Correção** | data do **laudo do perito** — **Súmula 75 do TFR** | data do **laudo de avaliação** — Súmula 75 do TFR |

Literal do JSON de cadeia: *"A correção monetária é contada a partir da data do laudo do perito
(Súmula n. 75 do TFR)."*

**`N-12` — ausência assimétrica, registrada:** o item **4.5.1** traz a **NOTA** com o termo inicial
(`pagina_pdf` 66); o item **4.6.1** **não tem nota equivalente** (`pagina_pdf` 72), e o manual usa
**três grafias do mesmo conceito**. `bloco-08-jf-detalhe.md` § 4.

---

## 3. Segunda cadeia — JUROS DE MORA (itens 4.5.2 e 4.6.2)

**Cadeia própria, com eixo de corte próprio: a DATA DA SENTENÇA.**

| Corte | Literal | `pagina_pdf` |
|---|---|---|
| **26/9/1999 ÷ 27/9/1999** | *"no caso de sentença proferida até 26/9/1999"* | **68** (direta) e **75** (indireta) |

> **Este eixo não é a competência da parcela.** É o **fato do processo "data da sentença"**, e não
> aparece em nenhuma outra cadeia do capítulo 4. Passo 0 do procedimento: **a chave é o par
> `(data, eixo)`**, não a data.

**A partir de maio/2012** os itens 4.5.2 e 4.6.2 aplicam a **fórmula da poupança por
COMPETÊNCIA** — e é aqui que mora a armadilha `D8-C16`:

> **Mesmo cálculo, eixos diferentes.** A poupança do item **4.9.2** corta por **data de abertura
> da conta** (NOTA 2, `pagina_pdf` 86: *"contas abertas a partir de maio/2012"*); a de **4.5.2 e
> 4.6.2** corta por **competência**. Trocar um eixo pelo outro muda quais parcelas entram.

**A partir de dez/2021 os juros de mora são SELIC** — e é a esta linha que os compensatórios
remetem ao desaparecer (§ 4.3).

> **Escopo declarado desta seção.** O corpus registra desta cadeia **o eixo de corte
> (26/9/1999 ÷ 27/9/1999)**, a **fórmula da poupança a partir de maio/2012 por competência**, a
> **Selic a partir de dez/2021** e os **defeitos do original** do § 7. **A tabela de 4.5.2/4.6.2
> não foi extraída linha a linha para `tabelas-normativas/`** — as sete cadeias extraídas são as
> do § 4 de `bloco-08-jf.md`, e nenhuma delas é `desapropriacao.*.juros-mora`. **Não infiro os
> segmentos ausentes.**

**Atritos do próprio manual nesta cadeia:**

- **`N-7` — autorreferência.** A NOTA 1, "a", do item 4.2.2 (*"vedada sua incidência cumulada com
  os juros de mora"*) qualifica uma linha que **é de juros de mora**. **Boilerplate copiado da
  seção de correção**, e ele **se repete em 4.6.2**, 4.8.3 e 4.9.3;
- **sobreposição de dez/2021 na INDIRETA**, que a checagem automática não pega porque as linhas
  estão em tabelas diferentes: na **indireta**, a linha da poupança fecha em **"dez./2021"** e a da
  Selic abre em **"De dez./2021"** (`pagina_pdf` 74–75); na **direta**, com **fundamento
  idêntico**, a linha fecha em **"nov./2021"**. `bloco-08-jf-detalhe.md` § 5.

---

## 4. Terceira cadeia — JUROS COMPENSATÓRIOS (itens 4.5.3 e 4.6.3)

**É cadeia autônoma, além da correção e dos juros de mora — e desde o bloco 19, tarefa 3, tem JSON:**
`cjf.desapropriacao-direta.juros-compensatorios.json` e `...-indireta...` (3 segmentos cada).

> **ESCOPO DECLARADO DO JSON.** Os **períodos**, os **fundamentos** e os **três cortes** vieram da
> fonte. **As TAXAS das duas primeiras linhas NÃO estão na fonte extraída** e ficaram `taxa: null`,
> com o campo `taxa_nao_extraida` dizendo por quê. **Nenhum número foi inventado**, e o buraco está
> num arquivo que o validador lê — prosa não é lida pelo validador. Os **quatro** da tabela viraram
> **três** segmentos: as duas linhas de dez/2021 em diante têm a **mesma** observação e a extração
> **não transcreve onde uma termina e a outra começa**; arbitrar a fronteira seria inventar.

### 4.1 `D8-C10` — mesma súmula, DOIS termos iniciais

| | Direta (4.5) | Indireta (4.6) |
|---|---|---|
| **Compensatórios** | data da **imissão da posse**, **certificada no mandado** | data da **efetiva ocupação** do imóvel |

**Ambos por Súmula 69 do STJ.** Literal (`bloco-08-jf-detalhe.md` § 3.1): direta — *"a partir da
data da imissão da posse (Súmula n. 69 do STJ) certificada no mandado"*; indireta — *"a partir da
data da efetiva ocupação do imóvel (Súmula n. 69 do STJ)"*.

> **Não é defeito. Não há imissão na desapropriação indireta.** Mas **é bifurcação**, e o **eixo é
> a MODALIDADE da desapropriação — não uma data** —, e o schema precisa registrá-la.

**Consequência para o motor:** a resolução desta cadeia exige, antes de qualquer competência, o
atributo `modalidade ∈ {direta, indireta}`. Sem ele **não há termo inicial**.

### 4.2 Os três cortes no tempo — e **DOIS não aparecem em tabela nenhuma**

| Corte | O que muda | Fundamento |
|---|---|---|
| **10/6/1997 ÷ 11/6/1997** | a tabela vai *"Até 10/6/1997"* e *"De 11/6/1997 a nov./2021"* | **MP 1.577/1997** e sucessivas; **ADI 2332** citada nas observações |
| **ago./2017** | os compensatórios **deixam de seguir 4.5.3** e passam ao **percentual fixado para os TDAs depositados como oferta inicial** | art. 5º, § 9º, da **Lei 8.629/1993**, na redação da **Lei 13.465/2017** — item **4.5.4**, `pagina_pdf` 70 |
| **dez./2021** | **o regime autônomo acaba** — literal: *"Já incluídos na SELIC aplicada aos juros de mora"*. **Sem taxa adicional** | **`D8-C11`** |

**`D8-C25` — o corte de ago./2017 vive SÓ no item 4.5.4, sobre TDAs complementares. NENHUMA TABELA
O MOSTRA.** Literal do item 4.5.4, `pagina_pdf` 70:

> *"A conversão em TDAs complementares deverá ser efetuada **com base na data da respectiva conta
> de atualização**. A conta de atualização deverá abranger a correção monetária com base nos
> índices referidos no item 4.5.1, **desde a data do laudo**, além de juros de mora [...] e de
> juros compensatórios [...] **até julho de 2017**, e, a partir agosto de 2017, **em percentual
> correspondente ao fixado para os TDAs depositados como oferta inicial** (art. 5, § 9º, da Lei n.
> 8.629/1993, com alterações da Lei n. 13.465/2017)."*

**NOTA 1 do mesmo item:** havendo **imissão prévia**, os compensatórios incidem *"sobre a diferença
entre o valor fixado na sentença e o preço ofertado em juízo"* — **é regra de BASE, não de taxa**.

> É o padrão de `consolidado/07-leitura-do-corpus.md` § 1 — regra que vive fora da tabela —
> **aplicado a uma cadeia inteira**.

**O terceiro corte é o de dez/2021, e ele é o fim da cadeia:** a partir dali os compensatórios
**não têm taxa própria**; estão *"já incluídos na SELIC aplicada aos juros de mora"*. **Somar
compensatórios à Selic depois de dez/2021 é dupla contagem** — é `R1` aplicada a esta cadeia.

### 4.3 `N-6` — a contradição de UM MÊS, **não harmonizada**

| Onde | O que diz |
|---|---|
| **Texto** de 4.5.3, `pagina_pdf` **69** | *"**Até dez. 2021**, os juros compensatórios incidem:"* |
| **Tabela** de 4.5.3 | encerra o regime autônomo em **nov./2021** |

**Fundamento idêntico nas duas cadeias gêmeas.** **Dez./2021 fica sem regime coerente** — e é
justamente **o mês da consolidação da EC 113/2021**.

> **`P8-09` — pendência aberta, NÃO harmonizada.** Não se escolhe lado aqui. As duas leituras
> entram, e a conta que atravesse dez/2021 **grava qual aplicou** (R19). Resolver por inferência
> seria criar regra onde o corpus registra atrito.

A grafia *"Até dez. 2021"* é ela própria um defeito catalogado — **`D8-D23`**: fora do padrão
*"dez./2021"* do manual **e** em conflito com a linha de nov./2021.

### 4.4 `N-10` — a remissão errada, registrada e **não corrigida**

Em **4.6.3** (desapropriação **indireta**), as **duas linhas** de dez/2021 em diante remetem ao
*"item **4.5.2**"* — que é da desapropriação **direta** (`pagina_pdf` 76). **`D8-D15`**, duas
ocorrências.

> **O motor deve ler a remissão como apontando para 4.6.2**, o item de juros de mora da própria
> indireta — **e registrar que o fez**. **Isto é leitura declarada, não correção do original:** o
> defeito fica catalogado, o texto não se altera (`armadilhas-comparador.md`).

### 4.5 Juros COMPOSTOS: o manual proíbe aqui e prescreve noutro item

`pagina_pdf` 71, tratando dos juros compensatórios: **"vedado o cálculo de juros compostos"**
(art. 5º, § 9º, da Lei 8.629/1993).

**O mesmo documento prescreve capitalização composta em `cjf.trabalhista.juros-mora`** — linha
*"De mar./1987 a mar./1991 — 1,0% — **composta**"*, art. 3º do DL 2.322/1987 (`pagina_pdf` 78,
**`D8-C18`**, a **`R4-EXCEÇÃO`** do projeto). **O contraste é do original.** Aqui, nesta cadeia,
**vale a vedação**: compensatórios são **simples**.

---

## 5. `R-08-19` — não cabem compensatórios em precatório complementar

**NOTA 7 do item 5.2, `pagina_pdf` 90**, literal: *"pois, conforme jurisprudência do STJ, a
compensação pela perda da posse se resolve com a consolidação do montante devido ao expropriado"*.

**Mas** — e a ressalva é do próprio manual — *"devem ser incluídos os **juros vencidos antes da
apresentação da requisição**, e não computados no montante requisitado"*.

É também uma das **quatro regras estruturais do cap. 14 que sobrevivem** às ECs 113 e 136:
**exclusão de juros compensatórios** (`consolidado/06-encargos.md` § 8.1;
`tributario-federal.md` § 7).

**E os juros de mora SUSPENDEM no prazo constitucional — expressamente "inclusive nas
desapropriações"** (`R-08-16`, NOTA 1, `pagina_pdf` 89): *"Suspendem-se os juros moratórios no
prazo constitucional de pagamento dos precatórios de 1º de julho, até 2021, e de 2 de abril, a
partir de 2022, até o final do exercício seguinte (Súmula Vinculante n. 17 e Tema 1.037, ambos do
STF), **inclusive nas desapropriações**."*

**`D8-D31`, o defeito mais perigoso do bloco 08, está neste mesmo parágrafo:** *"observada a
transição decorrente da **EC n. 13/2021**"* — é a **113**/2021. **A EC 13/2021 existe e trata de
outra coisa.**

---

## 6. Consolidação de dez/2021 — **as duas desapropriações consolidam**

| Ramo | Índice de nov/2021 | Valor | Juros de dez/2021 | Item · `pagina_pdf` |
|---|---|---|---|---|
| **Desapropriação direta** | **IPCA-E** | **1,17%** | **0,4412%** | 4.5.1.1, NOTA 2 · **67** |
| **Desapropriação indireta** | **IPCA-E** | **1,17%** | **0,4412%** | 4.6.1.1, NOTA 2 · **74** |

Procedimento literal (`pagina_pdf` 50, repetido com redação quase idêntica em **59, 67, 74 e 79**):

> *"a) o crédito será consolidado tendo por base o mês de dez./2021 pelos critérios de juros e
> correção monetária até então aplicáveis, considerando, para esse fim, o [índice] de nov./2021
> ([x]%) e os **juros de dez./2021 (0,4412%)**; b) sobre o valor consolidado do crédito em
> dez./2021, **sem exclusão de qualquer parcela**, incidirá a taxa Selic a partir de jan./2022
> (competência dez./2021) [...]; c) o valor resultante [...] denominado 'Juros Selic', deve ser
> **integralmente somado à parcela denominada 'Juros até 12/2021'**."*

**A redação não é idêntica:** a `pagina_pdf` 50 diz *"tendo por base o mês de dez./2021"*; a **67**,
*"com base no mês de dez./2021"*. Registrado.

**`R-08-14` — "sem exclusão de qualquer parcela":** a SELIC incide sobre o consolidado **inteiro,
principal E juros**. Quadro completo dos cinco lugares em `references/tributario-federal.md` § 8.

> **Ponto de contato com `N-6`:** a consolidação ocorre **em dez/2021**, e é exatamente o mês em
> que o regime dos compensatórios fica sem definição coerente (§ 4.3). **As duas coisas se
> encontram no mesmo mês, e o corpus não as harmoniza.**

---

## 7. Os itens sem cadeia — e a pendência dos honorários de perito

### 7.1 `4.5.6` — honorários de perito(a): **três termos iniciais alternativos, sem critério**

`pagina_pdf` 71. Fixados nos termos do **art. 10 da Lei 9.289/1996**.

- **NOTA 1:** *"Cabe ao(à) expropriante **depositar previamente** esses honorários"*;
- **NOTA 2:** não depositando, *"incidirá correção monetária **a partir da data da decisão ou
  sentença que os tiver fixado, do desembolso feito pela parte ou da entrega do laudo pericial**"*.

> **Três termos iniciais alternativos, e o manual NÃO dá critério de escolha. PENDÊNCIA ABERTA.**
> **Não resolvida aqui**, e **não resolvível por inferência**: escolher um dos três seria inventar
> regra. O motor que encontre esta hipótese **pergunta ao usuário e registra a escolha** (R21).

### 7.2 `D8-C26` — o ônus da perícia INVERTE entre direta e indireta

| | Quem adianta os honorários periciais |
|---|---|
| **Direta** (4.5.6, NOTA 1) | **o expropriante**, por **depósito prévio** |
| **Indireta** (4.6.5, NOTA) | *"Cabe à parte que **requereu a prova pericial** o ônus de **adiantar** os honorários periciais"* |

**Declarado nos dois itens, com fundamentos próprios** (`pagina_pdf` 71 e 76–77).

### 7.3 Os demais itens remetem às regras gerais

- **4.5.7** — honorários de **assistentes técnicos**: art. 95 do CPC, cada parte paga o seu; ao
  final o expropriante reembolsa, *"em valor **não excedente ao fixado para o(a) perito(a)**"*
  (**Súmula 69 do TFR** — não confundir com a **Súmula 69 do STJ** do § 4.1);
- **4.5.8** (honorários de curador especial) e **4.5.9** (custas judiciais e multas): remetem às
  regras gerais, `pagina_pdf` 72;
- **4.6.4 a 4.6.6**: remetem a 4.1.4 e aos itens correspondentes de 4.5, **com a diferença
  declarada da NOTA de 4.6.5** (§ 7.2).

**Honorários fixados em múltiplos do salário mínimo** seguem `R-08-07`: o salário mínimo é
**unidade de conversão, nunca indexador** (art. 7º, IV, da CF) — `tributario-federal.md`, e
`bloco-08-jf.md` § 3.

---

## 8. Defeitos do original desta matéria — registrados, **nenhum corrigido**

| # | `pagina_pdf` | Item | Defeito |
|---|---|---|---|
| **`D8-D14`** | 68 | 4.5.2 | *"convertida na Lei n. **2.703**/2012"* — é a **12.703/2012**, grafada certa em 4.6.2 e 4.9.2 |
| **`D8-D15`** | 76 | 4.6.3 | remissão a *"item 4.5.2"* dentro do capítulo da **indireta**, **duas vezes** — é o `N-10` |
| **`D8-D16`** | 76 | 4.6.3 | *"este ponto reconhecida a constitucionalidade"* — falta o "n"; 4.5.3 grafa *"neste ponto"* |
| **`D8-D17`** | 69, 76 | 4.5.3, 4.6.3 | *"(ADI n. **2332**)"* sem ponto de milhar; a p. 70 grafa *"ADI n. 2.332"* |
| **`D8-D20`** | 71 | 4.5.5 | *"Súmulas n. 131 **n.** 141 do STJ"* — falta o conectivo |
| **`D8-D21`** | 70 | 4.5.4 | *"art. **5**, § 9º"* sem ordinal; a nota logo abaixo grafa *"art. 5º, § 9º"* |
| **`D8-D22`** | 70 | 4.5.4 | *"a partir **agosto** de 2017"* — falta a preposição |
| **`D8-D23`** | 69 | 4.5.3 | *"Até **dez. 2021**"* fora do padrão e **em conflito com a linha de nov./2021** — é o `N-6` |
| **`D8-D26`** | 66, 73 | 4.5.1.1, 4.6.1.1 | *"Parágrafo Único"* × *"parágrafo único"* em tabelas **gêmeas** |
| **`D8-D27`** | 66 | 4.5.1.1 | **única linha da tabela sem a preposição "De"** |
| **`D8-D28`** | 68, 75 | 4.5.2, 4.6.2 | vírgula espúria antes de parêntese em 4.5.2, **ausente na gêmea** |
| **`D8-D29`** | 67, 74 | 4.5.1.1, 4.6.1.1 | *"relativos **a** valores"* × *"relativos **aos** valores"* em notas que deveriam ser idênticas |
| **`D8-D30`** | 65, 72 | 4.5.1, 4.6.1 | espaço antes da pontuação, resíduo de hyperlink |
| **`D8-D31`** | 90 | 5.2, NOTA 7 | *"**EC n. 13/2021**"* — é a **113**/2021, num parágrafo sobre compensatórios em precatório complementar |

Fonte: `bloco-08-jf-detalhe.md` § 6 (trinta e três defeitos no total).
Índice geral: `docs/calculo/armadilhas-comparador.md`.

---

## 9. Invariantes que mordem nesta matéria

- **`R1`** — o segmento **SELIC** de dez/2021 a ago/2025 **engloba correção E juros**. E, a partir
  de dez/2021, **engloba também os compensatórios** (*"Já incluídos na SELIC aplicada aos juros de
  mora"*). **Somar qualquer um deles por fora é dupla contagem**;
- **`R2`** — as sobreposições de **jan/1989** (que o manual explica, `R-08-04`) e **mar/1990** (que
  **não** explica, `D8-C21`) estão nesta cadeia como nas outras três do tronco; a de **dez/2021 na
  indireta** (§ 3) é específica desta matéria;
- **`R3`** — ORTN, OTN, BTN e Ufir são **nominais**; IPC/IBGE, **IPC/FGV**, IPCA-E e IPCA-15 são
  **percentuais**. **Cada virada entre tipos exige ajuste de defasagem**;
- **`R4`** — juros **simples**, e aqui com **vedação expressa** de composição (§ 4.5);
- **`R5`** — **piso nominal POR PARCELA**: *"considerada cada parcela do principal"*, item 4.1.2.2.
  Fundamento: **REsp 1.265.580**;
- **`R7`** — **quatro termos iniciais diferentes convivem nesta matéria**: laudo do perito / laudo
  de avaliação (correção), imissão da posse / efetiva ocupação (compensatórios), a sentença (eixo
  dos juros de mora) e os **três alternativos** dos honorários de perito. **Não são
  intercambiáveis**;
- **`R8`** — título > escolha > default, com a **única exceção** de `R-08-01` (NOTA 2): mudança
  superveniente de legislação **sobre o indexador** passa por cima do título;
- **`R19`** — toda conta que atravesse **10/6/1997**, **ago/2017** ou **dez/2021** grava **qual
  lado aplicou a cada competência**.

---

## 10. Limitações declaradas

1. **`P8-09` — dez/2021 dos juros compensatórios fica SEM REGIME COERENTE** (texto *"Até dez.
   2021"* × tabela que encerra em **nov./2021**). **Pendência aberta, NÃO harmonizada.** Não se
   resolve aqui;
2. **`N-10` — a remissão de 4.6.3 ao "item 4.5.2" está errada.** **Registrada, não corrigida**;
3. **Honorários de perito (4.5.6): três termos iniciais alternativos sem critério de escolha.**
   **Pendência aberta**, § 7.1;
4. **A cadeia de juros de mora (4.5.2 / 4.6.2) não foi extraída segmento a segmento** para
   `tabelas-normativas/`. O que o corpus registra dela está no § 3, com o escopo declarado ali.
   **Os segmentos ausentes não foram inferidos**;
5. **A cadeia de correção da INDIRETA (4.6.1.1) TEM JSON próprio desde o bloco 19, tarefa 3** —
   `cjf.desapropriacao-indireta.correcao-monetaria.json`, **11 segmentos DERIVADOS em tempo de
   geração** do arquivo da direta (campo `DERIVADA_DE`). **São duas cadeias, e não uma com dois
   escopos**, porque a modalidade muda o **termo inicial** — campo de cadeia — e não a linha do
   tempo; a justificativa inteira está no campo
   `DECISAO_1_DUAS_CADEIAS_E_NAO_UMA_COM_DOIS_ESCOPOS` do JSON. **A identidade das duas tabelas
   segue sendo afirmação da extração** (`bloco-08-jf-detalhe.md` § 3.1), e é dela que a derivação
   depende;
6. **Sem preset nomeado no corpus.** O catálogo de `01-plano-extracao.md` não tem ID para esta
   matéria. **Entra como cadeia, não como preset.** Registrado, **não inventado**;
7. **`P8-07` — `ponta_materializada` no início:** o manual abre com *"De 1964"*, **sem mês**;
8. **ECs 113/2021 e 136/2025, precatório e a fase pré-requisitório** não se reproduzem aqui —
   `references/tributario-federal.md` §§ 6 e 7. **Fazenda estadual e municipal pós-EC 136/2025
   segue em vácuo normativo — lacuna de LEGISLAÇÃO, não de pesquisa**; **ADI 7873 pendente**;
9. **As séries não estão aqui.** ORTN, OTN, BTN, **IPC/FGV**, Ufir, IPCA-E, IPCA-15 e Selic são
   dado **(B)** — contrato em `skills/indices-judiciais/`. **O IPC/FGV é série que só esta cadeia
   consome**, e é a que mais facilmente falta no catálogo.

---

## 11. Ponteiros

- `skills/calculo-judicial-atualizacao/regras/cjf.desapropriacao-direta.correcao-monetaria.json` — 11 segmentos
- `skills/calculo-judicial-atualizacao/regras/cjf.desapropriacao-indireta.correcao-monetaria.json` — 11 segmentos
- `skills/calculo-judicial-atualizacao/regras/cjf.desapropriacao-direta.juros-compensatorios.json` — 3 segmentos
- `skills/calculo-judicial-atualizacao/regras/cjf.desapropriacao-indireta.juros-compensatorios.json` — 3 segmentos
- `docs/calculo/consolidado/02-atualizacao-detalhe.md` **§ 5.3.1** — os compensatórios como cadeia
  própria, os três cortes, `N-6` e `N-10`
- `docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md` §§ 3.1, 3.1.1 — direta × indireta
  linha a linha, os itens sem cadeia; § 4 — os doze atritos; § 6 — os trinta e três defeitos
- `docs/calculo/extracao/justica-federal/bloco-08-jf.md` §§ 6 e 7 — consolidação de dez/2021 e
  capítulo 5 (requisições), com `R-08-16` e `R-08-19`
- `docs/calculo/consolidado/06-encargos.md` § 8.1 — as quatro regras do cap. 14 que sobrevivem
- `references/tributario-federal.md` §§ 6, 7 e 8 — ECs, precatório, consolidação nos cinco lugares
- `references/civel-federal.md` — condenatórias em geral, o tronco comum e as fórmulas D1/D2
- `docs/calculo/armadilhas-comparador.md` — índice dos defeitos do original
