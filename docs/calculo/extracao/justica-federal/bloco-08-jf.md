# Bloco 8 — Manual de Cálculos da Justiça Federal

**Espinha.** `manual_de_calculos_2026.pdf`, **Resolução CJF n. 990/2026**, 93 páginas,
integral. 177.361 caracteres.

**Paginação.** A página 1 do PDF é folha em branco; a página 2 traz o rótulo impresso "1".
Logo **`pagina_pdf = numero_impresso + 1`**. Toda proveniência aqui grava `pagina_pdf`.

> Esta é a **única fonte do corpus cuja edição está vigente**. Não há marcas de Fase 4 neste
> bloco — não há nada a confrontar com norma posterior.

| Onde está o quê | |
|---|---|
| **(A) Cadeias** — o núcleo | `../../tabelas-normativas/cjf.*.json` — 7 cadeias, 78 segmentos |
| **(C) Procedimento** | este arquivo |
| Detalhe, notas, defeitos | [`bloco-08-jf-detalhe.md`](bloco-08-jf-detalhe.md) |
| Relatório, cruzamentos, R1/R2 | [`bloco-08-relatorio.md`](bloco-08-relatorio.md) |

---

## 1. A regra que governa o manual inteiro

`pagina_pdf: 41`, item 4.1, literal:

> "A decisão judicial é o balizador do cálculo e **prevalece sobre as orientações deste manual**
> se houver divergência."

É a invariante **R8** do projeto, escrita pela própria fonte. E vem com duas ressalvas que a
limitam, item 4.1.2, `pagina_pdf: 41`:

> "**NOTA 1**: Incide correção monetária ainda que a petição inicial ou a sentença sejam omissas."
>
> "**NOTA 2**: Os cálculos de liquidação observarão o disposto no respectivo título judicial,
> **salvo quanto ao indexador de correção monetária no caso de mudança superveniente da
> legislação**."
>
> "**NOTA 3**: Efetuando-se mera atualização do cálculo original, já aceito pelas partes ou
> definido judicialmente, deve-se ser observada a mesma metodologia do cálculo anterior,
> ressalvado o contido na Nota 2."

**R-08-01 — o título vence, menos contra lei superveniente.** A NOTA 2 abre a única exceção:
mudança de legislação sobre o indexador passa por cima do título. O mesmo se repete para juros
em 4.1.3, NOTA 2 (`pagina_pdf: 43`), com fundamento próprio — "REsp n. 1.112.746, Tema 176/STJ".

**R-08-02 — atualizar não é recalcular.** A NOTA 3 fixa que a mera atualização preserva a
metodologia do cálculo original. É a mesma disciplina que o manual do TRT-3 adota no item 9.2.7.3.

---

## 2. Índices nominais e percentuais — o item que sustenta a R3

**Item 4.1.2.4**, `pagina_pdf: 42`. Literal e integral:

> "Indexadores serão determinados segundo cada tipo de liquidação. Para garantir um correto
> encadeamento de indexadores, importa esclarecer a diferença entre índices nominais e
> percentuais:
>
> a) **Nominais**: fixados em valores nominais na moeda corrente da época. Ex.: Ufir, BTN, OTN,
> ORTN. **Refletem a inflação do mês (ou dia) anterior** à data do valor divulgado.
>
> b) **Percentuais (ou reais)**: fixados em valores percentuais. Ex.: INPC, IGP-DI, IGP-M.
> **Refletem a inflação do próprio mês de competência** e terão aplicação prática no mês (ou dia)
> seguinte à data da divulgação."

**R-08-03 — trocar entre tipos sem ajustar a defasagem desloca o cálculo em um mês.** É a
invariante R3 do projeto, e este é o texto que a sustenta.

O manual usa essa regra para **justificar uma sobreposição aparente**. Item 2.3.1.3,
`pagina_pdf: 25`, literal:

