# Atualização — detalhe

As cadeias da Justiça Federal segmento a segmento, as quatro fórmulas de `aplicacao` do CJF, e a consolidação de dezembro de 2021 nos cinco lugares em que ocorre.

Companheiro de [`02-atualizacao.md`](02-atualizacao.md). **Offset de paginação zero** no manual do TRT-3; `pagina_pdf = impresso + 1` no do CJF.

---
## 5. Justiça Federal — as cadeias do CJF

Fonte: Manual CJF, Res. 990/2026 — `../extracao/justica-federal/bloco-08-jf.md`;
JSON em `../tabelas-normativas/cjf.*.json`. **Única fonte do corpus cuja edição está vigente.**

### 5.0 A varredura — **item × JSON × consolidado**, caps. 2 e 4

**Escopo declarado.** Relidos no PDF `manual_de_calculos_2026.pdf`: **todas** as 93 páginas para o
sumário de itens numerados (regex `^[2-5](\.\d+){1,4}\s`), e **integralmente** as `pagina_pdf`
**22–39** (cap. 2) e **41–87** (cap. 4). Cruzado contra `ls ../tabelas-normativas/*.json` e busca em
`../consolidado/` por `JAM`, `poupan`, `UPC`, `LBC`, `LFT`, `FGTS`, `compensatóri`, `desapropria`.

| Item | O que é | JSON | Consolidado | Veredito |
|---|---|---|---|---|
| 2.3.1.2 | correção — dívida fiscal | **sim** | sim | ok |
| **2.3.2.2** | **juros — dívida fiscal**, 8 linhas, com `base_incidencia` | **sim, bloco 19 T3** | § 5.3.6 (agora) | **era lacuna; GERADA** — 8 segmentos |
| 2.3.3.2 · 2.4.2.3 · 2.4.4.2 · 2.4.5.2/.3 | multas por período | não | parcial | **não é atualização** — fora do componente |
| 2.4.2.1.2 | correção — contribuição previdenciária | não | detalhe § 2.3 | **remissão + janela própria**: *"mesmos critérios do IR, item 2.3.1.2"*, mais o vácuo fev–mar/1997. Cadeia derivada |
| **2.4.2.2.2** | **juros — contribuição previdenciária** | **não** | detalhe § 2.3 | **SEGUE AUSENTE** — `P18-02`. A fonte extraída tem do item **uma frase só** (o `N-2`); a tabela nunca foi transcrita. § 5.3.6 |
| **2.4.4.1** | **FGTS fiscal (`JCM`)** | **sim, bloco 19 T3** | §§ 5.3.2 e 5.3.6 | **era lacuna; GERADA** — 5 segmentos, e **é OUTRA que a de 4.8** |
| 2.4.5.1 | juros — Incra | não | — | **remissão** a 2.3.2.2 a partir de maio/1990; só a linha "até abr/1990" é própria |
| 2.6 · 2.7.1.1 · 2.8.5 | conselhos, foro/laudêmio, multas adm. | não | detalhe § 2.5 | **remissão** a 2.3.1.2 — não é lacuna |
| 2.9 | falência | não | detalhe § 2.6 | **não é cadeia** — `D8-C23`, segmento condicional a evento futuro |
| 4.2.1.1 · 4.2.2 | condenatórias | **sim ×2** | §§ 5.1–5.2 | ok |
| 4.3.1.1 | previdenciário | **sim** | § 5.2 | ok |
| 4.4.1.1 | repetição de indébito | **sim** | § 5.2 | ok |
| 4.5.1.1 | correção — desapropriação **direta** | **sim** | § 5.2 | ok |
| **4.5.2** | **juros de mora — desapropriação direta**, 5 linhas | **não** | § 5.3.1 (em prosa) | **SEGUE AUSENTE** — `P18-02`. A tabela **nunca foi extraída linha a linha**, e o corpus o declara com escopo. § 5.3.6 |
| **4.5.3** | **juros compensatórios — direta**, 4 linhas | **sim, bloco 19 T3** | §§ 5.3.1 e 5.3.6 | **era lacuna; GERADA** — **3** segmentos, e a diferença para as 4 linhas está declarada. As **taxas** das duas primeiras linhas **não estão na fonte** e ficam `null` |
| 4.5.4–4.5.9 | TDAs, honorários, custas | não | § 5.3.1 | **não são cadeia** — `D8-C25` vive só em 4.5.4 |
| **4.6.1.1** | correção — desapropriação **indireta** | **sim, bloco 19 T3** | §§ 5.2 e 5.3.6 | **era lacuna; GERADA** — 11 segmentos, **DERIVADA** da de 4.5.1.1, que lhe é idêntica, inclusive no IPC/FGV |
| **4.6.2** | **juros de mora — indireta** | **não** | § 5.3.1 | **SEGUE AUSENTE** — `P18-02`, pela mesma razão de 4.5.2. Fecha em **dez/2021**, e a gêmea 4.5.2 em **nov/2021** |
| **4.6.3** | **juros compensatórios — indireta** | **sim, bloco 19 T3** | §§ 5.3.1 e 5.3.6 | **era lacuna; GERADA** — 3 segmentos. Carrega o `N-10` (remete a *"item 4.5.2"*, da direta), **transcrito, não corrigido** |
| **4.7.1** | correção — ações trabalhistas | **não, e não deve haver** | §§ 6 e 5.3.6 | **NÃO É LACUNA — não existe tabela.** **Registra-se a DELEGAÇÃO, não a ausência.** Só lista de leis, e a NOTA 2 **delega**: *"utilizar a tabela de coeficientes trabalhistas expedida pelo TST"*. Mesmo desenho do `P9-02`. A cadeia vive numa **série**, não numa regra |
| 4.7.2 | juros — trabalhista | **sim** | § 5.2 e **§ 5.2-B** | **escopo restrito e termo inicial próprios** — `pagina_pdf` 77 e 78 |
| **4.8.1.1** | **correção — FGTS (`JAM`)** | **sim, bloco 18** | **§ 5.3.2 (agora)** | **era lacuna; consolidada** |
| 4.8.2 | juros remuneratórios — FGTS | não | § 5.3.2 | **não é cadeia temporal** — eixo = conta existente em 22/9/1971 |
| **4.8.3** | **juros de mora — FGTS** | **sim, bloco 18** | **§ 5.3.4 (agora)** | **era lacuna; consolidada** |
| **4.9.1.1** | **correção — poupança** | **sim, bloco 18** | **§ 5.3.3 (agora)** | **era lacuna; consolidada** |
| 4.9.2 | juros remuneratórios — poupança | não | § 5.3.3 | **não é cadeia temporal** — eixo = **abertura da conta** (`D8-C16`) |
| **4.9.3** | **juros de mora — poupança** | **sim, bloco 18** | **§ 5.3.4 (agora)** | **era lacuna; consolidada** |
| 4.1.4–4.1.8 · 4.x.3/4.x.4 | honorários, custas, imputação | não | `03-verbas`, `06-encargos` | **não são cadeia** |
| cap. 3 | dívidas diversas | não | — | **não há cadeia: há o título** (R-08-26) |

**Não eram só duas.** Além de FGTS e poupança, a varredura encontrou **oito cadeias tabuladas sem
JSON**: 4.5.2, 4.5.3, **4.6.1.1, 4.6.2, 4.6.3** (a desapropriação **indireta inteira**), **2.3.2.2**,
**2.4.2.2.2** e **2.4.4.1**. Todas têm tabela período × taxa/índice no manual; nenhuma está em
`tabelas-normativas/`. **Registradas como `P18-02`, não geradas no bloco 18** — ver § 5.3.5.

> **Atualizado na tarefa 3 do bloco 19.** Das oito, **cinco foram geradas** — 4.5.3, 4.6.1.1, 4.6.3,
> 2.3.2.2 e 2.4.4.1 — e **três seguem ausentes**: **4.5.2**, **4.6.2** e **2.4.2.2.2**, e por uma
> razão só, que não é de modelagem: **a tabela dessas três nunca foi extraída linha a linha.**
> `P18-02` **encolhe de oito para três**. Ver **§ 5.3.6**, que traz as cinco decisões e o que faltou.

**E uma que parecia lacuna e não é: 4.7.1.** O manual **não tem** tabela de correção trabalhista; ele
delega ao TST. Afirmá-la ausente seria afirmar ausência de algo que a fonte nunca prometeu.

### 5.1 O tronco comum — 1964 a fev/1991

Quatro cadeias de correção (condenatórias, previdenciário, repetição, desapropriação)
compartilham o mesmo tronco, **palavra por palavra**:

| Período | Indexador | Observação do manual |
|---|---|---|
| 1964 a fev/1986 | ORTN | Lei 4.357/1964 |
| mar/1986 a jan/1989 | OTN | débitos anteriores a jan/1989 multiplicados, neste mês, por **6,17** |
| jan/1989 | **IPC/IBGE 42,72%** | "Expurgo, em substituição ao BTN" |
| fev/1989 | **IPC/IBGE 10,14%** | idem |
| mar/1989 a mar/1990 | BTN | — |
| mar/1990 a fev/1991 | IPC/IBGE | "Expurgo, em substituição ao BTN e ao INPC de fev./1991" |

**O expurgo SUBSTITUI, não soma** (item 4.1.2.1, `pagina_pdf` 42). **A dívida fiscal (cap. 2)
NÃO tem este tronco.**

### 5.2 Depois de fev/1991 — por ramo

| Ramo | Após fev/1991 | Bifurca por devedor? |
|---|---|---|
| **Condenatórias gerais** | INPC → IPCA série especial (dez/91) → Ufir (92–00) → IPCA-E (01–nov/21) → **dez/21**: Selic (FP) × IPCA-E (não-FP) → set/24: Selic (FP) × IPCA-15 (não-FP) → **set/25: IPCA-15 para os dois** | **sim, dez/2021**; reconverge em **set/2025** |
| **Previdenciário** | INPC → IRSM → URV → IPC-R → INPC → IGP-DI → INPC (set/06–nov/21) → Selic (dez/21–ago/25) → **INPC (set/25→)** | **nunca** |
| **Repetição de indébito** | INPC → IPCA esp. → Ufir (92–jan/96) → **Selic desde jan/1996** | **nunca** |
| **Desapropriação direta** | **IPC/FGV (mar–dez/1991)** — índice exclusivo desta cadeia → Ufir → IPCA-E → Selic (dez/21–ago/25) → IPCA-15 | **nunca** |
| **Dívida fiscal** | BTN (jan/89–jan/91) → janela 1991-02..1991-12 → **Ufir → Selic, bifurcado pelo `data-do-fato-gerador`** | por fato gerador, não por devedor |

**Juros — cadeias autônomas:**

- `cjf.condenatorias-gerais.juros-mora`: 0,5% a.m. até dez/2002 → Selic (03–jun/09) →
  **bifurca em jul/2009** (FP: 0,5%/poupança; não-FP: Selic) → dez/21 Selic para os dois →
  set/24 Selic (FP) × taxa legal (não-FP) → **set/25 taxa legal para os dois**;
- `cjf.trabalhista.juros-mora`: 0,5% (até fev/87) → **1,0% composta mar/87–mar/91 (DL 2.322/87)**
  → 1,0% (abr/91–jul/01) → **bifurca em ago/2001** e **nunca reconverge** — o ramo
  empresa pública/prestador segue em **1,0% a.m.** até jun/2026.

**R-08-08 — a bifurcação por devedor não é universal.** Três cadeias nunca bifurcam.

### 5.2-A Servidores e empregados públicos — o recorte que não é Fazenda × não-Fazenda

**Achado `L1`/`L2` de [`10-literais-na-extracao.md`](10-literais-na-extracao.md), e é o único
`BLOQUEIA` da varredura.** As condenatórias em geral têm **um terceiro recorte** que nem a tabela
de 4.2.2 nem a bifurcação de jul/2009 exibem: **a qualidade do crédito**. Sem ele, quem lê a
cadeia acima aplica **Selic** onde o manual manda **0,5% ao mês**, por até oito anos de
competências.

**Juros — item 4.2.2, NOTA 3, `pagina_pdf` 55, literal:**

> *"Nos créditos referentes a **servidores(as) e empregados(as) públicos(as)**, no período
> **anterior a julho/2009**, os juros serão computados à taxa de: a) **1% ao mês até jul./2001**
> (Decreto-Lei n. 2.322/1987; AgRg no REsp n. 1.085.995); b) **0,5% ao mês de ago./2001 a
> jun./2009** (MP n. 2.180-35/2001, que acrescentou o art. 1º-F da Lei n. 9.494/1997)."*

**Correção — item 4.2.1.1, NOTA 3, `pagina_pdf` 49, literal:**

> *"Para as **remunerações** de servidores(as) e empregados(as) públicos(as), o **termo inicial da
> correção monetária** deve ser o **mês da competência e não o mês de pagamento**."*

**Três consequências, e nenhuma é dedutível da tabela:**

1. **O recorte é do CRÉDITO, não do devedor.** *"Créditos referentes a servidores e empregados
   públicos"* não é o mesmo universo de `condicao.devedor: fazenda-publica`, e o manual não os
   equipara. **Não harmonizado** — os dois recortes convivem no mesmo item;
2. **A janela de ago/2001 a jun/2009 contradiz a linha da tabela**, que dá **Selic** desde
   jan/2003. A nota **restringe** a tabela, como o `N-11` faz na poupança. **É a nota que
   prevalece para esses créditos**, porque é ela que os nomeia;
3. **O eixo da correção muda**: mês de competência, não de pagamento. Alinha-se ao da NOTA 1 do
   previdenciário (4.3.1.1), que diz o mesmo para benefícios.

> **Por que não virou segmento nem ramo.** O eixo é a **qualidade do crédito**, não a competência
> nem o devedor, e `dominio_condicoes` das duas cadeias declara **`devedor: [fazenda-publica,
> nao-fazenda-publica]`** como exaustivo. Abrir um terceiro valor ali afirmaria uma
> ortogonalidade que a fonte não declara. **Fica como nota de aplicação, com item e página** — o
> mesmo tratamento de 4.8.2, 4.9.2 e da NOTA 3 de 4.9.1.1.

### 5.2-B A cadeia trabalhista do CJF — escopo e termo inicial **não são os da Justiça do Trabalho**

**Achado `L12` de [`10-literais-na-extracao.md`](10-literais-na-extracao.md), promovido a
`BLOQUEIA` no bloco 20, mais o termo `estatutário` da varredura de entidade (§ 5 daquele
arquivo).** `cjf.trabalhista.juros-mora` aparece na § 5.2 como *"a cadeia trabalhista do CJF"*, e
quem lê só isso importa de **R7** ([`01-dominio-e-invariantes.md`](01-dominio-e-invariantes.md)
§ 2.4) o termo inicial da linha **Trabalhista**, que é **ajuizamento**. **O CJF escreve outra
coisa, e escreve para quem o capítulo alcança.**

**Termo inicial — item 4.7.2, `pagina_pdf` 78, campo `termo_inicial` de
`../tabelas-normativas/cjf.trabalhista.juros-mora.json`, literal:**

> *"Os juros são contados a partir da **notificação inicial (Súmula n. 224 do STF)**, salvo
> determinação judicial em outro sentido."*

**Escopo — NOTA de abertura do item 4.7, `pagina_pdf` 77, campo `escopo_restrito`, literal:**

> *"Este capítulo aplica-se **apenas a ações trabalhistas relativas a contratos regidos pela
> Consolidação das Leis do Trabalho (CLT) anteriores à promulgação da vigente Constituição
> Federal**, nos termos do art. 27, § 10, do ADCT/1988, **não se aplicando a ações relativas a
> servidores(as) públicos(as) sob regime estatutário**."*

**Por que muda resultado, e nos dois literais:**

1. **`ajuizamento` ≠ `notificação inicial`.** São datas distintas, e o termo inicial é operando
   de **D2**. Reclamação ajuizada em **10/03/1995** e notificada em **05/04/1995**, **1,0% a.m.
   simples**: pela espinha os juros correm desde **março**; pelo literal, desde **abril**. **Um
   mês inteiro de juros sobre todo o principal**. *(O segmento aplicável em 1995 é o
   `1991-04..2001-07`, **sem `condicao`**: em 1995 a cadeia é **tronco**, e a bifurcação por
   devedor — Fazenda × empresa pública/prestador — só nasce em **ago/2001**. Qualificar o caso
   por ramo seria anacronismo.)*;
2. **o escopo decide se a cadeia é sequer a certa.** Contrato **celetista posterior à promulgação
   da vigente Constituição Federal** em ação na Justiça Federal: pela § 5.2 o implementador aplica
   esta cadeia e obtém **1,0% a.m.** em 2005; pelo literal o item 4.7 **não o alcança**, e a conta
   corre por **4.2.2** — **Selic** desde jan/2003. **Servidor(a) estatutário(a) está excluído(a)
   por escrito**, e é o recorte da § 5.2-A que o governa.

> **`05/10/1988` é GLOSA, não literal.** O `escopo_restrito` escreve *"anteriores à promulgação da
> vigente Constituição Federal"*; a data é **inferência nossa** sobre qual dia isso é. **Correta**
> — e ainda assim inferência, dentro de uma seção cujo produto é o literal. Fica marcada como tal,
> e o texto acima usa a formulação da fonte.

