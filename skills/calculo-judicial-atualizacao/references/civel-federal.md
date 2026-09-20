# Federal — ações condenatórias em GERAL, cadeia do CJF

Correção monetária e juros de mora das **ações condenatórias em geral** na Justiça Federal.
Item **4.2** do **Manual de Orientação de Procedimentos para os Cálculos na Justiça Federal,
CJF, Res. 990/2026** — **única fonte do corpus cuja edição está vigente**.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 5;
`consolidado/02-atualizacao-detalhe.md` §§ 5.1, 5.2, 5.3 e 10;
`docs/calculo/extracao/justica-federal/bloco-08-jf.md` §§ 4 e 5 e `bloco-08-jf-detalhe.md` § 4;
`docs/calculo/00-base-normativa.md` §§ 4, 6 e 8;
`docs/calculo/tabelas-normativas/cjf.condenatorias-gerais.correcao-monetaria.json` (15 segmentos)
e `cjf.condenatorias-gerais.juros-mora.json` (11 segmentos).

> **Cível FEDERAL, não cível estadual.** A cadeia do **Código Civil** — Tema 1368, Lei
> 14.905/2024, termos iniciais das Súmulas 43, 54 e 362 do STJ — vive em
> `references/civel-cc-nacional.md`. O Manual CJF **não governa o contencioso cível estadual**
> (`00-base-normativa.md` § 10).

> **Escopo deste arquivo:** condenatórias em geral. **Desapropriação** (direta e indireta, com os
> **juros compensatórios**) está em `references/desapropriacao.md`. **Repetição de indébito** e
> **dívida fiscal** em `references/tributario-federal.md`. **Benefício previdenciário** em
> `references/previdenciario.md`.

**Escopo declarado de "cinco ramos do CJF":** o Manual tem **sete cadeias** extraídas (78
segmentos) — **cinco de correção monetária** (condenatórias gerais, previdenciário, repetição de
indébito, desapropriação direta, dívida fiscal) e **duas de juros** autônomas (condenatórias
gerais e trabalhista-JF). `bloco-08-jf.md` § 4, `pagina_pdf` 48, 54, 57, 63, 66, 78 e 23.

**Cabeçalho literal da tabela de correção** (`pagina_pdf` 48): *"Caso não haja decisão judicial em
contrário, utilizar os seguintes indexadores:"* — é **R8** dita pela fonte.

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

**O expurgo SUBSTITUI, não soma** — item 4.1.2.1, `pagina_pdf` 42, literal: *"descontando o BTN ou
outro índice utilizado, evitando bis in idem"*. É o **único** lugar do manual em que a operação é
declarada (`R-08-05`).

> **A DÍVIDA FISCAL (cap. 2) NÃO TEM ESTE TRONCO.** Ela não substitui o BTN pelos expurgos
> (atrito **N-4**) e usa **dois** multiplicadores de transição em jan/1989 — **6,92 para o IR** e
> **6,17 para o II** (`D8-C2`, `D8-C3`). Ver `references/tributario-federal.md` § 3.

**`R-08-04` e `R3` — o manual justifica EXPRESSAMENTE a sobreposição de jan/1989** (item 2.3.1.3,
`pagina_pdf` 25):

> *"O mês de janeiro de 1989 marca o termo final da OTN e o início da BTN. Entretanto, por serem
> indexadores nominais, este fato não implica duplicidade de correção monetária, pois a OTN de
> janeiro serve para definir a inflação de dez./1988, e a BTN de janeiro, comparada com a de
> fevereiro, para fixar a inflação de jan./1989."*

**A sobreposição de mar/1990 NÃO é coberta por esse argumento** — `D8-C21`: o IPC/IBGE é índice
**percentual**, e o item 4.1.2.4 diz que percentuais *"refletem a inflação do próprio mês de
competência"*. BTN de mar/1990 e IPC de mar/1990 medem o mesmo mês. **Pendência, não harmonizada.**

**A ponta inicial é `ponta_materializada`:** o manual abre com *"De 1964 a fev./1986"*, **sem
mês**. `1964-01` é materialização de janela para permitir a checagem de R1/R2 — **`P8-07`**.

---

## 2. A cadeia de CORREÇÃO — item 4.2.1.1, `pagina_pdf` 48

**Bifurca em dez/2021 por qualidade do devedor — e RECONVERGE em set/2025.**

