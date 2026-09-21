---
name: calculo-judicial-core
description: >-
  Base obrigatória de qualquer cálculo judicial brasileiro — cível, trabalhista, tributário
  federal ou previdenciário. DISPARE SEMPRE que a tarefa envolver conferir, refazer, auditar ou
  produzir conta de processo judicial, ANTES de qualquer skill de jurisdição. Gatilhos: "confira
  este cálculo", "refaça esta conta", "o perito errou?", "compare estas duas planilhas", "quanto
  dá isso hoje?", "monte a memória de cálculo", "este laudo está certo?". Também com as palavras
  liquidação, execução, atualização monetária, juros de mora, correção monetária, impugnação aos
  cálculos, planilha do perito ou embargos à execução. Traz o modelo de domínio, as invariantes
  R1-R24 cuja violação produz ERRO MATERIAL, a aritmética decimal exata e o comparador. Sem ela
  as outras três produzem número plausível e errado.
---

# Cálculo judicial — núcleo

**Modelo de domínio, invariantes, aritmética e comparador.** É a base sobre a qual as outras
três skills assentam. Toda afirmação aqui sai de `docs/calculo/consolidado/`.

---

## Quando usar / quando não usar

**Use sempre.** Esta skill não é opcional nem específica: as invariantes R1–R24 valem nas
quatro jurisdições, e violá-las produz **erro material** — não divergência de critério.

| Use para | Não use para |
|---|---|
| decidir **qual camada** resolve a questão | achar **qual índice** vale num período → `calculo-judicial-atualizacao` |
| aritmética, arredondamento, precisão | **valor** de índice ou faixa → `indices-judiciais` |
| comparar dois cálculos e nomear a divergência | apurar **verba** trabalhista → `calculo-trabalhista-liquidacao` |
| memória de cálculo e reprodutibilidade | — |

> **Se a pergunta é "quanto dá", esta skill sozinha não responde.** Ela diz o que **não** pode
> acontecer no caminho.

---

## Modelo de domínio

### As três camadas, nesta ordem

```
1. REGIME TEMPORAL      qual REGRA vale nesta competência?        R19–R22
2. PARÂMETRO            quanto VALE o que a regra manda aplicar?  R14–R18, R24
3. APURAÇÃO             a conta                                   R1–R13, R23
```

**Inverter a ordem produz número plausível com a conta inteira no regime errado.**

**A camada 1 decide se a camada 2 é sequer consultada.** Sob `pr.in-itinere` na variante
`suprimidas`, o parâmetro `pn.in-itinere.prefixacao` **não existe** — não é que valha zero.

### Vocabulário — os termos têm sentido exato

| Termo | Significado |
|---|---|
| **competência** | o mês a que a parcela se refere. **Unidade da apuração** |
| **corte** | data **+ eixo** a partir da qual muda a regra |
| **eixo de corte** | **qual fato do processo** se compara com a data do corte |
| **regime** | escolha jurídica sobre *qual regra aplicar*. **Não é negociável por sindicato** |
| **parâmetro** | valor resolvido por `(parâmetro, categoria, competência)` |
| **cadeia temporal** | segmentos `período → regra`, **sem lacuna nem sobreposição** |
| **englobamento** | segmento cujo índice cobre **correção e juros** (SELIC, taxa legal) |
| **regra (A)** | muda quando muda a lei ou a jurisprudência |
| **série (B)** | muda quando o governo publica portaria. **Dado externo, não regra** |

**A distinção (A) × (B) é operacional.** Tabela de IRRF desatualizada é **série a atualizar**;
alíquota mudada por emenda é **regra a bifurcar**.

### A chave de resolução tem três componentes

```
(regra, tribunal, competência)
```

`tribunal` só entra onde há **variante regional cadastrada** — ver **R24**.

---

## Invariantes

**Violadas, produzem erro material.** Devem ser impedidas **na composição**, não detectadas no
resultado. Enunciado completo em
[`../../docs/calculo/consolidado/01-dominio-e-invariantes.md`](../../docs/calculo/consolidado/01-dominio-e-invariantes.md)
§ 2. Abaixo, as que mordem com mais frequência.

### R1 — Exclusividade de englobamento

Segmento cujo `engloba` cobre correção e juros **não admite outro do mesmo componente no mesmo
intervalo**.

> **SELIC e taxa legal englobam correção monetária e juros.** Aplicar correção monetária
> **junto** com qualquer das duas é **erro material**, não escolha de critério: conta a
> inflação duas vezes.

