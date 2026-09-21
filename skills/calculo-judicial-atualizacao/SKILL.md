---
name: calculo-judicial-atualizacao
description: >-
  Use quando for preciso decidir QUAL índice de correção e QUAL taxa de juros incidem sobre um
  débito judicial em cada mês, por jurisdição e por período. Gatilhos: "atualize este débito",
  "quanto vale esta condenação hoje", "qual índice vale de 2015 a 2024", "o perito aplicou o
  índice certo?", "IPCA-E ou IPCA?", "SELIC engloba juros?", "taxa legal do art. 406 do CC",
  "ADC 58", "Lei 14.905/2024", "Tema 1368 do STJ", "EC 113/2021", "EC 136/2025", "precatório",
  "juros compensatórios de desapropriação", "TR até quando", "índice da Fazenda Pública",
  "repetição de indébito", "benefício previdenciário atrasado". Cobre trabalhista, cível,
  condenatórias da Justiça Federal, desapropriação, tributário federal e previdenciário. NÃO use
  para apurar verbas nem para obter o valor mensal de um índice.
---

# Atualização monetária e juros — cadeias por jurisdição

Esta skill responde a **duas** perguntas, e só a essas duas:

```
período → indexador de correção monetária
período → taxa de juros de mora
```

É a skill que muda quando o **STF**, o **STJ**, o **TST** ou o **Congresso** mexem na regra.

---

## Quando usar / quando não usar

**Use quando** a pergunta for sobre *qual critério* atualiza um valor já apurado: escolher a
cadeia, encontrar o corte, decidir se um segmento engloba juros, conferir o critério que um
perito aplicou.

**Não use — e carregue a skill indicada:**

| Pergunta | Skill |
|---|---|
| Invariantes, aritmética decimal, truncamento, ordem das operações | `calculo-judicial-core` |
| Quanto valeu o IPCA-E de mar/2019; série mensal de qualquer índice | `indices-judiciais` |
| Apuração de horas extras, 13º, férias, RSR, INSS, IRRF | `calculo-trabalhista-liquidacao` |

**Fronteira que importa:** esta skill diz *"IPCA-E"*. **Ela não sabe quanto o IPCA-E valeu.**
O valor vem de `indices-judiciais`; a conta, de `calculo-judicial-core`.

**Interface:** o usuário escolhe **preset** (cadeia nomeada e completa). O motor compõe
segmentos. **Segmento solto nunca é exposto** — é montando bloco a bloco que se produz
combinação inválida (`README.md` desta skill).

---

## Modelo de domínio

| Termo | Significado exato |
|---|---|
| **competência** | o mês a que a parcela se refere. Unidade da apuração |
| **corte** | **data + eixo** a partir do qual muda a regra |
| **eixo de corte** | **qual fato do processo** se compara com a data do corte |
| **segmento** | `período → regra`, com `engloba`, `aplicacao` e fundamento |
| **cadeia temporal** | sequência de segmentos, sem lacuna nem sobreposição (R2) |
| **englobamento** | segmento cujo índice cobre **correção e juros** — SELIC, taxa legal |
| **`aplicacao`** | a **defasagem**: qual mês do índice se usa para qual competência |
| **regra (A)** | muda quando muda a lei ou a jurisprudência — é o que vive aqui |
| **série (B)** | muda quando o órgão publica. **Dado externo** — vive em `indices-judiciais` |

Fonte: `docs/calculo/consolidado/01-dominio-e-invariantes.md` § 1.1.

### As cadeias, por jurisdição e por qualidade do devedor

| # | Jurisdição | Devedor | Reference |
|---|---|---|---|
| 1 | Trabalhista | privado | `references/trabalhista-nacional.md` § 2 |
| 2 | Trabalhista | Fazenda Pública | `references/trabalhista-nacional.md` § 3 |
| 3 | Trabalhista | Fazenda **subsidiária** | **ramo vazio por decisão** — `P9-01` |
| 4 | Cível | qualquer | `references/civel-cc-nacional.md` |
| 5 | Federal | repetição · dívida fiscal | `references/tributario-federal.md` |
| 6 | Federal | benefício previdenciário | `references/previdenciario.md` |
| 7 | Federal | **condenatórias em geral** | `references/civel-federal.md` — correção (§ 2) e **juros autônomos** (§ 3) |
| 8 | Federal | **desapropriação** direta e indireta | `references/desapropriacao.md` — **três cadeias**: correção (§ 2), juros de mora (§ 3) e **juros compensatórios** (§ 4) |
| 9 | Federal | **FGTS** (item 4.8, critério **`JAM`**) | `references/fgts.md` — **tronco próprio**, corte por **saque integral** (`D8-C12`) e **calendário de juros próprio**. **Não é** o FGTS fiscal de 2.4.4.1 (`JCM`) |
| 10 | Federal | **caderneta de poupança** (item 4.9) | `references/poupanca.md` — só incide **se o título mandar**; corte por **data de abertura da conta** (`D8-C16`); **UPC** e **LBC** |