| Período | Fazenda Pública | Não Fazenda Pública |
|---|---|---|
| 1964-01 .. 1991-02 | **tronco comum** (§ 1) | idem |
| 1991-03 .. 1991-11 | **INPC/IBGE** | idem |
| **1991-12** | **IPCA série especial** — art. 2º, § 2º, da Lei 8.383/1991 | idem |
| 1992-01 .. 2000-12 | **Ufir** — Lei 8.383/1991 | idem |
| 2001-01 .. **2021-11** | **IPCA-E/IBGE** | **IPCA-E/IBGE** |
| **2021-12** .. 2024-08 | **SELIC** — art. 3º da EC 113/2021 | **IPCA-E/IBGE** |
| 2024-09 .. 2025-08 | **SELIC** | **IPCA-15/IBGE** — CC art. 389, § único |
| **a partir de 2025-09** | **IPCA-15/IBGE** | **IPCA-15/IBGE** |

**Fundamento do IPCA-E de 2001–2021:** RE 870.947 e RE 870.947 ED (**Tema 810 do STF**).
**Fundamento da reconvergência de set/2025:** **ARE 1.557.312/SP (Tema 1.419 do STF)** + art. 389,
§ único, do CC — `R-08-23`: o corte de set/2025 que aparece em **todas** as cadeias é a **EC
136/2025**, que **nenhuma tabela do corpo nomeia**.

**Saída da Ufir:** extinção como indexador pelo art. 29, § 3º, da **MP 1.973-67/2000** (observação
do próprio segmento).

**`aplicacao` do primeiro mês do IPCA-E, literal do manual:** *"O percentual a ser utilizado em
janeiro de 2001 deverá ser o IPCA-E acumulado no período de janeiro a dezembro de 2000. A partir
de janeiro de 2001, deverá ser utilizado o IPCA-E mensal (IPCA-15/IBGE)."* — **um mês da cadeia
usa um acumulado de doze**; tratá-lo como mês normal erra o segmento inteiro.

**`dominio_condicoes` declara que os dois ramos ESGOTAM o eixo** (`fazenda-publica` ×
`nao-fazenda-publica`). Sem a declaração o validador cobraria o universo *"nenhuma condição se
aplica"*, porque **exaustividade se declara, não se presume** (**R2**).

**NOTA 2 do item 4.2.1, `pagina_pdf` 49 — é `R1` dita pela fonte:**

> *"Se os juros de mora corresponderem à taxa Selic (ver item 4.2.2, a seguir), o IPCA-E deixa de
> ser aplicado como indexador de correção monetária, a partir da incidência da Selic (que engloba
> juros e correção monetária)."*

O ramo não-Fazenda de dez/2021 traz a observação correspondente no segmento: *"observada a vedação
de acumulação com a Selic, nos termos da Nota 2"*.

---

## 3. A cadeia AUTÔNOMA de JUROS — item 4.2.2, `pagina_pdf` 54

**É cadeia própria, com bifurcação própria e em data própria.** `cjf.condenatorias-gerais.juros-mora`.
**Bifurca em jul/2009 — dois anos e meio antes da correção — e reconverge em set/2025.**

| Período | Fazenda Pública | Não Fazenda Pública |
|---|---|---|
| 1964-01 .. 2002-12 | **0,5% a.m.** — CC/1916, arts. 1.062, 1.063 e 1.064 | idem |
| 2003-01 .. 2009-06 | **SELIC** — CC art. 406 | idem |
| **2009-07** .. 2012-04 | **0,5% a.m.** — art. 1º-F da Lei 9.494/1997, red. da Lei 11.960/2009 | **SELIC** — CC art. 406 |
| 2012-05 .. 2021-11 | **poupança**: 0,5% a.m. se a Selic anual > 8,5%; senão **70% da Selic a.a., mensalizada** — MP 567/2012 / Lei 12.703/2012 | **SELIC** |
| **2021-12** .. 2024-08 | **SELIC** — art. 3º da EC 113/2021 | **SELIC** — CC art. 406 |
| 2024-09 .. 2025-08 | **SELIC** | **taxa legal** — CC art. 406, red. da Lei 14.905/2024 |
| **a partir de 2025-09** | **taxa legal** | **taxa legal** |

**Duas datas cravadas nas observações dos segmentos, e as duas são `aplicacao`, não taxa:**

- a **Selic de ago/2025 (1,16%)** é computada em **set/2025** — item "c" da NOTA 1;
- a **taxa legal de set/2025 (1,305984%)** é computada em **out/2025** — **D1**.

