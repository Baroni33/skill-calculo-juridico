# Cadernetas de poupança — cadeia própria do CJF

Correção monetária (**"remuneração básica"**) e juros de mora sobre valores devidos segundo os
critérios das contas de poupança, na Justiça Federal. Item **4.9** do **Manual de Orientação de
Procedimentos para os Cálculos na Justiça Federal, CJF, Res. 990/2026**.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 5;
`consolidado/02-atualizacao-detalhe.md` **§ 5.0** (a varredura), **§ 5.3.3**, **§ 5.3.4** e
**§ 5.3.5**;
`docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md` §§ 3.3 e 4 (`N-7`, `N-11`);
`skills/calculo-judicial-atualizacao/regras/cjf.poupanca.correcao-monetaria.json` (12 segmentos) e
`cjf.poupanca.juros-mora.json` (3 segmentos);
`skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json` (`P18-01`).

---

## 0. A advertência que justifica este arquivo existir

> ### **SÓ INCIDE SE O TÍTULO MANDAR — E O EIXO DOS JUROS REMUNERATÓRIOS NÃO É A COMPETÊNCIA.**

Item 4.9, `pagina_pdf` **84**, literal:

> *"**Havendo decisão judicial determinando** a correção monetária dos valores apurados com base
> nos critérios adotados para as contas de poupança, aplicam-se os seguintes indexadores"*.

**Não havendo**, os cálculos seguem o **item 4.2 — ações condenatórias em geral** (REsp 1.075.627;
Resp 754.013; REsp. 1.314.478; EDcl no REsp 1.355.333), *"considerando-se como **termo inicial o
mês em que o crédito deveria ter sido efetivado na conta**"*. `references/civel-federal.md`.

**Alcance declarado:** a poupança **"livre"**, *"a mais encontrada"*. Para modalidades específicas
— *"vinculada, programada, a prazo fixo, de rendimentos crescentes etc."* — o manual manda
**"consultar o juízo"**. **Não há regra de cálculo para elas neste corpus.**

**São três coisas distintas nesta matéria:**

| | Item | Onde |
|---|---|---|
| **Correção monetária** (remuneração básica) — 12 segmentos | 4.9.1.1 | § 2 |
| **Juros remuneratórios** — **não é cadeia temporal**, eixo = **abertura da conta** | 4.9.2 | § 3 |
| **Juros de mora** — mesma tabela do FGTS | 4.9.3 | § 5 |

---

## 1. Dois termos iniciais, e o segundo não é o mês civil

- **NOTA 1** (`pagina_pdf` 85): se a sentença manda aplicar os índices da poupança *"a partir de
  quando era devido o crédito, **sem fixar o termo final**, o cômputo deve-se dar **até o efetivo
  pagamento**"*;
- **NOTA 2** (`pagina_pdf` 85): *"O termo inicial [...] é **o dia em que o crédito deveria ter sido
  efetivado**, aplicando-se, **em cada aniversário, os índices relativos à DATA-BASE DA CONTA**"*.

> ### **EIXO DE ANIVERSÁRIO — a competência não é o mês civil.**
>
> **Nenhuma outra cadeia de correção do manual tem este eixo**
> (`02-atualizacao-detalhe.md` § 5.3.3). O schema `cadeia-temporal` **não o expressa**: os
> segmentos do § 2 são o mapa **período → indexador**, e a **aplicação ao caso passa pelo
> aniversário da conta** (`cjf.poupanca.correcao-monetaria.json`, NOTA 2, campo `efeito`).

**Escopo declarado desta afirmação de ausência:** a varredura do bloco 18 releu **as 93 páginas**
do `manual_de_calculos_2026.pdf` para o sumário de itens e **integralmente** as `pagina_pdf`
**22–39** e **41–87** (`02-atualizacao-detalhe.md` § 5.0). **Fora deste escopo não há afirmação.**

---

## 2. Primeira cadeia — CORREÇÃO MONETÁRIA (item 4.9.1.1, `pagina_pdf` 84–85)