### R2 — Cobertura sem lacuna nem sobreposição

> **Exaustividade se declara, não se presume.** Ramos condicionados só esgotam o domínio se a
> cadeia declarar `dominio_condicoes`. Sem a declaração, o universo "nenhuma condição se
> aplica" continua sendo cobrado.
>
> O conserto que presumia exaustividade **escondia 25 anos de lacuna**.

### R3 — Tipo do indexador na virada

**Três classes desde o bloco 19:** nominal reflete a inflação do mês **anterior**; percentual, a
do **próprio**; **`janela-deslocada`**, metade de cada. **Trocar entre classes sem ajustar desloca
o cálculo em um mês** — e **a régua desse ajuste não existe no corpus** (ver Limitações).

> **A classe de cada índice NÃO se copia para cá:** a fonte é
> `tabelas-normativas/indexadores-tipo-catalogo.json` (o que o validador lê). Classificar por
> semelhança de nome (*"IPCA-E soa percentual"*) é a dedução que o bloco 17 removeu; sem fonte, a
> classe é **`indeterminado`** e a virada **bloqueia** sob `R3-INDETERMINADO`.

### R4 — Capitalização: juros sempre simples

**R4-EXCEÇÃO — juros COMPOSTOS de 27/02/1987 a 03/03/1991**, por força do **DL 2.322/87,
art. 3º**. Mecânica literal: *"1,0% ao mês, c/ taxa capitalizada. Ex.: 3 meses = 3,03%"*.

> **Gravada dentro do invariante, não em nota:** quem ler só "sempre simples" **erra quatro
> anos** de qualquer conta que atravesse o período. Confirmada de forma independente pelas duas
> jurisdições.

**Granularidade divergente entre as fontes:** o TRT-3 dá ao dia (27/02/1987–03/03/1991), o CJF dá
ao mês (mar/87–mar/91). **O corpus justapõe as duas sem enunciar a divergência — a constatação é
composição desta skill, não citação.** Não harmonizada: na virada do mês a escolha muda o número.

### R5 e R6 — Pisos

**R5 — piso nominal.** Índices negativos **entram no cálculo**, mas nenhuma parcela do principal
fica abaixo do nominal. **O piso é por parcela**, não sobre o total.

> A instrução de *"dividir pelo índice negativo"* é **redação defeituosa do original e NÃO se
> implementa**. O que se implementa é R5.

**R6 — piso zero da taxa legal.** Resultado negativo vira **zero**, nunca negativo.

### R7 — Termo inicial dos juros não é intercambiável

| Jurisdição | Termo inicial |
|---|---|
| **Trabalhista** | **ajuizamento** |
| Cível | citação, salvo Súmulas 54 e 362 do STJ |
| Repetição de indébito | trânsito em julgado |

### R8 e R16 — Precedência

**São duas escadas, e não são versões concorrentes da mesma.** R16 **especializa** R8 na camada
de parâmetro, inserindo um degrau que a regra geral não tem.

```
R8  (geral)     título judicial  >  escolha do usuário  >  default da jurisdição
R16 (parâmetro) título judicial  >  norma coletiva da competência  >  escolha  >  default legal
```

> **Onde a norma coletiva entra, ela entra ACIMA da escolha do usuário** — e é isso que R16
> acrescenta. Fora da camada de parâmetro, vale R8, com três degraus.
>
> **Ler a de quatro como se fosse a geral** faz o motor procurar instrumento coletivo onde não
> há categoria; **ler a de três na camada de parâmetro** deixa a escolha do usuário sobrepor a
> CCT. *Fonte do enunciado de R16: `camada-norma-coletiva-schema.json`, que prevalece sobre a
> leitura humana quando divergem — `parametros-negociaveis.md` § 1.*

**Toda divergência entre níveis fica registrada.**

**R16 — título judicial não é barrado pelo piso.** Título que fixe adicional **abaixo do piso** é
**aplicado**, com a divergência registrada.

> **Aplicar a lei contra o título é competência do juízo, não do motor.** É a diferença entre
> calcular e julgar.
>
> **Não confundir com R18**, que é outra regra: cláusula coletiva abaixo do piso é **rejeitada
> sem correção**. O título vence o piso; a cláusula, não.

**Três consequências que o motor precisa honrar:**

1. **título silente não é título contrário** — sentença que nada diz sobre o divisor não afasta
   o IRR-849;
