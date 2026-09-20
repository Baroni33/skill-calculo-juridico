# Encargos processuais — custas, honorários, sindical e precatórios

Fonte: `docs/calculo/consolidado/06-encargos.md` (capítulos 8, 12 e 14 do Manual TRT-3).
Vereditos: `C8-01`, `C8-02`, `C8-03`, `C12-01`, `C12-02`, `C12-03`, `C14-01`, `C14-02`, `C14-03`.

**Fronteira instável, declarada:** as faixas de honorários são do **CPC art. 85, § 3º**, não da
CLT, e valem nos três ramos. Ficam aqui **provisoriamente** (`README.md` da skill).

---

## 1. O quadro geral

| Encargo | Base | Alíquota / valor | Responsabilidade | Momento | Fundamento |
|---|---|---|---|---|---|
| **Custas processuais** (8.1) | valor do acordo, da condenação, da causa ou, indeterminado, o que o juiz fixar | **2%**, mínimo **R$ 10,64** | **não declarada** no item 8.1 | **não enunciado** no cap. 8 | CLT art. 789, I a IV; Lei 10.537/02 |
| **Custas de execução** (8.2) | por **natureza do ato** — 14 rubricas C-1 a C-14 do Anexo II | tabela; teto **R$ 1.915,38** em adjudicação/arrematação/remição | **SEMPRE do executado** | **ao final**, após a quitação do débito exequendo | CLT art. 789-A, caput; **IN GP/CR/VCR 001/2002 do TRT-3**, art. 2º |
| **CE sobre o cálculo de liquidação** (8.2.1) | o cálculo de liquidação, **definida por exclusão** — § 3 | **0,5%**, até **R$ 638,46** | executado | ao final | CLT art. 789-B, IX; IN 001/02, art. 6º |
| **Honorários periciais** (8.3) | valor **arbitrado pelo juízo** | arbitrado — o manual **não fixa percentual nem tabela** | **não declarada** no item 8.3 | correção do arbitramento até o efetivo pagamento | **IPCA-E** (Res. 66/10 do CSJT); OJ 198 |
| **Honorários advocatícios** (8.4) | valor da condenação **sem dedução dos descontos fiscais e previdenciários** + FGTS a depositar, **excluída a cota patronal** | **arbitrado** — 15% no exemplo da p. 106 | vencido / assistência sindical, conforme o regime | liquidação | § 4 |
| **Emolumentos** (E-1 a E-8) | por folha | R$ 0,28 a R$ 5,53 | **do requerente**, **independentemente de processo** | a qualquer momento | Anexo II da IN 001/02 |

> **Os valores do Anexo II são nominais de 2002, reproduzidos em 2016.** O item 8.2 diz
> **expressamente que não sofrem atualização monetária**, e a tabela não tem data-base nem regra
> de reajuste. As custas do art. 789 **já arbitradas** corrigem-se pelas Leis 6.899/81 e 8.177/91
> a partir do arbitramento — **corrige-se o resultado, não a base**.

**Ausências do manual, registradas e NÃO preenchidas por inferência:** **teto** das custas do
art. 789 — **não declarado**; **responsabilidade e momento** das custas do conhecimento — **não
enunciados** no item 8.1; **responsabilidade na perícia** — **não declarada** no item 8.3.

---

## 2. Custas de execução — a base é definida POR EXCLUSÃO

**Item 8.2.1** (p. 101; **ausente do sumário**, que traz só 8.1/8.2/8.3/8.4), literal:

> *"Da base de cálculo das CE será excluída apenas a parcela de custas processuais (custas da fase
> de conhecimento), na forma do art. 6º da IN GP/CR/VCR n. 001/02"*
>
> *"Nenhuma outra verba deverá ser excluída da base, nem mesmo imprensa oficial e honorários,
> salvo determinação judicial contrária"*

**O manual diz o que SAI. Nunca o que ENTRA, nem em que estado.**

| Busca dirigida | Escopo | Resultado |
|---|---|---|
| `bruto` · `líquido` | **itens 8.2 e 8.2.1** | **zero ocorrências** cada |
| `bruto` | pp. 100–106 | 2× na p. 105 e 2× na p. 106, **ambas sobre honorários advocatícios** |
| `líquido` | pp. 100–106 | 1× p. 104, 2× p. 105, 2× p. 106 — **IR de peritos e honorários** |

**O que o capítulo 8 decide:** honorários **entram**; imprensa oficial **entra**; custas do
conhecimento **saem** — única exclusão autorizada. **O que não decide:** o **estado (bruto ou
líquido)** em que o crédito do reclamante entra. **O eixo simplesmente não é endereçado.** É a
pendência **`P13B-01`**, aberta. **Resolver seria inventar.**

