---
name: calculo-trabalhista-liquidacao
description: >-
  Use quando a pergunta for QUANTO SE DEVE num cálculo trabalhista — verbas, reflexos, descontos
  legais e encargos, ANTES de qualquer atualização monetária. Gatilhos: "confira este cálculo de
  liquidação", "revise a planilha do perito", "o INSS está certo?", "quanto dá a rescisão?",
  "horas extras", "qual o divisor desta jornada?", "reflexo de RSR em férias e 13º", "aviso
  prévio proporcional", "insalubridade ou periculosidade", "RRA", "gross-up", "art. 12-A ou
  12-B", "dedução de valores já pagos", "imputação de pagamento parcial", "honorários
  sucumbenciais", "custas de execução", "contribuição sindical", "multa do art. 467 ou 477",
  "o que muda depois da Reforma", "MP 808", "OJ 394". NÃO use para escolher índice ou taxa de
  juros (calculo-judicial-atualizacao), nem para valor de índice (indices-judiciais), nem para
  invariantes e aritmética (calculo-judicial-core).
---

# Liquidação trabalhista — verbas, descontos e encargos

Esta skill responde **uma** pergunta: **quanto se deve, antes de atualizar**.

```
comando exequendo  →  verbas e reflexos  →  descontos legais  →  encargos
```

É a skill que muda quando o **Congresso**, o **TST** ou a **Receita** mexem na regra de apuração. **Não é a
skill que decide índice nem juros.**

---

## Quando usar / quando não usar

**Use quando** a pergunta for sobre *o que compõe a conta*: quais verbas são devidas, qual a base de cada
uma, o que reflete em quê, quanto se desconta de INSS e IRRF, como se abate o que já foi pago, quais
encargos incidem sobre o resultado.

| Não use para | Skill |
|---|---|
| Qual índice corrige de 2015 a 2024; taxa de juros; ADC 58; taxa legal; precatório | `calculo-judicial-atualizacao` |
| Quanto valeu o IPCA-E de mar/2019; faixas de INSS e IRRF **como valores** | `indices-judiciais` |
| R1–R24 na íntegra, aritmética decimal, truncamento, comparador/diff | `calculo-judicial-core` |

**Fronteira que importa, nos dois sentidos:** esta skill diz *"o INSS do mês é 14% sobre a faixa X"* — **ela
não tem a tabela de faixas**; e diz *"a contribuição se atualiza pelos mesmos índices do crédito do
reclamante"* — **ela não sabe quais são esses índices** (`F7-04`). **E um caso de fronteira que não é
fronteira:** a **imputação de pagamento parcial** mora **aqui**, apesar de manipular juros — o que ela
decide não é *qual* juros, é *sobre que base*.

---

## Como este corpus se lê

**Antes de abrir o manual.** Seis padrões confirmados em extração; ignorar qualquer um produziu erro real.
Fonte integral: `docs/calculo/consolidado/07-leitura-do-corpus.md`.

**1 — A regra de cálculo mora no exemplo; o enunciado normativo é minoria do texto.** Regras que só existiam
dentro de exemplo: **cap. 9 → 7**; **cap. 10.1 → 12**; **cap. 11 → 17** estruturais; **cap. 16 → 6**
fundamentos exclusivos. Três das mais consequentes: o **mês comercial de 30 dias com contagem inclusiva**
(`dias = 30 − dia_inicial + 1` — **5 de 5** períodos fecham pela inclusiva, **0 de 5** pela exclusiva; o
divisor está na fórmula impressa, **a convenção de contagem não**); a **precisão plena encadeada** (os
impressos com 2 casas **não são os operandos**); e a **base da multa do art. 467**, que inclui saldo de
salário e a multa de 40% sobre o FGTS — **nenhum dos dois no rótulo**. *Quem ler só os enunciados sai com
menos da metade das regras, e sem as que mais mexem no número.*

**2 — O fundamento pode estar fora do capítulo que executa — seis em trinta e seis.** A varredura do cap. 16
cruzou **36 fundamentos** contra os capítulos técnicos; **a maioria é citada**, seis não. O caso limite: a
**IN SRF 15/2001**, fonte declarada da fórmula de *gross-up*, tem **1 ocorrência em 471 páginas** — enquanto
"bruto em relação ao líquido" ocorre em 16 páginas, 15 delas no cap. 10, que **usa a fórmula em todos os
exemplos e nunca diz de onde ela vem**. Os outros cinco: **Súmula 15 do TRT-3** (cap. 10: zero em 69
páginas), **Súmula 454/TST** (3 ocorrências, todas no cap. 16 — fundamento de `R-07-19`), **Súmula 388/TST +
art. 83 da Lei 11.101/05**, **Prov. 03/91 e art. 104, § 5º, do PGC**, e o **anatocismo aplicado à
amortização** (p. 328; cap. 10: zero).

