# Bloco 7 — detalhe

Complemento de [`bloco-07-descontos.md`](bloco-07-descontos.md). Aqui estão os **roteiros
completos**, as **hipóteses de atualização**, o **acordo**, o **IR sobre acordo**, a **PLR**, o
**pré-1980** e os **defeitos do original**.

Manual TRT-3 (2016), capítulo 9, `pagina_pdf` 107–208. Offset 0.

---

## 1. As duas tabelas de Selic, e o erro que elas causam

**Item 9.2.6**, `pagina_pdf: 123–128`. O manual abriu um tópico só para isto, e é achado de
primeira ordem.

Existem **duas** tabelas, ambas da Receita Federal, e elas estão **deslocadas em um mês**:

| Tabela | Para quê | Onde a taxa fica alocada |
|---|---|---|
| **Tabela prática a ser aplicada nas contribuições em atraso** | contribuição previdenciária | dentro do **próprio mês de competência** |
| **Taxa de Juros Selic – Acumulados** | tributos federais, incl. IR | no **mês do vencimento** do prazo de recolhimento |

Literal, `pagina_pdf: 123`:

> "A diferença entre elas é que a tabela prática a ser aplicada nas contribuições previdenciárias
> em atraso traz a taxa de juros acumulada alocada **dentro do próprio mês de competência**,
> enquanto a tabela de Juros Selic - Acumulados apresenta a taxa de juros alocada **no mês do
> vencimento do prazo para o recolhimento**"

O exemplo que fixa a diferença, `pagina_pdf: 124`, literal:

> "se formos atualizar um valor de contribuição previdenciária referente à competência jan/10,
> na tabela prática a ser aplicada nas contribuições em atraso, basta multiplicar o valor devido
> pela taxa constante no mês de jan/10 (dentro do próprio mês). Por outro lado, se utilizarmos a
> tabela de Juros Selic - Acumulados incidente sobre os tributos federais, o valor devido deverá
> ser multiplicado pela taxa constante no mês de **fevereiro/10**, ou seja, o mês subsequente."

**D7-01 — a mesma competência lê linhas diferentes conforme a tabela.** Usar a linha de jan/10
na tabela errada erra por um mês inteiro de Selic. As duas tabelas dão o mesmo número, desde
que se saiba **onde ler**.

### A regra do 1% — e a duplicidade que ela causa

`pagina_pdf: 126`, literal:

> "quando o cálculo já está atualizado com os juros Selic, **não é correto** utilizar a taxa de
> juros constante na tabela prática para recolhimento em atraso a partir do último cálculo.
> Primeiro, porque a tabela é formatada para a atualização dos valores originais nas competências
> próprias [...] Segundo, **a tabela já contém a Selic acumulada com 1% de juros**. Como no momento
> de elaborar os cálculos originais, já foram utilizados os percentuais da tabela acumulados com
> 1% de juros, se for utilizada novamente a taxa acumulada da tabela, sem a exclusão de 1%,
> **ocorrerá duplicidade**."

**D7-02 — reatualizar exige subtrair 1%.** Vale para todas as reatualizações de 9.2.7.3.

### As quatro fórmulas de variação da Selic

| Caso | Tabela prática (INSS) | Taxa Selic – Acumulados (IR) |
|---|---|---|
| **a.1 / a.2** — achar taxa de data retroativa, valor **original** | taxa do mês inicial − taxa dos **dois meses anteriores** ao mês-alvo, **+ 1%** | taxa do mês subsequente ao pagamento − taxa do **mês anterior** ao mês-alvo, **+ 1%** |
| **b.1.1 / b.2.1** — reatualizar até a data da tabela | taxa dos **dois meses anteriores** à data final do cálculo-base **− 1%** | taxa do **mês anterior** à data final do cálculo-base **− 1%** |
| **b.1.2 / b.2.2** — reatualizar até data retroativa | taxa dos dois meses anteriores à data-base − taxa dos dois meses anteriores ao alvo | taxa do mês anterior à data-base − taxa do mês anterior ao alvo |

Ambas conferem: nos exemplos do próprio 9.2.6 as duas dão **9,62%** (`pagina_pdf: 125`),
**13,07%** (`pagina_pdf: 126` e `128`) e **7,63%** (`pagina_pdf: 127` e `128`).

> A primeira redação deste parágrafo citava **4,28%** como um dos pares de 9.2.6. O número é
> real, mas é dos exemplos de **9.2.7.3** (pp.141, 142, 147, 149, 152, 153) — não ocorre em
> nenhuma das pp.123–128. Corrigido pela validação adversarial.

**Sistemática que justifica o deslocamento**, literal `pagina_pdf: 125`: "Soma-se a taxa Selic a
partir do mês seguinte ao vencimento até o mês anterior ao pagamento e acrescenta 1% de juros no
final." E `pagina_pdf: 127`: "a taxa do mês é divulgada a partir do primeiro dia do mês
subsequente."

---

## 2. Roteiros do INSS — cota empregador e cota empregado

**Item 9.2.7.1**, `pagina_pdf: 129–130`.

### 2.1 Cota empregador — 3 passos

