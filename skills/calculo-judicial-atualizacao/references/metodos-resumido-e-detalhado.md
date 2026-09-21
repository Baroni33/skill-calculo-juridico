# Método resumido × método detalhado — os dois procedimentos do Manual CJF

**Carregue este arquivo quando for implementar o cálculo de atualização, ou quando precisar
reproduzir as fixtures 2 e 4.** Ele contém **o procedimento**, não só o resultado.

**Fonte:** Manual CJF, Res. 990/2026 — `manual_de_calculos_2026.pdf`, **93 páginas**, offset de
paginação **1** (`numero_impresso = pagina_pdf − 1`). Itens **4.2.1.1, NOTA 6** (`pagina_pdf`
50–53) e **5.2.1** (`pagina_pdf` 90–92).

> **O erro que este arquivo existe para não cometer:** implementar **um** método e comparar o
> resultado com o número de **outro**. As fixtures **2** e **4** asseveram divergência **entre os
> dois métodos do próprio manual** — R$ 0,01 e R$ 0,03, com `divergencia_e_assercao: true`. **Sem
> os dois procedimentos, um motor produz um número e não tem o que comparar.**

---

## 1. A regra de escolha — **o default é o RESUMIDO**

Literal, item **5.2.1**, `pagina_pdf` **90**:

> "A apuração do resíduo pode ser feita mediante **dois procedimentos: o método resumido ou o
> método detalhado**. **Salvo decisão judicial em contrário ou necessidade de informações
> específicas, deve-se utilizar o cálculo resumido**."

**É a única regra de escolha entre os dois em todo o manual.** O item **4.2.1.1** apresenta os
dois lado a lado e **não hierarquiza** — ali a escolha é do operador.

**Comum aos dois**, mesma página: *"Para qualquer método utilizado, **separam-se as parcelas que
compõem o total do débito** (principal, juros, honorários etc.)"*. **Principal e juros andam em
linhas próprias do começo ao fim, e os honorários incidem sobre cada um separadamente.**

---

## 2. Procedimento **RESUMIDO** — executável

**Definição literal**, item 5.2.1.1, `pagina_pdf` 90:

> "Neste procedimento, a conta considera o **abatimento de valores pagos, sem a incidência de
> juros sobre juros**, quando for o caso de aplicar juros, **para uma única data de atualização,
> partindo dos valores do cálculo original**."

**A legenda das colunas é IMPRESSA pelo manual** — isto é **citação**, não reconstrução. **Mas são
DUAS legendas diferentes, e a de baixo só existe na `pagina_pdf` 53.** Reusar as letras de uma na
outra troca juros por total.

**`pagina_pdf` 52** — 1º Exemplo, data-base jun/2022, **duas** colunas de taxa, **nove** letras:

```
(A) Valor   (B) Coeficiente   (C) = A x B   (D) % Juros até 12/2021   (E) % SELIC
(F) = C x D%        Juros até 12/2021
(G) = (C + F) x E%  Juros SELIC          ← aqui (G) é SELIC, não "juros até 12/2021"
(H) = F + G         Juros Soma
(I) = C + H         TOTAL                ← aqui (I) é o TOTAL, não "juros pós-set/2025"
```

**`pagina_pdf` 53** — 2º Exemplo, data-base jun/2026, **três** colunas de taxa, **onze** letras:

```
(A) Valor
(B) Coeficiente de correção monetária          ← acumulado da competência até a DATA-BASE, 10 casas
(C) = A x B      Principal correção monetária
(D) % Juros Até 12/2021      (E) % SELIC      (F) % a partir de out./2025
(G) = C x D%     Juros Até 12/2021
(H) = (C + G) x E%           Juros SELIC
(I) = C x F%     Juros a partir de out./2025
(J) = G + H + I  Juros Total
(L) = C + J      Total
```

> **As letras são POSICIONAIS, e a tabela de S1–S9 abaixo usa as da `pagina_pdf` 53.** O esquema da
> **52** é o **mesmo procedimento com um regime a menos** — ele não tem `(I) = C × F%` porque o caso
> termina em jun/2022, antes de out/2025. Quem citar "`(G) = C × D%`" apontando para a `pagina_pdf`
> **52** está citando a **coluna errada**: lá `(G)` é a SELIC.