2. **divergir do default é legítimo; esquecer de justificar não é** — R21 rejeita;
3. **o default marca a conta** — é o que permite revisar **o que ninguém decidiu**.

### R9 — Fazenda Pública é atributo do processo

Não é configuração de sistema nem cadastro de empresa. **A mesma parte pode receber
classificações distintas em processos distintos.**

> **E o corpus não resolve quem é Fazenda Pública:** um capítulo isenta os entes *"que não
> explorem atividade econômica"*; outro isenta a administração *"direta e indireta"*, **sem a
> ressalva**. **Dois testes incompatíveis.** Não é matéria de cálculo — é pergunta ao jurídico.

### R10 — Pagamentos parciais

| Jurisdição | Regra |
|---|---|
| **Cível** | imputação pelo **art. 354 do CC** — juros primeiro |
| **Trabalhista** | **proporcional** — `(B/D)×E` principal, `(C/D)×E` juros |

> **Não são duas normas concorrentes.** São **uma norma contra um costume de liquidação sem
> base declarada**: `art. 354` tem **zero ocorrências em 471 páginas**; `proporcional` ocorre
> **101 vezes** só no segmento que o aplica.
>
> Por isso entra como preset **`pr.imputacao`, sem default**. Escolher seria o motor **tomar
> posição jurídica**.

### R11 — Taxa legal é razão entre fatores

**Nunca subtração de percentuais.** Seis decimais, IPCA-15 do mês anterior.

### R12 — Aritmética decimal

**Aritmética decimal exata; ponto flutuante binário proibido no caminho de cálculo** — o tipo
concreto é escolha do implementador (`references/linguagem-alvo-e-aritmetica.md`). E **o critério
de arredondamento é POR ETAPA, não global** — ver a seção seguinte.

### R13 — Reprodutibilidade

Toda conta grava: **preset aplicado**, *overrides* **com justificativa**, **versão do conjunto
normativo**, **versão das séries consumidas**.

### R14 a R18 — Norma coletiva

**R14 — ausência de norma coletiva não é erro.** Competência sem instrumento cadastrado resolve
pelo **default legal** e marca a conta **`sem cobertura coletiva`**.

> **Exceção que quebra a regra geral:** verba **exclusivamente convencional** — como a
> ajuda-alimentação — **não tem default legal**. Sem instrumento **ela não existe**, e a conta
> não a apura. *A diferença entre "vale o legal" e "não existe" é a diferença entre um número e
> uma linha ausente.*

**R17 — a norma coletiva é atributo do CONTRATO**, não do processo nem da empresa. Dois
empregados da mesma empresa, no mesmo processo, podem resolver o mesmo parâmetro de formas
diferentes.

**Derivado não é parâmetro.** O **divisor decorre da jornada** e não se cadastra avulso, sob
pena de admitir o par inconsistente `(jornada 44h, divisor 200)`.

### R19 a R22 — Regime temporal

**R20 — o default marca a conta.** **R21 — divergir exige justificativa**: escolher contra o
default sem justificar é **rejeitado** (`ErroDeDados`, não aviso). **R22 — regime antes de
parâmetro.**

> **`R20-EXCEÇÃO` — quatro presets sem default.** Em três, o corpus deixa a questão aberta. Em
> **`pr.imputacao`**, a prática não tem norma e a norma não tem prática.

### R23 — Descarregar antes de aplicar juros

Antes de aplicar juros sobre saldo remanescente, **os juros já contidos nesse saldo devem ser
excluídos**. Aplicar juros sobre saldo que já os contém produz **anatocismo**.

> **São duas regras anti-anatocismo distintas, que o corpus nunca reúne:** (1) juros acumulam
> por **soma**, nunca por multiplicação — Súmula 121 do STF; (2) o **descarregar**.
>
> **Efeito medido: não descarregar produziria +R$ 30.452,43** num único exemplo. É o maior
> delta de método do corpus.

### R24 — Ausência de súmula regional não é erro

Competência **sem verbete regional cadastrado para o tribunal** resolve pela **regra nacional**
e marca a conta **`sem cobertura regional`**.

> **Mesma forma da R14, e a simetria é deliberada:** `sem cobertura coletiva` e `sem cobertura
> regional` são a mesma espécie de silêncio — **o dado não existe**, não **a regra não existe**.

**R24 não cria exceção à R8:** comando exequendo expresso (art. 879, § 1º, da CLT) afasta o
verbete regional **mesmo dentro da região que o editou**.

---

## Aritmética — as cinco cadeias de arredondamento

