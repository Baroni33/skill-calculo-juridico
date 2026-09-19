# Bloco 1 — tabelas do Manual TRT-3 (2016), páginas 373 a 471

Fase 2 do pipeline. Conteúdo tabular, extração determinística, validada por script.
Nenhuma skill escrita nesta sessão.

| | |
|---|---|
| Fonte | `manual-de-calculo-trabalhista_2016-1.pdf` (TRT-3, julho/2016, 471 p.) |
| Offset de paginação | 0 — `pagina_pdf` = número impresso (`docs/calculo/fontes.md`) |
| Extrator | `scripts/calculo/extrai_bloco_01.py` |
| Validador | `scripts/calculo/valida_bloco_tabelas.py` |
| Resultado | 15 checagens OK, 31 divergências do original, 1 não verificável, **0 erros de extração** |

```
python scripts/calculo/extrai_bloco_01.py          # reextrai tudo
python scripts/calculo/valida_bloco_tabelas.py     # exit 0 = sem erro de extração
```

---

## 1. O que saiu, e para onde

### (A) Semântica — `docs/calculo/tabelas-normativas/`

Regra estrutural. É o que a skill consome.

| Arquivo | Item | Conteúdo |
|---|---|---|
| `trt3-18.1-incidencia-parcelas.json` | 18.1 | 44 parcelas × INSS/FGTS/IRRF, **com o fundamento legal de cada coluna** |
| `trt3-18.4-18.6-irrf-estrutura.json` | 18.4–18.6 | Estrutura da faixa progressiva com parcela a deduzir; regra do RRA; PLR em tabela própria |
| `trt3-18.7-contribuicao-estrutura.json` | 18.7 | Faixa com teto e sem parcela a deduzir; os dois formatos do original |
| `trt3-18.8-grau-de-risco-estrutura.json` | 18.8 | Grau → alíquota; corte por fato gerador; relação entre 18.8.1 e o Anexo I |
| `trt3-18.10-urv-conversao.json` | 18.10 | O que a tabela contém — e a lacuna: o método de conversão não está no bloco |
| `trt3-18.13-rsr-criterios.json` | 18.13 | Os quatro critérios de contagem, isolados das contagens |

### (B) Série — `docs/calculo/extracao/trabalhista/`

CSV, cabeçalho `OUT_OF_SCOPE`. Manutenção separada (regra 4 de `01-plano-extracao.md`).
Fica como evidência de conferência contra a tabela mantida à parte.

| Arquivo | Item | Linhas | Páginas |
|---|---|---:|---|
| `serie-18.2-salario-minimo.csv` | 18.2 | 145 | 381 |
| `serie-18.2-moedas-e-paridades.csv` | 18.2 | 16 | 381 |
| `serie-18.3-salario-familia.csv` | 18.3 | 94 | 382–384 |
| `serie-18.4-irrf-tabela-progressiva-mensal.csv` | 18.4 | 44 | 385–386 |
| `serie-18.5-irrf-rra.csv` | 18.5 | 30 | 387–388 |
| `serie-18.6-irrf-plr.csv` | 18.6 | 15 | 389 |
| `serie-18.7-contribuicao-matriz-1982-1991.csv` | 18.7 | 218 | 390–391 |
| `serie-18.7-contribuicao-faixas.csv` | 18.7 | 245 | 391–399 |
| `serie-18.8.1-grau-risco-cnae-ate-2007-05.csv` | 18.8.1 | 560 | 400–417 |
| `serie-18.8.2-grau-risco-cnae-desde-2007-06.csv` | 18.8.2 | 1.412 | 418–449 |
| `serie-18.8.2-aliquotas-por-fpas.csv` | — | 35 | 449 |
| `serie-18.9-seguro-desemprego.csv` | 18.9 | 39 | 450–452 |
| `serie-18.10-urv.csv` | 18.10 | 546 | 453–454 |
| `serie-18.11-otn-btn-mvr.csv` | 18.11 | 40 | 455 |
| `serie-18.12-ufir.csv` | 18.12 | 108 | 455 |
| `serie-18.13-rsr-contagens.csv` | 18.13 | 768 | 456–459 |
| `serie-18.14-calendarios.csv` | 18.14 | 5.096 | 460–466 |
| `serie-18.15-tabela-unica-trabalhista.csv` | 18.15 | 126 | 467 |
| `serie-18.15-juros-selic-acumulados.csv` | 18.15 | 528 | 468 |
| `serie-18.15-tabela-pratica-contribuicoes-em-atraso.csv` | 18.15 | 438 | 469–470 |

