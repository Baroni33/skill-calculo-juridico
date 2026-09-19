# Bloco 7 — relatório

Descontos legais: previdenciário e fiscal. Capítulo 9 do Manual TRT-3 (2016),
**páginas 107 a 208** do PDF. Offset de paginação **0**, confirmado nas bordas.

**O maior bloco do manual:** 351.605 caracteres, 102 páginas, **47 itens numerados**.

Nenhuma skill escrita.

| Entrega | Situação |
|---|---|
| `bloco-07-descontos.md` — espinha (A) | **Feita** — 35 regras numeradas |
| `bloco-07-descontos-detalhe.md` — detalhe | **Feito** — roteiros, acordo, IR, pré-1980, **31 defeitos** |
| Séries (B) `OUT_OF_SCOPE` | **Feita** — 1 série nova, 185 linhas. Ver § 4 |
| Cruzamento com 18.1 | **Feito** — e rendeu divergência. Ver § 3 |
| Cruzamento com o bloco 6 (jan/2010) | **Feito** — e a resposta é negativa. Ver § 2 |
| Marcas Fase 4 | **Feitas** — 12 marcas |

**Cobertura: integral.** Os 47 itens foram lidos. Não parei em limite de item.

---

## 1. O achado central: três eixos temporais dentro de um desconto só

O enunciado pedia fato gerador, regime de competência × caixa, responsabilidade. O capítulo
entrega isso — e entrega mais do que um corte.

O **corte de 05/03/2009** (MP 449/08 → Lei 11.941/09, Súmula 45 do TRT-3, TST Pleno
`E-RR-1125-36.2010.5.06.0171` de 20/10/2015) divide caixa de competência. Mas **dentro** do
regime de competência o Pleno do TST cindiu as rubricas, e cada uma tem marco inicial próprio:

| O quê | Desde | Sobre quem |
|---|---|---|
| Atualização monetária | prestação do serviço | reclamante **e** reclamada |
| Juros de mora | prestação do serviço | **só** a reclamada |
| **Multa** | **exaurimento do prazo de citação** | **só** a reclamada |

E há um quarto eixo, que não é nenhum dos três: o **FAP** produz efeitos "a partir do primeiro
dia do quarto mês subsequente ao de sua divulgação" (`pagina_pdf: 109`). Divulgação mais quatro
meses — não é competência, não é fato gerador, não é pagamento.

Isso confirma, com dado novo, a tese do bloco 6: **o eixo de corte não é único**, e aqui há
quatro dentro de um único desconto.

### O que a granularidade faz com isso

O corte é **ao dia**: 05/03/2009. A apuração é **mensal**. Março de 2009 fica dos dois lados —
exatamente o caso que o bloco 6 modelou como `competencia-atravessa-o-corte`.

O manual resolve **rateando**, e a regra **só existe dentro de um exemplo** (`pagina_pdf:
135–136`): `52,81/30 × 4` para o bloco TR e `52,81/30 × 26` para o bloco Selic. **Mês comercial
de 30 dias num mês de 31.** Registrado, não corrigido.

É um dado relevante para a camada de regimes: o corpus **tem** uma convenção de rateio, e ela é
aritmeticamente inexata. O bloco 6 recusa competências que atravessam o corte; este capítulo
mostra o que a prática faz no lugar.

---

## 2. As duas portarias de janeiro de 2010 — a resposta é negativa

O enunciado mandou: *"O bloco 1 registrou duas portarias simultaneamente vigentes para janeiro de
2010, com eixo de corte pela data do cálculo. Confirme como o capítulo 9 trata isso e cruze com o
regime já modelado no bloco 6."*

**O capítulo 9 não trata disso. Em nenhum lugar.** Verificado por varredura no texto integral das
102 páginas: `350/09` e `333/10` **não ocorrem**; "portaria" aparece **duas vezes** no capítulo
inteiro, e ambas são citações de regimento interno da RFB dentro de atos declaratórios
transcritos (`pagina_pdf: 183`), sem relação com faixas de contribuição.

O regime `pr.faixas-inss-jan2010` do bloco 6 vem do **item 18.7** (capítulo 18), e continua sendo
o único ponto do corpus com eixo `data-do-calculo`. **O capítulo 9 não o confirma nem o
contradiz — cala.**

### Mas o capítulo 9 tem um problema de duas tabelas, e é outro

Item **9.2.6**, `pagina_pdf: 123–128`, um tópico inteiro dedicado a isso. Duas tabelas de Selic,
ambas da Receita Federal, **deslocadas em um mês**:

