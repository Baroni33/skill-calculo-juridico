# Nacional e regional — classificação das regras do consolidado

**Bloco 16, tarefa 0.** Percorre os **11 arquivos** de `docs/calculo/consolidado/` e classifica cada
regra como **NACIONAL**, **REGIONAL** ou **DÚVIDA**. Não altera nenhum arquivo do consolidado: é
documento de classificação, e a aplicação fica para depois.

---

## 1. A correção de premissa

> **Origem declarada: EXTERNA AO CORPUS.** O que segue **não tem lastro em nenhum arquivo deste
> repositório**. Vem do **enunciado do bloco 16**, que o declara verificado em fonte externa. Não
> foi conferido por pesquisa nesta tarefa, e o projeto exige que toda afirmação sem lastro no
> corpus declare a origem (`07-leitura-do-corpus.md` § 6).

A atualização monetária trabalhista é **NACIONAL** desde a **Resolução CSJT 8/2005**, que unificou
as **24 tabelas** usadas pelos TRTs e tornou obrigatória a **Tabela Única** em todo o Brasil. Hoje
vale a **Resolução CSJT 380/2024**, com duas tabelas — **débitos comuns** e **Fazenda Pública**,
esta tendo como referência o **Manual de Cálculos do CJF**. O **PJe-Calc**, desenvolvido pelo
**TRT-8** a pedido do CSJT, é o sistema de cálculo de toda a Justiça do Trabalho.

**O que isto corrige.** O projeto vinha tratando o **manual do TRT-3** como *fonte de prática
regional*. Está errado. O manual é **fonte procedimental de uma região que aplica norma nacional**
— e o próprio corpus já dizia isso sem tirar a consequência: `02-atualizacao.md` § 6 registra que
*"o TRT-3 **delega o encadeamento inteiro à Tabela Única do CSJT** (Resolução CSJT 08/2005, vigente
a partir de **novembro/2005**; até outubro/2005 o TRT-3 publicava tabela própria, `pagina_pdf` 84)"*.

**Duas consequências de arquitetura:**

- **(d)** A **aritmética** do manual do TRT-3 — divisores, RSR, arredondamento, ordem INSS→IR,
  reconstrução de bruto, hora centesimal — **NÃO é prática regional divergente**. O que dele é
  regional são **as súmulas que ele invoca**.
- **(e)** A **Tabela Única do CSJT** deixa de ser *"integração desejável"* e passa a ser **a
  dependência que torna o motor nacional**. Em `00-validacao-casos.md` § C33 ela figura entre as
  *três dependências externas*; a classificação correta é **dependência estrutural**.

---

## 2. As duas regras de classificação aplicadas

| Rótulo | Critério |
|---|---|
| **NACIONAL** | lei federal, CF, súmula/OJ/tese do TST, STF, STJ, resolução CSJT/CNJ/CJF, IN da Receita |
| **REGIONAL** | súmula, OJ ou tese prevalecente de **um** TRT ou TJ (art. 896, § 6º, CLT) — vincula a região, pode divergir entre regiões até o TST uniformizar |
| **DÚVIDA** | usado sem hesitação. Não se presume tribunal, não se presume vigência |

**Fora das duas listas por definição do enunciado, e portanto NACIONAIS:** divisores (Súmula 431 e
**IRR-849** do TST), RSR, critérios de arredondamento, cadeias de indexador, e **toda regra de CLT,
CPC e Código Civil**.

---

## 3. Escopo da busca — declarado

**Varredura 1 — os 11 arquivos de `docs/calculo/consolidado/`**, `grep -rn -i`, termos:
`TRT-3`, `TRT3`, `TRT 3`, `TJMG`, `CGJ`, `tese prevalecente`, `896`, `regional`, `Súmula 15`,
`Súmula 46`, `OJ 23`, `TRT-`, mais os regex `TRT-?[0-9]+`, `SEE/TRT-[0-9]`, `TJ[A-Z]{2}`,
`Provimento`, `001/02|001/2002`, `OJ 348`, `IRR-849`, `Súmula 431`.

