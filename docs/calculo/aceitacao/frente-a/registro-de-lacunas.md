# Registro de lacunas — frente A

**Agente implementador, teste de aceitação.** Escopo de leitura autorizado: as quatro
`skills/**/SKILL.md`, tudo que elas apontam, e `tests/fixtures/calculo/`.

**Arquivos efetivamente abertos** (escopo declarado, para todas as buscas negativas abaixo):

```
skills/calculo-judicial-core/SKILL.md
skills/calculo-judicial-atualizacao/SKILL.md
skills/calculo-judicial-atualizacao/references/civel-federal.md
skills/calculo-judicial-atualizacao/references/tributario-federal.md  (§§ 7 e 8)
skills/indices-judiciais/SKILL.md
docs/calculo/00-base-normativa.md  (§§ 4, 5 e 8 — ponteiro declarado das skills)
docs/calculo/tabelas-normativas/  (listagem completa; conteúdo de
    cjf.condenatorias-gerais.correcao-monetaria.json e .juros-mora.json)
tests/fixtures/calculo/  (README + as 4 fixtures)
```

**Não abri** (e digo por quê, porque a omissão também é dado):

- `docs/calculo/consolidado/09-ordem-de-calculo.md` — é **ponteiro declarado** do core
  ("A ordem ponta a ponta — dezenove passos — está em ..."), logo eu **podia** abrir.
  Optei pelo "mínimo operacional" de 5 passos que a própria skill imprime, porque as
  fixtures travaram antes na camada (B) e a ordem não desbloquearia nada. **É escolha
  minha, não impedimento.**
- `skills/calculo-trabalhista-liquidacao/` — nenhuma das quatro fixtures é trabalhista.
- os CSV de `docs/calculo/extracao/trabalhista/` — **proibidos pelo enunciado** e, além
  disso, a própria skill `indices-judiciais` diz que eles abrem com
  `# OUT_OF_SCOPE — série de valores, não entra na skill` e existem "como evidência de
  conferência, **não como fonte de consulta**". Não os usei nem indiretamente.

---

## 1. Lacunas, em ordem de encontro

### #1 — Nenhuma série de índices existe no escopo lido. **Bloqueia as quatro fixtures.**

| Campo | |
|---|---|
| **onde** | Montar o coeficiente de correção monetária de qualquer parcela de qualquer fixture |
| **o que faltou** | O **valor mensal** de todo indexador que as quatro fixtures exigem: **IPCA-E/IBGE de 2001-01 a 2021-11** (fixtures 1, 2 e 3), **SELIC mensal de 2021-12 a 2025-08** (1, 2, 3), **IPCA-15/IBGE de 2024-09 a 2026-06** (2 e 3), **taxa legal mensal de 2024-09 a 2026-06** (2 e 3), **INPC de 2016-01 a 2017-06 e de 2019-01 a 2020-05** (4), **IPCA-E de 2017-07 a 2018-12** (4). Primeiro ponto exato em que travou: **IPCA-E/IBGE de 2020-01** |
| **onde procurou** | os sete caminhos listados no topo. `skills/indices-judiciais/SKILL.md` responde à pergunta de forma **explícita e afirmativa**: *"E esta skill **não carrega série** — é o ponto inteiro dela: descreve o **contrato**, não o dado."* `references/civel-federal.md` § 11, item 8: *"**As séries não estão aqui.** ORTN, OTN, BTN, Ufir, INPC, IPCA série especial, IPCA-E, IPCA-15 e Selic são dado **(B)**"*. Os 33 JSON de `tabelas-normativas/` são **cadeias e catálogos**, nenhum é série de valores |
| **o que fez** | Implementei `series.py` como provedor que **levanta `SerieAusente`** com a competência e o escopo de busca. **Não interpolei, não estimei, não busquei na web.** O runner reporta a fixture como `BLOQUEADA`, não como falha |
| **bloqueia?** | **IMPOSSÍVEL** nas quatro. Não é imprecisão: sem (B) não há número algum |

> Isto não é defeito das skills: elas **declaram** a fronteira (A)×(B) e dizem, com todas as
> letras, que (B) é dado externo a integrar. **O motor está do lado (A) e (A) está completo.
> O que falta é o dado, e as skills dizem que falta.**