**NOTA 4, `pagina_pdf` 55, literal:** *"Os juros de mora à base de 70% da taxa Selic ao ano,
mensalizada, quanto esta for igual ou inferior a 8,5%, incidirão **independentemente da data de
vencimento do principal ou do termo inicial dos juros de mora**."* — a regra da poupança **não**
tem eixo no vencimento nem no termo inicial.

**Termo inicial dos juros, literal do JSON de cadeia (`pagina_pdf` 53):** *"Os juros são contados
a partir da citação, salvo determinação judicial em outro sentido."* **`R7`: não é o ajuizamento
(que é o trabalhista) nem o trânsito em julgado (que é a repetição de indébito).**

### 3.1 `N-8` — um ramo paralelo que a tabela NÃO mostra

**NOTA 3 do item 4.2.2, `pagina_pdf` 55, literal:**

> *"Nos créditos referentes a servidores(as) e empregados(as) públicos(as), no período anterior a
> julho/2009, os juros serão computados à taxa de: a) **1% ao mês até jul./2001** (Decreto-Lei n.
> 2.322/1987; AgRg no REsp n. 1.085.995); b) **0,5% ao mês de ago./2001 a jun./2009** (MP n.
> 2.180-35/2001, que acrescentou o art. 1º-F da Lei n. 9.494/1997)."*

A tabela diz **0,5% simples até dez/2002** e **Selic de jan/2003 a jun/2009**. **A nota cria um
caminho inteiro para um subconjunto de credores, e a tabela não o mostra.** Gravado no JSON como
`efeito: "RAMO PARALELO — sobrepõe as duas primeiras linhas da tabela para um subconjunto de
credores"`. **Atrito N-8, registrado e não harmonizado** (`bloco-08-jf-detalhe.md` § 4).

> **É um terceiro ramo por qualidade do CREDOR, não do devedor.** Um motor que resolva a cadeia só
> pelo eixo `devedor` não o alcança.

---

## 4. `R-08-08` — a bifurcação por devedor NÃO é universal

| Cadeia | Bifurca em | Reconverge em |
|---|---|---|
| **Condenatórias — correção** | **dez/2021** | **set/2025** (IPCA-15 para os dois) |
| **Condenatórias — juros** | **jul/2009** | **set/2025** (taxa legal para os dois) |
| Previdenciário — correção | **nunca** | — |
| Repetição de indébito | **nunca** | — |
| **Desapropriação direta** | **nunca** | — |
| Trabalhista-JF — juros | ago/2001 | **nunca** (o ramo empresa pública/prestador segue em 1,0% a.m.) |

**Três cadeias nunca bifurcam por devedor** — previdenciário, repetição de indébito e
desapropriação direta. **Presumir a bifurcação onde ela não existe é erro de cadeia inteira**, e é
o que `R-08-08` existe para impedir.

**Passo 2 do procedimento:** bifurcação entra com **as duas versões**. Competência anterior ao
corte **usa a antiga**. Nunca substituir.

---

## 5. As fórmulas de `aplicacao` — **D1 ≠ D2 sobre a MESMA série**

**NOTA 4 do item 4.2.1, `pagina_pdf` 50, literal e integral:**

> *"A taxa Selic (Sistema Especial de Liquidação e Custódia): a) deve ser capitalizada de forma
> simples, vedada a sua incidência cumulada com os juros de mora e com a correção monetária;
> b) quando se tratar de devedor **não enquadrado como "Fazenda Pública"**, a taxa Selic deve ser
> aplicada **a partir do mês seguinte ao da citação** ou de outro termo inicial dos juros de mora
> **até o mês anterior ao pagamento, e 1% no mês do pagamento**; c) sendo devedora a **Fazenda
> Pública**, a taxa Selic deve ser aplicada **no mês posterior ao de sua competência, inclusive
> para o mês de pagamento**."*

| # | Regra | Onde |
|---|---|---|
| **D1** | Selic **no mês posterior ao de sua competência, inclusive no mês de pagamento**. *Ex.: a Selic de dez/2021 é computada em jan/2022* | **Fazenda, a partir de dez/2021**. A **taxa legal segue D1** — item 4.2.2, NOTA 7 |
| **D2** | Selic **do mês seguinte ao termo inicial dos juros até o mês anterior ao pagamento, e 1% no mês do pagamento** | **não-Fazenda**; e **Fazenda de jan/2003 a jun/2009** |