| # | O que se faz | Sobre que valor | Casas | Trunca? | Proveniência |
|---|---|---|---|---|---|
| **S1** | uma linha por **parcela devida** e uma por **pagamento**; principal e juros originais em linhas separadas | — | — | — | **citação** (5.2.1, p. 90) |
| **S2** | `(B)` = **coeficiente acumulado único**, da competência da linha até a **data-base**, produto de toda a cadeia de indexadores do intervalo | — | **10** | impresso com 10 casas | **citação** das 10 casas; **inferência** de ser o produto da cadeia |
| **S3** | `(C) = A × B` | valor nominal | **2** | **SIM** | fórmula é **citação**; truncamento é **inferência** — `1.000,00 × 1,1339588923 = 1.133,9588923`, publicado **1.133,95** |
| **S4** | `(G) = C × D%` | **`(C)`**, o principal **já corrigido até a data-base** | **2** | **SIM** | **citação** da fórmula; truncamento **inferido** — `1.142,01 × 2,45% = 27,979245` → **27,97** |
| **S5** | `(H) = (C + G) × E%` | **principal corrigido + juros do passo anterior** | **2** | **SIM** | **citação** — é aqui que a SELIC incide sobre principal **E** juros (`R-08-14`) |
| **S6** | `(I) = C × F%` | **`(C)` puro** — **sem** os juros anteriores | **2** | **SIM** | **citação**. **A assimetria com `(H)` é do manual, não engano de transcrição** |
| **S7** | `(J) = G + H + I`; `(L) = C + J`; totais por **soma de coluna** | valores já truncados | — | não | **citação** |
| **S8** | pagamentos: mesmo tratamento, **subtraídos**; a parcela de **juros do cálculo original** recebe **só correção monetária** — célula `(juros cor/mon.)` | — | **2** | **SIM**, cada célula | **citação** da rotulação e de *"sem juros sobre juros"* |
| **S9** | **honorários** = `% ×` subtotal, **separadamente** sobre principal e sobre juros | subtotais | **2** | **SIM** | **inferência** — `1.575,38 × 10% = 157,538` → **157,53** |

> **O ponto que mais se erra:** `(G) = C x D%` aplica uma taxa **de período anterior** sobre um
> principal **corrigido até a data-base**. Parece dupla contagem e **não é** — é a mesma conta do
> detalhado com os fatores em ordem trocada. A § 4 prova por comutatividade.

---

## 3. Procedimento **DETALHADO** — executável

**Definição literal**, item 5.2.1.2, `pagina_pdf` 91:

> "Neste procedimento, a conta é elaborada **passo a passo, partindo-se dos valores originários**,
> com a aplicação da correção monetária e juros devidos, com o abatimento dos valores pagos, **nos
> seguintes momentos: 1º) até a data da apresentação do precatório; 2º) até a data final do prazo
> constitucional; 3º) até a data final de atualização**."

**Os marcos de 4.2.1.1 são os títulos das alíneas** (`pagina_pdf` 51–52, **citação**):
`a) Atualização dos valores até dez./2021` · `b) [...] de dez./2021 até set./2025` ·
`c) [...] de set./2025 a jun./2026`.

| # | O que se faz | Sobre que valor | Casas | Trunca? | Proveniência |
|---|---|---|---|---|---|
| **T0** | definir os **marcos** — um por regime/evento | — | — | — | **citação** |
| **T1** | corrigir o principal pelo coeficiente **daquele trecho só** | principal vigente no marco anterior | **10** coef · **2** valor | **SIM** | truncamento **inferido** — `20.000 × 1,0777734324 = 21.555,468648` → **21.555,46** |
| **T2** | aplicar a **taxa do trecho** sobre o principal corrigido **do próprio trecho** | resultado de T1 | **2** | **SIM** | **inferência** — `21.555,46 × 9% = 1.939,9914` → **1.939,99** |
| **T3a** | corrigir o **bloco de juros acumulado** pelo coeficiente do trecho — célula `(juros correção monetária)` / `(juros cor/mon.)` | juros acumulados até o marco anterior | **2** | **SIM** | **citação** da rotulação; truncamento **inferido** |
| **T3b** | **se o indexador de juros do trecho ENGLOBA correção** (SELIC, taxa legal), aplicar a **taxa também sobre o bloco de juros** | bloco de juros de T3a | **2** | **SIM** | **citação** — `Dez./2021 · R$ 55,75 · (juros) · 5,05 · R$ 2,81` (p. 51) e `· 43,89 · R$ 24,46` (p. 52) |
| **T4** | **agregar por coluna** (`Soma:` / `TOTAL`) e levar **o agregado** ao marco seguinte | — | — | não | **citação** |
| **T5** | parcela **posterior** ao marco entra pelo **nominal**, com a taxa do seu trecho — que **não é** a do agregado | nominal | **2** | **SIM** | **citação** — linha `Fev./2022`: **3,55%** contra os 5,05% do agregado (p. 51); **42,39%** contra 43,89% (p. 52) |
| **T6** | **pagamento**: corrigido pelo coeficiente do seu trecho, principal e juros em linhas próprias, **subtraído dentro do passo do marco** | nominal pago | **2** | **SIM**, cada célula | **citação** — *"com o abatimento dos valores pagos"* e as linhas entre parênteses da p. 92 |
| **T7** | honorários, igual a S9 | — | **2** | **SIM** | **inferência** |