---

### #2 — Os três valores literais que as skills publicam não cobrem sequer um mês de cálculo

| Campo | |
|---|---|
| **onde** | Tentar preencher o mínimo de `series.py` com o que houvesse de literal |
| **o que faltou** | As skills publicam exatamente **cinco** valores de índice: IPCA-E nov/2021 = 1,17%; INPC nov/2021 = 0,84%; TR nov/2021 = 0,00%; SELIC ago/2025 = 1,16%; taxa legal set/2025 = 1,305984%. Mais os juros de dez/2021 = 0,4412% e a menção a *"5,05% de Selic"* nas duas linhas de dez/2021 do exemplo da `pagina_pdf` 51. **Nenhum outro mês.** A fixture 1 precisa de 23 meses de IPCA-E e de 12 meses de juros de poupança |
| **onde procurou** | `civel-federal.md` §§ 3, 7 e 8; `tributario-federal.md` § 8; `indices-judiciais/SKILL.md` §§ R11 e "Fixtures de aceite"; `00-base-normativa.md` § 4 |
| **o que fez** | Carreguei **só esses cinco**, cada um com a fonte textual ao lado (`series.VALORES_LITERAIS`) |
| **bloqueia?** | **IMPOSSÍVEL** — cinco pontos isolados não fazem cadeia |

---

### #3 — A ordem de operações **dentro** da consolidação de dez/2021 não é enunciada

| Campo | |
|---|---|
| **onde** | `motor.consolidar_dez_2021`, fixtures 1 e 2 |
| **o que faltou** | A NOTA 5 do item 4.2.1 diz *"o crédito será consolidado ... considerando, para esse fim, o IPCA-E de nov./2021 (1,17%) e os juros de dez./2021 (0,4412%)"*. **Não diz** (a) se os 0,4412% incidem sobre o principal **já corrigido por 1,17%** ou sobre o principal anterior; (b) se o 1,17% de nov/2021 é aplicado **em nov ou em dez** (é `aplicacao`, não taxa); (c) se os 0,4412% **somam** ao percentual acumulado de juros ou incidem à parte |
| **onde procurou** | `civel-federal.md` § 7 (transcrição literal da NOTA 5), `tributario-federal.md` § 8 (a mesma nota, repetida com o quadro dos cinco ramos), `calculo-judicial-core/SKILL.md`, a `observacao` da fixture 01 |
| **o que fez** | Implementei a leitura literal da alínea (a) — corrige o principal por 1,17% e trata 0,4412% como mais um mês do percentual acumulado de juros — e **marquei no docstring que isso é COMPOSIÇÃO, não citação**. A função nunca chegou a executar: a lacuna #1 trava antes |
| **bloqueia?** | **impreciso** (se a série existisse, o número poderia sair errado por aqui) |

---

### #4 — Fazenda, juros de 2012-05 a 2021-11: a regra é resolúvel, o **dado** não

| Campo | |
|---|---|
| **onde** | Fixtures 1 e 2, juros de 01/2021 (citação) a 11/2021 |
| **o que faltou** | O segmento diz *"poupança: 0,5% ao mês se a Selic **anual** > 8,5%; 70% da Selic ao ano, **mensalizada**, nos demais casos"*. Faltam (a) a **série da Selic anual** mês a mês de 2021, e (b) o que **"mensalizada"** significa aritmeticamente — divisão por 12? raiz duodécima? A skill não define, e `R4` (juros simples) sugere divisão, mas **sugerir não é dizer** |
| **onde procurou** | `civel-federal.md` § 3 e NOTA 4; `cjf.condenatorias-gerais.juros-mora.json` segmento `2012-05..2021-11`; `00-base-normativa.md` § 6 |
| **o que fez** | **Parei.** Não implementei "mensalizada" |
| **bloqueia?** | **IMPOSSÍVEL** nas fixtures 1 e 2 mesmo que a série aparecesse, enquanto "mensalizada" não for definida |

---

### #5 — Fazenda, `aplicacao` dos juros entre jul/2009 e nov/2021: **nem D1 nem D2 é declarado**

