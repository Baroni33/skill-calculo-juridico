# scripts/calculo — validadores determinísticos

**Fase do pipeline:** Fase 2 (validação da extração tabular) e Fase 6 (aceitação).

## Propósito

Validação **determinística**, por script, não por revisão de LLM (regra 2 do plano).
Dado tabular e aritmética normativa se verificam com código.

## BLOCO 25 — quatro validadores SAÍRAM daqui

**A classificação do bloco 24 virou endereço.** O que valida **a regra** foi morar ao lado
da regra, dentro da skill, e **viaja com ela na instalação**. O que valida **o repositório**
ficou aqui.

| Promovido a script de skill | Agora em | Lê |
|---|---|---|
| `valida_cobertura.py` | `skills/calculo-judicial-atualizacao/scripts/` | nada — é autocontido |
| `valida_taxa_legal.py` | `skills/calculo-judicial-atualizacao/scripts/` | nada — é autocontido |
| `valida_regimes.py` | `skills/calculo-judicial-core/scripts/` | `../regras/regimes-temporais-catalogo.json` |
| `valida_parametros.py` | `skills/calculo-trabalhista-liquidacao/scripts/` | `../regras/camada-norma-coletiva-catalogo.json` |

**`valida_regimes.py` e `valida_parametros.py` NÃO precisaram ser divididos.** A hipótese
era que fossem híbridos — parte validando estrutura de regra, parte tocando série de valor.
**A segunda parte não existe.** Nenhum dos dois abre `.csv`, nenhum resolve índice mensal:
o `resolve_serie` de `valida_parametros.py` é a **sequência de competências** de um
contrato, não série de valor, e o `MOTIVO_BLOQUEADO` de `valida_regimes.py` é um rótulo de
recusa, não leitura de série. Os dois eram inteiros de estrutura de regra; migraram
inteiros. **Dividir um script que não precisa ser dividido teria sido o defeito.**

**Os `test_*.py` continuam AQUI**, inclusive os dos quatro promovidos: teste é ferramenta
de pipeline. Eles importam o módulo pelo nome, e `caminhos_de_skill.py` põe os `scripts/`
das skills no `sys.path` — **um lugar só** para o caminho novo, em vez de nove cópias dele.

## Conteúdo

| Script | Verifica |
|---|---|
| `valida_bloco_tabelas.py` | Extração tabular do bloco 1 (Manual TRT-3): contagem contra o PDF, faixas, vigências, proveniência e calendários |
| `valida_cadeias.py` | CLI de R1/R2/R3 sobre as cadeias, e o **manifesto de cadeias**. **Ficou no pipeline porque ESCREVE:** grava no manifesto a cadeia nova que encontrar, e script que muta artefato versionado é manutenção de repositório |
| `caminhos_de_skill.py` | **não valida** — é a tabela de caminhos das regras e dos scripts migrados no bloco 25, e o bootstrap de `sys.path` dos testes |
| `migra_bloco19_tipos.py` | **Não valida — reescreve.** Migração one-shot do bloco 19: `tipo_indexador` da SELIC, da taxa legal, do IPCA-E/IPCA-15 e da família TR. Mantido para que a alteração seja auditável segmento a segmento (`--conferir` só lista) |
| `escrita_curada.py` | **não valida** — é a guarda de escrita dos geradores *one-shot* (bloco 25). Ver abaixo |

Testes em `test_valida_cobertura.py`, `test_valida_taxa_legal.py`,
`test_valida_regimes.py`, `test_valida_parametros.py`, `test_valida_bloco_tabelas.py`,
`test_ponteiros.py`, `test_numeros.py`, `test_geradores.py`, `test_aceite_nivel1.py` e
`test_metodos.py` — **todos aqui**, mesmo os dos quatro validadores que foram para as skills.

## Gerador one-shot não sobrescreve curadoria — `escrita_curada.py` (bloco 25)

