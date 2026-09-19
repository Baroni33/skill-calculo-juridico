# Bloco 8 — relatório

Manual de Orientação de Procedimentos para os Cálculos na Justiça Federal, CJF,
**Resolução n. 990/2026**. 93 páginas, **integral**. 177.361 caracteres.

**Paginação.** Página 1 do PDF em branco; página 2 com o rótulo impresso "1". Logo
`pagina_pdf = numero_impresso + 1`, confirmado nas duas bordas.

Nenhuma skill escrita.

| Entrega | Situação |
|---|---|
| `bloco-08-jf.md` — espinha (C) | **Feita** — 25 regras numeradas |
| `bloco-08-jf-detalhe.md` — detalhe | **Feito** — cadeias linha a linha, 12 atritos nota×linha, **33 defeitos** |
| **(A) Cadeias** em `tabelas-normativas/` | **Feitas** — 7 cadeias, 78 segmentos |
| (B) Séries `OUT_OF_SCOPE` | **Nenhuma** — e a razão é achado. Ver § 6 |
| Cruzamento com as 4 fixtures | **Feito** — as quatro conferem em valor, com uma ressalva. Ver § 7 |
| Item 2.8 — quadro anexo | **Confirmado ausente**, e há mais. Ver § 2 |
| Cruzamento 4.7 × TRT-3 | **Feito** — e rendeu quatro divergências. Ver § 3 |
| Verificação de notas × linhas | **Feita** — 12 atritos, 3 contradições diretas |
| Cobertura dos capítulos 1 a 5 | **Integral** — inclusive o cap. 3 e os itens 2.5–2.9 e 4.5.4–4.6.6, que a primeira redação omitiu |
| `valida_cobertura` sobre as cadeias | **Rodado** — R2: 0, R1: 15. Ver § 5 |

**Fase 4: não se aplica.** É a única fonte do corpus cuja edição está vigente.

---

## 1. O que esta edição mudou, e por quê

A apresentação (`pagina_pdf: 11–12`) declara as quatro alterações desta versão. A primeira
governa o bloco inteiro:

> "1) **Encerramento da incidência da taxa SELIC** (prevista no art. 3º da Emenda Constitucional
> n. 113/2021) **quanto à fase pré-requisitório, a partir de setembro de 2025**, em razão da
> **Emenda Constitucional n. 136/2025** e conforme decidido pelo Supremo Tribunal Federal no ARE
> 1.557.312/SP (Tema 1.419), com a consequente aplicação dos critérios do Código Civil [...]:
> correção monetária pelo IPCA/IBGE e juros de mora pela taxa legal — SELIC com dedução do IPCA"

**O corte de set./2025 que aparece em todas as cadeias é a EC 136/2025.** Nenhuma tabela do corpo
a nomeia — todas citam o ARE 1.557.312/SP e a Lei 14.905/2024. A emenda está a um grau de
distância em cada linha.

E o alcance é **a fase pré-requisitório**, não a requisição: por isso o capítulo 5 não muda, e o
único bullet de emendas do item 5.1 continua sendo "Emendas Constitucionais n. 113/2021 e
114/2021" (`pagina_pdf: 88` — o item arrola sete fundamentos).

> **Correção da primeira redação.** Eu havia escrito que "o manual não menciona a EC 136/2025",
> com base numa varredura própria. **Estava errado**: `136/2025` ocorre três vezes. Busquei por
> `EC 136`, forma que o manual não usa. O erro foi meu, e o achado correto é melhor: a emenda não
> está nos capítulos, mas **é a razão declarada da edição**.

---

## 2. O item 2.8 — confirmado, e pior do que o enunciado supunha

O enunciado mandou confirmar que o item 2.8 remete a um quadro de multas administrativas anexo
que não existe. **Confirmado**, `pagina_pdf: 38`, literal:

> "As multas administrativas são impostas pela autoridade administrativa em virtude de infração à
> legislação pertinente, **cujo quadro está anexado a este manual**."