**3 — "Cancelada" quase nunca significa "nunca valeu".** A **Res. 225/2025 do TST** cancelou 36 enunciados e
**cada inciso declara a data em que o verbete perdeu eficácia** — `a partir de` ocorre **27 vezes** no ato.
O TST não revogou: declarou perda de eficácia **no passado**. Quem registrar *"Súmula 437: cancelada"* e
apagar o verbete **erra todo fato anterior a 11/11/2017** — e o produto calcula passivo anterior. **Cadeia
temporal por ponto, nunca tabela de regras vigentes.**

**4 — Período que parece homogêneo pode ter subjanela.** A **MP 808/2017** vigorou de **14/11/2017 a
22/04/2018** e **não foi convertida**: cinco meses e nove dias **dentro** do período pós-Reforma, com texto
diferente dos dois lados. Quem olha só "antes e depois de 11/11/2017" não vê o terceiro estado. **Passo 3.**

**5 — Fronteira de conteúdo vence fronteira de página.** Nenhuma fronteira interna do cap. 10 é quebra de
página (10.1→10.2 na p. 223, offset 2.658; 10.2→10.3 na p. 237, offset 681; Ex. 4→Ex. 5 na p. 266, offset
2.141). A numeração impressa também não é guia: **para em 10.3.2.1, na p. 239**, e o capítulo segue por mais
38 páginas — **55% dele** — estruturadas só por `Exemplo 1` a `6`.

**6 — Afirmação de ausência exige escopo declarado.** *"Zero ocorrências no segmento"* e *"zero ocorrências
em 471 páginas"* são afirmações diferentes, e **só a segunda sustenta uma negativa sobre o manual**. O erro
mais caro da série foi este: registrou-se em dois blocos que *"a regra de arredondamento do NMP nunca é
declarada"* — **ela é declarada duas vezes**, pp. 226 e 230, com o artigo transcrito. A varredura que a
sustentava cobria só o que já tinha sido extraído. **Toda negativa desta skill vem com o universo em que se
buscou.**

---

## Modelo de domínio

**Três camadas, nesta ordem** (`01-dominio-e-invariantes.md` § 1). Inverter produz número plausível com a
conta inteira no regime errado. **A camada 1 decide se a camada 2 é sequer consultada** — sob
`pr.in-itinere` na variante `suprimidas`, o parâmetro `pn.in-itinere.prefixacao` **não existe**, não é que
valha zero.

```
1. REGIME TEMPORAL   qual REGRA vale nesta competência?        R19–R22
2. PARÂMETRO         quanto VALE o que a regra manda aplicar?  R14–R18
3. APURAÇÃO          a conta                                   R1–R13, R23
```

| Termo | Significado exato |
|---|---|
| **competência** | o mês a que a parcela se refere. **Unidade da apuração** |
| **corte** · **eixo de corte** | **data + eixo** a partir do qual muda a regra · **qual fato do processo** se compara com a data |
| **base de cálculo** | composição "no rigor dos arts. 457 e 458" — item 6.1 |
| **reflexo** | **dois sentidos que o motor não pode confundir:** (a) pôr a parcela **na base** de outra verba; (b) pôr a **média física** de uma verba na base de outra (Súmula 347) |
| **regra (A)** · **série (B)** | muda com lei/jurisprudência — vive aqui · muda com portaria: **dado externo**, `indices-judiciais` |

> **Quase tudo no capítulo 9 é (A).** Série (B) desatualizada é **defeito de cobertura** — recarrega-se.
> Regra (A) superada é **defeito de correção** — **inverte o resultado**.

**O divisor é DERIVADO, não parâmetro cadastrável.** Decorre da jornada — art. 64 da CLT e tese 3 do
IRR-849. **Não pode ser cadastrado avulso**, sob pena de admitir o par inconsistente **`(jornada 44h,
divisor 200)`**. Corolário: o **210 da 12×36 é atributo do regime de jornada**, não valor negociável — quem
o cadastrar como parâmetro cria a possibilidade de uma 12×36 com divisor de 44 horas. Por isso a variante
`enquadrado-sexta-diaria-divisor-180` **foi removida** no bloco 5, com teste que impede a reintrodução
(`test_nenhuma_variante_embute_um_derivado`).

**Ausência de norma coletiva não é erro — R14.** Competência **sem instrumento cadastrado** resolve pelo
**default legal** e marca a conta como **`sem cobertura coletiva`**. Não bloqueia, não erra: **registra**.

> **Exceção, e é a que quebra a regra geral:** verba **exclusivamente convencional** — como a
> **ajuda-alimentação** — **não tem default legal**. Sem instrumento, ela **não existe**, e a conta **não a
> apura**. A diferença entre *"vale o legal"* e *"não existe"* é a diferença entre **um número e uma linha
> ausente**.

**R17** — a norma coletiva é atributo do **contrato**: dois empregados da mesma empresa, no mesmo processo,
podem resolver o mesmo parâmetro de formas diferentes. **R18** rejeita e registra cláusula abaixo do piso
legal — **não corrige**.