**Varredura 2 — repositório inteiro** (`--include=*.md --include=*.json`), termos
`tese prevalecente`, `TJP [0-9]`, `art. 896, § 6`.

**Varredura 3 — dirigida**, fora do consolidado mas dentro do corpus de apoio:
`jurisprudencia-indice.md` (158 verbetes, seções **17.5 a 17.8**) e `02-base-normativa-verbas.md`.

**Resultados de ausência, com escopo:**

- `tese prevalecente` e `art. 896, § 6º` — **zero ocorrências em todo o repositório**. O consolidado
  nomeia a figura só pela sigla **`TJP 4`** (`06-encargos.md` § 5.2) e pelo título da seção **17.7**
  do índice.
- `TRT 3` com espaço, `TRT3` como referência a tribunal (e não a nome de arquivo) — **zero no
  consolidado**.
- `regional` como palavra — **uma única ocorrência no consolidado**, `06-encargos.md` § 2.1, e é o
  próprio corpus chamando a IN 001/02 de *"IN regional"*.
- Nenhum **TJ estadual** além do **TJMG** aparece no consolidado.

**A busca NÃO foi exaustiva do ponto de vista do universo de verbetes regionais existentes** — ela é
exaustiva **sobre o texto do consolidado**. O `jurisprudencia-indice.md` cataloga **15 súmulas do
TRT-3, 3 OJs de Turmas do TRT-3, 2 Teses Jurídicas Prevalecentes e 4 Provimentos do TRT-3** — **24
verbetes regionais** no capítulo 17 do manual, dos quais o consolidado só invoca os listados na
§ 4.

---

## 4. Tabela das regras REGIONAIS

**Achado: são mais de três.** O enunciado nomeia Súmula 15, Súmula 46 e OJ 23. O consolidado invoca
**pelo menos nove verbetes regionais nominados**, mais quatro fontes regionais não-verbete.

