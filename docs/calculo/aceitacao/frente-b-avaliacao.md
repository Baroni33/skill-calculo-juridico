# Frente B — avaliação do teste de aceitação das skills

**Objeto avaliado: as quatro `skills/`.** O código da Frente A é o instrumento de medida, não o
entregável.

## Declaração de sequência

Segui a ordem obrigatória do enunciado: **(1)** li as quatro `SKILL.md`, os `references/` de
`calculo-judicial-atualizacao` e `indices-judiciais`, e as quatro fixtures; **(2)** li e **rodei**
`frente-a/runner.py` (Python 3.11); **(3)** escrevi as §§ 1 a 5 abaixo, **inclusive a minha
própria lista de lacunas (§ 3.1)**, sem abrir `registro-de-lacunas.md`; **(4) só então** abri o
registro e escrevi a § 6. As §§ 1–5 **não foram alteradas** depois disso.

Usei, para julgar omissão, material que a Frente A não podia ver: `docs/calculo/consolidado/`,
`docs/calculo/extracao/`, `tabelas-normativas/*.json`, `pendencias.md` e `presets-regime.md`.

---

## 1 — As quatro fixtures batem?

**Nenhuma. Placar: 0 bateram · 0 divergiram · 4 BLOQUEADAS por dado ausente.** Saída do runner: 2.

| Fixture | Status | Ponto exato de parada |
|---|---|---|
| 01 — FP jun/2022 | BLOQUEADA | `SerieAusente: IPCA-E/IBGE de 2020-01` |
| 02 — FP jun/2026 | BLOQUEADA | `SerieAusente: IPCA-E/IBGE de 2020-01` |
| 03 — não-FP jun/2026 | BLOQUEADA | `SerieAusente: IPCA-E/IBGE de 2002-01` |
| 04 — precatório | BLOQUEADA | `SerieAusente: INPC de 2016-01` |

**Não há número a comparar contra `esperado` em fixture nenhuma.** A comparação número a número
pedida pelo critério 1 é, neste estado, vazia.

### As divergências-asserção (fixtures 2 e 4)

**A Frente A não as zerou — mas também não as produziu.** O motor não implementa "método
resumido" nem "detalhado"; produziria **um só número**. A divergência de R$ 0,01 e de R$ 0,03 é,
por construção, inatingível.

