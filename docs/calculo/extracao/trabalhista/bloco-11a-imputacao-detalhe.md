# Bloco 11A — detalhe

Companheiro de `bloco-11a-imputacao.md`. Material bruto conferido do **item 10.1**.
Gerado por script a partir de `cap10_1.json`. **Offset de paginação zero.**

---

## 1. Estrutura real do item 10.1

- **Faixa real:** pp.209 a 223 (10.1 termina no offset 2658 da p.223)
- **Faixa extraída por ordem:** pp.209-222

### Premissas do enunciado, conferidas

- **'Exemplo de atualizacao simples sem descontos previdenciarios ou fiscais' na p.209** → 
- **'Exemplo de atualizacao simples com juros vincendos' na p.210** → 
- **'Exemplo de atualizacao de calculo apresentado...' na p.213** → 
- **lista completa** → 
- **10.2 comeca na p.223 / parar na 222** → 

### Blocos

| Bloco | Natureza | `pagina_pdf` |
|---|---|---|
|  |  | 209 |
|  | unico bloco do item que compara duas ordens de operacao lado a lado | 209; 210 |
|  |  | 210 |
|  |  | 210; 211 |
|  |  | 211; 212 |
|  |  | 212; 213 |
|  |  | 213; 214 |
|  |  | 213; 214; 215 |
|  |  | 215; 216; 217 |
|  |  | 217; 218; 219; 220 |
|  |  | 220; 221; 222; 223 |

## 2. Ordem das operações

### Sequência canônica

1. 1. CORRIGIR o principal (total devido ao recte SEM juros) pelo indice acumulado a partir do 1o dia apos a data final da ultima atualizacao.
2. 2. APLICAR OS JUROS SOBRE O PRINCIPAL JA CORRIGIDO (nunca sobre o nominal).
3. 3. SOMAR principal corrigido + juros = total BRUTO.
4. 4. ATUALIZAR o INSS cota recte e cota recda ja apurados (multiplicacao pelo mesmo indice do debito; ou, se o fato gerador for a prestacao de servicos, pelos indices da legislacao previdenciaria).
5. 5. REFAZER a base de IR: corrigir a base SEM juros pelo mesmo indice, aplicar (ou nao) os juros sobre ela, e DEDUZIR o INSS ja corrigido.
6. 6. CALCULAR o IR sobre a base do passo 5 com a tabela vigente na DATA FINAL da atualizacao.
7. 7. LIQUIDO = bruto - INSS cota recte - IR.
8. 8/9. Despesas processuais.

### Sobre o que os juros incidem

- **resposta:** SOBRE O PRINCIPAL CORRIGIDO, sempre. Nunca sobre o principal nominal.
- **evidencia literal p209:** a) aplicar o percentual/índice desde a propositura da ação sobre o valor corrigido
- **evidencia literal p210 criterio b:** 2 - aplicar sobre o principal corrigido o percentual de  juros contados entre a data da atualização do último cálculo  até  e a data final de atualização
- **prova aritmetica:** p.209: 4.066,41 x 31,266667% = 1.271,43 (nominal) vs 4.169,65 x 31,266667% = 1.303,71 (corrigido). O manual imprime 1.303,71. Delta = 32,28.
- **prova p215:** Passo 2 declara 'Vr. Principal corrigido x % juros'; 2.832,71 x 110,70% = 3.135,81 = valor impresso.
- **prova cap7 p96:** Vr. Juros = Vr. Atualiz. x %juros (ex.: 314,96 x 9,20% = 28,98, impresso 28,98; sobre o nominal 309,75 daria 28,50).

### Os dois critérios de juros

- **criterio a literal:** a) aplicar o percentual/índice desde a propositura da ação sobre o valor corrigido
- **criterio b literal:** b) 1 - atualizar o total dos juros  apurado no último cálculo com o mesmo índice de correção    utilizado para corrigir o principal até data final de atualização;     2 - aplicar sobre o principal corrigido o percentual de  juros contados entre a data da atualização do último cálculo  até  e a data final de atualização;     3 - O valor encontrado no item 02 deverá ser somado ao valor apurado no item 01 para obter o…
- **afirmacao do manual:** Quando o cálculo não envolver juros vincendos, o calculista poderá optar por qualquer um dos dois critérios, visto que os resultados finais são idênticos.
- **teste numerico:** a: 4.169,65 x 31,266667% = 1.303,71. b: 580,14 x 1,02538895 = 594,87 mais 4.169,65 x 17% = 708,84; soma 1.303,71. IDENTICOS ate o centavo. Total bruto 5.473,36 nos dois. AFIRMACAO DO MANUAL CONFIRMADA.
- **razao algebrica:** 594,87 = 4.169,65 x 14,26667% (a taxa antiga preservada sobre o principal ja corrigido) e 14,26667% + 17% = 31,26667%. A identidade so vale porque (i) o mesmo indice corrige principal e juros e (ii) a taxa e uniforme em todas as linhas.

### A ordem altera o resultado?

- **resposta:** NAO, quando ha um unico indice de correcao e uma unica taxa de juros - e o caso de todos os exemplos de 10.1.
- **teste 1 p209:** Ordem do manual: (4.066,41 x 1,02538895) + (4.066,41 x 1,02538895 x 31,266667%) = 5.473,36. Ordem ALTERNATIVA (juros primeiro sobre o nominal, correcao depois sobre principal+juros): (4.066,41 + 4.066,41 x 31,266667%) x 1,02538895 = 5.473,36. DELTA = 0,00. Distributividade: P.i + P.i.j = (P + P.j).i.
- **teste 2 p210 vincendos:** Ordem do manual (criterio b agregado): 540,28 x 1,039177731 + 5.329,54 x 53% = 3.386,10. Ordem ALTERNATIVA linha-a-linha (estilo cap.7: cada Vr. corrigido x (taxa_original + 53 p.p.)) = 3.386,10. DELTA = 0,00.
- **teste 3 ordem ERRADA quantificada:** Se os juros do periodo novo incidissem sobre o principal NOMINAL: 540,28 x 1,039177731 + 5.128,61 x 53% = 3.279,61. DELTA = -106,49 sobre 3.386,10 (-3,15%). No ex. da p.209: 1.271,43 vs 1.303,71, DELTA = -32,28 (-2,48%).
- **conclusao:** A ordem CORRECAO->JUROS e comutativa com JUROS->CORRECAO. O que NAO e indiferente e a BASE dos juros: corrigida ou nominal. Essa e a unica escolha de ordem com efeito material no item 10.1.

