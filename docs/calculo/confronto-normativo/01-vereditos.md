# Vereditos — confronto normativo

**Tarefa 2 do bloco 14.** Cada ponto do inventário recebe **exatamente um** veredito,
com fonte, tipo de fonte e grau de confiança.

Inventário em `00-inventario.md`. Efeito sobre os arquivos de extração em
`02-efeito-extracao.md`. Suspeitas sobre a base em `03-suspeitas-base.md`.

**Data da auditoria: 19 e 20 de setembro de 2026.**

---

## 1. O resultado

| Veredito | Nº |
|---|---|
| `VIGENTE` | **9** |
| `BIFURCADO` | **32** |
| `SUPERADO` | **8** |
| `INAPLICÁVEL` | **1** |
| `SEM FONTE` | **0** |
| **total** | **50** |

### 1.1 O número que governa a Fase 5

**32 de 50 pontos são `BIFURCADO`** — as duas versões valem,
em períodos distintos.

Isso não é acidente da amostra: é **a forma como o direito do trabalho brasileiro mudou**
entre 2016 e 2026. Nem a Reforma, nem a ADC 58, nem a Resolução 225/2025 do TST revogaram
com efeito *ex nunc*. Todas cortaram no tempo.

> **Consequência de arquitetura:** o motor não pode ter *uma* tabela de regras vigentes.
> Tem de ter **cadeia temporal por ponto**, como já tem para índices. Um `SUPERADO` mal
> lido apaga o período anterior ao corte — e a maioria das contas do produto atravessa o
> corte.

---

## A. Jurisprudência — OJ 394, Súmulas 228, 437 e 90, intervalo e *in itinere*

### F4-01 — `BIFURCADO`

**OJ 394 da SDI-1 — reflexo do RSR majorado por horas extras habituais em férias, 13º, aviso prévio e FGTS. Manual TRT-3, pp. 35, 44, 45, 48, 286 e 291 (extraído como REGRA pelo bloco 03).**

| Norma nova | OJ 394 da SBDI-1 do TST, nova redação (itens I e II), aprovada no julgamento do IncJulgRREmbRep-10169-57.2013.5.05.0024 — Tema Repetitivo 9, Tribunal Pleno do TST, Rel. Min. Amaury Rodrigues Pinto Ju… |
|---|---|
| **Data de corte** | 20/03/2023 |
| **Eixo do corte** | DATA EM QUE A HORA EXTRA FOI TRABALHADA (competência do fato gerador). NÃO é a data do ajuizamento, nem a do julgamento… |

