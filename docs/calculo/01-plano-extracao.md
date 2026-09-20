# Plano de extração e arquitetura das skills

## Objetivo final

Um conjunto de skills que permita a um agente sem contexto prévio implementar o módulo de cálculo judicial do SaaS, com resultado que bate com fixtures conhecidas.

A skill não é o entregável. O código que um agente constrói lendo a skill é.

---

## Regra de projeto — identificador não carrega semântica que o campo já expressa

**Estabelecida no bloco 17, depois de a ambiguidade de etiqueta morder o projeto três vezes.**

| Quando | O quê | O que custou |
|---|---|---|
| bloco 15 | `F1`–`F9` do bloco 03 × `F1`–`F7` do bloco 04 | remissões cruzadas apontando para o ponto errado |
| bloco 15 | a renumeração `B03-`/`B04-` foi **cega** | reescreveu *"mesma raiz do F1 **do bloco 3**"* como `B04-F1` — **alvo errado, com rótulo bem-formado** |
| bloco 16 | `RG1`–`RG15` (regionais) × `R1`–`R24` (invariantes) | a **invariante R8** virou a **Súmula 48 do TRT-3**, cancelada e sobre prazo rescisório |

**A regra:**

> **O identificador identifica. O escopo se declara em campo.** A aplicação é decidida por
> `jurisdicao`, `tribunal`, `competencia` — **nunca pelo prefixo do id nem pelo nome do arquivo**.

**Três corolários, cada um com um caso real:**

1. **Prefixo de tribunal num id de regra nacional é defeito.** As cadeias `trt3.hist.*` têm
   fundamento em CC arts. 1.062–1.063, Lei 8.177/91 e Súmulas 200 e 381 do TST, com a correção
   delegada à Tabela Única do CSJT. Renomeadas para **`trab.hist.*`** no bloco 17, junto com
   sete `trt3.trabalhista.*` que são **IRRF, INSS, GILRAT, URV e RSR** — lei federal;
2. **Descoberta por nome de arquivo é a mesma falha, do lado do código.** `valida_cadeias.py`
   filtrava por `("cjf.", "trt3.hist.")`; a renomeação fez o validador cair de **11 cadeias para
   7 em silêncio**, seguindo a imprimir "OK" sobre as sete restantes. Passou a reconhecer cadeia
   por `tipo == "cadeia-temporal"`. Mesma espécie em `valida_bloco_tabelas.py`, que resolvia
   proveniência por `range` de páginas **constante**, acusando dez falsos erros permanentes;
3. **Namespaces distintos não compartilham letra.** `RG` para regra regional, `R` para
   invariante. **Se dois rótulos podem ser lidos um pelo outro, um dos dois está errado.**

**E toda renomeação é verificada:** listar as referências **antes**, aplicar por **mapa
explícito** — nunca regex cego —, e conferir que **nenhuma remissão mudou de sentido**. A do
bloco 17 fechou em **zero resíduos e zero remissões alteradas**, sobre 67 ocorrências.

---

## Arquitetura das skills

Fronteira por **eixo de mudança**, não por documento de origem. Documentos são fontes; o TRT-3 e o TJMG mudam pelos mesmos eventos legislativos e têm a mesma forma de regra.

| Skill | Eixo | Frequência de mudança |
|---|---|---|
| `calculo-judicial-core` | Modelo de domínio, invariantes, aritmética decimal, memória de cálculo, comparador/diff, catálogo de critérios | Rara |
| `calculo-judicial-atualizacao` | Cadeias período→indexador e período→juros, com `references/` por jurisdição | A cada mudança legislativa |
| `calculo-trabalhista-liquidacao` | Apuração de verbas, descontos legais, encargos | Média |
| `indices-judiciais` | Semântica de aplicação dos índices e contrato com a tabela mantida à parte | Mensal |

`references/` da skill de atualização, organizados por variante:
```
references/
  trabalhista-privado.md
  trabalhista-fazenda.md
  civel-cc-tema1368.md
  civel-mg-cgj.md
  tributario-federal.md
  previdenciario.md
```