1. `pagina_pdf: 129` — "Aplicar, mês a mês, a alíquota referente à cota empregador [...] sobre o
   **valor original** da base de cálculo, ou seja, sobre o total mensal das parcelas salariais
   antes da aplicação da correção monetária."
2. **2.a** até 04/03/09 — índices do débito trabalhista (tabela única CSJT).
   **2.b** a partir de 05/03/09 — juros Selic + 1% ao mês (tabela prática SRFB).
3. Multa sobre os valores do item 1, a partir de 05/03/09, **se o comando sentencial determinar**
   desde a prestação de serviços. "Não há incidência de multa sobre os juros."

### 2.2 Cota empregado — 8 passos

Literais, `pagina_pdf: 130`:

| # | Passo |
|---|---|
| 1 | "Verificar se nos autos existem os salários de contribuição efetivo [...] bem como as contribuições sociais já recolhidas em cada competência." |
| 2 | "Somar o salário de contribuição do item 1 com o valor original das parcelas salariais apuradas no cálculo, mês a mês, a fim de se apurar um novo salário de contribuição." |
| 3 | "estabelecer uma nova alíquota e apurar a contribuição social devida, respeitando o teto máximo de contribuição da época." |
| 4 | "Deduzir do valor apurado no item 03, a contribuição social já recolhida pelo empregador na época própria" |
| — | **"Importante:"** mês com desconto pelo limite máximo → **sem desconto** sobre o crédito |
| 5 | bifurcação 04/03/09, como na cota patronal |
| 6 | multa, se determinada desde a prestação de serviços |
| 7 | "A contribuição previdenciária que será deduzida do crédito do reclamante corresponde ao somatório dos valores apurados no item 04, **atualizados monetariamente**." |
| 8 | "No resumo do cálculo deverão constar os valores de INSS cota reclamante e reclamada acrescidos dos juros e multa para fins de totalização da execução." |

**D7-03 — assimetria entre o que se deduz e o que se recolhe.** O passo 7 diz que se deduz do
crédito do reclamante o principal **apenas corrigido**; o passo 8 diz que se recolhe o principal
**mais juros e multa**. A diferença é suportada pela reclamada — coerente com a cisão de
responsabilidades do Pleno do TST (espinha § 2.3).

---

## 3. O rateio do mês de março de 2009 — regra que só existe num exemplo

**Achado.** O mês em que a MP 449/08 entra em vigor precisa ser partido. **Não há enunciado
normativo**: a regra aparece só como observação sob a planilha do Exemplo 3.

Literal, `pagina_pdf: 135`:

> "Obs.: A contribuição previdenciária devida em mar/09 foi atualizada de forma proporcional até
> 04/03/09 com TR e a partir de 05/03/09 foram aplicados juros Selic.
> Total cont. previd. Mar/09 = 52,81
> Valor devido proporcionalmente até 04/03/09 = 52,81/30 x 4 = 7,04"

e `pagina_pdf: 136`: "Valor devido proporcionalmente de 05/03/09 a 31/03/09 = 52,81/30 x 26 =
45,77".

```
INSS_mar09_TR    = INSS(mar/09) / 30 × 4      → índice trabalhista
INSS_mar09_Selic = INSS(mar/09) / 30 × 26     → Selic (+ multa se devida)
```

**D7-04 — o manual usa mês comercial de 30 dias num mês de 31.** 4 + 26 = 30, e março tem 31.
Divergência do original, **registrada e não corrigida**. É exatamente o fenômeno de granularidade
que o bloco 6 modelou (`competencia-atravessa-o-corte`): o corte é ao dia, a apuração é mensal.

---

## 4. Atualizar cálculos já homologados — 9.2.7.2 e 9.2.7.3

### 4.1 O defeito de numeração

**Há DOIS subitens numerados 9.2.7.3.** Não existe 9.2.7.4. Títulos literais:

| Numeração impressa | `pagina_pdf` | Título literal |
|---|---|---|
| 9.2.7.2 | 137 | "Atualização de cálculos de liquidação homologados com a contribuição social corrigida pelos índices do débito trabalhista" |
| 9.2.7.3 **(1ª)** | 140 | "Atualização de cálculos de liquidação homologados com a contribuição social corrigida pelos índices da legislação previdenciária" |
| 9.2.7.3 **(2ª)** | 145 | "Atualização de cálculos de liquidação homologados com a contribuição social corrigida pelos índices do débito trabalhista até 04/03/09 e da legislação previdenciária a partir de 05/03/09)" |

O parêntese final do terceiro título fecha sem abrir — do original.

**D7-05 — qualquer remissão a "9.2.7.3" é ambígua.** Neste repositório chamam-se **9.2.7.3-A**
(p.140) e **9.2.7.3-B** (p.145).

### 4.2 Os três cenários

| Subitem | Cálculo homologado corrigido por | Corresponde a |
|---|---|---|
| **9.2.7.2** | só TR / índices trabalhistas | parcelas até 04/03/09, ou fato gerador = pagamento |
| **9.2.7.3-A** | só Selic + multa | parcelas a partir de 05/03/09 |
| **9.2.7.3-B** | misto — TR até 04/03/09, previdenciário a partir de 05/03/09 | contrato que atravessa o corte |

