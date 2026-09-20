# scripts/calculo — validadores determinísticos

**Fase do pipeline:** Fase 2 (validação da extração tabular) e Fase 6 (aceitação).

## Propósito

Validação **determinística**, por script, não por revisão de LLM (regra 2 do plano).
Dado tabular e aritmética normativa se verificam com código.

## Conteúdo

| Script | Verifica |
|---|---|
| `valida_cobertura.py` | R1 (englobamento concorrente), R2 (cobertura sem lacuna nem sobreposição) e **R3 (virada entre tipos de indexador sem ajuste de defasagem)** |
| `valida_taxa_legal.py` | `TL = (Fator_Selic / Fator_Deflator - 1) × 100`, truncado a 6 decimais, piso zero |
| `valida_bloco_tabelas.py` | Extração tabular do bloco 1 (Manual TRT-3): contagem contra o PDF, faixas, vigências, proveniência e calendários |
| `valida_cadeias.py` | CLI de R1/R2/R3 sobre as cadeias, e o **manifesto de cadeias** |
| `migra_bloco19_tipos.py` | **Não valida — reescreve.** Migração idempotente do bloco 19: `tipo_indexador` da SELIC, da taxa legal, do IPCA-E/IPCA-15 e da família TR. Mantido para que a alteração seja auditável segmento a segmento (`--conferir` só lista) |

Testes em `test_valida_cobertura.py`, `test_valida_taxa_legal.py`,
`test_valida_bloco_tabelas.py` e `test_ponteiros.py`.

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

## Manifesto de cadeias — `docs/calculo/tabelas-normativas/cadeias-manifesto.json`

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
`docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json`. **Sem fonte o valor é
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
python valida_cadeias.py    # 20 cadeias | R1: 21 | R2: 1 | R3: 62
```

**R3 foi de 46 para 51 na Tarefa 2 e de 51 para 62 na Tarefa 3.** O número publicado acima é o
**final do bloco**; os dois saltos são narrados em separado porque é isso que permite auditar
de novo.

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
