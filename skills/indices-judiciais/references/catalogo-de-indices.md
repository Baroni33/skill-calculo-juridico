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

**INDETERMINADOS — o conceito se aplica, e NÃO HÁ FONTE que os classifique:**

> **Não os presuma percentuais.** O item 4.1.2.4 nomeia **ORTN, OTN, BTN, Ufir** de um lado e
> **INPC, IGP-DI, IGP-M** do outro — **e mais nada**. As listas são exemplificativas, **o que não
> autoriza estendê-las por semelhança de nome**. Classificar o IPCA-E como percentual *"porque
> IPCA soa percentual"* é a dedução que o bloco 17 veio remover.

| Índice | O que é | Por que indeterminado |
|---|---|---|
| **IPCA** · **IPCA-E** · **IPCA-15** · **IPCA série especial** | IBGE — **três índices diferentes**, mais um segmento próprio do manual | o item 4.1.2.4 **não nomeia sequer "IPCA"**. `IPCA-15` é o deflator da taxa legal do mês `m−1`; `IPCA-E` **não é o IPCA** — ver "Armadilhas" |
| **IPC/FGV** | mar–dez/1991, **exclusivo da desapropriação direta** | sem classificação em fonte |
| **IPC-R** · **IRSM** | fase URV · Índice de Reajuste do Salário Mínimo — cadeia previdenciária | sem classificação em fonte |
| **TR** · **remuneração básica da poupança** | art. 39 da Lei 8.177/91 · art. 1º-F da Lei 9.494/97 (**a fórmula muda em 04/05/2012**; até lá, 0,5% a.m.) | **rebaixadas no bloco 17.** Eram `percentual` por critério **formal** — *"não é unidade monetária, logo é percentual"* —, e **inferência declarada não é fonte**. `bloco-09-relatorio.md` § 5.3: *"nenhum dos dois manuais classifica a TR"* |

**Consequência operacional:** virada em que uma das pontas é `indeterminado` **bloqueia** no
validador, sob `R3-INDETERMINADO`. Passar converteria *"não se sabe"* em *"está certo"* — e num
validador cuja razão de existir é que o erro de R3 **não tem sintoma**, o silêncio é o pior
resultado. Pendências **P17-01** e **P17-02**. Catálogo:
`docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json`.

**ENGLOBANTES — cobrem correção E juros (R1). Não são séries de correção:**

| Índice | Natureza | Nota |
|---|---|---|
| **SELIC** | publicada (Bacen) | **nunca conviver com índice inflacionário no mesmo intervalo** |
| **taxa legal** | **DERIVADA**, não publicada | razão entre fatores (R11); **6 decimais, truncamento**; piso zero (R6) |

**Não são índices, mas o contrato as trata como série:** **URV** (cotações diárias em CR$; **o
método de conversão não está no bloco** e não foi inferido), **moedas e paridades**
(multiplicadores de transição) e **calendários** (18.14). E **MVR**, extraída em
`serie-18.11-otn-btn-mvr.csv` ao lado de OTN e BTN, fica **sem classificação**: nenhuma cadeia
do repositório a consome, e classificar por analogia seria inventar.
