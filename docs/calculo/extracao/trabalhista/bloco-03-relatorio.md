# Bloco 3 — relatório

Manual de Cálculos do TRT-3, capítulo 6 (verbas trabalhistas), **itens 6.1 a 6.6**,
páginas 18 a 54. Fase 2 do pipeline, tipo *prosa e raciocínio*: validação **adversarial**.

Nenhuma skill escrita.

| | |
|---|---|
| Espinha | `bloco-03-verbas.md` |
| Detalhe | `bloco-03-verbas-detalhe.md` |
| Escopo coberto | 6.1 base de cálculo · 6.2 aviso-prévio · 6.3 13º · 6.4 férias + 1/3 · 6.5 RSR e feriados · 6.6 horas extras |
| Pontos marcados para a Fase 4 | 9 |
| Erros materiais do original | 11 |
| Pendências abertas | 7 (P7 a P13) |

---

## 1. Onde o bloco termina

O prompt dava **p. 18 a 82**; o escopo por item (6.1 a 6.6) **termina na p. 54**. As duas
coisas não coincidem porque o capítulo 6 tem quinze itens, não seis.

O que fica de fora, com páginas, está inventariado na § 0 da espinha: **6.7 a 6.15,
p. 55 a 82** — horas *in itinere*, sobreaviso, prontidão, intervalos, adicionais,
indenizações, multas, salário-família, FGTS e diferenças salariais. O capítulo 7
(atualização monetária e juros) abre na **p. 83**, confirmando a fronteira da triagem.

Não comprimi o final: parei no limite do item, como instruído.

**Não existe item 6.12** na numeração impressa — salta de 6.11 (p. 59) para 6.13 (p. 67).
Pendência P7.

---

## 2. A data do manual está errada nos metadados do repositório

Achado que afeta os três blocos já extraídos.

`fontes.md` e `00-base-normativa.md` § 10 registram **julho/2016**. Evidência recolhida:

| Evidência | Página |
|---|---|
| A **capa não traz data** — só a composição da direção do Tribunal | 1 |
| Acórdão do **IRR-849-83.2013.5.03.0138**, julgado em **21/11/2016**, publicado em **19/12/2016**, transcrito na íntegra | 38–39 |
| Salário mínimo de **01/01/2017** (R$ 937,00) | 381 |
| Tabela de IRRF **jan/2017 a dez/2017** | 386 |
| Contribuição previdenciária **jan/2017 a dez/2017** | 399 |
| Calendários até **2020** e tabelas de RSR até **2020** | 460–466 |

O documento é, no mínimo, **de 2017**.

**Por que importa.** Não é detalhe bibliográfico: muda o que se pode afirmar sobre a
defasagem do manual. Ele **não é anterior ao IRR-849** — transcreve o acórdão e comenta a
revisão esperada da Súmula 124. Continua anterior à Lei 13.467/2017, cuja vigência é
11/11/2017.

**O que foi feito.** `fontes.md` recebeu nota com a evidência; o valor declarado não foi
sobrescrito. `00-base-normativa.md` **não foi tocado** — é fonte de verdade do usuário.
Registrado em `pendencias.md` § 11.

---

## 3. O que saiu

**Espinha**, por verba: base de cálculo e o que a integra; fórmula de apuração; regra de
proporcionalidade; incidência de INSS, FGTS e IRRF; reflexos; súmulas e OJs que governam
cada ponto. Mais o índice completo dos 26 verbetes do item 6.6.1, com marcação dos que o
manual cita mas não desenvolve.

**Detalhe**: 21 seções de exemplos literais, todos reconferidos com `Decimal` em precisão
30.

Fórmulas extraídas como fórmula:

```
dias_aviso   = 30 + 3 × anos_completos                    (teto 90)
13º          = remuneração_dez × meses_civis_≥15d / 12
férias        = base × doze_avos_em_dias_corridos / 12
HE_mensal    = remuneração / divisor × adicional(nº índice) × nº_HE
adicional_HE = remuneração / divisor × (adicional − 1) × nº_HE   (Súm. 85 e 340)
HE_mensal    = HE_semanal × 4,285714
hora_noturna = hora_relógio × 1,142857                    (= 8/7 = 60/52,5)
reflexo_RSR  = valor_HE × nº_RSR / dias_úteis
reflexo_FGTS = valor_HE × 0,112                           (0,08 × 1,4)
reflexo_aviso = média_12m / 30 × dias_de_aviso × valor_unitário_HE
indenização_supressão = média_12m × valor_HE_supressão × n_anos
```

