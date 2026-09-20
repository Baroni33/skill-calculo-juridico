# Bloco 9 — cadeias históricas de atualização trabalhista

**Fonte:** `manual-de-calculo-trabalhista_2016-1.pdf`, capítulo 7, páginas 83 a 99 do PDF.
**Offset de paginação: zero.** O número impresso é igual à página do PDF.
**Extração dirigida**, não integral. Ver § 1.

---

## 1. Escopo, e por que ele é estreito

O capítulo 7 está **materialmente superado como norma**: ADC 58 (STF), EC 113/2021,
Lei 14.905/2024 e EC 136/2025 substituíram seus critérios de correção e de juros. O que
não caduca é o **encadeamento histórico** — competência de 1994 se corrige pelo índice
de 1994, qualquer que seja a regra de hoje.

Extraído: mapas período → indexador e período → taxa, com fundamento e vigência;
multiplicadores de transição e conversões de moeda; expurgos com percentual cravado;
regras de defasagem (campo `aplicacao`); tipo do indexador; marcos de padrão monetário.

Não extraído, ainda que o capítulo trate: critério de juros vigente; regime de
capitalização como regra atual; qualquer afirmação sobre o que se aplica hoje.

Todo segmento posterior a novembro de 2021 leva `status_norma: "superado"` e o item da
base normativa que o substitui.

---

## 2. O achado que governa o bloco

> **O capítulo 7 não tem mapa período → indexador de correção monetária.**

Não é omissão do extrator. É desenho do manual, e ele diz por quê, na `pagina_pdf 85`:

> "A tabela mensal de correção está escalonada em meses e anos, já computa as conversões
> e paridades da moeda nacional e não contém juros."

O TRT-3 delega **o encadeamento inteiro** à Tabela Única do CSJT. Consequência prática:
a cadeia trabalhista histórica **não é derivável deste manual**. Ela vive numa série —
categoria (B), dado externo — e não numa regra.

Varredura das dezessete páginas por `IPC`, `IGP`, `INPC`, `expurgo`, `ORTN`, `OTN`,
`BTN`, `Ufir`, `42,72`, `10,14`, `6,17`, `6,92`, `126,8621`: **nenhuma ocorrência.**
Os multiplicadores e expurgos que o enunciado mandou procurar **não estão no capítulo 7**.
"IPC" só aparece dentro de "IPCA-E".

**Ressalva importante, que a releitura adversarial impôs.** A afirmação acima vale para
**correção monetária**. O capítulo *tem* dois mapas período → **taxa**, ambos de juros da
Fazenda, ambos na `pagina_pdf 92` — e a primeira redação deste documento, por enunciar a
tese em termos absolutos, deixou de procurá-los. Ver § 4 e o relatório, § 6.

### 2.1 O marco da Tabela Única

| | |
|---|---|
| Vigência | a partir de **novembro/2005** |
| Fundamento | **Resolução nº 08/2005** do CSJT |
| `pagina_pdf` | 84 |

> "Até outubro de 2005, o TRT/3ª Região publicava a tabela de correção monetária mensal"

---

## 3. Cadeia de correção monetária

`trab.hist.correcao-monetaria` — 3 segmentos.

### 3.1 O índice antes de março de 1991 é `nao-declarado`

A TR foi criada pelo **art. 39 da Lei 8.177/91**, de março de 1991. O manual **não diz**
qual índice vale antes disso — delega à Tabela Única. O campo `indexador` do primeiro
segmento é portanto `NAO-DECLARADO-PELO-MANUAL`, não "TR".

Isto corrige a primeira versão, que gravava `TR` para `1942-11..2009-06` — afirmando um
índice para quarenta e nove anos em que ele não existia. É a mesma classe de erro que o
bloco 8 cometeu com o IPC/FGV, e foi a releitura que a pegou. Pendência **P9-02**.

### 3.2 Defasagem — o campo `aplicacao`

`aplicacao: "primeiro-dia-do-mes-subsequente-a-prestacao"`, por força da **Súmula 381 do
TST** (`pagina_pdf 84`).

A mecânica importa mais que a regra, e o manual a explicita na `pagina_pdf 85`:

