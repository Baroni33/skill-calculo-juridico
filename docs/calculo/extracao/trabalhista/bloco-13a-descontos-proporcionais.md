# Bloco 13A — capítulo 10, segmento B: descontos proporcionais

Manual TRT-3, item 10.2, pp. 223 (offset 2.658) a 237 (offset 681). 39.656 caracteres.
**Offset de paginação zero.** Detalhe em `bloco-13a-descontos-proporcionais-detalhe.md`.

**Com este segmento o capítulo 10 está integralmente extraído.**

---

## 1. A ordem é inversa da que se esperava

A pergunta do enunciado era *"como INSS e IR se distribuem quando o pagamento é parcial?"*. A
resposta é que **o manual não distribui os descontos: ele reconstrói o bruto primeiro.**

```
1.  do LÍQUIDO levantado, achar o VR. BRUTO LEVANTADO   (fórmula fechada)
2.  ratear o INSS:  (VB / TB) × INSS_devido_na_data
3.  recalcular o IR do zero:  base = VB × IPIR − INSS_proporcional
```

Literal, sobre o INSS (`pagina_pdf` 227, 232, 234, 236):

> "dividir o valor bruto levantado pelo total bruto devido ao recte na data da amortização e
> multiplicar pelo valor da contribuição social devida na data do levantamento"

Aplica-se a **cota reclamante e cota reclamada**, com a ressalva de que a cota reclamada é
dispensada quando o fato gerador é a prestação de serviço.

**O IR não é rateado.** É apurado de novo, com alíquota e parcela a deduzir da tabela do **mês
do levantamento**.

### 1.1 Duas proporções diferentes no mesmo exemplo

Nos ramos "sem juros" o manual usa **duas razões distintas**:

| Razão | Para quê |
|---|---|
| `VB / TB` | ratear o **INSS** |
| `TBSJ / TBCJ` | expurgar os **juros** da base do IR |

Não é erro — são objetos diferentes. Mas é decisão estrutural que nenhum enunciado declara.

---

## 2. Critério próprio, e a mesma lacuna de fundamento

**O rateio de 10.2 não é o de 10.3.** Em 10.3 rateia-se **principal × juros**; em 10.2
rateia-se **bruto → INSS**. Objetos distintos, sem conflito numérico.

Mas **a lacuna é a mesma**: nenhum dispositivo é citado para o rateio. Busca no segmento:

| Termo | Escopo | Ocorrências |
|---|---|---|
| `art. 56` · `§ 1` · `3000/99` | segmento B | **0** cada |
| `art. 354` | segmento B | **0** |
| `art. 354` | **471 páginas** | **0** |

**O capítulo 10 inteiro aplica dois critérios de rateio e não fundamenta nenhum.**

---

## 3. O capítulo 9 delega — não há sobreposição

Achado literal, `pagina_pdf` 207:

> "**9.3.12 Imposto de renda proporcional ao valor pago** — O cálculo do imposto de renda
> proporcional ao valor pago **será detalhado no item 10.2**."

**O cap. 9 tem o fundamento e o 10.2 tem a operação.** O fundamento está na `pagina_pdf` 186:
art. 12-A § 1º, art. 12-B, art. 56 do Dec. 3000/99. **O item 10.2 nunca o repete.**

É o padrão do manual invertido: aqui o capítulo técnico *remete* ao outro capítulo técnico, e
a remissão funciona.

### 3.1 Mas há divergência de citação entre os dois

| Onde | Cita |
|---|---|
| **10.2.2** | arts. 26, **44 e 45** da IN 1500/14 |
| **9.3.8** | arts. 26, **43** e 44 da IN 1500/14 |

E o **art. 45 é a regra de meses do RRA — inaplicável ao art. 12-B**, que não usa meses. A
citação de 10.2.2 é a que está errada. Registrado, não corrigido. Defeito **D13A-12**.

---

## 4. O art. 12-B, que o segmento D não nomeava