### 2.1 `R8-CE-01` — invariante promovida de exemplo

> **A base das custas de execução é o total do cálculo ANTES da própria linha de CE.**

Fecha exato na `pagina_pdf` **163**: `4.502,08 → 22,51 → total 4.524,59`. **Regra que só existe na
aritmética** — promovida **com marcação de origem**, porque o manual não a enuncia.

### 2.2 `A12` — o rótulo do cap. 9 ignora o juro Selic da cota-reclamante

| | |
|---|---|
| **Impresso** (p. 132) | `"(Vr. Bruto do recte + INSS recda) x 0,5%"` |
| **Base real** | `líquido + INSS recte COM Selic + INSS recda` |
| **Delta** | **35,29** no exemplo da p. 280 — a base dá **30.312,81** e não 30.277,52 |

```
líquido 28.416,25 + INSS recte 606,12 + INSS recda 1.290,44 = 30.312,81
bruto   28.987,08 +                     INSS recda 1.290,44 = 30.277,52
                                                     delta  =      35,29
                                          606,12 − 570,83   =      35,29   ✓
```

`bruto ≡ líquido + INSS recte SEM Selic`. **O rótulo só coincide quando o INSS não carrega juro** —
que é o caso nas três ocorrências do cap. 9 (pp. 132, 137 e 163, **todas verificadas**). Isto
reclassifica a `P10-18` de divergência normativa entre capítulos para **defeito de rótulo**
(`D13B-06`). E o `151,39` do bloco 10 **não é impresso em nenhuma das 471 páginas** — era valor
derivado da análise.

### 2.3 O confronto com a Justiça Federal — registrado, não harmonizado

| Eixo | TRT-3 | CJF |
|---|---|---|
| **normatização** | arts. 789/790/790-A da CLT + Lei 10.537/02 + IN 20/2002 do TST + **IN regional** 001/02 | **Lei 9.289/1996**, norma única federal |
| **base** | acordo, condenação, causa ou arbitramento | **só o valor da causa**, e **corrigido** desde o ajuizamento |
| **alíquota** · **piso** | 2% impressa · R$ 10,64 | Tabela I da Lei 9.289/96 — **remissão externa, não reproduzida** · não declarado |
| **momento** | concentrado ao final da execução | **metade na distribuição**, metade de quem recorrer ou do vencido (art. 14, I a IV); na apelação, **tabela vigente na data de interposição** |
| **atualização** | corrige o **resultado** | corrige a **base** |
| **isenções** | por **qualidade do sujeito** — § 5 | também por **tipo de ação** (HC, HD, reconvenção) e por **rito** (JEF) |
| **eletrônico** | nenhuma dispensa registrada | **porte dispensado** em autos eletrônicos (art. 1.007, § 3º, CPC) |

**`D8-C1` — dois eixos numa frase só, do lado federal:** na apelação, a *tabela* segue a data de
interposição; o *valor da causa* segue o encadeamento desde o ajuizamento. **A comparação direta
de valor é impossível com o corpus atual** — a Tabela I **não foi extraída**.

---

## 3. Honorários periciais — item 8.3

- **Base:** valor **arbitrado pelo juízo**. O manual **não fixa percentual nem tabela**.
- **Atualização: IPCA-E**, prática da Secretaria de Cálculos de Belo Horizonte, com apoio na
  **Res. 66/10 do CSJT** — **índice DISTINTO do crédito principal**.
- **Sem juros**, por serem despesa processual — art. 407 do CC e **OJ 198**.
- **Termo inicial:** data do arbitramento, ou outra fixada pelo juízo, até o efetivo pagamento.
- **Tributação:** IR do perito lançado **separadamente**, e **o total soma honorários líquidos
  MAIS o IR** (art. 106, § 2º, "h", p. 104). Conferido em `Decimal` nos dois peritos do exemplo.
- **Responsabilidade: NÃO DECLARADA.** No exemplo da p. 280 a sentença põe por conta da ré.

> **Divergência jurisprudencial registrada, não resolvida — `P13B-04`.** **Quatro acórdãos em cada
> sentido** sobre a incidência de juros nos honorários periciais. **Duas variantes com fundamento
> próprio, nenhuma arbitrada.**

**Do lado federal:** quem requereu a prova tem o ônus de **adiantar** os honorários, e o manual
CJF traz **três termos iniciais alternativos** para a correção dos honorários não depositados
**sem critério de escolha** (`P8-14`, aberta).