O agente carrega só o arquivo da jurisdição em questão.

**Comparador fica no core**, não na skill trabalhista: "recalcular pelo critério correto e produzir o diff parcela a parcela" é a mesma operação nas três jurisdições.

**Encargos processuais** ficam provisoriamente em `calculo-trabalhista-liquidacao`, mas provavelmente se separam: as faixas de honorários são do CPC art. 85, § 3º, não da CLT, e valem nos três ramos.

---

## Schema da espinha (SKILL.md)

Estrutura fixa para toda skill do conjunto, para que o agente saiba onde procurar.

```
frontmatter: name, description (explícita e "pushy" sobre quando disparar)
## Quando usar / quando não usar
## Modelo de domínio       — entidades e vocabulário mínimo
## Invariantes             — regras que, violadas, produzem erro material
## Procedimento            — passo a passo do cálculo
## Catálogo de critérios   — resumo; detalhe em references/
## Armadilhas conhecidas   — casos difíceis
## Fixtures de aceite      — casos com resultado numérico esperado
## Ponteiros               — references/ e scripts/
```

SKILL.md abaixo de 500 linhas. Passando disso, mais uma camada de hierarquia com ponteiro explícito.

---

## Schema das tabelas normativas

Artefato central. Representa **regra**, não série de valores.

```json
{
  "id": "trab.correcao-monetaria.privado",
  "jurisdicao": "justica-do-trabalho",
  "tipo_acao": "reclamacao-trabalhista",
  "componente": "correcao-monetaria",
  "fonte": { "documento": "...", "norma": "...", "item": "4.2.1.1", "pagina": 48 },
  "vigencia_norma": { "desde": "2024-10-25" },
  "segmentos": [
    {
      "inicio": "2021-12", "fim": "2024-08",
      "indexador": "SELIC",
      "condicao": { "devedor": "fazenda-publica" },
      "engloba": ["correcao-monetaria", "juros-mora", "compensacao-mora"],
      "capitalizacao": "simples",
      "aplicacao": "mes-posterior-a-competencia",
      "fundamento": "EC 113/2021, art. 3º"
    }
  ]
}
```

Campos obrigatórios e por quê:

- **`engloba`** — torna a checagem de cumulação (R1) mecânica. Segmento que engloba juros não admite segmento de juros concorrente no mesmo período.
- **`condicao`** — as tabelas bifurcam por qualidade do devedor, mas também por **data da sentença** (desapropriação: antes/depois de 27/09/1999 e 13/09/2001) e por **data do fato gerador** (dívida fiscal: até 31/12/1994 ou a partir de jan/1995).
- **`aplicacao`** — a defasagem é fonte silenciosa de divergência. "Mês posterior ao da competência" e "mês seguinte ao da citação até o mês anterior ao pagamento, mais 1% no mês do pagamento" dão resultados diferentes sobre a mesma série.
- **`multiplicador_transicao`** — conversões de moeda e indexador: débitos anteriores a jan/1989 multiplicados por 6,17 (ou 6,92 para IR); último BTN a 126,8621.
- **`valor_fixo_pct`** — expurgos com percentual cravado: jan/1989 = 42,72%; fev/1989 = 10,14%.

Para juros, mesmo esqueleto mais **`base_incidencia`** — as tabelas fiscais distinguem juros sobre valor originário e sobre valor corrigido.

Para faixas (INSS, IRRF): vigência + faixas com alíquota e parcela a deduzir.

Para o catálogo de índices, o campo que não pode faltar é **`tipo: nominal | percentual`** (ver invariante R3).

---

## Catálogo de critérios — presets

O usuário escolhe **presets** (cadeias nomeadas e completas). O motor compõe **segmentos**. A interface nunca expõe segmento solto: é montando bloco a bloco que se produz combinação inválida.

### Justiça do Trabalho

