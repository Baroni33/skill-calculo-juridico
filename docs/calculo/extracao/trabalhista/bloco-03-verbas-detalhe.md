# Bloco 3 — detalhe: exemplos numéricos do manual

Manual de Cálculos do TRT-3, itens 6.2 a 6.6 (p. 19 a 54). Offset de paginação 0.

Exemplos **literais**, como impressos. A conferência foi recalculada com `Decimal` em
precisão 30, para separar arredondamento de erro do original. **Nada foi corrigido.**

Regras correspondentes em `bloco-03-verbas.md`.

**Três erros materiais foram encontrados** — §§ 6, 14 e 16. Todos preservados.

---

## 1. Tabela do aviso-prévio proporcional (6.2, p. 21)

Da Nota Técnica 184/12/CGRT/SRT/MTE, em substituição à do Memo. Circular 10/2011.

| Anos completos | Dias | Anos completos | Dias |
|---:|---:|---:|---:|
| 0 | 30 | 11 | 63 |
| 1 | 33 | 12 | 66 |
| 2 | 36 | 13 | 69 |
| 3 | 39 | 14 | 72 |
| 4 | 42 | 15 | 75 |
| 5 | 45 | 16 | 78 |
| 6 | 48 | 17 | 81 |
| 7 | 51 | 18 | 84 |
| 8 | 54 | 19 | 87 |
| 9 | 57 | 20 | **90** |
| 10 | 60 | | |

Conferência: `30 + 3 × anos` em toda a extensão, teto de 90 em 20 anos. Fecha.

---

## 2. Aviso-prévio — quatro exemplos (6.2, p. 21–24)

### 2.1 Salário fixo

| | Até 1 ano | Mais de 1 ano |
|---|---|---|
| Período | 01/02/2015 a 30/11/2015 | 01/08/12 a 30/11/2015 |
| Vínculo com projeção | 11 meses (10 + 1 de projeção) | 3 anos e 5 meses → **3 anos completos** |
| Dias de aviso | 30 | **39** |
| Salário na rescisão | R$ 1.200,00 | R$ 1.200,00 |
| **Valor** | **R$ 1.200,00** | **R$ 1.560,00** = `1.200,00 / 30 × 39` |

### 2.2 Com adicional de periculosidade de R$ 360,00

Mesmos períodos. Base = 1.200,00 + 360,00 = 1.560,00.

| | Até 1 ano | Mais de 1 ano |
|---|---|---|
| **Valor** | **R$ 1.560,00** | **R$ 2.028,00** = `(1.200,00 + 360,00) / 30 × 39` |

Conferência: `1560/30×39 = 2.028,00` exato.

### 2.3 Parcelas variáveis — menos de 1 ano, horas extras

Admissão 03/10/14, demissão 30/07/15. Salário na rescisão R$ 1.400,00.

| Mês | HE | Mês | HE |
|---|---:|---|---:|
| out/14 | 16 | mar/15 | 16 |
| nov/14 | 15 | abr/15 | 12 |
| dez/14 | 15 | mai/15 | 13 |
| jan/15 | 16 | jun/15 | 11 |
| fev/15 | 14 | jul/15 | 14,20 |
| | | **Total** | **142,20** |

```
Média              = 142,20 / 10 = 14,22
Reflexo no aviso   = 1.400,00 / 220 × 1,5 × 14,22 = 135,74
Valor do aviso     = 1.400,00 + 135,74 = R$ 1.535,74
```

Conferência: média exata; reflexo = 135,73636… → 135,74 (arredondado). Fecha.

> **Defeito do original.** Duas linhas depois do texto "admitido em 03/10/14", o mesmo
> exemplo imprime "Período trabalhado: **03/10/15** a 30/07/15" — data de admissão
> posterior à demissão. Erro de digitação; o cálculo usa 2014.

### 2.4 Parcelas variáveis — menos de 1 ano, comissões

Admissão 03/10/14, demissão 30/07/15. Salário fixo R$ 788,00.

| Mês | Comissões | Índice AM até 30/04/16 | Atualizado |
|---|---:|---:|---:|
| out/14 | 1.200,00 | 1,025392517 | 1.230,47 |
| nov/14 | 800,00 | 1,024897492 | 819,92 |
| dez/14 | 1.500,00 | 1,023819410 | 1.535,73 |
| jan/15 | 1.350,00 | 1,022921285 | 1.380,94 |
| fev/15 | 1.550,00 | 1,022749463 | 1.585,26 |
| mar/15 | 1.450,00 | 1,021425695 | 1.481,07 |
| abr/15 | 1.380,00 | 1,020329861 | 1.408,06 |
| mai/15 | 1.200,00 | 1,019154775 | 1.222,99 |
| jun/15 | 1.050,00 | 1,017310392 | 1.068,18 |
| 30/07/2015 | 1.100,00 | 1,014970884 | 1.116,47 |
| **Total atualizado** | | | **12.849,08** |
| **Média mensal** | | | **1.284,91** |

Salário fixo jul/15: `788,00 × 1,014970884 = 799,80`.

```
Valor do aviso = 799,80 + 1.284,91 = R$ 2.084,71
```

> **Divergência de um centavo no original.** A soma da coluna "atualizado", como impressa,
> dá **12.849,09** — não 12.849,08. A média publicada (1.284,91) fecha com os dois valores,
> então o resultado final não muda. Resíduo de arredondamento por linha.

Observação do próprio manual: o cálculo segue a OJ 181/SDI-I/TST, mas "alguns documentos
coletivos de trabalho fixam a forma de correção das comissões, assim como estabelecem prazo
inferior para apuração da média".