| # | Verbete / fonte | Tribunal | O que muda no resultado | Arquivo e seção | Fallback nacional quando não houver súmula regional |
|---|---|---|---|---|---|
| **R1** | **Súmula 15** — execução, depósito em dinheiro, atualização e juros: a responsabilidade do executado **não cessa com o depósito** | **TRT-3** | dedução na **data do levantamento** (depósito em garantia) × **data do depósito** (depósito para pagamento) — muda o principal deduzido e a existência de diferença a apurar | `05-imputacao.md` § 5; `02-atualizacao.md` § 12 (`P9-04`); `07-leitura-do-corpus.md` § 4 | **ADC 58, item "i"** (`05-imputacao.md` § 4) e **CC arts. 352–355** (imputação) — e, na falta, o critério do **cap. 14, p. 306, letra "c"**: dedução na **data do pagamento**, salvo determinação do juízo |
| **R2** | **Súmula 46** — base do adicional de insalubridade é o **salário mínimo**, salvo critério mais vantajoso | **TRT-3** | troca a base do adicional: mínimo × salário contratual/piso — altera o adicional e todos os reflexos | `03-verbas.md` § 5.9 e § 10 (pendência de vigência) | **Súmula 228/TST** (cassada, MC na ADPF 151/STF) + **Súmula Vinculante 4/STF** — o conflito fica **aberto**, não resolvido aqui |
| **R3** | **OJ 23 das Turmas** — jornada 12×36, **divisor 210** | **TRT-3** | divisor do salário-hora na 12×36: 210 × 220 — muda o valor de toda hora extra e de todo adicional calculado sobre hora | `03-verbas.md` § 5.6 | **IRR-849 do TST**, tese 3 (divisor decorre da jornada; horas **remuneradas**) + **Súmula 431/TST** + **art. 64 da CLT** — `01-dominio-e-invariantes.md` § 2.7 |
| **R4** | **Súmula 24** — contribuições devidas a **terceiros**: incompetência da JT para executar | **TRT-3** | tira as contribuições de terceiros da conta (`R-07-16`) — reduz o total de INSS executado | `04-descontos.md` § 2.1 | **art. 114, VIII, da CF** + **Súmula 368, I, do TST** (competência limitada às contribuições do art. 195, I, "a", e II) |
| **R5** | **Súmula 45** — fato gerador da contribuição previdenciária até **04/03/2009** é o **pagamento** (regime de caixa) | **TRT-3** | escolhe o regime de apuração do INSS antes de 05/03/2009 — caixa × competência; muda alíquota, teto e atualização | `04-descontos.md` § 2.2 e § 2.4 (`R-07-08`, `F7-11 VIGENTE`); `04-descontos-detalhe.md` § 3.6 | **art. 43, § 2º, da Lei 8.212/91** (redação da MP 449/2008 → Lei 11.941/2009) e **Súmula 368, III, do TST** — o corte de **05/03/2009** é nacional e **sobrevive** ao verbete |
| **R6** | **TJP 4** — Tese Jurídica Prevalecente: a **cota-parte patronal** de contribuição previdenciária **não integra** a base dos honorários advocatícios | **TRT-3** | exclui R$ 18.574,26 da base no exemplo da `pagina_pdf` 106 — reduz os honorários | `06-encargos.md` § 5.2 e § 1 | **art. 791-A da CLT** — *"valor que resultar da liquidação da sentença"* — e **art. 85, §§ 2º a 5º, do CPC** para a Fazenda |
| **R7** | **Súmula 39** — art. 384 da CLT, intervalo de 15 min da mulher — **cancelada** pela **RA 123/2025**, perda de eficácia a partir de **11/11/2017** | **TRT-3** | enquanto viva, criava parcela (15 min extras diários); cancelada, **não há parcela** | `03-verbas.md` § 2 (`B04-F6`) | **art. 384 revogado** pela Lei 13.467/2017 + **STF Tema 528** + **TST Tema 63**, delimitados ao período anterior |
| **R8** | **Súmula 48** — prazo do art. 477 — **superada e cancelada** no portal do TRT-3; **o manual não a invoca** (zero em 471 páginas) | **TRT-3** | nenhuma, hoje: o prazo foi unificado em **10 dias corridos** | `03-verbas.md` § 5.11 | **art. 477, § 6º, da CLT** (redação da Lei 13.467/2017) + **Teses 71 e 139 do TST** |
| **R9** | **Súmulas 2 e 38** — turno ininterrupto de revezamento, horas além da 6ª, **divisor 180** | **TRT-3** | divisor do turno de revezamento | `03-verbas.md` § 5.6 | **OJ 396 da SDI-1/TST** (citada no mesmo parágrafo) + **art. 7º, XIV, da CF** — o fallback já está **ao lado** do verbete regional, o que torna a substituição barata. **Ver D3: a Súmula 38 não consta do índice.** |
| **R10** | **Tabela CGJ/TJMG** — correção monetária cível em Minas | **TJMG** (Corregedoria-Geral de Justiça) | índice de correção do crédito cível para períodos **anteriores a jan/2003** | `02-atualizacao.md` § 1 (linha 4 do quadro) e § 4 | **STJ, Tema 1368** (Corte Especial, j. 15/10/2025, REsp 2.199.164/PR e REsp 2.070.882/RS), **vinculante** — ver § 6.1 abaixo |
| **R11** | **IN GP/CR/VCR 001/2002 do TRT-3** — arts. 2º e 6º e **Anexo II** (14 rubricas de custas de execução C-1 a C-14, emolumentos E-1 a E-8, teto R$ 1.915,38, CE de 0,5% até R$ 638,46) | **TRT-3** | fixa **todos os valores** de custas de execução e emolumentos — valores nominais de 2002, **sem atualização monetária** | `06-encargos.md` § 1, § 2.1, § 3 | **CLT arts. 789-A e 789-B** (a CLT dá as rubricas e os valores do art. 789-A; a IN regulamenta) + **IN 20/2002 do TST**. Fora do TRT-3 há **outra IN regional**, e os valores do Anexo II **não valem** |
| **R12** | **Acórdão TRT-3, AP 0001624-31.2012.5.03.0010** — sentença que defere reflexo em RSR não autoriza incluir feriados | **TRT-3** | limite de coisa julgada: impede inclusão de feriados no reflexo | `03-verbas.md` § 5.5 | **CLT art. 67 + Lei 605/49** e **art. 879, § 1º, da CLT** (limites do comando exequendo) — a distinção RSR × feriado é **nacional**; o acórdão só a ilustra |
| **R13** | **Três ementas do TRT-3 sobre juros na falência**, *"duas delas divergentes entre si"* | **TRT-3** | se os juros param na decretação da falência | `02-atualizacao.md` § 2.2 | **art. 124 da Lei 11.101/05** + **Súmula 388/TST** (esta só quanto às multas dos arts. 467 e 477) |
| **R14** | **SEE/TRT-4** — RSR sobre comissões **integram** a base das HE variáveis (Súmula 264) | **TRT-4** | inclui ou exclui o RSR da base da HE do comissionista | `03-verbas.md` § 5.10 | **Súmula 264/TST** + **Súmula 340/TST** + **OJs 235 e 397** — a divergência é registrada, **não arbitrada** |
| **R15** | **Tabela própria do TRT-3 até outubro/2005** | **TRT-3** | índices de correção do débito trabalhista até out/2005 | `02-atualizacao.md` § 6 | **Tabela Única do CSJT** (Res. 8/2005) a partir de **nov/2005**; antes disso, **não há fallback nacional no corpus** — é lacuna, ligada a `P9-02` |