## 3. Aritmética

**Método:** decimal.Decimal, getcontext().prec=50/60, ROUND_HALF_UP, quantize('0.01'). Nenhum float. Scripts: raw/verif_10_1_a.py, raw/verif_10_1_b.py, raw/verif_10_1_c.py.

### 10.1 contra a hipótese do capítulo 11

- **hipotese testada:** no cap.11 ficou provado que a aritmetica e encadeada em precisao plena e que os numeros impressos com 2 casas NAO sao os operandos; e que nao ha regra de arredondamento monetario declarada.
- **10 1 se comporta:** IGUAL, e com provas ainda mais fortes.
- **prova 1 precisao plena:** p.210, total de juros 3.386,10. Parcelas: 540,28 x 1,039177731 = 561,44694... e 5.329,54 x 53% = 2.824,6562. Somadas em PRECISAO PLENA: 3.386,10314 -> 3.386,10 (= manual). Somadas apos arredondar cada parcela (561,45 + 2.824,66): 3.386,11. O manual imprime 3.386,10. Logo a cadeia NAO passa por arredondamento intermediario.
- **prova 2 operandos impressos nao sao os operandos:** p.209: a tabela declara o indice '1,02538895' mas a formula na mesma pagina grafa '(4.066,41 x 1,025388925)' - dois operandos diferentes para o mesmo indice, ambos produzindo 4.169,65.; p.210: declara '1,039177731' e grafa '(540,28 x 1,03917731)' (um digito a menos).; p.215/216: declara 'Ind. AM ... 1,060860803' e grafa '(2.670,20 x 1,06086080)'.; p.219/223: declara o percentual tributavel como '0,81777777 ou 81,777777%' mas 25.890,35 / 31.659,54 = 0,8177…
- **prova 3 somas de coluna:** p.213, coluna 'Vr. Corrigido ate 30/06/09': soma dos 11 valores impressos = 2.670,18; total impresso 2.670,20. Delta +0,02.; p.213, coluna 'Dif. INSS recte': soma = 142,77; total impresso 142,78. Delta +0,01.; p.213, coluna 'INSS cota recda': soma = 354,99; total impresso 355,00. Delta +0,01.; p.217/220, coluna 'Total corrigido em 30/06/15': soma = 31.659,53; total impresso 31.659,54. Delta +0,01.; p.217/220, coluna 'Parcelas trib.': soma = 25.890,33; tot…
- **prova 4 regra de arredondamento:** Busca 'arredond' nas pp.209-223: ZERO ocorrencias. Em todo o manual (471 paginas) so ha 6 ocorrencias, TODAS sobre a regra de arredondamento do IR do par. unico do art.45 da IN/RFB 1500/14 (pp.226, 230) e notas '( * ) observada a regra de arredondamento' (pp.243, 250, 257) - nenhuma sobre arredondamento MONETARIO geral. Buscas 'casas decimais', 'duas casas', 'centavo', 'truncar', 'precisao': ZERO no segmento. CONFIRMADO: nao existe regra de arredondamento…

### Reproduzem exatamente (39)

