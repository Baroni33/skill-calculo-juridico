# Bloco 11C — detalhe

Companheiro de `bloco-11c-vincendos.md`. Material bruto do **segmento D do capítulo 10**
— Exemplos 5 e 6, juros vincendos e regime do art. 12-B.

Gerado por script a partir de `cap10_3d.json`. **Offset de paginação zero.**

---

## 1. Fronteiras

- **offset paginacao:** 0
- **metodo:** PyMuPDF doc[pagina-1].get_text(), encoding utf-8
**inicio**

- **pagina pdf:** 266
- **offset:** 2141
- **texto literal:** Exemplo 5:  Atualização com amortização para cálculo envolvendo rendimentos decorrentes  do ano-calendário do recebimento ou rendimentos pagos por entidades de previdência  complementar  até 10/03/15– juros incluídos na base de cálculo do IR
- **anterior:** TOTAL DO CÁLCULO EM 31/05/16  43.077,24 (fecho do Exemplo 4, segmento C)
- **confirmado:** True

**fim**

- **pagina pdf:** 277
- **confirmado:** True
- **observacao:** A p.277 contém apenas a cauda da planilha-resumo do Exemplo 6 (continuação de linhas cortadas na p.276: 'parcelas passíveis IR – cont. previd. s/ o saldo remanescente) ... 4.519,52', 'Dedução imposto de renda (4.519,52 x 22,5% - 636,13)) 380,77', 'Total líquido do recte 4.348,51') seguida de linhas em branco. O capítulo 11 abre na p.278 com '11 - EXEMPLO DE CÁLCULOS, ACORDOS E ATUALIZAÇÕES'. Limite de conteúdo e limite de página coincidem.

**heading numerado**

- **existe:** False
- **busca:** regex '^\s*1[01]\.\d' em todas as linhas das pp.266-278; 18 matches, TODOS valores monetários (11.418,94 / 11.708,40 / 11.731,57 / 11.959,42 / 10.453,85). Nenhum heading de seção.
- **conclusao:** CONFIRMADO: Exemplo 5 e Exemplo 6 continuam pendurados em 10.3.2.1, sem subtítulo próprio. A premissa do enunciado se confirma.

- **conteudo:** {'rotulo': 'Exemplo 5', 'pagina_inicio': 266, 'pagina_fim': 271, 'item': '10.3.2.1'}; {'rotulo': 'Exemplo 6', 'pagina_inicio': 271, 'pagina_fim': 277, 'item': '10.3.2.1'}
**moldura aplicada**

- **observacao importante:** Os Exemplos 5 e 6 NÃO seguem a moldura A–H,J de 10.3.1 (p.237) descrita no enunciado; seguem a moldura de 10.3.2 (pp.239-241), que tem letras A a O/P e INCLUI a letra I. Correspondência: 10.3.1.F (rateio) = 10.3.2.G ; 10.3.1.G = 10.3.2.H ; 10.3.1.H = 10.3.2.I ; 10.3.1.J = 10.3.2.J.
- **consequencia:** A afirmação do enunciado de que 'não há letra I' vale só para 10.3.1. Exemplo 5 e Exemplo 6 usam letra I.


## 2. O critério alternativo da letra C

- **onde esta enunciado:** p.237 (moldura 10.3.1); p.239 (moldura 10.3.2)
**tres passos literal p237**

- 1 - atualizar o total dos juros do último cálculo com o mesmo índice de correção utilizado para corrigir o principal até a data da amortização;
- 2 - aplicar os juros contados da data da atualização do último cálculo até a data da dedução apenas sobre o principal corrigido apurado na letra “B”;
- 3 - O valor encontrado no item 02 deverá ser somado ao valor apurado no item 01 para obter o total de juros até a data da dedução.

- **observacao literal p237:** Quando o cálculo não envolver juros vincendos, o calculista poderá optar por qualquer um dos dois critérios, visto que os resultados finais são idênticos. Porém, quando há juros vincendos no cálculo base para a atualização, o segundo é obrigatório.
- **observacao literal p239:** Quando o cálculo não envolver juros vincendos, o calculista poderá optar por qualquer um dos dois critérios, visto que os resultados finais são idênticos. Porém, quando há juros vincendos no cálculo base para a atualização, o segundo critério é obrigatório.
- **variacao entre as duas impressoes:** p.239 acrescenta a palavra 'critério' ('o segundo critério é obrigatório'); p.237 escreve 'o segundo é obrigatório'. Mesma regra, redação não idêntica.
**em que difere do resultado do rateio**

- **resposta:** Em NADA que chegue ao rateio. O critério alternativo decompõe o total de juros em duas parcelas de origem distinta (juros pretéritos corrigidos + juros do período novo sobre o principal), mas a letra D soma tudo num único 'C', e o rateio (F em 10.3.1 / G em 10.3.2) usa apenas C/D. A decomposição é DESCARTADA antes do rateio.
- **prova Ex5:** C.1=61.088,53 (pretéritos) e C.2=11.418,94 (novos) entram na letra G apenas como C=72.507,46; a linha 'Juros contidos no saldo' aplica 72.507,46/144.627,07 sobre 105.842,17.
- **prova Ex6:** C.1=251,51 e C.2=164,24 entram na letra G apenas como 415,75; 'Juros contidos no saldo (415,75 / 12.147,12) x 5.236,71 = 179,23'.
- **consequencia:** o critério alternativo altera o VALOR de C, não a MECÂNICA de F/G.

**os exemplos usam de fato**

- **Ex5:** usa: True; prova_aritmetica: ['passo 1: 60.162,49 x 1,0153923 = 61.088,5286... -> 61.088,53 (impresso 61.088,53) OK', 'passo 2: 72.119,61 x 0,15833330 = 11.418,9399... -> 11.418,94 (impresso 11.418,94) OK — base é o PRINCIPAL CORRIGIDO da letra B, como manda o passo 2', 'passo 3: 61.088,53 + 11.418,94 = 72.507,47 (impresso 72.507,47 na letra C)']; texto_de_acionamento: Como o cálculo envolve juros vincendos, será necessário atualizar o total dos juros apurado no último cálculo até a data da amortização e aplicar o percentual de juros devido entre a data do último cálculo e a amortização apenas sobre o principal corrigido.
- **Ex6:** usa: True; prova_aritmetica: ['passo 1: 251,02 x 1,00196157 = 251,5124... -> 251,51 (impresso 251,51) OK', "passo 2: 11.731,57 x 1,40% = 164,2420 -> 164,24 (impresso 164,24) OK. ATENÇÃO: a coluna 'Vr. Base' imprime 11.708,40, que daria 163,92. O valor publicado só fecha com o principal CORRIGIDO (11.731,57).", 'passo 3: 251,51 + 164,24 = 415,75 (impresso 415,75) OK']; texto_de_acionamento: idêntico ao do Exemplo 5, literal
- **conclusao:** CONFIRMADO o objetivo primário do bloco: os Exemplos 5 e 6 são os ÚNICOS do capítulo 10 que executam o critério alternativo 1/2/3 da letra C. O segmento C (Ex.1–4) não o executa.

