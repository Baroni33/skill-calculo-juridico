# Bloco 4 — detalhe: exemplos numéricos do manual

Manual de Cálculos do TRT-3, itens 6.6.8 (fecho) e 6.7 a 6.15, páginas 55 a 82. Offset de
paginação 0.

Exemplos **literais**, como impressos. Conferência recalculada com `Decimal` em precisão 30.
**Nada foi corrigido.**

Regras correspondentes em `bloco-04-verbas2.md`.

**Cinco erros materiais** — §§ 4, 6, 8, 10 e 13. Todos preservados.

---

## 1. Fecho do item 6.6.8 — supressão de horas extras (p. 55)

Completa o exemplo que o bloco 3 deixou na p. 54. Salário no mês da supressão: **R$ 980,00**.
Médias apuradas no bloco 3: **21,17** HE com 50% e **4,67** com 100%.

| Passo | Conta | Valor |
|---|---|---|
| Valor unitário HE 50% | `980,00 / 220 × 1,5` | **6,68** |
| Valor unitário HE 100% | `980,00 / 220 × 2,0` | **8,91** |
| Valor mensal HE 50% | unitário × média 50% | **141,43** |
| Valor mensal HE 100% | unitário × média 100% | **41,58** |
| **Indenização** | `141,43 × 12 + 41,58 × 12` | **R$ 2.196,12** |

**Conferência.** Os dois valores mensais só fecham com **precisão plena em toda a cadeia**,
inclusive nas médias:

| | Com valores exibidos | Com precisão plena | Publicado |
|---|---:|---:|---:|
| HE 50% (`6,68 × 21,17`) | 141,4156 → **141,42** | 141,4318 → **141,43** | **141,43** |
| HE 100% (`8,91 × 4,67`) | 41,6097 → **41,61** | 41,5758 → **41,58** | **41,58** |

`141,43 × 12 + 41,58 × 12 = 2.196,12` exato.

> **Duas médias, dois adicionais.** É a demonstração de por que o passo (b) do item 6.6.8
> exige uma média por adicional: somar 254 + 56 e usar um único valor unitário daria outro
> número.

---

## 2. Horas *in itinere* (6.7, p. 55)

Não há tabela: o manual dá o encadeamento em linha.

```
06:00  embarque na condução fornecida pela empresa → início da jornada
18:00  desembarque                                 → fim da jornada
─────────────────────────────────────────────────────────────────────
12:00  total da jornada
−1:00  intervalo de almoço
─────────
11:00  horas trabalhadas
−8:00  jornada normal
─────────
03:00  horas extras por dia
```

**O ponto que o exemplo estabelece:** embarque e desembarque **são** os marcos da jornada.
O tempo de percurso não é parcela autônoma — entra na contagem e o excedente vira hora extra
pela fórmula do item 6.6.

---

## 3. Intervalo intrajornada comum (6.10.1, p. 56)

Jornada de **segunda a sábado, 9h às 17h**, sem intervalo. Salário mensal **R$ 750,00**.
Intervalo deferido: **1 hora por dia**.

```
Horas de intervalo por semana  = 1 × 6 dias = 6
Horas de intervalo por mês     = 6 × 4,285714 = 25,71
Salário-hora                   = 750,00 / 220 = 3,41
Valor unitário da hora extra   = 3,41 × 1,50 = 5,11
Valor mensal do intervalo      = 5,11 × 25,71 = R$ 131,38
```

**Conferência — aqui o manual usa os valores EXIBIDOS:**

| Cadeia | Resultado | Publicado |
|---|---:|---:|
| `5,11 × 25,71` (valores exibidos) | 131,3781 → **131,38** | **131,38** |
| `(750/220 × 1,5) × (6 × 4,285714)` (precisão plena) | 131,4935 → 131,49 | — |

Diferença de **R$ 0,11 num único mês**, só pela escolha do ponto de arredondamento. Contraste
com o § 1, onde a mesma operação exigia precisão plena. Ver § 15.

---

## 4. Intervalo especial do art. 253 — câmara fria (6.10.1, p. 57–58)

Comando sentencial transcrito pelo manual: intervalo de **20 minutos a cada 1h40**, pago como
hora extra, adicional da CCT, **divisor 220**, com reflexos em RSR, 13º, férias e aviso.

