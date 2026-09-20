# Armadilhas do comparador

**Para que este arquivo existe.** Um perito que usa o Manual de Cálculos do TRT-3 **reproduz
os erros do manual**. O motor precisa reconhecer o número errado — não para aceitá-lo, mas
para saber que a divergência tem causa conhecida e nomeá-la em vez de apenas acusar diferença.

Os defeitos estavam espalhados pelos relatórios de bloco. Aqui ficam num lugar só, com o que
o comparador precisa: **onde**, **o que está impresso**, **o que seria correto**, e a
**assinatura detectável**.

**Offset de paginação zero** — número impresso = página do PDF. Fonte:
`manual-de-calculo-trabalhista_2016-1.pdf`, julho/2016.

**Nada aqui foi corrigido no corpus.** Os defeitos ficam registrados como são; este arquivo é
índice, não errata aplicada.

---

## 1. Defeitos com efeito de valor

Ordenados por magnitude do erro.

### A1 — Exemplo 8 do capítulo 11: juros do FGTS contados duas vezes

| | |
|---|---|
| **`pagina_pdf`** | **297** (operandos na 296; total propagado na 298) |
| **Impresso** | `21.476,22` |
| **Correto** | `17.673,59` |
| **Erro** | **+3.802,63** |
| **Bloco** | 10 |

```
Principal corrigido   12.824,00 × 1,01087868 = 12.963,51
Juros corrigidos       3.761,71 × 1,01087868 =  3.802,63
Juros 36,333333% s/ principal corrigido     =  4.710,08
                                    TOTAL   = 21.476,22   ← impresso
```

Os **36,333333% já contêm** os 29,33% de juros até out/15 (`3.761,71 / 12.824,00`) mais 7%.
Os dois métodos coerentes convergem em `17.673,59`. **O excesso é exatamente a linha de juros
corrigidos.**

**Assinatura detectável:** a linha de juros aparece duas vezes na soma — uma explicitamente,
outra embutida no percentual. Testar se `pct_juros_total ≈ (juros/principal) + pct_periodo_novo`;
se sim e ambas as linhas somarem, há dupla contagem. Na **mesma página** o crédito principal
usa corretamente duas linhas — a incoerência é interna.

**Propaga** ao resumo e ao total de `292.265,29` (`pagina_pdf` 298).

> **Correção de página feita na consolidação.** O bloco 10 registrara `pagina_pdf: 296`. A
> linha do defeito e o percentual `36,333333` estão na **297**; a 296 traz os operandos.

### A2 — P10D-01: Exemplo 5 do capítulo 10, letra I

| | |
|---|---|
| **`pagina_pdf`** | 269 e 271 |
| **Impresso** | `53.199,50`; total **`154.874,90`** |
| **Correto** | `55.236,01`; total **`156.911,41`** |
| **Erro** | **−2.036,51** na linha, **−11,00** no total após propagação |
| **Bloco** | 11C |

```
53.063,01 × 1,04095137 = 55.236,01      impresso 53.199,50
índice implícito: 1,00257222 — não corresponde a índice algum do exemplo
```

**Assinatura detectável:** `53.199,50` ocorre **apenas nas pp. 269 e 271**; `55.236,01` **não
existe em nenhuma das 471 páginas**. Não é cópia de outro exemplo, não é transposição, não é
arredondamento. Origem desconhecida.

**Propaga:** J `138.448,90 → 140.485,41`; IR `4.162,83 → 4.468,30`.

### A3 — P11B-01: Exemplo 4 do capítulo 10

| | |
|---|---|
| **`pagina_pdf`** | 266 |
| **Impresso** | total `43.077,24` |
| **Correto** | total `43.088,23` |
| **Erro** | **−10,99** |
| **Bloco** | 11B |

```
coluna H, declarada (D + G):   976,82 + 384,69 = 1.361,51   impresso 1.360,52   Δ −0,99
coluna K, declarada (F + H + J), com os impressos:  5.181,98  impresso 5.171,98   Δ −10,00
```

