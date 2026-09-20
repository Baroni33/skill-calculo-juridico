# Bloco 11C — capítulo 10, segmento D: vincendos e art. 12-B

Manual TRT-3, Exemplos 5 e 6, pp. 266 (offset 2141) a 277.
**Offset de paginação zero.** Detalhe em `bloco-11c-vincendos-detalhe.md`.

Fecha o capítulo 10 na parte da amortização. O segmento B (descontos proporcionais,
pp. 223–236) passa para o 11D.

---

## 1. Quatro premissas do enunciado que não resistiram

Registradas primeiro, porque mudam a leitura de tudo o que vem depois.

| Premissa | Realidade conferida |
|---|---|
| "os exemplos seguem a moldura A–H, J de 10.3.1; o rateio é a letra F" | **Seguem a de 10.3.2** (pp. 239–241), que vai de A a O/P e **tem letra I**. O rateio é a letra **G** |
| "Ex. 5 e Ex. 6 são um par controlado, distinguidos pelo título" | **Os títulos são idênticos** — o do Ex. 6 é cópia literal do Ex. 5, inclusive "juros incluídos na base de cálculo do IR", **contradizendo seu próprio parâmetro OJ 400**. O que difere é o primeiro *bullet* de "Parâmetros" |
| "são um par controlado" | **Não são.** Objeto, datas, INSS, regime de IR e ordem de grandeza variam todos junto. Não se isola o efeito da OJ 400 |
| "com vincendos o tempo residual é maior por definição" | **Falso.** O Exemplo 6 — justamente o dos vincendos — tem o **menor** período residual do capítulo: 19 dias |
| "a escala é tempo residual × participação dos juros no bruto" | **Incompleta.** Ver § 5, que traz a fórmula fechada |

---

## 2. O critério alternativo da letra C

O objetivo primário do bloco. Os três passos, literais (`pagina_pdf` 237):

> 1 — atualizar o total dos juros do último cálculo com o mesmo índice de correção utilizado
> para corrigir o principal até a data da amortização;
> 2 — aplicar os juros contados da data da atualização do último cálculo até a data da dedução
> **apenas sobre o principal corrigido apurado na letra "B"**;
> 3 — O valor encontrado no item 02 deverá ser somado ao valor apurado no item 01 para obter o
> total de juros até a data da dedução.

### 2.1 Em que difere do rateio: em nada que chegue lá

**A decomposição é descartada.** Os dois componentes — juros pretéritos corrigidos e juros
novos — são somados num único `C` pela letra D, e o rateio usa apenas `C / D`. A distinção
que os três passos produzem **não sobrevive à letra seguinte**.

### 2.2 Os exemplos usam, provado pela aritmética

- **Ex. 5:** `60.162,49 × 1,0153923 = 61.088,53` (passo 1) e `72.119,61 × 0,15833330 =
  11.418,94` (passo 2, sobre o **principal corrigido**, como manda o texto).
- **Ex. 6:** `251,02 × 1,00196157 = 251,51`; e `164,24` só sai de `11.731,57 × 1,40%`.

### 2.3 Mas a obrigatoriedade não tem lastro em lugar nenhum

**O manual declara a regra e não a razão.** Buscas nas pp. 266–277: `obrigatór*` → **0**,
`porque` → **0**, `razão` → **0**. A palavra só existe nas pp. 237 e 239, onde a regra é
enunciada.

Pior: **o par não demonstra a obrigatoriedade.** Algebricamente os dois critérios coincidem
quando `p_total − p2 = J0/P0`. Nenhum dos dois exemplos informa data de ajuizamento ou
percentual acumulado — o **critério 1 é inexecutável a partir do publicado**. Sob a única
reconstrução possível os dois dão **delta 0,00** (Ex. 5: `C = 72.507,47` pelos dois; Ex. 6:
`C = 415,75` pelos dois).

