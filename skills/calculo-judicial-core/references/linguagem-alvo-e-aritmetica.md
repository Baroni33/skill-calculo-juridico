# Linguagem-alvo e aritmética — o que a skill exige e o que ela não prescreve

**Carregue este arquivo antes de decidir tipos numéricos, antes de escrever o verificador de R12
e antes de usar qualquer código deste repositório como modelo de implementação.**

**A regra que governa tudo: a skill exige PROPRIEDADE, não MECANISMO.** Onde o conteúdo normativo
já está enunciado como propriedade — truncamento por etapa, número de casas decimais, razão entre
fatores, piso nominal, ordem das operações — **nada aqui o altera**. O que este arquivo delimita é
o que era instrução de linguagem disfarçada de invariante.

---

## 1. O requisito que NÃO é universal — e por isso é declarado

> **A linguagem-alvo precisa de aritmética decimal exata, nativa ou por biblioteca. Linguagem que
> não a tenha não serve sem dependência.**

Este é o único requisito do conjunto de skills que **não é satisfeito por toda linguagem**. É
pré-condição de `R12`, e portanto de `R5`, `R6` e `R11`, que dependem de casas exatas.

**Ele vive nesta skill — `calculo-judicial-core` — e não nas outras três**, porque é aqui que
moram os invariantes e a aritmética: as três SKILL.md restantes já roteiam *"aritmética decimal"*
para cá (`calculo-judicial-atualizacao` § "Quando usar", `indices-judiciais` § "Quando usar",
`calculo-trabalhista-liquidacao` § "Quando usar"). Declará-lo em qualquer outro lugar criaria um
segundo dono para R12.

### 1.1 O que muda, e o que não

| Formulação antiga — **mecanismo** | Formulação vigente — **propriedade** |
|---|---|
| *"Decimal, sem float"*, *"nenhum `float`"*, *"`decimal.Decimal`"* | **aritmética decimal exata; ponto flutuante binário proibido no caminho de cálculo** |
| *"verificado por AST"* | **a ausência de ponto flutuante binário deve ser VERIFICÁVEL; o método depende da linguagem** |
| *"usar `Decimal(1)/Decimal(30)`"* | **dividir 1 por 30 em decimal exato, nunca o truncamento impresso** |

**O tipo concreto é escolha do implementador.** `System.Decimal`, `java.math.BigDecimal`,
`decimal.Decimal`, `BigDecimal` de qualquer runtime — todos satisfazem, desde que a precisão
disponível cubra as cadeias longas. **A skill não pressupõe linguagem.** O alvo atual do produto é
**C#**, que tem `System.Decimal` nativo; isso é **fato do produto, não exigência da skill**.

**Atenção à precisão, que é propriedade e não detalhe de tipo:** `System.Decimal` tem 28–29
dígitos significativos; cadeias de dezenas de fatores encadeados em precisão plena podem
consumi-los. Onde o corpus exige precisão plena antes do truncamento de emissão, **o implementador
precisa garantir que o tipo escolhido não arredonde por falta de dígitos** — e, se arredondar,
elevar a precisão do contexto ou usar tipo de precisão arbitrária.

### 1.2 Verificabilidade — a propriedade, não o método

> **A ausência de ponto flutuante binário no caminho de cálculo deve ser VERIFICÁVEL por meio
> mecânico e repetível. Qual meio, depende da linguagem.**

Não se prescreve AST. AST é **como se faz em Python**; em C# seria analisador de código (Roslyn
analyzer, regra de build), em Java um *bytecode/source checker*, em outra linguagem outra coisa.
**O que a skill cobra é o resultado:** existe um passo automatizado, rodado em toda varredura, que
falha se ponto flutuante binário aparecer no caminho de cálculo.

**Duas propriedades que o verificador precisa ter, e elas não são de linguagem:**

1. **escopo declarado** — o que é varrido e o que é excluído, com a razão escrita. Teste negativo
   que **planta** ponto flutuante de propósito, para provar que o caminho aritmético o recusa,
   **tem de ficar fora do escopo**, senão a prova acusa a si mesma;
2. **prova contra vacuidade** — o verificador precisa demonstrar que **detecta** um caso plantado.
   Varredura que passa porque não olha nada é o pior modo de falha.

---

## 2. Os scripts de verificação permanecem em Python — e isso é contraintuitivo

> **Script de skill roda no ambiente do AGENTE, para verificar a implementação — não no produto.**
> **A linguagem do script de verificação é independente da linguagem do motor.**

**Os validadores não são o motor e não viram o motor.** São executados por quem lê as skills para
aferir norma, cadeia e aritmética normativa. Eles são Python **de fato**, e o termo é correto
quando o texto fala deles.

