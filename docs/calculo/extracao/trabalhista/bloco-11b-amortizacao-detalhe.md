# Bloco 11B — detalhe

Companheiro de `bloco-11b-amortizacao.md`. Material bruto do **segmento C do capítulo 10**
— item 10.3, amortização de valor pago sob o regime do art. 12-A.

Gerado por script a partir de `cap10_3c.json`. **Offset de paginação zero.**

---

### 1. Fronteiras conferidas

- **offset paginacao:** 0
- **metodo:** PyMuPDF doc[pagina-1].get_text(), utf-8
- **inicio:** pagina_pdf: 237; offset: 681; texto: 10.3 Atualização com amortização de valor  pago; confirmado: True
- **fim:** pagina_pdf: 266; offset: 2141; texto_anterior: TOTAL DO CÁLCULO EM 31/05/16  43.077,24; confirmado: True
- **itens confirmados:** 10.3; 10.3.1; 10.3.2; 10.3.2.1
- **exemplos confirmados:** {'rotulo': 'EXEMPLO', 'numerado': False, 'pagina_inicio': 238, 'pagina_fim': 239, 'item': '10.3.1'}; {'rotulo': 'Exemplo 1', 'pagina_inicio': 241, 'pagina_fim': 248, 'item': '10.3.2.1'}; {'rotulo': 'Exemplo 2', 'pagina_inicio': 248, 'pagina_fim': 255, 'item': '10.3.2.1'}; {'rotulo': 'Exemplo 3', 'pagina_inicio': 255, 'pagina_fim': 262, 'item': '10.3.2.1'}; {'rotulo': 'Exemplo 4', 'pagina_inicio': 262, 'pagina_fim': 266, 'item': '10.3.2.1'}
- **lista do enunciado confere:** True
- **corte parte hipotese:** constatado: True; explicacao: O corte em p.266/off.2141 NAO fecha o item 10.3.2.1. Varredura de headings de p.262 a p.300 (regex '^(1[01]\.\d[\.\d]*)') nao encontra NENHUM heading numerado apos '10.3.2.1' (p.239). Exemplo 5 (p.266) e Exemplo 6 (p.271) continuam pendurados no mesmo item 10.3.2.1, sem subtitulo proprio. Portanto a hipotese 10.3.2.1 so termina em ~p.277 (antes do bloco de 'Exemplo 1 - Parcelas rescisorias' em p.278, que ja e outro capitulo).…

## 2. A moldura — o roteiro em letras

### Item 10.3.1

- **letras:** A; B; C; D; E; F.1; F.2; G; H; J
- **letra I ausente:** True
- **confirmacao enunciado:** CONFIRMADO - o roteiro salta de H para J (p.238: 'J - somar o resultado  encontrado na letra “G” e  “ H “')
- **ressalva:** O proprio EXEMPLO de 10.3.1 rotula a linha final como 'Demonstração item " I "' (p.239), usando uma letra que o roteiro nao tem.
- **letra C alternativa:** presente: True; pagina_pdf: 237; texto: 1 - atualizar o total dos juros do último cálculo com o mesmo índice de correção utilizado para corrigir o principal até a data da amortização; 2 - aplicar os juros contados da data da atualização do último cálculo até a data da dedução apenas sobre o principal corrigido apurado na letra “B”; 3 - O valor encontrado no item 02 deverá ser somado ao valor apurado no item 01; obs: 'Quando o cálculo não envolver juros vincendos, o calculista poderá optar por qualquer um dos dois…

### Item 10.3.2.1

- **letras:** A; B; C; D; E; E.1; F; G.1; G.2; H; I; J; K; L; M; N; O; O(dup)
- **defeito:** p.241 traz DUAS letras 'O' consecutivas ('O - Os valores de INSS cota reclamante e reclamada...' e 'O - Apresentar o resumo na forma do art. 106...'). Nao ha letra P no roteiro, mas os Exemplos 1 e 2 rotulam o resumo como 'P'.
- **deslocamento:** Em 10.3.2.1 as letras deslocam-se em relacao a 10.3.1: E/E.1 = INSS+IR proporcionais, F = deduzir valor pago, G.1/G.2 = proporcao, H = atualizar principal, I = atualizar juros, J = somar. Ou seja, o F/G/H/J de 10.3.1 vira G/H/I/J em 10.3.2.1.
- **erro de referencia cruzada:** A letra I de 10.3.2.1 (p.240) manda 'incidir juros do período restante ... sobre o valor encontrado através da letra “H”' (correto), mas a alternativa logo abaixo diz 'aplicar os juros integrais ... sobre o crédito atualizado apurado na letra “G”' - deveria ser letra H. O texto de 10.3.1 tem o mesmo par (G correto / G na alternativa).

## 3. Cada exemplo contra a moldura

### EXEMPLO (10.3.1) (`pagina_pdf` 238; 239)

- **Descontos:** False
- **Alternativa da letra H:** alternativa 1 (atualiza os juros de F.2 pelo indice AM e soma juros do periodo restante sobre G)
- **Faz além da moldura:**
  - Fixa a alternativa 1 da letra H de forma explicita na propria formula da linha i, sem dizer que esta escolhendo: 'vr. juros contidos na diferença atualizado com AM até 3/05/16 (2.310,08 x 1,00172879) acrescido do vr. juros apurado sobre o principal (letra " h ") entre 27/04/16 a 31/05/16 (12.396,84 x 1,13333%)' (p.238).
  - Aplica a letra C sobre o PRINCIPAL JA CORRIGIDO ate a data da amortizacao (17.270,16 x 18,666667%), e nao sobre o valor da data do calculo anterior. A moldura nao diz sobre qual base incidem os juros da letra C.
  - Introduz percentual de juros 'ao dia' (0,33% ao dia) para fracao de mes: 'Juros 07/10/14 a 26/04/16 (1% ao mês ou 0,33% ao dia no período de 18 meses e 20 dias) 18,666667%' - a moldura nao prevê pro rata die.
  - Usa a letra 'i' do demonstrativo e a letra 'I' de referencia, que nao existem na moldura.
  - Nao ha nenhuma linha correspondente ao criterio alternativo 1/2/3 da letra C, embora o exemplo nao tenha juros vincendos (caso em que a moldura permite os dois).
- **Moldura não executada:**
  - criterio alternativo 1/2/3 da letra C
  - alternativa 2 da letra H (juros integrais sobre G)
- **Mapa linha → letra:** a 17.270,16: A+B (rotulado 'Demonstração itens " A “  e  “ B "'); b 3.223,76: C; c 20.493,92: D; d (5.808,39): E; e 14.685,53: E; f 12.375,45: F.1; g 2.310,08: F.2; h 12.396,84: G; i 2.454,58: H (alternativa 1); j 14.851,42: J - mas rotulado 'Demonstração item " I "'

### Exemplo 1 (`pagina_pdf` 241; 248)

