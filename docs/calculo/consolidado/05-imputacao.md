# Imputação e amortização

Espinha consolidada. Amortização de valor pago, rateio principal × juros, o *descarregar*, e
o item "i" da modulação da ADC 58.

**É a operação que o produto mais usa** — quem está no polo passivo paga, deposita e acorda,
então quase toda conta tem valor pago antes do resultado final.

Fontes: blocos **11A**, **11B**, **11C**, **13A**; `../00-base-normativa.md` §§ 1.1 e 7;
`../confronto-normativo/01-vereditos.md`.

---

## 1. A linha de base — sem amortização

Estabelecida no bloco 11A, item 10.1 do manual:

```
principal corrigido  →  juros sobre o CORRIGIDO  →  descontos
```

**Os juros incidem sobre o principal corrigido, não sobre o nominal.** É a decisão mais
consequente do item, e o manual oferece dois critérios que **são idênticos ao centavo**
(1.303,71 pelos dois).

**A ordem entre correção e juros é indiferente** — distributividade, delta `0,00` verificado:

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

**Uma regra enunciada, rara neste capítulo:** *"na hipótese do cálculo envolver juros
vincendos, **o segundo critério torna-se obrigatório**"* — `pagina_pdf` 209.

> **Mas a obrigatoriedade não tem lastro demonstrativo em todo o manual.** `obrigatór*`,
> `porque` e `razão` → **zero ocorrências nas pp. 266–277**. E o par de exemplos que deveria
> exercitá-la **dá delta 0,00** pelos dois critérios: o critério 1 é **inexecutável a partir do
> publicado**, porque nenhum exemplo informa data de ajuizamento nem percentual acumulado.
> Pendência **P10D-04**.

---

## 2. Com amortização — a linha do tempo se parte em duas

**A amortização não é um passo a mais no fim.** Tudo é trazido até a data do levantamento,
**rateado ali**, e só então levado ao marco final.

Roteiro do item **10.3.1** (letras A–H, J — **neste item não existe letra I**):

| | Passo |
|---|---|
| **A** | **decompor** — excluir os juros do saldo ("descarregar") |
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

**O valor pago é deduzido nominal.** O que se atualiza é o **crédito**, trazido até a data da
amortização. Nenhuma linha de levantamento tem coluna de índice preenchida.

### 2.1 Bruto ou líquido — depende do subitem

| Item | Incide sobre |
|---|---|
| **10.3.1** (sem descontos) | o **bruto** |
| **10.3.2.1** (com descontos) | o bruto **já reduzido do INSS e IR proporcionais ao levantamento** |

**Consequência que a moldura não enuncia:** no 10.3.2.1 os **tributos também são rateados**
proporcionalmente entre principal e juros. Regra estrutural que só existe na aritmética.

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
> apaga a letra I de 10.3.2 — que é justamente a alternativa sem exemplo da **P10D-05**, § 7.

*Origem: `bloco-11c-vincendos-detalhe.md` §§ 3–4, pp. 237 e 239–241.*

---

## 3. A regra de imputação — e a ausência que a define

**É proporcional.** Confirmada nos cinco exemplos, fechando exato (`F.1 + F.2 = E`).

**E não tem fundamento normativo declarado:**

| Termo | Escopo | Ocorrências |
|---|---|---|
| `art. 354` · `354 do C` · `artigo 354` | **471 páginas** | **0** |
| `354` · `imputa` · `Código Civil` · `Súmula` · `anatocismo` | segmento que a aplica | **0** cada |
| `proporcional` | mesmo segmento | **101** |

> **Aplicada 101 vezes, fundamentada zero.** A única justificativa é aritmética — evitar
> anatocismo, "descarregar" o saldo.
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

**Direção: juros primeiro produz saldo MAIOR, logo dívida maior.** O art. 354 favorece o
**credor**; o critério proporcional favorece o **devedor**.

> **Armadilha de previsão.** O Exemplo 5 tem **quase o dobro** da participação de juros do
> Exemplo 1 e amplitude percentual **menor** — porque ali o limitante é o **abatimento**, não
> os juros. **Qual das três grandezas limita muda de caso para caso.**

**Modelagem:** preset **`pr.imputacao`, sem default** — quarto caso de `R20-EXCEÇÃO`, e o único
em que o problema não é o corpus deixar a questão aberta, mas **a prática não ter norma**.
Escolher um default seria o motor **tomar posição jurídica**.

---

## 4. O item "i" da ADC 58 — e por que o conflito é condicional

O bloco 11B marcou como **maior atrito do projeto** o conflito entre o rateio e a modulação. **A
distinção de duas situações o dissolve** — `../00-base-normativa.md` § 1.1.

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
> manual — **recompor o bruto até a data do pagamento antes de deduzir** — é **exatamente o que
> a modulação veda em i.1**, e **exatamente o comportamento correto em i.2**.
>
> Conflito **condicional**, não estrutural. Por isso vira preset, não correção.

**Preset `pr.adc58-item-i`**, eixo composto: estado processual ⊕ questionamento expresso ⊕
**natureza do depósito**. **Tem default** — i.1, que é a regra; i.2 é declarada exceção.

**Ordem de avaliação, por R22:** `pr.adc58-item-i` **antes** de `pr.imputacao`. Em i.1 a
imputação **sequer é consultada** para o valor pago.

> **Origem declarada.** A § 1.1 vem de **pesquisa jurisprudencial externa ao corpus**, conferida
> em fontes secundárias. **O inteiro teor dos três precedentes do TST não foi lido.** Confirmar
> antes de produção.