> **Não harmonizado, e é o ponto.** **R7** continua dizendo **ajuizamento** para a Justiça do
> Trabalho (CLT art. 883; Súmula 200 do TST) — é outra jurisdição e outra fonte. O que este
> parágrafo acrescenta é que **a cadeia do CJF tem termo inicial próprio, escrito**, e um escopo
> que a espinha não exibia. **Os dois ficam registrados lado a lado**, como em
> [`08-nacional-e-regional.md`](08-nacional-e-regional.md).
>
> **Ressalva de proveniência:** o JSON **não grava `termo_inicial_pagina_pdf`** para esta cadeia;
> a página citada é a da `fonte` do item (78). A do `escopo_restrito` é gravada (77).

### 5.3 As quatro fórmulas de `aplicacao` do CJF

| # | Regra | `aplicacao` (token) | Onde |
|---|---|---|---|
| **D1** | Selic **no mês posterior ao de sua competência, inclusive no mês de pagamento** | `mes-posterior-a-competencia` | Fazenda, a partir de dez/2021; e a taxa legal |
| **D2** | Selic **do mês seguinte ao termo inicial dos juros até o mês anterior ao pagamento, e 1% no mês do pagamento** | `mes-seguinte-ao-termo-inicial-dos-juros-e-1pct-no-mes-do-pagamento` | não-Fazenda; e Fazenda jan/03–jun/09 |
| **D3** | do mês seguinte ao **recolhimento indevido** até o mês anterior à repetição, e 1% no mês | `mes-seguinte-ao-recolhimento-indevido-e-1pct-no-mes-da-repeticao` | repetição de indébito |
| **D4** | do mês seguinte à **competência da parcela** até o mês anterior ao pagamento, e 1% no mês | `mes-seguinte-a-competencia-da-parcela-e-1pct-no-mes-do-pagamento` | dívida fiscal (2.3.2.2), **FGTS (4.8.3) e poupança (4.9.3)** |

**D1 e D2 dão resultados diferentes sobre a mesma série.** A taxa legal segue **D1**
(item 4.2.2, NOTA 7, `pagina_pdf` 56).

> **As quatro são TOKEN, e a coluna do meio é o contrato com o validador — bloco 20.**
> `valida_cobertura.py` só desliga R3 contra o **vocabulário fechado**
> `APLICACOES_QUE_AJUSTAM_DEFASAGEM`, e ele nasceu com **dois** valores enquanto esta tabela
> declarava **quatro fórmulas**: `D2`, `D3` e `D4` estavam gravadas em **prosa** e eram rejeitadas
> **pela grafia**, não pelo conteúdo. **Uma das duas violações de R3 que o fechamento revelou era,
> por isso, falso positivo de modelagem** — a `Ufir → Selic` de
> `cjf.repeticao-indebito.correcao-monetaria`, que é o `D3` do próprio componente do segmento
> (`componente: correcao-monetaria`, `engloba` os dois). Tokenizadas as três, ela desapareceu.
>
> **O literal não se perdeu:** a prosa do manual migrou para `aplicacao_literal`, e
> `aplicacao_formula` grava qual `D` é. A **outra** violação revelada **se sustenta**: o
> `aplicacao` do IPCA-E de jan./2001 (`cjf.condenatorias-gerais.correcao-monetaria`) diz **qual
> valor** usar naquele mês, **não quando** o índice incide — **não é regra de defasagem**, e por
> isso **não foi tokenizada**.

### 5.3.1 Desapropriação — os juros compensatórios são cadeia própria

**Terceira cadeia autônoma, além da correção (§ 5.2) e dos juros de mora.** Itens 4.5.3
(direta) e 4.6.3 (indireta). Quem tratar a desapropriação só pela linha de correção monetária
perde esta inteira.

**Termo inicial — mesma súmula, dois marcos (D8-C10):**

| | Direta (4.5) | Indireta (4.6) |
|---|---|---|
| Correção | data do **laudo do perito** — Súmula 75 do TFR | data do **laudo de avaliação** |
| **Compensatórios** | data da **imissão da posse**, certificada no mandado | data da **efetiva ocupação** do imóvel |

Ambos por **Súmula 69 do STJ**. Não é defeito: não há imissão na desapropriação indireta. Mas é
bifurcação, e o schema precisa registrá-la.

**Cortes no tempo — três, e dois deles não aparecem em tabela nenhuma:**

| Corte | O que muda | Fundamento |
|---|---|---|
| **10/6/1997 ÷ 11/6/1997** | tabela vai "Até 10/6/1997" e "De 11/6/1997 a nov./2021" | MP 1.577/1997 e sucessivas; ADI 2332 citada nas observações |
| **ago./2017** | os compensatórios **deixam de seguir 4.5.3** e passam ao **percentual fixado para os TDAs depositados como oferta inicial** | art. 5º, § 9º, da Lei 8.629/1993, na redação da Lei 13.465/2017 (item 4.5.4, `pagina_pdf` 70) |
| **dez./2021** | **o regime autônomo acaba** — literal: *"Já incluídos na SELIC aplicada aos juros de mora"*. Sem taxa adicional | **D8-C11** |

> **O corte de ago./2017 vive só no item 4.5.4, sobre TDAs complementares.** Nenhuma tabela o
> mostra. É o padrão do § 1 de [`07-leitura-do-corpus.md`](07-leitura-do-corpus.md) aplicado a
> uma cadeia inteira. **D8-C25.**

**Dois defeitos que o motor precisa conhecer:**

- **N-6 — contradição de um mês.** O texto de 4.5.3 diz *"Até dez. 2021, os juros compensatórios
  incidem:"* (`pagina_pdf` 69) e a **tabela encerra o regime autônomo em nov./2021**. Fundamento
  idêntico nas duas cadeias gêmeas. **Dez./2021 fica sem regime coerente** — e é justamente o mês
  da consolidação da EC 113/2021. Não harmonizado: **P8-09**;
- **N-10 — remissão errada.** Em **4.6.3** (indireta), as duas linhas remetem ao *"item 4.5.2"*,
  que é da desapropriação **direta**.

**Não cabem compensatórios em precatório complementar** — **R-08-19**, § 8.1 de
[`06-encargos.md`](06-encargos.md).

**Pendência aberta:** os **honorários de perito** de 4.5.6 têm **três termos iniciais
alternativos** — decisão que os fixou, desembolso da parte, entrega do laudo — **sem critério de
escolha** (`pagina_pdf` 71).

*Origem: `bloco-08-jf-detalhe.md` §§ 3.1 e 3.1.1, `pagina_pdf` 68–71 e 75–76.*

### 5.3.2 FGTS (item 4.8) — cadeia própria, índice **JAM**, e um calendário só dela

**Mesmo modo de falha do § 5.3.1, e foi por isso que esta seção existe:** quem tratou o FGTS pela
linha de correção monetária geral perdeu a cadeia inteira. `JAM` tinha **zero ocorrências** neste
diretório até o bloco 18. JSON: `../tabelas-normativas/cjf.fgts.correcao-monetaria.json` (11
segmentos) e `cjf.fgts.juros-mora.json` (3).

**O critério**, item 4.8, `pagina_pdf` 81, literal: *"os valores apurados deverão ser corrigidos com
base nos critérios adotados para as contas fundiárias (**Juros e Atualização Monetária — JAM**), com
os indexadores seguintes"*. **JAM é o nome do critério, não um indexador** — os indexadores estão na
tabela 4.8.1.1. Não é a tabela JAM da CEF do item 6.14 do TRT-3 (`pr.fgts-indice-jam`), que é outro
manual e outro eixo.

**Duas notas abrem escapes, e a segunda traz um eixo que nenhuma outra cadeia do manual usa:**

| Nota | Literal (`pagina_pdf` 81) | Efeito |
|---|---|---|
| **1** | *"Se o título judicial determinar [...] como dívida comum (ex.: REsp. n. 630.372) e não havendo previsão de índice na sentença, aplicam-se os indexadores previstos para condenações em geral"* | eixo de **conteúdo do título** — a cadeia inteira cede à Seção 4.2 |
| **2** | *"Se o título judicial determinar a correção e juros pelos critérios fundiários **somente até a data do saque integral** (ex.: REsp n. 694.365; AgRg no REsp n. 622.298), devem ser aplicados, **a contar do saque integral** [...] os indexadores previstos para condenações em geral"* | **`D8-C12` — corte por SAQUE INTEGRAL.** Não é competência, não é sentença: é um **fato do contrato de trabalho**. Nenhuma tabela o mostra |

**A cadeia — 11 segmentos, item 4.8.1.1, `pagina_pdf` 82.** Note que a tabela **não tem coluna de
observações**, e por isso **nenhuma linha traz fundamento legal**:

| Período | Indexador | |
|---|---|---|
| jan/1967–fev/1986 | **ORTN** | início **declarado**, não materializado — raro no manual |
| mar/1986–jan/1987 | **IPC** | rótulo **nu**; a poupança escreve `IPC/IBGE` nos mesmos meses |
| **fev/1987** | LBC | segmento de **um mês** |
| mar–jun/1987 | **OTN** | **diverge da poupança (LBC)** |
| jul–set/1987 | LBC – 0,5% | |
| out/1987–dez/1988 | OTN | |
| jan–abr/1989 | **LFT – 0,5%** | é sobre esta linha que a NOTA 2 manda incluir 42,72% |
| maio/1989–mar/1990 | IPC | |
| **abr/1990–jan/1991** | **BTN** | é sobre esta linha que a NOTA 2 manda incluir 44,80% |
| fev/1991–abr/1993 | TRD | |
| maio/1993 → | TR | |

**`D8-C13` / `N-5` — dois conjuntos de expurgos, e o do FGTS não diz o que faz.** NOTA 2,
`pagina_pdf` 82, literal: *"a liquidação deve incluir os expurgos inflacionários reconhecidos pelo
STJ em casos de FGTS: **42,72% em jan./1989 e 44,80% em abr./1990**"*.

| | Capítulo 4 geral | FGTS (4.8.1.1) |
|---|---|---|
| jan/1989 | 42,72% | **42,72%** |
| fev/1989 | **10,14%** | — |
| abr/1990 | — | **44,80%** |
| **operação** | *"Expurgo, **em substituição** ao BTN"*; item 4.1.2.1: *"descontando o BTN ou outro índice utilizado, **evitando bis in idem**"* | **não declarada** |

**Substitui ou acresce? O manual não diz.** As linhas de jan/1989 e abr/1990 **já trazem indexador**
(LFT – 0,5% e BTN) e a tabela **não menciona expurgo algum**. **`N-5` fica aberta**, e por isso os dois
percentuais **não foram gravados como segmento**: gravá-los exigiria escolher entre substituir e somar.

**`D8-C14` — a bifurcação contraintuitiva.** NOTA 1: quem **discute** expurgos só recebe *"os períodos
definidos pelo julgado"*. NOTA 2: quem **não discute** recebe **os dois por padrão**. *Quem discute pode
receber menos do que quem não discute.* Não é erro formal; é o que está escrito.

