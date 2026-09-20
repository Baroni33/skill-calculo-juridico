# Bloco 13E — capítulo 16: varredura dirigida

Manual TRT-3, pp. 310 a 336. **Offset de paginação zero.** 27 páginas varridas página a
página. Estrutura real conferida no corpo: **78 rubricas numeradas**.

**Não é extração integral das minutas.** É varredura atrás de regra de cálculo, fundamento e
decisão de ordem de operações escondidos em texto processual.

**39 achados registrados, todas as citações conferidas por script — 0 falhas.**

---

## 1. O entregável principal: 36 fundamentos cruzados

Para cada fundamento normativo do capítulo 16, a pergunta é se o **capítulo técnico
correspondente o cita**. A ausência é o achado.

### 1.1 Os seis que só existem no capítulo 16

| Fundamento | Onde | Ocorrências no manual |
|---|---|---|
| **Súmula 15 do TRT-3** — dedução na data do levantamento | 16.4.11, pp. 333–334 (4×) | **cap. 10: ZERO em 69 páginas.** Cap. 7: 1×, p. 83, só em lista |
| **IN SRF 15/2001** — fonte do *gross-up* bruto↔líquido | 16.4.4.10, p. 326 | **1 em 471 páginas, e é essa** |
| **Súmula 454/TST** — SAT na desoneração | 16.4.3.19, pp. 320–322 | **3, todas no cap. 16** |
| **Súmula 388/TST** — massa falida | 16.4.9.2, p. 332 | **2, ambas na p. 332** |
| **art. 83 da Lei 11.101/05** | 16.4.9.2, p. 332 | **1, e é essa** (o cap. 7 só cita o art. 124) |
| **Prov. 03/91** e **art. 104, § 5º, do PGC TRT-3** | 16.3.5, 16.4.2, 16.4.8.3, 16.4.12.1 | **0 em qualquer capítulo técnico** |

**A IN SRF 15/2001 é a mais grave.** É a **fonte declarada da fórmula de gross-up**:

> "apurado a partir de critérios fornecidos pela Secretaria da Receita Federal, **Instrução
> Normativa nº 15/2001** e adaptados por esta SCJ, visto a inclusão da contribuição
> previdenciária"

E a expressão "bruto em relação ao líquido" ocorre em **16 páginas, 15 delas no capítulo 10**
— que usa a fórmula em todos os exemplos e **nunca diz de onde ela vem**.

### 1.2 O padrão não é universal — e isso importa

Dos 36 fundamentos cruzados, **a maioria É citada pelo capítulo técnico**: art. 124 da Lei
11.101/05, Res. 66/10 do CSJT, OJ 198, art. 407 do CC, Súmulas 24 e 45 do TRT-3, E-RR
1125-36.2010.5.06.0171, AD PGFN 09/11, Rcl 22.012, Lei 8.541/92, art. 56 do Dec. 3000/99,
art. 725, OJ 400, Cosit 13/2016, LC 150/15, LC 123/06, Res. CNJ 115/10, art. 39 da Lei
8.177/91, Prov. 04/00.

**O capítulo 16 não é a fonte de tudo. É a fonte de seis coisas — e uma delas sustenta a
operação mais usada do capítulo 10.**

---

## 2. Correções às premissas — três caíram

| Premissa | Realidade |
|---|---|
| "16.4.11 está na `pagina_pdf` 335" | **Está em 333–334.** A p. 335 é o 16.4.12.2 (Fazenda Pública) e não menciona a Súmula 15 |
| "16.4.7 é caso de fundamentar só na minuta" | **Falso.** O cap. 6, item **6.13.10 "Multa diária", p. 77**, enuncia a mesma regra **com o texto íntegro da OJ 54** e o art. 412 dentro das aspas. **Melhor que a minuta** |
| "a p. 328 é o único lugar do manual com `anatocismo`" | **Parcialmente falso.** `anatocismo` ocorre nas pp. **16, 90, 328 e 335**. Exclusiva do cap. 16 é a **aplicação do conceito à amortização** |
| "o capítulo técnico do FGTS não cita a OJ 302" | **Falso.** O cap. 6, p. 79, **transcreve a OJ**; e o cap. 7, p. 83, a cita |

**As três primeiras eu gravei no bloco 12 sem cruzá-las.** A varredura dirigida as derrubou —
e, no saldo, **reforçou a reclassificação**: eram três achados, um caiu, e apareceram quatro
novos. **São seis.**

---

## 3. O 16.4.11 aprofundado: duas teses e o critério que as separa

O manual reconhece **duas teses** sobre a data da dedução. **A condição que as separa é a
finalidade do depósito**, aferida por dois indícios que o próprio manual nomeia:

| Indício | Efeito |
|---|---|
| **código aposto na guia** — "código 02" | depósito **para pagamento** |
| **cronologia** — depósito que *"precedeu aos embargos e agravo de petição"* | depósito **em garantia** |

| Finalidade | Dedução | Consequência |
|---|---|---|
| **garantia** da execução | na data do **levantamento** | há diferença a apurar |
| **pagamento** | na data do **depósito** | *"não há diferença a ser apurada"* |

A tese do pagamento exige ainda que o depósito seja do **total** da execução e **já atualizado**
até a data do depósito.

