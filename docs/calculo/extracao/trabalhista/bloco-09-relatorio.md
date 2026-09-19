# Bloco 9 — relatório

Capítulo 7 do Manual de Cálculos do TRT-3 (julho/2016), páginas 83 a 99 do PDF.
Extração dirigida. Produto em `bloco-09-cadeias-historicas.md` e em
`docs/calculo/tabelas-normativas/trt3.hist.*.json`.

---

## 1. Entregas

| Item | Estado |
|---|---|
| Tarefa 0 — corrigir o validador | **Feita, e depois refeita.** Ver § 2 |
| Tarefa 1 — extração das cadeias | **Feita** — 4 cadeias, 19 segmentos |
| Tarefa 2 — cruzamento com a cadeia federal | **Feito** — § 4 |
| Tarefa 3 — validação R1/R2 e tipo de indexador | **Feita** — § 5 |
| Releitura adversarial de todo segmento | **Feita** — § 6. Derrubou seis coisas |
| Verificação de citação literal por script | **Feita** — 34 de 36 LITERAL-OK, 0 página errada |
| Notas conferidas contra as linhas que qualificam | **Feita** |

Cadeias: `trt3.hist.trabalhista.correcao-monetaria` (3), `trt3.hist.trabalhista.juros-mora`
(3), `trt3.hist.fazenda-publica.juros-mora` (5), `trt3.hist.moedas-e-paridades` (8).

---

## 2. Tarefa 0 — o validador, e o defeito que o conserto introduziu

O pedido era corrigir `valida_cobertura.py` **no validador, não em runner à parte**:
segmento sem `condicao` vale para todos os ramos, e a cobertura de cada ramo se avalia
como tronco ∪ ramo.

### 2.1 Primeira versão — correta no alvo, errada no contrato

Implementei tronco ∪ ramo. As cadeias do bloco 8 passaram a reportar R2 = 0 sem o runner,
e R1 caiu de 15 para 12. `valida_cadeias_cjf.py` foi apagado e virou `valida_cadeias.py`,
um CLI fino. Os 199 testes passaram.

**E estava errado.** A implementação deixava de cobrar o universo incondicional sempre que
houvesse *algum* ramo — assumindo que as `condicao` observadas **esgotam o domínio**. Nada
garante isso: elas vêm dos dados, não de um domínio declarado.

O contraexemplo, reproduzido:

```
tronco  1964-01..2000-12  (sem condicao)
ramo    2001-01..2025-12  {devedor: fazenda-publica}
janela  1964-01..2025-12
→ OK, nenhuma violação
```

Não há segmento algum para devedor **não**-Fazenda depois de 2000. **Vinte e cinco anos
descobertos, e o validador diz que está íntegro.** A versão anterior teria acusado.

Troquei um falso positivo por um falso negativo. Num validador de cobertura, é o pior
negócio possível: falso positivo custa leitura, falso negativo passa para produção.
**Nenhum dos 199 testes pegou** — não havia teste de ramo não exaustivo.

### 2.2 Versão final — exaustividade se declara, não se presume

Quem sabe se os ramos esgotam o eixo é a cadeia. Então o domínio passou a ser
**declarável**, via `dominio_condicoes`:

- **eixo declarado** — cada valor vira um universo, *inclusive os que nenhum segmento
  menciona*. Valor sem ramo é avaliado contra o tronco sozinho, e a lacuna aparece,
  **nomeando o ramo que falta**;
- **eixo não declarado** — o universo incondicional continua sendo cobrado, como o caso
  "nenhuma condição se aplica".

O mesmo contraexemplo, agora:

```
sem dominio declarado   → [R2] (sem condição) | 2001-01..2025-12: lacuna
com dominio declarado   → [R2] devedor=nao-fazenda-publica | 2001-01..2025-12: lacuna
bifurcação exaustiva    → nenhuma violação
```