> **A ÚNICA diferença estrutural entre os métodos: o detalhado AGREGA antes de aplicar a taxa
> seguinte; o resumido nunca agrega antes do fim.** As duas linhas `Dez./2021` da `pagina_pdf` 51
> — **R$ 2.275,96** (principal) e **R$ 55,75** (juros) — **são os totais de coluna** da sub-tabela
> anterior, e a SELIC de 5,05% incide **uma vez sobre cada agregado**.

### 3.1 As três coisas que quase todo implementador erra — e cada uma tem célula que a refuta

**1. O primeiro marco NÃO tem um coeficiente só: tem um POR PARCELA, e trunca POR LINHA.** O marco
`a)` da `pagina_pdf` 51 traz `1,1420100005` para jan/2020 e `1,1339588923` para fev/2020, e os
juros saem `27,97 + 27,78 = 55,75`. **Um coeficiente sobre o agregado daria
`2.275,96 × 2,45% = 55,76102 → 55,76`**, e o manual publica **55,75**. Só depois de `Soma:` é que
existe agregado.

**2. A taxa do trecho INCIDE sobre o bloco de juros quando o indexador de juros engloba a
correção.** É célula impressa, nos dois Exemplos:

| `pagina_pdf` | Célula publicada |
|---|---|
| **51** | `Dez./2021 · R$ 55,75 · (juros) · 5,05 · R$ 2,81 · R$ 58,56` |
| **52** | `Dez./2021 · R$ 55,75 · (juros) · 43,89 · R$ 24,46 · R$ 80,21` |

`55,75 × 43,89% = 24,468675 → 24,46` — **é a mesma célula que a § 6 desta página já usava como
prova de truncamento** (half-up daria 24,47).

> **O discriminante NÃO é "juros não rendem juros". É `R1`.** Quando o indexador de juros do trecho
> **engloba correção monetária** (SELIC, taxa legal), **o trecho não tem coeficiente próprio** — a
> taxa é a **única** correção que o bloco de juros recebe ali, e por isso incide sobre ele
> (**T3b**). Quando o trecho **tem** coeficiente próprio (INPC, IPCA-E, IPCA-15), o bloco leva o
> **coeficiente** e **não** a taxa: é a célula `(juros correção monetária)` do marco `c)` da
> `pagina_pdf` 52 (`1.503,02 × 1,0417234826 = 1.565,73`, **sem coluna `% Juros`**) e a
> `(juros cor/mon.)` da `pagina_pdf` 92.
>
> **É EXATAMENTE a assimetria que o resumido já imprime na legenda:** `(H) = (C + G) × E%` —
> SELIC sobre principal **e** juros — contra `(I) = C × F%` — taxa legal **só** sobre o principal.
> Os dois métodos dizem a mesma coisa; o detalhado dizia-a em célula e o resumido em fórmula.
>
> **A célula correção-pura `1.503,02 → 1.565,73` é o marco `c)`, não o `b)`.** Ler o `c)` como se
> fosse a regra do `b)` é o erro que produz a proibição.

**3. Um marco pode ter MAIS DE UMA taxa ao mesmo tempo.** O marco `b)` da `pagina_pdf` 52 aplica
**43,89%** ao agregado de dez/2021 **e 42,39%** à parcela de fev/2022, **no mesmo passo** — porque
o trecho de fev/2022 começa depois. Na `pagina_pdf` 51, **5,05%** e **3,55%**.

**Verificado, e é executável:** `scripts/calculo/test_metodos.py` reproduz **3.484,95** (p. 51),
**5.218,27** (p. 52), **5.218,28** (p. 53) e **4.435,07 · 4.435,04 · Δ 0,03** (pp. 91–92) **célula
por célula, a partir dos coeficientes impressos** — **sem série**.

---

## 4. Onde os dois se separam — com a operação nomeada

### 4.1 Fixture 2 — R$ 0,01 (item 4.2.1.1, 2º Exemplo, data-base jun/2026)