### 3.1 Os cinco pontos de atenção especial do escopo

| Pedido | Onde está | Achado |
|---|---|---|
| Divisores e a tese do IRR-849 | Espinha § 6.3 e 6.3.1 | As **seis teses** transcritas, com a **modulação** — que é a parte operacional: título silente sobre divisor, em liquidação, segue o IRR |
| **OJ 394** | Espinha § 6.6.2 | Texto transcrito e a história completa: OJ 16 do TRT-3 → cancelada → OJ 394. Responde ao caso difícil nº 6 da Fase 3 |
| Projeção do aviso sobre os doze avos | Espinha §§ 2.3, 3.5, 4; detalhe §§ 3.1 e 6.4 | O manual repete o alerta em três itens; as duas demonstrações estão no detalhe |
| **Abono pecuniário** | Espinha § 4.9; detalhe § 8 | As duas formas somam **exatamente R$ 7.500,00**. A equivalência declarada é verdadeira — conferida |
| Ficção legal da hora noturna | Espinha § 6.5.4; detalhe § 13 | Os dois exemplos e a interação com HE. O caso de 19h–08h: **13 horas de relógio viram 14 legais** |

---

## 4. Validação adversarial

Dois revisores independentes, sem o contexto desta extração, lentes distintas, sem que um
visse o trabalho do outro.

| Revisor | Pergunta | Achados |
|---|---|---|
| A | Que regra do original ficou de fora? | 9 relevantes, 12 menores |
| B | Que afirmação da espinha não tem respaldo? | 3 graves, 14 menores |

O revisor B recalculou **toda** a aritmética do detalhe com `Decimal`. Veredicto: "Nenhuma
conferência do arquivo de detalhe está errada." Os onze erros materiais apontados no
original foram confirmados um a um, inclusive o diagnóstico de que o valor publicado em
§ 6.2 corresponde a 5/12 e não aos 4/12 declarados.

### 4.1 A omissão estrutural — e é a mais séria

**O item 6.6.1 inteiro não havia sido extraído como unidade.** É o índice de súmulas e OJs
aplicáveis ao cálculo das horas extras, e o escopo pedia expressamente "6.6 Horas extras,
**incluindo súmulas aplicáveis**". Dos 26 verbetes listados, 11 não sobreviviam em nenhum
ponto da extração.

Corrigido: o índice está agora reproduzido integralmente na espinha (§ 6.1-A), com **◆**
marcando os verbetes que o manual cita mas não desenvolve. Dois pesam de verdade:

- **Súmula 102** — a gratificação de função do bancário não inferior a 1/3 do salário **já
  remunera a 7ª e 8ª horas**. Define *se há* horas a pagar; a Súmula 124 e o IRR-849 só
  definem *por qual divisor*. Sem ela, o cálculo de bancário parte da premissa errada.
- **Súmula 39 do TRT-3** — o descumprimento do intervalo de 15 minutos do art. 384 da CLT
  gera pagamento **como hora extra**. Parcela autônoma que não aparecia em lugar nenhum.

Registrado como pendência **P13**.

### 4.2 Graves aceitos e corrigidos

| # | Achado | Correção |
|---|---|---|
| B1 | Eu havia apresentado as fontes da remuneração "**em ordem de confiabilidade declarada**". O manual não declara ordem nenhuma — e a ordenação que inventei colocava a CTPS **acima** dos recibos, invertendo a única preferência que o manual enuncia | Ordem removida; a preferência pelos recibos ficou isolada e literal |
| **B2** | "O manual registra que o **penúltimo** caso é a hipótese mais comum". O manual diz "**esta última**", referindo-se a *devidas superiores às pagas → dedução pelo valor*. Eu havia atribuído a frase à linha anterior, **invertendo o default de fato** do critério de dedução | Corrigido com a citação literal |
| B3 | "Carnaval não é feriado. […] O manual **acolhe a decisão sem ressalva**". O manual introduz aquele bloco de transcrições dizendo que "não há consenso jurisprudencial acerca da matéria" | Reenquadrado como conclusão **do acórdão**, com a ressalva do manual ao lado |

**B2 é o pior dos três.** Não é imprecisão de redação: inverte qual critério de dedução o
manual sinaliza como o usual, e a escolha entre deduzir pelo número ou pelo valor move o
resultado — os §§ 19 e 20 do detalhe, partindo dos mesmos dados, chegam a R$ 98,26 e
R$ 98,19.

