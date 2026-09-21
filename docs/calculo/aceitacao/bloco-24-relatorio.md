# Bloco 24 — empacotamento como plugin e linguagem-alvo

**Estado: fechado.** Manifesto criado com formato **verificado contra plugins reais**, instruções
ao implementador **traduzidas de mecanismo em propriedade**, os 21 `.py` **classificados e não
movidos**, e `RG10` **registrada sem ser extraída**.

> **Registro datado.** Não se atualiza. Estado corrente em
> [`../consolidado/00-numeros.md`](../consolidado/00-numeros.md).

---

## 1. Tarefa 1 — a classificação dos 21 `.py`

> **O enunciado mandou classificar, NÃO mover.** *"Produza a classificação, com a razão de cada
> um, para eu decidir."* **Nada foi movido** — `git diff --stat` sob `scripts/` mostra só os
> arquivos que este bloco editou por outra razão.

### FERRAMENTA DE PIPELINE — 16

**Servem a quem mantém o repositório.** Ou escrevem em `docs/`, ou leem caminho fixo, ou aferem
artefato interno.

| Script | Por quê |
|---|---|
| `extrai_bloco_01.py` | lê o PDF do TRT-3 e escreve extração |
| `gera_cadeias_bloco18.py` · `gera_cadeias_bloco19.py` | geradores one-shot de cadeia |
| `migra_bloco19_tipos.py` | migração one-shot, histórica |
| `gera_numeros.py` | **escreve** `00-numeros.md` |
| `valida_bloco_tabelas.py` | `DIR_SERIE` e `DIR_SEMANTICA` fixos no repositório |
| `valida_cadeias.py` | `TABELAS` fixo — valida **as cadeias deste repositório** |
| `test_numeros.py` · `test_ponteiros.py` · `test_classes_de_indice.py` | vigiam o repositório contra si mesmo |
| `test_metodos.py` | confronta `metodos.py`, artefato do bloco 22 |
| `test_valida_bloco_tabelas.py` · `test_valida_cobertura.py` · `test_valida_parametros.py` · `test_valida_regimes.py` · `test_valida_taxa_legal.py` | testes unitários **dos validadores**. **Dois plantam ponto flutuante de propósito** — só fazem sentido aqui dentro |

### SCRIPT DE SKILL — 2 limpos

| Script | Por quê |
|---|---|
| **`valida_taxa_legal.py`** | **o caso declarado pelo enunciado, e confirmado.** `argparse`, sem `RAIZ`, sem ler `docs/`. Implementa **R11** sobre um par que o usuário passa. **Autocontido** |
| **`valida_cobertura.py`** | **candidato mais forte do que parecia.** `main()` recebe a tabela como **caminho arbitrário de JSON**, e o domínio de R3 está **inline**, descrito como *"espelho"* do catálogo. **R1/R2/R3 sobre conjuntos de segmentos é exatamente "verificar uma implementação"** |

### HÍBRIDOS — 3, e é onde a decisão é sua

| Script | O atrito |
|---|---|
| **`valida_regimes.py`** · **`valida_parametros.py`** | **são resolvedores**, como o enunciado diz. Mas ambos têm `CATALOGO_PADRAO` apontando para `docs/calculo/tabelas-normativas/`. **Copiados sozinhos, não rodam.** Viram script de skill com uma mudança pequena — catálogo como argumento obrigatório, viajando junto |
| **`test_aceite_nivel1.py`** | **declara-se o aceite DA SKILL, e hoje é teste do repositório.** Ver § 5 |

> **E há uma armadilha plantada para essa decisão**, registrada no README: **a instrução de
> instalação manual manda NÃO copiar `docs/`** — o que quebraria os dois resolvedores no dia em
> que forem promovidos.

---

## 2. Tarefa 2 — mecanismo virou propriedade, e o que já estava certo não mudou

| Antes | Depois |
|---|---|
| *"Decimal, sem float"* | **aritmética decimal exata; ponto flutuante binário proibido no caminho de cálculo** |
| *"verificado por AST"* | **a ausência deve ser VERIFICÁVEL; o método depende da linguagem** |