### 2.5 Parcelas variáveis — mais de 1 ano

Admissão 10/09/12, último dia laborado 02/12/15, salário dez/15 R$ 1.400,00.

Horas extras dos últimos doze meses: dez/14 a nov/15 — 30, 30, 30, 32, 30, 26, 32, 30, 28,
15, 8, 8. **Total 299.**

```
Média              = 299 / 12 = 24,92
Reflexo no aviso   = 1.400,00 / 220 × 1,5 × 24,92 = 237,87
Vínculo + projeção = 3 anos, 2 meses e 23 dias → 3 anos completos → 39 dias
Valor do aviso     = (1.400,00 + 237,87) / 30 × 39 = R$ 2.129,23
```

Conferência: 299/12 = 24,9166… → 24,92; reflexo 237,8727… → 237,87; total 2.129,231 →
2.129,23. Fecha.

---

## 3. 13º salário (6.3, p. 25)

Período 19/10/2013 a 30/10/2015. Salários: 2.500,00 até 30/06/14; 2.700,00 de 01/07/14 a
30/06/15; 2.850,00 de 01/07/15 até a demissão.

| Ano | Meses | Cálculo | Valor |
|---|---|---|---|
| 2013 | **2** | `2 / 12 × 2.500,00` | **R$ 416,67** |
| 2014 | 12 | período integral | **R$ 2.700,00** |
| 2015 | **11** | `11 / 12 × 2.850,00` | **R$ 2.612,50** |

Observação do manual sobre 2013: "2/12, porque em outubro o período trabalhado é inferior a
15 dias" — admissão em 19/10 deixa 13 dias.

Sobre 2015: os 11 meses incluem "a projeção do aviso prévio indenizado e **os 06 dias de
acréscimo** ao aviso decorrente da Lei 12.506/11".

Conferência: os três fecham.

### 3.1 Efeito do aviso proporcional sobre os doze avos do 13º (6.3, p. 25)

Último dia laborado 13/12/2015.

| Aviso | Último dia de projeção | 13º proporcional de 2016 |
|---|---|---|
| 30 dias | 12/01/2016 | **0** — janeiro tem menos de 15 dias |
| 30 + 3 dias | **15/01/2016** | **1/12** |
| 30 + 60 dias | **12/03/2016** | **2/12** |

Três dias de aviso a mais valem 1/12 inteiro de 13º do ano seguinte.

---

## 4. Doze avos: férias × 13º, o mesmo contrato dando números diferentes (6.4, p. 26)

### 4.1 Contrato de 22/09 a 10/12 — férias 3/12, 13º 2/12

| Férias (dias corridos da admissão) | | 13º (mês civil) | |
|---|---|---|---|
| 22/set – 21/out | 1 mês → **1/12** | 22/set – 30/set | 9 dias → **0** |
| 22/out – 21/nov | 1 mês → **1/12** | 01/out – 30/out | 1 mês → **1/12** |
| 22/nov – 10/dez | 19 dias → **1/12** (≥ 15) | 01/nov – 30/nov | 1 mês → **1/12** |
| | | 01/dez – 10/dez | 10 dias → **0** |
| **Total** | **3/12** | **Total** | **2/12** |

### 4.2 Contrato de 16/08 a 22/10 — férias 2/12, 13º 3/12

| Férias | | 13º | |
|---|---|---|---|
| 16/ago – 15/set | 1 mês → **1/12** | 16/ago – 30/ago | **15 dias → 1/12** (igual a 15) |
| 16/set – 15/out | 1 mês → **1/12** | 01/set – 30/set | 1 mês → **1/12** |
| 16/out – 22/out | 7 dias → **0** | 01/out – 22/out | 22 dias → **1/12** |
| **Total** | **2/12** | **Total** | **3/12** |

> Os dois quadros juntos são o melhor teste de regressão do item: **a mesma regra dos 15
> dias, aplicada sobre bases de contagem diferentes, inverte qual verba sai maior.**

---

## 5. Tabela de férias proporcionais — CLT art. 130 (6.4, p. 27)

| Doze avos | Até 5 faltas | 6 a 14 | 15 a 23 | 24 a 32 |
|---|---|---|---|---|
| 1/12 | 2,5 dias | 2 dias | 1,5 dias | 1 dia |
| 2/12 | 5 | 4 | 3 | 2 |
| 3/12 | 7,5 | 6 | 4,5 | 3 |
| 4/12 | 10 | 8 | 6,0 | 4 |
| 5/12 | 12,5 | 10 | 7,5 | 5 |
| 6/12 | 15 | 12 | 9 | 6 |
| 7/12 | 17,5 | 14 | 10,5 | 7 |
| 8/12 | 20 | 16 | 12 | 8 |
| 9/12 | 22,5 | 18 | 13,5 | 9 |
| 10/12 | 25 | 20 | 15 | 10 |
| 11/12 | 27,5 | 22 | 16,5 | 11 |
| 12/12 | **30** | **24** | **18** | **12** |

Conferência: cada coluna é `doze_avos × {30, 24, 18, 12} / 12`. Linear e exata em toda a
tabela.

Exemplo do manual: 18 faltas injustificadas e 6/12 → **9 dias** de salário + 1/3.

---

## 6. Férias — exemplos (6.4, p. 27–30)

### 6.1 Mensalista

Período 20/08/12 a 17/12/14, salário na rescisão R$ 2.000,00, sem gozo e sem faltas.

