# Bloco 10 — relatório

Fechamento da extração trabalhista. Produto em `bloco-10-fechamento.md`,
`bloco-10-fechamento-detalhe.md`, `../../jurisprudencia-indice.md` e
`../mapa-de-cobertura.md`.

---

## 1. Entregas

| Item | Estado |
|---|---|
| Confirmar a numeração impressa | **Feito — e o escopo do enunciado não existia.** § 2 |
| Cap. 7 residual (juros vincendos) → espinha | **Feito** — método, 6 regras, aritmética refeita |
| Cap. 13 → espinha | **Feito** — 1 página, integral |
| Cap. 11 → regras dentro de exemplos | **Feito** — 7 casos, **17 achados estruturais**, 20 incidentais |
| Cap. 15 | **Feito** — 8 itens; reclassificado, ver § 4 |
| Cap. 17 → índice de referência | **Feito** — 158 verbetes |
| Confronto obrigatório do cap. 17 | **Feito** — os 4 casos de conferência reproduzidos |
| Releitura adversarial, inclusive tabular | **Feita** — toda a aritmética dos 7 exemplos em `Decimal` |
| Verificação literal por script | **Feita** — 150/154 OK; 10 páginas corrigidas |
| Notas contra as linhas que qualificam | **Feita** — 20 notas, 6 com atrito |
| **Mapa de cobertura** | **Feito** — e é o achado do bloco. § 6 |

---

## 2. A numeração do enunciado não existia

Pedido expressamente por causa do capítulo 6. Fez diferença: **quatro dos cinco rótulos do
escopo não correspondem ao manual.**

- "13 — Diferenças salariais" → **6.15**, já coberto pelo bloco 4. O cap. 13 é *dívida ativa
  da União*, com uma página;
- "o que houver entre 6.15 e o capítulo 16" → são os **capítulos 7 a 14 inteiros**;
- "item 7.6.1" → **não existe**; é subtítulo não numerado, e vai até a p. 99, não 98;
- "15.2 / 15.4 / 15.5" → **não existem**; o capítulo é lista de 1 a 8.

E o **capítulo 13 não consta do sumário do próprio manual** — a p. 6 salta de 12.4 para 14.

### 2.1 Um erro meu, da mesma classe do bloco 9

Ao instruir a extração do cap. 15, afirmei que o item 2 tratava da **multa do art. 477**.
Inferi de uma linha truncada do sumário. **É o art. 467** — `477` não ocorre nenhuma vez nas
pp. 307–309.

Foi apanhado porque a instrução exigia **registrar a busca que sustenta a negativa**, e a
varredura devolveu a contagem. É exatamente a disciplina que faltou no bloco 9, funcionando
na direção contrária: desta vez a premissa falsa era minha, e morreu antes de virar artefato.

**Lição que vale registrar: premissa do operador precisa da mesma verificação que afirmação
do extrator.** O enunciado do bloco é fonte tão falível quanto o manual.

---

## 3. Capítulo 11 — o padrão se repetiu, e maior

O bloco 7 encontrou sete regras sem enunciado normativo no capítulo 9. O capítulo 11 tem
**dezessete estruturais**. As três que mais pesam:

**Precisão plena sem regra de arredondamento.** Os números impressos com duas casas **não
são os operandos** — provado em três exemplos independentes. E o manual **não tem regra de
arredondamento monetário**: `arredond` aparece cinco vezes, todas sobre número de meses do
RRA; `casas decimais`, `truncad` → zero. Consequência medida: **as colunas impressas não
somam os totais impressos**. É a origem de toda a tolerância de centavos do corpus.

**Mês comercial de 30 dias contado do dia da admissão.** `17/02/2014` conta 14 dias, não os
12 de fevereiro. `mês comercial` e `30 avos` → zero ocorrências. A regra existe, o enunciado
não. Confirma o achado do bloco 9 por outra via.

**Acordos: os exemplos aplicam a corrente que o texto declara superada.** Correção e juros
do dia seguinte ao vencimento da parcela — que a p. 84 chama de **"4ª corrente"** histórica,
concluindo que *"Atualmente a aplicação dos índices de correção monetária ocorre na forma da
Súmula nº 381 do TST"*. E **Ex. 6 e Ex. 7 usam bases opostas para a multa** — original contra
corrigido —, consecutivos, sem nota.

