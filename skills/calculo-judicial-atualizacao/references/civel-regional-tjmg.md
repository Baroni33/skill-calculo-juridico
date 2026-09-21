# Cível — a parte REGIONAL: tabela da CGJ/TJMG

A **única** fonte regional cível catalogada no corpus. Vale para **Minas Gerais** e **só** para
os períodos e hipóteses abaixo.

**Fonte:** `docs/calculo/consolidado/02-atualizacao.md` § 4;
`consolidado/08-nacional-e-regional.md` § 4 (`R10`) e § 6.1; `00-base-normativa.md` § 3.

---

## 1. O que é

**Tabela de correção monetária publicada pela Corregedoria-Geral de Justiça do TJMG**, usada para
o **crédito cível em Minas** nos períodos **anteriores a jan/2003**.

| Classificação | REGIONAL — **TJMG**, item `R10` do catálogo |
|---|---|
| **Ponto de cálculo** | `correcao.tabela` — o índice de correção do crédito cível |
| **Fallback nacional** | **STJ, Tema 1368** (Corte Especial, j. 15/10/2025, REsp 2.199.164/PR e REsp 2.070.882/RS), **vinculante** |

**Juros do mesmo período são NACIONAIS:** **0,5% simples**, CC/1916, arts. 1.062–1.064. A tabela
governa **só a correção**.

> **Ressalva de tipologia — `D8`.** A tabela da CGJ **não é súmula nem tese prevalecente** do art.
> 896, § 6º: é **ato administrativo de corregedoria**. A tipologia NACIONAL × REGIONAL do
> enunciado **não tem casa para ela**. O que falta: uma terceira etiqueta — sugestão,
> `REGIONAL-ADMINISTRATIVO` — ou a decisão de que tabelas de corregedoria são **parâmetro de
> configuração**, não regra. **Mesmo problema atinge a IN 001/02 do TRT-3 e a tabela própria do
> TRT-3 até out/2005.** Não resolvido aqui.

---

## 2. A supersessão pelo Tema 1368 — e por que **não** é apagamento

Até **outubro de 2025** a jurisprudência majoritária do TJMG para o período anterior à Lei
14.905 era **tabela da CGJ mais juros de 1% ao mês**. O **Tema 1368 é vinculante e substitui essa
prática**. O TJMG já publicou o tema no seu portal de precedentes qualificados.

**Mas a tabela sobrevive em TRÊS hipóteses, literais no corpus:**

| # | Hipótese | Fundamento |
|---|---|---|
| 1 | **períodos anteriores a 2003** | é a linha da cadeia; o Tema 1368 diz qual taxa rege o **período pré-Lei 14.905** quanto aos **juros**, e a correção anterior a jan/2003 continua vindo da tabela |
| 2 | processos cujo **título fixou expressamente** aquele critério | **R8** — título > escolha > default |
| 3 | processos com **trânsito em julgado** sob o regime anterior | **R8** |

> **É bifurcação temporal com ressalva de título, NÃO resíduo a descartar.**
> `08-nacional-e-regional.md` § 6.1, "Armadilha 1, confirmada".

**Preset correspondente:** **`CIVEL-MG-TITULO-CGJ`** — *"título fixou a tabela da CGJ/TJMG"*.
Override total, com registro obrigatório (**R8** + **R13**).

---

## 3. A cadeia, com a fronteira

| Período | Correção | Classificação | Juros | Classificação |
|---|---|---|---|---|
| **até dez/2002** | **Tabela CGJ/TJMG** (em MG) | **REGIONAL** | 0,5% simples (CC/1916, arts. 1.062–1.064) | NACIONAL |
| jan/2003 a 29/08/2024 | **SELIC** — engloba ambos | NACIONAL | — | — |
| a partir de 30/08/2024 | **IPCA** (CC art. 389, § único) | NACIONAL | **taxa legal** (CC art. 406, § 1º) | NACIONAL |

**Só a primeira célula é regional.** Todo o resto é `civel-cc-nacional.md`.

