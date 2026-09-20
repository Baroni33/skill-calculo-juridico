# Catálogo de índices — classificação e fonte de cada um

Companheiro de [`../SKILL.md`](../SKILL.md). **Movido da espinha no bloco 17, pelo limite de
500 linhas** — nenhum índice foi removido.

A classificação normativa vive em
`docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json`, que é o que o validador lê.
**Este arquivo é a leitura humana dele. Divergiram, vale o JSON.**

---

### Os índices, com a classificação que decide tudo

Fontes: `02-atualizacao.md` §§ 5, 10 e 11; `02-atualizacao-detalhe.md` §§ 5.1, 5.2 e 10.
**Onde cada um incide é matéria de `calculo-judicial-atualizacao`** — aqui só a semântica.

**NOMINAIS — refletem a inflação do mês ANTERIOR (R3):**

| Índice | O que é | Registro no corpus |
|---|---|---|
| **ORTN** | Obrigação Reajustável do Tesouro Nacional | tronco CJF 1964–fev/1986, Lei 4.357/1964 |
| **OTN** | sucessora da ORTN | mar/1986–jan/1989, com **multiplicador 6,17** em jan/1989 |
| **BTN** | Bônus do Tesouro Nacional | mar/1989–mar/1990; dívida fiscal jan/89–jan/91 |
| **Ufir** | Unidade Fiscal de Referência | 1992–2000 (condenatórias); até jan/1996 (repetição) |

**PERCENTUAIS — refletem a inflação do PRÓPRIO mês (R3). Só entram aqui os NOMEADOS na fonte:**

| Índice | O que é | Nota que não pode ser perdida |
|---|---|---|
| **INPC** | IBGE, população de renda baixa | é o **deflator da variante previdenciária** da taxa legal |
| **IGP-DI** | FGV | cadeia previdenciária |
| **IPC/IBGE** | expurgos | **42,72%** (jan/89) e **10,14%** (fev/89) — valores fixos, **o expurgo SUBSTITUI, não soma**. Fonte: **D8-C21**, não o item 4.1.2.4 |
| **SELIC** | Bacen | **BLOCO 19** — deixou de ser `englobante`. Englobamento é fato de **R1** e vive no campo **`engloba`**, que não mudou; pô-lo em `tipo_indexador` deixava a SELIC **cega para R3**. Fonte: **externa ao corpus** (tabela do bloco 19) |

**JANELA-DESLOCADA — o período de coleta cai METADE em M−1 e METADE em M (R3, bloco 19):**

| Índice | O que é | Fonte |
|---|---|---|
| **IPCA-15/IBGE** | difere do IPCA **só** no período de coleta — do dia **16 de M−1** ao dia **15 de M** — e na abrangência geográfica | **FONTE EXTERNA AO CORPUS** (IBGE), declarada como externa no catálogo |
| **IPCA-E/IBGE** | criado em dez/1991, trimestral desde jan/1995; **o IPCA-E mensal das tabelas judiciais É o IPCA-15** | idem. A identificação é **da fonte**, não de semelhança de nome |

> **Não é `nominal` nem `percentual`.** Não reflete M−1 inteiro nem M inteiro. Com três classes
> há **três pares** de virada, e `IPCA-E → IPCA-15` **deixou de ser virada**: mesma classe.

**INDETERMINADOS — o conceito se aplica, e NÃO HÁ FONTE que os classifique:**

> **Não os presuma percentuais.** O item 4.1.2.4 nomeia **ORTN, OTN, BTN, Ufir** de um lado e
> **INPC, IGP-DI, IGP-M** do outro — **e mais nada**. As listas são exemplificativas, **o que não
> autoriza estendê-las por semelhança de nome**. Classificar o IPCA-E como percentual *"porque
> IPCA soa percentual"* é a dedução que o bloco 17 veio remover.

| Índice | O que é | Por que indeterminado |
|---|---|---|
| **IPCA série especial** | segmento **próprio** do manual, dez/1991 | **BLOCO 19** — a fonte externa alcança IPCA-15 e IPCA-E e **NÃO diz** que a série especial seja um ou outro. O manual a grava à parte; identificá-la por semelhança de nome é a dedução proibida. `IPCA-E` e `IPCA-15` **saíram daqui** e são `janela-deslocada` |
| **taxa legal** | **DERIVADA** (R11), razão entre fatores | **BLOCO 19, `P19-01`** — perdeu o rótulo `englobante`, que era fato de R1 no campo de R3. A fonte externa **não a alcança**, e `percentual` por analogia com a SELIC seria a dedução proibida |
| **IPC** (nu) · **UPC** · **LBC** · **LBC – 0,5%** · **LFT – 0,5%** · **TRD** | FGTS (4.8.1.1) e poupança (4.9.1.1) | `P18-01`, sem fonte. O **`IPC` nu** tem **ambiguidade registrada**: o manual usa **dois** IPC, de emissores distintos, e `D8-C21` sustenta **só o **IPC/IBGE**. A **TRD** NÃO herda a razão da TR — a fonte do BCB nomeia TBF, Redutor-R e TR, e não a TRD |
| **IPC/FGV** | mar–dez/1991, **exclusivo da desapropriação direta** | sem classificação em fonte |
| **IPC-R** · **IRSM** | fase URV · Índice de Reajuste do Salário Mínimo — cadeia previdenciária | sem classificação em fonte |
| **TR** · **remuneração básica da poupança** | art. 39 da Lei 8.177/91 · art. 1º-F da Lei 9.494/97 (**a fórmula muda em 04/05/2012**; até lá, 0,5% a.m.) | **BLOCO 19 — indeterminado COM RAZÃO REGISTRADA, não por ausência de fonte:** *"período entre datas de aniversário e prefixação"* (BCB, **fonte externa ao corpus**). **NÃO se fecha esperando fonte** — deixou de carregar `P17-02`, que afirmava *"não há fonte"* e passou a ser falso |

