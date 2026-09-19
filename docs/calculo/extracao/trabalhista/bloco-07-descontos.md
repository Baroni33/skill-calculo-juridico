# Bloco 7 — descontos legais: previdenciário e fiscal

**Espinha.** Capítulo 9 do Manual de Cálculos do TRT-3 (2016), **páginas 107 a 208** do PDF
(offset de paginação 0; número impresso == `pagina_pdf`).

O maior bloco do manual: 351.605 caracteres, 102 páginas, 47 itens numerados. Aqui está a
**regra**. Exemplos, roteiros longos, hipóteses de atualização e os defeitos do original estão
em [`bloco-07-descontos-detalhe.md`](bloco-07-descontos-detalhe.md).

> **Bifurcação.** Este arquivo é a parte **(A) CONCEITO** — muda quando muda a lei ou a
> jurisprudência. A parte **(B) FAIXA** está em `serie-*.csv`, marcada `OUT_OF_SCOPE`.
> O corte foi aplicado com o critério do enunciado, e ele produziu um resultado que merece
> registro: **quase tudo no capítulo 9 é (A)**. Ver § 12.

---

## 1. Os dois descontos, e a ordem entre eles

**Item 9.1**, `pagina_pdf: 107`. Cinco regras, todas literais:

> "Devem ser deduzidos do crédito do reclamante, na forma da Lei 8.212/91, Dec. 3048/99 Lei
> 10.833/03, Lei 8541/92 e Dec. 3000/99, ainda que o comando sentencial seja omisso,
> conforme Súmula 401/TST."

> "O desconto previdenciário precede sempre ao desconto do IR."

> "As bases de cálculo dos descontos previdenciários e fiscais são diferentes."

> "O empregador deve recolher as duas cotas previdenciárias (cota parte autor e réu), bem
> como o valor do imposto de renda. Embora o reclamado seja responsável pelo recolhimento,
> os valores de INSS e imposto de renda devem ser deduzidos do crédito do reclamante,
> conforme OJ SDI-1 nº 363/TST, **exceto se for acordado que o valor devido é líquido**. Nesta
> hipótese, a reclamada assume o ônus do recolhimento."

> "A cota do desconto previdenciário do reclamado é de 20% (empregadores em geral) ou 22,5%
> (somente p/ Bancos e instituições Financeiras) e 8% (empregador doméstico a partir da
> competência out/15) sobre as verbas salariais acrescido do risco ambiental do trabalho (RAT
> ou antigo SAT). **É calculada com base no crédito trabalhista, mas dele não é dedutível e não
> tem teto máximo**, incidindo sobre o total das parcelas passíveis de incidência"

**R-07-01 — ordem de aplicação.** INSS antes de IR, sempre. A base do IR é o valor **líquido de
INSS** (confirmado em 9.3.6, `pagina_pdf: 185`: "após a dedução da parcela previdenciária (art.
74 do Dec. 3000/99)").

**R-07-02 — assimetria das cotas.** A cota do **empregado** é deduzida do crédito, tem teto e
entra na totalização. A cota do **empregador** é calculada sobre o mesmo crédito, **não é
dedutível dele e não tem teto**. São grandezas de natureza diferente sobre a mesma base.

**R-07-03 — o acordo de valor líquido inverte o ônus.** É a única exceção declarada à dedução.

---

## 2. Fato gerador — o corte de 05/03/2009

**Item 9.2.5.1**, `pagina_pdf: 116–119`. É o eixo do capítulo inteiro.

### 2.1 A lei

Lei 11.941/09 (conversão da MP 449/08) acrescentou os §§ 2º e 3º ao art. 43 da Lei 8.212/91.
Transcrição literal do manual, `pagina_pdf: 117`:

> "§2º Considera-se ocorrido o fato gerador das contribuições sociais na data da prestação do
> serviço. (Incluído pela Lei nº 11.941/09, de 2009)"
>
> "§3º As contribuições sociais serão apuradas mês a mês, com referência ao período da
> prestação de serviços, mediante a aplicação de alíquotas, limites máximos do
> salário-de-contribuição e acréscimos legais moratórios vigentes relativamente a cada uma das
> competências abrangidas, devendo o recolhimento ser efetuado no mesmo prazo em que devam
> ser pagos os créditos encontrados em liquidação de sentença ou em acordo homologado, sendo
> nesse último caso o recolhimento será feito em tantas parcelas quantas as previstas no
> acordo, nas mesmas datas em que sejam exigíveis e proporcionalmente a cada uma delas."