---

## Invariantes

**Não reproduzidas aqui.** Enunciado integral de **R1 a R24** em
`docs/calculo/consolidado/01-dominio-e-invariantes.md` § 2, e em `calculo-judicial-core`.

| ID | Onde morde nesta skill |
|---|---|
| **R8** | **título judicial > escolha do usuário > default.** *"O calculista deverá observar estritamente as decisões existentes nos autos"* (`R-07-06`). **Título silente não é título contrário** |
| **R9** | Fazenda Pública é atributo do **processo** — e **o manual não resolve quem é** (Limitação 6) |
| **R10** | pagamentos parciais: trabalhista = **proporcional**, `(B/D)×E` e `(C/D)×E`; cível = art. 354 do CC. **Não intercambiáveis** |
| **R12** | **cinco cadeias de arredondamento convivem e não são intercambiáveis.** Grandeza física (hora centesimal, nº de HE): **half-up, 2 casas**. **NMP: três ramos, não é half-up.** Cadeias do cap. 6: **quatro práticas não enunciadas** (`P10`/`P17`) |
| **R14 · R17 · R18** | norma coletiva — acima |
| **R19** | **obrigatória.** Toda conta que atravesse um corte grava, **por competência**, qual lado aplicou |
| **R20 · R20-EXCEÇÃO · R21 · R22** | default marca a conta; **`pr.imputacao` não calcula sem escolha**; divergir sem justificar é **`ErroDeDados`**, não aviso; **regime antes de parâmetro** |

**`R23` — descarregar antes de aplicar juros.** Antes de aplicar juros sobre saldo remanescente, **os juros
já contidos nesse saldo devem ser excluídos**; do contrário há **anatocismo**. Efeito medido no Exemplo 5 do
cap. 10: **+R$ 30.452,43** — **o maior delta de método do corpus**.

> **Anomalia de localização do fundamento — é o § 2 de "Como este corpus se lê" em estado puro.** O manual
> **executa** a operação em todo o **capítulo 10** e a nomeia apenas como *"descarregar"* (p. **237**,
> **única ocorrência da palavra**), **sem fundamentá-la**: `anatocismo` tem **zero ocorrências no capítulo
> 10 inteiro**. Quem a qualifica é uma **minuta de petição do capítulo 16** (p. **328**), que abre com a
> **mesma frase** do item 10.3.1 e acrescenta: *"não incidindo juros sobre juros (anatocismo), vedada por
> Lei"*. **São duas regras anti-anatocismo distintas que o manual nunca reúne:** (1) juros acumulam por
> **soma**, nunca por multiplicação — p. 16, **única invocação da Súmula 121 do STF**; (2) o **descarregar**.

**`R24` — ausência de súmula regional não é erro.** Competência **sem verbete regional cadastrado para o
tribunal** resolve pela **regra nacional** e marca a conta como **`sem cobertura regional`**. **Não
bloqueia, não erra: registra.** É a mesma forma da R14, e a simetria é deliberada — os dois silêncios
significam **o dado não existe**, não **a regra não existe**. Chave:
**`(regra, tribunal, competência)`** — `regra` é o **ponto de cálculo**, não o verbete; `tribunal` só entra
onde há variante **cadastrada**; `competência` é necessária porque **verbete regional nasce e morre com
data**. **R24 não cria exceção à R8:** comando exequendo expresso (art. 879, § 1º, da CLT) afasta o verbete
**mesmo dentro da região que o editou**. E **silêncio do tribunal não é adesão ao verbete de outro
tribunal** — sem súmula própria sobre divisor na 12×36 aplica-se **IRR-849 / Súmula 431**, não a OJ 23.

---

## Procedimento

**A ordem ponta a ponta — dezenove passos, com `FONTE` / `DERIVADO` / `COMPOSIÇÃO`, o raciocínio de posição
e o custo medido de errá-la — está em `docs/calculo/consolidado/09-ordem-de-calculo.md`. Não repetida aqui.**

> **O corpus não enuncia a ordem do começo ao fim**, só a ordem *dentro* de cada operação. Os
> passos abaixo são **composição declarada**: três posições são `COMPOSIÇÃO` pura — **verbas**,
> **bloco de descontos**, **encargos** —, e uma tem custo medido (**−R$ 285,83**).

### Passo 0 — a chave não é a data, é o par `(data, eixo)`

**Dezoito pontos compartilham 11/11/2017 e cortam por três eixos diferentes.** *Dois processos ajuizados no
mesmo dia, com parcelas da mesma competência, recebem respostas diferentes conforme o eixo.*

