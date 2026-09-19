# Bloco 2 — relatório

Manual de Cálculos do TRT-3, julho/2016. Páginas **9 a 17** do PDF, mais o item 6.1
(p. 18). Fase 2 do pipeline, tipo *prosa e raciocínio*: validação **adversarial**, não
determinística (`01-plano-extracao.md`, Fase 2).

Nenhuma skill escrita.

| | |
|---|---|
| Espinha | `bloco-02-criterios.md` |
| Detalhe | `bloco-02-criterios-detalhe.md` |
| Escopo coberto | itens 1, 3, 4, 5.1, 5.2, 5.3 — e 6.1, para a URV |
| Fora de escopo, não extraído | item 2 (p. 10), bibliografia |

---

## 1. O que saiu

**Espinha.** Princípios que restringem a liquidação; competências e a cadeia de quem
elabora a conta; conceito, natureza e as três modalidades de liquidação; os sete elementos
do cálculo; composição obrigatória de memória e resumo geral; nove regras matemáticas, em
fórmula; conversão da URV.

**Detalhe.** Onze exemplos do manual, literais, cada um reconferido com `Decimal` em
precisão 30. A conferência serviu para separar arredondamento declarado de erro de
digitação — não para corrigir nada.

Todas as fórmulas pedidas no escopo saíram como fórmula:

```
i = p / 100 + 1                          percentual → número índice
p = (i - 1) × 100                        número índice → percentual
i_acum = i₁ × i₂ × … × iₙ                acumulação de correção
i_res = i₁ / i₂                          subtração de percentuais
taxa_acum = Σ tₘ                         SELIC e juros trabalhistas
h_cent = H + M / 60                      hora sexagesimal → centesimal
semanas = 30 / 7 = 4,285714              constante do manual, truncada
valor_mensal = valor_semanal × 4,285714  desde que fixo em todas as semanas
valor_CR$ = valor_URV × URV(dia_do_pagamento)
```

---

## 2. Validação adversarial

Dois revisores independentes, sem o contexto desta extração, com lentes distintas:

| Revisor | Pergunta | Achados |
|---|---|---|
| A | Que regra do original ficou de fora? | 5 relevantes, 11 menores |
| B | Que afirmação da espinha não tem respaldo? | 2 graves, 9 menores |

Método: cada um recebeu o texto bruto das páginas, os dois arquivos da extração, e
instrução para não sugerir correções — só apontar. Nenhum dos dois viu o trabalho do outro.

O revisor B conferiu também a aritmética do detalhe: os onze exemplos fecham.

### 2.1 Achados aceitos e corrigidos

**Graves (revisor B):**

| # | Achado | O que foi feito |
|---|---|---|
| B1 | A espinha enunciava "taxa que é juros acumula por soma; índice que é correção monetária acumula por produto" — **regra categórica de minha autoria**, que o manual não enuncia e que erra, por exemplo, na SELIC do art. 3º da EC 113/2021 (engloba correção **e** juros, e acumula por soma) | Removida. Substituída por uma advertência explícita de que o manual enuncia outro critério: **o regime de acumulação vem da lei que institui a taxa** |
| B2 | O método de conversão CR$ → URV de 1994 era atribuído ao manual com citação de página não verificável pelo revisor | Mantido — a fonte existe —, agora com **citação literal** da p. 81, conferível |

**Relevantes (revisor A), todos incorporados à seção 2 da espinha:**

| # | Omissão | Por que importa |
|---|---|---|
| A1 | Art. 104, § 5º, do Provimento Geral Consolidado, inteiro | Único ponto do bloco que menciona **precatório/RPV** e cria a etapa de **conferência da conta**, distinta da elaboração |
| A2 | Art. 105, VI: "que não puderem ser fixados na Secretaria da Vara do Trabalho" | Transforma a competência sobre encargos processuais de originária em **residual** |
| A3 | Art. 105, IV: "observado o disposto no § 5º do art. 104" | É o elo com A1; sem ele, a hipótese de perícia/partes nas causas contra a Fazenda some |
| A4 | Provimento TRT-SCR 02/00, art. 6º — atermação | Define uma classe de processos em que **a conta já nasce líquida** |
| A5 | Art. 104, § 4º — repartição por localidade e a expressão "em regra" | É o "em regra" que o § 5º excepciona |

**Menores aceitos:** "bom senso" entre os princípios (A7); liquidação como "elo" e o nexo
causal completo da natureza declaratória (A13); o exemplo do jornalista e o passo "articular
por petição" na liquidação por artigos (A14) — o exemplo foi para o **detalhe**, o passo
operacional para a espinha; a condensação das cinco camadas normativas do item 3.1, agora
**declarada** em vez de silenciosa (A8–A12).