### A jurisdição trabalhista é NACIONAL

> **Origem declarada: EXTERNA AO CORPUS.** Vem do **enunciado do bloco 16**, que a declara
> verificada em fonte externa. Não tem lastro em arquivo deste repositório. O projeto exige que
> toda afirmação sem lastro no corpus declare a origem
> (`consolidado/07-leitura-do-corpus.md` § 6; `consolidado/08-nacional-e-regional.md` § 1).

A atualização monetária trabalhista é **nacional** desde a **Res. CSJT 8/2005**, que unificou as
**24 tabelas** dos TRTs. Hoje vale a **Res. CSJT 380/2024**, com **duas tabelas** — débitos
comuns e Fazenda Pública, esta referenciada ao **Manual do CJF**. O **PJe-Calc** é o sistema de
cálculo de toda a Justiça do Trabalho.

**Três consequências que o motor precisa honrar:**

1. **A aritmética do manual do TRT-3 NÃO é prática regional divergente.** É procedimento de uma
   região que aplica norma nacional. **Regional são os verbetes que ele invoca** — diretriz (d);
2. **A Tabela Única do CSJT é fonte nacional** e é **a dependência que torna o motor nacional**.
   Deixou de ser "integração desejável": sem ela não há correção trabalhista em **nenhum** TRT —
   diretriz (e);
3. **As cadeias `trab.hist.*` são NACIONAIS com nome enganoso.** Fundamentos declarados nos
   próprios JSON: **CC arts. 1.062–1.063**, **Lei 8.177/91 art. 39**, **Súmulas 200 e 381 do
   TST**, e a correção **delega à Tabela Única do CSJT**. O prefixo é do **arquivo de origem**,
   não da norma. **Um motor que resolva cadeia por prefixo de tribunal não acha cadeia nenhuma
   para TRT-1, TRT-2 ou TRT-15.**

**Chave de resolução regional — `(regra, tribunal, competência)`** (R24). `tribunal` só entra
onde há variante regional **cadastrada**; ausente, cai no **fallback nacional**, e isso é
resolução, não erro.

---

## Invariantes

**Não reproduzidas aqui.** Enunciado integral de **R1 a R24** em
`docs/calculo/consolidado/01-dominio-e-invariantes.md` § 2, e em `calculo-judicial-core`.

**As sete que mordem nesta skill**, e onde:

| ID | Onde morde |
|---|---|
| **R1** — exclusividade de englobamento | **SELIC e taxa legal englobam correção e juros.** Cumular com índice inflacionário é **erro material**, não escolha de critério: conta a inflação duas vezes. Vale em `trabalhista-nacional` §§ 2–3, `civel-cc-nacional`, `civel-federal`, `desapropriacao`, `tributario-federal`, `previdenciario` |
| **R2** — cobertura sem lacuna nem sobreposição | a ponta `1942-11` das cadeias históricas é **janela de análise** (`ponta_materializada`), não afirmação do manual. Em cadeia de índices **nominais**, fim e início no mesmo mês (OTN/BTN em jan/1989) **não é dupla contagem** — R-08-04, e o manual o diz expressamente |
| **R3** — classe do indexador na virada | `nominal` reflete a inflação do mês **anterior**; `percentual`, a do **próprio**; **`janela-deslocada`**, metade de cada. **Trocar de classe sem ajustar a defasagem desloca o cálculo em um mês** — e **a régua do ajuste não existe no corpus**. **A classe de cada rótulo sai de `indexadores-tipo-catalogo.json`**, nunca desta skill |
| **R4** — juros sempre simples | **com a `R4-EXCEÇÃO`**: ver abaixo |
| **R5** — piso nominal | índice negativo **entra** no cálculo, mas o piso é **por parcela**, não sobre o total |
| **R7** — termo inicial não é intercambiável | trabalhista = **ajuizamento**; cível = citação (salvo Súmulas 54, 43 e 362/STJ); repetição = **trânsito em julgado** |
| **R11** — taxa legal | **razão entre fatores**, nunca subtração de percentuais |

### `R4-EXCEÇÃO` — juros **COMPOSTOS** de 27/02/1987 a 03/03/1991

**Dentro do invariante, não em nota.** Por força do **DL 2.322/87, art. 3º**, em **três registros
independentes, duas jurisdições** (`trabalhista-nacional.md` § 4). Mecânica literal do manual:
*"1,0% ao mês, c/ taxa capitalizada. Ex.: 3 meses = 3,03%"*. **Quem ler só "juros sempre simples"
erra quatro anos de qualquer conta que atravesse o período.**