| Eixo | Quem usa |
|---|---|
| **competência do fato gerador** | os **quinze** pontos da Reforma; `F7-01`, `F7-05`, `F7-09`, `C12-01` |
| **data de propositura da ação** | **`C8-01`** — honorários advocatícios, e **só ele** |
| **trânsito em julgado** · **data em que a HE foi trabalhada** · **ciência da lesão** | `F7-10` (GPS → DARF 6092) · `F4-01` (OJ 394 / Tema 9) · `B04-F7` (prescrição do FGTS) |
| **início do aviso · data da sentença · data da dispensa · data de admissão** | `pr.aviso-proporcional` · `pr.multa467-base` · seguro-desemprego · `pr.periculosidade-eletricitarios` |
| **modalidade · natureza · setor · opção** — **não temporais** | `F7-06` (acordo), `F7-02` (desoneração), `C12-03` (assistencial) |

### Passo 1 — resolver o regime temporal antes de tudo (R22)

Avaliar os presets aplicáveis a **cada competência** e gravar por competência (R19). **Granularidade:**
cortes ao **dia**, motor indexado por **competência mensal** — novembro de 2017 fica dos dois lados, e o
resolvedor **recusa** (`competencia-atravessa-o-corte`) em vez de convencionar. **A recusa é visível; a
convenção não.**

### Passo 2 — bifurcação entra com AS DUAS versões

```
BIFURCADO   → as duas versões entram, com corte e eixo declarados.
              NUNCA substituir a antiga pela nova. Competência anterior ao corte USA A ANTIGA.
SUPERADO    → a vigente entra; a do manual vai para armadilhas, COM A DATA DE CORTE.
INAPLICÁVEL → fora, com a razão registrada.      SEM FONTE → pendência. NUNCA regra.
```

> **O erro que esta regra existe para não cometer.** Quinze pontos cortam em **11/11/2017** e o produto
> calcula passivo anterior. **Apagar a regra antiga destrói o cálculo de todo contrato pré-Reforma.** O
> Pleno do TST, no próprio caso líder do Tema 23, **manteve a condenação em horas *in itinere* até
> 10/11/2017** — é a prova mais forte de que estes pontos são **bifurcação, não supersessão**.

**Catálogo das trinta bifurcações, cada uma com as duas versões, o corte e o eixo:**
`references/cortes-e-bifurcacoes.md`. **Não repetido aqui.**

### Passo 3 — checar a subjanela da MP 808/2017 (14/11/2017 a 22/04/2018)

**Três colunas, não duas.** A MP vigorou cinco meses **dentro** do período pós-Reforma, com texto
**diferente dos dois lados**: abonos integravam, prêmios só ficavam fora se pagos até 2×/ano, a
12×36 exigia norma coletiva.

> **Uma parcela de competência janeiro/2018 não segue nem a regra antiga nem a da Reforma. Segue a
> MP.** É a variante mais fácil de perder, porque quem olha "antes e depois de 11/11/2017" não vê
> que há um **terceiro estado no meio**.

**Afeta** `B03-F1`, `B03-F2`, `B03-F3`, `B03-F6`, `B04-F3`, `B04-F5` e `F7-05`. **Não afeta
`F7-06`** — o acordo extrajudicial corta pela **modalidade**, e a MP não tocou no art. 855-B.

**Variante V-05, registrada e não arbitrada.** Tabela das cinco linhas e as duas posições em
[`references/cortes-e-bifurcacoes.md`](references/cortes-e-bifurcacoes.md).

### Passo 4 — apurar verbas e reflexos

Espinha verba a verba em
[`references/verbas-catalogo.md`](references/verbas-catalogo.md), que traz também os cinco pontos
que mais escapam. **Os dois de maior efeito:**

- **mensalista: o RSR já está no salário** (Dec. 605/49, art. 7º, § 2º) — calculá-lo em separado é
  **contar duas vezes**. E **RSR não abrange feriados**: a distinção é **limite de coisa julgada**;
- **cumulação de insalubridade e periculosidade é vedada** (Tema Repetitivo 17): calcular os dois,
  aplicar o maior, **registrar o descarte**. O adicional noturno é cumulável com ambos.

### Passo 5 — descontos: INSS **sempre** antes do IR

`R-07-01`. *"O desconto previdenciário precede sempre ao desconto do IR"*; *"as bases de cálculo dos
descontos previdenciários e fiscais são **diferentes**"*. A base do IR é o **líquido de INSS**. **`R-07-21`
— no INSS pergunta-se *a verba é salarial?*; no IR, *a lei isenta?*** Usar o mesmo teste nos dois é erro de
método, **e o manual o diz expressamente**. Detalhe: `references/descontos-inss-irrf.md`.

### Passo 6 — o arredondamento do NMP, que **não é half-up**

**A regra É declarada** — pp. **226** e **230**, com o artigo transcrito: **parágrafo único do
art. 45 da IN 1500/14**, **três ramos**. 2ª casa `<5` mantém, `>5` sobe, **`=5` manda olhar a 3ª
casa** (0–4 mantém, 5–9 sobe).