| Tabela | Para quê | Taxa alocada em |
|---|---|---|
| Tabela prática para contribuições em atraso | INSS | o **próprio mês de competência** |
| Taxa de Juros Selic – Acumulados | tributos federais, IR | o **mês do vencimento** do prazo |

Literal, `pagina_pdf: 124`: atualizar a competência jan/10 usa a linha de **jan/10** na primeira
tabela e a de **fevereiro/10** na segunda.

**Não é o mesmo fenômeno das portarias.** Ali eram duas normas concorrentes para a mesma
competência, decididas pela data do cálculo. Aqui é **uma norma só, apresentada em duas
convenções de indexação**. As duas tabelas dão o mesmo número; errar é ler a linha errada.

E há um segundo laço: a tabela prática **já embute 1% de juros**. Reatualizar um cálculo que já
tem Selic sem subtrair esse 1% **conta juros duas vezes** — o manual diz isso com todas as letras
(`pagina_pdf: 126`).

**Achado para a camada de regimes:** isto não é regime temporal nem parâmetro negociável. É
**convenção de indexação de série** — uma terceira categoria, que nenhuma das duas camadas
modeladas cobre. Registrado como pendência de modelagem **P7-M1**.

---

## 3. O cruzamento com o item 18.1 — e a divergência que ele revelou

O enunciado: *"Cruzar a matriz de incidência do capítulo 9 com a de 18.1. Divergência entre as
duas é achado, não erro a harmonizar."*

### 3.1 Primeiro achado: o capítulo 9 não tem matriz de incidência do INSS

O capítulo 9 **nunca enumera** quais parcelas sofrem INSS. Fala sempre em "parcelas de natureza
salarial" (`pagina_pdf: 128`) e "parcelas passíveis de incidência" (`pagina_pdf: 109`). A matriz
existe **só no item 18.1** (p.373–380), extraída no bloco 1 — 44 parcelas × INSS/FGTS/IRRF, com
fundamento por coluna.

**Não há divergência porque não há duas matrizes.** O capítulo 9 delega, sem dizer que delega.

### 3.2 Segundo achado: o capítulo 9 TEM uma lista de IR — e o cruzamento pegou o 18.1

O item **9.3.2** (`pagina_pdf: 180`) traz uma lista de verbas não tributáveis. Cruzada com a
coluna IRRF de 18.1, dois pontos de atrito:

| Verba | 9.3.2 (p.180) | 18.1 (p.373–380) |
|---|---|---|
| **Diárias** | "diárias destinadas a cobrir despesas c/ alimentação e pousada" — não tributável, sem ressalva | **duas linhas de IRRF**: até 50% da remuneração → não; acima de 50% → **sim** |
| Indenização citada | "indenização da Lei **6.708/89**" | "Indenização adicional (Lei **7238/84**, art. 9º)" |

**Correção da primeira redação deste relatório.** Eu havia registrado a linha das diárias como
divergência material entre o capítulo 9 e o item 18.1. **A validação adversarial mostrou que não
é.** A nota da própria tabela 18.1 diz, literal:

> "Para fins previdenciários, ver Lei 8212/91 e Dec. 3048/99, que fixam o limite de 50% em função
> da remuneração e não do salário. **Para fins de incidência de IR, não há limite** desde que
> destinadas, exclusivamente, ao pagamento de despesas de alimentação e pousada, por serviço
> eventual realizado em município diferente do da sede de trabalho (Solução de Consulta Cosit n.
> 73, de 31 de dezembro de 2013)."

O corte de 50% é **previdenciário**. Para o IR **não há limite** — e é exatamente o que o
capítulo 9 diz.

O achado, portanto, **não é divergência entre os dois; é contradição interna do 18.1**: a
estrutura de duas linhas marca `IRRF = sim` na faixa acima de 50%, enquanto a nota da mesma
tabela afirma que para o IR não há limite. O capítulo 9 concorda com a **nota**, não com a
**linha**. E é a linha que um motor leria.

A segunda linha permanece: divergência de citação, e "Lei 6.708/**89**" é suspeita em si — a Lei
6.708 é de 1979. Registrado, **não corrigido**.

### 3.3 Terceiro achado, e o mais pesado: juros de mora

| | Veredito | Fundamento citado |
|---|---|---|
| **18.1** (p.373–380) | IRRF **= SIM**, categórico | "IN/RFB 1500/14, art. 36, § 2º, e art. **62, § 5º, inciso I**" |
| **9.3.3** (p.180–182) | "apenas deverão ser **excluídos** [...] se houver decisões nos autos neste sentido **ou se pagas no contexto da rescisão** do contrato de trabalho" | IN/RFB 1500/14, art. **62, § 3º, II, "a"**; Cosit 13/2016; OJ 400/SDI-I |