> **`R-08-09` — D1 e D2 dão resultados diferentes sobre a MESMA série.** D1 desloca a série um mês
> e **inclui** o mês de pagamento; D2 ancora no **termo inicial dos juros**, **exclui** o mês de
> pagamento e o substitui por **1% fixo**. **A mesma Selic, dois números.**

**`R-08-11` — a taxa legal segue D1.** NOTA 7, `pagina_pdf` 56, literal: *"O cálculo da taxa legal
observará o disposto na Resolução CMN n. 5.171/2024 ou no ato normativo que vier a alterá-la. A
taxa legal deverá ser aplicada **no mês posterior ao de sua competência**, de acordo com a
metodologia divulgada pelo Banco Central do Brasil, por meio da ferramenta 'Calculadora do
Cidadão'."*

**As outras duas fórmulas não são desta cadeia:** **D3** (eixo no **recolhimento indevido** —
repetição) e **D4** (competência da parcela — dívida fiscal), ambas em
`references/tributario-federal.md` § 4.

**A metodologia da taxa legal** — razão entre fatores, seis decimais, truncamento, piso zero — não
se repete aqui: `references/civel-cc-nacional.md` § 4 (deflator **IPCA-15**, regra geral) e
`references/previdenciario.md` § 3 (deflator **INPC**, variante). **`R11`: nunca subtração.**

---

## 6. Termos iniciais — `R7`

| Situação | Termo inicial | `pagina_pdf` |
|---|---|---|
| **Juros**, regra geral | **citação**, salvo determinação judicial em outro sentido | 53 |
| Correção — **ato ilícito** | data do **efetivo prejuízo** — **Súmula 43/STJ** | 49 |
| Correção — **dano moral** | o **arbitramento** — **Súmula 362/STJ** | 49 |
| Correção — **servidores(as) e empregados(as) públicos(as)** | **o mês da COMPETÊNCIA, e não o mês de pagamento** | 49 |

NOTA 1 e NOTA 3 do item 4.2.1. **O termo inicial não é intercambiável entre jurisdições** (R7):
trabalhista é **ajuizamento**; repetição de indébito é **trânsito em julgado**.

> **O benefício ASSISTENCIAL cai nesta cadeia, não na previdenciária.** Literal do item 4.3:
> *"Nas condenações relativas a benefícios de natureza assistencial, aplica-se a correção
> monetária das ações condenatórias em geral (item 4.2.1.1 deste manual)."* — e **esta bifurca por
> devedor em dez/2021**, enquanto a previdenciária **nunca bifurca**. É **bifurcação por natureza
> do benefício, eixo não temporal** (`references/previdenciario.md` § 5).

---

## 7. Consolidação de dez/2021 — esta cadeia é um dos cinco lugares

**NOTA 5 do item 4.2.1, `pagina_pdf` 50, literal:**

> *"Sendo devedora a Fazenda Pública, quanto às prestações devidas até dez./2021: a) o crédito será
> consolidado tendo por base o mês de dez./2021 pelos critérios de juros e correção monetária até
> então aplicáveis, considerando, para esse fim, o **IPCA-E de nov./2021 (1,17%)** e os **juros de
> dez./2021 (0,4412%)**; b) sobre o valor consolidado do crédito em dez./2021, **sem exclusão de
> qualquer parcela**, incidirá a taxa Selic a partir de jan./2022 (competência dez./2021) (§ 1º do
> art. 22 da Res. CNJ n. 303/2019, com redação dada pelo art. 6º da Res. CNJ n. 448/2022); c) o
> valor resultante [...] denominado 'Juros Selic', deve ser **integralmente somado à parcela
> denominada 'Juros até 12/2021'**."*

| Ramo | Índice de nov/2021 | Valor | Juros de dez/2021 | Item · `pagina_pdf` |
|---|---|---|---|---|
| **Condenatórias em geral** | **IPCA-E** | **1,17%** | **0,4412%** | 4.2.1, NOTA 5 · **50** |

**`R-08-12`** — são **cinco lugares, três valores de fechamento, uma dispensa**; os **juros de
dez/2021 são os mesmos (0,4412%) nos cinco**, e o índice assume três valores. Quadro completo em
`references/tributario-federal.md` § 8.

**`R-08-14` — "sem exclusão de qualquer parcela":** a SELIC incide sobre o consolidado **inteiro,
principal E juros**. Nos exemplos da `pagina_pdf` 51 há **duas** linhas de dez/2021 — principal
corrigido **R$ 2.275,96** e juros **R$ 55,75** — **ambas recebendo 5,05% de Selic**.