**Assinatura detectável:** o delta de `10,00` **exatos** não é absorvível por arredondamento.
Para fechar K seria preciso `H = 1.350,52`, que não resulta de operação alguma do exemplo
(`373,70 / 3.184,55 = 11,735%`, não os 12,08% da Selic). **Dois desvios independentes, de
ordens de grandeza diferentes, na mesma linha.**

### A4 — Linha copiada da p. 261 para a p. 223, com a multa junto

| | |
|---|---|
| **`pagina_pdf`** | 223 (origem: 261) |
| **Impresso** | `956,19` e `8.912,54` |
| **Correto** | `831,08` e `7.744,33` |
| **Erro** | **+125,11** e **+1.168,21** — a multa |
| **Bloco** | 11A |

```
831,08   + 125,11   = 956,19      (125,11   = 625,56   × 20%)
7.744,33 + 1.168,21 = 8.912,54    (1.168,21 = 5.841,04 × 20%)
```

**Assinatura detectável:** a coluna F do quadro A–K não fecha com `C + D + E`, e a diferença
é **exatamente 20%** de outra coluna. `956,19` e `8.912,54` ocorrem em **duas páginas apenas,
223 e 261**; a multa que os explica ocorre **só na 261**. As *letras* das colunas foram
remapeadas na cópia ("col. G × Selic" na 223 contra "col. F × Selic" na 261); os *números*,
não.

**Agravante:** a p. 220 declara literalmente *"Aplicação apenas dos Juros Selic, sem a
inclusão da multa"*, e a própria coluna E vem `0,00`.

### A11 — Fórmula do bruto levantado com o colchete fechado cedo demais

| | |
|---|---|
| **`pagina_pdf`** | **227** e **231**; propaga para **244** e **250** |
| **Impresso (fórmula)** | `{ 1 – [(TB × IPIR – INSS) × ALIQ / TB] + (INSS / TB) }` |
| **Correto** | `{ 1 – [(TB × IPIR – INSS) × ALIQ / TB  +  (INSS / TB)] }` |
| **Erro** | **−3.771,73** (p. 227) e **−3.071,48** (p. 231) se a fórmula for seguida à risca |
| **Bloco** | 13A |

Com os parâmetros do próprio exemplo — `TB = 412.023,32`, `IPIR = 0,8340`,
`INSS = 1.871,37`, `ALIQ = 27,5%`, `TL = 282.500,00`, `PD = 723,95425`, `NMP = 48,5`:

```
literal, como impresso   → 318.618,21
com o colchete correto   → 322.389,94   = o valor impresso no manual   ✓
```

**Assinatura detectável, e é forte:** a fórmula publicada e o resultado publicado **não
coincidem**, e **o próprio manual publica a forma correta duas páginas depois** — item
10.2.2.1, `pagina_pdf` 233: `1 – [(TB x IPIR – INSS) x (ALIQ. / TB) + (INSS / TB)]`.

Mesma classe de A7 (gross-up): **fórmula errada, resultado certo**. Um motor que implemente o
que está escrito diverge; um que reproduza o resultado, não.

**Cuidado adicional:** com `INSS = 0` as duas leituras **coincidem**. Os exemplos do art. 12-B
usam `INSS = 0,00`, logo **não exercitam o defeito** — ele só aparece quando há INSS.

### A12 — Rótulo do cap. 9 ignora o juro Selic da cota-reclamante

| | |
|---|---|
| **`pagina_pdf`** | 132 (rótulo), 280 (onde a divergência aparece) |
| **Impresso** | `"(Vr. Bruto do recte + INSS recda) x 0,5%"` |
| **Correto** | a base real é `líquido + INSS recte COM Selic + INSS recda` |
| **Erro** | **35,29** no exemplo da p. 280 — a base dá 30.312,81 e não 30.277,52 |
| **Bloco** | 13B |

```
606,12 − 570,83 = 35,29     ← o juro Selic sobre a cota-reclamante
```

`bruto ≡ líquido + INSS recte SEM Selic`. O rótulo **só coincide quando o INSS não carrega
juro** — que é o caso nas três ocorrências do cap. 9 (pp. 132, 137, 163).

