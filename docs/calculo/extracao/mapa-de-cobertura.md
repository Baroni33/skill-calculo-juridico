# Mapa de cobertura da extração

Artefato de fechamento da Fase 2. Lista **todo capítulo e item dos dois manuais**, com o
bloco que o cobriu ou a razão de não ter sido coberto.

Produzido no bloco 10, **fechado no bloco 13**. Fronteiras de capítulo obtidas por varredura
do PDF, não do sumário impresso — o sumário deste manual já se mostrou incompleto mais de uma
vez.

> **ESTADO FINAL — os dois PDFs fecham em 100%.**
>
> | Manual | Páginas | Cobertas | Pré-textuais com decisão | Sem decisão |
> |---|---|---|---|---|
> | TRT-3 (2016) | 471 | **463** | 8 | **0** |
> | CJF (Res. 990/2026) | 93 | **83** | 10 | **0** |
> | **total** | **564** | **546** | **18** | **0** |
>
> **Nenhuma página sem destino registrado.** Conferido por script.

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
| 8 | Encargos e despesas processuais | 100–106 | 7 | **13B** | **coberto** |
| 9 | Descontos legais: previdenciário e fiscal | 107–208 | 102 | 7 | coberto |
| 10 | Atualização de débitos trabalhistas | 209–277 | 69 | **11A, 11B, 11C, 13A** | **coberto** — ver § 2.1 |
| 11 | Exemplo de cálculos, acordos e atualizações | 278–298 | 21 | 10 | coberto |
| 12 | Contribuição sindical | 299–302 | 4 | **13C** | **coberto** — estrutura, marcado superado |
| 13 | Atualização de créditos da dívida ativa da União | 303 | 1 | 10 | coberto |
| 14 | Precatórios | 304–306 | 3 | **13C** | **coberto** — estrutura, marcado superado |
| 15 | Comandos facilitadores do cálculo de liquidação | 307–309 | 3 | 10 | coberto |
| 16 | Promoções | 310–336 | 27 | **13E** | **coberto** por varredura dirigida — **FONTE NORMATIVA**. Ver § 3 |
| 17 | Súmulas, OJs e TJPs — TST e TRT-3 | 337–372 | 36 | 10 | coberto |
| 18 | Tabelas | 373–471 | 99 | 1 | coberto |

**Conferido em script**, não estimado. **Fechado no bloco 13.**

Página não coberta exige decisão registrada, e o mapa separa os dois casos:

| | Páginas |
|---|---|
| **Cobertas** | **463** |
| Não cobertas **sem decisão** | **0** |
| Pré-textuais (pp. 1–8) — **decisão registrada** | 8 |
| **Total do PDF** | **471** |

**Todas as 463 páginas de capítulo estão cobertas.** As 8 pré-textuais — capa, folha de rosto
e sumário — não têm conteúdo normativo; **decisão registrada, não omissão**.

**Cobertura: 100% das páginas de capítulo; 100% do PDF com destino registrado.**

### Não coberto — nenhuma página

O bloco 13 cobriu as 54 que faltavam: segmento B do cap. 10 (13 pp.), cap. 8 (7), cap. 12
(4), cap. 14 (3) e cap. 16 (27).

**Ressalva de natureza, registrada:** o capítulo 16 foi coberto por **varredura dirigida**, não
por extração integral. As 27 páginas foram lidas e cruzadas; o que não é regra de cálculo —
endereçamento, fecho, pedido de prazo — **foi deliberadamente não extraído**. Isso é decisão,
não lacuna: ver § 3.

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

## 2. Os capítulos fora dos blocos concluídos, e seu destino

**A busca que sustentou a afirmação original** (bloco 10), conforme a regra de afirmação
negativa: varredura por `grep -rn` em `docs/calculo/extracao/` pelos termos `capítulo 8`,
`capítulo 10`, `capítulo 12`, `capítulo 14`, `capítulo 16` e pelas faixas de página
`100`–`106` e `209`–`277`. Nenhuma ocorrência que indicasse extração.

**Atualização do bloco 12:** o capítulo 10 tem **56 das 69 páginas cobertas** (segmentos A, C
e D) — **a amortização está fechada**. Resta o segmento B, 13 pp., para o 11D. E **nenhum
capítulo segue sem decisão**: 8, 12, 14 e 16 foram destinados ao **bloco 13**.

### 2.1 Capítulo 10 — em extração, dividido por operação

**69 páginas, 56 cobertas.** O bloco 11A fez a varredura estrutural e extraiu o segmento A;
o 11B extraiu o **C**, onde vive a regra de imputação; o 11C extraiu o **D**, que fecha a
amortização. Resta o segmento **B**.

A numeração impressa **para em 10.3.2.1, na p. 239** — e o capítulo segue por mais 38 páginas
estruturadas apenas por `Exemplo 1` a `Exemplo 6`. Dividir pela numeração perderia 55% do
capítulo. A divisão real, medida por script:

| Seg. | Item | Operação | pp. | Caracteres | Bloco |
|---|---|---|---|---|---|
| **A** | 10.1 | Atualização **sem** amortização | 209–223 (parcial) | 41.471 | **11A — feito** |
| **B** | 10.2 | Descontos proporcionais | 223–236 | 41.228 | 11D |
| **C** | 10.3 | Amortização — **RRA, art. 12-A** | 237 (off. 681)–266 (off. 2141) | 89.290 | **11B — feito** |
| **D** | 10.3 | Amortização — vincendos e **art. 12-B** (Ex. 5–6) | 266 (off. 2141)–277 | 33.694 | **11C — feito** |

**Nenhuma das fronteiras internas do capítulo 10 é quebra de página** — todas caem no meio de
uma folha, e foram localizadas por offset. O capítulo termina na p. 277; o cap. 11 abre na 278.

**A numeração impressa não volta depois de `10.3.2.1` (p. 239).** Varredura de
`^1[01]\.\d[\.\d]*` nas pp. 240–300: uma única ocorrência, e é uma remissão a "10.2" no meio
do texto da p. 249, não um título. Os Exemplos 1 a 6 ficam todos pendurados no mesmo subitem.

**A fronteira A/B não é quebra de página:** o título `10.2` está no offset 2.658 da p. 223.

**A ordem dos blocos seguiu o valor, não o documento.** O 11B foi ao segmento C porque é onde
vive a regra de imputação e a resposta para R10. O 11C foi ao **D**, e não ao B, porque o 11B
mostrou que a hipótese que a moldura declara obrigatória — o critério alternativo da letra C,
sob juros vincendos — não tinha exemplo no segmento C: a amortização estava incompleta sem os
Exemplos 5 e 6.

Estrutura original, para referência:

| Item | Assunto |
|---|---|
| 10.1 | Atualização simples — **sem** amortização de valor pago |
| 10.2 | Descontos previdenciários e fiscais **proporcionais** |
| 10.2.1 | Critérios do art. **12-A** da Lei 7713/88 e arts. 36 a 42 e 45 da IN RFB |
| 10.2.2 | Critérios do art. **12-B** da Lei 7713/88 e arts. 26, 44 e 45 da IN RFB |
| 10.3 | Atualização **com amortização de valor pago** |
| 10.3.1 | Sem a inclusão dos descontos previdenciários e fiscais |

Isto é **núcleo de motor de cálculo**, não acessório:

- **amortização de valor pago** — extraída no bloco 11B. A regra é **proporcional** (letra F
  de 10.3.1), e a escolha da ordem move o saldo em até **23,83%**. Sem fundamento normativo
  declarado em nenhuma das 471 páginas;
- **descontos proporcionais** — o capítulo 9 (bloco 7) extraiu os critérios de IR e INSS,
  mas a **proporcionalização** na atualização está aqui. O art. 12-A já apareceu no bloco 7:
  há sobreposição a conferir, e possivelmente divergência de critério entre os dois
  capítulos do mesmo manual.

**Recomendação cumprida:** o capítulo ganhou bloco próprio, e a série 11A–11D o cobre por
operação. O bloco 11A confirmou a natureza mista de conceito e exemplo — em 41.471 caracteres
de 10.1 há **doze regras estruturais que só existem dentro de exemplo numérico**.

### 2.2 Capítulo 8 — encargos e despesas processuais

**7 páginas.** Itens: 8.1 Custas processuais · 8.2 Custas de execução · 8.2.1 Apuração do
valor das custas de execução · 8.3 Honorários periciais · 8.4 Honorários advocatícios
assistenciais e sucumbenciais.

**Assimetria a registrar:** o bloco 8 extraiu integralmente o capítulo 1 do manual federal,
que é *Custas processuais*. O lado trabalhista do mesmo assunto ficou de fora. Qualquer
comparação entre as duas jurisdições sobre custas está hoje pela metade.

O manual cita a IN nº 20/2002 do TST e a Lei 10.537/02 — fundamentos que não estão no corpus.

**Decisão do bloco 12: bloco 13.** Extração normal, sem ressalva de vigência. É o capítulo que
fecha a assimetria com o cap. 1 do Manual CJF.

**E já há um atrito conhecido esperando:** o bloco 10 mediu que a **base das custas de
execução do cap. 11 diverge da do cap. 9** (151,39 contra 151,56 no mesmo exemplo), e que na
mesma base o crédito entra líquido e os honorários entram brutos. O cap. 8 é onde a regra
deveria estar enunciada. Pendência **P10-18**.

### 2.3 Capítulo 12 — contribuição sindical

