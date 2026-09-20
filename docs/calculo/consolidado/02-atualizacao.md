# Espinha consolidada — atualização monetária e juros

**Bloco 15, fusão.** Não é extração: funde o que está espalhado nos blocos 08, 09, 11 e na
base normativa, **aplicando os vereditos** de `../confronto-normativo/01-vereditos.md`.

**Chave primária:** `00-calendario-de-cortes.md` — o par `(data, eixo)`, não a data.

**Regra de leitura, que governa o arquivo inteiro:**

| Veredito | Tratamento aqui |
|---|---|
| `VIGENTE` | entra como está |
| `SUPERADO` | a **regra vigente** entra na espinha; a do manual vai para `../armadilhas-comparador.md` **com a data de corte** |
| `BIFURCADO` | **as duas entram**, com corte e eixo. Competência anterior ao corte **usa a antiga** |
| `INAPLICÁVEL` | fora, com a razão registrada |
| `SEM FONTE` | pendência, nunca regra |

> **O erro que este arquivo existe para não cometer:** tratar bifurcação como substituição.
> `CH-01` a `CH-05` são **`BIFURCADO`**, e o `status_norma: "superado"` gravado nos JSON
> `trab.hist.*` está **certo quanto ao futuro e incompleto quanto ao passado** — ver § 9.

---

## 1. As cadeias, por jurisdição e por qualidade do devedor

| # | Jurisdição | Devedor | Cadeia vigente | Cadeia histórica |
|---|---|---|---|---|
| 1 | Trabalhista | privado | § 2.1 | § 2.2 (`trab.hist.*`) |
| 2 | Trabalhista | Fazenda Pública | § 3.1 | § 3.2 (`trab.hist.fazenda-publica.juros-mora`) |
| 3 | Trabalhista | Fazenda **subsidiária** | **ramo vazio, por decisão** — § 3.3 | — |
| 4 | Cível | qualquer | § 4 | § 4 (tabela CGJ/TJMG) |
| 5 | Federal | sete ramos do CJF | § 5 | § 5 (o tronco comum 1964–fev/1991) |

**Escopo declarado:** o Manual CJF (Res. 990/2026) tem **11 cadeias** em
`../tabelas-normativas/cjf.*.json` (107 segmentos) — **7 de correção** (condenatórias, previdenciário,
repetição, desapropriação direta, dívida fiscal, **FGTS**, **poupança**) e **4 de juros**
(condenatórias, trabalhista-JF, **FGTS**, **poupança**). **Oito outras cadeias tabuladas do manual
ainda não têm JSON** — `P18-02`, detalhe § 5.0.

---

## 2. Trabalhista — devedor privado

### 2.1 Regime vigente — `VIGENTE`

Fonte: `../00-base-normativa.md` § 1. STF, ADC 58 e ADC 59; TST, SDI-1,
E-ED-RR-713-03.2010.5.04.0029, DEJT 25/10/2024.

| Fase | Correção monetária | Juros de mora |
|---|---|---|
| Pré-judicial | **IPCA-E** | art. 39, *caput*, Lei 8.177/1991 (TRD) |
| Ajuizamento até 29/08/2024 | **SELIC** (engloba ambos) | — |
| A partir de 30/08/2024 | **IPCA** (sem E) | **Taxa legal** (CC art. 406, § único) |

- **Marco inicial dos juros: AJUIZAMENTO**, não citação (R7).
- IPCA-**E** na pré-judicial, IPCA a partir de 30/08/2024 — a distinção é do dispositivo.
- Taxa legal por **razão entre fatores**, nunca por subtração (R11) — `../00-base-normativa.md` § 4.
- **Divergência registrada, não resolvida:** parte da doutrina sustenta que juros pela TRD na
  fase pré-judicial contraria a própria ADC 58. Variante, não default (base § 1; V-14).

### 2.2 Cadeia histórica — `BIFURCADO` (`CH-01`, `CH-02`, `CH-04`)

**Estas linhas continuam sendo a regra aplicável às competências que cobrem.** O que caduca é
usá-las para competências posteriores ao corte da ADC 58 (18/12/2020), eixo = competência da
parcela.

**Correção — `trab.hist.correcao-monetaria`** (cap. 7, `pagina_pdf` 83–85):

| Período | Indexador | Fundamento | Veredito |
|---|---|---|---|
| 1942-11 .. 1991-02 | **`NAO-DECLARADO-PELO-MANUAL`** | — | **pendência P9-02**, § 6 |
| 1991-03 .. 2009-06 | TR | art. 39 da Lei 8.177/91 | `BIFURCADO` CH-01 |
| 2009-07 .. 2016-05 | TR | art. 39 da Lei 8.177/91 | `BIFURCADO` CH-02 |

`aplicacao`: `primeiro-dia-do-mes-subsequente-a-prestacao` — Súmula 381 do TST,
`pagina_pdf` 84. Ver § 7.

**Juros — `trab.hist.juros-mora`** (quadro sinóptico, `pagina_pdf` 89):