| Campo | |
|---|---|
| **onde** | Escolher qual fórmula de defasagem rege os juros da fixture 1 antes de dez/2021 |
| **o que faltou** | `civel-federal.md` § 5 declara **D1** para "Fazenda, **a partir de dez/2021**" e **D2** para "não-Fazenda; **e Fazenda de jan/2003 a jun/2009**". A janela **Fazenda de jul/2009 a nov/2021 fica sem fórmula atribuída**. A fixture 1 cai exatamente nela (citação 01/2021) |
| **onde procurou** | `civel-federal.md` § 5 inteira (tabela D1/D2 + NOTA 4 literal + NOTA 7), `tributario-federal.md` § 4 ("as quatro fórmulas de `aplicacao`" — o índice de seções foi lido; D3 e D4 são declaradamente de outras cadeias), `calculo-judicial-atualizacao/SKILL.md` Passo 4 |
| **o que fez** | **Parei e registrei.** Não estendi D1 nem D2 por analogia. Implementei as duas funções (`d1_competencias`, `d2_competencias`) sem escolher qual se aplica ali |
| **bloqueia?** | **impreciso** — mas num ponto que muda o número (`R-08-09`: *"a mesma Selic, dois números"*) |

---

### #6 — Fixtures 2 e 4: **"método resumido" e "método detalhado" nunca são definidos**

| Campo | |
|---|---|
| **onde** | Produzir a divergência de **R$ 0,01** (fixture 2) e de **R$ 0,03** (fixture 4), que as duas fixturas declaram ser **asserção do teste** |
| **o que faltou** | **O procedimento de cada um dos dois métodos.** As skills dizem que eles existem, que devem convergir, que divergem por truncamento e que *"um motor que zera essas diferenças está arredondando errado"* — e **nunca dizem o que cada método faz**. Único fragmento: a `observacao` da fixture 4 menciona *"a regra do item 5.2.1.1 de que o **resumido não aplica juros sobre juros**"*. Isso é **uma** diferença, não um método |
| **onde procurou** | `calculo-judicial-core/SKILL.md` "Fixtures de aceite"; `calculo-judicial-atualizacao/SKILL.md` "Fixtures de aceite"; `civel-federal.md` § 8; `tests/fixtures/calculo/README.md`; `00-base-normativa.md` § 8; as `observacao` das quatro fixtures |
| **o que fez** | **Não implementei nenhum dos dois métodos.** Registrei. O runner **imprime a tolerância e avisa que a divergência é asserção**, e não tenta convergi-la |
| **bloqueia?** | **IMPOSSÍVEL** nas fixtures 2 e 4 **independentemente da lacuna #1**. Mesmo com todas as séries do mundo eu produziria *um* número, não *dois* — e a asserção dessas duas fixtures é sobre **o par** |

> Esta é, na minha leitura, a lacuna mais cara do conjunto: ela não é de dado externo, é de
> **procedimento**, e é exatamente o que as skills dizem ser "o melhor teste de arredondamento
> do conjunto".

---

### #7 — Fixture 4: `pr.imputacao` **não tem default**, e a fixture exige imputação

| Campo | |
|---|---|
| **onde** | Abater o pagamento de ago/2018 (principal 21.000,00 + juros 3.150,00) no passo 2 do método detalhado |
| **o que faltou** | **Nada — e é esse o ponto.** A skill é explícita: `pr.imputacao` é preset **sem default** (`R20-EXCEÇÃO`), *"escolher seria o motor tomar posição jurídica"*, `art. 354` tem *"zero ocorrências em 471 páginas"*. A fixture 4 **não informa** qual imputação usar (`invariantes_exercidas` cita `R10`, e as entradas não trazem preset) |
| **onde procurou** | `calculo-judicial-core/SKILL.md` R10, R20-EXCEÇÃO, "Limitações declaradas"; as `entradas` da fixture 4 |
| **o que fez** | `motor.imputar` **recusa** com `ErroDeDados` quando o preset não é informado — e isso é **autotestado** no runner. **Não arbitrei** |
| **bloqueia?** | **IMPOSSÍVEL** na fixture 4 sem que alguém informe o preset. É bloqueio **por decisão da skill**, não por falta dela |