### 4.3 Regra-mãe do 9.2.7.2 — `pagina_pdf: 137`

> "Nos cálculos com parcelas apuradas até 04/03/09 ou que o pagamento é considerado como fato
> gerador, os valores das contribuições previdenciárias (cota reclamante e reclamada) são
> atualizados pelos mesmos índices dos débitos trabalhistas **até o momento em que ocorre o
> pagamento** do crédito ao exequente. Se houver pagamento integral do crédito do reclamante e o
> não recolhimento da contribuição previdenciária no prazo legal, a atualização da contribuição
> segue os critérios da legislação previdenciária. **Quando o pagamento é efetuado de forma
> parcial, a parcela da contribuição proporcional ao valor pago** passará também a sofrer os
> acréscimos previstos na legislação previdenciária para recolhimento fora do prazo."

Quatro hipóteses: sem pagamento (H1, p.137); pagamento integral sem recolhimento (H2, p.138);
pagamento parcial sem recolhimento (H3, p.139); pagamento parcial **e** recolhimento parcial
(H4, p.140).

### 4.4 A dispensa de refazer mês a mês — 9.2.7.3-A, `pagina_pdf: 140`

> "Para reatualizar valores de contribuição social já corrigidos com os juros Selic e multa, **não
> é necessário refazer o cálculo mês a mês**, sendo necessário apenas que na planilha de cálculo
> [...] estejam discriminados os totais de INSS cota reclamante e reclamada, o total dos juros e o
> total da multa apurados até uma determinada data."

É por isso que a segregação do passo 8 (detalhe § 2.2) importa.

Roteiro, `pagina_pdf: 141`, literais dos passos 2 e 4:

> "2) Sobre os valores de INSS reclamante e reclamada (sem juros e multa), incidir o percentual da
> Selic acumulado de forma simples entre a data do último cálculo e a data final de atualização,
> **não acrescendo o percentual de 1% de juros para evitar duplicidade**"
>
> "4) Verificar se já foi apurada a multa no cálculo de origem. Caso positivo, basta repetir o
> valor, visto que **sobre multa não há correção ou juros**. Caso negativo ou se a multa tiver sido
> apurada em percentual inferior a 20%, apurar o percentual devido até a data final"

**D7-06 — a multa é inerte.** Não corrige, não rende juros, e o teto de 20% é absorvente: uma vez
atingido, repete-se.

**D7-07 — o pagamento não interfere no regime de competência.** `pagina_pdf: 142`: "o levantamento
parcial ou integral do crédito do exequente **não interfere** na atualização do débito
previdenciário a ser recolhido pela reclamada."

### 4.5 A decomposição proporcional do saldo — 9.2.7.3-A, 3ª hipótese

Recolhimento parcial. Roteiro de 13 passos, `pagina_pdf: 142–143`. O núcleo:

```
Total_K         = INSS_principal_G + Juros_I + Multa_J
Diferença_M     = Total_K − Recolhido_L
Principal_saldo = (INSS_principal_G / Total_K) × Diferença_M
Juros_saldo     = (Juros_I         / Total_K) × Diferença_M
Multa_saldo     = (Multa_J         / Total_K) × Diferença_M
Juros_novo      = Principal_saldo × Selic_acum(mês_recolhimento → data_final) + Juros_saldo
Multa_novo      = Multa_saldo                    ← não atualiza (passo 12)
```

**D7-08 — a amortização é rateada, não imputada.** O recolhimento parcial não quita primeiro o
principal nem primeiro a multa: abate proporcionalmente as três rubricas. Contraste com **D7-10**.

Observação literal, `pagina_pdf: 143`: "b - **Não importa o dia do recolhimento**, visto que a
taxa Selic é mensal."

### 4.6 A proporção do pagamento — 9.2.7.3-B, 3ª hipótese

`pagina_pdf: 151`, dois critérios declarados **alternativos**:

> "b) Determinar a proporção do crédito paga em relação ao total devido ao reclamante, utilizando
> **qualquer um dos dois critérios** demonstrados a seguir:
> 1) dividir o INSS cota reclamante proporcional ao levantamento pelo total de INSS cota
> reclamante atualizado até a data do pagamento
> 2) dividir o total bruto levantado pelo total bruto devido na data do levantamento"

No exemplo os dois dão **49,3227%**.

### 4.7 A ordem de imputação — 9.2.7.3-B, 4ª hipótese

`pagina_pdf: 152–153` — o trecho atravessa a quebra de página. Literal:

> "Quando há recolhimento parcial da contribuição previdenciária e o cálculo abrange os dois
> critérios de atualização [...] **geralmente, o abatimento ocorre primeiro em relação às
> competências mais antigas**. Dessa forma, primeiro deduz o montante recolhido do total apurado
> de contribuição previdenciária e atualizado com a TR (competências até 04/03/09) e se o valor
> for suficiente para quitar todo o período, restando saldo remanescente [...] deduz este saldo do
> montante de contribuição previdenciária já atualizado com os juros e multa"