Varredura das 93 páginas: `anex*` ocorre **duas vezes** em todo o PDF — a frase acima e uma
referência a "tabelas anexas **às resoluções**" do CJF (`pagina_pdf: 46`), que são anexos de outro
documento. O sumário não traz entrada de anexo; os marcadores do PDF não trazem; não há arquivo
embutido; a última página é a 93, com o item 5.3.1.

**E há mais, que o enunciado não previa:** os subitens **2.8.1 (Ibama), 2.8.2 (Sudepe), 2.8.3
(IBDF) e 2.8.4 (Bacen) são títulos vazios** (`pagina_pdf: 39`). Numerados, sumariados, sem uma
linha de conteúdo. Só o 2.8.5 tem texto, e é uma remissão de uma frase.

Quatro órgãos nomeados, nenhum critério para nenhum deles, e o quadro que os teria não existe.
**Pendência P8-01**, e é a mais concreta do bloco.

---

## 3. O cruzamento com o TRT-3 — item 4.7

O enunciado: *"Cruze com o que foi extraído do TRT-3 e registre as diferenças de critério."*

### 3.1 O escopo é estreitíssimo, e é a primeira diferença

NOTA de abertura, `pagina_pdf: 77`, literal:

> "Este capítulo aplica-se **apenas a ações trabalhistas relativas a contratos regidos pela
> Consolidação das Leis do Trabalho (CLT) anteriores à promulgação da vigente Constituição
> Federal**, nos termos do art. 27, § 10, do ADCT/1988, **não se aplicando a ações relativas a
> servidores(as) públicos(as) sob regime estatutário**."

Contratos **anteriores a 05/10/1988**. É o resíduo de competência que o ADCT deixou na Justiça
Federal. O manual do TRT-3 cobre a competência trabalhista inteira; este item cobre um bolsão
histórico. **Os dois quase não se sobrepõem** — e essa é a diferença que explica as demais.

### 3.2 As quatro divergências de critério

| # | Ponto | CJF (4.7) | TRT-3 (cap. 9 / blocos 3–4) |
|---|---|---|---|
| **X-1** | **Desconto previdenciário** | "deve-se proceder à dedução do **percentual** da contribuição previdenciária devida pelo reclamante, **com base no valor da condenação**" (`pagina_pdf: 77`) | apuração **mês a mês** sobre o salário-de-contribuição somado às parcelas do cálculo, com teto e alíquota por faixa da época (cap. 9, item 9.2.7.1) |
| **X-2** | **Capitalização dos juros** | mar./1987 a mar./1991: **"1,0% – composta"** (`pagina_pdf: 78`) | R4 do projeto: juros de mora sempre simples |
| **X-3** | **Tabela de correção** | "deve-se utilizar a **tabela de coeficientes trabalhistas expedida pelo Tribunal Superior do Trabalho**" (`pagina_pdf: 77`) | "tabela única para atualização de débitos trabalhistas, divulgada pelo **CSJT**" (cap. 9, `pagina_pdf: 129`) |
| **X-4** | **Termo inicial dos juros** | "a partir da **notificação inicial** (Súmula n. 224 do STF)" (`pagina_pdf: 78`) | R7 do projeto: trabalhista = **ajuizamento** |

**X-1 é a divergência material.** A dedução "por percentual sobre o valor da condenação" é um
método inteiramente diferente do da contadoria trabalhista, que reconstrói o salário-de-contribuição
mês a mês, aplica o teto e abate o já recolhido. Os dois produzem números diferentes sobre o mesmo
crédito. **Não harmonizado** — é achado.

**X-2 é a mais grave para o motor.** É a **única linha de juros de mora com capitalização composta
em todo o manual do CJF**, e contraria a invariante R4. Transcrita como está, com alerta no JSON
da cadeia (`ALERTA_R4`).

**X-3 e X-4 podem ser diferenças de nomenclatura e de doutrina, não de resultado.** CSJT e TST
divulgam a mesma tabela por vias diferentes; notificação inicial e ajuizamento costumam coincidir
em dias. Registrados sem afirmar equivalência.

### 3.3 O que os dois manuais dizem igual