| ID | Quando |
|---|---|
| `TRAB-ADC58-LEI14905` | Devedor privado — **default** |
| `TRAB-ADC58-SEM-TRD` | Variante doutrinária, sem juros TRD na fase pré-judicial |
| `TRAB-FAZENDA` | Devedor Fazenda Pública |
| `TRAB-TITULO` | Título fixa critério próprio — override total, com registro |

### Cível

| ID | Quando |
|---|---|
| `CIVEL-CC-TEMA1368` | Regra geral — **default** |
| `CIVEL-MG-TITULO-CGJ` | Título fixou a tabela da CGJ/TJMG |
| `CIVEL-DANO-MORAL` | Correção do arbitramento (Súmula 362/STJ) |
| `CIVEL-ATO-ILICITO` | Correção do efetivo prejuízo (Súmula 43/STJ); juros do evento danoso se extracontratual (Súmula 54/STJ) |

### Tributário federal

| ID | Quando |
|---|---|
| `TRIB-FED-REPETICAO` | Repetição de indébito |
| `TRIB-FED-DIVIDA-ATIVA` | Empresa como devedora |

### Fluxo da tela

Jurisdição → tipo de ação → qualidade do devedor → preset (default marcado, alternativas visíveis com fundamento) → override por segmento, com justificativa obrigatória quando diverge do default.

---

## Triagem do corpus

### Trabalhista (TRT-3, 2016) — 471 páginas

**Declaração de base:** as páginas 1–45 foram lidas integralmente. A classificação das páginas 46–471 vem do índice, dos títulos de capítulo e de amostragem das aberturas. Tratar como hipótese a confirmar na extração.

| Págs | Conteúdo | Tipo | Destino |
|---|---|---|---|
| 1–8 | Capa, apresentação, índice | — | Descartar |
| 9–17 | Competências, liquidação, estrutura, critérios matemáticos | Prosa | Espinha — núcleo conceitual, pouco defasado |
| 18–82 | Verbas trabalhistas (aviso, 13º, férias, RSR, HE, reflexos) | Prosa + fórmulas | Detalhe — miolo da apuração; confrontar com Reforma 2017 |
| 83–99 | Atualização monetária e juros | Prosa | **Fase 4 obrigatória** — superado |
| 100–106 | Encargos e despesas processuais | Prosa | Fase 4 — honorários sucumbenciais mudaram em 2017 |
| 107–208 | Descontos previdenciário e fiscal | Misto | Bifurcar: conceitos vigentes, faixas superadas |
| 209–277 | Atualização de débitos trabalhistas | Procedimento | Fase 4 |
| 278–298 | Exemplos de cálculos, acordos, atualizações | Fixtures | Usar a **estrutura** dos casos, não os números |
| 299–302 | Contribuição sindical | Prosa | Provavelmente superado (Reforma tornou facultativa) |
| 303–309 | Dívida ativa, precatórios, comandos facilitadores | Prosa | Fase 4 |
| 310–336 | Promoções (modelos de petição) | Templates | Decidir escopo antes de extrair |
| 337–372 | Súmulas, OJs, TJPs | Referência | Índice com verificação de vigência |
| 373–471 | Tabelas | Tabular | Extração determinística → CSV/JSON |

Volume por bloco (caracteres de texto extraído): 21k / 233k / 77k / 336k / 253k / 128k / 138k / 361k.

### Justiça Federal (CJF, 2026) — 93 páginas

Passada única, sem map-reduce — cabe em contexto. Cap. 1 custas, cap. 2 dívida fiscal, cap. 3 dívidas diversas, cap. 4 liquidação de sentença (núcleo), cap. 5 requisições de pagamento. Tabelas de indexadores dentro dos cap. 2 e 4 saem como tabular; o resto como prosa.

---

## Pipeline

**Fase 0 — Contrato de saída.** Fechada. Este documento mais `00-base-normativa.md`.

**Fase 1 — Triagem.** Feita. Tabelas acima.

**Fase 2 — Extração bifurcada por tipo de conteúdo.**
- Normativo tabular → CSV/JSON, validação determinística (contagem de linhas, cobertura de períodos sem lacuna nem sobreposição, checksum contra o original)
- Procedimento e raciocínio → prosa, validação adversarial (Claude extrai, Codex valida contra o original)
- Jurisprudência → índice de referência, não conteúdo embutido
- Modelos de petição → decidir escopo antes de gastar extração