Período **07/03/2011 a 30/09/2011**. Adicional da CCT: **80%**. Jornada: segunda a sexta,
7h–11h30 e 13h–17h30.

### 4.1 Apuração do número de intervalos

| Jornada inicial | Jornada final | Intervalo |
|---|---|---|
| 07:00 | 08:40 | 00:20 |
| 09:00 | 10:40 | 00:20 |
| 11:00 | 11:30 | 00:00 |
| 13:00 | 14:40 | 00:20 |
| 15:00 | 16:40 | 00:20 |
| 17:00 | 17:30 | 00:00 |
| **Total diário** | | **80 min** |

```
Horas diárias de intervalo   = 80 / 60 = 1,33
Horas por semana             = 1,33 × 5 = 6,65
Horas extras por mês         = 6,65 × 4,285714 = 28,50
```

Conferência: `6,65 × 4,285714 = 28,4999981 → 28,50` ✓. Note que os blocos de 1h40 que não
completam o ciclo (11:00–11:30 e 17:00–17:30) **não geram intervalo**.

### 4.2 A planilha

| Mês | Salário | Nº HE | Unitário (`sal/220 × 1,8`) | Valor devido | RSR | Dias úteis | Reflexo RSR | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 07/03/2011 | 1.200,00 | 28,5 | 9,82 | 279,82 | 5 | 26 | 53,81 | 333,63 |
| abr/11 | 1.500,00 | 28,5 | 12,27 | 349,77 | 6 | 24 | 87,44 | 437,22 |
| mai/11 | 1.500,00 | 28,5 | 12,27 | 349,77 | 5 | 26 | 67,26 | 417,04 |
| jun/11 | 1.500,00 | 28,5 | 12,27 | 349,77 | 5 | 25 | 69,95 | 419,73 |
| jul/11 | 1.500,00 | 28,5 | 12,27 | 349,77 | **6** | **26** | 80,72 | 430,49 |
| ago/11 | 1.500,00 | 28,5 | 12,27 | 349,77 | 4 | 27 | 51,82 | 401,59 |
| set/11 | 1.500,00 | 28,5 | 12,27 | 349,77 | 5 | 25 | 69,95 | 419,73 |
| aviso prévio | | 28,5 | 12,27 | 349,77 | | | | 349,77 |
| 13º sal. **8/12** | | 19 | 12,27 | 233,18 | | | | 233,18 |
| Férias **8/12** | | 19 | 12,27 | 233,18 | | | | 233,18 |
| 1/3 s/ férias | | | | 77,73 | | | | 77,73 |

Médias declaradas, idênticas para 13º e férias:

```
199,50 / 7 meses × 8/12 = 19
```

**Conferência.** Aqui a cadeia é de **precisão plena**: `1500/220 × 1,8 × 28,5 = 349,7727 →
349,77` (com o exibido 12,27 daria 349,695 → 349,70). O 13º: `19 × 12,272727 = 233,1818 →
233,18` (com 12,27 daria 233,13). O terço: `233,1818 / 3 = 77,7273 → 77,73`.

Os sete reflexos em RSR fecham.

### 4.3 Três defeitos do original

> **(a) Julho de 2011 tem 32 dias.** A linha imprime **RSR 6 + dias úteis 26 = 32**, e julho
> tem 31. Conferência de todos os meses:
>
> | Mês | RSR | Dias úteis | Soma | Dias do mês |
> |---|---:|---:|---:|---:|
> | 03/2011 | 5 | 26 | 31 | 31 ✓ |
> | 04/2011 | 6 | 24 | 30 | 30 ✓ |
> | 05/2011 | 5 | 26 | 31 | 31 ✓ |
> | 06/2011 | 5 | 25 | 30 | 30 ✓ |
> | **07/2011** | **6** | **26** | **32** | **31** ✗ |
> | 08/2011 | 4 | 27 | 31 | 31 ✓ |
> | 09/2011 | 5 | 25 | 30 | 30 ✓ |
>
> Uma linha em sete. O reflexo publicado (80,72) é consistente com os números impressos, de
> modo que o erro está na contagem, não na conta.

> **(b) O salário de março contradiz os dados do exemplo.** A seção de dados declara
> "Evolução salarial: **R$ 1.500,00**", valor único; a primeira linha da tabela traz
> **R$ 1.200,00**. O manual não explica a diferença, e março é mês parcial (contrato inicia
> em 07/03).

