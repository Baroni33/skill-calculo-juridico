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

**R3 lê `tipo_indexador`**, de domínio fechado em cinco valores — `nominal`, `percentual`,
`englobante`, `nao-indexador`, `indeterminado`. O catálogo, com a fonte de cada
classificação, é `docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json`. **Sem
fonte o valor é `indeterminado`, e a virada BLOQUEIA sob a regra `R3-INDETERMINADO`** —
passar converteria "não se sabe" em "está certo". Pendências em
`docs/calculo/pendencias.md` § 23.

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
