# Imputação e amortização — o que fazer com o que já foi pago

Fonte: `docs/calculo/consolidado/05-imputacao.md`; `04-descontos.md` § 4; `01-dominio-e-invariantes.md`
§§ 2.2 e 2.5; `armadilhas-comparador.md` § 3.

**É a operação que o produto mais usa.** Sempre que houve pagamento, depósito ou acordo antes do
resultado final — em qualquer polo — a conta passa por aqui.

---

## 1. A linha de base — sem amortização

Item 10.1 do manual:

```
principal corrigido  →  juros sobre o CORRIGIDO  →  descontos
```

**Os juros incidem sobre o principal corrigido, não sobre o nominal.** É a decisão mais
consequente do item, e o manual oferece dois critérios **idênticos ao centavo** (1.303,71 pelos
dois).

**A ordem entre correção e juros é INDIFERENTE** — distributividade, delta `0,00` verificado:

```
manual : (4.066,41 × 1,02538895) × (1 + 31,266667%) = 5.473,36
inversa: (4.066,41 + 4.066,41 × 31,266667%) × 1,02538895 = 5.473,36
```

**O que altera é a BASE**, e as três diferenças foram medidas:

| Decisão | Efeito |
|---|---|
| juros sobre o **nominal** em vez do corrigido | **−2,48%** |
| idem, com juros vincendos | **−3,15%** |
| deduzir INSS **antes** dos juros na base de IR | **−R$ 285,83** |

> **A pergunta "qual a ordem das operações?" tem resposta *não importa*. A pergunta produtiva é
> "sobre que base cada uma incide?".**

**Uma regra enunciada, rara neste capítulo:** *"na hipótese do cálculo envolver juros vincendos,
**o segundo critério torna-se obrigatório**"* — p. 209. **Mas a obrigatoriedade não tem lastro
demonstrativo em todo o manual:** `obrigatór*`, `porque` e `razão` → **zero ocorrências nas pp.
266–277**. E o par de exemplos que deveria exercitá-la **dá delta 0,00** pelos dois critérios: o
critério 1 é **inexecutável a partir do publicado**, porque nenhum exemplo informa data de
ajuizamento nem percentual acumulado. Pendência **`P10D-04`**.

---

## 2. Com amortização — a linha do tempo se parte em duas

**A amortização não é um passo a mais no fim.** Tudo é trazido até a data do levantamento,
**rateado ali**, e só então levado ao marco final.

Roteiro do item **10.3.1** (letras **A–H, J** — **neste item não existe letra I**):

| | Passo |
|---|---|
| **A** | **decompor** — excluir os juros do saldo (*"descarregar"*) |
| **B** | atualizar o principal **sem juros** até a data da amortização |
| **C** | aplicar juros do ajuizamento até a data da amortização |
| **D** | `= B + C` — bruto devido |
| **E** | **deduzir o valor pago, NOMINAL** → saldo remanescente |
| **F** | **ratear o saldo entre principal e juros, por PROPORÇÃO** |
| **G** | atualizar o principal de F.1 da dedução até o marco final |
| **H** | atualizar os juros de F.2 e incidir juros do período restante sobre G |
| **J** | `= G + H` |

```
F.1  principal no saldo = (B / D) × E
F.2  juros     no saldo = (C / D) × E
```

**O valor pago é deduzido NOMINAL.** O que se atualiza é o **crédito**, trazido até a data da
amortização. **Nenhuma linha de levantamento tem coluna de índice preenchida.**

### 2.1 Bruto ou líquido — depende do subitem

| Item | Incide sobre |
|---|---|
| **10.3.1** (sem descontos) | o **bruto** |
| **10.3.2.1** (com descontos) | o bruto **já reduzido do INSS e IR proporcionais ao levantamento** |

**Consequência que a moldura não enuncia:** no 10.3.2.1 os **tributos também são rateados**
proporcionalmente entre principal e juros. **Regra estrutural que só existe na aritmética.**

### 2.2 São DUAS molduras, com letreiros diferentes — e os exemplos seguem a segunda

**Ler o capítulo 10 com um letreiro só produz erro de endereço.** O item **10.3.2** (pp. 239–241)
**não** repete a moldura de 10.3.1: vai de **A a O/P** e **tem letra I**.