| Verba | Cálculo | Valor |
|---|---|---|
| Férias 2012/2013 **em dobro** | `2.000,00 × 2` | 4.000,00 |
| 1/3 | `4.000,00 / 3` | 1.333,33 |
| **Total 2012/2013** | | **R$ 5.333,33** |
| Férias 2013/2014 simples | | 2.000,00 |
| 1/3 | | 666,67 |
| **Total 2013/2014** | | **R$ 2.666,67** |
| Férias proporcionais 2014/2015 — **5/12** | `2.000,00 / 12 × 5` | 833,33 |
| 1/3 | | 277,78 |
| **Total proporcionais** | | **R$ 1.111,11** |

Os 5/12 decorrem "da projeção do aviso prévio e **06 dias de acréscimo**".

**Variante com 10 faltas injustificadas** no último aquisitivo: pela tabela do art. 130,
5/12 com 6 a 14 faltas → **10 dias**.

```
Valor = 2.000,00 / 30 × 10 = 666,67
1/3   = 222,22
Total = R$ 888,89
```

Conferência: tudo fecha. Note a mudança de divisor — `/12 × doze_avos` sem faltas,
`/30 × dias` com faltas.

### 6.2 Horista com jornada variável — **erro material do original**

Período 02/05/14 a 31/07/15. Salário-hora em julho/15: R$ 9,09.

| Mês | Horas | Mês | Horas | Mês | Horas |
|---|---:|---|---:|---|---:|
| mai/14 | 205 | out/14 | 215 | mar/15 | 203 |
| jun/14 | 216 | nov/14 | 212 | abr/15 | 198 |
| jul/14 | 207 | dez/14 | 218 | mai/15 | 190 |
| ago/14 | 208 | jan/15 | 204 | jun/15 | 205 |
| set/14 | 209 | fev/15 | 215 | jul/15 | 192 |

Somatório mai/14 a abr/15 (1º aquisitivo): **2.510**. Somatório mai/15 a jul/15: **587**.

**Férias simples 2014/2015:**

```
Média = 2.510 / 12 = 209,17 horas
Valor = 209,17 × 9,09 = R$ 1.901,36
1/3   = R$ 633,79
Total = R$ 2.535,15
```

Conferência: fecha (1.901,3553 → 1.901,36).

**Férias proporcionais 2015/2016 — aqui o original erra:**

```
Período aquisitivo: 02/05/15 a 31/07/15
Doze avos: 4/12  (projeção do aviso + 03 dias de acréscimo)
Média: 587 / 3 = 195,67
Valor devido publicado: R$ 741,10   com a memória "(195,67 horas x 9,09 x 4 / 12)"
```

| Conta | Resultado |
|---|---|
| `195,67 × 9,09` | 1.778,6403 |
| `× 4/12` — como a memória declara | **592,88** |
| `× 5/12` | **741,10** ← é o valor publicado |

> **A memória de cálculo e o resultado não são a mesma conta.** O valor publicado
> corresponde a **5/12**, não aos 4/12 declarados duas linhas acima.
>
> *Análise desta extração, não do manual:* os 4/12 são o que as datas sustentam — período
> aquisitivo de 02/05/15 a 31/07/15 (3 meses) mais projeção de 33 dias a partir de 31/07
> leva a 02/09/15, fechando o quarto mês. Isso faz de **741,10 o número fora do lugar**.
>
> O erro **propaga** dentro do próprio exemplo: o 1/3 publicado (R$ 247,03) e o total
> (R$ 988,13) derivam dele. Com 4/12 seriam R$ 197,63 e R$ 790,51.
>
> Nada foi corrigido. Ver `bloco-03-relatorio.md` § 5.

### 6.3 Tarefeiro

Período aquisitivo 01/07/14 a 30/06/15; 3.600 peças; salário/tarefa R$ 5,60.

```
Média de produção = 3.600 / 12 = 300
Salário médio     = 300 × 5,60 = R$ 1.680,00
1/3               = R$ 560,00
Total             = R$ 2.240,00
```

Conferência: exato.

### 6.4 Efeito do aviso proporcional sobre os doze avos de férias (6.4, p. 29–30)

Admissão 10/09/14, último dia laborado 21/10/14.

| Aviso | Data de saída | Férias proporcionais |
|---|---|---|
| 30 dias | 20/11/14 | **2/12** |
| 30 + 6 dias (admissão em 10/09/12) | **26/11/2014** | **3/12**, apuradas de 10/09/14 a 26/11/14 |
| 30 + 60 dias (admissão em 10/09/04) | **19/01/2015** | **4/12**, apuradas de 10/09/14 a 19/01/2015 |

Note que o manual **altera a data de admissão** em cada linha para produzir os anos de
serviço necessários, mantendo o último dia laborado. É recurso didático, não incoerência.

---

## 7. Tabela de férias em regime de tempo parcial — CLT art. 130-A (6.4, p. 30)

| Horas semanais (até) | Dias devidos | Com 8 ou mais faltas injustificadas |
|---|---:|---:|
| 25 horas | 18 | 9 |
| 22 horas | 16 | 8 |
| 20 horas | 14 | 7 |
| 15 horas | 12 | 6 |
| 10 horas | 10 | 5 |
| Igual ou inferior a 5 horas | 8 | 4 |

A segunda coluna é a primeira **pela metade** — regra explicitada no cabeçalho do original.

### 7.1 Exemplo de tempo parcial

Período 01/05/14 a 31/07/15; salário na rescisão R$ 900,00; jornada semanal **24 horas**.