**E a mecânica sem a fronteira é função morta — o GATILHO:**

| | |
|---|---|
| **eixo** | **competência da parcela** (Passo 1, par 1) — não o ajuizamento nem o pagamento. **Não é preset**: é cadeia temporal, e o motor a liga sozinho |
| **entra / sai** | **27/02/1987** e **03/03/1991** (TRT-3) — `1987-03` e `1991-03` (CJF) |
| **onde** | `cjf.trabalhista.juros-mora` e o quadro do TRT-3 (`trabalhista-nacional.md` §§ 4 e 6). **NÃO é das condenatórias gerais** — `civel-federal.md` § 10 |
| **fora dela** | **R4 puro:** 0,5% a.m. até fev/87; **1,0% a.m. SIMPLES** desde a Lei 8.177/91, art. 39 |

> **A fronteira NÃO está harmonizada, e na virada do mês a escolha muda o número.** O **TRT-3 dá
> ao dia**; o **CJF, ao mês**. **Leve as duas, não escolha um lado**: a granularidade adotada é
> **override com justificativa** (R21), gravada na memória de cálculo (R13).

### `R11` — a taxa legal não é subtração

```
TL_m = (Fator_Selic_m / Fator_Deflator_{m-1} − 1) × 100
```

Seis decimais, **truncamento** (não half-up). Deflator: **IPCA-15** na regra geral (Res. CMN
5.171/2024); **INPC** na variante previdenciária (Manual CJF, item 4.3.2, Nota 3). A lei e o
acórdão descrevem *"SELIC deduzido o IPCA"* — **isso é descrição do efeito, não a operação**.
A subtração literal erra ~0,003 p.p./mês, e **acumula**. Piso zero por **R6** (CC art. 406, § 3º).

---

## Procedimento

### Passo 0 — a chave não é a data, é o par `(data, eixo)`

**Dezoito pontos compartilham 11/11/2017 e cortam por três eixos diferentes** — dezesseis por
competência do fato gerador, `C8-01` por **data de propositura**, `F7-06` por **modalidade do
acordo** (que não é eixo temporal). *Dois processos ajuizados no mesmo dia, com parcelas da mesma
competência, recebem respostas diferentes conforme o eixo.* Fonte:
`consolidado/00-calendario-de-cortes.md` §§ 1 e 2.

**O eixo determina qual fato do processo se compara com a data:**

| Eixo | Fato comparado |
|---|---|
| competência do fato gerador | mês da parcela |
| data de propositura / ajuizamento | ajuizamento |
| data do julgamento | o acórdão — governa o **alcance da declaração**, não o índice do mês |
| data do trânsito em julgado | trânsito |
| expedição do requisitório | data da expedição |
| **data do fato gerador** (tributo) | fato gerador |
| **recolhimento indevido** | data do recolhimento |
| modalidade · natureza · ente devedor | **não temporal** — atributo do caso |

### Passo 1 — resolver os pares que governam esta skill

**Dezesseis pares**, e o eixo está na coluna 2. Detalhe segmento a segmento nos `references/`.

| # | Data | **Eixo** | O que muda | Onde |
|---|---|---|---|---|
| 1 | **27/02/1987** e **03/03/1991** | competência da parcela | entra e sai a capitalização **composta** — `R4-EXCEÇÃO` | trab. nacional §§ 4 e 6; `tributario-federal` § 5.1 |
| 2 | **04/03/1991** | competência da parcela | Lei 8.177/91 art. 39 — 1,0% a.m. simples; e a **TR** passa a existir | trab. nacional §§ 2.2, 4 |
| 3 | **nov/2005** | competência da parcela | tabela própria do TRT-3 → **Tabela Única do CSJT** (Res. 8/2005) | trab. nacional § 5; regional-trt3 `R15` |
| 4 | **27/08/2001** | competência da parcela | Fazenda trabalhista: 0,5% a.m. **limitado a 6% a.a.** (MP 2.180-35) | trab. nacional § 3.2 |
| 5 | **ago/2001** | competência ⊕ **devedor** | `cjf.trabalhista.juros-mora` **bifurca e nunca reconverge** | trab. nacional § 6 |
| 6 | **29/06/2009** | competência da parcela | Lei 11.960/09 — poupança, sem cumulação | trab. nacional § 3.2 |
| 7 | **jul/2009** | competência ⊕ **devedor** | `cjf.condenatorias-gerais.juros-mora` bifurca | `civel-federal` § 3 |
| 8 | **04/05/2012** | competência da parcela | **qualificação** do segmento da poupança, **não segmento novo** — muda a fórmula, não a regra | trab. nacional § 3.2 |
| 9 | **jan/2003** | competência da parcela | cível: tabela CGJ/TJMG → **SELIC** | `civel-cc-nacional` § 2 |
| 10 | **18/12/2020** | **data do julgamento** | ADC 58/59, ADI 5867/6021 — governa o **alcance da declaração** | trab. nacional § 2.3 |
| 11 | **18/12/2020** | **competência da parcela** | governa **qual índice** se aplica a cada mês — cai a TR | trab. nacional §§ 2.1–2.2 |
| 12 | **dez/2021** (EC promulgada em 09/12/2021) | competência da parcela | **EC 113/2021**: SELIC única, *"independentemente de sua natureza"* | trab. nacional § 3.1; `tributario-federal` § 6 |
| 13 | **30/08/2024** | fase do débito ⊕ mês de atualização — **eixo NÃO nomeado pelo consolidado** | Lei 14.905/2024: IPCA + **taxa legal** | trab. nacional § 2.1; `civel-cc-nacional` § 2 |
| 14 | **09/09/2025** | **três eixos simultâneos** — objeto ⊕ ente ⊕ período | **EC 136/2025** reescreve o art. 3º da EC 113 | `tributario-federal` § 6 |
| 15 | **múltiplos** | **expedição do requisitório ⊕ ente devedor** | `C14-02` — precatório | `tributario-federal` § 7 |
| 16 | **jan/1997 · abr/1995** | **data do fato gerador** | dívida fiscal: Ufir → SELIC | `tributario-federal` § 3 |