**4 páginas.** Itens: 12.1 Esclarecimentos gerais · 12.2 Forma de cálculo · 12.3 Contribuição
sindical rural · 12.4 Forma de atualização.

É **verba com forma de cálculo e forma de atualização próprias**. Cabe na espinha.

**Decisão do bloco 12: bloco 13, como ESTRUTURA, marcado SUPERADO pela Reforma.** O manual é
de 2016 e a Lei 13.467/2017 tornou a contribuição **facultativa**. Extrai-se a mecânica de
cálculo e atualização — que continua valendo para competências anteriores e para os casos em
que há autorização — com `status_norma: superado` no que pressupõe obrigatoriedade.

### 2.4 Capítulo 14 — precatórios

**3 páginas.** Itens: 14.1 Esclarecimentos gerais · 14.2 Diretrizes para elaboração e
atualização de cálculos em precatórios.

**Cruza diretamente com o capítulo 5 do manual federal** (requisições, precatório e RPV,
inclusive EC 136/2025), extraído no bloco 8. O confronto entre os dois regimes é material —
e hoje só um lado existe.

**Decisão do bloco 12: bloco 13, como ESTRUTURA, marcado SUPERADO pela EC 113/2021 e pela
EC 136/2025.** Extrai-se a estrutura e as diretrizes de elaboração; o regime de atualização
que o capítulo pressupõe está superado. O valor do bloco 13 aqui é **o confronto com o cap. 5
do CJF**, não a regra em si.

---

## 3. Capítulo 16 — reclassificado para FONTE NORMATIVA

**27 páginas, 82 subitens.** *Promoções* aqui não são promoções funcionais: são **minutas de
petição e despacho**.

O bloco 10 o classificou como `fora-de-escopo-com-ressalva-confirmada`. **O bloco 12 promove a
classificação para FONTE NORMATIVA**, porque três achados confirmados mostram que o capítulo
**enuncia regra que o capítulo técnico não enuncia** — e num caso é o **único lugar do manual**
onde a regra é fundamentada.

### 3.1 Os três achados que forçaram a reclassificação

**16.4.11 — imputação na data do levantamento** (`pagina_pdf` **333–334**):

> "a dedução do valor recebido pelo reclamante foi efetuada na data do efetivo levantamento,
> na forma do disposto na **Súmula nº 15 do TRT/3ª Região**, considerando que o depósito de
> fl. 130 foi feito à disposição do juízo e precedeu aos embargos e agravo de petição,
> tratando-se, portanto, de **depósito em garantia da execução**."

Regra de imputação **com fundamento e condição de incidência**. E o capítulo 10, que executa a
dedução em 56 páginas, **nunca cita a Súmula 15** — `Súmula` tem zero ocorrências no segmento
que a aplica.

**16.4.7 — multa limitada ao principal CORRIGIDO** (`pagina_pdf` 330), com fundamento duplo:
art. 412 do CC (art. 920 do CC/1916) e OJ 54 da SDI.

> **CORRIGIDO NO BLOCO 13 — este achado caiu.** Não é caso de "fundamenta só na minuta": o
> capítulo técnico **enuncia a mesma regra, e melhor**. Item **6.13.10 "Multa diária",
> `pagina_pdf` 77**, com o texto **íntegro** da OJ 54 e o art. 412 dentro das aspas — o que a
> p. 330 traz **truncado e com erro** (*"não poderá **se** superior"*). A p. 77 ainda
> acrescenta duas regras que a minuta não tem: a correção começa **um dia após** o teto ser
> atingido, e *"A incidência de juros sobre a multa é controversa."*
>
> **Eu gravei esta afirmação no bloco 12 sem cruzá-la contra o capítulo 6.** A varredura
> dirigida do bloco 13 a derrubou.

**p. 328 — o fundamento do "descarregar"**:

> "recalculando os juros de mora desde a inicial, **não incidindo juros sobre juros
> (anatocismo)**"

**É o único lugar do manual que conecta a operação de descarregar ao anatocismo.** O capítulo
10 executa a operação e a nomeia apenas "descarregar" — `descarreg` tem **uma única ocorrência
em todo o manual**, na p. 237 —, e `anatocismo` tem **zero ocorrências** nas 69 páginas do
capítulo 10. Ver `00-base-normativa.md` § 7, **R23**.

> **Precisão acrescentada no bloco 13.** `anatocismo` **não é exclusivo do capítulo 16**:
> ocorre nas pp. **16, 90, 328 e 335**. A p. 16 o usa para a acumulação da Selic (com a
> Súmula 121 do STF) e a p. 90 para a Fazenda Pública. **O que é exclusivo do capítulo 16 é a
> aplicação do conceito à operação de amortização** — e a p. 328 abre com a **mesma frase** do
> item 10.3.1, qualificando juridicamente o que lá é apenas nomeado.

### 3.1.1 E o bloco 13 achou mais quatro, todas confirmadas