Total: 10.503 linhas de série + 44 parcelas em JSON. Toda linha com `documento`, `item`
e `pagina_pdf`.

---

## 2. Divergências entre o índice do escopo e o que o manual traz

| Escopo declarado | O que está no PDF |
|---|---|
| 18.8 grau de risco, p. 401–418 | Começa na **p. 400**; 18.8.1 vai de 400 a 417 |
| Anexo I tabelas 1 e 2, p. 419–449 | É o **18.8.2**, e começa na **p. 418**. Tabela 1: 418–447. Tabela 2: 448–449 |
| 18.11 OTN, BTN, MVR, p. 455 | Correto, mas a mesma página traz o **18.12 Ufir**, ausente do escopo |
| 18.15, p. 467–471 | Termina na **p. 470**. A p. 471 é "Equipe de Trabalho", não tabela |
| — | A p. 381 traz dois quadros sem numeração 18.x: **MOEDAS** e **PARIDADES** |
| — | A p. 449 traz um quarto quadro: **Anexo I da IN/RFB 1238/2012**, alíquotas por FPAS |

Os quadros sem numeração foram extraídos em arquivos próprios, marcados como fora do
escopo declarado. Não foram misturados às tabelas numeradas.

**Sobre a "regra dos doze avos" do RRA.** O escopo descreve 18.5 assim. O manual não
diz doze: a legenda da p. 388 define **NM = número de meses a que se refere o pagamento
acumulado**, e os limites de faixa e a parcela a deduzir são multiplicados por NM. O
multiplicador é variável. Gravar 12 como constante diverge da fonte. Registrado em
`trt3-18.4-18.6-irrf-estrutura.json`.

---

## 3. 18.8 e o Anexo I são a mesma tabela? Não.

Conferido antes de extrair, como pedido.

| | 18.8.1 | 18.8.2 (Anexo I, IN/RFB 1027/10) |
|---|---|---|
| Vigência | até 31/05/2007 | a partir de 01/06/2007 |
| Codificação | CNAE 1.0 — `NN.NN-N` | CNAE 2.0 — `NNNN-N/NN` |
| Resultado | grau de risco 1/2/3 | alíquota GILRAT em % |
| Colunas extras | nenhuma | FPAS; GILRAT dividido por fato gerador |
| Linhas | 560 | 1.412 |

Chave diferente, colunas diferentes, vigências que não se sobrepõem. São **normas
sucessivas**, não duas impressões do mesmo arquivo. As duas foram extraídas, em arquivos
separados, e a relação está registrada em `trt3-18.8-grau-de-risco-estrutura.json`.

Dentro do 18.8.2 há um segundo corte: a coluna GILRAT se divide em *fato gerador até
31/12/2009* e *a partir de 01/01/2010* (Dec. 6.957/2009, art. 4º). É o **fato gerador**
que manda, não a data do cálculo nem a do ajuizamento.

---

## 4. Validação determinística

### Contagem contra a camada de texto do PDF

Cada checagem conta, no texto bruto, uma marca que ocorre uma vez por linha de dado, e
compara com o CSV. Caminhos independentes: se batem, nenhum dos dois perdeu linha.

| Tabela | Extraído | No PDF |
|---|---:|---:|
| 18.8.1 atividades | 560 | 560 |
| 18.8.2 códigos CNAE | 1.412 | 1.412 |
| 18.10 cotações da URV | 546 | 546 |
| 18.13 competências de RSR | 768 | 768 |
| 18.15 taxas Selic | 264 | 264 |

18.1 não fecha por contagem e não deveria: 149 segmentos gravados contra 171 ocorrências
de "sim"/"não" no texto, porque a palavra aparece também nas observações em prosa dentro
das células. Registrado como divergência esperada, não como erro.

### Faixas, vigências e proveniência