**Sobre o par 13, afirmação de ausência com escopo declarado:** varredura de `eixo` em
`consolidado/02-atualizacao.md` e `02-atualizacao-detalhe.md` — **7 ocorrências, nenhuma sobre
30/08/2024**; varredura de `29/08/2024`, `30/08/2024`, `14.905` e `14905` nos 11 arquivos do
consolidado — **8 ocorrências, todas em quadro de fase, nenhuma nomeando eixo**. O eixo do par
13 é, portanto, **inferido da forma do quadro**, não declarado. Marcar `eixo_inferido: true`.

### Passo 2 — bifurcação entra com AS DUAS versões

```
BIFURCADO  →  as duas versões entram, com fronteira declarada.
              NUNCA substituir a antiga pela nova.
              Competência anterior ao corte USA A ANTIGA.
```

**O `status_norma: "superado"` gravado nos JSON `trab.hist.*` está certo quanto ao futuro e
incompleto quanto ao passado.** Ler como **fronteira superior do segmento**, jamais como
invalidade. Não apagar, não substituir. `consolidado/02-atualizacao.md` § 9.

**Onze bifurcações entram nesta skill com as duas versões:** `CH-01` a `CH-05` (cadeias
históricas trabalhistas), `AM-03` (bifurca **por segmento**, não por data), `C14-02`
(precatório), a bifurcação por devedor de dez/2021 nas condenatórias gerais do CJF (que
**reconverge** em set/2025), a de jul/2009 nos juros das condenatórias, a de ago/2001 nos juros
trabalhistas do CJF (que **nunca** reconverge) e a bifurcação temporal da tabela CGJ/TJMG
(`R10`, com ressalva de título).

**`R-08-08` — a bifurcação por devedor não é universal:** três cadeias do CJF **nunca** bifurcam
— previdenciário, repetição de indébito e desapropriação direta.

### Passo 3 — checar englobamento antes de somar (R1)

Se o segmento é **SELIC** ou **taxa legal**, ele **engloba correção e juros**. Não existe
"correção + SELIC". Não existe "taxa legal + IPCA". Rejeitar na composição.

### Passo 4 — checar a defasagem (R3 e `aplicacao`)

**Trabalhista — quatro réguas no mesmo cálculo**, três de correção e uma de juros:

| # | Régua | Granularidade | Regra |
|---|---|---|---|
| 1 | **Súmula 381/TST** | um mês | índice do mês **seguinte** ao da prestação |
| 2 | tabela diária do CSJT | um dia | TR acumulada **até o dia anterior** ao final informado |
| 3 | pro-ratização | **dias úteis** | índice mensal decomposto por dias úteis |
| 4 | **juros** | **mês comercial de 30 dias** | 1% a.m. ou `1/30` ao dia, contagem **inclusiva** |

> Correção pro-ratizada por **dias úteis** e juros por **dias corridos/30** no mesmo cálculo é
> **atrito real do manual**. Registrado, **não harmonizado**.

**Justiça Federal — quatro fórmulas de `aplicacao`, e D1 ≠ D2 sobre a mesma série:** **D1**
(Selic no mês posterior ao de competência, **inclusive no mês de pagamento** — Fazenda desde
dez/2021; a **taxa legal segue D1**); **D2** (do mês seguinte ao termo inicial até o mês anterior
ao pagamento, **e 1% no mês do pagamento**); **D3** (eixo no **recolhimento indevido**); **D4**
(competência da parcela — dívida fiscal).