**o manual declara o porque**

- **resposta:** NÃO. Só declara a regra.
- **buscas no segmento D pp266 277:** obrigator*: 0; porque: 0; razao/razão: 0; vincend*: 5
- **as 5 ocorrencias de vincend:** p.267 letra C (Ex.5) — 'Como o cálculo envolve juros vincendos, será necessário...'; p.269 letra I (Ex.5) — '(procedimento correto para todas as hipóteses, sendo juros vincendos ou não)'; p.271 demonstrativo do cálculo homologado (Ex.6) — 'Juros vincendos 251,02'; p.272 letra C (Ex.6) — mesma frase de acionamento; p.274 letra I (Ex.6) — '(procedimento correto para todas as hipóteses, sendo juros vincendos ou não)'
- **leitura:** o segmento D repete a frase de acionamento e a ressalva da letra I, mas em nenhum ponto explica por que o segundo critério seria obrigatório. A própria palavra 'obrigatório' não reaparece nas pp.266-277 (só nas pp.237 e 239).
- **razao reconstruida por algebra NAO declarada pelo manual:** criterio_1: C = (P0 x idx) x p_total; criterio_2: C = J0 x idx + (P0 x idx) x p2; igualdade: os dois coincidem se e somente se p_total - p2 = J0/P0, isto é, se os juros já contidos no cálculo-base forem exatamente o percentual acumulado devido até a data do último cálculo; com_vincendos: J0 contém juros de período posterior ao último cálculo, logo J0/P0 > p_total - p2 e o critério 1 APAGARIA a parcela vincenda; o critério 2 a preserva; status: inferência do agente, NÃO está escrita no manual
- **o par Ex5 Ex6 prova a obrigatoriedade:** resposta: NÃO PROVA.; motivo: nem o Exemplo 5 nem o Exemplo 6 informam a data de ajuizamento ou o percentual acumulado de juros desde o ajuizamento. Sem esse dado o critério 1 é INEXECUTÁVEL a partir do que está publicado, logo não há como confrontar os dois resultados.; teste_feito: assumindo p_total = J0/P0 + p2 (a única reconstrução possível), o critério 1 reproduz o critério 2 com delta 0,00 nos dois exemplos: Ex.5 J0/P0 = 0,84704465, p_total implícito = 1,00537795, C1 = C2 = 72.507,47; Ex.6 J0/P0 = 0,02143931, p_total implícito = 0,03543931, C1 = C2 = 415,75.; conclusao: o par controlado exercita o critério 2, mas NÃO demonstra a necessidade dele. A obrigatoriedade permanece um comando…


## 3. Vincendos e rateio

**os vincendos entram no bruto antes do rateio**

- **resposta:** ANTES, sem exceção.
- **conta Ex6:** vincendos_originais: 251,02 (rótulo literal 'Juros vincendos' no demonstrativo homologado, p.271); corrigidos_letra_C1: 251,51; juros_novos_letra_C2: 164,24; C_total: 415,75; D_bruto: 11.731,37 + 415,75 = 12.147,12; abatimento: 12.147,12 - 5.236,71 = 6.910,41 (= bruto levantado); juros_absorvidos_pelo_pagamento: 415,75 x 6.910,41 / 12.147,12 = 236,52; juros_remanescentes_G2: 415,75 x 5.236,71 / 12.147,12 = 179,23 (impresso 179,23); fechamento: 236,52 + 179,23 = 415,75 = C; parcela_dos_vincendos_absorvida: 251,51 x 6.910,41 / 12.147,12 = 143,08
- **consequencia juridica nao discutida pelo manual:** 56,89% dos juros vincendos são tratados como QUITADOS pelo pagamento, embora sejam juros de período ainda não vencido. O manual não comenta.

**o rateio muda com vincendos**

- **resposta:** A fórmula não muda. A invariante F.1 + F.2 = E é testada nos dois exemplos:
- **Ex5:** 52.779,16 + 53.063,01 = 105.842,17 = E  -> FECHA EXATO
- **Ex6:** 5.057,47 + 179,23 = 5.236,70 contra E = 5.236,71 -> NÃO FECHA, delta -0,01. O centavo perdido é carregado para H/I/J: o total bruto 5.271,66 está construído sobre 5.236,70.
- **origem do centavo:** 5.057,47 é o arredondamento de 11.731,37/12.147,12 x 5.236,71 = 5.057,4798 -> 5.057,48 half-up. O manual imprime 5.057,47 (truncamento). Com 5.057,48 a soma fecharia em 5.236,71.

**letra I e a alternativa**

- **texto literal Ex5 p269:** I - atualizar o valor encontrado a título de juros no item 02 da letra “G” com o mesmo índice de correção monetária da data em que ocorreu o levantamento até o final do cálculo e  incidir juros do período restante (da dedução até a data final de atualização do cálculo) sobre o valor encontrado através da letra “H”, somando-se os dois resultados (procedimento correto para todas as hipóteses, sendo juros vincendos ou não).
- **texto literal Ex6 p274:** I - atualizar o valor encontrado a título de juros contidos no saldo com o mesmo índice de correção monetária da data em que ocorreu o levantamento até o final do cálculo e  incidir juros do período restante (da dedução até a data final de atualização do cálculo) sobre o valor do principal corrigido encontrado no item 10, somando-se os dois resultados (procedimento correto para todas as hipóteses, sendo juros vincendos ou não).
- **a alternativa da moldura p240:** aplicar os juros integrais (desde o ajuizamento da ação) sobre o crédito atualizado apurado na letra “G” (ressalvando que tal procedimento é adequado apenas quando não se tratar de juros vincendos)
- **constatacao:** a alternativa NÃO é usada em nenhum dos dois exemplos; ambos imprimem só o procedimento 'correto para todas as hipóteses'. Portanto a 'alternativa 1 da letra H/I' também permanece sem exemplo no manual.


## 4. Art. 12-B contra 12-A

**a string 12-B no segmento D**

- **ocorrencias pp266 277:** 0
- **ocorrencias 12-A pp266 277:** 4
- **paginas do manual com 12-B:** 6; 185; 186; 190; 191; 193; 203; 207; 224; 233; 240
- **leitura:** o segmento D nunca escreve '12-B'. O enquadramento é feito por PARÁFRASE do art. 12-B: 'rendimentos decorrentes do ano-calendário do recebimento ou rendimentos pagos por entidades de previdência complementar até 10/03/15 ... e que não se enquadram no art. 12-A da Lei 7713/88'. Essa é exatamente a definição do universo do art. 12-B dada nas pp.190-191.

**o que muda na apuracao**

- **regra geral 12B p190 literal:** sobre o montante tributável será aplicada a regra geral prevista no art. 12-B da Lei 7713/88, incluído pela Lei 13.149/15 (art. 12, caput, para períodos anteriores a 11/03/15), no art. 28 da Lei 10.833/03 e nos art. 26, 43 e 44 da IN/RFB 1500/14, utilizando a tabela progressiva mensal correspondente ao mês do pagamento, sem qualquer multiplicação pelos números de meses a que se refiram os rendimentos.
- **efeito sobre o NM:** sob o 12-B NÃO HÁ número de meses. O RRA/NM desaparece: alíquota e parcela a deduzir da tabela mensal, aplicadas uma única vez sobre a base integral.
- **codigo de recolhimento:** 5936 (regime geral) em vez de 1889 (RRA)