**12 segmentos. Não é o tronco comum do capítulo 4.**

| Período | Indexador | `tipo_indexador` | Observação do manual |
|---|---|---|---|
| **até abr/1967** | **ORTN** | nominal | ponta **materializada** em `1964-01` |
| **maio/1967 – jun/1983** | **UPC** | **indeterminado** | **diverge do FGTS (ORTN)** — § 6 |
| jul/1983 – fev/1986 | **ORTN** | nominal | *"Fev./1986: ORTN **pro rata** até 28/2/1986"* (DL 2.284/1986, art. 4º, § único; Dec. 92.492/1986) |
| mar/1986 – jan/1987 | **IPC/IBGE** | **percentual** | **`R3` cheia na entrada** — § 4 |
| **fev – jun/1987** | **LBC** | **indeterminado** | **diverge do FGTS (OTN) em mar–jun** — § 6 |
| jul – set/1987 | **LBC – 0,5%** | **indeterminado** | |
| out/1987 – dez/1988 | **OTN** | nominal | |
| jan – abr/1989 | **LFT – 0,5%** | **indeterminado** | |
| maio/1989 – mar/1990 | **IPC/IBGE** | **percentual** | *"Mar./1990: contas com data-base e depósitos efetuados **entre 19 e 28/3 – BTNF**"* (art. 6º da Lei 8.024/1990) |
| **abr/1990 – jan/1991** | **BTN** | nominal | *"Jan./1991: **BTNF** desde o último crédito até 31/1/1991 **+ TRD** de 1º/2/1991 até a data do crédito"* (Lei 8.177/1991, art. 13, § único) — **`R3` cheia na entrada**, § 4 |
| fev/1991 – abr/1993 | **TRD** | **indeterminado** | *"Abr./1993: TRD até 2/5/1993 **+ TR pro rata** de 3/5/1993 até a data do crédito"* (Lei 8.660/1993, art. 7º, § 2º) |
| **a partir de maio/1993** | **TR** | **indeterminado** | *"Jun./1994: TR pro rata até 30/6/1994 **+ TR pro rata** de 1º/7/1994 até a data do crédito"* (Lei 9.069/1995, art. 16, §§ 1º e 2º) |

**`ponta_materializada` — as duas pontas:**

- **início `1964-01`**: a primeira linha é *"Até abr./1967"*, **sem início**. `1964-01`
  **materializa** a ponta pelo ano da **Lei 4.380/1964**, primeira norma da lista do item 4.9.1
  (`pagina_pdf` 84). **É materialização declarada, não afirmação do manual**;
- **fim `2026-06`**: o manual escreve *"A partir de maio/1993"*; `2026-06` é a **data-base dos
  exemplos do manual** (item 4.2.1.1, `pagina_pdf` 52).

**A cadeia é perfeitamente contígua**, e por isso **R1 e R2 não se moveram** ao absorvê-la
(`02-atualizacao-detalhe.md` § 5.3.5).

> **Note a assimetria com o FGTS:** esta tabela traz **observação em seis linhas**, com
> fundamento legal e regras de `pro rata` por dia; **a de 4.8.1.1 nem sequer tem coluna de
> observações** (`fgts.md` § 2).

### 2.1 `UPC` e `LBC` só aparecem aqui

**A `UPC` é consumida por esta cadeia e por nenhuma outra** — e a `LBC` (com a `LBC – 0,5%`),
**só por esta e pela do FGTS** (`02-atualizacao-detalhe.md` § 5.3.3; campos
`tipo_indexador_por_que` do JSON).

| Rótulo | Janela | O que o corpus tem |
|---|---|---|
| **UPC** — *"Unidade Padrão de Capital"* | maio/1967 – jun/1983 | **nenhuma classificação em fonte**. O item 2.4.4.1 (`pagina_pdf` 35) apenas **EXPANDE A SIGLA**, o que é **rotulagem, não classificação** |
| **LBC** — *"Letra do Banco Central"* | fev – jun/1987 | **nenhuma classificação em fonte**; não está na lista do item 4.1.2.4 |
| **LBC – 0,5%** | jul – set/1987 | idem, **e o rótulo já embute uma dedução de 0,5% cuja natureza a tabela não declara** — juros descontados? desconto do índice? |