- **Descontos:** True
- **Alternativa da letra H:** alternativa 1 da letra I (Vr. Juros atualiz. + Juros s/ o principal). NAO usa juros integrais.
- **Faz além da moldura:**
  - Inverte a letra E: a moldura manda 'deduzir os valores recolhidos a titulo de INSS e IR' (ou E.1, proceder aos descontos). O exemplo transforma E em 'Atualizar os valores de INSS cota reclamante e reclamada ate a data do levantamento' e executa E.1 sem nunca testar a hipotese E.
  - Cria toda a maquinaria de GROSS-UP nao prevista na moldura: a formula VR. BRUTO LEVANTADO = [TL - (PD x NMP)] / {...} (p.244) para reconstruir o bruto a partir do liquido levantado. A moldura assume que o 'valor pago' ja e conhecido em termos brutos.
  - Cria a nocao de NMP (numero de meses proporcional ao valor levantado) por regra de tres sobre o LIQUIDO, com nota de rodape '( * ) Observada a regra de arredondamento.' (p.243) - a regra de arredondamento nunca e declarada.
  - Cria um passo de VERIFICACAO (p.244-245: A bruto - B INSS - C IR = D liquido) que nao existe na moldura.
  - Atualiza o INSS cota reclamada (que nao e credito do reclamante) pelo mesmo indice do principal, e deduz o INSS recda proporcional do total bruto do reclamante na tabela da letra F (p.245, linha 'INSS cota recda proporcional ao valor pago 4.823,39') - mas NAO o subtrai no saldo. A linha aparece sem sinal e sem efeito.
  - Aplica 90,91% (percentual arredondado) na base de IR do levantamento e o percentual PLENO 0,90905739... na base de IR do saldo (ver aritmetica). A moldura fala de um unico 'indice das parcelas passiveis de IR'.
- **Moldura não executada:**
  - letra E na forma principal (deduzir recolhimentos ja feitos)
  - criterio alternativo 1/2/3 da letra C
  - alternativa 2 da letra I
- **Mapa linha → letra:** 46.183,06: A; 46.893,92: B; 17.272,59/17.272,58: C; 64.166,51/64.166,50: D; 3.410,34 e 8.676,53: E.1 passo 1; 90,91%: E.1 passo 2; 20 meses: E.1 passo 3; 58.389,34: E.1 passo 4; 11,1: E.1 passo 5 (NMP); 35.670,95: E.1 passo 6 (VR BRUTO LEVANTADO); 1.895,85 / 4.823,39: E.1 passo 7; 30.532,61: E.1 passo 8; 1.321,10: E.1 passo 9; 28.495,55: F; 20.825,01: G.1; 7.670,54: G.2; 21.677,83: H; 7.894,67 + 11.958,93: I; 41.621,43: J; 1.576,51: K; 36.259,77 / 2.496,93: L; 37.547,99: M; 3.853,14: N; tabelas Selic/multa: O(1); 58.916,60: P (rotulo fora do roteiro)

### Exemplo 2 (`pagina_pdf` 248; 255)

- **Descontos:** True
- **Alternativa da letra H:** alternativa 1 da letra I
- **Faz além da moldura:**
  - Introduz um passo 8 inexistente na moldura: expurgar a proporcao de juros DO VALOR BRUTO LEVANTADO antes de calcular a base de IR ('Valor bruto levantado sem juros = 34.611,21 x 46.893,02 / 64.166,50 = 25.293,98', p.251).
  - Altera a formula de gross-up para uma versao com dois totais (TBSJ sem juros e TBCJ com juros) - p.250.
  - Altera o passo 2: o percentual de parcelas passiveis de IR passa a ser 41.983,06 / 46.183,06 (principal sobre principal), mas a '2a forma' impressa na mesma tabela continua 50.799,50 / 55.881,51 (com juros sobre com juros). Duas bases diferentes, mesmo resultado 90,91%.
  - Introduz a Obs. de p.250 ('Para identificar a alíquota e a parcela a deduzir ... basta aplicar o índice das parcelas passíveis de IR sobre o valor levantado, excluindo a proporção dos juros, dividir pelo número de meses...') - criterio de pre-determinacao de aliquota ausente da moldura.
  - Na letra L a base de IR do saldo passa a ser o PRINCIPAL corrigido (22.484,02) e nao o saldo bruto - p.253. Divergencia direta do Exemplo 1.
- **Moldura não executada:**
  - letra E principal
  - criterio alternativo da letra C
  - alternativa 2 da letra I

### Exemplo 3 (`pagina_pdf` 255; 262)

- **Descontos:** True
- **Alternativa da letra H:** alternativa 1 da letra I
- **Faz além da moldura:**
  - Como o fato gerador e a prestacao de servico, suprime inteiramente o INSS cota reclamada da cadeia do credito e o atualiza a parte com Selic+multa (letra N, p.261) - previsto nas Obs. da moldura, mas a moldura nao diz como. O exemplo cria uma tabela de 10 colunas A..J com formula por coluna.
  - Renumera: usa DUAS letras 'N' (p.261: 'N - Atualizar os valores de contribuicao previdenciaria...' e logo abaixo 'N - Atualizar o valor do imposto de renda sobre o valor levantado') e depois 'O - Apresentar o resumo'. Nao ha letra 'O' de INSS/IR a recolher.
  - Aplica juros Selic e multa de 20% tambem sobre o IR do levantamento (p.261) - a moldura (letra O) so fala em 'indices previstos na legislacao previdenciaria e tributaria', sem citar multa de 20% para IR.
  - Declara a Selic a usar por uma regra de defasagem de 2 meses: 'Variação da Selic de jun/15 até maio/16: 12,08% (13,08% - 1,00%), correspondente ao percentual de juros constante na tabela prática no mês de abr/15 (dois meses anteriores à data final de atualização do cálculo base) menos 1% de juros' (p.261). Ausente da moldura.
- **Moldura não executada:**
  - letra E principal
  - criterio alternativo da letra C
  - alternativa 2 da letra I
  - letra N de INSS recda (substituida)

### Exemplo 4 (`pagina_pdf` 262; 266)

- **Descontos:** True
- **Alternativa da letra H:** alternativa 1 da letra I (herdada do Exemplo 3)
- **Faz além da moldura:**
  - Reduz toda a parte trabalhista a uma unica letra A ('nos mesmos moldes explicados nas letras “A” até “M” do exemplo 3', p.264) e reaproveita numero por numero o Exemplo 3. Nenhuma letra B..M aparece.
  - Cria uma letra B inteiramente nova (p.264-266, passos 1 a 6) para cindir o INSS em dois regimes temporais - ausente da moldura.
  - Cria a 'proporcao do credito paga' como grandeza autonoma e demonstra que ela pode ser obtida por DOIS caminhos equivalentes: 179,01 / 646,32 = 27,696% e 12.816,17 / 46.274,56 = 27,696% (p.265). E a unica passagem do segmento que declara explicitamente que a imputacao e uniforme (mesma proporcao para todas as rubricas).
  - Aplica a proporcao 27,696% ao INSS das competencias ate 04/03/09 para cinda-lo entre 'parcela paga' (juros Selic + multa desde o pagamento) e 'saldo remanescente' (TR ate o marco final). A moldura nao contempla cisao de INSS por proporcao de levantamento.
- **Moldura não executada:**
  - letras B a M explicitas
  - letra E principal
  - criterio alternativo da letra C
  - alternativa 2 da letra I

---

### 4. Imputação