---

## 8. As fixtures 1 a 3 são DESTA cadeia

Do Manual CJF, **item 4.2.1.1, NOTA 6**. Fonte: `docs/calculo/00-base-normativa.md` § 8.

| # | Caso | Esperado |
|---|---|---|
| **1** | **Fazenda Pública**, data-base **jun/2022**. Parcelas 01/2020, 02/2020 e 02/2022 de R$ 1.000,00; citação 01/2021 | **R$ 3.484,95** — principal corrigido 3.275,96; juros até 12/2021 55,75; juros SELIC 153,24 |
| **2** | mesmo caso, data-base **jun/2026** | **R$ 5.218,28** — principal 3.412,64; juros 1.805,64 |
| **3** | **não** Fazenda, data-base jun/2026. Parcelas 01/2002 e 08/2024 de R$ 1.000,00; citação 01/2005 | **R$ 5.772,95** — principal 2.554,45; juros 3.218,50 |

**A divergência de centavos é parte do teste.** Fixture 2: **R$ 0,01** entre detalhado e resumido.
Literal do manual, `pagina_pdf` 53: *"Os dois métodos de cálculo devem conduzir ao mesmo resultado.
Eventuais diferenças de centavos [...] **não decorrem de erro, mas são inerentes ao critério de
truncamento** de casas decimais aplicado em cada etapa do cálculo, sendo, portanto, desprezíveis."*
**Um motor que zera essas diferenças está arredondando errado.**

**Ressalva de extração declarada (`D8-D32`):** o dígito final do método detalhado da fixture 2
(R$ 5.218,27) foi **derivado por aritmética** — a camada de texto do PDF trunca em *"R$ 5.218,2"*
(`pagina_pdf` 52). O valor esperado da fixture, que é o do **método resumido**, **não depende
disso**. `pendencias.md` § 6.

**A fixture 4 é de precatório complementar**, não desta cadeia — `tributario-federal.md` § 7.

---

## 9. ECs 113/2021 e 136/2025, e o precatório

**Não reproduzidos aqui, para não duplicar norma.** Os dois regimes valem para esta cadeia e estão
em `references/tributario-federal.md`:

| Assunto | Onde |
|---|---|
| **EC 113/2021** — redação original, *"independentemente de sua natureza"*, e a refutação do erro **interno** do *"só federal"* | `tributario-federal.md` § 6.1 |
| **EC 136/2025** — requisitórios da Fazenda **federal**, **IPCA + 2% a.a. simples**, trava pela Selic, três estreitamentos simultâneos | `tributario-federal.md` § 6.2 |
| Fase **pré-requisitório**, STJ REsp 2.236.270/SP e STF ARE 1.557.312/SP (Tema 1.419) | `tributario-federal.md` § 6.3 |
| **Precatório** — `C14-02`, eixo **expedição do requisitório ⊕ ente devedor**, as quatro regras que sobrevivem, `R-08-17` | `tributario-federal.md` § 7 |

---

## 10. Invariantes que mordem com força nesta cadeia

