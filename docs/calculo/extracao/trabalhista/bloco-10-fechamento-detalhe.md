# Bloco 10 — detalhe

Companheiro de `bloco-10-fechamento.md`. Aqui vai o material bruto conferido: os sete
casos do capítulo 11 com a aritmética refeita, os trinta e sete achados, as vinte notas
confrontadas, os oito itens do capítulo 15 e o que não reproduziu.

Gerado por script a partir dos JSON de extração. **Offset de paginação zero.**

---

## 1. Capítulo 11 — os sete casos

**7 exemplos**, numerados `1, 2, 4, 5, 6, 7, 8`.

> Não existe 'Exemplo 3' no capítulo: o texto salta de 'Exemplo 2: Adicional de insalubridade e reflexos' (p.280) para 'Exemplo 4 – Horas extras' (p.283). Busca do literal 'Exemplo 3' em todas as 471 páginas do PDF retorna apenas p.134, 156, 161 e 255 (capítulos anteriores); busca de 'EXEMPLO 3' retorna vazio.

| # | Título | pp. | O que demonstra |
|---|---|---|---|
| ex1 | Exemplo 1  - Parcelas rescisórias | 278-280 | liquidação integral de rescisão com multas 467/477, indenização substitutiva do seguro-desemprego, INSS Súm.45 TRT-3 e RRA |
| ex2 | Exemplo 2: Adicional de insalubridade e reflexos | 280-283 | apuração mês a mês de adicional sobre salário mínimo com reflexos, INSS com recomposição do salário-de-contribuição, honorários p… |
| ex4 | Exemplo 4 – Horas extras | 283-286 | HE com divisor 220 e adicional 50%, reflexo em RSR com OJ 394, médias para aviso/13º/férias, competências anteriores a 04/03/09 (… |
| ex5 | Exemplo 5 – Diferença salarial piso CCT e horas extras | 286-292 | diferença de piso normativo, HE apuradas dia a dia por cartão de ponto (divisor 200, adicional 60%), hora relógio→centesimal, ref… |
| ex6 | Exemplo 6 – Acordo descumprido e multa apenas sobre a… | 293-294 | acordo em 8 parcelas, 3 pagas; multa 50% só sobre a parcela vencida + vencimento antecipado; rateio da contribuição previdenciári… |
| ex7 | Exemplo 7 – Acordo descumprido e multa sobre o saldo d… | 295 | acordo sem reconhecimento de vínculo, descumprido integralmente; multa 100% sobre o saldo já corrigido; INSS 11% (teto) + 20% na… |
| ex8 | Exemplo 8 – Atualização do cálculo apresentado pelas p… | 296-298 | reatualização de cálculo já homologado (de 31/10/15 para 31/05/16): correção do principal E dos juros já apurados; equivalência e… |

## 2. Achados estruturais do capítulo 11

17 achados. Cada um com a evidência e se o manual o enuncia.

### E01 — Na reatualização de cálculo homologado (Ex.8), o FGTS a depositar soma TRÊS linhas: principal corrigido + jur…

- **Evidência:** Principal - FGTS a depositar 01/11/15 31/05/16 12.824,00 1,01087868 12.963,51 / Valor juros - FGTS a depositar 01/11/15 31/05/16 3.761,71 1,01087868 3.802,63 / Juros s/ o principal - FGTS a depositar 21/05/13 31/05/16 12.963,51 36,333333% 4.710,07 / Total FGTS a depositar 31/05/16 31/05/16 21.476,22
- **Enunciada no manual:** não (é defeito, não regra). O mesmo Exemplo 8 enuncia o método correto na p.297: 'Recalculando os juros a partir da inicial, apura-se o mesmo valor bruto até a data final de atualização'
- **Observação:** O valor 21.476,22 propaga para o RESUMO GERAL e para o TOTAL DO CÁLCULO 292.265,29 (p.298). Não corrigido, apenas registrado.
- **`pagina_pdf`:** 297
- **Estrutural:** True · **confiança:** alta

### E02 — Ex.1: o INSS cota reclamante deduzido do crédito (570,83) foi obtido aplicando o índice de correção DUAS veze…

- **Evidência:** Base INSS em vrs. Originais / ... / 4.226,72 11% 472,62 ... 8% 98,21 ... total 570,83  \|\|  na tabela da Súmula 45: 'aviso e saldo de sal. 4.158,00 11% 457,38' e 'jul. 15 13º sal. 1.188,00 8% 95,04' total '552,42'
- **Enunciada no manual:** não. O cabeçalho só diz 'INSS recte atualizado com TR apenas para fins de dedução do crédito do recte' (p.279) — nada sobre dupla incidência.
- **Observação:** Efeito: total líquido do recte reduzido em 9,28 a mais do que a contribuição efetivamente recolhida. Nos Ex.2 e Ex.5 a mesma coluna aplica o índice UMA vez (Ex.5: 45,48 × 1,036175834 = 47,12 ✓). Ou seja, Ex.1 diverge dos demais.
- **`pagina_pdf`:** 279-280
- **Estrutural:** True · **confiança:** alta

### E03 — A base das custas de execução (0,5%) do capítulo 11 é 'total líquido do recte + INSS cota recte (com juros e…

- **Evidência:** cap.11: 'Custas execução s/ o cálculo de liquidação 30.312,80 0,50% 151,56' (28.416,25 líquido + 606,12 + 1.290,44)  \|\|  cap.9 p.132: 'Custas execução s/ o cálculo de liquidação (Vr. Bruto do recte + INSS recda) x 0,5% 0,50% 26,04' (4.729,81 bruto + 477,73)
- **Enunciada no manual:** parcialmente. p.101 item 2: 'Da base de cálculo das CE será excluída apenas a parcela de custas processuais (custas da fase de conhecimento)'. Não diz se o crédito entra bruto ou líquido, nem como tratar juros/multa previdenciários.
- **`pagina_pdf`:** 280 (e 132 para confronto)
- **Estrutural:** True · **confiança:** alta

### E04 — Ex.2: a mesma base de custas de execução mistura critérios — o crédito do reclamante entra LÍQUIDO (já deduzi…

- **Evidência:** Total custas execução s/ (total do recte, cont. previd. e hon. Periciais) 35,19
- **Enunciada no manual:** não. Busca por 'custas de execução' em todo o PDF: p.83, 100, 101, 102 — nenhuma dessas trata de honorários periciais na base.
- **`pagina_pdf`:** 283
- **Estrutural:** True · **confiança:** alta

### E05 — Toda a aritmética dos exemplos é encadeada em precisão plena: os valores exibidos com 2 casas NÃO são os oper…

- **Evidência:** Ex.2, linha '17/02/2014 (14 dias)': colunas '67,57 \| 5,41 \| 15,54 \| 24,99% \| 0,00% \| 1,35 \| 6,76 \| 3,88 \| 19,43'. A soma das parcelas exibidas 15,54+3,88 = 19,42, mas o manual imprime 19,43.  \|\|  Ex.4 out/07: '49,64 + 9,55 + 5,56' exibidos, total impresso '64,74' (a soma dos exibidos é 64,75).
- **Enunciada no manual:** não. Busca literal em todas as 471 páginas: 'arredond' → p.226, 230, 243, 250, 257 (todas sobre o nº de meses do RRA, IN/RFB 1500/14 art.45 §único); 'casas decimais' → 0 ocorrências; 'truncad' → 0 ocorrências; 'centavo' → p.99 apenas (paridades monetárias históricas).
- **Observação:** Consequência mensurável: as somas das colunas impressas não fecham com os totais impressos — Ex.2 coluna 'Total corrigido' soma 3.919,51 mas o total é 3.919,48; coluna 'Dif. INSS' soma 269,57 mas o total é 269,59; coluna 'Parcelas tributáveis' reproduzida dá 3.449,57 contra 3.449,63. Ex.4 coluna 'Dif. INSS' soma 123,08 contra 123,09 impresso; 'INSS recda' soma 324,96 contra 324,94.
- **`pagina_pdf`:** 282, 283
- **Estrutural:** True · **confiança:** alta

### E06 — Mês incompleto: sempre mês comercial de 30 dias, e o número de dias do mês de ADMISSÃO é contado do dia da ad…

- **Evidência:** '17/02/2014 (14 dias) 337,87' (Ex.2, p.281) — 724,00/30×14 = 337,8667.  'Vr. prop. a 20 dias em set/14 (640 / 30 x 20)' com período iniciado em 11/09/14 (Ex.6, p.293). 'Em fev/13 a diferença salarial foi apurada proporcionalmente aos 20 dias trabalhados: (1.126,00 - 945,00) / 30 x 20 = 120,67' com admissão em 11/02/13 (Ex.5, p.291).
- **Enunciada no manual:** não localizada. Buscas literais: 'mês comercial' → 0; '30 avos' → 0.
- **`pagina_pdf`:** 281, 291, 293
- **Estrutural:** True · **confiança:** alta

### E07 — Ex.6: ao ratear o acordo, o SALÁRIO-DE-CONTRIBUIÇÃO do mês incompleto também é proporcionalizado (1.420,00/30…

- **Evidência:** linha '11/09/14 \| 426,67 \| 946,67 \| 1.373,33 \| 9% \| 123,60 \| 75,73 \| 47,87 \| 19,62% \| 9,39'
- **Enunciada no manual:** não localizada
- **`pagina_pdf`:** 294
- **Estrutural:** True · **confiança:** alta

### E08 — Ex.6: o RESUMO GERAL exclui a multa previdenciária que o demonstrativo da mesma página incluiu. Cota recte 99…

- **Evidência:** 'INSS cota recte 741,30 101,94 20,00% 148,26 991,50' e 'INSS cota recda 1.840,00 253,49 20,00% 368,00 2.461,49' seguidos de 'RESUMO GERAL ... Total contribuição previdenciária cota recte 843,24 ... Total contribuição previdenciária cota recda 2.093,49'
- **Enunciada no manual:** não (defeito)
- **Observação:** A base das custas de execução declarada (16.328,35) não corresponde a nenhuma das duas versões: com multa daria 16.328,65; sem multa daria 15.812,39. Não reproduzido (ver seção 'nao_reproduzidos').
- **`pagina_pdf`:** 294
- **Estrutural:** True · **confiança:** alta

### E09 — ACORDO — termo inicial: correção monetária e juros correm a partir do DIA SEGUINTE ao vencimento da parcela i…

- **Evidência:** Ex.6: 'Principal atualizado - total do acordo, deduzindo as três parcelas pagas (18.200,00 – 2.275,00 x 3) 16/03/16 31/05/16 11.375,00' (4ª parcela vencia 15/03/16); 'Juros 16/03/16 31/05/16 12.561,62 2,500000% 314,04'. Ex.7: 'Principal atualizado 13/04/16 31/05/16 12.300,00' (1ª parcela vencia 12/04/2016); 'Juros 13/04/16 31/05/16 24.656,98 1,600000% 394,51'
- **Enunciada no manual:** não para acordos. A p.84 descreve 'Da efetiva data de vencimento da parcela... a partir do dia seguinte ao vencimento da parcela' como a '4ª corrente' histórica, e conclui: 'Atualmente a aplicação dos índices de correção monetária ocorre na forma da Súmula nº 381 do TST'. Buscas: 'acordo descumprido' → 0 ocorrências; 'descumprimento do acordo' → 0 ocorrências; 'vencimento da parcela' → apenas p.84.
- **`pagina_pdf`:** 293, 295
- **Estrutural:** True · **confiança:** alta

### E10 — ACORDO — base da contribuição previdenciária é o valor ORIGINAL do acordo (ou a parcela salarial declarada),…

- **Evidência:** Ex.7: 'Base INSS ... abr/16 12.300,00 570,88 2.460,00' quando o total devido ao recte já era 25.051,50 (com multa de 100% e juros). Ex.6: 'O(A) reclamado(a) providenciará o recolhimento das contribuições previdenciárias referentes à parcela salarial do acordo (R$ 8.000,00)' e a tabela de rateio soma exatamente 8.000,00.
- **Enunciada no manual:** parcialmente (p.172-173 e OJ-SDI1-398 quanto às alíquotas 20%+11% com teto em acordo sem vínculo); a exclusão de multa/juros/correção da base não foi localizada como enunciado
- **`pagina_pdf`:** 293, 295
- **Estrutural:** True · **confiança:** alta

### E11 — ACORDO — a multa por descumprimento é calculada sobre o valor ORIGINAL da parcela e só depois corrigida (Ex.6…

- **Evidência:** Ex.6: 'Multa 50% s/ parcela em atraso (2.275,00 x 50%) 16/03/16 31/05/16 1.137,50 1,00392549 1.141,97'  \|\|  Ex.7: 'Multa 100% 13/04/16 31/05/16 12.328,49 100,00% 12.328,49' (12.328,49 é o principal JÁ corrigido)
- **Enunciada no manual:** não
- **`pagina_pdf`:** 293, 295
- **Estrutural:** True · **confiança:** alta

### E12 — Ex.1 — a base da multa do art. 467 inclui o saldo de salário e a multa de 40% sobre o FGTS rescisório, nenhum…

- **Evidência:** dispositivo: 'h) Multa art. 467 incidente sobre aviso prévio 40% do FGTS, férias vencidas e proporcionais e 13º salário'; rótulo da linha: 'Multa art. 467 ( 50% s/ aviso prévio, 40% FGTS, férias + 1/3 e 13o sal.)'; valor: '5.911,54'
- **Enunciada no manual:** sim, quanto ao saldo de salário: p.76 — 'O acréscimo de 50% sobre as parcelas rescisórias geralmente incidirá sobre o aviso prévio, férias pagas na rescisão, 13º salário da rescisão, saldo de salários'; e OJ 29 TRT-3 quanto à multa de 40% do FGTS. Não enunciada a inclusão da multa de 40% sobre o FGTS incidente nas verbas rescisórias (171,07).
- **Observação:** O rótulo da linha e o dispositivo contradizem a conta. Registrado, não corrigido.
- **`pagina_pdf`:** 278-279
- **Estrutural:** True · **confiança:** alta

### E13 — Ex.1 — a parcela TRIBUTÁVEL da multa do art. 467 é 50% apenas de (saldo de salário + 13º): o aviso prévio ind…

- **Evidência:** coluna 'Parcelas tributáveis' na linha da multa 467: '1.358,59'; total das tributáveis '4.075,76'
- **Enunciada no manual:** sim, p.76: 'apenas a proporção da multa incidente sobre as parcelas passíveis de incidência de imposto de renda (13º salário e saldo de salários) será tributável'
- **`pagina_pdf`:** 279
- **Estrutural:** True · **confiança:** alta

### E14 — Ex.4 — os juros de mora SÃO somados à base do imposto de renda; nos Ex.1, 2, 5 e 8 são excluídos.

- **Evidência:** 'Juros s/ parcelas tributáveis 982,64 91,70% 901,08 / RRA (Base IR) com juros (982,64 + 901,08 - 123,09) 1.760,63'
- **Enunciada no manual:** sim, p.182: 'os juros de mora sobre as parcelas tributáveis apenas deverão ser excluídos da base de cálculo do imposto de renda se houver decisões nos autos neste sentido ou se pagas no contexto da rescisão do contrato de trabalho'. O dispositivo do Ex.4 não invoca a OJ 400, o que explica a inclusão.
- **Observação:** Atrito: o Ex.4 é indiscutivelmente rescisório (aviso prévio, 13º, férias 11/12) — a segunda hipótese da p.182 ('se pagas no contexto da rescisão do contrato de trabalho') mandaria excluir os juros. O exemplo não discute isso.
- **`pagina_pdf`:** 285
- **Estrutural:** True · **confiança:** alta

### E15 — Ex.8 — a base do IR na reatualização é obtida aplicando ao principal corrigido o PERCENTUAL de parcelas tribu…

- **Evidência:** 'RRA (Base IR) no período 31/05/16 31/05/16 160.076,78 83,200% 133.183,88'
- **Enunciada no manual:** sim, p.211: 'Outra alternativa, é apurar o percentual ou o índice de parcelas tributáveis nos cálculos de liquidação e determinar a base sempre a partir deste percentual/índice', com a fórmula 'Total das parcelas passíveis de IR constante no cálculo homologado e sem a inclusão dos juros / Total do principal corrigido constante no cálculo homologado'
- **`pagina_pdf`:** 297
- **Estrutural:** True · **confiança:** alta

### E16 — Ex.8 — na reatualização do INSS já corrigido, a Selic é reposicionada subtraindo 1% da taxa do mês situado do…

- **Evidência:** 'Juros Selic acumulados = taxa de juros constante em agosto/15 (dois meses anteriores à data final de atualização do cálculo base – 1% de juros), tendo em vista que a contribuição previdenciária apurada no cálculo homologado já estava atualizada com juros Selic até out/15. Taxa de juros Selic = 8,61% (% juros em ago/15 na tabela de maio/16) – 1% = 7,61%'
- **Enunciada no manual:** variante. A p.124 enuncia a operação inversa: 'verificar qual é a taxa deste mês na tabela disponível..., subtrair deste valor a taxa de juros acumulada posicionada nos dois meses anteriores ao mês em que se deseja atualizar o cálculo e somar 1% de juros'. O Ex.8 usa diretamente a taxa de ago/15 MENOS 1%, sem a subtração descrita.
- **`pagina_pdf`:** 298
- **Estrutural:** True · **confiança:** media

### E17 — Ex.8 — os juros já apurados no cálculo homologado sofrem correção monetária pelo mesmo índice do principal (j…

- **Evidência:** 'Valor juros 01/11/15 31/05/16 46.450,54 1,01087868 46.955,86' e 'OU / Recalculando os juros a partir da inicial, apura-se o mesmo valor bruto até a data final de atualização'
- **Enunciada no manual:** enunciada no próprio exemplo; não localizada como regra no cap.7
- **`pagina_pdf`:** 297
- **Estrutural:** True · **confiança:** alta

## 3. Achados incidentais

| # | Achado | `pagina_pdf` |
|---|---|---|
| i01 | Ex.4 — o terço constitucional é aplicado por fator 1,3333 (quatro casas), não por divisão por 3. | 284 |
| i02 | Ex.4 — a soma declarada das horas extras (142,22) não confere com as linhas da tabela, que somam 142,20. | 284 |
| i03 | Ex.4 — etapa intermediária impressa truncada: '14,22 x 11/12 = 13,03' (arredondamento normal daria 13,04); o valor final, porém, usa precisão plena. | 284 |
| i04 | Ex.4 — o cabeçalho da coluna de INSS patronal declara base 'col. a' (total devido, que inclui o reflexo em FGTS+40%), mas a conta usa 'col. d' (base INSS do débito trabalhist… | 285 |
| i05 | Ex.5 — o RESUMO GERAL informa custas de execução de 74,15, mas a linha imediatamente acima apura 70,32, e é 70,32 que compõe o TOTAL. | 287 |
| i06 | Ex.5 — o RESUMO informa como base do IR o valor BRUTO tributável (6.885,06), enquanto a linha de apuração usa o valor LÍQUIDO de INSS (6.119,43). Nos Ex.1 e Ex.2 o resumo mos… | 287 (e 280) |
| i07 | Nº de meses do RRA aparece sem fórmula que o produza. Ex.1 traz valor 2 sob rótulo copiado do Ex.5; Ex.4 traz valor 9 sob rótulo cuja fórmula daria 12. | 280, 285, 287 |
| i08 | Ex.1 — a nota do seguro-desemprego usa um período de vínculo divergente dos dados complementares do próprio exemplo. | 279 |
| i09 | Ex.1 — a coluna rotulada 'Base INSS em vrs. Originais' contém 4.226,72, que é a base já corrigida (4.158,00 × 1,016526834). | 279 |
| i10 | Alíquota patronal de 23% é aplicada nos Ex.2 e Ex.5 sem constar dos dados complementares; os Ex.1 (22%) e Ex.4 (21%) declaram a alíquota. | 278, 282, 283, 292 |
| i11 | Ex.8 — a parcela a deduzir do RRA não é o produto da parcela mensal pelo nº de meses. | 296, 297 |
| i12 | Ex.8 — o SAT é apurado como 2% da contribuição cota patronal, não 2% da base de cálculo. | 296 |
| i13 | Ex.6 — custas processuais 'pelas partes' (R$364,00) foram apuradas pela metade (182,00) e corrigidas do dia seguinte à homologação. | 293 |
| i14 | Ex.6 — a multa previdenciária de 20% incide apenas sobre o principal, não sobre principal + juros Selic. | 294 |
| i15 | Ex.7 — multa previdenciária de 0,33% ao dia × 49 dias (13/04/16 a 31/05/16) = 16,17%, contados do dia seguinte ao vencimento da 1ª parcela; juros Selic 0,00% por a competênci… | 295 |
| i16 | Ex.2 — 13º proporcional 10/12 e férias proporcionais 7/12 no mesmo período contratual (17/02/14 a 22/09/15), sem justificativa no texto. | 281 |
| i17 | Ex.5 — não há reflexo de FGTS+40% sobre os reflexos em aviso prévio, 13º e férias; o FGTS+40% só foi computado mês a mês sobre a diferença salarial e sobre as HE. | 286, 291 |
| i18 | Ex.5 — reflexo da diferença salarial em FGTS+40% de fev/13 impresso como 13,51 quando 120,67 × 0,112 = 13,5150. | 291 |
| i19 | Ex.1 — o índice de correção aplicado a TODAS as parcelas é o do mês da rescisão (jul/15 = 1,016526834), inclusive às multas 467 e 477 e à indenização do seguro-desemprego, e… | 279 |
| i20 | Ex.2 — honorários periciais corrigidos por índice distinto do crédito principal (IPCA-e / tabela CJF, OJ 198) e tributados pela tabela MENSAL vigente em maio/16, não pelo reg… | 281, 282 |

## 4. O que não reproduziu

A maioria é diferença de centavo causada pela precisão plena (achado E05). Os materiais estão marcados.

| Onde | Item | Manual | Recalculado | Leitura |
|---|---|---|---|---|
| Ex.1, p.280 | Total bruto | 28.987,08 | 28.987,07 | 26.667,04 + 2.320,03 (= 26.667,04 × 8,70%, exato 2.320,0324). Diferença 0,01 provavelmente por soma em precisão plena na planilha. |
| Ex.1, p.280 | Base das custas de execução | 30.312,80 | 30.312,81 | 28.416,25 + 606,12 + 1.290,44. As custas (151,56) coincidem nas duas hipóteses. |
| Ex.2, p.281 | Total do principal corrigido | 3.919,48 | 3.919,51 | Soma das 25 linhas impressas da coluna 'Total corrigido' = 3.919,51; recálculo em precisão plena também dá 3.919,51. Diferença 0,… |
| Ex.2, p.281/282 | Soma da coluna 'Dif. INSS devida' | 269,59 | 269,57 | Soma das 23 linhas impressas = 269,57. A coluna atualizada (275,97) fecha exatamente. |
| Ex.2, p.282 | Parcelas tributáveis | 3.449,63 | 3.449,57 | Soma de (ad. insal. + 1/3 férias gozadas) corrigidos, excluídas férias prop. e 1/3. Diferença 0,06. |
| Ex.4, p.285 | Soma 'Dif. INSS a ser descontada' | 123,09 | 123,08 | Três linhas divergem 0,01 (dez/07 4,79 vs 4,78; mar/08 5,59 vs 5,60; jul/08 4,76 vs 4,75) — encadeamento em precisão plena. |
| Ex.4, p.285 | Soma 'INSS recda' | 324,94 | 324,96 | Soma das linhas impressas. |
| Ex.6, p.293/294 | Base das custas de execução | 16.328,35 | 16.328,65 (com multa) ou 15.812,39 (sem multa) | Nenhuma das duas composições reproduz 16.328,35. As custas (81,64) batem com 16.328,35 × 0,5% e também com 16.328,65 × 0,5%. Dife… |
| Ex.6, p.294 | Soma dos juros Selic cota recte | 101,94 | 101,93 | Soma das 13 linhas impressas. |
| Ex.7, p.295 | Total do recte | 25.051,50 | 25.051,49 (dos valores impressos) / 25.051,48 (precisão plena) | 24.656,98 × 1,6% = 394,5117. |
| Ex.8, p.297 | Total bruto (ambos os métodos) | 218.238,02 | 218.238,01 | Diferença 0,01 nas duas variantes. |
| Ex.8, p.297 | Total líquido do recte | 214.935,90 | 214.935,91 | 218.238,02 − 3.302,11. |
| Ex.8, p.298 | Total geral | 292.265,29 | 292.265,28 | Soma das 8 linhas do resumo. |

## 5. Notas confrontadas contra as linhas que qualificam

20 notas conferidas.

| Nota | Estado | Atrito | Impacto |
|---|---|---|---|
| Ex.1, obs.2 (p.279) | **ATRITO** | período laborado citado (10/11/09 a 08/09/15) diverge dos dados complementares (10/11/2009 a 25/07/15) | nenhum sobre o resultado (5 parcelas em qualquer hipótese) |
| Ex.1, rótulo da linha da multa 467 e item 'h' do dispositivo (p.278-279) | **ATRITO** | nenhum dos dois inclui saldo de salário nem a multa de 40% sobre o FGTS rescisório, mas a conta os inclui (ver E12) | 828,04 a mais na multa 467 em valores originais |
| Ex.1, rótulo do nº de meses do RRA (p.280) | **ATRITO** | '(fev/13 a set/13 + 1 mês 13º sal.)' é o rótulo do Exemplo 5, incompatível com o caso (período jul/15); valor impresso 2 | nenhum (alíquota 0% nas duas hipóteses) |
| Ex.1, cabeçalho 'Base INSS em vrs. Originais' (p.279) | **ATRITO** | contém 4.226,72 = base já corrigida | ver E02 |
| Ex.2, obs.1 (p.281) | **ATRITO** | nenhum — confere com a linha mai/15 (só 1/3 lançado: 52,53 = 157,60/3), coerente com a justificativa de evitar duplicidade | nenhum |
| Ex.2, obs.2 (p.281) | **ATRITO** | nenhum — a coluna '% de multa' é 0,00% em todas as 23 competências, coerente com a nota; a própria nota ressalva que 'há decisões determinando a… | nenhum |
| Ex.2, obs.3 (p.281) | **ATRITO** | nenhum — índice 1,00942193 aplicado só aos honorários | nenhum |
| Ex.4, obs.1 (p.286) | **ATRITO** | nenhum — confere: FGTS+40% = col. C × 0,112, sem o RSR; e as médias usam só o nº de HE, sem RSR | nenhum |
| Ex.4, obs.2 (p.286) | **ATRITO** | a nota diz que 'o fato gerador da contribuição previdenciária é o pagamento do crédito ao reclamante', mas a tabela apura o INSS competência a c… | não quantificado; contradição conceitual entre a justificativa e o mé… |
| Ex.4, cabeçalho 'INSS recda (21% s col. a)' (p.285) | **ATRITO** | a conta usa a col. d, não a col. a (ver i04) | sem a correção do rótulo, o leitor obtém 14,75 em vez de 13,49 na 1ª… |
| Ex.5, obs.1 e 2 (p.287) | **ATRITO** | nenhum — 'A hora relógio foi convertida em hora sexagesimal' com exemplos '3:00h = 3,00 / 2:30h = 2,5 (2 + 30/60)'; as colunas dos cartões de po… | nenhum |
| Ex.5, obs.3 (p.287) | **ATRITO** | nenhum — a coluna de multa não existe na tabela de INSS do Ex.5, coerente | nenhum |
| Ex.5, RESUMO 'Total custas execução 74,15' (p.287) | **ATRITO** | contradiz a linha 70,32 e o próprio TOTAL 14.134,33 | 3,83 |
| Ex.5, RESUMO 'Base de cálculo: R$ 6.885,06' (p.287) | **ATRITO** | a linha de apuração usa 6.119,43 (líquida de INSS) | nenhum (alíquota 0%), mas é o valor que vai para a DIRF |
| Ex.5, notas de rodapé da tabela (p.291) | **ATRITO** | nenhum — 'Base de cálculo HE = Sal.CCT', 'Vr. devido HE = Base de cálculo / 200 x 1,60 x número de HE' e 'Reflexo no FGTS + 40% = 11,2% ou 0,112… | nenhum |
| Ex.5, nota 'Base de cálculo contribuição previdenciária: diferença salarial, reflexos dif. sal… | **ATRITO** | nenhum — a coluna 'Base INSS déb. Trab.' = col. d + col. g + col. j confere em todas as linhas e as linhas de férias ficam em branco | nenhum |
| Ex.6, 'Obs.: Multa aplicada, tendo em vista que a reclamada já ultrapassou o prazo para pagame… | **ATRITO** | a multa está no demonstrativo mas foi retirada do RESUMO GERAL (ver E08) | 516,26 (148,26 + 368,00) |
| Ex.7, obs. sobre art. 103, §3º da IN/RFB 971/09 (p.295) | **ATRITO** | nenhum — justifica a competência abr/16 e o Selic 0,00% | nenhum |
| Ex.8, obs. sobre juros Selic acumulados (p.298) | **ATRITO** | o mecanismo descrito (taxa de ago/15 menos 1%) não é o mesmo enunciado na p.124 ('subtrair... a taxa acumulada posicionada nos dois meses anteri… | ver E16 |
| Ex.8, '( * ) Tabela prática consta no final deste manual' (p.298) | **ATRITO** | o asterisco não tem chamada correspondente no corpo do demonstrativo da p.297/298 | nenhum |

---

## 6. Juros vincendos — regras extraídas

**A.1** (`pagina_pdf` 95) — Juros vincendos, decrescentes e regressivos sao sinonimos e designam os juros que incidem sobre parcelas/verbas vincendas, de epoca propria posterior ao ajuizamento.

**A.2** (`pagina_pdf` 95) — O passo do decrescimo mensal e igual a propria taxa de juros mensal aplicavel ao periodo de apuracao; no mes do ajuizamento o decrescimo e proporcional aos dias.

**A.3** (`pagina_pdf` 95) — 

**A.4** (`pagina_pdf` 95) — 

**A.5** (`pagina_pdf` 95) — 

**A.6** (`pagina_pdf` 98) — 

## 7. Capítulo 15 — os oito itens

Numeração real: itens 1 a 8, numeracao simples, sem prefixo '15.'.

### Item 1 (`pagina_pdf` 307)

> 1 – Forma de apuração da multa do acordo, quando há várias parcelas (multa do acordo apenas sobre a parcela vencida e antecipação das demais, multa sobre o saldo devedor inclusive sobre parcelas vencidas e vincendas ou multa sobre o saldo devedor, considerando apenas as parcelas efetivamente em atraso até a data do despacho para o cálculo ou do requerimento do reclamante para a execução do acordo, excluindo as vincendas).

- **No cálculo:** Fixa a base de incidencia da multa do acordo. O manual apresenta TRES variantes, sem eleger uma: (a) multa apenas sobre a parcela vencida, com antecipacao das demais; (b) multa sobre o saldo devedor, incluindo parcelas vencidas e vincendas; (c) multa sobre o saldo devedor considerando apenas as parcelas efetivamente em atraso ate a data do despacho para o calculo ou do requerimento do reclamante para execucao do acordo, excluindo as vincendas.
- **Fundamento:** Nao indicado. O item e fundamentado apenas na pratica (justificativa).

### Item 2 (`pagina_pdf` 307)

> 2 - Discriminação das parcelas sobre as quais incide a multa do art. 467.

- **No cálculo:** Que a sentenca discrimine expressamente sobre quais parcelas incide a multa do art. 467 da CLT, delimitando a base de calculo. Pontos controvertidos apontados: FGTS nao recolhido no curso do contrato, ferias indenizadas e decimos terceiros nao quitados no curso do pacto laboral. O manual tambem registra como equivoco frequente a aplicacao da multa sobre TODAS as parcelas deferidas, inclusive as nao rescisorias (exemplifica: indenizacao salario familia, vale transporte, hora…
- **Fundamento:** art. 467 da CLT

### Item 3 (`pagina_pdf` 307)

> 3 – Fixação do critério de atualização e o fato gerador da contribuição previdenciária

- **No cálculo:** Que a decisao fixe o criterio de atualizacao e o fato gerador da contribuicao previdenciaria (competencia vs. pagamento), o que define a partir de quando incidem juros Selic e multa sobre o credito previdenciario.
- **Fundamento:** Sumula 45 do TRT-3a Regiao

### Item 4 (`pagina_pdf` 307)

> 4 – Responsabilidade pelo pagamento dos acréscimos legais da legislação previdenciária (juros Selic e multa) em relação à contribuição previdenciária cota reclamante, quando a incidência dos acréscimos ocorrer a partir da  efetiva prestação de serviço

- **No cálculo:** REGRA DE CALCULO EXPRESSA: do credito do reclamante deduz-se APENAS o valor da contribuicao previdenciaria ATUALIZADO. Os acrescimos legais (juros Selic e multa de 10% ou 20%) sobre a cota do empregado sao de responsabilidade EXCLUSIVA do reclamado e nao podem ser descontados do credito do exequente.
- **Fundamento:** art. 33, § 5o, da Lei 8.212/91 - a empresa e diretamente responsavel pela importancia que deixa de receber ou arrecadar em desacordo com a Lei 8.212/91

### Item 5 (`pagina_pdf` 308)

> 5 –  Juros na base de cálculo do imposto de renda

- **No cálculo:** Que a decisao se pronuncie expressamente sobre a inclusao ou exclusao dos juros de mora da base de calculo do imposto de renda. Sem pronunciamento judicial nos autos a Receita Federal tributa os juros; com pronunciamento (ou tratando-se de parcelas pagas no contexto da rescisao contratual) aceita a isencao.

### Item 5 (documento de apoio) (`pagina_pdf` [308, 309])


### Item 6 (`pagina_pdf` 308)

> 6 –Composição da base de cálculo das verbas deferidas (horas extras, adicional noturno e quinquênios, entre outras), quando o reclamante recebe durante o período contratual várias parcelas além do salário base

- **No cálculo:** Que a decisao fixe quais verbas integram a base de calculo de cada parcela deferida, quando o contrato contempla multiplas parcelas variaveis alem do salario base.
- **Fundamento:** Nao indicado (remete genericamente a 'leis federais, estaduais ou municipais especificas' que instituem as parcelas).

### Item 7 (`pagina_pdf` 308)

> 7 – Discriminação das parcelas salariais e indenizatórias do acordo para fins de cálculo do imposto de renda.

- **No cálculo:** REGRA SUPLETIVA EXPRESSA: se o acordo nao indicar as verbas pagas, os respectivos valores e o periodo correspondente, o imposto de renda incide sobre o TOTAL da avenca, observados a base de calculo e as aliquotas vigentes nos meses dos pagamentos das parcelas do acordo. Havendo discriminacao, o valor tributavel pode situar-se na faixa de isencao pela regra do art. 12-A, nao havendo IR a apurar.
- **Fundamento:** art. 12-A da Lei 7.713/88; Instrucao Normativa no 1500/14 da Secretaria da Receita Federal do Brasil

### Item 8 (`pagina_pdf` 309)

> 8 – Fixação do valor máximo da multa diária arbitrada por descumprimento de obrigação de fazer (assinatura e entrega de CTPS, entrega de perfil profissiográfico, entre outras), se houver a intenção de limitar a sua apuração.

- **No cálculo:** Que a decisao fixe desde logo o teto da multa diaria (astreintes) quando houver intencao de limita-la. Sem o teto, e havendo posterior determinacao de limitacao nos termos do art. 412 do Codigo Civil, o calculista nao tem parametro para determinar o valor da obrigacao principal e a apuracao fica impossibilitada ate novas diretrizes.
- **Fundamento:** art. 412 do Codigo Civil

---

## 8. Capítulo 17 — achados de extração

O índice completo está em `../../jurisprudencia-indice.md`. Aqui só o que é defeito ou divergência, preservado como está.

### 8.1 Verbetes cuja verificação literal não fechou

| Verbete | Veredicto | Nota |
|---|---|---|
| Súmula 437 (TST) | literal-atravessa-folha | 90% casado; quebra exatamente no folio "349" impresso no meio da frase. Conferido a olho: é literal, partido entre pp.348-349. |
| OJ SDI-1 397 (TST) | NAO-LOCALIZADA | ACHADO: a ementa não foi localizada no PDF na forma gravada. A p.351 traz outro verbete no ponto declarado. "remuneração mista" ocorre nas pp.351 e 354. Pendência P10-17. |
| Súmula 45 (TRT-3) | literal-atravessa-folha | Início casa 100% na p.359. O restante segue na folha seguinte. |
| Parecer Parecer Normativo COSIT nº 25, de 05/12/2013 (RFB — Secretaria da Receita Federal do Brasil) | literal-atravessa-folha | Ementa longa, pp.369-372, com folios no meio. O manual a imprime DUAS VEZES seguidas — registrado, não corrigido. |

### 8.2 Páginas corrigidas pela verificação literal

O script localizou onde cada ementa de fato está. Dez atribuições estavam erradas.

| Verbete | Declarava | Está em |
|---|---|---|
| Súmula 102 (TST) | 338 | **339** |
| Súmula 132 (TST) | 337 | **338** |
| Súmula 199 (TST) | 339 | **346** |
| Súmula 314 (TST) | 347 | **348** |
| Súmula 401 (TST) | 340 | **341** |
| OJ SDI-1 54 (TST) | 355 | **356** |
| OJ SDI-1 103 (TST) | 350 | **351** |
| OJ SDI-1 198 (TST) | 353 | **354** |
| OJ SDI-1 410 (TST) | 356 | **357** |
| Súmula 27 (TRT-3) | 360 | **361** |

