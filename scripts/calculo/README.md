# scripts/calculo — validadores determinísticos

**Fase do pipeline:** Fase 2 (validação da extração tabular) e Fase 6 (aceitação).

## Propósito

Validação **determinística**, por script, não por revisão de LLM (regra 2 do plano).
Dado tabular e aritmética normativa se verificam com código.

## Conteúdo

| Script | Verifica |
|---|---|
| `valida_cobertura.py` | R1 (englobamento concorrente) e R2 (cobertura sem lacuna nem sobreposição) |
| `valida_taxa_legal.py` | `TL = (Fator_Selic / Fator_Deflator - 1) × 100`, truncado a 6 decimais, piso zero |

Testes em `test_valida_cobertura.py` e `test_valida_taxa_legal.py`.

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
