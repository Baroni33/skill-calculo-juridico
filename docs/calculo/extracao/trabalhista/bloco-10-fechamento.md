# Bloco 10 — fechamento da extração trabalhista

Manual TRT-3: item 7.6 residual (juros vincendos), capítulos 11, 13, 15 e 17.
Detalhe em `bloco-10-fechamento-detalhe.md`. Índice do cap. 17 em
`../../jurisprudencia-indice.md`. Mapa de cobertura em `../mapa-de-cobertura.md`.

**Offset de paginação: zero.** Número impresso = página do PDF.

---

## 1. A numeração do enunciado não existe no manual

Conferida antes de extrair, como pedido. Quatro divergências, todas verificadas por
varredura e nenhuma cosmética:

| Enunciado | Realidade conferida |
|---|---|
| "13 — Diferenças salariais" | **Diferenças salariais é o item 6.15**, coberto pelo bloco 4. O capítulo 13 é *Atualização de créditos da dívida ativa da União*, e tem **uma página** |
| "15 — o que houver entre 6.15 e o capítulo 16" | Entre 6.15 e o cap. 16 estão os **capítulos 7 a 14 inteiros**. O cap. 15 é *Comandos facilitadores* |
| "item 7.6.1, pp. 95-98" | **Não existe item 7.6.1.** Juros vincendos é **subtítulo não numerado** dentro de 7.6, e vai até a p. **99** |
| itens "15.2 / 15.4 / 15.5" | **Não existem.** O cap. 15 é lista simples de **1 a 8**, sem prefixo. Buscas: `15.\d` nas pp. 307–309 → **zero ocorrências** |

**Uma quinta divergência é de minha própria autoria, e vai registrada como tal.** Ao
instruir a extração do cap. 15, escrevi que o item 2 tratava da "multa do art. 477",
inferindo de uma linha truncada do sumário. **É o art. 467**: a sequência `477` não ocorre
**nenhuma vez** nas pp. 307–309, contra três ocorrências de `467`. Mesma classe do "o manual
NÃO segmenta" do bloco 9 — desta vez apanhada antes de virar artefato.

**O capítulo 13 não consta do sumário.** A p. 6 salta de `12.4 ... 301` direto para
`14 - PRECATÓRIOS ... 304`. Achado do original, não corrigido.

---

## 2. Juros vincendos (item 7.6, subtítulo não numerado, pp. 95–99)

Método, não mapa. Entra na espinha.

**Conceito.** Juros vincendos, decrescentes e regressivos são sinônimos: incidem sobre
parcelas de época própria **posterior** ao ajuizamento. O passo do decréscimo mensal é a
própria taxa de juros do período; no mês do ajuizamento o decréscimo é **proporcional**.

**Mês comercial de 30 dias, aplicado explicitamente** — `"1/30 x 6 dias"`, `"0,5% / 30 x 5
dias"`. Confirma e reforça o achado do bloco 9.

**Três critérios de atualização de cálculo homologado que já contempla juros vincendos**
(p. 98) — extraídos literais no detalhe.

### 2.1 Aritmética refeita em `Decimal`

| Exemplo | Resultado |
|---|---|
| Ex. 2 (Fazenda, 26/04/12→31/05/16) | **reproduz 100%** — `0,5%×49 + 0,5%×5/30 − 0,9240% = 23,65933%`. Os 15 degraus de jun/12–ago/13 e os 34 de 0,5% fecham exatos |
| Três critérios (p. 98) | **reproduzem centavo a centavo** — `6.723,13×1,03828066=6.980,50`; `461,13×1,03828066=478,78`; `6.980,50×52%=3.629,86`; total `11.089,14` |
| Ex. 1 | **um erro no original** — ver abaixo |

**DEFEITO DO ORIGINAL — índice de dez/10 (p. 96).** O índice impresso `1,012012029`
aplicado a 309,75 dá **313,47**; o manual imprime **313,76**. O índice implícito é
`1,012945924`, e cruzando com a p. 98 (`1,051730038 ÷ 1,038280657`) o correto seria
`1,012953512`. O índice impresso **ainda quebra a monotonicidade** da série — é menor que o
de jan/11. O somatório do manual fecha com o índice implícito: **o erro está no índice
impresso, não no valor.** Não corrigido.