> "O mês de janeiro de 1989 marca o termo final da OTN e o início da BTN. Entretanto, **por serem
> indexadores nominais, este fato não implica duplicidade de correção monetária**, pois a OTN de
> janeiro serve para definir a inflação de dez./1988, e a BTN de janeiro, comparada com a de
> fevereiro, para fixar a inflação de jan./1989."

**R-08-04 — em cadeia de índices nominais, fim e início no mesmo mês não é dupla contagem.**
Sem esta regra, quatro das sete cadeias extraídas pareceriam violar R1 em jan./1989. Ver
relatório § 5.

E a regra de continuidade, item 2.3.1.3, `pagina_pdf: 25`:

> "O mês da mudança do indexador deve ser considerado, sob pena de **solução de continuidade**."

É R2 dita pela fonte.

---

## 3. Expurgos, deflação e salário mínimo

**Item 4.1.2.1 — expurgos**, `pagina_pdf: 42`, literal:

> "Devem-se considerar, também, os expurgos inflacionários, IPC/IBGE integrais (**descontando o
> BTN ou outro índice utilizado, evitando bis in idem**), já consolidados pela jurisprudência,
> salvo decisão judicial em contrário, nos seguintes períodos: **jan./1989 = 42,72%; fev./1989 =
> 10,14%; mar./1990 a fev./1991 = IPC/IBGE em todo o período.**"

**R-08-05 — o expurgo SUBSTITUI, não soma.** O parêntese "descontando o BTN ou outro índice
utilizado" é a chave, e o único lugar do manual onde a operação é declarada. Nas tabelas do
capítulo 4 a coluna de observações diz apenas "Expurgo, em substituição ao BTN" — coerente.

> **Mas no FGTS a regra não se repete**, e isso é achado. Ver detalhe § 5.

**Item 4.1.2.2 — deflação**, `pagina_pdf: 42`, literal:

> "os índices negativos de correção monetária (deflação) **serão considerados** no cálculo de
> atualização. Contudo, se, no resultado do cálculo, a atualização implicar redução do principal,
> **considerada cada parcela do principal**, deve prevalecer o valor nominal."

**R-08-06 — o piso nominal é POR PARCELA.** É a invariante R5 do projeto, e a qualificação
"considerada cada parcela do principal" é o que a torna operacional: o piso não se afere no
total. Fundamento citado: "REsp. n. 1.265.580".

**Item 4.1.2.3 — salário mínimo**, `pagina_pdf: 42`: condenação em múltiplos do salário mínimo
converte-se "para a moeda corrente na data da parcela devida definida pela decisão judicial",
porque "o inciso IV do art. 7º da Constituição Federal veda o uso do salário mínimo como
indexador de correção monetária".

**R-08-07 — o salário mínimo é unidade de conversão, nunca indexador.** A fórmula se repete
cinco vezes no manual (`pagina_pdf: 42, 45, 46, 47`) — para honorários, custas, multas e
indenizações processuais. Muda a data da conversão, não o princípio:

| Onde | Data de conversão | `pagina_pdf` |
|---|---|---|
| Condenação | data da parcela devida | 42 |
| Honorários fixados em múltiplos | sentença líquida, ou decisão de liquidação | 45 |
| Honorários periciais / tradução | data da decisão judicial | 46 |
| Multas e indenizações processuais | data da decisão que as arbitrou | 46, 47 |

---

## 4. As cadeias — o núcleo do bloco

Sete cadeias extraídas para `tabelas-normativas/`, no schema `cadeia-temporal`.

| Cadeia | Item | `pagina_pdf` | Segmentos |
|---|---|---|---|
| `cjf.condenatorias-gerais.correcao-monetaria` | 4.2.1.1 | 48 | 15 |
| `cjf.condenatorias-gerais.juros-mora` | 4.2.2 | 54 | 11 |
| `cjf.previdenciario.correcao-monetaria` | 4.3.1.1 | 57 | 15 |
| `cjf.repeticao-indebito.correcao-monetaria` | 4.4.1.1 | 63 | 10 |
| `cjf.desapropriacao-direta.correcao-monetaria` | 4.5.1.1 | 66 | 11 |
| `cjf.trabalhista.juros-mora` | 4.7.2 | 78 | 11 |
| `cjf.divida-fiscal.correcao-monetaria` | 2.3.1.2 | 23 | 5 |

