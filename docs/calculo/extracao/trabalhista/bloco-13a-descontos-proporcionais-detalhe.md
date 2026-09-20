# Bloco 13 — detalhe

Companheiro de `bloco-13a-descontos-proporcionais.md`, `bloco-13b-encargos.md`,
`bloco-13c-sindical-precatorios.md` e `bloco-13e-capitulo16.md`.

Material bruto das três frentes do último bloco de extração. Gerado por script a partir de
`cap10_2b.json`, `cap8_12_14.json` e `cap16.json`. **Offset de paginação zero.**

---

## A. Capítulo 10, segmento B — descontos proporcionais

### A.1 Fronteiras

- **confirmadas:** True
- **inicio:** pagina_pdf: 223; offset: 2658; texto_inicial: 10.2  Descontos previdenciários e fiscais proporcionais
- **fim:** pagina_pdf: 237; offset: 681; texto_seguinte: 10.3 Atualização com amortização de valor  pago
- **offset paginacao:** 0
- **metodo:** PyMuPDF doc[pagina-1].get_text(), encoding utf-8
- **chars extraidos:** 39656
- **observacao:** Ambas as fronteiras conferidas literalmente. Nenhuma premissa do enunciado precisou de correção quanto a fronteiras.

### A.2 Estrutura

- **confirmada:** os 7 subitens do enunciado conferidos um a um; nenhum subitem adicional existe no intervalo
**itens**

- id: 10.2; titulo: Descontos previdenciários e fiscais proporcionais; pagina_pdf: 223
- id: 10.2.1; titulo: Critérios - Art. 12-A da Lei 7713/88 e  arts. 36 a 42 e 45 da IN RFB 1500/14; pagina_pdf: 224
- id: 10.2.1.1; titulo: Metodologia de apuração — INCLUSÃO dos juros na base de cálculo do IR; pagina_pdf: 224; letras: A a J + quadro de verificação; fim_pagina_pdf: 228
- id: 10.2.1.2; titulo: Metodologia de apuração — EXCLUSÃO dos juros da base de cálculo do IR; pagina_pdf: 228; letras: A a J + quadro de verificação; fim_pagina_pdf: 233
- id: 10.2.2; titulo: Critérios - Art. 12-B da Lei 7713/88 e arts. 26, 44 e 45 da IN/RFB 1500/14; pagina_pdf: 233
- id: 10.2.2.1; titulo: Metodologia — INCLUSÃO dos juros na base do IR (12-B); pagina_pdf: 233; letras: A a H; fim_pagina_pdf: 235
- id: 10.2.2.2; titulo: Metodologia — EXCLUSÃO dos juros da base do IR (12-B); pagina_pdf: 235; letras: A a H; fim_pagina_pdf: 237

**exemplos**

- ref: 10.2 preambular; pagina_pdf: 224; tipo: levantamento coincidente com o líquido de cálculo já existente nos autos; valores: bruto 348.005,30 / INSS 409,44 / IR 18.725,00 / líquido 328.870,86; conferido: 348.005,30 - 409,44 - 18.725,00 = 328.870,86 exato
- ref: 10.2.1.1; paginas_pdf: 224-228; levantamento: 282.500,00 em 25/10/11; bruto_reconstituido: 322.389,94; inss_prop: 1.464,26; ir_prop: 38.425,68
- ref: 10.2.1.2; paginas_pdf: 229-233; levantamento: 282.500,00 em 25/10/11; bruto_reconstituido: 297.402,53; inss_prop: 1.350,77; ir_prop: 13.551,75
- ref: 10.2.2.1; paginas_pdf: 233-235; levantamento: 4.233,42 em 26/03/12; bruto_reconstituido: 4.795,71; inss_prop: 0,00; ir_prop: 562,29
- ref: 10.2.2.2; paginas_pdf: 235-237; levantamento: 4.233,42 em 26/03/12; bruto_reconstituido: 4.407,73; inss_prop: 0,00; ir_prop: 174,31


### A.3 Distribuição de INSS e IR

- **pergunta:** Como INSS e IR se distribuem quando o pagamento é parcial?
- **resposta sintetica:** Nenhum dos dois é rateado diretamente. O manual INVERTE a ordem: primeiro reconstitui o VALOR BRUTO correspondente ao líquido levantado (fórmula fechada, letra G no 12-A / letra D no 12-B); só depois (i) ratea o INSS proporcionalmente a esse bruto e (ii) RECALCULA o IR do zero sobre a base proporcional.
**INSS**

- **criterio:** rateio proporcional linear tendo o BRUTO como base
- **citacao literal:** -dividir o valor bruto levantado pelo total bruto devido ao recte na data da amortização e multiplicar pelo valor da contribuição social devida na data do levantamento
- **paginas pdf:** 227; 232; 234; 236
- **formula:** INSSprop = (VR_BRUTO_LEVANTADO / TOTAL_BRUTO_DEVIDO) x INSS_devido_na_data_do_levantamento
- **aplica a:** cota reclamante E cota reclamada
- **ressalva literal:** Obs.: Se o fato gerador contribuição previdenciária for a prestação de serviço, não será necessário fazer esta operação em relação à contribuição previdenciária cota reclamada, visto que o seu valor será atualizado a parte.
- **paginas da ressalva:** 228; 232
- **ressalva correlata p224:** Se o fato gerador da contribuição previdenciária for a prestação de serviço, o cálculo do INSS proporcional será efetuado apenas em relação à cota do reclamante para fins de dedução do crédito do autor e da base de cálculo do imposto de renda.
- **conferido:** 322.389,94/412.023,32 x 1.871,37 = 1.464,26 \| x 49.281,25 = 38.560,39 \| 297.402,53/412.023,32 x 1.871,37 = 1.350,77 \| x 49.281,25 = 35.571,70 — todos delta 0,00

**IR**

- **criterio:** NÃO é rateado. É integralmente RECALCULADO sobre a base proporcional, com alíquota e parcela a deduzir da tabela vigente no mês do levantamento.
- **citacao literal base:** Base de cálculo IR prop. ao valor levantado  = Total bruto em relação ao valor levantado X índice parcelas passíveis IR – INSS proporcional ao valor levantado
- **pagina pdf base:** 228
- **sob 12A:** a parcela a deduzir é multiplicada pelo NMP (nº de meses PROPORCIONAL ao levantamento): "Parcela a deduzir multiplicada pelo número de meses proporcional ao valor levantado (723,95425 x 48,5)" = 35.111,78 (p.228)
- **sob 12B:** parcela a deduzir única, sem multiplicação por meses: "Valor imposto de renda = 4.795,71 x 0,275 – 756,53 = 562,29 (aplicando a tabela vigente em mar/12)" (p.234)
- **ordem de dependencia:** o INSS proporcional é insumo da base do IR proporcional; logo o INSS é apurado ANTES do IR (letra H antes da letra I)

**fundamento da proporcionalizacao**

- **no segmento B:** NENHUM dispositivo é citado como fundamento do rateio. Todas as citações normativas do segmento são de METODOLOGIA de IR: art.12-A, art.12-B, IN/RFB 1127/11, IN/RFB 1500/14 arts.36 a 42 e 45 (12-A) e 26, 44 e 45 (12-B).
- **busca que sustenta:** no segmento 223-237: 'art. 56'=0, '§ 1'=0, 'Decreto nº 3000'=0, '3000/99'=0, 'art. 354'=0 (art. 354 = 0 ocorrências nas 471 páginas)
- **fundamento existe mas fora do segmento:** cap.9, pagina_pdf 186: "o imposto de renda  não poderá incidir  sobre o total devido ao reclamante, mas apenas sobre a parte efetivamente disponível, conforme art. 12-A, § 1º e art. 12-B  da Lei 7713/88 e  art. 56 do Decreto nº 3000, de 26/03/99 (Regulamento do Imposto de Renda)."
- **lacuna residual:** esse fundamento cobre a proporcionalidade do IR; nada no manual fundamenta a proporcionalidade do INSS


### A.4 Critério de rateio

- **pergunta:** O desconto proporcional segue a MESMA regra de rateio da amortização, ou tem critério próprio? Com que fundamento?
- **resposta:** CRITÉRIO PRÓPRIO, com base de rateio diferente. Não é a mesma regra.
**comparacao**

- **amortizacao 10.3 segmento C:** rateia o VALOR PAGO entre principal e juros: principal_no_saldo=(B/D)xE, juros_no_saldo=(C/D)xE. Objeto do rateio = composição principal/juros do saldo.
- **desconto 10.2 segmento B:** rateia o BRUTO RECONSTITUÍDO contra o BRUTO TOTAL e aplica esse quociente único SOMENTE ao INSS. O IR não é rateado: é recalculado. Objeto do rateio = VR_BRUTO_LEVANTADO / TOTAL_BRUTO_DEVIDO.

- **bases sao as mesmas:** False
**duas proporcoes no mesmo exemplo**

- **descricao:** Nos ramos 'sem juros' (10.2.1.2 e 10.2.2.2) o manual usa DUAS proporções distintas dentro do mesmo exemplo
- **proporcao 1:** VB/TB — para ratear o INSS
- **proporcao 2:** TBSJ/TBCJ (principal corrigido / bruto com juros) — para expurgar os juros da base do IR
- **citacao literal:** Valor bruto levantado sem juros   = 297.402,53 X 276.667,36 / 412.023,32 = 199.701,25
- **pagina pdf:** 232
- **analogo 12B:** Valor bruto levantado, excluindo a proporção dos juros: 4.407,73 (total bruto em relação ao levantamento) x 18.000,00  (principal devido até a data do levantamento) / 24.736,40 (total bruto com juros até a data do levantamento) = 3.207,38 (p.236)

- **fundamento:** NENHUM no segmento B — mesma lacuna do segmento C. Busca: 'art. 354' = 0 ocorrências nas 471 páginas; '354' aparece em 23 páginas, todas como número de página ou valor monetário, e 0 vezes no segmento 223-237.
- **conclusao:** A premissa do enunciado (rateio proporcional sem fundamento normativo citado) CONFIRMA-SE também no segmento B. Mas os objetos rateados são distintos — em 10.3 principal/juros, em 10.2 bruto→INSS — de modo que não há conflito numérico entre as duas regras; há apenas a mesma ausência de fundamentação.

### A.5 Art. 12-A contra 12-B

**12A**

- **rubrica literal:** 10.2.1  Critérios - Art. 12-A da Lei 7713/88 e  arts. 36 a 42 e 45 da IN RFB 1500/14
- **pagina pdf:** 224
- **hipotese literal:** -Cálculo envolvendo rendimentos referente a anos-calendário anteriores ao recebimento e submetidos à incidência do imposto sobre a renda com base na tabela progressiva (regime especial de tributação).
- **paginas da hipotese:** 224; 228
- **base:** total bruto na data do levantamento x IPIR − INSS cota recte (ramo com juros); ou principal corrigido x IPIR − INSS (ramo sem juros)
- **aliquota:** da faixa em que se situa a BASE MENSAL = base / nº de meses
- **meses:** NMT total e NMP proporcional; a parcela a deduzir é multiplicada pelo nº de meses
- **codigo de recolhimento:** NÃO informado no segmento B ('código' = 0 ocorrências em 223-237)

**12B**

- **pendencia 11C resolvida:** True
- **rubrica literal:** 10.2.2 Critérios - Art. 12-B da Lei 7713/88 e arts. 26, 44 e 45 da IN/RFB 1500/14
- **pagina pdf:** 233
- **ocorrencias da string no segmento:** 2
- **paginas com a string:** 224; 233
- **hipotese literal:** - Cálculo envolvendo apenas rendimentos referentes ao ano-calendário do recebimento, rendimentos pagos por entidades de previdência complementar e liberados ao reclamante até 10/03/15 e rendimentos pagos em cumprimento da decisão da Justiça do Trabalho e que não se enquadram ao disposto no art. 12-A da Lei 7713/88
- **paginas da hipotese:** 233; 235
- **segunda citacao literal:** é necessário verificar se o cálculo abrange rendimentos passíveis de tributação nos termos do art. 12-A da Lei 7713/88 ou pelo regime geral do art. 12-B do mesmo diploma legal
- **pagina segunda citacao:** 224
- **base:** VR_BRUTO_LEVANTADO x IPIR − INSS proporcional (ramo com juros); ou VR_BRUTO_LEVANTADO x (Principal/TBCJ) x IPIR − INSS (ramo sem juros)
- **aliquota:** tabela progressiva MENSAL do mês do pagamento, aplicada diretamente à base integral (27,5% no ex. 10.2.2.1; 15% no ex. 10.2.2.2)
- **parcela a deduzir:** única, NÃO multiplicada por número de meses (756,53 e 306,80 nos exemplos)
- **numero de meses:** inexistente no regime 12-B — confirma integralmente o achado do segmento D
- **codigo de recolhimento:** NÃO informado no segmento B. Busca: 'código'=0 e '5936'=0 em 223-237. O código 5936 para o 12-B consta apenas do cap.9, pagina_pdf 207: "foi informado o código de recolhimento 5936, tendo em vista que não houve discriminação do período pago. Dessa forma, o imposto de renda foi calculado na forma do art. 12-B da Lei 7713/88 e arts. 26 e 44 da IN/RFB 1500/14"
- **como se distingue do 12A:** exclusivamente pelo ENUNCIADO de hipótese (ano-calendário do recebimento vs anos anteriores) e, na mecânica, pela ausência total de número de meses: no 12-A a PD é multiplicada por NMP e a faixa é determinada pela base MENSAL; no 12-B a PD entra uma vez e a faixa é determinada pela base INTEGRAL. Nenhum outro critério operacional é dado no segmento.

**divergencia de citacao normativa**

- **descricao:** O cabeçalho 10.2.2 (p.233) cita 'arts. 26, 44 e 45 da IN/RFB 1500/14'. O cap.9, p.190, cita para o mesmo art.12-B 'arts. 26 , 43 e 44  da IN/RFB nº 1500/14'. O art.45 da IN 1500/14 é a regra de arredondamento do nº de meses do RRA, que o próprio manual diz não existir no 12-B ('sem qualquer multiplicação pelos números de meses', p.190).
- **busca:** 'arts. 26, 43' = 0 páginas com essa grafia exata; 'arts. 26, 44' = pp. 6, 233, 275
- **classificacao:** citação normativa inconsistente entre capítulos do mesmo manual


### A.6 Relação com o capítulo 9

- **ha sobreposicao:** False
- **natureza da relacao:** DELEGAÇÃO EXPLÍCITA do cap.9 para o item 10.2
- **citacao chave:** 9.3.12  Imposto de renda proporcional ao valor pago — O cálculo do imposto de renda proporcional ao valor pago será detalhado no item 10.2.
- **pagina pdf citacao:** 207
- **divisao de trabalho:** cap.9 (pp.107-208) define hipóteses de incidência, tabelas, alíquotas, bases, códigos de recolhimento e o FUNDAMENTO da proporcionalidade (p.186). O item 10.2 fornece apenas a ÁLGEBRA da proporcionalização, isto é, a reconstituição do bruto a partir do líquido levantado.
- **consistencia de criterio:** O cap.9 já usa o MESMO desenho proporcional em outro contexto: rateio do nº de meses entre parcelas de acordo — "(2.250,00 / 10.000,00) x 34 = 7,7" (p.203) — e igualmente sem fundamento citado. Portanto o critério proporcional é consistente entre cap.9 e cap.10.
**divergencias encontradas**

- citação da IN 1500/14 para o 12-B: 'arts. 26, 44 e 45' (p.233) vs 'arts. 26 , 43 e 44' (p.190)
- o fundamento normativo da proporcionalidade está só no cap.9 (p.186) e não é repetido nenhuma vez em 10.2
- o critério de escolha entre base com juros e base sem juros (OJ 400) está no cap.9 e não é mencionado em 10.2 — 'OJ' = 0 ocorrências em 223-237

- **divergencia de criterio de calculo:** NENHUMA. As divergências são de citação normativa e de completude, não de método.

### A.7 Migração de regime

- **pergunta:** O segmento B disciplina a migração de regime tributário dentro do mesmo cálculo (Ex.5 do segmento D: levantamento pelo regime geral, saldo pelo 12-A por causa de 11/03/15)?
- **resposta:** NÃO.
**buscas que sustentam a negativa**

- **migra*:** 0 ocorrências nas 471 páginas do PDF
- **transição / transicao:** 0 ocorrências nas 471 páginas
- **dois regimes:** 0 ocorrências nas 471 páginas
- **duas apuraç*:** 0 no segmento 223-237; 1 página no documento inteiro (p.190, cap.9)
- **11/03/15:** 0 no segmento; documento: pp. 187, 188, 190, 191, 193, 269
- **10/03/15:** 2 no segmento (pp. 233 e 235), somente dentro do enunciado da hipótese do 12-B, nunca como marco de transição
- **IN RFB 1558/15:** 0 no segmento; documento: pp. 187, 188, 190, 191, 193

**o que existe de mais proximo**

- **pagina pdf:** 190
- **citacao:** Se houver rendimentos correspondentes ao ano atual do recebimento e de anos anteriores, será necessário efetuar duas apurações distintas
- **por que nao serve:** é regra de CISÃO por ano-calendário dentro de um mesmo cálculo, não regra de transição de regime entre pagamentos sucessivos ao longo do tempo

- **conclusao:** A pendência herdada do segmento D permanece ABERTA. O Exemplo 5 continua sendo caso único do manual, sem enunciado disciplinador em nenhum capítulo.

### A.8 As pendências do bloco 11B

**P11B-02**

- **status:** RESOLVIDA — e a premissa do enunciado NÃO se confirma
- **achado:** O segmento B DECLARA expressamente a regra de arredondamento do NMP e transcreve o texto normativo por inteiro, duas vezes.
- **paginas pdf:** 226; 230
- **citacao literal:** Na apuração do número de meses, deverá ser observada a regra de arredondamento prevista no parágrafo único do 45 da Instrução Normativa 1500/14 (art. 10 da Instrução Normativa RFB nº 1127/11, incluído pela IN RFB Nº 1145/11,  vigente até 29/10/14).
- **regra transcrita:** IN 1500/14 art.45 p.ú.: resultado em 1 casa decimal; observa-se a 2ª casa: I) menor que 5 mantém; II) maior que 5 soma uma unidade; III) igual a 5 analisa-se a 3ª casa — 0 a 4 mantém, 5 a 9 soma uma unidade
- **nao e ROUND HALF UP:** A regra DIFERE de ROUND_HALF_UP no intervalo x,y50 a x,y54, em que half-up arredondaria para cima e a IN manda MANTER. Deve ser implementada literalmente, não como HALF_UP.
- **conferencia nos exemplos:** NMP 10.2.1.1 = 282.500,00/361.054,19 x 62 = 48,510723556483308 -> 48,5 (impresso 48,5). NMP 10.2.1.2 = 282.500,00/391.415,49 x 62 = 44,747845824905908 -> 44,7 (impresso 44,7). Ambos coincidem sob as duas regras; os exemplos não discriminam entre elas.
- **onde a nota existe no doc:** 'arredond*' aparece nas pp. 226, 230, 243, 250, 257 — existe em 10.2 e em 10.3; o segmento D (Ex.5-6) não a reproduz porque o regime 12-B não tem contagem de meses

**P11B-03**

- **status:** PREMISSA REFUTADA
- **achado:** 0,9091 NÃO é percentual de imposto de renda. É o ÍNDICE DAS PARCELAS PASSÍVEIS DE IR (IPIR) do exemplo de 10.3, papel exatamente análogo ao 0,8340 usado em 10.2.
- **evidencia p244 formula:** VR. BRUTO LEVANTADO = [32.454,00 – (293,5845 x 11,1)] / { 1 – [(64.166,50 x 0,9091 – 3.410,34)  x  22,5% / 64.166,50]  + (3.410,34 / 64.166,50)} =35.670,95
- **evidencia p244 rotulo:** 35.670,95 (total bruto em relação ao valor levantado) x  0,9091(índice parcelas passíveis IR)  – 1.895,85(INSS proporcional ao valor levantado) = 30.532,61
- **no segmento B:** '0,9091'/'9091' = 0 ocorrências em 223-237. O IPIR do exemplo de 10.2 é 0,8340. As alíquotas usadas são sempre plenas: 27,5% e 22,5% (12-A), 27,5% e 15% (12-B).
- **conclusao:** Não existe o contraste 'alíquota plena no saldo vs 0,9091 no levantamento'. A pendência deve ser fechada como erro de leitura de rótulo no segmento C.

**P11B-04**

- **status:** REAPARECE, MAS AQUI É DECLARADA, NÃO ACIDENTAL
- **achado:** O segmento B transforma a inclusão/exclusão dos juros na base do IR numa BIFURCAÇÃO EXPLÍCITA de subitem, com duas metodologias completas e paralelas para cada regime.
- **evidencia:** p.224, 10.2.1.1: "-Inclusão dos juros na base de cálculo do IR."; p.228, 10.2.1.2: "-Exclusão dos juros da base de cálculo do IR."; p.233, 10.2.2.1: "-Inclusão dos juros na base de cálculo do IR."; p.235, 10.2.2.2: "-Exclusão dos juros na base de cálculo do IR."
- **efeito numerico 12A:** mesmo levantamento de 282.500,00: bruto 322.389,94 (com juros) vs 297.402,53 (sem juros); IR 38.425,68 vs 13.551,75; diferença de IR = 24.873,93
- **efeito numerico 12B:** mesmo levantamento de 4.233,42: bruto 4.795,71 vs 4.407,73; IR 562,29 vs 174,31; diferença de IR = 387,98
- **o que o segmento NAO faz:** não diz QUANDO aplicar cada ramo. A OJ 400 não é citada uma única vez em 223-237 (busca: 'OJ' = 0 no segmento; OJ 400 aparece em 21 páginas do documento, nenhuma entre 223 e 237).
- **conclusao:** A variação de base de IR observada entre os exemplos dos segmentos C e D é a projeção desta bifurcação declarada em 10.2 — é um parâmetro do método, não um defeito. O defeito residual é a ausência, dentro do capítulo 10, de regra de seleção do ramo.


