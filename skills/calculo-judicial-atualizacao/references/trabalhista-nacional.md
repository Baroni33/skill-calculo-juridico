# Trabalhista — cadeia NACIONAL

Correção monetária e juros de mora do débito trabalhista, **devedor privado e devedor Fazenda
Pública**, das cadeias históricas ao regime vigente.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` §§ 2, 3, 6, 7, 8, 9, 11 e 12;
`02-atualizacao-detalhe.md` § 5.2; `00-base-normativa.md` §§ 1, 1.1, 2 e 7;
`consolidado/08-nacional-e-regional.md` §§ 1, 5.1, 5.2 e 5.3.

---

## 1. Por que este arquivo se chama "nacional"

> **Origem declarada: EXTERNA AO CORPUS.** Enunciado do bloco 16, declarado verificado em fonte
> externa e **não conferido** nesta fase. O projeto exige a declaração
> (`consolidado/07-leitura-do-corpus.md` § 6).

A atualização monetária trabalhista é **NACIONAL** desde a **Resolução CSJT 8/2005**, que
unificou as **24 tabelas** usadas pelos TRTs e tornou obrigatória a **Tabela Única** em todo o
Brasil. Hoje vale a **Resolução CSJT 380/2024**, com **duas tabelas** — **débitos comuns** e
**Fazenda Pública**, esta tendo como referência o **Manual de Cálculos do CJF**. O **PJe-Calc**,
desenvolvido pelo TRT-8 a pedido do CSJT, é o sistema de cálculo de **toda** a Justiça do
Trabalho.

**Três consequências de arquitetura:**

**(a) A aritmética do manual do TRT-3 não é prática regional divergente.** É procedimento de uma
região que aplica norma nacional. São **nacionais**: o termo inicial dos juros no ajuizamento
(CLT art. 883, Súmula 200/TST), a `aplicacao` no primeiro dia do mês subsequente (Súmula
381/TST), divisores, RSR, arredondamento, ordem INSS→IR, reconstrução de bruto, hora centesimal.
**Regional são os verbetes que ele invoca** — `references/trabalhista-regional-trt3.md`.

**(b) A Tabela Única do CSJT é a dependência que torna o motor nacional.** Não é "integração
desejável": **sem ela não há correção trabalhista em nenhum TRT**, não só no 3. Classificação
correta: **dependência estrutural** (`08-nacional-e-regional.md` § 5.2).

**(c) As cadeias `trab.hist.*` são NACIONAIS com nome enganoso.** Os fundamentos que os próprios
JSON declaram:

| Arquivo | Fundamentos declarados | Alcance real |
|---|---|---|
| `trab.hist.correcao-monetaria.json` | **Súmula 381/TST**; e **delega a cadeia à Tabela Única do CSJT** | **NACIONAL** |
| `trab.hist.juros-mora.json` | **CC arts. 1.062–1.063**; **Lei 8.177/91 art. 39**; CLT art. 883; **Súmula 200/TST** | **NACIONAL** |
| `trab.hist.fazenda-publica.juros-mora.json` | mesma cadeia legal + juros da poupança desde 29/06/09 (**Lei 11.960/2009**) | **NACIONAL** |
| `trab.hist.moedas-e-paridades.json` | padrões monetários e paridades da **moeda nacional** | **NACIONAL** — paridade de moeda não tem região |

O prefixo é do **arquivo de origem**, não da norma. O campo `jurisdicao` já diz
`"justica-do-trabalho"`, **sem recorte regional**, o que corrobora a leitura.

> **Um motor que resolva cadeia por prefixo de tribunal não acha cadeia nenhuma para TRT-1,
> TRT-2 ou TRT-15.** Recomendação registrada e **não aplicada**: renomear para `trab.hist.*` ou
> `csjt.hist.*`, ou declarar `jurisdicao_alcance: "nacional"`.

---

## 2. Devedor privado

### 2.1 Regime vigente — `VIGENTE`

Fonte: STF, **ADC 58** e **ADC 59**; TST, SDI-1, E-ED-RR-713-03.2010.5.04.0029, Rel. Min.
Alexandre Agra Belmonte, j. 17/10/2024, DEJT 25/10/2024.

| Fase | Correção monetária | Juros de mora |
|---|---|---|
| **Pré-judicial** | **IPCA-E** | art. 39, *caput*, da Lei 8.177/1991 (**TRD**) |
| Ajuizamento até **29/08/2024** | **SELIC** — **engloba ambos** (R1) | — |
| A partir de **30/08/2024** | **IPCA** (sem E) | **taxa legal** (CC art. 406, § único) |

- **Marco inicial dos juros: AJUIZAMENTO**, não citação — **R7**. Difere do cível;
- **IPCA-E na pré-judicial, IPCA a partir de 30/08/2024.** A distinção é **do dispositivo do
  acórdão**. Fontes secundárias escrevem IPCA nos dois lugares e **estão erradas**;
- taxa legal por **razão entre fatores**, nunca por subtração — **R11**; admite resultado **zero**
  (CC art. 406, § 3º) — **R6**;
- nenhum segmento SELIC ou de taxa legal admite índice inflacionário no mesmo intervalo — **R1**.

**Regras acessórias do dispositivo:** ressalvados os valores eventualmente pagos, nos termos da
primeira parte do item "i" da modulação; **vedada a dedução ou compensação** de diferenças
apuradas pelo critério anterior.

**Divergência registrada, não resolvida:** parte da doutrina sustenta que aplicar juros pela
**TRD** na fase pré-judicial é **incompatível com a própria ADC 58**, que declarou a TR
inconstitucional para débitos trabalhistas. Entra como **variante `TRAB-ADC58-SEM-TRD`**,
**não como default** (`00-base-normativa.md` § 1; `pendencias.md` § 1).

### 2.1.1 O item "i" da modulação tem DUAS situações — `pr.adc58-item-i`

> **ORIGEM: pesquisa jurisprudencial EXTERNA AO CORPUS**, conferida em **fontes secundárias que
> reproduzem a fundamentação**. **O inteiro teor dos três precedentes do TST não foi lido.**
> Confirmar antes de produção. `00-base-normativa.md` § 1.1; `pendencias.md` § 20.6.

Precedentes citados: TST 6ª Turma, ED-RR (Min. Kátia Magalhães Arruda, DEJT 17/03/2023); TST 7ª
Turma, Ag-RR (Min. Cláudio Mascarenhas Brandão, DEJT 17/03/2023); TST SDI-1, E-Ag-RR (Min. Hugo
Carlos Scheuermann, DEJT 10/03/2023).

**i.1 — pagamento consolidado (regra, e é o default).** Valores pagos **sem qualquer
questionamento** ou objeto de **trânsito em julgado**: não são recalculados; desconsidera-se o
que já foi pago; os índices do STF incidem **apenas sobre o que falta pagar**.

| Alcança | Não alcança |
|---|---|
| depósito com **finalidade de pagamento** | **depósito recursal** |
| **valor incontroverso liberado** ao reclamante | a **parte controversa** do depósito em garantia |

**i.2 — execução questionada (exceção).** Execução instaurada **após o início dos debates da
ADC 58**, com **questionamento expresso** de qualquer das partes: a atualização usa os novos
índices **inclusive sobre valores já pagos**.

**Consequência:** **em i.1 não há o que ratear** — o pago sai da conta. **Em i.2 o rateio se
aplica**, sobre valores recalculados. O conflito entre o rateio proporcional do manual e a
modulação é **condicional, não estrutural**. A escolha **não é derivável do cálculo**: depende de
estado processual e de evento.

### 2.2 Cadeia histórica — `BIFURCADO` (`CH-01`, `CH-02`, `CH-04`)

**Estas linhas continuam sendo a regra aplicável às competências que cobrem.** O que caduca é
usá-las para competências **posteriores** ao corte da ADC 58 (**18/12/2020**), **eixo =
competência da parcela**.

**Correção** — `trab.hist.correcao-monetaria` (cap. 7, `pagina_pdf` 83–85):

| Período | Indexador | Fundamento | Veredito |
|---|---|---|---|
| 1942-11 .. 1991-02 | **`NAO-DECLARADO-PELO-MANUAL`** | — | **pendência `P9-02`** — § 5 |
| 1991-03 .. 2009-06 | **TR** | art. 39 da Lei 8.177/91 | `BIFURCADO` **CH-01** |
| 2009-07 .. 2016-05 | **TR** | art. 39 da Lei 8.177/91 | `BIFURCADO` **CH-02** |

`aplicacao`: **`primeiro-dia-do-mes-subsequente-a-prestacao`** — Súmula 381/TST, `pagina_pdf` 84.
Ver § 7.

**Juros** — `trab.hist.juros-mora` (quadro sinóptico, `pagina_pdf` 89) — `CH-04`:

| Período literal | Taxa | Capitalização | Fundamento |
|---|---|---|---|
| ajuizamento até **26/02/87** | 0,5% a.m. | simples | CC/1916, arts. 1.062 e 1.063 |
| **27/02/87 a 03/03/91** | 1,0% a.m. | **COMPOSTA** | DL 2.322/87, art. 3º — **`R4-EXCEÇÃO`**, § 4 |
| **04/03/91** até a satisfação | 1,0% a.m. | simples | Lei 8.177/91, art. 39 |

**Termo inicial: ajuizamento** (CLT 883; Súmula 200/TST), **salvo parcelas vincendas**, que
seguem a **época própria** (`pagina_pdf` 88).

**Situações especiais, transcritas sem harmonização** (`pagina_pdf` 89):

- **intervenção ou liquidação extrajudicial** — juros até a decretação (**Súmula 304/TST**);
- **falência** — juros limitados à data da falência **apenas se houver determinação nos autos**
  (art. 124 da Lei 11.101/05). O manual transcreve **três ementas do TRT-3, duas delas
  divergentes entre si**. **Regional** — `trabalhista-regional-trt3.md` `R13`.

> **Ponteiro, sem harmonização a fazer:** o cap. 16 registra a **Súmula 388 do TST** e o **art.
> 83 da Lei 11.101/05** (item 16.4.9.2). **O que a Súmula 388 decide é outro ponto**: ela isenta
> a massa **apenas** do art. 467 e do art. 477, § 8º — **INSS, IR e custas continuam integrando
> a execução** (armadilha **A21**, p. 332).

### 2.3 O que é `SUPERADO`, e para onde vai

| ID | O que o manual diz | Corte | Destino |
|---|---|---|---|
| **F7-04** | *"atualmente a TR"* (`pagina_pdf` 129, 138, 148, 149, 155) | **18/12/2020** | armadilhas, **com a data** |
| **JR-05** | OJ 300 da SDI-1 valida a TRD do art. 39 | ver F7-04 | consequência de F7-04, não ponto autônomo |
| **AM-01** | o item 10.1 pressupõe o critério pré-ADC 58 | ver F7-04 | **cai o índice, não o método** |

**Busca declarada em `AM-01`:** `compensa`, `ADC 58` e `IPCA` têm **zero ocorrências nas pp.
209–223**.

**O episódio IPCA-E fica como história, não como norma:** TST, ArgInc 479-60.2011.5.04.0231
(04/08/15) declarou a TR inconstitucional; **STF, Rcl 22012 MC/RS (14/10/15) suspendeu** —
*"permanece válida a TR"*. É o estado em que o manual congelou (`pagina_pdf` 84).

### 2.4 `AM-03` — `BIFURCADO` por segmento, não por data

Sob SELIC a distinção **principal × juros** perde objeto: no período de SELIC única **não há o
que ratear**. Enquanto houver período de índice + juros separados, o rateio do item 10.3 tem
objeto. **A conta real atravessa os dois regimes, logo os dois coexistem por segmento.**
Não é supersessão — é **mudança de natureza da operação**.

---

## 3. Devedor Fazenda Pública

### 3.1 Regime vigente — `VIGENTE`, com pendência declarada

Ramo **ressalvado expressamente** pela ADC 58.

| Período | Correção | Juros |
|---|---|---|
| Até **nov/2021** | **IPCA-E** | Lei 11.960/2009 |
| A partir de **dez/2021** | **SELIC** — **engloba ambos** | — |

Fonte: TST, 2ª Turma, ata da 17ª sessão ordinária de 2026 (RR 131300-14.2010.5.21.0006).

> **Pendência aberta, não resolvida por inferência:** o efeito da **EC 136/2025** sobre a Justiça
> do Trabalho **não foi consolidado pelo TST nem pelo CSJT** (base § 9, pendência 3). **Não se
> estende a cadeia do CJF ao trabalhista por analogia.**

**A EC 113/2021 não era "só federal".** A redação original diz *"independentemente de sua
natureza"*. A restrição a requisitórios federais é **criação da EC 136/2025** — `C14-01`,
`tributario-federal.md` § 6.

### 3.2 Cadeia histórica — `BIFURCADO` (`CH-03`, `CH-05`)

**Correção, ramo Fazenda** (`pagina_pdf` 85) — `CH-03`:

| Período | Indexador | Fundamento |
|---|---|---|
| 2009-07 .. 2016-05 | remuneração básica da poupança (**TR**) | art. 1º-F da Lei 9.494/97, redação do art. 5º da Lei 11.960/09 — corte ao dia **29/06/2009** |

**Juros** — `trab.hist.fazenda-publica.juros-mora`, quadro de **cinco** linhas, `pagina_pdf` 92 —
`CH-05`. *(Não três: a primeira extração lera o resumo em prosa da p. 90.)*

| Período literal | Taxa | Fundamento |
|---|---|---|
| ajuizamento até 26/02/87 | 0,5% a.m., simples | CC, arts. 1.062 e 1.063 |
| **27/02/87 a 03/03/91** | 1,0% a.m., **COMPOSTA** | DL 2.322/87, art. 3º — **`R4-EXCEÇÃO`** |
| 04/03/91 a 26/08/01 | 1,0% a.m., simples | Lei 8.177/91, art. 39 |
| 27/08/01 a 28/06/2009 | 0,5% a.m., **limitado a 6% ao ano** | Lei 9.494/97, art. 1º-F (MP 2.180-35/2001) |
| 29/06/2009 até o pagamento | juros da poupança, **sem cumulação** | Lei 9.494/97, art. 1º-F (art. 5º da Lei 11.960/09) |

**O limite de 6% a.a. não é redundante com 0,5% a.m.:** 0,5% simples por doze meses dá exatamente
6%, mas **o limite morde em qualquer contagem por dias que ultrapasse o ano**.

**Subcorte 04/05/2012** (MP 567/12 → Lei 12.703/12, `pagina_pdf` 91) — modelado como
**qualificação do último segmento, não como segmento próprio**: a **regra** (art. 1º-F, poupança)
não muda; **muda a fórmula da poupança**. Literal: *"Até 03/05/2012, os juros aplicáveis à
caderneta de poupança, correspondiam a 0,5% ao mês."*

**Série (B) embutida na cadeia** — **único lugar do capítulo 7 em que o manual crava percentual
mês a mês** (`pagina_pdf` 92; art. 12, II, "b", da Lei 8.177/91):

| jun/12 | jul/12 | ago/12 | set/12 | out/12 | nov/12–abr/13 | mai/13 | jun/13–jul/13 | ago/13 |
|---|---|---|---|---|---|---|---|---|
| 0,4828% | 0,4828% | 0,4551% | 0,4273% | 0,4273% | 0,4134% | 0,4273% | 0,4551% | 0,4828% |

Total impresso **6,5760%**; atalho do manual `15 × 0,5% = 7,5%`, diferença `0,9240%`.
**Conferido em `Decimal`: fecha exato.**

### 3.3 Fazenda **subsidiária** — ramo declarado e deliberadamente VAZIO

`pagina_pdf` 93, literal: *"grande parte da jurisprudência entende que os juros de mora são de 1%
ao mês de acordo com o art. 39 da Lei 8.177/91 (...) nos termos da OJ 382 da SDI-1/TST"*.

**"Grande parte da jurisprudência entende" é corrente, não regra assentada.** O quadro da
`pagina_pdf` 92 é expresso: vale para a Fazenda **"como reclamada principal"**. O ramo
`fazenda-publica-subsidiaria` é declarado em `dominio_condicoes` e **não recebe segmento**. O
validador o reporta como lacuna — **leitura correta**. **Pendência `P9-01`.**

> **Um motor que aplique 0,5% a.m. à Fazenda subsidiária erra por leitura de condição não
> qualificada.** Foi o defeito da primeira versão da cadeia.

### 3.4 `R9` — Fazenda Pública é atributo do PROCESSO

Não é configuração de sistema nem cadastro da empresa. **A mesma parte pode receber
classificações distintas em processos distintos.**

**E o manual não resolve quem é Fazenda Pública:** cap. 8 (`pagina_pdf` 102) isenta os entes
*"que não explorem atividade econômica"*; cap. 14 (306) isenta a administração *"direta e
indireta"*, **sem a ressalva**. **Dois testes incompatíveis para a mesma pergunta** — `P13B-02`.
**Busca declarada:** `economia mista` → **zero ocorrências nas 471 páginas**; a única equiparação
nominada é a **ECT**, e só *"para efeito de execução e do DL 779/1969"*.

---

## 4. `R4-EXCEÇÃO` — juros COMPOSTOS de 27/02/1987 a 03/03/1991

**Invariante R4:** juros de mora, SELIC e taxa legal são **sempre simples**. Capitalização mensal
só em juros remuneratórios.

**A exceção de quatro anos**, por força do **DL 2.322/87, art. 3º**, confirmada por **três
registros independentes, duas jurisdições, edições separadas por dez anos**:

| Fonte | Onde | Diz |
|---|---|---|
| TRT-3, quadro geral | `pagina_pdf` 89 | *"1,0% ao mês, c/ taxa capitalizada. Ex.: **3 meses = 3,03%**"* |
| TRT-3, quadro da Fazenda | `pagina_pdf` 92 | idem |
| CJF, cap. 4 (`cjf.trabalhista.juros-mora`) | `pagina_pdf` 78 | *"De mar./1987 a mar./1991 — 1,0% — **composta**"* |

**Não é erro de transcrição de nenhum dos dois manuais.** Gravada no campo `ALERTA_R4` dos
segmentos e **dentro do invariante**.

> **Atenção à diferença de granularidade entre as duas fontes:** o TRT-3 dá o corte **ao dia**
> (27/02/87 e 03/03/91); o CJF dá **ao mês** (mar/1987 a mar/1991). Registrado como está, **não
> harmonizado**.

---

## 5. `P9-02` — a cadeia anterior a 03/1991 NÃO é derivável do manual

**Governa o arquivo.** O capítulo 7 **não tem mapa período → indexador de correção monetária**.
**Não é omissão do extrator: é desenho do manual**, e ele diz por quê, literal na `pagina_pdf`
**85**:

> *"A tabela mensal de correção está escalonada em meses e anos, já computa as conversões e
> paridades da moeda nacional e não contém juros."*

O TRT-3 **delega o encadeamento inteiro à Tabela Única do CSJT** (Res. CSJT 08/2005, vigente a
partir de **novembro/2005**; **até outubro/2005 o TRT-3 publicava tabela própria**,
`pagina_pdf` 84). A cadeia vive numa **série — categoria (B), dado externo** — e não numa regra.

**Busca negativa, com escopo declarado:** varredura das **dezessete páginas do capítulo 7**
(`pagina_pdf` 83–99) por `IPC`, `IGP`, `INPC`, `expurgo`, `ORTN`, `OTN`, `BTN`, `Ufir`, `42,72`,
`10,14`, `6,17`, `6,92`, `126,8621` — **nenhuma ocorrência**. "IPC" só aparece dentro de
"IPCA-E". **Isto vale para o capítulo 7, não para as 471 páginas.**

**Consequência:** o segmento `1942-11 .. 1991-02` tem `indexador:
"NAO-DECLARADO-PELO-MANUAL"`, **não "TR"** — a TR foi criada pelo art. 39 da Lei 8.177/91, de
**março de 1991**, e **não existia no período**.

**A ponte não é inferida.** O tronco do CJF (1964–fev/1991) **cobre** o período, mas **o corpus
não faz a remissão** — usá-lo como cadeia trabalhista seria **ponte inventada**.

**A TR foi REBAIXADA a `tipo_indexador: "indeterminado"` no bloco 17.** Era `percentual` por critério **formal** do item 4.1.2.4 — não é unidade monetária, logo é percentual —, mas o critério **material** daquele item (*"refletem a inflação do próprio mês"*) **não a alcança**: é taxa apurada **prospectivamente** (art. 12, I, da Lei 8.177/91). **Nenhum dos dois manuais classifica a TR**, e **inferência declarada não é fonte**. Pendência `P17-02`; o validador bloqueia a virada sob `R3-INDETERMINADO`.

---

## 6. A cadeia trabalhista **na Justiça Federal** — `cjf.trabalhista.juros-mora`

Cadeia **autônoma** do Manual CJF (item 4.7.2, `pagina_pdf` 78), e **não é a mesma** das §§ 2–3.

| Período | Devedor | Taxa |
|---|---|---|
| 1964-01 .. 1987-02 | — | 0,5% a.m. |
| **1987-03 .. 1991-03** | — | **1,0% a.m., COMPOSTA** — `R4-EXCEÇÃO` |
| 1991-04 .. 2001-07 | — | 1,0% a.m. |
| 2001-08 .. 2012-04 | Fazenda Pública | 0,5% a.m. |
| 2001-08 .. 2012-04 | **empresa pública / prestador de serviços** | **1,0% a.m.** |
| 2012-05 .. 2021-11 | Fazenda Pública | poupança: 0,5% a.m. se a Selic anual > 8,5%; senão 70% da Selic a.a., mensalizada |
| 2012-05 .. 2021-11 | empresa pública / prestador | **1,0% a.m.** |
| 2021-12 .. 2025-08 | Fazenda Pública | **Selic** |
| 2021-12 .. 2025-08 | empresa pública / prestador | **1,0% a.m.** |
| 2025-09 .. 2026-06 | Fazenda Pública | **taxa legal** |
| 2025-09 .. 2026-06 | empresa pública / prestador | **1,0% a.m.** |

**Bifurca em ago/2001 e NUNCA reconverge.** O ramo empresa pública/prestador segue em **1,0%
a.m.** até o fim da janela.

**Consolidação de dez/2021 neste ramo:** índice de nov/2021 = **TR = 0,00%**; juros de dez/2021 =
**0,4412%** (item 4.7.2, NOTA 2, `pagina_pdf` 79). **A TR de 0,00% significa que, nesse ramo, o
principal não se move em nov/2021.**

---

## 7. As três defasagens de correção — e a QUARTA régua dos juros

O manual opera **três réguas de correção**, e os **juros usam uma quarta, incompatível com a
terceira**.

| # | Defasagem | Granularidade | Onde | Regra |
|---|---|---|---|---|
| 1 | **Súmula 381/TST** | **um mês** | tabela mensal, `pagina_pdf` 84 | índice do mês **seguinte** ao da prestação |
| 2 | tabela **diária** do CSJT | **um dia** | item 7.5.2, `pagina_pdf` 87 | TR acumulada **até o dia anterior** à data final informada |
| 3 | **pro-ratização** | **dias úteis** | item 7.5.2, `pagina_pdf` 87 | o índice mensal é decomposto por **dias úteis**, não corridos |
| 4 | **juros** | **mês comercial de 30 dias** | item 7.6, `pagina_pdf` 88 | 1% a.m. ou `1/30` ao dia |

**Régua 1 — a mecânica importa mais que a regra.** A tabela já posiciona o índice *"no próprio mês
da constituição do crédito"* (`pagina_pdf` 85), de modo que **aplicar a Súmula 381 equivale a
usar o índice do mês SEGUINTE**. Exemplo do manual: horas extras de **junho/14** → índice de
**julho/14**. *Quem lê a súmula sem a tabela, ou a tabela sem a súmula, erra por um mês.*

**Régua 2 — com o contra-exemplo do próprio manual.** `01/05/16` a `31/05/16` devolve
`1,001459947`, que é a TR de **01/05 a 30/05**. Para maio cheio é preciso informar **01/06/16**.

**Régua 4 — defeito do original registrado.** A regra imprime `0,0333%` e o exemplo, **duas linhas
abaixo**, `0,03333%`. No exemplo do manual (11/05/00 a 30/04/04, 47 meses e 20 dias) ambos dão
`47,67%`; **em contagens longas de dias, muda**. Por **R12**, o motor computa **1 dividido por 30
em decimal exato**, **nunca o truncamento impresso**.

**Contagem inclusiva do mês comercial:** `dias = 30 − dia_inicial + 1`. Testado em cinco períodos:
**5 de 5 fecham pela regra inclusiva, 0 de 5 pela exclusiva**. A **fórmula** aparece nos exemplos;
a **convenção de contagem**, não.

> **Correção pro-ratizada por dias úteis e juros por dias corridos/30 no mesmo cálculo é atrito
> real do manual.** Registrado, **não harmonizado**.

---

## 8. `status_norma` — `BIFURCADO`, não `SUPERADO`

| ID | Cadeia / segmento | `status_norma` no JSON | Veredito |
|---|---|---|---|
| **CH-01** | `trab.hist.correcao-monetaria` 1942-11..2009-06 | `superado` | **`BIFURCADO`** |
| **CH-02** | idem 2009-07..2016-05 (não-Fazenda) | `superado` | **`BIFURCADO`** |
| **CH-03** | idem 2009-07..2016-05 (Fazenda) | `superado` | **`BIFURCADO`** |
| **CH-04** | `trab.hist.juros-mora` 1991-04..2016-05 | `superado` | **`BIFURCADO`** |
| **CH-05** | `trab.hist.fazenda-publica.juros-mora` 2009-07..2016-05 | `superado` | **`BIFURCADO`** |

> **O `status_norma: "superado"` está certo quanto ao futuro e incompleto quanto ao passado.** O
> segmento continua sendo a regra aplicável às competências que cobre — **é essa a razão de a
> cadeia histórica existir**. O que caduca é usá-lo para competências **posteriores** ao corte da
> ADC 58. **Cadeia temporal, não supersessão** — a mesma estrutura da Res. 225/2025 do TST.

**Instrução para o motor:** **não apagar, não substituir.** Ler `status_norma` como **fronteira
superior do segmento**, não como invalidade. Por **R19**, toda conta que atravesse o corte grava
**qual lado aplicou a cada competência**.

---

## 9. Pendências e defeitos que atravessam esta cadeia

| ID | Estado |
|---|---|
| **`P9-01`** | juros da Fazenda **subsidiária** — ramo sem segmento, **por decisão** |
| **`P9-02`** | índice de correção **anterior a 03/1991** não declarado — **bloqueia o motor trabalhista** |
| **`P9-03`** | termo inicial de juros em processos vindos da Justiça Estadual ou Federal (`pagina_pdf` 95) |
| **`P9-04`** | termo inicial e índice **por tipo de verba** — Súmula 439/TST, Súmula 15/TRT-3, OJs 181, 198 e 302 (`pagina_pdf` 83) |
| **`P9-05`** | juros **vincendos** (mecânica de decréscimo) — método, não mapa; fora do escopo dirigido |
| **base 3** | efeito da **EC 136/2025** na Justiça do Trabalho — aguarda TST/CSJT |
| **`A5`** | índice de dez/10 (`pagina_pdf` 96) **quebra a monotonicidade**. **O erro está no índice publicado; o valor está certo** |
| **`DEFEITO_DO_ORIGINAL`** | `trab.hist.moedas-e-paridades` (`pagina_pdf` 99): a 1ª linha termina em **12/02/70** e a 2ª começa em **13/02/67** — **três anos de sobreposição**; quase certamente era 12/02/67. **Registrado, não corrigido** |

---

## 10. Ponteiros

- `docs/calculo/consolidado/02-atualizacao.md` §§ 2, 3, 6, 7, 8, 9, 12 — a espinha
- `docs/calculo/consolidado/08-nacional-e-regional.md` §§ 1, 5.1–5.3 — a classificação
- `docs/calculo/extracao/trabalhista/bloco-09-cadeias-historicas.md` — cadeias, defasagens, moedas
- `docs/calculo/tabelas-normativas/trab.hist.*.json` — as cadeias em schema `cadeia-temporal`
- `references/trabalhista-regional-trt3.md` — o que neste ramo **não** é nacional
