# Bloco 2 — detalhe: exemplos numéricos do manual

Manual de Cálculos do TRT-3, julho/2016. Quase tudo é do item 5.3 (p. 15 a 17); há um
exemplo do item 4.3 (p. 13) e uma nota do item 6.1 (p. 18). Offset de paginação 0.

Os exemplos estão **literais**, como impressos. A coluna "conferência" traz o resultado
recalculado com `Decimal` em precisão 30, para separar o que é arredondamento declarado do
que é erro de digitação do original. **Nada foi corrigido.**

A regra correspondente a cada exemplo está em `bloco-02-criterios.md`.

---

## 0. Exemplo não numérico — liquidação por artigos (4.3, p. 13)

Único exemplo do bloco fora do item 5.3. Ilustra o que o manual entende por "fato novo":

> "Exemplo: a sentença defere horas extras a jornalista, que teriam sido prestadas em
> cobertura de eventos esportivos, além da jornada normal, mas deixa de especificar o
> número, frequência e horários dos eventos ou jornadas esportivas. Instaurada a execução
> por artigos, as partes deverão articular por petição, oferecendo o número de horas
> extras que entendem devidas."

O direito às horas extras está reconhecido; o que falta é a **dimensão** — quantas, quando.
Daí "fato novo" ser "uma mera dimensão do fato velho".

---

## 1. Percentual → número índice (5.3, p. 15)

Impresso sob os rótulos `Percentual | Metodologia de cálculo | Nº índice`:

| Percentual | Metodologia de cálculo | Nº índice |
|---|---|---|
| 20% | = 20 / 100 + 1 = | 1,2 |
| 2,61% | = 2,61 / 100 + 1 = | 1,0261 |
| 150% | = 150/100 + 1 = | 2,5 |

Conferência: os três fecham exatos.

---

## 2. Número índice → percentual (5.3, p. 15)

| Nº índice | Metodologia de cálculo | Percentual |
|---|---|---|
| 1,2 | = 1,2 - 1 x 100 = | 20% |
| 1,0261 | = 1,0261 - 1 x 100 = | 2,61% |
| 2,5 | = 2,5 - 1 x 100 = | 150% |

Conferência: os três resultados fecham exatos.

**Dois defeitos do original nesta tabela, preservados:**

1. Os **rótulos das colunas estão trocados**. O original imprime
   `Percentual | Metodologia de cálculo | Nº índice` — os mesmos rótulos da tabela
   anterior — mas o conteúdo vai na direção inversa. A tabela acima está com os rótulos
   na ordem do conteúdo; os rótulos impressos são os da tabela 1.
2. **Faltam os parênteses.** `1,2 - 1 x 100` lido pela precedência usual dá
   `1,2 - 100 = -98,8`. A operação pretendida é `(1,2 - 1) × 100`. O próprio manual usa os
   parênteses corretamente uma página adiante: `(1,80 - 1) x 100 = 80%` (p. 16).

---

## 3. Acumulação de percentuais (5.3, p. 16)

```
20% + 50% = 1,20 x 1,50 = 1,80 = 80%
```

Detalhado no original:

| Percentuais | Número índice | Número índice acumulado | Percentual acumulado |
|---|---|---|---|
| 20% | 20 / 100 + 1 = 1,20 | 1,20 x 1,50 = 1,80 | (1,80 - 1) x 100 = 80% |
| 50% | 50 / 100 +1 = 1,50 | | |

Conferência: 1,20 × 1,50 = 1,80 exato. Percentual 80% exato.

---

## 4. Subtração de percentuais (5.3, p. 16)

```
50% - 20% = 1,50 : 1,20 = 1,25 = 25%
```

Conferência: 1,50 ÷ 1,20 = 1,25 exato. Percentual 25% exato.

Vale o contraste com a taxa legal (`00-base-normativa.md`, § 4): também ali a operação é
**razão entre fatores**, não subtração de percentuais. O manual de 2016 já enunciava o
princípio para correção monetária; a base normativa o reafirma para a taxa legal do
art. 406 do CC. Mesma matemática, oito anos antes.

---

## 5. Exemplo 1 — TR acumulada (5.3, p. 16)

Impresso literalmente:

> **1º) Apuração da TR de 01/02/2015 a 23/03/2015**
>
> TR de 01/02/2015 a 28/02/2015 = 0,0168% ou 1,000168 (0,0168/100 + 1)
> TR de 01/03/2015 a 22/03/2015 = 0,0883454% ou 1,000883454 (0,0883454/100 + 1)
>
> Logo
>
> TR acumulada de 01/02/2015 a 22/03/2015 = 0,10516% ou 1,0010516
> (1,0001608 x 1,000883454)

### Conferência — duas inconsistências do original

**(a) O fator repetido está errado por um dígito.**

| Cálculo | Produto | Percentual |
|---|---|---|
| 1,000168 × 1,000883454 (fator declarado acima) | 1,001051602420 | 0,105160% |
| **1,0001608** × 1,000883454 (fator impresso no parêntese) | 1,001044396059 | 0,104440% |

O resultado publicado — 1,0010516 e 0,10516% — corresponde a **1,000168**, não a
1,0001608. O `0` extra no parêntese é erro de digitação. O resultado está certo; a memória
de cálculo, não.

**(b) A data final do título não bate com o corpo.** O título diz "a 23/03/2015"; os dois
sub-períodos e a linha de resultado dizem **22/03/2015**. A composição `01/02 a 28/02` mais
`01/03 a 22/03` cobre até 22/03. O `23/03` do título é que está errado.

Nenhuma das duas foi corrigida.

---

## 6. Exemplo 2 — IPCA-E acumulado, set/15 a fev/16 (5.3, p. 16)

> **2º) Determinar o índice acumulado do IPCA-E entre set/15 a fev/16:**

| Mês/Ano | IPCA-E ( % ) | Número índice |
|---|---|---|
| Set-15 | 0,34 | 1,0034 |
| Out-15 | 0,66 | 1,0066 |
| Nov-15 | 0,85 | 1,0085 |
| Dez-15 | 1,18 | 1,0118 |
| Jan-16 | 0,92 | 1,0092 |
| Fev-16 | 1,42 | 1,0142 |

| | |
|---|---|
| Índice acumulado de set/15 a fev/16 (1,0034 x 1,0066 x 1,0085 x 1,0118 x 1,0092 x 1,0142) | **1,0548785** |
| Total da variação do IPCA-E em percentual | **5,48785%** |

**Conferência.** Produto exato: `1,054878518418558184908480`.

| | Publicado | Exato | Truncado | Half-up |
|---|---|---|---|---|
| Número índice (7 casas) | 1,0548785 | 1,05487851841… | 1,0548785 | 1,0548785 |
| Percentual (5 casas) | 5,48785% | 5,48785184185…% | 5,48785 | 5,48785 |

Fecha. Este exemplo **não distingue truncamento de arredondamento** — o dígito seguinte é
1 nos dois casos. Não serve como oráculo para P3.

### Observação do original sobre índice negativo

> "Obs. Se houver um Índice com sinal negativo em algum mês, basta dividir o total
> acumulado até o referido mês pelo número índice que apresentou a variação negativa."

**O manual não dá exemplo numérico com índice negativo.** A regra fica sem oráculo — é a
pendência P1 de `bloco-02-criterios.md`.

---

## 7. Exemplo 3 — SELIC acumulada por soma (5.3, p. 17)

| Mês/Ano | Juros Selic |
|---|---|
| Jan/16 | 1,06% |
| Fev/16 | 1,00% |
| Mar/16 | 1,16% |
| Abril/16 | 1,06% |

| | |
|---|---|
| Taxa Selic de jan/16 a abr/16 (1,06% + 1,00% + 1,16% + 1,06%) | **4,28** |
| Percentual de juros devidos no mês do pagamento (Lei 9430/96, art. 61, § 3º) | **1,0%** |
| Taxa de Juros Selic – Acumulados aplicáveis aos tributos federais em atraso no mês de maio/16 vencidos em dez.15 (Lei 9430/96, art. 61, § 3º) | **5,28%** |

**Conferência.** Soma = 4,28 exato. Total 4,28 + 1,00 = 5,28 exato.

**Contraste com o exemplo 2, que é o ponto do bloco.** Se os mesmos quatro percentuais
fossem acumulados por multiplicação de números índice, o resultado seria
`1,0106 × 1,0100 × 1,0116 × 1,0106 = 1,04349117920976`, ou **4,349118%** — 0,069 p.p. a
mais que os 4,28% da soma. Essa diferença é exatamente o anatocismo que a Súmula 121 do
STF veda: em quatro meses, sobre R$ 100.000,00, são R$ 69,12 indevidos.