### A.9 Divergências entre exemplos

**internas ao segmento**

- 10.2.1.1 vs 10.2.1.2: mesmos dados de entrada (levantamento 282.500,00 em 25/10/11, mesmo cálculo-base de 30/06/10), resultados diferentes por construção. Coerente.
- 10.2.2.1 vs 10.2.2.2: mesmos dados (4.233,42 em 26/03/12, bruto 24.736,40, IPIR 100%), brutos 4.795,71 vs 4.407,73. Coerente por construção.
- IPIR 0,8340 apurado de duas formas: em 10.2.1.1 = 302.432,14/362.635,86 = 0,833982993...; em 10.2.1.2 = 227.238,16/272.473,37 = 0,833983005...; bases diferentes, mesmo índice a 4 casas. Coerente.
- Formato do quadro de verificação: 10.2.1.x usa 4 linhas (A-D); 10.2.2.x usa 6 linhas (A-F, acrescentando percentual e base de IR). Assimetria de formato sem efeito numérico.
- Os itens 10.2.2.1 e 10.2.2.2 não demonstram numericamente as letras A, B e C (o exemplo só começa na letra D), ao contrário de 10.2.1.x, que demonstra todas.

**contra segmento C**

- A fórmula de VR. BRUTO LEVANTADO de 10.2.1 é reproduzida IDÊNTICA em 10.3 (pp.244 e 250), inclusive com o MESMO defeito de colchete no termo (INSS/TB) — ver defeito D-01.
- O NMP e a regra de arredondamento da IN 1500/14 art.45 p.ú. são os mesmos (pp.226/230 e 243/250) — o segmento C herda a metodologia do segmento B.
- O rótulo 'Nº de meses referente ao RRA sobre o saldo remanescente' é a MESMA string nas pp.226, 230, 243 e 250: correto em 243/250 (10.3, onde há saldo), incorreto em 226/230 (10.2, onde não há).

- **contra segmento D:** Confirma integralmente: no regime 12-B não há número de meses nem NMP; a parcela a deduzir entra uma única vez.; O segmento B nomeia o art.12-B literalmente (pp.224 e 233), suprindo a paráfrase identificada no segmento D.
- **conclusao:** Os exemplos concordam entre si e com os dos segmentos C e D. Não foi encontrada nenhuma divergência de método entre segmentos; as diferenças observadas decorrem de parâmetros declarados (com/sem juros, 12-A/12-B).

### A.10 Aritmética

- **metodo:** decimal.Decimal, getcontext().prec=50, ROUND_HALF_UP, nenhum float em nenhuma etapa
- **operacoes verificadas:** 44
- **conclusao geral:** Todas as operações fecham com delta 0,00 quando a cadeia é executada em PRECISÃO PLENA, com UMA exceção de origem identificada (índice de juros impresso arredondado, delta 0,66) e UM erro estrutural de fórmula (colchete/sinal), que não é erro aritmético mas de redação.
- **prova de precisao plena:** a cadeia completa de 10.2.1.1 e de 10.2.1.2, executada em precisão plena a partir dos dados de entrada, devolve EXATAMENTE 282500.00000000000000000000000000 como líquido levantado, sem casas residuais. Isso prova que os impressos de 2 casas não são os operandos. Caso concreto: o IR de 10.2.1.2 calculado com operandos impressos dá 13.551,75575 (half-up 13.551,76), mas em cadeia plena dá 13.551,753602516279 -> 13.551,75, que é exatamente o impresso.
**10.2.1.1**

- item: A principal corrigido; conta: 272.473,37 x 1,0153923; exato: 276667.361853051; impresso: 276.667,36; delta: 0,00
- item: A juros corrigido; conta: 90.162,49 x 1,0153923; exato: 91550.298094827; impresso: 91.550,30; delta: 0,00
- item: A juros s/ o principal; conta: 276.667,36 x 0,15833330; exato: 43805.656111088; impresso: 43.805,66; delta: 0,00
- item: A total do recte; conta: soma das três linhas; exato_plena: 412023.31635236567989830; exato_2casas: 412023.32; impresso: 412.023,32; delta: 0,00
- item: B INSS cota recte; conta: 1.843,00 x 1,0153923; exato: 1871.3680089; impresso: 1.871,37; delta: 0,00
- item: B INSS cota recda; conta: 48.534,20 x 1,0153923; exato: 49281.25296666; impresso: 49.281,25; delta: 0,00
- item: C soma das parcelas passíveis; conta: 300.589,14 + 1.843,00; exato: 302432.14; impresso: 302.432,14; delta: 0,00
- item: C IPIR; conta: 302.432,14 / 362.635,86; exato: 0.83398299329801525972; impresso: 0,8340 ou 83,40%; delta: 0,00 a 4 casas
- item: E base de cálculo IR; conta: 412.023,32 x 0,8340 − 1.871,37; exato: 341756.07888; impresso: 341.756,08; delta: 0,00
- item: E base mensal; conta: 341.756,08 / 62; exato: 5512.19483870968; impresso: 5.512,19; delta: 0,00
- item: E parcela a deduzir x 62; conta: 723,95425 x 62; exato: 44885.1635; impresso: 44.885,16; delta: 0,00
- item: E IR devido; conta: 341.756,08 x 0,275 − 44.885,16; exato: 49097.762; impresso: 49.097,76; delta: 0,00
- item: E total líquido devido; conta: 412.023,32 − 1.871,37 − 49.097,76; exato: 361054.19; impresso: 361.054,19; delta: 0,00
- item: F NMP; conta: 282.500,00 / 361.054,19 x 62; exato: 48.510723556483307949; impresso: 48,5; delta: 0,00
- item: G vr. bruto levantado; conta: ver defeito D-01; exato_com_sinal_corrigido: 322389.94380710833671; exato_leitura_literal: 318618.21091754822860; impresso: 322.389,94; delta: 0,00 com sinal corrigido; −3.771,73 na leitura literal
- item: G base mensal p/ faixa; conta: (282.500,00 x 0,8340) / 48,5; exato: 4857.83505154639175; impresso: 4.857,84; delta: 0,00
- item: H INSS recte prop.; conta: 322.389,94 / 412.023,32 x 1.871,37; exato: 1464.26387229198580; impresso: 1.464,26; delta: 0,00
- item: H INSS recda prop.; conta: 322.389,94 / 412.023,32 x 49.281,25; exato: 38560.38835526348363; impresso: 38.560,39; delta: 0,00
- item: I base IR prop.; conta: 322.389,94 x 0,8340 − 1.464,26; exato: 267408.94996; impresso: 267.408,95; delta: 0,00
- item: J base mensal; conta: 267.408,95 / 48,5; exato: 5513.58659793814433; impresso: 5.513,59; delta: 0,00
- item: J PD x NMP; conta: 723,95425 x 48,5; exato: 35111.781125; impresso: 35.111,78; delta: 0,00
- item: J IR proporcional; conta: 267.408,95 x 0,275 − 35.111,78; exato: 38425.68125; impresso: 38.425,68; delta: 0,00
- item: Verificação (A−B−C=D); conta: 322.389,94 − 1.464,26 − 38.425,68; exato: 282500.00; impresso: 282.500,00; delta: 0,00

**10.2.1.2**

- item: C parcelas passíveis IR sem juros; conta_impressa: (300.589,14 + 1.843,00) / 1,3309; exato_com_divisor_impresso: 227238.815838906; impresso: 227.238,16; delta: +0,66; diagnostico: o divisor real não é 1,3309 e sim 362.635,86/272.473,37 = 1.3309038604396459; com ele 302.432,14 / 1,3309038604396459 = 227238.15670659763 -> 227.238,16, delta 0,00; classificacao: arredondamento de planilha — origem identificada, NÃO é bloqueio
- item: C IPIR; conta: 227.238,16 / 272.473,37; exato: 0.83398300538507671410; impresso: 83,40%; delta: 0,00 a 4 casas
- item: E base de cálculo IR; conta: 276.667,36 x 0,8340 − 1.871,37; exato: 228869.20824; impresso: 228.869,21; delta: 0,00
- item: E base mensal; conta: 228.869,21 / 62; exato: 3691.43887096774194; impresso: 3.691,44; delta: 0,00
- item: E PD x 62; conta: 528,37275 x 62; exato: 32759.1105; impresso: 32.759,11; delta: 0,00
- item: E IR devido; conta: 228.869,21 x 0,225 − 32.759,11; exato: 18736.46225; impresso: 18.736,46; delta: 0,00
- item: E total líquido devido; conta: 412.023,32 − 1.871,37 − 18.736,46; exato: 391415.49; impresso: 391.415,49; delta: 0,00
- item: F NMP; conta: 282.500,00 / 391.415,49 x 62; exato: 44.747845824905907531; impresso: 44,7; delta: 0,00
- item: G vr. bruto levantado; conta: ver defeito D-02; exato_com_sinal_corrigido: 297402.52706620245869; exato_leitura_literal: 294331.05067893563582; impresso: 297.402,53; delta: 0,00 com sinal corrigido; −3.071,48 na leitura literal
- item: G base mensal p/ faixa; conta: (276.667,36 / 412.023,32 x 282.500,00 x 0,8340) / 44,7; exato: 3539.26522059560990; impresso: 3.539,27; delta: 0,00
- item: H INSS recte prop.; conta: 297.402,53 / 412.023,32 x 1.871,37; exato: 1350.77347701120412; impresso: 1.350,77; delta: 0,00
- item: H INSS recda prop.; conta: 297.402,53 / 412.023,32 x 49.281,25; exato: 35571.69635826074116; impresso: 35.571,70; delta: 0,00
- item: I vr. bruto levantado sem juros; conta: 297.402,53 x 276.667,36 / 412.023,32; exato: 199701.25193986786961; impresso: 199.701,25; delta: 0,00
- item: I base IR prop.; conta: 199.701,25 x 0,8340 − 1.350,77; exato: 165200.0725; impresso: 165.200,07; delta: 0,00
- item: J base mensal; conta: 165.200,07 / 44,7; exato: 3695.75100671140940; impresso: 3.695,75; delta: 0,00
- item: J PD x NMP; conta: 528,37275 x 44,7; exato: 23618.261925; impresso: 23.618,26; delta: 0,00
- item: J IR proporcional; conta: 165.200,07 x 0,225 − 23.618,26; exato_operandos_impressos: 13551.75575 -> half-up 13.551,76; exato_cadeia_plena: 13551.753602516278754 -> 13.551,75; impresso: 13.551,75; delta: 0,00 em cadeia plena; +0,01 se usados os impressos
- item: Verificação (A−B−C=D); conta: 297.402,53 − 1.350,77 − 13.551,75; exato_operandos_impressos: 282500.01; exato_cadeia_plena: 282500.00000000; impresso: 282.500,00; delta: 0,00 em cadeia plena

**10.2.2.1**

- item: D vr. bruto levantado; conta: (4.233,42 − 756,53) / (1 − [(24.736,40 x 1,00 − 0,00) x (0,275/24.736,40) + 0]); exato: 4795.71034482758621; impresso: 4.795,71; delta: 0,00
- item: F base IR; conta: 4.795,71 x 1,000 − 0,00; exato: 4795.71; impresso: 4.795,71; delta: 0,00
- item: G IR; conta: 4.795,71 x 0,275 − 756,53; exato: 562.29025; impresso: 562,29; delta: 0,00
- item: Verificação; conta: 4.795,71 − 0,00 − 562,29; exato: 4233.42; impresso: 4.233,42; delta: 0,00
- item: consistência de faixa; conta: base 4.795,71 > 4.087,65 -> 27,5% / 756,53; resultado: coerente com a tabela impressa

**10.2.2.2**

- item: D vr. bruto levantado; conta: (4.233,42 − 306,80) / (1 − [(18.000,00 x 1,00 − 0,00) x (0,15/24.736,40) + 0]); exato: 4407.72734965783885; impresso: 4.407,73; delta: 0,00; observacao: o texto de anúncio na mesma página diz 4.795,71 — ver defeito D-03
- item: F vr. bruto sem juros; conta: 4.407,73 x 18.000,00 / 24.736,40; exato: 3207.38425963357643; impresso: 3.207,38; delta: 0,00
- item: F base IR; conta: 3.207,38 x 1,000 − 0,00; exato: 3207.38; impresso: 3.207,38; delta: 0,00
- item: G IR; conta: 3.207,38 x 0,15 − 306,80; exato: 174.307; impresso: 174,31; delta: 0,00
- item: Verificação; conta: 4.407,73 − 0,00 − 174,31; exato: 4233.42; impresso: 4.233,42; delta: 0,00
- item: consistência de faixa; conta: base 3.207,38 está em 2.453,51–3.271,38 -> 15% / 306,80; resultado: coerente com a tabela impressa

**bloqueios**

- **padrao delta 10 00 exatos:** NÃO reaparece. Maior delta do segmento = 0,66, com origem plenamente identificada.
- **padrao indice implicito sem origem:** NÃO reaparece. Todos os índices do segmento têm origem nos próprios dados: 1,0153923 e 0,15833330 são dados de entrada do exemplo; 0,8340 é derivado e conferido por duas vias; 1,3309 é derivado e conferido (com perda por arredondamento).
- **classificacao do unico desvio:** arredondamento de planilha (índice impresso a 4 casas usado como operando). Não é resíduo de versão anterior nem regra oculta.
- **nenhum bloqueio declarado:** True


### A.11 Notas e rótulos

- pagina_pdf: 226; tipo: rótulo contradizendo a operação; rotulo_impresso: Nº de meses referente ao RRA sobre o saldo remanescente; operacao_real: 62 = número de meses do rendimento TOTAL, dentro do quadro 'Apuração total líquido na data do levantamento', que por definição é calculado 'como se não houvesse liberação de crédito' — não existe saldo remanescente nesse ponto; assinatura: string literal idêntica nas pp.226, 230, 243, 250; correta apenas em 243/250 (item 10.3)
- pagina_pdf: 230; tipo: rótulo contradizendo a operação; rotulo_impresso: Nº de meses referente ao RRA sobre o saldo remanescente; operacao_real: idem p.226; assinatura: idem
- pagina_pdf: 225; tipo: nota conferida e CORRETA; texto: Obs.: O total das parcelas passíveis de IR pode ser apurado a partir da base informada no cálculo, somando ao valor da base de IR já informado o valor do INSS; conferencia: 300.589,14 + 1.843,00 = 302.432,14, exato
- pagina_pdf: 229; tipo: nota cuja aplicação literal ERRA; texto: Parcelas passíveis IR sem juros = (300.589,14 + 1.843,00) / 1,3309 = 227.238,16; conferencia: resultado literal = 227.238,82; o impresso exige divisor 1,3309038604396459
- pagina_pdf: 225; tipo: nota conferida e CORRETA; texto: Obs.: Para a apuração do número de meses, devem ser considerados apenas os meses com rendimento tributável constantes no cálculo de liquidação, não abrangendo o período trabalhado ou imprescrito; observacao: repetida na p.230 com erro de concordância: 'devem ser considerado apenas os meses'
- pagina_pdf: 228; tipo: nota conferida e CORRETA; texto: Obs.: Se o fato gerador contribuição previdenciária for a prestação de serviço, não será necessário fazer esta operação em relação à contribuição previdenciária cota reclamada, visto que o seu valor será atualizado a parte.; coerencia: coerente com o enunciado da p.224 e com a nota idêntica da p.232
- pagina_pdf: 234; tipo: referência cruzada ERRADA; texto: F – Apurar a base de cálculo do imposto de renda proporcional ao valor levantado, aplicando o índice das parcelas passíveis de IR sobre o valor bruto levantado e deduzindo do valor encontrado o INSS proporcional apurado no item “c”.; correto: o INSS proporcional é apurado no item E; o item C é o índice das parcelas passíveis de IR; repetido_em: 236
- pagina_pdf: 227; tipo: rótulo CORRETO; texto: cabeçalho 'Valor bruto levantado / Total bruto devido ao recte X Total contribuição social devida na data do levantamento = Total contribuição social proporcional ao valor levantado'; conferencia: 322.389,94/412.023,32 x 1.871,37 = 1.464,26 — a coluna faz exatamente a conta que o rótulo anuncia
- pagina_pdf: 235; tipo: notação inconsistente em rótulo de quadro; texto: BASE DE CÁLCULO IR COM BASE NO VALOR BRUTO PAGO AO MESMO (A. C - B); observacao: 'A. C' significa A x C (4.795,71 x 100%); a notação de multiplicação por ponto não é usada em nenhum outro quadro do segmento
- pagina_pdf: 237; tipo: rótulo CORRETO e autoexplicativo; texto: BASE DE CÁLCULO IR COM BASE NO VALOR BRUTO PAGO AO MESMO EXCLUINDO OS JUROS (4.407,73 X 18.000,00 / 24.736,40) X % PASSÍVEL IR - INSS; conferencia: 3.207,38, confere
- pagina_pdf: 227; tipo: nota metodológica declarando circularidade; texto: Poderão surgir dúvidas entre qual alíquota e qual parcela a serem aplicadas,   quando o total passível de IR em relação ao valor levantado se situar perto do limite máximo ou limite mínimo de uma faixa. Neste caso, será necessário aplicar a fórmula para as duas faixas e testar para qual delas a diferença entre o total bruto encontrado, o valor da contribuição social e o valor do IR resulta exatamente no valor líquido levantado pelo reclamant…

### A.12 Defeitos

15 catalogados. Nenhum corrigido.

| # | `pagina_pdf` | Defeito | Impresso | Correto |
|---|---|---|---|---|
| D-01 | 227 | erro do original; não corrigido na extração | VR. BRUTO LEVANTADO = [TL – (PD x NMP)] / { 1 – [(TB x IPIR – INSS)  x  ALIQ. / TB]  + (INSS / TB)} | VR. BRUTO LEVANTADO = [TL – (PD x NMP)] / { 1 – [(TB x IPIR – INSS) x ALIQ. / TB] – (INSS / TB)}, equivalentemente o colchete deve englobar também o termo INSS/TB, como faz a redação correta do item 10.2.2 |
| D-02 | 231 |  | VR. BRUTO LEVANTADO = [TL – (PD x NMP)] / { 1 – [(TBSJ x IPIR – INSS)  x  ALIQ. / TBCJ)]  + (INSS / TBCJ)} | ... / { 1 – [(TBSJ x IPIR – INSS) x ALIQ. / TBCJ] – (INSS / TBCJ)} |
| D-03 | 236 |  | Logo o total bruto levantado em 26/03/12, aplicando a fórmula acima, será de R$. 4.795,71, conforme demonstração abaixo: | 4.407,73 |
| D-04 | 234 |  | Até 1.637,11 / De 1..637,11 até 2.453,50 | De 1.637,12 até 2.453,50 |
| D-05 | 234 |  | 306,8 | 306,80 |
| D-06 | 231 |  | = (276.667,36 / 412.0323,32 x 282.500,00 x 0,8340) / 44,7 = 3.539,27 | 412.023,32 |
| D-07 | 226 |  | (412.023,32  x 0,8340 -1,871,37) | 1.871,37 |
| D-08 | 225 |  | 302.432,14 ( 300,589,14 + 1.843,00) | 300.589,14 |
| D-09 | 227 |  | (1.871,37/ 412023,32) | 412.023,32 |
| D-10 | 226 |  | Nº de meses referente ao RRA sobre o saldo remanescente | Nº de meses referente ao RRA — total do rendimento tributável (não há saldo remanescente neste quadro: o próprio texto manda apurar 'como se não houvesse liberação de crédito') |
| D-11 | 234 |  | o INSS proporcional apurado no item “c” | item “E” |
| D-12 | 233 |  | 10.2.2 Critérios - Art. 12-B da Lei 7713/88 e arts. 26, 44 e 45 da IN/RFB 1500/14 | arts. 26, 43 e 44 (grafia usada pelo próprio manual no item 9.3.8, p.190). O art.45 rege o arredondamento do nº de meses do RRA, inaplicável ao 12-B, que é 'sem qualquer multiplicação pelos números de meses' (p.190). |
| D-13 | 229 |  | Parcelas passíveis IR sem juros = (300.589,14 + 1.843,00) / 1,3309 = 227.238,16 |  |
| D-14 | 230 |  | devem ser considerado apenas os meses | devem ser considerados apenas os meses |
| D-15 | 226 |  | a regra de arredondamento prevista no parágrafo único do 45 da Instrução Normativa 1500/14 | do art. 45 |

### A.13 Pendências

- id: P10.2-01; descricao: Migração de regime tributário dentro do mesmo cálculo (levantamento sob 12-B, saldo sob 12-A) NÃO é disciplinada em 10.2 nem em nenhum outro ponto do manual.; status: ABERTA; evidencia: 'migra*'=0, 'transição'=0, 'transicao'=0, 'dois regimes'=0 nas 471 páginas; 'duas apuraç*' só na p.190 e trata de cisão por ano-calendário, não de transição de regime
- id: P10.2-02; descricao: Fundamento normativo do RATEIO PROPORCIONAL do INSS (VB/TB x INSS) não é citado em lugar nenhum. O manual fundamenta a proporcionalidade do IR (p.186: art.12-A §1º, art.12-B, art.56 do Dec.3000/99) mas nada diz sobre a do INSS.; status: ABERTA; evidencia: no segmento 223-237: 'art. 56'=0, '§ 1'=0, '3000/99'=0, 'Decreto nº 3000'=0, 'art. 354'=0 (0 no documento inteiro)
- id: P10.2-03; descricao: O segmento não estabelece QUANDO usar o ramo 'com juros' (10.2.1.1/10.2.2.1) e quando usar o ramo 'sem juros' (10.2.1.2/10.2.2.2). A OJ 400, que no cap.9 rege essa escolha, não é citada uma única vez.; status: ABERTA; evidencia: 'OJ'=0 ocorrências em 223-237; OJ 400 aparece em 21 páginas do documento, nenhuma delas entre 223 e 237
- id: P10.2-04; descricao: Código de recolhimento do IR não é informado em 10.2 para nenhum dos dois regimes.; status: ABERTA; evidencia: 'código'=0 e '5936'=0 em 223-237; o código 5936 (12-B) aparece apenas no cap.9, p.207
- id: P10.2-05; descricao: A fórmula de VR. BRUTO LEVANTADO exige alíquota e parcela a deduzir conhecidas, mas a faixa depende do bruto ainda desconhecido. O manual reconhece a circularidade e prescreve tentativa e erro, sem critério de convergência nem limite de iterações.; status: ABERTA — comportamento declarado, não defeito; citacao: será necessário aplicar a fórmula para as duas faixas e testar para qual delas a…
- id: P10.2-06; descricao: Os itens 10.2.2.1 e 10.2.2.2 enunciam as letras A, B e C sem qualquer demonstração numérica; o exemplo só começa na letra D. As três primeiras etapas ficam sem exemplo, ao contrário de 10.2.1.x.; status: ABERTA — lacuna de demonstração
- id: P10.2-07; descricao: Os exemplos do 12-B usam INSS = 0,00 e IPIR = 100%, de modo que os termos de INSS das fórmulas D e E de 10.2.2 nunca são exercitados numericamente. A correção do posicionamento dos colchetes na redação de 10.2.2 é inferida por comparação com 10.2.1, não verificada por número.; status: ABERTA — limite de verificabilidade