E duas alternativas, `pagina_pdf: 153`:

> "Todavia, nada impede que se faça uma comparação entre o montante recolhido e os totais devidos
> [...] para verificar de qual período será melhor deduzir o total recolhido a fim de agilizar as
> atualizações futuras [...] Outra alternativa é verificar o **código de recolhimento (2909 para a
> reclamada e 1708 para o reclamante)** e efetuar a dedução, observando o valor recolhido em
> relação à cada uma das cotas."

**D7-09 — "geralmente" não é regra.** O manual dá um padrão e duas alternativas, sem critério de
escolha entre elas. **Pendência P7-01.**

**D7-10 — duas ordens de imputação convivem no mesmo capítulo.** Em 9.2.7.3-A a amortização é
**proporcional entre rubricas** (D7-08); em 9.2.7.3-B é **cronológica entre períodos**. O manual
não articula as duas.

---

## 5. Acordo — 9.2.8 e 9.2.9

### 5.1 Com e sem discriminação

**Com discriminação**, `pagina_pdf: 153`, literal:

> "Enquanto não há trânsito em julgado, a contribuição previdenciária incide sobre as parcelas
> salariais discriminadas no acordo homologado, sendo que nos termos da **Súmula 23 do TRT/3ª
> Região**, tal discriminação **não precisa observar a proporção** entre as parcelas de natureza
> salarial e indenizatórias postuladas na inicial."

**Sem discriminação**, `pagina_pdf: 154`, literal:

> "se não houver discriminação das verbas que compõem o montante do acordo, a contribuição incide
> **sobre o total da avença**, conforme Lei 8212/91, art. 43, § 1º [...] OJ SDI-1 nº 368/TST e
> IN/RFB nº 971/09, art. 102, inciso II, alinea b."

**Percentual não é discriminação**, `pagina_pdf: 154`, literal:

> "o Dec. 3048/99 prevê, ainda, no § 3º do art. 276, que **não pode ser considerada como
> discriminação** de parcelas legais de incidência de contribuição previdenciária, a **fixação de
> percentual** de verbas remuneratórias e indenizatórias constantes dos acordos homologados."

**D7-11 — a alíquota mínima de 8% morreu em 2004.** `pagina_pdf: 154`: a OS 66/97 previa alíquota
mínima na ausência de discriminação; "A Instrução Normativa nº 100/03 [...] revogou a O.S. 66/97,
**não existindo mais base legal para a aplicação da alíquota mínima**".

### 5.2 Depois do trânsito em julgado — a proporcionalidade volta

**OJ 376 da SDI-I**, editada em 19/04/2010. Item 9.2.8.3, `pagina_pdf: 164`, literal:

> "a contribuição previdenciária apurada sobre o valor do acordo celebrado e homologado após o
> trânsito em julgado da decisão judicial deverá observar a proporcionalidade de valores entre as
> parcelas de natureza salarial e indenizatória deferidas na decisão condenatória e as parcelas
> objeto de acordo. **A proporção não é efetuada em relação aos valores de contribuição
> previdenciária** por ventura apurados nos autos, mas sim, em relação aos **valores das parcelas
> de natureza salarial deferidas na decisão condenatória**."

**D7-12 — duas súmulas, dois regimes, e o elo é temporal.** Súmula 23 (sem proporção) vale
**enquanto não há trânsito em julgado**; OJ 376 (com proporção) vale **depois**. O manual não
escreve a articulação; o único elo é a oração "Enquanto não há trânsito em julgado" da p.153.

Roteiro da OJ 376, 4 partes, `pagina_pdf: 165–168`:

1. "Determinar a proporção entre o total líquido devido ao reclamante e total acordado, dividindo
   o total líquido do acordo pelo valor líquido devido ao reclamante."
2. "Incidir a proporção encontrada sobre as parcelas salariais em valores originais, mês a mês, do
   cálculo homologado para determinar a nova base de cálculo".
3. "Recalcular, mês a mês, os valores de contribuição previdenciária cotas reclamante e
   reclamada, observando [...] os salários de contribuição das épocas próprias e os valores
   recolhidos."
4. "Atualizar os valores devidos com acréscimos moratórios da legislação previdenciária para as
   competências a partir de 05/03/09."

**Na omissão da reclamada**, `pagina_pdf: 164`: "a alternativa é utilizar como parâmetro as
parcelas de natureza salarial e indenizatória constantes no cálculo homologado [...] Todavia,
quando não consta cálculo homologado e o pedido inicial não é líquido, o calculista poderá
solicitar que a reclamada apresente os valores deferidos pela r. sentença ou elaborar os cálculos
de liquidação".

### 5.3 A bifurcação 9.2.8.1 × 9.2.8.2 — e o defeito de remissão

| Subitem | Fato gerador | Recorte |
|---|---|---|
| **9.2.8.1** (p.154) | **pagamento** das parcelas do acordo | título traz "(acordo [...] abrangendo parcelas devidas em relação ao período trabalhado **até 04/03/09**)" |
| **9.2.8.2** (p.157) | **prestação de serviços** | título **sem** recorte simétrico |

