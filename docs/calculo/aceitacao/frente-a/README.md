# Aceitação — frente A

Motor de atualização escrito **só a partir das quatro `skills/` e do que elas apontam**, para
reproduzir as quatro fixtures de `tests/fixtures/calculo/`.

```
python runner.py
```

Saída: `0` se tudo bateu; `1` se alguma fixture divergiu ou um autoteste falhou; **`2` se alguma
fixture ficou BLOQUEADA por dado ou procedimento ausente**. Hoje sai **2**.

| Arquivo | O que é |
|---|---|
| `aritmetica.py` | R12 — as cinco cadeias de arredondamento, taxa legal por razão (R11), pisos R5/R6, NMP de três ramos, `1/30` como dízima. **Nenhum float** |
| `series.py` | camada **(B)**. Nasce quase vazia por decisão declarada das skills; levanta `SerieAusente` com o escopo de busca |
| `cadeias.py` | camada **(A)**. Lê `docs/calculo/tabelas-normativas/*.json`, resolve segmento, checa R2 e impõe **R1 na composição** (NOTA 2 do item 4.2.1) |
| `motor.py` | correção, juros simples, D1/D2, consolidação de dez/2021, honorários, R23 (descarregar) e R10 (que **recusa** arbitrar `pr.imputacao`) |
| `runner.py` | roda as quatro fixtures + autotestes, honrando o campo `tolerancia` |
| `registro-de-lacunas.md` | **metade da entrega** — 12 lacunas, o que foi discordado, o que quase se inventou e o que se inventou |

**Leia o registro de lacunas antes do código.** O resultado deste teste é que **as quatro
fixtures são impossíveis** com o que as skills entregam: falta a camada (B) inteira (que as
skills declaram externa) e falta o procedimento dos métodos "resumido" e "detalhado" (que as
skills mencionam e nunca definem).

Nenhuma fixture foi ajustada. Nenhuma skill foi consertada. Nenhum índice veio da web.