> "Os índices de correção monetária estão posicionados no próprio mês da constituição do
> crédito"

Ou seja: a tabela já posiciona o índice no mês do crédito, de modo que **aplicar a Súmula
381 equivale a usar o índice do mês SEGUINTE**. Exemplo do próprio manual: horas extras
apuradas em junho/14 → índice de **julho/14** na tabela de maio/16.

Quem lê a súmula sem a tabela, ou a tabela sem a súmula, erra por um mês.

### 3.3 Tipo do indexador — inferência declarada, não extração

`tipo_indexador: "percentual"`, **com ressalva**. Pelo critério formal do item 4.1.2.4 do
manual federal (`pagina_pdf 42`), a TR não é unidade monetária como Ufir/OTN/BTN, logo é
percentual. Mas o critério material daquele item — "refletem a inflação do próprio mês" —
**não se aplica à TR**, que não é índice de preços, e sim taxa referencial apurada
prospectivamente (art. 12, I, da Lei 8.177/91).

**Nenhum dos dois manuais classifica a TR.** O rótulo é inferência por analogia e está
marcado como tal no JSON. O resultado operacional coincide com a mecânica do § 3.2.

### 3.4 O episódio IPCA-E

| Data | Ato |
|---|---|
| 04/08/15 | TST, ArgInc 479-60.2011.5.04.0231 — declara inconstitucional a TR |
| 14/10/15 | STF, Rcl 22012 MC/RS — liminar suspende |

> "permanece válida a TR"

Gravado com `status_norma: superado`. É história do regime, não regra.

---

## 4. Cadeias de juros

### 4.1 Geral — `trab.hist.juros-mora`

Quadro sinóptico da `pagina_pdf 89`, transcrito sem alteração:

| Período | Amparo legal | Critério |
|---|---|---|
| ajuizamento da ação até 26/02/87 | CC, 1062 e 1063 | 0,5% ao mês, simples |
| Entre 27/02/87 e 03/03/91 | DL 2322/87, art. 3º | **1,0% ao mês, c/ taxa capitalizada. Ex.: 3 meses = 3,03%** |
| Entre 04/03/91 até a satisfação | L. 8177/91, art. 39 | 1,0% ao mês, simples. Ex.: 3 meses = 3% |

**A linha do meio contraria a invariante R4** (juros de mora sempre simples). Não foi
harmonizada. Ver § 5.

### 4.2 Fazenda Pública — `trab.hist.fazenda-publica.juros-mora`

**Cinco** segmentos, do quadro da `pagina_pdf 92` — não três, como a primeira versão
trazia. Ver o relatório, § 6, sobre como o erro ocorreu.

| Período | Amparo legal | Critério |
|---|---|---|
| ajuizamento até 26/02/87 | CC, 1062 e 1063 | 0,5% ao mês, simples |
| Entre 27/02/87 e 03/03/91 | DL 2322/87, art. 3º | 1,0% ao mês, **capitalizada** |
| Entre 04/03/91 e 26/08/01 | L. 8177/91, art. 39 | 1,0% ao mês, simples |
| Entre 27/08/01 a 28/06/2009 | Lei 9494/97, art. 1º-F (MP 2180-35/2001) | 0,5% ao mês, **limitado a 6% ao ano** |
| Entre 29/06/2009 até o pagamento | Lei 9494/97, art. 1º-F (art. 5º da Lei 11960/09) | Juros da caderneta de poupança, sem cumulação |

O **limite de 6% ao ano** não é redundante com 0,5% ao mês: 0,5% simples por doze meses dá
exatamente 6%, mas o limite morde em qualquer contagem por dias que ultrapasse o ano.

**Subcorte em 04/05/2012** (MP 567/12 → Lei 12.703/12), `pagina_pdf 91`. Modelado como
qualificação do último segmento, não como segmento próprio: a **regra** (art. 1º-F,
poupança) não muda; muda a fórmula da poupança.

> "Até 03/05/2012, os juros aplicáveis à caderneta de poupança, correspondiam a 0,5% ao mês."

