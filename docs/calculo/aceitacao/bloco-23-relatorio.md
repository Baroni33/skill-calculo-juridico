# Bloco 23 — corrigir o que a aceitação apontou

**Estado: fechado.** As seis tarefas feitas, a validação adversarial rodada, e **três `GRAVE` que
ela achou no próprio trabalho deste bloco** corrigidos.

> **Registro datado.** Números do fechamento; não se atualizam. Estado corrente em
> [`../consolidado/00-numeros.md`](../consolidado/00-numeros.md).

| | Antes | No fechamento |
|---|---|---|
| Testes | 311 | **406**, com **3 `skipTest` declarados** |
| Arquivos de teste | 7 | **10** |
| Fixtures reproduzidas pelos dois métodos | **0** | **4.435,07 / 4.435,04 · 3.484,95 · 5.218,28 / 5.218,27** |

---

## 1. O maior achado: os dois métodos existiam e ninguém os tinha extraído

**A aceitação concluiu que a asserção central das fixtures era inalcançável:** *"método resumido"*
e *"método detalhado"* **nunca foram definidos no repositório**, e as fixtures 2 e 4 asseveram
divergência **entre eles**.

**Estavam no manual — e nenhum item sozinho os entrega.**

| Item | O que tem |
|---|---|
| **5.2.1** (pp. 90–91) | **define os dois em prosa** e **não imprime fórmula** |
| **4.2.1.1** (pp. 51–53) | **não define nenhum em prosa** e **imprime a legenda de fórmula** das colunas |

> **Cruzados, fecham.** O bloco 8 capturou os resultados e não os procedimentos porque **leu cada
> item isolado**. É o padrão *"a regra mora no exemplo"* numa forma nova: **a regra mora na
> interseção de dois itens que não se citam**.

**Achado normativo que o repositório não tinha:** o manual declara o **resumido como default** —
*"deve-se utilizar o cálculo resumido"* (5.2.1, p. 90).

### Onde divergem, nomeado na operação

**A hipótese do truncamento por etapa confirmou-se, e é causa única** — verificada reproduzindo
os três exemplos em `Decimal`, célula a célula.

| Fixture | Δ | A operação exata |
|---|---|---|
| **2** | **R$ 0,01** | **correção do bloco de juros acumulado, set/2025 → jun/2026.** Resumido `Σ(G)+Σ(H) = 1.565,74`; detalhado `trunc(1.503,02 × 1,0417234826) = 1.565,73`. **Principal e juros de 7,03% são idênticos** |
| **4** | **R$ 0,03** | **a subtração do pagamento.** Truncar o subtraendo (`22.192,058973 → 22.192,05`) empurra o resíduo **para cima**. **Honorários idênticos** |

**Sem truncamento os dois caminhos são o mesmo produto em ordem trocada** — comutatividade,
verificada a 60 dígitos.

**E duas correções à hipótese:** **não é a contagem de truncamentos, é QUANDO se trunca** — a
perda de `0,01123787` que o detalhado faz em `55,75` chega amplificada a `0,01684`, **maior que o
centavo em disputa**; e **truncar em subtraendo inverte o sinal do desvio**.

### Dois achados extras sobre o original

**`D8-D33` — a p. 92 escreve *"arredondamento"* e faz truncamento.** Seis células medidas em que
`ROUND_HALF_UP` dá outro número e o manual publica o truncado. **Quem ler ao pé da letra não
obtém 4.435,04.**

**`D8-D32` confirmado por renderização a 250 dpi:** a p. 52 **imprime mesmo `R$ 5.218,2`** —
defeito do original, não da camada de texto.

---

## 2. A classificação de índices: eram duas divergências, são nove

A aceitação apontou **duas**. A varredura achou **sete a mais**, sobre **31 arquivos contados**:

- `indices-judiciais/SKILL.md` publicava *"Dez dos vinte e oito ficaram `indeterminado`"*
  **contradizendo a própria tabela três linhas acima**;
