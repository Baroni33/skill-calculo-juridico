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
| **2.3.2.2** | **juros — dívida fiscal**, 8 linhas, com `base_incidencia` | **não** | detalhe § 2.2 do bloco 8 | **cadeia AUSENTE** — `P18-02` |
| 2.3.3.2 · 2.4.2.3 · 2.4.4.2 · 2.4.5.2/.3 | multas por período | não | parcial | **não é atualização** — fora do componente |
| 2.4.2.1.2 | correção — contribuição previdenciária | não | detalhe § 2.3 | **remissão + janela própria**: *"mesmos critérios do IR, item 2.3.1.2"*, mais o vácuo fev–mar/1997. Cadeia derivada |
| **2.4.2.2.2** | **juros — contribuição previdenciária** | **não** | detalhe § 2.3 | **cadeia AUSENTE** — `P18-02` |
| **2.4.4.1** | **FGTS fiscal (`JCM`)** | **não** | § 5.3.2 (agora) | **cadeia AUSENTE, e é OUTRA que a de 4.8** |
| 2.4.5.1 | juros — Incra | não | — | **remissão** a 2.3.2.2 a partir de maio/1990; só a linha "até abr/1990" é própria |
| 2.6 · 2.7.1.1 · 2.8.5 | conselhos, foro/laudêmio, multas adm. | não | detalhe § 2.5 | **remissão** a 2.3.1.2 — não é lacuna |
| 2.9 | falência | não | detalhe § 2.6 | **não é cadeia** — `D8-C23`, segmento condicional a evento futuro |
| 4.2.1.1 · 4.2.2 | condenatórias | **sim ×2** | §§ 5.1–5.2 | ok |
| 4.3.1.1 | previdenciário | **sim** | § 5.2 | ok |
| 4.4.1.1 | repetição de indébito | **sim** | § 5.2 | ok |
| 4.5.1.1 | correção — desapropriação **direta** | **sim** | § 5.2 | ok |
| **4.5.2** | **juros de mora — desapropriação direta**, 5 linhas | **não** | § 5.3.1 (em prosa) | **cadeia AUSENTE** — `P18-02` |
| **4.5.3** | **juros compensatórios — direta**, 4 linhas | **não** | § 5.3.1 (bloco 15) | **cadeia AUSENTE, recuperada em prosa e ainda sem JSON** |
| 4.5.4–4.5.9 | TDAs, honorários, custas | não | § 5.3.1 | **não são cadeia** — `D8-C25` vive só em 4.5.4 |
| **4.6.1.1** | correção — desapropriação **indireta** | **não** | § 5.2 (só a direta) | **cadeia AUSENTE — e é IDÊNTICA à de 4.5.1.1**, inclusive no IPC/FGV |
| **4.6.2** | **juros de mora — indireta** | **não** | § 5.3.1 | **cadeia AUSENTE.** Fecha em **dez/2021**, e a gêmea 4.5.2 em **nov/2021** |
| **4.6.3** | **juros compensatórios — indireta** | **não** | § 5.3.1 | **cadeia AUSENTE.** Carrega o `N-10` (remete a *"item 4.5.2"*, da direta) |
| **4.7.1** | correção — ações trabalhistas | **não** | § 6 | **NÃO É LACUNA — não existe tabela.** Só lista de leis, e a NOTA 2 **delega**: *"utilizar a tabela de coeficientes trabalhistas expedida pelo TST"*. Mesmo desenho do `P9-02`. A cadeia vive numa **série**, não numa regra |
| 4.7.2 | juros — trabalhista | **sim** | § 5.2 | ok |
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
`tabelas-normativas/`. **Registradas como `P18-02`, não geradas neste bloco** — ver § 5.3.5.

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

**Os novos baselines dos validadores** — `scripts/calculo/valida_cadeias.py`, que descobre cadeia por
`tipo == "cadeia-temporal"` e portanto absorveu os quatro arquivos sem alteração de código:

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
`LFT – 0,5%`, `TRD`, `IPC`). **`P18-02`** — oito cadeias tabuladas do manual sem JSON. **`N-5`** e
**`D8-C13`** continuam **abertas**: nada aqui as resolve.

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