- 4.066,41 x 1,02538895 = 4.169,6518... -> 4.169,65
- 4.169,65 x 31,266667% = 1.303,7105... -> 1.303,71
- 4.169,65 + 1.303,71 = 5.473,36
- 580,14 x 1,02538895 = 594,8691... -> 594,87
- 4.169,65 x 17% = 708,8405 -> 708,84
- 4.169,65 + 594,87 + 708,84 = 5.473,36 (identidade dos dois criterios)
- 10 linhas de juros vincendos (Vr x %): 522,59x15%=78,39 ... 503,87x6%=30,23
- 5.128,61 x 1,039177731 = 5.329,5373... -> 5.329,54
- 5.329,54 x 53% = 2.824,6562 -> 2.824,66
- 540,28x1,039177731 + 5.329,54x53% = 3.386,1031... -> 3.386,10
- 5.329,54 + 3.386,10 = 8.715,64
- 4.733,50+716,50+1.798,50+610,40 = 7.858,90; x30% = 2.357,67; bruto 10.216,57; -243,02 = 9.973,55
- 5.450,00/7.858,90 = 0,693481276 -> 0,6935 (4 casas, HALF_UP)
- 5.450,00x0,30 = 1.635,00; 5.450+1.635 = 7.085,00; 7.085,00/10.216,57 = 0,693481276 -> 0,6935
- 127,13 + 14,24 = 141,37; 145,00 + 16,24 = 161,24 (reflexo FGTS+40% = 11,2%)
- 2.401,25 + 665,15 = 3.066,40; -243,02 = 2.823,38
- 2.670,20 x 27,70% = 739,6454 -> 739,65; 2.401,25 x 27,70% = 665,14625 -> 665,15
- 3.409,85 - 243,02 - 154,68 = 3.012,15; +243,02+154,68+601,46 = 4.011,31
- 2.670,20 x 1,060860803 = 2.832,7105... -> 2.832,71
- 2.832,71 x 110,70% = 3.135,80997 -> 3.135,81 (a despeito do operando grafado)
- 243,02 x 1,060860803 = 257,8104 -> 257,81; 601,46 x idem = 638,0653 -> 638,07
- 2.401,25 x 1,060860803 = 2.547,392 -> 2.547,39
- (2.823,38+243,02)/3.409,85 = 0,8992770943 -> 0,8993
- 5.968,52 - 257,81 - 0,00 = 5.710,71; 5.710,71+257,81+638,07 = 6.606,59
- 2.547,39 - 257,81 = 2.289,58 (via direta)
- 2.832,71 x 0,8993 - 257,81 = 2.289,6461 -> 2.289,65 (via percentual, com o pct de 4 casas)
- 601,46 x 1,023071044 = 615,3363 -> 615,34
- 2.289,65 / 11 = 208,15
- 11 linhas: Total devido = Grat + Ref.1/3 + Ajuda; Total corrigido = Total devido x indice CSJT; Parcelas trib. = (Grat + Ref.1/3) x indice
- 11 linhas INSS: Base = Deb.Trab + sal.contrib; INSS devido = Base x 11%; Dif = devido - descontado
- 31.659,54 x 36,666667% = 11.608,4981 -> 11.608,50; bruto 43.268,04
- 25.890,35 - 637,79 = 25.252,56; x7,5% - 1.570,78 = 323,162 -> 323,16; 11 x 142,7985 = 1.570,7835 -> 1.570,78
- 31.659,54 x 1,01886993 = 32.256,9533 -> 32.256,95
- 637,79 x 1,01886993 = 649,825 -> 649,83; 25.890,35 x 1,01886993 = 26.378,899 -> 26.378,90
- 26.378,90 - 649,83 = 25.729,07; /11 = 2.339,006 -> 2.339,01; x7,5% - 1.570,78 = 358,90025 -> 358,90
- 46.624,05 + 906,64 + 8.449,93 + 358,90 = 56.339,52
- tabela Selic 3a hip.: Vr.Juros = INSS original x % Selic - 22 celulas conferidas
- tabela Selic 4a hip.: 21 de 22 celulas OK
- 625,56x12,08% = 75,5676 -> 75,57; 5.841,04x12,08% = 705,5976 -> 705,60; 5.841,04+2.608,89 = 8.449,93; 625,56+281,08 = 906,64

## 4. O que não reproduziu

