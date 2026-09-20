# Bloco 11B — capítulo 10, segmento C: amortização de valor pago (art. 12-A)

Manual TRT-3, item 10.3, pp. 237 (offset 681) a 266 (offset 2141).
**Offset de paginação zero.** Detalhe em `bloco-11b-amortizacao-detalhe.md`.

Este é o segmento que responde à invariante **R10**.

---

## 1. A resposta: imputação proporcional

> **F — separar no saldo remanescente o principal dos juros, através de proporção em relação
> ao total do cálculo da seguinte forma:**
> — `pagina_pdf` 237, item 10.3.1. Repetido como letra **G** no item 10.3.2.1, `pagina_pdf` 239.

```
F.1  principal no saldo = (B / D) × E
F.2  juros     no saldo = (C / D) × E

B = principal corrigido até a data da amortização
C = juros do ajuizamento até a data da amortização
D = B + C  (bruto devido)
E = D − valor pago  (saldo remanescente)
```

**O pagamento parcial não abate juros primeiro nem principal primeiro: abate os dois na
proporção em que compõem o bruto.** Confirmado nos cinco exemplos do segmento, fechando
exato (`F.1 + F.2 = E` em todos).

### 1.1 E não há fundamento jurídico nenhum

Esta é a parte que decide R10, e é uma **afirmação negativa** — vai com a varredura que a
sustenta.

| Termo | Escopo | Ocorrências |
|---|---|---|
| `art. 354` · `354 do C` · `artigo 354` | **PDF inteiro, 471 páginas** | **0** |
| `354` | segmento C | **0** |
| `imputa` | segmento C | **0** |
| `Código Civil` | segmento C | **0** |
| `Súmula` | segmento C | **0** |
| `anatocismo` | segmento C | **0** |
| `proporcional` | segmento C | **101** |
| `proporção` | segmento C | 14 |

As três ocorrências de `imputa` no manual estão nas pp. 319–320, em minuta do capítulo 16, e
tratam de **imputar juros e multa previdenciários ao reclamante** — sentido inteiramente
diverso.

**A regra é aplicada 101 vezes e fundamentada zero.** A única justificativa que o manual
oferece é aritmética, não jurídica (`pagina_pdf` 237):

> "não se pode partir de determinado crédito de saldo remanescente da execução, que já
> contenha juros, para sobre ele aplicar juros novamente, sendo necessário **“descarregar”**
> o saldo dos juros (excluir os juros do saldo, para aliá-los sem acumulação)."

`descarregar` ocorre **uma vez em todo o manual**, nesta frase.

### 1.2 O que isso faz com R10

R10 afirma que cível e trabalhista tratam imputação por regras não unificáveis, e o enunciado
do bloco observou que a afirmação fora escrita sem a regra trabalhista extraída.

**R10 está fundamentada, e por uma razão mais forte do que se supunha.** Não é que as duas
regras sejam diferentes e cada uma tenha seu fundamento: é que **o critério trabalhista existe
como prática de cálculo sem base normativa declarada**, enquanto o civil tem artigo de lei.
Não são duas normas concorrentes — são uma norma e um costume de liquidação.

**Consequência para o motor:** o critério proporcional não pode ser derivado nem justificado
a partir do corpus. Tem de ser **preset de regime com fundamento declarado como "prática do
manual do TRT-3, sem norma citada"**, e o contraditório sobre ele é matéria do juízo, não do
cálculo. Pendência **P11B-07**.

---

## 2. Quanto custa a escolha

Medido em `Decimal`, variando **apenas** a ordem de imputação e mantendo todo o resto.

**Exemplo 1** (`pagina_pdf` 241), período residual longo — juros de 55,17%:

| Ordem | Saldo final | Δ R$ | Δ % |
|---|---|---|---|
| **Proporcional (manual)** | 41.621,41 | — | — |
| Juros primeiro (art. 354 do CC) | 46.026,28 | **+4.404,87** | **+10,58%** |
| Principal primeiro | 36.107,36 | −5.514,05 | −13,25% |