---

## 4. Honorários advocatícios — o único corte de 11/11/2017 com eixo na propositura

**`C8-01`, `BIFURCADO`. As duas versões em [`cortes-e-bifurcacoes.md`](cortes-e-bifurcacoes.md)
§ 4.** É `BIFURCADO` e **não `SUPERADO`** porque ainda tramitam e se liquidam ações propostas
antes de 11/11/2017, **e nelas o capítulo 8 do manual é a norma aplicável, não peça de museu**.

### 4.1 A base do manual, e o que ela tem de próprio

- **Enunciada:** *"os honorários advocatícios incidem sobre o valor líquido da condenação, apurado
  na fase de liquidação, **sem a dedução dos descontos fiscais e previdenciários**"* — isto é, o
  **bruto** liquidado em favor do reclamante.
- **Exclusão expressa:** *"a cota-parte de contribuição previdenciária do empregador **não
  integra** a base"* — **OJ 348 e TJP 4 do TRT-3** (regional `R6`).
- **Conferido em `Decimal`** na p. 106: `264.131,80 (bruto) + 13.206,59 (FGTS a depositar) =
  277.338,39`, **excluída** a cota patronal de `18.574,26`.

> **`A13` — base impressa errada.** O rótulo diz `(15% s/ 277.338,69)` e o resultado é
> `41.600,76`, que é 15% de **277.338,39**. 15% de 277.338,69 daria 41.600,80. **Rótulo errado,
> resultado certo** — mesmo padrão de `A7` e `A11`.

**Divergência de base, registrada e não resolvida:** o **FGTS a depositar na base** é regra do
TRT-3 de 2016; **nada no corpus confirma que sobreviva ao art. 791-A**, que fala em *"valor que
resultar da liquidação da sentença"*. **`D4`:** o corpus a chama de *"regra do TRT-3 de 2016"*
**sem citar verbete** — se for prática do manual é **NACIONAL**; se houver súmula ou TJP por trás,
é **REGIONAL**. **O que falta é o veículo** (`P8-F4-03`).

**`D1`, dúvida não resolvida:** *"OJ 348 e TJP 4 do TRT-3"* admite duas leituras — o "do TRT-3"
governa **só a TJP 4** ou **as duas**. O `jurisprudencia-indice.md` lista **apenas três** OJs de
Turmas do TRT-3 (**4, 23 e 29**), o que **inclina** para a OJ 348 da **SDI-1 do TST** (nacional).
**Inclinação não é classificação.**

### 4.2 As faixas do art. 85, § 3º, do CPC

**`P8-F4-02`, fechada na auditoria com fonte primária** (acórdão do STJ). **Três consequências, e
todas mudam o modelo:**

1. **a unidade é o salário-mínimo** — as faixas são progressivas, e o cálculo observa *"o
   percentual da faixa inicial e, naquilo que a exceder, o percentual da faixa subsequente, e
   assim sucessivamente"* (art. 85, § 5º; regra `R-08-21`);
2. **a data do salário-mínimo é a do § 4º, IV** — **sentença líquida ou decisão de liquidação**,
   **não o ajuizamento**;
3. **o percentual é entrada arbitrada, não saída calculada.** O juiz arbitra dentro da faixa; **o
   motor não o deriva.**

> **Busca com escopo declarado, e o que ela não fecha.** A busca original do bloco 13B era
> **metodologicamente frágil** — o texto legal escreve *"200 (duzentos) salários-mínimos"*, com
> parêntese por extenso e hífen, e **nunca existiu** faixa de mil salários-mínimos (`S19`).
> Refeita sobre `docs/**/*.md` com `duzentos` e `salários-mínimos`: **duas ocorrências, ambas
> metalinguísticas**. **Os VALORES numéricos das faixas continuam não transcritos no
> repositório.** A regra estrutural está fechada; **a tabela, não**.

### 4.3 `C8-02` — ADI 5766: eixo SUBJETIVO, não temporal

**`SUPERADO`**, julgamento em **20/10/2021**, **sem modulação** (ED rejeitados em 21/06/2022),
efeitos ***ex tunc***. **Não há eixo temporal próprio: o eixo é a condição de beneficiário da
justiça gratuita.** Declarados inconstitucionais o **art. 790-B, caput e § 4º**, e o **art. 791-A,
§ 4º**, da CLT.

**Consequência de cálculo, frequentemente ignorada:** sendo o reclamante beneficiário da
gratuidade, os honorários sucumbenciais **devidos por ele não podem ser abatidos do seu crédito**
— **some uma parcela da cadeia de descontos sobre o líquido**.