**o esquema de dois NM do segmento C se mantem**

- **resposta:** PARCIALMENTE, e de forma assimétrica entre os dois exemplos.
- **Ex5:** levantamento_em_25_10_11: tributado pelo regime geral — resumo imprime 'Cód. Rec: 5936' e NÃO imprime nº de meses. Não há NMP.; saldo_em_31_05_16: tributado pelo art. 12-A — resumo imprime 'IR s/ o saldo remanescente art. 12-A da Lei 7713/88 ... Nº de meses RRA: 46,8 ... Cód. Rec: 1889'; justificativa_literal_p269: Como o cálculo refere-se à complementação de aposentadoria e a partir de 11/03/15 tais rendimentos se enquadram no regime especial de tributação, conforme nova redação do art. 12-A da Lei 77713/88, a forma de tributação será alterada em relação ao saldo remanescente e o número de meses referente ao rendimento tributável…
- **Ex6:** NM: NENHUM. Nem no levantamento nem no saldo. Resumo imprime 'Cód. Rec: 5936' nos dois.; consequencia: sob 12-B puro o esquema de DOIS NM do segmento C não se mantém — simplesmente não existe.; tensao: o cabeçalho do Exemplo 6 declara 'RRA (rendimentos recebidos acumuladamente) referente a ano-calendário do recebimento...' mas nenhum número de meses é apurado, corretamente, porque o 12-B dispensa a divisão por meses. O rótulo 'RRA' nos Parâmetros é, portanto, enganoso.

**rendimentos do ano calendario e previdencia complementar**

- **como altera a base:** não altera a BASE (que continua bruto x IPIR - INSS); altera o REGIME: tabela mensal única sem multiplicação por meses. A base do Ex.5 (138.448,90) e a do Ex.6 (4.519,52) são construídas pelas mesmas regras do segmento C.
- **previdencia complementar no Ex5:** o objeto é 'complementação de aposentadoria apurada no período de set/05 a jun/10', que é justamente a hipótese 'pagos por entidades de previdência complementar até 10/03/15'. Como o pagamento do saldo ocorre depois de 11/03/15, o manual migra o saldo para o 12-A. É o único exemplo do manual que executa essa migração.


## 5. R23 — descarregar

- **enunciado da invariante:** antes de aplicar juros sobre saldo remanescente, os juros já contidos devem ser excluídos ('descarregar'), sob pena de anatocismo
- **fundamento p237 literal:** Quando há amortização de valor pago, não se pode partir de determinado crédito de saldo remanescente da execução, que já contenha juros, para sobre ele aplicar juros novamente, sendo necessário “descarregar” o saldo dos juros (excluir os juros do saldo, para aliá-los sem acumulação).
- **nota de transcricao:** o original grafa 'para aliá-los sem acumulação' — provável erro por 'aplicá-los'. Transcrito como está.
**o segmento D observa**

- **resposta:** SIM, integralmente, nos dois exemplos.
- **evidencias:** letra A de ambos: 'decompor o cálculo original, excluindo dele os juros' (Ex.5: Principal corrigido = 71.026,35 ; Ex.6: Principal corrigido = 11.708,40); letra G de ambos: o saldo é separado em principal e juros antes de qualquer nova incidência; letra I de ambos: os juros do período residual incidem SOBRE O PRINCIPAL da letra H, nunca sobre a parcela de juros, que só recebe correção monetária. Ex.5: 54.940,54 x 55,166667% = 30.308,86 (não sobre 138.448,90). Ex.6: 5.061,90 x 0,600000% = 30,37 (não sobre 5.241,29).
- **teste de anatocismo por contraexemplo:** se os juros residuais incidissem sobre o saldo já com juros, Ex.6 daria 5.241,29 x 0,6% = 31,45 em vez de 30,37 (delta +1,08) e Ex.5 daria 110.140,04 x 55,166667% = 60.761,29 em vez de 30.308,86 (delta +30.452,43). Nenhum desses valores aparece.

**interacao com vincendos**

- **achado:** o 'descarregar' opera sobre TODO o C, vincendos incluídos. Não há tratamento especial. Em Ex.6 os 251,51 de juros vincendos corrigidos são rateados e a fração remanescente (179,23) recebe só correção monetária (179,39), sem nova incidência. Logo R23 é observada mesmo na presença de vincendos.
- **risco residual nao tratado pelo manual:** o percentual do período residual (Ex.6: 0,600000% de 13/05 a 31/05) é aplicado integralmente sobre o principal, sem verificar se os juros vincendos já cobriam parte desse período. No Ex.6 não há sobreposição visível porque o demonstrativo homologado diz 'Total bruto em 31/03/16' e os percentuais seguintes começam em 01/04/16. Ver 'defeitos' item DEF-10 sobre o rótulo 'vincendos'.

**sao duas regras distintas o manual as conecta**

