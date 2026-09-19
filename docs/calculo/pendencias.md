# Pendências

Consolidado em 18/09/2026. Três origens: a seção 9 de `00-base-normativa.md`,
lacunas descobertas na montagem desta base, e observações sobre o código do SaaS.

---

## 1. Pendências normativas (seção 9 da base normativa)

| # | Pendência | Tipo | Bloqueia |
|---|---|---|---|
| N1 | Classificação da Gasmig como Fazenda Pública ou não | Determinação jurídica do cliente | Tamanho do catálogo |
| N2 | Tabela Única do CSJT — contrato de integração | Integração | Motor trabalhista |
| N3 | Efeito da EC 136/2025 na Justiça do Trabalho | Aguarda consolidação TST/CSJT | Ramo FP trabalhista |
| N4 | ADI 7873 | Aguarda julgamento | Estabilidade do ramo FP |

**N1 é a de maior impacto.** Se a Gasmig não for Fazenda Pública, somem do escopo:
o ramo FP das três jurisdições, precatório, EC 113/136 e a consolidação de dez/2021.
Não é pesquisa — é pergunta ao jurídico do cliente, ou leitura de como os juízes vêm
decidindo nos processos existentes.

### Instabilidades registradas, não resolvidas

Divergência não se resolve, se registra (regra 6 do plano):

- **TJ-SP, 2ª Câmara de Direito Público** (AI 3001155-79.2026.8.26.0000) mantém a SELIC
  para débitos não submetidos à fase de precatório, aplicando a EC 136 apenas após a
  expedição do requisitório — contra CJF Res. 990/2026 e STJ REsp 2.236.270/SP.
- **Fazenda Pública estadual e municipal:** a EC 136/2025 menciona apenas "Fazenda
  Pública federal". Requisitórios estaduais e municipais ficam sem a regra antiga
  (revogada) e sem a nova (que não os alcança). Vácuo normativo.
- **Juros TRD na fase pré-judicial trabalhista:** parte da doutrina sustenta
  incompatibilidade com a própria ADC 58, que declarou a TR inconstitucional para
  débitos trabalhistas. Expor como variante (`TRAB-ADC58-SEM-TRD`), não como default.

---

## 2. Taxa legal — ausência de par de validação IPCA-15

**Status: aberta. Afeta a cobertura de teste de `scripts/calculo/valida_taxa_legal.py`.**

A fórmula é a mesma nos dois casos:

```
TL_m = (Fator_Selic_m / Fator_Deflator_{m-1} - 1) × 100
```

O que muda é o deflator:

| Variante | Deflator | Fundamento | Par de validação |
|---|---|---|---|
| Regra geral | IPCA-15 | Res. CMN 5.171/2024 | **nenhum** |
| Previdenciária | INPC | Manual CJF 990/2026, item 4.3.2, Nota 3 | dois, seção 4 |

Os dois pares publicados na seção 4 da base normativa — set/2025 = 1,377047% e
mai/2026 = 0,277807% — vêm da tabela de **taxa legal previdenciária** do Manual CJF,
cuja coluna é `Fator INPC`. São do caso INPC, e estão registrados como tal em
`PARES_VALIDACAO_INPC`.

**Consequência:** a variante IPCA-15, que é a regra geral e a de maior uso, está
implementada mas **sem verificação contra valor publicado**. A aritmética é
compartilhada e está coberta pelos pares INPC; o que falta é a confirmação de que a
série correta alimenta `fator_deflator` na regra geral.

**Como fechar:** o Banco Central divulga mensalmente a taxa legal, o Fator Selic e o
Fator IPCA (seção 4). A Calculadora do Cidadão do BCB tem módulo de taxa legal e serve
como oráculo. Extrair dois meses e acrescentar `PARES_VALIDACAO_IPCA15`.

---

## 3. Truncamento, não arredondamento — decidido, registrar

**Status: fechada, registrada aqui porque a base normativa não a explicitava.**

R12 exige "critério de truncamento definido e consistente por etapa", mas não dizia
qual. Os dois pares de validação resolvem a questão empiricamente:

| Competência | Razão exata | Truncado | Half-up | Manual |
|---|---|---|---|---|
| Set/2025 | 1,3770478004 | **1,377047** ✓ | 1,377048 ✗ | 1,377047 |
| Mai/2026 | 0,2778077572 | **0,277807** ✓ | 0,277808 ✗ | 0,277807 |

Arredondamento half-up erra o último dígito **nos dois casos**. Só truncamento fecha.

Corroborado pelo texto do próprio Manual CJF (`manual_de_calculos_2026.pdf`,
pagina_pdf 53): *"são inerentes ao critério de truncamento de casas decimais aplicado
em cada etapa do cálculo"*.

Implementado como `ROUND_DOWN` em `valida_taxa_legal.py`, com teste negativo que falha
se alguém trocar por half-up.

---

## 4. Observações sobre `CalculosService.cs` no repositório do SaaS