> **(c) O critério de contagem de RSR não é declarado.** No exemplo equivalente do bloco 3
> (p. 45) o manual registrou "considerando **apenas os domingos**". Aqui, não. Abril de 2011
> teve 4 domingos e a linha traz 6 — compatível com domingos **mais feriados** (21/04
> Tiradentes e 22/04 Sexta-Feira da Paixão), mas isso é leitura desta extração, não afirmação
> do manual.

---

## 5. Adicional de insalubridade (6.11.1, p. 59–60)

### 5.1 Ajuste ao aviso proporcional

```
Salário na rescisão (jul/12)          R$   900,00
Adicional para 30 dias (40% s/ 622,00) R$  248,80
Aviso prévio                               36 dias
Reflexo no aviso = 248,80 / 30 × 36    R$  298,56
```

Conferência: `40% × 622,00 = 248,80` e `248,80/30 × 36 = 298,56` — exatos.

### 5.2 Planilha completa — grau médio (20%)

Período **01/03/10 a 10/04/11**.

| Ano/mês | Salário mínimo | Adicional (20%) |
|---|---:|---:|
| mar/10 a dez/10 | 510,00 | **102,00** |
| 13º/10 prop. **(10/12)** | **425,00** | **85,00** |
| jan/11 a mar/11 | 545,00 | **109,00** |
| 10/04/2011 | **181,67** | **36,33** |

**Reflexos nas parcelas rescisórias**, todos sobre o salário mínimo da rescisão (545,00):

| Parcela | Conta | Valor |
|---|---|---:|
| Aviso prévio | 20% × 545,00 | 109,00 |
| Férias integrais | 20% × 545,00 | 109,00 |
| 1/3 s/ férias integrais | 109,00 / 3 | 36,33 |
| Férias proporcionais **2/12** | 109,00 × 2/12 | 18,17 |
| 1/3 s/ férias proporcionais | 18,17 / 3 | 6,06 |
| 13º proporcional **4/12** | 109,00 × 4/12 | 36,33 |

**Conferência.** Todas fecham. Duas linhas merecem atenção:

- **13º/10 proporcional**: a base é `510,00 × 10/12 = 425,00`, e só depois se aplica o 20%.
  O manual **proporcionaliza a base, não o adicional** — o resultado é o mesmo, mas a ordem
  fica explícita na tabela.
- **10/04/2011**: `545,00 / 30 × 10 = 181,67` — mês parcial pro rata die, dez dias.

O manual fecha repetindo a regra do aviso: "se o aviso prévio fosse superior a 30 dias, o
calculista deveria dividir o valor de R$ 109,00 por 30 e multiplicar pelo número de dias".

---

## 6. Redução da hora noturna — os três exemplos (6.11.4.1, p. 62)

```
horas_reduzidas = horas_efetivas × 1,142857143
```

| Jornada noturna | Horas efetivas | Publicado | Conferência |
|---|---:|---:|---:|
| 22h → 4h | 6:00 → **6** | **6,87** | `6 × 1,142857143 = ` **6,857142858** |
| 22h → 3h45 | 5:45 → **5,75** | **6,57** | `5,75 × 1,142857143 = 6,5714285` ✓ |
| 19h → 7h (só o trecho 22h→7h) | 9:00 → **9** | **10,29** | `9 × 1,142857143 = 10,2857142` ✓ |

> **Erro material do original.** `6 × 1,142857143 = 6,857142858`, que arredonda para **6,86**
> e trunca para **6,85**. O manual publica **6,87**. Os outros dois exemplos da mesma página
> fecham; só este não.

**A advertência do manual, que vale mais que os números** (6.11.4.1, p. 62):

> "Conforme vimos no tópico 5.3, não é correto trabalhar com hora sexagesimal (hora relógio)
> e sim com hora centesimal. **Multiplicar 5,45 por 1,142857 está totalmente equivocado.**"

Conferência do contra-exemplo: `5,45 × 1,142857 = 6,2286`, contra o correto
`5,75 × 1,142857143 = 6,5714`. Erro de **0,34 hora** — 20 minutos — num único lançamento.

> Note o terceiro exemplo: a jornada é 19h→7h, mas só o trecho **22h→7h** (9 horas) entra na
> redução. As horas prorrogadas após as 5h recebem a ficção legal por força do art. 73, § 5º,
> e da Súmula 60, II — ver espinha § 5.4.3.