O ruído tem remédio, e o remédio é declarar o domínio — **não silenciar a checagem**.
Seis cadeias passaram a declarar `dominio_condicoes`.

Dois defeitos derivados, também corrigidos:

- **Janela de universo vazio.** Um ramo declarado sem segmento algum quebrava o cálculo da
  janela (`min()` de sequência vazia). A janela passou a derivar de *todos* os segmentos
  que fornecem o componente, não só dos do universo.
- **Colisão tronco × tronco contada uma vez por ramo.** Como o tronco entra em todo ramo,
  a mesma colisão aparecia N vezes e inflava o total. Agora é uma violação, rotulada
  `(tronco)`. **R1 caiu de 17 para 15** — o número real de colisões distintas.

### 2.3 Testes

Cinco testes de regressão novos, em `TestExaustividadeNaoSePresume`, incluindo o
contraexemplo literal do § 2.1. Dois testes existentes passaram a **declarar** o domínio,
em vez de tê-lo presumido — não é afrouxamento, é tornar explícita a afirmação de
exaustividade que eles sempre fizeram em silêncio.

**204 testes, OK.**

---

## 3. Correção de uma afirmação do bloco 8

O relatório do bloco 8 e este, na primeira redação, diziam que as sete cadeias `cjf.*`
passam **sem runner especial, com R2 = 0**.

**É falso.** `valida_cadeias.py` *é* um runner especial: filtra R2 pelo componente que a
cadeia declara. Sem esse filtro, hoje:

| Cadeia | R2 direto | R2 componente próprio |
|---|---|---|
| cjf.condenatorias-gerais.correcao-monetaria | 3 | 0 |
| cjf.condenatorias-gerais.juros-mora | 5 | 0 |
| cjf.desapropriacao-direta.correcao-monetaria | 2 | 0 |
| cjf.divida-fiscal.correcao-monetaria | 0 | 0 |
| cjf.previdenciario.correcao-monetaria | 2 | 0 |
| cjf.repeticao-indebito.correcao-monetaria | 1 | 0 |
| cjf.trabalhista.juros-mora | 3 | 0 |
| **total** | **16** | **0** |

As dezesseis nascem do `engloba` da Selic: um segmento que declara
`engloba: [correcao-monetaria, juros-mora]` faz nascer, dentro de uma tabela de correção,
um universo do componente alheio. **O filtro é defensável; a afirmação de que não havia
filtro, não.** Corrigido aqui e no relatório do bloco 8.

As quatro cadeias `trt3.hist.*` passam com `valida_cobertura` direto, sem filtro.

---

## 4. Tarefa 2 — cruzamento com a cadeia federal

### 4.1 Concordância que vale como conferência

| Período | CJF (cap. 4) | TRT-3 (cap. 7) |
|---|---|---|
| até 26/02/87 | 0,5% simples | 0,5% simples |
| **27/02/87 a 03/03/91** | **1,0% composta** | **1,0% composta** |
| 04/03/91 em diante | 1,0% simples | 1,0% simples |