> **Achar fonte é citar item e `pagina_pdf`, não expandir a sigla.** É a regra que impede a
> `UPC` de virar `nominal` por parecer unidade de conta. **`P18-01`, § 4.**

---

## 3. `D8-C16` / `N-11` — o corte é por **DATA DE ABERTURA DA CONTA**

**Juros remuneratórios, item 4.9.2, `pagina_pdf` 86.** Regra base: **0,5% ao mês** (art. 52 do
Dec. 24.427/1934; art. 12 do DL 2.284/1986; art. 2º da Lei 8.088/1990; art. 12 da Lei 8.177/1991);
**6% ao ano**, ou fração *pro rata*, para **cruzados novos bloqueados** (art. 6º da Lei 8.024/1990;
art. 7º da Lei 8.177/1991).

**NOTA 2**, literal:

> *"Tratando-se de **contas abertas a partir de maio/2012** (art. 12 da Lei n. 8.177/1991 com
> alterações da MP n. 567/2012, convertida na **Lei n. 12.703/2012**): **0,5% ao mês, caso a taxa
> Selic ao ano seja superior a 8,5%; e 70% da taxa Selic ao ano, mensalizada, nos demais casos.**"*

> ### **O EIXO NÃO É A COMPETÊNCIA — É A ABERTURA DA CONTA.**
>
> *"Contas abertas a partir de maio/2012"* é um **fato da conta**, não do mês do cálculo. Por isso
> **4.9.2 NÃO virou cadeia temporal**: o schema indexa por competência e **não expressa este
> eixo** (`cjf.poupanca.juros-mora.json`, campo `POR_QUE_NAO_VIROU_CADEIA`).

### 3.1 **Mesmo cálculo, eixos diferentes** — e a armadilha é com 4.5.2 / 4.6.2

| Item | Cálculo a partir de maio/2012 | **Eixo** |
|---|---|---|
| **4.9.2** — poupança | 0,5% a.m. se Selic anual > 8,5%; senão **70% da Selic ao ano, mensalizada** | **abertura da conta** |
| **4.5.2** e **4.6.2** — juros de mora das desapropriações | **exatamente o mesmo** | **COMPETÊNCIA** |

> **`N-11` — registrado, NÃO harmonizado.** *Mesmo cálculo, eixos diferentes.* **Trocar um eixo
> pelo outro muda quais parcelas entram.** `02-atualizacao-detalhe.md` § 5.3.3;
> `references/desapropriacao.md` § 3.

**Os juros remuneratórios são CAPITALIZADOS MENSALMENTE** — NOTA 1 de 4.9.2, *"agregando-se ao
principal em cada período a que se referem"* (REsp 780.085; AgRg-Ag 1.192.553; AgRg-Ag 1.217.521;
**AgRg no REsp n. 1.554.66**; AgRg no Ag 1.098.926). **Não são juros de mora: a `R4` do projeto não
é tocada.**

---

## 4. `P18-01` e as **duas violações `R3` cheias**, que são do manual

### 4.1 Os rótulos `indeterminado`

**Sete rótulos entraram em `indexadores-tipo-catalogo.json` com
`tipo_indexador_pendencia: "P18-01"` e `fonte: null`:** `JAM`, **`UPC`**, **`LBC`**,
**`LBC – 0,5%`**, **`LFT – 0,5%`**, **`TRD`** e o **`IPC` nu**. **Nenhum está na lista do item
4.1.2.4**, e a busca de ausência está declarada no próprio catálogo
(`ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_18`).

**`TRD` e `TR`** seguem a **`P17-02`** do bloco 17: taxa **apurada prospectivamente**, fora do
critério material do item 4.1.2.4 — *"refletem a inflação do próprio mês"* (art. 12, I, da Lei
8.177/1991). **Nenhum dos dois manuais as classifica.**