---

## 7. Adicional noturno — planilha (6.11.4.2, p. 63)

Período fev/10 a abr/10, salário **R$ 650,00**. Horários: fev e mar, **19h às 1h**, segunda a
quinta; abr, **20h às 3h**, segunda a sexta.

### 7.1 Apuração do número de horas noturnas

**Fevereiro e março** (trecho noturno: 22h → 1h = 3 horas):

```
Horas noturnas diárias  = 3 × 1,142857 = 3,4285
Horas por semana        = 3,4285 × 4 dias = 13,71
Horas por mês           = 13,71 × 4,285714 = 58,76
```

**Abril** (trecho noturno: 22h → 3h = 5 horas):

```
Horas noturnas diárias  = 5 × 1,142857 = 5,71
Horas por semana        = 5,71 × 5 dias = 28,55
Horas por mês           = 28,55 × 4,285714 = 122,36
```

> **Terceira prática de arredondamento.** Aqui o manual arredonda **a cada passo**: sem isso,
> `3 × 1,142857 × 4 × 4,285714 = 58,7755` (não 58,76) e
> `5 × 1,142857 × 5 × 4,285714 = 122,4490` (não 122,36). A cadeia publicada só fecha
> arredondando 3,4285 → 13,71 → 58,76 e 5,71 → 28,55 → 122,36.
>
> Em abril a diferença chega a **0,09 hora** contra a precisão plena.

### 7.2 A planilha

| Ano/mês | Salário | Vr. hora normal (`/220`) | Unitário AN (`× 0,2`) | Nº horas noturnas | Valor total AN | RSR | Dias úteis | Reflexo RSR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fev/10 | 650,00 | 2,95 | 0,59 | 58,76 | **34,72** | 4 | 24 | **5,79** |
| mar/10 | 650,00 | 2,95 | 0,59 | 58,76 | **34,72** | 4 | 27 | **5,14** |
| abr/10 | 650,00 | 2,95 | 0,59 | 122,36 | **72,30** | 4 | 26 | **11,12** |

**Conferência — aqui volta a precisão plena:**

| Conta | Com 0,59 exibido | Com precisão plena | Publicado |
|---|---:|---:|---:|
| `0,59 × 58,76` | 34,6684 → **34,67** | 34,7218 → **34,72** | **34,72** |
| `0,59 × 122,36` | 72,1924 → **72,19** | 72,3036 → **72,30** | **72,30** |

Os três reflexos em RSR fecham a partir dos valores publicados.

### 7.3 Reflexos nas parcelas rescisórias (6.11.4.4, p. 64)

```
Total de horas noturnas nos três meses  = 58,76 + 58,76 + 122,36 = 239,88
Média (239,88 / 3)                      = 79,96
```

| Parcela | Conta | Valor |
|---|---|---:|
| Aviso-prévio | `0,59 × 79,96` | **47,18** |
| 13º salário proporcional **4/12** | `(79,96 × 0,59) × 4/12` | **15,73** |
| Férias proporcionais **4/12** | `(79,96 × 0,59) × 4/12` | **15,73** |
| 1/3 s/ férias | `15,73 / 3` | **5,24** |

Os 4/12 consideram a projeção do aviso-prévio sobre um contrato de três meses.

**Conferência — e aqui o manual volta ao valor EXIBIDO:**

| Conta | Com 0,59 exibido | Com precisão plena | Publicado |
|---|---:|---:|---:|
| `79,96 × 0,59` (aviso) | 47,1764 → **47,18** | 47,2491 → 47,25 | **47,18** |

> **Duas práticas em duas páginas consecutivas**, sobre o mesmo valor unitário: a coluna de
> valor mensal (p. 63) exige precisão plena; o reflexo (p. 64) exige o exibido. É exatamente
> o padrão que o bloco 3 encontrou entre as p. 42 e 46. Ver § 15.

---

## 8. Comissões (6.12, p. 66–67)

### 8.1 Horas extras do comissionista — Súmula 340

Recibo de jan/16:

| Rubrica | Horas | Devido |
|---|---:|---:|
| Comissões | 200,00 | 2.000,00 |
| RSR s/ comissões | | 307,69 |
| **Total bruto** | | **2.307,69** |

Adicional devido: **50%**. Horas extras prestadas: **42**.

