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
| `metodos.py` | **bloco 23** — os **dois procedimentos** do manual, `resumido()` e `detalhado()`, a partir de `references/metodos-resumido-e-detalhado.md`. No bloco 22 não existia porque os métodos não eram definidos em lugar nenhum |
| `runner.py` | roda as quatro fixtures + os autotestes de NÍVEL 1 + a **prova da asserção** |
| `registro-de-lacunas.md` | **metade da entrega** — 12 lacunas, o que foi discordado, o que quase se inventou e o que se inventou. **Registro datado do bloco 22: não se reescreve** |

**Leia o registro de lacunas antes do código.** O resultado do bloco 22 foi que **as quatro
fixtures são impossíveis** com o que as skills entregam: falta a camada (B) inteira (que as
skills declaram externa) e faltava o procedimento dos métodos "resumido" e "detalhado".

## O que o bloco 23 mudou aqui

**A tolerância deixou de ser banda.** As fixtures 2 e 4 declaram
`divergencia_e_assercao: true`: os dois métodos produzem **dois números**, e a **diferença entre
eles é a asserção**. O runner agora:

- **não passa** motor que produz **um número só** — ainda que o número esteja certo (`FALTA_UM_METODO`);
- **falha** motor que produz **dois números iguais** (`DIVERGENCIA_ZERADA`) — zerar significa
  arredondar errado;
- exige o delta **exato**: R$ 0,01 na fixture 2, R$ 0,03 na fixture 4. Fixtures 1 e 3 declaram
  `tolerancia 0,00` e são comparadas por **igualdade**. **Não há banda em lugar nenhum.**

**As fixtures seguem bloqueadas por série ausente — isso não mudou.** Como `asserir_par` nunca é
exercida por elas, o runner traz uma **prova da asserção** com entradas sintéticas, que roda sem
série e verifica os quatro comportamentos acima. Correção de comparador que ninguém roda
envelhece.

**A redação também estava errada, e induziu o defeito:** *"as fixtures 2 e 4 divergem **do
corpus**"* se lê como banda. Elas divergem **entre os dois métodos do próprio manual**. Corrigida
nas skills no mesmo bloco.

Nenhuma fixture foi ajustada. Nenhum índice veio da web.