> **A hipótese que a moldura declara obrigatória não tem, em todo o capítulo 10, um único
> exemplo que demonstre por que o outro critério falharia.** Pendência **P10D-04**.

E há um agravante de rotulagem: **os `251,02` que o Ex. 6 chama de "juros vincendos" são,
pela própria planilha, juros vencidos até 31/03/16.** Não há sobreposição com o período
residual — logo o exemplo dos vincendos não exercita vincendos no sentido do capítulo 7.

---

## 3. Vincendos e rateio

**Os vincendos entram no bruto ANTES do rateio.** Ex. 6:

```
415,75 × 6.910,41 / 12.147,12 = 236,52   → juros tratados como quitados (56,89%)
remanescente de juros                      179,23
236,52 + 179,23 = 415,75 = C               ✓
```

**Consequência:** o pagamento parcial quita **56,89% de juros que ainda não venceram**. A
moldura não discute isso, e é decisão estrutural — um motor que apure os vincendos sobre o
saldo já rateado produz número diferente.

**O rateio continua fechando — exceto num centavo.** Ex. 5 fecha exato
(`52.779,16 + 53.063,01 = 105.842,17`, com dois arredondamentos que se cancelam). **Ex. 6 não
fecha:** `5.057,47 + 179,23 = 5.236,70` contra `5.236,71`; o `G.1` correto é `5.057,48`. O
centavo se perde e o `J` é construído sobre o valor errado.

---

## 4. Art. 12-B contra 12-A

**A string `12-B` não ocorre nenhuma vez nas pp. 266–277.** (No manual inteiro: pp. 6, 185,
186, 190, 191, 193, 203, 207, 224, 233, 240.) `12-A` ocorre 4 vezes no segmento. **O
enquadramento no 12-B é paráfrase do extrator do manual, não rótulo do texto.**

**Sob o 12-B não há NM.** Literal, `pagina_pdf` 190: *"sem qualquer multiplicação pelos
números de meses"*. Código de recolhimento **5936**.

**O esquema de dois NM do segmento C não se mantém:**

| | Regime | NM |
|---|---|---|
| **Ex. 6** | 12-B puro | **nenhum NM apurado** |
| **Ex. 5** | **híbrido** | levantamento (25/10/11) pelo regime geral; saldo migrado para **12-A** por causa de 11/03/15 — NMP 17,2 (auxiliar) e NM do saldo 46,8, cód. 1889 |

**O Exemplo 5 é o único do manual que executa a migração de regime tributário dentro de um
mesmo cálculo.** É conteúdo estrutural que só existe nele.

---

## 5. A amplitude tem fórmula fechada

O bloco 11B mediu 23,83% no Exemplo 1 e 0,25% no exemplo curto, e eu descrevi a escala como
"tempo residual × participação dos juros no bruto". **Está incompleta.** A forma correta,
verificada nos quatro casos:

```
amplitude = min(abatimento, B, C) × índice_residual × percentual_juros_residual
```

| Caso | `min(...)` | Amplitude calculada | Reportada |
|---|---|---|---|
| EXEMPLO de 10.3.1 | 3.223,76 | **36,60** | 36,60 |
| Exemplo 1 | 17.272,58 | **9.919,52** | 9.918,92 |
| Exemplo 5 | 38.784,90 | **22.272,55** | 22.272,55 |

Reproduzida por mim, independentemente.

### 5.1 O que a fórmula revela

| Exemplo | Juros/bruto | Amplitude R$ | Amplitude % |
|---|---|---|---|
| Exemplo 1 | 26,92% | 9.918,92 | **23,83%** |
| **Exemplo 5** | **50,13%** | **22.272,55** | **15,85%** |
| Exemplo 6 | 3,42% | 2,51 | 0,05% |

**O Exemplo 5 tem participação de juros quase o dobro da do Exemplo 1 e amplitude percentual
MENOR** — porque ali o fator limitante é o **abatimento**, não os juros. Em valor absoluto é
2,25× maior.

