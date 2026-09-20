<!-- ARQUIVO GERADO. NÃO EDITE À MÃO: será sobrescrito. -->
<!-- Regenere com: python scripts/calculo/gera_numeros.py -->

# Números do repositório — **gerado por script**

> **Este arquivo é gerado a partir do estado real, não digitado.**
>
> ```
> python scripts/calculo/gera_numeros.py
> ```
>
> Toda contagem abaixo sai de **contar o repositório** ou de **executar o
> validador**. Nenhuma é transcrita de outro arquivo.
>
> **Este é o único lugar do repositório onde número de RESULTADO é
> publicado.** Os demais arquivos apontam para cá. Número de **conteúdo
> normativo** — 42,72% em jan./1989, 0,5% a.m., `pagina_pdf` 42 — não é
> resultado, é o dado, e continua onde sempre esteve. Número em
> **relatório de bloco** é registro datado e **não** se atualiza: um
> relatório que se atualiza sozinho deixa de ser registro.
>
> **Sem timestamp automático**, de propósito: data gerada produziria diff
> a cada rodada e o ruído esconderia a mudança real. Se precisar de data,
> passe `--data AAAA-MM-DD`.

---

## 1. Cadeias temporais

Contado dos `.json` de `docs/calculo/tabelas-normativas/` com
`tipo == "cadeia-temporal"` — **pelo campo, nunca pelo nome do arquivo**.

| cadeias | **20** |
|---|---|
| segmentos | **156** |
| rótulos de indexador **nomeados**, distintos | **35** |
| segmentos sem rótulo utilizável | **37** |
| rótulos **na convenção do catálogo** | **36** |

Segmento sem rótulo utilizável é `taxa` pura, `padrao-monetario`, ou o
único com `indexador: null` — `taxa` e moeda não têm índice a classificar,
e `null` é o dado dizendo isso, não um rótulo que alguém escreveu.

**As duas últimas linhas não se contradizem, e a diferença é declarada:**
`indexadores-tipo-catalogo.json` conta `(segmento sem indexador)` **como um
rótulo** da classe `nao-indexador`, porque para ele a pergunta é *"que
classe de R3 se aplica?"* e *"nenhuma"* é resposta. A primeira linha conta
só o que tem **nome**. A convenção do catálogo é a que a `§ 25.4` de
`../pendencias.md` usa; mantida aqui para não criar um terceiro número.

### 1.1 Segmentos por cadeia

Publicado por cadeia porque as `references/` descrevem cadeias uma a uma:
é contra esta tabela que se confere cada menção.

| cadeia (`id`) | componente | segmentos |
|---|---|---|
| `cjf.condenatorias-gerais.correcao-monetaria` | correcao-monetaria | 15 |
| `cjf.condenatorias-gerais.juros-mora` | juros-mora | 11 |
| `cjf.desapropriacao-direta.correcao-monetaria` | correcao-monetaria | 11 |
| `cjf.desapropriacao-direta.juros-compensatorios` | juros-compensatorios | 3 |
| `cjf.desapropriacao-indireta.correcao-monetaria` | correcao-monetaria | 11 |
| `cjf.desapropriacao-indireta.juros-compensatorios` | juros-compensatorios | 3 |
| `cjf.divida-fiscal.correcao-monetaria` | correcao-monetaria | 5 |
| `cjf.divida-fiscal.juros-mora` | juros-mora | 8 |
| `cjf.fgts-divida-fiscal.correcao-monetaria` | correcao-monetaria | 5 |
| `cjf.fgts.correcao-monetaria` | correcao-monetaria | 11 |
| `cjf.fgts.juros-mora` | juros-mora | 3 |
| `cjf.poupanca.correcao-monetaria` | correcao-monetaria | 12 |
| `cjf.poupanca.juros-mora` | juros-mora | 3 |
| `cjf.previdenciario.correcao-monetaria` | correcao-monetaria | 15 |
| `cjf.repeticao-indebito.correcao-monetaria` | correcao-monetaria | 10 |
| `cjf.trabalhista.juros-mora` | juros-mora | 11 |
| `trab.hist.correcao-monetaria` | correcao-monetaria | 3 |
| `trab.hist.fazenda-publica.juros-mora` | juros-mora | 5 |
| `trab.hist.juros-mora` | juros-mora | 3 |
| `trab.hist.moedas-e-paridades` | padrao-monetario | 8 |

## 2. Distribuição de `tipo_indexador`

Sobre os segmentos das cadeias acima. `indeterminado` **bloqueia R3** — não
é neutro nem é aprovação.

| `tipo_indexador` | segmentos |
|---|---|
| `nao-indexador` | 46 |
| `percentual` | 39 |
| `indeterminado` | 32 |
| `nominal` | 31 |
| `janela-deslocada` | 8 |
| **total** | **156** |

## 3. Invariantes R1 · R2 · R3