**Tolerância de 4 centavos.** O manual afirma que refazer mês a mês dá "o mesmo resultado";
a conferência fecha em **11.089,18 contra 11.089,14**. Causa em § 4.1.

**Confronto com o já extraído:** nenhuma divergência. Os decréscimos batem com a tabela
jun/12–ago/13 da p. 92 e o 0,9240% é o mesmo.

---

## 3. Capítulo 13 — Dívida ativa da União (p. 303)

Uma página. **Índice:** Selic acumulada mensalmente até o último dia do mês anterior, **+
1% no mês do pagamento** (arts. 13 e 18 da Lei 9.065/95; art. 61, §§, da Lei 9.430/96).
**Encargo legal de 20%** (DL 1.025/69, art. 1º; Lei 8.383/91, art. 57, § 2º) — o manual diz
que os créditos "podem sofrer" o encargo, **sem dar a hipótese de incidência**. Cálculo
delegado ao site da PGFN; formalização pelo Provimento 04/00.

**Termo inicial: não existe no capítulo.** Busca que sustenta a negativa: varredura da
p. 303 — única página do capítulo — sem qualquer termo inicial declarado. Pendência
**P10-13**.

---

## 4. Capítulo 11 — sete exemplos, e as regras que só vivem neles

**São sete exemplos, numerados 1, 2, 4, 5, 6, 7, 8. Não existe "Exemplo 3".** Busca que
sustenta: `Exemplo 3` nas 471 páginas → apenas pp. 134, 156, 161 e 255, todas de capítulos
anteriores; `EXEMPLO 3` → zero.

Toda a aritmética dos sete foi refeita em `Decimal` com `ROUND_HALF_UP`. **Dezessete
achados estruturais**, vinte incidentais. Os que mudam o motor:

### 4.1 Precisão plena, e nenhuma regra de arredondamento no manual

**Os números impressos com duas casas não são os operandos.** Provado em três exemplos
independentes: Ex. 2 (`15,54+3,88 = 19,42` impresso, manual **19,43** — só fecha partindo de
`724/30×14` sem arredondar), Ex. 4 (`49,64+9,55+5,56 = 64,75`, manual **64,74**), Ex. 5.

**Nenhuma regra de arredondamento monetário existe no manual.** Busca que sustenta:
`arredond` nas 471 páginas → 5 ocorrências (pp. 226, 230, 243, 250, 257), **todas** sobre o
número de meses do RRA; `casas decimais` → **zero**; `truncad` → **zero**; `centavo` → só a
p. 99, sobre paridades históricas.

**Consequência medida: as colunas impressas não somam os totais impressos** (Ex. 2:
3.919,51 contra 3.919,48; 269,57 contra 269,59). É a origem da tolerância de centavos que
aparece em todo o manual. **Regra estrutural para o motor: encadear em precisão plena e
arredondar só na apresentação.**

### 4.2 Mês comercial de 30 dias, contado do dia da admissão

`17/02/2014` conta **14 dias** — fevereiro real teria 12. `724/30×14 = 337,87` ✓. Idem
11/09 → 20 dias, rescisão em 22/09 → 22 dias. Buscas: `mês comercial` → **zero**;
`30 avos` → **zero**. A regra existe, o enunciado não.

### 4.3 Acordo — quatro regras, duas delas contraditórias entre si

- **Correção e juros do dia seguinte ao vencimento da parcela inadimplida**, e juros sobre
  **principal + multa** (Ex. 6: 16/03/16 para parcela vencida em 15/03). A p. 84 descreve
  isso como a **"4ª corrente"** histórica e conclui que *"Atualmente a aplicação dos índices
  de correção monetária ocorre na forma da Súmula nº 381 do TST"*. **Os exemplos aplicam a
  corrente que o texto declara superada.**
- **Base do INSS é o valor original**, sem multa, juros nem correção (Ex. 7: INSS sobre
  12.300,00 quando o devido já era 25.051,50).