**D7-13 — a regra de escolha não está no bloco do acordo.** Não é opção do calculista: decorre da
competência das parcelas (espinha § 2.2). Mas essa frase-chave está na `pagina_pdf: 129`, e o
bloco 9.2.8 só remete genericamente à Súmula 45 (`pagina_pdf: 154`: "deverá ser observada também
a Súmula TRT-3ª Região nº 45 no que se refere ao fato gerador").

**Exceção declarada dentro do 9.2.8.2**, `pagina_pdf: 157`: mesmo sob prestação de serviços, usa-se
a data da homologação "na hipótese de **não reconhecimento de vínculo sem a discriminação do
período** a que se refere a prestação de serviços. Neste caso será adotada como competência a data
da homologação do acordo ou a data do pagamento, se esta última anteceder a primeira (§ 3º, art.
103 da IN/RFB 971/09)."

### 5.4 Rateio — as três regras do 9.2.8.2

`pagina_pdf: 157–158`, literais:

- **com discriminação de parcelas E de meses** — "deverão ser adotados para fins de cálculo da
  contribuição social as alíquotas, critérios de atualização, taxas de juros de mora e multa
  vigentes à época das competências dos meses em que foram prestados os serviços."
- **com período mas sem mês a mês** — "o valor total indicado na ata deverá ser **rateado pelos
  meses de ocorrência efetiva da prestação de serviços**"
- **sem período algum** — "a base de cálculo constante na ata do acordo deverá ser rateada,
  **dividindo-se o seu valor pelo número de meses do período indicado na sentença ou na inicial**,
  limitados ao termo inicial e final do vínculo anotado na CTPS ou reconhecido judicialmente."

**D7-14 — recomposição presumida do salário de contribuição.** `pagina_pdf: 158`, literal:

> "Outra alternativa [...] é a **recomposição dos valores de contribuição previdenciárias
> recolhidos durante o contrato de trabalho, presumindo que a reclamada efetuou o recolhimento
> corretamente**, conforme dispõe o art. 33, § 5º da Lei 8212/91."
>
> "A recomposição é aconselhável, quando houver possibilidade de alteração da alíquota [...] ou
> quando o reclamante já contribuiu pelo teto máximo ou próximo."

É a única saída que o manual dá para a ausência do salário de contribuição nos autos — e é
**presunção declarada**, não dado.

### 5.5 Acordo parcelado

`pagina_pdf: 157`, literal:

> "O total da contribuição social, apurado com os acréscimos moratórios da legislação
> previdenciária até a data da homologação do acordo, poderá ser recolhido em tantas parcelas
> quanto as previstas no acordo, nas mesmas datas e proporcionalmente a cada uma delas, conforme
> art. 43, § 3º da Lei 8212/91. **Embora tal situação não seja usual na Justiça do Trabalho da 3ª
> Região**, visto que o mais comum é iniciar a execução da contribuição social após a quitação das
> parcelas [...] a legislação permite"

Para o acordo parcelado que **atravessa 05/03/09**, `pagina_pdf: 168`:

> "Quando o cálculo abranger competências anteriores à 05/03/09, os valores apurados no período
> serão atualizados com os índices dos débitos trabalhistas até a data do acordo e a partir daí o
> total apurado **será dividido proporcionalmente pelo número de parcelas do acordo**, sendo que
> os valores serão atualizados com juros Selic e multa a partir da data de pagamento de cada uma
> das parcelas"

### 5.6 Acordo sem vínculo — 9.2.9

`pagina_pdf: 171–174`.

| Período | Cota patronal | Cota do prestador |
|---|---|---|
| até fev/00 | 15% | — |
| mar/00 a mar/03 | 20% | — |
| **a partir de 01/04/03** | 20% | **11%**, limitado ao teto |
| Entidade beneficente isenta | — | **20%** |

**D7-15 — não se fala em 31%.** `pagina_pdf: 172`, literal: "Lembrando sempre que os **11%
descontados do contribuinte individual estão limitados ao teto máximo**, não sendo portanto
correto falar em 31%. Entendimento exposto também pela OJ-SDI1-398 do TST."

Fundamento dos 11%, `pagina_pdf: 172`: "de acordo com a Lei 8212/91, art. 30, § 4º é possível a
dedução de até 45% da contribuição patronal do contratante, efetivamente recolhida ou declarada
limitada a 9% do respectivo salário de contribuição."

**Quem NÃO arrecada**, `pagina_pdf: 172`: prestação a pessoa física, a outro contribuinte
individual, a produtor rural pessoa física, ou a missão diplomática — nestes casos o próprio
contribuinte individual recolhe 20%.

**Complementação até o piso**, `pagina_pdf: 172`: "se o total da remuneração mensal recebida for
inferior ao limite mínimo do salário de contribuição [...] o contribuinte individual deverá
recolher **diretamente a complementação** [...] aplicando sobre a parcela complementar a alíquota
de 20%."

**D7-16 — o descumprimento do acordo é irrelevante, e a regra só existe num exemplo.**
`pagina_pdf: 175`, observação da 2ª hipótese: "O fato do acordo ter sido descumprido **não tem
relevância**, tendo em vista que o fato gerador é a prestação de serviço, não importando o
pagamento das parcelas do acordo." Não há enunciado equivalente no corpo de 9.2.9.

---

## 6. IR — metodologia, acordo e PLR

### 6.1 O roteiro do 12-B — 3 passos, `pagina_pdf: 191`

> "1º passo: Apurar a base de cálculo do imposto de renda, somando as parcelas passíveis de
> tributação constantes no cálculo de liquidação e deduzindo o valor da contribuição
> previdenciária."
> "2º passo: Verificar em qual faixa da tabela progressiva mensal está enquadrada a base"
> "3º passo: [...]"
>
> "**VALOR IR = [(BASE DE CÁLCULO X ALÍQUOTA) – PARCELA A DEDUZIR]**"

### 6.2 O roteiro do 12-A — 3 passos enunciados, 5 no exemplo

`pagina_pdf: 193`, literais:

> "1º passo: Apurar a base de cálculo do imposto de renda"
> "2º passo: Verificar o número de meses referente ao rendimento tributável, lembrando que o **13º
> salário representa um mês** e que os meses a serem considerados são **apenas aqueles com
> rendimentos passíveis de incidência** de imposto de renda."
> "3º passo: Verificar em qual faixa da tabela está situado o rendimento tributável"

**D7-17 — os passos 4 e 5 só existem dentro do exemplo.** `pagina_pdf: 196`:

> "4) Multiplicar a parcela a deduzir da faixa em que o rendimento encontra situado pelo número de
> meses referente ao rendimento tributável:"
> "5) Calcular o IR, aplicando sobre o total do rendimento tributável a alíquota encontrada no
> item 03 e do resultado apurado diminuir o valor da parcela a deduzir encontrada no item 04"

**D7-18 — o manual anuncia dois critérios de enquadramento e só enuncia um.** `pagina_pdf: 193`
promete "dois critérios" e descreve apenas o (a), da IN 1500/14: "Multiplicar o valor do limite
máximo de cada faixa da tabela [...] pelo número de meses". O **"critério rápido"** — dividir a
base pelo NM — aparece só nos exemplos: `pagina_pdf: 196`, "b) critério rápido: / Dividir a base
de IR pelo número de meses referente ao RRA, verificando em qual faixa o mesmo está situado."

**D7-19 — a regra de escolha sobre juros na base do IR também é frase de exemplo.**
`pagina_pdf: 195`: "No exemplo, estamos considerando os juros na base de cálculo do imposto de
renda. Todavia, o calculista poderá excluir os juros da base, **se houver determinação judicial
neste sentido**."

### 6.3 IR sobre acordo — 9.3.11

**Regra-mãe**, `pagina_pdf: 201`, literal:

> "O cálculo do imposto de renda é efetuado **sobre cada uma das parcelas do acordo pagas em meses
> distintos**, observando a discriminação das parcelas componentes do acordo e as tabelas para
> apuração do IR vigentes nos meses dos pagamentos. Se não houver discriminação das parcelas que
> compuseram o acordo, o imposto de renda incide sobre o total da avença, conforme dispõe o art.
> 28, §2º da Lei 10.833/03."

**Três portas para o regime do 12-A**, `pagina_pdf: 201`, literais:

> "- a discriminação de todas as parcelas que compuseram o acordo, indicando, de forma
> individualizada o valor, bem como a que título e a qual período se referem;
> - ou a indicação de que as parcelas acordadas referem-se àquelas constantes no pedido inicial ou
> deferidas pela sentença, desde que líquido o pedido ou o comando sentencial;
> - ou a indicação de que a apuração do imposto de renda será efetuada com base nas parcelas
> apuradas em cálculo das partes, peritos ou calculistas do juízo existentes nos autos."

**D7-20 — discriminar salarial × indenizatório não basta para o IR.** `pagina_pdf: 201`: "para
fins de imposto de renda, não basta apenas discriminar o montante entre salarial e indenizatório"
— porque a lógica do IR é a da isenção expressa (espinha § 8).

**Parcelas no mesmo mês somam**, `pagina_pdf: 202`: "As parcelas pagas dentro do mesmo mês deverão
ser somadas para formarem a base de cálculo do IR naquele mês."

**Rateio por parcela**, `pagina_pdf: 202–203`: base e NM são rateados — se as parcelas são
idênticas, divide-se; se variadas, "dividindo o valor da parcela pelo total do acordo e
multiplicando pela base de IR" (e idem para o NM). **É aqui que o NM vira fracionário** (8,5; 5,6;
2,4 nos exemplos).