**Executando** `valida_cadeias.py --sem-atualizar-manifesto`. Gerar
relatório não pode alterar o dado que o relatório descreve.

| | violações |
|---|---|
| **R1** — englobamento concorrente | **21** |
| **R2** — lacuna de cobertura do componente próprio | **1** |
| **R3** — virada de tipo sem ajuste de defasagem | **63** |

**Composição de R3**, contada das linhas de violação:

| | violações | o que significa |
|---|---|---|
| `[R3]` — **confirmada** | **23** | as duas pontas têm tipo em fonte, e a virada não declara ajuste |
| `[R3-INDETERMINADO]` | **40** | uma das pontas não tem tipo em fonte — **R3 não pôde ser verificada**; é pendência, não aprovação |
| **soma** | **63** | confere com o fecho do validador |

> **Toda violação acima é do MANUAL, transcrita como está.** Nenhuma foi
> harmonizada. A leitura de cada uma está nos relatórios dos blocos 8 e 9.

## 4. `valida_bloco_tabelas.py`

**Executando.** Divergência é resultado esperado do trabalho — é defeito
do original, registrado e não consertado. **Só `erros` é defeito nosso**,
e só `erros` faz o validador sair não-zero.

| | |
|---|---|
| ok | **15** |
| divergências (do original) | **31** |
| não verificados mecanicamente | **1** |
| **erros (da extração)** | **0** |

## 5. Testes

Duas contagens, e elas respondem coisas diferentes: `def test_` é o que
**está escrito**; `Ran N` é o que **rodou**. Divergirem é sinal — teste
não coletado, arquivo fora do padrão de descoberta, erro de importação.

| arquivo | `def test_` |
|---|---|
| `scripts/calculo/test_aceite_nivel1.py` | 20 |
| `scripts/calculo/test_classes_de_indice.py` | 12 |
| `scripts/calculo/test_metodos.py` | 32 |
| `scripts/calculo/test_numeros.py` | 18 |
| `scripts/calculo/test_ponteiros.py` | 7 |
| `scripts/calculo/test_valida_bloco_tabelas.py` | 10 |
| `scripts/calculo/test_valida_cobertura.py` | 121 |
| `scripts/calculo/test_valida_parametros.py` | 71 |
| `scripts/calculo/test_valida_regimes.py` | 86 |
| `scripts/calculo/test_valida_taxa_legal.py` | 29 |
| **total escrito** | **406** |

**Executados:** `python -m unittest discover -s scripts/calculo -p "test_*.py"` → **406 testes, OK**.

## 6. Arquivos

| o que se conta | quantos |
|---|---|
| `docs/calculo/consolidado/` — arquivos `.md` | **15** |
| `skills/` — arquivos `.md`, em toda a árvore | **32** |
| `skills/*/SKILL.md` — skills publicadas | **4** |
| `skills/*/references/*.md` | **23** |
| `docs/calculo/tabelas-normativas/*.json` — todos | **32** |

## 7. Linhas das `SKILL.md` — o limite de 500 é verificável

O limite existe para que a skill caiba na leitura de entrada; declará-lo
sem medi-lo seria promessa. Aqui ele é **medido**, e
`test_numeros.py` faz dele **teste**.

| `SKILL.md` | linhas | limite 500 |
|---|---|---|
| `skills/calculo-judicial-atualizacao/SKILL.md` | 499 | cabe, folga de 1 |
| `skills/calculo-judicial-core/SKILL.md` | 499 | cabe, folga de 1 |
| `skills/calculo-trabalhista-liquidacao/SKILL.md` | 499 | cabe, folga de 1 |
| `skills/indices-judiciais/SKILL.md` | 497 | cabe, folga de 3 |

## 8. O que este arquivo NÃO conta, e por quê

**Pendências abertas, por família.** `docs/calculo/pendencias.md` **não é**
**contável por script com confiança**, e o motivo não é preguiça de regex:

- a numeração das seções é heterogênea — há `9-A` e `9-B`, não há `10`, e a
  `14` vem depois da `16`. Ordem de seção não é ordem de pendência;
- *aberta* e *fechada* aparecem ora em prosa, ora em linha de tabela, ora
  no título da subseção (`### 20.1 FECHADAS pelo bloco 12`) — e uma mesma
  seção mistura as duas coisas;
- sub-pendência é tanto `### 15.1` quanto linha de tabela sem título
  próprio. Não há unidade contável estável.

Qualquer regex produziria um número com **aparência de exatidão e sem**
**lastro** — e número inventado é pior que número ausente, porque o
primeiro é usado. **Enquanto a pendência não tiver campo, a contagem fica
fora daqui.** Para saber o que está aberto, leia `../pendencias.md`.

> O caminho para tornar isso contável já está proposto na `§ 26.1` de
> `../pendencias.md`: **campo, não prosa**. Quando existir, esta seção vira
> tabela.

