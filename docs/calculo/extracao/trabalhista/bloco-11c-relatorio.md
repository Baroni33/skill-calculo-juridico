# Bloco 11C — relatório

Capítulo 10, segmento D — Exemplos 5 e 6, juros vincendos e art. 12-B.
pp. 266 (offset 2141) a 277. Produto em `bloco-11c-vincendos.md` e
`bloco-11c-vincendos-detalhe.md`.

**Com este bloco a amortização do capítulo 10 está fechada.** Resta o segmento B.

---

## 1. Entregas

| Item | Estado |
|---|---|
| Critério alternativo da letra C (objetivo primário) | **Extraído — e a obrigatoriedade não tem lastro** |
| Por que o segundo passo é obrigatório | **O manual declara a regra, não a razão** |
| Vincendos antes ou depois do rateio | **Respondida: antes** |
| O rateio muda com vincendos? | **Não — mas perde um centavo no Ex. 6** |
| Art. 12-B contra 12-A | **Respondida: sob 12-B não há NM** |
| Ex. 5 e 6 concordam entre si e com 1–4? | **Não** |
| Medição da amplitude | **Feita — e rendeu fórmula fechada** |
| Continuidade das pendências do 11B | **Feita — 2 reaparecem, 1 muda de forma, 1 não** |
| **R23** | **Verificada e observada** |
| Fase 4 / ADC 58 | **Feita — o segmento produz os dois extremos** |
| Releitura adversarial, tabular inclusive | **Feita — 14 defeitos** |
| Verificação literal por script | **Feita** |
| Notas e rótulos contra as linhas | **Feita — 11 conferidos** |
| Mapa de cobertura | **Atualizado — 86,8%** |

---

## 2. Cinco premissas do enunciado caíram

Este foi o bloco em que mais premissas minhas não resistiram. Registradas porque mudam a
leitura do resto:

1. **A moldura não é a de 10.3.1.** Os exemplos seguem a de **10.3.2** (pp. 239–241), que vai
   de A a O/P e **tem letra I**. O rateio é a letra **G**, não F.
2. **Os títulos dos Exemplos 5 e 6 são idênticos** — o do 6 é cópia literal do 5, inclusive
   "juros incluídos na base de cálculo do IR", **contradizendo seu próprio parâmetro OJ 400**.
   O que difere é o primeiro *bullet* de "Parâmetros".
3. **Não são um par controlado.** Objeto, datas, INSS, regime de IR e ordem de grandeza variam
   todos junto — não se isola o efeito da OJ 400.
4. **"Com vincendos o tempo residual é maior por definição" é falso.** O Exemplo 6, o dos
   vincendos, tem o **menor** residual do capítulo: 19 dias.
5. **Minha formulação da escala da amplitude estava incompleta.** Ver § 4.

É a quarta vez na série que uma premissa do enunciado — não do manual — não resiste. A regra
que as apanha é sempre a mesma: exigir a busca que sustenta a afirmação, inclusive quando a
afirmação é minha.

---

## 3. O objetivo primário, e o que ele revelou

O critério alternativo da letra C existe e os dois exemplos o usam — provado pela aritmética,
não pelo rótulo (`60.162,49 × 1,0153923 = 61.088,53`; `72.119,61 × 0,15833330 = 11.418,94`,
sobre o **principal corrigido**, como o passo 2 manda).

**Mas três coisas o esvaziam:**

**A decomposição é descartada duas letras adiante.** Os dois componentes são somados num
único `C` pela letra D, e o rateio usa apenas `C / D`. A distinção que os três passos
produzem **não sobrevive**.

**A obrigatoriedade não tem lastro.** `obrigatór*`, `porque`, `razão` → **0 ocorrências** nas
pp. 266–277. E o par **não a demonstra**: os dois critérios coincidem quando
`p_total − p2 = J0/P0`, e nenhum dos exemplos informa data de ajuizamento ou percentual
acumulado — **o critério 1 é inexecutável a partir do publicado**. Sob a única reconstrução
possível, os dois dão **delta 0,00**.

**E o exemplo dos vincendos não exercita vincendos.** Os `251,02` que o Ex. 6 rotula como
"juros vincendos" são, pela própria planilha, juros **vencidos** até 31/03/16. Não há
sobreposição com o período residual.

> A hipótese que a moldura declara obrigatória atravessa o capítulo inteiro **sem um único
> exemplo que demonstre por que o outro critério falharia.** Pendência **P10D-04**.

Isto é o mesmo padrão do bloco 11B, noutro plano: lá a regra mais cara era aplicada sem
fundamento jurídico; aqui a regra declarada **obrigatória** é aplicada sem demonstração de
necessidade.

---

## 4. A amplitude tem fórmula fechada

O 11B mediu 23,83% e 0,25%, e eu descrevi a escala como "tempo residual × participação dos
juros no bruto". **Incompleto.** A forma correta:

```
amplitude = min(abatimento, B, C) × índice_residual × percentual_juros_residual
```

Verificada por mim nos três casos disponíveis: 36,60 · 9.919,52 · 22.272,55 — batendo com os
valores reportados.

**O que ela revela, e que a formulação anterior escondia:**

| Exemplo | Juros/bruto | Amplitude R$ | Amplitude % |
|---|---|---|---|
| Exemplo 1 | 26,92% | 9.918,92 | **23,83%** |
| **Exemplo 5** | **50,13%** | **22.272,55** | **15,85%** |
| Exemplo 6 | 3,42% | 2,51 | 0,05% |

**O Exemplo 5 tem quase o dobro da participação de juros e amplitude percentual MENOR** —
porque ali o limitante é o **abatimento**, não os juros. Em valor absoluto é 2,25× o Ex. 1.