**Quatro scripts deste diretório escrevem artefato: `gera_cadeias_bloco18.py`,
`gera_cadeias_bloco19.py`, `migra_bloco19_tipos.py` e `extrai_bloco_01.py`.** Todos rodaram
uma vez, no bloco que lhes dá nome, e **tiveram a saída curada depois, à mão, por outros
blocos** — a tokenização de `aplicacao` do bloco 23, as linhas de proveniência de R3 nos
`serie-*.csv`. **Nenhum deles sabia disso, e todos escreviam por cima em silêncio.**

> **Rodar `gera_cadeias_bloco19.py` derrubava a suíte.** E, depois da migração do bloco 25,
> o que se estragava deixou de ser `docs/` e passou a ser o **artefato empacotado**.

A guarda é uma só, compartilhada: **`escrita_curada.grava_lote` confere o lote inteiro antes
de tocar em disco.** Idêntico **não escreve**; inexistente **escreve**; divergente **RECUSA o
lote inteiro** e sai com **código 2** — que não é `1`, porque `1` é *"o validador achou
violação"*. `--forcar` para o dia em que a intenção for mesmo regerar.

**`test_geradores.py` cobra as duas metades**: que rodar cada gerador **não mude byte nenhum**
— `sha256` das árvores antes e depois — e que a guarda **detecte divergência plantada**, com
recusa atômica. A primeira sozinha passaria por vacuidade se a guarda nunca recusasse.

> **`migra_bloco19_tipos.py` afirmava idempotência no próprio cabeçalho, e não era verdade.**
> Por isso a guarda é mecânica: afirmação de idempotência em prosa não é idempotência.

> **A guarda de R12 seguiu os scripts.** `test_aceite_nivel1.py` varre por AST os `.py` de
> `scripts/calculo/` **e dos `scripts/` das quatro skills**: sair daqui não podia tirar
> ninguém da proibição de `float`. E as guardas que liam a fonte por
> `Path(__file__).parent / "nome.py"` passaram a lê-la pelo `__file__` do **módulo
> importado** — assim acompanham o script para onde ele for da próxima vez.

## `test_metodos.py` — o procedimento dos dois métodos, contra célula publicada

**Bloco 23.** Até então **nenhum teste confrontava `metodos.py`** — `grep -l metodos
scripts/calculo/test_*.py` devolvia **vazio**, e a única verificação era um `hasattr` dentro do
runner de aceitação, que afere que a função **existe** e não que ela está **certa**. Estava errada:
a regra `T3` proibia, em prosa, a célula `55,75 × 43,89% = 24,46` que o manual **publica** na
`pagina_pdf` 52 e que o consolidado **já usava** como prova de truncamento.

**Não precisa de série, e é o ponto.** Os coeficientes estão **impressos** no PDF com 10 casas. O
que se afere é o **procedimento**: dado o coeficiente publicado, a sequência de operações e de
truncamentos reproduz — ou não — o número publicado. Reproduz **3.484,95** (`pagina_pdf` 51),
**5.218,27** (52), **5.218,28** (53) e **4.435,07 · 4.435,04 · Δ 0,03** (91–92), célula por célula.