> **Variante `V-11`, não resolvida.** (A) a inconstitucionalidade **afasta a fixação**; (B) os
> honorários **são fixados** e ficam sob **condição suspensiva de exigibilidade** (art. 98, § 3º,
> do CPC). **O efeito sobre o líquido do reclamante é o mesmo nas duas.** A diferença é de
> composição da conta e de dispositivo — **não é matéria que o cálculo decida.**

**Ressalva de fonte:** `portal.stf.jus.br` respondeu **HTTP 403** em todas as tentativas. **O
acórdão não foi lido**; a ausência de modulação está apurada em **fonte secundária**.

---

## 5. Isenções — o manual se contradiz sobre Fazenda Pública

**`D13B-02`.** Duas isenções **incompatíveis** para **a mesma pergunta**.

| Onde | Teste |
|---|---|
| **Cap. 8, p. 102, item 4** | *"São isentos (…) os entes públicos das 3 esferas, inclusive autarquias e fundações, **que não explorem atividade econômica**, o Ministério Público do Trabalho e os beneficiários da Justiça Gratuita (art. 790-A, CLT)"* |
| **Cap. 14, p. 306, letra "e"** | *"Custas execução: Estão isentos os órgãos públicos das três esferas da administração pública **direta e indireta**, inclusive fundações e autarquias"* |

**O cap. 14 omite a cláusula da atividade econômica e acrescenta "indireta"** — que abrange
sociedade de economia mista. **NÃO RESOLVO.** A condicional fica registrada **nos dois ramos**:
pelo cap. 8, ente da indireta que explore atividade econômica **paga**; pelo cap. 14, **é isento**.

> **Busca que sustenta a negativa, com escopo:** `economia mista` → **zero ocorrências nas 471
> páginas**; a única equiparação nominada é a **ECT**, e só *"para efeito de execução e do DL
> 779/1969"*. **O manual não pode ser fonte para fechar a Pendência 1 da § 9 da base.**

**É a pendência de maior impacto do projeto:** se a resposta for negativa, somem do escopo o ramo
Fazenda Pública das três jurisdições, precatório, ECs 113 e 136 e a consolidação de dez/2021.
**`C14-03` é `INAPLICÁVEL` por prejudicialidade**, e `C14-01` e `C14-02` são **condicionais a
ela**. **Não é matéria de cálculo — é pergunta ao jurídico do usuário do módulo** (R9).

---

## 6. Contribuição sindical — capítulo 12

**`C12-01`, `BIFURCADO`, corte em 11/11/2017, eixo na competência da contribuição.** As duas
versões em [`cortes-e-bifurcacoes.md`](cortes-e-bifurcacoes.md) § 1. **O que sobrevive para as
competências anteriores: TUDO** — *"a Lei 13.467/2017 não mexeu no QUANTO nem no COMO: mexeu no
SE"*. O exemplo dos R$ 28 milhões **confere em `Decimal`: `11.572,82`**.

**`C12-02` — `VIGENTE`.** O STF, na **ADI 5794** (29/06/2018, 6 × 3), julgou constitucional o fim
da obrigatoriedade. **Fecha a possibilidade de reversão retroativa** — a estrutura do cap. 12 vira
**estritamente histórica**.

**`V-12`, aberta:** a autorização deve ser **individual**, ou a assembleia supre? **Confirmei
"prévia" e "expressa"; NÃO confirmei "individual"** (`B-06`). Lacuna de fonte declarada.

**`A14` — defeito de série no cap. 12:** teto rural de 2011 impresso `10.867,51` contra
`10.867,32` pelo fecho da própria tabela — **delta 0,19**, **uma ordem de grandeza acima do ruído
de 0,01 dos demais anos**. Na mesma família: faixa de 2013 com **sobreposição** em `3.255,47` e
**buraco de R$ 2,01**; faixa de 2014 com `6.89.754,21` malformado.

**`C12-03` — contribuição assistencial: `BIFURCADO` por eixo NÃO temporal** (existência de direito
de oposição assegurado) — § 4 daquele arquivo. **Efeito sobre o manual: indireto** — o cap. 12
**nomeia** a assistencial mas **não a calcula**. O Tema 935 não supera conta existente: **abre
hipótese que o manual não cobre.**

> **Ressalva de escopo, essencial:** a **contribuição negocial** do ACT 2025/2027 (5% do
> salário-base mais adicional de periculosidade, teto R$ 260) **não é nenhuma das quatro** do
> capítulo. `negocial` → **zero ocorrências no cap. 12**. **Não confundir.**

