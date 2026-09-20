# Cível — cadeia NACIONAL do Código Civil

Correção monetária e juros de mora das dívidas de **natureza civil**, em qualquer tribunal.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 4; `00-base-normativa.md` §§ 3 e 4;
`consolidado/08-nacional-e-regional.md` § 6.1; `consolidado/01-dominio-e-invariantes.md` §§ 2.4,
2.5 e 2.6.

---

## 1. Por que "nacional"

O trecho central desta cadeia vem do **STJ, Tema 1368** — Corte Especial, j. **15/10/2025**,
REsp **2.199.164/PR** e REsp **2.070.882/RS**, Rel. Min. Ricardo Villas Bôas Cueva, acórdão
publicado em **20/10/2025**. É **vinculante**, e **substitui a prática anterior do TJMG** (tabela
CGJ + 1% a.m.) para o período pré-Lei 14.905.

**A parte regional desta jurisdição — a tabela da CGJ/TJMG — está em
`references/civel-regional-tjmg.md`.** Aqui fica o que vale em qualquer estado.

---

## 2. A cadeia

| Período | Correção monetária | Juros de mora |
|---|---|---|
| **Até dez/2002** | Tabela da corregedoria local (**em MG**, a CGJ/TJMG) | **0,5% simples** — CC/1916, arts. 1.062–1.064 |
| **Jan/2003 a 29/08/2024** | **SELIC** — **engloba ambos** (R1) | — |
| **A partir de 30/08/2024** | **IPCA** — CC art. 389, § único | **taxa legal** — CC art. 406, § 1º |

### 2.1 Tema 1368 — o que ele decidiu, literal

> *"O art. 406 do Código Civil de 2002, antes da entrada em vigor da Lei n° 14.905/2024, deve ser
> interpretado no sentido de que é a SELIC a taxa de juros de mora aplicável às dívidas de
> natureza civil, por ser esta a taxa em vigor para a atualização monetária e a mora no pagamento
> de impostos devidos à Fazenda Nacional."*

**A SELIC engloba simultaneamente correção monetária e juros moratórios, vedada sua cumulação
com outros índices inflacionários** — é **R1** dita pelo próprio acórdão.

**Precedentes referenciados:** EREsp 727.842/SP; Temas 99, 112 e 113 dos repetitivos da 1ª Seção;
REsp 1.795.982/SP; RE 1.558.191/SP (STF, 2ª Turma, j. 12/09/2025).

### 2.2 O corte de 30/08/2024 — Lei 14.905/2024

A partir de 30/08/2024 a cadeia **deixa de englobar**: correção por **IPCA** e juros por **taxa
legal**, dois componentes distintos, que **somam** — e é o **único** ponto desta cadeia em que
somar correção e juros é correto.

> **Afirmação de ausência, com escopo declarado.** Varredura de `eixo` em
> `consolidado/02-atualizacao.md` e `02-atualizacao-detalhe.md` — 7 ocorrências, **nenhuma sobre
> 30/08/2024**; varredura de `29/08/2024`, `30/08/2024`, `14.905` e `14905` nos 11 arquivos do
> consolidado — 8 ocorrências, **todas em quadro de fase**. **O consolidado não nomeia o eixo
> deste corte.** Ele é **inferido da forma do quadro** (mês de atualização), e a resolução deve
> marcar `eixo_inferido: true`.

---

## 3. Termos iniciais — `R7`, e não são intercambiáveis

| Situação | Correção monetária | Juros |
|---|---|---|
| **Regra geral** | — | **citação** (CPC) |
| Responsabilidade **extracontratual** | — | **evento danoso** — **Súmula 54/STJ** |
| **Ato ilícito** | **efetivo prejuízo** — **Súmula 43/STJ** | — |
| **Dano moral** | **arbitramento** — **Súmula 362/STJ** | — |

> **O termo inicial cível NÃO é o trabalhista.** Lá é o **ajuizamento** (CLT art. 883, Súmula
> 200/TST). Na repetição de indébito é o **trânsito em julgado**. Trocar entre jurisdições é
> violação de **R7**.

Presets correspondentes: `CIVEL-DANO-MORAL` (Súmula 362) e `CIVEL-ATO-ILICITO` (Súmula 43 para a
correção; Súmula 54 para os juros, se extracontratual).

---

## 4. A taxa legal — `R11`

**Fonte:** **Resolução CMN n. 5.171, de 29/08/2024** (DOU 30/08/2024, Edição 168, Seção 1, pp.
259–260), vigência imediata, regulamentando o art. 406 do CC na redação da Lei 14.905/2024.

```
TL_m = (Fator_Selic_m / Fator_IPCA15_{m-1} − 1) × 100
```

- **seis casas decimais**;
- razão entre a acumulação das **Taxas Selic diárias** e a variação do **IPCA-15**, ambos
  **relativos ao mês anterior** ao de referência;
- **resultado negativo é zero** no mês de referência — CC art. 406, § 3º (**R6**);
- **juros simples**, inclusive e especialmente na acumulação de taxas mensais e no *pro rata*
  (**R4**).

### 4.1 NÃO é subtração de percentuais

A lei e o acórdão descrevem *"SELIC deduzido o IPCA"*. **Isso é descrição do efeito. A operação é
razão entre fatores.** Implementar a subtração literal produz número errado.