A varredura dirigida cruzou **36 fundamentos** do capítulo 16 contra os capítulos técnicos.
**Quatro aparecem só no capítulo 16**, em todas as 471 páginas:

| Fundamento | Onde | Ocorrências no manual |
|---|---|---|
| **IN SRF 15/2001** — fonte do *gross-up* bruto↔líquido | 16.4.4.10, p. 326 | **1**, e é essa |
| **Súmula 454/TST** — SAT na desoneração | 16.4.3.19, pp. 320–322 | **3**, todas no cap. 16 |
| **Súmula 388/TST** + **art. 83 da Lei 11.101/05** — massa falida | 16.4.9.2, p. 332 | **2** e **1**, todas na p. 332 |
| **Prov. 03/91** e **art. 104, § 5º, do PGC TRT-3** | 16.3.5, 16.4.2, 16.4.8.3, 16.4.12.1 | **0 em qualquer capítulo técnico** |

A IN SRF 15/2001 é a mais gritante: é **a fonte declarada da fórmula de gross-up**, e a
expressão "bruto em relação ao líquido" ocorre em 16 páginas — **15 delas no capítulo 10**,
que nunca diz de onde a fórmula vem.

**A reclassificação para fonte normativa sai reforçada:** eram três achados, um dos quais caiu;
são **seis** confirmados.

### 3.2 O que isso significa para o bloco 13

**Varredura dirigida, não extração integral.** O alvo são os itens **16.4.3 a 16.4.7** e
**16.4.9 a 16.4.12**, que nomeiam assuntos de cálculo: INSS, IRRF, juros de mora, critérios de
atualização, limitação da multa, massa falida, certidão de dívida ativa, dedução na data do
depósito ou levantamento, Fazenda Pública.

**O padrão é estável e já se repetiu três vezes:** o manual **pratica** no capítulo técnico e
**fundamenta** na minuta. Quem extrair só os capítulos técnicos fica com as operações sem as
razões.

Pendência **P10-C16**, elevada a prioridade alta.

---

## 4. Manual de Cálculos da Justiça Federal (CJF, Res. 990/2026) — 93 páginas

**Offset de paginação: 1.** `pagina_pdf = impresso + 1`.

**Fronteiras conferidas por varredura no bloco 13** — não estavam mapeadas página a página.

| Faixa | Conteúdo | Nº | Bloco | Estado |
|---|---|---|---|---|
| 1–10 | brancas (1 e 3), composição do Conselho, elaboração e revisão, **sumário** (5–10) | 10 | — | **pré-textual — decisão registrada** |
| 11–12 | **Apresentação** — declara os critérios da Lei 14.905/2024 | 2 | 8 | **coberto** |
| 13 | **Resolução CJF n. 990, de 3 de julho de 2026** | 1 | 8 | **coberto** |
| 14–21 | Capítulo 1 — Custas processuais | 8 | 8 | coberto |
| 22–39 | Capítulo 2 — Dívida fiscal (2.1 a 2.9) | 18 | 8 | coberto |
| 40 | Capítulo 3 — Dívidas diversas | 1 | 8 | coberto |
| 41–87 | Capítulo 4 — Liquidação de sentença (4.1 a 4.9) | 47 | 8 | coberto — ver § 4.1 |
| 88–93 | Capítulo 5 — Requisições de pagamento (EC 136/2025) | 6 | 8 | coberto |
| | **cobertas** | **83** | | |
| | **pré-textuais com decisão** | **10** | | |
| | **total** | **93** | | |

**100% com destino registrado.**

### 4.0 Uma imprecisão corrigida no bloco 13

Desde o bloco 8 este manual era descrito como **"93 páginas, integral"**. A descrição
superestimava: **os capítulos ocupam 80 páginas**; as outras 13 são pré-textuais, e **3 delas
têm conteúdo normativo** — a Apresentação, que declara os critérios da Lei 14.905/2024, e a
própria Resolução 990/2026.

**Essas três estão cobertas** — `bloco-08-jf.md` cita a Apresentação literalmente, e a
**Resolução CMN n. 5.171/2024**, que ela invoca, está na § 4 de `00-base-normativa.md`. A
imprecisão era de contagem, não de leitura.

É a única fonte do corpus cuja edição está vigente.

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
| Cadeias históricas trabalhistas | 9 | `trab.hist.*.json` |
| Índice de jurisprudência | 10 | `jurisprudencia-indice.md` |

---

## 6. O que a Fase 3 recebe

### 6.1 Lacunas de extração, por prioridade

| # | O que falta | Tamanho | Por que pesa |
|---|---|---|---|
| **L1** | **Capítulo 10, segmentos C, B e D** — amortização de valor pago e descontos proporcionais | 54 pp | Núcleo do motor. **Em curso: 11A feito, 11B vai ao segmento C** |
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
