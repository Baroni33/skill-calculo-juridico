# FGTS — cadeia própria do CJF, critério `JAM`

Correção monetária e juros de mora sobre valores devidos **ao titular da conta fundiária**, na
Justiça Federal. Item **4.8** do **Manual de Orientação de Procedimentos para os Cálculos na
Justiça Federal, CJF, Res. 990/2026**.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 5 (linhas de FGTS e poupança);
`consolidado/02-atualizacao-detalhe.md` **§ 5.0** (a varredura), **§ 5.3.2**, **§ 5.3.4** e
**§ 5.3.5**;
`docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md` §§ 3.2 e 4 (`N-5`, `N-7`);
`skills/calculo-judicial-atualizacao/regras/cjf.fgts.correcao-monetaria.json` (11 segmentos) e
`cjf.fgts.juros-mora.json` (3 segmentos);
`skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json` (`P18-01`).

---

## 0. A advertência que justifica este arquivo existir

> ### **O FGTS NÃO SEGUE A CORREÇÃO MONETÁRIA GERAL DO CAPÍTULO 4.**
>
> **Tronco próprio desde jan/1967**, calendário de juros próprio, **três eixos de corte que
> nenhuma outra cadeia usa** e **dois conjuntos de expurgos incompatíveis** com os do capítulo 4.

**É o mesmo modo de falha que produziu `desapropriacao.md`** — e o consolidado o diz com todas as
letras (`02-atualizacao-detalhe.md` § 5.3.2): *"quem tratou o FGTS pela linha de correção monetária
geral perdeu a cadeia inteira"*. O rótulo **`JAM` tinha zero ocorrências no diretório
`consolidado/` até o bloco 18**.

**São DUAS cadeias aqui, e uma terceira que não é desta matéria:**

| | Item | Onde |
|---|---|---|
| **Correção monetária** — critério `JAM` | 4.8.1.1 | § 2 |
| **Juros de mora** | 4.8.3 | § 5 (comum à poupança) |
| **Juros remuneratórios** — **não é cadeia temporal** | 4.8.2 | § 6 |
| **FGTS fiscal** — critério **`JCM`**, **OUTRA cadeia, outro sujeito** | **2.4.4.1** | § 7 |

---

## 1. `JAM` é o NOME DO CRITÉRIO, não um indexador

Item **4.8**, `pagina_pdf` **81**, literal:

> *"os valores apurados deverão ser corrigidos com base nos critérios adotados para as contas
> fundiárias (**Juros e Atualização Monetária — JAM**), com os indexadores seguintes"*.

**Os indexadores são os da tabela 4.8.1.1** (§ 2). `JAM` nomeia o critério inteiro.

> **Não é a tabela JAM da CEF** do item **6.14 do Manual do TRT-3** (regime `pr.fgts-indice-jam`).
> Outro manual, outra fonte e **outro eixo** — lá o eixo é o **conteúdo do título**, e a tabela
> *"já computa juros de 3% ao ano"*. Aquilo pertence a `calculo-trabalhista-liquidacao`;
> **isto**, ao cap. 4 do CJF. `cjf.fgts.correcao-monetaria.json`, campo
> `criterio_declarado.NOTA_DO_EXTRATOR`.

### 1.1 As duas notas que abrem escapes — e o eixo `D8-C12`

Ambas em `pagina_pdf` **81** (`escapes_declarados` do JSON):

| Nota | Literal | Efeito |
|---|---|---|
| **1** | *"Se o título judicial determinar [...] como **dívida comum** (ex.: REsp. n. 630.372) e **não havendo previsão de índice na sentença**, aplicam-se os indexadores previstos para condenações em geral (Seção 4.2 deste capítulo)"* | **eixo de CONTEÚDO DO TÍTULO** — a cadeia inteira cede a `cjf.condenatorias-gerais.*` e **deixa de valer** |
| **2** | *"Se o título judicial determinar a correção e juros pelos critérios fundiários **somente até a data do saque integral** (ex.: REsp n. 694.365; AgRg no REsp n. 622.298), devem ser aplicados, **a contar do saque integral** e se não houver previsão de índice na sentença, os indexadores previstos para condenações em geral"* | **`D8-C12` — corte por SAQUE INTEGRAL** |