**E isto não é falha do implementador: é falha da skill.** Varri `skills/` (**4 `SKILL.md` + 19
arquivos em `references/`**) e `docs/calculo/consolidado/` (**11 arquivos**) pelos termos
`resumido` e `método detalhado`: **as skills citam os dois métodos quatro vezes — sempre pelo
resultado, nunca pelo procedimento**; nenhum texto do repositório define o que cada um faz. A
única pista procedimental está na `observacao` da **fixture 4** (*"o resumido não aplica juros
sobre juros"*) — e pista em fixture não é skill.

> **Consequência para o critério de reprovação:** o teste "reprovar quem zera a divergência" não
> pôde sequer ser executado, porque as skills não entregam o par de métodos que a divergência
> pressupõe. **A asserção mais valiosa do conjunto de fixtures é inalcançável a partir das skills.**

**Defeito colateral no runner (registro, não crítica ao motor):** `Resultado.comparar` usa
`tolerancia.valor` como **banda de aceitação de um único número**. Um motor convergente (delta
0,00) passaria. `divergencia_e_assercao: true` é **impresso**, não **asserido**. Ver § 5.4: a
redação do core induz exatamente esse desenho.

**Verificação circular declarada da fixture 3:** a Frente A confere a **montagem** consumindo os
coeficientes e percentuais que a própria fixture publica (`1,4590697197`, `209,65%`). Fecha exato
nos seis números — e **declara a circularidade** no código e na tela. **Não conta como fixture
reproduzida**, e ela mesma o escreve.

---

## 2 — Os invariantes

Três estados distintos, conforme o enunciado pede distinguir.

| ID | Estado | Evidência |
|---|---|---|
| **R1** — cumulação englobante × juros | **IMPLEMENTADO E EXERCITADO** | `cadeias.compor` impõe a supressão **na composição** (não detecta no resultado), citando a NOTA 2 do item 4.2.1. Rodado mês a mês sobre `cjf.condenatorias-gerais.*` de 1964-01 a 2026-06, **nos dois ramos**: zero cumulações. `checar_englobamento` cobre o caso genérico |
| **R2** — cobertura | **IMPLEMENTADO** | acusa exatamente as duas sobreposições **do original** (1989-01 OTN×IPC/IBGE; 1990-03 BTN×IPC/IBGE) e as rotula como do original. Confere com `civel-federal.md` §§ 1 e 11.3 (`R-08-04` salva jan/1989; `D8-C21` deixa mar/1990 em aberto). Implementa `dominio_condicoes` como R2 manda — exaustividade declarada, não presumida |
| **R3** — virada entre classes + defasagem | **NÃO IMPLEMENTADO, por recusa declarada** | `motor.coeficiente_de_correcao` documenta: *"a defasagem vive na CADEIA... Este motor nao desloca sozinho porque o corpus nao declara o eixo do par 13"*. Nenhum código lê `tipo_indexador`; nenhum bloqueio `R3-INDETERMINADO`. **Ausência, não erro** — e ver § "o que a skill disse e estava errado", porque aqui a skill dá instrução contraditória |
| **R4** — juros simples | **IMPLEMENTADO** | `acumular_simples` soma percentuais (Súmula 121/STF); `juros_simples` é `base × taxa` |
| **R4-EXCEÇÃO** — compostos 27/02/1987–03/03/1991 | **MECÂNICA SIM, FRONTEIRA NÃO** | `acumular_composto` traz a mecânica literal do DL 2.322/87 e registra a granularidade divergente TRT-3 (dia) × CJF (mês). **Mas nenhum chamador**: nada decide *quando* a exceção vale. Função morta no grafo |
| **R5** — piso nominal por parcela | **IMPLEMENTADO CORRETAMENTE** | `piso_nominal_parcela` é chamada de **dentro de `corrigir`** — logo **por parcela**, nunca sobre o total. Recusa a instrução defeituosa de "dividir pelo índice negativo" |
| **R6** — piso zero | **IMPLEMENTADO** | dentro de `taxa_legal` |
| **R11** — taxa legal por razão | **IMPLEMENTADO E VERIFICADO** — é o ponto mais forte do motor | `taxa_legal` = `(Fs/Fd − 1) × 100`, truncado em 6. Bate nos **dois pares publicados**: set/2025 → `1.377047`; mai/2026 → `0.277807`. E o runner **verifica ativamente que a subtração literal diverge** (`1.374156` e `0.280058`) — o motor não só acerta, como demonstra o erro que a skill antecipa |
| **R12** — `Decimal`, nenhum `float` | **IMPLEMENTADO E CONFERIDO** | varri os 5 `.py` por AST à procura de literal `float`: **zero ocorrências**. `D()` **levanta `TypeError` se receber float**. As cinco cadeias de arredondamento estão todas lá, e o **NMP de três ramos está correto**: `NMP(12.450) = 12.4` contra `ROUND_HALF_UP = 12.5` — a faixa exata em que a skill diz que difere. `1/30` como `Decimal(1)/Decimal(30)` |
| **R23** — descarregar antes de juros | **PRIMITIVA IMPLEMENTADA, NÃO ALCANÇADA** | `motor.descarregar` existe e está correto; **nenhum caminho de fixture a chama** — nenhuma chega à fase de juros. Não dá para julgar seu **posicionamento na ordem** |
| **R10 / `pr.imputacao`** | **RECUSA IMPLEMENTADA E TESTADA** | sem preset, `ErroDeDados`; o autoteste **exige** a recusa. Correto por `R20-EXCEÇÃO` — mas ver § 6.5, item 1 |
| **R13** | **PARCIAL, com o bloqueio nomeado** | `Registro` grava preset, overrides e versão normativa, e grava literalmente que `versao_series` **não existe**, citando `indices-judiciais` Lim. 3 |

**Resumo dos sete que o enunciado manda checar:** **4 implementados e exercitados** (R1, R5, R11,
R12), **1 implementado mas não alcançado** (R23), **1 meio-implementado** (R4 sim; R4-EXCEÇÃO com
mecânica e sem fronteira) e **1 não implementado por recusa declarada** (R3). **Nenhum está
implementado errado.**

---

## 3 — O implementador precisou de informação que a skill não deu?

### 3.1 Minha lista independente — 13 itens

Escrita antes de abrir o registro da Frente A. Para cada item julgo a natureza: **(D)** declarada
na skill; **(ND)** não declarada; **(PA)** a skill diz, mas em lugar que o ponteiro não alcança.

| # | O que falta | Natureza | Bloqueia? |
|---|---|---|---|
| **L1** | **A camada (B) inteira** — IPCA-E 2001–2021, SELIC 2022–2026, IPCA-15, INPC 2016–2020, TR | **(D)**, mas **negada** pela seção "Fixtures de aceite" das mesmas skills | **as 4** |
| **L2** | **O procedimento do "método resumido" e do "método detalhado"** | **(ND)** — 0 definições em 4 `SKILL.md` + 19 `references/` + 11 arquivos do consolidado | **as fixtures 2 e 4, como asserção** |
| **L3** | **O que "mensalizada" significa aritmeticamente** (70% da Selic a.a.) — ÷12? raiz 12ª? | **(ND)** — `mensaliz` não ocorre em `pendencias.md` | **1, 2 e 4** |
| **L4** | **A série da Selic ANUAL** (para o teste `> 8,5%`), distinta da mensal | **(ND)** | 1, 2, 4 |
| **L5** | **Ordem interna da consolidação de dez/2021** — sobre que base incidem os 0,4412%; se o 1,17% entra antes | **(ND)** — a NOTA 5 dá os ingredientes, não a sequência | 1 e 2 |
| **L6** | **A RETOMADA da correção ao fim do englobamento.** A NOTA 2 diz que o IPCA-E *"deixa de ser aplicado a partir da incidência da Selic"*; **nada diz que volta** quando a SELIC sai (set/2024, não-FP) | **(ND)** — e é indispensável para o coeficiente `1,4590697197` da fixture 3 | 3 |
| **L7** | **Precisão interna.** "Precisão plena encadeada" sem número de dígitos | **(ND)** | todas |
| **L8** | **Granularidade do truncamento do fator** — por mês ou só no acumulado? E **6 casas contra os 10 decimais publicados** no `coeficiente_correcao` da fixture 3 | **(ND)**, e é contradição entre skill e fixture | todas |
| **L9** | **Honorários incidem sobre principal e juros separadamente** | **(PA)** — só na `observacao` da fixture 4; nenhuma skill diz | 4 |
| **L10** | **Quando a imputação NÃO se consulta.** Na fixture 4 o pagamento já vem discriminado (principal 21.000 / juros 3.150) — não há o que imputar. A skill trata `pr.imputacao` como bloqueio incondicional | **(ND)** — risco de bloqueio indevido | 4 |
| **L11** | **Como se monta a coluna "% de juros" acumulado** quando a cadeia troca de regime (SELIC → taxa legal): fixture 3 publica `209,65%` para uma parcela | **(ND)** | 3 |
| **L12** | **"Percentual devido"** como regra de juros nas fases 1 e 3 do precatório | **(ND)** — expressão não definida | 4 |
| **L13** | **Versão das séries (R13)** | **(D)** — `indices-judiciais`, Limitações 3 | R13, não o número |

**Contagem: 13. Declaradas: 2. Parcialmente alcançáveis: 1. NÃO declaradas: 10.**

### 3.2 A pior categoria — "diz, mas o ponteiro não alcança"

Um caso puro (**L9**) e um caso **agravado, pior que silêncio**: a skill **diz duas coisas
incompatíveis em dois arquivos** (classificação de IPCA-E/IPCA-15 — § 5.1). Quem consultar o
ponteiro correto — `calculo-judicial-core`, que a própria skill declara obrigatória e prévia —
recebe a instrução **errada com aparência de invariante**.

---

## 4 — As limitações declaradas correspondem ao que bloqueou?

**Parcialmente, e o desencontro é o resultado do teste.**

### O que as skills declararam e de fato bloqueou

**Quatro limitações declaradas correspondem ao vivido, e uma não foi alcançada.** Bloquearam de
fato: `indices-judiciais` Lim. 4 (*"séries correntes de INPC, IPCA, IPCA-E, IPCA-15"* são **dado
externo a integrar**) e `civel-federal.md` § 11.8 (*"As séries não estão aqui"*) — **é o bloqueio
único e total**; `indices-judiciais` Lim. 3 (versionamento ausente, **bloqueia R13**), que o motor
registra literalmente; e `pr.imputacao` sem default, que o motor recusou. **Não alcançada:** a
Tabela Única do CSJT (`P9-02`) — as quatro fixtures são federais, não trabalhistas.

### O que bloqueou e NÃO estava declarado — é aqui que está o defeito

1. **O procedimento dos dois métodos (L2).** Nenhuma das quatro seções `## Limitações declaradas`
   o menciona. Ao contrário: as skills **exigem** a divergência entre eles como critério de
   aprovação (*"Um motor que zera essas diferenças está arredondando errado"*) sem entregar o
   procedimento que a produz. **Não declarada, e a mais cara do conjunto.**
2. **"Mensalizada" sem fórmula (L3).** Não está em `pendencias.md` nem em nenhuma seção de
   limitações. **O projeto conhecia o problema** — a expressão ocorre literal em **4 JSON de
   cadeia e 3 `references/`, sempre sem definição** — e **nenhuma skill passou adiante**. É a
   espécie que o enunciado chama de pior.
3. **A retomada da correção após o englobamento (L6)**; **a precisão interna e a granularidade do
   truncamento (L7, L8).**

### A contradição estrutural, e é o achado central do critério 4

`skills/indices-judiciais/SKILL.md` declara, corretamente, que **a série não existe no
repositório**. As **quatro** skills, porém, trazem uma seção `## Fixtures de aceite` apresentando
as quatro fixtures como critério de aceite operacional, e `tests/fixtures/calculo/README.md`
afirma: *"um agente novo lê a skill, implementa, e o resultado bate aqui"*.

**As duas afirmações não podem ser verdadeiras ao mesmo tempo.** Conferi no material que a Frente A
não podia ver: os **21 CSV** de `docs/calculo/extracao/trabalhista/` abrem com
`# OUT_OF_SCOPE — série de valores, não entra na skill`, e **nenhum** contém IPCA-E, IPCA-15 ou
INPC mensal do período das fixtures. Os quatro totais (`3.484,95`, `5.218,28`, `5.772,95`,
`4.435,07`) ocorrem em **um só arquivo do repositório inteiro** — `00-base-normativa.md` § 8 — e
**sempre como resultado transcrito, nunca com os operandos**.

> **Conclusão do critério 4: as quatro fixtures não são reproduzíveis por implementador algum,
> com skill ou sem skill, com o repositório no estado em que está.** O bloqueio da Frente A não
> mede a competência do implementador; mede a integridade do conjunto de aceite.

---

## 5 — Pendência tratada como REGRA por omissão da skill

**Sim, e há um caso grave.**

### 5.1 O caso grave — R3 e a classificação de IPCA-E / IPCA-15

`skills/calculo-judicial-core/SKILL.md`, § R3, afirma:

> *"Só estes sete estão classificados em fonte (item 4.1.2.4, `pagina_pdf` 42), mais o IPC/IBGE
> por D8-C21. **Dez indexadores em uso são `indeterminado` — entre eles IPCA-E, IPCA-15**, IPC-R,
> IRSM e a TR. Não os presuma percentuais por semelhança de nome; o validador bloqueia a virada
> sob `R3-INDETERMINADO`."*

`skills/calculo-judicial-atualizacao/references/civel-federal.md` § 10 repete:

> *"Mas **IPCA-E e IPCA-15 são `indeterminado`**: nenhuma fonte os classifica... (`P17-01`)"*

**A fonte não sustenta.** `tabelas-normativas/indexadores-tipo-catalogo.json` — que a própria
`indices-judiciais` declara ser *"o que o validador lê"* — grava `IPCA-E/IBGE ->
janela-deslocada` e `IPCA-15/IBGE -> janela-deslocada`, e `MAPEAMENTO_BLOCO_19.totais` grava
`indeterminado: 17`, **não dez**. E `skills/indices-judiciais/SKILL.md` o diz com todas as
letras: *"`IPCA-E` e `IPCA-15` saíram de `P17-01` no bloco 19 e são `janela-deslocada`"*.

**As duas citações, lado a lado:**

| Skill | Fonte (`indexadores-tipo-catalogo.json` + `indices-judiciais/SKILL.md`) |
|---|---|
| *"Dez indexadores em uso são `indeterminado` — entre eles IPCA-E, IPCA-15"* (core, R3) | `IPCA-E/IBGE -> janela-deslocada`; `IPCA-15/IBGE -> janela-deslocada`; `indeterminado: 17` |
| tabela R3 do core e da atualização: **duas classes** (nominal × percentual) | *"**Três classes** desde o bloco 19"*; *"Três classes com defasagem = TRÊS pares de virada"* |

**Efeito operacional, e cai exatamente em cima das fixtures 1, 2 e 3:** um motor construído sobre
`calculo-judicial-core` — que a própria skill declara **obrigatória e anterior às outras três** —
classifica IPCA-E como `indeterminado` e **bloqueia sob `R3-INDETERMINADO`** a virada
IPCA-E → SELIC de dez/2021 e IPCA-E → IPCA-15 de set/2025. Um motor construído sobre
`indices-judiciais` aplica `janela-deslocada` e segue. **Duas skills do mesmo pacote dão
instruções mutuamente excludentes para o mesmo mês da mesma fixture.**

**Classificação:** é ao mesmo tempo **regra errada** (a mais grave das categorias do enunciado) e
**pendência fechada apresentada como aberta** — o inverso do defeito procurado, e igualmente
tóxico: `P17-01` foi **fechado** no bloco 19 para esses dois rótulos, e duas skills seguem
tratando-o como aberto.

### 5.2 Pendência apresentada como regra

| Item | Grau |
|---|---|
| **Honorários 10% sobre principal e juros separadamente** — só na `observacao` da fixture 4 | chega ao implementador como fato, **sem fonte normativa em skill alguma** |
| **"Percentual devido"** como regra de juros (fixture 4, fases 1 e 3) | expressão não definida, apresentada como se fosse critério |
| `pr.adc58-item-i` default i.1 · `pr.imputacao` sem default · os dois bloqueios aritméticos (A2, A3) | **todos corretamente marcados** como pendência ou default declarado. **Não** viraram regra |

### 5.3 Afirmações operacionais que conferi contra a fonte — e que SE SUSTENTAM

Para não atribuir defeito por amostragem enviesada: **R4-EXCEÇÃO** (→
`cjf.trabalhista.juros-mora.json`: `"capitalizacao": "composta"`, `"fundamento": "Art. 3º do
Decreto-Lei n. 2.322/1987"`); **R10 `(B/D) × E`** (→ `05-imputacao.md` l. 72, literal);
**`art. 354` = 0 em 471 páginas** (→ `05-imputacao.md` l. 119); **+R$ 30.452,43 de não
descarregar** (→ `00-base-normativa.md` § 7); **os quatro validadores citados pelo core**
(→ existem; contei **18 `.py`** em `scripts/calculo/`); **consolidação de dez/2021, cinco
lugares e 0,4412% nos cinco** (→ `02-atualizacao-detalhe.md` § 10); **quatro presets sem
default** (→ `presets-regime.md` § 3). **Todas conferem.**

### 5.4 O segundo erro — pequeno, e induz conduta errada no comparador

`calculo-judicial-core`, § "Fixtures de aceite": *"As fixtures 2 e 4 **divergem do corpus** em
R$ 0,01 e R$ 0,03."* **Falso.** Elas divergem **entre o método resumido e o detalhado, ambos
publicados pelo corpus** (`pagina_pdf` 52 × 53 e 91 × 92). A `calculo-judicial-atualizacao` diz
certo (*"R$ 0,01 entre detalhado e resumido"*), e a fixture também
(`divergencia_e_assercao: true`). **A redação do core converte uma asserção de dois métodos numa
tolerância de um número** — exatamente o defeito que o runner da Frente A acabou tendo (§ 1).
**A skill induziu o defeito que o código apresenta.**

---

## 6 — A comparação das duas listas

### 6.1 Tamanhos

O registro da Frente A traz **12 itens numerados**, mas **dois não são lacunas** — `#11`
(`aplicacao` de jan/2001) e `#12` (as sobreposições de R2), que ela mesma registra como *"caso em
que a skill cobriu"* e como achado do validador. **Lacunas efetivas: 10**, mais **4
discordâncias** (§ 2 dela), 6 quase-invenções e 3 invenções declaradas.

**Minha lista (§ 3.1 + os dois erros de skill das §§ 5.1 e 5.4): 15. Dela: 14. Fatos comuns: 9.
Só meus: 6. Só dela: 5.** E as duas **elegem o mesmo item #1 e o mesmo item #2, na mesma ordem de
gravidade**: a série ausente e os dois métodos não definidos.

### 6.2 Onde convergimos

| Meu | Dela | Fato comum |
|---|---|---|
| L1 | **#1** e **#2** | a camada (B) inteira. Ela é mais precisa que eu: enumera os **seis intervalos** exigidos pelas quatro fixtures e conta que as skills publicam **exatamente cinco valores de índice**, *"cinco pontos isolados não fazem cadeia"* |
| **L2** | **#6** | **o procedimento dos dois métodos nunca é definido.** Ela chega à mesma conclusão que eu sobre a consequência: *"IMPOSSÍVEL nas fixtures 2 e 4 **independentemente da lacuna #1**"* |
| L3 | #4 e #8 | "mensalizada" sem definição aritmética |
| L4 | #4 | série da Selic **anual** |
| L5 | #3 | ordem interna da consolidação de dez/2021 — e ela decompõe em três sub-perguntas (base dos 0,4412%; mês do 1,17%; soma ou incidência à parte) |
| L7 | #9 | precisão interna sem número declarado |
| L12 | #8 | *"percentual devido"* indefinido |
| **L8** | **§ 2 (b)** | **6 casas de truncamento da skill × 10 decimais publicados no `coeficiente_correcao` da fixture 3.** Convergência num ponto fino: nós dois notamos que *neste caso* não muda o resultado, e que **noutro mudaria** |
| **§ 5.4** | **§ 2 (c)** | **o core diz *"as fixtures 2 e 4 divergem do corpus"*, e elas divergem é entre os dois métodos do próprio manual.** Achado idêntico, palavra por palavra no diagnóstico |

> **As duas últimas linhas são as que mais valem.** Não são o item óbvio: são erros de redação e
> de critério que só aparecem para quem confronta a skill com a fixture, e **duas leituras
> independentes acharam os dois**. Não é coincidência — é o defeito sendo real.

### 6.3 O que eu achei e ela não — 6

| Meu | Ela veria? |
|---|---|
| **§ 5.1 — a CONTRADIÇÃO entre `calculo-judicial-core` + `civel-federal.md` (`indeterminado`) e `indices-judiciais` + o catálogo JSON (`janela-deslocada`) para IPCA-E e IPCA-15** | **Ela citou os DOIS lados no mesmo item (#10) e não notou que se contradizem.** Transcreveu `janela-deslocada` da `indices-judiciais` e, três linhas abaixo, *"onde a ponta é indeterminada não se sabe sequer se há virada"* de `civel-federal.md` — e tratou as duas como compatíveis. **A contradição foi invisível ao implementador**, que a resolveu silenciosamente a favor de uma das duas. É o pior resultado possível para uma skill: não bloqueou, não alertou, **passou** |
| **L6 — a retomada da correção ao fim do englobamento**; **L9 — honorários separados**; **L11 — a montagem da coluna "% de juros"** | parou na primeira `SerieAusente`, antes de montar o coeficiente composto da fixture 3 e de chegar aos honorários |
| **L10 — quando a imputação NÃO se consulta** | ver § 6.5, item 1: ela foi para o lado oposto |
| **L13 / a contradição do critério 4** — "Fixtures de aceite" nas quatro skills × "a série não existe" em `indices-judiciais` | ver § 6.5, item 3: **divergência de julgamento, não de leitura** |

### 6.4 O que ela achou e eu não — 5

**Os cinco são bons, e dois são melhores que qualquer item meu do mesmo tipo.**

1. **#5 — a janela `Fazenda, jul/2009 a nov/2021` não tem fórmula de `aplicacao` atribuída.**
   `civel-federal.md` § 5 dá **D1** a *"Fazenda, a partir de dez/2021"* e **D2** a
   *"não-Fazenda; e Fazenda de jan/2003 a jun/2009"*. **A janela do meio fica descoberta — e a
   fixture 1 cai exatamente nela** (citação 01/2021). Eu li a mesma tabela e não vi o buraco.
   **Ver a ressalva em § 6.5, item 2: acho que a skill responde, mas responde mal.**
2. **§ 2 (a) — R1 está na prosa, não no dado.** O core manda impedir R1 *"na composição"*, mas as
   duas cadeias em schema **se sobrepõem de verdade** em `2003-01..2009-06` (correção `IPCA-E` ×
   juros `Selic` com `engloba: ["juros-mora","correcao-monetaria"]`). Quem resolve é a **NOTA 2**,
   que é **texto de `reference`, não campo de schema**. Conferi nos JSON: exato. **Achado
   arquitetural** — um motor que cheque R1 só pelo dado acusa erro material em 6 anos de cadeia
   vigente. Eu não o fiz.
3. **§ 2 (d) — `tributario-federal.md` § 7 diz *"0,5% a.m. desde ago/2001"* como regra que
   sobrevive no precatório; a fixture 4 transcreve o critério da poupança.** Conflito
   reference × fixture que eu não confrontei. Ela não arbitrou — correto.
4. **#2 — a contagem: as skills publicam cinco valores; a fixture 1 sozinha precisa de 23 meses
   de IPCA-E e 12 de juros de poupança.** Eu afirmei a ausência; ela a **quantificou**.
5. **#10, segunda metade — `indices-judiciais` dá as três classes e os três pares de virada e NÃO
   dá a régua de ajuste de nenhum dos três.** *"Diz o que o validador faz (bloqueia), não o que o
   motor calcula."* **Mais preciso que o meu § 5.1 num aspecto:** mesmo resolvida a contradição
   que eu achei, **ainda não há como implementar R3**. Os dois achados são aditivos.

### 6.5 As divergências — e cada uma é um achado

**Três. Nenhuma delas é "ela errou".**

**1 — `pr.imputacao` na fixture 4. Ela bloqueou; eu digo que não havia o que imputar.**
Item **#7** dela: *"a fixture 4 **não informa** qual imputação usar... IMPOSSÍVEL na fixture 4 sem
que alguém informe o preset"*. Meu **L10**: o pagamento de ago/2018 da fixture 4 vem **já
discriminado** (`principal: 21000.00`, `juros: 3150.00`) — **não há ordem de imputação a
arbitrar**; há abatimento componente a componente.

> **Ela bloqueou uma fixture por uma decisão que a fixture já tomou.** E a causa é da skill: o
> core apresenta `pr.imputacao` como bloqueio **incondicional** (*"sem default: NÃO arbitre.
> Pergunte ou bloqueie"*) e **nunca diz quando a imputação sequer se consulta**. **O mesmo
> silêncio produziu, em mim, um item de lista e, nela, um falso bloqueio.** É a demonstração mais
> limpa deste teste: a lacuna existe, e a forma como ela se manifesta depende de quem lê.

**2 — `#5`, a janela D1/D2 descoberta. Ela registrou como lacuna; a skill responde — mal.**
O literal da NOTA 4, transcrito na própria `civel-federal.md` § 5, abre com ***"A taxa Selic***
*: a)... b)... c)..."*. **D1 e D2 são fórmulas de defasagem DA SELIC** — e a janela
`Fazenda 2009-07..2021-11` **não usa Selic** (usa 0,5% a.m. e, de 2012-05, a poupança). Não há
`aplicacao` a atribuir: a pergunta não se põe.