**`R1` a partir de jan/2003:** a SELIC engloba. **Somar a tabela da CGJ à SELIC no mesmo intervalo
é erro material**, não escolha de critério.

---

## 4. Fora de Minas

**Não existe no corpus tabela de corregedoria de nenhum outro estado.**

**Afirmação de ausência com escopo declarado:** varredura dos **11 arquivos do consolidado** com
os regex `TJ[A-Z]{2}` e os termos `CGJ`, `Corregedoria`, `tese prevalecente`, `art. 896, § 6` —
**nenhum TJ estadual além do TJMG aparece**; `tese prevalecente` e `art. 896, § 6º` têm **zero
ocorrências em todo o repositório**. `08-nacional-e-regional.md` § 3.

**Consequência operacional, por `R24`:** para uma causa cível fora de MG com competências
anteriores a jan/2003, o ponto `correcao.tabela` fica **sem variante regional cadastrada**, a
conta é marcada **`sem cobertura regional`** e resolve pelo **fallback nacional**. **Não
bloqueia, não erra: registra.** E **silêncio do tribunal não é adesão à tabela mineira** —
aplicar a CGJ/TJMG a uma causa de outro estado seria exatamente o erro que `R24` existe para
impedir.

**Cadastrar outra corregedoria é cadastro, não refatoração:** acrescentar a entrada
`(correcao.tabela, TJ-XX, competência ≤ 2002-12) → tabela própria`. O motor não muda.

---

## 5. Limitações declaradas

1. **A tabela em si não está no repositório.** O corpus a **nomeia** e diz **quando** se aplica;
   **não traz a série de valores mensais**. Isso é dado de categoria **(B)** e pertence ao
   contrato de `skills/indices-judiciais/`. Sem a série, a hipótese 1 da § 2 **não calcula**;

   > **Bloco 25 — a série foi localizada, lida e NÃO migrada.** O PDF da **Contadoria Judicial da
   > Comarca de Belo Horizonte** (*"Fatores de Atualização Monetária Baseados em: ICGJ (TJMG)"*,
   > válido para agosto de 2026) foi lido nas **4 páginas**: **63 linhas-ano, 1964 a 2026, 742
   > fatores mensais de 7 casas**, e **nenhuma célula nomeia índice ou declara corte**. A nota da
   > p. 4 — *"multiplica-se o valor histórico pelo fator correspondente à data de origem"* —
   > classifica o documento como **SÉRIE DE VALORES, categoria (B)**, não como cadeia.
   > **Esta reference continua sendo a REGRA; aquele PDF é o VALOR que ela consome.** Veredito,
   > escopo contado e as três perguntas respondidas em `docs/calculo/pendencias.md` § 28.2.
   > **`ICGJ` fica `indeterminado`** — o PDF não classifica, e herdar a classe dos seis índices do
   > subtítulo é a dedução proibida;

2. **A tipologia não a comporta** — `D8`, § 1 acima. Não resolvido;
3. **A cobertura regional cível é do TJMG e só.** Outras regiões exigem **cadastro**, não
   refatoração;
4. **`R8` é quem sustenta as hipóteses 2 e 3**, e tem **uma exceção registrada** (`R-08-01`,
   NOTA 2): **mudança superveniente de legislação sobre o indexador passa por cima do título**.
   Ou seja: título que fixou a tabela da CGJ **não** congela a cadeia contra alteração legislativa
   posterior do indexador. Registrado, não desenvolvido pelo corpus para este caso concreto.

---

## 6. Ponteiros

- `references/civel-cc-nacional.md` — a cadeia nacional, o Tema 1368 e a taxa legal
- `docs/calculo/consolidado/08-nacional-e-regional.md` § 4 (`R10`) e § 6.1 — a classificação e a
  bifurcação temporal
- `docs/calculo/consolidado/01-dominio-e-invariantes.md` §§ 2.5 (**R8**) e 2.9 (**R24**)
- `references/trabalhista-regional-trt3.md` — a outra região catalogada, e a mesma mecânica