> **Total: 15 itens REGIONAIS**, dos quais **9 são verbetes** (súmula/OJ/TJP) — R1 a R9 — e **6 são
> fontes regionais não-verbete**: uma tabela de corregedoria (R10), uma instrução normativa (R11),
> dois conjuntos de acórdãos (R12, R13), uma posição de órgão fracionário de outro TRT (R14) e uma
> tabela administrativa histórica (R15).

---

## 5. NACIONAL que se confunde com regional

### 5.1 A aritmética do manual do TRT-3 — **NACIONAL**, diretriz (d)

Nada disto é prática regional divergente. É procedimento de uma região aplicando norma nacional:

| Regra | Onde vive | Fonte que sustenta a classificação |
|---|---|---|
| Ordem **INSS antes de IR**, base do IR = líquido de INSS (`R-07-01`) | `04-descontos.md` § 2.1 | art. 74 do Dec. 3000/99; IN RFB 1.500/2014 |
| Assimetria das cotas empregado/empregador (`R-07-02`) | `04-descontos.md` § 2.1 | art. 20 e art. 22 da Lei 8.212/91 |
| Base do INSS = valor **original**, correção depois (`R-07-10`), bloqueio pelo teto (`R-07-11`) | `04-descontos.md` § 2.4 | art. 20 da Lei 8.212/91; art. 276, § 4º, do Dec. 3048/99 |
| **NMP** do RRA e seu arredondamento — três ramos | `01-dominio-e-invariantes.md` § 2.6; `04-descontos.md` § 5 | **IN RFB 1500/2014, art. 45, § único** |
| Regimes do **art. 12-A × 12-B** e tabela de IRRF | `04-descontos.md` §§ 3.3, 3.5 | Lei 7.713/88; Lei 12.350/2010 |
| **Divisores** 220/200/180/150/120 e o 240 pré-CF/88 | `03-verbas.md` § 5.6 | **Súmula 431/TST**, **IRR-849/TST**, art. 64 da CLT, CF/88 |
| **RSR e feriados**, rol e forma de remuneração | `03-verbas.md` § 5.5 | CLT art. 67; Lei 605/49; Leis 10.607/02, 6.802/80, 9.093/1994; Súmula 146/TST |
| **Arredondamento** — half-up em grandeza física, 2 casas | `01-dominio-e-invariantes.md` § 2.6 | classificado NACIONAL **pelo enunciado do bloco 16**; o corpus registra `P10 · P17` — cadeia **não declarada**, quatro práticas distintas |
| Hora centesimal; ficção da hora noturna `×1,142857`; `×4,285714` | `03-verbas.md` § 5.6 | art. 73, § 1º, da CLT; Súmula 60/TST; OJ 97 — a tensão **P8** com o `4,2857` do IRR-849 é entre **duas fontes nacionais** |
| Reconstrução do bruto antes do rateio; `R23` descarregar antes dos juros | `04-descontos.md` § 4; `04-descontos-detalhe.md` § 4.4 | regra de conta, sem veículo regional; fundamento no cap. 10 e no 16 |
| Termo inicial dos juros = ajuizamento, salvo vincendas | `02-atualizacao.md` § 2.2 | **CLT art. 883; Súmula 200/TST** |
| `aplicacao` = 1º dia do mês subsequente à prestação | `02-atualizacao.md` § 2.1, § 7 | **Súmula 381/TST** |