| Período literal | Taxa | Capitalização | Fundamento |
|---|---|---|---|
| ajuizamento até **26/02/87** | 0,5% a.m. | simples | CC/1916, 1062 e 1063 |
| **27/02/87 a 03/03/91** | 1,0% a.m. | **COMPOSTA** | DL 2322/87, art. 3º — **R4-EXCEÇÃO**, § 8 |
| **04/03/91** até a satisfação | 1,0% a.m. | simples | Lei 8.177/91, art. 39 |

`BIFURCADO` **CH-04**. Termo inicial: ajuizamento (CLT 883; Súmula 200/TST), **salvo parcelas
vincendas**, que seguem a época própria (`pagina_pdf` 88).

**Situações especiais, transcritas sem harmonização** (`pagina_pdf` 89): intervenção ou
liquidação extrajudicial — juros até a decretação (Súmula 304/TST); falência — juros limitados
à data da falência **apenas se houver determinação nos autos** (art. 124 da Lei 11.101/05; o
manual transcreve três ementas do TRT-3, **duas delas divergentes entre si**).

> **O capítulo técnico cita só o art. 124 — o resto do regime da massa falida está no cap. 16.**
> `extracao/trabalhista/bloco-13e-capitulo16.md` § 2 registra a **Súmula 388 do TST** (2
> ocorrências, **ambas na p. 332**) e o **art. 83 da Lei 11.101/05** (**1 ocorrência, e é
> essa**), os dois no item **16.4.9.2**, entre os **seis fundamentos que só existem no cap. 16**
> (`07-leitura-do-corpus.md` § 2). O que a Súmula 388 decide é **outro ponto**, não os juros
> deste parágrafo: ela isenta a massa **apenas** do art. 467 e do art. 477, § 8º — **INSS, IR e
> custas continuam integrando a execução** (armadilha **A21**, p. 332). Fica o ponteiro;
> **não há harmonização a fazer aqui**.

### 2.3 O que é `SUPERADO`, e para onde vai

| ID | O que o manual diz | Regra vigente na espinha | Data de corte | Destino do texto do manual |
|---|---|---|---|---|
| **F7-04** | *"atualmente a TR"* (`pagina_pdf` 129, 148, 149, 138, 155) | § 2.1 | **18/12/2020** | armadilhas, com a data |
| **JR-05** | OJ 300 da SDI-1 valida a TRD do art. 39 | idem | ver F7-04 | consequência de F7-04, não ponto autônomo |
| **AM-01** | item 10.1 pressupõe o critério pré-ADC 58 | idem | ver F7-04 | **cai o índice, não o método** — busca declarada: `compensa`, `ADC 58` e `IPCA` têm **zero ocorrências nas pp. 209–223** |

**O episódio IPCA-E fica como história, não como norma:** TST, ArgInc 479-60.2011.5.04.0231
(04/08/15) declarou a TR inconstitucional; STF, Rcl 22012 MC/RS (14/10/15) suspendeu —
*"permanece válida a TR"*. É o estado em que o manual congelou (`pagina_pdf` 84).

### 2.4 `AM-03` — `BIFURCADO` por segmento, não por data

Sob Selic pós-citação a distinção **principal × juros** perde objeto: no período de Selic
única (que engloba) **não há o que ratear**. Enquanto houver período de índice + juros
separados, o rateio de 10.3 tem objeto. **A conta real atravessa os dois regimes, logo os dois
coexistem por segmento.** Não é supersessão — é mudança de natureza da operação.
Fonte: `../extracao/trabalhista/bloco-11c-vincendos.md` § 9.

---

## 3. Trabalhista — devedor Fazenda Pública

### 3.1 Regime vigente — `VIGENTE`, com pendência declarada

`../00-base-normativa.md` § 2. Ramo **ressalvado expressamente** pela ADC 58.

| Período | Correção | Juros |
|---|---|---|
| Até **nov/2021** | IPCA-E | Lei 11.960/2009 |
| A partir de **dez/2021** | **SELIC** (engloba ambos) | — |

Fonte: TST, 2ª Turma, ata da 17ª sessão ordinária de 2026 (RR 131300-14.2010.5.21.0006).

> **Pendência aberta, não resolvida por inferência:** o efeito da **EC 136/2025** sobre a
> Justiça do Trabalho **não foi consolidado pelo TST nem pelo CSJT** (base § 9, pendência 3).
> Não se estende a cadeia do CJF ao trabalhista por analogia.

### 3.2 Cadeia histórica — `BIFURCADO` (`CH-03`, `CH-05`)

**Correção, ramo Fazenda** (`pagina_pdf` 85) — `CH-03`:

| Período | Indexador | Fundamento |
|---|---|---|
| 2009-07 .. 2016-05 | remuneração básica da poupança (**TR**) | art. 1º-F da Lei 9.494/97, redação do art. 5º da Lei 11.960/09 (corte ao dia **29/06/2009**) |

**Juros — `trab.hist.fazenda-publica.juros-mora`**, quadro de **cinco** linhas,
`pagina_pdf` 92 (não três: a primeira extração lera o resumo em prosa da p. 90) — `CH-05`:

| Período literal | Taxa | Fundamento |
|---|---|---|
| ajuizamento até 26/02/87 | 0,5% a.m., simples | CC, 1062 e 1063 |
| **27/02/87 a 03/03/91** | 1,0% a.m., **COMPOSTA** | DL 2322/87, art. 3º — **R4-EXCEÇÃO** |
| 04/03/91 a 26/08/01 | 1,0% a.m., simples | Lei 8.177/91, art. 39 |
| 27/08/01 a 28/06/2009 | 0,5% a.m., **limitado a 6% ao ano** | Lei 9.494/97, art. 1º-F (MP 2.180-35/2001) |
| 29/06/2009 até o pagamento | juros da poupança, **sem cumulação** | Lei 9.494/97, art. 1º-F (art. 5º da Lei 11.960/09) |

**O limite de 6% a.a. não é redundante** com 0,5% a.m.: 0,5% simples por doze meses dá
exatamente 6%, mas o limite morde em qualquer contagem por dias que ultrapasse o ano.

**Subcorte 04/05/2012** (MP 567/12 → Lei 12.703/12, `pagina_pdf` 91): modelado como
**qualificação do último segmento**, não como segmento próprio — a **regra** (art. 1º-F,
poupança) não muda; muda a fórmula da poupança. Literal: *"Até 03/05/2012, os juros aplicáveis
à caderneta de poupança, correspondiam a 0,5% ao mês."*

**Série (B) embutida na cadeia** — único lugar do capítulo 7 em que o manual crava percentual
mês a mês (`pagina_pdf` 92, art. 12, II, "b", da Lei 8.177/91):

| jun/12 | jul/12 | ago/12 | set/12 | out/12 | nov/12–abr/13 | mai/13 | jun/13–jul/13 | ago/13 |
|---|---|---|---|---|---|---|---|---|
| 0,4828% | 0,4828% | 0,4551% | 0,4273% | 0,4273% | 0,4134% | 0,4273% | 0,4551% | 0,4828% |

Total impresso **6,5760%**; atalho do manual `15 × 0,5% = 7,5%`, `7,5% − 6,5760% = 0,9240%`.
**Conferido em `Decimal`:** fecha exato.

### 3.3 Fazenda **subsidiária** — ramo declarado e deliberadamente vazio

`pagina_pdf` 93, literal: *"grande parte da jurisprudência entende que os juros de mora são de
1% ao mês de acordo com o art. 39 da Lei 8.177/91 (...) nos termos da OJ 382 da SDI-1/TST"*.

**"Grande parte da jurisprudência entende" é corrente, não regra assentada.** O quadro da
`pagina_pdf` 92 é expresso: vale para a Fazenda **"como reclamada principal"**. O ramo
`fazenda-publica-subsidiaria` é declarado em `dominio_condicoes` e **não recebe segmento**. O
validador o reporta como lacuna — leitura correta. **Pendência P9-01.**

> Um motor que aplique 0,5% a.m. à Fazenda subsidiária erra por leitura de condição
> não qualificada. Foi o defeito da primeira versão da cadeia.

---

## 4. Cível

`../00-base-normativa.md` § 3.

| Período | Correção monetária | Juros de mora |
|---|---|---|
| Até dez/2002 | Tabela CGJ/TJMG (em MG) | 0,5% simples (CC/1916, arts. 1.062–1.064) |
| Jan/2003 a 29/08/2024 | **SELIC** (engloba ambos) | — |
| A partir de 30/08/2024 | **IPCA** (CC art. 389, § único) | **Taxa legal** (CC art. 406, § 1º) |

Fonte do trecho central: **STJ, Tema 1368**, Corte Especial, j. 15/10/2025, REsp 2.199.164/PR e
REsp 2.070.882/RS, acórdão publicado em 20/10/2025. **Vinculante**, e substitui a prática
anterior do TJMG (tabela CGJ + 1% a.m.) para o período pré-Lei 14.905.

**Quando a tabela CGJ/TJMG ainda se aplica** — é bifurcação, não resíduo: períodos anteriores a
2003; processos cujo título fixou expressamente aquele critério; processos com trânsito em
julgado sob o regime anterior (R8: título > escolha > default).

**Termos iniciais** (R7): regra geral, citação; extracontratual, evento danoso (Súmula 54/STJ);
ato ilícito, efetivo prejuízo (Súmula 43/STJ); dano moral, arbitramento (Súmula 362/STJ).

## 5. Justiça Federal — as cadeias do CJF

Manual CJF, Res. 990/2026 (`../extracao/justica-federal/bloco-08-jf.md`); JSON em
`../tabelas-normativas/cjf.*.json` — **11 cadeias** (7 do bloco 8 + **4 do bloco 18**).
**Única fonte do corpus cuja edição está vigente. Segmento a segmento no detalhe § 5.**