| # | Item | `pagina_pdf` | Manual | Minha conta | Delta | Origem |
|---|---|---|---|---|---|---|
| NR01 | Passo 5, 'Juros sobre a base de IR' | 215 | 2.820,40 | 2.547,39 x 110,70% = 2.819,96073 -> 2.819,96 | +0,44 | REGRA OCULTA ou erro. Nao e arredondamento intermediario: nenhuma variante fecha. Testei: base… |
| NR02 | Passo 5, 'Total base IR' | 215 | 5.109,98 | (2.547,39 + 2.819,96) - 257,81 = 5.109,54 pela via direta; 5.968,52 x 0,8993 - 257,81 = 5.109,68 pela via do percentual | +0,44 (via direta) / +0,30 (via percentual) | REGRA OCULTA. O manual apresenta as duas vias como se dessem o mesmo 5.109,98 e nenhuma da. Ca… |
| NR03 | DEMONSTRATIVO art.12-A, 'RRA mensal (5.109,98 / 11)' | 215 | 465,54 | 5.109,98 / 11 = 464,5436... -> 464,54 | +1,00 exatos | Nao e arredondamento. 465,54 x 11 = 5.120,94, valor que nao existe no exemplo. Digito trocado… |
| NR04 | 'Total líquido devido ao reclamante' 30/06/15 | 218 | 42.307,10 | 43.268,04 - 637,79 - 323,16 = 42.307,09; em cadeia plena (31.659,54+11.608,4981-637,79-323,1585) = 42.307,0896 -> 42.307,09 | +0,01 | Nem arredondamento intermediario nem precisao plena fecham. Valor nao reproduzido. Repetido id… |
| NR05 | Passo 2, 'Juros 11/06/12 a 31/05/16' | 219 | 15.375,82 | 32.256,95 x 47,666667% = 15.375,81294 -> 15.375,81; cadeia plena 31.659,54x1,01886993x(47+20/30)/100 = 15.375,81452 -> 15.375,81; taxa exata 47+20/30: 15.375,81283 -> 15.375,81 | +0,01 | Todas as tres variantes dao 15.375,81. So um ROUND_UP (nao HALF_UP) produziria 15.375,82. Como… |
| NR06 | percentual parcelas passiveis IR | 219 | 0,81777777 ou 81,777777% | 25.890,35 / 31.659,54 = 0,8177740422... | -0,0000037 | REGRA OCULTA / erro de digitacao. O resultado que o manual atribui a essa via (25.729,07) so e… |
| NR07 | Passo 7, operandos grafados | 216 | (4.417,32 -248,63 -0,00) = 5.710,71 | 4.417,32 - 248,63 = 4.168,69 | -1.542,02 | RESIDUO DE VERSAO ANTERIOR. Os numeros 4.417,32 e 248,63 nao aparecem em nenhuma outra pagina… |
| NR08 | Passo 2, operando grafado | 215 | (2.731,80  x 110,70%) = 3.135,81 | 2.731,80 x 110,70% = 3.024,1026 | -111,71 | RESIDUO. O valor 2.731,80 so ocorre nas pp.215 e 216. O rotulo da celula ('Vr. Principal corri… |
| NR09 | Passo 4, INSS cota recda | 216 | (601,46 x 1,023071044) = 615,34 | aritmeticamente OK, mas o indice declarado em 'Dados para atualizacao' da MESMA pagina e 1,060860803, que daria 638,07 | 22,73 | RESIDUO. O indice 1,023071044 so ocorre na p.216. E o RESUMO da 2a hipotese (p.217) usa 638,07… |
| NR10 | tabela Selic 4a hip., linha '13o sal.', 'Vr. Juros INSS r… | 221 | 97,29 | 301,88 x 32,23% = 97,2959... -> 97,30 | -0,01 | arredondamento para baixo de um valor cuja 3a casa e 5+. Unica celula das 44 celulas Selic das… |
| NR11 | tabela Selic 3a hip., coluna 'Total INSS cota recte ate 3… | 219 | 54,11 / 53,80 / 53,53 | 37,92+16,18 = 54,10; 37,92+15,87 = 53,79; 37,92+15,60 = 53,52 | +0,01 em cada | a coluna nao e a soma das duas colunas impressas ao lado. Confirma operandos em precisao plena… |
| NR12 | tabela INSS, coluna 'base de cálculo de INSS pelo recte',… | 213 | 832,66 | 127,13 + 667,75 = 794,88 | +37,78 | REGRA OCULTA. A linha dez/05 tambem tem 'INSS cota recda' = 58,48 = exatamente 2 x 29,24 (o do… |
| NR13 | tabela INSS, coluna 'base de cálculo de INSS pelo recte',… | 213 | 957,56 | 145,00 + 957,50 = 1.102,50 | -144,94 | REGRA OCULTA (limitacao ao teto). O rotulo desta tabela diz apenas 'INSS devido'; a tabela equ… |
| NR14 | tabela INSS, coluna 'INSS descontado no decorrer do pacto… | 213 | 69,36 (ago/05); 67,00 (set/05); 68,37 (out/05); 73,75 (nov/05); 69,25 (fev/06) | sal.contrib x aliquota: 630,62x11% = 69,3682 -> 69,37; 609,14x11% = 67,0054 -> 67,01; 621,62x11% = 68,3782 -> 68,38; 670,52x11% = 73,7572 -> 73,76; 629,60x11% = 69,256 -> 69,26 | -0,01 em 5 das 11 linhas | arredondamento intermediario/precisao plena - a coluna nao e o produto dos dois valores impres… |

## 5. Achados estruturais

12 achados.

### AE01 — Contagem de dias do periodo de juros: o mes-calendario e normalizado para 30 dias E a contagem e INCLUSIVA do dia inici…

> Juros 23/10/13  a 31/05/16  referente 31 meses e 8 dias  (31 x 1% + 8  x 1%/30); Juros  - 10/03/07 a 31/05/16 - 110 meses e 21 dias  - (1% x 110 + 21 x  1%/30)); % juros  de 11/06/12 a 31/05/16 – 47 meses e 20 dias (47 x  1% + 20 x 1% / 30)

- **Teste:** 4 casos no segmento + 1 no calculo-base, todos fecham pela regra inclusiva e NENHUM pela exclusiva: 23/10 -> 30-23+1 = 8 (exclusiva daria 7); 10/03 -> 30-10+1 = 21 (daria 20); 11/06 -> 30-11+1 = 20 (daria 19); 11/06 ate 30/06/15 -> 20 (daria 19, e a data final e dia 30, nao 31); 10/03/07 a 30/06/09 -> 27,70% = 27 + 21/30, com a data final no dia 30 tratada como 30. 5/5.
- **Enunciada no manual:** NAO no segmento 209-223. Buscas: 'mes incompleto' 0 ocorrencias; 'pro rata' 0; '30 dias' 0; 'proporcional' 1 (p.223, e sobre descontos, nao sobre dias). A regra so aparece EMBUTIDA nos parenteses dos exemplos.
- **`pagina_pdf`:** 209; 215; 218 · **estrutural:** SIM - muda o motor. Um motor que use (data_final - data_inicial) em dias corridos erra 1 dia em todo periodo terminado em fim de mes. · **confiança:** alta

### AE02 — Os juros de mora incidem SEMPRE sobre o principal ja corrigido monetariamente, e apenas sobre o principal (sem os juros…

> a) aplicar o percentual/índice desde a propositura da ação sobre o valor corrigido; Vr. Principal corrigido x % juros

- **Teste:** 1.303,71 = 4.169,65 x 31,266667% (corrigido); sobre o nominal daria 1.271,43. Busca 'capitaliz' no segmento: 0 ocorrencias; 'juros simples': 0 ocorrencias. O regime simples e demonstrado, nunca nomeado.
- **Enunciada no manual:** parcialmente - a base corrigida esta enunciada na letra 'a' da p.209; a NAO capitalizacao nunca e enunciada, so demonstrada.
- **`pagina_pdf`:** 209; 215 · **estrutural:** SIM · **confiança:** alta

### AE03 — A correcao monetaria e a taxa de juros sao COMUTATIVAS entre si; o manual escolhe corrigir primeiro por convencao, nao…

> Quando o cálculo não envolver juros vincendos, o calculista poderá optar por qualquer um dos dois critérios, visto que os resultados finais são idênticos.

- **Teste:** (P x i) + (P x i x j) = 5.473,36 e (P + P x j) x i = 5.473,36. Delta 0,00.
- **Enunciada no manual:** a equivalencia dos criterios a/b esta enunciada (p.209); a comutatividade correcao/juros NAO esta - o manual nunca cogita inverter a ordem.
- **`pagina_pdf`:** 209 · **estrutural:** SIM - autoriza o motor a fixar uma ordem unica sem risco. · **confiança:** alta

### AE04 — Na atualizacao, o valor de JUROS ja apurado no calculo anterior e tratado como um saldo que se corrige monetariamente (…

> Vr. Juros vincendos apurados até 31/12/11 atualizado até 31/05/16 com o mesmo índice de correção monetária do principal  (540,28 x 1,039177731) + os Juros incidentes sobre o principal corrigido  entre 01/01/12 a 31/05/16  (5.329,54 x 53%)