### 2.2 A regra de corte — Súmula 45 do TRT-3

`pagina_pdf: 117–118` — o verbete atravessa a quebra de página. Literal:

> "o fato gerador da contribuição previdenciária relativamente ao período trabalhado até
> 04/03/2009 é o pagamento do crédito trabalhista (**regime de caixa**), pois quanto ao período
> posterior a essa data o fato gerador é a prestação dos serviços (**regime de competência**), em
> razão da alteração promovida pela Medida Provisória n. 449/2008, convertida na Lei n.
> 11.941/2009, incidindo juros conforme cada período"

O TST Pleno decidiu no mesmo sentido em **20/10/2015**, `TST-E-RR-1125-36.2010.5.06.0171`,
Rel. Min. Alexandre Agra Belmonte (`pagina_pdf: 118`).

| Competência da parcela | Fato gerador | Regime |
|---|---|---|
| até **04/03/2009** | pagamento do crédito ao reclamante | **caixa** |
| a partir de **05/03/2009** | prestação do serviço | **competência** |

**R-07-04 — o eixo de corte é a competência da PARCELA**, não a do processo, do ajuizamento
ou do pagamento. Um contrato que atravesse 05/03/2009 tem **os dois regimes na mesma conta**.

### 2.3 A cisão que o Pleno do TST fez, e que muda quem paga o quê

`pagina_pdf: 118`, da ementa transcrita:

> "a) pela atualização monetária, o trabalhador e a empresa, por serem ambos contribuintes do
> sistema; e b) pelos juros de mora e pela multa, **apenas a empresa**, não sendo cabível que por
> eles pague quem, até então, sequer tinha o reconhecimento do crédito sobre o qual incidiriam
> as contribuições previdenciárias e que não se utilizou desse capital."

**R-07-05 — três marcos temporais distintos dentro do mesmo regime de competência:**

| O quê | Desde quando incide | Sobre quem |
|---|---|---|
| Atualização monetária | prestação do serviço | reclamante **e** reclamada |
| Juros de mora | prestação do serviço | **só** a reclamada |
| **Multa** | **exaurimento do prazo de citação para pagamento** | **só** a reclamada |

A multa **não retroage** à prestação de serviços. Literal, `pagina_pdf: 118`: "decidiu-se que
não incide retroativamente à prestação de serviços, e sim a partir do exaurimento do prazo de
citação para pagamento, uma vez apurados os créditos previdenciários, se descumprida a
obrigação, observado o limite legal de 20%".

### 2.4 A ressalva que o manual impõe ao calculista

`pagina_pdf: 119`, literal:

> "Portanto, o calculista deverá observar **estritamente as decisões existentes nos autos** e se
> não houver definição quanto ao critério de correção do débito previdenciário, deverá observar
> o que dispõe a Súmula 45 para a elaboração dos cálculos de liquidação."

**R-07-06 — precedência.** O título vence a Súmula 45. A Súmula 45 é o *default*. É a
invariante **R8** aplicada a este capítulo, e a mesma fórmula reaparece em 9.2.7
(`pagina_pdf: 129`): "Ressalvamos, porém, que o calculista deverá observar sempre as decisões
existentes nos autos."

---

## 3. Os três regimes de atualização da contribuição

**Item 9.2.7**, `pagina_pdf: 129`. Literais, na íntegra, porque é a espinha operacional:

> "**a)** cálculo de liquidação com parcelas salariais apuradas até 04/03/09 - O fato gerador é
> o pagamento do crédito ao reclamante e aplica-se o regime de caixa. As contribuições
> previdenciárias apuradas, mês a mês, são atualizadas com os mesmos índices de atualização do
> crédito do reclamante (atualmente a TR) até a data do pagamento do reclamante e a partir daí
> sofrem a incidência dos acréscimos legais da legislação previdenciária, quando não recolhidas
> no prazo legal pela reclamada."

> "**b)** cálculo de liquidação com parcelas salariais apuradas a partir de 05/03/09 – O fato
> gerador é a prestação de serviços e aplica-se o regime de competência. As contribuições
> previdenciárias apuradas, mês a mês, são atualizadas com os acréscimos legais previstos no
> art. 35 da Lei 8.212/91 (atualização monetária e juros), conforme tabela para recolhimento em
> atraso, divulgada pela Secretaria da Receita Federal do Brasil. Os juros de mora correspondem
> à Selic e a multa ao percentual de 0,33% ao dia, limitada a 20%. De acordo com a decisão do
> Pleno do TST, a multa incide após o vencimento do prazo de citação para o recolhimento
> previdenciário. **Todavia, há decisões determinando que a multa incida também desde a efetiva
> prestação de serviços. Nesta hipótese, deverá ser observado o contido na decisão.**"