### 4.1 O tronco comum

Quatro cadeias de correção — condenatórias, previdenciário, repetição e desapropriação —
compartilham **o mesmo tronco de 1964 a fev./1991**, palavra por palavra:

| Período | Indexador | Observação do manual |
|---|---|---|
| De 1964 a fev./1986 | ORTN | — |
| De mar./1986 a jan./1989 | OTN | "Os débitos anteriores a jan./1989 deverão ser multiplicados, neste mês, por **6,17**." |
| Jan./1989 | IPC/IBGE de **42,72%** | "Expurgo, em substituição ao BTN." |
| Fev./1989 | IPC/IBGE de **10,14%** | "Expurgo, em substituição ao BTN." |
| De mar./1989 a mar./1990 | BTN | — |
| De mar./1990 a fev./1991 | IPC/IBGE | "Expurgo, em substituição ao BTN e ao INPC de fev./1991." |

Depois de fev./1991 elas divergem — e a **desapropriação** diverge com um índice que nenhuma
outra cadeia usa: **IPC/FGV**, de mar./1991 a dez./1991 (`pagina_pdf: 66`, e a gêmea 4.6.1.1 na
`73`). É o único índice exclusivo de uma cadeia em todo o capítulo 4, e a primeira extração o
gravou como INPC — erro corrigido pela validação adversarial.

**A dívida fiscal (cap. 2) NÃO tem esse tronco** — ver relatório § 4.

### 4.3 O capítulo 3 — uma regra só

**Capítulo 3**, `pagina_pdf: 40`, integral. Alcança "Títulos de crédito, contratos bancários,
contratos cíveis e outros, envolvendo a Caixa Econômica Federal, ECT, Conab etc." A regra,
literal:

> "Os cálculos serão realizados **na forma prevista no respectivo título extrajudicial**, com as
> eventuais alterações determinadas pelo juízo."

**R-08-26 — nas dívidas diversas não há cadeia: há o título.** É a precedência da R-08-01 levada
ao limite — aqui o título extrajudicial não apenas prevalece sobre o manual, ele **é** o critério.
O capítulo não tem tabela, indexador nem juros próprios.

### 4.2 Onde cada cadeia bifurca por qualidade do devedor

| Cadeia | Bifurca em | Reconverge em |
|---|---|---|
| Condenatórias — correção | **dez./2021** | **set./2025** (IPCA-15 para os dois) |
| Condenatórias — juros | **jul./2009** | **set./2025** (taxa legal para os dois) |
| Previdenciário — correção | **nunca** | — |
| Repetição de indébito | **nunca** | — |
| Desapropriação direta | **nunca** | — |
| Trabalhista — juros | **ago./2001** | **nunca** (o ramo privado segue em 1,0%) |

**R-08-08 — a bifurcação por devedor não é universal.** Três das cadeias nunca bifurcam: o
benefício previdenciário, a repetição de indébito e a desapropriação seguem um caminho só.

---

## 5. A defasagem — o campo `aplicacao`

O enunciado chamou isso de "fonte silenciosa de divergência". O manual tem **quatro fórmulas
distintas**, e a escolha entre elas depende do devedor e do período.