> ### **`D8-C12` — o saque integral não é competência e não é sentença.**
>
> É um **fato do contrato de trabalho / da conta**. **Nenhuma outra cadeia do manual usa este
> eixo**, e **nenhuma tabela o mostra** — ele vive só no texto do item 4.8
> (`02-atualizacao-detalhe.md` § 5.3.2; `escapes_declarados[1].efeito` do JSON).
>
> **Consequência para o motor:** antes de resolver qualquer competência é preciso saber
> **(a)** o que o título determinou e **(b)** se houve saque integral e quando. Sem isso **não há
> cadeia aplicável** — há duas, e não se sabe onde uma termina.

**Escopo declarado desta afirmação de ausência:** a varredura do bloco 18 releu **as 93 páginas**
do `manual_de_calculos_2026.pdf` para o sumário de itens e **integralmente** as `pagina_pdf`
**22–39** e **41–87** (`02-atualizacao-detalhe.md` § 5.0). **Fora deste escopo não há afirmação.**

---

## 2. Primeira cadeia — CORREÇÃO MONETÁRIA (item 4.8.1.1, `pagina_pdf` 82)

**11 segmentos. Não é o tronco comum do capítulo 4** — compare com `civel-federal.md` § 1 e
`desapropriacao.md` § 1, que compartilham ORTN→OTN→IPC/IBGE→BTN→IPC/IBGE.

| Período | Indexador | `tipo_indexador` | |
|---|---|---|---|
| **jan/1967 – fev/1986** | **ORTN** | nominal | início **declarado**, não materializado |
| mar/1986 – jan/1987 | **IPC** | **indeterminado** | rótulo **nu** — § 4 |
| **fev/1987** | **LBC** | **indeterminado** | segmento de **UM MÊS** |
| mar – jun/1987 | **OTN** | nominal | **diverge da poupança (LBC)** — § 3 |
| jul – set/1987 | **LBC – 0,5%** | **indeterminado** | |
| out/1987 – dez/1988 | **OTN** | nominal | |
| **jan – abr/1989** | **LFT – 0,5%** | **indeterminado** | é sobre esta linha que a NOTA 2 manda incluir **42,72%** |
| maio/1989 – mar/1990 | **IPC** | **indeterminado** | rótulo nu |
| **abr/1990 – jan/1991** | **BTN** | nominal | é sobre esta linha que a NOTA 2 manda incluir **44,80%** |
| fev/1991 – abr/1993 | **TRD** | **indeterminado** | |
| **a partir de maio/1993** | **TR** | **indeterminado** | ponta materializada em `2026-06` |

**A tabela 4.8.1.1 NÃO TEM COLUNA DE OBSERVAÇÕES** — e por isso **nenhuma linha traz fundamento
legal** (`02-atualizacao-detalhe.md` § 5.3.2). É o contraste exato com a poupança, cuja tabela
gêmea traz observação em seis linhas (`poupanca.md` § 2).

**`ponta_materializada` — as duas pontas:**

- **início `1967-01`**: a primeira linha é *"De jan./1967 a fev./1986"* — **início declarado, sem
  materialização**, o que é **raro no manual**: as demais cadeias do cap. 4 abrem com *"De 1964"*,
  sem mês (`P8-07`);
- **fim `2026-06`**: o manual escreve *"A partir de maio/1993"*; `2026-06` é a **data-base dos
  exemplos do próprio manual** (item 4.2.1.1, `pagina_pdf` 52).

**A cadeia é perfeitamente contígua** — fim e início nunca caem no mesmo mês. Por isso as
validações **R1 e R2 não se moveram** ao absorvê-la (`02-atualizacao-detalhe.md` § 5.3.5): o FGTS
**não tem** o problema de sobreposição de jan/1989 e mar/1990 do tronco comum.

---

## 3. `D8-C15` — FGTS × poupança divergem em **dezesseis anos e quatro meses**

| Janela | FGTS (4.8.1.1) | Poupança (4.9.1.1) | Duração |
|---|---|---|---|
| **maio/1967 – jun/1983** | **ORTN** | **UPC** | 16 anos e 2 meses |
| **mar – jun/1987** | **OTN** | **LBC** | 4 meses |