**Tronco comum de 1964 a fev/1991**, idêntico palavra por palavra em quatro cadeias de correção
(condenatórias, previdenciário, repetição, desapropriação): ORTN (1964–fev/86) → OTN
(mar/86–jan/89, com multiplicador **6,17** em jan/89) → **IPC/IBGE 42,72%** (jan/89) →
**IPC/IBGE 10,14%** (fev/89) → BTN (mar/89–mar/90) → IPC/IBGE (mar/90–fev/91). **O expurgo
SUBSTITUI, não soma** (item 4.1.2.1, `pagina_pdf` 42). **A dívida fiscal (cap. 2) NÃO tem este
tronco.**

| Ramo | Depois de fev/1991 | Bifurca por devedor? |
|---|---|---|
| **Condenatórias gerais** | INPC → IPCA esp. (dez/91) → Ufir → IPCA-E (01–nov/21) → **dez/21**: Selic (FP) × IPCA-E (não-FP) → set/24: Selic × IPCA-15 → **set/25: IPCA-15 para os dois** | **sim, dez/2021**; reconverge em **set/2025** |
| **Previdenciário** | INPC → IRSM → URV → IPC-R → INPC → IGP-DI → INPC (set/06–nov/21) → Selic (dez/21–ago/25) → **INPC** | **nunca** |
| **Repetição de indébito** | INPC → IPCA esp. → Ufir (92–jan/96) → **Selic desde jan/1996** | **nunca** |
| **Desapropriação direta** | **IPC/FGV (mar–dez/1991)** — índice exclusivo desta cadeia → Ufir → IPCA-E → Selic → IPCA-15 | **nunca** |
| **Dívida fiscal** | BTN (jan/89–jan/91) → janela 1991-02..1991-12 → **Ufir → Selic, bifurcado pelo `data-do-fato-gerador`** | por fato gerador |
| **FGTS** (4.8.1.1, **`JAM`**) | **tronco próprio, não o comum:** ORTN (jan/67–fev/86) → IPC → LBC → **OTN (mar–jun/87)** → LBC–0,5% → OTN → LFT–0,5% → IPC → BTN → TRD → **TR (maio/93→)** | **nunca** |
| **Poupança** (4.9.1.1) | **idem, salvo:** **UPC (maio/67–jun/83)** e **LBC (fev–jun/87)** onde o FGTS usa ORTN e OTN | **nunca** |