Um bloco por prompt. `/clear` entre blocos.

> **ORDEM CORRIGIDA NO BLOCO 15.** Este documento numerava a consolidação como Fase 3 e o
> confronto normativo como Fase 4. **A ordem real é a inversa, e não é detalhe de rótulo:** o
> confronto tem de vir antes, porque é ele que impede a consolidação de fundir conteúdo
> invertido. Foi executado assim — bloco 14 (confronto) antes do bloco 15 (consolidação). Os
> títulos abaixo estão na ordem de execução.

**Fase 3 — Confronto normativo.** Só trabalhista. Cada regra extraída dos capítulos 7, 8, 9,
10, 12 e 14 é confrontada com `00-base-normativa.md` e recebe um veredito: **vigente**,
**superado**, **bifurcado**, **inaplicável** ou **sem fonte**.

Sem esta fase, a validação adversarial confirma fidelidade ao manual de 2016 e o motor produz
valores errados com aparência de fundamentação.

**Executada no bloco 14.** Resultado em `confronto-normativo/`: 50 vereditos, **32
bifurcados** — nem a Reforma, nem a ADC 58, nem a Res. 225/2025 do TST revogaram com efeito
*ex nunc*.

**Fase 4 — Consolidação em espinha + detalhe.**

A validação adversarial contra o original **não funciona aqui**, porque os erros de consolidação são cruzados: contradição entre capítulos, exceção perdida, regra de precedência invertida. Não existe "original" contra o qual comparar a espinha.

Validação por lista de casos difíceis. Se a espinha não responde às seis abaixo, perdeu
informação essencial.

> **SUPERADO NO BLOCO 15.** Esta lista de seis foi escrita **antes da extração**, e o caso 6
> está errado — a OJ 394 foi revertida pelo Tema Repetitivo 9 em 20/03/2023.
>
> **Substituída por [`03-casos-dificeis.md`](03-casos-dificeis.md): 33 casos em nove grupos**,
> dos quais 27 marcados `[NOVO]` porque **vieram da extração, não da antecipação**. A validação
> do bloco 15 responde aos 33, em `consolidado/00-validacao-casos.md`.
>
> Os seis ficam por registro do que se sabia antes de começar.

1. SELIC e taxa legal englobam correção e juros — fica claro que aplicar CM junto é erro?
2. O título judicial prevalece sobre o manual — sobreviveu à consolidação?
3. Deflação entra no cálculo, mas o valor nominal da parcela não reduz
4. Consolidação em dez/2021 usa IPCA-E 1,17% no geral, INPC 0,84% no previdenciário e TR 0,00% no trabalhista
5. Juros compensatórios em desapropriação passam a estar embutidos na SELIC a partir de dez/2021, sem taxa adicional
6. OJ 394 da SDI-I: reflexo de HE no RSR não repercute em férias, 13º, aviso e FGTS

**Fase 5 — Build das skills.** A estrutura se escreve a partir do conteúdo consolidado, não antes.

**Fase 6 — Aceitação.** Agente novo, sem contexto, lê a skill e implementa. O resultado bate com as fixtures da seção 8 de `00-base-normativa.md`.

---

## Regras de trabalho para os agentes

1. **Nunca inferir norma vigente a partir do manual de 2016.** `00-base-normativa.md` prevalece.
2. **Tabela não vira prosa.** Dado tabular sai como CSV/JSON e é validado por script, não por revisão de LLM.
3. **Extração registra proveniência**: documento, página, item. Sem proveniência, a regra não entra.
4. **Séries de valores mensais não entram.** Só a semântica de aplicação e o contrato com a tabela mantida à parte.
5. **Um bloco por sessão.** Contexto limpo entre blocos.
6. **Divergência não se resolve, se registra.** Onde tribunais divergem, ambas as correntes viram preset com fundamento.