- **`R1`** — **SELIC e taxa legal englobam correção E juros.** Nos segmentos de dez/2021 a ago/2024
  (Fazenda) e de jan/2003 a jun/2009 **não existe "correção + SELIC"**. A NOTA 2 do item 4.2.1 e a
  NOTA 4, alínea "a" (*"vedada a sua incidência cumulada com os juros de mora e com a correção
  monetária"*), dizem isso com todas as letras;
- **`R2`** — a exaustividade dos dois ramos é **declarada** em `dominio_condicoes`. As
  sobreposições de **jan/1989** e **mar/1990** são do **original**, não do modelo: a primeira o
  manual explica (`R-08-04`), a segunda **não** (`D8-C21`);
- **`R3`** — o tronco é quase todo **nominal** (ORTN, OTN, BTN, Ufir), todos nomeados na fonte, e
  a ponta **INPC** é **percentual**, também nomeado. Mas **IPCA-E e IPCA-15 são `indeterminado`**:
  nenhuma fonte os classifica, e o item 4.1.2.4 **não nomeia sequer "IPCA"** (`P17-01`). **Cada
  virada entre tipos exige ajuste de defasagem**, sob pena de deslocar o cálculo em um mês — e
  onde a ponta é indeterminada **não se sabe sequer se há virada**;
- **`R4`** — juros **simples**, inclusive a Selic: *"deve ser capitalizada de forma simples"*
  (NOTA 4, "a"). A **`R4-EXCEÇÃO`** (1,0% composta, mar/1987–mar/1991) **não é desta cadeia** — é
  de `cjf.trabalhista.juros-mora` (`trabalhista-nacional.md` §§ 4 e 6);
- **`R5`** — **o piso nominal é POR PARCELA**, não sobre o total: *"considerada cada parcela do
  principal"*, item 4.1.2.2, `pagina_pdf` 42. Fundamento: **REsp 1.265.580**;
- **`R8`** — o cabeçalho *"Caso não haja decisão judicial em contrário"* e a regra do item 4.1
  (*"A decisão judicial é o balizador do cálculo e prevalece sobre as orientações deste manual"*).
  **Única exceção registrada** (`R-08-01`, NOTA 2): **mudança superveniente de legislação sobre o
  indexador passa por cima do título**;
- **`R12`** — **truncamento**, não arredondamento (`pagina_pdf` 53).

---

## 11. Limitações declaradas

1. **Sem preset nomeado no corpus.** O catálogo de `01-plano-extracao.md` tem
   `TRIB-FED-REPETICAO` e `TRIB-FED-DIVIDA-ATIVA`, e **nada para as condenatórias gerais**. Entra
   como **cadeia, não como preset**. Registrado, **não inventado**;
2. **`N-8` — o ramo paralelo dos servidores e empregados públicos (§ 3.1) não é tabulado.**
   Registrado, **não harmonizado**. A tabela e a nota discordam para o período anterior a jul/2009,
   e **o corpus não arbitra**;
3. **`D8-C21` — a sobreposição de mar/1990 não tem justificativa no manual.** O argumento dos
   índices nominais salva jan/1989 e **não alcança** mar/1990. **Pendência**;
4. **`P8-07` — `ponta_materializada` no início.** O manual abre com *"De 1964"*, **sem mês**.
   `1964-01` é materialização de janela, **não afirmação do manual**;
5. **A classificação da devedora como Fazenda Pública é determinação jurídica do usuário do
   módulo**, não matéria de cálculo — e **esta cadeia bifurca por ela duas vezes**. Se a resposta
   for negativa, somem o ramo FP, o precatório, as ECs 113/136 e a consolidação de dez/2021
   (`tributario-federal.md` § 10, item 8);
6. **Fazenda estadual e municipal pós-EC 136/2025:** sem a regra antiga (revogada) e sem a nova
   (que não a alcança). **Lacuna normativa, não de pesquisa**;
7. **ADI 7873 pendente**; **divergência do TJ-SP** registrada e **não arbitrada**
   (`tributario-federal.md` § 6.4);
8. **As séries não estão aqui.** ORTN, OTN, BTN, Ufir, INPC, IPCA série especial, IPCA-E, IPCA-15
   e Selic são dado **(B)** — contrato em `skills/indices-judiciais/`;
9. **O campo `tipo` (nominal/percentual) que `R3` exige não existe em nenhuma série extraída.**
   Está nos **segmentos** desta cadeia (`tipo_indexador`, com `tipo_indexador_fonte` apontando o
   item 4.1.2.4), **não no catálogo de séries**. `bloco-16-relatorio.md` § 6.

---

## 12. Ponteiros

- `docs/calculo/tabelas-normativas/cjf.condenatorias-gerais.correcao-monetaria.json` — 15 segmentos
- `docs/calculo/tabelas-normativas/cjf.condenatorias-gerais.juros-mora.json` — 11 segmentos
- `docs/calculo/consolidado/02-atualizacao-detalhe.md` §§ 5.1, 5.2, 5.3 e 10
- `docs/calculo/extracao/justica-federal/bloco-08-jf.md` §§ 4, 5 e 6 — as sete cadeias, as quatro
  fórmulas de `aplicacao`, a consolidação
- `docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md` § 4 — os doze atritos nota × linha
- `references/desapropriacao.md` — a outra cadeia do cap. 4 sem casa própria antes deste bloco
- `references/tributario-federal.md` §§ 4, 6, 7 e 8 — `aplicacao`, ECs, precatório, consolidação
- `references/previdenciario.md` § 5 — o benefício **assistencial** cai nesta cadeia
- `references/civel-cc-nacional.md` — a cadeia **cível do Código Civil**, que não é esta