---

## 7. Precatórios — capítulo 14

**Três páginas, zero exemplos numéricos.** O único dos capítulos do bloco 13C **sem planilha** —
**não há conta a reproduzir**. **O capítulo conhece a EC 62/2009 e para aí.**

**Ausências, com busca declarada nas pp. 304–306:** requisição complementar/suplementar → nenhuma
ocorrência; limite de RPV (`pequeno valor`) → **0**; data de apresentação → **ausente**.

**O que SOBREVIVE — quatro regras estruturais**, cruzadas contra o cap. 5 do manual CJF: suspensão
dos juros de mora durante o prazo constitucional de pagamento; **juros de 0,5% ao mês desde
ago/2001**; exclusão de juros compensatórios; **exceção à precedência do título**. Nenhuma depende
da EC 62/2009 nem foi tocada pelas ECs 113 e 136.

**A cadeia de índices de `C14-01` e `C14-02` NÃO é matéria desta skill** — é
`skills/calculo-judicial-atualizacao/`. O que fica registrado aqui é o **erro corrigido no bloco
14**: a EC 113/2021 **não era "só federal"** (*"independentemente de sua natureza"*), e **a
restrição veio com a EC 136/2025**. Para Fazenda **estadual ou municipal**, entre **dez/2021 e
set/2025**, vale o regime da **Selic única**.

**A divergência do cap. 14 sobre imputação** — p. 306, letra "c", *"Amortizar com observância da
**data do pagamento** e não da data do levantamento, salvo determinação do juízo da origem"* — é a
**terceira posição** de [`imputacao-e-amortizacao.md`](imputacao-e-amortizacao.md) § 6.

---

## 8. Ordem de cálculo e interação com o resto do motor

1. **R22** — regimes avaliados **antes** de qualquer parâmetro;
2. apuração das verbas ([`verbas-catalogo.md`](verbas-catalogo.md)) e dos descontos;
3. **honorários advocatícios** sobre o bruto do reclamante + FGTS, **excluída a cota patronal** —
   e **sem abatimento do crédito** se houver gratuidade;
4. **custas de execução** por `R8-CE-01`: `0,5%` sobre o **total do cálculo antes da própria linha
   de CE**, excluídas **apenas** as custas do conhecimento, teto **R$ 638,46**;
5. **R19** — gravar, por competência, qual lado de cada corte foi aplicado; **para `C8-01`, gravar
   a data de propositura usada, que é o eixo.**

**R8 prevalece em todo o capítulo:** *"salvo determinação judicial contrária"* está no texto do
próprio item 8.2.1, e o momento da CE depende de despacho — **omisso o despacho, o manual manda
perguntar ao Juiz ou ao Diretor de secretaria, não inferir.**

---

## 9. Pendências abertas — não resolvidas por inferência

| # | O que está aberto |
|---|---|
| `P13B-01` | a base das CE é definida **por exclusão**; **o estado (bruto ou líquido) não é declarado** |
| `P13B-02` | **contradição cap. 8 × cap. 14** sobre a isenção de entes públicos — § 5 |
| **Pendência 1 da § 9** | classificação de sociedade de economia mista como Fazenda Pública. **Pergunta ao jurídico**, não matéria de cálculo |
| `P13B-04` | juros sobre honorários periciais — **quatro acórdãos em cada sentido** |
| `P8-F4-02` | regra **fechada**; **os valores numéricos das faixas do art. 85, § 3º, continuam ausentes do repositório** |
| `V-11` · `V-12` | ADI 5766: afasta a fixação × condição suspensiva · autorização sindical individual ou por assembleia |
| `D1` · `D4` · `D7` · `D8` | veículo da OJ 348 · veículo do FGTS a depositar na base · os **quatro Provimentos do TRT-3** (01/93, 03/91, 04/00 e o Prov. Conjunto GCR/GVCR n. 3/2015), **procedimentais, não de cálculo** — mas o 04/00 disciplina **memória e resumo**, e o Conjunto remete **expressamente ao Manual** · a **IN 001/02** não é súmula nem tese do art. 896, § 6º: **a tipologia não tem casa para ela** |
| — | **responsabilidade e momento** das custas do conhecimento e **teto** do art. 789: **não enunciados** |
| — | base do art. 791-A: **o FGTS a depositar sobrevive na base? Nada no corpus confirma** |
| — | **aditamentos de setembro/2025 do Tema 935** — só fonte secundária |