> ### **NENHUMA DAS DUAS TABELAS TRAZ FUNDAMENTO LEGAL PARA A DIVERGÊNCIA.**
>
> A de **4.8.1.1 sequer tem coluna de observações**, e **o manual não a explica**
> (`02-atualizacao-detalhe.md` § 5.3.3; campo `DIVERGENCIAS_COM_A_POUPANCA` dos dois JSON).
> **NÃO HARMONIZADA.** Quem resolver o FGTS pela tabela da poupança — ou o contrário — **erra
> dezesseis anos e quatro meses**.

**Fev/1987 é o único mês em que as duas concordam entre fev. e jun./1987**, e ainda assim com
recorte diferente: o FGTS abre um **segmento de um mês só** com LBC; a poupança **funde** fev/1987
no bloco fev–jun/1987 (`cjf.fgts.correcao-monetaria.json`, campo `fev_1987`).

**Some-se a divergência de RÓTULO do IPC**, em duas janelas (mar/1986–jan/1987 e
maio/1989–mar/1990): o FGTS escreve **`IPC`**; a poupança, **`IPC/IBGE`**. **Mesmos meses,
rótulos diferentes.** Registrado, **não harmonizado** — e é o que sustenta o § 4.

---

## 4. `P18-01` — por que o **`IPC` nu** é `indeterminado`

**Sete rótulos entraram em `indexadores-tipo-catalogo.json` com
`tipo_indexador_pendencia: "P18-01"` e `fonte: null`:** `JAM`, `UPC`, `LBC`, `LBC – 0,5%`,
`LFT – 0,5%`, `TRD` e **`IPC`**. **Nenhum está na lista do item 4.1.2.4**, e a busca de ausência
está declarada no próprio catálogo (`ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_18`).

### A razão do `IPC`, que é a menos óbvia das sete

1. **`D8-C21` sustenta o `IPC/IBGE`, não o `IPC`.** O literal registrado é *"O IPC/IBGE é índice
   percentual"* (`bloco-08-jf-detalhe.md`). **Ele não alcança um rótulo sem emissor**;
2. **o manual usa DOIS IPC de emissores distintos** — **IPC/IBGE** no tronco comum do cap. 4 e
   **IPC/FGV** no item 4.5.1.1 (desapropriação, `pagina_pdf` 66). O pressuposto que justificou
   identificar `INPC` com `INPC/IBGE` — *"não existe INPC de outro emissor"* — **é falso para o
   IPC**;
3. **a tabela gêmea da poupança escreve `IPC/IBGE` nos mesmos meses** (§ 3). Concluir que o `IPC`
   do FGTS **é** aquele `IPC/IBGE` é **dedução a partir do rótulo**, que este projeto proíbe;
4. **é a mesma classe de erro que já ocorreu aqui:** o bloco 8 registrou a troca de **IPC/FGV por
   IPC/IBGE em 78 segmentos** (`02-atualizacao-detalhe.md` § 5.3.4).

> **E classificá-lo não limparia nada — pioraria.** `cjf.fgts.correcao-monetaria` tem **0
> violações `R3` cheias e 10 `R3-INDETERMINADO`**. **Classificar o `IPC` nu criaria DUAS R3 a
> mais, não menos** (`02-atualizacao-detalhe.md` § 5.3.5), exatamente as que a poupança exibe
> (`poupanca.md` § 4). **A abstenção é o resultado, não a falta dele.**

**As 19 `R3-INDETERMINADO` das duas cadeias não são defeito do manual nem da modelagem: são a
`P18-01` tornada visível.** Se `UPC`, `LBC`, `LFT` e `TRD` fossem classificados por dedução,
**as 19 sumiriam e a dedução passaria limpa** — que é o que o bloco 17 proibiu.

**`JAM` não é indexador** — é o nome do critério (§ 1). Foi registrado no catálogo **porque o
rótulo circula como se fosse**.

---

## 5. Segunda cadeia — JUROS DE MORA (item 4.8.3, `pagina_pdf` 83)

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
> **Quem aplicar aqui o calendário das condenatórias gerais erra**: cria um corte em dez/2021 que
> esta tabela não tem, e atrasa a taxa legal em um ano.
>
> **Consequência verificada:** **FGTS e poupança NÃO estão entre os cinco lugares que consolidam
> em dez/2021.** Varredura de `0,4412`: ocorre nas `pagina_pdf` **50, 59, 67, 74 e 79** —
> **nenhuma é 83 nem 86**. `02-atualizacao-detalhe.md` §§ 5.3.4 e 10; quadro dos cinco lugares em
> `tributario-federal.md` § 8. **Transcrito como está, não harmonizado.**