**Por que o `IPC` nu é `indeterminado` — e esta cadeia é a prova.** `D8-C21` sustenta o
**`IPC/IBGE`**, não o `IPC` sem emissor; **o manual usa DOIS IPC** (IBGE no tronco comum,
**IPC/FGV** no item 4.5.1.1); e **a poupança escreve `IPC/IBGE` nos MESMOS meses em que o FGTS
escreve `IPC`** (mar/1986–jan/1987 e maio/1989–mar/1990). **Identificar os dois rótulos seria a
dedução proibida.** Desenvolvimento em `fgts.md` § 4.

> **Aqui o `IPC/IBGE` É `percentual`, com fonte** — `D8-C21`, literal *"O IPC/IBGE é índice
> percentual"*. **É por isso que esta cadeia tem duas `R3` cheias e a do FGTS não tem nenhuma:**
> a virada só é verificável quando **as duas pontas** têm tipo. `02-atualizacao-detalhe.md`
> § 5.3.5.

### 4.2 As duas `R3` cheias — **do manual, não da modelagem**

| Virada | De | Para | `aplicacao` |
|---|---|---|---|
| **`1986-03`** | **ORTN** — *nominal* | **IPC/IBGE** — *percentual* | **AUSENTE** |
| **`1990-04`** | **IPC/IBGE** — *percentual* | **BTN** — *nominal* | **AUSENTE** |

> ### **TROCA DE TIPO SEM AJUSTE DE DEFASAGEM DESLOCA O CÁLCULO EM UM MÊS.**
>
> Item 4.1.2.4, `pagina_pdf` 42. **É o mesmo padrão que as cadeias do tronco comum já exibem em
> jan/1989 e mar/1990.** **AS DUAS SÃO DO MANUAL — transcritas, NÃO harmonizadas**
> (`02-atualizacao-detalhe.md` § 5.3.5).

**Placar do bloco 18** (`valida_cadeias.py`, 11 → **15** cadeias):

| Cadeia | R1 | R2 | **R3** | **R3-INDETERMINADO** |
|---|---|---|---|---|
| `cjf.poupanca.correcao-monetaria` | 0 | 0 | **2** | **9** |
| `cjf.poupanca.juros-mora` | 0 | 0 | 0 | 0 |
| `cjf.fgts.correcao-monetaria` | 0 | 0 | 0 | 10 |
| `cjf.fgts.juros-mora` | 0 | 0 | 0 | 0 |

**As 19 `R3-INDETERMINADO` são a `P18-01` tornada visível**, não defeito. **Classificar por dedução
as faria sumir — e a dedução passaria limpa.**

---

## 5. Segunda cadeia — JUROS DE MORA (item 4.9.3, `pagina_pdf` 86)

**É a MESMA TABELA do FGTS, palavra por palavra** (`pagina_pdf` 83 e 86).

**Termo inicial:** *"Os juros são contados a partir da citação, salvo determinação judicial em
outro sentido."*

| Período | Taxa / índice | Fundamento |
|---|---|---|
| até **dez/2002** | **0,5% ao mês, simples** | arts. 1.062, 1.063 e 1.064 do CC/1916 |
| **jan/2003 – ago/2024** | **SELIC** — engloba correção **e** juros | art. 406 do CC/2002 |
| **a partir de set/2024** | **taxa legal** (SELIC com dedução do **IPCA-15**) | art. 406 do CC, redação da **Lei 14.905/2024**, e **Res. CMN 5.171/2024** |

> ### **ACHADO — O CALENDÁRIO DE JUROS DESTA CADEIA É OUTRO.**
>
> **Não há corte de dez/2021** (EC 113/2021) **nem de set/2025** (EC 136/2025). A taxa legal entra
> em **set/2024** — **um ano antes** de todas as demais cadeias do manual — com fundamento **só**
> na Lei 14.905/2024 e na Res. CMN 5.171/2024, **SEM citar o ARE 1.557.312/SP (Tema 1.419 do
> STF)**, que todas as outras citam.
>
> **Quem aplicar aqui o calendário das condenatórias gerais erra.**
>
> **Consequência verificada:** **poupança e FGTS NÃO estão entre os cinco lugares que consolidam
> em dez/2021.** Varredura de `0,4412`: ocorre nas `pagina_pdf` **50, 59, 67, 74 e 79** —
> **nenhuma é 83 nem 86**. `02-atualizacao-detalhe.md` §§ 5.3.4 e 10; quadro completo em
> `tributario-federal.md` § 8. **Transcrito como está, não harmonizado.**