### Passo 5 — registrar (R19, R13, R20, R21)

Toda conta que atravesse um corte grava **qual lado aplicou a cada competência**. Default marca
a conta (`origem: "default"`); divergir do default **exige justificativa**, sob pena de
`ErroDeDados` (R21). Precedência **R8: título > escolha > default** — com a **única exceção**
registrada (`R-08-01`, NOTA 2): mudança **superveniente de legislação sobre o indexador** passa
por cima do título.

---

## Catálogo de critérios

Presets — cadeias nomeadas e completas. Fonte: `docs/calculo/01-plano-extracao.md` § "Catálogo
de critérios".

| Preset | Quando | Reference |
|---|---|---|
| `TRAB-ADC58-LEI14905` | devedor privado — **default** | `trabalhista-nacional.md` § 2 |
| `TRAB-ADC58-SEM-TRD` | variante doutrinária, sem juros TRD na fase pré-judicial | `trabalhista-nacional.md` § 2.1 |
| `TRAB-FAZENDA` | devedor Fazenda Pública | `trabalhista-nacional.md` § 3 |
| `TRAB-TITULO` | título fixa critério próprio — override total, com registro (R8) | — |
| `CIVEL-CC-TEMA1368` | regra geral — **default** | `civel-cc-nacional.md` |
| `CIVEL-MG-TITULO-CGJ` | título fixou a tabela da CGJ/TJMG | `civel-regional-tjmg.md` |
| `CIVEL-DANO-MORAL` | correção do **arbitramento** (Súmula 362/STJ) | `civel-cc-nacional.md` § 3 |
| `CIVEL-ATO-ILICITO` | correção do efetivo prejuízo (Súmula 43); juros do evento danoso se extracontratual (Súmula 54) | `civel-cc-nacional.md` § 3 |
| `TRIB-FED-REPETICAO` | repetição de indébito | `tributario-federal.md` § 2 |
| `TRIB-FED-DIVIDA-ATIVA` | empresa como devedora | `tributario-federal.md` § 3 |

**Sem preset nomeado no corpus, e por isso listados como cadeia e não como preset:**
previdenciário do CJF (`previdenciario.md`), **condenatórias em geral** do CJF
(`civel-federal.md`) e **desapropriação direta/indireta** (`desapropriacao.md`).

**Presets de regime temporal são outra família** e não pertencem a este catálogo — respondem
*"qual regra de apuração vale"*, não *"como se atualiza"*. `docs/calculo/presets-regime.md` § 1.
O único que toca esta skill é **`pr.adc58-item-i`** (ver "Armadilhas").

---

## Armadilhas conhecidas

**1 — `R1`: cumular SELIC ou taxa legal com índice inflacionário.** Erro material, não escolha.
Foi observado em código de produção: `CalculosService.cs` do SaaS soma juros à base
(`pendencias.md` § 4, itens a–d). Quatro invariantes violadas no mesmo trecho.

**2 — `R11`: implementar a taxa legal por subtração.** `selic − ipca` é o erro que a base
antecipa. E o deflator é o do mês **`m−1`**, não o corrente.

**3 — `R4-EXCEÇÃO`: quatro anos de juros compostos.** 27/02/1987 a 03/03/1991.

**4 — `R3`: trocar de classe de indexador sem ajustar a defasagem.** Desloca **um mês**. São
**cinco** classes, não duas, e `tipo` é campo que **não pode faltar** no catálogo de índices.
**E a régua do ajuste é lacuna declarada** — não se inventa uma.

**5 — IPCA-**E** × IPCA.** IPCA-**E** na fase pré-judicial trabalhista; **IPCA (sem E)** a partir
de 30/08/2024. A distinção é do dispositivo do acórdão. **Fontes secundárias escrevem IPCA nos
dois lugares — estão erradas.**

**6 — `R7`: marco inicial dos juros trabalhistas é o AJUIZAMENTO**, não a citação (CLT art. 883;
Súmula 200/TST), **salvo parcelas vincendas**, que seguem a época própria.

**7 — a EC 113/2021 NÃO era "só federal".** A redação original diz *"independentemente de sua
natureza"*. **A restrição a requisitórios federais é criação da EC 136/2025.** Refutação
registrada, e a fonte do erro é **interna**: `bloco-13c-sindical-precatorios.md` § 7. Não repetir.

**8 — os juros compensatórios da desapropriação são CADEIA AUTÔNOMA**, além da correção e dos
juros de mora. **O corte de ago./2017 não aparece em tabela nenhuma** — vive só no item 4.5.4,
sobre TDAs complementares. Quem tratar a desapropriação só pela linha de correção monetária
**perde a cadeia inteira**. `references/desapropriacao.md` § 4; `02-atualizacao-detalhe.md`
§ 5.3.1.