**Isto alimenta diretamente o preset `pr.adc58-item-i`**, cujo segundo input é a *natureza do
depósito* — e mostra que o eixo não foi invenção da modelagem: **é o critério que o próprio
manual usa.**

### 3.1 E há uma terceira posição, no capítulo 14

`pagina_pdf` 306, letra "c": *"Amortizar com observância da **data do pagamento** e não da
data do levantamento, salvo determinação do juízo da origem"* — **sem** a distinção por
finalidade. Ver `bloco-13c-sindical-precatorios.md` § 6. **Não harmonizado.**

---

## 4. A p. 328, confirmada e precisada

A minuta **descreve a operação de 10.3.1**. A primeira frase da p. 328 e a primeira frase do
item 10.3.1 (p. 237) são **a mesma frase** — a diferença é que em 10.3.1 a operação é apenas
**nomeada** ("descarregar") e na p. 328 é **qualificada juridicamente**:

> "não incidindo juros sobre juros (anatocismo), **vedada por Lei**"

Confirmado por busca: `anatocismo` e `juros sobre juros` → **zero ocorrências nas 69 páginas
do capítulo 10**; `descarreg` → **uma única ocorrência em todo o manual**, p. 237.

---

## 5. Outros achados estruturais

| # | Achado | `pagina_pdf` |
|---|---|---|
| **A15** | Juros e multa tributários incidem **apenas sobre a diferença** entre o devido na liberação e o já depositado | 327 |
| **A17** | **Três regimes distintos de atualização de depósito**: judicial = poupança (TR + 0,5% a.m.) · recursal = FGTS (TR + 3% a.a.) · crédito trabalhista = art. 39 da Lei 8.177/91 (TR + 1% a.m. simples) | 329 |
| **A18/A19** | Honorários periciais por **IPCA-E** (Res. 66/10 CSJT) e **sem juros**, por serem despesa processual | 330 |
| **A21** | Massa falida: a Súmula 388/TST isenta **apenas** do art. 467 e do art. 477, § 8º. **INSS, IR e custas integram a execução** | 332 |
| **A30** | Reflexo de HE em férias + 1/3 pela **média do período aquisitivo × valor de 1 HE no mês das férias**; zero horas no mês de gozo | 314 |

**A17 é estruturalmente importante:** três taxas diferentes conforme a natureza do depósito —
e é o mesmo eixo que o 16.4.11 usa e que o preset `pr.adc58-item-i` modela.

---

## 6. A regra do `imputa`

`imputa` tem **3 ocorrências no manual, todas nas pp. 319–320**. A regra:

> juros e multa previdenciários por recolhimento a destempo **não se imputam ao reclamante**;
> deduz-se apenas a contribuição atualizada — *"salvo se houver decisão em contrário"*

Fundamentos: art. 30, I, "a" e "b", e art. 33, § 5º, da Lei 8.212/91, e o **E-RR
1125-36.2010.5.06.0171** (TST Pleno, 20/10/15) — este **citado também no cap. 9**, pp. 118 e
128.

Confirma o item 4 do capítulo 15, já extraído no bloco 10.

---

## 7. Defeitos

Doze registrados. Os que importam:

- **numeração `16.4.4.12` duplicada** — pp. 326 e 327;
- **transcrição truncada e com erro da OJ 54** na p. 330: *"não poderá **se** superior"* (falta
  o "r"), e a citação **omite o art. 412/2002 de dentro das aspas** — ao contrário da p. 77,
  que a traz íntegra;
- **corpo do 16.4.4.13 repete literalmente o marcador do item anterior** ("multa pelo atraso ou
  inadimplemento da parcela do acordo") em vez de litigância de má-fé;
- **frase truncada em vírgula** ao fim do 16.4.3.18, p. 320;
- alíneas faltantes em 16.3.5 (a, c, d) e 16.4.9.2 (a, c);
- `"Lei 9.317/96**15**"` na p. 317 — marcador de nota colado ao número da lei;
- e, no **capítulo técnico**: *"para **aliá-los** sem acumulação"* (p. 237) e o "10.2" reaberto
  na p. 249.

---

## 8. O que não fechou

- o **sumário impresso não foi conferido contra o corpo** neste capítulo;
- o **único exemplo numérico do capítulo 16** (índices de TR, item 16.4.8.4) **não foi
  recalculado**, por falta da tabela do CSJT — que é série externa, categoria (B);
- o início do capítulo 9 não foi confirmado por cabeçalho (a varredura capturou 1–8 e 10–16,
  não o 9); adotada a faixa 107–208 já estabelecida nos blocos anteriores.

---

## 9. Conclusão sobre a classificação

**A reclassificação para fonte normativa, feita no bloco 12, está confirmada e reforçada** —
mas por razões parcialmente diferentes das que a motivaram.

Caiu o 16.4.7. Ficaram o 16.4.11 e a p. 328, e entraram IN SRF 15/2001, Súmula 454, Súmula 388
com o art. 83 da Lei 11.101/05, e o Prov. 03/91 com o art. 104, § 5º.

**O padrão "pratica no técnico, fundamenta na minuta" é real, mas não universal** — vale para
seis fundamentos de trinta e seis. **A lição é mais estreita e mais útil do que a que eu
escrevera:** não é que o capítulo 16 seja a fonte do manual; é que **há operações centrais
cuja única fundamentação está fora do capítulo que as executa**, e a do *gross-up* é uma
delas.