### 4.3 O único mapa período → taxa do capítulo

`pagina_pdf 92`, fundamento no art. 12, II, "b", da Lei 8177/91 (MP 567/12). Existe porque:

> "a meta anual da taxa Selic apenas ficou inferior ou igual a 8,5% no período de junho/12
> a agosto/13. De setembro/13 até o mês de atualização deste manual (maio/16), a meta anual
> da taxa Selic é superior a 8,5% e os juros correspondem a 0,5% ao mês."

| Mês | % a.m. | Mês | % a.m. | Mês | % a.m. |
|---|---|---|---|---|---|
| jun/12 | 0,4828% | out/12 | 0,4273% | fev/13 | 0,4134% |
| jul/12 | 0,4828% | nov/12 | 0,4134% | mar/13 | 0,4134% |
| ago/12 | 0,4551% | dez/12 | 0,4134% | abr/13 | 0,4134% |
| set/12 | 0,4273% | jan/13 | 0,4134% | mai/13 | 0,4273% |
| | | | | jun/13 | 0,4551% |
| | | | | jul/13 | 0,4551% |
| | | | | ago/13 | 0,4828% |

> "Total % de juros de jun/12 a ago/13 — 6,5760%"

**Conferido em `Decimal`:** a soma dos quinze percentuais dá exatamente `6,5760`. E o
atalho do manual fecha: `15 × 0,5% = 7,5%`; `7,5% − 6,5760% = 0,9240%`.

É série — categoria (B) —, não regra. Gravada dentro da cadeia por ser o único lugar do
capítulo onde o manual crava percentual mês a mês.

### 4.4 Fazenda subsidiária — ramo declarado e deliberadamente vazio

O quadro da `pagina_pdf 92` vale para a Fazenda **"como reclamada principal"**. A primeira
versão usava `condicao: {devedor: fazenda-publica}` sem qualificar — e um motor teria
aplicado 0,5% a.m. a Fazenda subsidiária, que o manual trata na `pagina_pdf 93`:

> "grande parte da jurisprudência entende que os juros de mora são de 1% ao mês de acordo
> com o art. 39 da Lei 8.177/91 (...) nos termos da OJ 382 da SDI-1/TST"

**"Grande parte da jurisprudência entende" é corrente, não regra assentada.** Pela
disciplina do projeto, divergência jurisprudencial não se resolve. O ramo
`fazenda-publica-subsidiaria` é declarado em `dominio_condicoes` e **não recebe segmento**.
O validador o reporta como lacuna — que é a leitura correta: o manual não fecha a questão.
Pendência **P9-01**.

---

## 5. A anomalia da capitalização composta

Três registros independentes dizem o mesmo sobre **27/02/87 a 03/03/91**:

| Fonte | `pagina_pdf` | Diz |
|---|---|---|
| TRT-3, quadro geral | 89 | 1,0% ao mês, capitalizada. Ex.: 3 meses = 3,03% |
| TRT-3, quadro da Fazenda | 92 | idem |
| CJF, cap. 4 | — | composta, mesmo período |

Não é erro de transcrição de nenhum dos dois manuais: **é o DL 2322/87**. A invariante R4
(juros de mora sempre simples) tem aqui uma exceção histórica de quatro anos, e o motor
precisa honrá-la. Registrada no campo `ALERTA_R4` dos segmentos, não harmonizada.

---

## 6. Moedas e paridades

`trab.hist.moedas-e-paridades` — 8 segmentos, `pagina_pdf 99`, conferidos caractere a
caractere.