**Status: nota para a Fase 5 (build do motor). SEM AÇÃO AGORA.**

Arquivo: `Plataforma-SaaS-Jus/saas/saas/backend/src/Services/CalculosService.cs`.
Repositório distinto deste; nada foi alterado lá. Registrado para que a portabilidade
do motor não herde os defeitos.

O que há de bom: o backend usa `decimal` em toda parte — **zero ocorrências de `double`
ou `float`** em `src/`. A base para R12 já existe.

Três violações observadas no cálculo de taxa legal (linhas ~127-137):

```csharp
var ipca  = Valor(series, Indice.IPCA,  mesAno) / 100m;
var selic = Valor(series, Indice.SELIC, mesAno) / 100m;
var taxaLegal = Math.Max(0m, selic - ipca);          // (a) e (b)
...
var baseParaJuros = acumulado + jurosAcumulado;
jurosAcumulado = Math.Round(jurosAcumulado + baseParaJuros * taxaLegal, 2);  // (c)
```

| # | Invariante | Observação |
|---|---|---|
| (a) | **R11** | Subtração literal de percentuais. É exatamente o erro que a seção 4 antecipa: ~0,003 p.p./mês, acumulativo. A operação é razão entre fatores. |
| (b) | **R11** | Usa o IPCA do mês corrente. A norma exige o IPCA-15 do mês **anterior** (`m-1`). |
| (c) | **R4** | `baseParaJuros` inclui `jurosAcumulado`, capitalizando. Juros de mora, SELIC e taxa legal são sempre simples. |
| (d) | **R12** | Todo `Math.Round(x, 2)` sem `MidpointRounding`. O default do .NET é *banker's rounding*; a norma exige truncamento. |

Também ausente: a distinção IPCA-E / IPCA (a enum tem ambos, mas a cadeia não bifurca
por fase), e o marco inicial dos juros trabalhistas usa `DataCitacao` — R7 exige
**ajuizamento** no trabalhista.

**Recomendação para a Fase 5:** o motor nasce em `src/Domain/Calculo/`, ao lado de
`Domain/Pareceres/` e `Domain/Sla/`, não evolui de `CalculosService`. O serviço atual
é POC e está acoplado a repositório e EF.

---

## 5. Versionamento de séries de referência — ausente no SaaS

**Status: aberta. Bloqueia R13.**

`IndicesSyncService` faz upsert destrutivo sobre `IndicesMonetarios`:

```csharp
if (existente != null) { existente.Valor = valor; }
```

Sem histórico, sem versão, sem data de coleta. R13 exige que toda conta grave a
**versão das séries consumidas**. Hoje, uma série revisada pelo órgão emissor altera
silenciosamente cálculos já emitidos — e uma conta não pode ser reproduzida.

O contrato definido em `skills/indices-judiciais/` precisa suportar leitura por versão,
não só por competência. O backend também não tem migrations EF (só `db/Dockerfile`);
o schema vem de seed.

---

## 6. Fixture 2 — dígito final do método detalhado

**Status: verificação pendente, baixo risco.**

Em `fixture-02-fazenda-publica-jun2026.json`, o total pelo método detalhado consta como
R$ 5.218,27. A camada de texto do PDF trunca o valor em `R$ 5.218,2` (pagina_pdf 52).
O dígito foi derivado por aritmética: 3.412,64 + 1.805,63 = 5.218,27, consistente com a
divergência de R$ 0,01 que o manual declara na pagina_pdf 53.

Confirmar visualmente antes de tratar como transcrição literal. O valor esperado da
fixture (R$ 5.218,28, método resumido) não depende disso.

---

## 7. Schema das tabelas normativas — duas famílias, um diretório

**Status: aberta. Bloqueia a Fase 3.**

O schema canônico de `01-plano-extracao.md` descreve cadeia período → indexador, com
`segmentos`, `engloba` e `aplicacao`. O bloco 1 produziu seis tabelas de outra natureza
— matriz de incidência, estrutura de faixa, enquadramento por atividade, critério de
contagem — que não têm linha do tempo de indexador e que `valida_cobertura.py` não
alcança.

Foram gravadas com shape próprio, marcado `categoria: "A-semantica"`, **sem forçar o
schema canônico**. Duas saídas aparentes: um campo `tipo` discriminando as famílias
dentro do mesmo schema, ou dois diretórios. Decidir antes que a Fase 5 leia daqui.

Detalhe em `tabelas-normativas/README.md`.

---

## 8. Calendários do Manual TRT-3 são defeituosos

**Status: fechada como constatação; abre trabalho na Fase 4.**

O item 18.14 (p. 460–466) imprime treze meses com menos dias do que têm. Conferido na
imagem da página, não só na camada de texto:

- **Setembro de 2009**: a célula de sábado da primeira semana traz **7** onde deveria
  estar **5**; o dia 5 não aparece em lugar nenhum.