- **regra do manual:** proporcional (rateio principal/juros na mesma razao do total bruto)
- **citacao:** pagina_pdf: 237; texto: F - separar no saldo remanescente o principal dos juros, através de proporção em relação ao  total do cálculo da seguinte forma:
- **citacao 10 3 2 1:** pagina_pdf: 239; texto: G - separar no saldo remanescente o principal dos juros, através de proporção em relação ao  total do cálculo da seguinte forma:
- **exemplos confirmam:** True
- **prova por exemplo:** EXEMPLO: f = a/c x e = 17.270,16/20.493,92 x 14.685,53 = 12.375,45 ; g = b/c x e = 2.310,08. f+g = 14.685,53 = e. Fecha exato.; Exemplo 1: 46.893,92/64.166,50 x 28.495,55 = 20.825,01 ; 17.272,58/64.166,50 x 28.495,55 = 7.670,54. Soma = 28.495,55. Fecha exato.; Exemplo 2: 46.893,92/64.166,50 x 29.555,29 = 21.599,49 ; 17.272,58/64.166,50 x 29.555,29 = 7.955,80. Soma 29.555,29. Fecha exato.; Exemplo 3: 32.083,13/46.274,56 x 33.458,39 = 23.197,40 ; 14.191,44/46.274,56 x 33.458,39 = 10.260,99. Soma 33.458,39. Fecha exato.; Exemplo 4: reaproveita Exemplo 3 e ainda demonstra a identidade das duas vi…
- **algum exemplo abate juros primeiro:** False
- **algum exemplo abate principal primeiro:** False
- **fundamento legal citado:** 
- **busca negativa:** escopo: paginas 237-266 do PDF, texto integral por PyMuPDF (91.469 chars); termos_e_contagem: {'354': 0, 'imputa': 0, 'Código Civil': 0, 'CC': 0, 'Súmula': 0, 'Súmula 15': 0, '16.4.11': 0, 'OJ 400': 3, '12-A': 8, '12-B': 1, 'proporcional': 101, 'proporção': 14, 'propor*': 121}; conclusao: NAO ha, em todo o segmento C, qualquer fundamento normativo para a imputacao proporcional. O art. 354 do CC nao e citado (0 ocorrencias de '354' inclusive como numero isolado, em todo o segmento). Busca global no PDF inteiro: 'art. 354' = 0, '354 do' = 0. A proporcionalidade e afirmada como metodo, nao como…

### 5. Data de referência

- **termos usados na moldura:** data da amortização; data da dedução; data em que ocorreu o levantamento
- **sao a mesma data nos exemplos:** True
- **prova:** EXEMPLO: pagamento/levantamento/amortizacao = 26/04/16 em todas as linhas; corte de indices 01/04-26/04 e 27/04-31/05.; Exemplo 1 e 2: 25/10/11 em todas as linhas (B, C, D, E, F, G). Atualizacao seguinte 26/10/11 a 31/05/16.; Exemplo 3 e 4: 17/02/16 em todas as linhas. Atualizacao seguinte declarada nos Dados como 18/02/16 a 31/05/16, mas as linhas H e I imprimem Dt.Inicio 17/02/16 (ver defeitos).
- **data base final:** 31/05/16 em todos os cinco exemplos
- **divergencia de marco inicial do periodo seguinte:** Exemplo 1 e 2: 26/10/11 (dia seguinte ao levantamento) - coerente com os Dados ('Índ. AM de 26/10/11 A 31/05/16').; Exemplo 3 e 4: Dados dizem 'Índ. AM de 18/02/16 a 31/05/16' e 'Juros 18/02/16 a 31/05/16', mas TODAS as linhas H, I, K imprimem Dt.Inicio 17/02/16. Ha dupla contagem aparente do dia 17/02/16 (esta no periodo 01/07/15-17/02/16 e no periodo que comeca em 17/02/16).; EXEMPLO: corte limpo 26/04 / 27/04.
- **sumula 15 trt3:** citada_no_segmento: False; busca: 'Súmula 15' e 'Súmula' = 0 ocorrencias em p.237-266; onde_aparece_no_manual: [334]; contexto_p334: De acordo com o entendimento exposto na Súmula 15 do TRT-3ª Região, s.m.j., a responsabilidade do executado pela correção monetária e juros de mora apenas não cessa, quando o depósito é realizado pa...; confronto: Nao ha confronto possivel dentro do segmento: o segmento C simplesmente adota o levantamento como data unica e nao discute deposito x levantamento.
- **item 16 4 11:** citado_no_segmento: False; busca: '16.4.11' = 0 ocorrencias em p.237-266; onde_aparece_no_manual: [7, 333]; titulo_p333: 16.4.11 Dedução na data do depósito ou levantamento; subitens: ['16.4.11.1 Dedução na data do levantamento e não na data do depósito', '16.4.11.2 Dedução na data do depósito']; confronto: O item 16.4.11 do manual reconhece as DUAS teses (deducao na data do levantamento e deducao na data do deposito) como modelos de peticao alternativos. O segmento C adota, sem discutir e sem remeter a 16.4.11, e…

### 6. O valor pago é atualizado antes de deduzido?

- **resposta:** DEDUZIDO NOMINAL, na data do levantamento. Nunca e atualizado antes de deduzir.
- **conta:** EXEMPLO: c (total bruto em 26/04/16) 20.493,92 - d (Ded. Valor levantado) 5.808,39 = e 14.685,53. O 5.808,39 entra sem indice e sem juros; a linha 'd' nao tem coluna de indice.; Exemplo 1: 64.166,50 - 1.895,85 (INSS prop) - 1.321,10 (IR prop) - 32.454,00 (dedução vr. Levantado) = 28.495,55. O 32.454,00 e o valor liquido nominal levantado em 25/10/11.; Exemplo 3: 46.274,56 - 179,01 - 103,17 - 12.534,00 = 33.458,38 (manual imprime 33.458,39).
- **porem:** A deducao nominal NA DATA DO LEVANTAMENTO equivale economicamente a deduzir o pagamento atualizado ate o marco final, porque o que sobra e que e atualizado depois. O que o manual NUNCA faz e levar tudo ao marco final e la subtrair o valor nominal - essa seria a alternativa cara ao devedor. Medicao em 'medicao_ordens_alternativas'.
- **correcao de premissa do enunciado:** O enunciado sugeria que 'o valor pago e atualizado antes de deduzido' seria uma possibilidade viva. Nao e: em nenhum dos 5 exemplos ha linha de atualizacao do valor pago. Busca por linha com 'levantado' + coluna Indice preenchida: 0 ocorrencias.

### 7. Amortização sobre bruto ou líquido