> **Mas a skill não diz isso.** Apresenta D1/D2 numa tabela de *"fórmulas de `aplicacao`"*
> indexada por **devedor e período**, descolada do escopo *"a taxa Selic"* do literal. **Quem lê
> a tabela — o formato que a skill escolheu para ensinar — vê um buraco onde não há.** Pelo
> desenho do teste isso é resultado, não erro dela: **a skill diz, e diz em forma que induz a
> leitura errada.** É a categoria "diz mal", a mais grave por **parecer coberta**.

**3 — o julgamento sobre a responsabilidade da skill pela camada (B).**
Ela **absolve**, logo abaixo do item #1: *"Isto não é defeito das skills: elas declaram a
fronteira (A)×(B)... O motor está do lado (A) e (A) está completo. O que falta é o dado, e as
skills dizem que falta."*

**Eu não absolvo, e a divergência é de escopo, não de fato.** Ela tem razão sobre a camada (A).
Mas as **quatro** skills trazem `## Fixtures de aceite` apresentando as fixtures como **critério
de aceite operacional**, e o `README.md` delas afirma *"um agente novo lê a skill, implementa, e
o resultado bate aqui"*. **Declarar a limitação num lugar e negá-la noutro, no mesmo pacote, é o
defeito.** Ela não podia ler `00-base-normativa.md` § 8 com o consolidado ao lado, e portanto não
tinha como ver que **os quatro totais ocorrem num único arquivo do repositório, sempre como
resultado transcrito e nunca com os operandos.** Eu podia, e vi.