**Não há um critério global.** Cinco convivem, e não são intercambiáveis:

| Etapa | Critério | Casas | Fonte |
|---|---|---|---|
| Fator de índice e taxa legal | **truncamento** | 6 | CJF 4.2.1.1, Nota 6 |
| Grandeza física (hora centesimal, nº de HE) | **half-up** | 2 | TRT-3, item 5.3 |
| Valor monetário intermediário e final | **truncamento** | 2 | CJF |
| **NMP** (nº de meses do RRA) | **três ramos** | 1 | IN 1500/14, art. 45, § único |
| Cadeias do capítulo 6 | **quatro práticas não enunciadas** | — | armadilha |

**A regra do NMP não é half-up.** 2ª casa `<5` mantém, `>5` sobe, **`=5` manda olhar a 3ª casa**
(0–4 mantém, 5–9 sobe). **Difere de `ROUND_HALF_UP` na faixa `x,y50` a `x,y54`.**

> **O corpus escreve "arredondamento" onde faz TRUNCAMENTO** (`D8-D33`). CJF `pagina_pdf` **53**:
> *"critério de **truncamento** [...] em cada etapa"*; a **92**, sobre a mesma coisa,
> *"**arredondamento** de casas decimais"*. **Medido: seis células de 4.2.1.1 e 5.2.1 em que
> `ROUND_HALF_UP` dá outro número e o manual publica o truncado** (`1.133,9588923 → 1.133,95`).

### Quatro regras que o motor não pode violar

1. **Precisão plena encadeada.** Os números impressos com 2 casas **não são os operandos**. O
   truncamento é só na **emissão**, e **valor exibido nunca realimenta cálculo** — mesmo que
   parte dos exemplos do corpus o faça;
2. **`1/30` é dízima.** Dividir 1 por 30 em decimal exato, nunca o truncamento impresso — o
   corpus grafa `0,0333%` na regra e `0,03333%` no exemplo **duas linhas abaixo**;
3. **Ponto flutuante binário em lugar nenhum — e a ausência tem de ser VERIFICÁVEL.**
4. **`TRUNCAMENTO POR ETAPA` é MODO, não default — e as fixtures 2 e 4 o exigem.** Os métodos
   **resumido** e **detalhado** do CJF **truncam a 2 casas a cada célula e realimentam o valor
   truncado**. Exceção declarada da regra 1: **rodar em precisão plena faz os dois convergirem
   e zera as divergências de R$ 0,01 e R$ 0,03 que as fixtures asseveram.** O motor precisa dos
   **dois modos**, descritos em `skills/calculo-judicial-atualizacao/references/metodos-resumido-e-detalhado.md`.

> **Consequência que muda o comparador: as colunas impressas do corpus não somam os totais
> impressos**, por 0,01 a 0,02. **O limiar de alarme não deve ser o centavo.**

---

## Procedimento

**A ordem ponta a ponta — dezenove passos, cada um com a fonte da sua posição e o custo medido
de errá-la — está em `docs/calculo/consolidado/09-ordem-de-calculo.md`. Não repetida aqui.**

> **Por que ela mora lá e não aqui.** **O corpus não enuncia a ordem de cálculo do começo ao
> fim** — só a ordem *dentro* de cada operação. A sequência abaixo é **composição declarada**,
> e as marcações `FONTE` / `DERIVADO` / `COMPOSIÇÃO`, o raciocínio de posição e a busca que
> sustenta a negativa ficam naquele arquivo. **Discordar da ordem é legítimo: o ponto exato da
> discordância e o que ele custa estão lá.**

O mínimo operacional desta skill:

```
0. CLASSIFICAR    jurisdição, e se a devedora é Fazenda Pública (R9)
1. REGIME         para cada competência, qual preset vale? (R19-R22)
                  -> sem default: NÃO arbitre. Pergunte ou bloqueie (R20-EXCEÇÃO)
                  -> pr.adc58-item-i ANTES de pr.imputacao: em i.1 nada se rateia
2. PARÂMETRO      resolver (parâmetro, categoria, competência) (R14-R18)
                  -> e (regra, tribunal, competência) para o regional (R24)
3. APURAR         a conta, em decimal exato, precisão plena (R12)
4. ATUALIZAR      cadeia período->regra, sem lacuna (R1-R3)
                  -> se houve pagamento parcial, descarregar ANTES (R23)
                  -> a amortização PARTE a linha do tempo: tudo é trazido até o
                     levantamento, RATEADO ali, e só então levado ao marco final
5. REGISTRAR      preset, overrides com justificativa, versões (R13)
```

