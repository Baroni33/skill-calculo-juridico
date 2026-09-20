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

Testes em `test_valida_cobertura.py`, `test_valida_taxa_legal.py` e
`test_valida_bloco_tabelas.py`.

**Proveniência: a faixa de páginas se resolve por arquivo, nunca por constante de bloco.**
`valida_bloco_tabelas.py` varre todos os `serie-*.csv` do diretório, e o diretório recebe séries
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