### 6.6 O que a Frente A inventou

Ela declara **três** invenções, todas confirmadas no código: **`getcontext().prec = 50`**
(necessária — a skill não dá número); **a ordem interna de `consolidar_dez_2021`** (marcada
`COMPOSIÇÃO` no docstring); e **a tradução de *"inclusive para o mês de pagamento"* em
`d1_competencias`** (ela mesma registra que *"admite outra leitura"*). **As três nunca
executaram.**

**Achei duas que ela NÃO declarou na § 4**, ambas só no docstring: **generalizar a NOTA 2 — que
fala de Selic × IPCA-E — para a "taxa legal"** (inferência legítima, R1 a sustenta, mas é
extensão de norma literal) e **`honorarios()` aplicando o pct separadamente a principal e juros**
(vem da `observacao` da fixture, não de skill). **Sub-declaradas, não silenciosas.**

**Nenhum valor de índice foi inventado.** Confirmei os cinco de `VALORES_LITERAIS` contra as
`references/` citadas: 1,17% · 0,84% · 0,00% · 1,16% · 1,305984%. **Todos corretos, com fonte ao
lado.** Nenhuma fixture tocada, nenhuma skill editada, nada da web.

**E a § 3 dela — "onde quase inventei, e me contive" — é a melhor parte da entrega.** Em especial
o item 2: ela **mostra a álgebra** que extrairia a Selic de 3,548% da parcela de 02/2022
**a partir do gabarito da fixture**, nomeia isso como *"engenharia reversa do gabarito, não
cálculo"*, e **não faz**. E o item 1: recusa usar a taxa legal de mai/2026 publicada porque é da
**variante INPC** e a cadeia pede a variante **IPCA-15** — *"seria trocar a série por semelhança
de número"*. **Exatamente a disciplina que as skills pedem, aplicada contra o próprio interesse
de fazer a fixture passar.**