**9 — `A5`, defeito do original:** índice de dez/10 (`pagina_pdf` 96) **quebra a monotonicidade**
da série. **O erro está no índice publicado; o valor está certo** — o inverso do caso usual.

**10 — `DEFEITO_DO_ORIGINAL` das moedas:** em `trab.hist.moedas-e-paridades`, a primeira linha
termina em **12/02/70** e a segunda começa em **13/02/67** — três anos de sobreposição. Quase
certamente era 12/02/67. **Registrado, não corrigido.**

**11 — `pr.adc58-item-i`:** a ressalva de valores pagos do item "i" **não é incondicional**.
Duas situações — i.1 pagamento consolidado (regra) × i.2 execução questionada (exceção). **Em i.1
o rateio sequer é consultado**: o pago sai da conta. Default: **i.1**.

**12 — tolerância do comparador.** Diferenças de **0,01 a 0,03** entre recalculado e impresso são
esperadas: a aritmética do manual roda em **precisão plena** e os impressos com duas casas **não
são os operandos**. **O limiar de alarme não deve ser o centavo.**

Índice completo dos defeitos: `docs/calculo/armadilhas-comparador.md`.

---

## Fixtures de aceite — **NÍVEL 2: exigem série**

Do Manual CJF (Res. 990/2026, item 4.2.1.1, Nota 6). Fonte: `00-base-normativa.md` § 8. **São
NÍVEL 2 — aceite do SISTEMA, não desta skill: exigem série de índices.** Ver Limitações, item 8.

| # | Caso | Esperado |
|---|---|---|
| **1** | Fazenda Pública, data-base **jun/2022**. Parcelas 01/2020, 02/2020 e 02/2022 de R$ 1.000,00; citação 01/2021 | **R$ 3.484,95** — principal corrigido 3.275,96; juros até 12/2021 55,75; juros SELIC 153,24 |
| **2** | mesmo caso, data-base **jun/2026** | **R$ 5.218,28** — principal 3.412,64; juros 1.805,64 |
| **3** | **não** Fazenda, data-base jun/2026. Parcelas 01/2002 e 08/2024 de R$ 1.000,00; citação 01/2005 | **R$ 5.772,95** — principal 2.554,45; juros 3.218,50 |
| **4** | precatório complementar (item 5.2.1): principal 20.000,00 + juros 3.000,00 em jan/2016, honorários 10%, INPC; pagamento ago/2018 dentro do prazo, precatório apresentado 01/07/2017; atualização até mai/2020 | **R$ 4.435,07** resumido · **R$ 4.435,04** detalhado |

**A divergência de centavos é parte do teste.** Fixture 2: R$ 0,01; fixture 4: R$ 0,03 — **o melhor
teste de arredondamento do conjunto**. **Um motor que zera essas diferenças está arredondando
errado — e para produzir DOIS números tem de implementar DOIS procedimentos**, passo a passo, com
casas e ponto de truncamento, em `references/metodos-resumido-e-detalhado.md`. **O default é o
resumido** (5.2.1). Divergem na **correção do bloco de juros acumulado** (fixt. 2) e na
**subtração do pagamento** (fixt. 4). **`R12` vale nos dois itens: truncamento** (`D8-D33`).

**Verificação numérica embutida na cadeia da Fazenda trabalhista** (`pagina_pdf` 92): a série (B)
de jun/12 a ago/13 soma **6,5760%**; o atalho do manual é `15 × 0,5% = 7,5%`, com diferença de
`0,9240%`. **Conferido em `Decimal`: fecha exato.**

**`D8-D32`, conferido a 250 dpi:** a `pagina_pdf` 52 **imprime** `R$ 5.218,2` — **defeito do
original**, não da extração. O 5.218,27 é derivado, e o detalhado o produz. `pendencias.md` § 6.

---

## Limitações declaradas

**Não é rodapé. É o que impede usar a skill fora do que ela sustenta.**

1. **A cobertura de súmulas regionais é de TRT-3, TRT-4 e TJMG — e só esses três.** São **15 regras regionais
   catalogadas** (9 verbetes + 6 fontes não-verbete), de **três** tribunais: TRT-3, TRT-4 e TJMG.
   **Outras regiões exigem cadastro de súmulas, não refatoração** — a chave
   `(regra, tribunal, competência)` já existe e o fallback nacional está identificado para 14 das
   15. **Silêncio do tribunal não é adesão ao verbete de outro tribunal** (R24).

