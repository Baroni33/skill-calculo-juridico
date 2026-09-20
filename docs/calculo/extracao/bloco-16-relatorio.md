# Bloco 16 — Fase 5: construção das skills

**Estado: fechado.** Quatro skills, quinze arquivos de `references/` divididos entre nacional e
regional, cobertura dos 33 casos difíceis. **O motor é de produto: nenhuma skill cita cliente,
nem assume UF, tribunal ou polo processual.**

| Arquivo | Linhas |
|---|---|
| `skills/calculo-judicial-core/SKILL.md` | **465** |
| `skills/calculo-judicial-atualizacao/SKILL.md` + 6 `references/` | **458** + 1.552 |
| `skills/calculo-trabalhista-liquidacao/SKILL.md` + 9 `references/` | **494** + 1.900 |
| `skills/indices-judiciais/SKILL.md` | **498** |
| `skills/00-cobertura-casos.md` | 247 |

**Nenhuma acima de 500.** Onde o conteúdo passou, foi para `references/` **com ponteiro
explícito e nota de movimentação** — nunca cortado em silêncio.

---

## 1. A premissa que o bloco corrigiu, e o que ela derrubou

O enunciado trouxe um fato verificado em fonte externa ao corpus:

> A atualização monetária trabalhista é **NACIONAL** desde a **Res. CSJT 8/2005**, que unificou
> as 24 tabelas usadas pelos TRTs. Hoje vale a **Res. CSJT 380/2024**, com duas tabelas — débitos
> comuns e Fazenda Pública, esta referenciada ao Manual do CJF. O **PJe-Calc** é o sistema de
> cálculo de toda a Justiça do Trabalho.

**Consequência estrutural:** o manual do TRT-3 é **fonte procedimental de uma região que aplica
norma nacional**. Sua aritmética **não é prática regional divergente**. Regional são os
**verbetes que ele invoca**.

### O enunciado nomeava três regras regionais. São quinze.

A varredura classificou **53 itens**: 15 REGIONAIS, 30 NACIONAIS, 8 DÚVIDAS.

| | Regionais |
|---|---|
| **verbetes** (`RG1`–`RG9`) | Súmulas 15, 24, 45, 46, 39 (cancelada), 48 (superada), 2 e 38; **OJ 23** das Turmas; **TJP 4** |
| **fontes não-verbete** (`RG10`–`RG15`) | tabela CGJ/TJMG · **IN GP/CR/VCR 001/2002** (todas as custas de execução) · acórdão AP 0001624-31.2012.5.03.0010 · três ementas sobre falência · **posição da SEE/TRT-4** · tabela própria do TRT-3 até out/2005 |

**Três tribunais, não um:** **TRT-3**, **TRT-4** e **TJMG**. **Fallback nacional identificado
para catorze das quinze** — a exceção é `RG15`, que é a lacuna `P9-02`.

> **`tese prevalecente` e `art. 896, § 6º`: zero ocorrências em todo o repositório.** A única
> tese prevalecente do consolidado aparece **só pela sigla** (`TJP 4`).

### O achado que mais muda a arquitetura

**As cadeias `trt3.hist.*` são NACIONAIS com nome enganoso.** Seus fundamentos declarados são
CC arts. 1.062–1.063, Lei 8.177/91 art. 39, Súmulas 200 e 381 do TST e as paridades da moeda — e
a correção monetária **delega à Tabela Única do CSJT**.

> **Um motor que resolva cadeia por prefixo de tribunal não acha cadeia nenhuma para TRT-1,
> TRT-2 ou TRT-15.** O prefixo é do arquivo, não da norma.

**A Tabela Única do CSJT deixa de ser "integração desejável"** e passa a ser **a dependência que
torna o motor nacional**. Segue não integrada (`P9-02`).

---

## 2. R24 — a invariante nova

**Ausência de súmula regional não é erro.** Competência sem verbete cadastrado para o tribunal
resolve pela **regra nacional** e marca a conta **`sem cobertura regional`**.

```
(regra, tribunal, competência)
```

- **`regra`** identifica o **ponto de cálculo**, não o verbete;
- **`tribunal`** só entra onde há variante cadastrada;
- **`competência`** é necessária porque **verbete regional nasce e morre com data** — a Súmula 39
  do TRT-3 foi cancelada com eficácia **retroagida a 11/11/2017**.

> **Mesma forma da R14, e a simetria é deliberada:** `sem cobertura coletiva` e `sem cobertura
> regional` são a mesma espécie de silêncio — **o dado não existe**, não **a regra não existe**.