| Checagem | Resultado |
|---|---|
| Faixas 18.4 | 8 vigências íntegras, 2 com divergência (de 10) |
| Faixas 18.5 | 6 de 6 íntegras |
| Faixas 18.6 | 3 de 3 íntegras |
| Faixas 18.7 | 66 íntegras, 5 com divergência (de 71) |
| Faixas 18.9 | 12 íntegras, 1 com divergência (de 13) |
| Vigências 18.7 | 68 interpretadas, 5 descontinuidades |
| Vigências 18.9 | 13 interpretadas, 0 descontinuidades |
| Vigências 18.3 | 49 interpretadas, 3 descontinuidades |
| Proveniência | 10.547 linhas, todas com documento, item e `pagina_pdf` no intervalo declarado |

O validador separa **erro de extração** de **divergência do original** e só sai com
código não-zero no primeiro. Hoje: zero erros.

Uma nota de método: a checagem de faixas usa `Decimal`, nenhum float (R12). E quando uma
faixa não é legível, a análise daquela vigência é **suspensa** em vez de reportar a
lacuna aparente — o vão seria artefato da leitura, não do original.

---

## 5. Erros do original — registrados, não corrigidos

### 5.1 Dígito a mais ou a menos nos limites de faixa

Todos verificados contra a página. O CSV guarda a string literal do original.

| Item | Página | Impresso | Efeito |
|---|---|---|---|
| 18.4 | 385 | `De 2.2347,86 até 3.130,51` | Lê 22.347,86; abre lacuna de 20.000,01 |
| 18.4 | 386 | `Até 1.1710,78` | Lê 11.710,78; sobrepõe a faixa seguinte |
| 18.7 | 392 | `De 25.924,49 até 43.207.47` | Ponto no lugar da vírgula: 4.320.747 |
| 18.7 | 393 | `De 478.78 até 957,56` | Ponto no lugar da vírgula, duas vezes |
| 18.7 | 393 | `De 337,00 até 478,78` | Deveria abrir em 336,01: lacuna de 1,00 |
| 18.7 | 395 | `De 627,67 até 1.328,25` | Limite herdado do quadro anterior; sobrepõe |
| 18.7 | 398 | `Até 1.1174,86` | Lê 11.174,86; sobrepõe a faixa seguinte |
| 18.9 | 451 | `Até R$ 1.1151,06` | Lê 11.151,06; sobrepõe a faixa seguinte |
| 18.7 | 396 | `De 720,01até 1.200,00` | Falta o espaço antes de "até" (três ocorrências) |

### 5.2 Rótulos de vigência com marcador de nota colado

`04/04/9116` (p. 382) e `Dez/1017` (p. 384): o "16" e o "17" são chamadas de nota de
rodapé grudadas na data. O validador acusa uma lacuna de 1018-01 a 2010-12 por causa
disso. É ruído conhecido do original, não erro de leitura.

### 5.3 Sobreposições reais de vigência

Nem toda sobreposição é erro. Em 18.7:

- **jan/10** — o original traz dois quadros vigentes: o da Portaria Interministerial
  MPS/MF 350/09, revogada mas usada nos cálculos de janeiro a junho, e o da 333/10.
  Os dois foram mantidos. A escolha depende da data do cálculo, não do bloco.
- **jun/99, jun/00, jun/11** — mudança de tabela no meio do mês. Os rótulos do original
  ("01/06/99 até 16/06/99", "A partir de 17 de junho de 2000") são precisos ao dia; a
  checagem trabalha em competência mensal e por isso acusa sobreposição.

### 5.4 Dias ausentes nos calendários (18.14)

Treze meses impressos com menos dias do que têm. **Conferido na imagem da página**, não
só na camada de texto:

| Mês | Dias ausentes | Impresso / real |
|---|---|---|
| 09/2009 | 5 | 29 / 30 |
| 06/2010 | 5, 12 | 28 / 30 |
| 02/2011 | 5 | 27 / 28 |
| 03/2011 | 5 | 30 / 31 |
| 11/2011 | 5 | 29 / 30 |
| 05/2012 | 5, 12 | 29 / 31 |
| 01/2013 | 5 | 30 / 31 |
| 10/2013 | 5 | 30 / 31 |
| 04/2014 | 5 | 29 / 30 |
| 07/2014 | 5 | 30 / 31 |
| 09/2015 | 5 | 29 / 30 |
| **03/2017** | 6, 13, 20, 27 | 27 / 31 |
| 09/2020 | 5 | 29 / 30 |