As duas partes do mesmo manual citam **parágrafos diferentes do mesmo artigo 62** e chegam a
resultados opostos. O § 3º é a dispensa; o § 5º é a exceção à dispensa (juros na continuidade do
contrato). **18.1 escolheu o § 5º e gravou "sim"; 9.3.3 desenvolve o § 3º e conclui pela
exclusão.**

Não é erro de uma das duas: é a mesma norma lida de dois pontos. Mas **a tabela não tem a linha
"não"**, e é a tabela que um motor consultaria. Em cálculo trabalhista os juros de mora são
parcela grande — a divergência move dinheiro.

**Achado, não harmonizado.** Registrado aqui, em `bloco-07-descontos.md` § 8.3 e como pendência
**P7-02**.

### 3.4 O que confere

Conferidos um a um contra 18.1, sem divergência: férias + 1/3 indenizadas na rescisão (IRRF não);
abono pecuniário (não); danos morais (não); aviso-prévio indenizado (IRRF não, INSS sim);
multa de 40% do FGTS (não); PLR (IRRF sim, INSS não); honorários sucumbenciais (IRRF sim, INSS
não).

---

## 4. A bifurcação (A)/(B) — e por que ela saiu tão assimétrica

O enunciado deu o critério: **"se muda quando o governo publica portaria, é (B). Se muda quando
muda a lei ou a jurisprudência, é (A)."** Aplicado com rigor, o resultado surpreende:

**Quase todo o capítulo 9 é (A).** As alíquotas previdenciárias (20%, 22,5%, 15%, 11%, 8,8%), os
percentuais de multa por competência (50% → 10% → 40% → 4/7/10% → 8/14/20% → 0,33%/dia), a regra
do FAP, os graus de risco — tudo está em **lei**, não em portaria. Pelo critério do enunciado,
são conceito.

O que é genuinamente (B) — as **tabelas de faixas** — **não mora no capítulo 9**. Está no
capítulo 18, extraído no bloco 1. O capítulo 9 apenas remete: "de acordo com as tabelas vigentes
nas épocas próprias constantes nos **anexos deste manual**" (`pagina_pdf: 130`).

Uma série nova foi extraída:

| Arquivo | Item | Linhas | Cobertura | `pagina_pdf` |
|---|---|---:|---|---|
| `serie-9.2.11-ufir-juros-ate-dez79.csv` | 9.2.11 | **185** | ago/64 a dez/79, sem lacuna | 178 |

Conferida mês a mês: 185 competências contíguas. **`jan/80` não está na Tabela I** — o exemplo da
p.179 o usa com o coeficiente de dez/79, por extensão não declarada.

As tabelas de Selic reproduzidas nas pp.123–128 **não foram re-extraídas**: são as mesmas do item
18.15, já em `serie-18.15-*.csv`.

---

## 5. A progressividade — respondida, e com data de validade

O enunciado: *"verificar se o manual aplica alíquota sobre faixa ou sobre o total, e se isso muda
por período."*

**Alíquota única sobre o total.** Literal, `pagina_pdf: 130`: "estabelecer uma nova alíquota e
apurar a contribuição social devida, respeitando o teto máximo de contribuição da época."
Confirmado pela aritmética de três exemplos: 951,99 × 9% ; 1.085,60 × 8% ; 1.675,98 × 11%.

**E não muda por período dentro do manual** — o critério é o mesmo em 2008, 2009 e 2013/14.

Mas muda **depois** dele: a **EC 103/2019** instituiu alíquotas progressivas **por faixa** para o
segurado empregado a partir de **01/03/2020**. É a marca **F7-01**, e é a de maior impacto do
bloco: altera a aritmética de toda cota do empregado em competências recentes. **Marcada, não
confrontada** — a base normativa do repositório não cobre descontos.

---

## 6. O padrão mais persistente: regras que só existem dentro de exemplos

Sete ocorrências, nenhuma com enunciado normativo:

| # | Regra | Onde |
|---|---|---|
| 1 | Rateio do mês de mar/09 entre TR e Selic | Obs. de exemplo, p.135–136 |
| 2 | **13º salário como base autônoma no INSS** | só nas planilhas, p.131, 133, 135, 144 |
| 3 | Tabela vigente na data do cálculo (acordo sem discriminação) | Obs. 1, p.155 |
| 4 | Irrelevância do descumprimento do acordo para o fato gerador | Obs. 2, p.175 |
| 5 | Recálculo do IR na virada do ano (12-B → 12-A) | "Observações", p.193 |
| 6 | Passos 4 e 5 do 12-A e o "critério rápido" de enquadramento | p.196 |
| 7 | **Vencimento do IR no dia 20** do mês subsequente ao pagamento | Obs. de tabela, p.208 |