```
Total de horas efetivamente trabalhadas = 200 + 42 = 242
Valor-hora = 2.000,00 / 242 = 8,26        ← comissões SEM o RSR
Adicional HE = 8,26 × 0,5 × 42 = R$ 173,55
```

**Conferência.** `2000/242 × 0,5 × 42 = 173,5537 → 173,55` — **precisão plena**; com o
exibido 8,26 daria 173,46.

O RSR impresso, de **307,69**, **não entra na base** e suas horas não entram no divisor — é a
regra da simetria (espinha § 6.3). *Reconstrução desta extração, não do manual:* o valor é
compatível com `2.000,00 / 26 dias úteis × 4 RSR = 307,6923`, mas o exemplo não declara o
número de dias úteis nem de RSR.

> A coluna "Horas" da linha do RSR imprime **30,77**, sem explicação no texto. A camada de
> texto do PDF funde as duas colunas nesse ponto; o valor não é usado em conta alguma.

### 8.2 Média de comissões atualizada — OJ 181

| Mês | Comissões | Índice AM até 31/10/06 | Atualizado |
|---|---:|---:|---:|
| out/01 | 1.200,00 | 1,150639430 | 1.380,77 |
| nov/01 | 800,00 | 1,148425266 | 918,74 |
| dez/01 | 1.500,00 | 1,146152446 | 1.719,23 |
| jan/02 | 1.350,00 | 1,143190439 | 1.543,31 |
| fev/02 | 1.550,00 | 1,141853329 | 1.769,87 |
| mar/02 | 1.450,00 | 1,139849474 | 1.652,78 |
| abr/02 | 1.380,00 | 1,137169166 | 1.569,29 |
| mai/02 | 1.200,00 | 1,134783850 | 1.361,74 |
| jun/02 | 1.050,00 | 1,132991458 | 1.189,64 |
| 30/07/2002 | 1.100,00 | 1,129990204 | 1.242,99 |

**Reflexos publicados:**

| Parcela | Conta | Valor |
|---|---|---:|
| Total out/01 a jul/02 | soma | 14.348,36 |
| Média mensal (÷ 10) | | **1.434,84** |
| Reflexo no aviso-prévio | = média | **1.434,84** |
| Reflexo em férias prop. **11/12** | `1.434,84 / 12 × 11` | **1.315,27** |
| Total **out/01 a dez/01** | | **5.562,04** |
| Média (÷ 3) | | 1.854,01 |
| Reflexo no 13º/01 **3/12** | `1.854,01 × 3/12` | **463,50** |
| Total jan/02 a jul/02 | | 10.329,63 |
| Média (÷ 7) | | 1.475,66 |
| Reflexo no 13º/02 **8/12** | `1.475,66 × 8/12` | **983,77** |

> ### Erro material do original — o total de out/01 a dez/01
>
> As três linhas de out, nov e dez/01 somam **4.018,74**, não 5.562,04.
>
> A diferença é **1.543,30** — exatamente a linha de **jan/02** (1.543,31, a um centavo de
> arredondamento). O total rotulado "out/01 a dez/01" inclui **quatro** meses e é dividido
> por **três**.
>
> | | Publicado | Com a soma dos três meses rotulados |
> |---|---:|---:|
> | Total | 5.562,04 | **4.018,74** |
> | Média | 1.854,01 | **1.339,58** |
> | Reflexo no 13º/01 (3/12) | **463,50** | **334,90** |
>
> O erro **infla o reflexo em R$ 128,60**. Nada foi corrigido.
>
> *Observação desta extração:* o total geral (14.348,36) e a média de dez (1.434,84) **estão
> corretos**. As somas exatas são 4.018,74 e 10.329,6257 — juntas, 14.348,3657, que arredonda
> para os 14.348,36 publicados. Somar os dois totais **já arredondados** do manual daria
> 14.348,37: a cadeia é de precisão plena. O defeito é local ao bloco do 13º/01.

Os demais fecham: `14.348,36/10 = 1.434,836 → 1.434,84`; `1.434,84/12 × 11 = 1.315,27`;
`10.329,63/7 = 1.475,66`; `1.475,66 × 8/12 = 983,7733 → 983,77`.

---

## 9. Seguro-desemprego — regime até 27/02/2015 (6.13.4, p. 71)