2. **A cadeia trabalhista anterior a 03/1991 depende da Tabela Única do CSJT, ainda não
   integrada — `P9-02`.** O capítulo 7 do manual **não tem mapa período → indexador de correção**,
   e diz por quê: *"A tabela mensal de correção está escalonada em meses e anos, já computa as
   conversões e paridades da moeda nacional e não contém juros."* O segmento `1942-11 .. 1991-02`
   tem `indexador: "NAO-DECLARADO-PELO-MANUAL"`, **não "TR"**. **A ponte para o tronco do CJF não
   é inferida** — o corpus não faz a remissão. É a **única** das 15 regras regionais sem fallback
   nacional (`R15`), e **bloqueia o motor trabalhista** (base § 9, pendência 2).

3. **Pontos que repousam em fonte secundária, e o mais grave deles:**
   - **a modulação da ADC 58, item "i", NÃO tem transcrição literal verificada em fonte
     primária.** `portal.stf.jus.br` respondeu **HTTP 403 em 100% das tentativas**. O
     desdobramento i.1 × i.2 vem de `00-base-normativa.md` § 1.1, que **ele próprio declara**
     origem secundária, e **o inteiro teor dos três precedentes do TST não foi lido**. Confirmar
     antes de produção: a distinção decide se o critério do STF alcança valores já pagos;
   - a **premissa da nacionalidade trabalhista** (Res. CSJT 8/2005 e 380/2024, PJe-Calc) é
     **externa ao corpus**, do enunciado do bloco 16, **não conferida nesta fase**;
   - a **regra de incidência assimétrica** do Prov. CNJ 207/2025 **não decorre da leitura da
     emenda** — é especificação de implementação;
   - a **TR** foi `percentual` por **inferência declarada**, e o bloco 17 a rebaixou: hoje é
     **`indeterminado` com razão registrada** (bloco 19). **Nenhum dos dois manuais a classifica.**

4. **`pr.intertemporal` tem default, e a ultratividade continua disponível.** O **Tema 23 do TST**
   (IRR, Pleno, 25/11/2024, 15 × 10, transitado, **modulação negada por unanimidade**) fixou
   *tempus regit actum*, eixo na competência do fato gerador. A **ultratividade** é **posição
   vencida**, mas permanece aplicável **mediante justificativa** (**R21**) ou a título que a tenha
   adotado expressamente (**R8**). Não é opção apagada — é opção que custa justificativa.

5. **Pendências abertas que esta skill não resolve** — viram limitação, nunca regra:
   | ID | O que está aberto |
   |---|---|
   | `P9-01` | juros da Fazenda **subsidiária** — *"grande parte da jurisprudência entende"* é **corrente, não regra**. Ramo declarado e **deliberadamente vazio**. Um motor que aplique 0,5% a.m. ali erra por leitura de condição não qualificada |
   | `P9-03` | termo inicial de juros em processos vindos da Justiça Estadual ou Federal |
   | `P9-04` | termo inicial e índice **por tipo de verba** — Súmula 439/TST, Súmula 15/TRT-3, OJs 181, 198 e 302 |
   | `P9-05` | juros **vincendos** — método, não mapa. Fora do escopo dirigido |
   | `P8-09` | **dez/2021 dos juros compensatórios fica sem regime coerente** — o texto de 4.5.3 diz "Até dez. 2021" e a tabela encerra em nov./2021 |
   | base 3 | **efeito da EC 136/2025 na Justiça do Trabalho** — TST e CSJT **não consolidaram**. Não se estende a cadeia do CJF por analogia |
   | base 4 | **ADI 7873** pendente |
   | — | **Fazenda estadual e municipal pós-EC 136/2025**: sem a regra antiga (revogada) e sem a nova (que não a alcança). **Lacuna normativa, não de pesquisa** |
   | — | **classificação da devedora como Fazenda Pública** é **determinação jurídica do usuário do módulo**, não matéria de cálculo. O manual se contradiz: cap. 8 isenta quem *"não explore atividade econômica"*; cap. 14, a administração *"direta e indireta"*, **sem a ressalva**. Se a resposta for negativa, **somem** o ramo FP das três jurisdições, precatório, ECs 113/136 e a consolidação de dez/2021 |

6. **Divergências registradas e NÃO harmonizadas** — as duas correntes entram, com fundamento:
   juros pela **TRD na fase pré-judicial** (variante `TRAB-ADC58-SEM-TRD`, não default); **juros na
   falência** (três ementas do TRT-3, **duas divergentes entre si**); **TJ-SP** mantendo a SELIC
   fora da fase de precatório contra a Res. CJF 990/2026 e o STJ.