> "**c)** cálculo de liquidação com parcelas salariais abrangendo os dois períodos: O calculista
> deverá atualizar as contribuições previdenciárias, observando os dois critérios. Os valores
> mensais da contribuição previdenciária apurados até 04/03/09 serão atualizados com o mesmo
> índice de correção do débito trabalhista e somente após o pagamento do crédito ao reclamante,
> haverá a incidência dos juros Selic e da multa. Já os valores de contribuição previdenciária,
> apurados a partir de 05/03/09, sofrem os acréscimos legais da legislação previdenciária, desde
> a efetiva prestação de serviços."

**R-07-07 — determinação de apurar o período contratual muda tudo.** `pagina_pdf: 129`:

> "Se houver determinação para apurar as contribuições previdenciárias do período contratual,
> os acréscimos legais próprios da legislação previdenciária (atualização, juros e multa)
> incidirão a partir da data da efetiva prestação dos serviços **durante todo o período de
> apuração**. Nesta hipótese, a mora da reclamada é incontestável, visto que o empregado já
> recebeu na época própria os salários devidos."

---

## 4. Cota do empregado — a apuração mês a mês

**Item 9.2.7.1**, `pagina_pdf: 128–130`.

**R-07-08 — base legal.** `pagina_pdf: 128`: "As contribuições sociais a cargo do reclamante
devem ser calculadas, **mês a mês**, na forma do art. 20 da Lei 8212/91, art. 276, § 4º, do Dec.
3048/99, Súmula/TST nº 368, III e Súmula 45 do TRT-3ª Região."

**R-07-09 — salário de contribuição.** `pagina_pdf: 128`: "O salário de contribuição constitui
no valor que a executada tomou como base para recolher a contribuição previdenciária na época
própria, ou seja, o valor sobre o qual foi calculado o desconto previdenciário efetuado no
recibo salarial do exequente, mês a mês, durante o contrato de trabalho."

### A fórmula

```
SC_novo(m)      = SC_contrato(m) + BaseSalarialOriginal(m)      ← valor ORIGINAL, sem correção
alíquota(m)     = f(SC_novo(m), tabela_salário_contribuição(época))
INSS_devido(m)  = SC_novo(m) × alíquota(m)   , limitado ao teto da época
Dif_INSS(m)     = INSS_devido(m) − INSS_recolhido_contrato(m)

Se SC_contrato(m) já atingiu o limite máximo  ⇒  Dif_INSS(m) = 0
```

Literal do passo 2, `pagina_pdf: 130`: "Somar o salário de contribuição do item 1 com o valor
original das parcelas salariais apuradas no cálculo, mês a mês, a fim de se apurar **um novo
salário de contribuição**. Este valor servirá de base para fixação de uma nova alíquota".

**R-07-10 — a base é o valor ORIGINAL, antes da correção monetária.** Literal do roteiro da
cota patronal, `pagina_pdf: 129`: "sobre o valor original da base de cálculo, ou seja, sobre o
total mensal das parcelas salariais **antes da aplicação da correção monetária**". A correção
entra depois, sobre a contribuição apurada — não sobre a base.

**R-07-11 — bloqueio do mês pelo teto.** Literal, `pagina_pdf: 130`:

> "**Importante:** No mês em que ficar comprovado que a contribuição foi descontada pelo limite
> máximo do salário-de-contribuição durante o contrato de trabalho, não haverá desconto a ser
> efetuado referente àquele mês sobre o crédito trabalhista devido ao exequente."

**R-07-12 — a multa não incide sobre juros.** `pagina_pdf: 129`: "Não há incidência de multa
sobre os juros."

**R-07-13 — memória de cálculo segregada.** `pagina_pdf: 130`: "os totais apurados nos itens 1,
2.a e 2.b e 3 deverão ser informados separadamente, tendo em vista que o somatório do
principal, juros e multa dificulta as atualizações futuras." Não é formalidade: 9.2.7.3 depende
disso para reatualizar sem refazer mês a mês.

---

## 5. Progressividade — alíquota única sobre o total

**Pergunta do enunciado, respondida.** O manual aplica **alíquota única sobre o total** do novo
salário de contribuição, **não por faixas**. Literal, `pagina_pdf: 130`, passo 3:

> "Com base no salário de contribuição encontrado no item 2 e nas tabelas de salário de
> contribuição da época, **estabelecer uma nova alíquota** e apurar a contribuição social devida,
> respeitando o teto máximo de contribuição da época."

Confirmado pela aritmética dos exemplos: `pagina_pdf: 131` — 951,99 × 9,00% = 85,68;
`pagina_pdf: 133` — 1.085,60 × 8,00% = 86,85; `pagina_pdf: 135` — 1.675,98 × 11,00% = 184,36.
Uma alíquota, o total inteiro.

**E isso NÃO muda por período dentro do manual.** O critério é o mesmo em exemplos de 2008,
2009 e 2013/14.

> **⚑ FASE 4 — F7-01.** A **EC 103/2019** instituiu alíquotas **progressivas por faixa** para o
> segurado empregado a partir de **01/03/2020**. O critério descrito na p.130 deixa de valer para
> competências a partir dessa data. O manual é de 2016 e não a conhece. **Marcado, não
> confrontado** — a base normativa do repositório não cobre descontos.

---

## 6. Cota patronal

**Item 9.2.4.1**, `pagina_pdf: 109–110`.

| Situação | Alíquota | Fonte |
|---|---|---|
| Empresas em geral, com vínculo, desde nov/91 | **20% + RAT (1, 2 ou 3%)** | p.109 |
| Instituições financeiras | **+ 2,5%** sobre o 20% | Lei 8212/91, art. 22, § 1º — p.109 |
| Aposentadoria especial | **+ 12, 9 ou 6 pontos**, só sobre a remuneração do empregado exposto | p.109 |
| Sem vínculo, mai/96 a fev/00 | 15% | art. 201, II, Dec. 3048/99 — p.109 |
| Sem vínculo, a partir de mar/00 | 20% | Lei 9876/99 — p.110 |
| Sem vínculo, a partir de abr/03 | 20% **+ 11% de retenção** do contribuinte individual | p.110 |
| Empregador doméstico, a partir de **01/10/15** | **8% + 0,8% (SAT) = 8,8%** | LC 150/15, art. 34 — p.115 |

**R-07-14 — o FAP tem eixo de vigência próprio.** `pagina_pdf: 109`, literal:

> "A partir de setembro/2007, as alíquotas referentes ao risco ambiental de trabalho poderão
> ser reduzidas em até 50% ou aumentadas em até 100%, em razão do desempenho da empresa em
> relação à sua respectiva atividade, aferido pelo Fator Acidentário de Prevenção – FAP"
>
> "O FAP é disponibilizado pelo Ministério da Fazenda [...] e **produz efeitos tributários a
> partir do primeiro dia do quarto mês subsequente ao de sua divulgação**."

Um quarto eixo temporal — não é competência, não é fato gerador: é **divulgação + 4 meses**.

**R-07-15 — quando só se apura a cota do empregado.** Quatro hipóteses, todas com cota patronal
substituída ou isenta:

| Hipótese | Item | `pagina_pdf` |
|---|---|---|
| Optante pelo SIMPLES | 9.2.4.3 | 114 |
| Associação desportiva com clube de futebol profissional (5% da receita de espetáculos) | 9.2.4.4 | 115 |
| Entidade beneficente certificada (Lei 12.101/09) | 9.2.4.5 | 115 |
| Produtor rural PJ/PF e agroindústria sob contribuição substitutiva | 9.2.4.2 | 114 |

Ressalva comum, literal (`pagina_pdf: 115`, beneficentes): a partir de **abril/03** as entidades
beneficentes "são obrigadas a descontar e recolher 20% das remunerações pagas ou creditadas a
contribuinte individual" — logo, **sem vínculo, a cota do reclamante é 20% e não 11%**.

**R-07-16 — contribuições de terceiros ficam fora.** Item 9.2.2, `pagina_pdf: 108`. Súmula 24
do TRT-3, literal: "A Justiça do Trabalho é incompetente para executar as contribuições
arrecadadas pelo INSS, para repasse a terceiros, decorrentes das sentenças que proferir".

---

## 7. Desoneração da folha

**Item 9.2.10**, `pagina_pdf: 176`. Curto e cirúrgico.

**R-07-17 — o calculista não calcula CPRB; deixa de calcular os 20%.** Literal:

> "quando a atividade da empresa é abrangida pelos setores beneficiados pela medida de
> desoneração da folha de pagamento, não há o que se falar na apuração dos 20% sobre as
> parcelas salariais apuradas nos cálculos trabalhistas."

**R-07-18 — o ônus da comprovação é da reclamada, e o manual diz por quê.** Literal:

> "a comprovação nos autos pela reclamada do seu enquadramento é fundamental, visto que dada a
> especificidade da matéria, as alterações constantes na legislação [...] **não é possível ao
> calculista identificar se a empresa faz jus ou não**, bem como o período em que foi
> beneficiada. Cabe também a reclamada informar o percentual, se a mesma estiver enquadrada no
> sistema misto."

**R-07-19 — o RAT/SAT sobrevive sempre.** Literal:

> "O regime substitutivo estabelecido pela Lei 12546/11 engloba apenas as contribuições
> previstas nos incisos I e III do art. 22 da Lei 8212/91, continuando a reclamada responsável
> pelo recolhimento do grau de incidência de incapacidade laborativa [...] **mesmo se houver
> substituição integral da alíquota de 20%**."

**R-07-20 — o benefício se afere pelo período da PRESTAÇÃO DE SERVIÇOS.** Literal: "é
necessário analisar se o período de apuração das contribuições previdenciárias da reclamatória
trabalhista alcança o período em que a reclamada é beneficiária [...] Se no período de apuração
das verbas trabalhistas, a reclamada não for atingida pela medida, a contribuição previdenciária
cota patronal deverá ser apurada em sua integralidade."

> **⚑ FASE 4 — F7-02.** A desoneração mudou muitas vezes depois de 2016: Lei 13.670/2018,
> prorrogações, Lei 14.784/2023, **Lei 14.973/2024** (reoneração gradual 2025–2027). O texto da
> p.176 está materialmente superado. Marcado, não confrontado.

---

## 8. Imposto de renda — o que é tributável

**Item 9.3.2**, `pagina_pdf: 180`. A regra de método, literal:

> "Diferentemente do desconto previdenciário, no caso do imposto de renda **é de pouca valia
> orientar-se pelo conceito de verba indenizatória ou salarial** para definir se determinada
> verba deferida pode ou não ser tributada."
>
> "Isto porque **são verbas não-tributáveis somente aquelas que a lei expressamente mencionar**.
> Em outras palavras: a não ser aquelas verbas que a lei expressamente permite a exclusão da
> base de cálculo, por isenção ou não incidência, todas as demais estão sujeitas à tributação."

**R-07-21 — inversão de lógica entre os dois descontos.** No INSS pergunta-se *a verba é
salarial?*; no IR pergunta-se *a lei isenta?*. Usar o mesmo teste nos dois é erro de método, e o
manual diz isso expressamente.

**R-07-22 — deduções ≠ verbas não tributáveis.** `pagina_pdf: 180`: "As deduções ocorrem em
função da pessoa do contribuinte (dependentes, pensão judicial e contribuição previdenciária).
As parcelas não tributáveis têm vinculação com a previsão legal de isenção."

### 8.1 Férias e abono — não incide IR

**Item 9.3.4**, conclusão literal, `pagina_pdf: 184`:

> "conclui-se que não há incidência de imposto de renda sobre:
> - Férias integrais + 1/3 não gozadas por necessidade de serviço e pagas em pecúnia na rescisão
>   contratual, exoneração ou aposentadoria;
> - Férias em dobro + 1/3, pagas na rescisão contratual, exoneração ou aposentadoria;
> - Férias proporcionais + 1/3, pagas na rescisão contratual, aposentadoria ou exoneração e
> - Abono pecuniário"

### 8.2 Danos morais — não incide IR

**Item 9.3.5**, conclusão literal, `pagina_pdf: 185`: "o valor referente à indenização por danos
morais recebido pelo reclamante em reclamatória trabalhista **não está mais sujeito à
tributação**." Fundamento: Ato Declaratório PGFN nº 09/2011.

### 8.3 Juros de mora — a regra com duas portas

**Item 9.3.3**, `pagina_pdf: 180–182`. Conclusão literal, `pagina_pdf: 182`:

> "na elaboração dos cálculos de liquidação, os juros de mora sobre as parcelas tributáveis
> apenas deverão ser excluídos da base de cálculo do imposto de renda **se houver decisões nos
> autos neste sentido ou se pagas no contexto da rescisão do contrato de trabalho**."

Duas portas independentes:

1. **decisão nos autos** — OJ 400/SDI-I do TST exclui os juros, "independentemente da natureza
   jurídica da obrigação inadimplida" (`pagina_pdf: 181`);
2. **contexto da rescisão** — IN/RFB 1500/14, art. 62, § 3º, II, "a", e Solução de Consulta
   Interna Cosit nº 13, de 30/06/2016, transcrita integralmente na `pagina_pdf: 181`.