> **Difere de `ROUND_HALF_UP` na faixa `x,y50` a `x,y54`.** Entra como **regra literal**, não como
> inferência — e o projeto já afirmou duas vezes, por engano, que ela não era declarada.

**Limite de verificabilidade, declarado:** **nenhum exemplo do corpus exercita o ramo `=5`**.
Detalhe e a pendência `P13A-05` em
[`references/descontos-inss-irrf.md`](references/descontos-inss-irrf.md).

### Passo 7 — imputação do que já foi pago

**A amortização não é um passo a mais no fim.** Tudo é trazido até a data do levantamento, **rateado ali**,
e só então levado ao marco final. **O valor pago é deduzido NOMINAL** — o que se atualiza é o crédito, e
nenhuma linha de levantamento tem coluna de índice. **Antes de tudo, descarregar (R23).**

**São DUAS molduras no capítulo 10, e os exemplos seguem a segunda.**

| Passo | **10.3.1** (A–H, **J**; **sem letra I**) | **10.3.2** (A a **O/P**; **COM letra I**) |
|---|---|---|
| **rateio proporcional** | **F** | **G** |
| atualizar principal · atualizar juros · soma final | **G** · **H** · **J** | **H** · **I** · **J** |

```
F.1  principal no saldo = (B / D) × E        F.2  juros no saldo = (C / D) × E
```

> **Ler o capítulo 10 com um letreiro só produz erro de endereço.** Os **Exemplos 5 e 6 seguem 10.3.2**, e
> **"não há letra I" vale só para 10.3.1** — sobre o capítulo inteiro, apaga a de 10.3.2 (`P10D-05`).

**Sobre o quê incide:** **10.3.1** (sem descontos) sobre o **bruto**; **10.3.2.1** (com descontos) sobre o
bruto **já reduzido do INSS e IR proporcionais ao levantamento**, **rateados também** — **são dois momentos
de desconto, não um**. **E o rateio de 10.2 não é o de 10.3:** em **10.3** rateia-se **principal × juros**;
em **10.2**, **bruto → INSS** — objetos distintos, **e nenhum dispositivo citado para nenhum dos dois**.
Detalhe: `references/imputacao-e-amortizacao.md`.

### Passo 8 — encargos, e a ordem entre eles

1. **honorários advocatícios** sobre o **bruto do reclamante + FGTS a depositar**, **excluída a cota
   patronal** (OJ 348 e **TJP 4 do TRT-3**);
2. **custas de execução** — `R8-CE-01`, **invariante promovida de exemplo**: `0,5%` sobre o **total do
   cálculo ANTES da própria linha de CE**, excluídas **apenas** as custas do conhecimento, teto R$ 638,46.
   **Os honorários entram nessa base** (8.2.1, literal) — por isso vêm antes;
3. **R19** — gravar qual lado de cada corte foi aplicado; para `C8-01`, gravar a **data de propositura**.

**Gratuidade muda a conta:** sendo o reclamante beneficiário, os honorários sucumbenciais devidos por ele
**não podem ser abatidos do seu crédito** (ADI 5766, *ex tunc*) — **some uma parcela da cadeia de descontos
sobre o líquido**. Detalhe: `references/encargos-processuais.md`.

### Passo 9 — registrar (R13, R19, R20, R21)

Preset aplicado por competência, *overrides* com justificativa, versão do conjunto normativo, versão das
séries consumidas. Default marca a conta (`origem: "default"`). **Divergir do default sem justificar é
rejeitado**, não avisado.

---

## Catálogo de critérios

**Presets de regime temporal** — família distinta dos presets de atualização. **28 regimes,
catorze eixos de corte distintos.** Catálogo completo em
**[`references/cortes-e-bifurcacoes.md`](references/cortes-e-bifurcacoes.md)**; fonte em
`docs/calculo/presets-regime.md`.

**Na espinha ficam só os que BLOQUEIAM a conta** — os quatro sem default, que o motor **não deve
arbitrar**:

| Preset | Decide | Por que sem default |
|---|---|---|
| **`pr.imputacao`** | proporcional × art. 354 do CC | **a prática não tem norma e a norma não tem prática** |
| `pr.he-adicional-cf88` | adicional de 20/25/50% | corpus deixa aberto; **eixo não declarado** |
| `pr.tema1046-validade-clausula` | cláusula que limita direito | corpus deixa aberto; **eixo não declarado** |
| `pr.sumula17-salario-profissional` | — | corpus deixa aberto |

**Dois presets com default que o motor erra se ignorar:** `pr.adc58-item-i` (default **i.1**, e é
avaliado **antes** de `pr.imputacao` por R22) e `pr.intertemporal` (default *tempus regit actum*,
pelo **Tema 23 do TST** — a ultratividade segue disponível **mediante justificativa**, R21).

**Um bloqueado por falta de dado, não por dúvida:** `pr.planos-economicos` — dez planos,
1986–1996, **sem série** (`P19`).