- a enumeração `indeterminado (17)` **omitia `JAM`** — o catálogo tem 18;
- *"Catálogo completo — 28 indexadores"* — o catálogo tem **36 rótulos**;
- o `README.md` da mesma skill **classificava `IPCA` como percentual por dedução**;
- `atualizacao/SKILL.md` dava a **TR como `percentual`** — rebaixada no bloco 17;
- quatro arquivos escreviam `tipo: nominal | percentual` **como domínio de dois valores**.

> **Onde a skill copiava, passou a apontar.** O catálogo é a fonte; **a skill aponta, não copia**.

### O teste, e o custo declarado

`test_classes_de_indice.py` usa **dois idiomas e nenhuma janela de proximidade**. **Medido antes
de decidir**, como o bloco 20 estabeleceu: janelas de ±40/±60/±80/±120 davam 28/52/75/103
"divergências", e **das 52 do ±60, 48 eram falso positivo** — a prosa que ensina R3 põe as classes
lado a lado.

**Custo aceito, escrito no arquivo: sem ledger de exceções.** Aqui não há divergência legítima; em
troca, **classe afirmada em prosa fora dos dois idiomas passa**. A mitigação é editorial.

---

## 3. R4-EXCEÇÃO ganhou gatilho; a régua de R3 não existe

**R4-EXCEÇÃO tinha a mecânica e nenhuma fronteira — nasceu função morta.** Agora tem o gatilho:
eixo = **competência da parcela**, entra e sai em **27/02/1987–03/03/1991**, alcança
`cjf.trabalhista.juros-mora` e o quadro do TRT-3, **não as condenatórias gerais**.

**E a divergência foi junto, sem escolher lado:** TRT-3 **ao dia**, CJF **ao mês**.

**A régua de R3 NÃO existe.** Busca negativa com escopo contado — os **15** arquivos de
`consolidado/` e as **31** páginas de `skills/`, por `defasagem`, `desloca`, `ajuste`, `na
virada`, `um mês`, `pro rata`, `régua`.

> **Tudo enuncia o efeito ou descreve D1–D4; nada dá o procedimento.** O próprio corpus já
> registrava a indecisão — `L3` reclassificada `DÚVIDA` no bloco 20.
>
> **Declarada como `P23-01`, não inventada.**

---

## 4. Os seis pontos de quase-invenção

| # | O que era | Veredito |
|---|---|---|
| **1** | taxa legal de mai/2026 — **variante previdenciária** onde o caso pede **IPCA-15** | **CORRIGIDO** — a tabela de R11 ganhou coluna **variante** |
| **2** | SELIC por **álgebra do gabarito** | **CORRIGIDO** — conduta nomeada: *"a fixture passa a validar a si mesma; bloqueie"* |
| **3** | IPCA-E como percentual | **A SKILL IMPEDIU** |
| **4** | estender **D1 à Fazenda 2009–2021** | **LACUNA DECLARADA** — `P23-02` |
| **5** | interpolar IPCA-E | **A SKILL IMPEDIU** |
| **6** | procurar série nos CSV de `extracao/` | **A SKILL IMPEDIU** |

### O padrão, e é replicável

**As três que a skill impediu tinham a proibição COM O CASO CONCRETO DENTRO** — *"porque IPCA soa
percentual"*, *"registrar e parar, nunca costurar"*, `# OUT_OF_SCOPE` **no próprio dado**.

> **As duas que a skill NÃO cobria eram exatamente aquelas em que o valor certo existe no
> repositório para OUTRO uso** — e nenhuma tinha o caso nomeado. **Agora têm.**

---

## 5. O aceite em dois níveis

**A contradição era real:** o conjunto declara não ter série **e** usava como critério de aceite
fixtures que consomem 23 meses de IPCA-E só na primeira.

| | O que é | Executável |
|---|---|---|
| **NÍVEL 1** | invariantes e aritmética — **o que o implementador de fato acertou** | **só com a skill** |
| **NÍVEL 2** | as quatro fixtures do CJF | **exige série carregada** |