```
Período trabalhado: 05/03/2012 a 25/01/2015  (35 meses)
Salários: nov/14 R$ 1.200,00 · dez/14 R$ 1.485,00 · jan/15 R$ 1.200,00
Propositura da ação: 12/05/15
```

**Passo 1 — salário médio**

```
(1.200,00 + 1.485,00 + 1.200,00) / 3 = R$ 1.295,00
```

**Passo 2 — enquadrar na tabela de jan/15** (SM = 788,00), 2ª faixa:

```
Vr. da parcela = [(1.295,00 − 1.222,77) × 0,5] + 978,22 = R$ 1.014,34
```

**Passo 3 — número de parcelas**: 35 meses → **5 parcelas**

```
1.014,34 × 5 = R$ 5.071,67
```

**Passos 4 e 5 — atualização e juros**

| | Valor |
|---|---:|
| Indenização | 5.071,67 |
| Índice de atualização 01/02/15 a 31/05/16 | 1,024489426 |
| Atualizada até 31/05/16 | **5.195,87** |
| Juros 12/05/15 a 31/05/16 — **12,6333%** | **656,41** |
| **Total** | **R$ 5.852,28** |

### 9.1 Conferência — e duas anotações

`(1.295,00 − 1.222,77) × 0,5 + 978,22 = 1.014,335`, publicado como **1.014,34**.

> **Quarta prática de arredondamento: truncamento.** `1.014,34 × 5 = 5.071,70`, mas o manual
> publica **5.071,67** — que é `1.014,335 × 5 = 5.071,675` **truncado**. Nem o valor exibido,
> nem arredondamento: a parcela entra sem arredondar e o produto é cortado.

`5.071,67 × 1,024489426 = 5.195,872 → 5.195,87` ✓.
`5.195,87 × 12,6333% = 656,4098 → 656,41` ✓. Total `5.195,87 + 656,41 = 5.852,28` ✓.

> **A taxa de juros está grafada errada.** O manual escreve "**0,33% ao dia** ou 1% ao mês".
> A 0,33% ao dia, um mês daria ~10%. A conferência mostra que a taxa efetivamente usada é
> **0,0333% ao dia**:
>
> ```
> 12/05/15 a 31/05/16 = 12 meses + 19 dias
> 12 × 1% + 19 × (1/30)% = 12% + 0,63333% = 12,63333%   = os 12,6333% publicados
> ```
>
> A taxa diária efetiva é **1% ÷ 30 = 0,0333…% ao dia** — um centésimo do que está impresso.
> Confere exatamente; com 0,0333% arredondado daria 12,6327%.
>
> O erro de grafia se repete no exemplo seguinte (p. 73).

---

## 10. Seguro-desemprego — regime a partir de 28/02/2015 (6.13.4, p. 73)

```
Período trabalhado: 01/03/2014 a 31/07/2015  (17 meses)
Salários: mai/15 R$ 950,00 · jun/15 R$ 985,00 · jul/15 R$ 985,00
Propositura da ação: 25/09/15
```

**Passo 1 — número de parcelas.** 17 meses de vínculo comprovado → **4 parcelas**,
"independentemente do número de solicitações". É o atalho da espinha § 7.4.3: acima de 12
meses as três linhas da tabela convergem.

**Passo 2 — salário médio**

```
(950,00 + 985,00 + 985,00) / 3 = R$ 973,33
```

**Passo 3 — enquadrar**: 1ª faixa da tabela jan/15 a dez/15.

```
973,33 × 0,8 = 778,66
```

> **O piso entra aqui.** 778,66 é inferior ao salário mínimo de **R$ 788,00** vigente em
> jul/15. Prevalece **788,00** — Lei 7.998/90, art. 5º, § 2º. É o único exemplo do capítulo
> em que o piso efetivamente muda o resultado.

**Passo 4** — `788,00 × 4 = R$ 3.152,00`

**Passos 5 e 6**

| | Valor |
|---|---:|
| Indenização | 3.152,00 |
| Índice 01/08/15 a 31/05/16 | 1,01652683 |
| Atualizada até 31/05/16 | **3.204,09** |
| Juros 25/09/15 a 31/05/16 — **8,2%** | **262,74** |
| **Total** | **R$ 3.466,83** |