**É por isso que a formulação por "participação dos juros" enganava:** o termo que limita é o
mínimo entre três grandezas, e qual delas manda varia de caso para caso.

Ex. 5, ordens alternativas: juros primeiro **+7,91%**, principal primeiro **−7,95%**.

---

## 6. R23 — observada, e com fundamento em lugar inesperado

**O segmento D observa o "descarregar" integralmente**, inclusive com vincendos:

- **Ex. 5:** juros residuais sobre **54.940,54**, não sobre 138.448,90 — a diferença seria
  **+30.452,43**;
- **Ex. 6:** sobre 5.061,90, não sobre 5.241,29 — **+1,08**.

### 6.1 São duas regras anti-anatocismo distintas

| Regra | Onde | Operação |
|---|---|---|
| **1** | `pagina_pdf` **16** | juros acumulam por **soma** de percentuais, nunca por multiplicação |
| **2** | `pagina_pdf` **237** | **"descarregar"** — excluir do saldo os juros nele contidos antes de aplicar juros novos |

A **Súmula 121 do STF** é invocada **uma única vez em todo o manual**, na p. 16, e **só para a
regra 1**:

> "a multiplicação dos percentuais caracterizaria anatocismo (incidência de juros sobre
> juros), vedado pela **Súmula 121 do STF**. O mesmo ocorre com os juros aplicáveis aos
> débitos trabalhistas."

### 6.2 O fundamento da regra 2 está numa minuta do capítulo 16

`anatocismo` → **0 ocorrências** no segmento D; `Súmula 121` → **0**. A palavra ocorre nas
pp. 16, 90, 328 e 335 — **nenhuma no capítulo 10**.

Mas a **p. 328 conecta explicitamente** as duas coisas, ao descrever a operação do
"descarregar":

> "tomou como base o valor do principal bruto devido ao reclamante sem juros de mora,
> atualizando o mesmo até (...) e recalculando os juros de mora desde a inicial, **não
> incidindo juros sobre juros (anatocismo)**"

**É uma minuta de petição — item 16.4 — não o capítulo técnico.** O capítulo que *executa* a
operação nunca a nomeia nem a fundamenta; quem a explica é o modelo de ofício.

**Isto repete, com outro assunto, o achado central do bloco 11B:** a regra mais consequente é
praticada sem que o capítulo que a pratica declare seu fundamento. Reforça a decisão de
tratar o capítulo 16 como fonte normativa, não como formulário (pendência **P10-C16**).

---

## 7. BLOQUEIO — P10D-01

`pagina_pdf` 269 e 271, Exemplo 5, **letra I**. Maior que o do bloco 11B.

```
53.063,01 × 1,04095137 = 55.236,01      impresso: 53.199,50      delta 2.036,51
índice implícito: 1,00257222  — não corresponde a nenhum índice do exemplo
```

**Não é cópia de outro exemplo:** `53.199,50` ocorre **apenas nas pp. 269 e 271**, e
`55.236,01` **não existe em nenhuma página do manual** — conferido nas 471.

**Propaga por toda a cadeia final:**

| | Impresso | Coerente |
|---|---|---|
| J | 138.448,90 | 140.485,41 |
| IR | 4.162,83 | 4.468,30 |
| **TOTAL** | **154.874,90** | **156.911,41** |

**Não contornado.** Verificado por mim, além do extrator.

---

## 8. As pendências do 11B

| # | Estado no segmento D |
|---|---|
| **P11B-02** arredondamento do NMP | **Reaparece e piora.** `17,16303 → 17,2`, e aqui nem a nota *"( * ) Observada a regra de arredondamento"* existe: `arredond*` → **0** |
| **P11B-03** percentual pleno × `0,9091` | **Não reaparece como divergência** (IPIR = 100% nos dois) — mas reaparece como **resíduo**: a p. 267 imprime `(50.799,50 / 55.881,51) 100%`, operandos do **Exemplo 1**, cujo quociente é 0,90905 |
| **P11B-04** base de IR do saldo | **Reaparece, agora com causa declarada:** Ex. 5 com juros, Ex. 6 sem (OJ 400). A divergência é **instanciada, não resolvida** |
| **P11B-05** gross-up invertido | **Não reaparece** — fecha exato nos dois. Sobra tipografia: p. 268 grafa "NSS" e omite parênteses do denominador |

