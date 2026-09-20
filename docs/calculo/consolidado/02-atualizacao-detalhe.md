# Atualização — detalhe

As cadeias da Justiça Federal segmento a segmento, as quatro fórmulas de `aplicacao` do CJF, e a consolidação de dezembro de 2021 nos cinco lugares em que ocorre.

Companheiro de [`02-atualizacao.md`](02-atualizacao.md). **Offset de paginação zero** no manual do TRT-3; `pagina_pdf = impresso + 1` no do CJF.

---
## 5. Justiça Federal — as cinco cadeias do CJF

Fonte: Manual CJF, Res. 990/2026 — `../extracao/justica-federal/bloco-08-jf.md`;
JSON em `../tabelas-normativas/cjf.*.json`. **Única fonte do corpus cuja edição está vigente.**

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

### 5.3 As quatro fórmulas de `aplicacao` do CJF

| # | Regra | Onde |
|---|---|---|
| **D1** | Selic **no mês posterior ao de sua competência, inclusive no mês de pagamento** | Fazenda, a partir de dez/2021 |
| **D2** | Selic **do mês seguinte ao termo inicial dos juros até o mês anterior ao pagamento, e 1% no mês do pagamento** | não-Fazenda; e Fazenda jan/03–jun/09 |
| **D3** | do mês seguinte ao **recolhimento indevido** até o mês anterior à repetição, e 1% no mês | repetição de indébito |
| **D4** | do mês seguinte à **competência da parcela** até o mês anterior ao pagamento, e 1% no mês | dívida fiscal |

**D1 e D2 dão resultados diferentes sobre a mesma série.** A taxa legal segue **D1**
(item 4.2.2, NOTA 7, `pagina_pdf` 56).

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