### 4.3 Menores aceitos

**Do revisor B** — quatorze, todos corrigidos. Os que importam:

- **Proveniência errada**: reflexo proporcional no aviso é 6.6.6.3, não 6.6.6.4; FGTS do
  aviso trabalhado está na p. 20, não na 19; aspas de "tópico específico deste manual" são
  da p. 29, não da 37.
- **Acréscimos meus a texto do manual**: "art. 7º, **XVI**" (o manual cita só "CF, 7º");
  "7 dias **corridos**"; "a hora noturna tem **52 minutos e 30 segundos**".
- **Supressões que ampliam a regra**: eu havia escrito "norma mais favorável" onde o manual
  diz "norma **infralegal** mais favorável".
- **Aspas alteradas ou truncadas**: "Descabe falar" por "descabendo em falar"; OJ 415
  terminando em "do contrato" em vez de "do contrato **de trabalho**"; elisão não sinalizada
  na ementa da coisa julgada.
- **"Revogou"** onde o manual diz "modificando o entendimento" (Nota Técnica 184/12 ×
  Memo. Circular 10/11).
- **Generalização**: "frações de ano são desprezadas **nos dois entendimentos**" — o manual
  só o afirma do segundo.
- **Remissão do manual**: o original remete ao "item **5.3.2**", que **não existe** — o
  item 5.3 não tem subitens numerados (bloco 2). Agora citado como está, com a nota.

**Do revisor A** — relevantes incorporados além do índice 6.6.1:

- **Súmula 276/TST e art. 487, *caput* e § 6º** — o aviso é direito **irrenunciável** e
  integra sempre o período contratual. Faltava a natureza da verba (nova § 2.0).
- **OJ SDI-I Transitória** sobre o 13º de 1994: o desconto do adiantamento tem **piso** —
  "não podendo a 2ª parcela ser inferior à metade do 13º salário, em URV". Regra de
  apuração com teto implícito, não regra de conversão.
- **Critérios da Lei 9.093/1994** para feriados, transcritos dentro de um acórdão: limite
  de **quatro** feriados religiosos municipais e o feriado de **centenário do Município**.
  São eles que fecham o rol contável.
- **Lei 9.528/97** como marco inicial da controvérsia do INSS sobre o aviso indenizado — a
  história começava em 2009 na minha versão.
- Regras de **juntada de documentos** (Prov. 01/89, art. 31 do Provimento Geral, Resolução
  CSJT 136/2014), com a instrução de que "deve ser exigido das partes".

### 4.4 Não aceitos

| Achado | Por quê |
|---|---|
| A18/A19 parcialmente — detalhes de formato de papel (216 × 356 mm, A-4) e do § 1º do art. 31 | A regra e a instrução estão extraídas; as dimensões não afetam cálculo |
| A14 — Súmula 333 e art. 896, § 4º, da CLT dentro da ementa | São óbices processuais de conhecimento do recurso, não regra de cálculo |
| A17 — recorte do pedido no acórdão da 12×36 | Aceito e incorporado, na verdade |
| Observação de B sobre §§ 0 e 11 da espinha não serem verificáveis | Correta, mas não é achado: o recorte dado ao revisor terminava na p. 54, e aquelas afirmações vêm do survey de p. 55–83 |

---

## 5. Erros materiais do original — registrados, não corrigidos