- **Março de 2017**: a coluna inteira de segunda-feira está vazia — faltam 6, 13, 20 e
  27 — e os demais dias aparecem deslocados uma coluna à direita.

Outros onze meses perdem um ou dois dias. A extração é fiel ao impresso: `dia_da_semana`
reproduz a coluna do original e por isso diverge do calendário real em 42 dias.

**Consequência:** o calendário do manual não serve para contar dias úteis nem feriados.
As contagens de RSR do item 18.13 dependem de calendário e de feriados; confrontá-las
com um calendário independente é trabalho da Fase 4. Até lá, não derivar dias úteis de
`serie-18.14-calendarios.csv`.

---

## 9. Método de conversão da URV

**Status: parcialmente fechada no bloco 2. Resta o arredondamento.**

O item 18.10 (p. 453–455) traz as cotações diárias da URV em CR$ e nada mais. O método
**não estava no capítulo de critérios matemáticos** (p. 9–17), como se supunha, mas no
item 6.1, página 18:

> "os salários dos recibos de março/94 a junho/94 estão expressos em URV, sendo necessária,
> para o cálculo, a conversão para cruzeiros reais, multiplicando-se a expressão em URV
> pelo valor nominal da URV **do dia do pagamento**."

```
valor_em_CR$ = valor_em_URV × URV(dia_do_pagamento)
```

**Fechado:** direção da operação e data-base.
**Aberto:** critério de arredondamento, que o manual não declara.

Não confundir com a conversão inversa, CR$ → URV, de março/1994 (MP 434/94 e Lei 8880/94),
que se faz por divisão e média aritmética de quatro meses (p. 81).

Detalhe em `extracao/trabalhista/bloco-02-criterios.md`, § 7.
Registrado em `tabelas-normativas/trt3-18.10-urv-conversao.json`.

---

## 9-A. Critério de arredondamento: as duas fontes primárias divergem

**Status: aberta. Bloqueia o núcleo aritmético de `calculo-judicial-core`.**

O § 3 acima fixou truncamento a partir do Manual CJF, e isso continua certo **para a taxa
legal**. O bloco 2 mostrou que o problema é maior: o Manual TRT-3 **arredonda**.

| Operação (TRT-3, item 5.3, p. 17) | Exato | Publicado | Truncado |
|---|---|---|---|
| 25 / 60 | 0,41666… | **0,42** | 0,41 |
| 10 / 60 | 0,16666… | **0,17** | 0,16 |
| 5 × 4,285714 | 21,428570 | **21,43** | 21,42 |
| 180,00 × 4,285714 | 771,428520 | **771,43** | 771,42 |

Quatro exemplos, nenhum compatível com truncamento. Não é acidente de um caso.

R12 exige "critério de truncamento definido e consistente por etapa". **Um critério global
único contraria uma das duas fontes.** Decidir se o critério é atributo da jurisdição, do
tipo de operação, ou de ambos — antes de escrever o núcleo aritmético.

Detalhe em `extracao/trabalhista/bloco-02-relatorio.md`, § 4.

---

## 9-B. Regra do índice negativo é ambígua

**Status: aberta. Interage com R5.**

Manual TRT-3, item 5.3, p. 16:

> "Se houver um Índice com sinal negativo em algum mês, basta dividir o total acumulado até
> o referido mês pelo número índice que apresentou a variação negativa."

A regra só produz redução se o número índice for construído com o **valor absoluto** do
percentual (−0,23% → 1,0023, e dividir). Construído pela fórmula geral do próprio manual
(`i = p/100 + 1`, −0,23% → 0,9977), **dividir aumentaria** o acumulado.

O manual não diz qual construção usar e **não traz exemplo numérico com índice negativo**.
Sem oráculo. Não foi inferido.

---

## 10. Escopo não decidido

- **Modelos de petição** (págs. 310–336 do manual trabalhista): decidir escopo antes de
  gastar extração (Fase 2). Podem ficar inteiramente fora.
- **Encargos processuais**: provisoriamente em `calculo-trabalhista-liquidacao`, mas as
  faixas de honorários são do CPC art. 85, § 3º, não da CLT, e valem nos três ramos.
  Provável separação na Fase 5.
- **Triagem das págs. 46–471 do manual trabalhista**: as págs. 1–45 foram lidas
  integralmente; o restante vem do índice e de amostragem das aberturas. Tratar como
  hipótese a confirmar na extração. As fronteiras de 83 e 373 foram verificadas e
  conferem. **As págs. 373–471 foram confirmadas na extração do bloco 1**, com quatro
  desvios de paginação em relação ao índice do escopo — ver
  `extracao/trabalhista/bloco-01-tabelas.md`, seção 2.
- **Dois quadros sem numeração 18.x** foram encontrados e extraídos em arquivos próprios:
  MOEDAS/PARIDADES (p. 381) e alíquotas por código FPAS, Anexo I da IN/RFB 1238/2012
  (p. 449). Decidir se entram no escopo do módulo.