**Assinatura detectável:** a base impressa difere do bruto + INSS recda exatamente pelo juro
Selic da cota do reclamante. **Isto reclassifica o achado P10-18** de divergência normativa
entre capítulos para **defeito de rótulo**. E o `151,39` do bloco 10 **não é impresso em
nenhuma das 471 páginas** — era valor derivado.

### A13 — Base impressa errada no percentual de honorários

| | |
|---|---|
| **`pagina_pdf`** | 106 |
| **Impresso** | `(15% s/ 277.338,69)` → resultado `41.600,76` |
| **Correto** | a base é `277.338,39` |
| **Bloco** | 13B |

**Assinatura detectável:** 15% de 277.338,69 daria **41.600,80**; o impresso é **41.600,76**,
que é 15% de **277.338,39**. **O rótulo está errado e o resultado certo** — terceiro caso do
mesmo padrão (ver A7 e A11).

### A14 — Teto rural de 2011 fora do padrão de arredondamento

| | |
|---|---|
| **`pagina_pdf`** | cap. 12, tabelas rurais |
| **Impresso** | `10.867,51` |
| **Correto** | `10.867,32` pelo fecho da própria tabela |
| **Erro** | **0,19** |
| **Bloco** | 13C |

**Assinatura detectável:** os demais anos fecham com delta de **0,01**; este destoa em **0,19**
— uma ordem de grandeza acima do ruído de arredondamento do manual. Na mesma família: faixa de
2013 com **sobreposição** em `3.255,47` e **buraco de R$ 2,01**; faixa de 2014 com
`6.89.754,21` malformado.

### A15 — OJ 54 transcrita truncada e com erro na minuta

| | |
|---|---|
| **`pagina_pdf`** | 330 (errada) contra **77** (correta) |
| **Impresso** | *"não poderá **se** superior"* — falta o "r" — e a citação **omite o art. 412/2002 de dentro das aspas** |
| **Correto** | `pagina_pdf` 77, item 6.13.10, com o texto íntegro |
| **Bloco** | 13E |

**Assinatura detectável:** o mesmo verbete aparece duas vezes no manual, e a versão do capítulo
técnico é **mais completa** que a da minuta. A p. 77 ainda acrescenta duas regras ausentes da
p. 330: a correção começa **um dia após** o teto ser atingido, e *"A incidência de juros sobre
a multa é controversa."*

### A5 — Índice de dez/10 com monotonicidade quebrada

| | |
|---|---|
| **`pagina_pdf`** | 96 |
| **Impresso** | índice `1,012012029`, valor `313,76` |
| **Correto** | índice `1,012945924` (implícito) ou `1,012953512` (cruzado com a p. 98) |
| **Erro** | o índice, não o valor |
| **Bloco** | 9 |

`309,75 × 1,012012029 = 313,47`, mas o manual imprime `313,76`.

**Assinatura detectável, dupla:** (1) o índice impresso **quebra a monotonicidade** da série —
é **menor** que o de jan/11; (2) o somatório do manual fecha com o índice **implícito**, não
com o impresso. **O erro está no índice publicado, e o valor está certo** — o inverso do caso
usual.

### A6 — RESUMO GERAL do Exemplo 2 com o NM do Exemplo 1

| | |
|---|---|
| **`pagina_pdf`** | 254 |
| **Impresso** | `Nº de meses RRA: 11,10` e `8,90` |
| **Correto** | `10,8` e `9,2` (apurados no próprio Exemplo 2) |
| **Bloco** | 11B |

Também `Base de cálculo: 21.154,54` contra `21.155,21` apurado.

**Assinatura detectável:** o NM do resumo **não bate com o NM calculado no corpo do mesmo
exemplo**, e bate com o do exemplo anterior. Mesmo padrão de A4 — cópia entre exemplos.

### A7 — Gross-up publicado com sinal invertido

| | |
|---|---|
| **`pagina_pdf`** | 244 |
| **Impresso** | fórmula que, aplicada literalmente, dá `31.570,74` |
| **Correto** | `35.670,95` |
| **Erro** | **−4.100,21** se a fórmula for seguida à risca |
| **Bloco** | 11B |