| # | Onde | Erro |
|---|---|---|
| 1 | 6.4, p. 29 | **Férias proporcionais do horista.** A memória diz `195,67 × 9,09 × 4/12`, que dá **592,88**; o valor publicado é **741,10**, que corresponde a **5/12**. O erro propaga para o 1/3 (247,03) e o total (988,13) |
| 2 | 6.6.5, p. 42 | `10 × 4,285714 = 42,857`, e o manual publica **42,8**. Propaga como 42,80 por todas as tabelas seguintes. Equivale a usar o fator 4,28 |
| 3 | 6.6.6.4, p. 46 | A segunda rota do reflexo no aviso é impressa como `133,08 **×** 30 × 39`. Com multiplicação daria 155.703,60. A operação é **divisão**; o resultado publicado (173,00) está certo |
| 4 | 6.2, p. 22 | "Período trabalhado: **03/10/15** a 30/07/15" — admissão posterior à demissão. O mesmo exemplo diz "admitido em 03/10/14" |
| 5 | 6.2, p. 23 | A coluna de comissões atualizadas soma **12.849,09**; o total impresso é 12.849,08. A média publicada fecha com os dois |
| 6 | 6.6.4, p. 39 | Base impressa como "R$ **3.0000**,00" — um zero a mais. A conta usa 3.000,00 |
| 7 | 6.6.6.4, p. 46 | "Vr. Unitário da HE no mês de **dez/02**" num exemplo de 2010 |
| 8 | 6.6.6.5, p. 47 | "Média física de **fev/02 a jan/03**" no mesmo exemplo de 2010/2011 |
| 9 | 6.6.7, p. 51 | "Somatório […] dividido por 12 = **312,86 / 2** = 26,07". O divisor da conta é 12 |
| 10 | 6.6.6, p. 45–48 | Remissões internas a "**6.7.5.1**", "6.6.5.2", "6.6.5.3" etc., quando os itens são **6.6.6.x**. Numeração cruzada de uma versão anterior |
| 11 | 6.6.5, p. 41 | Remissão ao "item **5.3.2**", que não existe — o item 5.3 não tem subitens numerados |

**Os erros 7, 8 e 10 têm a mesma origem**: o exemplo-mestre das horas extras foi
renumerado e reambientado de 2002/2003 para 2010/2011 numa revisão, e sobraram referências
à versão antiga.

### 5.1 O erro 1, em detalhe

É o único que muda um resultado sem aviso. A análise desta extração — não do manual — é que
**os 4/12 estão certos e o 741,10 é o outlier**: o período aquisitivo declarado (02/05/15 a
31/07/15) mais a projeção de 33 dias a partir de 31/07 chega a 02/09/15, fechando o quarto
mês. O valor com 4/12 seria R$ 592,88, com 1/3 de R$ 197,63 e total de R$ 790,51.

Nada foi alterado no arquivo de detalhe: os números publicados estão lá como impressos, com
as duas contas lado a lado.

---

## 6. A cadeia de arredondamento — o achado técnico do bloco

O manual **não enuncia** critério de arredondamento em nenhum ponto do capítulo 6. Os
exemplos revelam **duas práticas incompatíveis, em itens adjacentes**.

**Onde só a precisão plena reproduz o publicado** (tabela-mestre de HE, p. 42, e reflexo
no RSR, p. 44–45):

| Conta | Com o valor exibido | Com precisão plena | Publicado |
|---|---:|---:|---:|
| `3,92 × 32,14` | 125,99 | **126,00** | 126,00 |
| `4,26 × 32,14` | 136,92 | **136,96** | 136,96 |
| `4,26 × 42,80` | 182,33 | **182,39** | 182,39 |
| `182,39 × 5/26` | 35,08 | **35,07** | 35,07 |

**Onde só o valor exibido reproduz o publicado** (reflexos por média física, p. 45–47):

| Conta | Com o valor exibido | Com precisão plena | Publicado |
|---|---:|---:|---:|
| `31,24 × 4,26` (aviso) | **133,08** | 133,13 | 133,08 |
| `26,3 × 4,26 × 11/12` (13º) | **102,70** | 102,73 | 102,70 |
| `27,67 × 4,26` (férias) | **117,87** | 117,91 | 117,87 |

E na planilha de dedução (p. 50–51) **as médias também entram sem arredondamento**: o 13º/09
publicado (142,21) só fecha com a média plena 26,0717; com a exibida 26,07 daria 142,20.

> **Consequência.** A coluna "valor unitário da HE" é **apresentação em algumas tabelas e
> insumo em outras**, sem sinal que distinga. Um motor que fixe um único comportamento
> diverge do manual em metade dos exemplos.

Isto **agrava** a pendência aberta no bloco 2 (`pendencias.md` § 9-A): lá o problema era
divergência **entre** as duas fontes primárias — CJF trunca, TRT-3 arredonda. Aqui é
divergência **dentro** de uma delas, e não sobre o modo de arredondar, mas sobre **em que
ponto da cadeia** arredondar. Pendência **P10**.

---

## 7. Marcado para a Fase 4

Nove pontos afetados pela **Lei 13.467/2017**, identificados e **não corrigidos** — seção 8
da espinha. Os três de alta gravidade:

| # | Ponto | Dispositivo |
|---|---|---|
| **F1** | Base de cálculo integra **abonos e prêmios habituais** | CLT art. 457, §§ 1º e 2º |
| **F2** | Habitualidade como teste de integração, com lapso até anual | CLT art. 457, § 2º |
| **F3** | 12×36: feriado laborado pago em dobro | CLT art. 59-A, parágrafo único |