## 7 — Veredito por fixture

| Fixture | Veredito | Fundamento |
|---|---|---|
| **01 — FP jun/2022** | **NÃO REPRODUZÍVEL PELA SKILL** | falta IPCA-E 01/2020–11/2021, Selic 2022, e a fórmula de "mensalizada". Bloqueio honesto e no lugar certo |
| **02 — FP jun/2026** | **NÃO REPRODUZÍVEL PELA SKILL — e a asserção é inalcançável** | além de 01, exige os **dois métodos**, que a skill nunca define. A divergência de R$ 0,01 **não podia** ser produzida |
| **03 — não-FP jun/2026** | **NÃO REPRODUZÍVEL PELA SKILL** | falta a série e falta a regra de **retomada da correção** após o fim do englobamento (L6). A montagem aritmética foi conferida, circularmente e com a circularidade declarada |
| **04 — precatório** | **NÃO REPRODUZÍVEL PELA SKILL — e a asserção é inalcançável** | falta INPC/IPCA-E 2016–2020, "mensalizada", "percentual devido" e os **dois métodos**. A divergência de R$ 0,03 — *"o melhor teste de arredondamento do conjunto"* — **não podia** ser produzida |

**Veredito sobre o motor da Frente A:** 0 de 4 reproduzidas, **0 de 4 erradas**, 4 de 4 bloqueadas
com o ponto de parada nomeado e o escopo de busca declarado. **Aritmética correta onde foi
possível verificá-la** (R11 nos dois pares publicados; NMP de três ramos; R12 sem um único float;
R1/R2 sobre as cadeias reais nos dois ramos, 1964–2026).

**Veredito sobre as skills — que é o objeto deste teste:**

1. **A camada de invariantes e aritmética funciona.** Tudo que o implementador podia construir só
   com a skill, ele construiu, e está certo. R11 e R12 passam com verificação externa.
2. **A camada de dados não existe, e as skills afirmam o contrário na seção de fixtures** — o
   defeito de integridade central.
3. **O procedimento dos dois métodos é a lacuna não declarada mais cara do conjunto**: torna
   inalcançável a asserção que as próprias skills chamam de melhor teste do pacote.
4. **Há uma regra errada, operacional, na skill declarada obrigatória**: IPCA-E e IPCA-15 como
   `indeterminado` no core e em `civel-federal.md`, contra `janela-deslocada` no catálogo e em
   `indices-judiciais`. **Cai em cima das fixtures 1, 2 e 3, e passou despercebida.**
5. **Há uma redação errada que induziu defeito visível no código**: *"divergem do corpus"* em vez
   de *"divergem entre os dois métodos"*.