| Componente | Resumido (p. 53) | Detalhado (p. 52) | Diverge? |
|---|---|---|---|
| Principal corrigido | Σ`(C)` = **3.412,64** | `trunc(3.275,96 × 1,0417234826)` = **3.412,64** | **não** |
| Juros pós-set/2025 | Σ`(I)` = **239,90** | `trunc(3.412,64 × 7,03%)` = **239,90** | **não** |
| **Bloco juros-até-12/2021 + SELIC, trazido a jun/2026** | Σ`(G)`+Σ`(H)` = **1.565,74** | `trunc(1.503,02 × 1,0417234826)` = **1.565,73** | **SIM** |
| **Total** | **5.218,28** | **5.218,27** | **R$ 0,01** |

**Operação nomeada: a correção monetária do bloco de juros acumulado, de set/2025 a jun/2026.** O
detalhado a faz **uma vez, sobre o agregado já truncado**; o resumido a tem **embutida em `(C)`** e
chega ao mesmo lugar por **cinco truncamentos de linha** (dois `(G)`, três `(H)`).

### 4.2 Fixture 4 — R$ 0,03 (item 5.2.1, precatório complementar)

| Componente | Resumido (p. 91) | Detalhado (p. 92) | Δ |
|---|---|---|---|
| Subtotal principal | **1.575,38** | **1.575,36** | **0,02** |
| Subtotal juros | **2.456,51** | **2.456,50** | **0,01** |
| Honorários 10% | 157,53 · 245,65 | 157,53 · 245,65 | **0,00** |
| **TOTAL DA CONTA** | **4.435,07** | **4.435,04** | **R$ 0,03** |

**Operação nomeada: a subtração do pagamento.** O resumido faz
`trunc(20.000 × 1,1883716656) − trunc(21.000 × 1,0567647130)`. Os `0,008973` desprezados ao
truncar `22.192,058973 → 22.192,05` estão no **subtraendo** — **e ficam no resíduo**. O detalhado
trunca o principal **três vezes em cascata descendente** e chega **0,014339 abaixo** do exato.

---

## 5. A hipótese do truncamento — **CONFIRMADA**, com duas correções

**Confirmada, e é causa única.** Removido o truncamento, os dois métodos produzem o **mesmo número
exato**. Por linha da fixture 2:

```
resumido   G+H = 1000 · c · k · (0,0245 + 1,0245 × 0,4389)
detalhado      = 1000 · c · (0,0245 + 1,0245 × 0,4389) · k
Decimal(60):     564.08027018950592144500596500   ← idêntico dos dois lados
```

**É comutatividade da multiplicação.** Na fixture 4, sem truncamento, os caminhos dão
`1.575,3743390000` e `1.575,374339710024…` — **7 × 10⁻⁷**, **sete ordens de grandeza abaixo do
centavo**: o arredondamento dos coeficientes publicados a 10 casas **não contribui com nada**.

**Correção 1 — não é a CONTAGEM de truncamentos, é QUANDO se trunca.** Perda truncada cedo é
**multiplicada por todos os fatores seguintes**. Na fixture 2 o detalhado perde `0,01123787` ao
truncar `55,76123787 → 55,75` no **primeiro** marco; essa perda chega a jun/2026 amplificada por
`1,4389 × 1,0417234826` = **`0,01684`** — **sozinha maior que o centavo em disputa**. Os cinco
truncamentos de linha do resumido compensam **em parte**, e o saldo é o R$ 0,01.

**Correção 2 — truncamento em SUBTRAENDO inverte o sinal do desvio.** Na fixture 4 o resumido cai
**acima** do exato. **Um comparador que suponha *"truncar sempre puxa para baixo"* erra este
caso.**

---

## 6. `D8-D33` — o manual diz "arredondamento" e faz **truncamento**

| `pagina_pdf` | Palavra usada |
|---|---|
| **53** (4.2.1.1) | *"inerentes ao critério de **truncamento** de casas decimais aplicado em cada etapa do cálculo"* |
| **92** (5.2.1.2) | *"de **arredondamento** de casas decimais no decorrer do cálculo"* |

**A aritmética diz truncamento nos dois.** Seis células em que `ROUND_HALF_UP` daria outro número:

| Célula | Exato | Truncado | Half-up | **Publicado** |
|---|---|---|---|---|
| 4.2.1.1 fev/2020 principal | 1.133,9588923 | 1.133,95 | 1.133,96 | **1.133,95** |
| 4.2.1.1 jan/2020 juros 2,45% | 27,979245 | 27,97 | 27,98 | **27,97** |
| 4.2.1.1 SELIC 43,89% s/ juros | 24,468675 | 24,46 | 24,47 | **24,46** |
| 5.2.1 resumido, pago 8/2018 | 22.192,058973 | 22.192,05 | 22.192,06 | **22.192,05** |
| 5.2.1 detalhado, 3º passo | 1.575,368833977 | 1.575,36 | 1.575,37 | **1.575,36** |
| 5.2.1 detalhado, juros pagos | 3.176,18682129 | 3.176,18 | 3.176,19 | **3.176,18** |