| # | Fórmula literal | Onde | `pagina_pdf` |
|---|---|---|---|
| **D1** | "a taxa Selic deve ser aplicada **no mês posterior ao de sua competência, inclusive para o mês de pagamento**. Ex.: a Selic de dez./2021 será computada em jan./2022" | Fazenda Pública, a partir de dez./2021 | 50, 55, 59, **67**, **73**, 79 |
| **D2** | "a taxa Selic deve ser aplicada **a partir do mês seguinte ao da citação** ou de outro termo inicial dos juros de mora **até o mês anterior ao pagamento, e 1% no mês do pagamento**" | não-Fazenda; e Fazenda de jan./2003 a jun./2009 | 50, 55 |
| **D3** | "deve ser aplicada **a partir do mês seguinte ao recolhimento indevido até o mês anterior à repetição, e 1% no mês da repetição**" | repetição de indébito | 63, 65 |
| **D4** | "devem ser aplicadas **a partir do mês seguinte ao da competência da parcela devida** até o mês anterior ao pagamento, e 1% no mês do pagamento" | dívida fiscal | 25, 27 |

**R-08-09 — D1 e D2 dão resultados diferentes sobre a mesma série.** D1 desloca a série um mês
e **inclui** o mês de pagamento; D2 ancora no termo inicial dos juros, **exclui** o mês de
pagamento e o substitui por 1% fixo. A mesma Selic, dois números.

**R-08-10 — D3 tem eixo próprio.** Não é competência nem citação: é a **data do recolhimento
indevido**, com exceção declarada para rendimentos sujeitos a ajuste anual, quando "fluem a
partir da data final prevista para a entrega da aludida declaração e não a partir da retenção na
fonte (antecipação)" (`pagina_pdf: 63`).

**R-08-11 — a taxa legal segue D1.** Item 4.2.2, NOTA 7, `pagina_pdf: 56`: "A taxa legal deverá
ser aplicada **no mês posterior ao de sua competência**, de acordo com a metodologia divulgada
pelo Banco Central do Brasil, por meio da ferramenta 'Calculadora do Cidadão'."

### O termo inicial da correção também varia

| Tipo de ação | Termo inicial | `pagina_pdf` |
|---|---|---|
| Condenatória — ato ilícito | data do efetivo prejuízo (Súmula 43/STJ) | 49 |
| Condenatória — dano moral | o arbitramento (Súmula 362/STJ) | 49 |
| Servidores e empregados públicos | **o mês da competência, e não o mês de pagamento** | 49 |
| Benefício previdenciário | **o mês de competência, e não o mês de pagamento** | 59 |
| Desapropriação | **a data do laudo do perito** (Súmula 75/TFR) | 66 |
| Trabalhista | **o mês de competência, e não o mês de pagamento** | 77 |

---

## 6. A consolidação de dezembro de 2021

Prioridade do enunciado. A EC 113/2021 fecha um regime e abre outro, e **o valor de fechamento
muda por ramo**.

O procedimento se repete em **cinco** lugares, com redação quase idêntica. Literal
(`pagina_pdf: 50`):

> "a) o crédito será consolidado tendo por base o mês de dez./2021 pelos critérios de juros e
> correção monetária até então aplicáveis, considerando, para esse fim, **o [índice] de nov./2021
> ([x]%) e os juros de dez./2021 (0,4412%)**;
>
> b) sobre o valor consolidado do crédito em dez./2021, **sem exclusão de qualquer parcela**,
> incidirá a taxa Selic a partir de jan./2022 (competência dez./2021) (§ 1º do art. 22 da
> Resolução CNJ n. 303/2019, com redação dada pelo art. 6º da Resolução CNJ n. 448/2022);
>
> c) o valor resultante da aplicação da Selic sobre o valor consolidado do crédito até dez./2021,
> denominado 'Juros Selic', deve ser **integralmente somado à parcela denominada 'Juros até
> 12/2021'**, para apuração do montante final da condenação."

**O que muda é o índice de nov./2021:**

