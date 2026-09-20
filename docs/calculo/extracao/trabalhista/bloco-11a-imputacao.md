# Bloco 11A — capítulo 10, varredura estrutural e item 10.1

Manual TRT-3, capítulo 10 — *Atualização de débitos trabalhistas*, pp. 209–277.
**Offset de paginação zero.** Detalhe em `bloco-11a-imputacao-detalhe.md`.

Este bloco entrega **o mapa do capítulo** e **o primeiro segmento**. Os demais ficam para
11B em diante, a partir do mapa do § 1.

---

## 1. Varredura estrutural — o capítulo tem quatro operações, não duas

Levantada do texto, não do sumário. O capítulo abre declarando sua própria divisão
(`pagina_pdf` 209):

> "Há basicamente dois tipos de atualização dos créditos:
> 1 - atualização sem amortização de valor pago;
> 2 - atualização com amortização de valor pago."

**A declaração do manual é insuficiente para dividir o trabalho.** Medido por script, o que
existe são quatro operações distintas:

| Seg. | Item | Operação | pp. | Nº | Caracteres |
|---|---|---|---|---|---|
| **A** | 10.1 | Atualização **sem** amortização | 209–**223 (parcial)** | 14+ | **41.471** |
| **B** | 10.2 | Descontos previdenciários e fiscais **proporcionais** | 223–236 | 14 | 41.228 |
| **C** | 10.3 | Amortização de valor pago — **RRA, art. 12-A** (Ex. 1 a 4) | 237–265 | 29 | 89.290 |
| **D** | 10.3 | Amortização — **ano-calendário / previdência, art. 12-B** (Ex. 5 e 6) | 266–277 | 12 | 33.694 |
| | | **total** | 209–277 | 69 | **205.683** |

Subitens impressos, conferidos no corpo: `10.1` (209) · `10.2` (223) · `10.2.1` (224) ·
`10.2.1.1` (224) · `10.2.1.2` (228) · `10.2.2` (233) · `10.2.2.1` (233) · `10.2.2.2` (235) ·
`10.3` (237) · `10.3.1` (237) · `10.3.2` (239) · `10.3.2.1` (239).

**A numeração impressa para em 10.3.2.1, na p. 239 — e o capítulo segue por mais 38
páginas.** A estrutura dessas 38 páginas **não é numerada**: são `Exemplo 1` (241),
`Exemplo 2` (248), `Exemplo 3` (255), `Exemplo 4` (262), `Exemplo 5` (266), `Exemplo 6`
(271). Quem dividir o capítulo pela numeração impressa perde 55% dele.

O corte C/D não é arbitrário nem por contagem de páginas: os Exemplos 5 e 6 são
**"Atualização com amortização para cálculo envolvendo rendimentos decorrentes do
ano-calendário do recebimento ou rendimentos pagos por entidades de previdência"** — regime
do **art. 12-B**, contra o **12-A** dos Exemplos 1 a 4. Regimes tributários distintos, com
metodologias que o próprio item 10.2 separa em 10.2.1 e 10.2.2.

### 1.1 A divisão sugerida para 11B em diante

| Bloco | Segmento | Por quê |
|---|---|---|
| 11B | **C** (10.3, Ex. 1–4) | **É onde a imputação vive.** Maior segmento, e o que responde R10 |
| 11C | **B** (10.2) | Descontos proporcionais; pré-requisito conceitual de C, mas C é mais urgente |
| 11D | **D** (10.3, Ex. 5–6) | Regime do art. 12-B, menor e mais especializado |

**Recomendo inverter a ordem documental e ir a C no 11B.** O produto precisa da regra de
imputação, e ela não está em 10.1 nem em 10.2.

### 1.2 A fronteira do segmento A não é uma quebra de página

**O item 10.1 não termina na p. 222.** O título `10.2` está no **offset 2.658 da p. 223**,
que tem 3.258 caracteres — os primeiros 2.658 ainda são 10.1, e contêm o fecho da 4ª
hipótese (Passos 6 e 7), o demonstrativo do art. 12-A, o quadro A–K e o RESUMO GERAL.

Isto **derruba uma premissa deste enunciado**, que fixava o corte em 222. Cortar ali partiria
a 4ª hipótese no meio do Passo 5 — e o achado mais grave do segmento (§ 5) está justamente
nesse trecho da p. 223.

---

## 2. O que 10.1 estabelece: a linha de base

**Correção do principal.** Literal, `pagina_pdf` 209:

> "o principal (total devido ao recte sem juros de mora) deve ser atualizado com os índices
> de correção monetária acumulados a partir do primeiro dia após a data final da última
> atualização. A título de exemplo, se o cálculo estiver atualizado até 31/12/15, o índice
> será acumulado a partir de 01/01/16."

**Mecânica da tabela única**, coerente com o bloco 9:

> "o índice constante em janeiro/16 na tabela de maio/16 corresponde à TR acumulada entre
> 01/01/16 a 31/05/16."

**Os juros incidem sobre o principal CORRIGIDO, não sobre o nominal.** É a decisão mais
consequente do item, e está nos dois critérios que o manual oferece.

### 2.1 Os dois critérios de juros, e quando um deixa de ser opcional

| | Critério |
|---|---|
| **(a)** | "aplicar o percentual/índice desde a propositura da ação sobre o valor corrigido" |
| **(b)** | corrigir o total de juros do último cálculo com o mesmo índice do principal; aplicar sobre o principal corrigido o percentual de juros do intervalo novo; somar os dois |

> "Quando o cálculo não envolver juros vincendos, o calculista poderá optar por qualquer um
> dos dois critérios, visto que os resultados finais são idênticos. Porém, na hipótese do
> cálculo envolver juros vincendos, **o segundo critério torna-se obrigatório**, visto que
> há parcelas vencendo após a inicial e sobre as quais incidirão taxas d[iferentes]"

**A identidade dos dois critérios foi conferida ao centavo:** 1.303,71 pelos dois. E a
obrigatoriedade do critério (b) sob juros vincendos é **regra enunciada**, não inferida.

---

## 3. A ordem das operações altera o resultado?

**Pergunta do enunciado. Resposta: não — mas a pergunta certa é outra.**

Testado em `Decimal`, na ordem do manual e na inversa:

```
manual : (4.066,41 × 1,02538895) × (1 + 31,266667%) = 5.473,36
inversa: (4.066,41 + 4.066,41 × 31,266667%) × 1,02538895 = 5.473,36
                                                   delta = 0,00
```

É distributividade. Corrigir-depois-juros e juros-depois-corrigir dão o mesmo número, e o
mesmo vale no exemplo com vincendos (3.386,10 nos dois métodos).

**O que altera o resultado é a BASE, não a ordem:**

| Decisão | Efeito medido |
|---|---|
| Juros sobre o principal **nominal** em vez do corrigido | 1.271,43 contra 1.303,71 — **−32,28 (−2,48%)** |
| Idem, no exemplo com vincendos | 3.279,61 contra 3.386,10 — **−106,49 (−3,15%)** |
| Deduzir INSS **antes** dos juros na base de IR | 4.824,15 contra 5.109,98 — **−285,83** |

**Consequência para o motor:** a comutatividade dispensa fixar a ordem entre correção e
juros, mas **não** dispensa fixar sobre que base cada um incide. As três decisões acima são
de base, e duas delas o manual não enuncia.

---

## 4. Regras que só existem dentro de exemplo

Doze achados estruturais. Os que mudam o motor:

### 4.1 AE01 — contagem de dias: mês de 30 dias, contagem inclusiva

O manual imprime a fórmula dentro do exemplo (`pagina_pdf` 209):

> "Juros 23/10/13 a 31/05/16 referente **31 meses e 8 dias** (31 x 1% + 8 x 1%/30)"

`31 + 8/30 = 31,266667%` — confere. De 23 a 30 contados de forma **inclusiva** dão 8 dias.
Testado em cinco períodos do item: **5 de 5 fecham pela regra inclusiva, 0 de 5 pela
exclusiva** (23/10 → 8 dias, não 7; 10/03 → 21, não 20; 11/06 → 20, não 19).

**O divisor 30 está à vista na fórmula; a convenção de contagem, não.** Buscas que sustentam:
`mês comercial` → 0 ocorrências nas pp. 209–223; `pro rata` → 0; `30 dias` → 0.

Um motor que conte dias corridos erra **um dia em todo período**.

### 4.2 AE07 — o índice de parcelas tributáveis é invariante aos juros

`5.450 / 7.858,90` e `7.085 / 10.216,57` são idênticos **até a 50ª casa decimal**. Ou seja:
incluir ou não os juros no numerador e no denominador não muda o índice. **O manual nunca
afirma isso**, e usa as duas formas em lugares diferentes — o que faz parecer divergência
onde há identidade algébrica.