| Verba | Cálculo | Valor |
|---|---|---|
| Férias 2014/2015 — **18 dias** | `900,00 / 30 × 18` | 540,00 |
| 1/3 | | 180,00 |
| **Total** | | **R$ 720,00** |
| Férias proporcionais 2015 — 18 dias, **4/12** | `(900,00 / 30 × 18) × 4/12` | 180,00 |
| 1/3 | | 60,00 |
| **Total** | | **R$ 240,00** |

> **Anomalia do original, preservada.** A jornada declarada é de **24 horas semanais**, que
> não consta da tabela do art. 130-A — as faixas são 25, 22, 20, 15, 10 e ≤ 5. O manual
> aplica os **18 dias** da faixa "até 25 horas". A leitura é defensável (24 ≤ 25), mas o
> critério de enquadramento **não é enunciado**.

Conferência aritmética: as duas linhas fecham exatas.

---

## 8. Abono pecuniário — as duas formas, lado a lado (6.4, p. 33)

Base: remuneração de férias de R$ 4.500,00. Reflexo de gratificação deferida.

| | **(a)** terço sobre 30 dias | **(b)** terço sobre 20 dias |
|---|---:|---:|
| Reflexo em 20 dias de férias `4.500,00 / 30 × 20` | 3.000,00 | 3.000,00 |
| Reflexo da gratificação em 10 dias trabalhados | 1.500,00 | 1.500,00 |
| 1/3 sobre os **30** dias `4.500,00 / 3` | **1.500,00** | — |
| 1/3 sobre os **20** dias | — | **1.000,00** |
| Reflexo em abono pecuniário `4.500,00 / 3` | 1.500,00 | 1.500,00 |
| 1/3 constitucional sobre o abono | — | **500,00** |
| **Total** | **R$ 7.500,00** | **R$ 7.500,00** |

Conferência: os dois somam exatamente 7.500,00. **A equivalência declarada é verdadeira.**

O invariante que sobrevive às duas rotas: o terço constitucional incide sempre sobre o
equivalente a **30 dias** de férias — `1.500,00 = 1.000,00 + 500,00`. Nunca 40.

---

## 9. Dobra do RSR e do feriado por forma de salário (6.5, p. 34)

| Forma de salário | Valor do RSR trabalhado |
|---|---|
| Por hora ou semanal | Valor de uma jornada diária **× 2** |
| Por quinzena | Salário quinzenal **÷ 15 × 2** |
| Mensal | Salário mensal **÷ 30 × 2** |
| Por tarefa | (Valor da semana pelo total de tarefas ÷ nº de dias trabalhados na semana) **× 2** |

---

## 10. Horas extras — fórmula básica (6.6, p. 35–36)

```
Remuneração mensal: R$ 500,00
Jornada:            220 horas/mês
Nº de HE mensal:    40
Adicional:          50% → 50/100 + 1 = 1,50

Total = 500,00 / 220 × 1,50 × 40 = R$ 136,36
```

Conferência: 136,3636… → 136,36. Fecha.

### 10.1 Apenas o adicional — Súmulas 85 e 340 (6.6.4, p. 39)

```
Base:      R$ 3.000,00
Divisor:   180
Adicional: 60% → 1,60
HE mensais: 25

3.000,00 / 180 × 0,6 (1,60 − 1,00) × 25 = R$ 250,00
```

Conferência: exato.

> **Defeito do original:** a base é impressa como "**R$ 3.0000,00**" — um zero a mais. A
> conta usa 3.000,00.

---

## 11. O feriado no módulo semanal — a mesma semana, dois resultados (6.6.5, p. 40)

Semana de 17 a 22/03/2008, com feriado na sexta-feira 21/03.

| Dia | Entrada | Saída | Entrada | Saída | Horas |
|---|---|---|---|---|---|
| 17/03 segunda | 08:00 | 11:45 | 13:00 | 19:00 | 09:45 |
| 18/03 terça | 07:45 | 12:00 | 13:15 | 18:30 | 09:30 |
| 19/03 quarta | 08:00 | 12:00 | 13:00 | 17:00 | 08:00 |
| 20/03 quinta | 07:30 | 12:30 | 14:00 | 18:30 | 09:30 |
| 21/03 sexta | **feriado** | | | | **08:00** ou **00:00** |
| 22/03 sábado | 08:00 | 13:00 | | | 05:00 |

| | Lançando 8h no feriado | Não lançando |
|---|---|---|
| Total na semana | **49:45** | 41:45 |
| Jornada normal | 44:00 | 44:00 |
| **HE acima da 44ª** | **05:45** | **00:00** (resultado com distorção) |

> Palavras do manual: sem o lançamento, "o calculista **compensa as horas extras prestadas
> no decorrer da semana com o feriado**".

Conferência: 9:45 + 9:30 + 8:00 + 9:30 + 8:00 + 5:00 = 49:45; − 44:00 = 5:45. Exato.

---

## 12. Comparação semanal × diária (6.6.5, p. 41)

### Semana A — vence a apuração diária

| Dia | Horas | Além da 44ª | Além da 8ª |
|---|---:|---:|---:|
| Seg | 09:00 | | 01:00 |
| Ter | 05:00 | | |
| Qua | 09:00 | | 01:00 |
| Qui | 09:00 | | 01:00 |
| Sex | 09:00 | | 01:00 |
| Sáb | 06:00 | | |
| **Total** | **47:00** | **03:00** | **04:00** |

### Semana B — vence a apuração semanal