### 3.1 O defeito de maior impacto do manual

**Ex. 8: o FGTS a depositar conta os juros duas vezes.** Verificado por mim, não só pelo
extrator:

```
Principal corrigido  12.824,00 × 1,01087868 = 12.963,51
Juros corrigidos      3.761,71 × 1,01087868 =  3.802,63
Juros 36,333333% s/ principal corrigido    =  4.710,08
                                   TOTAL   = 21.476,22  ← impresso no manual
```

Os **36,333333% já contêm** os 29,33% de juros até out/15 (`3.761,71 / 12.824,00`) mais 7%.
**Os dois métodos coerentes convergem em 17.673,59** — somar juros e depois 7%, ou aplicar
36,33% direto. O **excesso é 3.802,63**, exatamente a linha de juros corrigidos.

Na **mesma página**, o crédito principal usa corretamente duas linhas. Propaga para o resumo
e para o total de 292.265,29. Os quatro números foram confirmados no PDF. **Não corrigido.**

---

## 4. Capítulo 15 — reclassificado

O enunciado o mandava para a espinha "como método". **Não é método.** O manual declara na
p. 307 que são parâmetros a serem *"fixados previamente pelas decisões"* — é um **catálogo de
subdeterminação declarada pela própria fonte**, e o destino natural é a **camada de presets
do bloco 6**, não a espinha. O item 1 traz **três variantes sem eleger nenhuma**: a estrutura
exata de `variantes com fundamento, sem default`.

Dois itens escapam e vão para a espinha:

- **item 7** — regra supletiva expressa: sem discriminação no acordo, o IR incide sobre **o
  total da avença**;
- **item 8** — **R20-EXCEÇÃO**: sem teto fixado, *"a apuração fica impossibilitada"*. O
  manual proíbe resolver por default.

Registrei a reclassificação em vez de forçar o destino pedido. É decisão de modelagem, e
fica exposta para revisão.

---

## 5. Capítulo 17 — o índice serve para tornar a lacuna contável

**158 verbetes. A base normativa cobre 12 — 7,6%.**

Os 146 restantes ficaram `não coberto`, jamais `vigente`. A regra dura foi o ponto do
exercício: **ausência de notícia não é notícia de vigência**, e o número só aparece porque
nenhum verbete foi presumido.

**Os quatro casos de conferência foram reproduzidos pelo procedimento sozinho.** Três
bateram; o quarto devolveu um fato novo: **a Súmula 48 do TRT-3 não existe no manual** —
zero ocorrências em 471 páginas, e os dois "48" que aparecem são `ex-OJ 48` dentro de súmula
do TST. Isso **fecha a pendência 2 de `02a` § 19**.

Dois achados que o índice não podia deixar passar:

- **OJ 47 da SDI-1 aparece com duas redações divergentes**, pp. 350 e 354, sem sinalização —
  e a diferença (`este calculado sobre o salário-mínimo`) **muda a base de cálculo da hora
  extra**;
- **a OJ 394 é o verbete mais desenvolvido do manual em matéria de reflexos** — pp. 35, 44,
  45, 48, 286, 291, com exemplos numéricos. Está superada desde 20/03/2023. **Todo esse
  trecho do manual está invertido**, e o bloco 3 o extraiu como regra.

O capítulo ainda devolveu duas coisas ao corpus: o **Provimento 04/00** como **especificação
de contrato de saída do motor**, e o **Parecer COSIT 25** como o anexo que o item 9.2.10
citava sem localizar — fechando **P7-11**.

---

## 6. O mapa de cobertura, que era para ser burocracia

`../mapa-de-cobertura.md`. **Conferido em script, não estimado.**

| | Páginas |
|---|---|
| Cobertas | **353** |
| **Lacuna real** | **83** |
| Fora de escopo (cap. 16) | 27 |
| Pré-textuais | 8 |
| **Total** | **471** |

**Cobertura real: 74,9%** — não os ~95% que a sequência de dez blocos sugeria.