**`D8-D18` — defeito do original, transcrito como está.** Item 4.8.2, `pagina_pdf` 82: *"art. 4º da
Lei n. 5.107/**1986**"*. A Lei 5.107 é de **13 de setembro de 1966**, como o **próprio item 4.8.1 a
data uma página antes** (`pagina_pdf` 81). **Não corrigido.**

**Os juros remuneratórios de 4.8.2 não são cadeia temporal.** O eixo é a **existência da conta em
22/9/1971** (progressivos de 3/4/5/6%, Súmula 154/STJ) ou o enquadramento no art. 1º da Lei
8.678/1993 (6% a.a.) — não a competência. Registrados no JSON, fora dos segmentos.

**O corte de maio/2000 do FGTS fiscal é de OUTRA cadeia.** O item **2.4.4.1** (`pagina_pdf` 35–36)
trata do FGTS como **dívida fiscal** — débito do **empregador para com o Fundo** — sob o critério
**`JCM`** (*"coeficiente da remuneração das contas vinculadas"*), não `JAM`. Sujeito distinto, sigla
distinta, capítulo distinto. **E o corte da ORTN difere nos três lugares: set/1983 em 2.4.4.1,
fev/1986 em 4.8.1.1, jun/1983 na poupança.** O `D8-C8` (*"De fev./1991 a maio/2000"* × *"A partir de
maio/2000"*, sem desempate) **é de 2.4.4.1 e não alcança 4.8**.

### 5.3.3 Poupança (item 4.9) — 12 segmentos, e o eixo é a **abertura da conta**

JSON: `../tabelas-normativas/cjf.poupanca.correcao-monetaria.json` (12 segmentos) e
`cjf.poupanca.juros-mora.json` (3). Item 4.9.1.1, `pagina_pdf` 84–85.

**Só incide se o título mandar.** Literal, `pagina_pdf` 84: *"**Havendo decisão judicial determinando**
a correção monetária dos valores apurados com base nos critérios adotados para as contas de
poupança"*; **não havendo**, vai para o item 4.2, *"considerando-se como termo inicial o mês em que o
crédito deveria ter sido efetivado na conta"*. E o alcance é a poupança **"livre"** — para vinculada,
programada, a prazo fixo ou de rendimentos crescentes, *"deve-se consultar o juízo"*.

| Período | Indexador | Observação do manual |
|---|---|---|
| até abr/1967 | ORTN | ponta materializada em `1964-01` (Lei 4.380/1964, primeira do item 4.9.1) |
| **maio/1967–jun/1983** | **UPC** | **diverge do FGTS (ORTN) — dezesseis anos e dois meses** |
| jul/1983–fev/1986 | ORTN | *"Fev./1986: ORTN pro rata até 28/2/1986"* |
| mar/1986–jan/1987 | **IPC/IBGE** | o FGTS escreve `IPC` nos mesmos meses |
| **fev–jun/1987** | **LBC** | **diverge do FGTS (OTN) em mar–jun — quatro meses** |
| jul–set/1987 | LBC – 0,5% | |
| out/1987–dez/1988 | OTN | |
| jan–abr/1989 | LFT – 0,5% | |
| maio/1989–mar/1990 | IPC/IBGE | *"Mar./1990: contas com data-base e depósitos efetuados entre 19 e 28/3 – BTNF"* |
| abr/1990–jan/1991 | BTN | *"Jan./1991: BTNF até 31/1/1991 + TRD de 1º/2/1991 até a data do crédito"* |
| fev/1991–abr/1993 | TRD | *"Abr./1993: TRD até 2/5/1993 + TR pro rata de 3/5/1993 até a data do crédito"* |
| maio/1993 → | TR | *"Jun./1994: TR pro rata até 30/6/1994 + TR pro rata de 1º/7/1994 até a data do crédito"* |

**`D8-C15` — a divergência FGTS × poupança soma dezesseis anos e quatro meses**, em duas janelas:
**maio/1967–jun/1983** (FGTS **ORTN** × poupança **UPC**) e **mar–jun/1987** (FGTS **OTN** × poupança
**LBC**). **Nenhuma das duas tabelas traz fundamento legal para a divergência** — a de 4.8.1.1 sequer
tem coluna de observações — e o manual não a explica. **Não harmonizada.** Some-se a ela a divergência
de **rótulo do IPC** (`IPC` × `IPC/IBGE`) nos mesmos meses, em duas janelas.

**Os juros REMUNERATÓRIOS de 4.9.2 — a regra-base, e ela não estava em ponto nenhum da espinha.**
Item **4.9.2**, `pagina_pdf` **86**, campo `JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA.regra` de
`../tabelas-normativas/cjf.poupanca.juros-mora.json`, literal:

> *"**0,5% ao mês** (art. 52 do Decreto n. 24.427/1934; art. 12 do DL n. 2.284/1986; art. 2º da
> Lei n. 8.088/1990 e art. 12 da Lei n. 8.177/1991); **6% ao ano ou fração *pro rata* para
> cruzados novos bloqueados** (art. 6º da Lei n. 8.024/1990; art. 7º da Lei n. 8.177/1991)."*

**São um componente de VALOR, e incidem concomitantemente aos moratórios** — e são
**capitalizados mensalmente** (NOTA 1 do mesmo item, `pagina_pdf` 86; é a exceção a **R4**
enunciada em [`02-atualizacao.md`](02-atualizacao.md) § 8).

> **Achado do bloco 20 — o ponteiro de `L7` não alcançava.** A absolvição dizia *"a espinha não
> silencia: ela aponta"*, e o ponteiro existia; mas o **destino** — esta § 5.3.3 — trazia só a
> **NOTA 2** (contas abertas a partir de maio/2012) e a nota dos cruzados novos **da correção**.
> **A regra-base do 4.9.2 não estava em lugar nenhum**, e o caso que a própria seção nomeia —
> **conta bloqueada, 1990** — chegava ao destino e **não encontrava taxa**. A frase *"Registrados
> no JSON, fora dos segmentos"* é dita da § 5.3.2, sobre **4.8.2 (FGTS)**, não sobre 4.9.2.
> **O ponteiro passou a alcançar**, e é por isso que `L7` segue `ENFRAQUECE`.

**`D8-C16` / `N-11` — o corte da poupança é por DATA DE ABERTURA DA CONTA.** Item 4.9.2, NOTA 2,
`pagina_pdf` 86, literal: *"Tratando-se de **contas abertas a partir de maio/2012** (art. 12 da Lei
8.177/1991 com alterações da MP 567/2012, convertida na Lei 12.703/2012): 0,5% ao mês, caso a taxa
Selic ao ano seja superior a 8,5%; e 70% da taxa Selic ao ano, mensalizada, nos demais casos."*

**A mesma fórmula, e um eixo diferente.** Os itens **4.5.2** e **4.6.2** (juros moratórios das
desapropriações) aplicam **exatamente este cálculo** a partir de maio/2012 — **por competência**.
A poupança o aplica **por abertura da conta**. *Mesmo cálculo, eixos diferentes.* Não harmonizado.
É também por isso que **4.9.2 não virou cadeia temporal**: o schema indexa por competência.

**Uma segunda cadeia que só vive em nota.** NOTA 3 de 4.9.1.1, `pagina_pdf` 85: para **cruzados novos
bloqueados** (Lei 8.024/1990, Plano Collor), *"BTNF desde o bloqueio até jan./1991; e TRD, de fev./1991
em diante"* — **dois trechos que a tabela não mostra**. Mesmo padrão do `N-8`. Não gravados como
segmentos: são **regime alternativo**, não trecho desta linha do tempo.

**Termo inicial por ANIVERSÁRIO.** NOTA 2, `pagina_pdf` 85: *"o dia em que o crédito deveria ter sido
efetivado, aplicando-se, **em cada aniversário, os índices relativos à data-base da conta**"*. A
competência não é o mês civil. Nenhuma outra cadeia de correção do manual tem este eixo.

**`UPC` e `LBC` só aparecem aqui** — e, com `LFT – 0,5%`, `TRD`, `IPC` e `JAM`, entraram no catálogo
como **`indeterminado`** (§ 5.3.4).

**Defeitos do original, transcritos como estão:** **`D8-D19`** — *"AgRg no REsp n. **1.554.66**"*,
número truncado (4.9.2, `pagina_pdf` 86); **`D8-D24`** — *"de **31de** outubro de 1990"* (4.9.1,
`pagina_pdf` 84); **`D8-D25`** — *"REsp"*, *"Resp"* e *"REsp."* na mesma linha (4.9, `pagina_pdf` 84).
E o contraste que **absolve a poupança**: 4.9.2 grafa **"Lei n. 12.703/2012"** corretamente, enquanto
a gêmea 4.5.2 grafa *"Lei n. 2.703/2012"* (`D8-D14`, `pagina_pdf` 68).

### 5.3.4 O que as duas cadeias têm em comum — e o achado do calendário

**Os juros de mora de 4.8.3 e 4.9.3 são a MESMA tabela, palavra por palavra** (`pagina_pdf` 83 e 86):

| Período | Taxa | Fundamento |
|---|---|---|
| até dez/2002 | **0,5% simples** | arts. 1.062, 1.063 e 1.064 do CC/1916 |
| jan/2003–**ago/2024** | **Selic** | art. 406 do CC/2002 |
| **a partir de set/2024** | **taxa legal (Selic − IPCA-15)** | art. 406 do CC, na redação da **Lei 14.905/2024**, e Res. CMN 5.171/2024 |

> **ACHADO — o calendário destas duas cadeias é outro.** Não há corte de **dez/2021** (EC 113/2021)
> nem de **set/2025** (EC 136/2025). A taxa legal entra em **set/2024**, **um ano antes** de todas as
> demais, com fundamento **só** na Lei 14.905/2024 — **sem citar o ARE 1.557.312/SP (Tema 1.419)**,
> que todas as outras cadeias citam.
>
> **Consequência verificada, e ela confirma o § 10:** FGTS e poupança **não estão entre os cinco
> lugares que consolidam em dez/2021**. Varredura: `0,4412` ocorre nas `pagina_pdf` **50, 59, 67, 74 e
> 79** — **nenhuma é 83 ou 86**. A lista de cinco está completa. Transcrito como está.

**`N-7` — a nota autorreferente, e ela se repete quatro vezes.** NOTA 1, alínea *a*, de 4.8.3 e 4.9.3:
*"deve ser capitalizada de forma simples, sendo **vedada sua incidência cumulada com os juros de mora**
e com a correção monetária"* — **e a tabela que ela qualifica É de juros de mora**. **Boilerplate**
copiado da seção de correção monetária; ocorre em **4.2.2 NOTA 1 a), 4.6.2, 4.8.3 e 4.9.3**.
Registrado, não corrigido.

**A alínea *b* é a fórmula D4, não a D2.** *"a partir do mês seguinte ao de **competência da parcela
devida** até o mês anterior ao pagamento, e 1% no mês do pagamento"*. O bloco 8 atribuía a **D4** só à
**dívida fiscal** (§ 5.3, itens 2.3.1.2 e 2.4.2.2.2). **FGTS e poupança também a usam** — a quarta
fórmula tem mais um domicílio do que o registrado.

**A R1 dita pela fonte, com nomes próprios.** NOTA 3 de 4.8.3: pela Selic *"não deve incidir
concomitantemente a correção monetária, já contemplada, mas tão somente [...] os juros
**remuneratórios**"*. NOTA 3 de 4.9.3 diz o mesmo trocando "correção monetária" por **"remuneração
básica"**. É a exclusividade de englobamento escrita pelo manual — e ela **preserva** os juros
remuneratórios por fora.

**`tipo_indexador` — sete rótulos novos, todos `indeterminado`.** `JAM`, `UPC`, `LBC`, `LBC – 0,5%`,
`LFT – 0,5%`, `TRD` e `IPC` entraram em
`../tabelas-normativas/indexadores-tipo-catalogo.json` com `tipo_indexador_pendencia: "P18-01"` e
`fonte: null`. **Nenhum está na lista do item 4.1.2.4**, e a busca de ausência está declarada no
próprio catálogo (`ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_18`). Três notas de método:

- **`JAM` não é indexador** — é o nome do critério. Registrado porque o rótulo circula como se fosse;
- **`UPC`** — o item 2.4.4.1 **expande a sigla** (*"Unidade Padrão de Capital (UPC)"*), o que é
  **rotulagem, não classificação**. Achar fonte é citar item e `pagina_pdf`, não expandir a sigla;
- **`IPC` nu ≠ `IPC/IBGE`** — a `identificacao_declarada` que o catálogo usou para `INPC/IBGE` tinha
  por fundamento *"não existe INPC de outro emissor"*. **Para o IPC o pressuposto é falso:** o próprio
  manual usa **IPC/FGV** no item 4.5.1.1. É a mesma classe de erro que o bloco 8 registrou ao trocar
  IPC/FGV por IPC/IBGE entre 78 segmentos.

*Origem: PDF `pagina_pdf` 81–87 (itens 4.8 e 4.9) e 35–36 (item 2.4.4.1), relidos integralmente;
`bloco-08-jf-detalhe.md` §§ 3.2, 3.3 e 4 (`N-5`, `N-7`, `N-11`).*

### 5.3.5 Os JSON: por que gerei quatro, e por que **não** gerei as outras oito

**Gerei** — `cjf.fgts.correcao-monetaria` (11 segmentos), `cjf.fgts.juros-mora` (3),
`cjf.poupanca.correcao-monetaria` (12) e `cjf.poupanca.juros-mora` (3), no schema `cadeia-temporal`
exato das sete existentes. **Razão:** as quatro são tabelas **período → indexador/taxa** contíguas,
exatamente a forma que o schema expressa; deixá-las em prosa repetiria o modo de falha que esta seção
existe para reparar — **prosa não é lida pelo validador**. Gerador em
`scripts/calculo/gera_cadeias_bloco18.py` (sem `float`; `encoding='utf-8'` explícito).

**Não gerei as oito de `P18-02`** (4.5.2, 4.5.3, 4.6.1.1, 4.6.2, 4.6.3, 2.3.2.2, 2.4.2.2.2, 2.4.4.1).
**Razão declarada:** estão fora do escopo desta tarefa, e três delas exigem decisão de modelagem que
não cabe decidir de passagem — **2.3.2.2 e 2.4.2.2.2 precisam do campo `base_incidencia`** (`D8-C5`:
a base alterna quatro vezes entre originário e corrigido) e **2.4.4.1 é lista, não tabela**, com o
`D8-C8` em aberto. **A ausência está registrada, não silenciada.**

> **Superado em parte na tarefa 3 do bloco 19 — § 5.3.6.** Cinco das oito foram geradas; **três seguem ausentes** (4.5.2, 4.6.2, 2.4.2.2.2), e por falta de **fonte**, não de schema: o campo `base_incidencia` **existe e está em uso**.

**Os novos baselines dos validadores** — `scripts/calculo/valida_cadeias.py`, que descobre cadeia por
`tipo == "cadeia-temporal"` e portanto absorveu os quatro arquivos sem alteração de código:

> **As tabelas *antes × depois* desta subseção são REGISTRO DATADO e NÃO se atualizam** — uma
> variação só é auditável se as duas pontas ficarem como estavam. **O placar corrente está em
> [`00-numeros.md`](00-numeros.md) § 3**, gerado por script.

| | antes | **depois** |
|---|---|---|
| cadeias | 11 | **15** |
| **R1** | **15** | **15** — *inalterado* |
| **R2** | **1** | **1** — *inalterado* |
| **R3** | 25 | **46** (+21) |

**R1 e R2 não se moveram, e isso é resultado, não sorte.** As duas cadeias de correção do bloco 18
são **perfeitamente contíguas** — fim e início nunca caem no mesmo mês, ao contrário do tronco comum
do capítulo 4 (jan/1989 e mar/1990). **FGTS e poupança não têm o problema de sobreposição que
justifica o argumento dos índices nominais do item 2.3.1.3.**

**As 21 violações novas de R3, uma a uma:**

| Cadeia | R1 | R2 | R3 | R3-INDETERMINADO |
|---|---|---|---|---|
| `cjf.fgts.correcao-monetaria` | 0 | 0 | **0** | **10** |
| `cjf.fgts.juros-mora` | 0 | 0 | 0 | 0 |
| `cjf.poupanca.correcao-monetaria` | 0 | 0 | **2** | **9** |
| `cjf.poupanca.juros-mora` | 0 | 0 | 0 | 0 |

- **19 são `R3-INDETERMINADO`** — o validador dizendo *"não posso verificar"*, porque uma das pontas
  da virada é um dos sete rótulos sem fonte. **Não são defeito do manual nem da modelagem: são a
  pendência `P18-01` tornada visível.** Se `UPC`, `LBC`, `LFT` e `TRD` fossem classificados por
  dedução, as 19 sumiriam **e a dedução passaria limpa** — que é exatamente o que o bloco 17 proibiu;
- **2 são `R3` cheia**, e **as duas são do manual**, na cadeia da poupança: `1986-03` ORTN
  (**nominal**) → IPC/IBGE (**percentual**) e `1990-04` IPC/IBGE (**percentual**) → BTN (**nominal**),
  ambas **sem `aplicacao` declarada**. É o mesmo padrão que as cadeias do tronco comum já exibem em
  jan/1989 e mar/1990 — **troca de tipo sem ajuste de defasagem, que desloca o cálculo em um mês**
  (item 4.1.2.4, `pagina_pdf` 42). **Transcritas, não harmonizadas.** A cadeia do FGTS **não** as tem,
  e só porque o `IPC` nu é `indeterminado`: **classificá-lo criaria duas R3 a mais, não menos**.

**`P18-01`** — sete rótulos sem classificação em fonte alguma (`JAM`, `UPC`, `LBC`, `LBC – 0,5%`,
`LFT – 0,5%`, `TRD`, `IPC`). **`P18-02`** — oito cadeias tabuladas do manual sem JSON, **hoje três**
(§ 5.3.6). **`N-5`** e
**`D8-C13`** continuam **abertas**: nada aqui as resolve.

### 5.3.6 `P18-02` — **cinco geradas, três bloqueadas**, e as cinco decisões

**Bloco 19, tarefa 3.** Gerador: `scripts/calculo/gera_cadeias_bloco19.py` (sem `float`;
`encoding='utf-8'` explícito). As oito cadeias de `P18-02` foram reexaminadas uma a uma contra a
**fonte extraída**, e o critério foi um só: **segmento sai da fonte, com `fundamento` e
`pagina_pdf`; onde a fonte não trouxe, o campo fica `null` com a razão** — não se inventa valor, e
não se reconstrói estrutura.

> **O critério valia para `taxa` e não valia para `fundamento` — corrigido.** `pagina_pdf` está em
> 100% dos segmentos e `taxa` foi tratada com o rigor prometido (`taxa: null` + `taxa_nao_extraida`),
> mas `fundamento` simplesmente **sumia do segmento**: ausência **sem razão**, indistinguível de
> esquecimento. Nas **cadeias novas deste bloco** o campo passa a sair como **`fundamento: null` +
> `fundamento_nao_extraido`** — **13 segmentos**: 7 de 8 em `cjf.divida-fiscal.juros-mora`, 4 de 5 em
> `cjf.fgts-divida-fiscal.correcao-monetaria` e 1 de 3 em **cada** cadeia de
> `juros-compensatorios`. Quem faz isso é `declara_fundamento_ausente`, em
> `gera_cadeias_bloco19.py`.
>
> **Os 8 de `cjf.desapropriacao-indireta.correcao-monetaria` NÃO foram consertados, e a razão é
> declarada:** eles são **derivados** de `cjf.desapropriacao-direta.correcao-monetaria.json`, onde já
> estavam assim desde o **bloco 8** — são **pré-existentes, não deste bloco**. Convertê-los aqui
> seria assumir defeito alheio como próprio **e** fazer o derivado **divergir da origem**, que é
> exatamente o que `DERIVADA_DE` existe para impedir. Fica registrado no próprio campo
> (`DERIVADA_DE.FUNDAMENTO_AUSENTE_E_PRE_EXISTENTE`) e **fecha junto com a direta**, num bloco que a
> revisite. **A ausência é mais larga que estas duas cadeias** — no repositório inteiro são **77
> segmentos sem `fundamento`, em 11 cadeias**, quase todos anteriores ao bloco 19; este bloco
> responde **pelos seus 13**.

| Cadeia gerada | Item | Segmentos |
|---|---|---|
| `cjf.desapropriacao-indireta.correcao-monetaria` | 4.6.1.1 | **11** |
| `cjf.divida-fiscal.juros-mora` | 2.3.2.2 | **8** |
| `cjf.fgts-divida-fiscal.correcao-monetaria` | 2.4.4.1 | **5** |
| `cjf.desapropriacao-direta.juros-compensatorios` | 4.5.3 | **3** |
| `cjf.desapropriacao-indireta.juros-compensatorios` | 4.6.3 | **3** |

**As três que ficaram de fora, e por quê:**

- **4.5.2 e 4.6.2 — juros de mora das desapropriações.** A tabela **nunca foi extraída linha a
  linha**, e o corpus o declara **com escopo**, duas vezes (`references/desapropriacao.md` §§ 3 e
  10: *"Não infiro os segmentos ausentes"*). O que existe são **quatro marcas soltas** — o eixo
  26/9/1999 ÷ 27/9/1999 (que é **condição por data da sentença**, não fronteira de período), a
  fórmula da poupança de maio/2012 **por competência**, a Selic de dez/2021 e a taxa legal de
  set/2025 — mais a informação de que a tabela tem **cinco linhas**. **Nenhuma taxa anterior a
  maio/2012 está registrada**, e mapear cinco linhas sobre quatro marcas é **reconstruir a
  estrutura**, que é pior do que inventar um valor;
- **2.4.2.2.2 — juros da contribuição previdenciária.** Do item, a fonte extraída tem **uma frase**:
  a ressalva do `N-2`, `pagina_pdf` 33. Sem períodos, sem taxas, sem bases. Copiar 2.3.2.2 porque
  *"é quase igual à do IR"* seria **herança por analogia** — e a analogia é frágil **pela própria
  fonte**, porque o `N-2` existe justamente para registrar que **as duas tabelas irmãs não são
  idênticas**.

> **O campo `base_incidencia` deixou de ser o bloqueio.** `P18-02` dizia que 2.3.2.2 e 2.4.2.2.2
> *"exigem `base_incidencia`"*. **Exigiam, e o campo existe e está em uso** (decisão 4). O que
> bloqueia 2.4.2.2.2 é **fonte**, não schema.

**E 4.7.1 não entra: registra-se a DELEGAÇÃO, não a ausência.** O manual não tem tabela de correção
trabalhista; a NOTA 2 manda *"utilizar a tabela de coeficientes trabalhistas expedida pelo Tribunal
Superior do Trabalho"* (`pagina_pdf` 77). A cadeia vive numa **série**, não numa regra — desenho do
`P9-02`. **Não há nada a extrair, e dizer que falta seria afirmar ausência do que a fonte nunca
prometeu.**

#### As cinco decisões

**1. Desapropriação indireta — DUAS cadeias, não uma com dois escopos.** O eixo que separa direta de
indireta é a **modalidade**, e modalidade **não é eixo da linha do tempo**: o que ela muda é o
**termo inicial**, campo de *cadeia*, enquanto `condicao` e `dominio_condicoes` são campos de
*segmento*. Carregar modalidade em `condicao` obrigaria a repeti-la nos 11 segmentos para dizer que
não muda nenhum deles — **e ainda assim não alcançaria o termo inicial, que é onde a diferença
mora** (`D8-C10`). Somem-se as divergências fora da correção (juros fechando em nov/2021 ×
dez/2021, o `N-10` de 4.6.3) e a regra do bloco 17 — o identificador identifica, e
`cjf.desapropriacao-direta.*` já existe, com o manifesto tratando perda de `id` como regressão.
**O único argumento contrário era a duplicação, e ele foi pago:** os 11 segmentos da indireta são
**derivados em tempo de geração** do arquivo da direta (campo `DERIVADA_DE`) — **conteúdo idêntico
derivado não diverge**.

**2. Os compensatórios e o corte de ago/2017 — NÃO É TABULÁVEL, e é isso que fica escrito.** A taxa
do regime é *"o percentual fixado para os TDAs depositados como oferta inicial"*: **valor do caso**,
fixado no ato de oferta — não índice publicado, não série, não percentual legal. Gravá-lo como
segmento exigiria um número que **não existe em fonte alguma para caso nenhum**; e gravá-lo com
`taxa: null` sobre 2017-08..2021-11 **sobrescreveria a linha *"De 11/6/1997 a nov./2021"* que a
tabela declara** — trocando um fato do manual por uma regra de outro item (`D8-C25`: o corte vive só
em 4.5.4). Fica em **campo de cadeia**, com o literal; quem calcula **pergunta** o percentual (R21) e
**registra** a resposta (R19).

**3. `N-6` — grava-se a TABELA, e a contradição fica legível.** O texto de 4.5.3 diz *"Até dez.
2021"*; a tabela encerra em **nov/2021**. **Os segmentos são a tabela**, e o texto de abertura é
enunciado de seção, não linha: gravar dez/2021 criaria uma sobreposição que **o manual não tem** e
resolveria `N-6` por escolha. **Não se escolhe lado.** As duas leituras ficam no JSON e a conta que
atravesse dez/2021 grava qual aplicou. **`P8-09` segue aberta.**

**4. `base_incidencia` — campo novo, e o schema o acomoda sem tocar no validador.** É campo de
*segmento* e diz **sobre que valor a taxa incide** — originário × corrigido (*"cor/mon."*) —,
dimensão **ortogonal** a período, indexador e englobamento. `Segmento.de_dict` lê uma lista fechada
de campos e ignora os demais, de modo que **R1, R2 e R3 seguem exatas** e o dado fica gravado para
quem calcula. **Não se acrescentou campo ao validador**: R1/R2/R3 não têm o que fazer com a base, e
pôr no dataclass um campo sem regra que o consuma é cerimônia. `D8-C5` está inteiro no JSON: a base
alterna **quatro vezes**, e **só a dívida fiscal a exercita**.

**5. O FGTS fiscal é outra cadeia, e o `id` o diz.** `cjf.fgts-divida-fiscal.correcao-monetaria` ×
`cjf.fgts.correcao-monetaria`. **Sujeito distinto** (o Fundo é credor aqui; o titular da conta, lá),
**capítulo distinto**, **critério distinto** e até o **corte da ORTN distinto** — set/1983 aqui,
fev/1986 em 4.8.1.1, jun/1983 na poupança. Regra do bloco 17 aplicada nas duas pontas: **o
identificador identifica** — `fgts-divida-fiscal` diz qual cadeia é — e **o escopo se declara em
campo**: `criterio: "JCM"`, `tipo_acao`, `ESCOPO`. **A sigla do critério não entrou no `id`**, porque
sigla é rótulo e rótulo muda. **O corte de maio/2000 (`D8-C8`) é dele e está gravado nele; a cadeia
de 4.8 não tem corte em maio/2000, e o JSON diz isso com todas as letras.**

#### `tipo_indexador` — dois rótulos novos, os dois `indeterminado`

**Nenhum foi classificado por semelhança de nome nem por herança**, e os dois entraram no catálogo:

| Rótulo | Onde | Por quê |
|---|---|---|
| **`BTNF`** | FGTS fiscal, 1989-11..1991-01 | **não está** no item 4.1.2.4 — que nomeia o **BTN**, não o BTNF — e nada no corpus o classifica. Herdar *"nominal"* do BTN é a mesma classe de erro de `IPC` × `IPC/IBGE`. **Sem fonte: `P19-02`** |
| **`UPC → índices básicos de atualização dos saldos da poupança`** | FGTS fiscal, 1983-10..1989-10 | **segmento composto**: o item 2.4.4.1 lista os dois indexadores e **não data a fronteira**. A cura é **partir o segmento** quando a fonte der a data, não classificá-lo. **`P17-03`**, como `Ufir → Selic` |

**`JCM` e `TDA` continuam fora do catálogo de indexadores, e agora com a razão fechada:** `JCM` é
**nome de critério** e vive no campo `criterio` da cadeia — que **deixou de ser ausente**; `TDA` é
**objeto de direito material**, e o corte de ago/2017 que o invoca **não é tabulável** (decisão 2).
Escopo da busca de ausência declarado no catálogo, chave
`ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_19_TAREFA_3`.

#### Os baselines — e por que cada um se moveu

| | antes (bloco 19, T2) | **depois (T3)** |
|---|---|---|
| cadeias | 15 | **20** |
| **R1** | **15** | **21** (+6) |
| **R2** | **1** | **1** — *inalterado* |
| **R3** | **51** | **62** (+11: **5** `R3` cheia + **6** `R3-INDETERMINADO`) |

**As 6 violações novas de R1, uma a uma — e nenhuma é modelagem:**

| Cadeia | Mês | O que é |
|---|---|---|
| `cjf.desapropriacao-indireta.correcao-monetaria` | **1989-01** e **1990-03** | as **mesmas duas** da gêmea direta, e pelo mesmo motivo: OTN × IPC/IBGE e BTN × IPC/IBGE. A de jan/1989 o manual explica (`R-08-04`); a de mar/1990 **não** (`D8-C21`) |
| `cjf.desapropriacao-direta.juros-compensatorios` · `...-indireta...` | **1997-06** (×2) | **corte intramensal**: a fronteira do manual é **10/6/1997 ÷ 11/6/1997**, e o schema indexa por **mês**. Escolher um dos dois meses seria harmonizar |
| `cjf.divida-fiscal.juros-mora` | **1992-01** | **corte intramensal**: *"a 2/1/1992"* × *"de 3/1/1992"*. É o `D8-C6`, o mês sem juros por falta de lei, encostando na TRD |
| `cjf.fgts-divida-fiscal.correcao-monetaria` | **2000-05** | **`D8-C8`** — *"De fev./1991 a maio/2000"* × *"A partir de maio/2000"*, **sem regra de desempate**. O bloco 8 já a listava como sobreposição que a checagem não pegava **porque a cadeia não existia**. Agora existe, e a checagem pega |

> **Três das seis são cortes por DIA numa modelagem por MÊS.** Não são defeito do manual nem erro da
> extração: são a **granularidade do schema** encontrando a granularidade da fonte. Registradas no
> campo `CORTE_INTRAMENSAL` de cada segmento.

**R2 não se moveu, e isso foi decidido.** A tabela de 2.3.2.2 traz a bifurcação Selic/TMMCTN
**dentro de uma única linha** — quem a desdobra é a de correção, 2.3.1.2. Marcar o segmento com
`condicao` criaria um ramo sem gêmeo e **abriria lacuna** no universo incondicional; declarar
`dominio_condicoes` para fechá-la seria **afirmar exaustividade de um domínio que esta tabela não
enumera**. O eixo ficou em `eixo_declarado`, campo de registro.

**As 11 de R3:** **5 cheias**, todas na indireta de correção e **todas herdadas da direta** —
jan/1989, mar/1989, mar/1990, 2001-01 (Ufir → IPCA-E, `nominal × janela-deslocada`) e 2025-09
(Selic → IPCA-15); **6 `R3-INDETERMINADO`**, sendo 2 na indireta (as pontas do IPC/FGV) e **4 no
FGTS fiscal**, que é uma cadeia de **quatro rótulos indeterminados em cinco segmentos**. **As quatro
do FGTS fiscal são `P18-01`, `P19-02` e `P17-03` tornadas visíveis** — classificá-los por dedução as
faria sumir, e a dedução passaria limpa.

**As duas cadeias de compensatórios não produzem R3 alguma**, e isso é resultado: **não têm
indexador**. A regra do manual ali é percentual de juros, não índice — `nao-indexador`. **O que
falta nelas não é classe, é o VALOR da taxa**, e ele está gravado como ausente.

> **`P18-02` encolhe de oito para três.** `P18-01`, `N-5`, `D8-C8`, `D8-C13`, `D8-C25`, `N-6` e
> `N-10` continuam **abertas**: nada aqui as resolve, e **nenhuma foi harmonizada**.

### 5.4 `C14-01` — `SUPERADO`, com a refutação registrada

A EC 136/2025 reescreveu o art. 3º da EC 113/2021. **Regra vigente na espinha:** requisitórios
da Fazenda **federal**, da expedição ao pagamento — **IPCA** + **juros simples de 2% a.a.**,
com **trava**: se a soma superar a Selic do período, aplica-se a Selic.

**Três estreitamentos simultâneos:** objeto (discussões e condenações → só requisitórios); ente
(toda Fazenda → só federal); período (do início → da expedição).

> **Refutação registrada, e a fonte é interna.** `bloco-13c-sindical-precatorios.md` § 7 afirma
> que *"a EC 113/2021 art. 3º alcança apenas requisitórios federais"*. **Está errado:** o § 5 da
> base transcreve a redação original — *"independentemente de sua natureza"*, sem a palavra
> "federal". A restrição é criação da **EC 136/2025**. Não corrigido na base; registrado aqui.

**Regra de incidência (CNJ, Provimento 207/2025), assimétrica:** o IPCA incide sobre
**principal e juros somados**; os 2% a.a. incidem sobre o **principal, excluídos os juros já
apurados**. É especificação de implementação, **não decorre da leitura da emenda**.

### 5.5 `C14-02` — `BIFURCADO`, eixo = expedição do requisitório ⊕ ente devedor

**Sobrevivem quatro regras estruturais do cap. 14 do manual**, independentes da EC 62/2009 e
não tocadas pelas ECs 113 e 136: (a) suspensão dos juros no prazo constitucional de pagamento;
(b) juros de 0,5% a.m. desde ago/2001; (c) exclusão de juros compensatórios; (d) exceção à
precedência do título. **Não sobrevive** o índice.

**Cadeia do CJF no requisitório complementar** (R-08-17, `pagina_pdf` 89): o indexador troca
**três vezes** — original até a apresentação → administrativo no prazo constitucional →
**novamente o original** depois. Governada pelo **estado da requisição**, não pela competência.

**Data de apresentação do precatório:** 1º de julho até 2021; **2 de abril a partir de 2022**.

**Fase pré-requisitório:** vácuo preenchido pelo CC — STJ, REsp 2.236.270/SP (pub. 02/03/2026);
STF, ARE 1.557.312/SP (Tema 1.419); CJF, Res. 990/2026 encerra a Selic a partir de **set/2025**.

**Divergência registrada, não resolvida:** TJ-SP, 2ª Câmara de Direito Público
(AI 3001155-79.2026.8.26.0000) mantém a Selic para débitos não submetidos a precatório.
**ADI 7873 pendente.** Fazenda **estadual e municipal** fica sem a regra antiga (revogada) e sem
a nova (que não a alcança) — **lacuna normativa, não pendência de pesquisa**.

### 5.6 `C14-03` — `INAPLICÁVEL`, com a razão registrada

Aplicabilidade do regime de precatórios ao caso do produto. **Razão:** prejudicialidade — depende
de classificar a devedora como Fazenda Pública ou não, que é a **Pendência 1** de
`../00-base-normativa.md` § 9, qualificada como *"pergunta ao jurídico do usuário do módulo"*.
**C14-01 e C14-02 são condicionais a ela.** Busca declarada do bloco 13C: `economia mista` tem
**zero ocorrências nas 471 páginas** do Manual TRT-3; a única equiparação nominada é a ECT, e só
*"para efeito de execução e do DL 779/1969"*.

---

## 10. Consolidação de dez/2021 — cinco lugares, três valores de fechamento

Literal, `pagina_pdf` 50 (repetido com redação quase idêntica em 59, 67, 74 e 79):

> "a) o crédito será consolidado tendo por base o mês de dez./2021 pelos critérios de juros e
> correção monetária até então aplicáveis, considerando, para esse fim, o [índice] de nov./2021
> ([x]%) e os **juros de dez./2021 (0,4412%)**; b) sobre o valor consolidado do crédito em
> dez./2021, **sem exclusão de qualquer parcela**, incidirá a taxa Selic a partir de jan./2022
> (competência dez./2021) (§ 1º do art. 22 da Res. CNJ n. 303/2019, com redação dada pelo art.
> 6º da Res. CNJ n. 448/2022); c) o valor resultante [...] denominado 'Juros Selic', deve ser
> **integralmente somado à parcela denominada 'Juros até 12/2021'**."

| Ramo | Índice de nov/2021 | Valor | Juros de dez/2021 | Item | `pagina_pdf` |
|---|---|---|---|---|---|
| Condenatórias em geral | IPCA-E | **1,17%** | 0,4412% | 4.2.1, NOTA 5 | **50** |
| Benefícios previdenciários | INPC | **0,84%** | 0,4412% | 4.3.1, NOTA 5 | **59** |
| Desapropriação **direta** | IPCA-E | **1,17%** | 0,4412% | 4.5.1.1, NOTA 2 | **67** |
| Desapropriação **indireta** | IPCA-E | **1,17%** | 0,4412% | 4.6.1.1, NOTA 2 | **74** |
| Ações trabalhistas (JF) | **TR** | **0,00%** | 0,4412% | 4.7.2, NOTA 2 | **79** |
| Repetição de indébito | — | **não consolida** | — | 4.4.1.1, NOTA 4 | 64 |

**Três valores de fechamento, cinco lugares, uma dispensa.** Os juros de dez/2021 são os mesmos
(**0,4412%**) nos cinco; o índice assume **três** valores. **A TR trabalhista de 0,00% significa
que, nesse ramo, o principal não se move em nov/2021.**

**A repetição de indébito não consolida** — literal, `pagina_pdf` 64: *"não altera o cálculo
[...] sendo, portanto, desnecessário consolidar"*, porque já observa a Selic desde jan/1996.

**"Sem exclusão de qualquer parcela"**: a Selic incide sobre o consolidado inteiro, principal
**e** juros. Nos exemplos (`pagina_pdf` 51) há duas linhas de dez/2021 — principal corrigido
R$ 2.275,96 e juros R$ 55,75 — **ambas recebendo 5,05% de Selic**.

> **Verificação por varredura:** `0,4412` ocorre nas páginas **50, 59, 67, 74 e 79**. A primeira
> redação do bloco 08 listava **quatro** lugares e três ramos; são **cinco** — as duas
> desapropriações ficaram de fora.

---

## 11. Atualização do DEPÓSITO — **três regimes, conforme a natureza** (`A17`)

**Achado `A17`, promovido a `BLOQUEIA` no bloco 20.** Manual TRT-3, **capítulo 16**,
`pagina_pdf` **329** — `../extracao/trabalhista/bloco-13e-capitulo16.md` § 5. **A dedução do
depósito é passo do cálculo** (passo **11** de [`09-ordem-de-calculo.md`](09-ordem-de-calculo.md)
§ 3, item 10.3.1 letra **E**), e **qual regime se aplica muda o número deduzido**.

| Natureza do depósito | Critério de atualização |
|---|---|
| **judicial** | critérios da **caderneta de poupança** — **TR + 0,5% a.m.** |
| **recursal** | critérios do **FGTS** — **TR + 3% a.a.** |
| **crédito trabalhista** (o exequendo) | **art. 39 da Lei 8.177/1991** — **TR + 1% a.m. simples** |

**São três taxas diferentes sobre o mesmo eixo de tempo**, e o discriminante não é a competência:
é a **natureza do depósito**. Quem atualizar um depósito recursal pela régua do crédito troca
**3% a.a.** por **1% a.m.** — doze pontos percentuais ao ano de diferença sobre o valor
depositado, e o resultado é o **saldo**, não uma linha acessória.

> **Por que isto era lacuna, e por que escapou de duas peneiras.** A § 6.4 de
> [`10-literais-na-extracao.md`](10-literais-na-extracao.md) classificara `A17` como *"lacuna de
> REGRA, não de entidade"*, porque o **termo** `depósito recursal` ocorre no consolidado
> ([`05-imputacao.md`](05-imputacao.md) § 4). **O fato é verdadeiro e a consequência não se
> sustentava:** o termo estar lá qualificando o alcance do item "i" da ADC 58 **não põe os três
> regimes em lugar algum**. Busca literal nos arquivos do consolidado por `TR + 3% a.a.`,
> `3% ao ano`, `TR +` e `poupança … 0,5%`: **zero ocorrências**. E a classificação fez `A17`
> escapar **das duas varreduras** — não entrou na reauditoria dos dez (que cobriu `L1`–`L13`) nem
> na varredura de entidade (excluída pelo critério do termo). **Uma regra que não está em peneira
> nenhuma não é "registrada como insumo": é lacuna.**

**Eixo vizinho, e NÃO é o mesmo.** [`05-imputacao.md`](05-imputacao.md) § 5 registra as **três
posições sobre a DATA da dedução** (levantamento, depósito ou cálculo). Aquilo é **quando**
deduzir; isto é **com que régua o depósito chega até lá**. As duas perguntas são independentes, e
errar qualquer uma muda o saldo.

---

