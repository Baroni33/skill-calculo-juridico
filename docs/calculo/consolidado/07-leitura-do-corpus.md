# Leitura do corpus

**Os padrões de como este manual se lê.** Não é metodologia abstrata: cada padrão abaixo foi
**confirmado em extração**, e ignorá-lo produziu erro real em algum bloco.

Serve a quem for ler o corpus adiante — ou reabri-lo quando sair a próxima edição do manual.

---

## 1. Regra de cálculo mora no exemplo; enunciado é minoria do texto

**Confirmado nos capítulos 9, 10, 11 e 16.**

| Capítulo | Regras que só existiam dentro de exemplo |
|---|---|
| 9 — descontos | **7** |
| 10.1 — atualização simples | **12** |
| 11 — exemplos | **17** estruturais, 20 incidentais |
| 16 — minutas | **6** fundamentos exclusivos |

**Regra encontrada em exemplo é PROMOVIDA à espinha**, com marcação de origem. Três das mais
consequentes:

- **mês comercial de 30 dias com contagem inclusiva** — `dias = 30 − dia_inicial + 1`. Testado
  em cinco períodos: **5 de 5** fecham pela regra inclusiva, **0 de 5** pela exclusiva. O
  divisor aparece na fórmula impressa; **a convenção de contagem, não**;
- **precisão plena encadeada** — os números impressos com 2 casas **não são os operandos**;
- **a base da multa do art. 467** inclui saldo de salário e a multa de 40% sobre o FGTS —
  **nenhum dos dois no rótulo**.

> Um extrator que leia só os enunciados normativos sai com **menos da metade** das regras — e
> sem as que mais mexem no número.

---

## 2. O manual pratica no capítulo técnico e fundamenta na minuta

**Confirmado três vezes, e depois medido.** A varredura dirigida do capítulo 16 cruzou **36
fundamentos** contra os capítulos técnicos. **A maioria É citada.** Mas **seis não são**:

| Fundamento | Onde só ele aparece | Ocorrências no manual |
|---|---|---|
| **IN SRF 15/2001** — fonte declarada do *gross-up* | 16.4.4.10, p. 326 | **1 em 471 páginas** |
| **Súmula 15 do TRT-3** — dedução no levantamento | 16.4.11, pp. 333–334 | **cap. 10: zero em 69 páginas** |
| **Súmula 454/TST** — SAT na desoneração | 16.4.3.19 | 3, todas no cap. 16 |
| **Súmula 388/TST** + art. 83 da Lei 11.101/05 | 16.4.9.2 | 2 e 1, na p. 332 |
| **Prov. 03/91** e art. 104, § 5º, do PGC | 4 itens | **zero em capítulo técnico** |
| **anatocismo aplicado à amortização** | p. 328 | cap. 10: **zero** |

**A IN SRF 15/2001 é a mais grave:** é a fonte da fórmula de *gross-up*, e a expressão "bruto em
relação ao líquido" ocorre em **16 páginas, 15 delas no capítulo 10** — que usa a fórmula em
todos os exemplos e **nunca diz de onde ela vem**.

> **A lição é mais estreita do que "o capítulo 16 é a fonte do manual".** É que **há operações
> centrais cuja única fundamentação está fora do capítulo que as executa** — seis de trinta e
> seis. Quem extrair só os capítulos técnicos fica com as operações sem as razões.

---

## 3. "Cancelada" quase nunca significa "nunca valeu"

**O achado que reorganizou o confronto normativo** (Fase 3, bloco 14).

A **Resolução 225/2025 do TST** cancelou 36 enunciados. **E cada inciso declara a data em que o
verbete perdeu eficácia** — `a partir de` ocorre **27 vezes** no ato:

> "Súmula nº 437 (cancelada por perda de eficácia **a partir de 11/11/2017**, pela Lei
> 13.467/2017)"

**O TST não revogou: declarou que os verbetes já haviam perdido eficácia no passado.** Isso é
**cadeia temporal**, não supersessão.

> **Quem registrar "Súmula 437: cancelada" e apagar o verbete erra todo fato anterior a
> 11/11/2017.** E o produto calcula passivo anterior.

**É por isso que 32 dos 50 vereditos são `BIFURCADO`.** Nem a Reforma, nem a ADC 58, nem a
Res. 225/2025 revogaram com efeito *ex nunc*. **Todas cortaram no tempo.**

**Consequência de arquitetura:** o motor não pode ter *uma* tabela de regras vigentes. Precisa
de **cadeia temporal por ponto** — como já tem para índices.

---

## 4. Dentro de período homogêneo pode haver subjanela

**A MP 808/2017** vigorou de **14/11/2017 a 22/04/2018** e não foi convertida em lei. Cinco
meses **dentro** do período pós-Reforma, com texto **diferente dos dois lados**: abonos
integravam, prêmios só ficavam fora se até 2×/ano, a 12×36 exigia norma coletiva.

**Afeta cinco pontos.** É a variante mais fácil de perder, porque quem olha "antes e depois de
11/11/2017" não vê que há um terceiro estado no meio.

> **Generalização:** um corte não garante que o período seguinte seja homogêneo. Medida
> provisória não convertida cria janela; modulação cria janela; e o calendário precisa
> registrá-las **como período próprio**, não como exceção em nota.