A ADC 58 entra nos dois, com a mesma modulação: "apenas aos processos **não transitados em
julgado** e, aos transitados, **quando omissa a decisão exequenda**" (`pagina_pdf: 80`). E o bloco
6 já havia catalogado a ADC 58 como marca de Fase 4 do lado trabalhista (F7-04, F4-01). **Aqui ela
não é marca: é direito vigente aplicado.**

---

## 4. O cruzamento interno — capítulo 2 contra capítulo 4

Não foi pedido, e é o achado mais consequente do bloco.

**As duas partes do mesmo manual tratam o mesmo período de formas incompatíveis.**

| | Cap. 2 — dívida fiscal | Cap. 4 — liquidação |
|---|---|---|
| jan./1989 | **BTN integral** | **IPC/IBGE de 42,72%** (expurgo, em substituição ao BTN) |
| fev./1989 | **BTN integral** | **IPC/IBGE de 10,14%** (expurgo) |
| mar./1990 a fev./1991 | BTN até jan./1991 | **IPC/IBGE** (expurgo) |
| Multiplicador de jan./1989 | **6,92 (IR)** e **6,17 (II)** | **6,17**, sem variante |

E o capítulo 2 **justifica expressamente** a sua escolha, item 2.3.1.3, `pagina_pdf: 25`:

> "por serem indexadores nominais, este fato **não implica duplicidade de correção monetária**"

**Nenhum dos dois capítulos remete ao outro.** Não há nota de compatibilização, não há ressalva.
A leitura mais provável é que sejam universos distintos — o crédito **do** Fisco contra o
contribuinte (cap. 2) e o crédito **contra** a Fazenda (cap. 4), com jurisprudências de expurgo
que só se firmaram no segundo. **Mas isso não está escrito**, e não foi inferido.

**Consequência prática do multiplicador:** o item 2.8.5 manda adotar "os mesmos critérios de
correção monetária indicados no item 2.3.1.2 **para o Imposto de Renda**" — o que arrasta o fator
**6,92**, e não o 6,17 de todo o capítulo 4. Quem aplicar o 6,17 às multas administrativas erra
12% no multiplicador de transição. **Pendência P8-02.**

---

## 5. R1 e R2 — o bloco que mais os exercita

`scripts/calculo/valida_cadeias_cjf.py`, sobre as sete cadeias:

```
7 cadeias | R1: 15 violações | R2: 0 violações
```

### 5.1 Por que foi preciso um runner próprio

`valida_cobertura.py` trata cada `condicao` como **universo separado** — e está certo, porque
tabelas que bifurcam por devedor, data da sentença ou fato gerador não devem ser comparadas entre
si. Mas as cadeias do CJF são **incondicionais até nov./2021 e só então bifurcam**. Rodado direto,
o tronco aparecia como lacuna em cada ramo.

O runner faz duas coisas antes de validar:

1. **replica o tronco em cada ramo** — o ramo herda o tronco, que é o que a leitura do manual
   manda;
2. **cobra R2 apenas do componente próprio** da cadeia — uma tabela de correção não deve ser
   cobrada de cobrir juros ao longo de toda a linha do tempo, e a Selic, que declara
   `engloba: [correcao-monetaria, juros-mora]`, criava um universo de juros dentro de uma tabela
   de correção.

E distingue **bifurcação** de **lacuna**: quando o tronco encerra e os ramos condicionados cobrem
o período, não é buraco.

**Isto é achado de modelagem, não defeito do manual.** O schema do projeto não tinha, até aqui,
como expressar "tronco comum + ramos condicionados". **Pendência P8-M1.**

### 5.2 Zero lacunas

As sete cadeias cobrem de 1964 à data-base sem buraco. O manual é disciplinado nisso, e o diz:
"O mês da mudança do indexador deve ser considerado, **sob pena de solução de continuidade**"
(`pagina_pdf: 25`).

### 5.3 Quinze sobreposições, em três meses

As quinze somam **por universo de condição**, não por cadeia: o runner valida cada ramo
condicionado em separado, e a cadeia de condenatórias, com três universos, contribui com seis.
Distribuição real: **jan./1989 = 8 · mar./1990 = 6 · jan./1996 = 1**.