> **Quem implementar 5.2.1.2 lendo a obs. ao pé da letra e usar `ROUND_HALF_UP` não reproduz
> nenhuma das doze células e não obtém R$ 4.435,04.** Vale a `pagina_pdf` 53 — **truncamento** — e
> ela vale para **os dois itens**. É o que `R12` já dizia; **agora com a refutação medida**.

---

## 7. `D8-D32` confirmado — e **não** era artefato da extração

A `pagina_pdf` **52 imprime `R$ 5.218,2`** — conferido por **renderização da página a 250 dpi**, e
não só pela camada de texto. **É defeito do original**: a célula estourou a largura e o dígito
final não está no PDF. O valor **5.218,27** segue **derivado por aritmética**
(`3.412,64 + 1.805,63`), e a § 4.1 mostra que **1.805,63 é o número que o procedimento detalhado
produz** — não uma conveniência para fechar a diferença declarada.

---

## 8. Escopo da varredura que sustenta o "não há mais nada"

`manual_de_calculos_2026.pdf`, **todas as 93 páginas**, texto normalizado sem acento, caixa baixa:

| termo | ocorrências | `pagina_pdf` |
|---|---|---|
| `resumid` | 6 | 10 (sumário), **52**, **53**, **90** |
| `detalhad` | 5 | 10 (sumário), **51**, **52**, **90**, **91** |
| `trunca` | **1** | **53** |
| `arredond` | **1** | **92** |
| `casas decimais` | 2 | **53**, **92** |
| `passo a passo` | **1** | **91** |
| `centavo` · `desprezivel` | 1 · 1 | **53** · **92** |

**Fora do sumário, o universo são duas ilhas — 51–53 e 90–92 — lidas inteiras**, mais as vizinhas
**49–50**, **89** e **93**, que confirmam que o procedimento não continua fora delas.

**O que a varredura NÃO achou, e por isso é inferência e não citação:**

1. **o número de casas decimais** nunca é declarado. `casas decimais` ocorre **duas vezes**, nas
   duas observações, e **nenhuma diz quantas**. As **2 casas** dos valores e as **10** dos
   coeficientes saem de **contar os dígitos impressos** nas tabelas;
2. **o item 4.2.1.1 não define nenhum dos dois métodos em prosa.** Usa *"Cálculo detalhado"* e
   *"Cálculo resumido"* como rótulo de tabela e, no fim, *"Os dois métodos de cálculo devem
   conduzir ao mesmo resultado"*. **A definição em prosa só existe em 5.2.1**, e a **legenda de
   fórmula** só existe em 4.2.1.1. **Os dois itens se completam, e nenhum é executável sozinho** —
   é por isso que este arquivo cruza os dois;
3. **o truncamento por célula** é inferido da aritmética em todas as tabelas. **Nunca há uma
   sentença dizendo "trunque cada etapa em duas casas"** — há só a obs. da p. 53 dizendo que o
   critério **existe** e é aplicado *"em cada etapa"*.

---

## 9. Ponteiros

| Assunto | Onde |
|---|---|
| Espinha — os dois métodos condensados | `docs/calculo/consolidado/02-atualizacao.md` § 10-A |
| Detalhe — proveniência linha a linha, aritmética completa | `docs/calculo/consolidado/02-atualizacao-detalhe.md` §§ 10-A.0 a 10-A.9 |
| Fixtures 1 a 3 — a cadeia | `references/civel-federal.md` § 8 |
| Fixture 4 — precatório complementar | `references/tributario-federal.md` § 7 |
| **O teste que confronta o procedimento** — células publicadas, **sem série**. Teste **do repositório**, em Python; confere o procedimento contra o número impresso e **não é modelo de implementação** | `scripts/calculo/test_metodos.py` |
| `R12` e as cinco cadeias de arredondamento | `skills/calculo-judicial-core/SKILL.md` |
| Linguagem-alvo, tipo decimal exato, e por que a implementação de referência não é exemplo de aceite | `skills/calculo-judicial-core/references/linguagem-alvo-e-aritmetica.md` |
| Consolidação de dez/2021 | `docs/calculo/consolidado/02-atualizacao.md` § 10 |