- **Teste:** 540,28 x 1,039177731 + 5.329,54 x 53% = 3.386,10 = manual.
- **Enunciada no manual:** SIM, na letra 'b' da p.209 (tres sub-itens numerados).
- **`pagina_pdf`:** 210 · **estrutural:** SIM - exige que o motor persista o saldo de juros como estado, nao so a taxa. · **confiança:** alta

### AE05 — O IMPOSTO DE RENDA nunca se atualiza: e recalculado do zero com a tabela vigente na data final. O INSS, ao contrario, n…

> Em relação à contribuição social, basta atualizar os valores das contribuições cota reclamante e reclamada apurados no cálculo original; Quanto ao imposto de renda não é correto atualizar o valor do imposto apurado no cálculo original; É necessário reatualizar a base de cálculo do imposto, refazendo o cálculo do tributo no marco final da atualização com a tabela vigente no mês de apuração.

- **Teste:** 1a hip.: IR original 154,68 desaparece; novo IR = 0,00 sobre base 5.109,98. 3a hip.: IR original 323,16 -> novo 358,90 sobre base 25.729,07. O INSS 243,02 vira 257,81 por simples multiplicacao.
- **Enunciada no manual:** SIM, pp.210-211.
- **`pagina_pdf`:** 210; 211 · **estrutural:** SIM · **confiança:** alta

### AE06 — A base do IR e deduzida do INSS DEPOIS de sobre ela incidirem os juros (quando a hipotese inclui juros na base).

> Total base IR  Base corrigida + juros s/ base de IR – INSS  (2.547,39 + 2.820,40) – 257,81

- **Teste:** a ordem inversa (deduzir INSS e depois aplicar juros) daria (2.547,39-257,81)x2,1070 = 4.824,15, delta -285,83 sobre 5.109,98.
- **Enunciada no manual:** NAO como regra; so aparece na formula da celula. O roteiro do item 5 (p.214) grafa a ordem em prosa ('Sobre o resultado encontrado aplicar os juros de mora da data da propositura da ação até a data final de atualização e deduzir o valor do INSS') mas nao a ju…
- **`pagina_pdf`:** 215 · **estrutural:** SIM - a ordem aqui NAO e indiferente, diferente do caso principal/juros. · **confiança:** alta

### AE07 — O percentual/indice de parcelas tributaveis e INVARIANTE a inclusao ou exclusao dos juros, desde que a mesma taxa de ju…

> ( * ) Total das parcelas passíveis de IR com juros = somatório das horas extras e reflexos no  RSR e 13º salários acrescido dos  juros s/ as parcelas tributáveis:

- **Teste:** 5.450,00/7.858,90 = 0,69348127600554785020804438280166435506241331484050 e 7.085,00/10.216,57 = 0,69348127600554785020804438280166435506241331484050 - identicos ate a 50a casa.
- **Enunciada no manual:** NAO. O manual apresenta as duas formulas como alternativas de conveniencia ('para evitar de somar as parcelas tributáveis constantes no cálculo, o que muitas vezes constitui um processo trabalhoso') sem afirmar a invariancia.
- **`pagina_pdf`:** 212; 213 · **estrutural:** SIM - permite ao motor derivar o indice de qualquer das duas bases. · **confiança:** alta

### AE08 — Ha DOIS valores simultaneos e divergentes do mesmo INSS cota reclamante quando o fato gerador e a prestacao de servicos…

> Contribuição previdenciária cota recte atualizada até 31/05/16 com os índices do débito trabalhistas apenas para fins de dedução do crédito do reclamante

- **Teste:** 3a hipotese: 637,79 -> 649,83 (indice AM 1,01886993, usado no Passo 7 e no Passo 5) e 625,56 -> 906,64 (Selic 12,08%, levado ao RESUMO GERAL). Os dois entram no TOTAL DO CALCULO, cada um em seu papel.
- **Enunciada no manual:** parcialmente - o rotulo da celula enuncia; nao ha texto normativo no segmento explicando por que a deducao usa uma base e o recolhimento outra. Note-se que as BASES tambem divergem: 637,79 (corrigido a 30/06/15) vs 625,56 (valores originais).
- **`pagina_pdf`:** 219 · **estrutural:** SIM - o motor precisa manter duas trilhas para o mesmo tributo. · **confiança:** alta

### AE09 — Selic acumulada de forma SIMPLES, subtraindo 1 ponto percentual, e lida na tabela pratica do mes DOIS meses anterior a…

> Variação da Selic  de jun/15 até maio/16:  12,08% (13,08% - 1,00%), correspondente ao percentual de juros constante na tabela prática no mês de  abr/15 (dois meses anteriores à data final de atualização do cálculo base ) menos 1% de juros

- **Teste:** confirma-se por diferenca nas proprias tabelas do manual: jun/11 a maio/16 = 48,97% e jun/11 a jun/15 = 36,89%; 48,97 - 36,89 = 12,08. Exato nas duas tabelas (pp.219/220 e 221).
- **Enunciada no manual:** SIM no passo 8 da 4a hipotese (p.222), com remissao ao topico 9.2.6. NAO enunciada na 3a hipotese, que usa o mesmo mecanismo.
- **`pagina_pdf`:** 222 · **estrutural:** SIM · **confiança:** alta

### AE10 — A aritmetica e encadeada em precisao plena; os numeros impressos com 2 casas sao apresentacao, nao operandos. Nao ha re…

> (540,28 x 1,03917731)  +   (5.329,54 x 53,0%)