| Mês | Cadeias | Conflito | O manual explica? |
|---|---|---|---|
| **jan./1989** | 4 do cap. 4 + dívida fiscal | OTN ("a jan./1989") × IPC ou BTN ("Jan./1989") | **Sim** — argumento dos índices nominais, item 2.3.1.3 |
| **mar./1990** | 4 do cap. 4 | BTN ("a mar./1990") × IPC ("De mar./1990") | **Não** |
| **jan./1996** | repetição de indébito | Ufir ("a jan./1996") × Selic ("A partir de jan./1996") | **Não** |

**A explicação de jan./1989 não alcança mar./1990.** O IPC/IBGE é índice **percentual**, e o
próprio item 4.1.2.4 diz que percentuais "refletem a inflação do próprio mês de competência". BTN
de mar./1990 e IPC de mar./1990 não medem meses diferentes — medem o mesmo. **Pendência P8-03.**

**Nem jan./1996.** Ufir é nominal, Selic não é índice de inflação, e não há nota. **Pendência
P8-04.**

### 5.4 Duas sobreposições que a checagem não pega

Porque estão em tabelas diferentes, fora do alcance de uma cadeia:

- **maio/2000** no FGTS fiscal: "De fev./1991 a maio/2000" × "A partir de maio/2000"
  (`pagina_pdf: 35`);
- **dez./2021** nos compensatórios da desapropriação **indireta**: fecha em "dez./2021" enquanto a
  gêmea **direta** fecha em "nov./2021", com fundamento legal idêntico (`pagina_pdf: 74–75` × `68`).

---

## 6. A bifurcação (A)/(B)/(C) — e o manual que não tem séries

**Nenhuma série foi extraída deste manual.** Não por corte: **ele não traz nenhuma**.

Todas as tabelas de valores são remissões a normas externas — Tabela I e III da Lei 9.289/1996,
resoluções do STF e do STJ, tarifas dos Correios, tabelas mensais da Caixa, séries do IBGE e do
Bacen. Onze chaves registradas em `bloco-08-jf-detalhe.md` § 8, nenhuma com valor.

A única tabela numérica reproduzida é o quadro da taxa legal previdenciária de set./2025 a
jun./2026 (`pagina_pdf: 61`) — e é **ilustração de metodologia**, não a série: a fonte declarada é
"Bacen (SGS — Sistema Gerenciador de Séries Temporais)".

**É o inverso do manual do TRT-3**, que traz 10.503 linhas de série no capítulo 18. O CJF é um
manual de **regra**; o TRT-3 é regra **mais** tabela.

---

## 7. As quatro fixtures — todas conferem

O enunciado: *"As quatro fixtures de tests/fixtures/calculo/ vieram deste manual. Confirme que os
valores extraídos reproduzem as fixtures. Divergência é achado."*

| Fixture | Item | `pagina_pdf` | Valor esperado | Confere |
|---|---|---|---|---|
| `fixture-01-fazenda-publica-jun2022` | 4.2.1.1, NOTA 6, ex. 1 | 51 detalhado, 52 resumido | **R$ 3.484,95** | ✓ os dois métodos |
| `fixture-02-fazenda-publica-jun2026` | 4.2.1.1, NOTA 6, ex. 1, 2º | 52 detalhado, 53 resumido | **R$ 5.218,27**\* / **R$ 5.218,28** | ✓ com a ressalva\* |
| `fixture-03-nao-fazenda-publica-jun2026` | 4.2.1.1, NOTA 6, ex. 2 | 53 | **R$ 5.772,95** | ✓ |
| `fixture-04-precatorio-complementar` | 5.2.1.1 e 5.2.1.2 | 91 resumido, 92 detalhado | **R$ 4.435,07** / **R$ 4.435,04** | ✓ com a diferença de R$ 0,03 |

**Nenhuma divergência de valor.** E as fixtures já gravavam `pagina_pdf` com o offset 1 correto.