**O requisito que não é universal foi declarado** em
`skills/calculo-judicial-core/references/linguagem-alvo-e-aritmetica.md`:

> **A linguagem-alvo precisa de aritmética decimal exata, nativa ou por biblioteca. Linguagem que
> não a tenha não serve sem dependência.**

**Ali e não em outro lugar** porque é onde moram R12 e os invariantes, e as outras três skills já
roteavam *"aritmética decimal"* para o core. **Dono único.**

### O defeito simétrico não ocorreu

**Truncamento por etapa, casas decimais, razão entre fatores, piso nominal e ordem de operações
seguem como estavam.** A auditoria confirmou, e o próprio arquivo novo traz a salvaguarda:

> *"Onde o conteúdo normativo já está enunciado como propriedade — truncamento por etapa, número
> de casas decimais, razão entre fatores, piso nominal, ordem das operações — nada aqui o
> altera."*

### E o motor de referência deixou de ser modelo

**Nenhuma skill o apresentava como *"o jeito de implementar"** — a auditoria verificou. As duas
menções eram ponteiros, e foram reescritas: `frente-a/` passa a ser **artefato datado do bloco 22
e evidência da aceitação**, e o ponteiro operacional aponta para **`tests/fixtures/calculo/` — o
par asserido em dado**.

**O código não foi apagado.** O que mudou é o papel que as skills lhe atribuem.

---

## 3. Tarefa 3 — o manifesto, e a regra de parada foi satisfeita sem web

> **O enunciado proíbe inventar:** *"Se o formato exato não estiver claro, PARE e reporte."* **E
> proíbe pesquisar na web.**

**A saída foi verificar contra plugins que de fato carregam nesta máquina.**

| Evidência | O que confirmou |
|---|---|
| **51 `plugin.json` reais** em `~/.claude/plugins/cache/` | `name` 51/51 · `description` 51/51 · `author` 47/51 · `version` 25/51 · `homepage` 16/51 · `keywords` 16/51 · `repository` 5/51 |
| **5 `marketplace.json` reais**, 243 entradas de plugin | **`name`, `description` e `source`: 223/223** no oficial — **os três obrigatórios, confirmados por contagem** |
| `superpowers` e `impeccable` | **`"skills": "./skills/"`** existe em plugins reais — **não é invenção**. E `source: "./"` com os manifestos em `.claude-plugin/` na raiz é o arranjo do `superpowers` |

**Frontmatter: válido nas quatro.** Parseado com YAML: **exatamente `name` e `description`**,
**zero campos fora dos seis aceitos**.

### O achado que podia impedir o carregamento

**Duas `description` passavam de 1024 caracteres** — `calculo-trabalhista-liquidacao` em **1133**
e `calculo-judicial-atualizacao` em **1034**.

> **O máximo entre as 124 `SKILL.md` instaladas nesta máquina é 895.** E a `description` é o
> **único** mecanismo de invocação: skill que não carrega **não existe**.

**As quatro foram encurtadas** e hoje estão entre **794 e 890** — abaixo do máximo observado no
mundo real, sem perder gatilho. **O teto de 1024 não foi confirmado** (exigiria web); o que
sustenta a decisão é o dado empírico.

### E o manifesto ganhou guarda

`test_ponteiros.py` recebeu **três testes**: o caminho de `skills` **resolve e tem skill** — um
manifesto que aponta para diretório vazio instala e **carrega zero skills, em silêncio** —; a
contagem *"Quatro skills"* da prosa **bate com as que existem**; e o **frontmatter só usa campos
aceitos**.

---

## 4. Tarefas 4 e 5

**README ganhou seção `Instalação`**, com os dois caminhos, o que **não** copiar, e a declaração
de que as skills são ***model-invoked*** — disparam pela `description`, **sem comando**.

**`P24-01` registrada em `pendencias.md` § 28.** A tabela **ICGJ/TJMG** da Contadoria de Belo
Horizonte, 4 páginas, 1964–2026, candidata a `RG10`.

> **Não destrava as fixtures** — elas consomem **IPCA-E e INPC** das cadeias federais; esta é
> **ICGJ**. **Séries de jurisdições diferentes.**

