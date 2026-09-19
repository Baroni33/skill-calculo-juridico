# Mapa de cobertura da extração

Artefato de fechamento da Fase 2. Lista **todo capítulo e item dos dois manuais**, com o
bloco que o cobriu ou a razão de não ter sido coberto.

Produzido no bloco 10. Fronteiras de capítulo obtidas por varredura do PDF, não do sumário
impresso — o sumário deste manual já se mostrou incompleto mais de uma vez.

---

## 1. Manual de Cálculos do TRT-3 (julho/2016) — 471 páginas

**Offset de paginação: zero.** Número impresso = página do PDF.

| Cap. | Título | Páginas | Nº | Bloco | Estado |
|---|---|---|---|---|---|
| 1 | Introdução | 9 | 1 | 2 | coberto |
| 2 | Bibliografia utilizada na atividade de cálculo | 10 | 1 | 2 | coberto |
| 3 | Competências relativas às atividades de cálculo | 11–12 | 2 | 2 | coberto |
| 4 | Liquidação de sentenças | 13 | 1 | 2 | coberto |
| 5 | Cálculos de liquidação — como se estrutura | 14–17 | 4 | 2 | coberto |
| 6 | Verbas trabalhistas | 18–82 | 65 | 3 e 4 | coberto |
| 7 | Atualização monetária e juros de mora | 83–99 | 17 | 9 e 10 | coberto |
| **8** | **Encargos e despesas processuais** | **100–106** | **7** | **—** | **NÃO COBERTO** |
| 9 | Descontos legais: previdenciário e fiscal | 107–208 | 102 | 7 | coberto |
| **10** | **Atualização de débitos trabalhistas** | **209–277** | **69** | **—** | **NÃO COBERTO** |
| 11 | Exemplo de cálculos, acordos e atualizações | 278–298 | 21 | 10 | coberto |
| **12** | **Contribuição sindical** | **299–302** | **4** | **—** | **NÃO COBERTO** |
| 13 | Atualização de créditos da dívida ativa da União | 303 | 1 | 10 | coberto |
| **14** | **Precatórios** | **304–306** | **3** | **—** | **NÃO COBERTO** |
| 15 | Comandos facilitadores do cálculo de liquidação | 307–309 | 3 | 10 | coberto |
| **16** | **Promoções** | **310–336** | **27** | **—** | fora de escopo — ver § 3 |
| 17 | Súmulas, OJs e TJPs — TST e TRT-3 | 337–372 | 36 | 10 | coberto |
| 18 | Tabelas | 373–471 | 99 | 1 | coberto |

**Conferido em script**, não estimado:

| | Páginas |
|---|---|
| Cobertas | **353** |
| Lacuna real (caps. 8, 10, 12, 14) | **83** |
| Fora de escopo (cap. 16) | 27 |
| Soma dos capítulos | 463 |
| Pré-textuais (capa e sumário, pp. 1–8) | 8 |
| **Total do PDF** | **471** |

**Cobertura: 74,9% do PDF, 76,2% das páginas de capítulo.**

### 1.1 Detalhamento do capítulo 6 (blocos 3 e 4)

| Itens | Bloco |
|---|---|
| 6.1 a 6.6 (com 6.6.1 a 6.6.8) | 3 |
| 6.7 a 6.15 (com 6.10.1, 6.11.1–4, 6.13.1–11) | 4 |

**Correção de numeração.** O enunciado do bloco 10 pedia "13 — Diferenças salariais". Não
existe: **Diferenças salariais é o item 6.15**, coberto pelo bloco 4. O capítulo 13 é
*Atualização de créditos da dívida ativa da União*. Igualmente, "o que houver entre 6.15 e o
capítulo 16" não é o capítulo 15: entre eles estão os capítulos 7 a 14 inteiros.

### 1.2 Detalhamento do capítulo 7 (blocos 9 e 10)

| Itens | Bloco |
|---|---|
| 7.1 a 7.6 e 7.7 (moedas e paridades) | 9 |
| 7.6.1 residual — juros vincendos, pp. 95–98 | 10 |

---

## 2. Os quatro capítulos não cobertos

**A busca que sustenta esta afirmação**, conforme a regra de afirmação negativa: varredura
por `grep -rn` em `docs/calculo/extracao/` pelos termos `capítulo 8`, `capítulo 10`,
`capítulo 12`, `capítulo 14`, `capítulo 16` e pelas faixas de página `100`–`106` e
`209`–`277`. Nenhuma ocorrência que indique extração. As únicas menções às faixas são
`p.208` e `p.223`, ambas em contexto de fronteira do bloco 7, não de conteúdo.

### 2.1 Capítulo 10 — a lacuna que mais pesa

**69 páginas, 38 subitens.** Título: *Atualização de débitos trabalhistas*.

| Item | Assunto |
|---|---|
| 10.1 | Atualização simples — **sem** amortização de valor pago |
| 10.2 | Descontos previdenciários e fiscais **proporcionais** |
| 10.2.1 | Critérios do art. **12-A** da Lei 7713/88 e arts. 36 a 42 e 45 da IN RFB |
| 10.2.2 | Critérios do art. **12-B** da Lei 7713/88 e arts. 26, 44 e 45 da IN RFB |
| 10.3 | Atualização **com amortização de valor pago** |
| 10.3.1 | Sem a inclusão dos descontos previdenciários e fiscais |