**R-07-23 — o alcance da segunda porta é mais largo do que "verbas rescisórias".** Literal da
Cosit 13/2016 (`pagina_pdf: 181`): a dispensa "está direcionada apenas ao contexto da **perda do
emprego**, não se destinando à extinção do contrato de trabalho decorrente de **pedidos de
demissão** por iniciativa unilateral do empregado e abrange os juros referentes às verbas
rescisórias em sentido amplo [...] abarcando, assim, além dos juros referentes às verbas
rescisórias em sentido estrito, também os juros relativos às demais verbas trabalhistas devidas
ao trabalhador e não adimplidas no curso do contrato do trabalho".

**R-07-24 — o principal continua tributado.** `pagina_pdf: 181–182`: "a dispensa de retenção e
tributação atinge apenas os juros [...] não incluindo, a parcela principal em si. Dessa forma, o
valor principal da verba (horas extras, do adicional de insalubridade, do saldo de salário, do
13º salário, entre outros) **acrescido de correção monetária, continua sendo tributado**."

**R-07-25 — contrato em curso: os juros são tributáveis.** `pagina_pdf: 182`: "Os juros de mora
incidentes sobre as verbas decorrentes de reclamatória trabalhista passíveis de tributação,
**quando há continuidade do contrato de trabalho**, não foram incluídos nas hipóteses de dispensa
de retenção aceitas pela Secretaria da Receita Federal do Brasil".

> **⚑ FASE 4 — F7-03.** O manual registra a repercussão geral reconhecida no **RE 855091**
> (`pagina_pdf: 181` — o manual grafa sem ponto) e diz que "a questão não está resolvida". O **Tema 808 do STF** foi julgado
> depois de 2016. Marcado, não confrontado.

---

## 9. Os dois regimes do IR: art. 12-A e art. 12-B

**Itens 9.3.7 e 9.3.8**, `pagina_pdf: 187–191`.

| | **art. 12-A** — regime especial (RRA) | **art. 12-B** — regime geral |
|---|---|---|
| Quando | rendimentos de **anos-calendário anteriores** ao do recebimento | rendimentos do **mesmo ano-calendário** do pagamento |
| Tabela | progressiva mensal do mês do recebimento, **multiplicada pelo NM** | progressiva mensal do mês do pagamento, **sem multiplicação** |
| Tributação | exclusivamente na fonte, **em separado** dos demais rendimentos do mês | junto aos demais |
| Código | 1889 | 5936 |

**R-07-26 — quando há os dois, são duas apurações.** `pagina_pdf: 190`, literal:

> "Se houver rendimentos correspondentes ao ano atual do recebimento e de anos anteriores, será
> necessário efetuar **duas apurações distintas**"

**R-07-27 — o marco inicial do 12-A é 01/01/2010.** `pagina_pdf: 189`: "os rendimentos recebidos
acumuladamente a partir de 1º de janeiro de 2010 poderão ser tributados pela nova regra".

**R-07-28 — a partir de 11/03/2015 o 12-A deixa de ter restrição por tipo de rendimento.**
`pagina_pdf: 187`: "A partir de 11/03/15, não há mais a restrição quanto ao tipo de rendimento
imposta pela antiga redação do art. 12-A, bastando que os mesmos sejam submetidos à incidência
do imposto de renda com base na tabela progressiva e correspondentes a anos-calendário
anteriores ao do recebimento." (MP 670/15 → Lei 13.149/15.)

---

## 10. O número de meses (NM) — variável, nunca doze

**Item 9.3.7.3**, `pagina_pdf: 188`. Confirma o que o bloco 1 já havia registrado contra o
escopo declarado: **NM é variável**.

Regra literal:

> "serão considerados **apenas os meses em foram apurados rendimentos passíveis de tributação**
> no cálculo de liquidação."

E o manual nomeia **dois erros comuns**, literalmente:

> "Alguns cálculos tomam como base para a apuração do número de meses **o período trabalhado ou
> o período imprescrito. Todavia, tal critério está incorreto**, visto que a norma legal aplicável
> faz menção à quantidade de meses a que se referem os rendimentos tributáveis."
>
> "Outro equívoco cometido é **considerar todos os meses constantes no cálculo**, mesmo que em
> determinados meses não sejam apuradas parcelas passíveis de incidência de imposto de renda."

**R-07-29 — o 13º salário vale um mês, sempre.** Item 9.3.7.2, `pagina_pdf: 188`: "O 13º salário
entra no cômputo da quantidade dos meses do rendimento como um mês calendário [...] **não
importando se proporcional ou integral**, visto que a Instrução Normativa nº 1500/14 não faz
distinção."