- **Teste:** a celula acima imprime 3.386,10; somando as parcelas arredondadas da 3.386,11. Somas de 9 colunas divergem dos totais impressos em 0,01 a 0,02. 'arredond' = 0 ocorrencias nas pp.209-223 e 6 em 471 paginas, todas sobre IR.
- **Enunciada no manual:** NAO.
- **`pagina_pdf`:** 210 · **estrutural:** SIM - o motor deve decidir sozinho a politica de arredondamento, e essa decisao produz deltas de ate 0,02 por coluna. · **confiança:** alta

### AE11 — Verbas indenizatorias sao excluidas da base de IR E da base de INSS mediante subtracao de coluna, sem qualquer enunciad…

> Ind.  Ajuda  transp.

- **Teste:** 'Parcelas trib.' = (Grat. Devida + Ref. 1/3 ferias) x indice, excluindo 'Ind. Ajuda transp.'; verificado nas 11 linhas. A coluna 'Deb. Trab. Ref. Parcelas salariais' da tabela de INSS da mesma hipotese tambem exclui a ajuda transporte (2.250,00 e nao 2.779,00) mas INCLUI o 1/3 de ferias em jan/12 (3.333,33). Na 1a/2a hipoteses, o excluido e o FGTS+40%: 2.670,20 - 2.401,25 = 268,95.
- **Enunciada no manual:** NAO no segmento. Busca 'natureza indenizatoria' / 'indenizator' no segmento: ver buscas_negativas.
- **`pagina_pdf`:** 217 · **estrutural:** SIM - a lista de verbas tributaveis e uma tabela de parametros que 10.1 pressupoe e nao fornece. · **confiança:** alta

### AE12 — Aliquota patronal de INSS de 23% aplicada sobre o debito trabalhista, sem enunciado.

> INSS  cota  recda

- **Teste:** p.213: 29,24/127,13 = 23,00%; dez/05 58,48/127,13 = 46,00% (2x, pelo 13o); mai/06 33,35/145,00 = 23,00%. p.217: 517,50/2.250,00 = 23,00%; 301,88/1.312,50 = 23,00%; 766,67/3.333,33 = 23,00%; 575,00/2.500,00 = 23,00%. Constante em 22 linhas.
- **Enunciada no manual:** NAO no segmento. Buscas '20%' = 0 ocorrencias, 'RAT' = 0 como termo isolado (18 falsos positivos por substring em 'gratificacao'/'atualizar'), 'grau de risco' = 0.
- **`pagina_pdf`:** 213; 217 · **estrutural:** SIM - a aliquota patronal (20% + RAT + terceiros) e parametro externo ao item. · **confiança:** alta

## 6. Achados incidentais

| # | Achado | `pagina_pdf` |
|---|---|---|
| AI01 | A tabela de juros vincendos da p.210 nao declara a taxa integral (18,70%) nem a regra de decremento; imprime apenas a serie 15%..6%. Quem le 10.1 isolado nao consegue reconstruir a ser… | 210 |
| AI02 | O rotulo da coluna de juros vincendos e '% juros 10/06/10 a 31/12/11' - um unico intervalo - mas a coluna contem 10 taxas diferentes, cada uma referida a um intervalo distinto. O rotul… | 210 |
| AI03 | Na 1a hipotese o manual escolhe a via DIRETA para a base de IR (5.109,98) e na 2a hipotese escolhe a via do PERCENTUAL (2.289,65, levada ao demonstrativo art.12-A), embora nas duas ele… | 215; 216; 217 |
| AI04 | A 2a hipotese, cujo titulo anuncia 'excluindo os juros da base de cálculo do IR', deriva o percentual tributavel de uma razao COM juros: 'Percentual parcelas passíveis IR ( Base IR com… | 216 |
| AI05 | 1a e 2a hipoteses produzem RESUMO identico (liquido 5.710,71; TOTAL 6.606,59) apesar de definirem bases de IR diferentes (5.109,98 com juros vs 2.289,65 sem juros). A identidade so oco… | 215; 217 |
| AI06 | A 2a hipotese anuncia mudanca de fato gerador da contribuicao ('o pagamento do crédito ao reclamante') mas o Passo 4 continua corrigindo o INSS pelo indice do debito trabalhista, exata… | 214; 216 |
| AI07 | O quadro 'Atualizacao dos valores' tem DOIS 'Passo 4': o quarto passo (INSS cota recte) e, ao final, outro rotulado 'Passo 4' para o INSS cota recda. Ocorre nas 1a e 2a hipoteses. | 215; 216 |
| AI08 | Erros de data nos rotulos: 'Total bruto em 3105/16' (sem barra, 4 ocorrencias); 'no período de 01/07/2009 a 31/05/19' (p.216); 'aplicar a correção monetária acumulada entre 01/07/09 a… | 215; 216; 219; 222 |
| AI09 | O DEMONSTRATIVO art.12-A da 3a hipotese (p.219) tem 'Mês início Jun/11 / Mês final Mar/12' mas o rotulo do numero de meses diz 'Nº de meses referente ao RRA de jul/05 a maio/06' - peri… | 219; 223 |
| AI10 | O calculo-base da p.213 lista 14 competencias (jul/05 a ago/06) mas 3 delas (jun, jul e ago/06) tem todas as colunas zeradas, e a tabela de INSS que a acompanha tem so 11 linhas. O 'Nº… | 213; 215 |
| AI11 | A 3a e a 4a hipoteses tem quadros de Passos 1 a 5 literalmente identicos, com os mesmos valores. A unica diferenca entre as duas hipoteses esta no passo 8 (atualizacao do INSS): a 3a a… | 219; 222; 223 |
| AI12 | O item 10.1, cujo titulo e 'sem amortização de valor pago', contem 4 hipoteses cuja diferenca e o FATO GERADOR da contribuicao previdenciaria e o tratamento dos juros na base do IR - n… | 209 |