**Amplitude: R$ 9.918,92 — 23,83% do saldo.**

**EXEMPLO de 10.3.1** (`pagina_pdf` 238), período residual curto — juros de 1,13%:

| Ordem | Saldo final | Δ % |
|---|---|---|
| **Proporcional (manual)** | 14.851,42 | — |
| Juros primeiro | 14.877,64 | +0,18% |
| Principal primeiro | 14.841,04 | −0,07% |

**O efeito escala com o tempo residual × a participação dos juros no bruto na data da
amortização.** Num caso de 1 mês, 0,25% de amplitude; num de anos, 23,83%.

Reproduzi o **+10,58%** de forma independente, por caminho próprio — bate na terceira casa.

Comparando com os deltas do bloco 11A (−2,48%, −3,15%, −285,83), **a ordem de imputação é a
decisão mais cara já medida no corpus.**

### 2.1 Dedução nominal × atualizada

| Forma | Saldo final | Δ % |
|---|---|---|
| Nominal no marco final | 14.917,03 | +0,44% |
| Atualizada só por correção | 14.906,99 | +0,37% |
| Atualizada por correção + juros | 14.841,04 | −0,07% |
| **Método do manual** | **14.851,42** | — |

O método do manual fica entre a segunda e a terceira formas.

---

## 3. As respostas às perguntas obrigatórias

### 3.1 Data de referência — levantamento, e os três termos são a mesma data

A moldura usa **três** expressões: "data da amortização" (letra B), "data da dedução"
(letras F e G) e "data em que ocorreu o **levantamento**" (letra H). **Nos exemplos são
sempre a mesma data** — 26/04/16, 25/10/11, 17/02/16.

**Confirma o indício do bloco 11A.** Os exemplos dizem "levantou", e a letra H diz
"levantamento". Converge com o item 16.4.11 e a Súmula 15 do TRT-3.

**Mas o segmento não os cita.** `Súmula` e `16.4.11` → **0 ocorrências** no segmento C; ambos
existem nas pp. 333–334. E o 16.4.11 reconhece **duas teses** — dedução na data do
levantamento *ou* na do depósito. **O segmento C adota uma sem mencionar a outra.**
Incoerência interna do manual, registrada, não harmonizada. Pendência **P11B-06**.

### 3.2 O valor pago é deduzido NOMINAL

Não é atualizado antes de deduzido. O que se atualiza é o **crédito**, trazido até a data da
amortização (letras B e C); o pagamento entra pelo valor de face naquela data.

```
20.493,92 − 5.808,39 = 14.685,53
64.166,50 − 1.895,85 − 1.321,10 − 32.454,00 = 28.495,55
```

Busca que sustenta: nenhuma linha de levantamento tem coluna de índice preenchida.

### 3.3 Bruto ou líquido — depende do subitem, e a moldura não diz

Em **10.3.1** (sem descontos) a amortização incide sobre o **bruto**. Em **10.3.2.1** incide
sobre o bruto **já reduzido do INSS e do IR proporcionais ao levantamento**.

**Consequência que a moldura não enuncia:** os tributos passam a ser rateados
proporcionalmente entre principal e juros junto com o resto. É regra estrutural que só existe
na aritmética dos exemplos.

### 3.4 RRA — dois números de meses distintos

`NM` é variável e o segmento usa **dois**:

```
NMP (do valor levantado) = (líquido levantado / líquido devido na data) × NM total
NM do saldo              = NM total − NMP
```

Sobre base **líquida**. Valores apurados: 11,116 → **11,1** · 10,788 → **10,8** · 3,045 →
**3,0**.

**A regra de arredondamento nunca é declarada.** O `10,788 → 10,8` exclui truncamento e
sugere uma casa, half-up — mas é inferência. Pendência **P11B-02**.

### 3.5 Os exemplos não concordam entre si

**Catorze divergências catalogadas.** As três que afetam resultado:

- a **base do percentual de IR** muda de exemplo para exemplo;
- a **base de IR do saldo** é o bruto **com** juros no Exemplo 1 e o principal **sem** juros
  nos Exemplos 2, 3 e 4;
- **o mesmo exemplo** usa `0,9091` no levantamento e o **percentual pleno** no saldo.

---

## 4. BLOQUEIO — P11B-01

`pagina_pdf` 266, Exemplo 4. **Reportado como bloqueio, não contornado.**

A coluna H é declarada `(col. D + col. G)`:

```
976,82 + 384,69 = 1.361,51     impresso: 1.360,52     delta −0,99
```

A coluna K é declarada `(col. F + col. H + col. J)`. **Mesmo usando os valores impressos**, dá
`5.181,98` contra os `5.171,98` impressos — **delta de 10,00 exatos**. Para fechar seria
preciso `H = 1.350,52`, que não resulta de operação nenhuma do exemplo (`373,70 / 3.184,55 =
11,735%`, não os 12,08% da Selic).

**São dois desvios independentes, de ordens de grandeza diferentes, na mesma linha.** O
segundo não é absorvível por arredondamento.

**Propaga até o total.** O `TOTAL DO CÁLCULO EM 31/05/16 = 43.077,24` — que eu havia usado
como marca de fronteira do segmento — deveria ser **43.088,23**.

---

## 5. A pendência herdada NÃO reaparece

O bloco 11A deixou `2.820,40` e `5.109,98` (p. 215) com delta 0,44 sem via declarada, e o
enunciado mandou tratar como bloqueio se o padrão se repetisse.