**`scripts/calculo/test_aceite_nivel1.py`, 20 testes, executável.** Ali e não em
`tests/fixtures/` — que é **dado**, onde arquivo novo seria prosa que ninguém roda — nem só numa
seção de skill, que **declara e não verifica**.

**Uma classe guarda a própria declaração:** falha se o README das fixtures ou as skills deixarem
de declarar o bloqueio, e se `divergencia_e_assercao` for mexido.

**E o README das fixtures dizia algo falso:** *"um agente novo lê a skill, implementa, e o
resultado bate aqui"*. **Corrigido, com o porquê.** Nenhuma fixture alterada.

---

## 6. O runner: a tolerância não era banda

**Era tratada como faixa de aceitação.** Agora:

| Situação | Resultado |
|---|---|
| um número só | **`FALTA_UM_METODO`** — não passa, **ainda que o número esteja certo** |
| dois números **iguais** | **`DIVERGENCIA_ZERADA`** — falha: **zerar significa arredondar errado** |
| delta ≠ declarado | `DIVERGIU` |

**Como as fixtures seguem bloqueadas, a asserção nunca seria exercida** — então o runner traz uma
**prova sintética** com entradas sem índice nenhum, cobrindo os quatro comportamentos. **Sem ela,
a correção seria afirmação sobre código que ninguém roda.**

**A redação *"divergem do corpus"*:** **8 ocorrências em 208 arquivos contados**, **2 corrigidas**
nas skills. **Seis não** — são relatório de bloco e registro de frente, **registro datado**, e as
duas últimas classes **são justamente o achado sobre a redação: apagá-lo apagaria a medição**.

---

## 7. A validação adversarial achou três `GRAVE` no próprio bloco

**E o primeiro é o defeito mais sério que este projeto pode produzir.**

### G1 — o bloco publicou um procedimento que contradiz o manual

A regra **`T3`** dizia *"corrigir o bloco de juros **sem nova taxa**"*, marcada como **citação**.

**O manual aplica taxa sobre o bloco de juros**, e publica a célula: `55,75 × 43,89% =
24,468675 → 24,46` (p. 52). **O próprio bloco a documentava três seções adiante.**

**Consequência medida:** o detalhado das fixtures 1 e 2 **não reproduzia número nenhum** —
`5.221,30` contra `5.218,27`.

**A correção não foi ajustar a regra até o número bater.** O discriminante saiu de **R1**:

> **Trecho cujo indexador de juros ENGLOBA correção** (SELIC, taxa legal) **não tem coeficiente
> próprio** — logo a taxa é a **única** correção que o bloco de juros recebe. **Trecho com
> coeficiente próprio** (INPC, IPCA-E, IPCA-15) dá ao bloco **o coeficiente e não a taxa**.
>
> **É a mesma assimetria que o resumido já imprimia na legenda:** `(H) = (C+G) × E%` contra
> `(I) = C × F%`.

**A regra saiu de um invariante e fechou os três casos de uma vez** — `3.484,95`, `5.218,27` e
`4.435,04`, célula por célula. **É o que distingue regra de ajuste ao gabarito.**

E caíram junto os outros dois impedimentos: **coeficiente por parcela** no primeiro marco
(`27,97 + 27,78 = 55,75`; sobre o agregado daria `55,76`) e **taxa por entrada**, não por marco.

### G2 — o runner duplicava parcelas e usava cortes constantes

Injetava **8.000,00 nominais** onde o caso tem **3.000,00**, e para a fixture 1 — data-base
**jun/2022** — criava um marco **três anos além da data-base** e outro que **andava para trás**.

**Os marcos passaram a sair do caso:** caminham mês a mês compondo com R1, e **abrem marco novo
quando muda a assinatura `(indexador de correção, juros, engloba)`**.

### G3 — nenhum teste confrontava `metodos.py`