**D7-21 — o travamento pelo cálculo homologado.** `pagina_pdf: 202`: "consta em alguns termos de
acordo que o valor do imposto de renda será recolhido, conforme cálculo homologado. Quando ocorre
esta situação, **não há como alterar o valor do imposto de renda apurado**."

### 6.4 PLR — 9.3.10, `pagina_pdf: 199–201`

**Regime próprio, tabela própria, sem NM.** Literal, `pagina_pdf: 199`:

> "Os valores percebidos a título de participação nos lucros ou resultados são tributados
> **exclusivamente na fonte, em separado dos demais rendimentos e com base em tabela progressiva
> anual específica**."
>
> "A base de cálculo constitui no valor total apurado a título de PLR encontrado nos cálculos de
> liquidação, **sem qualquer divisão pelo número de meses**"

E `pagina_pdf: 191`: "Os rendimentos referentes à participação nos lucros ou resultados **não estão
submetidos ao regime especial** de tributação do art. 12-A da Lei 7713/88."

**Lançamento separado**, `pagina_pdf: 200`: "não devendo ser somado ao imposto de renda apurado
sobre os demais rendimentos, tendo em vista que o imposto incidente sobre a PLR tem base de
cálculo, tributação e **código de recolhimento diferentes**."

**D7-22 — e ainda assim o TRT-3 usa o código genérico.** `pagina_pdf: 201`, literal:

> "Foi utilizado o código **5936** - IRRF - REND DECOR DEC JUSTIÇA TRABALHO, EXCETO ART 12A L.
> 7.713/88 para recolhimento PLR e **não o código específico 3562** [...] tendo em vista que o valor
> de participação nos lucros ou resultados será pago em decorrência de uma decisão da Justiça do
> Trabalho e não no decorrer do pacto laboral."

Opção declarada do tribunal, contra o código próprio da RFB.

### 6.5 IR em atraso — 9.3.13, `pagina_pdf: 207`

> "- juros de mora calculados à taxa SELIC, acumulada mensalmente a partir do primeiro dia do mês
> subsequente ao vencimento do prazo até o mês anterior ao do pagamento e de 1% no mês do
> pagamento.
> - multa de 0,33% (trinta e três centésimos) ao dia, limitada a 20%, calculada a partir do
> primeiro dia subsequente ao do vencimento do prazo previsto para o pagamento do tributo."

**D7-23 — o vencimento do IR é dia 20, e a regra está numa "Obs." de exemplo.**
`pagina_pdf: 208`: "tendo em vista que **o vencimento para recolhimento do IR é o dia 20 do mês
subsequente ao pagamento**." Sem ela não se conta juros nem multa.

**9.3.12 é uma frase.** `pagina_pdf: 207`, integral: "O cálculo do imposto de renda proporcional
ao valor pago será detalhado no item 10.2." Remissão **válida** — 10.2 existe na p.223, fora
deste bloco.

---

## 7. Competências anteriores a jan/80 — 9.2.11

`pagina_pdf: 176–179`. Motivo declarado: "A Secretaria da Receita Federal do Brasil e a
Previdência Social divulgam, atualmente, a tabela prática [...] **apenas a partir da competência
jan/80**."

Roteiro literal, `pagina_pdf: 176–177`, resumido em fórmula:

```
2)  valor_real      = INSS_originário / 2.750.000.000.000
3)  corr_monetária   = (INSS_originário × coef_UFIR) × 0,9108 − valor_real
4)  %juros           = %juros_tabela_I(competência) + %juros_jan/80(tabela prática vigente)
5.1) até set/79      → juros = valor_real × %juros
5.2) out/79 a dez/94 → juros = (valor_real + corr_monetária) × %juros
6)  multa            = 50% sobre (valor_real + corr_monetária)
7)  total            = itens 2 + 3 + 5 + 6
```

**D7-24 — a base dos juros muda em out/79.** Nota literal, `pagina_pdf: 179`: "Até a competência
set/79, os juros incidiam sobre o valor originário, a partir de out/79 a dez/94, os juros incidem
sobre o **valor atualizado**." É um corte próprio, e antecede todo o resto do capítulo.

**D7-25 — três datas de referência no mesmo exemplo.** O roteiro (p.177) manda usar a tabela
prática "vigente no mês da atualização do cálculo"; a nota do exemplo (p.179) diz que usou a de
**dezembro/09**; e o resumo do mesmo exemplo é rotulado "Total contribuição previdenciária até
**abril/12**". Três datas, sem conciliação. Registrado, não corrigido.

**D7-26 — a Tabela I termina em dez/79, e o exemplo usa jan/80.** Conferido: `jan/80` **não
aparece** na Tabela I (p.178), que vai de ago/64 a dez/79 — 185 competências, sem lacuna. No
exemplo, a linha jan/80 usa o coeficiente de dez/79 (`0,00194635`) e 0% de juros. A extensão é
**inferência do exemplo**, não da tabela.

---

## 8. Os defeitos do original — índice

**Trinta e um** achados, todos **registrados e não corrigidos**, conforme a regra do projeto.

Numeração própria `E7-nn`. Os rótulos `D7-nn` que aparecem no corpo deste documento numeram
**achados em geral** — regras, observações e defeitos —, e só quatro deles são defeitos; daí a
numeração separada. A primeira redação desta seção dizia "vinte e seis", que era a contagem dos
`D7`, não a das linhas desta tabela. Corrigido pela validação adversarial.