### 4.3 AE08 — dois valores simultâneos e divergentes do mesmo INSS

**649,83 para deduzir** do crédito e **906,64 para recolher**. Convivem no mesmo exemplo.
Não é erro aritmético: são bases diferentes para finalidades diferentes, e o manual não
explica a distinção. Um motor que use um só número erra um dos dois lados.

### 4.4 AE12 — alíquota patronal de 23%, em 22 linhas, nunca enunciada

Constante em vinte e duas linhas do item. O capítulo 11 já exibira 22% no Ex. 1 e 21% no
Ex. 4, ambos **declarados nos dados**. Aqui o 23% não é declarado em lugar nenhum.

---

## 5. Defeitos do original

### 5.1 RT04 — uma linha copiada de outro exemplo, com a multa junto

O mais grave do segmento, e está no trecho da p. 223 que a fronteira errada teria cortado.

No quadro A–K, a coluna **F**, rotulada `Total recolhido a ser recolhido em junho/15`, traz
**956,19** e **8.912,54**. Mas `C + D + E` dá **831,08** e **7.744,33**.

Rastreados no manual inteiro, `956,19` e `8.912,54` ocorrem em **exatamente duas páginas:
223 e 261**. Na p. 261 o mesmo quadro tem dez colunas e inclui
`Multa (0,33% ao dia limitada a 20%)`, com 125,11 e 1.168,21 — que ocorrem **só na p. 261**. E:

```
831,08   + 125,11   = 956,19     ✓   (125,11   = 625,56   × 20%)
7.744,33 + 1.168,21 = 8.912,54   ✓   (1.168,21 = 5.841,04 × 20%)
```

**A linha de dados foi copiada da p. 261 sem remover a multa.** As *letras* das colunas foram
remapeadas — a p. 223 diz "col. G × Selic" onde a p. 261 diz "col. F × Selic" —, os *números*
não. E o contexto torna o erro inequívoco: a p. 220 declara literalmente
`"Obs.: Aplicação apenas dos Juros Selic, sem a inclusão da multa"`, e a própria coluna E vem
**0,00**.

**Não corrigido.** Registrado.

### 5.2 Remissão cruzada errada

`pagina_pdf` 209: *"Os juros, calculados nos percentuais estudados no tópico **7.3** deste
manual"*. **O item 7.3 é "Aplicação do IPCA-E".** Juros de mora são o **7.6**. Conferido no
sumário impresso.

### 5.3 Resíduos de versão anterior

Os valores `2.731,80`, `4.417,32`, `248,63` e o índice `1,023071044` ocorrem **apenas nas
pp. 215–216** e em nenhum outro ponto do manual — são restos de uma versão anterior do
exemplo, não recalculados. Um deles aparece num rótulo que anuncia `(2.731,80 × 110,70%)` e
produz 3.135,81, que é na verdade `2.832,71 × 110,70%`.

### 5.4 Operandos impressos que não são os operandos

Mesmo padrão do capítulo 11, agora confirmado em 10.1 por quatro provas independentes:
índices declarados `1,02538895` e grafados `1,025388925`; `1,039177731` grafado `1,03917731`;
percentual declarado `0,81777777` quando `25.890,35 / 31.659,54 = 0,8177740422`. **Nove somas
de coluna divergem dos totais impressos** em 0,01 a 0,02. `arredond` → **0 ocorrências** nas
pp. 209–223.

---

## 6. Confronto com os juros vincendos do capítulo 7

**Coincidem no resultado, divergem no procedimento.**

A tabela da p. 210 **não declara** a taxa integral nem a regra de decremento. Reconstruída
pela regra do cap. 7 — ação em 10/06/10 → taxa integral 18,70% → jun/10 = 18,70 − 0,70 =
18,00%, decremento de 1 p.p. ao mês — **as dez linhas impressas coincidem exatamente**
(set/10 15% … jun/11 6%), inclusive na contagem inclusiva de 21 dias.

A divergência é de método: o cap. 7 recalcula **linha a linha**; o 10.1 abandona isso na
reatualização e opera **em bloco**. Aqui dão o mesmo número (3.386,10) **só porque o
acréscimo de 53 p.p. é uniforme**. Se houvesse parcelas vencendo entre 01/01/12 e 31/05/16,
a regra do cap. 7 imporia decremento e **o método agregado de 10.1 superestimaria**.