**Menores do revisor B, todos aceitos:**

| # | Achado | Correção |
|---|---|---|
| B3 | "A **única** exceção declarada" — o manual diz "faz exceção", sem exclusividade | Trocado por "a exceção declarada", com nota de que o manual não afirma ser a única |
| B4 | "O comando decisório precede o manual" — inferência apresentada como texto | Marcada como *leitura desta extração*, com o texto literal ao lado |
| B5 | Atribuição ao art. 105, IV, de uma conclusão sobre R9 que ele não sustenta | Removida |
| B6 | "É a razão formal da inalterabilidade" — construção minha | Substituída pela citação literal do nexo que o manual faz |
| **B7** | **Proveniência errada**: hora centesimal e semanas do mês estão **inteiras na p. 17**, não em "p. 16–17" | Corrigido em três lugares |
| B8 | "três páginas adiante" onde é uma | Corrigido |
| B9 | C3 aparecia na coluna "Afirmação do manual", mas o manual não enuncia critério de arredondamento algum | Rotulada como resultado **observado nos exemplos**, critério não enunciado |
| B10 | Glosa "não o da competência nem o do fechamento da folha" na data-base da URV | Removida; ficou a citação literal |
| B11 | "capítulo 7, p. 83–99" atribuído ao manual, que não indica páginas | Reatribuído à triagem de `01-plano-extracao.md` |

**B7 é o achado mais importante do lado B**, porque proveniência errada é o único defeito
desta extração que sobreviveria em silêncio: todo o resto é discutível em leitura, aquilo é
simplesmente falso e teria sido copiado adiante.

### 2.2 Achados não aceitos

| # | Achado | Por quê |
|---|---|---|
| A6, A16 | Pré-requisitos de domínio e destinatários do manual (p. 9) | Não têm conteúdo normativo nem operacional; é apresentação |
| A15 | "Peritos judiciais utilizam planilha eletrônica…" (p. 14) | Descrição de prática de escritório, não regra |
| A11 | Finalidade declarada do Prov. 04/00 | A regra e a sanção do Prov. 04/00 estão extraídas; a frase de propósito não acrescenta |
| A12 (parcial) | Art. 105, incisos I, II e VII | Competência interna do tribunal, sem efeito sobre a conta. A condensação está declarada na espinha |

### 2.3 Cobertura confirmada

O revisor A, depois de ler o original linha a linha, registrou que **nada do item 5.3 ficou
de fora**: todas as fórmulas, as constantes (4,285714 e 30/7), os exemplos numéricos, a
observação do índice negativo, os quatro fundamentos legais da SELIC, a Súmula 121 do STF e
o 1,0% do mês do pagamento estão na extração.

O revisor B confirmou fidelidade item a item nos capítulos 1, 3, 4, 5.1, 5.2 e na regra da
URV, e validou as pendências P4 e P5 como contradições reais do original.

O item 5.3 é justamente o que forma o núcleo aritmético de `calculo-judicial-core`. É o
que se queria blindado.

---

## 3. Defeitos do original, registrados e não corrigidos

| # | Onde | Defeito |
|---|---|---|
| 1 | 5.2, p. 14 | A numeração do resumo geral é `1 2 3 4 5 6 7 8 5 6` — os dois últimos itens reiniciam em 5. A espinha renumera de 1 a 10 e **declara a renumeração**; o texto de cada item está literal |
| 2 | 5.3, p. 15 | Na tabela "número índice → percentual", os **rótulos das colunas são os da tabela anterior**, invertidos em relação ao conteúdo |
| 3 | 5.3, p. 15 | **Faltam parênteses**: `1,2 - 1 x 100` pela precedência usual dá −98,8. A operação é `(1,2 - 1) × 100`. O manual acerta os parênteses uma página adiante |
| 4 | 5.3, p. 16 | No exemplo da TR, o parêntese imprime **1,0001608**; o resultado publicado corresponde a **1,000168**. Erro de digitação na memória de cálculo — o resultado está certo |
| 5 | 5.3, p. 16 | O título do mesmo exemplo diz "a **23**/03/2015"; os sub-períodos e o resultado dizem **22**/03/2015 |
| 6 | 5.1 × 5.2, p. 14 | O manual enumera **sete** elementos do art. 106, § 1º e, na página seguinte, refere-se a "incisos **I ao VIII**" |
| 7 | 5.2, p. 14 | Remete às alíneas "**a" a "k**" do art. 106, § 2º — onze — e enumera dez itens |

Os defeitos 6 e 7 não se resolvem dentro do bloco: dependem do texto do Provimento Geral
Consolidado, que não está no manual. Viraram pendências P4 e P5.

---

## 4. Conflitos com a base normativa