### 5.2 A **Tabela Única do CSJT** — **NACIONAL**, diretriz (e)

`02-atualizacao.md` § 6 é explícito: o capítulo 7 **não tem mapa período → indexador**, e o manual
diz por quê, literal na `pagina_pdf` 85 — *"A tabela mensal de correção está escalonada em meses e
anos, já computa as conversões e paridades da moeda nacional e não contém juros."* A cadeia é
**série (B), dado externo**, não regra (A). A Tabela Única **é a dependência que torna o motor
nacional**: sem ela não há correção trabalhista em nenhum TRT, não só no 3.

### 5.3 As cadeias `trab.hist.*` — **NACIONAL com nome enganoso** (achado)

**Armadilha 2, confirmada.** Os quatro JSON de `tabelas-normativas/` com prefixo `trab.hist.` têm
**conteúdo inteiramente nacional**. O prefixo é do **arquivo de origem**, não da norma:

| Arquivo | Fundamentos que o próprio JSON declara | Classificação |
|---|---|---|
| `trab.hist.correcao-monetaria.json` | Súmula 381/TST; e **delega a cadeia à Tabela Única do CSJT** | **NACIONAL** |
| `trab.hist.juros-mora.json` | CC arts. 1.062–1.063; **Lei 8.177/91, art. 39**; CLT art. 883; Súmula 200/TST | **NACIONAL** |
| `trab.hist.fazenda-publica.juros-mora.json` | mesma cadeia legal + juros da poupança a partir de 29/06/09 (**Lei 11.960/2009**) | **NACIONAL** |
| `trab.hist.moedas-e-paridades.json` | padrões monetários e paridades da **moeda nacional** — cruzeiro, cruzeiro novo etc. | **NACIONAL**, e o mais evidente de todos: paridade de moeda **não tem região** |

**Consequência de arquitetura:** o prefixo `trt3.` nesses quatro IDs **mente sobre o alcance**. Um
motor que resolva cadeia por prefixo de tribunal passará a não achar cadeia nenhuma para TRT-1,
TRT-2, TRT-15. **Recomendação (não aplicada): renomear para `trab.hist.*` ou `csjt.hist.*`**, ou
declarar `jurisdicao_alcance: "nacional"` — o campo `jurisdicao` já diz
`"justica-do-trabalho"`, sem recorte regional, o que **corrobora** a leitura nacional.

Observação correlata: os arquivos `trt3-18.*.json` (incidência de parcelas, URV, RSR, IRRF, grau de
risco) têm o mesmo vício de nome — são tabelas dos **anexos 18.x** do manual, e seu conteúdo é
IN RFB, Lei 8.212/91 e Lei 8.880/94. **Não classificados individualmente aqui**: estão fora dos 11
arquivos do consolidado. Fica registrado como escopo não coberto.

### 5.4 As três posições sobre a data da dedução — **armadilha 3, resolvida**