**Assinatura detectável:** a **fórmula publicada está errada, o resultado impresso está
certo**. Com o denominador correto fecha exato. Um motor que implemente a fórmula como escrita
diverge; um que reproduza o resultado, não.

**Nota:** não reaparece no segmento D — lá o gross-up fecha exato nos dois exemplos.

---

## 2. Defeitos sem efeito de valor, mas que confundem o leitor

### A8 — Remissão cruzada errada: "tópico 7.3" onde deveria ser 7.6

`pagina_pdf` 209. O manual manda calcular os juros *"nos percentuais estudados no tópico
**7.3** deste manual"*. **O item 7.3 é "Aplicação do IPCA-E".** Juros de mora são o **7.6**.
Conferido no sumário impresso. **Bloco 11A.**

### A9 — Títulos idênticos dos Exemplos 5 e 6

`pagina_pdf` 266 e 271. O título do Exemplo 6 é **cópia literal** do Exemplo 5, incluindo
*"juros incluídos na base de cálculo do IR"* — **contradizendo seu próprio parâmetro, que é a
OJ 400** (juros **excluídos** da base). O que de fato os distingue é o primeiro *bullet* de
"Parâmetros", não o título. **Bloco 11C.**

**Consequência para quem lê rápido:** os dois exemplos parecem tratar da mesma tese quando
tratam de teses opostas.

### A10 — Duplicações de letra e numeração fantasma

| Onde | Defeito | Bloco |
|---|---|---|
| p. 239 | não existe letra **I** em 10.3.1 (sequência A–H, J), mas o EXEMPLO rotula sua linha final como `Demonstração item " I "` e a descreve como `(l + m)` — letras inexistentes | 11B |
| p. 241 | **duas letras `O`** e nenhuma `P` em 10.3.2.1, mas os Exemplos 1 e 2 rotulam o resumo como "P" | 11B |
| pp. 267–268 | o Exemplo 5 tem **duas letras D, duas E, duas G e duas H** | 11C |
| p. 276 | o mesmo principal impresso como **`11.731,57` e `11.731,37` na mesma página**; o correto é 11.731,37, e **a letra B, onde ele é calculado, imprime o errado** | 11C |

---

## 3. Os deltas de método — o que o comparador procura

Diferente da seção 1: aqui não há erro do manual. São **decisões de método** que produzem
números distintos, e cuja divergência o comparador deve saber nomear.

### 3.1 Base dos juros e ordem dos descontos

| Decisão | Efeito medido | Bloco |
|---|---|---|
| Juros sobre o principal **nominal** em vez do corrigido | **−2,48%** | 11A |
| Idem, em cálculo com juros vincendos | **−3,15%** | 11A |
| Deduzir INSS **antes** dos juros na base de IR | **−R$ 285,83** | 11A |

**A ordem entre correção e juros é indiferente** — distributividade, delta 0,00 verificado.
O que altera é a **base**.

### 3.2 Imputação de pagamento parcial — a mais cara

```
amplitude = min(abatimento, principal, juros) × índice_residual × pct_juros_residual
```

**Qual das três grandezas limita muda de caso para caso.**

| Caso do manual | Amplitude R$ | Amplitude % |
|---|---|---|
| EXEMPLO de 10.3.1 | 36,60 | 0,25% |
| **Exemplo 1** | **9.918,92** | **23,83%** |
| Exemplo 5 | 22.272,55 | 15,85% |
| Exemplo 6 | 2,51 | 0,05% |

**Direção:** juros primeiro produz saldo **maior** — o art. 354 do CC favorece o **credor**; o
critério proporcional do manual favorece o **devedor**.

**Armadilha de leitura:** o Exemplo 5 tem quase o dobro da participação de juros do Exemplo 1
e amplitude percentual **menor**, porque ali o limitante é o **abatimento**. Quem raciocinar
só por "quanto de juros há no bruto" erra a previsão.

Ver `presets-regime.md` § 7.4 — `pr.imputacao`, sem default.

### 3.3 Anti-anatocismo: não descarregar

Aplicar juros sobre saldo que já os contém (violação de **R23**): no Exemplo 5 do capítulo 10,
**+R$ 30.452,43**. É o maior delta de método do corpus.