- **Ex. 6 e Ex. 7 aplicam a multa do acordo sobre bases opostas** — Ex. 6 sobre o valor
  **original** da parcela, Ex. 7 sobre o **já corrigido**. Exemplos consecutivos, critérios
  inversos, sem nota que explique.

### 4.4 Bases de cálculo que o rótulo contradiz

- **Multa do art. 467 (Ex. 1):** a base inclui saldo de salário **e a multa de 40% sobre o
  FGTS rescisório**, nenhum dos dois no rótulo. Reproduzido exatamente: `11.823,07 × 50% =
  5.911,54` ✓. A base do rótulo daria 5.083,50.
- **Aviso prévio indenizado entra na base do INSS e sai da base do IR** (Ex. 1) — enunciado
  na p. 76, confirmado numericamente.
- **Ex. 4 soma os juros à base do IR; Ex. 1, 2, 5 e 8 os excluem.** Enunciado na p. 182,
  mas com atrito: o Ex. 4 é rescisório, hipótese em que a mesma p. 182 manda excluir.
  **Cruza com o item 5 do capítulo 15** — ver § 5.2.
- **Custas de execução:** a base do cap. 11 **diverge da do cap. 9**. O cap. 9 (p. 132) dá
  `"(Vr. Bruto do recte + INSS recda) x 0,5%"`; o cap. 11 usa líquido do reclamante + INSS
  do reclamante + INSS da reclamada. No Ex. 1 a diferença é 151,39 contra 151,56. E dentro
  da mesma base, **o crédito entra líquido e os honorários entram brutos** (Ex. 2).

### 4.5 DEFEITO DO ORIGINAL — o FGTS conta os juros duas vezes (Ex. 8)

O achado de maior impacto do capítulo.

```
Principal  - FGTS a depositar  12.824,00 × 1,01087868 = 12.963,51
Valor juros - FGTS a depositar  3.761,71 × 1,01087868 =  3.802,63
Juros s/ o principal - FGTS    12.963,51 × 36,333333% =  4.710,07
Total FGTS a depositar                                  21.476,22   ← manual
```

Os **36,333333% já contêm** os 29,333333% de juros até out/15 (`3.761,71 / 12.824,00`) mais
7%. Por qualquer dos dois métodos coerentes o total é **17.673,59**. **Excesso: 3.802,63** —
a linha de juros entra duas vezes. Na **mesma página**, o crédito principal usa corretamente
apenas duas linhas. Propaga para o resumo e para o total de 292.265,29.

**Não corrigido.** Registrado como defeito do original.

### 4.6 Outros dois defeitos com efeito de valor

- **Ex. 1: o índice de correção incide duas vezes sobre o INSS deduzido do crédito.**
  `457,38 × 1,016526834² = 472,62` e `95,04 × 1,016526834² = 98,21`, somando os 570,83
  deduzidos — mas o INSS efetivamente recolhido parte de 552,42. Uma única incidência daria
  561,55. **Ex. 2 e Ex. 5 aplicam o índice uma só vez.**
- **Ex. 6: o resumo geral retira a multa previdenciária que o demonstrativo da mesma página
  incluiu** (991,50 → 843,24; 2.461,49 → 2.093,49). O total usa o resumo. E a base de custas
  declarada (16.328,35) não corresponde a nenhuma das duas versões.

---

## 5. Capítulo 15 — oito parâmetros que o manual reconhece indeterminados

Não são regras de cálculo autoexecutáveis. O manual declara o propósito (p. 307):

> "Alguns equívocos cometidos nos cálculos trabalhistas e nas atualizações de débitos,
> decorrentes de uma interpretação incorreta de um comando judicial ou de um texto legal,
> poderiam ser evitados se alguns parâmetros fossem fixados previamente pelas decisões na
> fase de conhecimento, atas de acordo ou por despachos."

**É um catálogo de subdeterminação declarada pela própria fonte** — e mapeia direto na
camada de presets do bloco 6. O item **1** apresenta **três variantes da base da multa do
acordo sem eleger nenhuma**: estrutura `variantes com fundamento, sem default`.

### 5.1 Os dois que não são preset