### 5.1 `N-7` — *"vedada sua incidência cumulada com os juros de mora"*

NOTA 1, alínea *a*: *"A taxa Selic [...] deve ser capitalizada de forma simples, sendo **vedada sua
incidência cumulada com os juros de mora** e com a correção monetária"*.

> **E a tabela que ela qualifica É de juros de mora.** **Boilerplate autorreferente**, copiado da
> seção de correção monetária, que ocorre em **4.2.2 NOTA 1 a), 4.6.2, 4.8.3 e 4.9.3** — quatro
> vezes. **Registrado, não corrigido.** `02-atualizacao-detalhe.md` § 5.3.4;
> `desapropriacao.md` § 3.

### 5.2 A alínea *b* é a fórmula **D4**

*"a partir do mês seguinte ao de **competência da parcela devida** até o mês anterior ao pagamento,
e 1% no mês do pagamento"*.

> **O bloco 8 atribuía a `D4` SÓ À DÍVIDA FISCAL** (itens 2.3.1.2 e 2.4.2.2.2). **4.8.3 e 4.9.3
> também a usam** — a quarta fórmula **tem mais um domicílio do que o registrado**
> (`02-atualizacao-detalhe.md` § 5.3.4). **Não é a `D2`** das condenatórias, que ancora no **termo
> inicial dos juros**.

**A taxa legal, porém, segue a `D1`** — NOTA 4: *"A taxa legal observará as mesmas orientações
estabelecidas na Nota 7 do item 4.2.2"*, e a Nota 7 (`pagina_pdf` 56) manda aplicá-la **no mês
posterior ao de sua competência** (`R-08-11`).

### 5.3 `R1` dita pela fonte, **com o nome próprio da poupança**

NOTA 3 (`pagina_pdf` 87): pela Selic, *"que também contempla correção monetária, não devem incidir
concomitantemente com a **remuneração básica**, mas tão somente com os juros remuneratórios
respectivos. A Selic incidirá sobre o principal acrescido dos juros remuneratórios"*.

**O que a Selic exclui é a REMUNERAÇÃO BÁSICA (item 4.9.1); o que ela PRESERVA por fora são os
juros remuneratórios (item 4.9.2).** A NOTA 3 do FGTS diz o mesmo trocando *"remuneração básica"*
por *"correção monetária"*. E a **NOTA 2** confirma: *"Os juros remuneratórios e moratórios incidem
concomitantemente, ou seja, não são reciprocamente excludentes"* (REsp 466.732).

---

## 6. `D8-C15` — a divergência com o FGTS, **sem fundamento legal**

| Janela | Poupança (4.9.1.1) | FGTS (4.8.1.1) | Duração |
|---|---|---|---|
| **maio/1967 – jun/1983** | **UPC** | **ORTN** | 16 anos e 2 meses |
| **mar – jun/1987** | **LBC** | **OTN** | 4 meses |

**Dezesseis anos e quatro meses.** **Nenhuma das duas tabelas traz fundamento legal para a
divergência** — a de 4.8.1.1 **sequer tem coluna de observações** — **e o manual não a explica.
NÃO HARMONIZADA** (`02-atualizacao-detalhe.md` § 5.3.3).

**Fev/1987 é o único mês de concordância entre fev. e jun./1987**, e com recorte diferente: a
poupança **funde** fev/1987 no bloco fev–jun/1987; o FGTS abre **segmento de um mês só**.

**E o corte da ORTN difere nos TRÊS lugares:** **jun/1983** aqui, **fev/1986** em 4.8.1.1,
**set/1983** no **FGTS fiscal** do item 2.4.4.1 (`fgts.md` § 7).