Validação aritmética contra a tabela do Manual CJF (Res. 990/2026):

| Competência | Fator Selic | Fator deflator | Manual | **Razão** | Subtração |
|---|---|---|---|---|---|
| **Set/2025** | 1,01164156 | 0,9979 | 1,377047% | **1,377047%** ✓ | 1,374156% ✗ |
| **Mai/2026** | 1,01090058 | 1,0081 | 0,277807% | **0,277807%** ✓ | 0,280058% ✗ |

**Divergência de ~0,003 p.p./mês. Acumula.**

> **Ressalva de cobertura, declarada.** Os dois pares acima são da tabela de **taxa legal
> PREVIDENCIÁRIA** do Manual CJF, cuja coluna é `Fator INPC` — **são do caso INPC, não do caso
> geral**. A variante **IPCA-15**, que é a regra geral e a de maior uso, está **sem par de
> validação contra valor publicado**. A aritmética é compartilhada e está coberta; o que falta é
> a confirmação de que a **série correta** alimenta `fator_deflator`. **Pendência aberta** —
> `pendencias.md` § 2.

### 4.2 Truncamento, não arredondamento

| Competência | Razão exata | **Truncado** | Half-up | Manual |
|---|---|---|---|---|
| Set/2025 | 1,3770478004 | **1,377047** ✓ | 1,377048 ✗ | 1,377047 |
| Mai/2026 | 0,2778077572 | **0,277807** ✓ | 0,277808 ✗ | 0,277807 |

**Half-up erra o último dígito nos dois casos.** Corroborado pelo texto do Manual CJF
(`pagina_pdf` 53): *"são inerentes ao critério de truncamento de casas decimais aplicado em cada
etapa do cálculo"*. `ROUND_DOWN`, com teste negativo que falha se alguém trocar por half-up.

### 4.3 Divulgação e oráculo de teste

O **Banco Central** divulga mensalmente a taxa legal, o `Fator Selic_m` e o `Fator IPCA_m`.
Séries no SGS — **série 29541** = Fator da Taxa Selic mensal para cálculo da Taxa Legal. Primeira
taxa divulgada em **30/08/2024**, aplicável aos dias **30 e 31/08/2024**; a partir de setembro de
2024, no **primeiro dia útil** de cada mês. A **Calculadora do Cidadão** do BCB tem módulo de
taxa legal e **serve como oráculo**.

---

## 5. Pagamento parcial — `R10`

**No cível, a imputação é pelo art. 354 do CC: juros primeiro.** É regra **com norma**, e por
isso **não** entra como preset sem default — diferentemente do trabalhista, onde a prática é o
rateio **proporcional**, aplicado **101 vezes** no segmento que o usa e **fundamentado zero**
(`art. 354` tem **zero ocorrências nas 471 páginas** do manual trabalhista).

> **Não são duas normas concorrentes: são uma norma contra um costume de liquidação sem base
> declarada.** **Direção do delta:** juros primeiro produz saldo **maior** — o art. 354 **favorece
> o credor**; o critério proporcional **favorece o devedor**. **Amplitude medida: até 23,83% do
> saldo.**

---

## 6. Erros observados em implementação

Registrados em `pendencias.md` § 4 a partir de código de produção do SaaS — **quatro invariantes
violadas no mesmo trecho de cálculo de taxa legal**:

| # | Invariante | Defeito |
|---|---|---|
| (a) | **R11** | `Math.Max(0m, selic - ipca)` — **subtração literal de percentuais** |
| (b) | **R11** | usa o **IPCA do mês corrente**; a norma exige o **IPCA-15 do mês `m−1`** |
| (c) | **R4** | a base dos juros inclui os juros acumulados — **capitaliza** |
| (d) | **R12** | `Math.Round(x, 2)` **sem `MidpointRounding`** — o default do .NET é *banker's rounding*; a norma exige **truncamento** |

Também ausente: a distinção **IPCA-E / IPCA** (a enum tem ambos, mas a cadeia não bifurca por
fase) e o marco inicial dos juros trabalhistas usando `DataCitacao` — **R7 exige ajuizamento**.

---

## 7. Limitações e ponteiros

- **A tabela da corregedoria para o período até dez/2002 é REGIONAL.** O corpus cataloga **uma
  só** — a da CGJ/TJMG. **Nenhum TJ estadual além do TJMG aparece no consolidado** (busca
  declarada em `08-nacional-e-regional.md` § 3). Para outro estado, a linha "até dez/2002" fica
  **sem tabela cadastrada**, e resolve por **R24** (`sem cobertura regional`), com o Tema 1368
  como fallback vinculante;
- **`pr.adc58-item-i` não se aplica aqui** — é preset da jurisdição trabalhista.

| Assunto | Onde |
|---|---|
| Tabela CGJ/TJMG e as três hipóteses de sobrevida | `references/civel-regional-tjmg.md` |
| Espinha | `docs/calculo/consolidado/02-atualizacao.md` § 4 |
| Taxa legal, metodologia completa | `docs/calculo/00-base-normativa.md` § 4 |
| Par de validação IPCA-15 ausente | `docs/calculo/pendencias.md` § 2 |
| Truncamento × arredondamento | `docs/calculo/pendencias.md` §§ 3 e 9-A |