- **hipotese do enunciado:** a p.16 veda MULTIPLICAR percentuais (acumulação por soma); o 'descarregar' da p.237 é excluir do saldo os juros nele contidos — duas regras anti-anatocismo distintas
- **veredito:** HIPÓTESE CONFIRMADA quanto à distinção, PARCIALMENTE REFUTADA quanto à desconexão.
- **busca anatocismo no manual:** paginas: [16, 90, 328, 335]; ocorrencias_no_segmento_D_pp266_277: 0
- **busca sumula 121:** paginas: [16]; ocorrencias_no_segmento_D: 0
- **detalhamento:** p.16 — regra 1 (acumulação por soma). É o ÚNICO lugar do manual onde a Súmula 121 do STF é invocada. Literal: 'A sua acumulação é efetuada de forma simples, ou seja, através do somatório dos percentuais mensais, visto que a multiplicação dos percentuais caracterizaria anatocismo (incidência de juros sobre juros), vedado pela Súmula 121 do STF. O mesmo ocorre com os juros aplicáveis aos débitos trabalhistas.'; pp.90 e 335 — regra 1 aplicada à poupança/precatórios ('Aplicar juros acumulados das cadernetas é praticar anatocismo'), com fundamento em Lei, OS/VPADM 01/2011 e Res. CNJ 115/10, NÃO na Súmula 121.; p.237 — regra 2 ('descarregar') enunciada com a RATIO do anatocismo ('não se pode ...…
- **conclusao:** são de fato duas regras distintas. O manual as reúne sob o rótulo 'anatocismo' na p.328, mas a Súmula 121 do STF é invocada UMA ÚNICA VEZ em todo o manual (p.16) e apenas para a regra 1. O segmento D não menciona nem 'anatocismo' nem 'Súmula 121': a invariante R23 é ali praticada, não fundamentada.


## 6. Medição da amplitude

- **metodo:** decimal.Decimal, prec=50, ROUND_HALF_UP, duas casas em cada elo da cadeia. Variada APENAS a ordem de imputação do abatimento entre principal e juros; todos os demais parâmetros mantidos.
**Ex5**

- **parametros:** B_principal_25_10_11: 72.119,61; C_juros_25_10_11: 72.507,46; D_bruto: 144.627,07; abatimento: 38.784,90 (IR 9.941,90 + levantado 28.843,00); E_saldo: 105.842,17; idx_residual_26_10_11_a_31_05_16: 1,04095137; juros_residuais: 55,166667%; participacao_dos_juros_no_bruto: 50,13%
- **ordens:** {'ordem': 'PROPORCIONAL (manual)', 'principal': '52.779,17', 'juros': '53.063,00', 'total_31_05_16': '140.485,42', 'delta_R$': '0,00', 'delta_pct': '0,0000%'}; {'ordem': 'JUROS PRIMEIRO (art. 354 do CC)', 'principal': '72.119,61', 'juros': '33.722,56', 'total_31_05_16': '151.591,84', 'delta_R$': '+11.106,42', 'delta_pct': '+7,9057%'}; {'ordem': 'PRINCIPAL PRIMEIRO', 'principal': '33.334,71', 'juros': '72.507,46', 'total_31_05_16': '129.319,28', 'delta_R$': '-11.166,14', 'delta_pct': '-7,9482%'}
- **amplitude R$:** 22.272,55
- **amplitude pct:** 15,8540% sobre a base proporcional recomputada (140.485,41)
- **ressalva:** o manual PUBLICA 138.448,90, não 140.485,41 — ver defeito DEF-01. Sobre a base publicada a amplitude seria 16,0872%.

**Ex6**

- **parametros:** B_principal_12_05_16: 11.731,37; C_juros_12_05_16: 415,75; D_bruto: 12.147,12; abatimento: 6.910,41; E_saldo: 5.236,71; idx_residual_13_05_a_31_05_16: 1,00087571; juros_residuais: 0,600000%; participacao_dos_juros_no_bruto: 3,42%
- **ordens:** {'ordem': 'PROPORCIONAL (manual)', 'principal': '5.057,48', 'juros': '179,23', 'total_31_05_16': '5.271,67', 'delta_R$': '0,00'}; {'ordem': 'JUROS PRIMEIRO (art. 354 do CC)', 'principal': '5.236,71', 'juros': '0,00', 'total_31_05_16': '5.272,75', 'delta_R$': '+1,08'}; {'ordem': 'PRINCIPAL PRIMEIRO', 'principal': '4.820,96', 'juros': '415,75', 'total_31_05_16': '5.270,24', 'delta_R$': '-1,43'}
- **amplitude R$:** 2,51 (fórmula fechada: 2,50)
- **amplitude pct:** 0,0476% sobre 5.271,66

**a escala se confirma**

- **resposta:** SIM, e de forma mais forte do que o 11B formulou: a amplitude tem FÓRMULA FECHADA.
- **lei:** amplitude = min(abatimento, B, C) x idx_residual x pct_juros_residual
- **derivacao:** deslocar Δ do abatimento dos juros para o principal reduz o principal em Δ e aumenta os juros em Δ; o total varia em -Δ x idx x pct. A excursão máxima do principal é min(abatimento, B, C).
- **verificacao nos 4 casos:** {'caso': '10.3.1 (11B caso A)', 'span': '3.223,76', 'formula': '3.223,76 x 1,00172879 x 1,1333333% = 36,60', 'publicado_11B': '36,60', 'confere': True}; {'caso': 'Exemplo 1 (11B caso B)', 'span': '17.272,58', 'formula': '17.272,58 x 1,04095137 x 55,166667% = 9.918,92', 'publicado_11B': '9.918,92', 'confere': True}; {'caso': 'Exemplo 5 (segmento D)', 'span': '38.784,90', 'formula': '38.784,90 x 1,04095137 x 55,166667% = 22.272,55', 'publicado_11B': None, 'confere': None}; {'caso': 'Exemplo 6 (segmento D)', 'span': '415,75', 'formula': '415,75 x 1,00087571 x 0,600000% = 2,50', 'publicado_11B': None, 'confere': None}
- **correcao a formulacao do 11B:** a escala NÃO é 'tempo residual x participação dos juros no bruto'. É 'tempo residual x MENOR entre abatimento, principal e juros'. Por isso o Exemplo 5, com participação de juros MAIOR (50,13% contra 26,92% do Exemplo 1) e mesmo tempo residual, dá amplitude PERCENTUAL MENOR (15,85% contra 23,83%): o limitante ali é o abatimento (38.784,90), não os juros. Em valor absoluto a amplitude do Ex.5 é 2,25x a do Ex.1.
- **vincendos aumentam o tempo residual:** premissa do enunciado NÃO se confirma no segmento D. O Ex.6, que é o exemplo com vincendos declarados, tem o MENOR tempo residual do capítulo inteiro (19 dias, 0,6%). O Ex.5 tem tempo residual longo por ser um cálculo antigo (levantamento em 2011), não por causa dos vincendos.


## 7. As pendências do bloco 11B

**P11B-02 arredondamento do NMP**

- **reaparece:** SIM, em Ex.5, e AGORA SEM NEM A NOTA.
- **evidencia:** 38.784,90 / 144.627,02 x 64 = 17,16303... impresso 17,2. Consistente com 1 casa decimal half-up (truncamento daria 17,1). Mas no segmento D não há a nota '( * ) Observada a regra de arredondamento' que existia nas pp.243/250/257. A regra segue sem enunciado.
- **busca arredond pp266 277:** 0
- **Ex6:** não aplicável (regime 12-B, sem NM)

**P11B-03 percentual pleno x 0 9091**

- **reaparece:** NÃO como divergência ativa.
- **motivo:** nos dois exemplos do segmento D o índice das parcelas passíveis de IR é 100% (1,000) exato, tanto no levantamento quanto no saldo. Não há arredondamento a testar.
- **achado lateral:** o valor 0,9091 aparece em pp.244, 246, 250, 251, 253 — todas do segmento C. Mas um RESÍDUO do Exemplo 1 aparece na p.267 do segmento D: o rótulo '% parcelas passíveis de IR (50.799,50 / 55.881,51)' seguido do resultado '100%'. 50.799,50/55.881,51 = 0,90905 — é exatamente o par de operandos do Exemplo 1 (pp.242-243, 249). Ver DEF-04.

**P11B-04 base de IR do saldo varia**

- **reaparece:** SIM, e no segmento D a variação passa a ter CAUSA DECLARADA.
- **Ex5:** base do saldo = bruto COM juros (138.448,90 x 100%), coerente com o parâmetro 'Inclusão dos juros na base de cálculo do imposto de renda'
- **Ex6:** base do saldo = PRINCIPAL CORRIGIDO sem juros menos INSS (5.061,90 x 100% - 542,38 = 4.519,52), coerente com o parâmetro 'Base de cálculo imposto de renda na forma da OJ 400'
- **leitura:** no segmento C a variação entre Ex.1 (com juros) e Ex.2–4 (sem juros) era a mesma divergência, aqui explicitada como escolha de tese. O segmento D não resolve a divergência: apenas a instancia duas vezes, lado a lado, sem critério de escolha. Consistente com o item 5 do capítulo 15, que a registra sem resolver.

**P11B-05 gross up com sinal invertido**

- **reaparece:** NÃO. O gross-up fecha EXATO nos dois exemplos.
- **Ex5:** (28.843,00 - 723,95) / (1 - [(144.627,07 x 1,00 - 0) x (0,275/144.627,07) + 0]) = 28.119,05 / 0,725 = 38.784,90 EXATO; verificação inversa 38.784,90 - 0,00 - 9.941,90 = 28.843,00 EXATO
- **Ex6:** (5.426,00 - 869,36) / (1 - [(11.731,37 x 1,00 - 1.257,01) x (0,275/12.147,12) + (1.257,01/12.147,12)]) = 6.910,41 EXATO; verificação inversa 6.910,41 - 715,10 - 769,31 = 5.426,00 EXATO
- **defeito tipografico distinto:** a fórmula da p.268 grafa 'NSS' onde deveria ler 'INSS' e omite os parênteses do denominador ('/ 1 – [...]'). Não afeta o resultado publicado.

- **padrao de bloqueio delta 10 00:** procurado: True; reaparece: NÃO com magnitude 10,00.; mas: reaparece um bloqueio de MAIOR magnitude e da mesma natureza (não absorvível por arredondamento, sem regra derivável): o delta de 2.036,51 na letra I do Exemplo 5. Ver DEF-01.

## 8. Os Exemplos 5 e 6 são um par controlado?

**premissa do enunciado sobre os titulos**

- **veredito:** NÃO SE CONFIRMA.
- **titulo literal Ex5 p266:** Exemplo 5:  Atualização com amortização para cálculo envolvendo rendimentos decorrentes do ano-calendário do recebimento ou rendimentos pagos por entidades de previdência complementar  até 10/03/15– juros incluídos na base de cálculo do IR
- **titulo literal Ex6 p271:** Exemplo 6: Atualização com amortização para cálculo envolvendo rendimentos decorrentes do ano-calendário do recebimento ou rendimentos pagos por entidades de previdência complementar  até 10/03/15– juros incluídos na base de cálculo do IR
- **constatacao:** os TÍTULOS são idênticos, inclusive o fecho '– juros incluídos na base de cálculo do IR'. O que difere é o PRIMEIRO BULLET dos 'Parâmetros' (Ex.5: 'Inclusão dos juros na base de cálculo do imposto de renda'; Ex.6: 'Base de cálculo imposto de renda na forma da OJ 400'). O título do Exemplo 6 CONTRADIZ o seu próprio parâmetro. Ver DEF-09.

**sao um par controlado**

- **resposta:** NÃO, no sentido estrito. Não é o mesmo enunciado de fato com duas teses tributárias.
- **prova:** objeto diferente: Ex.5 = complementação de aposentadoria set/05-jun/10, principal 71.026,35; Ex.6 = salários jan-mar/16 com reintegração, principal 11.708,40; datas diferentes: Ex.5 levantamento 25/10/11 com residual de 4,6 anos; Ex.6 levantamento 12/05/16 com residual de 19 dias; INSS diferente: Ex.5 sem INSS (0,00); Ex.6 com INSS cota recte 1.254,55 e reclamada optante pelo SIMPLES; regime de IR do saldo diferente: Ex.5 migra para 12-A (RRA 46,8 meses, cód. 1889); Ex.6 permanece no regime geral (cód. 5936); ordens de grandeza diferentes: 144.627,07 contra 12.147,12
- **o que de fato varia em conjunto:** a tese sobre juros na base do IR varia JUNTO com todo o resto. Não há isolamento da variável.
- **consequencia:** não é possível medir, a partir do segmento D, o efeito isolado da OJ 400 sobre um mesmo crédito. A divergência do item 5 do capítulo 15 permanece sem quantificação no manual.

**efeito da tese sobre a base medido dentro de cada exemplo**

- **Ex5 base do saldo:** com juros 138.448,90 -> IR 4.162,83
- **Ex5 contrafactual OJ400:** se a base fosse só o principal corrigido (54.940,54): 54.940,54 x 15% - 16.604,51 = -8.363,43, negativo. Com a alíquota correta da faixa (54.940,54/46,8 = 1.173,94 mensal, isento) o IR seria 0,00. Diferença de 4.162,83, ou 100% do imposto do saldo.
- **Ex6 base do saldo:** sem juros 4.519,52 -> IR 380,76
- **Ex6 contrafactual com juros:** base = 5.271,66 - 542,38 = 4.729,28; 4.729,28 x 22,5% - 636,13 = 427,958 -> 427,96. Diferença +47,20, ou +12,40% do imposto do saldo.
- **ressalva:** contrafactuais calculados pelo agente, NÃO constam do manual.


## 9. Fase 4 — ADC 58

- **buscas no segmento D pp266 277:** ADC: 0; IPCA: 0; EC 113: 0; emenda: 0; Súmula: 0; taxa referencial: 0; SELIC: 12
- **observacao sobre SELIC:** as 12 ocorrências de 'Selic' são todas de acréscimos moratórios de tributos federais/previdenciários (Ex.4 na p.266 e Ex.5 letra M), nunca de correção do crédito trabalhista.
- **paginas do manual com IPCA:** 6; 15; 16; 84; 102; 104; 282; 330; 332; 368
- **regime do segmento D:** integralmente TR (índices AM da tabela única do TRT-3) + juros simples de 1% ao mês. Manual de 2016, anterior à ADC 58 (2020) e à EC 113 (2021).
**agrava ou atenua**

- **resposta:** AGRAVA no Exemplo 5; ATENUA no Exemplo 6. O segmento D produz os dois extremos do capítulo 10.
- **participacao dos juros no bruto na data da amortizacao:** Exemplo_1_segmento_C: 17.272,58 / 64.166,50 = 26,92%; Exemplo_5_segmento_D: 72.507,46 / 144.627,07 = 50,13% — a MAIOR do capítulo 10; Exemplo_6_segmento_D: 415,75 / 12.147,12 = 3,42% — a MENOR do capítulo 10
- **por que agrava no Ex5:** metade do bruto rateado é juros calculados sob TR+1%. Sob o critério da ADC 58 (IPCA-E + TRD na fase pré-judicial, SELIC a partir da citação, com SELIC já englobando juros) toda essa metade é recalculada, e a proporção B/D que comanda o rateio muda com ela.

**quantificacao da sensibilidade do rateio**

- **metodo:** mantido o saldo E (o pagamento é um fato) e variado C em ±20%, recalculando o rateio e a cadeia H/I/J
- **Ex5:** {'C': '58.005,97 (-20%)', 'principal_contido': '58.661,00', 'juros_contidos': '47.181,17', 'total_31_05_16': '143.863,11', 'delta_vs_base': '+3.377,69 (+2,40%)'}; {'C': '72.507,46 (base)', 'principal_contido': '52.779,17', 'juros_contidos': '53.063,00', 'total_31_05_16': '140.485,42', 'delta_vs_base': '0,00'}; {'C': '87.008,95 (+20%)', 'principal_contido': '47.969,36', 'juros_contidos': '57.872,81', 'total_31_05_16': '137.723,35', 'delta_vs_base': '-2.762,07 (-1,97%)'}
- **Ex6:** {'C': '332,60 (-20%)', 'principal_contido': '5.092,34', 'juros_contidos': '144,37', 'total_31_05_16': '5.271,88', 'delta_vs_base': '+0,21 (+0,004%)'}; {'C': '415,75 (base)', 'principal_contido': '5.057,48', 'juros_contidos': '179,23', 'total_31_05_16': '5.271,67', 'delta_vs_base': '0,00'}; {'C': '498,90 (+20%)', 'principal_contido': '5.023,09', 'juros_contidos': '213,62', 'total_31_05_16': '5.271,46', 'delta_vs_base': '-0,21 (-0,004%)'}
- **leitura:** a sensibilidade do TOTAL ao recálculo de C é ~600x maior no Ex.5 (2,4%) que no Ex.6 (0,004%), pelo produto participação-dos-juros x tempo-residual. O atrito da Fase 4 é praticamente todo concentrado em créditos antigos com juros pesados.
- **atrito adicional especifico do segmento D:** no Ex.6 o recálculo por ADC 58 atinge também o conceito de 'juros vincendos': sob SELIC pós-citação não há separação principal/juros, e a linha 'Juros vincendos 251,02' do demonstrativo homologado perde referente. O critério alternativo 1/2/3 da letra C, que existe para preservar esses vincendos, torna-se inaplicável.


## 10. Aritmética

### Exemplo 5

- **B principal atualizado:** conta: 71.026,35 x 1,0153923; calculado: 72.119,61; impresso: 72.119,61; status: OK
- **C1 juros pretéritos corrigidos:** conta: 60.162,49 x 1,0153923; calculado: 61.088,53; impresso: 61.088,53; status: OK
- **C2 juros novos:** conta: 72.119,61 x 0,15833330; calculado: 11.418,94; impresso: 11.418,94; status: OK
- **C total:** conta: 61.088,53 + 11.418,94; calculado: 72.507,47; impresso_letra_C: 72.507,47; impresso_letras_F_G_e_p270: 72.507,46; status: INCONSISTENTE 0,01
- **D bruto:** impresso: 144.627,07; status: só fecha com C = 72.507,46; com 72.507,47 daria 144.627,08
- **gross up:** conta: (28.843,00 - 723,95) / 0,725; calculado: 38.784,90; impresso: 38.784,90; status: OK EXATO
- **IR levantamento:** conta: 38.784,90 x 0,275 - 723,95; calculado: 9.941,8975 -> 9.941,90; impresso: 9.941,90; status: OK
- **verificacao inversa:** conta: 38.784,90 - 0,00 - 9.941,90; calculado: 28.843,00; status: FECHA
- **F saldo:** conta: 144.627,07 - 9.941,90 - 28.843,00; calculado: 105.842,17; impresso: 105.842,17; status: OK
- **G1 principal contido:** conta: 72.119,61 / 144.627,07 x 105.842,17; calculado: 52.779,1699 -> 52.779,17; impresso: 52.779,16; status: delta -0,01 (truncamento)
- **G2 juros contidos:** conta: 72.507,46 / 144.627,07 x 105.842,17; calculado: 53.063,0001 -> 53.063,00; impresso: 53.063,01; status: delta +0,01
- **rateio fecha:** conta: 52.779,16 + 53.063,01; calculado: 105.842,17; status: FECHA (os dois arredondamentos se cancelam)
- **H principal atualizado:** conta: 52.779,16 x 1,04095137; calculado: 54.940,54; impresso: 54.940,54; status: OK
- **I1 juros atualizados:** conta: 53.063,01 x 1,04095137; calculado: 55.236,01; impresso: 53.199,50; status: *** DIVERGE 2.036,51 — BLOQUEIO, ver DEF-01 ***; indice_implicito: 1,00257222
- **I2 juros s principal:** conta: 54.940,54 x 55,166667%; calculado: 30.308,86; impresso: 30.308,86; status: OK
- **J total bruto:** conta_publicada: 54.940,54 + 53.199,50 + 30.308,86 = 138.448,90; status: internamente consistente com o valor errado; valor_coerente: 54.940,54 + 55.236,01 + 30.308,86 = 140.485,41
- **NMP:** conta: 38.784,90 / 144.627,02 x 64; calculado: 17,16303; impresso: 17,2; regra: 1 casa half-up, não declarada; nota: o divisor impresso é 144.627,02, não 144.627,07; com o valor correto o NMP também dá 17,2
- **NM saldo:** conta: 64 - 17,2; calculado: 46,8; impresso: 46,8; status: OK
- **parcela a deduzir x NM:** conta: 354,79725 x 46,8; calculado: 16.604,5113; impresso: 16.604,51; status: OK
- **IR saldo:** conta_com_valor_arredondado: 138.448,90 x 15% - 16.604,51 = 4.162,825 -> 4.162,83; conta_com_valor_pleno: 138.448,90 x 15% - 16.604,5113 = 4.162,8237 -> 4.162,82; impresso: 4.162,83; status: só fecha com o intermediário arredondado
- **liquido:** conta: 138.448,90 - 4.162,83; calculado: 134.286,07; impresso: 134.286,07; status: OK
- **IR atrasado juros:** conta: 9.941,90 x 45,22%; calculado: 4.495,7273 -> 4.495,73; impresso: 4.495,72; status: delta -0,01
- **IR atrasado multa:** conta: 9.941,90 x 20%; calculado: 1.988,38; impresso: 1.988,38; status: OK
- **IR atrasado total:** conta: 9.941,90 + 4.495,72 + 1.988,38; calculado: 16.426,00; impresso: 16.426,00; status: OK com o valor errado do juros
- **resumo geral:** conta: 134.286,07 + 0,00 + 0,00 + 16.426,00 + 4.162,83; calculado: 154.874,90; impresso: 154.874,90; status: OK

### Exemplo 6

**B principal atualizado**

- **conta:** 11.708,40 x 1,00196157
- **calculado:** 11.731,3676 -> 11.731,37
- **impresso letra B e p276:** 11.731,57
- **impresso pp273 274 276:** 11.731,37
- **status:** DOIS VALORES DIFERENTES NO MESMO EXEMPLO; o correto é 11.731,37 e é ele que faz o resto fechar

- **C1 vincendos corrigidos:** conta: 251,02 x 1,00196157; calculado: 251,5124 -> 251,51; impresso: 251,51; status: OK; defeito_de_coluna: a coluna Vr. Base imprime 11.708,40 em vez de 251,02
- **C2 juros novos:** conta_declarada_pela_coluna: 11.708,40 x 1,40% = 163,92; conta_que_reproduz_o_impresso: 11.731,57 x 1,40% = 164,2420; impresso: 164,24; status: só fecha com o principal CORRIGIDO; a coluna Vr. Base está errada
- **C total:** conta: 251,51 + 164,24; calculado: 415,75; impresso: 415,75; status: OK
- **D bruto:** conta: 11.731,37 + 415,75; calculado: 12.147,12; impresso: 12.147,12; status: OK com 11.731,37
- **INSS atualizado:** conta: 1.254,55 x 1,00196157; calculado: 1.257,01; impresso: 1.257,01; status: OK
- **gross up:** conta: (5.426,00 - 869,36) / (1 - [(11.731,37 - 1.257,01) x (0,275/12.147,12) + 1.257,01/12.147,12]); calculado: 6.910,41; impresso: 6.910,41; status: OK EXATO com 11.731,37; com 11.731,57 daria 6.910,46
- **INSS proporcional:** conta: 6.910,41 / 12.147,12 x 1.257,01; calculado: 715,10; impresso: 715,10; status: OK
- **bruto levantado sem juros:** conta: 6.910,41 x 11.731,37 / 12.147,12; calculado: 6.673,89; impresso: 6.673,89; status: OK com 11.731,37; com 11.731,57 daria 6.674,01
- **base IR levantamento:** conta: 6.673,89 - 715,10; calculado: 5.958,79; impresso: 5.958,79; status: OK
- **IR levantamento:** conta: 5.958,79 x 0,275 - 869,36; calculado: 769,3072 -> 769,31; impresso: 769,31; status: OK
- **verificacao inversa:** conta: 6.910,41 - 715,10 - 769,31; calculado: 5.426,00; status: FECHA EXATO
- **F saldo:** conta: 12.147,12 - 715,10 - 769,31 - 5.426,00; calculado: 5.236,71; impresso: 5.236,71; status: OK
- **G1 principal contido:** conta: 11.731,37 / 12.147,12 x 5.236,71; calculado: 5.057,4798 -> 5.057,48; impresso: 5.057,47; status: delta -0,01 (truncamento)
- **G2 juros contidos:** conta: 415,75 / 12.147,12 x 5.236,71; calculado: 179,23; impresso: 179,23; status: OK
- **rateio fecha:** conta: 5.057,47 + 179,23 = 5.236,70; saldo: 5.236,71; status: NÃO FECHA, delta -0,01
- **H principal atualizado:** conta: 5.057,47 x 1,00087571; calculado: 5.061,90; impresso: 5.061,90; status: OK
- **I1 juros atualizados:** conta: 179,23 x 1,00087571; calculado: 179,39; impresso: 179,39; status: OK
- **I2 juros s principal:** conta: 5.061,90 x 0,600000%; calculado: 30,3714 -> 30,37; impresso: 30,37; status: OK
- **J total bruto:** conta: 5.061,90 + 179,39 + 30,37; calculado: 5.271,66; impresso: 5.271,66; status: OK
- **K INSS saldo:** conta: (1.257,01 - 715,10) = 541,91 x 1,00087571; calculado: 542,38; impresso: 542,38; status: OK
- **L base IR saldo:** conta: 5.061,90 x 100% - 542,38; calculado: 4.519,52; impresso: 4.519,52; status: OK
- **L IR saldo:** conta: 4.519,52 x 0,225 - 636,13; calculado: 380,762 -> 380,76; impresso_letra_L: 380,76; impresso_letras_M_N_e_resumo: 380,77; status: INCONSISTENTE 0,01; o valor aritmeticamente correto é 380,76 e é o MINORITÁRIO
- **M liquido:** conta: 5.271,66 - 542,38 - 380,77; calculado: 4.348,51; impresso: 4.348,51; status: OK com 380,77
- **O INSS juros:** conta_declarada: 1.250,00 x 1,06% = 13,25 + 5,50 = 18,75; impresso: 18,75; status: OK — o rótulo da coluna explicita '+ valor juros apurados até mar/16', logo 13,25 + 5,50
- **O INSS multa:** conta: 0,33% x 31 dias = 10,23%; 1.250,00 x 10,23%; calculado: 127,875 -> 127,88; impresso: 127,88; status: OK
- **O INSS total:** conta: 1.250,00 + 18,75 + 127,88; calculado: 1.396,63; impresso: 1.396,63; status: OK
- **resumo geral:** conta: 4.348,51 + 1.396,63 + 769,31 + 380,77; calculado: 6.895,22; impresso: 6.895,22; status: OK

## 11. Notas e rótulos conferidos contra a conta que a coluna faz

11 conferidos.

| # | Ex. | `pagina_pdf` | Rótulo impresso | Conta real | Veredicto |
|---|---|---|---|---|---|
| NR-01 | Ex.5 | 267 | % parcelas passíveis de IR  (131.299,84 / 131.188,84) | 131.188,84 / 131.188,84 = 100% | o numerador do rótulo (131.299,84) é erro de digitação de 131.188,8… |
| NR-02 | Ex.5 | 267 | % parcelas passíveis de IR  (50.799,50 / 55.881,51) | 50.799,50 / 55.881,51 = 90,905%, não 100% | rótulo COPIADO DO EXEMPLO 1. Os dois operandos aparecem nas pp.242-… |
| NR-03 | Ex.5 | 269 | Parcela a deduzir multiplicada pelo número de meses proporcional ao valor lev… | 46,8 é o número de meses do SALDO REMANESCENTE; o proporcional ao valor levan… | rótulo descreve a coluna errada. O número usado está certo. |
| NR-04 | Ex.6 | 272 | Valor dos juros apurado no último cálculo corrigido até a data da amortização… |  | a coluna Vr. Base contradiz o próprio rótulo. O rótulo está certo (… |
| NR-05 | Ex.6 | 272 | Juros s/ o principal corrigido entre o último cálculo e a data da amortização |  | rótulo diz 'principal CORRIGIDO' mas a coluna imprime o principal O… |
| NR-06 | Ex.5 | 269 | Total bruto devido ao reclamante 144.627,02 | 144.627,07 em todas as demais 4 ocorrências (pp.267, 268, 270) | transposição de dígito na tabela de apuração do NM. Não altera o NM… |
| NR-07 | Ex.6 | 274 | incidir juros do período restante ... sobre o valor do principal corrigido en… |  | não existe 'item 10' no Exemplo 6. A referência correta é a letra H… |
| NR-08 | Ex.5 | 268 | VR. BRUTO LEVANTADO = (TL - PD) / 1 – [(TB x IPIR – INSS)  x  (ALIQ. / TB)  +… |  | duas falhas tipográficas: 'NSS' por 'INSS'; e ausência de parêntese… |
| NR-09 | Ex.5 | 268 | deduzindo do valor encontrado o INSS proporcional apurado no item “c” |  | não há item 'c' no Exemplo 5 (não há INSS algum; INSS = 0,00). Refe… |
| NR-10 | Ex.6 | 275 | 1o) aplicar o índice das parcelas passíveis de IR em relação ao saldo remanes… | o índice não foi aplicado sobre o 'saldo remanescente atualizado' (5.271,66)… | o texto da moldura (10.3.2, letra L, hipótese 12-B) foi copiado sem… |
| NR-11 | Ex.5 | 270 | Base imposto de renda s/ o valor levantado ... 100,00%  38.784,90 |  | cabeçalho deslocado: '100,00%' ocupa a coluna 'Índice' e '38.784,90… |

## 12. Defeitos do original

14 catalogados. Nenhum corrigido.

### DEF-01 — BLOQUEIO

- **Exemplo:** Ex.5
- **Letra:** I
- **`pagina_pdf`:** 269; 271
- **Linha:** Vr. Juros atualiz.  \| 26/10/11 \| 31/05/16 \| 53.063,01 \| 1,04095137 \| 53.199,50
- **O que não fecha:** 53.063,01 x 1,04095137 = 55.236,0055 -> 55.236,01. Impresso 53.199,50. Delta 2.036,51.
- **Índice implícito:** 53.199,50 / 53.063,01 = 1,00257222 — não corresponde a nenhum índice declarado no exemplo (os únicos são 1,0153923 e 1,04095137).
- **Por que é bloqueio:** delta de 2.036,51 não é absorvível por arredondamento, não é transposição de dígito e não decorre de nenhuma operação demonstrada. O valor 53.199,50 aparece SÓ nas pp.269 e 271, ambas do Exemplo 5, logo não é resíduo copiado de outro exemplo identificável.
- **Ação:** NÃO contornado. Registrado como bloqueio. Todo o desfecho do Exemplo 5 é produto deste desvio.

### DEF-02 — inconsistência interna

- **Exemplo:** Ex.5
- **`pagina_pdf`:** 267; 268; 270

### DEF-03 — inconsistência interna

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 272; 273; 274; 276

### DEF-04 — linha copiada de outro exemplo

- **Exemplo:** Ex.5
- **`pagina_pdf`:** 267

### DEF-05 — sequência de letras corrompida

- **Exemplo:** Ex.5
- **`pagina_pdf`:** 267; 268

### DEF-06 — letra faltante

- **Exemplo:** Ex.5
- **`pagina_pdf`:** 270

### DEF-07 — arredondamento inconsistente

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 274; 275; 276; 277

### DEF-08 — arredondamento inconsistente

- **Exemplo:** Ex.5
- **`pagina_pdf`:** 270

### DEF-09 — título contradiz o próprio conteúdo

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 271

### DEF-10 — rótulo tecnicamente duvidoso

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 271

### DEF-11 — campo em branco

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 276

### DEF-12 — erro de citação normativa

- **Exemplo:** Ex.5
- **`pagina_pdf`:** 269

### DEF-13 — parâmetro contradiz o cálculo

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 271

### DEF-14 — rateio não fecha

- **Exemplo:** Ex.6
- **`pagina_pdf`:** 274

## 13. Pendências

| # | Classe | Refere | Descrição | Ação |
|---|---|---|---|---|
| P10D-01 | BLOQUEIO | DEF-01 | 53.199,50 na letra I do Exemplo 5, contra 55.236,01 derivável. Delta 2.036,51, não absorvível, sem regra derivável, propagando até o total do cálculo. | não contornado; o Exemplo 5 não pode ser usado como caso-teste de referência sem esta r… |
| P10D-02 | regra oculta |  | arredondamento do NMP a 1 casa half-up (17,16303 -> 17,2) segue não declarado, e no segmento D nem a nota '( * ) Observada a regra de arredondamento' está presente (busca 'ar… |  |
| P10D-03 | regra oculta |  | no Exemplo 5 o IR do saldo (4.162,83) só fecha se a parcela a deduzir multiplicada pelo NM for ARREDONDADA a 2 casas antes de subtrair (16.604,51); com o valor pleno (16.604,… |  |
| P10D-04 | regra sem exemplo |  | a obrigatoriedade do critério alternativo da letra C quando há juros vincendos é declarada duas vezes (pp.237 e 239) e nunca demonstrada. Os Exemplos 5 e 6, únicos que execut… |  |
| P10D-05 | regra sem exemplo |  | a alternativa da letra I da moldura de 10.3.2 ('aplicar os juros integrais desde o ajuizamento sobre o crédito atualizado apurado na letra G', adequada só quando não há vince… |  |
| P10D-06 | divergência doutrinária não resol… |  | OJ 400 (juros fora da base do IR) x inclusão dos juros. O segmento D instancia as duas teses em exemplos vizinhos, com títulos idênticos e parâmetros opostos, sem enunciar cr… |  |
| P10D-07 | Fase 4 / ADC 58 |  | o Exemplo 5 é o caso de maior exposição do capítulo 10 ao recálculo por ADC 58 (juros = 50,13% do bruto rateado; sensibilidade do total de 2,40% para cada 20% de variação em… |  |
| P10D-08 | conceitual |  | os juros vincendos são incluídos no bruto ANTES do rateio, de modo que uma fração deles é tratada como quitada pelo pagamento (Ex.6: 236,52 de 415,75, ou 56,89%), embora seja… |  |

## 14. Buscas que sustentam as afirmações negativas

Nenhuma negativa deste bloco é opinião.

| Termo | Escopo | Ocorrências | Nota |
|---|---|---|---|
| `obrigatório / obrigator*` | pp.266-277 | 0 | a palavra só existe na moldura, pp.237 e 239 |
| `porque` | pp.266-277 | 0 |  |
| `razão / razao` | pp.266-277 | 0 |  |
| `anatocismo` | pp.266-277 | 0 | no manual inteiro: pp.16, 90, 328, 335 |
| `Súmula 121` | pp.266-277 | 0 | no manual inteiro: só p.16, e só para a regra de acumulação por soma |
| `Súmula (qualquer)` | pp.266-277 | 0 |  |
| `ADC` | pp.266-277 | 0 |  |
| `IPCA` | pp.266-277 | 0 | no manual inteiro: pp.6, 15, 16, 84, 102, 104, 282, 330, 332, 368 |
| `EC 113 / emenda` | pp.266-277 | 0 |  |
| `12-B` | pp.266-277 | 0 | no manual inteiro: pp.6, 185, 186, 190, 191, 193, 203, 207, 224, 233, 240. O segmento D aplica o regime por paráfrase,… |
| `art. 354 / Código Civil` | pp.266-277 | 0 | a ordem de imputação nunca é fundamentada em norma no capítulo 10 |
| `taxa referencial / TR` | pp.266-277 | 0 | os índices são apresentados só como 'Índ. AM' / 'índice de atualização' |
| `arredond*` | pp.266-277 | 0 | a nota '( * ) Observada a regra de arredondamento' das pp.243/250/257 NÃO reaparece |
| `heading numerado ^1[01]\.\d` | pp.266-278 | 18 matches, todos valores monetários; 0 headings reais | confirma que Ex.5 e Ex.6 permanecem em 10.3.2.1 |
| `12-A` | pp.266-277 | 4 | busca POSITIVA registrada para contraste: p.266 (parâmetros Ex.5, 'não se enquadram no art. 12-A'), p.269 (justificativ… |
| `vincend*` | pp.266-277 | 5 | busca POSITIVA registrada: pp.267, 269, 271, 272, 274 |
| `Selic` | pp.266-277 | 12 | busca POSITIVA registrada: todas referentes a acréscimos moratórios de tributos, nunca a correção do crédito trabalhista |