\* **Ressalva na fixture 02, apontada pela validação adversarial.** O valor `5.218,27` **não está
impresso em página nenhuma do PDF**. A planilha do método detalhado (`pagina_pdf: 52`) imprime o
total **truncado: "R$ 5.218,2"** — e a camada de texto confirma que não é corte de margem. O
`5.218,27` é **derivado** da soma das colunas (3.412,64 + 1.805,63), não transcrito. O caveat já
existia na própria fixture e em `pendencias.md` § 6; faltava aqui, no artefato que declara a
conferência. Registrado como defeito do original **D8-D32**.

**As duas diferenças de centavos são asserção, não erro** — e o manual as declara nos dois casos:

> "Eventuais diferenças de centavos — como a de R$ 0,01 verificada neste exemplo — **não decorrem
> de erro**, mas são inerentes ao critério de **truncamento** de casas decimais aplicado em cada
> etapa do cálculo, sendo, portanto, desprezíveis." (`pagina_pdf: 53`)
>
> "Os métodos devem levar à obtenção de valores iguais, podendo ocorrer pequenas variações, como
> no caso anteriormente descrito (**de R$ 0,03 de diferença**), o que não é proveniente de erro,
> mas de **arredondamento** de casas decimais no decorrer do cálculo" (`pagina_pdf: 92`)

**Achado de terminologia:** o manual diz **"truncamento"** no capítulo 4 e **"arredondamento"** no
capítulo 5, para o mesmo fenômeno. São operações aritméticas distintas e produzem resultados
distintos. A invariante **R12** do projeto exige "critério de truncamento definido e consistente
por etapa" — e a fonte usa os dois termos. **Pendência P8-05.**

---

## 8. A verificação de notas contra linhas

O enunciado: *"No bloco 7 apareceu contradição entre linha e nota na mesma tabela — procure o
padrão aqui."*

**O padrão se repete. Doze atritos, três contradições diretas.** Tabela completa em
`bloco-08-jf-detalhe.md` § 4. As que mudam resultado:

1. **N-1** — a tabela de correção da dívida fiscal encerra a janela sem correção em **dez./1991**;
   a tabela de juros que ela própria manda consultar estende a TRD até **2/1/1992**. Dois dias em
   que a correção já começou (Ufir) e a nota diz que não há correção.
2. **N-3** — o item 2.3.1.1 rotula a Lei n. 4.357/1964 como "(OTN)" e a Lei n. 6.899/1981 como
   "(ORTN)"; a tabela do mesmo item usa **ORTN** para 1964 e **OTN** para 1986. **Rótulos
   invertidos**, e o item 4.4.1 repete a inversão.
3. **N-6** — a tabela de juros compensatórios encerra o regime autônomo em **nov./2021**; o texto
   logo abaixo diz "Até dez. 2021". **Um mês sem regime coerente.**

E uma nota que **altera a linha sem dizer como**: **N-5**, os expurgos do FGTS. A NOTA 2 manda
incluir "42,72% em jan./1989 e 44,80% em abr./1990" sobre linhas que já trazem indexador (LFT–0,5%
e BTN). **Substitui ou acresce?** No capítulo 4 a operação é declarada — "descontando o BTN [...]
evitando bis in idem" (`pagina_pdf: 42`). No FGTS, não. **Pendência P8-06, a mais cara do bloco.**

---

## 9. Pendências