**Não foi extraída**, e há **três perguntas abertas** antes de extrair, nenhuma respondível sem
ler o documento: `ICGJ` é índice ou nome da tabela? Qual o `tipo_indexador` dele? E **é `RG10` ou
é a série que `RG10` consome** — (A) ou (B)?

**A auditoria confirmou materialmente:** `git status` não mostra alteração sob
`tabelas-normativas/`. **Nenhum fator entrou.**

---

## 5. A validação adversarial — nada de GRAVE, e quatro MÉDIA

**Nenhuma das cinco classes que o enunciado mandou procurar se confirmou como grave:** frontmatter
válido, manifesto não inventado, **nenhum script movido**, skills não presas a linguagem, e o
README sem ponteiro morto.

### M3 é o achado mais substantivo, e é sobre a fronteira da tradução

**`test_aceite_nivel1.py` declarava-se o aceite de R12 e chamava-se `TestR12ZeroFloatPorAST`**,
com `ARVORES` **fixas** em `scripts/calculo/` e `frente-a/`.

> **Rodado ao lado de um motor em C#, ele passaria sem olhar uma linha dele** — verificando o
> Python deste repositório. E `linguagem-alvo-e-aritmetica.md` nomeia exatamente esse modo de
> falha: *"varredura que passa porque não olha nada é o pior modo de falha"*.

**A prosa foi traduzida; o artefato que a prosa cita, não.** A tradução **parou na borda do
`.py`**.

**Corrigido sem fingir que resolve:** a classe passou a se chamar
`TestR12SemPontoFlutuanteBinarioNoCodigoDesteRepositorio`, com **ressalva de alcance** dizendo
que **não é o aceite de uma implementação em outra linguagem**, que **AST é como se faz em
Python, não o requisito**, e que **o aceite poliglota segue registrado e não implementado**.

### M2 — a razão que eu escrevi estava factualmente errada

Ao declarar `.claude-plugin/` fora da varredura de números, escrevi que ***"não tem prosa: é
metadado"***. **É falso** — `plugin.json` tem uma `description` com ~420 caracteres, e ela diz
**"Quatro skills"**, que **é contagem do repositório**, duplicada nos dois arquivos.

**A exclusão continua valendo** — manifesto é contrato de empacotamento, não lugar de consultar
estado. **A razão foi reescrita**, e o número **ganhou dono**: o teste da § 3.

### M1 e M4

**M1** são as `description` longas, § 3. **M4** é a armadilha do `docs/`, § 1 — **registrada no
README, não consertada**, porque a decisão de promover script é sua.

### E uma guarda pegou este bloco enquanto ele trabalhava

Ao criar `.claude-plugin/`, `test_numeros.py` falhou com *"árvore nova no repositório, fora do
escopo declarado"*.

> **A terceira contagem tem de ser nomeada.** Foi o que o bloco 20 estabeleceu, e a guarda
> cobrou. **Declarei em vez de afrouxar** — e o teste passou a exigir que toda exclusão tenha
> alvo, para que exclusão órfã não vire anistia.

---

## 6. O que fica em aberto

| Aberto | Natureza |
|---|---|
| **promover ou não os 3 híbridos** | **decisão sua.** A classificação está em § 1, com o atrito de cada um |
| **`skills/00-cobertura-casos.md`** | arquivo solto na raiz de `skills/`. **21 de 21 plugins reais têm só diretórios ali.** Não tem frontmatter; um carregador que varra `skills/*/SKILL.md` o ignora. **Dúvida declarada — não movido**, porque o único ponteiro vivo é o do próprio README deste bloco |
| **teto de 1024 na `description`** | **não confirmado** — exigiria web. As quatro estão abaixo do máximo observado em 124 skills reais |
| **`/plugin marketplace add` em repositório PRIVADO** | **não testado.** Depende da credencial de git da máquina. O README declara |
| **aceite poliglota** | **requisito registrado, não implementado.** O bloco de aceitação futuro deve rodar contra implementação em qualquer linguagem |
| **`P24-01` — ICGJ/TJMG** | registrada, **não extraída**. Cadeia sem tabela extraída não se gera |