**Dois são estruturais.** Sem o item 2, a cota do empregado sai errada em todo cálculo com 13º —
e note a inversão: no **INSS** o 13º é base separada (só por planilha); no **IR sob o art. 12-A**
ele expressamente **não** é tributado em separado (`pagina_pdf: 188`, com enunciado). Sem o item
7, juros e multa do IR não se contam.

Um motor que leia só os enunciados normativos do capítulo **não calcula**.

---

## 7. Defeitos do original

**Trinta e um**, todos registrados e **nenhum corrigido**. Índice completo em
`bloco-07-descontos-detalhe.md` § 8, numerados `E7-01` a `E7-31`. Os que importam para quem for implementar:

1. **Dois subitens numerados 9.2.7.3** (pp.140 e 145), sem 9.2.7.4. Toda remissão a "9.2.7.3" é
   ambígua. Aqui são chamados **9.2.7.3-A** e **9.2.7.3-B**.
2. **Rateio de mar/09 com divisor 30 num mês de 31 dias** (p.135–136).
3. **Mesmo valor grafado 205,61 e 205,51** — `205,61` nas pp.136, 137, 147, 150, 152, 153; `205,51` nas pp.147 e 149. A p.147 traz os dois.
4. Quatro remissões cruzadas quebradas ou circulares (pp.143, 146, 174, 201).
5. Um exemplo com três pares de alíquotas incompatíveis entre si (pp.156–157).
6. Seis erros aritméticos ou tipográficos em números usados no passo seguinte.

---

## 8. Pendências

| # | Pendência | Efeito |
|---|---|---|
| **P7-01** | Ordem de imputação do recolhimento parcial: o manual dá um padrão — "geralmente, o abatimento ocorre primeiro em relação às competências mais antigas" — e **duas alternativas**, sem critério de escolha | p.152–153. E convive com uma segunda ordem, proporcional entre rubricas, em 9.2.7.3-A (p.143) |
| **P7-02** | **Juros de mora na base do IR** — 18.1 diz "sim", 9.3.3 conclui pela exclusão em duas hipóteses | § 3.3 |
| **P7-03** | **Diárias** — contradição **interna ao 18.1**: a linha marca `IRRF = sim` acima de 50%, a nota da mesma tabela diz que "para fins de incidência de IR, não há limite". O capítulo 9 concorda com a nota | § 3.2 |
| **P7-04** | **13º como base autônoma no INSS** não tem enunciado; existe só em planilha | estrutural |
| **P7-05** | **Termo inicial da multa quando há citação** — o manual diz "após o vencimento do prazo de citação" mas nunca define qual prazo | p.129 vs pp.138, 141 |
| **P7-06** | **Multa sobre a cota do reclamante** — os exemplos a aplicam; não há enunciado justificando | pp.138, 141, 149 |
| **P7-07** | **Ausência do salário de contribuição nos autos** — a saída é a "recomposição dos valores de contribuição previdenciárias recolhidos durante o contrato de trabalho, **presumindo que a reclamada efetuou o recolhimento corretamente**" (p.158). É presunção declarada, não dado |
| **P7-08** | **Honorários advocatícios** não aparecem como dedução da base do IR em lugar nenhum do capítulo 9 |
| **P7-09** | **RRA por ano-calendário** — não há regra de segregação anual; os exemplos usam NM único atravessando anos |
| **P7-10** | **Arredondamento e casas decimais** — não tratados em nenhum ponto do capítulo |
| **P7-11** | **Parecer Cosit nº 25** (desoneração) — remetido "nos anexos deste manual" sem número nem página |
| **P7-12** | Súmulas 45 e 23 do TRT-3 e OJs 368 e 376 são **citadas sem transcrição** (a OJ 398, por contraste, é transcrita) |
| **P7-M1** | **Modelagem:** convenção de indexação de série (as duas tabelas de Selic) não é regime temporal nem parâmetro negociável. Nenhuma das duas camadas a cobre | § 2 |

---

## 9. Marcas Fase 4

Doze, todas **apenas marcadas**. A base normativa do repositório **não cobre descontos** — é
lacuna declarada de `00-base-normativa.md`, e este bloco a confirma. Tabela completa em
`bloco-07-descontos.md` § 13.

As três de maior impacto:

- **F7-01 — EC 103/2019.** Alíquotas progressivas por faixa desde 01/03/2020. Derruba o critério
  de alíquota única sobre o total para competências recentes.