Isto é **núcleo de motor de cálculo**, não acessório:

- **amortização de valor pago** — a ordem em que um pagamento parcial se imputa entre
  principal, correção e juros determina o saldo. É a operação mais sensível a ordem de
  cálculo de todo o manual, e não está extraída;
- **descontos proporcionais** — o capítulo 9 (bloco 7) extraiu os critérios de IR e INSS,
  mas a **proporcionalização** na atualização está aqui. O art. 12-A já apareceu no bloco 7:
  há sobreposição a conferir, e possivelmente divergência de critério entre os dois
  capítulos do mesmo manual.

**Recomendação: bloco próprio.** Não cabe em fechamento — é maior que o capítulo 7 e o 11
somados, e tem a mesma natureza mista de conceito e exemplo que tornou o capítulo 9 o maior
bloco do projeto.

### 2.2 Capítulo 8 — encargos e despesas processuais

**7 páginas.** Itens: 8.1 Custas processuais · 8.2 Custas de execução · 8.2.1 Apuração do
valor das custas de execução · 8.3 Honorários periciais · 8.4 Honorários advocatícios
assistenciais e sucumbenciais.

**Assimetria a registrar:** o bloco 8 extraiu integralmente o capítulo 1 do manual federal,
que é *Custas processuais*. O lado trabalhista do mesmo assunto ficou de fora. Qualquer
comparação entre as duas jurisdições sobre custas está hoje pela metade.

O manual cita a IN nº 20/2002 do TST e a Lei 10.537/02 — fundamentos que não estão no corpus.

### 2.3 Capítulo 12 — contribuição sindical

**4 páginas.** Itens: 12.1 Esclarecimentos gerais · 12.2 Forma de cálculo · 12.3 Contribuição
sindical rural · 12.4 Forma de atualização.

É **verba com forma de cálculo e forma de atualização próprias**. Cabe na espinha. Fica a
ressalva de direito intertemporal: o manual é de 2016 e a Reforma de 2017 tornou a
contribuição facultativa — o que o corpus precisa marcar, e a base normativa deve responder.

### 2.4 Capítulo 14 — precatórios

**3 páginas.** Itens: 14.1 Esclarecimentos gerais · 14.2 Diretrizes para elaboração e
atualização de cálculos em precatórios.

**Cruza diretamente com o capítulo 5 do manual federal** (requisições, precatório e RPV,
inclusive EC 136/2025), extraído no bloco 8. O confronto entre os dois regimes é material —
e hoje só um lado existe.

---

## 3. Capítulo 16 — por que fica fora

**27 páginas, 82 subitens.** *Promoções* aqui não são promoções funcionais: são **minutas de
petição e despacho** — "pedindo elementos", "reiterando pedido", "manifestando sobre
impugnações das partes", "pedindo retorno dos autos ao perito".

É **texto processual, não regra de cálculo.** Não produz número, não altera base, não define
critério. Fica fora do escopo da espinha por natureza, não por falta de tempo.

**E, no entanto, contém regra de cálculo.** Isto não é hipótese: foi verificado por leitura
das pp. 310–336 no fechamento deste bloco. Três casos, literais:

**16.4.11 — Dedução na data do depósito ou levantamento** (`pagina_pdf` 335). Subitem
16.4.11.1, *"Dedução na data do levantamento e não na data do depósito"*:

> "a dedução do valor recebido pelo reclamante foi efetuada na data do efetivo levantamento,
> na forma do disposto na Súmula nº 15 do TRT/3ª Região, considerando que o depósito de fl.
> 130 foi feito à disposição do juízo e precedeu aos embargos e agravo de petição,
> tratando-se, portanto, de depósito em garantia da execução."

É **regra de imputação com fundamento e condição de incidência**: depósito em garantia da
execução deduz-se na data do **levantamento**, não na do depósito. Muda o saldo. E é
exatamente a operação do **capítulo 10** (amortização de valor pago), que também não está
extraído.

**16.4.7 — Limitação da multa a 100%** (`pagina_pdf` 330), com fundamento duplo:

> "a multa diária (...) foi limitada ao valor da obrigação principal (...) tendo em vista o
> disposto no art. 412 do CC (art.920, CC/1916) e OJ/SDI/TST nº 54 da SDI ("Multa estipulada
> em cláusula penal, ainda que diária, não poderá se superior ao principal corrigido -
> Aplicação do art. 920 do C[C]")"

Note: **"superior ao principal CORRIGIDO"** — o teto é medido sobre o principal já corrigido,
não sobre o nominal. É decisão de ordem de operações.

**16.4.6.2 — FGTS** (`pagina_pdf` 327): atualizado "na forma do art. 39 da Lei 8177/91, tendo
em vista o disposto na OJ nº 302/TST" — amarra o FGTS à mesma cadeia dos débitos
trabalhistas, e a OJ 302 é justamente um dos verbetes que o capítulo 17 lista.

**Classificação: `fora-de-escopo-com-ressalva-confirmada`.** A natureza do capítulo é
processual, mas ele **enuncia regra que o capítulo técnico não enuncia** — o mesmo padrão que
o capítulo 9 exibiu e que o capítulo 11 foi varrido para encontrar. Varredura dirigida aos
itens 16.4.3–16.4.7 e 16.4.9–16.4.12, **não** extração integral. Pendência **P10-C16**,
elevada a prioridade média por causa de 16.4.11.

---

## 4. Manual de Cálculos da Justiça Federal (CJF, Res. 990/2026) — 93 páginas

**Offset de paginação: 1.** `pagina_pdf = impresso + 1`.

| Cap. | Título | Bloco | Estado |
|---|---|---|---|
| 1 | Custas processuais | 8 | coberto |
| 2 | Dívida fiscal (2.1 a 2.9) | 8 | coberto |
| 3 | Dívidas diversas | 8 | coberto |
| 4 | Liquidação de sentença (4.1 a 4.9) | 8 | coberto — ver § 4.1 |
| 5 | Requisições de pagamento (precatório, RPV, EC 136/2025) | 8 | coberto |

**Integralmente extraído.** É a única fonte do corpus cuja edição está vigente.

### 4.1 Cadeias do capítulo 4 lidas mas não codificadas

Declaradas no bloco 8, repetidas aqui porque são lacuna de **artefato**, não de leitura:

- correção: 4.6 (desapropriação indireta), 4.8 (FGTS, 11 segmentos), 4.9 (poupança, 12);
- juros: 4.3.2, 4.4.2, 4.5.2, 4.5.3, 4.6.2, 4.6.3, 4.8.2, 4.8.3, 4.9.2, 4.9.3 — **dez cadeias**.

Sete cadeias estão em `docs/calculo/tabelas-normativas/cjf.*.json`; estas treze, não.

---

## 5. Camadas construídas sobre os manuais

| Camada | Bloco | Artefato |
|---|---|---|
| Parâmetros negociáveis e norma coletiva (R14–R18) | 5 | `valida_parametros.py` |
| Presets de regime temporal (R19–R22) | 6 | `valida_regimes.py`, `regimes-temporais-catalogo.json` |
| Cobertura temporal (R1, R2) | 8 e 9 | `valida_cobertura.py`, `valida_cadeias.py` |
| Cadeias históricas trabalhistas | 9 | `trt3.hist.*.json` |
| Índice de jurisprudência | 10 | `jurisprudencia-indice.md` |

---

## 6. O que a Fase 3 recebe

### 6.1 Lacunas de extração, por prioridade

| # | O que falta | Tamanho | Por que pesa |
|---|---|---|---|
| **L1** | **Capítulo 10 do TRT-3** — atualização, amortização de valor pago, descontos proporcionais | 69 pp | Núcleo do motor. Ordem de imputação de pagamento parcial. Bloco próprio |
| **L2** | **Capítulo 8 do TRT-3** — custas, honorários periciais e advocatícios | 7 pp | O lado federal já está extraído; a comparação está pela metade |
| **L3** | **Dez cadeias de juros e três de correção** do cap. 4 do CJF | — | Lidas e conferidas, não codificadas |
| **L4** | **Capítulo 14 do TRT-3** — precatórios | 3 pp | Cruza com o cap. 5 do CJF, já extraído |
| **L5** | **Capítulo 12 do TRT-3** — contribuição sindical | 4 pp | Verba com cálculo e atualização próprios |
| **L6** | **Varredura dirigida do cap. 16** (16.4.3–16.4.7, 16.4.9–16.4.12) | ~10 pp | **Confirmado que enuncia regra de cálculo**: 16.4.11 (dedução na data do levantamento, Súmula 15/TRT-3), 16.4.7 (multa ≤ principal **corrigido**, art. 412 CC + OJ 54), 16.4.6.2 (FGTS pela Lei 8177/91, OJ 302). Ver § 3 |

### 6.2 Lacunas de fundamento — não se fecham por extração

Estas **não estão em manual nenhum** e exigem a base normativa:

- **P9-02** — índice de correção trabalhista **anterior a março de 1991**. O capítulo 7
  delega à Tabela Única do CSJT, que é série, não regra. A cadeia trabalhista histórica não
  é derivável do corpus atual;
- **P9-01** — juros da Fazenda **subsidiária**: o manual registra corrente jurisprudencial,
  não regra assentada;
- **P8-M1** e **P8-M2** — limites de modelagem do schema `cadeia-temporal`.

### 6.3 O que está sólido

- Os dois manuais têm **paginação, fronteiras de capítulo e offsets conferidos por script**.
- **Onze cadeias temporais** validadas por R1/R2, com toda violação lida e classificada
  entre defeito do original e artefato de granularidade.
- **204 testes** cobrindo as invariantes R1–R22.
- A disciplina de **não harmonizar** foi mantida: divergência entre manuais, entre linha e
  nota, e entre correntes jurisprudenciais está registrada como divergência, com os dois
  fundamentos, em todos os blocos.