| # | Pendência | Efeito |
|---|---|---|
| **P8-01** | **Itens 2.8.1 a 2.8.4 vazios** e quadro anexo inexistente | Quatro órgãos nomeados (Ibama, Sudepe, IBDF, Bacen) sem critério algum |
| **P8-02** | **Multiplicador 6,92 × 6,17** — o cap. 2 tem dois, o cap. 4 só um; o 2.8.5 remete ao do IR | Erro de 12% no multiplicador de transição de jan./1989 para multas administrativas |
| **P8-03** | **Sobreposição em mar./1990** — BTN × IPC, ambos no mesmo mês, sem a justificativa dos nominais | Risco de dupla contagem num mês |
| **P8-04** | **Sobreposição em jan./1996** — Ufir × Selic na repetição de indébito, sem nota | Idem |
| **P8-05** | **"Truncamento" (cap. 4) × "arredondamento" (cap. 5)** para o mesmo fenômeno | R12 exige critério consistente; a fonte usa dois termos |
| **P8-06** | **Expurgos do FGTS substituem ou acrescem?** | Não declarado. Muda o valor em dois meses de toda ação de FGTS |
| **P8-07** | **"De 1964" sem mês** no início de quatro cadeias | Materializado como 1964-01 na janela de análise, com marca |
| **P8-08** | **maio/2000 em dois intervalos** no FGTS fiscal; e fronteiras incompatíveis entre 2.4.4.1 e 2.4.4.2 | Sem regra de desempate |
| **P8-09** | **dez./2021 nos compensatórios** — direta fecha em nov./2021, indireta em dez./2021, fundamento idêntico | Um mês de diferença entre tabelas gêmeas |
| **P8-10** | **FGTS × poupança divergem de mar. a jun./1987** — OTN × LBC, sem fundamento por linha | Não explicado |
| **P8-11** | **"cor/mon." nunca definida**, usada nove vezes | Abreviação crítica sem glossário |
| **P8-12** | **Gatilho "Selic ao ano superior a 8,5%"** — meta ou efetiva? com que periodicidade se reavalia? | Não definido, e governa a fórmula da poupança em três cadeias |
| **P8-13** | **Capítulo 2 × capítulo 4 sobre expurgos** — incompatíveis, sem remissão recíproca | Ver § 4 |
| **P8-14** | **4.5.6 — três termos iniciais alternativos** para a correção dos honorários periciais não depositados, sem critério de escolha | `pagina_pdf: 71` |
| **P8-15** | **4.5.4 — corte em ago./2017** nos juros compensatórios, que passam a seguir o percentual dos TDAs de oferta inicial | Regra vive só no item; nenhuma tabela a mostra |
| **P8-M1** | **Modelagem:** o schema não expressa "tronco comum + ramos condicionados" | Exigiu um runner próprio. Ver § 5.1 |
| **P8-M2** | **Modelagem:** a suspensão da correção na falência (item 2.9) é um segmento que **existe ou não conforme evento futuro** — liquidado o débito no ano, suspende; não liquidado, a suspensão desaparece retroativamente | `cadeia-temporal` não expressa. `pagina_pdf: 39` |

---

## 10. O que este bloco entrega, e o que não

**Entrega:** sete cadeias no schema executável, com `aplicacao`, `engloba`, `condicao`,
multiplicadores de transição e expurgos com percentual cravado; a consolidação de dez./2021 com
os três valores de fechamento por ramo; as quatro fórmulas de defasagem; o item que sustenta R3;
os cruzamentos pedidos; e a checagem de R1/R2 com resultado interpretado.

**Não entrega, por decisão:**

- **harmonização** entre o capítulo 2 e o capítulo 4 sobre expurgos e multiplicadores;
- **correção** dos 31 defeitos do original nem das 15 sobreposições;
- **resolução** de "substitui ou acresce" nos expurgos do FGTS;
- **séries** — o manual não tem nenhuma;
- as cadeias de **4.6 (desapropriação indireta), 4.8 (FGTS) e 4.9 (poupança)**, que foram lidas,
  conferidas quanto a contiguidade e descritas no detalhe, mas **não foram codificadas em JSON**.
  4.6 é idêntica a 4.5 na correção; 4.8 tem **11** segmentos e 4.9 tem **12**, e mereceriam bloco
  próprio, junto com as dez cadeias de juros que faltam (4.3.2, 4.4.2, 4.5.2, 4.5.3, 4.6.2, 4.6.3,
  4.8.2, 4.8.3, 4.9.2, 4.9.3). **Declarado, não escondido.**

---

## 11. O que a validação adversarial verificou, e o que derrubou

Feita por script sobre o PDF: **211 candidatas a citação literal** — 145 dos três `.md` e 66 dos
sete JSON — normalizadas e confrontadas por match exato, cross-página e `difflib`. Mais a
conferência **linha a linha dos 78 segmentos** contra as tabelas do PDF, e o inventário de 180
itens numerados contra o que os documentos citam.