| Ramo | Índice de nov./2021 | Valor | Juros de dez./2021 | Item | `pagina_pdf` |
|---|---|---|---|---|---|
| Condenatórias em geral | **IPCA-E** | **1,17%** | 0,4412% | 4.2.1, NOTA 5 | **50** |
| Benefícios previdenciários | **INPC** | **0,84%** | 0,4412% | 4.3.1, NOTA 5 | 59 |
| **Desapropriação direta** | **IPCA-E** | **1,17%** | 0,4412% | 4.5.1.1, NOTA 2 | **67** |
| **Desapropriação indireta** | **IPCA-E** | **1,17%** | 0,4412% | 4.6.1.1, NOTA 2 | **74** |
| Ações trabalhistas | **TR** | **0,00%** | 0,4412% | 4.7.2, NOTA 2 | 79 |
| Repetição de indébito | — | **não se consolida** | — | 4.4.1.1, NOTA 4 | 64 |

**R-08-12 — três valores de fechamento, cinco lugares, e uma dispensa.** Os juros de dez./2021
são os mesmos (0,4412%) nos cinco ramos que consolidam; o índice de correção assume **três**
valores. A TR trabalhista de **0,00%** significa que, nesse ramo, o principal não se move em
nov./2021.

> **Correção.** A primeira redação listava quatro lugares e três ramos. São **cinco** — as duas
> desapropriações também consolidam, com IPCA-E de 1,17%, e ficaram de fora. Verificado por
> varredura: `0,4412` ocorre nas páginas **50, 59, 67, 74 e 79**. E a redação **não é idêntica**:
> a p.50 diz "tendo por base o mês de dez./2021"; a p.67, "com base no mês de dez./2021".

**R-08-13 — a repetição de indébito não consolida.** Literal, `pagina_pdf: 64`: "A superveniência
da EC n. 113/2021 **não altera o cálculo** nas repetições de indébito tributário, o qual já
observa a atualização pela Selic desde jan./1996, sendo, portanto, **desnecessário consolidar** o
crédito em relação ao período anterior a dez./2021."

**R-08-14 — "sem exclusão de qualquer parcela".** A Selic incide sobre o consolidado inteiro,
principal **e** juros. Nos exemplos do manual (`pagina_pdf: 51`) há duas linhas de dez./2021: uma
para o principal corrigido (R$ 2.275,96) e outra para os juros (R$ 55,75), ambas recebendo 5,05%
de Selic.

---

## 7. Capítulo 5 — requisições

**Item 5.2**, `pagina_pdf: 88`. Requisição complementar é a diferença entre o cálculo e a
extinção do débito. Quatro hipóteses, literais:

- **juros** "no período entre a data do cálculo e a data de apresentação do precatório (**1º de
  julho, até 2021, e 2 de abril, a partir de 2022**) ou da RPV"; e "no período posterior ao prazo
  constitucional e/ou legal de pagamento";
- **correção monetária** "quando o indexador adotado judicialmente for maior do que o utilizado
  administrativamente pelo Tribunal"; e no período posterior ao prazo.

**R-08-15 — a data de apresentação do precatório mudou em 2022.** De 1º de julho para 2 de
abril. É um eixo de corte, e o manual o escreve entre parênteses.

**R-08-16 — os juros SUSPENDEM no prazo constitucional.** NOTA 1, `pagina_pdf: 89`, literal:

> "Suspendem-se os juros moratórios no prazo constitucional de pagamento dos precatórios de 1º de
> julho, até 2021, e de 2 de abril, a partir de 2022, **até o final do exercício seguinte**
> (Súmula Vinculante n. 17 e Tema 1.037, ambos do STF), **inclusive nas desapropriações**."

E NOTA 2: o mesmo vale para RPV, com prazo de "**60 dias a partir da data de apresentação**".

**R-08-17 — o indexador troca três vezes dentro de uma requisição complementar.** NOTA 4,
`pagina_pdf: 89`, literal:

> "a) o indexador utilizado na conta originária **até a data da apresentação** da requisição;
> b) **no período constitucional** e/ou legal de pagamento da requisição: - O IPCA-E/IBGE nos
> precatórios das propostas orçamentárias de 2001 a 2010; - A partir de 2011, aplicar o indexador
> de atualização indicado na Resolução do CJF [...]
> c) **novamente o indexador da conta originária após este período** (final do exercício seguinte,
> no caso de precatório, e 60 dias, no caso de RPV)."