**R24 não cria exceção à R8:** comando exequendo expresso (art. 879, § 1º, da CLT) afasta o
verbete regional **mesmo dentro da região que o editou**.

---

## 3. Tarefa 0(f) — a varredura, reportada antes de alterar

| Termo | No consolidado | Decisão |
|---|---|---|
| **`Gasmig`** | **0** | nada a fazer — o nome ficou contido nas fixtures |
| `polo passivo` | 1 | **alterado** — a frase assumia o polo |
| `cliente` | 6, sempre *"jurídico do cliente"* | **uniformizado** para "o usuário do módulo" |
| `reclamante` / `reclamada` | ~20 | **mantido** — é o vocabulário do corpus para as partes |
| `TJMG` / `CGJ` | 4 | **mantido e marcado REGIONAL** |

**Verificação final nas skills:** `gasmig`, `polo passivo`, `polo ativo`, `o cliente`, `nosso` →
**zero**. `MG`/`Minas` ocorre 8 vezes, **todas** no contexto legítimo da tabela CGJ/TJMG e do
alcance da OJ 23.

---

## 4. Tarefa 4 — os 33 casos difíceis

**Critério de aceite.** Resultado em
[`../../../skills/00-cobertura-casos.md`](../../../skills/00-cobertura-casos.md):

| | Casos |
|---|---|
| **COBERTO** | **33** |
| **PARCIAL** | **0** |
| **PERDIDO** | **0** |

**Nenhum caso que o consolidado respondia desapareceu das skills.** Distribuição por skill
primária: **core 15 · liquidação 12 · atualização 4 · índices 2**.

**C31 e C33, que o bloco 15 deixou como parciais "fecháveis no bloco 16", fecharam** — as
fixtures 2 e 4 nomeadas com seus deltas em `core § Fixtures`, e as dependências externas reunidas
em `core § Limitações declaradas`.

**Dois parciais ABRIRAM na transposição, e foram fechados no mesmo bloco:**

- **C22** — `R16` tinha **zero ocorrências nas quatro skills**. Sumira o degrau da **norma
  coletiva** na precedência;
- **C24** — a **anti-heurística do art. 611-B** se perdera: *"a âncora é o artigo, não a presença
  de 'no mínimo'"*, mais os parâmetros concretos por inciso.

---

## 5. Validação adversarial — o que ela pegou

**Três graves, e duas eram minhas.**

**G1 — a invariante `R8` virou o verbete `RG8`.** Minha renomeação dos rótulos regionais foi
parcial e atingiu uma remissão à precedência: a sobrevida da tabela CGJ/TJMG em processo transitado
passou a se fundamentar na **Súmula 48 do TRT-3 — cancelada, e sobre prazo rescisório**.

**G2 — a colisão que a espinha declarava ter evitado persistia na prosa.** A convenção `RG` valia
só na coluna 1 das tabelas; o texto voltava a `R`. No mesmo arquivo, `R8` aparecia nos dois
sentidos **a nove linhas de distância**; e `R14` significava "SEE/TRT-4" numa linha e "ausência de
norma coletiva não é erro" em outra.

> **É a terceira vez que a colisão de etiquetas morde este projeto** — `F1`–`F9` × `F1`–`F7` no
> bloco 15, a renumeração cega no mesmo bloco, e agora `RG` × `R`. **Renomear sem ler a frase
> inteira produz um rótulo bem-formado apontando para o alvo errado**, que é pior que o
> ambíguo, porque ninguém desconfia.

**G3 — a escada de precedência tinha três degraus em duas skills e quatro na terceira.** Eu a
tinha alterado para quatro com base no caso C22. **A auditoria mostrou que o consolidado diz três
em três lugares** e que os quatro só existem no `camada-norma-coletiva-schema.json`.

**Resolução: não são versões concorrentes.**

```
R8  (geral)     título judicial > escolha do usuário > default da jurisdição
R16 (parâmetro) título judicial > norma coletiva da competência > escolha > default legal
```

**R16 especializa R8 na camada de parâmetro.** Ler a de quatro como geral faz o motor procurar
instrumento onde não há categoria; ler a de três na camada de parâmetro deixa a escolha do
usuário sobrepor a CCT. **Eu havia fundido as duas.**

### Seis médias, todas corrigidas