- **F7-04 — ADC 58/59 e ADIs 5867/6021.** Alcança **todo** ponto do capítulo que diga "mesmos
  índices de atualização do débito trabalhista" — e são muitos: o regime de caixa inteiro depende
  disso.
- **F7-03 — Tema 808 do STF.** O manual registra a repercussão geral do RE 855091 e diz
  expressamente que "a questão não está resolvida" (p.181). Foi resolvida depois.

---

## 10. O que este bloco entrega, e o que não

**Entrega:** a espinha conceitual dos dois descontos, com fato gerador, regimes, responsabilidades
segregadas, roteiros de apuração mês a mês, tratamento do acordo com e sem vínculo, os dois
regimes do IR, o número de meses, e os cruzamentos pedidos.

**Não entrega, por decisão:**

- **harmonização** entre 18.1 e o capítulo 9 — as divergências ficaram como achado;
- **confronto** com norma posterior a 2016 — só marcação;
- **correção** dos 31 defeitos do original;
- as **faixas**, que são (B) e moram no capítulo 18;
- o **item 10.2**, destino da remissão de 9.3.12 (IR proporcional ao valor pago) — está na p.223,
  fora deste recorte. É o próximo bloco natural.

---

## 11. O que a validação adversarial verificou, e o que derrubou

O enunciado exigiu verificação específica de citação literal, "o defeito recorrente dos blocos 5
e 6". Foi feita por script sobre o PDF: **104 citações literais extraídas e conferidas uma a uma**,
com normalização de espaços, quebras de linha e aspas tipográficas antes da comparação.

**Nenhuma citação inventada.** 101 das 104 batem exatamente com o texto do PDF na página
atribuída; as três restantes são compressões de texto que existe. **Zero `NAO-ENCONTRADA`, zero
página errada entre as citações.** O defeito dos blocos 5 e 6 não se repetiu.

### O que ela derrubou

| # | Erro | Correção |
|---|---|---|
| 1 | **Contagem de defeitos.** Três números em circulação: "26" (relatório), "22" (espinha), 31 (real) | São **31**, numerados `E7-01` a `E7-31`. O "26" era a contagem dos rótulos `D7`, que numeram achados em geral e não só defeitos |
| 2 | **"4,28%"** citado como um dos pares de conferência do item 9.2.6 | O número é real, mas é dos exemplos de **9.2.7.3**; não ocorre nas pp.123–128. O par correto é **13,07%** |
| 3 | **Páginas do defeito 205,61 × 205,51** | `205,61` em 136, 137, 147, 150, 152, 153; `205,51` em 147 e 149. A p.149 faltava e a moldura "três páginas / uma quarta" não descrevia o achado |
| 4 | **"mesmos índices do débito trabalhista"** entre aspas | Não existe nessa forma. É "mesmos índices **de atualização** do débito trabalhista" |
| 5 | **Citação da P7-07** comprimida e com palavra trocada ("recolheu" por "efetuou o recolhimento") | Restaurada literal |
| 6 | **A divergência das diárias** | **Superdimensionada.** Não é divergência entre 18.1 e o capítulo 9; é contradição interna do 18.1 — ver § 3.2 |
| 7 | Elisão sem reticências na P7-01; atribuições de página que deveriam ser intervalo (117–118, 152–153); "RE 855.091" onde o manual grafa "855091" | Corrigidos |

### O que resistiu

- **A série** `serie-9.2.11-ufir-juros-ate-dez79.csv`: as **185 linhas** foram confrontadas
  exaustivamente contra a p.178 — competência, coeficiente e percentual de juros. **Zero
  divergências, zero lacunas.** E `jan/80` corretamente ausente da Tabela I, corretamente
  identificado na p.179 com o coeficiente herdado de dez/79.
- **Dez dos onze números estruturais**, incluindo 351.605 caracteres, 102 páginas, 47 itens (com
  a duplicata de 9.2.7.3 corretamente absorvida), 44 parcelas, 185 linhas, 35 regras, 12 marcas,
  13 pendências.
- **A varredura negativa do § 2**, inclusive o número de ocorrências de "portaria" (duas), a
  página (183) e a natureza (fórmula de regimento interno da RFB).
- **Toda a aritmética citada**, e todos os números nas páginas indicadas.
- **O cruzamento com 18.1 nos cinco pontos** conferidos, inclusive a citação do `art. 62, § 5º,
  inciso I`, que casa literalmente com o JSON.
- **As três afirmações negativas.** A do arredondamento é absoluta: `arredond`, `truncar`,
  `casas decimais`, `centavos`, `aproximação` — **zero ocorrências em 102 páginas**.
- **15 dos 16 defeitos amostrados** confirmados na página indicada.