`05-imputacao.md` § 5 registra **três posições no mesmo manual**:

| # | Onde | Data | Fundamento | Classificação |
|---|---|---|---|---|
| 1 | **Cap. 10**, todos os exemplos | **levantamento** | **nenhum** — `Súmula` e `16.4.11` têm **zero ocorrências** no segmento (`07-leitura-do-corpus.md` § 4: *"cap. 10: zero em 69 páginas"*) | **NACIONAL** — prática aritmética sem veículo regional; é a diretriz (d) em estado puro |
| 2 | **Cap. 16, item 16.4.11** (pp. 333–334) | **duas teses**, separadas pela finalidade do depósito (código 02 na guia × cronologia) | **Súmula 15 do TRT-3** | **REGIONAL — esta é a regional.** É a única das três que se apoia em verbete de TRT |
| 3 | **Cap. 14**, p. 306, letra "c" | **pagamento**, *"salvo determinação do juízo"* | — | **NACIONAL** — sem verbete; alinha-se ao regime de precatórios e à ADC 58, item "i" |

**Qual é a regional: a 2.** As posições 1 e 3 são nacionais — e note que **coincidem em resultado
com os dois ramos da tese regional** (levantamento e pagamento), o que significa que retirar a
Súmula 15 **não apaga o critério**: apaga o **eixo de escolha** entre os dois, que é o
`natureza_do_deposito` do preset `pr.adc58-item-i` (`05-imputacao.md` § 4).

---

## 6. As DÚVIDAS

Oito. Nenhuma resolvida por inferência.

**D1 — `OJ 348` em `06-encargos.md` § 5.2.** O texto diz *"OJ 348 e TJP 4 do TRT-3"*. A frase admite
duas leituras: o "do TRT-3" governa **só a TJP 4**, ou **as duas**.
**O que falta:** `jurisprudencia-indice.md` § 17.6 lista **apenas três** OJs de Turmas do TRT-3 —
**4, 23 e 29**. Não há OJ 348 regional catalogada, o que **inclina** para OJ 348 da **SDI-1 do TST**
(nacional). **Inclinação não é classificação.** Resolver lendo o `pagina_pdf` 106 do manual.

**D2 — os verbetes de `P13`** (`03-verbas.md` § 10): *"Súmulas 24, 102, 109, 118, 199 e 370, OJ
235"*. A **Súmula 24 é do TRT-3** (confirmado em `04-descontos.md` § 2.1). As outras **não têm
tribunal declarado no consolidado**, e o índice tem numeração colidente entre 17.1 (TST) e 17.5
(TRT-3). **O que falta:** conferir cada número contra a seção do capítulo 17 de origem.

**D3 — `Súmula 38 do TRT-3`** (`03-verbas.md` § 5.6, divisor 180 no turno de revezamento). O
`jurisprudencia-indice.md` § 17.5 traz **15 súmulas do TRT-3** e lista os números **2, 5, 10, 11,
15, 23, 24, 25, 27, 28, 29, 39, 45, 46, 50** — **a 38 não está lá**. Ou é súmula regional não
catalogada no cap. 17, ou é erro de número no consolidado, ou é verbete de outro tribunal.
**O que falta:** conferir a p. 37/48 do manual. Enquanto isso, R9 vale com segurança **só para a
Súmula 2**.

**D4 — `FGTS a depositar` na base dos honorários** (`06-encargos.md` § 5.2). O corpus a chama de
*"regra do TRT-3 de 2016"*, **sem citar verbete**. Se for prática do manual, é NACIONAL por (d); se
houver súmula ou TJP por trás, é REGIONAL. **O que falta:** o veículo. O próprio corpus registra a
pendência `P8-F4-03` em `extracao/trabalhista/bloco-13a-descontos-proporcionais-detalhe.md`.