### A.14 Buscas que sustentam as negativas

| Termo | Escopo | Ocorrências | Conclusão |
|---|---|---|---|
| `art. 354` | 471 páginas | 0 |  |
| `354 (qualquer contexto)` | 471 páginas | 23 páginas, todas como número de página ou valor monetário; 0 no segmento 223-237 |  |
| `migra*` | 471 páginas | 0 |  |
| `transição / transicao` | 471 páginas | 0 |  |
| `dois regimes` | 471 páginas | 0 |  |
| `duas apuraç*` | segmento 223-237 | 0 |  |
| `OJ 400` | segmento 223-237 | 0 |  |
| `0,9091 / 9091` | segmento 223-237 | 0 |  |
| `arredond*` | segmento 223-237 | 2 páginas (226, 230) |  |
| `12-B` | segmento 223-237 | 2 (pp. 224 e 233) |  |
| `12-A` | segmento 223-237 | 12, em 8 páginas (223, 224, 226, 228, 230, 232, 233, 235) |  |
| `código / codigo / 5936` | segmento 223-237 | 0 |  |
| `art. 56 / Decreto nº 3000 / 3000/99 / § 1` | segmento 223-237 | 0 |  |
| `11/03/15` | segmento 223-237 | 0 |  |
| `10/03/15` | segmento 223-237 | 2 (pp. 233 e 235), somente no enunciado da hipótese do 12-B |  |
| `IN RFB 1558/15 ('1558')` | segmento 223-237 | 0 |  |
| `arts. 26, 43` | 471 páginas | 0 com essa grafia exata (o cap.9 grafa 'arts. 26 , 43 e 44') |  |

---

## B. Capítulos 8, 12 e 14

### B.1 Fronteiras

- **metodo:** PyMuPDF doc[pagina-1].get_text(), encoding utf-8, offset 0. Varredura regex das aberturas de capitulo em todas as 471 paginas.
- **total paginas pdf:** 471
**confirmadas**

- capitulo: 8; titulo_impresso: 8 - ENCARGOS E DESPESAS PROCESSUAIS; pp: 100-106; prox_capitulo_abre: 107; status: CONFERE
- capitulo: 12; titulo_impresso: 12 - CONTRIBUICAO SINDICAL; pp: 299-302; prox_capitulo_abre: 303; status: CONFERE
- capitulo: 14; titulo_impresso: 14 - PRECATORIOS; pp: 304-306; prox_capitulo_abre: 307; status: CONFERE

- **mapa completo aberturas:** 1: 9; 2: 10; 3: 11; 4: 13; 5: 14; 6: 18; 7: 83; 8: 100; 9: 107; 10: 209; 11: 278; 12: 299; 13: 303; 14: 304; 15: 307; 16: 310; 17: 337; 18: 373
- **observacao:** Cap. 13 ocupa uma unica pagina (303). Cap. 16 chama-se PROMOCOES (p. 310), nao 'minuta'.

### B.2 Premissas do enunciado, conferidas