---

## 7. NOTA 3 de 4.9.1.1 — **uma segunda cadeia que só vive na nota**

`pagina_pdf` **85**, literal:

> *"Para correção de **cruzados novos bloqueados** na forma da Lei n. 8.024/1990 — Plano Collor
> (conversão da MP n. 168/1990), aplicam-se os seguintes índices até a data da conversão:
> **BTNF desde o bloqueio até jan./1991; e TRD, de fev./1991 em diante.**"*

> ### **CADEIA PARALELA QUE NENHUMA TABELA MOSTRA.**
>
> **Dois trechos — BTNF e TRD — que a tabela de 4.9.1.1 não exibe**, para um **subconjunto de
> saldos**. É o padrão *"a regra vive só no item"*
> (`consolidado/07-leitura-do-corpus.md` § 1), o **mesmo desenho do `N-8`** e do corte de
> **ago/2017** dos compensatórios (`desapropriacao.md` § 4.2).
>
> **NÃO gravados como segmentos:** são **regime alternativo**, não trecho desta linha do tempo
> (`cjf.poupanca.correcao-monetaria.json`, NOTA 3, campo `efeito`).
>
> **O eixo é o BLOQUEIO, e o termo final é a DATA DA CONVERSÃO** — nem um nem outro é competência.

**Há ainda um BTNF dentro da própria tabela**, e também só em observação: *"Mar./1990: contas com
data-base e depósitos efetuados **entre 19 e 28/3 – BTNF**"* (§ 2). **A regra que troca o índice
está na coluna de observação, não na de indexador.**

---

## 8. Defeitos do original — **transcritos como estão**

| # | `pagina_pdf` | Item | Defeito |
|---|---|---|---|
| **`D8-D19`** | 86 | 4.9.2 | *"AgRg no REsp n. **1.554.66**"* — **número truncado** no original |
| **`D8-D24`** | 84 | 4.9.1 | *"de **31de** outubro de 1990"* — falta o espaço |
| **`D8-D25`** | 84 | 4.9 | *"**REsp** n. 1.075.627; **Resp** n. 754.013; **REsp.** n. 1.314.478"* — **três grafias da mesma abreviatura na mesma linha** (e *"REsp."* também em 4.8, `pagina_pdf` 81) |

**NENHUM CORRIGIDO.** `cjf.poupanca.correcao-monetaria.json`, campo
`DEFEITOS_DO_ORIGINAL_TRANSCRITOS`; `cjf.poupanca.juros-mora.json`, campo `D8_D19`. Índice geral
em `docs/calculo/armadilhas-comparador.md`.

> **E o contraste que ABSOLVE a poupança:** 4.9.2 grafa corretamente **"Lei n. 12.703/2012"**,
> enquanto a gêmea **4.5.2 grafa *"Lei n. 2.703/2012"*** (**`D8-D14`**, `pagina_pdf` 68). **O
> defeito é de 4.5.2, e a poupança é a prova** (`desapropriacao.md` § 8).

---

## 9. Limitações declaradas

1. **As duas `R3` cheias (`1986-03` e `1990-04`) são DO MANUAL** — troca de tipo **sem `aplicacao`
   declarada**. **Transcritas, NÃO harmonizadas** (§ 4.2). Toda conta que as atravesse **grava
   qual defasagem aplicou** (`R19`);
2. **`D8-C15` — dezesseis anos e quatro meses de divergência com o FGTS, sem fundamento legal em
   nenhuma das duas tabelas.** **Não harmonizada** (§ 6);
3. **`P18-01` — `UPC`, `LBC`, `LBC – 0,5%`, `LFT – 0,5%`, `TRD`, `TR` e o `IPC` nu ficam
   `indeterminado`.** **Expandir a sigla não é classificar**, e **classificar por dedução a partir
   do nome é proibido**. Daí **9 `R3-INDETERMINADO`** nesta cadeia (§ 4);