### 5.1 `N-7` — a nota autorreferente

NOTA 1, alínea *a*: *"A taxa Selic [...] deve ser capitalizada de forma simples, sendo **vedada
sua incidência cumulada com os juros de mora** e com a correção monetária"* — **e a tabela que ela
qualifica É de juros de mora**.

**Boilerplate copiado da seção de correção monetária.** Ocorre em **4.2.2 NOTA 1 a), 4.6.2, 4.8.3
e 4.9.3** — quatro vezes. **Registrado, não corrigido** (`desapropriacao.md` § 3;
`02-atualizacao-detalhe.md` § 5.3.4).

### 5.2 A alínea *b* é a fórmula **D4** — e o bloco 8 a dava só à dívida fiscal

Literal: *"deve ser aplicada a partir do mês seguinte ao de **competência da parcela devida** até
o mês anterior ao pagamento, e 1% no mês do pagamento"*.

| Fórmula | Eixo | Onde o bloco 8 a localizava |
|---|---|---|
| **D4** | **competência da parcela** | **só a dívida fiscal** (2.3.1.2 e 2.4.2.2.2) |

> **`D4` tem mais um domicílio — dois, na verdade: 4.8.3 e 4.9.3.** **Não é a `D2`** das
> condenatórias, que ancora no **termo inicial dos juros**. `02-atualizacao-detalhe.md` § 5.3.4;
> as quatro fórmulas em `tributario-federal.md` (seção transversal) e em
> `02-atualizacao-detalhe.md` § 5.3.

**A taxa legal, porém, segue a `D1`** — NOTA 4: *"A taxa legal observará as mesmas orientações
estabelecidas na Nota 7 do item 4.2.2"*, e a Nota 7 (`pagina_pdf` 56) manda aplicá-la **no mês
posterior ao de sua competência** (`R-08-11`). **Duas fórmulas diferentes dentro da mesma cadeia
de juros.**

### 5.3 `R1` dita pela fonte, **com nome próprio**

NOTA 3: pela Selic *"não deve incidir concomitantemente a correção monetária, já contemplada, mas
tão somente [...] os juros **remuneratórios** respectivos. A Selic incidirá sobre o principal
acrescido dos juros remuneratórios"* (REsp 1.102.552).

**O que a Selic exclui é a correção monetária; o que ela PRESERVA por fora são os juros
remuneratórios do item 4.8.2.** E a **NOTA 2** o confirma: *"Os juros remuneratórios e moratórios
incidem concomitantemente, ou seja, não são reciprocamente excludentes"* (REsp 897.043).

---

## 6. Juros remuneratórios (4.8.2) — **não são cadeia temporal**, e o `D8-D18`

**Regra**, `pagina_pdf` 82: 3% a.a. (Lei 5.705/1971 e art. 13 da Lei 8.036/1990); **3%, 4%, 5% ou
6% progressivos** para **contas existentes em 22/9/1971** (Súmula 154 do STJ); **6% a.a.** para os
casos enquadrados no art. 1º da Lei 8.678/1993.

> **O eixo NÃO É A COMPETÊNCIA:** é a **existência da conta em 22/9/1971**, ou o enquadramento no
> art. 1º da Lei 8.678/1993. O schema `cadeia-temporal` indexa por competência e **não expressa
> este eixo** — por isso a regra está **registrada no JSON, fora dos segmentos**
> (`JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA`).

### `D8-D18` — defeito do original, **transcrito como está**

> *"art. 4º da Lei n. 5.107/**1986**"* — item 4.8.2, `pagina_pdf` 82.

**A Lei 5.107 é de 13 de setembro de 1966**, como **o próprio item 4.8.1 a data uma página antes**
(`pagina_pdf` 81). **NÃO CORRIGIDO.** Índice geral em `docs/calculo/armadilhas-comparador.md`.

---

## 7. O **FGTS fiscal do item 2.4.4.1 é OUTRA cadeia** — `JCM`, não `JAM`