F1 e F2 atingem a **base de cálculo de todas as verbas do bloco**, não um item isolado.
F3 atinge justamente o ponto em que o manual já registrava dissenso jurisprudencial.

**O conteúdo novo de cada dispositivo não foi verificado** nesta extração — só o ponto de
impacto. Verificar é trabalho da Fase 4.

---

## 8. A base normativa não cobre este bloco

A instrução do escopo era: "Se o manual disser algo que a base contradiz, extraia como está
e marque com o item da base que conflita."

**Não há a quem apontar.** `00-base-normativa.md` trata de correção monetária, juros,
Fazenda Pública, invariantes R1–R13 e fixtures. Não tem uma linha sobre aviso-prévio, 13º,
férias, RSR ou horas extras.

Há exatamente **dois pontos de contato**, e os dois **confirmam** em vez de conflitar:

- **R8** (título > usuário > default) — o manual subordina-se expressamente ao comando
  sentencial em três itens distintos: aviso indenizado ("salvo se nos autos constar
  entendimento contrário"), base de cálculo das HE ("observando estritamente os limites
  impostos pelo comando exequendo") e OJ 394 ("deverão ser analisadas as decisões
  transitadas em julgado").
- **Regra 6 do plano** (divergência se registra) — o manual transcreve dois acórdãos
  opostos sobre o feriado na 12×36 e recusa-se a arbitrar.

É lacuna do corpus normativo, não do manual, e precisa ser fechada antes da Fase 4:
**contra o que se vai confrontar o capítulo 6?** Registrado em `pendencias.md` § 12.

---

## 9. Pendências abertas

| # | Pendência | Bloqueia |
|---|---|---|
| P7 | Não existe item 6.12 na numeração impressa | Inventário do capítulo 6 |
| **P8** | Duas constantes para 30/7 no mesmo documento: IRR-849 fixa **4,2857**, item 5.3 usa **4,285714** | Núcleo aritmético |
| P9 | Contradição interna sobre o multiplicador do reflexo de HE em férias indenizadas — prosa × quadro sinóptico | Reflexo em férias vencidas |
| **P10** | Cadeia de arredondamento: o manual alterna entre usar o valor exibido e a precisão plena, sem enunciar critério | Toda a apuração de HE |
| P11 | Critério do feriado na 12×36 sem árbitro — dois acórdãos opostos | Catálogo de critérios |
| P12 | A Súmula 124 não foi revista dentro do manual após o IRR-849 | Divisor de bancário |
| **P13** | Oito verbetes do índice 6.6.1 sem regra desenvolvida — com destaque para a **Súmula 102** (bancário) e a **Súmula 39 do TRT-3** (art. 384) | Cálculo de bancário; intervalo do art. 384 |

P10 e P13 são as que precisam de decisão antes do próximo bloco. P8 e P10 se somam à § 9-A
de `pendencias.md`.

---

## 10. O que este bloco entrega ao comparador

O escopo dizia que este é "o conteúdo de maior valor para o comparador". O que ficou
utilizável, em ordem de força:

1. **Regras de contagem que produzem números discretos e verificáveis** — doze avos de
   férias por dias corridos × 13º por mês civil, com o corte de 15 dias. Uma conta alheia
   que use a mesma regra nas duas verbas está errada, e isso é detectável sem recalcular
   nada.
2. **OJ 394** — reflexo de HE no RSR não repercute em férias, 13º, aviso e FGTS. Divergência
   de estrutura, não de valor: se a média usada para as demais verbas inclui o RSR, a conta
   diverge por construção.
3. **A regra do feriado no módulo semanal** — lançar a jornada normal no dia do feriado. No
   exemplo do manual, a diferença entre fazer e não fazer é **5h45 contra zero** na mesma
   semana.
4. **Comparação semanal × diária, adotando o maior** — os dois exemplos do manual mostram
   que nenhuma apuração domina a outra.
5. **A equivalência do abono pecuniário** — duas rotas, mesmo total, e o invariante de que
   o terço incide sobre 30 dias e nunca 40. É teste de arredondamento e de estrutura ao
   mesmo tempo.
6. **Saldo negativo mensal que viaja corrigido** (OJ 415) — "o calculista não poderá zerar a
   diferença negativa apurada no mês". Zerar é o erro mais comum e o mais fácil de detectar.