**Consequência operacional:** virada em que uma das pontas é `indeterminado` **bloqueia** no
validador, sob `R3-INDETERMINADO`. Passar converteria *"não se sabe"* em *"está certo"* — e num
validador cuja razão de existir é que o erro de R3 **não tem sintoma**, o silêncio é o pior
resultado. Pendências **P17-01**, **P18-01** e **P19-01**. Catálogo:
`docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json`.

> **Duas razões de `indeterminado`, e elas se fecham diferente (bloco 19).** *Sem fonte*, campo
> `tipo_indexador_pendencia`, **fecha quando a fonte chegar**. *A fonte diz que não cabe*, campo
> `tipo_indexador_razao`, **não fecha esperando fonte** — é o caso da **TR**. Os campos são
> **mutuamente excludentes**, e as duas situações **bloqueiam** a virada.

**ENGLOBAM correção E juros (R1) — e isso vive no campo `engloba`, NÃO em `tipo_indexador`:**

| Índice | Natureza | Nota |
|---|---|---|
| **SELIC** | publicada (Bacen) | **nunca conviver com índice inflacionário no mesmo intervalo**. Em R3 é **`percentual`** (bloco 19) |
| **taxa legal** | **DERIVADA**, não publicada | razão entre fatores (R11); **6 decimais, truncamento**; piso zero (R6). Em R3 é **`indeterminado`** (`P19-01`) |

> **O valor `englobante` de `tipo_indexador` foi RETIRADO no bloco 19** — era um fato de R1
> dentro do campo de R3, e deixava a SELIC cega para a comparação de defasagem. **`engloba` não
> mudou**, e R1 segue lendo exatamente o que lia.

---

## A régua de ajuste da virada de `R3` — **LACUNA DECLARADA, não régua a inventar**

`R3` diz que `nominal` reflete **M−1**, `percentual` reflete **M** e `janela-deslocada` reflete
**metade de cada**, e que trocar de classe **sem ajustar desloca o cálculo em um mês**. **O que o
corpus não diz é o que FAZER na virada** — se o mês da ponta se repete, se pula, ou se o índice se
pro-ratiza. **Não há régua, e inventar uma plausível produziria número plausível e errado.**

**O que existe, e não é isso:** o campo **`aplicacao`** do segmento, com o vocabulário fechado
**D1–D4** (`02-atualizacao-detalhe.md` § 5.3). Ele declara **se** a defasagem foi tratada naquele
segmento — é contra ele que o validador decide entre `[R3]` e segmento limpo —, **não qual
deslocamento aplicar na fronteira entre dois segmentos de classes diferentes**.

**Busca negativa, com escopo contado:** os **15** arquivos de `docs/calculo/consolidado/` e as
**31** páginas `.md` de `skills/`, por `defasagem`, `desloca`, `ajustar`, `ajuste`, `na virada`,
`um mês`, `pro rata`, `régua`. Todas as ocorrências **enunciam o efeito de não ajustar** ou
**descrevem D1–D4**; **nenhuma dá o procedimento**. E o corpus registra a própria indecisão: a
`L3` de [`../../../docs/calculo/consolidado/10-literais-na-extracao.md`](../../../docs/calculo/consolidado/10-literais-na-extracao.md)
§ 5.2 foi reclassificada como **`DÚVIDA`** com a frase *"ninguém sabe qual é o comportamento
certo"*, e nomeia as três perguntas que faltam responder — a primeira delas é **decisão de
modelagem, não leitura de fonte**.

**Conduta enquanto a lacuna existir:** onde uma das pontas é `indeterminado`, o validador já
**bloqueia** sob `R3-INDETERMINADO`. Onde as duas pontas têm classe **e são diferentes**, a
violação é **registrada como `[R3]` e não é consertada pelo motor** — as confirmadas que
`00-numeros.md` § 3 publica são **do manual**. **Quem precisar do número tem de decidir a régua, declarar
a decisão como override justificado (R21) e gravá-la na memória de cálculo (R13).**

---

**Não são índices, mas o contrato as trata como série:** **URV** (cotações diárias em CR$; **o
método de conversão não está no bloco** e não foi inferido), **moedas e paridades**
(multiplicadores de transição) e **calendários** (18.14). E **MVR**, extraída em
`serie-18.11-otn-btn-mvr.csv` ao lado de OTN e BTN, fica **sem classificação**: nenhuma cadeia
do repositório a consome, e classificar por analogia seria inventar.