| | **4.8** (este arquivo) | **2.4.4.1** |
|---|---|---|
| **Sujeito** | **titular da conta** é credor | **o Fundo** é credor — débito do **empregador** |
| **Critério** | **`JAM`** — *"Juros e Atualização Monetária"* | **`JCM`** — *"coeficiente da remuneração das contas vinculadas"* |
| **Capítulo** | 4 (condenatórias e matérias afins) | **2 (dívida fiscal)** |
| **Corte da ORTN** | **fev/1986** | **set/1983** |

E há um terceiro valor para o mesmo corte: **jun/1983 na poupança** (§ 3). **O corte da ORTN
difere nos três lugares.**

A cadeia de 2.4.4.1 (`pagina_pdf` 35–36) segue com **UPC** e *"os índices básicos de atualização
dos saldos da poupança"*, conversão em **BTNF** em 1º/11/1989, multiplicação por **126,8621** em
1º/2/1991, **TRD** de fev/1991 a maio/2000 e **TR** a partir de maio/2000.

> ### **O corte de maio/2000 é DELE, e NÃO alcança o item 4.8.**
>
> O **`D8-C8`** — *"De fev./1991 a maio/2000"* × *"A partir de maio/2000"*, **sem regra de
> desempate** — **é do item 2.4.4.1**. Aplicá-lo a esta cadeia é misturar sujeito, sigla e
> capítulo. `02-atualizacao-detalhe.md` § 5.3.2; campo `NAO_E_A_CADEIA_DO_ITEM_2_4_4_1` do JSON.

**E ela segue como LACUNA.** 2.4.4.1 está entre as **oito cadeias tabuladas do manual sem JSON**
registradas como **`P18-02`** (`02-atualizacao-detalhe.md` §§ 5.0 e 5.3.5). **Razão declarada da
não geração:** *"2.4.4.1 é lista, não tabela"*, com o `D8-C8` em aberto. **A ausência está
registrada, não silenciada** — e **não foi suprida aqui**.

---

## 8. `D8-C13` / `N-5` — dois conjuntos de expurgos, e o do FGTS **não diz o que faz**

**NOTA 2** do item 4.8.1.1, `pagina_pdf` 82, literal:

> *"Se a ação de revisão dos saldos do FGTS **não discutir** os expurgos inflacionários (ex.: juros
> progressivos), a liquidação deve **incluir** os expurgos inflacionários reconhecidos pelo STJ em
> casos de FGTS: **42,72% em jan./1989 e 44,80% em abr./1990**."*

| | **Capítulo 4 geral** | **FGTS (4.8.1.1)** |
|---|---|---|
| jan/1989 | 42,72% | **42,72%** |
| fev/1989 | **10,14%** | — |
| abr/1990 | — | **44,80%** |
| **operação** | *"Expurgo, **em substituição** ao BTN"*; item 4.1.2.1: *"descontando o BTN ou outro índice utilizado, **evitando bis in idem**"* | **NÃO DECLARADA** |

> ### **SUBSTITUI OU ACRESCE? O MANUAL NÃO DIZ. PENDÊNCIA ABERTA — NÃO SE RESOLVE AQUI.**
>
> As linhas de **jan/1989** e **abr/1990** **já trazem indexador** (`LFT – 0,5%` e `BTN`), e a
> **tabela não menciona expurgo algum**.
>
> **Por isso os dois percentuais NÃO foram gravados como segmento:** gravá-los **exigiria escolher
> entre substituir e somar**, e a escolha não está na fonte. `N-5` e `D8-C13` **continuam
> abertas** — `02-atualizacao-detalhe.md` §§ 5.3.2 e 5.3.5; campo `PENDENCIA_ABERTA` da NOTA 2 no
> JSON.
>
> **Toda conta que atravesse jan/1989 ou abr/1990 grava qual leitura aplicou** (`R19`).

### 8.1 `D8-C14` — a bifurcação contraintuitiva das duas notas

| | Quem **DISCUTE** expurgos (NOTA 1) | Quem **NÃO discute** (NOTA 2) |
|---|---|---|
| Recebe | *"somente [...] os períodos definidos pelo julgado"* | **os dois expurgos, por padrão** |

> ***Quem discute pode receber menos do que quem não discute.***
>
> **Não é erro formal; é o que está escrito** (`02-atualizacao-detalhe.md` § 5.3.2). Registrado,
> **não harmonizado**. O motor precisa do atributo *"a ação discute expurgos?"* **antes** de
> montar a cadeia.