**Conferência**: `3.152 × 1,01652683 = 3.204,0926 → 3.204,09` ✓;
`3.204,09 × 8,2% = 262,735 → 262,74` ✓; `3.204,09 + 262,74 = 3.466,83` ✓.

Juros: `8 meses × 1% + 6 dias × 0,0333% = 8,1998% ≈ 8,2%` ✓ — confirmando de novo que a taxa
diária é 0,0333%, não os 0,33% impressos.

> **Defeito do original.** A linha de total imprime "(3.204,09 + **404,78**)". O valor dos
> juros é 262,74, e `3.204,09 + 404,78 = 3.608,87`, não os 3.466,83 publicados. O número
> 404,78 não aparece em nenhum outro ponto do exemplo. O total publicado está correto.

---

## 11. Vale-transporte — com e sem a dedução dos 6% (6.13.6, p. 74–75)

Base comum: **2,15** por passagem, **44 passagens/mês** (22 dias × 2), valor mensal
`2,15 × 44 = 94,60`.

### 11.1 Sem redução dos 6%

| Mês | Salário | 6% | Indenização | Índice AM mar/12 | Corrigido |
|---|---:|---:|---:|---:|---:|
| jan/11 | 600,00 | 36,00 | 94,60 | 1,033108290 | 97,73 |
| fev/11 | 600,00 | 36,00 | 94,60 | 1,012780133 | 95,81 |
| mar/11 | 720,00 | 43,20 | 94,60 | 1,011554129 | 95,69 |
| abr/11 | 720,00 | 43,20 | 94,60 | 1,011184003 | 95,66 |
| **Total corrigido até 31/03/12** | | | | | **384,89** |
| Juros 25/07/11 a 31/03/12 — 8,20% | | | | | 31,56 |
| **Total** | | | | | **R$ 416,45** |

### 11.2 Com redução dos 6%

| Mês | Base (`94,60 − 6% do salário`) | Índice | Corrigido |
|---|---:|---:|---:|
| jan/11 | 58,60 | 1,033108290 | 60,54 |
| fev/11 | 58,60 | 1,012780133 | 59,35 |
| mar/11 | 51,40 | 1,011554129 | 51,99 |
| abr/11 | 51,40 | 1,011184003 | 51,97 |
| **Total corrigido** | | | **223,86** |
| Juros 8,20% | | | 18,36 |
| **Total** | | | **R$ 242,21** |

**Conferência.** Os dois quadros fecham **com precisão plena**, e a aparente divergência de um
centavo no segundo é só exibição:

```
soma exata com 6%  = 223,8578…  → publicado 223,86 ✓
223,8578 × 1,082   = 242,2141…  → publicado 242,21 ✓
(a soma das quatro linhas arredondadas daria 223,85)
```

> **O contraste é o ponto do par de exemplos**: a mesma situação de fato produz **R$ 416,45**
> ou **R$ 242,21** conforme a dedução dos 6% se aplique — diferença de **42%**. O manual não
> escolhe: manda olhar o comando exequendo.

---

## 12. Ajuda-alimentação (6.13.7, p. 75)

`2,15 × 22 dias = 47,30` por mês.

| Mês | Valor | Índice AM mar/12 | Corrigido |
|---|---:|---:|---:|
| jan/11 | 47,30 | 1,033108290 | 48,87 |
| fev/11 | 47,30 | 1,012780133 | 47,90 |
| mar/11 | 47,30 | 1,011554129 | 47,85 |
| abr/11 | 47,30 | 1,011184003 | 47,83 |
| **Total corrigido** | | | **192,45** |
| Juros 8,20% | | | 15,78 |
| **Total** | | | **R$ 208,23** |

Conferência: todas fecham.

> O valor unitário de R$ 2,15 é o mesmo da passagem do § 11 — o manual reaproveitou o número
> do exemplo anterior. E o cabeçalho da coluna diz "**Nº de passagens**" numa tabela de
> ajuda-alimentação. Resíduo de cópia, sem efeito na conta.

---

## 13. Multa do art. 467 e a base proporcional do IR (6.13.9, p. 76)

Salário-base de cálculo: **R$ 5.000,00**.