| Passo | Em **10.3.1** | Em **10.3.2** |
|---|---|---|
| rateio proporcional | **F** | **G** |
| atualizar o principal | **G** | **H** |
| atualizar os juros | **H** | **I** |
| soma final | **J** | **J** |

**Os Exemplos 5 e 6 seguem 10.3.2, não 10.3.1** — embora o enunciado do capítulo descreva a
moldura de 10.3.1. E é por 10.3.2 que se entra no caso "com descontos" de § 2.1.

> **A afirmação "não há letra I" vale só para 10.3.1.** Repetida sobre o capítulo inteiro, ela
> apaga a letra I de 10.3.2 — que é justamente a alternativa **sem exemplo** da pendência
> **`P10D-05`**.

---

## 3. A regra de imputação — e a ausência que a define

**É proporcional.** Confirmada nos cinco exemplos, fechando exato (`F.1 + F.2 = E`).

**E não tem fundamento normativo declarado. Escopo das buscas, declarado:**

| Termo | Escopo | Ocorrências |
|---|---|---|
| `art. 354` · `354 do C` · `artigo 354` | **471 páginas** | **0** |
| `354` · `imputa` · `Código Civil` · `Súmula` · `anatocismo` | segmento que a aplica | **0** cada |
| `proporcional` | mesmo segmento | **101** |

> **Aplicada 101 vezes, fundamentada zero.** A única justificativa é aritmética — evitar
> anatocismo, *"descarregar"* o saldo.
>
> **Não são duas normas concorrentes: são uma norma — o art. 354 do CC — contra um costume de
> liquidação sem base declarada.**

### 3.1 Quanto custa a escolha

```
amplitude = min(abatimento, principal, juros) × índice_residual × pct_juros_residual
```

| Caso do manual | Amplitude R$ | Amplitude % |
|---|---|---|
| EXEMPLO de 10.3.1 | 36,60 | 0,25% |
| **Exemplo 1** | **9.918,92** | **23,83%** |
| Exemplo 5 | 22.272,55 | 15,85% |
| Exemplo 6 | 2,51 | 0,05% |

**Direção: juros primeiro produz saldo MAIOR, logo dívida maior. O art. 354 favorece o CREDOR; o
critério proporcional favorece o DEVEDOR.**

> **Armadilha de previsão.** O Exemplo 5 tem **quase o dobro** da participação de juros do Exemplo
> 1 e amplitude percentual **menor** — porque ali o limitante é o **abatimento**, não os juros.
> **Qual das três grandezas limita muda de caso para caso.** Quem raciocinar só por "quanto de
> juros há no bruto" erra a previsão.

**Modelagem:** preset **`pr.imputacao`, sem default** — quarto caso de `R20-EXCEÇÃO`, e **o único
em que o problema não é o corpus deixar a questão aberta, mas a prática não ter norma**. Escolher
um default seria o motor **tomar posição jurídica**. Pendência **`P11B-07`**.

---

## 4. `R23` — descarregar antes de aplicar juros

Antes de aplicar juros sobre saldo remanescente, **os juros já contidos nesse saldo devem ser
excluídos**; do contrário há **anatocismo**. Efeito medido: no Exemplo 5 do capítulo 10,
**+R$ 30.452,43** — **o maior delta de método do corpus**.

**Anomalia de localização do fundamento.** O manual **executa** a operação em todo o **cap. 10** e
a nomeia apenas como *"descarregar"* (`pagina_pdf` **237**, **única ocorrência da palavra nas 471
páginas**), **sem fundamentá-la** — `anatocismo` tem **0 ocorrências em todo o capítulo 10**. Quem
a qualifica é uma **minuta de petição do cap. 16** (`pagina_pdf` **328**), que abre com a **mesma
frase** do item 10.3.1 e acrescenta: *"não incidindo juros sobre juros (anatocismo), vedada por
Lei"*.

**E são duas regras anti-anatocismo distintas que o manual nunca reúne:**

1. **juros acumulam por SOMA de percentuais, nunca por multiplicação** — `pagina_pdf` 16, **única
   invocação da Súmula 121 do STF** no manual;
2. **o descarregar** — `pagina_pdf` 237.

---

## 5. O item "i" da ADC 58 — e por que o conflito é condicional

O bloco 11B marcou como **maior atrito do projeto** o conflito entre o rateio e a modulação. **A
distinção de duas situações o dissolve.**