*O produto acima é conferência desta extração, não consta do manual.*

**Note a estrutura do exemplo**: acumula-se a SELIC dos meses **decorridos** (jan a abr/16)
e acrescenta-se **1,0% fixo no mês do pagamento** (maio/16). O mês do pagamento não entra
pela SELIC do próprio mês. É a regra do art. 61, § 3º, da Lei 9430/96, aplicada a tributos
federais em atraso — o manual não a enuncia em prosa nem diz se vale para o débito
trabalhista (pendência P6).

---

## 8. Hora sexagesimal → centesimal (5.3, p. 17)

Regra impressa: "para transformar hora sexagesimal em hora centesimal, cabe dividir o
número de minutos por 60".

| Impresso | Conta do manual | Resultado publicado | Valor exato | Truncado a 2 casas |
|---|---|---|---|---|
| 25 minutos | 25 / 60 | **0,42** centésimos da hora | 0,416666… | 0,41 |
| 1:25 | — | **1,42** | 1,41666… | 1,41 |
| 4 horas e 45 minutos | 45/60 = 0,75 | **4,75** | 4,75 exato | 4,75 |
| 8 horas e 10 minutos | 10/60 = 0,17 | **8,17** | 8,16666… | 8,16 |

**Três dos quatro casos só fecham com arredondamento.** O caso de 45 minutos é exato e não
discrimina. O manual não declara o critério em lugar nenhum: ele aparece só nos resultados.

Consequência prática: `0,42` contra `0,4167` é uma diferença de 0,0033 h por lançamento.
Sobre centenas de lançamentos de hora extra, deixa de ser desprezível — e o critério não
está escrito.

---

## 9. Número de semanas do mês (5.3, p. 17)

Constante impressa: "O mês possui **4,285714** semanas equivalente à divisão de 30 / 7."

Valor exato de 30/7 = 4,28571428571428571428571428571…
A constante impressa está **truncada na sexta casa**.

### Exemplo (a) — horas extras semanais → mensais

> "O deferimento de 5 horas extras semanais resultará em 21,43 horas extras no mês.
> Número semanal de HE = 5
> Número de semanas no mês = 4,285714
> Logo
> Número de hora extra mensal = **21,43** (5 x 4,285714)"

Conferência: 5 × 4,285714 = **21,428570**. Publicado 21,43 → arredondado. Truncado daria
21,42.

### Exemplo (b) — remuneração semanal → mensal

> "Se o empregado recebe fixos R$ 180,00 por semana, a remuneração média mensal será
> R$ 771,43.
> Valor da remuneração semanal = R$ 180,00
> Número de semanas no mês = 4,285714
> Logo
> Remuneração média mensal = **771,43** (R$ 180,00 x 4,285714)"

Conferência: 180,00 × 4,285714 = **771,428520**. Publicado 771,43 → arredondado. Truncado
daria 771,42.

### Constante truncada × constante exata

Nos dois exemplos, usar 30/7 exato em vez de 4,285714 não muda o resultado em duas casas:

| | Com 4,285714 | Com 30/7 exato |
|---|---|---|
| 5 × s | 21,428570 | 21,428571… |
| 180 × s | 771,428520 | 771,428571… |

A escolha entre a constante truncada e a fração exata é indiferente aqui, mas **não é
indiferente em geral** — a diferença relativa é de 6,7 × 10⁻⁸ e cresce com o multiplicador.
O manual não diz qual usar; usa a truncada.

*Esta comparação é conferência desta extração, não consta do manual.*

---

## 10. Conversão da URV (6.1, p. 18)

O manual **não traz exemplo numérico** da conversão URV → CR$. Só a regra e dois registros
de referência:

> "- a tabela de URV consta dos anexos deste manual;
> - em 01/07/94, uma URV equivalia a um (01) Real;"

A paridade de 01/07/94 aparece quantificada em outro ponto do manual, no quadro PARIDADES
(p. 99, e também na p. 381 extraída no bloco 1): **"2750/1 — uma URV de CR$-2.750,00 =
1 real"**.

Cruzando com a série extraída no bloco 1
(`serie-18.10-urv.csv`): a cotação de 30/06/1994 é **CR$ 2.750,00**. Confere com a
paridade declarada.

*O cruzamento é conferência desta extração. O manual não o faz.*