---

## 5. Ficha de tema localiza o acórdão; não o substitui

**Verificado em PDF:**

| Ficha | Defeito |
|---|---|
| **Tema 9 do TST** | traz a tese firmada e **omite a modulação**. Quem consultar só ela conclui `SUPERADO` onde o correto é `BIFURCADO` |
| **Tema 23 do TST** | *"Tese Firmada"* **em branco**, situação *"Afetado"* — cache anterior ao julgamento de 25/11/2024 |

**Os acórdãos publicados supriram, com texto primário completo.** Canais que funcionaram:
`portal.trt3.jus.br` — que hospeda acórdãos do STF —, `stj.jus.br` e `juslaboris.tst.jus.br`.

**Recusaram acesso automatizado:** Planalto, DOU, Receita Federal, `portal.stf.jus.br`, Legin.

---

## 6. Afirmação de ausência exige escopo declarado

> **"Zero ocorrências no segmento" e "zero ocorrências em 471 páginas" são afirmações
> diferentes, e só a segunda sustenta uma negativa sobre o manual.**

**O erro mais caro da série foi meu, e foi exatamente este.** Escrevi em **dois blocos** que
*"a regra de arredondamento do NMP nunca é declarada"* e a tratei como inferência.

**Ela é declarada, duas vezes**, nas pp. 226 e 230 — com o artigo transcrito. **A varredura que
sustentava minha negativa cobria só o que eu já tinha extraído.** A regra estava nas 13 páginas
que faltavam.

**E não era detalhe:** o art. 45, par. único, da IN 1500/14 tem **três ramos** e **não é
half-up** — difere de `ROUND_HALF_UP` na faixa `x,y50`–`x,y54`.

**Corretivo que funcionou:** declarar o escopo **junto com o resultado**. "Zero ocorrências" sem
dizer *em quantas páginas* é afirmação que não pode ser auditada.

---

## 7. Fronteira de conteúdo vence fronteira de página

**Nenhuma das fronteiras internas do capítulo 10 é quebra de página.** Todas caem no meio de uma
folha:

| Fronteira | Onde |
|---|---|
| 10.1 → 10.2 | p. 223, **offset 2.658** |
| 10.2 → 10.3 | p. 237, **offset 681** |
| Ex. 4 → Ex. 5 | p. 266, **offset 2.141** |

**E o achado mais grave do segmento A estava no trecho que a fronteira errada teria cortado** —
a **A4** (`../armadilhas-comparador.md` § 1), a linha copiada da p. 261 para a p. 223, com a
multa junto.

**Corolário:** a numeração impressa também não é guia. Ela **para em 10.3.2.1, na p. 239**, e o
capítulo segue por mais 38 páginas — **55% dele** — estruturadas apenas por `Exemplo 1` a
`Exemplo 6`.

---

## 8. Catorze premissas caíram na extração — nenhuma veio do manual

Este é o padrão que mais custou, e o mais desconfortável de registrar.

| Bloco | Premissas derrubadas |
|---|---|
| 10 | 4 — numeração do escopo, mais a "multa do art. 477" que era 467 |
| 11C | 5 — moldura, títulos, par controlado, residual, escala da amplitude |
| 12 | 2 — "terceiro caso" de R20-EXCEÇÃO, página de A1 |
| 13 | 7 — arredondamento do NMP (duas vezes), IPIR, 16.4.11, 16.4.7, sumário, faixas do art. 85 |
| 14 | a EC 113/2021 "só federal" |

**Todas vieram de quem conduzia a extração — eu ou o enunciado.** Nenhuma veio do manual.

> **O manual erra muito** — 47 defeitos catalogados, 15 promovidos a armadilhas. **Mas erra de
> forma detectável**, porque publica os operandos. As premissas de quem o resume **não publicam
> nada**, e por isso atravessam blocos.

**Corretivo:** tratar premissa do enunciado com o mesmo ceticismo que afirmação do manual — e
exigir dela a mesma busca declarada.

---

## 9. O que ainda não se sabe ler

Registrado para que ninguém presuma que o corpus está compreendido:

| Aberto | Natureza |
|---|---|
| **dois bloqueios aritméticos** — pp. 266 e 269 | deltas de **10,00 exatos** e **2.036,51** com índice sem origem. Nenhum é arredondamento |
| **a obrigatoriedade do critério alternativo da letra C** | declarada e **não demonstrada** em 69 páginas |
| **migração de regime tributário no mesmo cálculo** | caso único (Ex. 5), **sem disciplina em todo o manual** |
| **a contradição sobre Fazenda Pública** | caps. 8 e 14 dão **testes incompatíveis** |

---

## 10. Resumo operacional

Para quem for reler o corpus:

1. **meça o capítulo antes de dividi-lo**, e meça do texto — não do sumário;
2. **leia os exemplos**, não só os enunciados. É onde está a maioria das regras;
3. **procure o fundamento fora do capítulo** que executa a operação;
4. **trate "cancelada" como data**, não como apagamento;
5. **desconfie de período homogêneo** — pode haver MP no meio;
6. **declare o escopo de toda negativa**;
7. **refaça toda conta em `Decimal`**, e não alarme no centavo;
8. **duvide da sua própria premissa** tanto quanto da do manual.
