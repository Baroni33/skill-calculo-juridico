# Previdenciário — benefícios, cadeia do CJF

Correção monetária e juros das condenações relativas a **benefícios previdenciários** na Justiça
Federal. Item **4.3** do Manual CJF, Res. 990/2026.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 5; `02-atualizacao-detalhe.md` §§ 5.1,
5.2 e 10; `00-base-normativa.md` §§ 4 e 6; `docs/calculo/pendencias.md` § 2;
`docs/calculo/tabelas-normativas/cjf.previdenciario.correcao-monetaria.json`.

> **Não confundir com a contribuição previdenciária em dívida fiscal.** Aquela é outra cadeia,
> com outros cortes — `references/tributario-federal.md` § 3.3.

---

## 1. A cadeia de correção — **a mais longa do manual**, 15 segmentos

**Nunca bifurca por devedor** (`R-08-08`).

| Período | Indexador |
|---|---|
| 1964-01 .. 1986-02 | **ORTN** — `ponta_materializada`: o manual escreve *"De 1964"*, sem mês (`P8-07`) |
| 1986-03 .. 1989-01 | **OTN** |
| **1989-01** | **IPC/IBGE** — *"Expurgo, em substituição ao BTN"* |
| **1989-02** | **IPC/IBGE** — idem |
| 1989-03 .. 1990-03 | **BTN** |
| 1990-03 .. 1991-02 | **IPC/IBGE** — *"Expurgo, em substituição ao BTN e ao INPC de fev./1991"* |
| 1991-03 .. 1992-12 | **INPC/IBGE** |
| 1993-01 .. 1994-02 | **IRSM** |
| **1994-03 .. 1994-06** | **conversão em URV** |
| 1994-07 .. 1995-06 | **IPC-R** |
| 1995-07 .. 1996-04 | **INPC/IBGE** |
| 1996-05 .. 2006-08 | **IGP-DI** |
| 2006-09 .. **2021-11** | **INPC/IBGE** |
| **2021-12 .. 2025-08** | **SELIC** — **engloba correção E juros** (R1) |
| **a partir de 2025-09** | **INPC/IBGE** |

Os seis primeiros segmentos são o **tronco comum** de 1964 a fev/1991, idêntico palavra por
palavra em quatro cadeias — ver `tributario-federal.md` § 1. **O expurgo SUBSTITUI, não soma.**

**Ressalva de extração declarada:** o segmento `1994-03 .. 1994-06` está gravado como
**PARÁFRASE, não citação** — o manual enumera os quatro percentuais um a um (`pagina_pdf` 58), e
os valores literais ficaram em campo próprio do JSON.

**`R3` morde aqui mais do que em qualquer outra cadeia:** ORTN, OTN, BTN são **nominais**
(refletem a inflação do mês **anterior**); INPC, IRSM, IPC-R, IGP-DI são **percentuais**
(refletem a do **próprio** mês). **São oito viradas entre tipos.** Trocar sem ajustar a defasagem
**desloca o cálculo em um mês** a cada uma.

---

## 2. Os juros

| Período | Juros |
|---|---|
| até nov/2021 | pela cadeia de juros aplicável (item 4.3.2) |
| **dez/2021 .. ago/2025** | **SELIC** — engloba, não há componente separado |
| **a partir de set/2025** | **taxa legal com dedução do INPC** |

**`aplicacao`:** a **taxa legal segue D1** — no mês **posterior** ao de sua competência,
**inclusive no mês de pagamento** (item 4.2.2, NOTA 7, `pagina_pdf` 56).

---

## 3. A taxa legal **previdenciária** — mesma fórmula, deflator diferente

```
TL_m = (Fator_Selic_m / Fator_INPC_{m-1} − 1) × 100
```

**O deflator é o INPC, não o IPCA-15.** Fonte: **Manual CJF, Res. 990/2026, item 4.3.2, Nota 3**.
Tudo o mais é idêntico à regra geral: **seis decimais**, **truncamento**, **juros simples**
(R4), **piso zero** (R6, CC art. 406, § 3º), e **razão entre fatores, nunca subtração** (R11).

| Variante | Deflator | Fundamento | Par de validação publicado |
|---|---|---|---|
| **Regra geral** | IPCA-15 | Res. CMN 5.171/2024 | **nenhum** — pendência |
| **Previdenciária** | **INPC** | Manual CJF 990/2026, item 4.3.2, Nota 3 | **dois** |

### 3.1 Os dois pares de validação SÃO deste caso

**Este é o ponto que o `README.md` de `references/` já sinalizava, e ele é verdadeiro.** Os dois
pares publicados na § 4 da base normativa vêm da tabela de **taxa legal previdenciária** do
Manual CJF, cuja coluna é **`Fator INPC`**:

| Competência | Fator Selic | **Fator INPC** | Manual | **Razão** | Subtração |
|---|---|---|---|---|---|
| **Set/2025** | 1,01164156 | 0,9979 | 1,377047% | **1,377047%** ✓ | 1,374156% ✗ |
| **Mai/2026** | 1,01090058 | 1,0081 | 0,277807% | **0,277807%** ✓ | 0,280058% ✗ |

Registrados como `PARES_VALIDACAO_INPC`. **Divergência da subtração: ~0,003 p.p./mês, e acumula.**

**Truncamento confirmado pelos mesmos pares:**

| Competência | Razão exata | **Truncado** | Half-up | Manual |
|---|---|---|---|---|
| Set/2025 | 1,3770478004 | **1,377047** ✓ | 1,377048 ✗ | 1,377047 |
| Mai/2026 | 0,2778077572 | **0,277807** ✓ | 0,277808 ✗ | 0,277807 |