Pendência herdada do bloco 11C: no segmento D a string `12-B` tem **zero ocorrências** e o
enquadramento foi por paráfrase. **Aqui está** — pp. 224 e 233.

**Hipótese de incidência, literal** (pp. 233 e 235, texto idêntico):

> "rendimentos referentes ao ano-calendário do recebimento, rendimentos pagos por entidades de
> previdência complementar e liberados ao reclamante até 10/03/15 e rendimentos pagos em
> cumprimento da decisão da Justiça do Trabalho e que não se enquadram ao disposto no art. 12-A"

| | 12-A | 12-B |
|---|---|---|
| Base | `VB × IPIR − INSS` | `VB × IPIR − INSS` |
| Alíquota | tabela do mês, sobre base **dividida por NM** | tabela **mensal** sobre a base **integral** |
| Parcela a deduzir | **× NM** | **única, sem multiplicação** |
| Nº de meses | **dois NM distintos** | **nenhum** |

Confirma o que o segmento D mostrara. **Código de recolhimento: ausente** — `código` e `5936`
têm zero ocorrências no segmento; o `5936` só existe no cap. 9, `pagina_pdf` 207.

---

## 5. A migração de regime continua sem disciplina

O Exemplo 5 do segmento D migra de regime tributário dentro do mesmo cálculo — caso único do
manual. **O segmento B não o disciplina.**

Busca que sustenta, nas 471 páginas: `migra*` → **0** · `transição` → **0** · `dois regimes`
→ **0**. No segmento: `11/03/15` → **0**; `10/03/15` → **2** (pp. 233 e 235), sempre **dentro
da hipótese do 12-B**, nunca como marco de transição.

O mais próximo continua sendo a `pagina_pdf` 190 ("duas apurações distintas"), que é **cisão
por ano-calendário**, não transição de regime. **Pendência P10D-08 permanece aberta.**

---

## 6. As três pendências do 11B — e duas eram erro meu

### 6.1 P11B-02 — RESOLVIDA. A regra É declarada

Escrevi nos blocos 11B e 11C que *"a regra de arredondamento do NMP nunca é declarada"*.
**Está declarada, duas vezes**, nas pp. 226 e 230 — no segmento que eu ainda não extraíra:

> "deverá ser observada a regra de arredondamento prevista no **parágrafo único do 45 da
> Instrução Normativa 1500/14**"

E o manual **transcreve o artigo**. Não é `ROUND_HALF_UP` — é regra de **três ramos**:

| 2ª casa decimal | Efeito |
|---|---|
| **< 5** | mantém a 1ª casa |
| **> 5** | acrescenta uma unidade à 1ª casa |
| **= 5** | **analisa a 3ª casa**: 0–4 mantém · 5–9 acrescenta |

**Difere de half-up na faixa `x,y50` a `x,y54`**, onde half-up sobe e a regra do art. 45
mantém. Vai para a espinha como **regra literal**, não como inferência.

Os dois NMP dos exemplos (48,5107 e 44,7478) **não discriminam** entre as duas regras — a
diferença só apareceria num NMP terminado em 50–54 no terceiro decimal.

### 6.2 P11B-03 — era erro meu de leitura

Registrei um contraste entre "percentual pleno de IR no saldo" e `0,9091` no levantamento.
**`0,9091` não é percentual de IR: é o IPIR** — índice das parcelas passíveis de IR. Rótulo
literal da `pagina_pdf` 244:

> "x 0,9091 **(índice parcelas passíveis IR)**"

Papel idêntico ao `0,8340` deste segmento. **O contraste que registrei não existe.** Fecha
como erro de leitura de rótulo.

### 6.3 P11B-04 — reaparece, e aqui é declarada

A inclusão ou exclusão de juros na base do IR é **bifurcação explícita de subitem**, quatro
vezes. Mesmo levantamento de `282.500,00` produz:

| | IR |
|---|---|
| **com** juros na base | `38.425,68` |
| **sem** juros na base | `13.551,75` |

**É parâmetro do método, não defeito.** O que falta é a regra de escolha: **`OJ 400` tem zero
ocorrências nas pp. 223–237** (21 páginas no manual, nenhuma no segmento).