**O que não fecha fica declarado com `skipTest` e a razão** — o rótulo do corte de dez/2021
(lacuna #3), o coeficiente a partir da série mensal (camada B) e a fixture 3, que tem um método só.
**Nunca silenciado, nunca ajustado para caber.**

## `test_aceite_nivel1.py` — o critério de aceite DA SKILL

**Bloco 23.** O conjunto declara **não carregar série de índices** e usava como critério de aceite
quatro fixtures do CJF que **consomem série** — a fixture 1 sozinha, 23 meses de IPCA-E. **As duas
afirmações não podem ser verdadeiras ao mesmo tempo.** A resolução não foi popular série; foi
declarar o nível:

| | O que é | Executável |
|---|---|---|
| **NÍVEL 1** | invariantes e aritmética: **R11** pelos dois pares publicados, **R12** por AST, **R1 na composição**, as **cinco cadeias de arredondamento**, o **NMP de três ramos** | **só com a skill** — este arquivo |
| **NÍVEL 2** | as **quatro fixtures** de `tests/fixtures/calculo/` | **exige série carregada** |

**NÍVEL 1 é o aceite da SKILL; NÍVEL 2 é o aceite do SISTEMA.** O conteúdo do NÍVEL 1 não é lista
idealizada: é o que a Frente A do bloco 22 de fato acertou sem série nenhuma
(`bloco-22-relatorio.md` § 1).

**Por que aqui e não em `tests/fixtures/calculo/` nem só numa seção de skill:** aquele diretório é
**dado**, e seção de skill **declara, não verifica**. Este é o único diretório que roda inteiro em
toda varredura. **Critério de aceite que ninguém roda envelhece** — foi exatamente o que aconteceu
com a afirmação que o bloco 23 veio corrigir, e por isso o arquivo também **guarda a própria
declaração**: falha se o README das fixtures ou as duas `SKILL.md` deixarem de declará-lo.

**Não é motor de cálculo** — a restrição de "O que não entra" segue valendo. Cada asserção está
ancorada em **número publicado pelo corpus**; não se liquida condenação e não se consulta série.
A varredura de R12 por AST **exclui os `test_*.py`**, e a exclusão é necessária:
`test_valida_taxa_legal.py` e `test_valida_parametros.py` **plantam float de propósito** para
provar que o caminho aritmético o recusa.

## Descoberta é por CONTEÚDO, nunca por convenção de nome

Regra do repositório desde o bloco 17, agora valendo também em código. Nenhum validador
decide o que ler pelo prefixo ou sufixo do nome do arquivo:

- `valida_cadeias.py` reconhece cadeia por `tipo == "cadeia-temporal"` e `segmentos` lista —
  não por `cjf.` / `trab.`;
- `valida_bloco_tabelas.py` varre `*.csv` do diretório de séries — **não** `serie-*.csv` —
  e resolve a faixa de páginas pelo cabeçalho declarado no próprio arquivo;
- os nomes de arquivo cravados que sobram (`trt3-18.1-incidencia-parcelas.json`, os CSV
  conferidos um a um) são **abertos direto**: se sumirem, o script morre com
  `FileNotFoundError`. Falha alta é aceitável; silêncio não é.

## Manifesto de cadeias — `skills/calculo-judicial-atualizacao/regras/cadeias-manifesto.json`

**PISO, não retrato.** `valida_cadeias.py` sai com **exit 1** se encontrar **menos** cadeias
do que o manifesto declara, ou cadeia com **menos** segmentos do que ele registra. A chave é
o campo `id`, nunca o nome do arquivo — renomear não pode acusar ausência.

Cadeia **a mais** é crescimento normal: o próprio script **grava** a entrada nova e avisa na
saída. Isso é deliberado — manifesto que exige edição manual a cada cadeia nova envelhece
igual à constante `== 11` que ele veio substituir. Cadeia **a menos** é regressão, e
desfazê-la exige editar o manifesto à mão, com o porquê no commit.

```
python valida_cadeias.py                            # confere e grava o crescimento
python valida_cadeias.py --sem-atualizar-manifesto  # só confere, não escreve (CI)
```

As guardas de `tipo_indexador` em `test_valida_cobertura.py` leem o mesmo manifesto, em vez
de cravar a contagem.

## `test_classes_de_indice.py` — a skill não diverge do catálogo

**O catálogo é a fonte; a skill APONTA, não copia.** Varre os `.md` de `skills/` — espinha e
`references/`, **sem exclusão nenhuma** — atrás de afirmação de classe de R3, e falha quando o
rótulo afirmado tem outra classe em `indexadores-tipo-catalogo.json`. Nasceu porque **IPCA-E e
IPCA-15 viraram `janela-deslocada` no bloco 19 e duas skills continuaram publicando
`indeterminado` até o bloco 23**, com as fixtures 1 a 3 apoiadas exatamente nisso.

**Dois idiomas, nenhuma janela de proximidade:** a linha de tabela com uma célula de classe — o
índice fica na célula vizinha, e a direção depende de a célula ser **só** o token ou o **rótulo**
da classe — e o predicado em prosa *"X e Y são `classe`"*, que era a forma das duas divergências
reais. **Medido antes de decidir:** a alternativa por proximidade de ±60 caracteres devolvia 52
achados divergentes, dos quais **48 eram falso positivo**, todos pela prosa que **ensina** R3
pondo as classes lado a lado. **Custo aceito e declarado: este arquivo NÃO tem ledger de
exceções.** Não há divergência legítima aqui — ou é a classe do catálogo, ou é defeito —, e a
cobertura parcial se paga com uma falha que nunca precisa ser anistiada. As medições, o que passa
ileso e a razão de `docs/` ficar fora estão no docstring.

## `test_ponteiros.py` — ponteiro morto não volta

Varre `README.md`, `docs/`, `skills/` e `scripts/` (`.md` e `.json`) atrás de referência a
caminho que não existe. O escopo, o que **não** é verificado e a razão de cada exclusão estão
no docstring do arquivo — leia antes de acrescentar exceção. Narrativa histórica (o nome
anterior de um script, os nomes de `references/` anteriores ao bloco 16) é tolerada por um
**ledger declarado e autolimpante**: a exceção vale para o par *(alvo, arquivo)* e para
mais nenhum, e uma segunda checagem falha quando a exceção fica órfã — alvo que passou a
existir, ou menção que sumiu.

> Este parágrafo já citou por nome o script renomeado, e **o teste o acusou**: o par
> *(alvo, arquivo)* tolerava a citação nos três relatórios que narram a fusão, não num
> README novo. Era o comportamento pedido — e é a razão de a chave não ser o alvo sozinho.

**Proveniência: a faixa de páginas se resolve por arquivo, nunca por constante de bloco.**
`valida_bloco_tabelas.py` varre todos os CSV do diretório, e o diretório recebe séries
de blocos diferentes. A faixa contra a qual cada linha é conferida vem, nesta ordem: **(1)** do
`pagina_pdf=` declarado no cabeçalho de comentário do próprio CSV; **(2)** do `item` da linha,
resolvido em `FAIXAS_DE_PAGINA`. Sem nenhuma das duas o arquivo sai como **não verificável** —
não como erro, e nunca em silêncio. Uma constante única de bloco produzia falso erro permanente
em série de outro bloco, e falso erro permanente treina quem lê a ignorar o relatório.

**R3 lê `tipo_indexador`**, de domínio fechado em seis valores — `nominal`, `percentual`,
**`janela-deslocada`**, `nao-indexador`, `indeterminado`, e `englobante` **retirado**. O
catálogo, com a fonte de cada classificação, é
`skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json`. **Sem fonte o valor é
`indeterminado`, e a virada BLOQUEIA sob a regra `R3-INDETERMINADO`** — passar converteria
"não se sabe" em "está certo". Pendências em `docs/calculo/pendencias.md` §§ 23 e 25.

### Bloco 19 — três classes com defasagem, e duas razões de `indeterminado`

**`janela-deslocada`** é a classe de quem coleta a cavaleiro de dois meses: **metade em M−1,
metade em M** — do dia 16 do mês anterior ao dia 15 do mês de referência. É o **IPCA-15** e o
**IPCA-E**, e quem o sustenta é **fonte externa ao corpus** (IBGE), declarada como externa no
catálogo. Com três classes há **três pares** de virada, e a regra **não os enumera**: exige que
os dois lados estejam em `TIPOS_COM_DEFASAGEM` e sejam diferentes.

**`englobante` foi RETIRADO.** Era erro de categoria — englobamento é fato de **R1**, gravado
em **`engloba`**, que não mudou. O efeito era deixar a **SELIC cega para R3**: ela saltava a
comparação de defasagem embora tenha defasagem. A SELIC passou a **`percentual`**; a **taxa
legal**, que fonte alguma alcança, a **`indeterminado`** (`P19-01`) — **não** `percentual` por
analogia. O valor segue legível no domínio, e um teste prova que **nenhuma cadeia voltou a
usá-lo**.

**`tipo_indexador_razao` não é `tipo_indexador_pendencia`**, e são mutuamente excludentes.
Pendência afirma *"não há fonte"* e **fecha quando a fonte chegar**. Razão afirma *"há fonte, e
ela diz que o índice não cabe em mês calendário"* — a da TR é *"período entre datas de
aniversário e prefixação"* — e **não se fecha esperando fonte**. As duas bloqueiam a virada; o
que muda é a mensagem, e é ela que diz a quem audita se vale a pena esperar.

```
python valida_cadeias.py
```

> **O placar não é transcrito aqui.** Cadeias, R1, R2 e R3 — com a composição de R3 entre
> confirmada e `R3-INDETERMINADO` — vivem em
> [`docs/calculo/consolidado/00-numeros.md`](../../docs/calculo/consolidado/00-numeros.md),
> **gerado por script a partir do estado real**. Placar digitado no comentário de um runbook é
> exatamente o que o bloco 18 deixou envelhecer: *"14 ok, 10 erros"* depois de os erros sumirem.

**O que segue é REGISTRO DATADO DO BLOCO 19, e não se atualiza.** São os números que valiam **ao
fim daquele bloco**. Narrativa de variação só é auditável se as duas pontas ficarem como estavam
— relatório que se atualiza sozinho deixa de ser registro. Para o estado de agora,
`00-numeros.md`.

**R3 foi de 46 para 51 na Tarefa 2 e de 51 para 62 na Tarefa 3**, e os dois saltos vão em
separado porque é isso que permite auditar de novo.

**Tarefa 2 — R3 de 46 para 51, e a variação é ACHADO, não regressão.** Oito violações novas,
três fechadas. As novas: **2** `Selic → IPCA-15/IBGE` (a SELIC deixou de saltar R3), **5**
`Selic → taxa-legal` sob `R3-INDETERMINADO` (a taxa legal perdeu o salto e não tem classe), e
**1** `Ufir → IPCA-E/IBGE` que era indeterminada e virou **confirmada**. As fechadas: uma
`Ufir → IPCA-E` salva por `aplicacao` declarada, uma que reabriu como confirmada, e
`IPCA-E → IPCA-15`, que deixou de ser virada porque os dois são a **mesma classe**. **Nesta
tarefa R1 e R2 não se moveram** (15 e 1) — nenhuma cadeia mudou de conteúdo.

**Tarefa 3 — cinco cadeias novas: 15 → 20 cadeias, R1 de 15 para 21, R3 de 51 para 62, R2
segue em 1.** **As 6 violações novas de R1 são do MANUAL**, não do gerador: **2** herdadas do
tronco na `desapropriacao-indireta.correcao-monetaria` (1989-01 `IPC/IBGE × OTN` e 1990-03
`BTN × IPC/IBGE`, idênticas às da direta); **3 cortes intramensais**, em que o mês da fronteira
cai nos dois segmentos — `desapropriacao-indireta.juros-compensatorios` 1997-06 (*"até 10/6"* ÷
*"de 11/6"*), `divida-fiscal.juros-mora` 1992-01 (*"a 2/1/1992"* ÷ *"de 3/1/1992"*) e
`divida-fiscal.correcao-monetaria` 1989-01 (OTN ÷ BTN); e **1** que é o **`D8-C8` de maio/2000**,
`fgts-divida-fiscal.correcao-monetaria` `TRD × TR`, com maio/2000 nos dois. **R2 seguiu em 1.**

## O que não entra

- **Motor de cálculo.** Estes scripts validam artefatos; não calculam condenação.
- Séries de valores.
- Qualquer uso de `float`. R12 é absoluto: `Decimal` em todo caminho aritmético.

## Convenções

- Python 3.11.
- `encoding='utf-8'` **explícito** em toda leitura de arquivo. Windows assume cp1252
  e corrompe acentuação silenciosamente.
- Aritmética de competência em `YYYY-MM`.
- Truncamento (`ROUND_DOWN`), nunca arredondamento. Ver `docs/calculo/pendencias.md`.

## Execução

```
python -m unittest discover -s scripts/calculo -p "test_*.py" -v
```

## Nota de convenção

Este repositório é Python; o SaaS jurídico que consumirá o motor é .NET 10 + Angular.
São bases separadas de propósito: aqui ficam a extração e a validação normativa,
lá fica o produto. A portabilidade do motor para C# é decisão da Fase 5.