**Não se repetiu.** O único delta próximo (0,45, `pagina_pdf` 251, "Valor bruto levantado sem
juros") **dissolve-se por completo**: o operando real é `34.611,2499` — não o `34.611,21`
impresso — combinado com a digitação `46.893,02` onde o valor é `46.893,92`. Com os operandos
reais a conta fecha **exata** em 25.293,98. Classe: arredondamento + digitação, **não** regra
oculta.

Varridos os 29 deltas não-nulos do segmento: nenhum tem magnitude inexplicada daquela ordem.

**Mas apareceram duas regras ocultas novas** — o arredondamento do NMP (§ 3.4) e o percentual
pleno de IR no saldo contra 0,9091 no levantamento (§ 3.5).

---

## 6. A moldura contra os exemplos

### 6.1 Defeitos da própria moldura

- **Não existe letra `I`** em 10.3.1: a sequência é A–H, J. Mas o EXEMPLO rotula sua linha
  final como `Demonstração item " I "` e a descreve como `(l + m)` — **letras que não existem**
  no demonstrativo, que vai de `a` a `j`.
- **10.3.2.1 tem duas letras `O`** e nenhuma `P` (`pagina_pdf` 241) — e os Exemplos 1 e 2
  rotulam o resumo como "P".
- As letras **deslocam** entre os dois subitens: `F/G/H/J` em 10.3.1 vira `G/H/I/J` em 10.3.2.1.

### 6.2 A hipótese que o manual chama de obrigatória não tem exemplo aqui

A letra C traz um critério alternativo em três passos, com a observação (`pagina_pdf` 237):

> "quando há juros vincendos no cálculo base para a atualização, **o segundo é obrigatório**"

**Nenhum dos cinco exemplos do segmento C o usa.** Os que exercitam juros vincendos são os
**Exemplos 5 e 6**, que estão no segmento D.

**Consequência de escopo:** o segmento C não contém um único exemplo da hipótese que a própria
moldura declara obrigatória. Ver § 7.

---

## 7. A fronteira do segmento, revista

O corte C/D foi fixado no bloco 11A entre o Exemplo 4 e o Exemplo 5, por mudança de regime
tributário (art. 12-A → 12-B). A varredura deste bloco mostra que **o corte parte uma
hipótese**:

- varredura de `^1[01]\.\d[\.\d]*` nas pp. 262–300: **nenhum heading numerado depois de
  `10.3.2.1`** (p. 239). Os Exemplos 5 e 6 continuam pendurados no mesmo item, que só termina
  por volta da p. 277;
- e são eles que exercitam o **critério alternativo da letra C** e os **juros vincendos** —
  a hipótese obrigatória.

**Registrado, não resolvido por conta própria.** A regra "limite de conteúdo vence limite de
página" recomendaria estender o segmento C até a p. 277, o que o fundiria com o D. Fica como
decisão para o 11C/11D, com a informação na mesa. Pendência **P11B-08**.

---

## 8. Contra a linha de base do 11A

O bloco 11A entregou, sem amortização: `principal corrigido → juros sobre o corrigido →
descontos`.

**Onde a amortização entra e o que altera:**

| Passo | Sem amortização (11A) | Com amortização (11B) |
|---|---|---|
| 1 | — | **decompor: excluir os juros do saldo** (letra A) |
| 2 | principal corrigido até a data-base | principal corrigido **até a data da amortização** (B) |
| 3 | juros sobre o corrigido | juros até a data da amortização (C) |
| 4 | — | **deduzir o pago, nominal** (E) |
| 5 | — | **ratear o saldo entre principal e juros, proporcionalmente** (F) |
| 6 | descontos | atualizar cada parte da data da dedução até o marco final (G, H) |

**A amortização não é um passo a mais no fim: ela parte a linha do tempo em duas.** Tudo é
trazido até a data do levantamento, rateado ali, e só então levado ao marco final. É por isso
que a escolha de rateio custa 23,83%: ela decide a composição do saldo que vai render juros
pelo período residual inteiro.

E o passo 1 — "descarregar" — é o que impede anatocismo. **Um motor que ignore a decomposição
e aplique juros sobre um saldo que já os contém produz juros sobre juros.**

---

## 9. Marcações para a Fase 4 — ADC 58

A modulação ressalva valores pagos e **veda dedução ou compensação de diferenças apuradas
pelo critério anterior**. O manual é de 2016 e opera sob TR + 1% ao mês.

**Aqui há conflito potencial real**, ao contrário do segmento A:

- todo o segmento C é **dedução de valor pago**, exatamente a operação que a modulação
  disciplina;
- o rateio proporcional distribui o pagamento entre principal e juros **calculados pelo
  critério antigo**. Se os juros forem recalculados pelo critério novo, a proporção muda, e
  com ela o saldo;
- a ressalva de valores pagos convive mal com um método que **recompõe** o bruto até a data do
  pagamento antes de deduzir.

Busca no segmento: `ADC`, `IPCA`, `EC 113`, `compensação de diferenças` → **0 ocorrências**,
como esperado num texto de 2016.

**Marcado, não harmonizado.** É o ponto de maior atrito entre o corpus extraído e a base
normativa vigente.

---

## 10. Pendências

| # | Pendência |
|---|---|
| **P11B-01** | **BLOQUEIO** — p. 266, Ex. 4: coluna H erra −0,99 e coluna K erra −10,00 exatos; o segundo não é arredondamento. Propaga ao total (43.077,24 → 43.088,23) |
| **P11B-02** | Arredondamento do NMP nunca declarado — inferido em 1 casa, half-up |
| **P11B-03** | Percentual pleno de IR no saldo contra `0,9091` no levantamento, no mesmo exemplo |
| **P11B-04** | Base de IR do saldo: bruto **com** juros no Ex. 1, principal **sem** juros nos Ex. 2–4 |
| **P11B-05** | Fórmula de gross-up publicada com sinal invertido (p. 244); com o denominador correto fecha exato |
| **P11B-06** | O segmento adota a dedução na data do levantamento sem citar a Súmula 15/TRT-3 nem o 16.4.11, que reconhece **duas** teses |
| **P11B-07** | **O critério proporcional não tem fundamento normativo declarado.** Tem de entrar como preset, não como regra derivada |
| **P11B-08** | O corte C/D parte a hipótese dos juros vincendos, que a moldura declara obrigatória |