**D5 — `SEE/TRT-4`** (`03-verbas.md` § 5.10). SEE é órgão fracionário — Seção Especializada em
Execução. Se a posição estiver em **súmula ou tese prevalecente** do TRT-4, é REGIONAL plena (R14);
se for jurisprudência de seção **sem verbete editado**, não entra na regra do art. 896, § 6º.
**O que falta:** o veículo da posição.

**D6 — vigência da Súmula 46 do TRT-3** (`03-verbas.md` § 10; `02-base-normativa-verbas.md` linha
126). **A classificação como REGIONAL é firme; a vigência é a dúvida.** A base manda conferir a
vigência após a **cassação da Súmula 228/TST de 2018**. `jurisprudencia-indice.md` marca o verbete
como **`não coberto`** — e a regra dura do índice é explícita: *"verbete não coberto pela base fica
`não coberto`, **nunca** `vigente` por omissão"*. **O que falta:** consulta ao portal do TRT-3.

**D7 — os Provimentos do TRT-3** (`jurisprudencia-indice.md` § 17.8: **01/93, 03/91, 04/00** e o
**Provimento Conjunto GCR/GVCR n. 3, de 15/12/2015**). **Zero ocorrências de `Provimento` no
consolidado** — a única ocorrência é o **Provimento 207/2025 do CNJ**, nacional
(`02-atualizacao-detalhe.md` § 5.5). Os quatro são regionais e **procedimentais**, não de cálculo —
mas o Prov. 04/00 disciplina **memória e resumo** do cálculo, e o Prov. Conjunto remete
**expressamente ao Manual**. **O que falta:** decidir se o motor deve emitir memória/resumo e, em
caso positivo, se o faz por regra nacional ou regional.

**D8 — a `IN 001/02` como REGIONAL (R11).** Classificada REGIONAL porque o próprio corpus a chama
de *"IN regional"* (`06-encargos.md` § 2.1) — mas ela **não é súmula nem tese do art. 896, § 6º**;
é ato administrativo de corregedoria. **A tipologia do enunciado não tem casa para ela.**
**O que falta:** uma terceira etiqueta — sugestão, `REGIONAL-ADMINISTRATIVO` — ou a decisão de que
valores de custas são parâmetro de configuração, não regra. Mesmo problema atinge **R10** (tabela
CGJ/TJMG) e **R15** (tabela própria do TRT-3).

### 6.1 A bifurcação temporal do R10 — **não é resíduo**

Armadilha 1, confirmada e com o corpus falando por si (`02-atualizacao.md` § 4):

| Período | Correção cível | Juros |
|---|---|---|
| **até dez/2002** | **Tabela CGJ/TJMG (em MG)** — REGIONAL | 0,5% simples (CC/1916, arts. 1.062–1.064) — NACIONAL |
| jan/2003 a 29/08/2024 | **SELIC** (engloba ambos) — NACIONAL | — |
| a partir de 30/08/2024 | **IPCA** (CC art. 389, § único) — NACIONAL | **taxa legal** (CC art. 406, § 1º) — NACIONAL |

O que a substitui é o **STJ, Tema 1368**, **vinculante**, que *"substitui a prática anterior do
TJMG (tabela CGJ + 1% a.m.) para o período pré-Lei 14.905"*. **Mas a tabela sobrevive em três
hipóteses**, literais no § 4: períodos anteriores a 2003; processos cujo **título** fixou
expressamente aquele critério; processos com **trânsito em julgado** sob o regime anterior — por
**R8: título > escolha > default** (`01-dominio-e-invariantes.md` § 3). **É bifurcação temporal
com ressalva de título, não resíduo a descartar.**

---

## 7. A chave de resolução `(regra, tribunal, competência)`

### 7.1 Como se compõe

- **`regra`** — o identificador do ponto de cálculo, **não do verbete**. Ex.: `divisor.12x36`,
  `insalubridade.base`, `deducao.data`, `inss.fato-gerador`, `honorarios.base`,
  `terceiros.competencia`, `custas-execucao.tabela`. A chave existe para que **o mesmo ponto** possa
  ter resposta diferente por região.