| # | Defeito | `pagina_pdf` |
|---|---|---|
| E7-01 · D7-04 | Rateio de mar/09 com mês comercial de 30 dias num mês de 31 | 135–136 |
| E7-02 · D7-05 | **Dois subitens numerados 9.2.7.3**; não existe 9.2.7.4 | 140, 145 |
| E7-03 · D7-25 | Três datas de referência no exemplo do pré-1980 | 177, 179 |
| E7-04 · D7-26 | Tabela I termina em dez/79; exemplo usa jan/80 | 178–179 |
| E7-05 | Parêntese que fecha sem abrir no título do 9.2.7.3-B | 145 |
| E7-06 | Barra "/" solta ao fim do § do art. 276, § 3º | 154 |
| E7-07 | "Lei 11.457/**06**" — a lei que acrescentou o § 6º ao art. 832 da CLT é de 2007 | 154 |
| E7-08 | Item 5 do roteiro remete ao próprio item 5 (autorreferência) | 143 |
| E7-09 | Incisos rotulados b.2/b.3/b.4 remetendo a "itens 2, 3 e 4" | 146 |
| E7-10 | 2º roteiro do 9.2.9: passo 2 manda aplicar sobre "os valores apurados no item 2" (circular) | 174 |
| E7-11 | Rótulo "g) Totalização" numa hipótese sem itens a)–f) | 153 |
| E7-12 | Exemplo 2 do 9.2.8.1 com três pares de alíquotas incompatíveis (8%/22% e 11%/21%) | 156–157 |
| E7-13 | Mesmo exemplo usa 0,08 contrariando a observação que diz não se aplicar mais a mínima | 155–156 |
| E7-14 | "parcelas apenas parcelas anteriores a 04/03/09" | 155 |
| E7-15 | Duas hipóteses com os mesmos números e competências diferentes (out/15 × out/11) | 174–175 |
| E7-16 | "atualizados até junho/**05**" em exemplo de acordo de 2015 | 170 |
| E7-17 | "7.7430,08" — número malformado | 167 |
| E7-18 | Totais divergentes no mesmo exemplo: 477,95 apurado, 477,73 totalizado | 138 |
| E7-19 | INSS cota reclamada do Exemplo 3 grafado **205,61** e **205,51**. `205,61` nas pp. **136, 137, 147, 150, 152, 153**; `205,51` nas pp. **147 e 149**. A p.147 traz **os dois**, e a p.149 traz 205,51 na mesma linha da mesma planilha em que a p.152 traz 205,61 | 136–153 |
| E7-20 | Selic escrita como 3,22% com resultado compatível com 4,28% | 141 |
| E7-21 | Base do IR: texto conclui 6.904,03, linha seguinte calcula com 6.904,93 | 192 |
| E7-22 | "142,7985 x 16 meses = 20.992,90" — valor copiado do exemplo anterior | 196 |
| E7-23 | Principal 45.115,88 e juros calculados sobre 45.114,88 | 198–199 |
| E7-24 | "2.260,00 **x** 5,5 = 410,91" — operador de divisão escrito como multiplicação | 205 |
| E7-25 | "**6.0000,00** / 20.000,00 x 8 = 2,4" | 207 |
| E7-26 | Total 72,50 quando a tabela soma 73,50 | 208 |
| E7-27 | Remissão de 9.3.11 ao "tópico 9.3.3"; a regra citada está em **9.3.2** | 201 |
| E7-28 | Remissão da p.146 ao "tópico 9.2.7.3" para exemplo que está em 9.2.7.1 | 146 |
| E7-29 | Tabela RRA com fim de vigência em branco ("a partir de abril/15 a ........") em 5 ocorrências | 194, 195, 198, 205, 206 |
| E7-30 | "serão considerados apenas os meses **em foram apurados**" | 188 |
| E7-31 | Parêntese aberto e não fechado no § das deduções | 188 |

---

## 9. Regras que só existem dentro de exemplos

O padrão mais persistente do capítulo. Sete ocorrências. Nenhuma tem enunciado normativo.

| # | Regra | Onde aparece |
|---|---|---|
| 1 | **Rateio do mês de mar/09** entre TR e Selic | Obs. do Exemplo 3, p.135–136 |
| 2 | **13º como base autônoma no INSS** | só nas planilhas, p.131, 133, 135, 144 |
| 3 | **Tabela vigente na data do cálculo**, não do pagamento, no acordo sem discriminação | Obs. 1 do Exemplo 1, p.155 |
| 4 | **Irrelevância do descumprimento do acordo** para o fato gerador | Obs. 2 da 2ª hipótese, p.175 |
| 5 | **Recálculo do IR na virada do ano-calendário** (12-B → 12-A) | "Observações" do Exemplo 1, p.193 |
| 6 | **Passos 4 e 5 do 12-A** e o **"critério rápido"** de enquadramento | p.196 |
| 7 | **Vencimento do IR no dia 20** do mês subsequente ao pagamento | Obs. de tabela, p.208 |

**Dois deles são estruturais**: o item 2 e o item 7. Sem o 13º como base autônoma, a cota do
empregado sai errada em todo cálculo com 13º; sem o dia 20, juros e multa do IR não se contam.