| | **i.1 — pagamento consolidado** | **i.2 — execução questionada** |
|---|---|---|
| **Quando** | pago sem qualquer questionamento, ou com trânsito em julgado | execução instaurada **após o início dos debates da ADC 58**, com **questionamento expresso** de qualquer das partes |
| **Recalcula o pago?** | **não** | **sim** |
| **Índices do STF incidem sobre** | só o que **falta pagar** | **inclusive o já pago** |
| **O rateio se aplica?** | **Não — não há o que ratear.** O pago sai da conta | **Sim**, sobre valores recalculados pelo critério novo |

**Alcance da proteção dentro de i.1:**

| Alcança | **Não** alcança |
|---|---|
| depósito com **finalidade de pagamento** | **depósito recursal** |
| **valor incontroverso liberado** ao reclamante | a **parte controversa** do depósito em garantia |

> **Não é que o manual esteja certo e a modulação errada, nem o contrário.** É que o método do
> manual — **recompor o bruto até a data do pagamento antes de deduzir** — é **exatamente o que a
> modulação veda em i.1**, e **exatamente o comportamento correto em i.2**. Conflito
> **condicional**, não estrutural. Por isso vira preset, não correção.

**Preset `pr.adc58-item-i`**, eixo composto: estado processual ⊕ questionamento expresso ⊕
**natureza do depósito**. **Tem default — i.1**, que é a regra; i.2 é declarada exceção.

**Ordem de avaliação, por R22:** `pr.adc58-item-i` **antes** de `pr.imputacao`. **Em i.1 a
imputação sequer é consultada** para o valor pago.

> **Origem declarada.** O desdobramento i.1 × i.2 vem de **pesquisa jurisprudencial externa ao
> corpus**, conferida em **fontes secundárias**. **O inteiro teor dos três precedentes do TST não
> foi lido**, e `portal.stf.jus.br` respondeu **HTTP 403 em 100% das tentativas** — a modulação
> **não tem transcrição literal verificada**. **Confirmar antes de produção:** a distinção decide
> se o critério do STF alcança valores já pagos.

---

## 6. A data da dedução — TRÊS posições no mesmo manual

| Onde | Data | Fundamento citado | Classificação |
|---|---|---|---|
| **Cap. 10**, todos os exemplos | **levantamento** | **nenhum** — `Súmula` e `16.4.11` têm zero ocorrências no segmento; *"cap. 10: zero em 69 páginas"* | **NACIONAL** — prática aritmética sem veículo regional |
| **Cap. 16, item 16.4.11** (pp. 333–334) | **duas teses**, separadas pela finalidade do depósito | **Súmula 15 do TRT-3** | **REGIONAL — é a única das três apoiada em verbete de TRT** (`R1`) |
| **Cap. 14**, p. 306, letra "c" | **pagamento**, *"salvo determinação do juízo"* | — | **NACIONAL** — alinha-se ao regime de precatórios e à ADC 58, item "i" |

**O critério que separa as duas teses do 16.4.11, e que o manual nomeia:**

| Indício | Leitura |
|---|---|
| **código na guia** — *"código 02"* | depósito **para pagamento** |
| **cronologia** — *"precedeu aos embargos e agravo de petição"* | depósito **em garantia** |

| Finalidade | Dedução | Consequência |
|---|---|---|
| **garantia** da execução | data do **levantamento** | há diferença a apurar |
| **pagamento** | data do **depósito** | *"não há diferença a ser apurada"* |

A tese do pagamento exige ainda que o depósito seja do **total** da execução e **já atualizado**
até a data do depósito.

> **Este é o eixo `natureza_do_deposito` do preset `pr.adc58-item-i`.** Não foi invenção da
> modelagem: **é o critério que o próprio manual usa** — só que numa minuta, e o capítulo que
> executa a dedução em 56 páginas **nunca o cita**.

**Não harmonizado.** Pendências **`P11B-06`** e **`P13C-01`**. **E retirar a Súmula 15 não apaga o
critério:** apaga o **eixo de escolha** entre os dois, porque as posições 1 e 3 **coincidem em
resultado** com os dois ramos da tese regional.

---

## 7. Descontos sob pagamento parcial — a ordem é inversa

**O manual não distribui os descontos: reconstrói o bruto primeiro.** Íntegra em
[`descontos-inss-irrf.md`](descontos-inss-irrf.md) § 4.