- **10 3 1 sem descontos:** A amortizacao incide sobre o BRUTO. EXEMPLO: c=20.493,92 (total bruto em 26/04/16) menos 5.808,39. Nao ha descontos, logo bruto=liquido.
- **10 3 2 1 com descontos:** A amortizacao incide sobre o BRUTO, mas o bruto e previamente reduzido pelo INSS e pelo IR PROPORCIONAIS AO LEVANTAMENTO (nao pelos descontos totais).
- **sequencia literal Exemplo 1 p245:** Total do recte 64.166,50; Dedução INSS cota reclamante proporcional ao valor pago (1.895,85); INSS cota recda proporcional ao valor pago 4.823,39; Base imposto de renda s/ o valor levantado 30.532,61; Dedução imposto de renda proporcional ao valor levantado (1.321,10); dedução vr. Levantado (32.454,00); Saldo devido ao recte em 25/10/11 28.495,55
- **achado:** A linha 'INSS cota recda proporcional ao valor pago 4.823,39' esta DENTRO do quadro de deducoes, sem parenteses (as deducoes reais vem entre parenteses) e nao entra na soma: 64.166,50 - 1.895,85 - 1.321,10 - 32.454,00 = 28.495,55 exato. A linha e informativa e o rotulo do quadro ('deduzir tais valores ... do total bruto') a contradiz. Mesmo defeito no Exemplo 2.
- **diferenca 10 3 1 x 10 3 2:** Em 10.3.1 o saldo rateado e (bruto - pago). Em 10.3.2.1 o saldo rateado e (bruto - INSSprop - IRprop - pago), isto e, o rateio proporcional principal/juros da letra G incide sobre uma base JA LIQUIDA de tributos proporcionais. Consequencia: os tributos proporcionais sao imputados tambem eles de forma proporcional entre principal e juros, sem que a moldura diga isso.
- **observacao:** Em 10.3.2.1 os descontos do SALDO (letras K e L) sao apurados DEPOIS da atualizacao ate o marco final, enquanto os descontos do LEVANTAMENTO sao apurados na data do levantamento. Duas datas de incidencia tributaria no mesmo calculo.

### 8. RRA e número de meses