**R-07-30 — no 12-A o 13º NÃO é tributado em separado.** `pagina_pdf: 188`: "A nova metodologia
de cálculo do imposto de renda também não prevê a tributação do 13º salário de forma separada,
sendo o mesmo englobado no total de rendimentos para a apuração do número de meses". É o
contrário do que vale no INSS, onde o 13º é base autônoma (§ 11).

### A fórmula do 12-A

```
NM              = nº de meses COM rendimento tributável   (+1 por 13º apurado)
faixa           = f(base ÷ NM)  ou  f(base, limites_da_faixa × NM)      ← equivalentes
parcela_deduzir = parcela_deduzir_da_faixa × NM
IR              = base × alíquota − parcela_deduzir
```

Os dois caminhos de enquadramento dão o mesmo resultado. O manual anuncia "dois critérios"
(`pagina_pdf: 193`) mas **só enuncia o primeiro**; o "critério rápido" (dividir a base pelo NM)
existe apenas dentro de exemplos — ver detalhe § 4.

### Deduções permitidas no 12-A

**Item 9.3.7.4**, `pagina_pdf: 188`, literal:

> "poderão ser deduzidas da base de cálculo a **contribuição previdenciária** e a **pensão
> alimentícia** paga em dinheiro em face das normas do Direito de Família (§ 3º, incisos I e II do
> art. 12-A da Lei 7713/88. Ressaltamos que **a dedução com dependente não está prevista** entre o
> elenco das deduções permitidas no § 3º do art. 12-A da Lei 7713/88."

**R-07-31 — duas deduções, não três.** Dependente **não** deduz no RRA. Honorários advocatícios
**não aparecem como dedução em lugar nenhum** do capítulo 9 — pendência P7-08.

---

## 11. Momento do cálculo e recálculo a cada pagamento

**Item 9.3.6**, `pagina_pdf: 185–186`.

**R-07-32 — o IR se recalcula a cada liberação.** Literal:

> "por ocasião de cada pagamento ao reclamante, o imposto de renda deverá **sempre ser
> recalculado**, incidindo apenas sobre o valor efetivamente disponibilizado, considerando a
> proporção das parcelas passíveis de tributação."

Razão declarada: "muitas vezes o pagamento da execução é parcial [...] Nesta hipótese, o imposto
de renda não poderá incidir sobre o total devido ao reclamante, mas apenas sobre a parte
efetivamente disponível" (art. 12-A § 1º, art. 12-B, art. 56 do Dec. 3000/99).

**R-07-33 — o valor do IR no cálculo de liquidação é estimativa.** `pagina_pdf: 190`: a tabela
é a "vigente no mês do recebimento do crédito pelo reclamante **ou na data final de atualização
dos cálculos, sendo que nesta última hipótese a apuração é apenas para fins estimativos**."

**R-07-34 — a virada do ano-calendário muda o regime.** `pagina_pdf: 193`: "Caso a reclamada não
pague o valor devido ao reclamante em 2016, o imposto de renda **será recalculado a partir de
2017 para observar o regime especial** de tributação do art. 12-A". Um cálculo do 12-B vira 12-A
pela simples passagem do ano — e a regra só existe em observação de exemplo (detalhe § 4).

**R-07-35 — prazo de 15 dias para comprovar.** `pagina_pdf: 186`: "a fonte pagadora tem prazo de
15 dias da data da retenção [...] para comprovar nos autos o recolhimento do imposto de renda
[...] Caso a reclamada não comprove a retenção, caberá ao Juízo do Trabalho determinar o cálculo
e o recolhimento."

---

## 12. O corte (A)/(B), e o resultado que ele produziu

O enunciado deu o critério: **"se muda quando o governo publica portaria, é (B). Se muda quando
muda a lei ou a jurisprudência, é (A)."** Aplicado ao capítulo 9, o resultado é assimétrico e
vale registro.

| Conteúdo | Muda por | Classe |
|---|---|---|
| Alíquota patronal 20% / 22,5% / 15% / 11% / 8,8% | **lei** (8.212/91, 9876/99, LC 150/15) | **(A)** |
| Percentuais de multa por competência (50% → 10% → 40% → 4/7/10% → 8/14/20% → 0,33%/dia) | **lei** (8.383/91, 9528/97, 9876/99, MP 449/08) | **(A)** |
| Regra do FAP (−50% a +100%; efeito no 4º mês) | **lei** (10.666/03, Dec. 3048/99 art. 202-A) | **(A)** |
| Fato gerador, regimes, NM, deduções | lei e jurisprudência | **(A)** |
| **Tabelas de faixas** do salário-de-contribuição e do IRRF | **portaria / IN** | **(B)** |
| Índices Selic e tabela única CSJT | divulgação mensal | **(B)** |
| Coeficientes UFIR ago/64–dez/79 | tabela administrativa | **(B)** |

**Quase tudo no capítulo 9 é (A).** As faixas — a parte genuinamente (B) — não moram aqui: estão
no **capítulo 18**, já extraídas no bloco 1 (`serie-18.4`, `18.5`, `18.6`, `18.7`, `18.15`). O
capítulo 9 **remete** a elas: `pagina_pdf: 130` — "de acordo com as tabelas vigentes nas épocas
próprias constantes nos **anexos deste manual**".

A única série genuinamente nova do capítulo 9:

| Arquivo | Item | Linhas | `pagina_pdf` |
|---|---|---:|---|
| [`serie-9.2.11-ufir-juros-ate-dez79.csv`](serie-9.2.11-ufir-juros-ate-dez79.csv) | 9.2.11 | **185** | 178 |

Cobre **ago/64 a dez/79**, sem lacuna. Conferido mês a mês. `jan/80` **não está** na Tabela I —
ver detalhe § 7.

---

## 13. Marcas Fase 4

Pontos afetados por norma posterior a 2016. **Apenas marcados; nenhum confrontado** — a base
normativa do repositório não cobre descontos.

| # | Ponto | `pagina_pdf` | Norma posterior |
|---|---|---|---|
| **F7-01** | Alíquota única sobre o total (cota do segurado) | 130, 158 | **EC 103/2019** — progressivas **por faixa** desde 01/03/2020. É a marca de maior impacto |
| **F7-02** | Desoneração da folha, item 9.2.10 inteiro | 176 | Lei 13.670/2018; Lei 14.784/2023; **Lei 14.973/2024** (reoneração gradual 2025–2027) |
| **F7-03** | Juros de mora na base do IR — "a questão não está resolvida" | 181 | **Tema 808 do STF** (RE 855091), julgado depois de 2016 |
| **F7-04** | "atualmente a TR" como índice do débito trabalhista | 129 | **ADC 58/59 e ADIs 5867/6021** (STF, 18/12/2020). Alcança todo ponto que diga "mesmos índices de atualização do débito trabalhista" (pp.148, 149) ou "mesmos índices de atualização do crédito do reclamante" (pp.129, 138, 155) |
| **F7-05** | Base = "parcelas de natureza salarial" | 128 | **Lei 13.467/2017** — art. 457, §§ 1º a 4º da CLT redefine integrações |
| **F7-06** | Acordo homologado sem o rito de jurisdição voluntária | 153–154, 201 | **Lei 13.467/2017** — arts. 855-B a 855-E da CLT |
| **F7-07** | RIR/99 (Dec. 3000/99), citado ao longo de todo o 9.3 | 180, 186, 207 | Revogado e substituído pelo **Dec. 9.580/2018 (RIR/2018)** |
| **F7-08** | IN/RFB 1500/14 com alterações da 1558/15 | 187–208 | INs posteriores |
| **F7-09** | Tabelas de IRRF e de salário-de-contribuição congeladas em abr/15 | anexos | Portarias e leis posteriores |
| **F7-10** | Códigos 2909, 1708, 1889, 5936 e a GPS | 153, 196, 207 | eSocial, DCTFWeb, EFD-Reinf |
| **F7-11** | Súmula 45 do TRT-3, editada em ago/15 | 117 | Confirmar redação e vigência atuais |
| **F7-12** | PLR — Lei 10.101/00 na redação da Lei 12.832/13 | 199 | **Lei 14.020/2020** alterou a Lei 10.101/00 |

---

## 14. Ver também

- [`bloco-07-descontos-detalhe.md`](bloco-07-descontos-detalhe.md) — roteiros completos, acordo,
  IR sobre acordo, PLR, pré-1980, e os **trinta e um defeitos do original**
- [`bloco-07-relatorio.md`](../bloco-07-relatorio.md) — relatório do bloco, cruzamentos e pendências
- [`bloco-01-tabelas.md`](bloco-01-tabelas.md) — item 18.1 (matriz de incidência) e as faixas
- `../../tabelas-normativas/trt3-18.1-incidencia-parcelas.json` — as 44 parcelas × INSS/FGTS/IRRF