## 7. Notas e rótulos conferidos contra a operação efetiva

### Notas de rodapé

| Nota | Confere? |
|---|---|
| ( * ) Total das parcelas passíveis de IR com juros = somatório das horas extras e reflexos no RSR e 13º salários a… | CONFERE. 4.733,50 + 716,50 = 5.450,00; 5.450,00 x 0,30 = 1.635,00; soma 7.085,00. Todas as tres linhas d… |
| Obs.: O total das parcelas passíveis de IR corresponde ao total das parcelas sujeitas à incidência de IR, acrescid… | CONFERE com o exemplo: 5.450,00 e valor corrigido e bruto de INSS (5.450,00 - 243,02 = 5.206,98 = base i… |
| Obs.: A segunda fórmula é utilizada, quando a base de cálculo do imposto de renda, apontada nos laudos periciais o… | CONFERE. 5.206,98 + 243,02 = 5.450,00. Observacao: a frase esta truncada ('quando a base ... , líquida d… |
| Obs.: Considerando a tabela única para a Justiça do Trabalho vigente para maio/16, o índice a ser utilizado será a… | CONFERE com a regra geral da p.209 e com o uso do indice 1,060860803. |
| Obs.: Considerando a tabela única ... o índice a ser utilizado será aquele posicionado em julho/15, visto que os c… | CONFERE (indice 1,01886993). |
| Obs.: O calculista poderá também determinar o percentual tributável e aplicá-lo sobre o principal corrigido para a… | NAO CONFERE COM A CONTA. 32.256,95 x 0,81777 - 649,83 = 25.728,94 e x 0,81777777 = 25.729,19; o manual i… |
| Obs.: Aplicação apenas dos Juros Selic, sem a inclusão da multa, considerando que a reclamada não foi citada para… | CONFERE para a tabela que qualifica (nao ha coluna de multa e os totais 906,64 / 8.449,93 sao INSS + jur… |
| Obs.: Se a multa já tiver sido apurada, mês a mês, informar também o seu valor. | CONFERE formalmente; na 4a hipotese a coluna E (Multa) vem 0,00. |

### Rótulos contra a conta que a coluna de fato faz

**RT01** (`pagina_pdf` 215; 216) — Vr. Principal corrigido x % juros


**RT02** (`pagina_pdf` 219) — 


**RT03** (`pagina_pdf` 216) — 


**RT04** (`pagina_pdf` 223) — 


**RT05** (`pagina_pdf` 223) — 


**RT06** (`pagina_pdf` 223) — as REMISSOES de coluna foram remapeadas em relacao a p.261 mas os DADOS nao: p.223 diz '(col. G x Selic acumulada)' e '(col. G + col. I + col. J)'; p.261 diz '(col. F x Selic acumulada)' e '(col. F +…


**RT07** (`pagina_pdf` 213) — 


**RT08** (`pagina_pdf` 213) — 


**RT09** (`pagina_pdf` 210) — 


**RT10** (`pagina_pdf` 213) — 


**RT11** (`pagina_pdf` 219; 221) — 


## 8. Confronto com os juros vincendos do capítulo 7

**pergunta:** o metodo de 10.1 (p.210) coincide com o do capitulo 7 (pp.95-99)?

**resposta:** COINCIDEM na regra de formacao das taxas e no resultado; DIVERGEM na forma de reatualizacao (agregada vs linha-a-linha). Os dois sao registrados abaixo sem harmonizacao.

**cap7 regra enunciada**

- **pagina pdf:** 95
- **literais:** Para calcular os juros vincendos, primeiro apura-se o percentual de juros total entre a data da propositura da ação e a data final de atualização dos cálculos.; Este percentual será aplicado sobre as parcelas devidas até o mês anterior ao da propositura da ação.; No mês referente ao ajuizamento, o percentual de juros devido reduzirá na proporção do número de dias entre a data da inicial e o término do referido mês.;…
- **mecanica cap7 p96:** tabela com colunas Diferencas deferidas \| Ind. AM \| Vr. Atualiz. \| % juros \| Vr. Juros \| Total bruto. Vr. Juros = Vr. ATUALIZ. x %juros (verificado em 9 linhas; sobre o nominal daria valores menores). Ultima linha jan/12: 0,00% e Vr. Juros '-'.

**teste de coincidencia**

- **descricao:** a tabela de 10.1 p.210 NAO declara a taxa integral nem a regra de decremento; so imprime 15%..6%. Reconstrui a serie pela regra do cap.7 e comparei.
- **dados:** acao 10/06/10, atualizado ate 31/12/11
- **taxa integral reconstruida:** 18 meses (10/06/10 a 10/12/11) + 21 dias = 18,70%
- **mes do ajuizamento:** jun/10 = 18,70% - (21 x 1%/30) = 18,00%
- **serie reconstruida:** {'Jun/10': '18,00', 'Jul/10': '17,00', 'Ago/10': '16,00', 'Set/10': '15,00', 'Out/10': '14,00', 'Nov/10': '13,00', 'Dez/10': '12,00', 'Jan/11': '11,00', 'Fev/11': '10,00', 'Mar/11': '9,00', 'Abr/11': '8,00', 'Mai/11': '7,00', 'Jun/11': '6,00'}
- **serie impressa em 10 1:** {'Set/10': '15,00', 'Out/10': '14,00', 'Nov/10': '13,00', 'Dez/10': '12,00', 'Jan/11': '11,00', 'Fev/11': '10,00', 'Mar/11': '9,00', 'Abr/11': '8,00', 'Mai/11': '7,00', 'Jun/11': '6,00'}
- **resultado:** COINCIDENCIA EXATA nas 10 linhas impressas. A regra do cap.7 (inclusive a contagem inclusiva de 21 dias) reproduz a serie de 10.1 sem residuo.

**divergencia de procedimento**

- **cap7:** recalcula LINHA A LINHA: cada competencia tem sua propria taxa e seus juros sao Vr. corrigido da linha x taxa da linha.
- **item 10 1:** na REATUALIZACAO abandona a linha-a-linha e opera em bloco: (juros vincendos ja apurados x indice de CM) + (principal corrigido total x taxa uniforme do novo periodo). Literal p.210: 'Vr. Juros vincendos apurados até 31/12/11 atualizado até 31/05/16 com o mesmo índice de correção monetária do principal  (540,28 x 1,039177731) + os Juros incidentes sobre o principal corrigido  entre 01/01/12 a 31/05/16  (5.329,54 x 5…
- **sao equivalentes:** SIM neste exemplo. Refiz linha-a-linha (Vr_nominal x 1,039177731 x (taxa_original + 53 p.p.)) = 3.386,10 = valor do manual. Delta 0,00.
- **quando deixariam de ser:** se houvesse parcelas vencendo ENTRE 01/01/12 e 31/05/16, o acrescimo de taxa nao seria uniforme (a regra do cap.7 imporia decremento e taxa zero no mes final) e o metodo agregado de 10.1 superestimaria os juros. O exemplo da p.210 nao tem parcelas posteriores a jun/11, entao a questao nao aparece. O item 10.1 NAO adverte sobre isso - so adverte sobre a escolha entre os criterios a e b.
- **busca negativa:** termo 'vincend' no segmento 209-223: 4 ocorrencias, todas em p.209 (2) e p.210 (2). Nenhuma delas trata da reatualizacao de parcelas vencidas APOS a data do calculo anterior.

## 9. Buscas que sustentam as afirmações negativas

Nenhuma negativa deste bloco é opinião: cada uma tem a varredura ao lado.

| Afirmação | Termos | Ocorrências | Páginas |
|---|---|---|---|
| Nao existe regra de arredondamento monetario declarada no item 10.1. | `arredond; casas decimais; duas casas; centavo; truncar; preci…` | 0 | 209-223 |
| A regra de contagem de dias (mes de 30 dias, contagem inclusiva) nao e enunciada no segmento. | `mes incompleto; pro rata; 30 dias; dia da citacao` | 0 | 209-223 |
| O regime de juros simples nao e nomeado no segmento. | `juros simples; capitaliz` | 0 | 209-223 |
| A aliquota patronal de 23% nao e enunciada no segmento. | `20%; RAT; grau de risco; salario de contribuicao` | '20%' 0; 'grau de risco' 0; 'salario de contribuicao' 0 (a expressao aparece como 'salário de contribuição ref. ao INSS' em cabecalho de coluna, com quebra de linha, o que a busca literal nao captura); 'RAT' 18, TODAS falso-positivo por substring em 'gratificacao'/'atualizar'/'gratuita' | 209-223 |
| O tema dos juros vincendos e tratado em apenas 2 paginas do segmento. | `vincend` | 4 | 209-223 |
| A data-base nao e nomeada como tal. | `data-base; data base` | 0 | 209-223 |
| Os valores 2.731,80, 4.417,32, 248,63 e 1,023071044 sao residuos sem origem no exemplo. | `` |  |  |
| Os valores 956,19 e 8.912,54 da coluna F do quadro A-K vem de outro exemplo. | `` |  |  |
| O titulo 10.2 nao comeca na p.223 no inicio da pagina. | `` |  |  |

## 10. Pendências

| # | Tipo | Descrição |
|---|---|---|
| P01 | escopo | A extracao foi limitada a p.222 por instrucao expressa, mas 10.1 continua ate o offset 2658 da p.223. Ficaram FORA: conclusao do Passo 5, Passos 6 e 7, DEMONSTRATIVO art.12-A e RESUMO GERAL da 4a hipotese, alem do quadro A-K. Li e verifiquei esse trecho para… |
| P02 | dependencia externa | 10.1 pressupoe e nao fornece: (a) a tabela unica CSJT de indices; (b) a tabela progressiva do IR e a parcela a deduzir (142,7985 usada na p.219); (c) a tabela pratica de Selic; (d) as tabelas de salario de contribuicao e teto da epoca; (e) a aliquota patronal… |
| P03 | remissao nao resolvida | O passo 8 da 4a hipotese remete ao topico 9.2.7.3 e ao 9.2.6 ('conforme já explicado no tópico 9.2.6'). Tambem ha remissao ao 'tópico 7.3 deste manual' na p.209 para os percentuais de juros. Nenhuma foi extraida neste segmento. |
| P04 | aritmetica aberta | NR01/NR02 (2.820,40 e 5.109,98 na p.215) nao tem origem identificada por nenhuma das vias declaradas. Delta de 0,44. Nao e arredondamento. Permanece como regra oculta ou erro. |
| P05 | aritmetica aberta | NR05: 15.375,82 nao e reproduzivel por HALF_UP em nenhuma variante (todas dao 15.375,81) e propaga +0,01 ao bruto e ao liquido. Aparece DUAS vezes (pp.219 e 222/223), o que afasta a hipotese de erro de digitacao isolado e sugere politica de arredondamento nao… |
| P06 | a testar no 10.3 | Linha de base estabelecida por este segmento, contra a qual a amortizacao de 10.3 deve ser comparada: (i) correcao e juros sao comutativos, mas a base dos juros (corrigida vs nominal) nao e indiferente (-2,5% a -3,2%); (ii) o saldo de juros anterior e estado… |
| P07 | verificacao nao feita | Nao conferi os indices CSJT das pp.209, 210, 215, 217 e 218 contra a tabela unica do final do manual (o proprio manual remete: 'vide tabela final do manual'). Todas as verificacoes de correcao monetaria assumiram os indices impressos como dados. |