### Parâmetros negociáveis (R14–R18) — a direção vem do art. 611-B

**A âncora é o artigo, NÃO a presença de "no mínimo" no texto de cada dispositivo.**

> **É a anti-heurística que este catálogo existe para impedir.** Procurar "no mínimo" parece
> funcionar e classifica errado. **O teste é: o 611-B alcança este parâmetro, e por qual via?**

| Via do art. 611-B | Direção | Parâmetros concretos |
|---|---|---|
| **inciso** alcança o parâmetro | **`apenas-elevacao`** (↑) | **insalubridade** e **periculosidade** (inciso XVIII); **adicional noturno** (inciso VI) |
| **parágrafo único** — duração do trabalho e intervalos, que **expressamente não são** normas de saúde para este fim | **`qualquer`** (↔) | jornada, intervalos |
| demais | **`qualquer`** (↔), sob o **Tema 1046** | — |

**Derivado (ƒ) não é nenhuma das duas:** o divisor decorre da jornada e **não se sobrescreve**.
**Lacuna declarada: 27 dos 30 incisos não estão no corpus**, e **16 parâmetros seguem com
`classificacao_provisoria: true`** — inventário em `docs/calculo/parametros-negociaveis.md` § 8.

### As regras REGIONAIS — quinze, de três tribunais

**Não três.** Nove verbetes (**RG1–RG9**) e seis fontes regionais não-verbete (**RG10–RG15**), de
**TRT-3**, **TRT-4** e **TJMG**. Tabela completa — verbete, tribunal, ponto de cálculo alterado e
**fallback nacional** de cada uma — em **[`references/regras-regionais.md`](references/regras-regionais.md)**.

> **Rótulo `RG`, não `R`.** As invariantes já ocupam `R1`–`R24`; usar `R` para as regionais
> reintroduziria a colisão de etiquetas que o projeto já pagou uma vez.

**As três que o enunciado do bloco 16 nomeava** — Súmula 15 (data da dedução), Súmula 46 (base da
insalubridade) e OJ 23 das Turmas (divisor 210 na 12×36), **todas do TRT-3** — são **um quinto** do
que a varredura encontrou.

> **A aritmética do manual do TRT-3 NÃO é prática regional divergente** — divisores, RSR,
> arredondamento, ordem INSS→IR, reconstrução de bruto, hora centesimal. É **procedimento de uma
> região que aplica norma nacional**. Regional são **os verbetes que ele invoca**.

**Fallback nacional identificado para catorze das quinze.** A exceção é **RG15** (`P9-02`) — lacuna
aberta, não escolha.

---

## Armadilhas conhecidas

**Quinze armadilhas com assinatura detectável.** Catálogo completo, com operandos, páginas e o
delta de cada uma, em
[`../../docs/calculo/armadilhas-comparador.md`](../../docs/calculo/armadilhas-comparador.md).

As que mais mexem no número:

| | Onde | Efeito |
|---|---|---|
| **A11** | pp. 227, 231 → 244, 250 | **colchete fechado cedo demais** na fórmula do bruto. Seguida à risca: **−3.771,73** e **−3.071,48**. *Fórmula errada, resultado certo* — a forma correta está na p. 233. **Com `INSS = 0` as duas leituras coincidem**, e os exemplos do art. 12-B usam INSS zero: **não exercitam o defeito** |
| **A1** | p. 297 | juros do FGTS **contados duas vezes** — excesso de **3.802,63**, exatamente a linha de juros já embutida nos `36,333333%` |
| **A4** | p. 223 (origem: 261) | **linha copiada com a multa junto** — **+125,11 e +1.168,21, que são 20% de outra coluna** |
| **A7** | p. 244 | **gross-up com sinal invertido**, **−4.100,21** |
| **A12** | pp. 132, 280 | rótulo que **ignora o juro Selic da cota-reclamante**. Reclassifica `P10-18` de divergência normativa para **defeito de rótulo** |

**Um padrão que se repete três vezes** (`A7`, `A11`, `A13`): **rótulo ou fórmula errada, resultado
certo.** Conferir só a fórmula impressa acusa erro que não existe; conferir só o total não acha o que
existe. **Precisa dos dois.**

**Três que não são defeito do corpus — e são de leitura:**

- **ficha de tema localiza o acórdão; não o substitui.** A do **Tema 9** transcreve o mérito e
  **omite a modulação** — quem consultar só ela conclui `SUPERADO` onde o correto é `BIFURCADO`, e
  **apaga todo o passivo anterior a 2023**. A do **Tema 23** está pior: *"Tese Firmada"* **em branco**;
- **`E14-02`, interna ao projeto:** a base **ainda invoca como vigentes** as Súmulas **90**, **423** e
  **437**. A 423 é a mais grave — sustenta o turno de revezamento e perdeu eficácia em **14/06/2022**.
  **Registrado, não corrigido**;