Original → administrativo → original. É uma cadeia de três trechos governada pelo **estado da
requisição**, não pela competência.

**R-08-18 — o art. 354 do CC não se aplica ao precatório complementar.** NOTA 5,
`pagina_pdf: 89`, literal: "não deve ser aplicado o art. 354 do Código Civil [...] pois **segue
legislação própria**." Contrasta com o item 4.1.8 (`pagina_pdf: 47`), que manda aplicar o art.
354 ao "pagamento parcial de crédito **não sujeito a requisição**". As duas regras convivem
porque os universos são disjuntos — e o manual diz qual é qual.

**R-08-19 — na desapropriação não cabem juros compensatórios em precatório complementar.**
NOTA 7, `pagina_pdf: 90`: "pois, conforme jurisprudência do STJ, a compensação pela perda da posse
se resolve com a consolidação do montante devido ao expropriado". Mas "devem ser incluídos os
juros vencidos antes da apresentação da requisição, e não computados no montante requisitado".

**Item 5.3 — requisição suplementar**, `pagina_pdf: 93`. Duas hipóteses: valor que "deixou de
constar da requisição originária porque sobre ele ainda pendia controvérsia" e "erro material na
conta [...] reconhecido judicialmente". E uma regra de método:

> "Parcela residual ou faltante **não facilmente destacável**. Ex.: Tema 810 do STF, tendo a
> requisição parcial utilizado a TR como correção monetária, que deve ser substituída pelo INPC ou
> IPCA-E: **deve-se efetuar novamente a conta originária, com a mesma data-base e com os novos
> critérios definidos**, apurando-se as diferenças de principal e de juros."

**R-08-20 — refazer a conta inteira, não emendar.** Quando o critério muda, a requisição
suplementar se apura por refazimento com a mesma data-base, e **"vedada a incidência de juros
sobre juros"**.

---

## 8. A EC 136/2025 — ela é a razão desta edição

**Ela não aparece em nenhum dos cinco capítulos.** Mas está na **apresentação** e na própria
**resolução**, e é a causa declarada da edição inteira.

Apresentação, `pagina_pdf: 11`, literal:

> "a Comissão Permanente de Revisão e Atualização [...] apresentou, por meio da Nota Técnica n.
> 1/2026, propostas de alterações [...] considerando a necessidade de **colmatar a lacuna
> normativa instaurada — quanto à fase pré-expedição dos requisitórios — pela Emenda
> Constitucional n. 136/2025**"

E a primeira das quatro alterações desta versão, `pagina_pdf: 11–12`, literal:

> "1) **Encerramento da incidência da taxa SELIC** (prevista no art. 3º da Emenda Constitucional
> n. 113/2021) **quanto à fase pré-requisitório, a partir de setembro de 2025**, em razão da
> Emenda Constitucional n. 136/2025 e conforme decidido pelo Supremo Tribunal Federal no ARE
> 1.557.312/SP (Tema 1.419), com a consequente aplicação dos critérios do Código Civil, na redação
> dada pela Lei n. 14.905/2024: **correção monetária pelo IPCA/IBGE** (art. 389, parágrafo único) e
> **juros de mora pela taxa legal — SELIC com dedução do IPCA** (art. 406 e Resolução CMN n.
> 5.171/2024)."

**R-08-23 — o corte de set./2025 que aparece em TODAS as cadeias é a EC 136/2025.** Nenhuma
tabela do corpo a nomeia; todas citam o ARE 1.557.312/SP (Tema 1.419) e a Lei 14.905/2024. A
emenda está a um grau de distância em cada linha.

**R-08-24 — o alcance é a FASE PRÉ-REQUISITÓRIO, não a requisição.** É por isso que o capítulo 5
não muda: o único bullet de emendas do item 5.1 (que arrola sete fundamentos) continua sendo as "Emendas Constitucionais n. 113/2021 e 114/2021"
(`pagina_pdf: 88`). A EC 136/2025 encerra a Selic **antes** da expedição do requisitório; o que
acontece **depois** dela segue o regime de precatório e RPV, inalterado nesta edição.