**Encargos (honorários, custas de execução) não estão nesta sequência por escopo** — entram nos
passos 17 e 18 da ordem completa, e a skill que os apura é `calculo-trabalhista-liquidacao`.

### Passo 1 é o que mais se erra

**A chave do corte não é a data — é o par `(data, eixo)`.** Dezoito pontos compartilham
11/11/2017 e cortam por **três eixos diferentes**: competência do fato gerador, data de
propositura da ação e modalidade do acordo.

> Dois processos ajuizados no mesmo dia, com parcelas da mesma competência, **recebem respostas
> diferentes**.

### Bifurcação entra com as DUAS versões

**Nunca substitua a antiga pela nova.** Competência anterior ao corte usa a antiga.

> **"Cancelada" quase nunca significa "nunca valeu".** A Res. 225/2025 do TST cancelou 36
> enunciados **declarando, em cada inciso, a data em que o verbete perdeu eficácia** — `a partir
> de` ocorre **27 vezes** no ato. **O TST não revogou: declarou perda de eficácia no passado.**
>
> **Consequência de arquitetura:** o motor **não pode ter uma tabela de regras vigentes**.
> Precisa de **cadeia temporal por ponto**.

---

## Catálogo de critérios

**O que o usuário escolhe é preset, não segmento.** Montar segmento a segmento é o que produz
combinação inválida — R1 e R2 existem para impedir isso **na composição**.

| Camada | Onde está o catálogo |
|---|---|
| Regimes temporais (28) | `docs/calculo/presets-regime.md` |
| Parâmetros negociáveis (32) | `docs/calculo/parametros-negociaveis.md` |
| Cadeias por jurisdição | skill `calculo-judicial-atualizacao` |
| Calendário de cortes | `docs/calculo/consolidado/00-calendario-de-cortes.md` |

**Quatro presets não têm default** e **não devem ser arbitrados pelo motor**.

---

## Comparador

**Fica aqui, não na skill trabalhista:** *"recalcular pelo critério correto e produzir o diff
parcela a parcela"* é a **mesma operação nas quatro jurisdições**.

### O comparador precisa distinguir três coisas

| Classe | O que é | O que fazer |
|---|---|---|
| **erro material** | violação de invariante | **acusar sempre** |
| **delta de método** | decisão legítima que muda o número | **nomear a decisão**, não acusar |
| **comportamento do original** | precisão plena, coluna que não soma | **não acusar** |

### Os deltas de método medidos

| Decisão | Efeito |
|---|---|
| **não descarregar** (viola R23) | **+R$ 30.452,43** — o maior do corpus |
| **ordem de imputação** | até **23,83%** do saldo |
| juros sobre o **nominal** em vez do corrigido | **−2,48%** (−3,15% com vincendos) |
| deduzir INSS **antes** dos juros na base de IR | **−R$ 285,83** |

```
amplitude_imputacao = min(abatimento, principal, juros)
                      × índice_residual × pct_juros_residual
```

> **Armadilha de previsão: qual das três grandezas limita muda de caso para caso.** Quem
> raciocinar só por "quanto de juros há no bruto" erra.

**A ordem entre correção e juros é indiferente** — distributividade, delta `0,00` verificado.
**O que altera é a base.**

---

## Armadilhas conhecidas

**Quinze armadilhas com assinatura detectável**, em
[`../../docs/calculo/armadilhas-comparador.md`](../../docs/calculo/armadilhas-comparador.md) — as de maior valor:

| | Efeito |
|---|---|
| **A1** | FGTS com juros contados **duas vezes** — **+3.802,63** |
| **A2** | bloqueio aritmético — **−2.036,51**, índice sem origem |
| **A4** | linha copiada entre páginas **com a multa junto** |
| **A11** | colchete fechado cedo demais, **propagando** por quatro páginas |

**A regra geral:** o corpus **erra de forma detectável**, porque publica os operandos.

> **Quem resume o corpus não publica nada — e por isso a premissa de quem conduz atravessa
> blocos.** Catorze premissas caíram na extração e **nenhuma veio do corpus**: vieram de quem o
> estava lendo. **Trate premissa de enunciado com o mesmo ceticismo que afirmação de fonte.**

---

## Fixtures de aceite — **dois níveis**