**O único "teste" era um `hasattr`.** E o runner afirmava *"falta só o coeficiente"* — **verdade
para a fixture 4, falso para as 1 e 2** enquanto G1 existisse.

**`test_metodos.py`, 32 testes, sem série** — os coeficientes estão impressos no PDF. Cobre as
células do resumido, os passos do detalhado, os honorários idênticos, os dois deltas, **a célula
que a regra antiga proibia**, e a prova de que o agregado daria `55,76`.

**Três `skipTest` declarados**, não silenciados.

### Quatro `MÉDIA`, e uma delas é evidência que se refutava

`02-atualizacao-detalhe.md` publicava dois números **visivelmente diferentes** afirmando que eram
*"iguais dos dois lados, dígito a dígito"* — eram **duas parcelas**, não dois métodos. **A tese
era verdadeira e a evidência a refutava.**

Mais: a legenda de coluna **atribuída a duas páginas onde as letras significam coisas
diferentes** — na p. 52, `(G)` é SELIC e `(I)` é o total, **o oposto do publicado**; e a lacuna
**#8** da Frente A, que dizia **IMPOSSÍVEL** para a fixture 4 e **nenhuma skill declarava**.

**E um `LEVE` que não se conciliou:** `k1 × k2 × k4` trunca em `…657`, o manual publica `…656`, e
**half-up daria o mesmo `…657`** — **nenhum critério produz o publicado**. Registrado como não
conciliado, com teste medindo o caso que trunca exato e o que não.

---

## 8. O que a auditoria confirmou íntegro

- **A classificação de índices está sincronizada: zero divergências.** Varredura por método
  diferente — **161 arquivos**, **239 pares candidatos**, os **22 de `skills/` vetados um a um em
  contexto**, todos falso positivo. E as **156 declarações `tipo_indexador`** dos **38 JSON**
  conferem **100%** com o catálogo;
- **Nenhuma fixture ajustada.** `git diff` toca **um** arquivo do diretório: o `README.md`, que era
  o caso autorizado;
- **Nenhuma série populada, por via alguma.** A **SELIC de 3,548%** tem 4 ocorrências, **todas
  narrativas** — **ninguém a implementou**. A **taxa legal de mai/2026** segue em
  `PARES_TAXA_LEGAL_INPC`, **nunca em `VALORES_LITERAIS`**;
- **A marcação citação × inferência está correta**, conferida palavra por palavra contra o PDF —
  e a afirmação de que **o número de casas decimais nunca é declarado** é verdadeira;
- **A separação está onde o bloco diz**, nas duas fixtures, recomputada de forma independente;
- **O escopo da varredura do PDF reproduz exato**, termo a termo e página a página.

---

## 9. O que continua aberto

| Aberto | Natureza |
|---|---|
| **as quatro fixtures** | **NÍVEL 2** — exigem a série carregada. **Dependência externa, por desenho** |
| **`P23-01` — a régua de R3** | não existe no corpus. **Declarada, não inventada** |
| **`P23-02` — `aplicacao` da Fazenda jul/2009–nov/2021** | nem D1 nem D2. O D1 **nasce com a EC 113/2021**, não com o devedor |
| **`"mensalizada"`** | indefinido nas fixtures 1/2 **e** na 4, com conflito entre `tributario-federal.md` § 7 e o critério da fixture |
| **`k1 × k2 × k4`** | **nenhum critério produz o `…656` publicado.** Não conciliado |
| **três `skipTest`** | rótulo do corte de dez/2021, coeficiente da série, fixture 3 |

> **Uma nota para blocos futuros, e não é da série do CJF:** há em
> `C:\Users\Rafaela\Downloads\Plataforma-SaaS-Jus\` um PDF de **Fatores de Atualização Monetária
> da Contadoria Judicial de Belo Horizonte (ICGJ/TJMG)**, 4 páginas, com fatores de 1964 em
> diante. **Não destrava as fixtures** — que precisam de IPCA-E e INPC mensais —, **mas é
> candidato à cadeia cível regional `RG10`.** Registrado, **não consumido**.