- premissa: O sumario lista 8.2.1 'Apuracao do valor das custas de execucao'; veredito: NAO CONFIRMA; evidencia: Sumario (pagina_pdf 6) lista apenas 8.1, 8.2, 8.3, 8.4. Nao ha linha 8.2.1. O corpo TEM 8.2.1, na pagina_pdf 101, com titulo mais longo: 'Apuracao do valor das custas de execucao sobre o calculo de liquidacao'. A forma curta citada no enunciado vem de docs/calculo/extracao/mapa-de-cobertura.md secao 2.2, nao do manual.
- premissa: O capitulo 1 do manual do CJF (custas) esta em extracao/justica-federal/bloco-08-jf.md; veredito: PARCIAL; evidencia: bloco-08-jf.md tem 1 ocorrencia de 'custas' e 0 de 'capitulo 1'. O capitulo 1 do CJF esta em bloco-08-jf-detalhe.md, secao 1 ('Capitulo 1 - custas processuais', pagina_pdf CJF 14-21). O capitulo 5 do CJF (requisicoes) esta sim em bloco-08-jf.md, secao 7. Cruzamento feito contra os dois arquivos.
- premissa: As faixas do art. 85, par. 3o, do CPC estao em docs/calculo/02-base-normativa-verbas.md secao 10; veredito: NAO CONFIRMA; evidencia: A secao 10 daquele arquivo e 'Inventario inicial de parametros negociaveis' (adicional de HE, jornada, divisor, etc.). Varredura por 'art. 85', '791-A', '200 salarios', '1.000 salarios', '2.000 salarios', '20.000 salarios', '100.000 salarios' em toda a arvore docs/: os VALORES das faixas do art. 85, par. 3o, NAO existem no corpus. Ha apenas mencoes de escopo em 01-plano-extracao.md e pendencias.md secao 16 ('as faixas de honorarios sao do CPC art. 85, par. 3o, nao da CLT'…
- premissa: cap. 11, Exemplo 1: base = liquido do reclamante + INSS do reclamante + INSS da reclamada, dando 151,56 contra 151,39; veredito: CONFIRMA A ARITMETICA, CORRIGE A CAUSA; evidencia: Ver bloco p10_18_custas_execucao. A string '151,39' nao ocorre em nenhuma das 471 paginas (0 ocorrencias) - e valor calculado pelo bloco 10, nao impresso. E a diferenca NAO e bruto-x-liquido: e o juro Selic sobre o INSS cota-reclamante.

### B.3 Capítulo 8 — encargos

- **paginas:** 100-106
**subitens no corpo**

- num: 8.1; titulo: Custas processuais; pagina_pdf: 100
- num: 8.2; titulo: Custas de execucao; pagina_pdf: 100
- num: 8.2.1; titulo: Apuracao do valor das custas de execucao sobre o calculo de liquidacao; pagina_pdf: 101; nota: AUSENTE do sumario
- num: 8.3; titulo: Honorarios periciais; pagina_pdf: 102
- num: 8.4; titulo: Honorarios advocaticios assistenciais e sucumbenciais; pagina_pdf: 105

**encargos**

- id: 8.1-custas-processuais; base_calculo: valor do acordo, da condenacao, da causa ou, se indeterminado, o que o juiz fixar; citacao_base: Os incisos I, II, III e IV do art. 789/CLT estabelecem a base de incidencia das custas como sendo o valor do acordo, da condenacao, da causa ou se tratando de valor indeterminado, sobre o que o juiz fixar.; aliquota_ou_valor: 2%, minimo de R$ 10,64; citacao_aliquota: Incidirao sempre a razao de 2%, observado o minimo de R$ 10,64.; teto: NAO DECLARADO no capitulo; responsabilidade: NAO DECLARADA no item 8.1 - o manual nao diz quem paga as custas da fase de conhecimento; moment…
- id: 8.2-custas-de-execucao; base_calculo: por natureza do ato, conforme tabela do Anexo II da IN GP/CR/VCR 001/2002/TRT-3 (14 rubricas C-1 a C-14); e, para a rubrica C-6, sobre o valor liquidado; aliquota_ou_valor: ver tabela_custas e tabela_emolumentos; responsabilidade: SEMPRE do executado; citacao_responsabilidade: Sao sempre de responsabilidade do executado e pagas ao final, conforme caput do art. 789-A, CLT.; momento: ao final; o calculo das CE se da apos a quitacao do total do debito exequendo (art. 2o da IN GP/CR/VCR 001/02). Se o despacho for omisso, o calculista deve perguntar ao Juiz ou Diretor de secr…
- id: 8.2.1-ce-sobre-calculo-de-liquidacao; base_calculo: o calculo de liquidacao, do qual se exclui APENAS a parcela de custas processuais da fase de conhecimento; citacao_base: Da base de calculo das CE sera excluida apenas a parcela de custas processuais (custas da fase de conhecimento), na forma do art. 6o da IN GP/CR/VCR n.; citacao_base_2: Nenhuma outra verba devera ser excluida da base, nem mesmo imprensa oficial e honorarios, salvo determinacao judicial contraria;; aliquota_ou_valor: 0,5%, ate o limite de R$ 638,46; citacao_aliquota: as custas de execucao geradas pelo calculo de liquidacao deverao ser apur…
- id: 8.3-honorarios-periciais; base_calculo: valor arbitrado pelo juizo; aliquota_ou_valor: arbitrado - o manual nao fixa percentual nem tabela; responsabilidade: NAO DECLARADA no item 8.3 (o manual nao enuncia a regra de sucumbencia na pericia). No exemplo da pagina_pdf 280 (cap. 11) a sentenca poe por conta da re; momento: correcao desde a data do arbitramento ou outra data fixada pelo juizo, ate o efetivo pagamento; indice: IPCA-E - pratica atual da Secretaria de Calculos de Belo Horizonte; citacao_indice: a Secretaria de Calculos em Belo Horizonte utiliza o IPCA-E como indice de atualizacao dos honorarios per…
- id: 8.4-honorarios-advocaticios; base_calculo_enunciada: valor liquido da condenacao apurado na liquidacao, SEM deducao dos descontos fiscais e previdenciarios - isto e, o valor BRUTO liquidado em relacao ao credito do reclamante; citacao_base: os honorarios advocaticios incidem sobre o valor liquido da condenacao, apurado na fase de liquidacao, sem a deducao dos descontos fiscais e previdenciarios; exclusao: NAO incide sobre a contribuicao previdenciaria cota reclamada; citacao_exclusao: A cota-parte de contribuicao previdenciaria do empregador nao integra a base de calculo dos honorarios advocaticios; base_cal…

**tabela custas anexo II IN 001 2002 TRT3**

- **pagina pdf:** 100-101
- **linhas:** {'ref': 'C-1', 'natureza': 'Agravo de Instrumento', 'valor': '44,26', 'base': 'para cada recurso', 'defeito_impressao': "impresso '44, 26' com espaco apos a virgula na p.100"}; {'ref': 'C-2', 'natureza': 'Agravo de Peticao', 'valor': '44,26', 'base': 'para cada recurso'}; {'ref': 'C-3', 'natureza': 'Auto de Adjudicacao', 'valor': '5% ate 1.915,38', 'base': 'sobre o valor ofertado'}; {'ref': 'C-4', 'natureza': 'Auto de Arrematacao', 'valor': '5% ate 1.915,38', 'base': 'sobre o valor ofertado'}; {'ref': 'C-5', 'natureza': 'Auto de Remicao', 'valor': '5% ate 1.915,38', 'base': 'sobre o valor ofertado'}; {'ref': 'C-…
- **observacao:** A tabela nao tem data-base nem regra de atualizacao. O item 8.2 diz expressamente que estes valores nao sofrem atualizacao monetaria. Sao valores nominais de 2002 reproduzidos em 2016.

**tabela emolumentos**

- **pagina pdf:** 101
- **linhas:** {'ref': 'E-1', 'natureza': 'Autenticacao de traslado', 'valor': '0,55', 'base': 'por folha/da parte'}; {'ref': 'E-2', 'natureza': 'Autenticacao de pecas', 'valor': '0,55', 'base': 'por folha'}; {'ref': 'E-3', 'natureza': 'Carta de adjudicacao', 'valor': '0,55', 'base': 'por folha'}; {'ref': 'E-4', 'natureza': 'Carta de arrematacao', 'valor': '0,55', 'base': 'por folha'}; {'ref': 'E-5', 'natureza': 'Carta de remicao', 'valor': '0,55', 'base': 'por folha'}; {'ref': 'E-6', 'natureza': 'Carta de sentenca', 'valor': '0,55', 'base': 'por folha'}; {'ref': 'E-7', 'natureza': 'Certidoes', 'valor': '5,53', 'base': 'por fo…
- **responsabilidade:** do requerente, a qualquer momento, independentemente de processo
- **citacao:** Os emolumentos sao devidos pelo requerente a qualquer momento, independentemente de processo

**conferencia decimal exemplo 8.4**

- **pagina pdf:** 106
- **todas as contas em decimal Decimal:** True
- **linhas:** {'rubrica': 'Total bruto devido ao reclamante', 'impresso': '264.131,80'}; {'rubrica': 'Deducao contribuicao previdenciaria cota autor', 'impresso': '1.508,96'}; {'rubrica': 'Imposto de renda devido', 'impresso': '13.484,57'}; {'rubrica': 'Total liquido do recte', 'impresso': '249.138,27', 'recalculado': '249138.27', 'confere': True}; {'rubrica': 'Total FGTS a depositar', 'impresso': '13.206,59'}; {'rubrica': 'Contribuicao previdenciaria cota reclamada', 'impresso': '18.574,26', 'nota': 'NAO entra na base dos honorarios - TJP 4'}; {'rubrica': 'Base dos honorarios', 'impresso': '277.338,39', 'recalculado': '26413…

**conferencia decimal exemplo 8.3**

- **pagina pdf:** 104
- **linhas:** {'perito': 'Dr. Joe Henrique - insalubridade fl. 454', 'periodo': '10/12/14 a 31/05/16', 'devido': '2.500,00', 'indice_IPCA_E': '1,15282710', 'corrigido_impresso': '2.882,07', 'recalculado': "Decimal('2500.00')*Decimal('1.15282710') = 2882.067750 -> 2882.07", 'confere': True, 'ir': '77,51', 'liquido': '2.804,56', 'confere_liquido': True}; {'perito': 'Dr. Augusto Cesar - contabil fase execucao fl. 725', 'periodo': '25/08/15 a 31/05/16', 'devido': '2.000,00', 'indice_IPCA_E': '1,06992911', 'corrigido_impresso': '2.139,86', 'recalculado': "Decimal('2000.00')*Decimal('1.06992911') = 2139.85822 -> 2139.86", 'confere'…
- **observacao:** O total do calculo soma honorarios liquidos MAIS o IR lancado separadamente - coerente com a regra do art. 106, par. 2o, h, enunciada na p.104. Nome impresso 'Joe Henrique' (provavel 'Jose'); nao corrigido.


### B.4 Cruzamento com o cap. 1 do CJF

- **fonte trt3:** manual-de-calculo-trabalhista_2016-1.pdf, cap. 8, pp. 100-106 (offset 0)
- **fonte cjf:** docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md secao 1 - Capitulo 1 do Manual CJF Res. 990/2026, pagina_pdf CJF 14-21 (offset +1)
- **ressalva de localizacao:** O enunciado apontou bloco-08-jf.md; o cap. 1 do CJF esta em bloco-08-jf-DETALHE.md. bloco-08-jf.md tem 1 ocorrencia de 'custas' (na tabela de series OUT_OF_SCOPE).
- **nao harmonizado:** True
**diferencas**

- eixo: normatizacao; trt3: arts. 789/790/790-A da CLT + Lei 10.537/02 + IN 20/2002 TST + IN GP/CR/VCR 001/02 do TRT-3 (norma REGIONAL); cjf: Lei n. 9.289, de 04/07/1996 (norma unica federal); achado: a Justica do Trabalho tem uma camada regional de regulamento que a Justica Federal nao tem. Custas de execucao no TRT-3 sao materia de Instrucao Normativa de Regional.
- eixo: base; trt3: valor do acordo, da condenacao, da causa, ou o que o juiz fixar (art. 789 CLT, incisos I a IV); cjf: valor da causa, corrigido monetariamente desde o ajuizamento pelo encadeamento das acoes condenatorias em geral (item 4.2.1); achado: BASE DIFERENTE. O TRT-3 admite o valor do ACORDO e o valor da CONDENACAO como base; o CJF trabalha so com o valor da causa. E o CJF manda CORRIGIR a base; o TRT-3 so corrige as custas JA ARBITRADAS, nao a base.
- eixo: aliquota; trt3: 2% fixo; cjf: tabela I da Lei 9.289/1996 - NAO reproduzida no manual, remissao externa (classificada (B) serie OUT_OF_SCOPE); achado: o TRT-3 imprime a aliquota; o CJF remete. Comparacao direta de valor e IMPOSSIVEL com o corpus atual.
- eixo: piso; trt3: R$ 10,64; cjf: NAO DECLARADO no corpus (esta na tabela I, nao extraida); achado: pendencia de dado
- eixo: teto; trt3: NAO declarado para as custas do art. 789 (fase de conhecimento). Ha teto apenas nas custas de EXECUCAO: R$ 638,46 para a rubrica C-6 e R$ 1.915,38 para adjudicacao/arrematacao/remicao; cjf: NAO declarado no corpus; achado: o TRT-3 tem teto por rubrica de execucao; nada equivalente registrado no CJF.
- eixo: momento do pagamento; trt3: custas do conhecimento: momento NAO enunciado no cap. 8. Custas de EXECUCAO: 'ao final', apos a quitacao do total do debito exequendo; cjf: metade na distribuicao, metade exigivel de quem recorrer ou do vencido (art. 14, I a IV, Lei 9.289/1996); na apelacao, tabela vigente na data de interposicao; achado: DIVERGENCIA FORTE. O CJF fraciona o recolhimento no tempo (50/50) e ancora a tabela na data do recurso; o TRT-3 concentra tudo no final da execucao e congela os valores de 2002.
- eixo: atualizacao; trt3: custas arbitradas: Leis 6.899/81 e 8.177/91, marco = data do arbitramento. Custas de EXECUCAO: NAO se atualizam (exceto a apurada sobre o calculo de liquidacao); cjf: valor da CAUSA corrigido pelo encadeamento do cap. 4 item 4.2.1 quando o pagamento ocorre em mes diverso do ajuizamento; achado: eixos opostos: o CJF corrige a BASE; o TRT-3 corrige o RESULTADO, e so em parte.
- eixo: responsabilidade; trt3: custas de execucao: SEMPRE do executado (art. 789-A caput). Conhecimento: nao enunciado; cjf: vencido / recorrente (art. 14); em execucao fiscal, 'o executado devera pagar a totalidade das custas' quando ha pagamento do debito (item 1.4.4); achado: CONVERGEM na execucao fiscal/trabalhista - executado paga o total. Divergem no conhecimento, onde o TRT-3 e silente.
- eixo: isencoes; trt3: entes publicos das 3 esferas (inclusive autarquias e fundacoes) que nao explorem atividade economica; beneficiarios da justica gratuita; MPT (art. 790-A, CLT); cjf: rol do art. 4o da Lei 9.289/1996; habeas corpus e habeas data (art. 5o); reconvencao (art. 7o); JEFs - sem custas no ajuizamento, mas com preparo no recurso (arts. 42 par.1o e 54 da Lei 9.099/1995); achado: CRITERIOS INCOMPARAVEIS. O TRT-3 isenta por QUALIDADE DO SUJEITO (ente publico, pobre, MPT). O CJF isenta tambem por TIPO DE ACAO (HC, HD, reconvencao) e por RITO (JEF). A clausula trabalhista 'que nao explorem atividade econ…
- eixo: emolumentos / porte; trt3: tabela propria E-1 a E-8, valores por folha (0,28 a 5,53); devidos pelo REQUERENTE a qualquer momento, independentemente de processo; cjf: porte de remessa e retorno DISPENSADO em autos eletronicos (art. 1.007, par. 3o, CPC) - item 1.3.3; achado: o TRT-3 nao registra dispensa por processo eletronico. O manual e de 2016 e o TRT-3 ja era PJe. Nenhuma ocorrencia de 'eletronico' ligada a emolumentos nas pp. 100-106.
- eixo: custas sobre o calculo de liquidacao; trt3: EXISTE - 0,5% ate R$ 638,46 (art. 789-B, IX, CLT); cjf: NAO EXISTE figura equivalente no corpus; achado: instituto exclusivo da Justica do Trabalho. E ele que gera a pendencia P10-18.


### B.5 P10-18 — custas de execução

- **pergunta:** O capitulo 8 enuncia a regra da base das custas de execucao? Se sim, qual das versoes sustenta?
- **resposta curta:** ENUNCIA, mas por EXCLUSAO, nao por composicao. E por isso NAO decide entre as duas versoes medidas pelo bloco 10.
**o que o cap 8 enuncia**

- **pagina pdf:** 101-102
- **citacao 1:** Da base de calculo das CE sera excluida apenas a parcela de custas processuais (custas da fase de conhecimento), na forma do art. 6o da IN GP/CR/VCR n.
- **citacao 2:** Nenhuma outra verba devera ser excluida da base, nem mesmo imprensa oficial e honorarios, salvo determinacao judicial contraria;
- **leitura:** A regra e negativa: define o que SAI da base (so as custas do conhecimento) e proibe qualquer outra exclusao. Nao diz o que ENTRA, nem em que estado (bruto ou liquido) o credito do reclamante entra. O eixo bruto-x-liquido simplesmente nao e enderecado. Busca dirigida nas pp. 100-106: 'bruto' ocorre 2x na p.105 e 2x na p.106 (ambas sobre honorarios advocaticios, nao sobre CE); 'liquido' ocorre 1x na p.104, 2x na p.105 e 2x na p.106 (IR de peritos e honorarios). ZERO ocorrencias de 'bruto' ou 'liquido' nos itens 8.2 e 8.2.1.

**o que o cap 8 decide**

- Honorarios ENTRAM na base ('nem mesmo ... honorarios'). Isso sustenta o achado do bloco 10 de que os honorarios entram brutos: o cap. 8 os poe na base sem qualificar estado, e nao manda deduzir o IR antes.
- Imprensa oficial ENTRA na base.
- Custas processuais da fase de conhecimento SAEM - unica exclusao autorizada.
- Atualizacao e retificacao de calculo NAO geram CE; parcela complementar gera.

**o que o cap 8 NAO decide**

- Se o credito do reclamante entra bruto ou liquido de INSS e IR.
- Se a contribuicao previdenciaria cota-reclamada entra na base (os exemplos dizem que sim; o enunciado e silente).
- Se os juros/Selic acrescidos a contribuicao previdenciaria entram na base - que e a causa real da divergencia.
- Os incisos III a V do art. 7o da IN 001/02, que listam mais hipoteses de nao incidencia, nao sao reproduzidos.

**diagnostico da divergencia medida**

- **correcao ao enunciado:** A divergencia 151,56 x 151,39 NAO e bruto-x-liquido. E o JURO SELIC SOBRE O INSS COTA-RECLAMANTE.
- **prova em Decimal:** exemplo: cap. 11, Exemplo 1, pagina_pdf 280; total_bruto: 28.987,08; deducao_previdenciaria_no_corpo_do_calculo: 570,83; total_liquido_do_recte: 28.416,25; INSS_recte_a_recolher_pela_recda_COM_juros_Selic: 606,12; INSS_recda_com_Selic: 1.290,44; via_liquida: Decimal('28416.25') + Decimal('606.12') + Decimal('1290.44') = Decimal('30312.81'); via_bruta_do_rotulo_do_cap_9: Decimal('28987.08') + Decimal('1290.44') = Decimal('30277.52'); delta: Decimal('30312.81') - Decimal('30277.52') = Decimal('35.29'); identidade_do_delta: Decimal('606.12') - Decimal('570.83') = Decimal('35.29') = juros Selic sobre a cota-reclamante; conclusao: bruto = liquido + INSS recte SEM Selic. Quando o INSS e atualizad…
- **por que o rotulo do cap 9 parecia certo:** Nas tres ocorrencias do cap. 9 as duas vias coincidem porque o IR e zero E o INSS nao carrega Selic. Verificado em Decimal: pagina_pdf 132 -> bruto+INSSrecda = 5.207,54 e liq+INSSrecte+INSSrecda = 5.207,53; ambas dao CE 26,04. pagina_pdf 137 -> 4.795,62 + 479,22 = 5.274,84 (impresso) -> 26,37, identico pelas duas vias. pagina_pdf 163 -> 3.892,89 + 294,37 + 314,82 = 4.502,08 -> 22,51 (impresso), e aqui nao ha deducao de INSS do credito, de modo que 'liquido' e 'bruto' coincidem por construcao.

**invariante que os quatro exemplos sustentam**

- **id:** R8-CE-01
- **enunciado:** A base das CE sobre o calculo de liquidacao e o TOTAL DO CALCULO, isto e, a soma de todas as linhas do resumo geral antes da propria linha de custas de execucao - menos as custas processuais do conhecimento.
- **origem:** PROMOVIDA DO EXEMPLO. O enunciado do item 8.2.1 so diz o que sai da base. A composicao positiva so existe nas planilhas das paginas_pdf 132, 137, 163 e 280.
- **verificacao Decimal:** p.163: 4.502,08 * 0,5% = 22,5104 -> 22,51 e TOTAL DO CALCULO 4.524,59 = 4.502,08 + 22,51. Fecha exatamente. p.280: 30.312,80 + 151,56 = 30.464,36 contra 30.464,37 impresso (defeito de 1 centavo, ver defeitos).
- **consequencia:** Sob R8-CE-01 a versao do cap. 11 e a correta e o rotulo do cap. 9 e uma FORMULA-ROTULO incompleta, valida apenas no subcaso sem Selic sobre o INSS. O cap. 8 nao contradiz R8-CE-01, mas tampouco a enuncia.

- **veredito P10 18:** PARCIALMENTE RESOLVIDA. O cap. 8 fixa o perimetro por exclusao e confirma que honorarios entram na base. Nao enuncia a composicao positiva nem o estado (bruto/liquido) do credito. A pendencia deixa de ser 'cap. 9 x cap. 11' e passa a ser 'o rotulo do cap. 9 na pagina_pdf 132 esta incompleto' - reclassificada como defeito do original (D8-06), nao como divergencia normativa. Resta aberto: se a linha 'imprensa oficial' e as custas do CONHECIMENTO aparecem no resumo, o calculista tem de subtrai-las manualmente, e nenhum exemplo do manual mostra essa subtracao.
- **pendencia residual:** P10-18b - nenhum dos quatro exemplos de CE do manual contem custas processuais da fase de conhecimento no resumo, de modo que a unica exclusao autorizada pelo item 8.2.1 nunca e praticada. Busca: 'custas processuais' nas pp. 100-106 -> ocorre no titulo 8.1 e no item 2 do 8.2.1; nas paginas de exemplo 132, 137, 163, 280 -> 0 ocorrencias.

### B.6 Fase 4 — honorários

- **marcacao:** CONFLITO NORMATIVO - NAO HARMONIZADO
- **fato 1:** O manual e de julho/2016. Varredura nas 471 paginas: '791-A' = 0 ocorrencias; '13.467' = 0; '13467' = 0. O manual NAO PODE conhecer o art. 791-A da CLT, criado pela Lei 13.467/2017.
- **fato 2:** Varredura nas 471 paginas: 'art. 85' = 0 ocorrencias; '85, par. 3o' = 0. O manual nunca cita o CPC art. 85. 'CPC' ocorre em 7 paginas (9, 13, 38, 39, 77, 302, 362), nenhuma delas no cap. 8.
- **fato 3:** O regime que o cap. 8 pratica e o da ASSISTENCIA JUDICIARIA sindical: Lei 1060/50 art. 11 par. 1o, Lei 5.584/70 art. 16, OJ 348 SDI-I/TST, Sumula 219/TST implicita. O exemplo da pagina_pdf 106 e de honorarios ao SINDICATO AUTOR, a 15%.
- **fato 4:** O cap. 8 menciona 'sucumbenciais' apenas no titulo do item 8.4 e em duas passagens sobre tributacao (IR incide; previdenciario nao). NAO fixa criterio de arbitramento, nem faixa, nem piso, nem teto, nem base.
**conflito a registrar**

- eixo: cabimento; manual_2016: honorarios so na assistencia sindical (Lei 5.584/70) ou por sucumbencia excepcional; nao ha sucumbencia geral na JT; norma_posterior: art. 791-A da CLT (Lei 13.467/2017) instituiu sucumbencia geral na Justica do Trabalho; status: NAO HARMONIZADO - o manual nao pode conhecer
- eixo: percentual; manual_2016: o que a decisao arbitrar (exemplo usa 15%); norma_posterior: art. 791-A caput: 5% a 15% sobre o valor que resultar da liquidacao da sentenca, do proveito economico obtido ou, nao sendo possivel mensura-lo, sobre o valor atualizado da causa; status: PENDENCIA DE FONTE - o texto do art. 791-A NAO esta no corpus; a faixa 5-15% aqui citada NAO foi conferida contra fonte do corpus e NAO deve ser usada sem confirmacao. Registrada como pendencia P8-F4-01, nao como dado.
- eixo: base de calculo; manual_2016: valor bruto liquidado em favor do reclamante + FGTS a depositar, EXCLUIDA a cota patronal de INSS (OJ 348 + TJP 4 do TRT-3); norma_posterior: art. 791-A: 'valor que resultar da liquidacao da sentenca'; art. 85 par. 3o do CPC para a Fazenda Publica, com faixas progressivas (art. 85 par. 5o); status: DIVERGENCIA DE BASE A RESOLVER NA FASE 4. O FGTS a depositar na base e regra do TRT-3 de 2016; nada no corpus confirma que sobreviva ao art. 791-A.
- eixo: faixas progressivas; manual_2016: inexistentes; norma_posterior: art. 85 par. 3o e par. 5o do CPC - progressividade por faixa; status: PENDENCIA DE DADO - os VALORES das faixas nao existem em lugar nenhum de docs/. So a regra de progressividade, em bloco-08-jf.md R-08-21: 'o calculo de honorarios deve observar o percentual da faixa inicial e, naquilo que a exceder, o percentual da faixa subsequente, e assim sucessivamente (art. 85, par. 5o, CPC)' (pagina_pdf CJF 44).
- eixo: termo inicial dos juros; manual_2016: incidencia INDIRETA dos juros do credito quando o percentual e sobre o valor final da liquidacao; ou art. 1o da Lei 6899/81 quando fixo; ou art. 1o-F da Lei 9494/97 se ente publico; norma_posterior_no_corpus: CJF item 4.1.4 (bloco-08-jf.md secao 9): tres termos iniciais conforme a forma de fixacao - valor da causa -> transito em julgado; valor certo -> transito em julgado (art. 85 par. 16 CPC); multiplos do salario minimo -> citacao na execucao ou fim do prazo do art. 523; status: DIVERGENCIA ENTRE JURISDICOES, REGISTRADA, NAO HARMONIZADA. O TRT-3 nao usa transito em j…
- eixo: multa do art. 523 par. 1o na base; manual_2016: NAO enderecado (0 ocorrencias de '523' no cap. 8); norma_posterior_no_corpus: CJF R-08-22: a multa de 10% do art. 523 par. 1o NAO entra na base dos honorarios (REsp 1.757.033), item 4.1.4.6, pagina_pdf CJF 45; status: LACUNA do lado trabalhista
- eixo: imposto de renda; manual_2016: assistenciais: NAO incide (OS 01/11 VPADM art. 21 III; Provimento Geral Consolidado art. 206 pars. 1o e 3o). Sucumbenciais: INCIDE; norma_posterior: nao ha alteracao registrada no corpus; status: PROVAVELMENTE VIGENTE - mas a expansao da sucumbencia pelo art. 791-A amplia muito o universo em que o IR incide. Efeito pratico a medir na Fase 4.
- eixo: previdenciario; manual_2016: nao integra a base da contribuicao da empresa; recolhimento direto pelo advogado contribuinte individual (art. 57 par. 15 IN RFB 971/09); norma_posterior: nao ha alteracao registrada no corpus; status: PROVAVELMENTE VIGENTE

- **nota de metodo:** Nao pesquisei norma na web. Tudo que nao esta no PDF do TRT-3 nem em docs/calculo/ virou pendencia explicita acima.

### B.7 Capítulo 12 — contribuição sindical

- **paginas:** 299-302
- **status:** SUPERADO - ESTRUTURA PRESERVADA
- **razao da superacao:** A Lei 13.467/2017 tornou a contribuicao sindical facultativa, condicionada a autorizacao previa e expressa. Varredura nas 471 paginas: '13.467' = 0, '13467' = 0, 'facultativ' = 0, 'autorizacao previa' = 0. O manual e de julho/2016 e NAO PODE conhecer a alteracao. A norma superveniente NAO esta no corpus - registrada como pendencia, nao como dado.
- **interesse residual:** A estrutura de apuracao permanece util para competencias ANTERIORES a 11/11/2017. Como a contribuicao do empregado e descontada na folha de MARCO de cada ano, as competencias potencialmente vivas sao marco/2017 e anteriores.
**subitens no corpo**

- num: 12.1; titulo: Esclarecimentos Gerais; pagina_pdf: 299; nota: corpo escreve 'Gerais' com G maiusculo; sumario em caixa alta
- num: 12.2; titulo: Forma de calculo; pagina_pdf: 299
- num: 12.3; titulo: Contribuicao Sindical Rural; pagina_pdf: 299
- num: 12.4; titulo: Forma de atualizacao; pagina_pdf: 301

- **confirmacao do sumario:** CONFERE - os quatro subitens do sumario (pagina_pdf 6) existem no corpo, com as mesmas paginas: 299, 299, 299, 301.
**quatro institutos distintos**

- **pagina pdf:** 299
- **citacao:** mensalidade associado (CLT, art. 548, b), contribuicao confederativa (CF/88, art. 8o, inciso IV), desconto ou contribuicao assistencial (CLT, art. 513, c)
- **quadro:** {'instituto': 'Contribuicao sindical', 'fundamento': 'CLT arts. 548, a, e 578 a 610', 'tratado_pelo_cap_12': True, 'base': '1 dia de trabalho (empregado) ou capital social (empregador)'}; {'instituto': 'Mensalidade de associado', 'fundamento': 'CLT art. 548, b', 'tratado_pelo_cap_12': False, 'nota': 'citado apenas na enumeracao de competencia; sem regra de calculo'}; {'instituto': 'Contribuicao confederativa', 'fundamento': 'CF/88 art. 8o, IV', 'tratado_pelo_cap_12': False, 'nota': 'citado apenas na enumeracao; sem regra de calculo. 1 ocorrencia em todo o manual, na p.299'}; {'instituto': 'Desconto ou contribuic…
- **achado:** o manual NOMEIA quatro institutos e CALCULA apenas um. Os outros tres ficam sem regra. O cap. 12 nao e sobre 'contribuicoes sindicais' no plural - e so sobre a contribuicao sindical do art. 578.

- **sujeito passivo:** todos os que participem de uma categoria economica ou profissional (art. 579, CLT)
**empregado**

- **base calculo:** remuneracao de 1 dia de trabalho, qualquer que seja a remuneracao
- **citacao:** Para o empregado: 01 dia de trabalho, qualquer que seja a remuneracao a ser descontada do empregado na folha de pagamento do mes de marco de cada ano
- **momento:** desconto na folha de pagamento do mes de MARCO de cada ano
- **fundamento:** CLT art. 580, I e art. 582, par. 1o, a, b, c e par. 2o
- **lacunas:** o manual NAO reproduz os prazos de RECOLHIMENTO pelo empregador (art. 583 CLT), nem a regra de admissao apos marco, nem a de rateio ao sindicato/federacao/confederacao (art. 589). Busca nas pp. 299-302: 'prazo' = 0 ocorrencias; 'recolhimento' = 2 na p.301 e 5 na p.302, todas dentro das ementas sobre multa do art. 600.

**empregador**

- **base calculo:** capital social da firma ou empresa registrado nas Juntas Comerciais ou orgaos equivalentes
- **fundamento:** CLT art. 580, III
- **tabela progressiva art 580 III:** {'faixa': 'I', 'descricao': 'Ate 150 vezes o Maior Valor de Referencia (MVR)', 'aliquota_pct': '0,8'}; {'faixa': 'II', 'descricao': 'Acima de 150 ate 1.500 vezes o MVR', 'aliquota_pct': '0,2'}; {'faixa': 'III', 'descricao': 'Acima de 1.500 ate 150.000 vezes o MVR', 'aliquota_pct': '0,1'}; {'faixa': 'IV', 'descricao': 'Acima de 150.000 ate 800.000 vezes o MVR', 'aliquota_pct': '0,02'}
- **piso:** 60% do Maior Valor de Referencia
- **teto:** 800.000 vezes o MVR
- **citacao piso teto:** a contribuicao minima corresponde a 60% do maior valor de referencia e o limite maximo para o calculo da contribuicao sindical equivale a 800.000 vezes o MVR.
- **fundamento piso teto:** art. 580, III, par. 3o, CLT
- **mecanica progressiva:** a tabela e progressiva e o valor corresponde a soma da aplicacao das aliquotas sobre a parcela do capital social distribuida em cada classe; a 'parcela a adicionar' so facilita o calculo
- **citacao mecanica:** A parcela a adicionar tem apenas a finalidade de facilitar o calculo, considerando que a tabela e progressiva
- **defeito estrutural:** A tabela do item 12.2 NAO TEM coluna 'parcela a adicionar'. O paragrafo imediatamente seguinte explica o que e a 'parcela a adicionar' como se a tabela a tivesse. A coluna so aparece nas tabelas RURAIS do item 12.3 (pp. 300-301). Ver defeitos D12-01.
- **remissao externa:** 'Se for necessario apurar a contribuicao sindical, as tabelas anuais constam disponiveis em varios sites da internet de acordo com a categoria do empregador.' - o manual NAO reproduz a tabela urbana anual, nem o valor do MVR.
- **lacuna MVR:** 'MVR' ocorre 5 vezes na p.299 e NENHUM valor de MVR e dado no capitulo. O MVR foi extinto e a serie serie-18.11-otn-btn-mvr.csv existe no corpus; a conversao entre MVR e real NAO e enunciada aqui. Pendencia P12-02.

**rural**

- **fundamento:** Decreto-lei n. 1.166/71, art. 4o, par. 1o
- **regra propria:** a base varia conforme o contribuinte seja pessoa fisica ou juridica
- **pessoa fisica:** base: Valor da Terra Nua Tributavel (VTNt) da propriedade, constante do Cadastro da Secretaria da Receita Federal, o mesmo utilizado para o lancamento do ITR; citacao: Na hipotese de pessoa fisica, a contribuicao e calculada com base no Valor da Terra Nua Tributavel da propriedade
- **pessoa juridica:** base: a parcela do capital social atribuida ao imovel; citacao: Se for pessoa juridica, a base de calculo sera a parcela do capital social atribuida ao imovel.
- **tabelas anuais:** pagina_pdf: 300-301; rubrica_impressa: TABELA VIGENTE CONTRIBUICAO SINDICAL RURAL - [ANO] - BASE LEGAL - ART. 580, III, CLT; anos_reproduzidos: [2011, 2012, 2013, 2014, 2015, 2016]; estrutura: 6 linhas por ano: contribuicao minima; 0,8%; 0,2% + parcela; 0,1% + parcela; 0,02% + parcela; contribuicao maxima; linhas: {'2011': [{'de': '0,01', 'ate': '2.886,14', 'regra': 'Cont. minima R$ 23,08'}, {'de': '2.886,15', 'ate': '5.772,29', 'aliquota_pct': '0,8', 'parcela': '-'}, {'de': '5.772,30', 'ate': '57.722,98', 'aliquota_pct': '0,2', 'parcela': '34,63'}, {'de': '57.722,99', 'ate': '5.772.297,87', 'aliquota_pct': '0,1…
- **exemplo de calculo:** pagina_pdf: 301; citacao: Valor da contribuicao sindical referente a 2015: R$ 28.000.000,00 x 0,02% + 5.972,82 (parcela a adicionar) = 11.572,82; recalculo_Decimal: Decimal('28000000.00') * Decimal('0.0002') + Decimal('5972.82') = Decimal('11572.82'); confere: True; enquadramento: 28.000.000,00 cai na 5a faixa de 2015 (7.319.625,01 a 39.038.000,00), aliquota 0,02%. Abaixo do teto de 13.780,42. CORRETO.; regra_promovida_do_exemplo: R12-EX-01: a aplicacao pratica NAO e progressiva por somatorio de faixas - e 'base x aliquota da faixa + parcela a adicionar'. O enunciado do item 12.2 descreve a progressividade por s…

**forma de atualizacao**

- **pagina pdf:** 301-302
- **regime revogado:** norma: art. 600 da CLT; conteudo: multa de 10% nos 30 primeiros dias, adicional de 2% por mes subsequente de atraso, juros de mora de 1% ao mes e correcao monetaria pelo INPC; citacao: multa de 10% nos 30 (trinta) primeiros dias com adicional de 2% por mes subsequente de atraso, alem de juros de mora de 1% (um por cento ao mes) e correcao monetaria calculada de acordo com o INPC; status: REVOGADO TACITAMENTE pela Lei 8.022 de 12/04/1990
- **regime aplicavel:** norma: art. 2o da Lei 8.022/90; citacao_de_fechamento: atualmente, a atualizacao das contribuicoes sindicais observa os criterios do art. 2o da Lei 8022/90.; conteudo_extraido_das_ementas: multa moratoria de 20% sobre o valor atualizado e juros de mora de 1% ao mes (ementa TRT-3 5a T, 0001201-35.2011.5.03.0098-RO, DEJT 10/02/12) e 'art. 2o, incisos I, II e III da Lei 8.022/1990' (ementa TRT-3 5a T, 0001069-71.2013.5.03.0109 RO, DEJT 19/12/2013); ressalva: O TEXTO DO ART. 2o DA LEI 8.022/90 NAO ESTA REPRODUZIDO no manual. O conteudo acima vem de EMENTAS citadas, nao de enunciado do manual. Padrao 2 do manual inve…
- **fundamento da revogacao:** Sumula 432/TST - Res. 177/2012, DEJT 13, 14 e 15.02.2012 (trata de contribuicao sindical RURAL); TST RR-38300-47.2009.5.04.0012, 4a Turma, Rel. Min. Maria de Assis Calsing, julgado 09/12/2015, DEJT 11/12/2015 - aplica a urbana; TST AIRR-420-40.2012.5.01.0225, 3a Turma, Rel. Des. Conv. Vania Maria da Rocha Abensur, julgado 16/09/2015, DEJT 18/09/2015 - contribuicao sindical URBANA; TRT-3 PJe 0010721-54.2015.5.03.0138 (RO), 1a Turma, Rel. Maria Cecilia Alves Pinto, DEJT 02/03/2016; TRT-3 3a T, 0000033-42.2011.5.03.00148-RO, Conv. Sueli Teixeira, DEJT 02/03/12; TRT-3 5a T, 0001201-35.2011.5.03.0098-RO, Conv. Helder…
- **extensao por analogia:** A Sumula 432/TST trata de contribuicao sindical RURAL; o manual a aplica ANALOGICAMENTE aos empregadores URBANOS. Citacao: 'Tal entendimento esta esposado na Sumula 432/TST, aplicada analogicamente aos empregadores urbanos'. A analogia e do manual e do TST (AIRR-420-40.2012.5.01.0225), nao do enunciado sumular.
- **revogacao do DL 1166 71:** A ementa do TRT-3 5a T (0001201-35.2011.5.03.0098-RO) registra que a Lei 8.022/90 revogou tacitamente o art. 9o do Decreto-Lei 1.166/71, que mandava aplicar a multa do art. 600 da CLT na mora da contribuicao rural. Registro de ementa, nao enunciado do manual.

**cobranca judicial**

- **rito:** execucao de titulo extrajudicial, com os privilegios da Fazenda Publica, EXCETO foro especial
- **fundamento:** art. 606, caput, par. 2o, CLT
- **citacao:** A cobranca judicial e efetuada atraves execucao de titulo extrajudicial e com os privilegios da Fazenda Publica, exceto foro especial nos termos do art. 606, caput, par. 2o.
- **achado:** e a unica passagem do manual em que uma entidade PRIVADA (sindicato) recebe privilegios de Fazenda Publica. Nao confundir com a qualificacao do DEVEDOR como Fazenda Publica, que e o tema do cap. 14.

- **competencia:** fundamento: EC 45 - inciso III do art. 114 da CF/88; alcance: acoes sobre representacao sindical entre sindicatos, entre estes e trabalhadores e entre sindicatos e empregadores

### B.8 Capítulo 14 — precatórios

- **paginas:** 304-306
- **status:** SUPERADO por EC 113/2021 e EC 136/2025 - ESTRUTURA PRESERVADA
- **varredura de superacao:** Nas 471 paginas: 'EC 113' = 0 ocorrencias; a string '136/2025' = 0. O corte normativo mais recente que o capitulo conhece e a EC 62/2009 ('EC 62' nas paginas 90, 305 e 335). O cap. 14 e anterior a EC 113/2021, a EC 136/2025, ao julgamento das ADIs 4357/4425 em seus desdobramentos posteriores e a ADC 58.
- **subitens no corpo:** {'num': '14.1', 'titulo': 'Esclarecimentos gerais', 'pagina_pdf': 304}; {'num': '14.2', 'titulo': 'Diretrizes para elaboracao e atualizacao de calculos em precatorios', 'pagina_pdf': 304}
- **confirmacao do sumario:** CONFERE - dois subitens, ambos na p.304.
**conceito**

- **citacao:** Precatorio e uma ordem judicial de pagamento de debitos da Fazenda Publica (Federal, Estadual ou Municipal), devidos por forca de sentenca judicial transitada em julgado (art. 100, CF/88), constituida em processo formado no juizo de execucao.
- **destino:** Vice-Presidencia Administrativa do Tribunal
- **pagina pdf:** 304

**competencia para calcular**

- **regra:** Diretoria da Secretaria de Calculo na capital; Nucleos dos Foros no interior com mais de uma Vara; Secretarias das Varas nas localidades com uma so Vara
- **fundamento:** art. 1o do Prov. 01/93 e art. 104, par. 4o, do Provimento Geral Consolidado TRT-3
- **excecao:** par. 5o do art. 104 do Provimento Geral Consolidado (publicado em dez/2015) permite calculo por PERICIA ou PELAS PARTES em caso de complexidade, extensao, acumulo de servico ou indisponibilidade de servidor calculista; o calculista confere antes da expedicao
- **citacao excecao:** o calculista conferira os calculos apresentados pelas partes ou pelo perito, antes da expedicao do precatorio ou RPV nos termos do art. 106, par. 5o.
- **pagina pdf:** 304

**RPV**

- **ocorrencias no capitulo:** 1
- **pagina pdf:** 304
- **conteudo:** mencionada uma unica vez, na regra de conferencia previa. O capitulo NAO define o que e RPV, NAO fixa limite de pequeno valor, NAO da prazo de pagamento e NAO diferencia o regime de atualizacao da RPV do de precatorio.
- **busca negativa:** 'pequeno valor' nas pp. 304-306 = 0 ocorrencias (ocorre nas pp. 357, 366 e 367, fora do cap. 14). LACUNA ESTRUTURAL do capitulo.

**fonte das diretrizes**

- **norma:** Ordem de Servico TRT 3a R./VPADM n. 01, de 05 de outubro de 2011, art. 13 (conforme o texto do manual) - reproduzida a Secao VII, arts. 21 e 22
- **defeito:** o manual anuncia 'art. 13' e reproduz os 'arts. 21 e 22'. Ver defeitos D14-01.
- **consideranda da OS:** EC 62 de 09/12/2009 - alterou o art. 100 da CF e acrescentou o art. 97 ao ADCT, regime especial para Estados, DF e Municipios; Resolucao CNJ n. 115 de 29/06/2010; Portaria Conjunta TJMG/TRT3/TRF1/TJMMG n. 01 de 17/08/2011 - ratifica o art. 24-A da Res. CNJ 115/2010
- **pagina pdf:** 304

**diretrizes art 21**

- inc: I; regra: nao acumular percentuais de juros de mora, antes ou depois das amortizacoes de valores pagos na execucao; destacar o valor dos juros; citacao: nao poderao acumular percentuais de juros de mora, antes ou depois das amortizacoes de valores pagos na execucao
- inc: II; regra: deduzir imposto de renda dos creditos de honorarios advocaticios de SUCUMBENCIA e PERICIAIS; citacao: dos creditos de honorarios advocaticios de sucumbencia e periciais devera ser deduzido o imposto de renda
- inc: III; regra: NAO incide imposto de renda sobre honorarios advocaticios ASSISTENCIAIS; citacao: nao incide imposto de renda sobre os honorarios advocaticios assistenciais (art. 150, VI, “c”, CR/1988); achado: fundamento DIVERGENTE do usado no cap. 8. Cap. 8 (p.105) fundamenta a nao incidencia na OS 01/11 VPADM art. 21 III e no Provimento Geral Consolidado art. 206 pars. 1o e 3o. Cap. 14 fundamenta na IMUNIDADE do art. 150, VI, 'c', da CR/1988 - imunidade de entidades sindicais. Mesmo resultado, fundamentos distintos. Registrado, nao harmonizado.
- inc: IV; regra: cota previdenciaria do exequente, IR e cota previdenciaria do empregador devem constar da planilha analitica E do Resumo Geral; a ausencia de qualquer deles, por isencao legal ou outro motivo, exige justificativa propria na planilha, por observacao especifica
- inc: V; regra: acoes plurimas: planilhas eletronicas com valores individualizados e juros de mora em colunas proprias; guarda do arquivo pelo juizo de origem
- inc: VI; regra: art. 790-A, I, da CLT - Fazenda Publica isenta de custas processuais; citacao: devera ser observado o art. 790-A, inciso I, da Consolidacao das Leis do Trabalho – CLT, que isentou a Fazenda Publica do pagamento das custas processuais
- inc: VII; regra: ECT equipara-se a Fazenda Publica para efeito de execucao e do DL 779/1969; citacao: a Empresa Brasileira de Correios e Telegrafos - ECT equipara-se a Fazenda Publica, para efeito de execucao e do disposto no Decreto-Lei no 779, de 21 de agosto de 1969; achado: e a UNICA equiparacao nominada no capitulo. Empresa publica federal, nao sociedade de economia mista. Ver aplicabilidade_fazenda.
- inc: VIII; regra: nao ha juros de mora durante o periodo do art. 100, par. 1o, da CR/1988, sem prejuizo da correcao monetaria; citacao: nao havera incidencia de juros de mora durante o periodo a que se refere o art. 100, par. 1o, da CR/1988, sem prejuizo da correcao monetaria
- inc: IX; regra: vista as partes sempre que houver atualizacao/modificacao dos calculos, independentemente da fase

**juros art 22**

- inc: I; hipotese: decisao transitada determinou juros de 0,5%, ou 'na forma da lei', ou citou a Lei 9.494/1997; regra: juros de 0,5% desde 27/08/2001 (art. 1o-F da Lei 9.494/97, red. MP 2.180-35 de 25/08/2001); a partir de 30/06/2009, red. da Lei 11.960 de 29/06/2009 - indices oficiais de remuneracao basica e juros da caderneta de poupanca, INCLUSIVE nas condenacoes subsidiarias; citacao: serao aplicados juros de 0,5%, desde 27/08/2001
- inc: II; hipotese: decisao exequenda fixou juros da Lei 8.177/91; regra: ate 10/12/2009 (publicacao da EC 62/2009) atualizar na forma das decisoes que os originaram, respeitados indices, juros e penalidades; fundamento: par. 12 do art. 100 da CR/1988 e caput do art. 36 da Res. CNJ 115/2010
- inc: III; hipotese: INDEPENDENTEMENTE do comando exequendo, a partir de 10/12/2009; regra: indice oficial de remuneracao basica da caderneta de poupanca; juros SIMPLES no mesmo percentual dos juros da poupanca; EXCLUIDOS juros compensatorios; fundamento: par. 3o do art. 36 da Res. CNJ 115/2010; citacao: a partir de 10/12/2009, data da publicacao da EC 62/2009, a atualizacao dos valores observara o indice oficial de remuneracao basica da caderneta de poupanca; achado_R8: este inciso e uma EXCECAO EXPRESSA a precedencia do titulo judicial - 'independentemente do comando exequendo'. Contrasta com a R8 do projeto e…

**definicoes do par 1o e 2o**

- par: 1o; texto_resumo: o indice oficial de remuneracao basica da caderneta de poupanca e o indice aplicado mensalmente a poupanca, EXCLUIDA a taxa de juros que o integra; achado: separacao explicita entre o indice de correcao e a taxa de juros dentro da poupanca - evita dupla contagem
- par: 2o; texto_resumo: usar a tabela de atualizacao de precatorios judiciais divulgada mensalmente pelo CNJ, com INDICES DIARIOS, a partir de 29/06/2009; fundamento: par. 2o do art. 36 da Res. CNJ 115/2010; citacao: Devera ser utilizada a tabela de atualizacao de precatorios judiciais divulgada mensalmente pelo CNJ, com indices diarios, a partir de 29/06/2009; achado: indices DIARIOS - o unico ponto do corpus trabalhista extraido que opera em base diaria, e nao mensal

**criterios adicionais do manual**

- **pagina pdf:** 306
- **nota:** sao criterios do proprio manual, fora da OS: 'Em materia de calculo, alem da diretrizes acima, o calculista devera observar, ainda, os seguintes criterios'
- **itens:** {'letra': 'a', 'regra': 'imposto de renda: embora o Municipio, suas autarquias e fundacoes nao tenham obrigatoriedade de recolhimento (art. 158, I, CF/88), o IR DEVE ser deduzido do credito do reclamante e constar no resumo', 'citacao': 'embora o Municipio, suas autarquias e fundacoes nao tenham a obrigatoriedade do recolhimento face o disposto no art. 158, I, da CF/88, o mesmo devera ser deduzido do credito do reclamante e constar no resumo de calculo', 'achado': 'o IR e DEDUZIDO mas nao e RECOLHIDO a Uniao - fica com o Municipio por reparticao constitucional de receita. Regra de calculo com consequencia de des…

**o que o capitulo NAO traz**

- Nenhum exemplo numerico. Zero planilhas. O cap. 14 e o unico dos tres extraidos aqui sem exemplo - o padrao 1 do manual (regra mora no exemplo) nao se aplica, e a consequencia e que a operacao de atualizacao de precatorio nao esta demonstrada em lugar nenhum.
- Nenhuma definicao ou limite de RPV / obrigacao de pequeno valor.
- Nenhum prazo constitucional de pagamento em numero de meses ou datas (so a remissao ao art. 100, par. 1o, CR).
- Nenhuma regra de precatorio COMPLEMENTAR ou SUPLEMENTAR.
- Nenhuma regra sobre ordem cronologica, preferencia alimentar, superpreferencia por idade/doenca, compensacao ou cessao de credito.
- Nenhuma mencao a sociedade de economia mista ('economia mista' = 0 ocorrencias em todas as 471 paginas; 'sociedade' = 0 ocorrencias nas pp. 304-306).


### B.9 Cruzamento com o cap. 5 do CJF

- **fonte trt3:** cap. 14, pp. 304-306 (offset 0)
- **fonte cjf:** docs/calculo/extracao/justica-federal/bloco-08-jf.md secao 7 (capitulo 5 - requisicoes, pagina_pdf CJF 88-93) e secao 8 (EC 136/2025)
- **fonte corpus:** docs/calculo/00-base-normativa.md secao 5 (EC 136/2025 - Fazenda Publica)
- **nao harmonizado:** True
**diferencas**

- eixo: edicao e alcance temporal; trt3_2016: para no regime da EC 62/2009 + Res. CNJ 115/2010. Ultimo corte: 10/12/2009; cjf_2026: EC 113/2021, EC 114/2021 e, na fase pre-requisitorio, EC 136/2025 (Res. CJF 990/2026). Cortes em dez/2021 e set/2025; achado: DEFASAGEM DE 17 ANOS DE NORMA. O cap. 14 nao conhece nada posterior a 2011.
- eixo: indexador do precatorio; trt3_2016: indice oficial de remuneracao basica da caderneta de poupanca (TR), com juros simples no mesmo percentual da poupanca, excluidos compensatorios, a partir de 10/12/2009, INDEPENDENTEMENTE do comando exequendo; cjf_2026: Selic de dez/2021 ate set/2025 na fase pre-requisitorio; depois IPCA + taxa legal. Na REQUISICAO: indexador administrativo indicado na Resolucao do CJF a partir de 2011, e IPCA-E/IBGE nos precatorios das propostas orcamentarias de 2001 a 2010; corpus_00_secao_5: EC 136/2025: nos requisitorios da Fazenda Publica FEDERAL, da expedicao ate o pagamento, IPCA +…
- eixo: assimetria de incidencia; trt3_2016: o par. 1o do art. 22 da OS separa o indice da poupanca da taxa de juros que o integra, para evitar dupla contagem, mas nao diz sobre QUE massa cada um incide; cjf_2026 / corpus: CNJ Prov. 207/2025 fixa assimetria explicita: IPCA sobre principal+juros; 2% a.a. so sobre o principal; achado: a assimetria e regra de implementacao posterior e nao tem antecedente no cap. 14
- eixo: suspensao de juros no prazo constitucional; trt3_2016: art. 21, VIII: nao ha juros de mora no periodo do art. 100, par. 1o, CR/1988, sem prejuizo da correcao monetaria. NAO da datas nem duracao; cjf_2026: R-08-16: suspendem-se os juros no prazo constitucional de 1o de julho (ate 2021) e 2 de abril (a partir de 2022) ATE O FINAL DO EXERCICIO SEGUINTE (SV 17 e Tema 1.037 do STF), inclusive nas desapropriacoes; RPV: 60 dias da apresentacao; achado: CONVERGEM NO PRINCIPIO, DIVERGEM NA OPERACIONALIZACAO. O TRT-3 remete a Constituicao; o CJF da as duas datas e a duracao. O cap. 14 e inoperavel sem essa informaca…
- eixo: data de apresentacao; trt3_2016: AUSENTE - o capitulo nao fixa data de apresentacao do precatorio; cjf_2026: R-08-15: 1o de julho ate 2021, 2 de abril a partir de 2022; achado: LACUNA do lado trabalhista
- eixo: requisicao complementar; trt3_2016: AUSENTE. 'complementar' nas pp. 304-306 = 0 ocorrencias; cjf_2026: item 5.2: quatro hipoteses (juros entre a data do calculo e a apresentacao; juros apos o prazo; correcao quando o indexador judicial for maior que o administrativo; correcao apos o prazo). R-08-17: o indexador troca TRES vezes dentro de uma requisicao complementar - original ate a apresentacao, administrativo no prazo constitucional, original de novo depois; achado: LACUNA ESTRUTURAL. A requisicao complementar e o principal problema de calculo em precatorio e o cap. 14 nao a menciona.
- eixo: requisicao suplementar; trt3_2016: AUSENTE; cjf_2026: item 5.3: valor pendente de controversia ou erro material reconhecido judicialmente. R-08-20: quando o criterio muda, REFAZER a conta originaria com a mesma data-base, vedada a incidencia de juros sobre juros; achado: LACUNA
- eixo: imputacao de pagamento parcial; trt3_2016: letra c da p.306: amortizar pela data do pagamento, nao pela do levantamento. Nao ha regra de ordem de imputacao; cjf_2026: R-08-18: o art. 354 do CC NAO se aplica ao precatorio complementar, que segue legislacao propria; aplica-se sim ao pagamento parcial de credito NAO sujeito a requisicao (item 4.1.8); achado: DIVERGENCIA DE EIXO. O TRT-3 regula o MARCO TEMPORAL da amortizacao; o CJF regula a ORDEM DE IMPUTACAO. Os dois sao necessarios e cada manual so tem um.
- eixo: RPV; trt3_2016: mencionada 1 vez, sem definicao, sem limite, sem prazo; cjf_2026: regime proprio: prazo de 60 dias a partir da apresentacao, com suspensao de juros nesse prazo (R-08-16, NOTA 2); achado: LACUNA
- eixo: equiparacao a Fazenda Publica; trt3_2016: apenas a ECT, e 'para efeito de execucao e do disposto no DL 779/1969' (art. 21, VII); cjf_2026 / corpus: nao ha rol de equiparacao registrado; a EC 136/2025 restringe a Fazenda Publica FEDERAL; achado: o cap. 14 tem UM caso nominado e nenhum criterio geral. Ver aplicabilidade_fazenda.
- eixo: juros de 0,5% e art. 1o-F da Lei 9494/97; trt3_2016: art. 22, I: 0,5% desde 27/08/2001; poupanca desde 30/06/2009, inclusive nas condenacoes SUBSIDIARIAS; cjf_2026: cadeia cjf.trabalhista.juros-mora bifurca em ago/2001 por qualidade do devedor e NAO reconverge - o ramo privado segue em 1,0%; achado: CONVERGEM NA DATA (ago/2001) e no percentual (0,5%). E o unico ponto de convergencia numerica forte entre o cap. 14 e o manual do CJF. A extensao as condenacoes SUBSIDIARIAS e regra do TRT-3 sem paralelo no CJF.
- eixo: imposto de renda em ente publico; trt3_2016: letra a da p.306: deduzir do credito e lancar no resumo ainda que Municipio/autarquia/fundacao nao tenham obrigacao de recolher (art. 158, I, CF/88); cjf_2026: nao registrado no corpus; achado: regra exclusiva do lado trabalhista
- eixo: honorarios assistenciais e IR; trt3_2016: art. 21, III: nao incide, por IMUNIDADE do art. 150, VI, 'c', CR/1988; cjf_2026: nao ha a figura dos honorarios assistenciais sindicais; achado: instituto sem paralelo

**convergencias**

- Juros suspensos no prazo constitucional de pagamento - mesmo principio nos dois (TRT-3 art. 21, VIII; CJF R-08-16).
- Juros de 0,5% para a Fazenda Publica desde ago/2001, art. 1o-F da Lei 9494/97.
- Exclusao de juros compensatorios em precatorio (TRT-3 art. 22, III; CJF R-08-19 para desapropriacao).
- Excecao expressa a precedencia do titulo quando a lei superveniente muda o indexador (TRT-3 art. 22, III 'independentemente do comando exequendo'; CJF R-08-01 / NOTA 2 do item 4.1.2).


### B.10 Aplicabilidade da Fazenda Pública

- **pergunta:** O capitulo 14 e sequer aplicavel ao caso de uso?
- **resposta:** CONDICIONAL. Nao resolvida - e correto que nao seja, porque nao e materia de calculo.
**fato 1 pendencia do corpus**

- **fonte:** docs/calculo/00-base-normativa.md, secao 9, pendencia 1
- **texto:** 'Classificacao da Gasmig como Fazenda Publica ou nao' - tipo: Determinacao juridica do cliente; bloqueia: Tamanho do catalogo
- **nota do corpus:** 'Pendencia 1 e a de maior impacto. Se a Gasmig nao for Fazenda Publica, somem do escopo: o ramo FP das tres jurisdicoes, precatorio, EC 113/136 e a consolidacao de dez/2021. Nao e pesquisa - e pergunta ao juridico do cliente, ou leitura de como os juizes vem decidindo nos processos existentes.'

**fato 2 alcance da EC 136**

- **fonte:** docs/calculo/00-base-normativa.md, secao 5
- **texto:** A nova redacao do art. 3o da EC 113/2021 alcanca 'Nos requisitorios que envolvam a Fazenda Publica federal'. Tres estreitamentos simultaneos: objeto (so requisitorios), ente (so Fazenda Publica FEDERAL), periodo (da expedicao ate o pagamento).
- **consequencia registrada no corpus:** 'Fazenda Publica estadual e municipal: a nova redacao menciona apenas Fazenda Publica federal. Requisitorios estaduais e municipais ficam sem a regra antiga (revogada) e sem a nova (que nao os alcanca).'

**fato 3 o que o manual do TRT3 oferece**

- **criterio de isencao de custas cap 8:** art. 790-A, I, CLT - entes publicos 'que NAO EXPLOREM ATIVIDADE ECONOMICA'. Esta clausula e o teste do cap. 8, e ela EXCLUI sociedade de economia mista exploradora de atividade economica.
- **criterio de isencao de custas cap 14:** letra e da p.306 - 'orgaos publicos das tres esferas da administracao publica direta E INDIRETA, inclusive fundacoes e autarquias', SEM a clausula da atividade economica. Administracao indireta abrange empresa publica e sociedade de economia mista.
- **divergencia interna:** OS DOIS CAPITULOS DO MESMO MANUAL DAO TESTES DIFERENTES PARA A MESMA PERGUNTA. Sob o cap. 8, uma distribuidora de gas sociedade de economia mista paga custas; sob o cap. 14, nao paga. Registrado como D14-02. NAO HARMONIZADO.
- **unica equiparacao nominada:** ECT (art. 21, VII da OS), empresa publica federal, e apenas 'para efeito de execucao e do disposto no DL 779/1969'. NAO ha criterio geral de equiparacao, nem mencao a sociedade de economia mista em nenhuma das 471 paginas.

**condicional registrada**

- **se Fazenda Publica:** Aplica-se o cap. 14 INTEIRO como estrutura procedimental: competencia para calcular (14.1), as nove diretrizes do art. 21 e as tres regras de juros do art. 22 da OS 01/2011.; MAS o regime de atualizacao do art. 22, III (TR da poupanca desde 10/12/2009) esta SUPERADO e deve ser substituido pelo regime vigente, que NAO esta no cap. 14: EC 113/2021 (Selic desde dez/2021) e, a partir de set/2025, EC 136/2025 - e esta so alcanca a Fazenda Publica FEDERAL.; Se for Fazenda Publica ESTADUAL (que e o caso de uma sociedade de economia mista estadual, se classificada como tal), cai-se exatamente no vacuo declarado na secao 5 de 00-base-normativa.md: sem a regra antiga (revogada pela EC 113) e sem a no…
- **se NAO Fazenda Publica:** O cap. 14 NAO SE APLICA em sua parte nuclear: nao ha precatorio, nao ha RPV, nao ha art. 100 da CF, nao ha prazo constitucional, nao ha suspensao de juros, nao ha regime de EC 62/113/136.; Cai tambem o art. 22, I do cap. 14: os juros de 0,5% do art. 1o-F da Lei 9494/97 nao se aplicam; volta o regime de juros do art. 39 da Lei 8.177/91 (1% ao mes), tratado no cap. 7 do manual.; Cai a isencao de custas do art. 790-A, I, da CLT, e a entidade paga custas processuais e custas de execucao pelo cap. 8.; Sobrevive, como boa pratica de calculo e nao como norma de precatorio, apenas a letra c da p.306 (amortizar pela data do pagamento) e a letra d (individualizacao dos creditos, ancorada na IN RFB 15…

- **nao resolvido deliberadamente:** A classificacao da sociedade de economia mista nao e materia de calculo. Nao foi decidida aqui, conforme instrucao. O que foi feito: registrar que o PROPRIO MANUAL contem dois testes incompativeis (cap. 8 com a clausula de atividade economica, cap. 14 sem ela), de modo que ele nao pode ser invocado como fonte para resolver a pendencia 1.

### B.11 Defeitos

20 catalogados. Nenhum corrigido.

| # | `pagina_pdf` | Defeito | Impresso | Correto |
|---|---|---|---|---|
| D8-01 | 106 |  | Hon. Advocaticios assistenciais (15% s/ 277.338,69) | 277.338,39 |
| D8-02 | 100 |  | 44, 26 | 44,26 |
| D8-03 | 102 |  | IN n. GP/CR/VCR n. 001/02/TRT-3a Regiao 01/02 TRT/3a Regiao, 7o, II | IN GP/CR/VCR n. 001/02/TRT-3a Regiao, art. 7o, II |
| D8-04 | 102 |  | nao mencionam a incidencia dos de juros sobre os honorarios periciais | nao mencionam a incidencia de juros |
| D8-05 | 104 |  | Dr. Joe Henrique | provavelmente 'Dr. Jose Henrique' |
| D8-06 | 132 |  | Custas execucao s/ o calculo de liquidacao (Vr. Bruto do recte + INSS recda) x 0,5% | a base efetivamente usada e o TOTAL DO CALCULO (todas as linhas do resumo antes da propria CE) |
| D8-07 | 132 |  | TOTAL DO CALCULO EM 31/01/16 = 5.233,58 | 5.233,57 |
| D8-08 | 280 |  | base das custas de execucao 30.312,80 e TOTAL DO CALCULO 30.464,37 | 30.312,81 e 30.464,36 |
| D12-01 | 299 |  | tabela do art. 580, III, com 4 colunas (faixa, descricao, aliquota) e paragrafo seguinte explicando a 'parcela a adicionar' | a tabela deveria ter a coluna 'parcela a adicionar', ou o paragrafo nao deveria estar ali |
| D12-02 | 300 |  | tabela 2013: 'De 0,01 a 3.255,47' seguida de 'De 3.255,47 a 6.510,95' | 'De 3.255,48 a 6.510,95' |
| D12-03 | 300 |  | tabela 2013: 'De 6.510.958,68' | 'De 6.510.956,68' |
| D12-04 | 300 |  | tabela 2013: 'ate 34.725,102,22' | 34.725.102,22 |
| D12-05 | 300 |  | tabela 2014: 'De 68.957,56 ate 6.89.754,21' | 6.895.754,21 |
| D12-06 | 300-301 |  | em todos os 6 anos, a linha de contribuicao maxima diz 'Acima de X' repetindo o X que a faixa anterior ja usa como limite superior | coerente, mas deixa o proprio X sem regra explicita de qual linha aplica |
| D12-07 | 300 |  | contribuicao maxima 2011 = R$ 10.867,51 | 10.867,32 pelo fecho da propria tabela |
| D14-01 | 304 |  | 'As diretrizes para a elaboracao dos calculos em precatorios estao fixadas nos art. 13, da Ordem de Servico no 01, de 05/10/11' | arts. 21 e 22 da mesma Ordem de Servico |
| D14-02 | 306 contra 100 e 102 |  | p.306 letra e: 'Estao isentos os orgaos publicos das tres esferas da administracao publica direta e indireta, inclusive fundacoes e autarquias' | incompativel com o cap. 8, que exige 'que nao explorem atividade economica' (art. 790-A, CLT) nas pp. 100 e 102 |
| D14-03 | 304 |  | 'nas Secretarias das Varas do Trabalhos nas demais localidades' | Varas do Trabalho |
| D14-04 | 304 |  | '(Art. 1o do Prov. 01/93 e art., 104, par. 4o do Provimento Geral Consolidado' | art. 104 |
| D14-05 | 306 |  | 'Em materia de calculo, alem da diretrizes acima' | alem das diretrizes |

### B.12 Pendências

- id: P10-18; status: PARCIALMENTE RESOLVIDA E RECLASSIFICADA; texto: O cap. 8 enuncia a base das CE por EXCLUSAO (item 8.2.1, itens 2 e 3), nao por composicao. Confirma que honorarios e imprensa oficial ENTRAM e que so as custas do conhecimento SAEM. Nao enderecà o eixo bruto x liquido. A divergencia numerica medida pelo bloco 10 nao era bruto x liquido: era o juro Selic sobre o INSS cota-reclamante (Decimal('35.29')…
- id: P10-18b; status: ABERTA; texto: A unica exclusao autorizada pelo item 8.2.1 (custas processuais da fase de conhecimento) nunca e praticada em nenhum dos quatro exemplos de CE do manual (pp. 132, 137, 163, 280), porque nenhum deles traz essa linha no resumo. Nao ha demonstracao de como a exclusao opera.
- id: P8-01; status: ABERTA; texto: Os incisos III a V do art. 7o da IN GP/CR/VCR 001/02/TRT-3, que listam hipoteses adicionais de nao incidencia das CE, sao apenas REMETIDOS pelo manual ('e demais hipoteses previstas nos incisos III ao V'), nunca reproduzidos. Norma regional fora do corpus.
- id: P8-02; status: ABERTA; texto: O item 8.1 nao diz QUEM paga as custas processuais da fase de conhecimento nem QUANDO. So a base, a aliquota, o piso e as isencoes. O manual do CJF cobre esse eixo (metade na distribuicao, metade do vencido ou recorrente); o do TRT-3 nao.
- id: P8-03; status: ABERTA; texto: As tabelas de custas e emolumentos do Anexo II da IN 001/2002 sao valores nominais sem data-base declarada, e o item 8.2 diz expressamente que nao se atualizam. Confirmar se os valores de 2016 ainda sao os de 2002 e qual a tabela vigente hoje.
- id: P8-04; status: ABERTA; texto: Tensao interna no item 8.3: a nota de rodape 8 (p.102) manda usar a tabela 'Das Acoes Civeis em Geral - Acoes Condenatorias em Geral', sem Selic, da Justica Federal Seccional MG; o corpo, cinco paragrafos abaixo, declara IPCA-E (Res. CSJT 66/10 e Provimento Consolidado TRT-3 art. 220, par. 2o). Nao harmonizado.
- id: P8-05; status: ABERTA - DIVERGENCIA JURISPRUDENCIAL, NAO RESOLVER; texto: Juros de mora sobre honorarios periciais. Corrente A (sem juros, 4 acordaos, fundamento OJ 198 + Lei 6899/81, despesa judicial) x Corrente B (com juros, 2 acordaos, fundamento art. 407 do CC). O manual adota a corrente A como pratica da Secretaria, mas reproduz as duas. Ambas viram variante com fundamento proprio.
- id: P8-F4-01; status: FASE 4; texto: Art. 791-A da CLT (Lei 13.467/2017) nao esta no corpus. Varredura: '791-A' = 0 ocorrencias no manual do TRT-3; docs/ tem apenas mencoes de escopo. O texto da norma precisa entrar antes de qualquer calculo de sucumbencia trabalhista.
- id: P8-F4-02; status: FASE 4 - PENDENCIA DE DADO; texto: Os VALORES das faixas do art. 85, par. 3o, do CPC nao existem em lugar nenhum do corpus. Buscas em toda a arvore docs/: '200 salarios', '1.000 salarios', '2.000 salarios', '20.000 salarios', '100.000 salarios' = 0 ocorrencias; 'art. 85' aparece so em notas de escopo. Existe apenas a REGRA de progressividade, em bloco-08-jf.md R-08-21. O enunciado apontou docs/…
- id: P8-F4-03; status: FASE 4; texto: A base dos honorarios com FGTS a depositar incluido (regra do TRT-3 de 2016, pp. 105-106) sobrevive ao art. 791-A? E a exclusao da cota patronal de INSS pela TJP 4 do TRT-3? Nada no corpus responde.
- id: P12-01; status: ABERTA; texto: O texto do art. 2o da Lei 8.022/90 - que e o regime de atualizacao efetivamente aplicavel segundo o proprio manual - NAO esta reproduzido no cap. 12. Os percentuais (multa de 20% e juros de 1% a.m.) so aparecem dentro de EMENTAS citadas. Fundamento fora do corpus.
- id: P12-02; status: ABERTA; texto: O cap. 12 usa MVR (Maior Valor de Referencia) como unidade em toda a tabela do art. 580, III, e nao da nenhum valor de MVR nem regra de conversao. Existe docs/calculo/extracao/trabalhista/serie-18.11-otn-btn-mvr.csv no corpus; a ligacao entre a tabela do art. 580 e essa serie nao esta feita.
- id: P12-03; status: ABERTA; texto: Prazos de recolhimento da contribuicao sindical (art. 583 CLT), regra de admissao apos marco, e rateio entre sindicato/federacao/confederacao (art. 589 CLT) nao constam do cap. 12. Busca 'prazo' nas pp. 299-302 = 0 ocorrencias.
- id: P12-04; status: FASE 4; texto: Lei 13.467/2017 - contribuicao sindical facultativa, condicionada a autorizacao previa e expressa. Nao esta no corpus. Varredura no manual: '13.467' = 0, 'facultativ' = 0, 'autorizacao previa' = 0. Necessaria para fixar o corte de 11/11/2017.
- id: P12-05; status: ABERTA; texto: Tabela urbana anual da contribuicao sindical do empregador nao reproduzida - o manual remete a 'varios sites da internet'. Apenas as tabelas RURAIS de 2011 a 2016 estao no manual.
- id: P14-01; status: ABERTA; texto: O cap. 14 nao tem nenhum exemplo numerico. A operacao de atualizacao de precatorio nao esta demonstrada em lugar nenhum do manual. Unico dos tres capitulos extraidos sem planilha.
- id: P14-02; status: ABERTA; texto: RPV mencionada uma unica vez, sem definicao, limite, prazo ou regime proprio. 'pequeno valor' = 0 ocorrencias nas pp. 304-306.
- id: P14-03; status: ABERTA; texto: Requisicao COMPLEMENTAR e SUPLEMENTAR ausentes do cap. 14. O manual do CJF as cobre (itens 5.2 e 5.3) com regras operacionais pesadas (R-08-17: tres indexadores dentro de uma requisicao; R-08-20: refazer a conta). Lacuna estrutural do lado trabalhista.
- id: P14-04; status: ABERTA; texto: A Ordem de Servico TRT 3a R./VPADM n. 01/2011 e reproduzida so parcialmente (Secao VII, arts. 21 e 22). O art. 13 anunciado nao aparece. Norma regional fora do corpus.
- id: P14-05; status: BLOQUEANTE - REMETE A PENDENCIA 1 DA SECAO 9 DE 00-base-normativa.md; texto: Aplicabilidade do cap. 14 depende da classificacao da sociedade de economia mista como Fazenda Publica. O manual NAO pode ser fonte para decidir, porque contem dois testes incompativeis (cap. 8 com a clausula 'que nao explorem atividade economica'; cap. 14 letra e sem ela, e com 'administracao direta e indireta'). Ver D1…
- id: P14-06; status: ABERTA; texto: Se a entidade for Fazenda Publica ESTADUAL, nem o cap. 14 (TR da EC 62), nem a EC 113/2021 (revogada no ponto), nem a EC 136/2025 (so federal) dao o regime. Vacuo ja declarado na secao 5 de 00-base-normativa.md e nao preenchido por esta extracao.

### B.13 Buscas que sustentam as negativas

| Termo | Escopo | Ocorrências | Conclusão |
|---|---|---|---|
| `` | 471 paginas, texto integral via PyMuPDF | 0 |  |
| `` | 471 paginas | 0 | 'CPC' ocorre em 7 paginas: 9, 13, 38, 39, 77, 302, 362. Nenhuma no cap. 8. |
| `` | pp. 100-106 | bruto: p.105 x2, p.106 x2 (todas sobre honorarios advocaticios). liquido: p.104 x1, p.105 x2, p.106 x2 (IR de peritos e honorarios). ZERO nos itens 8.2 e 8.2.1. |  |
| `` | 471 paginas | 0 | '151,56' ocorre em 1 pagina (280). O 151,39 e valor calculado pelo bloco 10. |
| `` | 471 paginas | 4 paginas: 83, 100, 101, 102 | a forma 'Custas execucao' (sem 'de') aparece em 16 paginas: 132, 137, 138, 160, 163, 280, 283, 285, 286, 287,… |
| `` | 471 paginas | 0 |  |
| `` | 471 paginas | 0 |  |
| `` | 471 paginas | 1 cada, ambas na p.299, na mesma frase de delimitacao de competencia |  |
| `` | pp. 299-302 | 0 |  |
| `` | pp. 304-306 | 0 | 'RPV' ocorre 1 vez, p.304. No manual inteiro, 'RPV' esta nas pp. 12, 304, 365, 366, 367 e 'pequeno valor' nas… |
| `` | 471 paginas | 0 | 'EC 62' ocorre nas pp. 90, 305 e 335. E o corte mais recente que o manual conhece. |
| `` | 471 paginas | 0 | 'sociedade' nas pp. 304-306 = 0. A unica equiparacao nominada a Fazenda Publica no cap. 14 e a ECT (art. 21,… |
| `` | pp. 304-306 | 0 | 'poupanca' ocorre 2x na p.305 e 3x na p.306 - o indexador do capitulo e a TR da poupanca. |
| `` | pp. 304-306 | 0 |  |
| `` | pagina_pdf 6 (sumario) | 0 | o sumario lista 8.1 (p.100), 8.2 (p.100), 8.3 (p.102) e 8.4 (p.105). O corpo tem 8.2.1 na p.101. |
| `` | docs/calculo/extracao/justica-federal/b… | custas: 1 (tabela de series OUT_OF_SCOPE); capitulo 1: 0 | esta em bloco-08-jf-detalhe.md secao 1, com 13 ocorrencias de 'custas' e 2 de 'capitulo 1'. |
| `` | toda a arvore C:/projetos/skill-calculo… | 0 |  |

---

## C. Capítulo 16 — varredura dirigida

### C.1 Fronteiras

- **fonte pdf:** C:\Users\Rafaela\Downloads\Plataforma-SaaS-Jus\manual-de-calculo-trabalhista_2016-1.pdf
- **paginas pdf total:** 471
- **offset paginacao:** 0
- **metodo:** PyMuPDF 1.27.2.3; doc[pagina-1].get_text(); encoding utf-8
- **cap16 inicio pagina pdf:** 310
- **cap16 inicio literal:** 16 - PROMOCOES
- **cap16 fim pagina pdf:** 336
- **cap17 inicio pagina pdf:** 337
- **cap17 inicio literal:** 17 - Sumulas, Orientacoes Jurisprudenciais e TJP - TST e TRT-3a Regiao
- **paginas varridas:** 27
- **confirmado:** True
**cabecalhos de capitulo detectados no pdf**

- **1:** 9
- **2:** 10
- **3:** 11
- **4:** 13
- **5:** 14
- **6:** 18
- **7:** 83
- **8:** 100
- **9:** 107 (nao capturado pelo regex de caixa-alta; inicio adotado 107 conforme enunciado)
- **10:** 209
- **11:** 278
- **12:** 299
- **13:** 303
- **14:** 304
- **15:** 307
- **16:** 310
- **17:** 337


### C.2 Estrutura real

- **observacao:** Numeracao conferida no corpo do PDF (nao no sumario). A estrutura anunciada (16.1 a 16.4, com 16.4.1 a 16.4.12) confere. Ha um defeito: 16.4.4.12 aparece duas vezes.
**itens**

- item: 16.1; titulo: Estrutura geral de qualquer promocao; pagina_pdf: 310
- item: 16.2; titulo: Campos Obrigatorios; pagina_pdf: 310
- item: 16.3; titulo: Estruturas dos cinco principais tipos de promocoes; pagina_pdf: 311
- item: 16.3.1; titulo: Pedindo elementos; pagina_pdf: 311
- item: 16.3.2; titulo: Reiterando pedido de elementos; pagina_pdf: 311
- item: 16.3.3; titulo: Manifestando sobre impugnacoes das partes; pagina_pdf: 311
- item: 16.3.4; titulo: Pedindo retorno dos autos ao perito; pagina_pdf: 311
- item: 16.3.5; titulo: Manifestando sobre calculos das partes; pagina_pdf: 312
- item: 16.4; titulo: Exemplos de textos por assunto; pagina_pdf: 312
- item: 16.4.1; titulo: Pedindo elementos; pagina_pdf: 312
- item: 16.4.1.1; titulo: Variacao salarial; pagina_pdf: 312
- item: 16.4.1.2; titulo: Percentuais de aumentos concedidos a titulo de promocao ou enquadramento; pagina_pdf: 312
- item: 16.4.1.3; titulo: Valor efetivamente levantado mediante alvara; pagina_pdf: 312
- item: 16.4.1.4; titulo: Valor efetivamente recolhido ao INSS e a RECEITA; pagina_pdf: 313
- item: 16.4.1.5; titulo: Elementos diversos; pagina_pdf: 313
- item: 16.4.1.6; titulo: Diretriz do Juiz sobre diversos aspectos; pagina_pdf: 313
- item: 16.4.2; titulo: Manifestando sobre calculo das partes; pagina_pdf: 313
- item: 16.4.3; titulo: Informando sobre INSS; pagina_pdf: 314
- item: 16.4.3.1; titulo: Como foram feitos os calculos de INSS mes a mes; pagina_pdf: 314
- item: 16.4.3.2; titulo: Como foram feitos os calculos do INSS patronal; pagina_pdf: 314
- item: 16.4.3.3; titulo: Forma de atualizacao da contribuicao previdenciaria; pagina_pdf: 314
- item: 16.4.3.4; titulo: Que nao ha INSS a recolher; pagina_pdf: 316
- item: 16.4.3.5; titulo: Extinta relacao juridica; pagina_pdf: 316
- item: 16.4.3.6; titulo: Empresa optante pelo SIMPLES ou SIMPLES NACIONAL, o calculo abrange apenas a cota do reclamante; pagina_pdf: 317
- item: 16.4.3.7; titulo: Microempresa ou empresa de pequeno porte e opcao pelo SIMPLES ou SIMPLES NACIONAL; pagina_pdf: 317
- item: 16.4.3.8; titulo: Extinta relacao juridica e empresa optante pelo SIMPLES ou SIMPLES NACIONAL; pagina_pdf: 317
- item: 16.4.3.9; titulo: Extinta relacao juridica e entidade beneficente de assistencia social isenta das contribuicoes sociais patronais; pagina_pdf: 317
- item: 16.4.3.10; titulo: Extinta relacao juridica entre duas pessoas fisicas; pagina_pdf: 317
- item: 16.4.3.11; titulo: Empregado domestico; pagina_pdf: 318
- item: 16.4.3.12; titulo: Contribuicao de terceiros; pagina_pdf: 318
- item: 16.4.3.13; titulo: Solicitacao para que o perito que elaborou o calculo apure a contribuicao previdenciaria com os juros e a multa desde a efetiva prestacao de servicos; pagina_pdf: 318
- item: 16.4.3.14; titulo: Solicitacao para que as partes forneçam os elementos necessarios a adequacao do calculo previdenciario ao disposto na Lei 11941/09; pagina_pdf: 318
- item: 16.4.3.15; titulo: Apuracao contribuicao previdenciaria referente a periodo anterior a 1980; pagina_pdf: 319
- item: 16.4.3.16; titulo: Justificando a nao incidencia de INSS sobre valores de ajuda-alimentacao ou vale transporte deferidos em sentenca; pagina_pdf: 319
- item: 16.4.3.17; titulo: INSS cota reclamante com juros e multa da legislacao previdenciaria e a relacao com o credito liquido do reclamante; pagina_pdf: 319
- item: 16.4.3.18; titulo: Justificando a nao imputacao dos juros e a multa da legislacao previdenciaria ao reclamante; pagina_pdf: 319
- item: 16.4.3.19; titulo: Desoneracao da folha de pagamento; pagina_pdf: 320
- item: 16.4.4; titulo: Informando sobre IRRF; pagina_pdf: 322
- item: 16.4.4.1; titulo: Incidencia sobre valor efetivamente levantado e nao sobre o total do credito; pagina_pdf: 322
- item: 16.4.4.2; titulo: Diretrizes quanto ao recalculo do imposto de renda, quando ha valor incorreto recolhido a titulo de IR apos as novas regras determinadas pelo art. 12-A da Lei 7713/88; pagina_pdf: 322
- item: 16.4.4.3; titulo: Justificando a nao aplicacao da Instrucao Normativa RFB 1127/11 em periodo anterior a 2010; pagina_pdf: 323
- item: 16.4.4.4; titulo: Diminuicao do valor apurado nos calculos homologados em razao da retificacao da base de calculo do imposto de renda; pagina_pdf: 323
- item: 16.4.4.5; titulo: IR sobre danos morais; pagina_pdf: 324
- item: 16.4.4.6; titulo: IR sobre honorarios periciais; pagina_pdf: 324
- item: 16.4.4.7; titulo: IR sobre honorarios sucumbenciais (pessoa juridica); pagina_pdf: 324
- item: 16.4.4.8; titulo: IR sobre juros; pagina_pdf: 324
- item: 16.4.4.9; titulo: Repelindo a tributacao em separado do 13o; pagina_pdf: 325
- item: 16.4.4.10; titulo: Justificando a nao apuracao do imposto de renda sobre o valor liquido levantado; pagina_pdf: 325
- item: 16.4.4.11; titulo: Justificando a atualizacao do imposto de renda com juros e multa aplicaveis aos tributos federais pelo recolhimento fora do prazo; pagina_pdf: 326
- item: 16.4.4.12 (1a ocorrencia); titulo: Valores de imposto de renda depositados a disposicao com o objetivo de pagamento e nao liberados no momento oportuno; pagina_pdf: 326
- item: 16.4.4.12 (2a ocorrencia - DEFEITO); titulo: Incidencia de imposto de renda sobre a multa do acordo; pagina_pdf: 327
- item: 16.4.4.13; titulo: Incidencia de imposto de renda sobre a multa de litigancia de ma fe; pagina_pdf: 327
- item: 16.4.5; titulo: Informando sobre juros de mora; pagina_pdf: 327
- item: 16.4.5.1; titulo: Juros sobre juros; pagina_pdf: 327
- item: 16.4.5.2; titulo: Juros e Falencia; pagina_pdf: 328
- item: 16.4.5.3; titulo: Juros decrescentes (o que sao e como se atualizam); pagina_pdf: 329
- item: 16.4.5.4; titulo: Explicando a metodologia de atualizacao do valor dos juros; pagina_pdf: 329
- item: 16.4.6; titulo: Criterios de atualizacao monetaria; pagina_pdf: 329
- item: 16.4.6.1; titulo: Amparo legal da correcao dos debitos trabalhistas; pagina_pdf: 329
- item: 16.4.6.2; titulo: FGTS - atualizacao; pagina_pdf: 329
- item: 16.4.6.3; titulo: Correcao utilizada pelos Bancos; pagina_pdf: 329
- item: 16.4.6.4; titulo: Correcao dos honorarios; pagina_pdf: 330
- item: 16.4.7; titulo: Sobre a limitacao da multa a 100% do valor da obrigacao principal; pagina_pdf: 330
- item: 16.4.8; titulo: Pedindo retorno dos autos ao perito ou para as partes; pagina_pdf: 330
- item: 16.4.8.1; titulo: Para que ajuste o laudo da fase de conhecimento; pagina_pdf: 330
- item: 16.4.8.2; titulo: Para que complemente o laudo com INSS, IRRF, RESUMO e atualizacao; pagina_pdf: 330
- item: 16.4.8.3; titulo: Para que o perito ou as partes ajustem o laudo/calculo apresentado na fase de execucao a decisao de embargos a execucao ou agravo de peticao; pagina_pdf: 331
- item: 16.4.8.4; titulo: Para que o perito ou as partes retifiquem o laudo/calculo apresentado, adotando a TR como indice de correcao; pagina_pdf: 332
- item: 16.4.9; titulo: Massa Falida; pagina_pdf: 332
- item: 16.4.9.1; titulo: Limitacao dos juros ate a data da falencia; pagina_pdf: 332
- item: 16.4.9.2; titulo: Exclusao das multas convencionais e dos valores de INSS, imposto de renda e custas processuais; pagina_pdf: 332
- item: 16.4.10; titulo: Certidao de divida ativa; pagina_pdf: 333
- item: 16.4.11; titulo: Deducao na data do deposito ou levantamento; pagina_pdf: 333
- item: 16.4.11.1; titulo: Deducao na data do levantamento e nao na data do deposito; pagina_pdf: 333
- item: 16.4.11.2; titulo: Deducao na data do deposito; pagina_pdf: 333
- item: 16.4.12; titulo: Fazenda Publica; pagina_pdf: 334
- item: 16.4.12.1; titulo: Solicitando as partes para apresentarem os calculos de liquidacao nos termos do art. 104 do Provimento Geral Consolidado do TRT da 3a Regiao; pagina_pdf: 334
- item: 16.4.12.2; titulo: Explicando a forma de incidencia dos indices de correcao monetaria e juros aplicaveis as cadernetas de poupanca sobre os debitos da Fazenda Publica; pagina_pdf: 335


### C.3 Os 39 achados

| # | Tipo | `pagina_pdf` | Regra | Fundamento citado | Estr. |
|---|---|---|---|---|---|
| A01 | fundamento-de-regra-praticada… | 333 | A dedução do valor recebido pelo reclamante é lançada na data do efetivo LEVANTAMENTO (não na do depósito) quando o depósito foi… | Súmula nº 15 do TRT/3ª Região | True |
| A02 | momento | 333 | Enunciado operativo da Súmula 15/TRT-3: a responsabilidade do executado por correção monetária e juros não cessa com o depósito e… | Súmula nº 15/TRT-3ª Região | True |
| A03 | momento | 334 | Tese oposta (mesma súmula, condição invertida): se o depósito foi feito para PAGAMENTO (código 02 na guia) e não para garantia do… | Súmula 15 do TRT-3ª Região; código 02 aposto na guia de d… | True |
| A04 | ordem-de-operacoes | 330 | A multa diária é limitada ao valor da obrigação principal CORRIGIDO — o teto se mede depois da correção monetária, não sobre o no… | art. 412 do CC/2002 (art. 920 do CC/1916); OJ 54 da SDI-I… | True |
| A05 | fundamento-de-regra-praticada… | 328 | Ao reatualizar, parte-se do principal bruto SEM juros e recalculam-se os juros desde a inicial; usar valor líquido/saldo que já c… | anatocismo "vedada por lei" (sem indicação de dispositivo… | True |
| A06 | ordem-de-operacoes | 328 | Procedimento de amortização: decompor o saldo em principal e juros; a parcela de juros apurada até a amortização só recebe correç… | "vedada por Lei" (sem dispositivo) | True |
| A07 | criterio | 329 | FGTS é atualizado como débito trabalhista comum, na forma do art. 39 da Lei 8177/91. | art. 39 da Lei 8177/91; OJ nº 302/TST | False |
| A08 | base-de-calculo | 319 | Juros e multa previdenciários por recolhimento fora do prazo NÃO podem ser imputados ao reclamante; do crédito do reclamante dedu… | art. 30, I, a e b, da Lei 8212/91; art. 33, § 5º, da Lei… | True |
| A09 | fundamento-de-regra-praticada… | 320 | Reforço jurisprudencial da não-imputação: Tribunal Pleno do TST, 20/10/15, E-RR 1125-36.2010.5.06.0171. | TST, Tribunal Pleno, E-RR 1125-36.2010.5.06.0171 | False |
| A10 | base-de-calculo | 320 | Consequência de cálculo da não-imputação. | art. 33, § 5º, Lei 8212/91 | True |
| A11 | base-de-calculo | 322 | IRRF incide sobre o valor efetivamente disponibilizado/levantado, não sobre o total do crédito trabalhista. | Lei 8.541/92, art. 46; Decreto 3.000/99, art. 56; Lei 7.7… | True |
| A12 | ordem-de-operacoes | 323 | A reatualização obriga a retornar ao principal e refazer os descontos previdenciários e fiscais — a base de cálculo do IR é recom… | Lei 7713/88; art. 55, IX e XIV, Dec. 3000/99; IN/RFB 1500… | True |
| A13 | ordem-de-operacoes | 325 | Gross-up: não se apura INSS e IR sobre valor líquido; encontra-se o valor bruto correspondente ao líquido levantado e sobre ele s… | art. 718 e art. 725 do Dec. 3000/99; art. 64 da IN/RFB 15… | True |
| A14 | fundamento-de-regra-praticada… | 326 | Fonte dos critérios do gross-up praticado nos capítulos 10 e 11: IN/SRF 15/2001, com adaptação da própria SCJ para incluir a cont… | Instrução Normativa SRF nº 15/2001 | True |
| A15 | base-de-calculo | 327 | Se parte do IR já estava depositada à disposição do juízo para quitação, os juros e a multa tributários incidem apenas sobre a DI… | art. 28 da Lei 10.833/03; art. 70 da Lei 11.196/05 | True |
| A16 | ordem-de-operacoes | 329 | Juros decrescentes: na reatualização, o valor dos juros do cálculo original recebe SÓ correção monetária; o percentual de juros d… | (nenhum dispositivo invocado) | True |
| A17 | criterio | 329 | Três regimes distintos de correção: depósito judicial = poupança (TR + 0,5% a.m.); depósito recursal = FGTS (TR + 3% a.a.); crédi… | art. 39 da Lei 8.177/91 | True |
| A18 | criterio | 330 | Honorários periciais: correção pelo IPCA-E (não pelos índices dos débitos trabalhistas) e SEM juros de mora, por serem despesa pr… | art. 1º da Lei 6899/81; OJ 198 da SBDI-I/TST; Resolução 6… | True |
| A19 | criterio | 330 | Negativa de juros sobre honorários periciais. | art. 1º da Lei 6899/81; OJ 198 da SBDI-I/TST (contra art.… | True |
| A20 | momento | 329 | Juros só se limitam à data da falência se o ativo não bastar — condição aferível apenas pelo juízo falimentar; sem determinação n… | art. 124 da Lei 11.101/05 | True |
| A21 | base-de-calculo | 332 | Massa falida: as multas convencionais NÃO são excluídas; a Súmula 388/TST isenta a massa apenas do art. 467 e do art. 477, § 8º,… | Súmula 388/TST; art. 83 da Lei 11.101/05 | True |
| A22 | momento | 315 | Em mera extinção de relação jurídica sem indicação de período, INSS = 11% (reclamante) + 20% (reclamada) sobre o total do acordo,… | art. 103, § 3º, da IN RFB nº 971/09; art. 132, § 3º, da I… | True |
| A23 | ordem-de-operacoes | 315 | Reatualização do INSS já corrigido com Selic: basta aplicar a Selic acumulada entre o último cálculo e a data final sobre o valor… | (nenhum dispositivo invocado) | True |
| A24 | base-de-calculo | 318 | Contribuição de terceiros não é apurada: fora da competência da Justiça do Trabalho. | Súmula 24/TRT-3ª Região; art. 101, I, da IN/RFB 971/09; E… | False |
| A25 | base-de-calculo | 320 | Desoneração da folha (Lei 12.546/11) não exclui o SAT/RAT do art. 22, II, da Lei 8212/91 — o valor do seguro acidente continua ex… | Lei 12.546/11; art. 22, I e II, da Lei 8212/91; Súmula 45… | True |
| A26 | base-de-calculo | 325 | IR sobre o total dos rendimentos, sem tributação isolada do 13º; da base deduzem-se apenas parcelas indenizatórias e a contribuiç… | art. 56 do Dec. 3.000/99; art. 12-A da Lei 7713/88; IN/RF… | True |
| A27 | base-de-calculo | 325 | Duas variantes sobre IR sobre juros de mora: (i) contrato vigente ou rescisão por iniciativa do empregado -> matéria controversa,… | OJ 400 da SDI-I/TST; art. 62, §§ 3º e 5º, da IN/RFB 1500/… | True |
| A28 | criterio | 332 | Índice de correção dos débitos trabalhistas é a TR, não o IPCA-E, por força da liminar na Rcl 22.012 MC/RS; tabela única do CSJT. | Reclamação 22.012 MC/RS (Min. Dias Toffoli, STF); tabela… | True |
| A29 | ordem-de-operacoes | 335 | Fazenda Pública: correção pela TR e juros simples de 0,5% a.m. (ou menos), em DUAS etapas e uma só vez; aplicar os juros acumulad… | art. 1º-F da Lei 9494/97 (red. Lei 11960/09); Resolução C… | True |
| A30 | base-de-calculo | 314 | Reflexo de horas extras em férias + 1/3 calcula-se pela MÉDIA das horas extras do período aquisitivo multiplicada pelo valor de 1… | (nenhum dispositivo invocado) | True |
| A31 | criterio | 313 | Requisito formal de conferibilidade do cálculo: memória com valores mês a mês, atualização, juros e descontos previdenciários e f… | art. 1º, § 1º, do Provimento 04/00 do TRT-3ª Região | False |
| A32 | ordem-de-operacoes | 314 | INSS cota reclamante apura-se com as tabelas das ÉPOCAS PRÓPRIAS das parcelas, deduzidas as contribuições já recolhidas no curso… | art. 20 da Lei 8.212/91; art. 274 do Dec. 3048/99 | True |
| A33 | criterio | 318 | Empregado doméstico, cota empregador: 12% até set/15; 8,8% a partir de out/15 (8% patronal + 0,8% grau de risco). | Lei Complementar 150/15; art. 24, I e II, da Lei 8212/91… | False |
| A34 | criterio | 326 | IR não recolhido no prazo: multa de 0,33% ao dia limitada a 20% mais juros de 1% + SELIC. | art. 28 da Lei 10.833/03; art. 46 da Lei 8.541/92; art. 6… | True |
| A35 | base-de-calculo | 319 | Não incide INSS sobre vale-transporte/ajuda-alimentação deferidos como indenização substitutiva (matéria submetida ao juiz). | art. 28, I, da Lei 8212/91 | False |
| A36 | base-de-calculo | 327 | Multa do acordo por atraso é tributável, calculada PROPORCIONALMENTE às parcelas do acordo passíveis de IR; multa por litigância… | art. 55 do Dec. 3000/99; Solução de Consulta 193 SRRF08 d… | True |
| A37 | base-de-calculo | 324 | Indenização por danos morais recebida por pessoa física não é rendimento tributável. | Ato Declaratório nº 09 da PGFN, de 20/12/11 | False |
| A38 | criterio | 333 | Dívida ativa da União: a atualização é feita no sistema da PGFN, que só exibe o valor final; exige-se memória da União para evita… | (nenhum dispositivo invocado; remete ao sistema www.pgfn.… | True |
| A39 | criterio | 312 | Cálculos das partes com vícios absurdos ou de extensão/complexidade elevada: via pericial. | art. 1º, § 3º, do Provimento 03/91 do TRT-3ª Região | False |

### C.4 O cruzamento dos fundamentos — o entregável principal

| Fundamento | No cap. 16 | Capítulo técnico cita? | Busca |
|---|---|---|---|
| Súmula nº 15 do TRT/3ª Região | 16.4.11.1 (p.333, 2 ocorrências) e… | cap.10 NÃO; cap.7 SIM (1 vez, p.83, apenas em lista de sú… | regex 'S[uú]mula\s*n?[.ºo°]*\s*15\s*(do\|/)\s*(TRT\|Regional)' sobre texto normalizado: cap6(18-82)=0; cap7(8… |
| art. 412 do CC/2002 (art. 920 do CC/1916) | 16.4.7 (p.330, 1 ocorrência) | SIM - cap.6, p.77, 3 ocorrências | regex 'art(igo)?\.?\s*412': cap6=3 [p.77]; cap7=0; cap8=0; cap9=0; cap10=0; cap11=0; cap15=1 [p.309]; cap16=1… |
| OJ 54 da SDI-I/TST | 16.4.7 (p.330, 1 ocorrência) | SIM - cap.6, p.77, 1 ocorrência | regex 'OJ/SDI[-/]?I?/?TST\s*n?\.?[ºo°]?\s*54\|OJ/SDI/TST\s*n[ºo°]\s*54': cap6=1 [p.77]; cap7..cap15=0; cap16=… |
| anatocismo (vedação de juros sobre juros) aplicado à amorti… | 16.4.5.1 (p.328, 4 ocorrências) e 1… | cap.10 NÃO (0 ocorrências em 69 páginas); cap.7 SIM (2 oc… | regex 'anatocismo': cap6=0; cap7=2 [p.90]; cap8=0; cap9=0; cap10=0; cap11=0; cap13=0; cap14=0; cap15=0; cap16… |
| Súmula 121 do STF (vedação de anatocismo) | não aparece | cap6..cap17 = 0; única ocorrência no manual é a p.16 | regex 'S[uú]mula\s*n?[.ºo°]*\s*121' em todas as 471 páginas = 1 ocorrência, p.16 |
| OJ nº 302/TST (índice de correção do FGTS) | 16.4.6.2 (p.329, 1 ocorrência) | SIM - cap.6 p.79 ('Entendimento consubstanciado na OJ/SDI… | regex '302': cap6=4 [pp.79,80]; cap7=2 [pp.83,86]; cap8=1 [p.103]; cap9=3; cap10=3; cap11=2; cap16=1 [p.329];… |
| Instrução Normativa SRF nº 15/2001 (critérios do gross-up b… | 16.4.4.10 (p.326, 1 ocorrência) | NÃO - nenhum dos capítulos técnicos | literal '15/2001' em todas as 471 páginas = 1 ocorrência, p.326. Em contrapartida, 'bruto em rela[çc][ãa]o ao… |
| Súmula 454/TST (SAT/RAT não abrangido pela desoneração) | 16.4.3.19 (pp.320, 321, 322 - 3 oco… | NÃO | regex 'S[uú]mula\s*n?[.ºo°]*\s*454' em todas as 471 páginas = 3 ocorrências, todas no cap.16 (pp.320,321,322)… |
| Súmula 388/TST (massa falida isenta só do art. 467 e do art… | 16.4.9.2 (p.332, 2 ocorrências) | NÃO | regex 'S[uú]mula\s*n?[.ºo°]*\s*388\|SUM-?388\|Nº 388' em todas as 471 páginas = 2 ocorrências, ambas na p.332… |
| art. 83 da Lei 11.101/05 (classificação de multas contratua… | 16.4.9.2 (p.332, 1 ocorrência) | NÃO (cap.7 cita apenas o art. 124) | regex 'art(igo)?\.?\s*83 da Lei' em todas as 471 páginas = 1 ocorrência, p.332. Regex 'art(igo)?\.?\s*124': c… |
| art. 124 da Lei 11.101/05 (limitação de juros na falência) | 16.4.5.2 (p.329) e 16.4.9.1 (p.332) | SIM - 4 ocorrências | regex 'art(igo)?\.?\s*124': cap7=4 [pp.89,90]; cap16=2 [pp.329,332] |
| Resolução 66/10 do CSJT (IPCA-E para honorários periciais)… | 16.4.6.4 (p.330, Res.66=2, OJ198=3) | SIM - Res.66/10: cap8=2 [p.102]; OJ 198: cap8=5 [pp.102,1… | regex 'Resolu[cç][aã]o 66' e 'OJ\s*n?[.ºo°]*\s*198\|198 da SBDI\|198/TST' por faixa |
| art. 407 do Código Civil (juros sobre honorários periciais… | 16.4.6.4 (p.330, 2 ocorrências) | SIM - cap8=3 [p.103] | regex 'art(igo)?\.?\s*407': cap8=3 [p.103]; cap16=2 [p.330]; demais faixas = 0 |
| Súmula 24/TRT-3ª Região (contribuição de terceiros) | 16.4.3.12 (p.318, 1 ocorrência) | SIM - cap.9, p.108 (conferido por inspeção; o regex estri… | regex 'S[uú]mula\s*24/TRT\|S[uú]mula\s*n?[.ºo°]*\s*24\s*do\s*TRT': cap16=1 [p.318]; demais=0. Busca ampliada… |
| Súmula 45/TRT-3ª Região (fato gerador da contribuição previ… | 16.4.3.3, 16.4.3.13, 16.4.3.19 (pp.… | SIM - cap9=8 [pp.117,118,119,128,129,174]; cap11=7; cap15… | regex 'S[uú]mula\s*n?[.ºo°]*\s*45' por faixa; cap10(209-277)=0 |
| TST Pleno E-RR 1125-36.2010.5.06.0171 (não imputação de jur… | 16.4.3.18 (p.320, 1 ocorrência) | SIM - cap9=2 [pp.118,128] | regex '1125-36': cap9=2 [pp.118,128]; cap16=1 [p.320]; demais faixas=0 |
| art. 30, I, a e b, e art. 33, § 5º, da Lei 8212/91 (respons… | 16.4.3.17 e 16.4.3.18 (pp.319-320) | SIM - o art. 33, § 5º é invocado no cap.15, p.307, com a… | inspeção da p.307: 'Os acréscimos legais são de responsabilidade exclusiva do reclamado, conforme art. 33, §… |
| Ato Declaratório nº 09 da PGFN de 20/12/11 (danos morais nã… | 16.4.4.5 (p.324, 1 ocorrência) | SIM - cap9=2 [p.184] | regex 'Ato Declarat[oó]rio n[ºo°]*\s*0?9': cap9=2 [p.184]; cap16=1 [p.324]; demais=0 |
| Reclamação 22.012 MC/RS (STF, Min. Dias Toffoli - TR e não… | 16.4.8.4 (p.332, 1 ocorrência) | SIM - cap7=1 [p.84] ('Reclamação nº 22012 MC/RS') | regex '22\.?012': cap7=1 [p.84]; cap16=1 [p.332]; demais=0 |
| art. 103, § 3º, da IN RFB 971/09 e art. 132, § 3º, da IN MP… | 16.4.3.3 (p.315, 1 ocorrência cada) | SIM - 'art. 103' cap9=6 [pp.157,173,174,175,176]; '132, §… | regex 'art(igo)?\.?\s*103' e '132, § 3' por faixa |
| art. 102, § 6º, II, da IN RFB 971/09 (extinta relação entre… | 16.4.3.10 (p.318, 1 ocorrência) | SIM - cap9=4 [pp.154,157,173] | regex 'art(igo)?\.?\s*102' por faixa |
| Lei 8.541/92, art. 46 e Dec. 3.000/99, art. 56 (IR sobre o… | 16.4.4.1 (p.322) e 16.4.4.11 (p.326) | SIM - '8541' cap8=1 [p.104], cap9=6 [pp.107,180,185,186];… | regex '8\.?541' e 'art\.?\s*56\b' por faixa; cap10=0 para ambos |
| art. 725 do Dec. 3000/99 (rendimento líquido / reajustament… | 16.4.4.10 (p.325, 1 ocorrência) | SIM - cap10=2 [p.224]; cap9=4 [pp.126,127,128]; cap8=2 [p… | regex '\b725\b' por faixa |
| Solução de Consulta Interna Cosit nº 13/RFB de 30/06/2016 (… | 16.4.4.8 (pp.324-325, 3 ocorrências… | SIM - cap9=7 | regex 'Cosit': cap9=7 [pp.176,181,185,199]; cap16=3 [pp.324,325]; cap17+=2 |
| OJ 400 da SDI-I/TST (IR não incide sobre juros de mora) | 16.4.4.8 (p.325, 3 ocorrências) | SIM - cap9=10; cap10=6; cap11=4 | regex 'OJ\s*n?[.ºo°]*\s*400\|400/TST\|400 da SDI' por faixa |
| Solução de Consulta 193 SRRF08 de 24/09/13 (IR sobre multa) | 16.4.4.13 (p.327, 1 ocorrência) | SIM - cap6=1 [p.77] | regex '193 SRRF08': cap6=1 [p.77]; cap16=1 [p.327]; demais=0 |
| Lei Complementar 150/15 e art. 24 da Lei 8212/91 (doméstico… | 16.4.3.11 (p.318, 1 ocorrência) | SIM - cap9=2 [pp.115,116]; cap6=3 [pp.19,74] | regex 'Lei Complementar\s*n?[.ºo°]*\s*150' por faixa |
| Lei Complementar 123/06, art. 13, VI (SIMPLES NACIONAL) | 16.4.3.6 e nota de rodapé 15 (p.317) | SIM | regex 'Lei Complementar\s*n?[º°.o]*\s*123\|LC\s*123': cap9 [pp.114,173]; cap16 [p.317] |
| Resolução CNJ 115/10, art. 36 e § 1º | 16.4.12.2 (p.335, 3 ocorrências) | SIM - cap7=2 [p.90]; cap14=4 [pp.304,305,306] | regex '115/10\|115/2010' por faixa |
| Ordem de Serviço/VPADM TRT-3ª Região 01/2011 (veda anatocis… | 16.4.12.2 (p.335, 2 ocorrências) | SIM - cap7=1 [p.90]; cap8=2 [p.105]; cap14=1 [p.304]; cap… | regex 'VPADM' por faixa |
| art. 1º-F da Lei 9494/97 | 16.4.12.2 (pp.335-336, 7 ocorrência… | SIM - cap7=24 | regex '1[ºo°]?\s*-\s*F\|1[ºo°]\s*F' por faixa; cap10=0 |
| art. 39 da Lei 8.177/91 | 16.4.6.1, 16.4.6.2, 16.4.6.3 (p.329… | SIM - cap6=8; cap7=9; cap8=1; cap11=1 | regex 'art(igo)?\.?\s*39 da Lei 8\.?177\|art\. 39 da lei 8177' por faixa; cap9=0 e cap10=0 |
| Lei 6.899/81, art. 1º (correção de débitos judiciais) | 16.4.6.4 (p.330, 4 ocorrências) | SIM - cap8=10; cap7=1 [p.83] | regex '6\.?899' por faixa |
| Provimento 03/91 do TRT-3ª Região (via pericial), art. 1º,… | 16.3.5 (p.312), 16.4.2 (pp.313,314)… | NÃO em nenhum capítulo técnico | regex 'Prov\.?\s*0?3/91\|Provimento\s*0?3/91': cap6=0; cap7=0; cap8=0; cap9=0; cap10=0; cap11=0; cap13=0; cap… |
| Provimento 04/00 do TRT-3ª Região, art. 1º, § 1º (memória d… | 16.4.2 (p.313) e 16.4.8.2 (p.331) | SIM - cap9=5; cap10=9; cap11=1; cap13=2 | regex 'Prov\.?\s*0?4/0?0' por faixa |
| art. 104, § 5º, do Provimento Geral Consolidado do TRT-3ª R… | 16.4.12.1 (pp.334-335, 4 ocorrência… | NÃO em nenhum capítulo técnico (cap.14 p.304 cita 'art. 1… | regex 'art(igo)?\.?\s*104': cap6=0; cap7=0; cap8=0; cap9=0; cap10=0; cap11=0; cap14=1 [p.304]; cap16=4 [pp.33… |

### C.5 Os três achados conhecidos, conferidos

**achado 1 sumula15**

- **premissa do enunciado:** 16.4.11 em pagina_pdf 335
- **verificacao:** PÁGINA ERRADA. O item 16.4.11 abre na pagina_pdf 333 e termina na 334. A pagina_pdf 335 contém 16.4.12.1 (final) e 16.4.12.2 (Fazenda Pública) e não menciona a Súmula 15.
- **paginas reais:** 333; 334
- **busca que sustenta:** regex 'S[uú]mula\s*n?[.ºo°]*\s*15\s*(do\|/)\s*(TRT\|Regional)' = 2 ocorrências na p.333 e 2 na p.334; 0 na p.335
- **duas teses reconhecidas:** True
- **tese A:** item: 16.4.11.1 Dedução na data do levantamento e não na data do depósito; pagina_pdf: 333; citacao_literal_1: Vem esta SCJ, respeitosamente, dizer que a dedução do valor recebido pelo  reclamante foi efetuada  na data do efetivo levantamento, na forma do disposto na Súmula nº 15  do TRT/3ª Região, considerando que  o depósito de fl. 130 foi feito à disposição do juízo e  precedeu aos embargos e agravo de petição,  tratando-se, portanto, de depósito em garantia da  execução.; citacao_literal_2: A dedução do valor recebido pelo exequente foi  efetuada na data do efetivo levantamento, visto que o depósito de fl. 562 v. foi realizado à  disposição do juízo, ou seja, apenas para a garantia da execução, sendo que de acordo com a  Súmula nº 15/TRT-3ª Regi…
- **tese B:** item: 16.4.11.2 Dedução na data do depósito; pagina_pdf: 333 (abertura) e 334 (texto); citacao_literal_1: não assiste razão ao reclamante, visto que a; citacao_literal_1_continuacao_p334: reclamada depositou o total da execução de forma atualizada até a data do efetivo depósito  (vide cálculo fl. e valores de guia fl.), objetivando o efetivo pagamento e não apenas a garantia  do juízo para interposição de embargos, conforme código 02 aposto nas guias de fl.).; citacao_literal_2: De acordo com o entendimento exposto na Súmula 15 do TRT-3ª  Região, s.m.j., a responsabilidade do executado pela correção monetária e juros de mora  apenas não cessa, quando o depósito é realizado para garantia da execução.; fundamento_citado: Súmula 15 do TRT-3ª Região (le…
- **condicao que separa:** A FINALIDADE DO DEPÓSITO, aferida por dois indícios documentais nomeados pelo próprio manual: (i) o código aposto na guia de depósito - 'código 02' indica depósito para pagamento; (ii) a cronologia processual - depósito que 'precedeu aos embargos e agravo de petição' indica garantia da execução. Se garantia -> dedução na data do levantamento. Se pagamento -> dedução na data do depósito e 'não há diferença a ser apurada'. Adicionalmente, na tese B o manual exige que o depósito tenha sido do TOTAL da execução e atualizado até a data do depósito.
- **terceira regra divergente no manual:** pagina_pdf: 306; capitulo: 14 - PRECATÓRIOS; citacao_literal: c) Amortizar com observância  da data do pagamento e não da data do levantamento,  salvo determinação do juízo da origem;; observacao: Para precatórios/Fazenda Pública o manual inverte a regra por default, sem citar a Súmula 15. Não harmonizado aqui: são três enunciados distintos no mesmo manual.

**achado 2 multa principal corrigido**

- **premissa do enunciado:** 16.4.7 em pagina_pdf 330, teto no 'principal corrigido', art. 412 do CC e OJ 54 da SDI
- **verificacao:** PÁGINA CONFIRMADA (330). Conteúdo confirmado.
- **citacao literal:** Vem esta SCJ, muito respeitosamente, dizer a V.Exa. que a multa diária fixada  na........ (o mais comum é na cláusula tal da CCT ou na ata do acordo de fl.) foi limitada ao valor  da obrigação principal, ou seja, ao ..........(o mais comum é  ao  total das parcelas rescisórias ou  total do acordo),  tendo em vista o disposto no art. 412 do CC (art.920, CC/1916) e OJ/SDI/TST  nº 54 da SDI (“Multa estipulada em cláusula penal, ainda que diária, não poderá se superior ao  principal corrigido - Aplicação do art. 920 do Código Civil”).
- **pagina pdf:** 330
- **ordem de operacoes:** O teto mede-se DEPOIS da correção monetária: o limite é o principal corrigido, não o nominal.
- **ha exemplo numerico no 16 4 7:** False
- **onde esta o exemplo numerico:** pagina_pdf: 77; item: 6.13.10 Multa diária; citacao_literal: A multa diária é atualizada um dia após alcançar o seu limite máximo. A título de exemplo, multa diária fixada à razão de R$  100,00 por dia, limitada a R$ 3.000,00, apenas sofrerá correção monetária a partir do 31º dia, visto que o limite máximo de R$ 3.000,00 será alcançado apenas no 30º dia, conforme exemplificação abaixo.; observacao: Esse exemplo demonstra o MOMENTO em que a multa passa a ser corrigida após atingir o teto; não demonstra a medição do teto contra o principal corrigido.
- **correcao a premissa:** A premissa de que o capítulo técnico não enuncia a regra NÃO se confirma. O item 6.13.10 (p.77) enuncia a mesma regra, com o texto integral e correto da OJ 54, e acrescenta duas regras que o 16.4.7 não tem: (a) a multa só é corrigida a partir do dia seguinte ao do atingimento do teto; (b) 'A incidência de juros sobre a multa é controversa. Quando aplicáveis, os juros também irão incidir a partir da mesma data do início da correção monetária.'

**achado 3 anatocismo descarregar**

- **premissa do enunciado:** p.328 é o único lugar do manual que conecta 'descarregar' ao anatocismo; 'anatocismo' tem zero ocorrências no cap.10
- **verificacao:** CONFIRMADO em parte. Confirmado: zero ocorrências de 'anatocismo' e de 'juros sobre juros' no cap.10 (209-277, 69 páginas). Confirmado: 'descarreg' tem 1 única ocorrência no manual inteiro, p.237 (item 10.3.1). NÃO confirmado que seja o único lugar com 'anatocismo': o termo aparece também na p.16 (cap.5, com fundamento na Súmula 121 do STF), na p.90 (cap.7, Fazenda Pública) e na p.335 (16.4.12.2). Total: 11 ocorrências em 4 páginas.
- **contexto completo p328:** Esclarece, ainda, que após a dedução do valor quitado em__/___/___, os juros  foram expurgados do saldo apurado, separando a parcela correspondente ao principal na  diferença encontrada em ___/___/___e evitando assim a cumulação.; Em atenção ao r. despacho de fl.___,  esta SCJ, respeitosamente, informa a  V.Exa. que, s.m.j., não assiste razão ao reclamante, visto que esta SCJ tomou como base o  valor  do principal bruto devido ao reclamante sem juros de mora, apurado à fl. 133, atualizando  o mesmo até  (informar a data final de atualização)  e recalculando os juros de mora desde a  inicial, não incidindo juros sobre juros (anatocismo).; Esclarece, ainda, que o reclamante considera como valor base para atualização  o valor líquido do cálculo de fl.…
- **a minuta descreve a operacao do 10 3 1:** True
- **correspondencia com 10 3 1:** pagina_pdf_10_3_1: 237; citacao_literal_10_3_1: Quando há amortização de valor pago, não se pode partir de determinado  crédito de saldo remanescente da execução, que já contenha juros, para sobre ele aplicar juros  novamente, sendo necessário “descarregar” o saldo dos juros (excluir os juros do saldo, para  aliá-los sem acumulação).; analise: A primeira frase de 10.3.1 (p.237) e a primeira frase do quinto trecho da p.328 são a MESMA frase, com uma diferença: em 10.3.1 a operação é nomeada 'descarregar' e não é qualificada juridicamente; na p.328 ela é qualificada como 'juros sobre juros (anatocismo), vedada por Lei'. 10.3.1 também descreve os dois critérios alternativos (A/B/C ou 1/2/3) e a regra de obrigatoriedade do segundo quando há juros vincen…


### C.6 Itens de cálculo

- item: 16.4.3; assunto: INSS; paginas_pdf: [314, 315, 316, 317, 318, 319, 320, 321, 322]; subitens: 19; regras_registradas: ['A22', 'A23', 'A08', 'A09', 'A10', 'A24', 'A25', 'A32', 'A33', 'A35']; nota: 16.4.3.3 traz quatro variantes sobre o fato gerador (Súmula 45/TRT-3 x tese da União x decisão do processo) e a metodologia de reatualização da Selic sem sobreposição. 16.4.3.5 a 16.4.3.10 fixam alíquotas por situação (extinta relação jurídica, SIMPLES, entidade beneficente, pessoas físicas). 16.4.3.19 trata da desoneração da folha em três variantes conforme o período de apuração.
- item: 16.4.4; assunto: IRRF; paginas_pdf: [322, 323, 324, 325, 326, 327]; subitens: 14; regras_registradas: ['A11', 'A12', 'A13', 'A14', 'A15', 'A26', 'A27', 'A34', 'A36', 'A37']; nota: Contém a regra de base (IR sobre o disponibilizado), o gross-up com fonte IN 15/2001, a proibição de tributação isolada do 13º, o tratamento dos juros de mora (duas variantes) e os acréscimos moratórios federais.
- item: 16.4.5; assunto: Juros de mora; paginas_pdf: [327, 328, 329]; subitens: 4; regras_registradas: ['A05', 'A06', 'A16', 'A20']; nota: 16.4.5.1 é o núcleo do anatocismo/amortização. 16.4.5.4 (p.329) repete a metodologia de 10.3.1 critério 2 para a atualização do valor dos juros.
- item: 16.4.6; assunto: Critérios de atualização monetária; paginas_pdf: [329, 330]; subitens: 4; regras_registradas: ['A07', 'A17', 'A18', 'A19']; nota: 16.4.6.2 confirmado: FGTS pelo art. 39 da Lei 8177/91 com base na OJ 302/TST. 16.4.6.3 é a tabela de três regimes de correção (depósito judicial, depósito recursal, crédito trabalhista).
- item: 16.4.9; assunto: Massa falida; paginas_pdf: [332]; subitens: 2; regras_registradas: ['A20', 'A21']; nota: 16.4.9.1 é cópia literal do 16.4.5.2 (p.328-329). 16.4.9.2 traz Súmula 388/TST e art. 83 da Lei 11.101/05, ambos inexistentes fora do cap.16.
- item: 16.4.10; assunto: Certidão de dívida ativa; paginas_pdf: [333]; subitens: 0; regras_registradas: ['A38']; nota: Três minutas, todas sobre o mesmo problema: o sistema da PGFN só devolve o valor final, sem índices nem dedução dos DARF, o que impede a conferência e cria risco de compensação em duplicidade. É limitação operacional, não regra de cálculo, mas condiciona a amortização.
- item: 16.4.12; assunto: Fazenda Pública; paginas_pdf: [334, 335, 336]; subitens: 2; regras_registradas: ['A29']; nota: 16.4.12.2 reproduz quase literalmente o texto da p.90 (cap.7) sobre as duas etapas TR + juros simples de 0,5% a.m. e a vedação do anatocismo.
- item: imputação de juros e multa previdenciários; assunto: verbete 'imputa'; paginas_pdf: [319, 320]; ocorrencias_no_manual: 3; detalhe: 'imputa' (raiz) ocorre 3 vezes: p.319 x2 (16.4.3.17 e título de 16.4.3.18) e p.320 x1 (corpo de 16.4.3.18). Formas flexionadas: 'imputados' p.319 e p.320; 'imputação' p.319 (no título do item 16.4.3.18).; regra: Os juros e a multa da legislação previdenciária por recolhimento fora do prazo NÃO se imputam ao reclamante; deduz-se do seu crédito apenas a contribuição previdenciária atualizada. Ressalva expressa: 'salvo se houver decisão em contrário'. Em 16.4.3.17 a SCJ ainda apre…

### C.7 Defeitos

12 catalogados. Nenhum corrigido.

| # | `pagina_pdf` | Defeito | Impresso | Correto |
|---|---|---|---|---|
|  | 327 |  | 16.4.4.12 Incidência de imposto de renda sobre a multa do acordo | 16.4.4.13 (e, em cadeia, 16.4.4.13 -> 16.4.4.14) |
|  | 330 |  | “Multa estipulada em cláusula penal, ainda que diária, não poderá se superior ao principal corrigido - Aplicação do art. 920 do Código Civil” | o próprio manual transcreve corretamente na p.77: “O valor da multa estipulada em cláusula penal, ainda que diária, não poderá ser superior à obrigação principal corrigida, em virtude da aplicação do artigo 412 do Código Civil de 2002 (art. 920 do Código Civil de 1916)” |
|  | 330 |  | OJ/SDI/TST nº 54 da SDI | OJ/SDI-I/TST nº 54 |
|  | 327 |  | 16.4.4.13 Incidência de imposto de renda sobre a multa de litigância de má fé, cujo corpo começa por '- Incidência de imposto de renda sobre a multa pelo atraso ou inadimplemento da parcela do acordo-' | o marcador do corpo deveria dizer 'multa de litigância de má fé' |
|  | 312 |  | (a) falta a compensação das horas extras pagas e descontos legais; (c)  os juros estão calculados a maior; (d) as férias indenizadas refletiram indevidamente no FGTS. | (a) ... (b) ... (c) ... |
|  | 332 |  | a) Exclusão das multas convencionais ... c) Separação dos valores devidos a título de INSS, imposto de renda e custas processuais | a) ... b) ... c) ... |
|  | 320 |  | Esclarece, ainda, que o cálculo deverá ser efetuado mês a mês, | desconhecido - a minuta 16.4.3.18 termina em vírgula, sem completar o período |
|  | 317 |  | Lei 9.317/9615 | Lei 9.317/96 (nota de rodapé 15) |
|  | 237 |  | excluir os juros do saldo, para aliá-los sem acumulação | provável 'aplicá-los' ou 'aliá-los' por 'agregá-los' - o original não permite reconstrução segura |
|  | 329 |  | os juros devem ser limitados até a data falência apenas, se o ativo não for suficiente | 'até a data da falência' |
|  | 330 |  | não determinam  a incidência dos  de juros sobre os  honorários periciais | 'a incidência de juros' |
|  | 249 |  | 10.2 | o item 10.2 já existia na p.223; a p.249 reabre '10.2' |

### C.8 Pendências

- Não foi verificado o SUMÁRIO impresso do manual (páginas de rosto) contra a numeração do corpo; a 'estrutura_real' aqui registrada foi extraída exclusivamente do corpo das pp.310-336.
- O início exato do capítulo 9 não foi confirmado por cabeçalho em caixa-alta (o regex de detecção de capítulos capturou 1-8 e 10-16, mas não o 9). Adotou-se a faixa 107-208 dada no enunciado; a p.107 contém texto de descontos, compatível.
- 16.4.1.6 ('Diretriz do Juiz sobre diversos aspectos', p.313) está incompleto no original: traz apenas '(a) relatar a questão controvertida'. Não há regra de cálculo a extrair.
- Não foi feita conferência de valores numéricos das tabelas do cap.16 (só há um exemplo numérico, em 16.4.8.4, p.332, que foi registrado em A28 mas não recalculado - não há dados para recomputar a TR acumulada de 01/09/08 a 30/09/15 sem a tabela do CSJT).
- A frase truncada da p.320 (16.4.3.18) impede saber se havia regra adicional sobre a apuração mês a mês do INSS sem acréscimos.

### C.9 Buscas que sustentam as negativas

| Termo | Escopo | Ocorrências | Conclusão |
|---|---|---|---|
| `anatocismo` |  | 0 |  |
| `juros sobre juros` |  | 0 |  |
| `S[uú]mula ... 15 ... (do\|/) (TRT\|Region…` |  | 0 |  |
| `S[uú]mula ... 15 ... (do\|/) (TRT\|Region…` |  | 0 |  |
| `S[uú]mula ... 15 ... (do\|/) (TRT\|Region…` |  | 0 |  |
| `S[uú]mula ... 15 ... (do\|/) (TRT\|Region…` |  | 0 |  |
| `garantia da execu` |  | 0 |  |
| `data do dep[óo]sito` |  | 0 |  |
| `15/2001` |  | 0 |  |
| `S[uú]mula ... 454` |  | 0 |  |
| `S[uú]mula ... 388` |  | 0 |  |
| `art. 83 da Lei` |  | 0 |  |
| `Prov. 03/91 \| Provimento 03/91` |  | 0 |  |
| `art. 104` |  | 0 |  |
| `S[uú]mula ... 121` |  | 0 |  |
| `S[uú]mula ... 45` |  | 0 |  |
| `art. 39 da Lei 8177` |  | 0 |  |
| `art. 1º-F` |  | 0 |  |
| `art. 412` |  | 0 |  |
| `OJ 54 (padrão OJ/SDI.../TST nº 54)` |  | 0 |  |
| `descarreg` |  | 0 |  |
| `imputa (raiz)` |  | 0 |  |
| `S[uú]mula 200` |  | 0 |  |
| `Sumula 362 (prescrição do FGTS)` |  | 0 |  |