---

## 9. Fase 4 — o segmento D produz os dois extremos

`ADC` → 0, `IPCA` → 0, `EC 113` → 0 no segmento, como esperado de um texto de 2016.

O bloco 11B identificou o maior atrito do projeto: o rateio distribui o pagamento entre juros
calculados por TR + 1%, e recalculados pela ADC 58 a proporção muda. **O segmento D agrava e
atenua ao mesmo tempo**, porque contém os dois extremos do capítulo:

| Exemplo | Juros / bruto | Sensibilidade do total a ±20% em `C` |
|---|---|---|
| **Ex. 5** | **50,13%** — o maior do capítulo | **2,40%** |
| Exemplo 1 | 26,92% | — |
| **Ex. 6** | **3,42%** — o menor | **0,004%** |

**Cerca de 600× de diferença de sensibilidade entre os dois exemplos do mesmo segmento.**

**E há um atrito adicional, estrutural:** sob **Selic** pós-citação, a distinção entre
principal e juros — que é o que sustenta tanto o rateio quanto o critério alternativo da
letra C — **deixa de existir**. Não é que o número mude: é que a operação perde objeto.

Marcado, não harmonizado.

---

## 10. Defeitos do original

Catorze catalogados. Os que repetem padrões conhecidos:

- **DEF-04 — linha copiada de outro exemplo** (p. 267), do Exemplo 1. Mesmo padrão das
  pp. 223 e 254.
- **DEF-03 — o mesmo principal impresso como `11.731,57` e `11.731,37` na mesma p. 276.** O
  correto é 11.731,37, e **a letra B, onde ele é calculado, imprime o errado**.
- **DEF-09 — o título do Ex. 6 é cópia literal do Ex. 5**, contradizendo seu próprio parâmetro.
- **DEF-05 — o Ex. 5 tem duas letras D, duas E, duas G e duas H** (pp. 267–268); o Ex. 6
  resolve o mesmo trecho com itens numerados.
- **DEF-07 — IR do saldo do Ex. 6:** a letra L imprime 380,76 (correto); M, N e o resumo
  imprimem 380,77 — **e é o errado que fecha o total**.
- Mais: cabeçalhos deslocados, rótulo contradizendo a própria coluna, "item 10" inexistente,
  "item c" órfão, "Lei 77713/88".

---

## 11. Pendências

| # | Pendência |
|---|---|
| **P10D-01** | **BLOQUEIO** — Ex. 5 letra I, delta 2.036,51, índice implícito sem origem; propaga ao total (154.874,90 → 156.911,41) |
| **P10D-02** | Centavo perdido no rateio do Ex. 6 (`5.057,47` onde o correto é `5.057,48`); o `J` é construído sobre o valor errado |
| **P10D-03** | `11.731,57` × `11.731,37` na mesma página, com a letra B imprimindo o errado |
| **P10D-04** | **A obrigatoriedade do critério alternativo da letra C não tem lastro demonstrativo em todo o manual.** O critério 1 é inexecutável a partir do publicado |
| **P10D-05** | A alternativa da **letra I** não tem exemplo em lugar nenhum do capítulo 10 |
| **P10D-06** | Os `251,02` rotulados "juros vincendos" no Ex. 6 são juros **vencidos** — o exemplo dos vincendos não exercita vincendos |
| **P10D-07** | Enquadramento no art. 12-B é paráfrase: a string não ocorre no segmento |
| **P10D-08** | Migração de regime tributário dentro do mesmo cálculo (Ex. 5) — único caso do manual, sem enunciado que a discipline |