---

### #8 — Fixture 4: os juros do precatório dependem de série **e** de definição

| Campo | |
|---|---|
| **onde** | `cadeia_juros` da fixture 4, fases "percentual devido" |
| **o que faltou** | O critério literal da fixture é *"mesmo percentual da caderneta de poupança ... 0,5% ao mês se a Selic anual > 8,5%; senão 70% da Selic anual, **mensalizada**"* — **a mesma lacuna #4**, agora de 2016 a 2020; e o que significa **"percentual devido"** como regra de juros nas fases 1 e 3 |
| **onde procurou** | fixture 4 `entradas`; `tributario-federal.md` § 7 (as quatro regras estruturais que sobrevivem: suspensão dos juros no prazo constitucional, 0,5% a.m. desde ago/2001, exclusão de compensatórios, exceção à precedência do título) |
| **o que fez** | Parei. Registrei que § 7 diz **"juros de 0,5% a.m. desde ago/2001"**, o que **conflita** com o critério poupança transcrito na fixture — e **não escolhi entre os dois** |
| **bloqueia?** | **IMPOSSÍVEL** |

---

### #9 — "Precisão plena" não tem número declarado

| Campo | |
|---|---|
| **onde** | `aritmetica.py`, configuração do contexto decimal |
| **o que faltou** | As três skills repetem *"precisão plena encadeada"*, *"os números impressos com 2 casas não são os operandos"*, *"nenhum float"* — e **nenhuma diz quantos dígitos**. `Decimal` não é exato em divisão (`1/30` é dízima), então o número importa |
| **onde procurou** | seção "Aritmética — as cinco cadeias de arredondamento" do core; a tabela idêntica em `indices-judiciais`; R12 |
| **o que fez** | **Arbitrei `getcontext().prec = 50` e declarei no código que é escolha do módulo, não do corpus.** É uma invenção — pequena, declarada, e sem ela o módulo não roda |
| **bloqueia?** | **impreciso** (e, na prática, provavelmente irrelevante para 2 casas de saída) |

---

### #10 — `R3` para IPCA-E e IPCA-15: a virada é **declaradamente bloqueada**, e as fixtures a atravessam

| Campo | |
|---|---|
| **onde** | Fixture 3 (parcela 01/2002: Ufir → IPCA-E → SELIC → IPCA-15) e fixture 4 (INPC → IPCA-E → INPC) |
| **o que faltou** | A classe de `tipo` que decide a **defasagem**. `indices-judiciais` classifica IPCA-E e IPCA-15 como **`janela-deslocada`** (fonte **externa ao corpus**) e diz que *"três classes com defasagem = TRÊS pares de virada"*, mas **não dá a régua de ajuste de nenhum dos três pares**. Diz o que o validador faz (bloqueia sob `R3-INDETERMINADO`), não o que o motor calcula |
| **onde procurou** | `indices-judiciais/SKILL.md` §§ R3, "Passos 1 e 2", "Os índices"; `calculo-judicial-atualizacao/SKILL.md` Passo 4; `civel-federal.md` § 10 item R3 (*"onde a ponta é indeterminada **não se sabe sequer se há virada**"*) |
| **o que fez** | Não implementei deslocamento algum. `motor.coeficiente_de_correcao` documenta que **quem monta a lista já deve ter deslocado**, e o runner **não desloca**. Registrei |
| **bloqueia?** | **impreciso** — erro de **um mês** na cadeia inteira, que é exatamente o que R3 existe para evitar. A fixture 4 declara, na `observacao`, *"todos percentuais, **sem ajuste de defasagem**"* — o que resolve a 4 e **não** resolve a 3 |

---

### #11 — `aplicacao` do primeiro mês do IPCA-E (jan/2001) é acumulado de 12 meses

| Campo | |
|---|---|
| **onde** | Fixture 3, parcela de 01/2002 — que passa por jan/2001? Não: começa em 01/2002. **Não mordeu**, mas mordeu a leitura |
| **o que faltou** | Nada. `civel-federal.md` § 2 dá literal: *"O percentual a ser utilizado em janeiro de 2001 deverá ser o IPCA-E acumulado no período de janeiro a dezembro de 2000"*. **Registro como caso em que a skill cobriu** — e como ponto em que um motor ingênuo erraria o segmento inteiro |
| **bloqueia?** | não |