```
1.  do LÍQUIDO levantado, achar o VR. BRUTO LEVANTADO   (fórmula fechada)
2.  ratear o INSS:  (VB / TB) × INSS_devido_na_data
3.  recalcular o IR do zero:  base = VB × IPIR − INSS_proporcional
```

**O IR não é rateado** — é apurado de novo, com alíquota e parcela a deduzir da tabela do **mês do
levantamento**. E **nos ramos "sem juros" há duas razões distintas no mesmo exemplo:** `VB/TB`
para o INSS e `TBSJ/TBCJ` para expurgar os juros da base do IR.

> **O rateio de 10.2 não é o de 10.3.** Em 10.3 rateia-se **principal × juros**; em 10.2, **bruto
> → INSS**. Objetos distintos, sem conflito numérico — **e a mesma lacuna: nenhum dispositivo é
> citado para nenhum dos dois** (`P13A-02`).

---

## 8. Armadilhas desta operação

| # | Onde | Erro |
|---|---|---|
| **A11** | pp. 227, 231 → 244, 250 | fórmula do bruto com **colchete fechado cedo demais** — lida à risca dá `318.618,21` contra `322.389,94`. **Com `INSS = 0` as duas leituras coincidem**, e os exemplos do 12-B usam INSS zero |
| **A2** | pp. 269, 271 | **BLOQUEIO** — delta de **2.036,51**, índice implícito `1,00257222` **sem origem**; `55.236,01` **não existe em nenhuma das 471 páginas**. Propaga: J `138.448,90 → 140.485,41`; IR `4.162,83 → 4.468,30` |
| **A3** | p. 266 | **BLOQUEIO** — delta de **10,00 exatos** na coluna K, **não absorvível por arredondamento**. Para fechar seria preciso `H = 1.350,52`, que **não resulta de operação alguma do exemplo** |
| **A1** | p. 297 | juros do FGTS **contados duas vezes** — excesso de `3.802,63` |
| **A4** | p. 223 (origem: 261) | **linha copiada com a multa junto** — `+125,11` e `+1.168,21`, que são **20% de outra coluna**, embora a p. 220 declare *"sem a inclusão da multa"* |
| **A9** | pp. 266, 271 | o título do **Exemplo 6 é cópia literal do Exemplo 5**, inclusive *"juros incluídos na base de cálculo do IR"* — **contra o próprio parâmetro do Exemplo 6, que é a OJ 400**. Dois exemplos de teses **opostas** parecem tratar da mesma |
| **A10** | pp. 239, 241, 267–268, 276 | **duplicações de letra e numeração fantasma** — § 2.2 e `armadilhas-comparador.md` |
| **A8** | p. 209 | remissão cruzada ao *"tópico 7.3"* (Aplicação do IPCA-E) onde deveria ser **7.6** (juros de mora) |

**Os dois bloqueios seguem abertos. Nenhum é arredondamento.** `A9` e `A10` estão no § 2 de
`armadilhas-comparador.md` — *"defeitos sem efeito de valor, mas que confundem o leitor"*: **não
mudam número; mudam o que o leitor pensa estar lendo.**

---

## 9. Pendências desta seção

| # | Pendência |
|---|---|
| `P11B-01` · `P10D-01` | os dois bloqueios — coluna K erra **10,00 exatos** (p. 266) · delta de **2.036,51** com índice sem origem (p. 269) |
| `P11B-07` | **o critério proporcional não tem norma.** Preset sem default; a questão jurídica segue aberta |
| `P10D-04` | a obrigatoriedade do critério alternativo da letra C, **declarada e não demonstrada** |
| `P11B-06` · `P13C-01` | **três posições** sobre a data da dedução, no mesmo manual |
| `P10D-05` | a alternativa da **letra I de 10.3.2** não tem exemplo em lugar nenhum do capítulo 10 |
| `P10D-08` | **migração de regime tributário** dentro do mesmo cálculo (Ex. 5) — caso único, **sem disciplina**: `migra*`, `transição` e `dois regimes` → **zero nas 471 páginas** |
| `P13A-02` · `P13A-03` | os **dois rateios sem fundamento** · **falta a regra de escolha da base do IR com/sem juros** (`OJ 400` → 0 nas pp. 223–237) |
| — | **origem externa do item "i"** — inteiro teor dos três precedentes **não lido** |