> **Bloco 25 — eles moram em dois lugares, e a divisão é por CONSUMO.** Quatro viraram **script de
> skill** e viajam com a skill que os instala: `valida_cobertura.py` e `valida_taxa_legal.py` em
> `calculo-judicial-atualizacao/scripts/`, `valida_regimes.py` em `calculo-judicial-core/scripts/`
> e `valida_parametros.py` em `calculo-trabalhista-liquidacao/scripts/`. Os demais são **ferramenta
> de pipeline** e continuam em `scripts/calculo/` do repositório — **que a instalação manual manda
> NÃO copiar**. Por isso nenhum artefato de skill deve apontar para lá: o ponteiro morreria na
> instalação.

**O caso central é `calculo-judicial-atualizacao/scripts/valida_taxa_legal.py`**, que implementa **R11** — taxa legal
por razão entre fatores, nunca subtração de percentuais — e **pode ser executado pela skill** para
conferir um par publicado sem que exista motor nenhum. Um motor em C# não o substitui e não é
substituído por ele: **um verifica a regra; o outro executa a conta do produto.**

O mesmo vale para `test_aceite_nivel1.py`, `valida_cobertura.py`, `valida_regimes.py`,
`valida_parametros.py` e `valida_bloco_tabelas.py`.

---

## 3. A implementação de referência NÃO é exemplo de aceite

O bloco 22 deixou um motor em Python em `docs/calculo/aceitacao/frente-a/` — `motor.py`,
`metodos.py`, `aritmetica.py`, `cadeias.py`, `series.py`, `runner.py`.

> **Ela NÃO é o exemplo de aceite. O exemplo é a TABELA DE ENTRADA E SAÍDA ESPERADA, em dado.**

**O código não foi apagado, e não deve ser:** é **artefato datado do bloco 22** e **evidência da
aceitação** — o inventário está em `docs/calculo/aceitacao/bloco-22-relatorio.md`. **O que mudou é
o papel que as skills lhe atribuem:** de *"faça como o `metodos.py` faz"* para *"dada esta
entrada, espere esta saída"*.

**Por que a mudança importa:** implementação de uma linguagem que serve de modelo vira **âncora
para a próxima**. Quem lê `metodos.py` copia o `Decimal` do Python junto com o procedimento, e o
procedimento é normativo enquanto o `Decimal` é acidente.

**Onde está a especificação de entrada e saída, que é o que o implementador precisa:**

| O que | Onde | Forma |
|---|---|---|
| As quatro fixtures do CJF — entrada, saída, e o par asserido das fixtures 2 e 4 | `tests/fixtures/calculo/` | **dado** (`json`) |
| Os dois métodos, procedimento passo a passo com casas e ponto de truncamento | `skills/calculo-judicial-atualizacao/references/metodos-resumido-e-detalhado.md` | prosa normativa |
| Aceite de NÍVEL 1 × NÍVEL 2, fixture a fixture, com o bloqueio nomeado | `references/aceite-em-dois-niveis.md` | tabela |
| Casos de entrada/saída de verbas e encargos | `skills/calculo-trabalhista-liquidacao/SKILL.md` § "Fixtures de aceite" | tabela |
| Lacunas declaradas, com classificação | `docs/calculo/aceitacao/frente-a/registro-de-lacunas.md` | registro datado |

**`scripts/calculo/test_metodos.py` é teste DO REPOSITÓRIO**, não da skill: ele confronta
`metodos.py` com as **células publicadas** pelo manual. É evidência de que o procedimento escrito
reproduz o número impresso — **não é "o jeito de implementar"**, e nenhuma skill o apresenta como
tal.

---

## 4. Requisito registrado para o aceite futuro — **não implementado agora**

O bloco 22 testou **composição e invariantes**, que são agnósticos. **A aceitação não se refaz.**

> **REQUISITO: o bloco de aceitação deve poder rodar contra implementação em QUALQUER linguagem.**

**Forma esperada quando for feito:** o critério de aceite se expressa como **par (entrada, saída
esperada) em dado**, e o harness invoca a implementação sob teste por uma fronteira que não
pressupõe linguagem — processo, arquivo ou serviço. **O que hoje acopla é o `runner.py`
importar os módulos Python diretamente.**

**Este bloco apenas registra o requisito.** O harness poliglota **não foi implementado**, e
implementá-lo por conta própria seria refazer aceitação já feita.

---

## 5. Ponteiros

| Assunto | Onde |
|---|---|
| `R12` enunciado, e as cinco cadeias de arredondamento | `skills/calculo-judicial-core/SKILL.md` §§ "R12 — Aritmética decimal" e "Aritmética — as cinco cadeias de arredondamento" |
| Aceite em dois níveis | `aceite-em-dois-niveis.md` |
| Os validadores, e o que cada um afere | `scripts/calculo/README.md` |
| Inventário do que a skill entregou sem série | `docs/calculo/aceitacao/bloco-22-relatorio.md` |
| Artefato datado do bloco 22 — **evidência, não modelo** | `docs/calculo/aceitacao/frente-a/` |