Dois exemplos verificados glifo a glifo:

- **Setembro de 2009**, primeira semana: o manual imprime `1 2 3 4 7` — a célula de
  sábado traz **7** onde deveria estar **5**, e o dia 5 não aparece em lugar nenhum.
- **Março de 2017**: a coluna inteira de segunda-feira está vazia. O manual imprime
  `1 2 3 4 / 7 8 9 10 11 12 / 14 …`, sem 6, 13, 20 e 27, e com os demais deslocados uma
  coluna à direita.

O campo `dia_da_semana` do CSV vem **da coluna sob o cabeçalho D S T Q Q S S do
original**, não de cálculo de calendário. Em 42 dias ele diverge do calendário real,
pelo mesmo deslocamento. É o que está impresso.

**Consequência prática:** este calendário não serve para contar dias úteis nem feriados.
Quem precisar disso em 18.13 (RSR) deve usar um calendário independente — e a divergência
entre as contagens de RSR do manual e um calendário correto precisa ser confrontada na
Fase 4.

---

## 6. O que não foi extraído de forma confiável

**O método de conversão da URV não está no bloco.** As páginas 453 a 455 trazem o título
`18.10 Tabela URV` e as cotações diárias em CR$, e nada mais: sem texto de procedimento,
sem fundamento legal, sem nota. O escopo pedia o método como categoria (A). Não foi
inferido. O critério — data-base da conversão, arredondamento, tratamento de dia não útil
— precisa vir do capítulo de critérios matemáticos (p. 9–17), que é outro bloco.
Registrado como lacuna em `trt3-18.10-urv-conversao.json`.

**Três rótulos de vigência de 18.7 ficam fora da linha do tempo verificável:**
`De 22/01/97 a abr/97`, `A partir de 17 de junho de 2000`, `De 1o a 16 de junho de 2000`.
São precisos ao dia; normalizá-los para competência mensal seria interpretar. Ficaram
como texto literal.

**Nove nomes de parcela em 18.1 não se separam do detalhamento por regra mecânica.** O
original quebra alguns nomes em várias linhas sem marcador, e isso é indistinguível de um
detalhamento sem marcador. Cada parcela grava `heuristica_nome` com o critério aplicado e
`parcela_texto_bruto` com a célula literal. Distribuição: 23 linha única, 11 até o
marcador, 9 célula inteira multilinha, 1 sem nome antes do marcador.

**Lacuna do original em 18.1:** a parcela "FGTS" não tem valor na coluna FGTS. Campo
deixado nulo, com `observacao`. Não preenchido.

**Cinco linhas de 18.1 atravessam a quebra de página.** O fundamento legal continua na
página seguinte. Foram reunidas, com as duas páginas gravadas em `paginas_pdf` e o
registro da junção em `continuacoes_de_pagina`.

**Uma entrada de 18.8.1 atravessa a quebra da p. 407 para a 408** (descrição numa página,
grau de risco na outra) e um código vem grafado `74 .13-6`, com espaço no meio. A forma do
original fica em `codigo_no_original`.

**`anexo 18.7.2` não existe.** A tabela de alíquotas por FPAS da p. 449 remete a um
"anexo 18.7.2"; a numeração do manual não tem esse item — o grau de risco é 18.8.

---

## 7. O que este bloco *não* estabelece

Nada aqui é norma vigente. O manual é de julho de 2016: anterior à Reforma Trabalhista,
à ADC 58, à EC 113/2021, à Lei 14.905/2024 e à EC 136/2025.

Em particular, `serie-18.15-tabela-unica-trabalhista.csv` é a Tabela Única do CSJT com
base na **TR** — declarada inconstitucional para débitos trabalhistas pela ADC 58. Está
aqui como registro histórico. Ver `00-base-normativa.md`, seção 1.

As faixas de IRRF param em 2015/2017 e as de contribuição previdenciária em 2017. São
séries: manutenção separada.

Confronto normativo item a item: Fase 4.