| Parcela | Vr. devido | Multa (50%) | Total | Base de cálculo do IR |
|---|---:|---:|---:|---:|
| Aviso prévio (**52 dias**) | 8.666,67 | 4.333,33 | 13.000,00 | — |
| 13º salário (**8/12**) | 3.333,33 | 1.666,67 | 5.000,00 | **5.000,00** |
| Férias prop. + 1/3 (**10/12**) | **5.555,42** | 2.777,71 | 8.333,13 | — |
| Saldo de salários | 4.166,67 | 2.083,33 | 6.250,00 | **6.250,00** |
| Multa 40% FGTS | 7.680,00 | 3.840,00 | 11.520,00 | — |
| **Totais** | **29.402,08** | **14.701,04** | **44.103,13** | **11.250,00** |

**Conferência.** Quatro das cinco linhas fecham:

- Aviso 52 dias: `5.000,00 / 30 × 52 = 8.666,67` ✓
- 13º 8/12: `5.000,00 × 8/12 = 3.333,33` ✓
- Saldo: `5.000,00 / 30 × 25 = 4.166,67` ✓ — *os 25 dias são reconstrução desta extração; o
  manual só imprime o valor*
- Multa de 40%: implica saldo de FGTS de `7.680,00 / 0,40 = 19.200,00`

A **linha de totais também não fecha**: as cinco parcelas somam **29.402,09** e o manual
imprime **29.402,08** — truncamento, a quarta prática do § 15. A partir daí a cadeia é
consistente: `29.402,08 / 2 = 14.701,04` e `29.402,08 + 14.701,045 = 44.103,125 → 44.103,13`.

> **Erro material do original — as férias proporcionais.**
>
> `5.000,00 × 10/12 = 4.166,67`; acrescido do terço, `× 4/3 = 5.555,56`. O manual publica
> **5.555,42**, R$ 0,14 a menos. Nenhuma variação plausível da conta reproduz esse número —
> testei `5.000/30 × 25 × 4/3`, `4.166,67 + 4.166,67/3` e a soma separada de férias e terço,
> e todas dão 5.555,56.
>
> O erro propaga para a multa (2.777,71 em vez de 2.777,78) e para o total.

> **A regra que o exemplo existe para demonstrar** é a última coluna. A multa do art. 467
> incide sobre cinco parcelas, mas **só duas são tributáveis** — 13º salário e saldo de
> salários. A base do IR da multa é a **proporção** correspondente, e não o total de
> R$ 14.701,04.

---

## 14. Multa diária — o marco da atualização (6.13.10, p. 77)

```
Multa fixada:  R$ 100,00 por dia
Limite:        R$ 3.000,00
Limite atingido no 30º dia  (100,00 × 30 = 3.000,00)
Correção monetária e juros correm a partir do 31º dia
```

> **Regra fácil de errar**, e é por isso que o manual a enuncia: a multa **não** se corrige
> enquanto ainda está crescendo. Corrigir desde o primeiro dia contaria correção sobre valor
> que ainda não era devido.

---

## 15. O quadro de arredondamento deste bloco

O manual continua sem enunciar critério algum. Este bloco exibe **quatro** práticas
distintas — uma a mais que o bloco 3.

| Prática | Onde | Evidência |
|---|---|---|
| **Precisão plena** | § 1 (supressão), § 4 (intervalo art. 253), § 7.2 (AN, coluna de valor), § 8.1 (comissionista), § 11 (vale-transporte) | `1500/220 × 1,8 × 28,5 = 349,77`; com 12,27 exibido daria 349,70 |
| **Valor exibido** | § 3 (intervalo comum), § 7.3 (AN, reflexos) | `5,11 × 25,71 = 131,38`; a plena daria 131,49 |
| **Arredondamento a cada passo** | § 7.1 (horas noturnas) | `3 → 3,4285 → 13,71 → 58,76`; a plena daria 58,7755 |
| **Truncamento** | § 9 (seguro-desemprego) | `1.014,335 × 5 = 5.071,675 → 5.071,67`; arredondado daria 5.071,68 |

> As duas primeiras aparecem **em páginas consecutivas sobre o mesmo valor unitário** (§§ 7.2
> e 7.3), como no bloco 3 ocorria entre as p. 42 e 46.
>
> A quarta — truncamento — é nova e **coincide com o critério do Manual CJF**
> (`pendencias.md` § 3), que o bloco 2 havia contraposto ao arredondamento do TRT-3. O
> mesmo manual faz as duas coisas.

Pendência **P17** da espinha; agrava a **P10** do bloco 3 e a **§ 9-A** de `pendencias.md`.