| Dia | Horas | Além da 44ª | Além da 8ª |
|---|---:|---:|---:|
| Seg | 08:00 | | 00:00 |
| Ter | 07:00 | | 00:00 |
| Qua | 11:00 | | 03:00 |
| Qui | 08:00 | | 00:00 |
| Sex | 08:00 | | 00:00 |
| Sáb | 06:00 | | |
| **Total** | **48:00** | **04:00** | **03:00** |

Os dois exemplos, juntos, demonstram que nenhuma das apurações domina a outra — daí a regra
de **comparar e adotar o maior**.

---

## 13. Ficção legal da hora noturna (6.6.5, p. 41)

Fator: `1,142857 = 8/7 = 60/52,5`. Conferência: as duas frações dão 1,142857142857…

### Exemplo de jornadas

| Jornada | Horas trabalhadas | HE por dia |
|---|---|---|
| 8h às 18h, intervalo de 2h | 8h | nenhuma |
| 8h às 20h, sem intervalo | 12h | **4** |
| **8h às 02h, sem intervalo** | **18,57h** | **10,57** |
| **19h às 08h, sem intervalo** | **14h** | **6** |

**Decomposição de 8h às 02h:**

```
8h → 22h  = 14 horas (diurnas)
22h → 02h =  4 horas × 1,1429 = 4,57 horas (ficção legal)
Total     = 18,57 h  →  HE = 18,57 − 8 = 10,57
```

**Decomposição de 19h às 08h:**

```
19h → 22h =  3 horas
22h → 05h =  7 horas-relógio → 8 horas legais  (7 × 8/7)
05h → 08h =  3 horas
Total     = 14 h  →  HE = 14 − 8 = 6
```

O segundo é o caso didático: **13 horas de relógio viram 14 horas legais**.

Conferência: `4 × 1,1429 = 4,5716 → 4,57`; `7 × 8/7 = 8` exato. Fecha.

O manual usa **1,1429** (4 casas) no primeiro exemplo e a fração exata no segundo. O
resultado a 2 casas não muda.

---

## 14. Exemplo-mestre de horas extras (6.6.5, p. 42) — e a cadeia de arredondamento

Admissão 08/02/10, demissão 28/02/11.

| Período | Jornada |
|---|---|
| abr/10 a dez/10 | 8:00–19:30 seg a qua; 8:00–17:00 qui e sex; 8:00–12:00 sáb; 1h de intervalo |
| jan/11 a fev/11 | 8:00–19:00 seg a sex; 8:00–12:00 sáb; 1h de intervalo |

```
abr/10 a dez/10: 10,5 × 3 + 8 × 2 + 4 = 51,5 h/semana
                 51,5 − 44 = 7,5 HE/semana
                 7,5 × 4,285714 = 32,14 HE/mês

jan/11 a fev/11: 10 × 5 + 4 = 54 h/semana
                 54 − 44 = 10 HE/semana
                 10 × 4,285714 = 42,8 HE/mês   ← ver defeito abaixo
```

> **Defeito do original.** `10 × 4,285714 = 42,857140`, que arredonda para **42,86** e
> trunca para **42,85**. O manual publica **42,8**, e esse número propaga para todas as
> tabelas seguintes como **42,80**.
>
> É o mesmo resultado de multiplicar por **4,28** em vez de 4,285714. Não foi corrigido: as
> conferências abaixo usam 42,80, como o manual.

### 14.1 A tabela

| Ano/mês | Salário | Vr. unitário HE (`b/220 × 1,5`) | Nº HE | Vr. HE devida (`c × d`) |
|---|---:|---:|---:|---:|
| fev/10 | 575,00 | 3,92 | – | – |
| mar/10 | 575,00 | 3,92 | – | – |
| abr/10 a jul/10 | 575,00 | 3,92 | 32,14 | **126,00** |
| ago/10 a dez/10 | 625,00 | 4,26 | 32,14 | **136,96** |
| jan/11 e fev/11 | 625,00 | 4,26 | 42,80 | **182,39** |

### 14.2 O achado: a coluna exibida não é a coluna usada

| Conta | Com o valor **exibido** (2 casas) | Com **precisão plena** | Publicado |
|---|---:|---:|---:|
| `3,92 × 32,14` | 125,9888 → **125,99** | 126,0034 → **126,00** | **126,00** |
| `4,26 × 32,14` | 136,9164 → **136,92** | 136,9602 → **136,96** | **136,96** |
| `4,26 × 42,80` | 182,3280 → **182,33** | 182,3864 → **182,39** | **182,39** |

> Nos três casos só a **precisão plena** reproduz o publicado. O valor unitário impresso na
> coluna C é **apresentação**, não insumo.
>
> **Mas o próprio manual não é consistente nisso.** No item 6.6.6.3 (§ 15 abaixo) o reflexo
> no aviso fecha com o valor **exibido** 4,26 e **não** fecha com a precisão plena:
>
> | Conta | Exibido | Pleno | Publicado |
> |---|---:|---:|---:|
> | `31,24 × 4,26` | 133,0824 → **133,08** | 133,1250 → **133,13** | **133,08** |
>
> Duas práticas de arredondamento em dois itens adjacentes do mesmo capítulo. Pendência
> **P10** de `bloco-03-verbas.md`.

---

## 15. Reflexo das HE no RSR e no FGTS (6.6.6.1 e 6.6.6.2, p. 44–45)

