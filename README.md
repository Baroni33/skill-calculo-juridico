# skill-calculo-juridico

Base para construir o módulo de cálculo judicial (cível, trabalhista, tributário
federal) do SaaS jurídico. Repositório **separado** do SaaS: aqui ficam a extração
normativa, as tabelas de regra e as skills; lá fica o produto.

A skill não é o entregável. O código que um agente constrói lendo a skill é.

## Fonte de verdade

| Documento | Papel |
|---|---|
| `docs/calculo/00-base-normativa.md` | Regras vigentes, validadas contra fontes primárias e acórdãos. **Prevalece sobre os manuais em PDF.** |
| `docs/calculo/01-plano-extracao.md` | Arquitetura das skills, schemas, triagem do corpus, pipeline |
| `docs/calculo/fontes.md` | Localização dos PDFs e offsets de paginação |
| `docs/calculo/pendencias.md` | O que está em aberto e o que bloqueia |

Os dois manuais em PDF **não são versionados aqui** — ver `docs/calculo/fontes.md`.

## Estrutura

```
docs/calculo/
  extracao/trabalhista/        Fase 2 — um arquivo por bloco de páginas
  extracao/justica-federal/    Fase 2 — passada única
  tabelas-normativas/          JSON de regra (não de série)
  confronto-normativo/         Fase 4 — só trabalhista
skills/
  calculo-judicial-core/           domínio, invariantes, aritmética, comparador
  calculo-judicial-atualizacao/    cadeias período→indexador, com references/
  calculo-trabalhista-liquidacao/  verbas, descontos, encargos
  indices-judiciais/               semântica dos índices e contrato de séries
scripts/calculo/             validadores determinísticos
tests/fixtures/calculo/      fixtures de aceite, seção 8 da base normativa
```

Cada pasta tem `README.md` com propósito, o que entra, o que não entra e a fase do
pipeline. Nenhuma contém conteúdo normativo ainda.

## Validadores

```
python -m unittest discover -s scripts/calculo -p "test_*.py"
python scripts/calculo/valida_taxa_legal.py --validar
python scripts/calculo/valida_bloco_tabelas.py     # exit 0 = sem erro de extração
python scripts/calculo/extrai_bloco_01.py          # reextrai o bloco 1
python scripts/calculo/valida_parametros.py --catalogo-ok
```

| Script | Verifica |
|---|---|
| `valida_cobertura.py` | R1 (englobamento concorrente), R2 (lacuna/sobreposição) |
| `valida_taxa_legal.py` | R6 (piso zero), R11 (razão, não subtração), R12 (decimal, truncamento) |
| `valida_bloco_tabelas.py` | Bloco 1: contagem contra o PDF, faixas, vigências, proveniência |
| `valida_parametros.py` | Camada de norma coletiva: R14 a R18, precedência, conflito, piso legal |

`valida_bloco_tabelas.py` separa **erro de extração** de **divergência do original** e só
sai com código não-zero no primeiro. Divergência é resultado esperado do trabalho: o
manual tem erros de digitação e calendários com dias faltando, e eles ficam registrados.

## Duas regras que economizam retrabalho

**Truncamento, nunca arredondamento.** Os dois pares de validação do Manual CJF só
fecham com truncamento; half-up erra o último dígito em ambos. Ver
`docs/calculo/pendencias.md` § 3.

**`encoding='utf-8'` explícito em toda leitura.** Windows assume cp1252 e corrompe
acentuação silenciosamente. A mojibake que aparece no terminal é renderização do
console, não corrupção do arquivo.

## Estado

Fases 0 e 1 fechadas (contrato de saída e triagem).

Fase 2 em curso.

| Bloco | Conteúdo | Relatório |
|---|---|---|
| 1 | Tabelas do Manual TRT-3, p. 373–471 | `docs/calculo/extracao/trabalhista/bloco-01-tabelas.md` |
| 2 | Critérios e estrutura do cálculo, p. 9–17 | `docs/calculo/extracao/trabalhista/bloco-02-relatorio.md` |
| 3 | Verbas trabalhistas, itens 6.1 a 6.6, p. 18–55 | `docs/calculo/extracao/trabalhista/bloco-03-relatorio.md` |
| 4 | Verbas trabalhistas, itens 6.7 a 6.15, p. 55–82 | `docs/calculo/extracao/trabalhista/bloco-04-relatorio.md` |
| 5 | Parâmetros negociáveis e camada de norma coletiva | `docs/calculo/extracao/bloco-05-relatorio.md` |

O **capítulo 6 do Manual TRT-3 está integralmente extraído**. Demais blocos não iniciados.
Nenhuma skill escrita.

O bloco 5 está **completo em cobertura e provisório em classificação**: os 32 parâmetros
negociáveis estão consolidados e a fixture do ACT Gasmig é real, mas **27 dos 30 incisos do
art. 611-B da CLT não estão no corpus**, o que deixa 16 parâmetros com
`classificacao_provisoria: true`. Ver `docs/calculo/extracao/bloco-05-relatorio.md` §§ 1-A e 7,
e `docs/calculo/pendencias.md` § 15.