- **NM e variavel:** True
- **regra declarada:** pagina_pdf: 240; texto: Número de meses proporcional ao saldo remanescente = diferença entre o número  total de meses e o número de meses, calculado de forma proporcional a cada  levantamento.
- **ha dois NM distintos:** True
- **NM total:** contado no calculo homologado. Ex1/Ex2: 'Número de meses total = 20 meses (janeiro/07 a junho/08 acrescidos de 02 meses referentes aos 13º salários)' (p.243). Ex3/Ex4: 'Número de meses total = 11 meses' (p.257).
- **NM do levantado NMP:** formula: NMP = (total liquido liberado ao recte / total liquido devido na data do levantamento) x NM total; base_e_LIQUIDA: True; Exemplo_1: 32.454,00 / 58.389,34 x 20 = 11,11641268... -> 11,1; Exemplo_2: 32.454,00 / 60.164,51 x 20 = 10,78841995... -> 10,8; Exemplo_3_e_4: 12.534,00 / 45.279,74 x 11 = 3,04493797... -> 3,0; nota_de_rodape: '( * ) Observada a regra de arredondamento.' (p.243) / '( * ) observando a regra de arredondamento.' (p.250, p.257). A regra NAO e declarada em lugar nenhum do segmento (busca 'ar…
- **NM do saldo:** formula: NM saldo = NM total - NMP; Exemplo_1: 20 - 11,1 = 8,9; Exemplo_2: 20 - 10,8 = 9,2; Exemplo_3_e_4: 11 - 3,0 = 8
- **efeito no art 12A:** Cada NM gera sua propria tabela: aliquota e parcela a deduzir sao determinadas por base_mensal = base_IR / NM, e a parcela a deduzir e multiplicada por NM. Logo o mesmo credito produz DOIS lancamentos de IR, um na tabela do mes do levantamento (IN/RFB 1127/11 no Ex1 e Ex2; IN/RFB 1500/14 no Ex3) e outro na tabela do marco final (IN/RFB 1500/14).
- **efeito documentado:** Ex1: IR levantado 1.321,10 (11,1 meses, 15%) + IR saldo 2.496,93 (8,9 meses, 22,5%) = 3.818,03. Ex2 (mesma base, sem juros no IR): 317,68 (10,8 m, 7,5%) + 96,56 (9,2 m, 7,5%) = 414,24. Diferenca de 3.403,79 entre incluir e nao incluir juros na base de IR, sobre dados identicos.
- **circularidade do NMP:** O NMP depende do liquido devido na data do levantamento, que depende do IR total, que depende do NM total - e a formula do VR BRUTO LEVANTADO depende do NMP. O manual resolve por dois passos sequenciais (passo 4 -> passo 5 -> passo 6) sem iterar; e por isso que a VERIFICACAO (passo 9) so fecha a menos de centavos.
- **art 12B:** citado: 1; pagina_pdf: 240; observacao: O roteiro de 10.3.2.1 preve a letra L tambem na versao do art. 12-B (regime geral), em 3 passos e SEM numero de meses. Nenhum dos 4 exemplos do segmento C exercita essa variante. Busca '12-B' = 1 ocorrencia.

## 9. Divergências entre os exemplos

14 catalogadas.

| # | Tema | Ex. 1 | Ex. 2 | Ex. 3 | Nota |
|---|---|---|---|---|---|
| 1 | base do percentual de parcelas passiveis de IR | 50.799,50 / 55.881,51 = 90,91% (com juros no… | 1a forma passa a 41.983,06 / 46.183,06 (sem j… | 25.890,35 / 31.659,54 = 81,777777% (sem juros… | as duas razoes do Ex2 dao 90,91% por coincidencia dos dados (ambas 0,90905...). Nao ha… |
| 2 | base de calculo do IR sobre o SALDO remanescente | saldo BRUTO COM juros: 41.621,43 x 0,9091 - 1… | principal corrigido SEM juros: 22.484,02 x 0,… |  |  |
| 3 | precisao do percentual de IR aplicado |  |  |  |  |
| 4 | o que consta como 'total a ser recolhido' nas tabel… |  |  |  |  |
| 5 | total original de INSS cota reclamada do mesmo quad… |  |  |  |  |
| 6 | soma da coluna 'INSS cota recte vrs. Originais' |  |  |  |  |
| 7 | soma da coluna 'Total INSS cota recte ate jun/15' |  |  |  |  |
| 8 | soma da coluna 'Total INSS cota recda ate jun/15' |  |  |  |  |
| 9 | numero de meses RRA impresso no RESUMO GERAL |  |  |  |  |
| 10 | base de calculo do IR impressa no RESUMO GERAL |  |  |  |  |
| 11 | valor de C (juros ate a amortizacao) no Exemplo 1 |  |  |  |  |
| 12 | cabecalho da tabela Selic de INSS |  |  |  |  |
| 13 | letra que rotula o resumo final |  |  |  |  |
| 14 | marco inicial do periodo posterior ao levantamento |  |  |  |  |

## 10. Aritmética

- **metodo:** decimal.Decimal, getcontext().prec=40, quantize 2 casas ROUND_HALF_UP apenas na comparacao final. Nenhum float.
- **placar:** linhas_conferidas: 168; reproduzem_exato: 139; delta_0_01_a_0_03: 20; delta_maior: 9
- **confirmacao da premissa:** CONFIRMADA. A aritmetica e encadeada em precisao plena e os impressos de 2 casas nao sao os operandos. Prova limpa: Exemplo 1, letra H, 20.825,01 x 1,04095137 = 21.677,8227 (-> 21.677,82), mas o manual imprime 21.677,83; refazendo com o operando pleno 20.825,010591 o produto e 21.677,834 (-> 21.677,83). Nenhuma regra de arredondamento e declarada em lugar nenhum do segmento.

### Reproduzem exatamente — destaques

- EXEMPLO: a=17.270,16 ; b=3.223,76 ; c=20.493,92 ; e=14.685,53 ; f=12.375,45 ; g=2.310,08 ; h=12.396,84 ; j=14.851,42 (todos exatos)
- Exemplo 1: 46.893,92 / 3.410,34 / 8.676,53 / 8.816,44 / 50.799,50 / 54.923,43 / 2.746,17 / 5.871,69 / 2.366,82 / 58.389,34 / 1.895,85 / 4.823,39 / 30.532,61 / 2.750,69 / 3.258,79 / 1.321,10 / 28.495,55 / 20.825,01 / 7.670,54 / 1.576,51 / 4.074,13 / 5.661,52 / 2.496,93 / 37.547,99 / 857,30 / 379,17 / 3.132,32 / 4.708,8…
- Exemplo 2: 17.272,58 / 64.166,50 / 39.220,92 / 1.961,05 / 2.349,92 / 591,65 / 60.164,51 / 1.839,53 / 4.680,09 / 8.885,72->n.a. / 1.958,81 / 1.268,95 / 1.996,48 / 29.555,29 / 21.599,49 / 7.955,80 / 22.484,02 / 8.281,60 / 12.403,68 / 43.169,30 / 18.804,13 / 2.043,92 / 1.313,75 / 96,56 / 831,84 / 367,91 / 4.674,40 / 11.8…
- Exemplo 3: 11.608,50 / 43.268,04 / 32.083,13 / 14.191,44 / 646,32 / 2.326,40 / 1.570,78 / 348,50 / 45.279,74 / 2.368,85 / 8.885,72 / 2.362,50 / 428,40 / 23.197,40 / 10.260,99 / 23.323,09 / 10.316,58 / 800,76 / 34.440,43 / 469,85 / 2.325,40 / 1.142,39 / 252,85 / 33.717,73 / 75,57 / 281,08* / 125,11 / 705,60 / 2.608,89…
- Exemplo 4: 743,00 / 6.875,89 / 50.249,15 / 27,696% (pelas duas vias) / 278,93 / 77,25 / 201,68 / 2.750,84 / 761,87 / 1.988,97 / 202,77 / 1.999,75 / 1,59 / 15,45 / 94,29 / 15,69 / 152,37 / 929,93 / 154,59 / 71,24 / 582,01 / 384,69 / 636,91 / 676,30 / 879,07 / 6.101,91 / 8.101,66 / 43.077,24

### Não reproduzem

| Onde | Impresso | Minha conta | Delta | Classe |
|---|---|---|---|---|
| 238 |  | 2.310,08 x 1,00172879 = 2.314,07 ; 12.396,84 x 1,13333% = 140… | -0,01 | arredondamento de planilha (cadeia plena da 2.454,571) |
| 242 |  | 46.893,92 x 0,368333 = 17.272,58 (indice impresso '0,36833300… | +0,01 | resido de versao / divergencia interna: p.247 e todo o resto do exemplo usam… |
| 244 |  |  |  | REGRA MAL IMPRESSA, resultado correto. A formula publicada tem o sinal de (IN… |
| 245 |  | 7.670,54 x 1,04095137 = 7.984,66 | -89,99 | TRANSPOSICAO DE DIGITOS (7.984,66 -> 7.894,67). Prova: o proprio manual soma… |
| 245 |  | 21.677,83 x 55,166667% = 11.958,94 | -0,01 | arredondamento de planilha |
| 246 |  |  |  | REGRA NAO DECLARADA: a coluna diz '90,91%' mas a conta usa o percentual pleno… |
| 247 |  | 3.853,14 x 1,04095137 = 4.010,93 | -157,79 | DEFEITO: a coluna 'Vr. Calculado' repete a base sem aplicar o indice. Que e d… |
| 247 |  | 4.823,39 + 2.181,14 + 964,68 = 7.969,21 | -0,01 | arredondamento de planilha |
| 251 |  |  |  | resolvido: (i) '46.893,02' e erro de digitacao de 46.893,92 e (ii) o operando… |
| 251 |  | 25.293,98 x 0,9091 - 1.839,53 = 21.155,23 | +0,03 | arredondamento de planilha / circularidade do gross-up (o manual escolhe o VB… |
| 251 |  | 21.155,20 x 7,5% - 1.268,95 = 317,69 | -0,01 | arredondamento |
| 253 |  | 8.676,53 - 4.680,09 = 3.996,44 | -0,90 | TRANSPOSICAO DE DIGITOS na base. O manual entao multiplica a base ERRADA: 3.9… |
| 254 |  | 4.680,09 x 45,22% = 2.116,34 ; x 20% = 936,02 ; total 7.733,03 | juros +0,40 ; multa +0,18 ; total +0,90 | a base efetivamente usada foi 4.680,99 (4.680,99 x 45,22% = 2.116,74 ; x 20%… |
| 253 |  | 1.570,81 x 1,04095137 = 1.635,14 | -0,01 | arredondamento |
| 255 |  | 43.268,04 - 637,79 - 323,16 = 42.307,09 | +0,01 | arredondamento herdado do calculo de origem; propaga para o RESUMO 30/06/15 (… |
| 256 |  | 31.659,54 x 1,001337943 = 31.701,90, nao 32.083,13. O indice… | -381,23 se o dado impresso fosse obedecido | DEFEITO DE DIGITACAO no quadro de Dados (um zero a mais). O calculo esta cert… |
| 256 |  | 32.083,13 + 14.191,44 = 46.274,57 | -0,01 | arredondamento de cadeia (operandos plenos 32.083,1289 + 14.191,4343 = 46.274… |
| 257 |  | 32.083,13 x (25.890,35/31.659,54) - 646,32 = 25.590,43 | -0,01 | arredondamento |
| 258 |  |  |  | mesma formula mal impressa do Exemplo 1 (sinal de INSS/TBCJ invertido). Resul… |
| 259 |  | 12.816,17 - 179,01 - 103,17 = 12.533,99 ; saldo 46.274,56 - 1… | +0,01 nos dois | arredondamento |
| 260 |  |  |  | DEFEITO DE TEXTO: o subtraendo impresso (252,85) e o PROPRIO IR resultante da… |
| 260 |  | 646,32 - 179,01 = 467,31 | +0,01 | arredondamento / digitacao. 467,32 x 1,00541801 = 469,85 (bate); 467,31 daria… |
| 261 |  | 625,56 + 281,08 + 125,11 = 1.031,75 | +0,01 | arredondamento; propaga para o RESUMO GERAL (44.746,40 x 44.746,41) |
| 262 |  | 33.717,73 + 1.031,76 + 9.618,14 + 125,93 + 252,85 = 44.746,41 | -0,01 | arredondamento |
| 263 |  | 275,25 + 356,18 = 631,43 | +5,87 | NAO E ERRO: 275,25 e valor JA CORRIGIDO ate 30/06/15 e 356,18 e valor ORIGINA… |
| 266 |  | 976,82 + 3.184,55 = 4.161,37 | separador decimal deslocado 3 casas | DEFEITO DE IMPRESSAO |
| 266 |  | 976,82 + 384,69 = 1.361,51 | -0,99 | BLOQUEIO (parte 1) - ver pendencias |
| 266 |  |  |  | BLOQUEIO (parte 2) - ver pendencias |
| 266 |  | 356,18 x 12,08% = 43,0265 -> 43,03 | -0,01 | arredondamento (truncamento?). Nao declarado. |

## 11. Medição — o efeito da ordem de imputação

### metodo

decimal.Decimal prec=40. Mantidos todos os demais parametros do exemplo; variada apenas a ordem de imputacao ou a forma de deduzir.

### caso A EXEMPLO 10 3 1

- **por que:** unico exemplo do segmento sem INSS/IR - isola o efeito puro da imputacao
- **dados:** B_principal_26_04_16: 17.270,16; C_juros_26_04_16: 3.223,76; D_bruto: 20.493,92; pago: 5.808,39; E_saldo: 14.685,53; AM_27_04_a_31_05: 1,00172879; juros_periodo_restante: 1,1333333%
- **ordens:** {'ordem': 'PROPORCIONAL (manual)', 'principal_apos': '12.375,45', 'juros_apos': '2.310,08', 'G': '12.396,84', 'H': '2.454,57', 'saldo_final_31_05_16': '14.851,42', 'delta_R$': '0,00', 'delta_pct': '0,0000%'}; {'ordem': 'JUROS PRIMEIRO (art. 354 do CC)', 'principal_apos': '14.685,53', 'juros_apos': '0,00', 'G': '14.710,92', 'H': '166,72', 'saldo_final_31_05_16': '14.877,64', 'delta_R$': '+26,23', 'delta_pct': '+0,1766%'}; {'ordem': 'PRINCIPAL PRIMEIRO', 'p…
- **amplitude:** R$ 36,60 entre o extremo credor e o extremo devedor, sobre um saldo de ~R$ 14,85 mil = 0,246%
- **sinal:** juros primeiro (art.354) e o MAIS CARO para o devedor; principal primeiro e o mais barato. O criterio proporcional do manual fica no meio, 0,18% abaixo do art. 354.
- **razao:** o periodo residual e curtissimo (1 mes e 4 dias, juros 1,1333%). O efeito cresce com o tempo residual - ver caso B.

### caso B EXEMPLO 1

- **por que:** periodo residual longo (26/10/11 a 31/05/16, juros 55,166667%, AM 1,04095137) - amplifica o efeito
- **dados:** B_principal: 46.893,92; C_juros: 17.272,58; D_bruto: 64.166,50; bruto_absorvido_pelo_levantamento: 35.670,95 (liquido 32.454,00 + INSS prop 1.895,85 + IR prop 1.321,10); S_saldo: 28.495,55
- **ordens:** {'ordem': 'PROPORCIONAL (manual)', 'principal_apos': '20.825,01', 'juros_apos': '7.670,54', 'saldo_bruto_31_05_16': '41.621,41', 'obs': 'o manual imprime 41.621,43; diferenca de 0,02 por cadeia plena', 'delta_R$': '0,00', 'delta_pct': '0,0000%'}; {'ordem': 'JUROS PRIMEIRO (art. 354 do CC)', 'principal_apos': '28.495,55', 'juros_apos': '0,00', 'saldo_bruto_31_05_16': '46.026,28', 'delta_R$': '+4.404,87', 'delta_pct': '+10,5832%'}; {'ordem': 'PRINCIPAL PRIM…
- **amplitude:** R$ 9.918,92 entre extremos = 23,83% do saldo apurado pelo manual
- **leitura:** a escolha da ordem de imputacao vale 10,58% a favor do exequente (art. 354) ou 13,25% a favor do executado (principal primeiro). O manual nao justifica a escolha do meio-termo.

### caso C deducao nominal x atualizada

- **exemplo:** EXEMPLO (10.3.1)
- **referencia:** saldo do manual em 31/05/16 = 14.851,42
- **total bruto em 31 05 16 sem amortizacao:** 20.725,42
- **variantes:** {'variante': 'deduzir o valor pago NOMINAL no marco final (nao atualiza nada do pagamento)', 'conta': '20.725,42 - 5.808,39', 'saldo': '14.917,03', 'delta_vs_manual_R$': '+65,61', 'delta_pct': '+0,4418%'}; {'variante': 'deduzir o valor pago atualizado SO por correcao monetaria ate o marco final', 'conta': '20.725,42 - 5.808,39 x 1,00172879 = 20.725,42 - 5.818,43', 'saldo': '14.906,99', 'delta_vs_manual_R$': '+55,57', 'delta_pct': '+0,3741%'}; {'variante':…
- **conclusao:** O metodo do manual (deduzir nominal NA DATA do levantamento e atualizar o resto) fica entre a segunda e a terceira variantes. Ele NAO equivale a deduzir nominal no marco final (isso custaria +0,44% ao devedor) nem a deduzir o pagamento plenamente atualizado (isso o beneficiaria em 0,07%). A diferenca entre o metodo do manual e a terceira variante e exatamente a mesma do 'principal primeiro' do caso A (-10,37 / -10,38): deduzir o pagamento atualizado com j…

### conclusao para R10

- **invariante sugerida:** R10 deve fixar (i) imputacao PROPORCIONAL principal/juros, (ii) deducao NOMINAL na data do levantamento, (iii) rateio incidindo sobre o bruto JA liquido dos tributos proporcionais ao levantamento.
- **numeros que decidem:** proporcional_x_juros_primeiro: +10,58% (Ex1) / +0,18% (EXEMPLO); proporcional_x_principal_primeiro: -13,25% (Ex1) / -0,07% (EXEMPLO); nominal_no_marco_final_x_manual: +0,44% (EXEMPLO)
- **sensibilidade:** o efeito da ordem de imputacao escala com (taxa de juros do periodo residual) x (participacao dos juros no bruto na data da amortizacao). No Ex1: juros = 26,92% do bruto e periodo residual = 55,17% -> 23,8% de amplitude. No EXEMPLO: juros = 15,73% do bruto e periodo residual = 1,13% -> 0,25% de amplitude.

## 12. Notas e rótulos

### notas de rodape conferidas

- **( * ) Observada a regra de arredondamento.** (`pagina_pdf` 243) — 
- **( * ) observando a regra de arredondamento.** (`pagina_pdf` 250) — 
- **( * ) observando a regra de arredondamento.** (`pagina_pdf` 257) — 
- **( * ) cópia da tabela prática vigente em maio/16, consta no final deste manual.** (`pagina_pdf` 265) — 
- **( * ) taxa Selic a ser utilizada = taxa Selic constante no mês de abril/15 (02 meses anteriores a jun/15) na tabela prática vigen…** (`pagina_pdf` 266) — 

### rotulos contra a conta que a coluna faz

- **Demonstração item " I "** (`pagina_pdf` 239) — j = h + i, que e a letra J do roteiro
- **- Diferença devida em 31/05/16 (l + m)** (`pagina_pdf` 239) — h + i (12.396,84 + 2.454,58)
- **atualizado  com AM até 3/05/16** (`pagina_pdf` 238) — ate 31/05/16
- **G 1.961,05 Base de cálculo mensal ... (D / E )** (`pagina_pdf` 250) — E / F = 39.220,92 / 20
- **K 591,65 Imposto de renda devido nos termos da RFB nº 1127/11  (D X E - I)** (`pagina_pdf` 250) — E x H - J = 39.220,92 x 7,5% - 2.349,92
- **Base imposto de renda s/ o valor levantado ... Índice 90,91%  30.532,61** (`pagina_pdf` 245) — 35.670,95 x 0,9091 - 1.895,85 (ha uma subtracao de INSS que a coluna 'Índice' nao anuncia)
- **INSS cota recda proporcional ao valor pago 4.823,39 (dentro do quadro 'deduzir tais valores ... do total bruto')** (`pagina_pdf` 245) — nao entra na soma do saldo
- **Base imposto de renda s/ o saldo remanescente \| Vr.Base 22.484,02 \| Índice 90,91% \| 18.804,13** (`pagina_pdf` 253) — 22.484,02 x 0,90905739 - 1.635,13 - usa o percentual PLENO, nao os 90,91% impressos
- **Base imposto de  renda s/ o saldo remanescente \| 41.621,43 \| 90,91% \| 36.259,77** (`pagina_pdf` 246) — 41.621,43 x 0,90905739 - 1.576,51
- **Multa (0,33% ao dia limitada a 20%) (col. G x col. E)** (`pagina_pdf` 261) — 125,11 = 625,56 x 20%, ou seja col.F x 20% (col.G e 75,57, col.E e 12,08%)
- **cabecalho A..J com 10 letras** (`pagina_pdf` 261) — a linha tem Comp + 9 valores; os rotulos estao deslocados uma coluna (a col. F 'Vr. INSS até maio/16 (vr. Col. C)' recebe o valor da col. B)
- **Total INSS recte com juros Selic e multa** (`pagina_pdf` 263) — 60,19 = 45,52 + 14,67 (principal + juros, SEM multa); total da coluna 467,75
- **RESUMO GERAL do Exemplo 2: 'Nº de meses RRA: 11,10' e 'Nº de meses RRA: 8,90'** (`pagina_pdf` 254) — o Exemplo 2 apurou 10,8 e 9,2
- **Saldo bruto em 29/02/12** (`pagina_pdf` 255) — 43.169,30 em 31/05/16 (Dt. Inicio e Dt. Final da propria linha sao 31/05/16)
- **Principal atualizado = valor principal constante no cálculo homologado x índice de atualização de 01/10/08 a 25/10/11** (`pagina_pdf` 254) — Dt. Inicio 01/07/10, Dt. Final 25/10/11, indice 1,0153923 (que e o AM de 01/07/10 a 25/10/11)
- **Base imposto de renda sobre o saldo remanescente = total do principal corrigido (vr. sem juros) em 31/05/16 x percentual das parc…** (`pagina_pdf` 260) — o subtraendo real e 469,85 (INSS), nao 252,85 (que e o proprio IR resultante)
- **IR s/ o vr. Levantado ... Base de cálculo: 30.530,86** (`pagina_pdf` 247) — 30.532,61
- **Dedução imposto de renda s/ 25.252,56 (11 meses) OJ 4/00** (`pagina_pdf` 256) — a orientacao e a OJ 400 da SBDI-1, e o '4/00' aqui colide com o 'Prov. 04/00' citado duas linhas abaixo

## 13. Defeitos do original

28 catalogados. Nenhum corrigido.

| # | Gravidade | Tipo | `pagina_pdf` | Observação |
|---|---|---|---|---|
| D05 | ALTA | formula errada | 244 | VR. BRUTO LEVANTADO publicado como '{ 1 – [(TB x IPIR – INSS)  x  ALIQ. / TB]  + (INSS / TB)}'. O sinal de (INSS/TB) esta invertido: o denominador correto e 1 - (INSS/TB) - [… |
| D06 | ALTA | parametro trocado | 244 | a substituicao numerica do Exemplo 1 usa 'x 22,5%' quando o passo 4 da mesma pagina anterior (p.243, letra G) apurou aliquota de 15,00%. Com 22,5% o resultado seria 38.706,96. |
| D07 | ALTA | transposicao de digitos | 245 | 'Vr. Juros atualiz. ... 7.670,54  1,04095137  7.894,67' - o produto e 7.984,66. Prova interna: o proprio manual declara o saldo bruto 41.621,43, que so fecha com 7.984,66. Re… |
| D08 | ALTA | coluna nao calculada | 247 | letra N do Exemplo 1: Vr.Base 3.853,14 x Indice 1,04095137 = Vr.Calculado 3.853,14 (indice nao aplicado). O valor correto 4.010,93 aparece sem demonstracao na tabela seguinte. |
| D12 | ALTA | transposicao de digitos com propagacao | 253 | letra N do Exemplo 2: Vr.Base impressa 3.995,54 quando 8.676,53 - 4.680,09 = 3.996,44. O manual multiplica a base errada e obtem 4.159,16 (o correto seria 4.160,10). Propaga… |
| D13 | ALTA | transposicao de digitos | 254 | tabela O do Exemplo 2, INSS cota reclamada: base impressa 4.680,09 mas juros 2.116,74, multa 936,20 e total 7.733,93 so fecham com base 4.680,99. |
| D14 | ALTA | linha copiada de outro exemplo | 254 | RESUMO GERAL do Exemplo 2 imprime 'Nº de meses RRA: 11,10' e '8,90' (valores do Exemplo 1) quando o proprio exemplo apurou 10,8 e 9,2; e 'Base de cálculo: 21.154,54' quando a… |
| D17 | ALTA | dado errado | 256 | quadro Dados do Exemplo 3: 'Índ. AM de 01/07/15 a 17/02/16  1,001337943'. Todas as linhas usam 1,01337943. Com o indice impresso o principal seria 31.701,90 em vez de 32.083,… |
| D19 | ALTA | formula errada no texto | 260 | '23.323,09 x 81,77777% - 252,85 = 18.603,17'. O subtraendo real e o INSS sobre o saldo (469,85); 252,85 e o IR que resulta da propria linha. Com 252,85 o resultado seria 18.8… |
| D23 | ALTA | separador decimal | 266 | '4,16137' na coluna C do INSS cota recda; o valor e 4.161,37 (= 3.184,55 + 976,82). |
| D24 | BLOQUEIO | aritmetica nao fecha por via declarada alguma | 266 | ver pendencias P01 |
| D01 | baixa | digitacao | 238 | 'atualizado  com AM até 3/05/16' - falta o 1 de 31/05/16 |
| D18 | baixa | inconsistencia de precisao | 256 | Dados declaram juros de 44,233333% e as linhas usam 44,23333%; Dados declaram AM de 18/02/16 a 31/05/16 e as linhas usam Dt.Inicio 17/02/16. |
| D26 | baixa | divergencia interna | 242 | letra C do Exemplo 1 imprime 17.272,59 e letra D imprime 64.166,51; todo o restante do exemplo e a planilha integral (p.247) usam 17.272,58 e 64.166,50. |
| D27 | baixa | sigla | 256 | 'Dedução imposto de renda s/ 25.252,56 (11 meses) OJ 4/00' - a orientacao aplicada e a OJ 400 da SBDI-1 (assim citada nos Parametros da mesma pagina); '4/00' colide com o 'Pr… |
| D28 | baixa | soma de coluna | 255 | somas declaradas do quadro de INSS do Exemplo 3 divergem da soma item a item: recte originais 625,56 x 625,55 ; total recte 831,08 x 831,10 ; recda originais 5.841,04 x 5.841… |
| D02 | media | rotulo | 239 | a linha final do EXEMPLO e rotulada 'Demonstração item " I "' e sua formula e '(l + m)'; o roteiro de 10.3.1 nao tem letra I e o demonstrativo nao tem linhas l e m (vai de a… |
| D03 | media | numeracao | 241 | o roteiro de 10.3.2.1 traz DUAS letras 'O' consecutivas e nenhuma letra 'P'; os Exemplos 1 e 2 rotulam o resumo como 'P' e os Exemplos 3 e 4 como 'O'. |
| D04 | media | referencia cruzada | 238 | na alternativa 2 da letra H (10.3.1) e da letra I (10.3.2.1, p.240) manda-se aplicar juros integrais 'sobre o crédito atualizado apurado na letra “G”' quando, em 10.3.2.1, o… |
| D09 | media | residuo | 247 | RESUMO GERAL do Exemplo 1: 'Base de cálculo: 30.530,86' contra 30.532,61 apurado (delta 1,75). |
| D10 | media | rotulo | 250 | '(D / E )' para a base mensal (correto E/F) e '(D X E - I)' para o IR (correto E x H - J). Mesmos rotulos errados em p.257 (Exemplo 3). Em p.243 (Exemplo 1) a formula esta co… |
| D11 | media | digitacao | 250 | '46.893,02' onde o principal corrigido e 46.893,92. Ocorre na substituicao da formula (p.250) e na conta do valor bruto sem juros (p.251). |
| D15 | media | rotulo de periodo | 254 | 'índice de atualização de 01/10/08 a 25/10/11' com Dt.Inicio 01/07/10 - 01/10/08 e o marco dos juros, nao da correcao. Em p.249 o mesmo registro esta correto. |
| D16 | media | residuo de versao | 255 | 'Saldo bruto em 29/02/12' numa linha cujas datas sao 31/05/16 e cujo valor e 43.169,30. |
| D20 | media | cabecalho deslocado + formula de coluna errada | 261 | tabela Selic do Exemplo 3: cabecalho A..J (10 letras) para Comp + 9 valores; 'Multa ... (col. G x col. E)' quando a conta e col.F x 20%; 'Total devido ... (col. F + col. H +… |
| D21 | media | letra duplicada | 261 | o Exemplo 3 tem duas letras 'N' consecutivas (INSS e depois IR) e nenhuma letra que corresponda a letra O do roteiro. |
| D22 | media | rotulo | 263 | coluna 'Total INSS recte com juros Selic e multa' cujo conteudo e principal + juros, sem multa (60,19 = 45,52 + 14,67). |
| D25 | media | linha sem efeito | 245 | 'INSS cota recda proporcional ao valor pago 4.823,39' figura no quadro de deducoes do saldo (cujo titulo manda 'deduzir tais valores ... do total bruto') mas nao e deduzida e… |

## 14. Pendências

### P01 — BLOQUEIO

- **Onde:** 266
- **Exemplo:** Exemplo 4
- **Linha:** tabela do passo B.5, INSS cota reclamada
- **Impresso:** 3.184,55 \| 976,82 \| 4,16137 \| 3.184,55 \| 12,08% \| 384,69 \| 1.360,52 \| 20% \| 636,91 \| 5.171,98
- **Valor implícito:** para que 5.171,98 feche seria preciso col.H = 1.350,52, que nao decorre de nenhuma operacao demonstrada (976,82 + 373,70; 373,70 / 3.184,55 = 11,735%, e nao os 12,08% de Selic declarados)
- **O que não fecha:** col. H declarada como '(col. D + col. G)': 976,82 + 384,69 = 1.361,51, impresso 1.360,52, delta 0,99; col. K declarada como '(col. F + col. H + col. J)': com os IMPRESSOS da 3.184,55 + 1.360,52 + 636,91 = 5.181,98, impresso 5.171,98, delta 10,00; com o H correto da 5.182,97, delta 10,99
- **Por que é bloqueio:** sao DOIS desvios independentes e de ordens de grandeza diferentes (0,99 e 10,00) na mesma linha, e o segundo NAO e absorvivel por arredondamento. Nao e resido de versao identificavel nem arredondamento de planilha; nao ha regra declarada que produza 1.360,52 nem 5.171,98.
- **Propagação:** 5.171,98 -> 'INSS cota reclamada com juros Selic e multa (929,93 + 5.171,98) 6.101,91' -> 'Total INSS reclamada 8.101,66' -> RESUMO GERAL -> 'TOTAL DO CÁLCULO EM 31/05/16 43.077,24', que e exatamente o marco final do segmento. Com a aritmetica correta: 5.182,97 / 6.112,90 / 8.112,65 / TOTAL 43.088,23. Delta do total: +10,99.
- **Ação:** NAO contornado. Registrado como bloqueio. O valor 43.077,24 usado como fronteira do segmento e, ele proprio, produto do defeito.

### P02 — regra oculta (resolvida por inferencia, nao declarada)


### P03 — regra oculta


### P04 — comparacao com a pendencia herdada do item 10.1 (p.215, 2.820,40 / 5.109,98, delta 0,44)


### P05 — corte de segmento


### P06 — coerencia interna do manual


## 15. Buscas que sustentam as afirmações negativas

Nenhuma negativa deste bloco é opinião.

| Termo | Escopo | Ocorrências | Conclusão |
|---|---|---|---|
| `354` | p.237-266 | 0 | o art. 354 do CC nunca e invocado |
| `art. 354 / 354 do` | PDF inteiro (471 paginas) | 0 | o manual nunca cita o art. 354 do CC |
| `imputa (imputar/imputacao)` | p.237-266 | 0 | o vocabulario da imputacao do pagamento nao e usado; o manual fala so em 'proporcao' |
| `Código Civil` | p.237-266 | 0 |  |
| `Súmula (qualquer)` | p.237-266 | 0 | nenhuma sumula e citada no segmento |
| `Súmula 15` | PDF inteiro | 3 | p.33 e a Sumula 15 do TST (RSR); p.334 e a Sumula 15 do TRT-3 (deposito judicial). Nenhuma no segmento C. |
| `16.4.11` | p.237-266 | 0 | o item existe (p.333, 'Dedução na data do depósito ou levantamento') mas nao e referenciado pelo segmento |
| `data-base` | p.237-266 | 0 | o termo nao e usado; o manual usa 'data da amortização', 'data da dedução', 'data do levantamento', 'data do pagamento'… |
| `proporcional` | p.237-266 | 101 |  |
| `proporção` | p.237-266 | 14 |  |
| `levantamento` | p.237-266 | 119 |  |
| `dedução` | p.237-266 | 57 |  |
| `amortiza*` | p.237-266 | 25 |  |
| `vincend*` | p.237-266 | 14 | todas as ocorrencias sao do texto do roteiro (as duas copias da letra C e da letra H/I). NENHUM dos 4 exemplos tem juro… |
| `arredond*` | p.237-266 | 3 | apenas as tres notas de rodape; a regra nunca e enunciada |
| `12-A` | p.237-266 | 8 |  |
| `12-B` | p.237-266 | 1 | previsto no roteiro, nao exercitado por nenhum exemplo do segmento |
| `OJ 400` | p.237-266 | 3 | citada apenas nos Parametros dos Exemplos 2, 3 e 4 |
| `linha com 'levantado' e coluna Índice pre…` | p.237-266 | 0 | sustenta a afirmacao de que o valor pago nunca e atualizado antes de deduzido |