- **`tribunal`** — o TRT ou TJ da causa. Só entra na chave para as regras que têm variante regional
  cadastrada; para as demais é **ignorado**, não *"nacional"* como valor.
- **`competência`** — a **data do fato gerador da parcela**, no mesmo sentido em que
  `00-calendario-de-cortes.md` § 2.1 a usa nos 16 pontos do corte `2017-11-11`. É o **terceiro**
  eixo porque verbete regional **nasce e morre com data** — a Súmula 39/TRT-3 foi cancelada pela
  RA 123/2025 **com perda de eficácia retroagida a 11/11/2017** (`03-verbas.md` § 2), e
  `03-verbas.md` § 6.1 já fixa a doutrina: **os cancelamentos são cadeia temporal**, não um
  interruptor. `07-leitura-do-corpus.md` § 3 diz o mesmo em uma frase: *"'Cancelada' quase nunca
  significa 'nunca valeu'"*.

### 7.2 O que acontece quando o tribunal não tem súmula cadastrada

**Cai no fallback nacional da coluna 6 da tabela da § 4 — e isso é resolução, não erro.** Três
consequências, e uma vedação:

1. **A resolução é total, nunca parcial.** Para cada uma das quinze regras regionais existe
   fallback nacional identificado — exceto **R15** (tabela própria do TRT-3 até out/2005), onde o
   corpus **não tem** fonte nacional para o período e a lacuna está registrada como **`P9-02`**
   (`02-atualizacao.md` § 6). **Esta é a única regra da lista que não resolve por fallback**, e
   permanece pendência aberta.
2. **O default não é a regra do TRT-3.** Hoje o motor herdaria do manual mineiro por ser a fonte
   extraída. Depois da correção de premissa, **o default é a norma nacional** e o TRT-3 é **uma**
   entrada da tabela regional, ao lado de TRT-4 (R14) e TJMG (R10).
3. **Silêncio do tribunal não é adesão ao verbete de outro tribunal.** Se o TRT-9 não tem súmula
   sobre divisor na 12×36, aplica-se **IRR-849/Súmula 431**, **não** a OJ 23 do TRT-3 — *"as três
   mudam resultado e não valem fora de Minas"*. Espelha a regra dura do
   `jurisprudencia-indice.md` § 1: **ausência de notícia não é notícia de vigência**.
4. **Vedação:** a chave **não harmoniza divergência**. Onde há duas correntes com fundamento
   próprio e nenhuma arbitrada — V-05, V-06, V-07, V-09 (`03-verbas.md` § 9), `F7-03`
   (`04-descontos.md` § 3.2), a divergência de base dos honorários (`06-encargos.md` § 5.2) —, a
   chave **seleciona o eixo, não o resultado**. Resolver seria inferir, e `03-verbas.md` § 11 veda:
   *"Não resolve pendência aberta por inferência."*

### 7.3 Ordem de precedência, contra `R8`

`01-dominio-e-invariantes.md` § 3 já dá a precedência do motor — **título > escolha > default**. A
chave regional entra **dentro do default**, nunca acima do título: comando exequendo que fixe
divisor 220 na 12×36 **afasta a OJ 23** mesmo em Minas, por **art. 879, § 1º, da CLT**
(`03-verbas.md` § 5.6, *"precedência expressa do comando exequendo"*).

---

## 8. O que esta classificação **não** faz

**Não altera os 11 arquivos do consolidado** — a aplicação é decisão posterior. **Não resolve
pendência aberta**: `P9-02`, `P9-04`, `P8`, `P13`, `P8-F4-03` e a vigência da Súmula 46 seguem
abertas. **Não renomeia** os JSON `trab.hist.*` — só registra o achado da § 5.3. **Não classifica**
os arquivos fora do consolidado: `tabelas-normativas/trt3-18.*.json`, `jurisprudencia-indice.md`
(158 verbetes) e os relatórios de `extracao/` foram **lidos para conferência**, não classificados
item a item. **Não confirma** a premissa da § 1 — ela é externa e assim está declarada.