---

## 4. Comportamentos do manual que não são defeito

Registrados para que o comparador **não** os acuse.

**Precisão plena.** A aritmética é encadeada em precisão plena e **os números impressos com
duas casas não são os operandos**. Consequência: **as colunas impressas não somam os totais
impressos**, por 0,01 a 0,02. Provado em três exemplos independentes do capítulo 11 e em
quatro do 10.1.

**Não existe regra de arredondamento monetário no manual.** Buscas: `arredond` → 5 ocorrências
em 471 páginas, **todas** sobre o número de meses do RRA; `casas decimais` → **0**;
`truncad` → **0**.

**Mês comercial de 30 dias com contagem inclusiva.** `dias = 30 − dia_inicial + 1`. Testado em
cinco períodos: **5 de 5 fecham pela regra inclusiva, 0 de 5 pela exclusiva**. A fórmula
aparece nos exemplos (`31 x 1% + 8 x 1%/30`); a **convenção de contagem**, não.

**Tolerância de centavos.** Diferenças de 0,01–0,03 entre o recalculado e o impresso são
esperadas e decorrem dos três itens acima. **O limiar de alarme do comparador não deve ser
o centavo.**

---

## 5. Índice por página

| `pagina_pdf` | Armadilha |
|---|---|
| 96 | A5 — índice de dez/10 |
| 209 | A8 — remissão a 7.3 |
| 223 | A4 — linha copiada da p. 261 |
| 239, 241 | A10 — letras I e P |
| 244 | A7 — gross-up invertido |
| 254 | A6 — NM do Exemplo 1 no Exemplo 2 |
| 266 | A3 — bloqueio P11B-01 · A9 — títulos idênticos |
| 267–268, 276 | A10 — duplicações e duplo valor |
| 269, 271 | A2 — bloqueio P10D-01 |
| 106 | A13 — base do percentual de honorários |
| 132, 280 | A12 — rótulo ignora o Selic da cota-reclamante |
| 227, 231 (→ 244, 250) | **A11 — colchete da fórmula do bruto** |
| 296–298 | A1 — FGTS em dobro (linha na 297) |
| 330 | A15 — OJ 54 truncada |

---

## 6. Proveniência

| Seção | Origem |
|---|---|
| A1 | `extracao/trabalhista/bloco-10-fechamento.md` § 4.5 |
| A2, A9, A10 (Ex. 5) | `bloco-11c-vincendos.md` §§ 7 e 10 |
| A3, A6, A7, A10 (letras I/P) | `bloco-11b-amortizacao.md` §§ 4 e 6.1 |
| A4, A8 | `bloco-11a-imputacao.md` § 5 |
| A5 | `bloco-10-fechamento.md` § 2.1 |
| § 3.1 | `bloco-11a-imputacao.md` § 3 |
| § 3.2 | `bloco-11b-relatorio.md` § 3 e `bloco-11c-relatorio.md` § 4 |
| § 3.3 | `bloco-11c-vincendos.md` § 6 |
| § 4 | `bloco-10-fechamento.md` § 4.1 e `bloco-11a-imputacao.md` §§ 4.1 e 5.4 |

Todos os valores foram reproduzidos em `decimal.Decimal` no bloco de origem, e os quatro de
maior impacto **foram reconferidos contra o PDF na consolidação**, com este resultado:

| | Verificação | Resultado |
|---|---|---|
| **A1** | `21.476,22` × coerente `17.673,59`, excesso `3.802,63` | confere |
| **A2** | `55.236,01` **não existe em nenhuma das 471 páginas**; `53.199,50` só nas 269 e 271 | confere |
| **A3** | `976,82 + 384,69 = 1.361,51` contra `1.360,52`; total `43.077,24` na p. 266 | confere |
| **A4** | `831,08 + 125,11 = 956,19`; **`125,11` ocorre só na p. 261** | confere |

**E a reconferência corrigiu uma página:** A1 estava registrado na 296 e a linha está na
**297**. É o tipo de erro que a verificação literal por script pega e a leitura não.