---

## 5. A data da dedução — três posições no mesmo manual

| Onde | Data | Fundamento citado |
|---|---|---|
| **Cap. 10**, todos os exemplos | **levantamento** | **nenhum** — `Súmula` e `16.4.11` têm zero ocorrências no segmento |
| **Cap. 16, item 16.4.11** (pp. 333–334) | **duas teses**, separadas pela finalidade do depósito | **Súmula 15 do TRT-3** |
| **Cap. 14**, p. 306, letra "c" | **pagamento**, "salvo determinação do juízo" | — |

**O critério que separa as duas teses do 16.4.11**, e que o manual nomeia:

| Indício | Leitura |
|---|---|
| **código na guia** — "código 02" | depósito **para pagamento** |
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

**Não harmonizado.** Pendência **P11B-06** e **P13C-01**.

---

## 6. Descontos sob pagamento parcial — a ordem é inversa

**O manual não distribui os descontos: reconstrói o bruto primeiro.**

```
1.  do LÍQUIDO levantado, achar o VR. BRUTO LEVANTADO   (fórmula fechada)
2.  ratear o INSS:  (VB / TB) × INSS_devido_na_data
3.  recalcular o IR do zero:  base = VB × IPIR − INSS_proporcional
```

**O IR não é rateado** — é apurado de novo, com alíquota e parcela a deduzir da tabela do **mês
do levantamento**.

**E nos ramos "sem juros" há duas razões distintas no mesmo exemplo:** `VB/TB` para o INSS e
`TBSJ/TBCJ` para expurgar os juros da base do IR.

> **O rateio de 10.2 não é o de 10.3.** Em 10.3 rateia-se **principal × juros**; em 10.2,
> **bruto → INSS**. Objetos distintos, sem conflito numérico — **e a mesma lacuna**: nenhum
> dispositivo é citado para nenhum dos dois.

Detalhe em `04-descontos.md` e `bloco-13a-descontos-proporcionais.md`.

---

## 7. Armadilhas desta operação

Íntegra em `../armadilhas-comparador.md`. As que afetam imputação:

| # | Onde | Erro |
|---|---|---|
| **A11** | pp. 227, 231 → propaga a **244 e 250** | fórmula do bruto com **colchete fechado cedo demais** — lida à risca dá 318.618,21 contra 322.389,94. **Com `INSS = 0` as duas leituras coincidem**, e os exemplos do 12-B usam INSS zero |
| **A2** | pp. 269, 271 | **bloqueio** — delta de 2.036,51, índice implícito sem origem. Propaga ao total |
| **A3** | p. 266 | **bloqueio** — delta de **10,00 exatos**, não absorvível por arredondamento |
| **A1** | p. 297 | juros do FGTS **contados duas vezes** — excesso de 3.802,63 |

**Os dois bloqueios seguem abertos.** Nenhum é arredondamento.

**E duas que a lista omitia.** `../armadilhas-comparador.md` § 6 atribui ao **Exemplo 5** e às
**letras I/P** também as armadilhas **A9** e **A10**, que tocam esta operação. Recorte
declarado: as duas estão no **§ 2 daquele arquivo — "defeitos sem efeito de valor, mas que
confundem o leitor"**. Não mudam número; mudam o que o leitor pensa estar lendo.

| # | Onde | Erro |
|---|---|---|
| **A9** | pp. 266 e 271 | o título do **Exemplo 6 é cópia literal do Exemplo 5**, inclusive *"juros incluídos na base de cálculo do IR"* — **contra o próprio parâmetro do Exemplo 6, que é a OJ 400** (juros excluídos). O que os distingue é o primeiro *bullet* de "Parâmetros", não o título: dois exemplos de teses **opostas** parecem tratar da mesma |
| **A10** | pp. 239, 241, 267–268, 276 | **duplicações de letra e numeração fantasma**: não existe letra **I** em 10.3.1 (sequência A–H, J), mas o EXEMPLO rotula a linha final como `Demonstração item " I "` e a descreve como `(l + m)`; em 10.3.2.1 há **duas letras `O` e nenhuma `P`**, e os Exemplos 1 e 2 rotulam o resumo como "P"; o Exemplo 5 tem **duas D, duas E, duas G e duas H**. A ocorrência da p. 276 é a única de outra natureza — o mesmo principal impresso como `11.731,57` **e** `11.731,37` na mesma página, com a **letra B imprimindo o errado** |

---

## 8. Pendências desta seção

| # | Pendência |
|---|---|
| **P11B-01** | Bloqueio da p. 266 — coluna K erra 10,00 exatos |
| **P10D-01** | Bloqueio da p. 269 — delta de 2.036,51 com índice sem origem |
| **P11B-07** | **O critério proporcional não tem norma.** Modelado como preset sem default; a questão jurídica segue aberta |
| **P10D-04** | A obrigatoriedade do critério alternativo da letra C, **declarada e não demonstrada** |
| **P11B-06** · **P13C-01** | **Três posições** sobre a data da dedução, no mesmo manual |
| **P10D-05** | A alternativa da **letra I de 10.3.2** (§ 2.2) não tem exemplo em lugar nenhum do capítulo 10 |
| **P10D-08** | **Migração de regime tributário** dentro do mesmo cálculo (Ex. 5) — caso único, sem disciplina. O segmento B **não** o disciplina: `migra*`, `transição` e `dois regimes` → zero nas 471 páginas |
| **§ 1.1** | Origem externa — inteiro teor dos três precedentes **não lido** |