*"TRT-3 e TJMG — e só"* em quatro lugares, **apagando o único verbete do TRT-4**; `B04-F7`
rotulado `INAPLICÁVEL` quando **o ponto é `VIGENTE`** e inaplicável é o **dispositivo invocado**;
**26 × 28 regimes** entre skills; o arquivo de cobertura apontando para um **estado anterior** das
skills; e a espinha anunciando *"as sete"* limitações quando o companheiro tem **dez**.

**Um achado não foi corrigido, e a razão está registrada:** o ponteiro para a *"armadilha A21"* não
resolve — o catálogo vai de `A1` a `A15`. **É herdado do consolidado**, não criado na transposição.

### O que a auditoria confirmou íntegro

- **Todos os 32 vereditos `BIFURCADO` cobertos, sem sobreposição e sem perda** — 26 em
  `liquidacao/references/cortes-e-bifurcacoes.md`, 6 em `atualizacao`. **Zero ocorrências** do
  padrão *"passou a ser X"* sem o lado antigo, de tabela de coluna única, ou de `SUPERADO` onde o
  veredito é `BIFURCADO`;
- **nenhuma pendência virou regra** — `pr.imputacao`, os dois bloqueios, Fazenda Pública,
  `P13B-01`, `P9-02` e `F7-03` seguem como limitação declarada;
- **as duas armadilhas de classificação** que o enunciado mandou caçar estão corretas nas skills;
- **amostragem dirigida de ~25 valores monetários e percentuais** contra a fonte: **todos batem**;
- **`R4-EXCEÇÃO`**, **NMP em três ramos**, **as duas molduras do cap. 10**, **`R16` × `R18`** e a
  **EC 113/2021 como *"independentemente de sua natureza"*** — todos íntegros. **O erro do "só
  federal" não reapareceu.**

---

## 6. Onde o consolidado não bastou — o resultado mais útil deste bloco

Quatro lugares em que escrever a skill **exigiu composição**, e cada um está marcado como tal no
arquivo onde aparece:

| Lacuna | Natureza |
|---|---|
| **A ordem de cálculo ponta a ponta não é enunciada em lugar nenhum do corpus** | O Procedimento das skills é **composição declarada** a partir de R22 e das seções de cada arquivo. **Não é citação.** É a lacuna estrutural mais consequente: o motor herdaria uma ordem que ninguém escreveu |
| **A lista de seis `references/` do enunciado não fecha o domínio** | **Condenatórias gerais** e **desapropriação** não são tributárias nem previdenciárias e **não têm arquivo**. Alojadas em `tributario-federal.md` §§ 5 e 7, com aviso no topo e o sétimo arquivo nomeado como candidato. **Não inventei arquivo fora da lista** |
| **Não existe contagem canônica de "quantas bifurcações há"** | O "32 dos 50 vereditos" é o universo dos vereditos, não o de cada skill. O inventário teve de ser construído cruzando quatro arquivos, **com o critério de contagem declarado no próprio arquivo** |
| **O campo `tipo` (nominal/percentual) não existe em nenhuma série extraída** | É o campo que **R3 declara indispensável**. Aparece uma única vez no repositório, como `tipo_indexador`, e ali é **inferência declarada sobre a TR**. O contrato o exige; o dado não o carrega |

### E uma correção de registro sobre os próprios validadores

O enunciado mandava registrar que `valida_bloco_tabelas.py` *"reporta 31 divergências e 10
erros"*. **O consolidado registrava 31 divergências e ZERO erros.**

Os dois estão certos, e a diferença é de **escopo do validador**: `PAGINAS_DO_BLOCO` é fixo em
`range(373, 472)` para o bloco 1, mas a verificação de proveniência varre **todos** os CSV do
diretório — e uma série de bloco posterior (p. 178) caiu no mesmo lugar.

> **O registro de "0 erros" estava certo para o escopo dele; o escopo é que ficou estreito.**
> Consequência de contrato: **proveniência exige o intervalo de páginas declarado junto com a
> série**, não constante global.

---

## 7. Para o bloco 17

**A ordem de cálculo ponta a ponta é o que falta.** Tudo o mais está escrito ou declarado como
limitação; essa é a única peça que o motor usaria sem que ninguém a tivesse enunciado.

Depois dela, em ordem de valor: o **sétimo arquivo de `references/`** para condenatórias gerais e
desapropriação; o campo **`tipo`** nas séries; e o **escopo de proveniência** por série.

> **Um veredito inventado é pior que uma pendência declarada.** Valeu para a extração, para o
> confronto e para a consolidação. Vale para a skill.