> **Modulação, literal:** OJ 394, item II (redação vigente): "O item I será aplicado às horas extras trabalhadas a partir de 20.03.2023." — Reproduzido literalmente em acórdão hospedado na base de jurisprudência do próprio TST, na forma: "O item 1 será aplicado às horas extras trabalhadas a partir de 20.03.2023". Item I (redação vigente): "A majoração do valor do repouso semanal remunerado, decorrente da integração das horas extras habituais, deve repercutir no cálculo, efetuado pelo empregador, das demais parcelas que têm como base de cálculo o salário, não se cogitando de bis in idem por sua incidência no cálculo das férias, da gratificação natalina, do aviso prévio e do FGTS." Tese firmada do Tema 9 (ficha oficia…

A resposta ao quesito do enunciado é BIFURCADO, não SUPERADO, e a razão é exatamente a modulação. O Tribunal Pleno reverteu o mérito — o bis in idem deixou de ser reconhecido — mas condicionou a nova tese às horas extras trabalhadas a partir de 20/03/2023. Para todo o passivo anterior, a OJ 394 na redação de 2010 continua sendo a norma aplicável, e o conteúdo que o bloco 03 extraiu do manual TRT-3 permanece CORRETO para esse intervalo. Chamar o ponto de 'superado' apagaria o regime que governa a maior parte do passivo de um contrato antigo. Registro ainda que a ficha oficial do Tema 9 do TST transcreve apenas o mérito (equivalente ao item I) e NÃO reproduz a modulação; quem consultar só a ficha do tema conclui erradamente que a regra nova vale para tudo. A modulação está no item II do verbete e no acórdão. Nota adicional: a OJ 394 NÃO consta do rol de cancelamentos da Res. 225/2025 do T…

— *TST, ficha oficial do Tema Repetitivo 9 — https://www.tst.jus.br/documents/10157/0/IRR009.pdf (tese firmada, relator, órgão, datas de julgamento 20/3/2023, publicação 31/3/2023 e trânsito em julgado…* · **primária** · confiança **alta**

### F4-02 — `SUPERADO`

**Súmula 228 do TST — base de cálculo do adicional de insalubridade. Manual TRT-3 p. 337 (imprime 'SÚMULA CUJA EFICÁCIA ESTÁ SUSPENSA POR DECISÃO LIMINAR DO SUPREMO TRIBUNAL FEDERAL — Res. 168/12') e p. 59 (comentário à Rcl 6.266).**

| Norma nova | A Súmula 228 do TST foi CANCELADA INTEGRALMENTE pela Resolução 225/2025 do TST (Pleno, 30/06/2025, DEJT caderno administrativo n. 4253, p. 2-3). A base de cálculo hoje é a do art. 192 da CLT — salári… |
|---|---|
| **Data de corte** | 18/04/2018 (perda de eficácia da Súmula 228, conforme art. 1º, VI, da Res. 225/2025); 30/06/2025 (cancelamento formal d… |
| **Eixo do corte** | Data da publicação da decisão do STF na reclamação. Não é eixo de cálculo: a súmula nunca chegou a produzir efeito prát… |

> **Modulação, literal:** Res. 225/2025, art. 1º, VI: "Súmula nº 228 (cancelada por perda de eficácia considerando a decisão da Rcl 6266, a partir da publicação em 18/04/2018)". Súmula Vinculante 4 do STF: "Salvo nos casos previstos na Constituição, o salário mínimo não pode ser usado como indexador de base de cálculo de vantagem de servidor público ou de empregado, nem ser substituído por decisão judicial."

O manual está duplamente defasado. (1) A qualificação 'suspensa por liminar' deixou de ser exata em 18/04/2018, com a cassação definitiva; (2) desde 30/06/2025 o verbete sequer existe. VERIFICAÇÃO SOLICITADA, RESULTADO: a base do projeto acertou o mérito (salário mínimo) e acertou a Rcl 6.275 como a decisão que cassou — a notícia oficial do STF confirma que a Rcl 6.275, da Unimed Ribeirão Preto, Rel. Min. Lewandowski, tornou definitiva a exclusão suspensa desde 2008 pela liminar da Rcl 6.266 (Min. Gilmar Mendes). Mas a base errou ao não registrar o cancelamento formal de 2025, e há uma DIVERGÊNCIA DE ATRIBUIÇÃO que registro sem resolver: a Res. 225/2025 do TST atribui a perda de eficácia à 'Rcl 6266' com data de publicação 18/04/2018, ao passo que a notícia do STF atribui à Rcl 6.275 a decisão publicada em 18/04/2018, sendo a Rcl 6.266 a liminar de 2008. A data confere com a Rcl 6.275;…

— *TST, Resolução 225/2025, inteiro teor — https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf (art. 1º, VI); STF, Súmula Vinculante 4 — https://portal.stf.jus.br/jurispr…* · **primária para o cancelamento (Res. 225/2025) e para a SV 4; secundária para a Rcl 6.275 (notícia oficial STF/TST, inteiro teor não lido) e para a Rcl 53.157 (inteiro teor não obtido — PDF retornou 0 bytes e o portal do STF retornou 403)** · confiança **alta para o cancelamento e para a base ser o salário mínimo; MÉDIA para a Rcl 6.275 (sem inteiro teor); BAIXA para a Rcl 53.157 (sem inteiro teor, decisão de Turma inter partes)**

### F4-03 — `BIFURCADO`

**Intervalo intrajornada — art. 71, § 4º, da CLT: duas mudanças simultâneas pela Lei 13.467/2017 (extensão: integral → apenas o suprimido; natureza: salarial → indenizatória) e estado atual da Súmula 437, I, do TST.**

| Norma nova | Art. 71, § 4º, da CLT na redação da Lei 13.467/2017, vigente desde 11/11/2017 (Lei publicada no DOU de 14/07/2017; art. 6º: vigência após 120 dias). A Súmula 437 do TST, inteira, foi CANCELADA pela R… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | DATA DO FATO GERADOR da parcela — isto é, a data em que o intervalo foi suprimido —, e não a data de admissão nem a dat… |

> **Modulação, literal:** NÃO HÁ MODULAÇÃO — e a recusa é expressa. TST, ED-IncJulgRREmbRep-528-80.2018.5.14.0004 (Tema 23), Pleno, j. 20/05/2025, embargos rejeitados por unanimidade, com o seguinte fundamento literal: "discutiu-se no presente incidente a aplicação do direito no tempo em relação aos contratos de emprego em curso quando da alteração imposta pela Lei nº 13.467/2017. Portanto, a hipótese é de superveniência de lei nova, e não de alteração de jurisprudência dominante do Supremo Tribunal Federal ou dos tribunais superiores, hipótese que, em tese, poderia resultar na necessidade de modulação dos efeitos do v. acórdão embargado, nos termos do § 3º do art. 927 do CPC. Ademais, sequer há falar em insegurança…

AS DUAS REDAÇÕES, LITERAIS, conferidas no Planalto. (a) Redação da Lei 8.923/1994, aplicável até 10/11/2017: a não concessão implicava o pagamento do período integral, com natureza salarial por força da Súmula 437, I e III. (b) Redação da Lei 13.467/2017, aplicável a partir de 11/11/2017: "A não concessão ou a concessão parcial do intervalo intrajornada mínimo, para repouso e alimentação, a empregados urbanos e rurais, implica o pagamento, de natureza indenizatória, apenas do período suprimido, com acréscimo de 50% (cinquenta por cento) sobre o valor da remuneração da hora normal de trabalho." CONFIRMADO: a Reforma muda DUAS coisas simultaneamente — extensão e natureza —, e o bloco 04 estava certo; capturar só a natureza perde metade do efeito no cálculo, porque a mudança de extensão é tipicamente a de maior impacto monetário (de 60 min para os 15 min suprimidos, por exemplo). ESTADO AT…

— *Planalto, Lei 13.467/2017, texto oficial — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm (redação dada ao art. 71, § 4º; art. 6º: 'Esta Lei entra em vigor após decorridos ce…* · **primária** · confiança **alta**

### F4-04 — `BIFURCADO`

**Horas in itinere — art. 58, § 2º, da CLT. O que rege contratos anteriores à Reforma.**

| Norma nova | Art. 58, § 2º, da CLT na redação da Lei 13.467/2017, vigente desde 11/11/2017. ATENÇÃO — CORREÇÃO DE FATO: o § 2º NÃO foi revogado; teve a REDAÇÃO ALTERADA. Quem a Lei 13.467/2017 revogou foi o § 3º… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | DATA DO FATO GERADOR — o dia do deslocamento. Não é a data de admissão. Tese vinculante do Tema 23 do TST, aplicada pel… |

> **Modulação, literal:** NÃO HÁ MODULAÇÃO, recusada expressamente nos embargos do Tema 23 (transcrição literal no verdito F4-03). Tese do Tema 23: "A Lei nº 13.467/2017 possui aplicação imediata aos contratos de trabalho em curso, passando a regular os direitos decorrentes de lei cujos fatos geradores tenham se efetivado a partir de sua vigência". Dispositivo do acórdão, item II, literal: "limitar a condenação ao pagamento de horas 'in itinere' a 10/11/2017, antes da vigência da Lei nº 13.467/2017". Res. 225/2025, art. 1º, II: "Súmula nº 90 (cancelada por perda de eficácia a partir de 11/11/2017, pela Lei 13.467/2017)"; art. 1º, XII: mesma fórmula para a Súmula nº 320; art. 1º, XXI: mesma fórmula para a Súmula nº 4…

Respondendo diretamente ao quesito: é BIFURCADO, com corte em 11/11/2017 pelo eixo da data do deslocamento. Não é SUPERADO puro, e o caso líder do Tema 23 é a prova mais forte disso — o Pleno do TST, no mesmo acórdão em que fixou a tese que favorece o empregador, MANTEVE a condenação em horas in itinere até 10/11/2017. Para fatos até essa data aplica-se a redação anterior do art. 58, § 2º e a Súmula 90 do TST. Para fatos a partir de 11/11/2017, o tempo de deslocamento não é computado na jornada, ainda que o transporte seja fornecido pelo empregador e ainda que o local seja de difícil acesso. Redação literal vigente, conferida no Planalto: "O tempo despendido pelo empregado desde a sua residência até a efetiva ocupação do posto de trabalho e para o seu retorno, caminhando ou por qualquer meio de transporte, inclusive o fornecido pelo empregador, não será computado na jornada de trabalho,…

— *Planalto, Lei 13.467/2017, texto oficial — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm (redação dada ao art. 58, § 2º; '§ 3º (Revogado)'; art. 5º, I, 'a': revogação do § 3…* · **primária** · confiança **alta**

### F4-05 — `BIFURCADO`

**Súmula 437 do TST — verificação item por item (a súmula tem quatro itens). A base registra que APENAS o item III foi superado pelo art. 71, § 4º.**

| Norma nova | Súmula 437 CANCELADA INTEGRALMENTE — todos os quatro itens — pela Res. 225/2025 do TST, art. 1º, XXII, com perda de eficácia declarada a partir de 11/11/2017, pela Lei 13.467/2017. Os itens II e IV t… |
|---|---|
| **Data de corte** | 11/11/2017 para todos os quatro itens; adicionalmente 14/06/2022 (Tema 1046) como marco autônomo para a invalidade de c… |
| **Eixo do corte** | Data do fato gerador (supressão do intervalo), por força do Tema 23 do TST. Para o item II, o eixo autônomo é a data de… |

> **Modulação, literal:** Res. 225/2025, art. 1º, XXII: "Súmula nº 437 (cancelada por perda de eficácia a partir de 11/11/2017, pela Lei 13.467/2017)". Justificativa oficial do TST para o cancelamento: confronto com o "§4º do art. 71 da CLT" e com os "arts. 611-A e 611-B da CLT". Considerando da Res. 225/2025, literal: "as súmulas, orientações jurisprudenciais e precedentes normativos em confronto com a Lei 13.467, de 13 de julho de 2017, perderam a eficácia com a vigência da Reforma Trabalhista (11/11/2017)".

A BASE DO PROJETO ESTÁ INCOMPLETA E EU DIVIRJO DELA. Ela registra a superação de UM item; a verificação mostra a superação dos QUATRO, por duas causas distintas. Item por item, com o texto do verbete conferido: (I) 'Após a edição da Lei nº 8.923/94, a não-concessão ou a concessão parcial do intervalo intrajornada mínimo (...) implica o pagamento total do período correspondente, e não apenas daquele suprimido, com acréscimo de, no mínimo, 50% (...), sem prejuízo do cômputo da efetiva jornada de labor para efeito de remuneração' — SUPERADO pela nova redação do § 4º, que restringe o pagamento 'apenas [ao] período suprimido'. A base NÃO registrava a superação do item I como tal, embora reconhecesse a mudança de extensão; a consequência formal (cancelamento do item) faltava. (II) 'É inválida cláusula de acordo ou convenção coletiva de trabalho contemplando a supressão ou redução do intervalo…

— *TST, Resolução 225/2025, inteiro teor — https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; TST, página oficial 'Cancelamento de Súmulas, OJs e Precedentes Normativos…* · **primária para o cancelamento, a data de corte e a causa; secundária para o texto literal dos itens I a IV do verbete, já removido do repositório ativo do TST** · confiança **alta para o veredito, a data e o eixo; MÉDIA para a literalidade da transcrição dos quatro itens (três fontes secundárias concordantes, sem repositório primário ativo)**

### F4-06 — `BIFURCADO`

**Súmula 90 do TST — estado atual após a alteração do art. 58, § 2º, da CLT.**

| Norma nova | Súmula 90 CANCELADA INTEGRALMENTE pela Res. 225/2025 do TST, art. 1º, II, com perda de eficácia declarada a partir de 11/11/2017, pela Lei 13.467/2017. Canceladas na mesma resolução e pelo mesmo fund… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | Data do fato gerador — o dia do deslocamento —, por força do Tema 23 do TST. A Súmula 90 rege integralmente os deslocam… |

> **Modulação, literal:** Res. 225/2025, art. 1º, II: "Súmula nº 90 (cancelada por perda de eficácia a partir de 11/11/2017, pela Lei 13.467/2017)". Art. 7º: "Esta Resolução entra em vigor na data de sua publicação." Considerando aplicável, literal: "considerando os termos do artigo 177, I, do Regimento Interno do Tribunal Superior do Trabalho e que as súmulas, orientações jurisprudenciais e precedentes normativos em confronto com a Lei 13.467, de 13 de julho de 2017, perderam a eficácia com a vigência da Reforma Trabalhista (11/11/2017)".

A pergunta do ponto 6 — 'estado atual da Súmula 90 após a revogação do dispositivo que lhe dava suporte' — contém duas imprecisões que a verificação corrige. Primeira: o dispositivo não foi revogado, foi alterado (ver F4-04). Segunda, e mais importante: 'estado atual' não é resposta binária. A Súmula 90 foi formalmente cancelada em 30/06/2025, mas o ato de cancelamento é expressamente datado para trás, a 11/11/2017, e o próprio Pleno do TST, no Tema 23, manteve condenação em horas in itinere até 10/11/2017. Logo: a Súmula 90 NÃO é lixo histórico. É a norma que rege o segmento pré-Reforma de qualquer contrato antigo, e o motor precisa dela como variante ativa, não como nota de rodapé. A construção normativa do art. 177, I, do RITST é digna de registro para o projeto: o TST não 'revogou' os verbetes com efeito ex nunc — declarou que eles JÁ haviam perdido eficácia no passado, o que é prec…

— *TST, Resolução 225/2025, inteiro teor — https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; TST, página oficial de cancelamentos — https://www.tst.jus.br/cancelamento…* · **primária** · confiança **alta**

## B. Reforma Trabalhista — blocos 03 e 04

### B03-F1 — `BIFURCADO`

**Base de cálculo integra abonos e prêmios habituais (manual 6.1, p. 18; quadro 6.6.6.5, p. 47)**

| Norma nova | CLT, art. 457, §§ 1º, 2º e 4º, na redação da Lei 13.467/2017. § 1º: 'Integram o salário a importância fixa estipulada, as gratificações legais e as comissões pagas pelo empregador.' § 2º: 'As importâ… |
|---|---|
| **Data de corte** | 11/11/2017 (com subjanela 14/11/2017 a 22/04/2018 sob a MP 808/2017) |
| **Eixo do corte** | competência do fato gerador da parcela (mês de pagamento/competência da verba) — Tema 23 do TST. NÃO é a data de admiss… |

> **Modulação, literal:** Lei 13.467/2017, art. 6º (vigência em 11/11/2017). TST, Res. 225/2025, art. 1º, IV: Súmula 152 (gratificação por ajuste tácito) cancelada 'por perda de eficácia a partir de 11/11/2017'. MP 808/2017, art. 2º, previa aplicação integral aos contratos vigentes — caducou.

A redação anterior do § 1º mandava integrar ao salário 'não só a importância fixa estipulada, como também as comissões, percentagens, gratificações ajustadas, diárias para viagens e abonos pagos pelo empregador'. O texto vigente suprime abonos, percentagens e gratificações ajustadas, e o § 2º exclui prêmios e abonos 'ainda que habituais', afastando-os até como base de incidência previdenciária. O manual de 2016 está correto para fatos até 10/11/2017 e errado para fatos posteriores. A revogação não retroage; logo o contrato se parte. Subjanela MP 808: entre 14/11/2017 e 22/04/2018 'abonos' não figurava na lista de exclusão do § 2º e a gratificação de função integrava o § 1º — o resultado do cálculo muda dentro do próprio período pós-reforma. Verificado no texto compilado da CLT no Planalto que não houve alteração posterior do art. 457 (consulta em 20/09/2026).

— *https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm; https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/20…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** sim

### B03-F2 — `BIFURCADO`

**Habitualidade como teste de integração, com lapso até anual (manual 6.1, p. 18)**

| Norma nova | CLT, art. 457, § 2º (Lei 13.467/2017): exclui as parcelas ali listadas 'ainda que habituais'. |
|---|---|
| **Data de corte** | 11/11/2017 (com subjanela 14/11/2017 a 22/04/2018 sob a MP 808/2017) |
| **Eixo do corte** | competência do fato gerador da parcela — Tema 23 do TST |

> **Modulação, literal:** Lei 13.467/2017, art. 6º. TST, Res. 225/2025, art. 1º, IV (Súmula 152, gratificação ajustada por ajuste tácito, perda de eficácia a partir de 11/11/2017).

A expressão 'ainda que habituais' do § 2º é exatamente a negação do teste do manual: para ajuda de custo, auxílio-alimentação, diárias, prêmios e abonos, a habitualidade deixou de ser critério de integração. O teste da habitualidade NÃO foi abolido em geral — continua governando horas extras, adicionais e demais parcelas de natureza salarial (Súmula 264 do TST, não cancelada) —, apenas foi afastado por lei para o rol do § 2º. Por isso o veredito é bifurcação de escopo e de tempo, não supressão do critério. Busca negativa declarada: nenhuma alteração do art. 457 posterior à Lei 13.467 no texto compilado do Planalto; a Súmula 264 não consta do rol de cancelamentos da Res. 225/2025.

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** sim

### B03-F3 — `BIFURCADO`

**12×36: feriado laborado pago em dobro, com dois critérios divergentes transcritos do TRT-3 (manual 6.5, pp. 34–35; pendência P11)**

| Norma nova | CLT, art. 59-A, parágrafo único (Lei 13.467/2017): 'A remuneração mensal pactuada pelo horário previsto no caput deste artigo abrange os pagamentos devidos pelo descanso semanal remunerado e pelo des… |
|---|---|
| **Data de corte** | 11/11/2017 (com subjanela 14/11/2017 a 22/04/2018: sob a MP 808 a 12×36 só era válida por norma coletiva, salvo setor d… |
| **Eixo do corte** | competência do fato gerador — o feriado efetivamente laborado. Secundariamente, a data e a forma do ajuste (individual… |

> **Modulação, literal:** TST, Res. 225/2025, art. 1º, XXIV: 'Súmula nº 444 (cancelada por perda de eficácia a partir de 11/11/2017, pela Lei 13.467/2017)'. A data está no texto da resolução — é a modulação mais explícita de todo este lote.

A Súmula 444 assegurava a remuneração em dobro dos feriados trabalhados na 12×36 e exigia norma coletiva. Foi cancelada pelo Pleno do TST em 30/06/2025, com perda de eficácia declarada a partir de 11/11/2017 — ou seja, continua regendo os feriados laborados até 10/11/2017, e é isso que preserva a divergência de critérios que o manual transcreve sem arbitrar (P11). Para feriados a partir de 11/11/2017 o parágrafo único do art. 59-A resolve a questão no plano legal: a remuneração mensal pactuada já abrange RSR e feriados. O STF, na ADI 5994 (Pleno, j. 30/06/2023), manteve o art. 59-A, inclusive quanto ao acordo individual escrito. Ressalvas que o motor precisa suportar: (a) o parágrafo único pressupõe regime 12×36 validamente pactuado — escala irregular ou não cumprida na prática reabre a dobra; (b) norma coletiva pode fixar pagamento superior (Tema 1046 do STF valida a cláusula). Busca n…

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; https://www.planalto.gov.br/ccivil_03/_ato…* · **primaria-lei-planalto + primaria-tribunal (Res. 225/2025) + secundaria (ADI 5994)** · confiança **alto para o corte de 11/11/2017 e o cancelamento da Súmula 444; medio para os dados da ADI 5994**

**Sensível ao intertemporal:** sim

### B03-F4 — `BIFURCADO`

**Súmula 85 e compensação de jornada (manual 6.6.1, p. 36; 6.6.5, p. 40)**

| Norma nova | CLT, art. 59-B (Lei 13.467/2017), caput e parágrafo único: 'O não atendimento das exigências legais para compensação de jornada, inclusive quando estabelecida mediante acordo tácito, não implica a re… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | competência do fato gerador — as horas prestadas/compensadas. Para o item VI da Súmula 85, há eixo concorrente: a data… |

> **Modulação, literal:** Não há modulação expressa: a Súmula 85 NÃO foi cancelada pela Res. 225/2025. O corte decorre apenas da vigência do art. 59-B.

O caput do art. 59-B positivou o item V da Súmula 85 (só o adicional é devido). O parágrafo único, porém, contradiz frontalmente o item IV, que dizia que a prestação de horas extras habituais descaracteriza o acordo de compensação. Achado relevante: o TST cancelou 36 enunciados em 30/06/2025 e NÃO incluiu a Súmula 85 — ela permanece formalmente vigente e em confronto parcial com a lei para fatos posteriores a 11/11/2017, e ainda mantém o item VI (nulidade de compensação em atividade insalubre sem licença prévia), que colide com o art. 60, parágrafo único, para a 12×36 e com o Tema 1046 do STF. Não resolvo: registro que o motor precisa das duas leituras. Busca negativa declarada: percorri o texto integral da Res. 225/2025 e a página oficial 'Cancelamento de Súmulas, OJs e Precedentes Normativos' do TST (20/09/2026) — a Súmula 85 não aparece em nenhuma das duas, nem localizei resolução po…

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; https://www.tst.jus.br/en/cancelamento-de-…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** sim

### B03-F5 — `BIFURCADO`

**Minutos residuais e Súmula 366 (manual 6.6.5, p. 40)**

| Norma nova | CLT, art. 4º, § 2º (Lei 13.467/2017): 'Por não se considerar tempo à disposição do empregador, não será computado como período extraordinário o que exceder a jornada normal, ainda que ultrapasse o li… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | competência do fato gerador — o dia trabalhado com registro de minutos residuais |

> **Modulação, literal:** TST, Res. 225/2025, art. 1º, XV: 'Súmula nº 366 (cancelada por perda de eficácia a partir de 11/11/2017, pela Lei 13.467/2017)'; art. 1º, XXV: Súmula 449 (minutos residuais e norma coletiva) cancelada com a mesma data de perda de eficácia.

O manual descreve corretamente o estado de 2016: art. 58, § 1º mais Súmula 366 (ultrapassado o limite, computa-se a totalidade do período como extraordinário). O art. 58, § 1º NÃO foi alterado — o que mudou foi o entorno: o art. 4º, § 2º criou hipóteses em que o excedente não é tempo à disposição, e o TST cancelou as Súmulas 366 e 449 com perda de eficácia declarada a partir de 11/11/2017. Consequência dupla: (a) para fatos até 10/11/2017 a regra do manual permanece íntegra, inclusive contra cláusula coletiva elastecedora (Súmula 449, também só cancelada a partir daquela data); (b) para fatos posteriores, a contagem depende de qualificar a causa da permanência, o que é matéria de prova e não de cálculo — entra no motor como atributo do período, não como fórmula. Registro que o cancelamento da Súmula 449, somado ao Tema 1046, reabre a validade de cláusula coletiva sobre minutos residuais…

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** sim

### B03-F6 — `VIGENTE`

**Gorjetas — Súmula 354 e a vedação de reflexos em aviso-prévio, adicional noturno, horas extras e RSR (manual 6.6.6.5, p. 48)**

> **Modulação, literal:** Nenhuma. A Súmula 354 não consta do rol de cancelamentos da Res. 225/2025 nem da página oficial de cancelamentos do TST.

Duas confirmações e um achado. Confirmações: (1) a atribuição do § 3º à Lei 13.419/2017 está correta — o texto compilado da CLT no Planalto marca expressamente '(Redação dada pela Lei nº 13.419, de 2017)'; (2) a Súmula 354 segue vigente, logo a vedação de reflexos que o manual aplica não foi superada. Achado: os §§ 4º a 11 que a Lei 13.419 acrescentara ao art. 457 (rateio, percentuais de retenção de 20%/33%, anotação em CTPS, incorporação pela média de doze meses após cessação da cobrança, comissão de empregados, multa de 1/30) NÃO constam do texto compilado vigente — a Lei 13.467 deu nova redação ao § 4º (prêmios) e o art. 457 hoje tem apenas quatro parágrafos. Ou seja, a parte operacional da Lei das Gorjetas foi revogada, e o que sobreviveu dela é exatamente o conceito do § 3º. A MP 808 reinstituiu esse bloco como §§ 12 a 21 entre 14/11/2017 e 22/04/2018, e ele caiu de novo com a cadu…

— *https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13419.htm; https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/20…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** não (quanto à Súmula 354 e à vedação de reflexos); sim quanto ao regramento de rateio dos §§ 4º a 11 da Lei 13.419

### B03-F7 — `BIFURCADO`

**Férias: regime de concessão e período único (manual 6.4, pp. 25–27)**

| Norma nova | CLT, art. 134, § 1º (Lei 13.467/2017): 'Desde que haja concordância do empregado, as férias poderão ser usufruídas em até três períodos, sendo que um deles não poderá ser inferior a quatorze dias cor… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | competência do fato gerador — a concessão/gozo das férias (e, para a dobra do art. 137, o vencimento do período concess… |

> **Modulação, literal:** Lei 13.467/2017, art. 6º e art. 5º, I, 'f' (revogação do § 2º do art. 134). Correlato com modulação própria: TST, Res. 225/2025, art. 1º, XXVI — Súmula 450 cancelada 'por perda de eficácia considerando a decisão da ADPF 501, a partir da publicação da ata de julgamento em 15/08/2022'.

Confirmado no compilado do Planalto que o art. 134 não sofreu alteração após 2017. O fracionamento passou de excepcional (dois períodos em casos excepcionais, vedado a menores de 18 e maiores de 50) para regra disponível em até três períodos mediante concordância do empregado, com pisos de 14+5+5 dias. O manual de 2016 descreve o regime antigo e continua correto para férias concedidas até 10/11/2017. ACHADO COLATERAL NO MESMO ITEM 6.4, fora dos 14 pontos mas material para o cálculo: o quadro do bloco 03 (linha 337) invoca a Súmula 450 para a dobra do pagamento fora do prazo do art. 145 alcançando férias + 1/3. A Súmula 450 foi cancelada, com perda de eficácia declarada a partir de 15/08/2022 — e por ADPF 501, não pela Reforma. É um segundo corte, em outra data e por outro eixo, dentro do mesmo item do manual.

— *https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm; https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** sim

### B03-F8 — `VIGENTE`

**Prescrição na supressão de horas extras — a prescrição quinquenal não reduz a contagem de anos da indenização da Súmula 291 (manual 6.6.8, p. 53)**

> **Modulação, literal:** TST, Res. 225/2025, art. 1º, IX: Súmula 294 cancelada 'por perda de eficácia a partir de 11/11/2017' — por reprodução no art. 11, § 2º, e não por superação de conteúdo.

O ponto do manual é de método de apuração, não de prescrição de parcela: o número de anos de prestação habitual é 'apenas um dado necessário para o cálculo da parcela deferida — a indenização — que não está abrangida pela prescrição' (6.6.8, p. 53, com três acórdãos transcritos). O art. 11, § 2º não toca nisso: trata de saber se a prescrição fulmina o próprio fundo do direito em prestações sucessivas decorrentes de alteração do pactuado. Busca negativa declarada: percorri o texto integral da Res. 225/2025 — a Súmula 291 NÃO foi cancelada, continua vigente na redação decorrente do IUJ-ERR-10700-45.2007.5.22.0101; e não localizei precedente vinculante do TST aplicando o art. 11, § 2º à supressão de horas extras (busca em tst.jus.br e busca aberta, 20/09/2026). Logo, o método do manual permanece. Registro variante em aberto (V4): há corrente sustentando que a própria Súmula 291 estaria sup…

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; https://www.tst.jus.br/en/cancelamento-de-…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto para a não incidência do art. 11, § 2º e para a vigência da Súmula 291; medio para o alcance da variante do art. 8º, § 2º**

**Sensível ao intertemporal:** sim — não pelo art. 11, § 2º, mas pelo art. 8º, § 2º (ver variante V4)

### B03-F9 — `BIFURCADO`

**Tempo parcial: tabela de férias do art. 130-A (manual 6.4, p. 30)**

| Norma nova | Lei 13.467/2017, art. 5º, I, 'e': REVOGADO o art. 130-A da CLT (confirmado no compilado: 'Art. 130-A. (Revogado pela Lei nº 13.467, de 2017)'). Em seu lugar, art. 58-A, § 7º: 'As férias do regime de… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | competência do fato gerador — a aquisição do direito a férias, isto é, o fechamento do período aquisitivo. Não é a data… |

> **Modulação, literal:** Nenhuma modulação expressa. A revogação opera pelo art. 6º da Lei 13.467/2017 e não retroage.

A tabela do art. 130-A (18 dias para jornada acima de 22h até 25h, descendo até 8 dias para jornada igual ou inferior a 5h, com redução à metade se houver mais de sete faltas) deixou de existir; os empregados em tempo parcial passaram à tabela geral do art. 130, com os mesmos 30 dias no topo. O efeito no cálculo é grande e em favor do empregado. Também mudou a própria definição do regime, o que pode reclassificar contratos. Variante não resolvida (V5): período aquisitivo a cavaleiro de 11/11/2017 — não localizei regra legal nem precedente vinculante definindo se se aplica a tabela vigente no início do período aquisitivo, no seu fechamento ou por rateio (busca declarada: texto da Lei 13.467, compilado da CLT, Res. 225/2025 e tabela de precedentes vinculantes do NUGEP/TST, 20/09/2026). Sob o Tema 23 a leitura mais direta é a do fato gerador consumado, isto é, o fechamento do período aquis…

— *https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm; https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm* · **primaria-lei-planalto** · confiança **alto para a revogação e a regra nova; baixo para a solução do período aquisitivo a cavaleiro (declarado como variante)**

**Sensível ao intertemporal:** sim

### B04-F3 — `BIFURCADO`

**Base do seguro-desemprego apurada pelo art. 457 da CLT, incluindo prêmios habituais e prestação in natura (manual 6.13.4, p. 70, nota atribuída ao MTE)**

| Norma nova | CLT, art. 457, §§ 1º e 2º (Lei 13.467/2017) — prêmios e abonos deixam de integrar a remuneração 'ainda que habituais' e não constituem base de incidência de qualquer encargo trabalhista e previdenciá… |
|---|---|
| **Data de corte** | 11/11/2017 (com subjanela 14/11/2017 a 22/04/2018 sob a MP 808/2017, em que 'abonos' não figurava na exclusão e prêmios… |
| **Eixo do corte** | competência do fato gerador — os meses de salário que compõem a média de apuração do benefício |

> **Modulação, literal:** Lei 13.467/2017, art. 6º. Nenhuma modulação específica para o seguro-desemprego.

O ponto é composto e se parte em dois: a metade dos PRÊMIOS bifurca em 11/11/2017 (não integram desde então, por força do § 2º, que alcança expressamente a base de incidência de encargos); a metade da PRESTAÇÃO IN NATURA permanece íntegra, porque o art. 458, caput, não foi tocado — salvo a exclusão nova do § 5º (assistência médica/odontológica), que é redução de escopo, não supressão do critério. O manual, portanto, não está inteiramente superado neste item: está superado pela metade, e a metade que cai é a dos prêmios. Busca NÃO realizada, declarada: não verifiquei nesta rodada as regras próprias de apuração do valor do benefício (Lei 7.998/1990, art. 5º, e resoluções do CODEFAT), nem se ato normativo do Ministério do Trabalho posterior a 2017 substituiu a nota que o manual reproduz. Esse trecho fica SEM FONTE verificada e não deve ser tratado como confirmado.

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/mpv/mpv808.htm* · **primaria-lei-planalto** · confiança **alto quanto ao art. 457/458; nulo quanto à nota do MTE e à fórmula do benefício (não pesquisadas)**

**Sensível ao intertemporal:** sim

### B04-F4 — `VIGENTE`

**Comissões integram a remuneração 'pela média dos últimos doze meses', com base no art. 457, § 1º (manual 6.12, p. 65)**

> **Modulação, literal:** Nenhuma. Súmulas 27, 264 e 340 e as OJs 235 e 397 da SBDI-1 não constam do rol da Res. 225/2025.

A Reforma enxugou o § 1º (saíram percentagens, gratificações ajustadas, diárias e abonos), mas manteve as comissões — que são, aliás, a única parcela variável nomeada que sobreviveu no caput do dispositivo. A integração que o manual aplica, e os reflexos em 13º, férias, FGTS, rescisórias, RSR e horas extras, continuam de pé. SUSPEITA SOBRE O MANUAL, registrada e não corrigida: a expressão 'pela média dos últimos doze meses' NÃO está no art. 457, § 1º — nem na redação de 2016 nem na atual. A média de doze meses aparecia no art. 457, § 8º, na redação da Lei 13.419/2017, e ali se referia a GORJETAS, não a comissões; para férias e 13º de comissionista os fundamentos são outros (CLT, art. 142, § 3º, e Lei 4.090/1962). O manual atribui a um dispositivo uma regra que ele não contém. Isso não muda o veredito de vigência, mas o fundamento citado é frágil.

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13419.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** não

### B04-F5 — `BIFURCADO`

**Adicional noturno em 12×36 — OJ 388 da SBDI-1 (manual 6.11.4, p. 62)**

| Norma nova | CLT, art. 59-A, parágrafo único, parte final (Lei 13.467/2017): 'e serão considerados compensados os feriados e as prorrogações de trabalho noturno, quando houver, de que tratam o art. 70 e o § 5º do… |
|---|---|
| **Data de corte** | 11/11/2017 (com subjanela 14/11/2017 a 22/04/2018: sob a MP 808 a mesma regra figurava como § 1º do art. 59-A, e a 12×3… |
| **Eixo do corte** | competência do fato gerador — a jornada noturna efetivamente prorrogada |

> **Modulação, literal:** Nenhuma no plano do verbete: a OJ 388 NÃO foi cancelada. O corte vem apenas da vigência do art. 59-A.

Distinção que decide o cálculo e que o rótulo do ponto esconde: o parágrafo único do art. 59-A NÃO suprime o adicional noturno das horas cumpridas entre 22h e 5h (art. 73, caput, e ficção da hora reduzida do § 1º, ambos intactos). Ele alcança apenas a PRORROGAÇÃO do trabalho noturno de que trata o § 5º do art. 73 — exatamente a hipótese da OJ 388 (horas após as 5h em jornada que abrange todo o período noturno). Logo: até 10/11/2017 incide a OJ 388 e o adicional é devido também nas prorrogações; a partir de 11/11/2017 a lei declara essas prorrogações compensadas pela remuneração mensal pactuada. Achado: a OJ 388 sobreviveu ao expurgo de 30/06/2025 e permanece formalmente vigente apesar do conflito frontal — assim como a Súmula 60, II, que também não foi cancelada. Busca negativa declarada: li o texto integral da Res. 225/2025 (36 enunciados, nenhum deles a OJ 388 nem a Súmula 60) e a pág…

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; https://www.tst.jus.br/en/cancelamento-de-…* · **primaria-lei-planalto + primaria-tribunal** · confiança **alto**

**Sensível ao intertemporal:** sim

### B04-F6 — `BIFURCADO`

**Súmula 39 do TRT-3 e o art. 384 da CLT — intervalo de 15 minutos para mulheres antes da sobrejornada (manual 6.10.1, p. 57)**

| Norma nova | Lei 13.467/2017, art. 5º, I, 'i': REVOGADO o art. 384 da CLT (confirmado no compilado: 'Art. 384 - (Revogado pela Lei nº 13.467, de 2017)'). O que rege o período anterior está fixado em dois preceden… |
|---|---|
| **Data de corte** | 11/11/2017 |
| **Eixo do corte** | competência do fato gerador — o dia de sobrejornada em que o intervalo foi negado. Confirmado pelo TST Tema 23 e pela p… |

> **Modulação, literal:** Tripla. (1) STF, Tema 528: a tese delimita-se ao 'período anterior à edição da Lei n. 13.467/2017' — julgamento em Plenário Virtual de 03 a 14/09/2021 (o acórdão de 27/11/2014 havia sido ANULADO em 05/08/2015 por vício de intimação; embargos de declaração finalizados em 10/06/2022). (2) TST, Tema 63: tese publicada em 14/03/2025, transitada em julgado, restrita ao 'período anterior à vigência da Lei nº 13.467/17'. (3) TRT-3: Súmula 39 CANCELADA por Resolução Administrativa 123, de 20/08/2025 (DEJT 02, 03 e 04/09/2025), com perda de eficácia declarada a partir de 11/11/2017.

É o ponto mais bem resolvido do lote e o único em que os três níveis convergem com data expressa. Para fatos até 10/11/2017: intervalo devido, descumprimento gera 15 minutos como labor extraordinário, sem exigência de tempo mínimo de sobrejornada. Para fatos a partir de 11/11/2017: não há parcela — o dispositivo não existe. Ajuste fino em relação ao manual: a Súmula 39 do TRT-3 falava em '15 minutos extras diários' por descumprimento 'parcial ou integral'; o TST Tema 63 confirma os 15 minutos e acrescenta a dispensa de tempo mínimo de sobrejornada, o que é mais favorável do que parte da jurisprudência exigia. Confirmado na página oficial de súmulas do TRT-3 que a Súmula 39 aparece como 'Cancelada'.

— *https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm; https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://portal.stf.jus.br/jurisprudenciaRepercussao/ve…* · **primaria-lei-planalto + primaria-tribunal (andamento/tese oficial do STF, tabela oficial NUGEP/TST, portal de súmulas do TRT-3)** · confiança **alto**

**Sensível ao intertemporal:** sim, mas com a resposta já dada por precedente vinculante nos dois tribunais

### B04-F7 — `VIGENTE`

**Prescrição do FGTS e a Súmula 362 do TST (manual 6.14, p. 79)**

> **Modulação, literal:** Súmula 362, II: para os casos em que o prazo prescricional já estava em curso em 13/11/2014, aplica-se o prazo que se consumar primeiro — trinta anos contados do termo inicial, ou cinco anos a partir de 13/11/2014. Item I: para ciência da lesão a partir de 13/11/2014, prescrição quinquenal, observado o limite de dois anos após o término do contrato.

O manual transcreve a Súmula 362 na redação da Res. 198/2015 e ainda reproduz as duas redações anteriores (Res. 121/2003 e a de trinta anos) — o que, neste ponto, é acerto e não defasagem, porque a regra de transição do item II exige justamente a comparação entre os dois prazos. Busca negativa declarada: li o texto integral da Res. 225/2025 (36 enunciados) e consultei a página oficial de cancelamentos do TST — a Súmula 362 não foi cancelada nem alterada, e não localizei resolução posterior à 225/2025 (20/09/2026). Portanto o ponto do manual está VIGENTE e o dispositivo indicado no bloco 04 (art. 11, § 2º) é INAPLICÁVEL a ele. Ressalva: o marco de contagem no caso concreto continua dependendo do comando exequendo, como o próprio manual registra.

— *https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm; https://juslaboris.tst.jus.br/bitstream/handle/20.500.12178/251919/2025_res0225.pdf; https://www.tst.jus.br/en/cancelamento-de-…* · **primaria-lei-planalto + primaria-tribunal (Res. 225/2025) + secundaria (redação literal da Súmula 362)** · confiança **alto para a vigência e para a inaplicabilidade do art. 11, § 2º; medio para a literalidade da Súmula 362, cujo texto oficial não foi lido no PDF da Res. 198/2015 (download retornou HTTP 500)**

**Sensível ao intertemporal:** não (quanto à Reforma); sim quanto à modulação própria do ARE 709.212

## C. Descontos, encargos, sindical e precatórios

### F7-01 — `BIFURCADO`

**Alíquota única sobre o total do salário-de-contribuição (cota do segurado), Manual TRT-3 pp. 130 e 158**

| Norma nova | EC 103/2019, art. 28, caput e §§ 1º e 2º (alíquotas de 7,5%, 9%, 12% e 14% aplicadas de forma progressiva sobre a faixa de valores compreendida nos respectivos limites) |
|---|---|
| **Data de corte** | 2020-03-01 |
| **Eixo do corte** | competência / fato gerador da contribuição. NÃO é a data do cálculo nem a data do pagamento. Até a competência 02/2020… |

> **Modulação, literal:** Não há modulação. A data de corte decorre de regra expressa de vigência: EC 103/2019, art. 36, I — 'Esta Emenda Constitucional entra em vigor: I - no primeiro dia do quarto mês subsequente ao da data de publicação desta Emenda Constitucional, quanto ao disposto nos arts. 11, 28 e 32'. Publicação em 13/11/2019 → vigência do art. 28 em 01/03/2020.

Texto literal conferido: 'Art. 28. Até que lei altere as alíquotas da contribuição de que trata a Lei nº 8.212, de 24 de julho de 1991, devidas pelo segurado empregado, inclusive o doméstico, e pelo trabalhador avulso, estas serão de: I - até 1 (um) salário-mínimo, 7,5%; II - acima de 1 (um) salário-mínimo até R$ 2.000,00, 9%; III - de R$ 2.000,01 até R$ 3.000,00, 12%; e IV - de R$ 3.000,01 até o limite do salário de contribuição, 14%. § 1º As alíquotas previstas no caput serão aplicadas de forma progressiva sobre o salário de contribuição do segurado, incidindo cada alíquota sobre a faixa de valores compreendida nos respectivos limites. § 2º Os valores previstos no caput serão reajustados, a partir da data de entrada em vigor desta Emenda Constitucional, na mesma data e com o mesmo índice em que se der o reajuste dos benefícios do Regime Geral de Previdência Social...'. \|\| O QUE REGE…

— *EC 103/2019, texto integral (reprodução institucional do arquivo do Planalto www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm, capturada em PDF e hospedada em https://oig.cepal.org/s…* · **PRIMÁRIA para o texto da EC 103/2019 (reprodução integral do arquivo oficial); SECUNDÁRIA para a tese do Tema 833 (portal STF inacessível)** · confiança **ALTO para a regra, a data de corte e o método; MÉDIO-ALTO para a tese do Tema 833 (tese estável e convergente em múltiplas fontes, mas inteiro teor não lido)**

### F7-02 — `BIFURCADO`

**Desoneração da folha — item 9.2.10 inteiro, Manual TRT-3 p. 176 (CPRB substitutiva da cota patronal, Lei 12.546/2011)**

| Norma nova | Lei 13.670/2018 (reduziu o rol de setores e vedou a opção a parte deles a partir de 01/09/2018); Lei 14.784/2023 (prorrogou a desoneração dos 17 setores até 31/12/2027); Lei 14.973, de 16/09/2024 (re… |
|---|---|
| **Data de corte** | Múltiplos cortes por competência: 01/09/2018 (Lei 13.670/2018); 01/01/2025, 01/01/2026 e 01/01/2027 (transição da Lei 1… |
| **Eixo do corte** | competência da folha E setor de atividade/CNAE do empregador E opção formal do contribuinte. Três eixos simultâneos — n… |

> **Modulação, literal:** Não aplicável (alterações legislativas, sem decisão judicial com modulação no núcleo do ponto). REGISTRO DE INSTABILIDADE: a Lei 14.784/2023 teve eficácia suspensa por decisão monocrática do Min. Cristiano Zanin na ADI 7633 (abril/2024), depois reformada/composta politicamente até a edição da Lei 14.973/2024. Esse episódio afeta as competências de 2024 e NÃO foi verificado em fonte primária nesta fase.

A estrutura do item 9.2.10 do manual — substituição da contribuição patronal de 20% sobre a folha pela contribuição sobre a receita bruta, com reflexo na apuração dos encargos da reclamada — NÃO foi revogada: foi progressivamente estreitada e está em extinção programada. O que morre é o alcance (quais setores, quais competências), não o instituto. Para qualquer competência dentro da janela de desoneração aplicável ao CNAE da reclamada, a mecânica do manual permanece a correta. \|\| Regime de transição da Lei 14.973/2024, por exercício: 2025 — 80% das alíquotas da CPRB e 25% das alíquotas da contribuição previdenciária patronal sobre a folha; 2026 — 60% da CPRB e 50% da folha; 2027 — 40% da CPRB e 75% da folha; a partir de 2028 — 100% folha, CPRB extinta. Durante a transição há CONCOMITÂNCIA: o contribuinte recolhe as duas bases proporcionalmente, o que o manual de 2016 não prevê em luga…

— *Lei 14.973, de 16/09/2024 (regime de transição). TEXTO INTEGRAL NÃO LIDO EM FONTE PRIMÁRIA — www.planalto.gov.br e www.in.gov.br responderam com fechamento de socket em todas as tentativas; www2.cama…* · **SECUNDÁRIA (convergente, quatro fontes independentes)** · confiança **MÉDIO — os percentuais da transição são convergentes e provavelmente corretos, mas NÃO foram conferidos contra o texto da lei. Uma fonte secundária consultada trazia 'até 31 de janeiro de 2025' onde deveria ler-se 'até 31 de dezembro de 2025', o que demonstra que a transcrição secundária deste ponto é ruidosa. NÃO USAR EM PRODUÇÃO SEM LER A LEI 14.973/2024.**

### F7-03 — `SUPERADO`

**Juros de mora na base de cálculo do IR — o manual (p. 181) registra que 'a questão não está resolvida'**

| Norma nova | STF, RE 855.091/RS, Tema 808 da Repercussão Geral, Rel. Min. Dias Toffoli, Plenário, j. 15/03/2021 |
|---|---|
| **Data de corte** | 2021-03-15 (julgamento). SEM CORTE TEMPORAL DE EFEITOS — a modulação foi expressamente recusada, de modo que a tese alc… |
| **Eixo do corte** | não há eixo temporal. O eixo é MATERIAL: natureza da verba principal sobre a qual os juros incidem — 'remuneração por e… |

> **Modulação, literal:** TRANSCRIÇÃO LITERAL da ementa do acórdão dos embargos de declaração (RE 855091 ED/RS, Plenário, sessão virtual de 11 a 18/06/2021): 'Dois embargos de declaração em recurso extraordinário. Tema nº 808 de repercussão geral. Ausência de omissão, contradição, obscuridade ou erro material no acórdão embargado. Pedido de modulação de efeitos não acolhido. 1. O Plenário da Corte enfrentou adequadamente todos os pontos colocados em debate, nos limites necessários ao deslinde do feito. Inexiste, portanto, qualquer dos vícios previstos no art. 1.022 do Código de Processo Civil. 2. Não se vislumbram razões para se modularem os efeitos do acórdão embargado. 3. Embargos de declaração rejeitados.' \|\| A…

TESE LITERAL do Tema 808: 'Não incide imposto de renda sobre os juros de mora devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função'. \|\| EMENTA, itens 1 a 3: '1. A materialidade do imposto de renda está relacionada com a existência de acréscimo patrimonial. Precedentes. 2. A palavra indenização abrange os valores relativos a danos emergentes e os concernentes a lucros cessantes. Os primeiros, correspondendo ao que efetivamente se perdeu, não incrementam o patrimônio de quem os recebe e, assim, não se amoldam ao conteúdo mínimo da materialidade do imposto de renda prevista no art. 153, III, da Constituição Federal. Os segundos, desde que caracterizado o acréscimo patrimonial, podem, em tese, ser tributados pelo imposto de renda. 3. Os juros de mora devidos em razão do atraso no pagamento de remuneração por exercício de emprego, cargo ou função visam,…

— *STF, RE 855.091/RS — inteiro teor do acórdão de mérito (37 p.) e do acórdão dos embargos de declaração, ambos obtidos do repositório oficial de precedentes do TRT-3: https://portal.trt3.jus.br/intern…* · **PRIMÁRIA — acórdão integral, assinado digitalmente (MP 2.200-2/2001), hospedado por tribunal** · confiança **ALTO**

### F7-04 — `SUPERADO`

**'atualmente a TR' como índice de atualização do débito trabalhista — Manual TRT-3 p. 129, e todo ponto que remeta a 'mesmos índices de atualização do débito trabalhista' (pp. 148, 149) ou 'do crédito do reclamante' (pp. 129, 138, 155)**

| Norma nova | STF, ADC 58, ADC 59, ADI 5867 e ADI 6021, Rel. Min. Gilmar Mendes, Plenário, j. 18/12/2020 — declarada a inconstitucionalidade da TR para débitos trabalhistas. Em seguida: Lei 14.905, de 28/06/2024 (… |
|---|---|
| **Data de corte** | Para a TR: 18/12/2020 (data do julgamento das ADCs), ressalvado o item 'i' da modulação. Para a cadeia posterior: 30/08… |
| **Eixo do corte** | Dois eixos empilhados, que NÃO devem ser confundidos: (a) eixo de FASE — pré-judicial x judicial, separados pelo AJUIZA… |

> **Modulação, literal:** NÃO TRANSCRITA NESTA FASE A PARTIR DO INTEIRO TEOR. O acórdão das ADC 58/59 e ADI 5867/6021 não foi lido: portal.stf.jus.br respondeu HTTP 403 a todas as tentativas de acesso direto e não localizei cópia integral em repositório de tribunal acessível. O que o projeto já possui — o desdobramento das duas situações do item 'i' feito pelo TST — está em 00-base-normativa.md § 1.1, que ELE PRÓPRIO declara ter sido conferido apenas em fontes secundárias, com os três precedentes do TST não lidos no inteiro teor. ESSA PENDÊNCIA CONTINUA ABERTA E NÃO FOI FECHADA NESTA FASE. Síntese secundária colhida, a conferir: '(i) são reputados válidos e não ensejarão qualquer rediscussão os pagamentos realizados…

Para o veredito, a parte do ponto que interessa é incontroversa e já está consolidada no repositório: a TR não é mais índice do débito trabalhista. O manual de 2016 é anterior à ADC 58 e não pode conhecê-la. \|\| CONFRONTO PEDIDO — Lei 14.905/2024 e EC 136/2025 alteram o que a ADC 58 fixou? (a) Lei 14.905/2024: SIM, e por dentro. A ADC 58 mandou aplicar ao crédito trabalhista 'os mesmos índices de correção monetária e de juros vigentes para as condenações cíveis em geral'. Como a Lei 14.905 mudou justamente esses índices cíveis (art. 389, § único: IPCA; art. 406: taxa legal), a remissão feita pelo STF arrastou a mudança para o trabalhista SEM necessidade de novo julgamento no STF. Quem executou a remissão foi o TST na SDI-1 em 17/10/2024. Portanto o critério da ADC 58 continua vigente como REGRA DE REMISSÃO, e o que mudou foi o índice remetido. (b) EC 136/2025: NÃO alcança o devedor pri…

— *00-base-normativa.md §§ 1, 1.1, 4 e 5 do próprio projeto (que cita: STF, ADC 58/59; TST, SDI-1, E-ED-RR-713-03.2010.5.04.0029, DEJT 25/10/2024; Resolução CMN 5.171/2024; EC 136/2025). Acórdão das ADC…* · **BASE DO PROJETO (que declara origem primária para o dispositivo do TST e secundária para o § 1.1) — não é fonte primária lida nesta fase** · confiança **ALTO quanto à superação da TR e à cadeia de índices; BAIXO quanto à transcrição literal da modulação da ADC 58, que permanece NÃO VERIFICADA em fonte primária.**

### F7-05 — `BIFURCADO`

**Base de incidência = 'parcelas de natureza salarial' — Manual TRT-3 p. 128**

| Norma nova | Lei 13.467/2017, que deu nova redação ao art. 457, §§ 1º, 2º e 4º, da CLT e acrescentou o § 3º |
|---|---|
| **Data de corte** | 2017-11-11 (vigência da Lei 13.467/2017). Corte intermediário a registrar: a MP 808/2017 alterou novamente o art. 457 e… |
| **Eixo do corte** | competência da parcela paga (data do fato gerador da verba), não data do ajuizamento nem data do cálculo. É um eixo de… |

> **Modulação, literal:** Não aplicável — alteração legislativa, sem modulação.

O CRITÉRIO do manual ('integram a base as parcelas de natureza salarial') permanece formalmente correto: a Lei 13.467/2017 não trocou o critério, trocou a LISTA do que tem natureza salarial. Redação vigente: '§ 1º Integram o salário a importância fixa estipulada, as gratificações legais e as comissões pagas pelo empregador. § 2º As importâncias, ainda que habituais, pagas a título de ajuda de custo, auxílio-alimentação, vedado seu pagamento em dinheiro, diárias para viagem, prêmios e abonos não integram a remuneração do empregado, não se incorporam ao contrato de trabalho e não constituem base de incidência de qualquer encargo trabalhista e previdenciário.' \|\| A expressão 'não constituem base de incidência de qualquer encargo trabalhista e previdenciário' é o que muda a conta: prêmios e abonos, que antes de 11/11/2017 integravam a base quando habituais, deixam de integrá-la. Para comp…

— *Art. 457 da CLT, redação da Lei 13.467/2017. TEXTO NÃO LIDO EM FONTE PRIMÁRIA nesta fase: planalto.gov.br inacessível (socket fechado), www2.camara.leg.br/legin em HTTP 429 persistente, jusbrasil em…* · **SECUNDÁRIA** · confiança **MÉDIO-ALTO para os §§ 1º e 2º (redação amplamente reproduzida e estável); BAIXO para os §§ 3º e 4º, não transcritos.**

### F7-06 — `BIFURCADO`

**Acordo homologado sem o rito de jurisdição voluntária — Manual TRT-3 pp. 153-154 e 201**

| Norma nova | Lei 13.467/2017, que acrescentou à CLT o Capítulo III-A do Título X (arts. 855-B a 855-E) — 'Do Processo de Jurisdição Voluntária para Homologação de Acordo Extrajudicial' |
|---|---|
| **Data de corte** | 2017-11-11 |
| **Eixo do corte** | MODALIDADE do acordo, e não competência. O rito dos arts. 855-B a 855-E é via NOVA e ADICIONAL — a homologação de acord… |

> **Modulação, literal:** Não aplicável — alteração legislativa, sem modulação.

O que o manual descreve nas pp. 153-154 e 201 (apuração de descontos sobre acordo homologado, discriminação de parcelas, reflexos previdenciários e fiscais) NÃO foi superado: continua sendo a mecânica do acordo em processo já instaurado. O que o manual DESCONHECE é a existência, desde 11/11/2017, de uma porta de entrada autônoma — petição conjunta, representação obrigatória por advogados distintos para cada parte (vedado advogado comum), facultada ao trabalhador a assistência pelo advogado do sindicato de sua categoria (art. 855-B, caput e §§). O art. 855-C ressalva que o procedimento não prejudica o prazo do art. 477, § 6º, da CLT nem afasta a multa do § 8º. O art. 855-D fixa prazo de quinze dias para o juiz analisar o acordo, designando audiência se entender necessário. O art. 855-E prevê a suspensão do prazo prescricional quanto aos direitos especificados no acordo, que volta a fluir…

— *Arts. 855-B a 855-E da CLT, acrescidos pela Lei 13.467/2017. TEXTO NÃO LIDO EM FONTE PRIMÁRIA nesta fase (mesmas indisponibilidades de F7-05). Conteúdo apurado por busca e por material de escola judi…* · **SECUNDÁRIA, com apoio em material institucional de tribunal (TRT-2 e Juslaboris/TST)** · confiança **MÉDIO — a existência e o desenho geral do rito são certos; a redação literal dos arts. 855-C, 855-D e 855-E não foi conferida.**

### F7-07 — `SUPERADO`

**RIR/99 (Decreto 3.000/1999) citado ao longo de todo o item 9.3 — Manual TRT-3 pp. 180, 186, 207**

| Norma nova | Decreto 9.580, de 22/11/2018 (RIR/2018), publicado no DOU de 23/11/2018, que regulamenta a tributação, a fiscalização, a arrecadação e a administração do Imposto sobre a Renda e Proventos de Qualquer… |
|---|---|
| **Data de corte** | 2018-11-23 (publicação e entrada em vigor) |
| **Eixo do corte** | veículo normativo, não regra material. O RIR é decreto de CONSOLIDAÇÃO: não cria nem extingue obrigação tributária, ape… |

> **Modulação, literal:** Não aplicável.

Todas as remissões do capítulo 9.3 do manual a artigos do Decreto 3.000/1999 estão mortas como ENDEREÇO. O veredito é SUPERADO e não BIFURCADO porque um regulamento revogado não continua regendo competências pretéritas: o que rege as competências pretéritas são as LEIS que o RIR/99 consolidava (Lei 7.713/1988, Lei 8.134/1990, Lei 9.250/1995, Lei 9.430/1996 etc.), que seguem vigentes e foram reconsolidadas pelo RIR/2018. \|\| IMPLICAÇÃO PARA O PROJETO, que é o ponto prático: as citações do manual precisam ser reescritas por DE-PARA de artigo, e o de-para NÃO foi levantado nesta fase. É trabalho de correspondência artigo a artigo entre o Decreto 3.000/1999 e o Decreto 9.580/2018, que exige leitura dos dois textos — nenhum dos dois foi lido aqui. Enquanto o de-para não existir, toda remissão a 'art. X do RIR/99' no corpus é uma referência quebrada. \|\| ATENÇÃO — armadilha: o RIR/2018 foi…

— *Decreto 9.580, de 22/11/2018 — identificação, data e revogação do Decreto 3.000/1999 confirmadas por convergência entre a ficha da norma no portal legislativo da Presidência (legislacao.presidencia.g…* · **SECUNDÁRIA convergente, com identificação da norma em fichas de repositórios oficiais** · confiança **ALTO para a revogação e as datas; NULO para o de-para de artigos, que não foi feito.**

### F7-08 — `VIGENTE`

**IN RFB 1.500/2014 'com as alterações da IN RFB 1.558/2015' — Manual TRT-3 pp. 187-208**

> **Modulação, literal:** Não aplicável.

A marca de Fase 4 registrada pelo projeto ('INs posteriores') sugere superação e a verificação NÃO a confirma. A IN RFB 1.500/2014 não foi revogada: é a norma geral de tributação do IRPF em vigor em setembro de 2026. A ESTRUTURA a que o capítulo 9.3 do manual remete — regime de competência x regime de caixa, rendimentos recebidos acumuladamente (RRA), tabela do art. 12-A da Lei 7.713/1988, deduções, responsabilidade da fonte pagadora — continua ancorada no mesmo ato. \|\| O que está desatualizado no manual é a MENÇÃO À REDAÇÃO ('com alterações da 1558/15'), não o ato. Corrigir a citação para 'IN RFB 1.500/2014, redação vigente' resolve a maior parte do problema. \|\| RESSALVA EXPLÍCITA, que impede grau de confiança maior: NÃO foi feita conferência artigo a artigo entre a redação de 2015, que o manual usou, e a redação vigente. Onde uma IN posterior tiver alterado dispositivo efetivament…

— *Receita Federal, Sistema de Normas SIJUT2 (normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=57670) — a página respondeu apenas com redirecionamento e NÃO entregou o texto anotado. Vigên…* · **SECUNDÁRIA (o sítio oficial da RFB não respondeu)** · confiança **MÉDIO-ALTO para a vigência do ato e a lista de alterações; BAIXO para qualquer afirmação artigo a artigo.**

### F7-09 — `BIFURCADO`

**Tabelas de IRRF e de salário-de-contribuição congeladas em abr/2015 — anexos do Manual TRT-3 (capítulo 18, séries 18.4, 18.5, 18.6, 18.7)**

| Norma nova | IRRF: Lei 13.149/2015 (tabela vigente de abr/2015) → MP 1.171/2023, convertida na Lei 14.663/2023 (tabela a partir de maio/2023) → Lei 14.848/2024 (fev/2024) → tabela de 2026 fundada na Lei 15.191/20… |
|---|---|
| **Data de corte** | IRRF: 01/05/2023. Salário-de-contribuição: 01/03/2020 (mudança de REGRA, por EC 103/2019) e, quanto aos VALORES das fai… |
| **Eixo do corte** | competência do fato gerador. Cada tabela rege exatamente o período para o qual foi editada. Não há substituição retroat… |

> **Modulação, literal:** Não aplicável.

ESTE É O PONTO EM QUE A LEITURA APRESSADA ERRA. A tabela de IRRF do manual não estava 'defasada em 2016': ela era a tabela VIGENTE, e permaneceu vigente por mais OITO ANOS. A Lei 13.149/2015 fixou a tabela aplicável a partir de abril de 2015 e nenhuma alteração ocorreu até a MP 1.171, de 30/04/2023, com efeitos a partir de 1º de maio de 2023. Ou seja: a série do manual é CORRETA E COMPLETA para o intervalo abr/2015 a abr/2023 — oito anos de competências que qualquer liquidação de contrato antigo ainda atravessa. O defeito é de COBERTURA (a série termina), não de correção (o que está lá está certo). \|\| Para o salário-de-contribuição a situação é diferente e pior, porque há duas camadas: (a) os VALORES das faixas mudam todo 1º de janeiro por portaria interministerial — série pura; (b) a REGRA de aplicação mudou em 01/03/2020 por emenda constitucional — ver F7-01. Uma série de faixas atu…

— *Portaria Interministerial MPS/MF nº 13, de 09/01/2026 (DOU 12/01/2026) — ficha e conteúdo via LegisWeb (id 489284); o PDF oficial em gov.br/previdencia não pôde ser aberto. Cadeia do IRRF (Lei 13.149…* · **SECUNDÁRIA com apoio em fichas de repositórios oficiais; nenhuma portaria ou lei lida em sítio oficial** · confiança **ALTO para a afirmação estrutural (a tabela de abr/2015 vigorou até abr/2023, e o corte é 01/05/2023); MÉDIO para os valores numéricos de 2026, que devem ser recarregados de fonte oficial antes de entrar em série.**

### F7-10 — `BIFURCADO`

**Códigos de recolhimento 2909, 1708, 1889, 5936 e a GPS — Manual TRT-3 pp. 153, 196, 207**

| Norma nova | IN RFB nº 2.005, de 29/01/2021, art. 19, § 1º, V — a DCTFWeb substitui a GFIP como instrumento de confissão de dívida e de constituição do crédito previdenciário oriundo de decisões condenatórias ou… |
|---|---|
| **Data de corte** | 2023-10-01 |
| **Eixo do corte** | DATA DO TRÂNSITO EM JULGADO da decisão condenatória ou homologatória — e não a data do pagamento, nem a competência da… |

> **Modulação, literal:** Não aplicável — ato normativo infralegal, com regra de transição expressa em vez de modulação.

Este ponto é REGRA, não série — e é a resposta à pergunta que o enunciado manda fazer. Não mudou um número numa tabela: mudou o instrumento de confissão, o documento de arrecadação, o código e o sujeito que declara. Um cálculo que produza GPS com código 2909 para sentença transitada em 2024 gera guia inservível. \|\| O que sobrevive do manual: a estrutura de APURAÇÃO (separação da cota do segurado e da cota patronal, terceiros, RAT/FAP, competência a competência) não foi tocada — muda o continente, não o conteúdo. E sobrevive integralmente para o acervo de processos com trânsito até 30/09/2023, que é volume relevante em liquidação. \|\| REGISTRO DE LIMITE DA VERIFICAÇÃO: confirmei o marco, o código DARF 6092 e a norma de regência. NÃO confirmei o destino individual de cada um dos quatro códigos citados pelo manual (2909, 1708, 1889, 5936) — se foram extintos, mantidos para outras hipóte…

— *TRT-3 (TRT-MG), comunicado institucional 'Recolhimento de contribuições previdenciárias deve ser feito via DARF (código 6092) para decisões condenatórias ou homologatórias transitadas em julgado a pa…* · **PRIMÁRIA em sentido administrativo (comunicado oficial do próprio TRT-3, tribunal autor do manual auditado), com a IN RFB identificada mas não lida no sítio da RFB** · confiança **ALTO para o marco, o eixo e o código 6092; NULO para o destino individual dos códigos 2909, 1708, 1889 e 5936.**

### F7-11 — `VIGENTE`

**Súmula 45 do TRT-3, editada em ago/2015 — Manual TRT-3 p. 117**

> **Modulação, literal:** Não aplicável.

CONFIRMADO: a Súmula 45 consta na relação de súmulas do TRT-3 sem nota de cancelamento, revisão ou alteração. Redação literal, conferida na Biblioteca Digital do TRT-MG: 'CONTRIBUIÇÃO PREVIDENCIÁRIA. FATO GERADOR. JUROS DE MORA. [MEDIDA PROVISÓRIA 449/2008]. REGIMES DE CAIXA E DE COMPETÊNCIA. O fato gerador da contribuição previdenciária relativamente ao período trabalhado até 04/03/2009 é o pagamento do crédito trabalhista (regime de caixa), pois quanto ao período posterior a essa data o fato gerador é a prestação dos serviços (regime de competência), em razão da alteração promovida pela Medida Provisória n. 449/2008, convertida na Lei n. 11.941/2009, incidindo juros conforme cada período.' \|\| Aprovação: sessão do Tribunal Pleno. Publicação: RA 194/2015 — DEJT/TRT3, edições 1799 (25/08/2015, Caderno Judiciário, p. 62-63), 1800 (26/08/2015, p. 117-118) e 1801 (27/08/2015, p. 79-80). \…

— *TRT-3: (a) página oficial de súmulas — portal.trt3.jus.br/internet/jurisprudencia/uniformizacao-de-jurisprudencia/sumulas, consultada, sem registro de cancelamento ou alteração; (b) Biblioteca Digita…* · **PRIMÁRIA — repositório oficial do próprio tribunal** · confiança **ALTO**

### F7-12 — `BIFURCADO`

**PLR — Lei 10.101/2000 na redação da Lei 12.832/2013 — Manual TRT-3 p. 199**

| Norma nova | Lei 14.020, de 06/07/2020, cujos dispositivos sobre PLR foram restabelecidos pela derrubada do veto presidencial em 06/11/2020, alterando a Lei 10.101/2000 (notadamente os arts. 2º e 3º) |
|---|---|
| **Data de corte** | 2020-07-06 quanto aos dispositivos sancionados; 06/11/2020 (promulgação das partes vetadas após derrubada do veto pelo… |
| **Eixo do corte** | data do PAGAMENTO da parcela de PLR e período de referência do programa. Não é a data do ajuizamento. |

> **Modulação, literal:** Não aplicável.

A Lei 14.020/2020 não revogou a Lei 10.101/2000: reescreveu partes dela. Sobrevive o desenho central que o manual usa — PLR não substitui nem complementa a remuneração, não se incorpora ao contrato e é tributada exclusivamente na fonte pela tabela própria do art. 3º, § 5º, separada dos demais rendimentos (série 18.6 do capítulo 18). \|\| O que muda, e afeta a conta: (a) PERIODICIDADE — vedado o pagamento de mais de duas parcelas no mesmo ano civil e em periodicidade inferior a um trimestre civil (art. 3º, § 2º); (b) SANÇÃO PROPORCIONAL — o descumprimento da periodicidade 'invalida exclusivamente os pagamentos feitos em desacordo com a norma', e não o programa inteiro, o que muda o efeito previdenciário: só a parcela irregular perde a natureza de PLR e é tributada como salário; (c) reforço da autonomia da vontade das partes na negociação e explicitação dos requisitos de clareza e objetiv…

— *Lei 14.020/2020 e Lei 10.101/2000. TEXTO NÃO LIDO EM FONTE PRIMÁRIA — planalto.gov.br inacessível; o PDF do texto atualizado da Lei 10.101/2000 no Legin da Câmara (www2.camara.leg.br/legin/fed/lei/20…* · **SECUNDÁRIA convergente** · confiança **MÉDIO — a direção das alterações e a regra de periodicidade são convergentes; a redação literal dos arts. 2º e 3º não foi conferida.**

### C8-01 — `BIFURCADO`

**Cap. 8 — alcance do art. 791-A da CLT (Lei 13.467/2017) e sobrevivência do regime de honorários do manual de 2016**

| Norma nova | Art. 791-A da CLT, incluído pela Lei 13.467/2017; e TST, Instrução Normativa nº 41/2018 (aprovada pela Resolução nº 221, de 21/06/2018), art. 6º |
|---|---|
| **Data de corte** | 2017-11-11 |
| **Eixo do corte** | DATA DE PROPOSITURA DA AÇÃO — e não a competência das verbas, nem a data da sentença, nem a data do cálculo. Este é o e… |

> **Modulação, literal:** Não há modulação judicial. A regra de direito intertemporal é normativa: TST, IN 41/2018, art. 6º — 'Na Justiça do Trabalho, a condenação em honorários advocatícios sucumbenciais, prevista no art. 791-A, e parágrafos, da CLT, será aplicável apenas às ações propostas após 11 de novembro de 2017. Nas ações propostas anteriormente, subsistem as diretrizes do art. 14 da Lei nº 5.584/1970 e das Súmulas nos 219 e 329 do TST.' (transcrição conferida em reprodução secundária; ver ressalva de fonte)

O manual descreve o regime ANTIGO e o descreve corretamente para o seu universo: honorários assistenciais, condicionados à assistência sindical e à insuficiência econômica, nunca superiores a 15%, sem sucumbência geral. A Lei 13.467/2017 criou a sucumbência geral. As duas versões valem — e valem SIMULTANEAMENTE hoje, em processos diferentes, separadas pela data de propositura. \|\| É por isso que o veredito é BIFURCADO e não SUPERADO: em setembro de 2026 ainda tramitam e se liquidam ações propostas antes de 11/11/2017, e nelas o capítulo 8 do manual é a norma aplicável, não uma peça de museu. \|\| PARÂMETROS DO ART. 791-A: percentual entre 5% e 15% sobre o valor que resultar da liquidação da sentença, do proveito econômico obtido ou, não sendo possível mensurá-lo, sobre o valor atualizado da causa — faixa distinta tanto do teto de 15% da Súmula 219 quanto da faixa de 10% a 20% do art. 8…

— *TST, IN 41/2018, art. 6º — texto reproduzido de forma convergente em normaslegais.com.br, GEN Jurídico e repositório Juslaboris do TST (juslaboris.tst.jus.br, artigo sobre direito processual intertem…* · **SECUNDÁRIA convergente, com apoio em repositório institucional do TST** · confiança **ALTO para o eixo e a data de corte (regra amplamente assentada e citada uniformemente); MÉDIO-ALTO para a literalidade do art. 6º.**

### C8-02 — `SUPERADO`

**Cap. 8 — honorários e gratuidade de justiça: o que a ADI 5766 decidiu**

| Norma nova | STF, ADI 5766, Rel. p/ acórdão Min. Alexandre de Moraes, Plenário, j. 20/10/2021, acórdão publicado em 03/05/2022; embargos de declaração julgados em 21/06/2022, acórdão publicado em 29/06/2022 |
|---|---|
| **Data de corte** | 2021-10-20 (julgamento). SEM MODULAÇÃO — efeitos ex tunc. |
| **Eixo do corte** | não há eixo temporal próprio. O que há é um eixo SUBJETIVO: a condição de beneficiário da justiça gratuita. |

> **Modulação, literal:** NÃO TRANSCRITA — o acórdão não foi lido. portal.stf.jus.br respondeu HTTP 403 em todas as tentativas e não localizei cópia integral em repositório de tribunal acessível. O que apurei, em fonte secundária, é que os embargos de declaração, que pediam modulação temporal, foram julgados em 21/06/2022 e NÃO foram acolhidos, e que a decisão tem eficácia erga omnes e ex tunc. ESSA AFIRMAÇÃO NÃO ESTÁ CONFERIDA EM FONTE PRIMÁRIA.

O STF julgou parcialmente procedente a ação para declarar a inconstitucionalidade do art. 790-B, caput e § 4º, e do art. 791-A, § 4º, da CLT — os dispositivos que impunham ao beneficiário da justiça gratuita o pagamento de honorários periciais e sucumbenciais com os créditos obtidos no próprio processo ou em outro. \|\| CONSEQUÊNCIA DE CÁLCULO, que é o que interessa ao motor e é frequentemente ignorada: quando o reclamante é beneficiário da gratuidade, os honorários sucumbenciais devidos POR ELE não podem ser abatidos do seu crédito. Isso remove uma parcela da cadeia de descontos sobre o líquido do reclamante. Não remove necessariamente a FIXAÇÃO dos honorários — há divergência sobre se a ADI 5766 afasta a fixação ou apenas suspende a exigibilidade —, e essa divergência está registrada em variantes_nao_resolvidas.

— *STF, ADI 5766 — ficha processual (portal.stf.jus.br, incidente 5250582) inacessível (HTTP 403). Conteúdo apurado por convergência de Trench Rossi Watanabe, AMATRA XV e artigo de análise técnica. Acór…* · **SECUNDÁRIA** · confiança **MÉDIO-ALTO para o dispositivo (quais artigos caíram — informação estável e convergente); MÉDIO para a ausência de modulação; BAIXO para qualquer transcrição.**

### C8-03 — `VIGENTE`

**Cap. 8 — honorários assistenciais (Lei 5.584/70, art. 14; Súmulas 219 e 329 do TST): subsistem?**

> **Modulação, literal:** Não aplicável.

SUBSISTEM, e por remissão normativa expressa: o art. 6º da IN 41/2018 do TST determina que, nas ações propostas antes de 11/11/2017, 'subsistem as diretrizes do art. 14 da Lei nº 5.584/1970 e das Súmulas nos 219 e 329 do TST'. Não há revogação, cancelamento ou superação das súmulas — há delimitação do universo em que operam. \|\| Súmula 219, I (redação dada pela Resolução nº 204/2016 do Tribunal Pleno, sessão de 15/03/2016, divulgada no DEJT em 17, 18 e 21/03/2016 — a mesma que acresceu os itens IV a VI em razão do CPC/2015): 'Na Justiça do Trabalho, a condenação ao pagamento de honorários advocatícios, nunca superiores a 15% (quinze por cento), não decorre pura e simplesmente da sucumbência, devendo a parte, concomitantemente: a) estar assistida por sindicato da categoria profissional; b) comprovar a percepção de salário inferior ao dobro do salário mínimo ou encontrar-se em situação e…

— *TST, Súmulas 219 e 329 — redação e dados da Resolução 204/2016 obtidos por busca em reproduções convergentes; o sítio de jurisprudência do TST (jurisprudencia.tst.jus.br) respondeu mas entrega a base…* · **SECUNDÁRIA convergente** · confiança **ALTO para a subsistência e o recorte de aplicação; MÉDIO-ALTO para a literalidade.**

### C12-01 — `BIFURCADO`

**Cap. 12 — contribuição sindical obrigatória e a estrutura de cálculo do manual**

| Norma nova | Lei 13.467/2017, art. 1º, que deu nova redação aos arts. 545, 578, 579, 582, 583, 587 e 602 da CLT, condicionando o recolhimento a autorização prévia e expressa do trabalhador |
|---|---|
| **Data de corte** | 2017-11-11 |
| **Eixo do corte** | competência da contribuição (mês de março, para o empregado). Até a competência de 2017 a contribuição é compulsória e… |

> **Modulação, literal:** Não aplicável — alteração legislativa. A ADI 5794, que a confirmou, declarou CONSTITUCIONALIDADE, com efeito ex tunc por natureza, sem modulação.

RESPOSTA DIRETA À PERGUNTA DO ENUNCIADO — o que sobrevive para competências anteriores a 11/11/2017: TUDO. Base de cálculo (um dia de remuneração para o empregado; tabela progressiva sobre o capital social para o empregador; valores fixos por faixa para o profissional liberal e o autônomo), forma de apuração, prazos de recolhimento, forma de atualização e a contribuição sindical RURAL com regra própria e tabelas de 2011 a 2016 — nada disso foi tocado pela reforma. A Lei 13.467/2017 não mexeu no QUANTO nem no COMO: mexeu no SE. \|\| Por isso o capítulo 12 não é lixo histórico: é a norma de regência de qualquer competência até 2017 que ainda esteja em liquidação. O bloco 13C do projeto acertou ao extraí-lo como estrutura. \|\| REQUISITOS DA AUTORIZAÇÃO, verificados: a exigência é de autorização PRÉVIA e EXPRESSA. Quanto à exigência de que seja também INDIVIDUAL — isto é, a invalidade de a…

— *Lei 13.467/2017, art. 1º. Texto NÃO lido em fonte primária (planalto inacessível; Legin em HTTP 429). Objeto da alteração identificado via resumo da ADI 5794.* · **SECUNDÁRIA** · confiança **ALTO para o corte e para a sobrevivência integral da estrutura de cálculo; MÉDIO para a literalidade dos dispositivos da CLT alterados.**

### C12-02 — `VIGENTE`

**Cap. 12 — ADI 5794 do STF: a facultatividade da contribuição sindical é constitucional?**

> **Modulação, literal:** NÃO TRANSCRITA — acórdão não lido (portal.stf.jus.br em HTTP 403). Não há notícia de modulação, e a declaração de constitucionalidade opera ex tunc por natureza, confirmando a norma desde a origem. A ausência de modulação NÃO foi conferida em fonte primária.

CONFIRMA a validade da regra que superou o capítulo 12: o STF, em 29/06/2018, por 6 votos a 3, julgou constitucional o fim da obrigatoriedade da contribuição sindical. Votaram pela constitucionalidade os Ministros Luiz Fux, Alexandre de Moraes, Luís Roberto Barroso, Marco Aurélio, Gilmar Mendes e Cármen Lúcia; vencidos os Ministros Edson Fachin, Rosa Weber e Dias Toffoli. \|\| A ADI 5794 foi ajuizada pela CONTTMAF e julgada em conjunto com outras 18 ADIs e com a ADC 55 — o julgamento alcança todas. \|\| IMPORTÂNCIA PARA O MOTOR: fecha a possibilidade de reversão. Enquanto a matéria estava pendente havia risco de a compulsoriedade ser restaurada com efeitos retroativos, o que obrigaria a manter a estrutura do manual como default. Julgada constitucional, a estrutura do capítulo 12 vira estritamente histórica — aplicável a competências até 2017 e a mais nada.

— *STF, ADI 5794 — notícia institucional do STF (portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=382819) INACESSÍVEL (HTTP 403). Conteúdo apurado por convergência de ConJur (29/06/2018), Mig…* · **SECUNDÁRIA convergente** · confiança **MÉDIO-ALTO — resultado, data e placar convergentes em fontes independentes; acórdão não lido.**

### C12-03 — `BIFURCADO`

**Cap. 12 — contribuição ASSISTENCIAL: há decisão posterior? (Tema 935 do STF, ARE 1.018.459)**

| Norma nova | STF, ARE 1.018.459, Tema 935 da Repercussão Geral — tese original de 2017 (inconstitucionalidade) REVISTA no julgamento dos embargos de declaração em abril de 2023; novos embargos, da PGR, acolhidos… |
|---|---|
| **Data de corte** | abril de 2023 (revisão da tese). Segundo marco: DJe 12/09/2025 (aditamentos integrativos). |
| **Eixo do corte** | EXISTÊNCIA DE DIREITO DE OPOSIÇÃO assegurado, e não data. É eixo de conteúdo da norma coletiva: a mesma competência pod… |

> **Modulação, literal:** NÃO TRANSCRITA — acórdãos não lidos (portal.stf.jus.br em HTTP 403). REGISTRO DO QUE APUREI, NÃO CONFERIDO EM PRIMÁRIA: nos embargos da PGR, publicados no DJe de 12/09/2025, o STF teria acolhido com efeitos integrativos para (i) vedar a cobrança retroativa da contribuição, (ii) impedir interferência de terceiros no exercício do direito de oposição e (iii) exigir razoabilidade na fixação do valor. O item (i) funciona como limitador temporal e é, materialmente, o que mais se aproxima de uma modulação — e é justamente o que precisa ser lido no original antes de virar regra de motor.

HÁ decisão posterior, e ela inverteu o sentido. Tese ORIGINAL (2017): 'É inconstitucional a instituição, por acordo, convenção coletiva ou sentença normativa, de contribuições que se imponham compulsoriamente a empregados da categoria não sindicalizados.' Tese VIGENTE (revisão de abril de 2023): 'É constitucional a instituição, por acordo ou convenção coletivos, de contribuições assistenciais a serem impostas a todos os empregados da categoria, ainda que não sindicalizados, desde que assegurado o direito de oposição.' \|\| O capítulo 12 do manual NOMEIA a contribuição assistencial mas NÃO A CALCULA — o bloco 13C já registrou isso. Logo, o efeito do Tema 935 sobre o manual é indireto: ele não supera nenhuma conta existente, ele ABRE uma hipótese de desconto que o manual não cobre. \|\| RESSALVA DE ESCOPO, essencial: a contribuição NEGOCIAL prevista no ACT 2025/2027 já registrada no corpu…

— *STF, ARE 1.018.459, Tema 935 — portal de repercussão geral (incidente 5112803) INACESSÍVEL (HTTP 403). Conteúdo apurado por convergência de Migalhas, material do portal Conexão Trabalho (CNI) e traba…* · **SECUNDÁRIA** · confiança **MÉDIO-ALTO para a tese vigente de 2023 (reproduzida uniformemente); BAIXO para o conteúdo e o alcance dos aditamentos de 2025.**

### C14-01 — `SUPERADO`

**Cap. 14 — art. 3º da EC 113/2021: a Selic como índice único alcança apenas requisitórios da Fazenda Pública FEDERAL?**

| Norma nova | EC 136, de 09/09/2025, que reescreveu o art. 3º da EC 113/2021 |
|---|---|
| **Data de corte** | 2021-12-09 (EC 113/2021, com efeitos de correção a partir da competência dez/2021) e 09/09/2025 (EC 136/2025). A Res. C… |
| **Eixo do corte** | três eixos simultâneos, que a EC 136/2025 estreitou de uma vez: OBJETO (de 'discussões e condenações' para 'requisitóri… |

> **Modulação, literal:** Emendas constitucionais não modulam. O que existe é regra de incidência administrativa — CNJ, Provimento 207/2025, a partir de setembro de 2025: os precatórios são atualizados pelo IPCA incidindo sobre principal e juros SOMADOS; os juros de 2% a.a., calculados mensalmente, incidem sobre o principal EXCLUÍDOS os juros já apurados. Essa assimetria é especificação de implementação e não decorre da leitura da emenda.

REFUTO A RESTRIÇÃO REGISTRADA PELO PROJETO. O arquivo bloco-13c-sindical-precatorios.md § 7 afirma que 'a EC 113/2021 art. 3º alcança apenas requisitórios federais'. Isso está ERRADO, e a prova está dentro do próprio repositório: 00-base-normativa.md § 5 transcreve a redação ORIGINAL do art. 3º da EC 113/2021 — 'Nas discussões e nas condenações que envolvam a Fazenda Pública, INDEPENDENTEMENTE DE SUA NATUREZA e para fins de atualização monetária, de remuneração do capital e de compensação da mora, inclusive do precatório, haverá a incidência, uma única vez, até o efetivo pagamento, do índice da taxa referencial do Sistema Especial de Liquidação e de Custódia (Selic), acumulado mensalmente.' Não há a palavra 'federal', não há a palavra 'requisitório' como limite, e há expressa cláusula de universalidade. \|\| A restrição a 'Fazenda Pública federal' é criação da EC 136/2025, não da EC 113…

— *00-base-normativa.md § 5 do próprio projeto, que transcreve as duas redações do art. 3º; e bloco-13c-sindical-precatorios.md § 7, que contém a afirmação refutada. Os textos das EC 113/2021 e EC 136/2…* · **BASE DO PROJETO (contradição interna documentada)** · confiança **ALTO quanto à contradição e quanto a qual dos dois registros é o correto — a redação transcrita no § 5 é autoconsistente e incompatível com a restrição afirmada no bloco 13C. MÉDIO enquanto o texto da EC 113/2021 não for lido no Planalto.**

### C14-02 — `BIFURCADO`

**Cap. 14 — o que a EC 136/2025 mudou, e o que sobrevive do manual, que conhece apenas a EC 62/2009**

| Norma nova | EC 136, de 09/09/2025; CNJ, Provimento 207/2025; CJF, Res. 990/2026 |
|---|---|
| **Data de corte** | setembro de 2025 |
| **Eixo do corte** | EXPEDIÇÃO DO REQUISITÓRIO (novo marco inicial) e ENTE DEVEDOR (Fazenda Pública federal x estadual/municipal). Antes da… |

> **Modulação, literal:** Não aplicável.

MUDANÇA: 'Nos requisitórios que envolvam a Fazenda Pública federal, a partir da sua expedição até o efetivo pagamento, a atualização monetária será feita pela variação do Índice Nacional de Preços ao Consumidor Amplo (IPCA), e, para fins de compensação da mora, incidirão juros simples de 2% a.a.', com TRAVA: se a soma da atualização monetária com os juros de mora superar a SELIC no mesmo período, aplica-se a SELIC em substituição. \|\| O QUE SOBREVIVE DO CAPÍTULO 14 DO MANUAL, que é a pergunta do enunciado: sobrevivem quatro regras estruturais, e o bloco 13C já as cruzou com o manual do CJF — (a) suspensão dos juros de mora durante o prazo constitucional de pagamento; (b) juros de 0,5% ao mês desde ago/2001; (c) exclusão de juros compensatórios; (d) exceção à precedência do título. Nenhuma delas depende da EC 62/2009 nem foi tocada pelas ECs 113 e 136. \|\| O que NÃO sobrevive: o índice…

— *00-base-normativa.md § 5 (texto da EC 136/2025, Provimento CNJ 207/2025, Res. CJF 990/2026, STJ REsp 2.236.270/SP, STF ARE 1.557.312/SP - Tema 1.419, ADI 7873 pendente); bloco-13c-sindical-precatorio…* · **BASE DO PROJETO** · confiança **ALTO (a § 5 da base é detalhada, datada e internamente consistente); a confirmação em fonte primária fica pendente.**

### C14-03 — `INAPLICÁVEL`

**Cap. 14 — aplicabilidade do regime de precatórios ao caso do produto**

> **Modulação, literal:** Não aplicável.

INAPLICÁVEL POR PREJUDICIALIDADE, e a razão é declarada, não presumida: a aplicação do capítulo 14 depende de uma classificação que não é matéria de cálculo — se a devedora é ou não Fazenda Pública. Essa é a Pendência 1 de 00-base-normativa.md § 9, expressamente qualificada como 'pergunta ao jurídico do cliente', e a de maior impacto do projeto: se a resposta for negativa, somem do escopo o ramo Fazenda Pública das três jurisdições, precatório, ECs 113 e 136 e a consolidação de dez/2021. \|\| Confirmei que o manual não resolve: busca declarada do bloco 13C — 'economia mista' tem ZERO ocorrências nas 471 páginas; a única equiparação nominada é a ECT, e só 'para efeito de execução e do DL 779/1969'. \|\| Enquanto a Pendência 1 estiver aberta, qualquer veredito de mérito sobre o capítulo 14 é especulativo. Os vereditos C14-01 e C14-02 são condicionais a ela.

— *00-base-normativa.md § 9, pendência 1; bloco-13c-sindical-precatorios.md § 7; bloco-13b-encargos.md § 4* · **BASE DO PROJETO** · confiança **ALTO**

---

## D. Os nove que a releitura adversarial encontrou sem veredito

O enunciado exigiu *"um segundo passe procurando ponto marcado sem veredito"*. Ele achou
**nove** — e um deles rendeu achado positivo.

### JR-01 — `VIGENTE`

**Súmula 124 do TST — divisor do bancário**

**Sobreviveu ao expurgo.** A Resolução 225/2025 do TST cancelou 27 súmulas — 6, 90, 114, 152, 219, 228, 268, 277, 294, 307, 311, 320, 329, 331-I, 366, 372-I, 375, 377, 423, 426, 429, 437, 439, 444, 449, 450 e 452. **A 124 não está na lista.** Permanece na redação da Res. 219/2017, com a modulação do IRR-849 já registrada em `pr.sumula124-divisor-bancario`.

— *Res. TST 225/2025, texto integral (DEJT 4253) — lista de incisos conferida por script* · **primária** · confiança **alta**

### JR-05 — `SUPERADO`

**OJ 300 da SDI-1 — valida a TRD do art. 39 da Lei 8.177/91**

| Norma nova | ADC 58 e ADC 59 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

**Consequência de F7-04, não ponto autônomo.** A OJ valida exatamente o índice que a ADC 58 declarou inconstitucional para débitos trabalhistas. Julgada em separado produziria veredito redundante; registrada para rastreabilidade.

— *ADC 58/59 (STF, 18/12/2020) — ver F7-04* · **secundária** · confiança **alta**

### AM-01 — `SUPERADO`

**Item 10.1 do manual pressupõe o critério pré-ADC 58 — marcação geral**

| Norma nova | ADC 58, EC 113/2021, Lei 14.905/2024 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

Segue F7-04. **Mas a marcação é geral, não pontual:** o bloco 11A registrou que não há em 10.1 regra de dedução ou compensação — `compensa`, `ADC 58` e `IPCA` têm zero ocorrências nas pp. 209–223. O que cai é o índice, não o método.

— *bloco-11a-imputacao.md § 10; ADC 58* · **secundária** · confiança **alta**

### AM-03 — `BIFURCADO`

**Sob Selic pós-citação a distinção principal × juros perde objeto**

| Norma nova | ADC 58 (Selic da citação) e EC 113/2021 |
|---|---|
| **Data de corte** | por segmento da cadeia |
| **Eixo do corte** | competência da parcela |

**Não é supersessão — é mudança de natureza da operação.** Enquanto houver período regido por índice + juros separados, o rateio de 10.3 tem objeto. No período de Selic única (que engloba), **não há o que ratear**. A conta real atravessa os dois regimes, logo os dois coexistem por segmento.

— *bloco-11c-vincendos.md § 9; 00-base-normativa.md § 1* · **secundária** · confiança **alta**

### CH-01 — `BIFURCADO`

**Cadeia `trab.hist.correcao-monetaria 1942-11..2009-06`**

| Norma nova | ADC 58, EC 113/2021 art. 3º, Lei 14.905/2024 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

**O `status_norma: superado` do JSON está certo quanto ao futuro e incompleto quanto ao passado.** O segmento continua sendo a regra aplicável às competências que cobre — é essa a razão de a cadeia histórica existir. O que caduca é usá-lo para competências posteriores ao corte da ADC 58. **Cadeia temporal, não supersessão** — a mesma estrutura da Res. 225/2025.

— *ADC 58/59; EC 113/2021; Lei 14.905/2024 — ver F7-04* · **secundária** · confiança **alta**

### CH-02 — `BIFURCADO`

**Cadeia `trab.hist.correcao-monetaria 2009-07..2016-05 (não-Fazenda)`**

| Norma nova | ADC 58, EC 113/2021 art. 3º, Lei 14.905/2024 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

**O `status_norma: superado` do JSON está certo quanto ao futuro e incompleto quanto ao passado.** O segmento continua sendo a regra aplicável às competências que cobre — é essa a razão de a cadeia histórica existir. O que caduca é usá-lo para competências posteriores ao corte da ADC 58. **Cadeia temporal, não supersessão** — a mesma estrutura da Res. 225/2025.

— *ADC 58/59; EC 113/2021; Lei 14.905/2024 — ver F7-04* · **secundária** · confiança **alta**

### CH-03 — `BIFURCADO`

**Cadeia `trab.hist.correcao-monetaria 2009-07..2016-05 (Fazenda)`**

| Norma nova | ADC 58, EC 113/2021 art. 3º, Lei 14.905/2024 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

**O `status_norma: superado` do JSON está certo quanto ao futuro e incompleto quanto ao passado.** O segmento continua sendo a regra aplicável às competências que cobre — é essa a razão de a cadeia histórica existir. O que caduca é usá-lo para competências posteriores ao corte da ADC 58. **Cadeia temporal, não supersessão** — a mesma estrutura da Res. 225/2025.

— *ADC 58/59; EC 113/2021; Lei 14.905/2024 — ver F7-04* · **secundária** · confiança **alta**

### CH-04 — `BIFURCADO`

**Cadeia `trab.hist.juros-mora 1991-04..2016-05`**

| Norma nova | ADC 58, EC 113/2021 art. 3º, Lei 14.905/2024 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

**O `status_norma: superado` do JSON está certo quanto ao futuro e incompleto quanto ao passado.** O segmento continua sendo a regra aplicável às competências que cobre — é essa a razão de a cadeia histórica existir. O que caduca é usá-lo para competências posteriores ao corte da ADC 58. **Cadeia temporal, não supersessão** — a mesma estrutura da Res. 225/2025.

— *ADC 58/59; EC 113/2021; Lei 14.905/2024 — ver F7-04* · **secundária** · confiança **alta**

### CH-05 — `BIFURCADO`

**Cadeia `trab.hist.fazenda-publica.juros-mora 2009-07..2016-05`**

| Norma nova | ADC 58, EC 113/2021 art. 3º, Lei 14.905/2024 |
|---|---|
| **Data de corte** | ver F7-04 |
| **Eixo do corte** | competência da parcela |

**O `status_norma: superado` do JSON está certo quanto ao futuro e incompleto quanto ao passado.** O segmento continua sendo a regra aplicável às competências que cobre — é essa a razão de a cadeia histórica existir. O que caduca é usá-lo para competências posteriores ao corte da ADC 58. **Cadeia temporal, não supersessão** — a mesma estrutura da Res. 225/2025.

— *ADC 58/59; EC 113/2021; Lei 14.905/2024 — ver F7-04* · **secundária** · confiança **alta**

---

## E. Variantes não resolvidas

O enunciado proíbe resolver divergência jurisprudencial. Onde há correntes, **as duas
ficam registradas com fundamento**.

### V-01 — VAR-01

- **ponto relacionado:** F4-02 — base de cálculo do adicional de insalubridade
- **corrente a:** tese: A base é o SALÁRIO MÍNIMO (art. 192 da CLT), enquanto não superada a inconstitucionalidade por LEI ou por NORMA COLETIVA. O Judiciário não pode fixar base diversa, sob pena de atuar como legislador positivo.; fundamento: STF, Súmula Vinculante 4, segunda parte: o salário mínimo não pode 'ser substituído por decisão judicial'. Cassação da parte da Súmula 228 do TST que fixava o salário básico (decisão publicada em 18/04/2018). Cancelamento integral da Súmula 228 pela Res. 225/2025 do TST.; status: corrente majoritária e default recomendado
- **corrente b:** tese: É inconstitucional impor o salário mínimo como base quando havia OUTRO parâmetro previamente adotado por norma interna, regulamento empresarial ou instrumento coletivo — porque nessa hipótese a troca imposta pela Justiça do Trabalho é ela própria a substituição judicial vedada pela SV 4. Prevalece o ato regulamentar anterior.; fundamento: STF, 2ª Turma, Ag.Reg. na Reclamação 53.157/PA, j. 20/10/2025, Rel. Min. Nunes Marques, vencido, redator do acórdão Min. Dias Toffoli, acompanhado pelos Min. Gilmar Mendes e André Mendonça. Caso concreto: enferme…
- **por que nao resolvo:** As duas teses não são logicamente incompatíveis — a segunda é uma exceção construída sobre a mesma SV 4, para a hipótese específica de haver parâmetro anterior. Mas o recorte da exceção (o que conta como 'parâmetro previamente adotado'? norma interna? prática reiterada? ACT expirado?) não está fixado em precedente qualificado, e resolvê-lo seria inventar critério. Para o motor: manter salário mínimo como default e expor a base como parâmetro negociável, com variante 'base anterior preservada' acionável mediante prova documental de norma interna ou colet…
- **impacto no calculo:** alto — a diferença entre salário mínimo e salário-base multiplica o valor do adicional na maioria dos vínculos.

### V-02 — VAR-02

- **ponto relacionado:** F4-03 e F4-05 — intervalo intrajornada em contratos iniciados antes de 11/11/2017
- **corrente a:** tese: Aplicação imediata: para intervalos suprimidos a partir de 11/11/2017 vale o art. 71, § 4º novo (só o período suprimido, natureza indenizatória), ainda que o contrato seja anterior.; fundamento: TST, Tema Repetitivo 23, Pleno, 25/11/2024, tese vinculante. Embargos rejeitados em 20/05/2025 com recusa expressa de modulação.; status: VINCULANTE (art. 896-C da CLT; art. 927 do CPC). É o default obrigatório.
- **corrente b:** tese: Ultratividade: contrato iniciado antes da Reforma segue o regime antigo por toda a sua duração.; fundamento: Voto divergente do Min. Mauricio Godinho Delgado e de outros nove ministros no Tema 23; princípio da proteção; vedação de alteração contratual lesiva.; status: VENCIDA no Pleno por 15 a 10. Sobrevive em decisões de primeiro e segundo graus e em doutrina, mas é posição contrária a precedente qualificado.
- **por que nao resolvo:** O enunciado manda registrar correntes sem resolver, e a base do projeto expõe as duas como presets de igual peso. Não as equiparo: registro que a corrente B foi VENCIDA em julgamento vinculante e que, materialmente, não há mais divergência de igual dignidade — há uma tese obrigatória e uma posição minoritária residual. A decisão de manter ou não o preset TRAB-INTERTEMP-ULTRATIVO é do jurídico do cliente, não do motor.
- **impacto no calculo:** alto para a Gasmig, que tem contratos anteriores a 11/11/2017 gerando passivo.

### V-03 — VAR-03

- **ponto relacionado:** F4-05, item II da Súmula 437 — validade de cláusula coletiva que reduz o intervalo intrajornada
- **corrente a:** tese: Cláusula de ACT/CCT que reduz o intervalo é válida, respeitado o mínimo de trinta minutos.; fundamento: Art. 611-A, III, da CLT (Lei 13.467/2017) e STF, Tema 1046 (ARE 1.121.633, Pleno, ata publicada em 14/06/2022). É a causa declarada do cancelamento do item II.; status: posição prevalente a partir de 11/11/2017
- **corrente b:** tese: O intervalo intrajornada é norma de saúde, higiene e segurança do trabalho e, como tal, direito absolutamente indisponível — logo, fora do alcance da negociação coletiva mesmo após o Tema 1046.; fundamento: Art. 611-B, parágrafo único e incisos sobre normas de saúde e segurança; a própria ressalva do Tema 1046 a 'direitos absolutamente indisponíveis'; fundamento original do item II da Súmula 437 (art. 7º, XXII, da CF).; status: corrente resistente, sustentada em que o art. 611-B trata normas de saúde e segurança como indisponíveis e que o art. 611…
- **por que nao resolvo:** O limite 'direitos absolutamente indisponíveis' do Tema 1046 é categoria expressamente aberta, e o próprio STF reconhece as normas de saúde e segurança como núcleo indisponível — ao mesmo tempo em que o legislador inscreveu o intervalo no rol negociável do art. 611-A. A tensão é normativa, não factual, e não há precedente qualificado que a feche. Registro como variante do parâmetro negociável 'intervalo intrajornada'.
- **impacto no calculo:** alto onde houver cláusula de redução no ACT.

### V-04 — Eixo do direito intertemporal da Reforma

- **correntes:** {'nome': 'tempus regit actum / competência do fato gerador', 'fundamento': 'TST, Tema 23 (IRR-528-80.2018.5.14.0004), tese vinculante, transitada em julgado; art. 6º da LINDB; MP 808/2017, art. 2º (enquanto vigeu)', 'peso': 'vinculante'}; {'nome': 'ultratividade da lei do contrato / data de admissão', 'fundamento': 'irretroatividade, princípio da proteção e segurança jurídica; voto vencido do Min. Mauricio Godinho Delgado no Tema 23 (10 votos); resistência em TRTs', 'peso': 'minoritária e hoje contra tese vinculante'}
- **pontos sensiveis:** B03-F1; B03-F2; B03-F3; B03-F4; B03-F5; B03-F7; B03-F9; B04-F3; B04-F5; B04-F6
- **observacao:** Não resolvo. Registro que a simetria acabou. O preset `pr.intertemporal` deve passar a gravar, junto com a escolha, a informação de que a opção 'ultratividade' contraria precedente vinculante.

### V-05 — Subjanela da MP 808/2017 (14/11/2017 a 22/04/2018)

- **correntes:** {'nome': 'aplicar o texto da MP no período em que vigeu', 'fundamento': 'a MP teve força de lei e produziu efeitos; atos praticados sob sua vigência são válidos'}; {'nome': 'ignorar a subjanela', 'fundamento': 'a MP perdeu eficácia sem decreto legislativo regulando as relações dela decorrentes, o que gera controvérsia sobre a disciplina do período'}
- **pontos sensiveis:** B03-F1; B03-F2; B03-F3; B04-F3; B04-F5
- **observacao:** Não resolvo. É a variante mais facilmente esquecida: cinco meses e nove dias dentro do período pós-reforma com regra própria para prêmios, abonos, gratificação de função, gorjetas e forma de pactuação da 12×36.

### V-06 — Verbetes que sobreviveram ao expurgo de 30/06/2025 apesar do conflito com a lei nova

- **correntes:** {'nome': 'verbete vigente vincula até cancelamento formal', 'fundamento': 'Súmula 85 (itens IV e VI), OJ 388 da SBDI-1 e Súmula 60, II não constam da Res. 225/2025'}; {'nome': 'verbete perdeu eficácia por confronto com a lei, independentemente de cancelamento', 'fundamento': "art. 177, I, do RITST, invocado nos 'considerandos' da própria Res. 225/2025: os verbetes em confronto com a Lei 13.467 'perderam a eficácia com a vigência da Reforma Trabalhista (11/11/2017)' — o cancelamento é declaratório, não constitutivo"}
- **pontos sensiveis:** B03-F4; B04-F5
- **observacao:** Não resolvo, e esta é a variante mais interessante do lote: o próprio TST escreveu, nos considerandos, a premissa que esvazia a sobrevivência formal dos verbetes que ele não cancelou.

### V-07 — Alcance da Súmula 291 (indenização pela supressão de horas extras) após a Reforma

- **correntes:** {'nome': 'Súmula 291 vigente e íntegra', 'fundamento': 'não foi cancelada pela Res. 225/2025; não há dispositivo novo sobre a matéria'}; {'nome': 'superada para supressões a partir de 11/11/2017', 'fundamento': 'art. 8º, § 2º, da CLT — súmulas não podem criar obrigações não previstas em lei'}
- **pontos sensiveis:** B03-F8
- **observacao:** Não resolvo. Se a segunda corrente prevalecer, o ponto do manual (a prescrição não reduz a contagem de anos) torna-se irrelevante para supressões pós-reforma, porque não haveria indenização a calcular.

### V-08 — Período aquisitivo de férias a cavaleiro de 11/11/2017 no regime de tempo parcial

- **correntes:** {'nome': 'tabela vigente no fechamento do período aquisitivo', 'fundamento': 'leitura do Tema 23 — fato gerador consumado'}; {'nome': 'tabela vigente no início do período aquisitivo', 'fundamento': 'expectativa formada sob a lei anterior'}; {'nome': 'rateio proporcional entre as duas tabelas', 'fundamento': 'nenhum fundamento normativo localizado'}
- **pontos sensiveis:** B03-F9
- **observacao:** Não resolvo e não infiro. Busca declarada abaixo (BN-6).

### V-09 — Feriado laborado em 12×36 a partir de 11/11/2017 quando a escala é irregular ou a norma coletiva prevê pagamento

- **correntes:** {'nome': 'sem dobra', 'fundamento': 'art. 59-A, parágrafo único — a remuneração mensal pactuada abrange feriados'}; {'nome': 'com dobra', 'fundamento': 'escala não validamente pactuada ou descumprida na prática; cláusula coletiva expressa de pagamento, validada pelo Tema 1046 do STF'}
- **pontos sensiveis:** B03-F3
- **observacao:** Não resolvo. É a sucessora datada da P11 do bloco 03: a divergência antiga (dois acórdãos do TRT-3) fica confinada aos fatos até 10/11/2017; esta é a divergência do período novo, e tem conteúdo diferente.

### V-10 — V-01

- **ponto relacionado:** F7-03
- **corrente A:** tese: Os juros de mora NUNCA integram a base do IR, qualquer que seja a natureza da obrigação inadimplida.; fundamento: TST, OJ 400 da SDI-1 (DEJT 02, 03 e 04/08/2010): 'Os juros de mora decorrentes do inadimplemento de obrigação de pagamento em dinheiro não integram a base de cálculo do imposto de renda, independentemente da natureza jurídica da obrigação inadimplida, ante o cunho indenizatório conferido pelo art. 404 do Código Civil de 2002 aos juros de mora.'; alcance: mais amplo que o Tema 808
- **corrente B:** tese: Os juros de mora não são tributados apenas quando acessórios de remuneração por exercício de emprego, cargo ou função; fora daí, o acessório segue a natureza do principal.; fundamento: STF, Tema 808 (RE 855.091), cuja tese é expressamente delimitada a 'remuneração por exercício de emprego, cargo ou função'; e a adaptação feita pelo STJ em recurso repetitivo (Tema 878) para compatibilizar sua jurisprudência anterior com o julgado do STF.; alcance: mais estreito
- **por que nao resolvo:** O Tema 808 não revogou a OJ 400, e a OJ 400 não foi cancelada. O STF decidiu um recorte; a OJ afirma a regra geral. A área de atrito é o espaço entre os dois: juros de mora sobre verbas indenizatórias, sobre honorários, sobre verbas rescisórias de natureza não remuneratória. Resolver isso é escolha jurídica do cliente, não determinação de cálculo.
- **registro no projeto:** O capítulo 15 do manual já trata a questão como divergência não resolvida, com duas correntes. Esta verificação CONFIRMA que a divergência persiste em 2026 — o que mudou é que uma das correntes ganhou apoio vinculante no seu recorte próprio.
- **encaminhamento:** Preset sem default, à semelhança de pr.imputacao. As duas correntes viram variante com fundamento.

### V-11 — V-02

- **ponto relacionado:** C8-02
- **corrente A:** tese: Afasta a fixação — nada é arbitrado contra o beneficiário.; fundamento: leitura de que a inconstitucionalidade do art. 791-A, § 4º, retira o próprio suporte da condenação
- **corrente B:** tese: Os honorários são fixados, mas ficam sob condição suspensiva de exigibilidade, sem abatimento dos créditos obtidos no processo.; fundamento: leitura conjugada com o art. 98, § 3º, do CPC
- **por que nao resolvo:** A diferença é irrelevante para o valor líquido do reclamante — em ambas as correntes nada se abate do seu crédito — mas relevante para a composição da conta e para o dispositivo. Não é matéria que o cálculo decida.
- **encaminhamento:** Registrar as duas; o efeito sobre o líquido é o mesmo.

### V-12 — V-03

- **ponto relacionado:** C12-01
- **corrente A:** tese: Deve ser prévia, expressa e INDIVIDUAL; autorização por assembleia não supre.; fundamento: leitura dos arts. 578 e 579 da CLT na redação da Lei 13.467/2017, e jurisprudência posterior do TST
- **corrente B:** tese: A autorização coletiva, por assembleia, é válida, à luz da valorização da negociação coletiva e do Tema 935 do STF sobre contribuição assistencial.; fundamento: analogia com o regime da assistencial pós-2023
- **por que nao resolvo:** Não consegui confirmar em fonte primária o precedente que fixa a exigência de individualidade. O enunciado desta fase pedia para verificar a exigência de autorização 'prévia, expressa e individual': CONFIRMEI 'prévia' e 'expressa'; NÃO CONFIRMEI 'individual'. Ver buscas_negativas, B-06.
- **encaminhamento:** Variante aberta, com lacuna de fonte declarada.

### V-13 — V-04

- **ponto relacionado:** F7-01
- **corrente A:** tese: Art. 20 da Lei 8.212/91, que permanece vigente e apenas sobrestado pela regra constitucional transitória do art. 28 da EC 103/2019.; fundamento: o art. 35 da EC 103/2019 traz lista exaustiva de revogações e NÃO inclui o art. 20 da Lei 8.212/91 — verificado no texto
- **corrente B:** tese: O art. 20 foi tacitamente revogado pela EC 103/2019, e as competências antigas regem-se por ele apenas como norma do tempo do fato.; fundamento: leitura de que a regra constitucional superveniente esvazia integralmente o dispositivo legal
- **por que nao resolvo:** Não muda o resultado numérico de nenhuma conta. Muda a fundamentação escrita no laudo, e laudo com fundamento errado é impugnável.
- **encaminhamento:** Registrar; a corrente A tem apoio textual direto verificado.

### V-14 — V-05

- **ponto relacionado:** F7-04
- **status:** JÁ REGISTRADA pelo projeto em 00-base-normativa.md § 1 ('Divergência doutrinária registrada'). Esta verificação não a resolve nem acrescenta fonte. Mantida como está.

---

## F. Buscas negativas, com escopo declarado

> *"Zero ocorrências no segmento" e "zero ocorrências em 471 páginas" são afirmações
> diferentes, e só a segunda sustenta uma negativa sobre o manual.*

| Afirmação | Escopo | Ocorrências |
|---|---|---|
| NÃO ENCONTREI verbete do TST editado em substituição à Súmula 437 ou à Súmula 90 após o cancelamento de 30/06/2025. | — | — |
| NÃO ENCONTREI cláusula de modulação de efeitos, ressalva de fatos anteriores ou regra de direito intertemporal no corpo da Res. 2… | — | — |
| NÃO ENCONTREI modulação de efeitos no acórdão do Tema 23 do TST. | — | — |
| NÃO OBTIVE o inteiro teor da Rcl 6.275 nem da Rcl 6.266 do STF. | — | — |
| NÃO OBTIVE o inteiro teor do Ag.Reg. na Rcl 53.157/PA do STF. | — | — |
| A ficha oficial do Tema 23 no portal do TST NÃO traz a tese firmada. | — | — |
| NÃO VERIFIQUEI a vigência da Súmula 46 do TRT-3 nem se o manual invoca a Súmula 48 do TRT-3. | — | — |
| NÃO CONSULTEI o PDF do Manual TRT-3 para conferir o texto das páginas citadas (35, 44, 45, 48, 59, 286, 291, 337). | — | — |
| A OJ 388 da SBDI-1 não foi cancelada nem alterada e permanece formalmente vigente. | — | Nenhum registro de cancelamento ou alteração. |
| As Súmulas 85, 354, 362, 291, 264, 340 e 60 do TST não constam de cancelamento. | — | Nenhuma delas figura no rol. A página oficial de cancelamentos não lista resolução posterior à 225/2025. |
| Não há alteração legislativa posterior à Lei 13.467/2017 nos arts. 4º, § 2º; 11; 58; 58-A; 59; 59-A; 59-B; 130-A; 134; 384; 457 e… | — | Todas as notas apontam para a Lei 13.467/2017 (ou, no art. 457, § 3º, para a Lei 13.419/2017; no art. 58, § 1º, para a Lei 10.243/2001; no art. 134, caput, para o DL 1.535/1977). Nenhuma norma posterior a 2017. |
| Não há precedente vinculante do TST sobre feriado laborado em 12×36 no período posterior a 11/11/2017. | — | Nada localizado. A jurisprudência permanece dividida. |
| Não há precedente vinculante do TST aplicando o art. 11, § 2º, da CLT à supressão de horas extras da Súmula 291. | — | Nada localizado. Localizei apenas manifestação doutrinária/jurisprudencial esparsa sustentando superação da Súmula 291 pelo art. 8º, § 2º — registrada como variante V4. |
| Não há regra legal nem precedente vinculante definindo a tabela de férias aplicável ao período aquisitivo de tempo parcial a cava… | — | Nada localizado. Mantido como variante V5, sem inferência. |
| SEM FONTE verificada para a nota do Ministério do Trabalho sobre a base do seguro-desemprego reproduzida no manual (6.13.4, p. 70… | — | Lacuna declarada, não fechada. |
| A lista completa dos verbetes cancelados pelo TRT-3, com as datas individuais de perda de eficácia, não foi obtida. | — | Confirmado o cancelamento das Súmulas 39 e 48 e a vigência da Súmula 46, mas sem o texto das resoluções administrativas nem as datas de perda de eficácia de cada verbete (exceto a Súmula 39: RA 123, de 20/08/2025, perda de eficácia a partir de 11/11/2017). |
| Inteiros teores não lidos. | — | Teses e datas conferidas em páginas oficiais dos tribunais; fundamentação não conferida. |
| — | www.planalto.gov.br e planalto.gov.br, via WebFetch, mais de dez tentativas em URLs disti… | INACESSÍVEL — fechamento de socket em 100% das tentativas por WebFetch; timeout de 60s no curl (rede direta bloqueada no ambiente). Também inacessíveis: www.in.gov.br (DOU), normas.receita.fazenda.gov.br (só redirecionamento), www.lexml.gov.br (HTTP 503), www2.senado.leg.br/bdsf (página de verificação de segurança), normas.leg.br (conteúdo renderizado por JavaScript). www2.camara.leg.br/legin respondeu HTTP 429 em todas as tentativas, ao longo de toda a sessão. |
| — | portal.stf.jus.br (detalhe de processo, repercussão geral, notícias), www.stf.jus.br, not… | HTTP 403 Forbidden em 100% das tentativas. jusbrasil.com.br também respondeu 403. |
| — | busca web dirigida ao tema DCTFWeb/reclamatória trabalhista; comunicados institucionais d… | NÃO ENCONTRADO. As fontes tratam da substituição em bloco (GPS → DARF 6092) sem mapear código a código. |
| — | não realizado — depende da leitura integral dos dois decretos, impossibilitada por B-01 | NÃO REALIZADO, e declarado como tal. |
| — | portal do STF (403); repositório de precedentes do TRT-3; busca web por transcrição liter… | NÃO OBTIDO EM FONTE PRIMÁRIA. Só consegui síntese secundária dos itens (i) e (ii), registrada em F7-04 com ressalva expressa. |
| — | busca web dirigida à ADI 5794 e à jurisprudência posterior do TST sobre autorização por a… | NÃO CONFIRMADO em fonte primária. A ADI 5794 decidiu a constitucionalidade da facultatividade, não a forma da autorização. |
| — | portal do STF (403); busca web | Apenas menção secundária aos três aditamentos (vedação de cobrança retroativa, não interferência de terceiros na oposição, razoabilidade do valor). |
| — | acórdão do STJ no REsp 1.850.512/SP — a transcrição do acórdão salta do § 4º para comentá… | § 5º reconstituído por busca, não lido em fonte primária. |
| — | portal do STF (403) | Apurado apenas em fonte secundária que os ED de 21/06/2022 foram rejeitados e que a decisão tem efeito ex tunc. |
| — | Planalto (socket fechado), DOU/in.gov.br (socket fechado), Legin da Câmara (HTTP 429, inc… | NÃO LIDOS. Uma das fontes secundárias consultadas sobre a Lei 14.973/2024 continha erro manifesto de transcrição de data ('até 31 de janeiro de 2025' onde deveria constar dezembro), o que é prova direta de que a via secundária é ruidosa neste ponto. |