| Ano/mês | Vr. HE devida | Nº RSR | Dias úteis | Reflexo RSR (`e × f / g`) | Reflexo FGTS+40% (`× 0,112`) |
|---|---:|---:|---:|---:|---:|
| abr/10 | 126,00 | 4 | 26 | 19,39 | 14,11 |
| mai/10 | 126,00 | 5 | 26 | 24,23 | 14,11 |
| jun/10 | 126,00 | 4 | 26 | 19,39 | 14,11 |
| jul/10 | 126,00 | 4 | 27 | 18,67 | 14,11 |
| ago/10 | 136,96 | 5 | 26 | 26,34 | 15,34 |
| set/10 | 136,96 | 4 | 26 | 21,07 | 15,34 |
| out/10 | 136,96 | 5 | 26 | 26,34 | 15,34 |
| nov/10 | 136,96 | 4 | 26 | 21,07 | 15,34 |
| dez/10 | 136,96 | 4 | 27 | 20,29 | 15,34 |
| jan/11 | 182,39 | 5 | 26 | **35,07** | 20,43 |
| fev/11 | 182,39 | 4 | 24 | **30,40** | 20,43 |

Observações do manual: "O número de RSR foi calculado considerando **apenas os domingos**
como dias de RSR" e "As tabelas com o número de RSR constam do anexo deste manual" — são
as quatro variantes do item 18.13, extraídas no bloco 1.

> **As duas últimas linhas confirmam a precisão plena.** Com o valor exibido 182,39:
> `182,39 × 5/26 = 35,0750`, que arredonda para **35,08** — o manual publica **35,07**.
> Com o valor pleno 182,3864: `35,0743 → 35,07` ✓. E `182,3864 × 4/24 = 30,3977 → 30,40` ✓.
> Só a precisão plena satisfaz as duas simultaneamente.

Nota 4 do manual: `11,2% ou 0,112 = 8 × 1,4 (FGTS + 40%)`.

---

## 16. Reflexo no aviso-prévio, com proporcionalidade (6.6.6.3, p. 45–46)

```
Total HE de mar/10 a fev/11 (últimos doze meses)       374,86
Média física (374,86 / 12)                              31,24
Reflexo para aviso de 30 dias = 31,24 × 4,26         R$ 133,08
```

### 16.1 As duas rotas para 39 dias, declaradas equivalentes

**Rota (i) — ajustar a média:**

```
Média para 39 dias = (374,86 / 12) / 30 × 39 = 31,24 / 30 × 39 = 40,61
Reflexo            = 40,61 × 4,26 = R$ 173,00
```

**Rota (ii) — ajustar o reflexo:**

```
Reflexo para 30 dias = R$ 133,08
Reflexo para 39 dias = 133,08 / 30 × 39 = R$ 173,00
```

Conferência: `40,61 × 4,26 = 172,9986 → 173,00` e `133,08 / 30 × 39 = 173,004 → 173,00`.
**As duas rotas fecham no mesmo centavo.**

> **Defeito do original.** A rota (ii) é impressa como
> "`Reflexo das HE s/ aviso 39 dias = 133,08 × 30 × 39 = 173,00`".
> Com **multiplicação** por 30 o resultado seria 155.703,60. A operação é **divisão**. O
> resultado publicado está certo; a fórmula impressa, não.

---

## 17. Reflexos no 13º e nas férias (6.6.6.4 e 6.6.6.5, p. 46–47)

### 17.1 13º salário

| | Total HE | Meses | Média | Multiplicador | Reflexo |
|---|---:|---:|---:|---|---:|
| 13º de 2010 | 289,26 (fev–dez/10) | 11 | **26,30** | `× 4,26 × 11/12` | **R$ 102,70** |
| 13º prop. de 2011 (**3/12**) | 85,60 (jan–fev/11) | 2 | **42,80** | `× 4,26 × 3/12` | **R$ 45,60** |

Os 3/12 de 2011 consideram a projeção do aviso.

> **Defeito do original:** o multiplicador do 13º/2010 é descrito como "Vr. Unitário da HE
> no mês de **dez/02**". O exemplo é de 2010. Resíduo de uma versão anterior do manual — o
> mesmo acontece em § 17.2 ("fev/02 a jan/03").

### 17.2 Férias

| | Total HE | Meses | Média | Reflexo | 1/3 |
|---|---:|---:|---:|---:|---:|
| Férias integrais 2010/2011 | 332,06 (fev/10–jan/11) | 12 | **27,67** | **R$ 117,87** | R$ 39,29 |
| Férias proporcionais (**2/12**) | 42,80 (fev/11) | 1 | **42,80** | **R$ 30,39** | R$ 10,13 |

Conferência dos somatórios: `32,14 × 9 = 289,26`; `289,26 + 42,80 × 2 = 374,86`;
`289,26 + 42,80 = 332,06`. Todos fecham com a tabela de § 14.

---

## 18. Dedução pelo valor — planilha completa (6.6.7, p. 50–52)

Salário-base R$ 800,00 em todo o período. Valor unitário da HE = `800/220 × 1,5 = 5,4545…`