- **o que o comparador NÃO deve acusar:** a aritmética roda em **precisão plena** e as colunas
  impressas **não somam os totais impressos** por 0,01–0,02. **Não existe regra de arredondamento
  monetário no corpus** — busca nas **471 páginas**: `arredond` → **5, todas sobre o NMP**; `casas
  decimais` → **0**; `truncad` → **0**. **O limiar de alarme não deve ser o centavo.**

---

## Fixtures de aceite

**Entrada e saída esperada — o exemplo de aceite é esta tabela, não código.** Todos conferidos em aritmética decimal exata no bloco de origem.

| # | Caso | Esperado |
|---|---|---|
| **1** | INSS, **alíquota única sobre o total** (método até a competência 02/2020), pp. 131, 133, 135 | `951,99 × 9,00% = 85,68` · `1.085,60 × 8,00% = 86,85` · `1.675,98 × 11,00% = 184,36` |
| **2** | Honorários advocatícios, p. 106 | base `264.131,80 + 13.206,59 = 277.338,39`, **excluída** a cota patronal de `18.574,26`; 15% = **`41.600,76`** (o rótulo `277.338,69` é `A13`) |
| **3** | Custas de execução, p. 163 — `R8-CE-01` | `4.502,08 → 22,51 → total 4.524,59` |
| **4** | Fórmula do bruto levantado: `TB = 412.023,32`, `IPIR = 0,8340`, `INSS = 1.871,37`, `ALIQ = 27,5%`, `TL = 282.500,00`, `PD = 723,95425`, `NMP = 48,5` | **`322.389,94`** com o colchete correto. `318.618,21` é a leitura literal de `A11` |
| **5** | Contribuição sindical do empregador sobre capital social de R$ 28 milhões | **`11.572,82`** |
| **6** | Base do IR do levantamento de `282.500,00` — **bifurcação declarada quatro vezes no segmento** | **`38.425,68`** com juros · **`13.551,75`** sem. **É parâmetro do método, não defeito** |
| **7** | Amplitude da escolha de imputação — `min(abatimento, principal, juros) × índice_residual × pct_juros_residual` | EXEMPLO 10.3.1 `36,60` (0,25%) · **Ex. 1 `9.918,92` (23,83%)** · Ex. 5 `22.272,55` (15,85%) · Ex. 6 `2,51` (0,05%) |
| **8** | Não descarregar (violação de `R23`), Exemplo 5 do cap. 10 | **`+30.452,43`** — o maior delta de método do corpus |
| **9** | Dedução de HE pagas (OJ 415), comando silente · deduzir INSS **antes** dos juros na base do IR | `98,26` pelo critério do **valor** × `98,19` pelo do **número** — **a escolha move o resultado** · **`−R$ 285,83`** |
| **10** | Base das custas de execução no exemplo da p. 280 — `A12` · honorários periciais da p. 104 | `28.416,25 + 606,12 + 1.290,44 = 30.312,81`, e **não** `30.277,52`; delta **35,29** = `606,12 − 570,83` · o total soma honorários **líquidos + o IR do perito**, lançado **separadamente** (art. 106, § 2º, "h") |

**Os dois bloqueios entram como fixture NEGATIVA** — nenhum fecha, e **nenhum é arredondamento**: p. **266**
(`A3`), delta de **10,00 exatos** na coluna K; p. **269** (`A2`), delta de **2.036,51** com índice implícito
`1,00257222` que **não corresponde a índice algum do exemplo** — e `55.236,01` **não existe em nenhuma das
471 páginas**. **Um motor que "fecha" essas duas está forçando o número.**

---

## Limitações declaradas

**Não é rodapé. É o que impede usar a skill fora do que ela sustenta.** **As sete que bloqueiam a
conta**, com a consequência de cada uma — mais **três de menor alcance** (RIR/99 com endereços
quebrados; divergências não arbitradas, entre elas **`F7-03`, Tema 808 × OJ 400**; e pendências de
extração), só no companheiro. Busca, operandos e pendência de cada item em
**[`references/limitacoes-declaradas.md`](references/limitacoes-declaradas.md)**.