- **Item 7 — regra supletiva expressa, vai para a espinha.** Se o acordo não discrimina as
  verbas, os valores e o período, **o IR incide sobre o total da avença**, observadas base e
  alíquotas dos meses de pagamento. Havendo discriminação, o valor pode cair na faixa de
  isenção pelo art. 12-A. Fundamento: art. 12-A da Lei 7.713/88 e IN RFB.
- **Item 8 — caso de R20-EXCEÇÃO.** Sem teto fixado para a multa diária, *"o calculista não
  tem parâmetro para determinar o valor da obrigação principal e a apuração fica
  impossibilitada até novas diretrizes"*. **O manual proíbe resolver por default.**

### 5.2 Item 5 — juros na base do IR, divergência não resolvida

| Corrente | Fundamento |
|---|---|
| **Não** integram | **OJ 400 da SDI-1/TST** |
| **Integram** | ausência de previsão legal de isenção — Acórdão DRJ/Curitiba nº 06-31148, de 12/04/2011, transcrito nas pp. 308–309 |

**Não resolvida.** O critério prático do manual — seguir o pronunciamento judicial nos autos
— é registrado como **desempate prático, não jurídico**. Cruza com o § 4.4 (Ex. 4 soma, os
demais excluem) e com o cap. 9. Pendência **P10-15**.

### 5.3 Item 4 — a única outra regra determinada

Deduz-se do crédito do reclamante **apenas a contribuição atualizada**; juros Selic e multa
são ônus do reclamado (art. 33, § 5º, da Lei 8.212/91). A multa previdenciária é declarada
como "10% ou 20%" **sem critério de escolha** — pendência **P10-14**.

---

## 6. Capítulo 17 — 158 verbetes, e o número que importa

Índice completo em `../../jurisprudencia-indice.md`.

| Seção | Espécie | Nº |
|---|---|---|
| 17.1 | Súmulas TST | 87 |
| 17.2 | OJs SDI-1/TST | 38 |
| 17.3 | OJs Pleno/TST | 3 |
| 17.4 | OJs Transitória/TST | 5 |
| 17.5 | Súmulas TRT-3 | 15 |
| 17.6 | OJs Turmas TRT-3 | 3 |
| 17.7 | TJPs TRT-3 | 2 |
| 17.8 | Provimentos | 4 |
| 17.9 | Parecer Normativo | 1 |
| | **total** | **158** |

> **A base normativa do repositório cobre 12 dos 158 — 7,6%.**

Não é falha desta extração: `00-base-normativa.md` § 10 e `bloco-07-relatorio.md` § 9 já
declaram a lacuna. **O índice torna a lacuna contável.** Regra dura aplicada: **nenhum
verbete marcado `vigente` por omissão** — 146 ficaram `não coberto`.

O manual **desenvolve** 96 verbetes e apenas **cita** 62.

### 6.1 Os quatro casos de conferência do método

Os quatro foram reproduzidos pelo procedimento **sozinho**, sem consulta externa.

| Caso | Resultado |
|---|---|
| **OJ 394 da SDI-1** | **Bateu** — `superado`. Agravante: é o verbete **mais desenvolvido do manual em matéria de reflexos** (pp. 35, 44, 45, 48, 286, 291, com exemplos numéricos). Todo esse trecho está invertido para HE a partir de 20/03/2023 |
| **Súmula 124 do TST** | **Bateu** — `alterado`. O manual traz a redação da Res. 185/2012 e **antecipava** a revisão: pp. 37–39 transcrevem o IRR-849 e recomendam acompanhar |
| **Súmula 228 do TST** | **Bateu** — `cancelado`. O manual imprime *"EFICÁCIA SUSPENSA POR DECISÃO LIMINAR"* (Rcl 6.266, julho/08); a base registra a cassação definitiva na Rcl 6.275, abril/2018 |
| **Súmula 48 do TRT-3** | **Não existe no manual.** Varredura das 471 páginas: `Súmula 48` → **zero ocorrências**. Os dois `48` que aparecem (pp. 339 e 346) são `ex-OJ 48` dentro de súmula do TST. **Fecha a pendência 2 de `02a` § 19** |

### 6.2 Divergência interna do manual — OJ 47 da SDI-1

O mesmo verbete, **duas redações**, sem que o manual sinalize:

| p. 350 | p. 354 |
|---|---|
| "É o resultado da soma do salário contratual mais o adicional de insalubridade, **este calculado sobre o salário-mínimo**" | "A base de cálculo da hora extra é o resultado da soma do salário contratual mais o adicional de insalubridade" *(Res. 148/2008)* — **sem** a cláusula final |

Muda a base de cálculo da hora extra. **Não resolvida.** Pendência **P10-16**.

### 6.3 O que o capítulo 17 tem além de jurisprudência

- **Provimento 04/00** é **especificação de contrato de saída do motor**: MEMÓRIA com oito
  itens ordenados (art. 1º, § 1º, I–VIII) e RESUMO com onze rubricas nominadas `a` a `k`. O
  manual a usa em dezenove páginas de exemplos.
- **Provimento Geral Consolidado (2015)** reincorpora os três anteriores e, no **art. 106,
  § 3º**, fecha o círculo: *"Os cálculos deverão observar, ainda, o disposto no Manual de
  Cálculo deste Egrégio Tribunal"*. Traz valores datados de 2015 — dispensa de intimação da
  União até R$ 20.000,00; RPV de 60 salários mínimos, 4.723 Ufemgs, 30 salários mínimos.
- **Parecer Normativo COSIT nº 25/2013** (pp. 369–372) **é o anexo a que o item 9.2.10
  remete sem indicar onde** — fecha a pendência **P7-11**. Acrescenta ao cap. 9 a mecânica
  do **regime misto** e a regra do **13º salário**, e confirma que o **RAT/SAT sobrevive
  sempre**, sem redução, em qualquer regime. Tudo sob a marca **F7-02**: a lista de setores
  está materialmente superada pelas Leis 13.670/2018, 14.784/2023 e 14.973/2024; **a
  mecânica sobrevive, a lista não**.

---

## 7. Verificação de citação literal

158 ementas confrontadas por script contra o PDF, normalizando NFKC, aspas tipográficas,
travessões, espaços e folios.

| Resultado | Nº |
|---|---|
| LITERAL-OK | **150** |
| literal, atravessa fronteira de folha | 3 |
| **NÃO LOCALIZADA** | **1** |
| sem ementa própria (Provimentos) | 4 |

**Dez atribuições de página estavam erradas** e foram corrigidas pela própria verificação —
o script localizou onde o texto de fato está. O padrão é deslocamento de uma folha, exceto
a Súmula 199 (declarava 339, está na 346) e a Súmula 401 (declarava 340, está na 341 e 347).

**A não localizada é a OJ 397 da SDI-1.** A ementa gravada não foi encontrada no PDF na
forma registrada; a p. 351 traz outro verbete no ponto declarado. Pendência **P10-17**.

---

## 8. Pendências do bloco

| # | Pendência |
|---|---|
| **P10-11** | Ex. 8 do cap. 11 — FGTS com juros em dobro (excesso de 3.802,63) e propagação ao total |
| **P10-12** | Cap. 11 — critérios opostos de base da multa em acordos consecutivos (Ex. 6 × Ex. 7) |
| **P10-13** | Cap. 13 — termo inicial ausente; hipótese de incidência do encargo de 20% não declarada |
| **P10-14** | Cap. 15, item 4 — multa previdenciária "10% ou 20%" sem critério de escolha |
| **P10-15** | Cap. 15, item 5 — juros na base do IR: duas correntes, não resolvida |
| **P10-16** | Cap. 17 — OJ 47 da SDI-1 com duas redações divergentes no mesmo manual |
| **P10-17** | Cap. 17 — ementa da OJ 397 não localizada no PDF na forma gravada |
| **P10-18** | Custas de execução: base do cap. 11 diverge da do cap. 9 |
| **P10-19** | Súmula 191 do TST — a base invoca o item II, mas o manual imprime a redação antiga, sem itens |
| **P10-20** | Dezenove verbetes citados no corpo e **ausentes** do cap. 17, incluindo a Súmula 38 do TRT-3, fundamento do divisor 180 em turnos |
| **P10-C16** | Capítulo 16 — varredura dirigida; confirmado que enuncia regra de cálculo |