| Período | Moeda | Símbolo | Proporção | Raciocínio |
|---|---|---|---|---|
| 01/11/42 a 12/02/70 | Cruzeiro | Cr$ | 1000/1 | 1.000 réis = 1 cruzeiro |
| 13/02/67 a 14/05/70 | Cruzeiro novo | NCr$ | 1000/1 | 1.000 cruzeiros = 1,00 cruzeiro novo |
| 15/05/70 a 27/02/86 | Cruzeiro | Cr$ | 1/1 | 1,00 cruzeiro novo = 1,00 cruzeiro |
| 28/02/86 a 15/01/89 | Cruzado | Cz$ | 1000/1 | 1.000 = 1,00 cruzado |
| 16/01/89 a 15/03/90 | Cruzado novo | NCz$ | 1000/1 | 1.000 cruzados = 1,00 cruzado novo |
| 16/03/90 a 31/07/93 | Cruzeiro | Cr$ | 1/1 | 1,00 cruzado novo = 1,00 cruzeiro |
| 01/08/93 a 30/06/94 | Cruzeiro real | CR$ | 1000/1 | 1.000 cruzeiros = 1,00 cruzeiro real |
| 01/07/94 a — | Real | R$ | **2750/1** | uma URV de CR$-2.750,00 = 1 real |

A elipse da quarta linha ("1.000 = 1,00 cruzado", sem unidade) é do manual.

**Defeito do original.** A primeira linha termina em **12/02/70** enquanto a segunda começa
em **13/02/67**: três anos em que as duas moedas coexistiriam. O cruzeiro novo foi
instituído em 13/02/67, e as outras seis transições são todas "dia D / dia D+1". Quase
certamente era **12/02/67**, e o "70" veio contaminado da linha seguinte. **Registrado
como `DEFEITO_DO_ORIGINAL`, não corrigido.**

---

## 7. Pendências

| # | Pendência | Onde |
|---|---|---|
| **P9-01** | Juros da Fazenda **subsidiária** — o manual registra corrente ("grande parte da jurisprudência"), não regra. Ramo sem segmento, por decisão | `pagina_pdf 93` |
| **P9-02** | Índice de correção **anterior a 03/1991** não declarado pelo manual. Buscar na Tabela Única do CSJT e na cadeia do CJF | `pagina_pdf 85` |
| **P9-03** | Termo inicial de juros em processos vindos da **Justiça Estadual ou Federal** | `pagina_pdf 95` |
| **P9-04** | Súmula 439/TST, Súmula 15/TRT-3, OJs 181, 198 e 302 — termo inicial e índice por tipo de verba | `pagina_pdf 83` |
| **P9-05** | **Juros vincendos** (mecânica de decréscimo) — método, não mapa; fora do escopo dirigido, registrado para decisão | `pagina_pdf 95-98` |

---

## 8. As três defasagens

O manual opera **três réguas diferentes**, e nenhuma delas é dispensável:

| Defasagem | Granularidade | Onde | Regra |
|---|---|---|---|
| Súmula 381/TST | **um mês** | tabela mensal, `pagina_pdf 84` | índice do mês seguinte ao da prestação |
| Tabela diária do CSJT | **um dia** | item 7.5.2, `pagina_pdf 87` | traz a TR acumulada **até o dia anterior** à data final informada |
| Pro-ratização | **dias úteis** | item 7.5.2, `pagina_pdf 87` | o índice mensal é decomposto por **dias úteis**, não corridos |

> "se lançarmos a data inicial em 01/05/16 e a data final como 31/05/16, encontraremos o
> índice de 1,001459947, referente à variação da TR entre 01/05/16 a 30/05/16."

Para obter maio cheio é preciso informar **01/06/16** como data final. É defasagem de um
dia, silenciosa, e o manual dá a regra e o contra-exemplo na mesma página.

**E os juros usam uma quarta régua**, incompatível com a terceira: **mês comercial de 30
dias** (`pagina_pdf 88`).

> "incidem atualmente à razão de 1% ao mês, simples (sem cumulação) ou 0,0333% ao dia
> (1 / 30), exceto para os débitos da Fazenda Pública."

**Defeito do original:** a regra imprime `0,0333%` e o exemplo, duas linhas abaixo, imprime
`0,03333%`. Neste exemplo não muda nada — ambos dão 47,666… → **47,67%**, conferido em
`Decimal`. Em contagens longas de dias, muda. O valor exato é a dízima `1/30`, e por R12 o
motor deve computar `Decimal(1)/Decimal(30)`, nunca o truncamento impresso.

Correção pro-ratizada por **dias úteis** e juros por **dias corridos/30** no mesmo cálculo
é atrito real do manual, registrado, não harmonizado.