**Quatro capítulos nunca foram extraídos**, e a busca que sustenta a afirmação está
registrada no § 2 do mapa:

| Cap. | Título | Págs |
|---|---|---|
| **10** | **Atualização de débitos trabalhistas** | **69** |
| 8 | Encargos e despesas processuais | 7 |
| 12 | Contribuição sindical | 4 |
| 14 | Precatórios | 3 |

**O capítulo 10 é o problema.** 38 subitens sobre **amortização de valor pago** e descontos
proporcionais (arts. 12-A e 12-B da Lei 7.713/88). A ordem de imputação de um pagamento
parcial entre principal, correção e juros determina o saldo — é a operação mais sensível do
manual, e não está no corpus. **Recomendação: bloco próprio.** Não foi dobrado neste
fechamento porque é maior que os capítulos 7 e 11 somados.

E há **assimetria**: o bloco 8 extraiu as custas do manual federal; o capítulo 8 trabalhista
ficou fora. A comparação entre jurisdições está pela metade.

### 6.1 O capítulo 16 não é o que o título diz

Ia ser descartado como minuta processual. Fui verificar antes de escrever a negativa, e
**contém regra de cálculo**: o item **16.4.11** determina que o depósito **em garantia da
execução** se deduz na data do **levantamento**, não na do depósito (Súmula 15 do TRT-3) — a
mesma operação do capítulo 10. E **16.4.7** limita a multa ao *"principal corrigido"*, não ao
nominal.

Classificado como `fora-de-escopo-com-ressalva-confirmada`, com varredura dirigida
recomendada. **É o padrão "regra que só existe dentro de exemplo" aparecendo num capítulo
que ninguém leria.**

---

## 7. Verificação de citação literal

154 ementas confrontadas por script, normalizando NFKC, aspas tipográficas, travessões,
espaços e **folios** — o número da folha se intromete no meio de ementa longa e produz falso
alarme.

| Resultado | Nº |
|---|---|
| LITERAL-OK | **150** |
| literal, atravessando folha | 3 |
| **não localizada** | **1** |

**Dez atribuições de página estavam erradas e foram corrigidas pela própria verificação.**
O padrão é deslocamento de uma folha, salvo a Súmula 199 (339 → 346) e a Súmula 401
(340 → 341/347).

A não localizada é a **OJ 397 da SDI-1** — pendência **P10-17**.

---

## 8. O que este bloco deixa para a Fase 3

O mapa de cobertura é o artefato que a abre. Em resumo:

**Seis lacunas de extração**, encabeçadas pelo capítulo 10; **quatro lacunas de fundamento**
que não se fecham por extração nenhuma (P9-01, P9-02, P8-M1, P8-M2); e **onze pendências
próprias** deste bloco, das quais três são defeitos do original com efeito de valor — o FGTS
em dobro, a dupla incidência do índice sobre o INSS e a multa previdenciária que some entre
o demonstrativo e o resumo.

O que está sólido: os dois manuais com **paginação e fronteiras conferidas por script**,
onze cadeias temporais validadas por R1/R2, **204 testes**, e a disciplina de não harmonizar
mantida em dez blocos — divergência entre manuais, entre linha e nota, entre exemplos
consecutivos e entre correntes jurisprudenciais está registrada como divergência, com os dois
fundamentos, e não como conserto.

---

## 9. Lição de método

O bloco 9 ensinou que afirmação negativa sobre a fonte é conclusão, não dado, e precisa da
varredura que a sustente. Este bloco aplicou a regra e ela pagou três vezes: derrubou uma
premissa minha (o art. 477), confirmou uma negativa arriscada (a Súmula 48 não existe) e
impediu que o capítulo 16 fosse descartado sem leitura.

Mas o bloco acrescenta outra:

> **Cobertura declarada não é cobertura verificada.** Dez blocos de extração produziram a
> impressão de um manual quase esgotado. A contagem por script mostrou 74,9%, e a maior
> lacuna — 69 páginas sobre a operação mais sensível do motor — nunca tinha sido nomeada,
> porque ninguém havia listado o que *não* fora feito.

O mapa de cobertura deveria ter sido o primeiro artefato do projeto, não o décimo.