O termo que manda é o **mínimo entre três grandezas**, e qual delas limita muda de caso para
caso. Era isso que a formulação por "participação dos juros" ocultava.

---

## 5. R23 — observada, e o fundamento está numa minuta

**O segmento D observa o "descarregar" integralmente**, inclusive com vincendos. Ex. 5: juros
residuais sobre 54.940,54, não sobre 138.448,90 — a diferença seria **+30.452,43**.

**A distinção que o enunciado pediu para testar confirma-se.** São duas regras
anti-anatocismo distintas:

| | Onde | Operação |
|---|---|---|
| Regra 1 | p. 16 | juros acumulam por **soma**, nunca por multiplicação |
| Regra 2 | p. 237 | **"descarregar"** — excluir os juros do saldo antes de aplicar juros novos |

A **Súmula 121 do STF** é invocada **uma única vez em todo o manual**, na p. 16, e **só para a
regra 1**.

**Mas a parte "o manual nunca as conecta" é parcialmente falsa** — e isso eu só descobri
procurando. A **p. 328** descreve exatamente a operação do "descarregar" e a nomeia:

> "recalculando os juros de mora desde a inicial, **não incidindo juros sobre juros
> (anatocismo)**"

**É uma minuta de petição do capítulo 16.** O capítulo técnico que executa a operação
(`anatocismo` → 0 ocorrências no cap. 10) nunca a nomeia; quem a explica é o modelo de ofício.

**Repete, com outro assunto, o achado do 11B** — e reforça que o capítulo 16 é fonte
normativa, não formulário (P10-C16).

---

## 6. BLOQUEIO, maior que o do 11B

**P10D-01**, Exemplo 5, letra I, pp. 269 e 271:

```
53.063,01 × 1,04095137 = 55.236,01      impresso: 53.199,50      delta 2.036,51
índice implícito 1,00257222 — não corresponde a nenhum índice do exemplo
```

Conferido nas 471 páginas: `53.199,50` ocorre **só nas pp. 269 e 271**, e `55.236,01` **não
existe em nenhuma**. Não é cópia, não é transposição, não é arredondamento.

**Propaga:** J 138.448,90 → 140.485,41; IR 4.162,83 → 4.468,30; **TOTAL 154.874,90 →
156.911,41.**

Verificado por mim. **Não contornado.**

---

## 7. As pendências do 11B

| # | Estado |
|---|---|
| **P11B-02** NMP | **Reaparece e piora** — `17,16303 → 17,2`, e aqui nem a nota sobre "regra de arredondamento" existe (`arredond*` → 0) |
| **P11B-03** | **Não reaparece como divergência**, mas reaparece como **resíduo**: a p. 267 imprime operandos do Exemplo 1 |
| **P11B-04** | **Reaparece com causa declarada** — Ex. 5 com juros, Ex. 6 pela OJ 400. Divergência **instanciada, não resolvida** |
| **P11B-05** gross-up | **Não reaparece** — fecha exato nos dois |

---

## 8. Fase 4 — os dois extremos no mesmo segmento

| Exemplo | Juros/bruto | Sensibilidade a ±20% em `C` |
|---|---|---|
| **Ex. 5** | **50,13%** (maior do capítulo) | **2,40%** do total |
| **Ex. 6** | **3,42%** (menor) | **0,004%** |

Cerca de **600× de diferença** entre dois exemplos do mesmo segmento. O atrito com a ADC 58
identificado no 11B **agrava no Ex. 5 e desaparece no Ex. 6**.

**E há um atrito estrutural que nenhum número expressa:** sob **Selic** pós-citação, a
distinção entre principal e juros — que sustenta tanto o rateio quanto o critério alternativo
da letra C — **deixa de existir**. Não é que o resultado mude: **a operação perde objeto**.

Marcado, não harmonizado.

---

## 9. Cobertura

**86,8%**, contra 84,5% ao fim do 11B.

| | Páginas |
|---|---|
| Cobertas | **409** |
| Não cobertas **com decisão registrada** | **40** |
| Não cobertas **sem decisão** | **14** |

O capítulo 10 tem **56 das 69 páginas cobertas** — a amortização está fechada. Resta o
segmento B (13 pp., bloco 11D).

**Os capítulos 8, 12 e 14 seguem sem destino**, mantidos visíveis e não classificados por
conta própria, conforme o enunciado.

---

## 10. Pendências

Oito, em `bloco-11c-vincendos.md` § 11. As que decidem:

- **P10D-01** — o bloqueio de 2.036,51, que propaga ao total;
- **P10D-04** — a obrigatoriedade do critério alternativo **sem lastro demonstrativo em todo o
  manual**; o critério 1 é inexecutável a partir do publicado;
- **P10D-06** — o exemplo dos vincendos não exercita vincendos;
- **P10D-08** — a migração de regime tributário dentro do mesmo cálculo (Ex. 5) é caso único
  do manual, sem enunciado que a discipline.

---

## 11. Lição de método

O 11A ensinou que fronteira de segmento não é fronteira de página. O 11B, que a regra mais
cara podia não ter fundamento. Este bloco fecha a tríade:

> **Uma regra pode ser declarada obrigatória e não ter demonstração de que é necessária.**
> O manual diz que o segundo critério "é obrigatório" quando há vincendos, e atravessa 69
> páginas sem mostrar um caso em que o primeiro erre. Pior: nos dois exemplos que deveriam
> exercitá-lo, os dois critérios dão o mesmo número.

Extração que registrasse "critério alternativo obrigatório sob vincendos, item 10.3.1, p. 237"
estaria correta e seria enganosa. **A pergunta "o manual declara a razão ou só a regra?" é o
que separa uma das outras** — e ela veio do enunciado, não da minha iniciativa. Vale mantê-la
como item fixo dos blocos seguintes.