**O manual não adverte.** Os dois registrados, sem harmonizar. Pendência **P11A-05**.

---

## 7. O que 10.1 NÃO responde

O enunciado pediu que estas perguntas não fossem presumidas. **Nenhuma delas é respondida
pelo segmento A** — por definição, já que 10.1 é a operação *sem* valor pago. Ficam para
11B/11C/11D, e são repetidas aqui para que o mapa as carregue:

| Pergunta | Onde deve estar |
|---|---|
| Ordem de imputação (juros primeiro, principal primeiro, proporcional) | 10.3, seg. C |
| Data de referência da dedução — pagamento, levantamento ou data-base | 10.3, seg. C |
| Valor pago é atualizado até a data-base antes de deduzido? | 10.3, seg. C |
| Descontos proporcionais sob pagamento parcial | 10.2 (seg. B) e 10.3 |
| Acordo: imputação com regra própria? | a confirmar — pode não estar no capítulo |
| A ordem altera o resultado? | **Respondida para 10.1: não.** Ver § 3 |

**Sinal já colhido, e forte.** Os seis exemplos do segmento C dizem *"o reclamante **levantou**
a quantia de R$ …"*, não "pagou". O capítulo 10 opera sobre a **data do levantamento** — o que
converge com o item 16.4.11 e a **Súmula 15 do TRT-3**, registrados no bloco 10. **Indício,
não conclusão:** a confirmação exige o texto de 10.3, e vai no 11B.

---

## 8. Invariante R10 — ainda não fundamentada nem derrubada

R10 afirma que cível e trabalhista tratam imputação por regras não unificáveis. **O segmento
A não toca a questão**, porque não há valor pago em 10.1.

O que o segmento A entrega para o julgamento de R10 é a **linha de base**: sem amortização, a
conta é `principal corrigido → juros sobre o corrigido → descontos`, e a ordem entre correção
e juros é indiferente por distributividade. **Qualquer regra de imputação de 10.3 será uma
alteração sobre esta base**, e é contra ela que o efeito deve ser medido.

---

## 9. Pendências

| # | Pendência |
|---|---|
| **P11A-01** | Fronteira 10.1/10.2 dentro da p. 223 (offset 2.658). Registrada; o trecho foi lido |
| **P11A-02** | `2.820,40` e `5.109,98` (p. 215) não reproduzem por via declarada alguma — delta 0,44. **Regra oculta, não arredondamento** |
| **P11A-03** | `15.375,82` diverge em +0,01 de **todas** as variantes testadas, e repete duas vezes — sugere arredondamento não-HALF_UP na planilha de origem |
| **P11A-04** | AE08 — dois valores simultâneos do mesmo INSS (649,83 deduzir × 906,64 recolher) sem critério declarado |
| **P11A-05** | Método agregado de juros vincendos de 10.1 × método linha a linha do cap. 7 — equivalentes só sob acréscimo uniforme |
| **P11A-06** | Alíquota patronal de 23% (AE12) nunca enunciada |
| **P11A-07** | Índices CSJT dos exemplos assumidos como dado; não conferidos contra a tabela do cap. 18 |

---

## 10. Marcações para a Fase 4

**ADC 58 — modulação.** A modulação ressalva valores pagos e **veda dedução ou compensação
de diferenças apuradas pelo critério anterior**. O manual é de 2016 e opera integralmente sob
TR + 1% ao mês.

**No segmento A a marcação é geral, não pontual:** todo o item 10.1 pressupõe o critério
pré-ADC 58. Não há, em 10.1, regra de dedução ou compensação de diferenças — logo **não há
conflito específico a marcar aqui**.

Busca que sustenta, rodada sobre as pp. 209–223:

| Termo | Ocorrências | Páginas |
|---|---|---|
| `compensa` | **0** | — |
| `dedução de diferenças` | **0** | — |
| `ADC 58` | **0** | — |
| `IPCA` | **0** | — |
| `amortiza` | 3 | 209 |
| `valor pago` | 3 | 209 |
| `levantamento` | 1 | **223** |

As três ocorrências de `amortiza` e `valor pago` estão todas na p. 209, e são a **declaração
da divisão do capítulo** — anunciam a operação do segmento C, não a executam. E a única
ocorrência de `levantamento` está na p. 223, **dentro do trecho que a fronteira errada do
enunciado teria cortado**.

**O conflito, se existir, estará no segmento C**, onde há valor pago e dedução. Marcado como
ponto de atenção obrigatório do 11B.