Registrados na seção 8 da espinha, não harmonizados. O resumo:

- **C1** — TR acumulando por multiplicação (art. 39 da Lei 8177/91). A TR está superada
  pela ADC 58; a **metodologia de acumulação por produto** continua válida para os índices
  que a substituíram.
- **C2** — juros do art. 39, § 1º, da Lei 8177/91 e do art. 1º-F da Lei 9494/97, por soma.
  Regime superado; o **princípio** — juros simples, soma e não produto — sobrevive e
  coincide com **R4**.
- **C3** — arredondamento. Ver abaixo.
- **C4** — Súmula 211/TST × modulação da ADC 58. Não se contradizem, mas o manual não trata
  da interação.

### C3 é o achado com maior consequência

O Manual CJF **trunca**. O Manual TRT-3 **arredonda** — quatro exemplos deste bloco só
fecham com arredondamento a duas casas e nenhum fecha com truncamento:

| Operação | Exato | TRT-3 | Truncado |
|---|---|---|---|
| 25 / 60 | 0,41666… | **0,42** | 0,41 |
| 10 / 60 | 0,16666… | **0,17** | 0,16 |
| 5 × 4,285714 | 21,428570 | **21,43** | 21,42 |
| 180,00 × 4,285714 | 771,428520 | **771,43** | 771,42 |

R12 exige "critério de truncamento definido e consistente por etapa". A base normativa
tratava isso como decisão de implementação; este bloco mostra que **as duas fontes primárias
divergem no conteúdo**. Um critério global único, seja qual for, contraria uma delas.

Registrado como pendência P3 e adicionado a `pendencias.md`.

---

## 5. A pendência do bloco 1 sobre a URV

`pendencias.md`, § 9, ficou aberta na extração das tabelas: o item 18.10 traz as cotações
diárias e nenhuma palavra sobre como converter.

**Encontrada no item 6.1, página 18** — o escopo deste bloco apontava para lá, e estava
certo:

> "os salários dos recibos de março/94 a junho/94 estão expressos em URV, sendo necessária,
> para o cálculo, a conversão para cruzeiros reais, multiplicando-se a expressão em URV
> pelo valor nominal da URV do dia do pagamento."

Fecha a **direção** (multiplicação) e a **data-base** ("do dia do pagamento"). Não fecha o
**arredondamento**. A pendência passa de aberta a parcial.

Conferência cruzada com a série do bloco 1: o manual registra que "em 01/07/94, uma URV
equivalia a um (01) Real", e o quadro PARIDADES quantifica em "uma URV de CR$-2.750,00 =
1 real". A cotação de 30/06/1994 em `serie-18.10-urv.csv` é **CR$ 2.750,00**. Confere.

---

## 6. Pendências abertas

| # | Pendência | Bloqueia |
|---|---|---|
| P1 | Regra do índice negativo é ambígua: "dividir pelo número índice que apresentou a variação negativa" só reduz se o índice for construído com o valor absoluto. O manual não diz qual construção usar e não dá exemplo | Acumulação de correção em meses de deflação; interage com **R5** |
| P2 | Arredondamento da conversão da URV não declarado | Parcelas de mar/94 a jun/94 |
| P3 | Critério de arredondamento por etapa: as duas fontes primárias divergem, sem árbitro | **Núcleo aritmético de `calculo-judicial-core`** |
| P4 | Sete elementos × "incisos I ao VIII" do art. 106, § 1º | Composição da memória |
| P5 | Dez itens × alíneas "a" a "k" do art. 106, § 2º | Composição do resumo geral |
| P6 | O 1,0% do mês do pagamento (Lei 9430/96, art. 61, § 3º) aparece só no exemplo, para tributos federais; o manual não diz se vale para o débito trabalhista | Juros sobre débito previdenciário em execução trabalhista |

P3 é a que precisa de decisão antes de qualquer código.

P4 e P5 se resolvem lendo o Provimento Geral Consolidado do TRT-3 (PRV GCR/GVCR 3/2015),
que está fora do corpus atual.

---

## 7. O que este bloco não cobre

O manual remete ao tópico "ATUALIZAÇÃO MONETÁRIA E JUROS DE MORA" para a questão dos juros
e da atualização (5.1, p. 14). É o capítulo 7, que a triagem marca como **Fase 4
obrigatória** — materialmente superado pela ADC 58, pela EC 113/2021, pela Lei 14.905/2024
e pela EC 136/2025.

Nada neste bloco estabelece cadeia período → indexador. O que ele dá é o **vocabulário e a
aritmética** sobre os quais essas cadeias operam: o que é principal, correção e juros; o que
a conta tem de conter e de exibir; como índices se acumulam e por que juros não se
multiplicam.