| Mês | Nº HE | Vr. devido | Vr. pago | **Dif. HE** | RSR | Dias úteis | Refl. RSR | Refl. pago | **Dif. RSR** | FGTS+40% | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| jan/09 | 42,86 | 233,77 | – | 233,77 | 4 | 27 | 34,63 | – | 34,63 | 26,18 | 294,58 |
| fev/09 | 30,00 | 163,64 | 190,91 | **(27,27)** | 4 | 24 | 27,27 | 31,82 | (4,55) | (3,05) | **(34,87)** |
| mar/09 | 12,86 | 70,13 | 116,88 | **(46,75)** | 4 | 26 | 10,79 | 19,48 | (8,69) | (5,24) | **(60,68)** |
| abr/09 | 38,57 | 210,39 | 109,09 | 101,30 | 4 | 26 | 32,37 | 18,18 | 14,19 | 11,35 | 126,83 |
| mai/09 | 42,86 | 233,77 | – | 233,77 | 4 | 26 | 35,96 | – | 35,96 | 26,18 | 295,91 |
| jun/09 | – | – | 109,09 | **(109,09)** | 4 | 26 | – | 18,18 | (18,18) | (12,22) | **(139,49)** |
| jul/09 | 12,86 | 70,13 | 163,64 | **(93,51)** | 4 | 27 | 10,39 | 27,27 | (16,88) | (10,47) | **(120,86)** |
| ago/09 | 30,00 | 163,64 | 327,27 | **(163,64)** | 5 | 26 | 31,47 | 54,55 | (23,08) | (18,33) | **(205,04)** |
| set/09 | 30,00 | 163,64 | 185,45 | (21,82) | 4 | 26 | 25,17 | 30,91 | (5,73) | (2,44) | (30,00) |
| out/09 | 30,00 | 163,64 | 196,36 | (32,73) | 4 | 27 | 24,24 | 32,73 | (8,48) | (3,67) | (44,88) |
| nov/09 | 25,71 | 140,26 | 190,91 | (50,65) | 5 | 25 | 28,05 | 31,82 | (3,77) | (5,67) | (60,09) |
| dez/09 | 17,14 | 93,51 | 136,36 | (42,86) | 4 | 27 | 13,85 | 22,73 | (8,87) | (4,80) | (56,53) |
| 13º/09 | 26,07 | 142,21 | 143,83 | (1,62) | | | | | | (0,18) | (1,81) |
| jan/10 | 30,00 | 163,64 | 136,36 | 27,27 | 5 | 26 | 31,47 | 22,73 | 8,74 | 3,05 | 39,07 |
| fev/10 | 40,00 | 218,18 | 49,09 | 169,09 | 4 | 24 | 36,36 | 8,18 | 28,18 | 18,94 | 216,21 |
| 13º/10 **3/12** | 8,75 | 47,73 | – | 47,73 | | | | | | 5,35 | 53,07 |
| Férias int. 2009/2010 | 26,07 | 142,21 | – | 142,21 | | | | | | | 142,21 |
| Férias prop. **3/12** | 8,75 | 47,73 | – | 47,73 | | | | | | | 47,73 |
| 1/3 s/ férias | | 63,31 | – | 63,31 | | | | | | | 63,31 |
| Aviso ind. | 25,83 | 140,91 | – | 140,91 | | | | | | 15,78 | 156,69 |

**Total devido, corrigido até 31/05/16: R$ 723,39.**

> **Oito meses com diferença negativa, mantidos e corrigidos.** É a exigência da OJ 415
> tornada visível: a coluna "Dif. HE corrigida" traz valores como (37,10), (64,47),
> (147,98), (217,25). Zerá-los inflaria o crédito.

### 18.1 Médias declaradas

```
13º/09    : 312,86 / 12 = 26,07
Férias int: 312,86 / 12 = 26,07
13º/10    : 70 / 2 × 3/12 = 8,75        (3/12 pela projeção do aviso)
Férias prop: 70 / 2 × 3/12 = 8,75
Aviso     : 310 / 12 = 25,83            (mar/09 a fev/10)
```

Conferência dos somatórios: a coluna de HE de jan a dez/09 soma **312,86** exatamente. O
período mar/09–fev/10 soma **310,00**. Fecham.

> **Defeito do original:** a memória do 13º/09 é impressa como "dividido por 12 = 312,86 /
> **2** = 26,07". O divisor da conta é 12; o "2" é erro de digitação.

### 18.2 Confirmação da precisão plena

| Conta | Média exibida | Média plena | Publicado |
|---|---:|---:|---:|
| 13º/09 `média × 5,4545…` | 26,07 → 142,20 | 26,0717 → 142,21 | **142,21** |
| Aviso `média × 5,4545…` | 25,83 → 140,89 | 25,8333 → 140,91 | **140,91** |

Nesta planilha **as médias também entram sem arredondamento**. Reforça P10: o manual
alterna entre as duas práticas sem enunciar nenhuma.

`1/3 s/ férias = (142,21 + 47,73) / 3 = 63,31` ✓ — o terço incide sobre integrais **e**
proporcionais.

---

## 19. Dedução pelo número (6.6.7, p. 52)

Mesmos dados de base, agora com o número deferido pelo comando sentencial (12 HE/mês) e o
número pago. Base R$ 650,00; unitário `650/220 × 1,5 = 4,43`.

| Mês | Nº deferido | Nº pago | **Diferença** | Dif. HE | RSR | Dias úteis | Refl. RSR | FGTS+40% | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| jun/09 | 12 | 8 | **4,00** | 17,73 | 4 | 26 | 2,73 | 1,99 | 22,44 |
| jul/09 | 12 | 6 | **6,00** | 26,59 | 4 | 27 | 3,94 | 2,98 | 33,51 |
| ago/09 | 12 | 15 | **(3,00)** | (13,30) | 5 | 26 | (2,56) | (1,49) | (17,34) |
| set/09 | 12 | 4 | **8,00** | 35,45 | 4 | 26 | 5,45 | 3,97 | 44,88 |
| out/09 | 12 | 15 | **(3,00)** | (13,30) | 4 | 27 | (1,97) | (1,49) | (16,75) |
| nov/09 | 12 | 15 | **(3,00)** | (13,30) | 5 | 25 | (2,66) | (1,49) | (17,44) |
| dez/09 | 12 | 8 | **4,00** | 17,73 | 4 | 27 | 2,63 | 1,99 | 22,34 |
| 13º/09 | 8,00 | 6,76 | 1,24 | 5,50 | | | | | 5,48 |
| Aviso ind. | 12,00 | 10,14 | 1,86 | 8,24 | | | | | 8,23 |
| Férias prop. | 8,00 | 6,76 | 1,24 | 5,50 | | | | | 5,48 |
| 1/3 s/ férias | 2,67 | 2,25 | 0,42 | 1,86 | | | | | 1,84 |