**R-08-25 — o previdenciário foi expressamente preservado.** Alteração 2, `pagina_pdf: 12`,
literal: "**Manutenção**, para os benefícios previdenciários, dos índices próprios da legislação
de regência: correção monetária pelo INPC/IBGE e **juros de mora pela taxa legal apurada com a
dedução do INPC**, a partir de setembro de 2025."

Duas taxas legais distintas convivem a partir de set./2025:

| Ramo | Taxa legal | set./2025 | `pagina_pdf` |
|---|---|---|---|
| Condenatórias, trabalhista, desapropriações | SELIC − **IPCA-15** | **1,305984%** | 55, **68**, **75**, 79 |
| Benefícios previdenciários | SELIC − **INPC** | **1,377047%** | 61 |

O manual traz a tabela de cálculo da taxa legal previdenciária mês a mês, de set./2025 a
jun./2026, com fator Selic e fator INPC por competência (`pagina_pdf: 61`, fonte "Bacen (SGS —
Sistema Gerenciador de Séries Temporais)").

> **Correção da primeira redação deste arquivo.** Eu havia escrito que "o manual não menciona a
> EC 136/2025" e que a varredura não a encontrava. **Estava errado**: `136/2025` ocorre três vezes
> — duas na apresentação (`pagina_pdf: 11`) e uma na resolução (`pagina_pdf: 13`). O erro foi meu,
> não da extração: busquei por `EC 136`, forma que o manual não usa. Ver relatório § 7.

---

## 9. Honorários — quatro regimes por forma de fixação

Item 4.1.4, `pagina_pdf: 43–45`. O marco temporal é declarado: "A **data da sentença** (ou do ato
jurisdicional equivalente, na competência originária dos tribunais) [...] deve ser considerada o
marco temporal para a aplicação das regras fixadas pelo CPC/2015 (EAREsp n. 1.255.986)".

| Fixação | Base de atualização | Termo inicial dos juros | `pagina_pdf` |
|---|---|---|---|
| Sobre o **valor da causa** | desde o ajuizamento (Súmula 14/STJ) | **trânsito em julgado** | 43 |
| Sobre a **condenação** ou proveito | valor atualizado da condenação | (não declarado neste item) | 44 |
| Em **valor certo** | desde a decisão que arbitrou | **trânsito em julgado** (art. 85, § 16, CPC) | 45 |
| Em **múltiplos do salário mínimo** | conversão + índices de 4.2.1 | **citação na execução**, ou fim do prazo do art. 523 | 45 |

**R-08-21 — três termos iniciais de juros para honorários, conforme a forma de fixação.** E as
faixas do art. 85, § 3º, do CPC são progressivas: "o cálculo de honorários deve observar o
percentual da faixa inicial e, naquilo que a exceder, o percentual da faixa subsequente, e assim
sucessivamente (art. 85, § 5º, CPC)" (`pagina_pdf: 44`).

**R-08-22 — a multa de 10% do art. 523, § 1º, não entra na base dos honorários.** Item 4.1.4.6,
`pagina_pdf: 45`, com fundamento em "REsp n. 1.757.033".

---

## 10. Ver também

- [`bloco-08-jf-detalhe.md`](bloco-08-jf-detalhe.md) — cadeias linha a linha, notas × linhas, os
  defeitos do original
- [`bloco-08-relatorio.md`](bloco-08-relatorio.md) — cruzamentos, R1/R2, fixtures, pendências
- `../../tabelas-normativas/cjf.*.json` — as sete cadeias
- `scripts/calculo/valida_cadeias.py` — o CLI de R1 e R2 sobre elas (renomeado no bloco 9,
  quando a lógica de tronco-e-ramo passou para `valida_cobertura.py`)