---

## 7. Aritmética — tudo fecha, e nenhum bloqueio

44 operações em `Decimal`, prec=50. **Tudo fecha em 0,00 em precisão plena.**

Prova forte: a cadeia completa de 10.2.1.1 e 10.2.1.2 devolve exatamente
`282500.00000000000000000000` — **zero casas residuais**.

Caso demonstrativo do encadeamento: o IR de 10.2.1.2 com operandos **impressos** dá
`13.551,75575` (half-up → 13.551,76); em **cadeia plena** dá `13.551,753602` → **13.551,75**,
que é o impresso.

**Nenhum bloqueio.** O padrão de `10,00 exatos` e o do índice sem origem — que apareceram nos
segmentos C e D — **não reaparecem**. Maior delta: **0,66**, no item C de 10.2.1.2, com origem
identificada (divisor impresso `1,3309` contra o real `1,3309038604396459`). Classe:
arredondamento de planilha.

---

## 8. O defeito principal — e ele propaga para o segmento C

**D13A-01 / D13A-02, pp. 227 e 231 — colchete fechado cedo demais na fórmula do bruto.**

```
impresso:  { 1 – [(TB × IPIR – INSS) × ALIQ / TB] + (INSS / TB) }
correto:   { 1 – [(TB × IPIR – INSS) × ALIQ / TB  +  (INSS / TB)] }
```

Com os parâmetros do próprio exemplo (`TB = 412.023,32`, `IPIR = 0,8340`,
`INSS = 1.871,37`, `ALIQ = 27,5%`, `TL = 282.500,00`, `PD = 723,95425`, `NMP = 48,5`):

| Leitura | Resultado |
|---|---|
| **literal, como impresso** | `318.618,21` |
| **com o colchete correto** | **`322.389,94`** |
| **impresso no manual** | **`322.389,94`** |

**Delta de `3.771,73`, e a versão correta fecha em 0,00.** Verificado por mim.

**O próprio manual acerta a redação duas páginas depois**, em 10.2.2.1 (`pagina_pdf` 233):

> `VR. BRUTO LEVANTADO = (TL - PD) / 1 – [(TB x IPIR – INSS) x (ALIQ. / TB) + (INSS / TB)]`

**E a versão errada propaga para as pp. 244 e 250**, já no segmento C, com os mesmos
parênteses. Vai para `armadilhas-comparador.md`.

Na variante sem juros (p. 231) o mesmo defeito dá `294.331,05` contra `297.402,53` —
delta `3.071,48` — e há ainda um `)` órfão em `TBCJ)]`.

---

## 9. Limite de verificabilidade, declarado

Os exemplos do 12-B usam **`INSS = 0,00` e `IPIR = 100%`**. Portanto **os termos de INSS das
fórmulas de 10.2.2 nunca são exercitados numericamente** — a correção do colchete ali é
**inferida por comparação com 10.2.1, não verificada por número**.

Registrado como limite, não como conclusão.

---

## 10. Os exemplos concordam

Internamente e com os segmentos C e D. A fórmula de 10.2.1 é **a mesma** reproduzida nas
pp. 244 e 250 — **inclusive com o mesmo defeito de colchete**.

---

## 11. Pendências

| # | Pendência |
|---|---|
| **P13A-01** | Fórmula do bruto com colchete errado, pp. 227 e 231; propaga para 244 e 250 |
| **P13A-02** | Rateio de 10.2 **sem fundamento citado** — mesma lacuna de 10.3 |
| **P13A-03** | `OJ 400` ausente do segmento: a escolha entre base com e sem juros não tem regra |
| **P13A-04** | Código de recolhimento do 12-B ausente do segmento (só no cap. 9, p. 207) |
| **P13A-05** | Divergência de citação da IN 1500/14 entre 10.2.2 e 9.3.8 — o art. 45 é inaplicável ao 12-B |
| **P10D-08** | **Permanece aberta** — migração de regime tributário sem disciplina em todo o manual |