**Total devido, corrigido: R$ 98,26.**

Diferença do método anterior: aqui o reflexo no **RSR incide sobre a diferença** de HE, não
sobre o valor integral deferido.

---

## 20. Dedução pelo valor, com reflexos sobre valores atualizados (6.6.7, p. 52–53)

Mesmos dados do § 19, outra rota: os reflexos saem dos **valores já corrigidos**.

| Mês | Vr. devido | Vr. pago | Dif. HE | Índice AM maio/16 | Dif. corrigida | RSR | Dias úteis | Refl. RSR | FGTS+40% | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| jun/09 | 53,18 | 35,45 | 17,73 | 1,060860803 | 18,81 | 4 | 26 | 2,89 | 2,11 | 23,81 |
| jul/09 | 53,18 | 26,59 | 26,59 | 1,059747009 | 28,18 | 4 | 27 | 4,17 | 3,16 | 35,51 |
| ago/09 | 53,18 | 66,48 | (13,30) | 1,059538280 | (14,09) | 5 | 26 | (2,71) | (1,58) | (18,38) |
| set/09 | 53,18 | 17,73 | 35,45 | 1,059538280 | 37,56 | 4 | 26 | 5,78 | 4,21 | 47,55 |
| out/09 | 53,18 | 66,48 | (13,30) | 1,059538280 | (14,09) | 4 | 27 | (2,09) | (1,58) | (17,76) |
| nov/09 | 53,18 | 66,48 | (13,30) | 1,059538280 | (14,09) | 5 | 25 | (2,82) | (1,58) | (18,49) |
| dez/09 | 53,18 | 35,45 | 17,73 | 1,058973847 | 18,78 | 4 | 27 | 2,78 | 2,10 | 23,66 |
| 13º/09 | | | | 1,058973847 | 5,81 | | | | | 5,81 |
| Aviso ind. | | | | 1,058973847 | 8,72 | | | | | 8,72 |
| Férias prop. | | | | 1,058973847 | 5,81 | | | | | 5,81 |
| 1/3 s/ férias | | | | 1,058973847 | 1,94 | | | | | 1,94 |

**Total devido, corrigido: R$ 98,19.**

Médias declaradas, todas sobre a coluna "Dif. HE corrigida" e **incluindo os negativos**:

```
13º/09        : soma jan–dez/09 / 7 × 8/12   (8/12 pela projeção do aviso)
Aviso ind.    : soma jun–dez/09 / 7
Férias prop.  : soma jun–dez/09 / 7 × 8/12
```

> **Os §§ 19 e 20 partem dos mesmos dados e chegam a R$ 98,26 e R$ 98,19.** Sete centavos.
> Não é erro: é a demonstração, pelo próprio manual, de que **a escolha do critério de
> dedução move o resultado**. Nenhum dos dois é apontado como preferível.

---

## 21. Indenização por supressão de horas extras (6.6.8, p. 54)

Supressão em junho/09; horas extras habituais de abril/97 a maio/09.

**(a) Número de anos:** 12 anos, de 1997 a 2008.

> "O ano de 2009 não entrará no cômputo, tendo em vista que o número de meses trabalhados
> corresponde a 05 meses, portanto fração inferior a 06 meses."
>
> Conferência: 1997 contribui com abr–dez (9 meses ≥ 6) ✓; 1998 a 2008 são 11 anos
> integrais; total 12 ✓. 2009 tem jan–mai (5 meses < 6) ✓.

**(b) Médias dos doze meses anteriores, por adicional:**

| Mês | HE 50% | HE 100% | Mês | HE 50% | HE 100% |
|---|---:|---:|---|---:|---:|
| jun/08 | 28 | 4 | dez/08 | 25 | 6 |
| jul/08 | 20 | 6 | jan/09 | 24 | 6 |
| ago/08 | 25 | 4 | fev/09 | 20 | 4 |
| set/08 | 15 | 4 | mar/09 | 20 | 4 |
| out/08 | 18 | 4 | abr/09 | 20 | 4 |
| nov/08 | 19 | 6 | mai/09 | 20 | 4 |
| | | | **Total** | **254** | **56** |
| | | | **Média (÷12)** | **21,17** | **4,67** |

Conferência: 254/12 = 21,1666… → 21,17; 56/12 = 4,6666… → 4,67. Fecham.

**Duas médias, porque há dois adicionais** — é a razão material da exigência de colunas
separadas do item 6.6.4.

> **Incoerência de redação no original:** o passo (b) da prosa diz "média das horas extras
> prestadas nos doze meses anteriores **à supressão**", em linha com a Súmula 291; o rótulo
> do exemplo diz "anteriores **à rescisão**". No caso não muda nada — a supressão é o evento
> relevante e os dados vão até mai/09 —, mas os dois marcos não são a mesma coisa.