**FGTS e poupança — cadeia própria, consolidadas no bloco 18; detalhe § 5.0 e §§ 5.3.2–5.3.5.** Três eixos
exclusivos: **`D8-C12`**, o FGTS corta por **SAQUE INTEGRAL** (4.8, NOTA 2) — **não é competência nem
sentença**; **`D8-C16`/`N-11`**, a poupança corta por **DATA DE ABERTURA DA CONTA**, enquanto **4.5.2
e 4.6.2 aplicam a mesma fórmula por competência**; e o **aniversário da conta** como termo inicial.
**`D8-C15`: divergem em dezesseis anos e quatro meses, e nenhuma das duas tabelas traz fundamento
legal para isso.** **`D8-C13`/`N-5` fica ABERTA** — os expurgos do FGTS (*"42,72% em jan./1989 e 44,80%
em abr./1990"*) **não dizem se substituem ou acrescem**, ao contrário do capítulo 4 geral (*"em
substituição ao BTN"*), e por isso **não viraram segmento**. **Calendário próprio:** 0,5% até
dez/2002 → Selic → **taxa legal em set/2024**, sem dez/2021 nem set/2025; **não consolidam**
(`0,4412` só nas `pagina_pdf` 50, 59, 67, 74, 79). Defeitos transcritos: `D8-D18` (*"Lei
5.107/**1986**"*, que é de 1966), `D8-D19`, `D8-D24`, `D8-D25`. **A varredura dos caps. 2 e 4
(detalhe § 5.0) achou mais oito cadeias tabuladas sem JSON** — 4.5.2, 4.5.3, **4.6.1.1, 4.6.2,
4.6.3** (indireta inteira), 2.3.2.2, 2.4.2.2.2 e **2.4.4.1** (FGTS **fiscal**, critério **`JCM`**,
que **não é** a de 4.8): **`P18-02`**. **`4.7.1` não é lacuna** — não há tabela de correção
trabalhista no manual; ele delega ao TST.

**Juros, cadeias autônomas:** `cjf.condenatorias-gerais.juros-mora` bifurca em **jul/2009** e
reconverge em **set/2025** (taxa legal); `cjf.trabalhista.juros-mora` bifurca em **ago/2001** e
**nunca reconverge** — o ramo empresa pública/prestador segue em **1,0% a.m.**, e traz a
**R4-EXCEÇÃO** (1,0% **composta**, mar/87–mar/91). **R-08-08 — a bifurcação por devedor não é
universal:** três cadeias nunca bifurcam.

**Quatro fórmulas de `aplicacao`, e D1 ≠ D2 sobre a mesma série:** **D1** — Selic no mês posterior
ao de sua competência, **inclusive no mês de pagamento** (Fazenda, desde dez/2021; a taxa legal segue
D1); **D2** — do mês seguinte ao termo inicial dos juros até o mês anterior ao pagamento, **e 1% no
mês do pagamento** (não-Fazenda; Fazenda jan/03–jun/09); **D3** — eixo no **recolhimento indevido**
(repetição); **D4** — competência da parcela — **dívida fiscal, e também FGTS e poupança**.

**`C14-01` — `SUPERADO`.** A EC 136/2025 reescreveu o art. 3º da EC 113/2021: requisitórios da
Fazenda **federal**, da expedição ao pagamento, **IPCA** + **juros simples de 2% a.a.**, com
**trava** pela Selic. Três estreitamentos: objeto, ente e período. **Refutação registrada, fonte
interna:** `bloco-13c-sindical-precatorios.md` § 7 afirma que a EC 113/2021 alcançava só
requisitórios federais — **está errado**; a redação original diz *"independentemente de sua
natureza"* (base § 5). A restrição é criação da EC 136/2025. **Regra de incidência assimétrica**
(CNJ, Prov. 207/2025): IPCA sobre **principal e juros somados**; 2% a.a. sobre o **principal,
excluídos os juros já apurados** — **não decorre da leitura da emenda**.

**`C14-02` — `BIFURCADO`**, eixo = **expedição do requisitório ⊕ ente devedor**. **Sobrevivem
quatro regras estruturais do cap. 14:** suspensão dos juros no prazo constitucional; juros de 0,5%
a.m. desde ago/2001; exclusão de juros compensatórios; exceção à precedência do título. **Não
sobrevive o índice.** Data de apresentação do precatório: **1º de julho até 2021; 2 de abril a
partir de 2022**. No requisitório complementar o indexador troca **três vezes** (original →
administrativo → original, R-08-17). **Divergência registrada:** TJ-SP mantém a Selic fora da fase
de precatório; **ADI 7873 pendente**; Fazenda **estadual e municipal** sem regra.

**`C14-03` — `INAPLICÁVEL` por prejudicialidade**, razão declarada: depende de classificar a
devedora como Fazenda Pública — **Pendência 1**, *"pergunta ao jurídico do usuário do módulo"*. **C14-01 e
C14-02 são condicionais a ela.** Busca declarada do bloco 13C: `economia mista` tem **zero
ocorrências nas 471 páginas**; a única equiparação nominada é a ECT, e só *"para efeito de execução
e do DL 779/1969"*.

---

## 6. `P9-02` — a cadeia trabalhista histórica **não é derivável do manual**

**Achado do bloco 09, e governa o bloco.** O capítulo 7 **não tem mapa período → indexador de
correção monetária**. Não é omissão do extrator: é desenho do manual, e ele diz por quê,
literal na `pagina_pdf` **85**:

> "A tabela mensal de correção está escalonada em meses e anos, já computa as conversões e
> paridades da moeda nacional e não contém juros."

O TRT-3 **delega o encadeamento inteiro à Tabela Única do CSJT** (Resolução CSJT 08/2005,
vigente a partir de **novembro/2005**; até outubro/2005 o TRT-3 publicava tabela própria,
`pagina_pdf` 84). A cadeia vive numa **série — categoria (B), dado externo** — e não numa regra.

**Busca negativa, com escopo declarado:** varredura das **dezessete páginas do capítulo 7**
(`pagina_pdf` 83–99) por `IPC`, `IGP`, `INPC`, `expurgo`, `ORTN`, `OTN`, `BTN`, `Ufir`,
`42,72`, `10,14`, `6,17`, `6,92`, `126,8621` — **nenhuma ocorrência**. "IPC" só aparece dentro
de "IPCA-E". **Isto vale para o capítulo 7, não para as 471 páginas.**

**Consequência na espinha:** o segmento `1942-11 .. 1991-02` tem
`indexador: "NAO-DECLARADO-PELO-MANUAL"`, **não "TR"** — a TR foi criada pelo art. 39 da Lei
8.177/91, de março de 1991, e não existia no período. **Pendência P9-02**, a fechar contra a
Tabela Única do CSJT e a cadeia do CJF (cap. 4), que **é** um mapa completo.

**Não infiro a ponte.** O tronco do CJF (§ 5.1) cobre o período, mas **o corpus não faz a
remissão** — usá-lo como cadeia trabalhista seria ponte inventada.

**A TR foi REBAIXADA a `tipo_indexador: "indeterminado"` no bloco 17.** Era `percentual` por critério **formal** do item 4.1.2.4 — não é unidade monetária, logo é percentual —, mas o critério **material** daquele item (*"refletem a inflação do próprio mês"*) **não a alcança**: é taxa apurada **prospectivamente** (art. 12, I, da Lei 8.177/91). **Nenhum dos dois manuais classifica a TR**, e **inferência declarada não é fonte**. Pendência `P17-02`; o validador bloqueia a virada sob `R3-INDETERMINADO`.

---

## 7. As três defasagens — e a quarta régua dos juros

O manual trabalhista opera **três réguas de correção**, e **os juros usam uma quarta**,
incompatível com a terceira.

| # | Defasagem | Granularidade | Onde | Regra |
|---|---|---|---|---|
| 1 | **Súmula 381/TST** | **um mês** | tabela mensal, `pagina_pdf` 84 | índice do mês **seguinte** ao da prestação |
| 2 | **Tabela diária do CSJT** | **um dia** | item 7.5.2, `pagina_pdf` 87 | traz a TR acumulada **até o dia anterior** à data final informada |
| 3 | **Pro-ratização** | **dias úteis** | item 7.5.2, `pagina_pdf` 87 | o índice mensal é decomposto por **dias úteis**, não corridos |
| 4 | **Juros** | **mês comercial de 30 dias** | item 7.6, `pagina_pdf` 88 | 1% a.m. ou `1/30` ao dia |

**Régua 1, a mecânica importa mais que a regra:** a tabela já posiciona o índice *"no próprio
mês da constituição do crédito"* (`pagina_pdf` 85), de modo que **aplicar a Súmula 381 equivale
a usar o índice do mês SEGUINTE**. Exemplo do manual: horas extras de **junho/14** → índice de
**julho/14**. *Quem lê a súmula sem a tabela, ou a tabela sem a súmula, erra por um mês.*

**Régua 2, com o contra-exemplo do próprio manual:** `01/05/16` a `31/05/16` devolve
`1,001459947`, que é a TR de **01/05 a 30/05**. Para maio cheio é preciso informar **01/06/16**.

**Régua 4, defeito do original registrado:** a regra imprime `0,0333%` e o exemplo, duas linhas
abaixo, `0,03333%`. No exemplo do manual (11/05/00 a 30/04/04, 47 meses e 20 dias) ambos dão
`47,67%`; em contagens longas de dias, muda. **Por R12, o motor computa
`Decimal(1)/Decimal(30)`**, nunca o truncamento impresso.

> **Correção pro-ratizada por dias úteis e juros por dias corridos/30 no mesmo cálculo é
> atrito real do manual.** Registrado, **não harmonizado**.
>
> **Contagem inclusiva do mês comercial:** `dias = 30 − dia_inicial + 1`. Testado em cinco
> períodos: **5 de 5 fecham pela regra inclusiva, 0 de 5 pela exclusiva**. A fórmula aparece
> nos exemplos; a **convenção de contagem**, não (`../armadilhas-comparador.md` § 4).

---

## 8. `R4-EXCEÇÃO` — juros **compostos** de 27/02/1987 a 03/03/1991

**Invariante R4:** juros de mora, Selic e taxa legal são **sempre simples**. Capitalização
mensal só em juros remuneratórios.

**A exceção histórica de quatro anos**, por força do **DL 2.322/87, art. 3º**, confirmada por
**três registros independentes, duas jurisdições, edições separadas por dez anos**:

| Fonte | Onde | Diz |
|---|---|---|
| TRT-3, quadro geral | `pagina_pdf` 89 | "1,0% ao mês, c/ taxa capitalizada. Ex.: **3 meses = 3,03%**" |
| TRT-3, quadro da Fazenda | `pagina_pdf` 92 | idem |
| CJF, cap. 4 (`cjf.trabalhista.juros-mora`) | `pagina_pdf` 78 | "De mar./1987 a mar./1991 — 1,0% — **composta**" |

**Não é erro de transcrição de nenhum dos dois manuais.** Gravada no campo `ALERTA_R4` dos
segmentos e **dentro do invariante**, não em nota de rodapé: quem ler apenas *"juros de mora
sempre simples"* erra quatro anos de qualquer conta que atravesse o período.

---

## 9. Os `status_norma` dos JSON `trab.hist.*` — **`BIFURCADO`, não `SUPERADO`**

Vereditos **`CH-01` a `CH-05`**, todos `BIFURCADO`:

| ID | Cadeia / segmento | `status_norma` no JSON | Veredito |
|---|---|---|---|
| **CH-01** | `trab.hist.correcao-monetaria` 1942-11..2009-06 | `superado` | **`BIFURCADO`** |
| **CH-02** | idem 2009-07..2016-05 (não-Fazenda) | `superado` | **`BIFURCADO`** |
| **CH-03** | idem 2009-07..2016-05 (Fazenda) | `superado` | **`BIFURCADO`** |
| **CH-04** | `trab.hist.juros-mora` 1991-04..2016-05 | `superado` | **`BIFURCADO`** |
| **CH-05** | `trab.hist.fazenda-publica.juros-mora` 2009-07..2016-05 | `superado` | **`BIFURCADO`** |

> **O `status_norma: "superado"` está certo quanto ao futuro e incompleto quanto ao passado.**
> O segmento continua sendo a regra aplicável às competências que cobre — é essa a razão de a
> cadeia histórica existir. **O que caduca é usá-lo para competências posteriores ao corte da
> ADC 58.** Cadeia temporal, não supersessão — a mesma estrutura da Res. 225/2025 do TST.

**Instrução para o motor:** não apagar, não substituir. Ler `status_norma` como **fronteira
superior do segmento**, e não como invalidade. Por **R19**, toda conta que atravesse o corte
grava **qual lado aplicou a cada competência**.

---

## 10. Consolidação de dez/2021 — cinco lugares, três valores de fechamento

Literal, `pagina_pdf` 50 (repetido em 59, 67, 74 e 79): *"o crédito será consolidado tendo por base
o mês de dez./2021 pelos critérios [...] até então aplicáveis, considerando [...] o [índice] de
nov./2021 ([x]%) e os **juros de dez./2021 (0,4412%)**"*; *"sobre o valor consolidado [...] **sem
exclusão de qualquer parcela**, incidirá a taxa Selic a partir de jan./2022 (competência
dez./2021)"* (§ 1º do art. 22 da Res. CNJ 303/2019, red. do art. 6º da Res. CNJ 448/2022); e o
resultado, *"denominado 'Juros Selic', deve ser **integralmente somado à parcela denominada 'Juros
até 12/2021'**"*.

| Ramo | Índice de nov/2021 | Valor | Juros de dez/2021 | Item · `pagina_pdf` |
|---|---|---|---|---|
| Condenatórias em geral | IPCA-E | **1,17%** | 0,4412% | 4.2.1, NOTA 5 · **50** |
| Benefícios previdenciários | INPC | **0,84%** | 0,4412% | 4.3.1, NOTA 5 · **59** |
| Desapropriação **direta** | IPCA-E | **1,17%** | 0,4412% | 4.5.1.1, NOTA 2 · **67** |
| Desapropriação **indireta** | IPCA-E | **1,17%** | 0,4412% | 4.6.1.1, NOTA 2 · **74** |
| Ações trabalhistas (JF) | **TR** | **0,00%** | 0,4412% | 4.7.2, NOTA 2 · **79** |
| Repetição de indébito | — | **não consolida** | — | 4.4.1.1, NOTA 4 · 64 |

**R-08-12 — três valores de fechamento, cinco lugares, uma dispensa.** Os juros de dez/2021 são os
mesmos (**0,4412%**) nos cinco; o índice assume **três** valores. **A TR trabalhista de 0,00%
significa que, nesse ramo, o principal não se move em nov/2021.** **R-08-13 — a repetição de
indébito não consolida**, porque já observa a Selic desde jan/1996 (`pagina_pdf` 64).
**R-08-14 — "sem exclusão de qualquer parcela":** a Selic incide sobre o consolidado inteiro,
principal **e** juros (exemplos da `pagina_pdf` 51: R$ 2.275,96 e R$ 55,75, **ambos recebendo
5,05%**). **Verificado por varredura:** `0,4412` ocorre nas páginas **50, 59, 67, 74 e 79** — a
primeira redação do bloco 08 listava **quatro** lugares e três ramos; são **cinco**.

---

## 11. As invariantes aplicadas às cadeias

| ID | Enunciado | Onde morde nesta espinha |
|---|---|---|
| **R1** | **Exclusividade de englobamento.** Segmento cujo `engloba` cobre correção **e** juros não admite outro segmento do mesmo componente no mesmo intervalo | todo segmento **Selic** e **taxa legal**: §§ 2.1, 3.1, 4, 5.2. **É o que impede contar inflação duas vezes** — e é a razão de `AM-03` (§ 2.4) |
| **R2** | **Cobertura sem lacuna nem sobreposição**, da parcela mais antiga até a data-base | a ponta `1942-11` das cadeias `trab.hist.*` é **janela de análise**, não afirmação do manual (`ponta_materializada`). No CJF, **R-08-04**: em cadeia de índices **nominais**, fim e início no mesmo mês (OTN/BTN em jan/1989) **não é dupla contagem** |
| **R3** | **Tipo do indexador na virada.** Nominal (Ufir, BTN, OTN, ORTN) reflete a inflação do mês **anterior**; percentual (**INPC, IGP-DI**) a do **próprio mês** | item 4.1.2.4 do CJF, `pagina_pdf` 42. **Trocar entre tipos sem ajustar a defasagem desloca o cálculo em um mês** — e é o que sustenta a ressalva da TR no § 6 |
| **R4** | Juros de mora, Selic e taxa legal **sempre simples** | **com a R4-EXCEÇÃO do § 8** |
| **R5** | **Piso nominal.** Índices negativos entram no cálculo, mas nenhuma parcela fica abaixo do valor nominal | **R-08-06: o piso é POR PARCELA**, não no total — *"considerada cada parcela do principal"*, item 4.1.2.2, `pagina_pdf` 42. Fundamento: REsp 1.265.580 |

Complementares que atravessam este arquivo: **R7** (termo inicial não intercambiável — § 2.1,
§ 4), **R8** (título > escolha > default — R-08-01, com a **única exceção** da NOTA 2: mudança
superveniente de legislação sobre o indexador passa por cima do título), **R9** (Fazenda Pública
é **atributo do processo**), **R11**, **R12**, **R19**.

---

## 12. Pendências — entram como pendência, nunca como regra

| # | Pendência | Onde | Estado |
|---|---|---|---|
| **P9-01** | Juros da Fazenda **subsidiária** — corrente, não regra | `pagina_pdf` 93 | ramo sem segmento, **por decisão** |
| **P9-02** | Índice de correção **anterior a 03/1991** não declarado | `pagina_pdf` 85 | aberta — buscar na Tabela Única do CSJT |
| **P9-03** | Termo inicial de juros em processos vindos da Justiça Estadual ou Federal | `pagina_pdf` 95 | aberta |
| **P9-04** | Súmula 439/TST, Súmula 15/TRT-3, OJs 181, 198 e 302 — termo inicial e índice **por tipo de verba** | `pagina_pdf` 83 | aberta |
| **P9-05** | Juros **vincendos** (mecânica de decréscimo) — método, não mapa | `pagina_pdf` 95–98 | fora do escopo dirigido |
| **Base 2** | Tabela Única do CSJT — contrato de integração | base § 9 | **bloqueia o motor trabalhista** |
| **Base 3** | Efeito da EC 136/2025 na Justiça do Trabalho | base § 9 | aguarda TST/CSJT |
| **Base 4** | ADI 7873 | base § 9 | aguarda julgamento |
| **`N-5`/`D8-C13`** | expurgos do FGTS — **substituem ou acrescem?** | `pagina_pdf` 82 | **aberta, e não se resolve** — os percentuais **não viraram segmento** |
| **P18-01** | `JAM`, `UPC`, `LBC`, `LBC – 0,5%`, `LFT – 0,5%`, `TRD`, `IPC` **sem classificação em fonte** | item 4.1.2.4 não os nomeia | `indeterminado` — **19 `R3-INDETERMINADO`** no validador |
| **P18-02** | **oito cadeias tabuladas do manual sem JSON** — 4.5.2, 4.5.3, 4.6.1.1, 4.6.2, 4.6.3, 2.3.2.2, 2.4.2.2.2, 2.4.4.1 | detalhe § 5.0 | aberta — 2.3.2.2 e 2.4.2.2.2 exigem `base_incidencia` (`D8-C5`) |

**Defeitos do original que atravessam a cadeia** — não corrigidos, catalogados em
`../armadilhas-comparador.md`: **A5** (índice de dez/10, `pagina_pdf` 96, monotonicidade quebrada — o
erro está no índice publicado e o valor está certo) e o **`DEFEITO_DO_ORIGINAL` das moedas**
(`trab.hist.moedas-e-paridades`, `pagina_pdf` 99): a primeira linha termina em **12/02/70** e a
segunda começa em **13/02/67** — três anos de sobreposição; era quase certamente **12/02/67**.

---

## 13. O que este arquivo **não** consolida, e por quê

| Aberto | Razão |
|---|---|
| **Modulação da ADC 58**, item "i", sem transcrição literal | `portal.stf.jus.br` respondeu **HTTP 403 em 100% das tentativas**. O desdobramento das **duas situações** (i.1 pagamento consolidado × i.2 execução questionada) está em `../00-base-normativa.md` § 1.1, que **ele próprio declara** origem secundária, com os três precedentes do TST **não lidos no inteiro teor** |
| **Índice trabalhista anterior a 03/1991** | P9-02 — o manual delega; a Tabela Única não foi integrada |
| **Fazenda subsidiária** | P9-01 — divergência jurisprudencial, que a disciplina do projeto **não resolve** |
| **Fazenda estadual e municipal pós-EC 136/2025** | lacuna **normativa**, não de pesquisa: a regra antiga foi revogada e a nova não os alcança |
| **EC 136/2025 na Justiça do Trabalho** | TST e CSJT não consolidaram |
| **Classificação da devedora como Fazenda Pública** | Pendência 1 — **determinação jurídica do usuário do módulo**. Se negativa, somem o ramo FP das três jurisdições, precatório, ECs 113/136 e a consolidação de dez/2021 |

---

## 14. Ponteiros para o detalhe

- `../extracao/trabalhista/bloco-09-cadeias-historicas.md` — cadeias trabalhistas, as três
  defasagens, a anomalia da capitalização, moedas e paridades
- `../extracao/justica-federal/bloco-08-jf.md` e `bloco-08-jf-detalhe.md` — as sete cadeias do
  bloco 8 linha a linha, notas × linhas, defeitos do original
- `../tabelas-normativas/cjf.*.json` (11) e `trab.hist.*.json` — schema `cadeia-temporal`, com
  `status_norma`, `ALERTA_R4` e `ponta_materializada`; validador `scripts/calculo/valida_cadeias.py`
- `../00-base-normativa.md` §§ 1, 1.1, 2, 4, 5, 6, 7 — regimes vigentes e invariantes;
  `00-calendario-de-cortes.md` — o par `(data, eixo)`
- `../confronto-normativo/01-vereditos.md` — F7-04, C14-01..C14-03, CH-01..CH-05, AM-01, AM-03, JR-05; `../armadilhas-comparador.md` — A5, e o índice por página

## Detalhe

As seções **5** e **10** estão aqui condensadas. O desenvolvimento — a **varredura item × JSON ×
consolidado** dos caps. 2 e 4 (§ 5.0), as cadeias **segmento a segmento**, **FGTS e poupança**
(§§ 5.3.2–5.3.5) e a consolidação de dez/2021 com texto integral — vive em
**[`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md)**, para manter a espinha abaixo de 500
linhas. **A espinha é o que o motor precisa para calcular; o detalhe é onde está a evidência.**