4. **`D8-C16` / `N-11` — o eixo de 4.9.2 é a ABERTURA DA CONTA, e 4.5.2/4.6.2 aplicam o mesmo
   cálculo POR COMPETÊNCIA.** **Registrado, não harmonizado**, e **4.9.2 não virou cadeia
   temporal** (§ 3);
5. **O eixo de ANIVERSÁRIO da NOTA 2 de 4.9.1.1 não é expresso pelo schema.** Os segmentos do § 2
   são o mapa período → indexador; **a aplicação ao caso passa pela data-base da conta** (§ 1);
6. **A cadeia paralela da NOTA 3 (cruzados novos bloqueados: BTNF + TRD) NÃO foi gravada como
   segmento** — é **regime alternativo**, e **não foi inferida** (§ 7);
7. **As modalidades não-"livre" de poupança não têm regra neste corpus** — o manual manda
   *"consultar o juízo"* (§ 0). **Nada foi suprido**;
8. **O calendário de juros não tem dez/2021 nem set/2025, e não cita o ARE 1.557.312.**
   **Transcrito como está** (§ 5); **poupança e FGTS não consolidam em dez/2021** — varredura de
   `0,4412` declarada em § 5;
9. **Os defeitos `D8-D19`, `D8-D24` e `D8-D25` foram transcritos, não corrigidos** (§ 8). O
   **`D8-D19` é número de acórdão truncado**: **não se completou o número**, porque completá-lo
   seria pesquisa externa;
10. **`P18-02` — oito cadeias tabuladas do manual seguem sem JSON**, entre elas **4.5.2 e 4.6.2**,
    que são justamente as que compartilham a fórmula do § 3.1. **A ausência está registrada, não
    silenciada**, e **não foi suprida aqui** (`02-atualizacao-detalhe.md` §§ 5.0 e 5.3.5);
11. **As séries não estão aqui.** ORTN, **UPC**, IPC/IBGE, **LBC**, `LBC – 0,5%`, OTN,
    `LFT – 0,5%`, BTN, **BTNF**, TRD e TR são dado **(B)** — contrato em
    `skills/indices-judiciais/`. **`UPC`, `LBC` e `BTNF` são as que mais facilmente faltam no
    catálogo: só esta cadeia (e, quanto à LBC, a do FGTS) as consome**;
12. **Sem preset nomeado no corpus para esta matéria.** Entra **como cadeia, não como preset**.
    Registrado, **não inventado**.

---

## 10. Ponteiros

- `skills/calculo-judicial-atualizacao/regras/cjf.poupanca.correcao-monetaria.json` — 12 segmentos, a condição
  de incidência, o escape para 4.2, as três notas e os defeitos transcritos
- `skills/calculo-judicial-atualizacao/regras/cjf.poupanca.juros-mora.json` — 3 segmentos, o achado do
  calendário e o bloco `JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA` (`D8-C16`, `N-11`, `D8-D19`)
- `skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json` — `P18-01` e o escopo da busca
  de ausência
- `docs/calculo/consolidado/02-atualizacao-detalhe.md` **§ 5.0** (a varredura item × JSON ×
  consolidado), **§ 5.3.3** (esta cadeia), **§ 5.3.4** (o que é comum ao FGTS) e **§ 5.3.5**
  (o placar dos validadores e as 21 violações novas de `R3`)
- `docs/calculo/consolidado/02-atualizacao.md` § 5 — a espinha
- `docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md` §§ 3.3 e 4 — `N-7` e `N-11`
- `references/fgts.md` — a cadeia gêmea, o `JAM`, o corte por **saque integral** e a razão do
  `IPC` nu
- `references/desapropriacao.md` § 3 — **4.5.2 e 4.6.2**, o mesmo cálculo **por competência**
- `references/civel-federal.md` — condenatórias em geral, **para onde vai quem não tem decisão
  determinando os critérios da poupança**
- `references/tributario-federal.md` — as quatro fórmulas de `aplicacao`, ECs 113/136 e os cinco
  lugares de dez/2021
- `docs/calculo/armadilhas-comparador.md` — índice dos defeitos do original