### O erro que importava

**Um segmento de cadeia com o índice errado.** `cjf.desapropriacao-direta.correcao-monetaria`,
mar. a dez./1991: eu havia gravado **INPC**; o PDF diz **IPC/FGV** (`pagina_pdf: 66`, e a gêmea
4.6.1.1 na `73`). Outro índice, de outra instituição, e o **único exclusivo de uma cadeia em todo
o capítulo 4**. Era o único errado dos 78 — e teria produzido dez meses de correção errada em
produção. Corrigido, com o registro no próprio JSON.

### O resto

| # | O que caiu | Correção |
|---|---|---|
| 1 | **Consolidação de dez./2021 em "quatro lugares", "três ramos"** | São **cinco**. As duas desapropriações também consolidam, com IPCA-E de 1,17%. `0,4412` ocorre nas páginas 50, 59, **67**, **74** e 79 |
| 2 | **Capítulo 3 sem cobertura** | Coberto — e é regra de precedência de fonte: nas dívidas diversas o título extrajudicial **é** o critério |
| 3 | **Itens 2.5, 2.6, 2.7 e 2.9 sem cobertura** | Cobertos. O **2.9 (Falência)** é regra temporal pura e rendeu a pendência de modelagem P8-M2 |
| 4 | **Itens 4.5.4, 4.5.6–4.5.9, 4.6.4–4.6.6 sem cobertura** | Cobertos. Renderam P8-14 e P8-15, e o achado de que **o ônus da perícia inverte** entre desapropriação direta e indireta |
| 5 | **"Poupança tem treze segmentos, a mais longa do manual"** | Tem **doze**, e a mais longa é a do previdenciário (15) |
| 6 | **"cor/mon. aparece nove vezes, p. 25/32/33"** | **Treze vezes**, p. 26/32/33/91/92 — e não na 25 |
| 7 | **"FGTS × poupança divergem em quatro meses"** | Divergem também de **maio/1967 a jun./1983** — dezesseis anos, UPC × ORTN |
| 8 | **Onze atribuições de página erradas** nos `.md` e nos JSON | A NOTA 5 da consolidação está na p.**50**, não na 49; a NOTA 7 da taxa legal na **56**, não na 55; a tabela 2.3.2.2 na **26–27**, não na 25–26; o escopo de 4.7 na **77** |
| 9 | **Uma paráfrase em campo literal** — "e assim para os demais meses", em `observacao` de um segmento | Não é texto do manual. Marcada como paráfrase |
| 10 | **A lista dos 31 defeitos omitia dois** | São **33**: o total truncado `R$ 5.218,2` (p.52) e `"art. 3ª da EC n. 113/2021"` (p.63) |
| 11 | **"As quatro fixtures conferem, nenhuma divergência"** | Confere em valor, mas o `5.218,27` é **derivado**, não transcrito — ver § 7 |

### O que resistiu

- **77 dos 78 segmentos**, conferidos linha a linha contra as tabelas do PDF.
- **O tronco comum 1964→fev./1991**, palavra por palavra idêntico nas quatro cadeias de correção
  (`pagina_pdf: 48, 57, 63, 66`), inclusive multiplicadores e expurgos.
- **Os 31 defeitos originalmente catalogados** — todos procedem, todos na página certa, incluindo
  os mais improváveis.
- **R1 = 15, R2 = 0, em exatamente três meses** (jan./1989, mar./1990, jan./1996). Reproduzido.
- **As seis afirmações negativas**, inclusive as arriscadas: `anex*` exatamente duas vezes,
  `136/2025` exatamente três, 2.8.1–2.8.4 vazios, e a capitalização composta única — que ganhou
  contraponto: na `pagina_pdf: 71` o manual **veda** juros compostos.
- **Os 12 atritos nota×linha**, os 4 percentuais de URV, as fixtures 01, 03 e 04, os números
  estruturais (93 páginas, 177.361 caracteres, 78 segmentos) e o offset de paginação.
- **A autocorreção da EC 136/2025** — o número novo está certo.