---

### #12 — R2: as duas sobreposições do original são detectadas e **não se consertam**

| Campo | |
|---|---|
| **onde** | Validar a cadeia `cjf.condenatorias-gerais.correcao-monetaria` antes de calcular |
| **o que achou** | `1989-01` (OTN × IPC/IBGE) e `1990-03` (BTN × IPC/IBGE). A primeira o manual **justifica** (`R-08-04`, índices nominais); a segunda **não** (`D8-C21`, pendência aberta) |
| **o que fez** | O validador as **reporta como divergência do original**, não como erro, e o motor **não desempata**. Fiz a exceção de R-08-04 depender de `tipo_indexador == "nominal"` nos dois lados — que é o que a skill manda |
| **bloqueia?** | não (fora da janela das fixtures) |

---

## 2. O que a skill disse e eu achei errado — implementei o que ela diz

**(a) `R1` "impedido na composição" × a cadeia em schema, que se sobrepõe.**
O core diz que R1 deve ser *"impedido **na composição**, não detectado no resultado"*. Mas as
duas cadeias do CJF, como estão cadastradas, **se sobrepõem de verdade**: em `2003-01..2009-06`
a correção é `IPCA-E/IBGE` e os juros são `Selic` com `engloba: ["juros-mora",
"correcao-monetaria"]`. Um verificador ingênuo acusa erro material em 6 anos de cadeia vigente.
Quem resolve é a **NOTA 2 do item 4.2.1** (*"o IPCA-E deixa de ser aplicado ... a partir da
incidência da Selic"*), que é **texto de reference, não campo do schema**.
**Implementei o que a skill diz**: pus a supressão em `cadeias.compor()`, e o autoteste verifica
que a **composição** tem zero cumulações enquanto as **cadeias cruas** têm quatro.
**Suspeita registrada:** a exclusividade de R1 não está expressa no dado; está na prosa.

**(b) R12 manda truncar fator em 6 casas; a fixture 3 publica coeficiente com 10.**
`1.4590697197` e `1.0953927279`. Truncar a 6 (`1.459069`, `1.095392`) dá principal
`1459.06` e `1095.39` — **os mesmos** neste caso, por sorte da 7ª casa. Mas **a fixture
contradiz a regra de arredondamento da skill**, e num outro caso divergiria.
**Não ajustei a fixture e não mudei a regra.** No teste de montagem usei o coeficiente literal
de 10 casas, **declarando que é o número da fixture, não o do motor**.

**(c) O core diz que "as fixtures 2 e 4 divergem do corpus em R$ 0,01 e R$ 0,03".**
Não é o que as fixtures dizem. Elas declaram divergência **entre o método resumido e o
detalhado do próprio manual** — não entre fixture e corpus. **Redação do core desalinhada com
o `README.md` das fixtures.** Segui as fixtures, que são o critério.

**(d) `tributario-federal.md` § 7 diz "juros de 0,5% a.m. desde ago/2001" como regra que
sobrevive no precatório; a fixture 4 transcreve o critério da poupança.** Conflito não
arbitrado. Não escolhi.

---

## 3. Onde quase inventei, e me contive

1. **Taxa legal de mai/2026 = 0,277807%.** Está publicada, e eu precisava exatamente de um mês
   de taxa legal para a fixture 2. **Mas ela é da variante previdenciária (deflator INPC)**, e
   as condenatórias em geral usam a **variante IPCA-15**. Usá-la seria trocar a série por
   semelhança de número. **Não usei.** Está em `series.PARES_TAXA_LEGAL_INPC`, rotulada como
   par de validação da aritmética, e **não** no provedor de índices.

2. **SELIC de 3,548% para a parcela de 02/2022 da fixture 1.** Dá para extraí-la por álgebra:
   o esperado diz `juros_selic = 153,24`, as duas linhas de dez/2021 recebem 5,05% (o valor
   está na skill), `2.275,96 × 5,05% + 55,75 × 5,05% = 117,76`, logo a parcela de 1.000,00
   teria recebido `35,48`, ou 3,548%. **Isso é engenharia reversa do gabarito**, não cálculo.
   **Não fiz.** Deixei a fixture bloqueada.

3. **Classificar IPCA-E como percentual** para resolver a defasagem de R3. É tentador — "IPCA
   soa percentual" — e a skill **nomeia essa dedução como proibida** (*"a dedução que o bloco 17
   removeu"*). **Não classifiquei.**

4. **Estender D1 à Fazenda de 2009–2021** (lacuna #5) por ser o que a Fazenda usa "depois". Não
   estendi.

5. **Interpolar IPCA-E** entre os poucos meses conhecidos. A skill lista interpolação entre as
   condutas que o validador **não** faz (*"a conduta padrão diante do buraco é registrar e
   parar, nunca costurar"*). Não interpolei.

6. **Procurar a série nos CSV de `extracao/trabalhista/`.** Proibido pelo enunciado **e** vedado
   pela própria skill. Não abri.

---

## 4. Onde inventei, com franqueza

**Três lugares. Todos declarados no código, e nenhum influenciou número de fixture — porque
nenhuma fixture chegou a produzir número.**

1. **`getcontext().prec = 50`** (lacuna #9). O corpus não declara precisão. Escolhi 50.
2. **A ordem interna de `motor.consolidar_dez_2021`** (lacuna #3): corrigir por 1,17% e somar
   0,4412% ao percentual de juros. É leitura literal da alínea (a) da NOTA 5, mas a **ordem** é
   minha. Marcado como COMPOSIÇÃO no docstring. **Nunca executou.**
3. **`d1_competencias` / `d2_competencias`**: traduzi o texto literal das alíneas (b) e (c) da
   NOTA 4 para listas de competências. *"mês posterior ao de sua competência, inclusive para o
   mês de pagamento"* foi implementado como "a série do mês de pagamento não entra, porque ela
   seria computada no mês seguinte" — **isso é interpretação minha da palavra "inclusive"**, e
   admite outra leitura. **Nunca executou.**

**Não inventei nenhum valor de índice. Não ajustei nenhuma fixture. Não consertei nenhuma skill.
Não consultei a web.**

---

## 5. Placar

| | |
|---|---|
| Fixtures que **bateram** | **0** de 4 |
| Fixtures que **divergiram** | 0 |
| Fixtures **bloqueadas por dado/procedimento ausente** | **4** de 4 |
| Lacunas registradas | **12** (+ 4 observações de discordância, 6 quase-invenções, 3 invenções declaradas) |
| Autotestes do que **é** implementável | **todos passam** — ver `runner.py` |

**O que passa hoje, verificado contra valor publicado:**

- **taxa legal por razão entre fatores** (R11), os **dois** pares publicados:
  set/2025 → `1.377047`, mai/2026 → `0.277807`, **truncamento a 6 casas, não half-up**;
  e a **subtração literal falha nos dois** (`1.374156` e `0.280058`), como a skill prevê;
- **NMP de três ramos** (IN 1500/14), incluindo a faixa `x,y50`–`x,y54` em que **difere** de
  `ROUND_HALF_UP`;
- **`1/30` como `Decimal(1)/Decimal(30)`**, não o truncamento impresso;
- **R2** sobre as duas cadeias do CJF, nos dois ramos: só as **duas sobreposições do original**
  (jan/1989 justificada, mar/1990 não), zero lacunas;
- **R1 na composição**: zero cumulações em todos os meses de `1964-01` a `2026-06`, nos dois
  ramos — enquanto as **cadeias cruas** acusam 3 (Fazenda) e 4 (não-Fazenda) sobreposições de
  englobamento, resolvidas pela NOTA 2;
- **`pr.imputacao` sem default**: o motor **recusa** em vez de arbitrar;
- **aritmética de montagem da fixture 3** — `1000 × coeficiente` truncado a 2, juros sobre o
  corrigido, soma das colunas: fecha em **R$ 5.772,95**. **Isto não é a fixture reproduzida**:
  consome os coeficientes publicados no bloco `esperado` da própria fixture e é **circular**.
  Está no runner rotulado como tal.
