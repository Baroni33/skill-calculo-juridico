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
| 6 | Presets de regime temporal | `docs/calculo/extracao/bloco-06-relatorio.md` |
| 7 | Descontos previdenciário e fiscal, cap. 9, p. 107–208 | `docs/calculo/extracao/bloco-07-relatorio.md` |
| 8 | Manual de Cálculos da Justiça Federal, CJF Res. 990/2026, integral | `docs/calculo/extracao/justica-federal/bloco-08-relatorio.md` |
| 9 | Cadeias históricas de atualização trabalhista — TRT-3, cap. 7, p. 83–99, extração dirigida | `docs/calculo/extracao/trabalhista/bloco-09-relatorio.md` |
| 10 | Fechamento trabalhista — cap. 7 residual, 11, 13, 15 e 17 | `docs/calculo/extracao/trabalhista/bloco-10-relatorio.md` |
| 11A | Capítulo 10 — varredura estrutural e item 10.1 (atualização sem amortização) | `docs/calculo/extracao/trabalhista/bloco-11a-relatorio.md` |
| 11B | Capítulo 10, segmento C — amortização de valor pago (art. 12-A) | `docs/calculo/extracao/trabalhista/bloco-11b-relatorio.md` |

O **Manual de Cálculos da Justiça Federal (CJF, Res. 990/2026) está integralmente extraído** —
93 páginas, sete cadeias temporais em `tabelas-normativas/`, e é a única fonte do corpus cuja
edição está vigente.

O **bloco 9** acrescenta quatro cadeias históricas trabalhistas (`trt3.hist.*`) e corrige o
validador de cobertura: a exaustividade dos ramos condicionados passou a ser **declarada**
(`dominio_condicoes`), não presumida. A primeira versão do conserto escondia lacuna real —
ver `bloco-09-relatorio.md` § 2.

**O artefato que abre a Fase 3 é [`docs/calculo/extracao/mapa-de-cobertura.md`](docs/calculo/extracao/mapa-de-cobertura.md)** —
todo capítulo e item dos dois manuais, com o bloco que o cobriu ou a razão de não ter sido
coberto. Conferido por script: **cobertura de 84,5%**, separando **não coberto com decisão
registrada** (51 pp.) de **não coberto sem decisão** (14 pp. — capítulos 8, 12 e 14).

O **capítulo 10** está em extração pela série 11A–11D, dividida **por operação** — 45 das 69
páginas cobertas. O **bloco 11B** respondeu a invariante **R10**:

> A imputação de pagamento parcial no trabalhista é **proporcional** — o pagamento abate
> principal e juros na razão em que compõem o bruto (item 10.3.1, letra F, p. 237). **E não
> tem fundamento normativo declarado:** `art. 354` não ocorre em nenhuma das 471 páginas,
> enquanto `proporcional` ocorre 101 vezes só no segmento. R10 fica fundamentada por razão
> mais forte que a suposta — não são duas normas concorrentes, mas **uma norma (art. 354 do
> CC) contra um costume de liquidação sem base declarada**.

A escolha da ordem de imputação move o saldo em até **23,83%** (juros primeiro: +10,58%;
principal primeiro: −13,25%) — **a decisão mais cara já medida no corpus**.

O **bloco 10** fecha a extração trabalhista com o índice de jurisprudência
([`docs/calculo/jurisprudencia-indice.md`](docs/calculo/jurisprudencia-indice.md), 158 verbetes,
dos quais **a base normativa cobre 12**) e 17 regras estruturais que só existiam dentro dos
exemplos do capítulo 11.

**Achado estrutural do bloco 9:** o capítulo 7 do TRT-3 **não traz cadeia período → indexador**.
Ele delega o encadeamento histórico à Tabela Única do CSJT. A cadeia trabalhista anterior a
março de 1991 continua sendo pendência do corpus (**P9-02**).

Do Manual TRT-3, o **capítulo 6 está integralmente extraído**, e agora também o **capítulo 9**
(descontos previdenciário e fiscal, p. 107–208) — o maior do manual, 102 páginas e 47 itens.
Nenhuma skill escrita.

O **bloco 6** acrescentou a camada que decide *qual regra* vale em cada competência,
distinta da que decide *quanto vale* cada parâmetro: 26 regimes e **catorze eixos de
corte distintos** — e apenas dois deles são de competência ou fato. Cinco regimes
ficaram inaplicáveis porque o corpus dá a data de corte sem dizer qual data governa.
Ver `docs/calculo/presets-regime.md` e `docs/calculo/pendencias.md` § 19.

O bloco 5 está **completo em cobertura e provisório em classificação**: os 32 parâmetros
negociáveis estão consolidados e a fixture do ACT Gasmig é real, mas **27 dos 30 incisos do
art. 611-B da CLT não estão no corpus**, o que deixa 16 parâmetros com
`classificacao_provisoria: true`. Ver `docs/calculo/extracao/bloco-05-relatorio.md` §§ 1-A e 7,
e `docs/calculo/pendencias.md` § 15.