Dois manuais independentes, de jurisdições distintas e de edições separadas por dez anos,
gravam a mesma capitalização **composta** para o mesmo período. **A anomalia contra a
invariante R4 não é erro de transcrição de nenhum dos dois: é o DL 2322/87.** O TRT-3
acrescenta a precisão ao dia ("Entre 27/02/87 e 03/03/91") e a mecânica ("Ex.: 3 meses =
3,03%"), que o federal não dá.

Confirmação tripla, aliás: o TRT-3 repete a linha composta **em dois quadros** — o geral da
`pagina_pdf 89` e o da Fazenda da `pagina_pdf 92`.

### 4.2 Divergência estrutural real — juros da Fazenda

| | CJF | TRT-3 |
|---|---|---|
| 0,5% a.m. | 2001-08 a **2012-04** | 2001-09 a **2009-06** |
| poupança | a partir de **2012-05** | a partir de **2009-07** |

**Cerca de 34 meses segmentados de forma diferente**, com os dois fundamentos registrados.
Materialmente o número coincide — o TRT-3 anota que "Até 03/05/2012, os juros aplicáveis à
caderneta de poupança, correspondiam a 0,5% ao mês" —, mas a **modelagem** difere e a
consequência é concreta:

> um motor que implemente a versão do TRT-3 precisa da série da poupança **desde 2009**;
> um que implemente a do CJF, só **desde 2012**.

Se a poupança tivesse variado entre 2009 e 2012, os dois dariam números diferentes. Não
variou. **Não harmonizado.**

Há ainda um limite que só o TRT-3 traz: **"0,5% ao mês, limitado a 6% ao ano"**.

### 4.3 A conferência do TR 0,00% de novembro/2021 — não é cruzável

O enunciado esperava cruzar o registro federal de **TR 0,00% em nov/2021** no ramo
trabalhista contra IPCA-E 1,17% no ramo geral.

**O manual do TRT-3 é de julho de 2016 e não alcança novembro de 2021.** O capítulo 7 não
trata daquele mês. A conferência direta é impossível, e registrar isso é a resposta.

O cruzamento possível é o inverso, e ele fecha:

| | Diz |
|---|---|
| TRT-3 (2016) | **por que** a TR é o índice trabalhista — art. 39 da Lei 8.177/91 — e registra o episódio IPCA-E, suspenso pelo STF em 14/10/15: "permanece válida a TR" |
| CJF (2026) | o **valor de fechamento**: `indice_nov2021: 0,00`, `indexador: TR`, `juros_dez2021: 0,4412` |

Um explica o regime, o outro dá o número final. São consistentes: **a TR seguiu sendo o
índice trabalhista até nov/2021, e naquele mês valeu zero.** O TRT-3 de 2016 já
antecipava, sem saber, o regime que o CJF encerraria cinco anos depois.

---

## 5. Tarefa 3 — R1, R2 e tipo do indexador

`11 cadeias | R1: 15 violações | R2: 1 violação`

### 5.1 R2 — a única é deliberada

`trt3.hist.fazenda-publica.juros-mora`, ramo **`fazenda-publica-subsidiaria`**: declarado
em `dominio_condicoes` e **sem segmento**, de propósito. O manual registra corrente
jurisprudencial ("grande parte da jurisprudência entende", `pagina_pdf 93`), não regra
assentada, e divergência jurisprudencial não se resolve neste projeto.

**A lacuna é a leitura correta**, e só aparece porque o validador passou a cobrar ramos
declarados. Pendência **P9-01**.

### 5.2 R1 — cinco na cadeia de moedas, uma real

Disciplina do bloco 8: sobreposição explicada pelo manual é registro; sem explicação, é
achado.

| Violação | Fronteiras no original | Leitura |
|---|---|---|
| **1967-02..1970-02** | "01/11/42 a **12/02/70**" × "**13/02/67** a 14/05/70" | **ACHADO — defeito do original** |
| 1970-05 | 14/05/70 × 15/05/70 | artefato de granularidade |
| 1986-02 | 27/02/86 × 28/02/86 | artefato de granularidade |
| 1989-01 | 15/01/89 × 16/01/89 | artefato de granularidade |
| 1990-03 | 15/03/90 × 16/03/90 | artefato de granularidade |

**Quatro das cinco não são defeito de nada.** As fronteiras do manual são ao dia e
contíguas — D e D+1 —, e a apuração é mensal: a competência que contém o corte fica
legitimamente dos dois lados. É o comportamento esperado, não um problema a consertar.

**A primeira é real.** O cruzeiro terminaria em 12/02/**70** enquanto o cruzeiro novo
começa em 13/02/**67** — três anos de coexistência impossível. O cruzeiro novo foi
instituído em 13/02/67 e as outras seis transições são todas D/D+1. Quase certamente era
**12/02/67**. **Não corrigido**, gravado em `DEFEITO_DO_ORIGINAL`.

As dez R1 restantes são das cadeias do bloco 8, já lidas lá.

### 5.3 Tipo do indexador — nominal × percentual

A virada entre nominal e percentual sem ajuste de defasagem seria erro estrutural. **Não há
virada neste capítulo**, porque não há cadeia de índices: o único indexador nomeado é a TR,
a partir de 03/1991.

E a classificação da TR **não é extração — é inferência, e está marcada como tal**. O item
4.1.2.4 do manual federal opõe nominais (Ufir, BTN, OTN, ORTN — refletem o mês anterior) a
percentuais (INPC, IGP-DI, IGP-M — refletem o próprio mês). Pelo critério formal a TR é
percentual. Pelo critério material, a dicotomia **não se aplica**: a TR não é índice de
preços, é taxa referencial apurada prospectivamente (art. 12, I, da Lei 8.177/91).
**Nenhum dos dois manuais classifica a TR.**

O resultado operacional coincide com o que o TRT-3 diz por outra via (`pagina_pdf 85`):
"Os índices de correção monetária estão posicionados no próprio mês da constituição do
crédito". Mas o rótulo é dedução, e está declarado como dedução.

### 5.4 As três — na verdade quatro — defasagens

Ver `bloco-09-cadeias-historicas.md` § 8. Súmula 381 defasa **um mês**; a tabela diária do
CSJT defasa **um dia**; a pro-ratização é por **dias úteis**; e os juros usam **mês
comercial de 30 dias**. Correção por dias úteis e juros por dias/30 no mesmo cálculo é
atrito real do manual.

---

## 6. O que a releitura adversarial derrubou

O enunciado foi explícito: *"releitura adversarial do conteúdo de TODO segmento, inclusive
os tabulares. No bloco 8 um índice trocado entre 78 segmentos passou por toda validação
estrutural e só a releitura pegou. Não repita."*

**Repeti — em forma pior.** A validação estrutural e a de literalidade passaram limpas:
R1/R2 explicados, 34 de 36 citações LITERAL-OK, zero páginas erradas. E havia seis defeitos.

### 6.1 O pior: um quadro inteiro não lido, e negado por escrito

`trt3.hist.fazenda-publica.juros-mora` foi montada sobre o **resumo em prosa** da
`pagina_pdf 90`. O **quadro sinóptico completo está na `pagina_pdf 92`, com cinco linhas** —
duas páginas adiante, nunca abertas.

Resultado: três segmentos onde há cinco, e o primeiro deles **errado em dois terços do
intervalo** — gravava `1,0% simples` para 1942–2001, quando o manual dá 0,5% simples até
26/02/87 e **1,0% composta** de 27/02/87 a 03/03/91.

E o agravante: eu havia escrito, no campo `observacao` do segmento,

> "O manual **NÃO segmenta** este trecho pela capitalização composta de 27/02/87 a
> 03/03/91"

**uma afirmação falsa sobre a fonte, que serviu de justificativa para não procurar.** Ela
é que travou a detecção. Nenhuma verificação de literalidade pega isso: o erro não está no
que foi citado, está no que **não** foi.

### 6.2 As outras cinco

| # | O que caiu | Correção |
|---|---|---|
| 2 | **`indexador: "TR"` para `1942-11..2009-06`** | A TR nasceu com a Lei 8.177/**91**. O manual não declara índice anterior — delega à Tabela Única. Campo passa a `NAO-DECLARADO-PELO-MANUAL`. **Mesma classe do IPC/FGV do bloco 8** |
| 3 | **`{devedor: fazenda-publica}` sem qualificar** | O quadro vale para a Fazenda "como **reclamada principal**". Um motor teria aplicado 0,5% a.m. a Fazenda subsidiária, que o manual trata a 1% (OJ 382, `pagina_pdf 93`) |
| 4 | **"limitado a 6% ao ano" ausente** | Não é redundante com 0,5% a.m.: morde em contagem por dias que ultrapasse o ano |
| 5 | **Tabela de juros jun/12–ago/13 omitida** | Quinze percentuais cravados, total 6,5760% — **o único mapa período → taxa do capítulo**, e eu havia escrito que o capítulo não tinha mapa nenhum |
| 6 | **Defasagem da tabela diária, mês comercial e Resolução CSJT 08/2005 omitidos** | Os dois primeiros estavam **nominalmente no enunciado do bloco**. Extraídos |

### 6.3 O que a tese verdadeira escondeu

A afirmação central do bloco — o capítulo 7 não tem mapa período → indexador — **é
verdadeira**, e foi confirmada por varredura exaustiva das dezessete páginas. Mas eu a
redigi em termos absolutos, e ela passou a funcionar como **licença para não procurar**.
Os dois mapas período → **taxa** da `pagina_pdf 92` estavam lá o tempo todo.

Uma conclusão correta, generalizada um passo além do que a evidência suportava, custou
mais caro que um erro comum — porque errar por excesso de confiança numa tese verificada
não dispara suspeita.

### 6.4 O que resistiu

- **`trt3.hist.moedas-e-paridades`, os 8 segmentos** — período, moeda, símbolo, proporção,
  data e raciocínio, caractere a caractere contra a `pagina_pdf 99`, inclusive a elipse
  "1.000 = 1,00 cruzado". E o `DEFEITO_DO_ORIGINAL` corretamente dimensionado em três anos.
- **`trt3.hist.trabalhista.juros-mora`, os 3 segmentos** — batem com o quadro da
  `pagina_pdf 89`, inclusive "Ex.: 3 meses = 3,03%".
- **O episódio IPCA-E** — todas as datas e autuações conferidas na `pagina_pdf 84`.
- **`aplicacao` e a mecânica da Súmula 381** — literais e corretos, com o exemplo
  junho/14 → julho/14.
- **A tese central do § 2 do documento** — nenhum expurgo, nenhum multiplicador (6,17,
  6,92, 126,8621), nenhum IPC/IGP/INPC/ORTN/OTN/BTN/Ufir no capítulo 7.
- **A aritmética da tabela nova**, conferida em `Decimal`: os quinze percentuais somam
  exatamente `6,5760`, e `7,5% − 6,5760% = 0,9240%`, como o manual afirma.
- **34 de 36 citações literais**, zero em página errada. As duas restantes são prosa do
  extrator, não citação — e uma delas era a afirmação falsa do § 6.1.

---

## 7. Pendências

Sete, listadas em `bloco-09-cadeias-historicas.md` § 7. As duas que mais pesam:

- **P9-01** — juros da Fazenda **subsidiária**: o manual registra corrente, não regra.
  Ramo declarado e vazio, por decisão.
- **P9-02** — índice de correção **anterior a 03/1991**: não declarado pelo manual. É a
  lacuna estrutural do capítulo, e só se fecha pela Tabela Única do CSJT ou pela cadeia do
  CJF.

---

## 8. Lição de método

O bloco 8 ensinou que validação estrutural não pega conteúdo trocado. O bloco 9 ensina algo
mais estreito e mais perigoso:

> **Uma afirmação negativa sobre a fonte — "o manual não diz X" — é uma conclusão, e
> conclusão em campo de dado não é verificável por nenhum script.**

As duas piores falhas deste bloco (§ 6.1 e § 6.3) foram exatamente isso: eu escrevi que o
manual não segmentava, e que o capítulo não tinha mapa. A verificação de literalidade
conferia tudo que **estava** citado e nada do que fora **negado**.

Afirmação negativa exige varredura declarada — página por página, termo por termo — e o
registro de qual foi a varredura. Onde isso foi feito (§ 6.4, os expurgos e multiplicadores),
a negativa resistiu. Onde não foi, caiu.