7. **Limitações da própria DIVISÃO em arquivos — e as lacunas que a varredura achou e não
   preencheu — não se repetem aqui:** estão em
   [`references/README.md`](references/README.md), seções *"Limitação da própria divisão"*, *"O que
   a varredura do bloco 17 encontrou, e NÃO foi criado"* e *"O que o bloco 18 fechou"*, com o
   **escopo contado** de cada busca negativa. Ali ficam, uma a uma, **`N-5`/`D8-C13`** (expurgos do
   FGTS: substituem ou acrescem?), **`P18-01`**, **`P18-02`**, **`P19-02`** e as **duas `R3`
   cheias** da poupança. **Nenhuma virou regra; todas seguem abertas.**

8. **As fixtures do CJF só são executáveis com a SÉRIE de índices carregada — são NÍVEL 2.**
   A fixture 1 sozinha consome **23 meses de IPCA-E**. A série é **dependência externa, e esta
   skill não a carrega por desenho** — o contrato está em `skills/indices-judiciais/`. **O aceite
   DESTA skill é o NÍVEL 1** — invariantes e aritmética —, executável em
   `scripts/calculo/test_aceite_nivel1.py`. Os dois níveis: `aceite-em-dois-niveis.md`.

---

## Ponteiros

| Assunto | Onde |
|---|---|
| **Espinha da atualização** | `docs/calculo/consolidado/02-atualizacao.md` |
| **Detalhe** — CJF segmento a segmento, `aplicacao`, consolidação de dez/2021, compensatórios | `docs/calculo/consolidado/02-atualizacao-detalhe.md` |
| **Os pares `(data, eixo)`** | `docs/calculo/consolidado/00-calendario-de-cortes.md` |
| **R1–R24, íntegra** | `docs/calculo/consolidado/01-dominio-e-invariantes.md` |
| **Nacional × regional**, as 15 regras regionais e os fallbacks | `docs/calculo/consolidado/08-nacional-e-regional.md` |
| **Vereditos** — F7-04, C14-01/02/03, CH-01..05, AM-01, AM-03, JR-05 | `docs/calculo/confronto-normativo/01-vereditos.md` |
| **Defeitos do original** | `docs/calculo/armadilhas-comparador.md` |
| **Pendências** | `docs/calculo/pendencias.md` |
| **Presets de regime temporal** (outra família) | `docs/calculo/presets-regime.md` |
| **Cadeias em schema** | `docs/calculo/tabelas-normativas/cjf.*.json`, `trab.hist.*.json` |
| **Séries mensais** (contrato) | `skills/indices-judiciais/` |
| **Invariantes e aritmética** | `skills/calculo-judicial-core/` |

**`references/` — carregue apenas o arquivo da jurisdição em questão:**

```
trabalhista-nacional.md        cadeia nacional, Tabela Única CSJT, R4-EXCEÇÃO, as quatro réguas
trabalhista-regional-trt3.md   os verbetes regionais que o manual invoca, e o fallback nacional
civel-cc-nacional.md           Tema 1368, Lei 14.905, taxa legal, termos iniciais
civel-regional-tjmg.md         tabela CGJ/TJMG, histórico pré-2003, as três hipóteses de sobrevida
civel-federal.md               condenatórias em geral do CJF: correção + juros autônomos, D1/D2
desapropriacao.md              as TRÊS cadeias: correção, juros de mora e juros compensatórios
fgts.md                        critério JAM, corte por SAQUE INTEGRAL, expurgos (N-5, aberta)
poupanca.md                    corte por ABERTURA DA CONTA, UPC e LBC, as duas R3 do manual
tributario-federal.md          repetição, dívida fiscal, aplicacao, ECs 113/136, precatório
previdenciario.md              INPC, e a taxa legal com deflator INPC
metodos-resumido-e-detalhado.md   transversal: é O PROCEDIMENTO dos dois métodos. Carregue
                               para IMPLEMENTAR, e para as fixtures 2 e 4
```

> **FGTS e poupança têm CALENDÁRIO DE JUROS PRÓPRIO:** vão de Selic **direto à taxa legal em
> set/2024**, **sem corte de dez/2021 nem de set/2025** e **sem citar o ARE 1.557.312**. **Quem
> aplicar nelas o calendário das condenatórias gerais erra.** Elas também **não estão** entre os
> cinco lugares que consolidam em dez/2021, e **usam a fórmula `D4`** — que o bloco 8 dava só à
> dívida fiscal. `02-atualizacao-detalhe.md` § 5.3.4.

> **Um arquivo por cadeia, não por capítulo do manual.** `civel-federal.md` e `desapropriacao.md`
> nasceram no bloco 17 porque **condenatórias em geral e desapropriação têm cadeia própria** e
> estavam hospedadas em `tributario-federal.md` por falta de lugar, não por classificação.
> **Índice completo, com o que a varredura achou e não foi criado:** `references/README.md`.

> **A separação nacional/regional nos nomes não é estética.** É o que permite **cadastrar outra
> região sem tocar no motor**: o arquivo regional é entrada de catálogo; o nacional é o default.