| # | Limitação | O que o motor NÃO pode fazer |
|---|---|---|
| **1** | **Súmulas regionais cobrem TRT-3, TRT-4 e TJMG — e só esses três.** Quinze regras de **três** tribunais (TRT-3, TRT-4, TJMG) | Tratar silêncio de outro tribunal como adesão ao verbete alheio. **Outras regiões exigem cadastro, não refatoração** — a chave `(regra, tribunal, competência)` já existe (**R24**) |
| **2** | **Dois bloqueios aritméticos abertos** — pp. 266 e 269. Deltas de **10,00 exatos** (`P11B-01`) e **2.036,51** (`P10D-01`) | Tratá-los como arredondamento. **Nenhum é.** O segundo **propaga**: J `138.448,90 → 140.485,41`; IR `4.162,83 → 4.468,30` |
| **3** | **`pr.imputacao` sem default** — **101 aplicações, zero fundamentos**; `art. 354` → **0 ocorrências em 471 páginas**, `proporcional` → **101** no segmento que a aplica | Arbitrar. **Seria tomar posição jurídica.** Amplitude **até 23,83%**; juros primeiro favorece o **credor**, proporcional favorece o **devedor**. `P11B-07` |
| **4** | **Art. 85, § 3º, do CPC e série histórica de normas coletivas são DADOS EXTERNOS.** A regra estrutural das faixas está fechada; **os valores não** | Calcular honorários por faixa. E `pr.planos-economicos` fica **bloqueado por falta de série** (`P19`) — dez planos, 1986–1996 |
| **5** | **Base das custas de execução definida SÓ POR EXCLUSÃO** (`P13B-01`). O item 8.2.1 diz o que **sai**, nunca o que **entra** | Escolher entre bruto e líquido. `bruto` e `líquido` → **zero ocorrências nos itens 8.2 e 8.2.1**. **O eixo não é endereçado. Resolver seria inventar** |
| **6** | **Fazenda Pública: dois testes incompatíveis no mesmo corpus.** Cap. 8 isenta quem *"não explore atividade econômica"*; cap. 14 isenta a administração *"direta e indireta"*, **sem a ressalva** | Classificar sozinho. **Não é matéria de cálculo** — é pergunta ao jurídico do usuário do módulo. Os dois ramos ficam registrados. **Não harmonizo** |
| **7** | **Pontos em FONTE SECUNDÁRIA:** item "i" da ADC 58 (STF em **HTTP 403**, inteiro teor **não lido**), Tema 833, **percentuais da Lei 14.973/2024** (*lei não lida*, secundária com erro comprovado), ADI 5766, Súmula 362 | Usar em produção sem conferir. O da Lei 14.973/2024 está marcado **"NÃO USAR SEM LER A LEI"** |

> **Uma armadilha dentro da limitação 3:** o Exemplo 5 tem **quase o dobro** da participação de
> juros do Exemplo 1 e amplitude percentual **menor** — ali o limitante é o **abatimento**, não os
> juros. **Qual das três grandezas limita muda de caso para caso.**

> **Registrar a pendência É a resposta certa.** Uma skill que "resolvesse" qualquer das sete
> estaria inventando.

## Ponteiros

| Assunto | Onde |
|---|---|
| **Verbas, base de cálculo, os quinze pontos da Reforma, MP 808** | `docs/calculo/consolidado/03-verbas.md` |
| **INSS, IRRF, RRA, rateio sob pagamento parcial** | `consolidado/04-descontos.md` · `04-descontos-detalhe.md` |
| **Amortização, rateio, descarregar, item "i" da ADC 58** | `consolidado/05-imputacao.md` |
| **Custas, honorários, sindical, precatórios** | `consolidado/06-encargos.md` |
| **R1–R24, íntegra** · **os pares `(data, eixo)`** | `01-dominio-e-invariantes.md` · `00-calendario-de-cortes.md` |
| **Como este manual se lê** (fonte da seção homônima) | `consolidado/07-leitura-do-corpus.md` |
| **Nacional × regional, as 15 regras e os fallbacks** | `consolidado/08-nacional-e-regional.md` |
| **Vereditos** — B03-F*, B04-F*, F4-*, F7-*, C8-*, C12-*, C14-* | `confronto-normativo/01-vereditos.md` |
| **Defeitos do original, com assinatura detectável** · **pendências** | `armadilhas-comparador.md` · `pendencias.md` |
| **Presets de regime temporal** (28 regimes, 14 eixos) · **parâmetros negociáveis** | `presets-regime.md` · `parametros-negociaveis.md` |
| **Correção e juros** · **séries e faixas** · **invariantes e aritmética** | `skills/calculo-judicial-atualizacao/` · `skills/indices-judiciais/` · `skills/calculo-judicial-core/` |

**`references/` — carregue apenas o arquivo do ponto em questão:**

```
cortes-e-bifurcacoes.md     as 30 bifurcações, cada uma com AS DUAS versões, corte e eixo
verbas-catalogo.md          verba a verba: base, fórmula, reflexos, divisores, adicionais
descontos-inss-irrf.md      fato gerador, alíquota única × progressiva, 12-A × 12-B, NM, RRA
imputacao-e-amortizacao.md  as duas molduras do cap. 10, rateio, ADC 58 item "i", data da dedução
encargos-processuais.md     custas, honorários, gratuidade, sindical, precatórios
regras-regionais.md         as 15 regionais com tribunal e o fallback nacional de cada uma
```

> **A separação não é estética.** `cortes-e-bifurcacoes.md` muda quando o Congresso ou o TST mexem
> na regra; `regras-regionais.md` é **entrada de catálogo** — cadastrar outro tribunal não toca em
> nenhum dos outros.