**NÍVEL 1 — o aceite DA SKILL**, executável só com a skill: R11 pelos dois pares publicados, R12
verificável — zero ponto flutuante binário —, R1 na composição, as cinco cadeias e o NMP de três
ramos. **NÍVEL 2 — o aceite do SISTEMA**, não da skill: as **quatro** fixtures de
`tests/fixtures/calculo/`, que **exigem a série de índices — camada (B) —, que esta skill não
carrega por desenho**. Os dois níveis, fixture a fixture: `references/aceite-em-dois-niveis.md`.

**As fixtures 2 e 4 divergem entre o método RESUMIDO e o DETALHADO do próprio manual** — R$ 0,01
e R$ 0,03 —, **não do corpus**. Motor que produz **um** número não passa; motor que **zera** a
diferença está arredondando errado.

**Validadores:** `scripts/calculo/`. **A contagem da suíte não se escreve aqui** — ela vive em
`docs/calculo/consolidado/00-numeros.md` § 5, gerado por script.

```
python scripts/calculo/test_aceite_nivel1.py       # NÍVEL 1 — o aceite DA SKILL
python scripts/calculo/test_valida_cobertura.py    # R1, R2
python scripts/calculo/test_valida_regimes.py      # R19-R22
python scripts/calculo/test_valida_parametros.py   # R14-R18
python scripts/calculo/test_valida_taxa_legal.py   # R6, R11, R12
```

---

## Limitações declaradas

**Esta seção não é rodapé.** Cada linha é um ponto em que o motor **não sabe**, e fingir que
sabe produz número errado com aparência de fundamentação.

| Limitação | Natureza |
|---|---|
| **`pr.imputacao` sem default** | 101 aplicações, **zero fundamentos**; `art. 354` → **0 em 471 páginas**. Arbitrar seria tomar posição jurídica |
| **dois bloqueios aritméticos** | deltas de **10,00 exatos** e **2.036,51 com índice sem origem**. **Nenhum é arredondamento** |
| **classificação como Fazenda Pública** | dois testes incompatíveis no mesmo corpus. **Não é matéria de cálculo** — é pergunta ao jurídico |
| **cadeia trabalhista anterior a 03/1991** | depende da **Tabela Única do CSJT**, ainda **não integrada** (`P9-02`) |
| **súmulas regionais** | cobertura é **TRT-3, TRT-4 e TJMG**. Outras regiões exigem **cadastro, não refatoração** (R24) |
| **modulação da ADC 58** | repousa em **fonte secundária**. O inteiro teor **não foi lido** |
| **art. 85, § 3º, do CPC** e **série histórica de normas coletivas** | **dados externos**, não integrados |
| **a ordem de cálculo ponta a ponta** | **não é enunciada em lugar nenhum do corpus.** O Procedimento acima é composição declarada a partir de R22 e das seções de cada skill — **não citação** |
| **`R4-EXCEÇÃO`** | granularidade divergente entre as duas fontes: uma dá ao dia, outra ao mês. **Não harmonizado** |
| **régua de ajuste de `R3`** | o corpus diz que trocar de classe desloca um mês e **não diz o que fazer**. `aplicacao` (D1–D4) declara *se* há ajuste, não *qual*. `10-literais-na-extracao.md` § 5.2 |
| **as fixtures do CJF só rodam com a SÉRIE carregada** | a fixture 1 sozinha consome **23 meses de IPCA-E**. A série é **dependência externa** — esta skill **não a carrega por desenho**. Por isso são **NÍVEL 2**, aceite do sistema, e o aceite **desta skill** é o NÍVEL 1 |

> **Registrar a pendência é a resposta certa.** Um veredito inventado é pior que uma pendência
> declarada.

---

## Ponteiros

| Para | Vá a |
|---|---|
| **índice de um período** | skill `calculo-judicial-atualizacao` |
| **valor de índice, contrato de série** | skill `indices-judiciais` |
| **verba, desconto, encargo trabalhista** | skill `calculo-trabalhista-liquidacao` |
| enunciado completo de R1–R24 | `docs/calculo/consolidado/01-dominio-e-invariantes.md` |
| os pares `(data, eixo)` | `docs/calculo/consolidado/00-calendario-de-cortes.md` |
| nacional × regional, 15 regras | `docs/calculo/consolidado/08-nacional-e-regional.md` |
| as 15 armadilhas | `docs/calculo/armadilhas-comparador.md` |
| o que está em aberto | `docs/calculo/pendencias.md` |
| **como este corpus se lê** | `docs/calculo/consolidado/07-leitura-do-corpus.md`, e a seção correspondente da skill de liquidação |