**Half-up erra o último dígito nos dois casos.** Implementado como `ROUND_DOWN`, com teste
negativo que falha se alguém trocar por half-up.

### 3.2 A consequência, declarada

> **A variante IPCA-15 — que é a regra geral e a de maior uso — está implementada mas SEM
> verificação contra valor publicado.** A aritmética é compartilhada e está coberta pelos pares
> INPC; o que falta é a confirmação de que a **série correta** alimenta `fator_deflator` na regra
> geral. **Pendência aberta** — `pendencias.md` § 2.
>
> **Como fechar:** o Banco Central divulga mensalmente a taxa legal, o Fator Selic e o Fator
> IPCA; a **Calculadora do Cidadão** do BCB serve como oráculo. Extrair dois meses e acrescentar
> `PARES_VALIDACAO_IPCA15`.

**A única tabela numérica que o Manual CJF reproduz é justamente esta** — o quadro da taxa legal
previdenciária de **set./2025 a jun./2026** (`pagina_pdf` 61), nove linhas, com fator Selic, fator
INPC e taxa resultante, fonte *"Bacen (SGS)"*. **Não foi extraída como série**, porque é
**ilustração de metodologia**, não a série em si — a série vive no Bacen.

---

## 4. Consolidação de dez/2021

| Ramo | Índice de nov/2021 | Valor | Juros de dez/2021 | Item · `pagina_pdf` |
|---|---|---|---|---|
| **Benefícios previdenciários** | **INPC** | **0,84%** | **0,4412%** | 4.3.1, NOTA 5 · **59** |

**É um dos cinco lugares, e o único com INPC** — os demais usam IPCA-E (1,17%) ou TR (0,00%). Os
**juros de dez/2021 são os mesmos (0,4412%) nos cinco**.

Literal da NOTA: *"Quanto às prestações devidas até dez./2021: a) o crédito será consolidado tendo
por base o mês de dez./2021 [...] considerando, para esse fim, o **INPC** [...]"*.

**`R-08-14` — "sem exclusão de qualquer parcela":** a SELIC de jan/2022 em diante incide sobre o
consolidado **inteiro, principal E juros**.

---

## 5. Duas notas do próprio manual que o motor precisa honrar

**(a) Termo inicial da correção é a COMPETÊNCIA, não o pagamento.** Literal: *"O termo inicial da
correção monetária deve ser o mês de competência, e não o mês de pagamento."*

**(b) Benefício ASSISTENCIAL não segue esta cadeia.** Literal: *"Nas condenações relativas a
benefícios de natureza assistencial, aplica-se a correção monetária das ações condenatórias em
geral (item 4.2.1.1 deste manual)."* — e **aquela cadeia BIFURCA por devedor em dez/2021**,
enquanto esta **nunca bifurca**. `tributario-federal.md` § 5.1.

> **É bifurcação por NATUREZA DO BENEFÍCIO, eixo não temporal.** Previdenciário × assistencial
> decide qual cadeia inteira se usa, não qual segmento.

---

## 6. Limitações declaradas

1. **Sem preset nomeado.** O catálogo de `01-plano-extracao.md` não tem ID para esta cadeia —
   há `TRIB-FED-REPETICAO` e `TRIB-FED-DIVIDA-ATIVA`, e nada para o previdenciário. **Entra como
   cadeia, não como preset.** Registrado, não inventado;
2. **O par de validação IPCA-15 continua ausente** — e é a regra geral, não esta variante (§ 3.2);
3. **As séries não estão aqui** — IRSM, IPC-R, IGP-DI, INPC, cotações da URV são dado **(B)**,
   contrato em `skills/indices-judiciais/`. O regime `pr.planos-economicos` está **bloqueado** por
   falta de série (IPC, URP, IRSM, FAS, FAZ, IPC-r, FRS — pendência P19);
4. **O critério de arredondamento da conversão URV não é declarado pelo manual.** O método está
   fechado — `valor_em_CR$ = valor_em_URV × URV(dia_do_pagamento)`, item 6.1 do manual trabalhista
   —, mas **o arredondamento, não** (`pendencias.md` § 9). **Não inferido**;
5. **EC 136/2025:** o previdenciário **mantém INPC e taxa legal com dedução do INPC** na fase
   pré-requisitório (Res. CJF 990/2026). Na fase de **requisitório**, valem as três restrições da
   EC 136 — **e a Fazenda estadual e municipal fica no vácuo normativo**
   (`tributario-federal.md` § 6);
6. **`ponta_materializada` no início** — o manual abre com *"De 1964"*, **sem mês**. `1964-01` é
   materialização de janela, **não afirmação do manual** (`P8-07`).

---

## 7. Ponteiros

- `docs/calculo/tabelas-normativas/cjf.previdenciario.correcao-monetaria.json` — os 15 segmentos
- `docs/calculo/consolidado/02-atualizacao-detalhe.md` §§ 5.1, 5.2 e 10
- `docs/calculo/00-base-normativa.md` § 4 — taxa legal, metodologia completa
- `docs/calculo/pendencias.md` § 2 — o par de validação IPCA-15 ausente
- `references/tributario-federal.md` §§ 1, 5.1 e 8 — tronco comum, condenatórias gerais
  (para o benefício **assistencial**) e a consolidação nos cinco lugares
- `references/civel-cc-nacional.md` § 4 — a taxa legal na regra geral, com deflator IPCA-15