---

## 9. Limitações declaradas

1. **`N-5` / `D8-C13` — os expurgos do FGTS não declaram se SUBSTITUEM ou ACRESCEM.** **Pendência
   aberta.** Os percentuais **não viraram segmento** e **não foram inferidos** (§ 8);
2. **`D8-C14` — a bifurcação das notas 1 e 2 é contraintuitiva e não foi harmonizada** (§ 8.1);
3. **`D8-C15` — a divergência de dezesseis anos e quatro meses com a poupança não tem fundamento
   legal em nenhuma das duas tabelas**, e **a de 4.8.1.1 sequer tem coluna de observações**.
   **Não harmonizada** (§ 3);
4. **`P18-01` — sete rótulos sem classificação em fonte alguma.** `JAM`, `UPC`, `LBC`,
   `LBC – 0,5%`, `LFT – 0,5%`, `TRD` e o **`IPC` nu** ficam **`indeterminado`**. **Classificá-los
   por dedução a partir do nome é proibido**, e no caso do `IPC` **criaria duas `R3` a mais**
   (§ 4). Daí **10 `R3-INDETERMINADO`** nesta cadeia;
5. **`P18-02` — o FGTS fiscal (item 2.4.4.1, critério `JCM`) NÃO TEM JSON** e segue como lacuna,
   entre as oito registradas. **Não é esta cadeia** e **não foi suprido aqui** (§ 7);
6. **`D8-D18` — *"Lei n. 5.107/1986"*, que é de 1966.** Defeito do original, **transcrito**;
7. **O corte por SAQUE INTEGRAL (`D8-C12`) não aparece em tabela alguma** — vive só no texto do
   item 4.8. **Afirmação de ausência com escopo declarado em § 1.1**;
8. **Os juros remuneratórios de 4.8.2 não são cadeia temporal** (eixo = conta existente em
   22/9/1971). Registrados fora dos segmentos, **não modelados por competência** (§ 6);
9. **O calendário de juros não tem dez/2021 nem set/2025, e não cita o ARE 1.557.312.**
   **Transcrito como está** (§ 5). **FGTS e poupança não consolidam em dez/2021** — varredura de
   `0,4412` declarada em § 5;
10. **As séries não estão aqui.** ORTN, OTN, IPC, LBC, `LBC – 0,5%`, `LFT – 0,5%`, BTN, TRD e TR
    são dado **(B)** — contrato em `skills/indices-judiciais/`. **`UPC` não é consumida por esta
    cadeia**; é da poupança;
11. **Sem preset nomeado no corpus para esta matéria.** Entra **como cadeia, não como preset**.
    Registrado, **não inventado**.

---

## 10. Ponteiros

- `skills/calculo-judicial-atualizacao/regras/cjf.fgts.correcao-monetaria.json` — 11 segmentos, os dois
  escapes, as duas notas de expurgo e o contraste com 2.4.4.1
- `skills/calculo-judicial-atualizacao/regras/cjf.fgts.juros-mora.json` — 3 segmentos e o achado do calendário
- `skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json` — `P18-01` e o escopo da busca
  de ausência
- `docs/calculo/consolidado/02-atualizacao-detalhe.md` **§ 5.0** (a varredura item × JSON ×
  consolidado), **§ 5.3.2** (esta cadeia), **§ 5.3.4** (o que é comum à poupança) e **§ 5.3.5**
  (por que quatro JSON, e por que não as outras oito)
- `docs/calculo/consolidado/02-atualizacao.md` § 5 — a espinha, com as linhas de FGTS e poupança
- `docs/calculo/extracao/justica-federal/bloco-08-jf-detalhe.md` §§ 3.2 e 4 — `N-5` e `N-7`
- `references/poupanca.md` — a cadeia gêmea, a divergência `D8-C15` e o eixo `D8-C16`
- `references/civel-federal.md` — condenatórias em geral, **para onde as duas notas de escape
  mandam**
- `references/tributario-federal.md` — as quatro fórmulas de `aplicacao`, ECs 113/136 e os cinco
  lugares de dez/2021
- `docs/calculo/armadilhas-comparador.md` — índice dos defeitos do original
