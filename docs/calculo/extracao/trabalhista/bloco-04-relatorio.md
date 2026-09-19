# Bloco 4 — relatório

Manual de Cálculos do TRT-3, capítulo 6, **itens 6.7 a 6.15**, páginas 55 a 82. Fase 2 do
pipeline, tipo *prosa e raciocínio*: validação **adversarial**.

Nenhuma skill escrita. **O capítulo 6 está agora integralmente extraído**, entre os blocos 3
e 4.

| | |
|---|---|
| Espinha | `bloco-04-verbas2.md` |
| Detalhe | `bloco-04-verbas2-detalhe.md` |
| Itens cobertos | 6.7 · 6.8 · 6.9 · 6.10 · 6.11 · **6.12** · 6.13 · 6.14 · 6.15 |
| Pontos marcados para a Fase 4 | 7 |
| Erros materiais do original | 11 |
| Pendências abertas | 6 (P14 a P19) |

---

## 1. Duas correções ao bloco 3

### 1.1 O item 6.12 existe, e a pendência P7 era um erro meu

O bloco 3 registrou, como pendência P7, que "não existe item 6.12 na numeração impressa —
salta de 6.11 para 6.13".

**Existe: 6.12 Comissões, páginas 65 a 67.**

A causa foi minha: o levantamento de títulos do bloco 3 usava um padrão que exigia espaço
logo após o número (`6.12 `), e o original imprime **`6.12. Comissões`**, com ponto. O item
escapou da varredura — e nenhuma leitura subsequente o recuperou, porque o bloco 3 parou na
p. 54.

Não é detalhe de inventário. O 6.12 é **exatamente o "tópico comissões"** para o qual os
itens 6.4 (p. 29) e 6.6.2 (p. 37) remetem, e que o bloco 3 declarou estar fora do recorte,
duas vezes. Ele traz a regra mais desenvolvida do capítulo sobre base de cálculo de horas
extras — a simetria entre base e divisor do comissionista (espinha § 6.3).

`pendencias.md` § 10 foi corrigida.

### 1.2 Os itens 6.1 a 6.6 terminam na p. 55, não na 54

Os passos (c) e (d) do exemplo de supressão de horas extras do item **6.6.8** ficam na p. 55.
O bloco 3 fechou na 54 e deixou o exemplo sem desfecho. O fecho está no detalhe deste bloco,
§ 1 — inclusive a demonstração de por que o passo (b) exige **uma média por adicional**.

---

## 2. Onde o capítulo termina

| Bloco | Itens | Páginas |
|---|---|---|
| 3 | 6.1 a 6.6 | 18–55 |
| **4** | **6.7 a 6.15** | **55–82** |

O capítulo **7 — Atualização monetária e juros de mora** abre na **p. 83**. Não há sobra: o
item 6.15 termina na p. 82. A fronteira da triagem de `01-plano-extracao.md` (18–82) confere.

---

## 3. O que saiu

**Espinha**, no mesmo schema do bloco 3 — por verba: base de cálculo, fórmula,
proporcionalidade, incidências de INSS/FGTS/IRRF, reflexos, súmulas e OJs.

Fórmulas extraídas como fórmula:

```
sobreaviso      = salário_normal × 1/3 × horas          escala ≤ 24h
prontidão       = salário_hora × 2/3 × horas            escala ≤ 12h
intrajornada    = intervalo INTEGRAL × (1 + adicional_HE)
interjornada    = 11h − intervalo concedido             (só a diferença)
interjornada+folga = 24h + 11h = 35h
insalubridade   = {10 | 20 | 40}% × salário_mínimo
periculosidade  = 30% × salário simples
transferência   = 25% × salário
adic_noturno    = remuneração / divisor × adicional × horas_reduzidas
horas_reduzidas = horas_efetivas × 1,142857143          (urbano; rural não reduz)
comissionista   = total_comissões / horas_efetivas × adicional_isolado × nº_HE
ind_tempo_serv  = maior_remuneração × anos              fração ≥ 6 meses = ano
seguro_desemp   = valor_da_parcela × {3|4|5}            piso = salário mínimo
vale_transporte = passagens/dia × dias × valor_unitário [− 6% do salário]
multa_477       = 1 salário mensal simples
multa_467       = 50% × parcelas rescisórias incontroversas
FGTS            = base × 0,08   ·   FGTS+40% = base × 0,112
multa_40%       = (saldo + JAM + saques no contrato) × 0,40
```

### 3.1 Os cinco pontos de atenção especial do escopo

| Pedido | Onde | Resultado |
|---|---|---|
| **6.7** — extrair integralmente e marcar a revogação com data de corte | Espinha § 1 e § 12 (F1) | Extraído com os dois requisitos cumulativos da Súmula 90 e o exemplo. Revogação marcada com corte em **11/11/2017** |
| **6.10** — natureza do intervalo suprimido | Espinha § 4.1 e § 12 (F2) | Marcado. E o manual explicita **duas** mudanças, não uma: a natureza (salarial → indenizatória) **e** a extensão (integral → período suprimido). Marcar só a primeira perderia metade |
| **6.11** — cumulação e base da insalubridade | Espinha § 5.1.1 e § 5.2 | A base tem histórico completo, com **duas súmulas do TST opostas, uma suspensa por liminar do STF**. **A cumulação não é tratada pelo manual** — pendência P15, nada inferido |
| **6.13** — distinguir 467 de 477 | Espinha §§ 7.8 e 7.9 | Bases e grandezas distintas, e a **regra proporcional do IR** da multa do 467 |
| **6.14** — apuração, multa de 40% e projeção do aviso | Espinha § 8 | Índice de 12 verbetes integral; **saques no curso do contrato entram na base da multa**; a tabela JAM **já embute juros de 3% a.a.** |

---

## 4. Validação adversarial

Dois revisores independentes, sem o contexto desta extração, sem que um visse o trabalho do
outro. O escopo pediu uma verificação específica: que nenhum índice de súmulas e OJs de
subitem ficasse de fora, como ocorreu com o 6.6.1 no bloco 3.

### 4.1 A verificação dos índices — resultado

O revisor de omissões varreu o original atrás de toda tabela ou lista de "Súmulas e OJs
aplicáveis" e reportou:

> **Quantos existem no original (p. 55–82): 1 (um), e só um** — o do item 6.14 FGTS,
> p. 78–79, com 12 verbetes em três tabelas. **Extraído integralmente. Nenhum verbete
> ausente. Nenhum índice perdido.**

Conferência verbete a verbete: Súmulas TST 63, 98, 206, 305, 362 (5/5); OJs SDI-I 42, 195,
302, 322, 394 (5/5); OJs das Turmas do TRT-3 4 e 29 (2/2).

O revisor confirmou também que os itens 6.7 a 6.13 e o 6.15 **realmente não têm** índice
tabulado — as súmulas aparecem no corpo — e validou a tabela de verificação da espinha § 11.

### 4.2 Aritmética

O segundo revisor refez **todas** as conferências do detalhe com `Decimal` em precisão 40.

> "Os cinco 'erros materiais' alegados: **todos existem e todos os diagnósticos estão
> corretos**."

E as demais conferências: "Todas as demais conferências do arquivo de detalhe **batem**."

**Nenhum achado GRAVE em nenhum dos dois revisores.**

### 4.3 O achado mais sério — uma afirmação falsa minha

> A espinha listava a **Súmula 264/TST** entre os verbetes "todos com regra desenvolvida na
> espinha". **Não havia uma linha sobre ela em nenhum dos dois arquivos**, e o manual a cita
> duas vezes — uma delas para fazer uma **distinção entre casos** que eu havia perdido
> inteira.

O acórdão do item 6.12 (p. 66) enfrenta o ponto: mesmo quando o comando manda observar a
Súmula 264 (globalidade salarial), "a base de cálculo constitui-se do valor-hora das
comissões recebidas no mês, porquanto o divisor mencionado na Súmula 340 refere-se apenas e
tão somente às horas de labor".

**A Súmula 264 amplia *o que entra* na base; a Súmula 340 fixa *como se apura o valor-hora*
do comissionista.** Uma não desloca a outra. Corrigido na espinha § 6.3.

Duas outras omissões no mesmo acórdão, ambas incorporadas:

- **A aritmética do divisor 220**: `[(44:6 = 7,33333) × 30 = 219,99999]` — com a leitura de
  *onde o repouso entra*: sai da divisão por 6 e volta na multiplicação por 30. Eu havia
  guardado só a frase das "188 horas no mês", que é a conclusão, e cortado a demonstração.
- **O art. 10 do Dec. 27.048/49**, fundamento expressamente **afastado** pelo acórdão: a
  integração do repouso ao salário "para todos os efeitos legais" não autoriza fazer as
  comissões que já compuseram o RSR retornarem como base das horas extras.

> O revisor resumiu bem: as três omissões se concentram no mesmo lugar — "o trecho de que a
> extração diz preservar 'o núcleo'. Preservou o núcleo retórico ('dois pesos e duas
> medidas') e perdeu a aritmética, o fundamento afastado e a distinção".

### 4.4 Outras omissões relevantes, incorporadas

| Achado | O que faltava |
|---|---|
| Base do seguro-desemprego | A **lista completa do MTE** (p. 70) é maior que a do corpo do texto: acrescenta **RSR, prêmios habituais, prestação in natura, biênios/triênios/quinquênios/decênios** e o **piso de 25%** do adicional de transferência |
| Aproveitamento de outros vínculos | A segunda condição — "**e que não tenham sido utilizados em requerimentos anteriores**" — que é a que impede dupla contagem |
| Lei 7.788/89 | A aplicação é **por fatias, cumulativa**: os primeiros 3 SM continuam no reajuste mensal, e só o excedente vai para o trimestral, que é **antecipação** |
| REsp 1.371.272/PR | Dois pontos fiscais: o **termo inicial** do crédito tributário é a **liberação** do depósito judicial, não o depósito; e a **exclusão da multa fiscal** quando a fonte pagadora erra |
| Lei 12.506/11 | A regra dos **3 dias por ano** é repetida em três itens (6.11.1, 6.11.2, 6.11.4.4); eu guardava só a fórmula de ajuste `/30 × dias` |
| Art. 73, § 1º, da CLT | O fundamento da ficção noturna e a explicação "**08 horas** entre 22 e 5, e não as **07 aparentes**" |
| Multa do art. 467 | "O valor é atualizável e passível de incidência dos juros, **acompanhando o principal**" |

Incorporadas também: atualização da ajuda-alimentação (Súmula 381/TST); a glosa do manual
sobre a OJ 388 ("incluindo o período de 22 às 05 horas"); o art. 8º do Dec. 2335/87 nas URPs;
a divisão em grupos da Lei 8222/91; o crédito da Lei 8900/94 na tabela de parcelas; e o
registro da **remissão quebrada ao "item 6.7.5.1"**, que não existe — o mesmo defeito de
numeração cruzada que o bloco 3 catalogou.

### 4.5 Afirmações sem respaldo, corrigidas

| Achado | Correção |
|---|---|
| "**Súmulas 110 e 118**" entre os verbetes que ganham conteúdo | A **Súmula 118 não aparece** em nenhum ponto das p. 55–82. Removida; voltou para a lista ◆ da pendência P13 |
| "O gatilho do art. 467 é a verba incontroversa não paga na **primeira audiência**" | Juridicamente correto, mas **o manual não enuncia gatilho algum** — nem do 467, nem do 477. Reescrito para dizer o que o manual diz, com a ausência registrada |
| "gatilho: atraso no pagamento" na multa do art. 477 | Mesma correção |
| Seguro-desemprego, "o **único** item com dois regimes por data de corte" | Falso: o doméstico (§ 7.5) e a multa do 467 (§ 7.9) também têm |
| F3 atribuía "prêmios e abonos habituais" à p. 68 | Os prêmios estão na **p. 70**, na nota do MTE; "abonos" não aparece no item |
| FGTS do adicional noturno atribuído à p. 64 | Está na **p. 63** |
| "Três práticas de arredondamento" (P17) contra "quatro" no detalhe | Uniformizado em **quatro** |
| Detalhe: "oito reflexos em RSR", "Dois defeitos" com três itens | São **sete** reflexos e **três** defeitos |
| Detalhe § 8.1: "2.000,00 / 26 dias úteis × 4 RSR" | Os 26 dias e os 4 RSR **não constam do exemplo** — marcado como reconstrução desta extração. Idem os "25 dias" do saldo de salários no § 13 |
| Detalhe § 9: "19 × 0,0333% = 0,633%" | Dá 0,6327%. A taxa que reproduz exatamente o publicado é **1% ÷ 30 por dia**. Demonstração corrigida |
| Detalhe § 11.2: cabeçalho "94,60 − 6%" | É 6% **do salário**, não de si mesmo |
| Detalhe § 8.2: "4.018,74 + 10.329,62 = 14.348,36" | Eu havia ajustado o segundo número para a conta fechar. O manual publica **10.329,63**; a soma só fecha em precisão plena (10.329,6257) |
| Detalhe § 13: totais não conferidos | As cinco parcelas somam **29.402,09** e o manual imprime 29.402,08 — mais uma ocorrência de **truncamento** |

---

## 5. Erros materiais do original — registrados, não corrigidos

| # | Onde | Erro |
|---|---|---|
| 1 | 6.12, p. 67 | **"Total percebido de out/01 a dez/01 = 5.562,04"**. As três linhas rotuladas somam **4.018,74**; a diferença é exatamente jan/02. O total abrange **quatro** meses e é dividido por **três** — inflando o reflexo no 13º/01 em **R$ 128,60** |
| 2 | 6.13.9, p. 76 | **Férias prop. + 1/3 (10/12) = 5.555,42**, quando `5.000 × 10/12 × 4/3 = 5.555,56`. Nenhuma variação plausível reproduz o número. Propaga para a multa e o total |
| 3 | 6.11.4.1, p. 62 | `6 × 1,142857143 = 6,857`, publicado como **6,87** (seria 6,86). Os outros dois exemplos da mesma página fecham |
| 4 | 6.10.1, p. 58 | **Julho de 2011 com 32 dias**: a linha imprime RSR 6 + dias úteis 26, e o mês tem 31. Uma linha em sete |
| 5 | 6.13.4, p. 73 | Linha de total imprime "(3.204,09 + **404,78**)". Os juros são 262,74; o total publicado (3.466,83) está certo e o 404,78 não aparece em nenhum outro ponto |
| 6 | 6.13.4, p. 68 e 70 | **"Salário por semana → base = valor da semana ÷ 30 × 7"**, que **reduz** o valor a 23% em vez de mensalizá-lo. Duas ocorrências idênticas; a p. 70 atribui ao Ministério do Trabalho |
| 7 | 6.13.4, p. 71 e 73 | **"0,33% ao dia ou 1% ao mês"**. A taxa efetivamente usada é **1% ÷ 30 = 0,0333…% ao dia** — um centésimo do impresso |
| 8 | 6.14, p. 78 | "8 × 1,40 = 11,2% **ou 1,112**". O coeficiente é **0,112**, como o próprio manual usa em todos os exemplos |
| 9 | 6.13.2, p. 68 | Título "Indenização do art. 9º da lei **6.708/89**". A Lei 6.708 é de **1979**, como o manual grafa corretamente na p. 19 |
| 10 | 6.11.2, p. 61 | O último parágrafo do item de **periculosidade** conclui falando do "reflexo do adicional de **insalubridade**". Cópia do item anterior |
| 11 | 6.11.4.4, p. 63 | Remissão ao "item **6.7.5.1**", inexistente. Mesma numeração cruzada que o bloco 3 catalogou |

Os erros 3, 4, 5 e 10 são locais. **Os erros 1, 2 e 6 alteram resultados**, e o 7 alteraria
qualquer cálculo de juros feito pela taxa impressa.

---

## 6. Arredondamento: agora são quatro práticas

O bloco 3 encontrou duas cadeias incompatíveis. Este bloco encontra **quatro**, nenhuma
enunciada, todas dentro do mesmo capítulo:

| Prática | Onde | Evidência |
|---|---|---|
| **Precisão plena** | Supressão (§ 1), intervalo do art. 253 (§ 4), coluna de valor do adicional noturno (§ 7.2), comissionista (§ 8.1), vale-transporte (§ 11) | `1500/220 × 1,8 × 28,5 = 349,77`; com o exibido 12,27 daria 349,70 |
| **Valor exibido** | Intervalo comum (§ 3), reflexos do adicional noturno (§ 7.3) | `5,11 × 25,71 = 131,38`; a plena daria 131,49 |
| **Arredondamento a cada passo** | Horas noturnas (§ 7.1) | `3 → 3,4285 → 13,71 → 58,76`; a plena daria 58,7755 |
| **Truncamento** | Seguro-desemprego (§ 9), totais da multa do 467 (§ 13) | `1.014,335 × 5 = 5.071,675 → 5.071,67`; arredondado daria 5.071,68 |

As duas primeiras aparecem **em páginas consecutivas sobre o mesmo valor unitário** (§§ 7.2
e 7.3) — o mesmo padrão que o bloco 3 encontrou entre as p. 42 e 46.

> **O achado novo é o truncamento.** O bloco 2 havia contraposto as duas fontes primárias
> — o Manual CJF trunca, o Manual TRT-3 arredonda. **O TRT-3 faz as duas coisas.** A
> divergência não é só entre fontes: é interna, e não sobre *como* arredondar, mas sobre *em
> que ponto da cadeia*.

Pendência **P17**; agrava a **P10** do bloco 3 e a **§ 9-A** de `pendencias.md`.

---

## 7. Marcado para a Fase 4

Sete pontos, **sem verificação do conteúdo novo** — a base normativa não cobre verbas. Os dois
de alta gravidade são exatamente os que o escopo antecipava:

| # | Ponto | Dispositivo |
|---|---|---|
| **F1** | **Horas *in itinere*** — item 6.7 inteiro | **CLT art. 58, § 2º** — hipótese suprimida. Corte em **11/11/2017** |
| **F2** | **Intervalo intrajornada suprimido** — integral, como hora extra, com natureza salarial e reflexos | **CLT art. 71, § 4º** — muda **natureza e extensão** |

Mais: base do seguro-desemprego e das comissões pelo art. 457 (F3, F4); adicional noturno em
12×36 e o art. 59-A (F5); **o art. 384 da CLT, revogado**, que sustenta a Súmula 39 do TRT-3
(F6); e a prescrição do art. 11, § 2º (F7).

**Não marcado, porque não muda**: interjornada e OJ 355; ficção legal da hora noturna;
sobreaviso e prontidão; multas dos arts. 467 e 477; OJ 54 e o teto do art. 412 do CC;
disciplina do FGTS; e toda a cronologia do item 6.15.

---

## 8. Relação com `00-base-normativa.md`

A base **continua não cobrindo verbas** (`pendencias.md` § 12). Cinco pontos de contato neste
bloco, **todos de confirmação**:

- **R7** — termos iniciais do dano moral: correção do arbitramento, juros do **ajuizamento**
  (Súmula 439/TST), contra citação ou evento danoso no cível. Terceira fonte confirmando que
  o termo inicial dos juros não é intercambiável.
- **R1** — a tabela JAM "**já computa juros de 3% ao ano**". Índice que embute juros não
  admite juros por fora. Exatamente o padrão de englobamento que R1 obriga a declarar.
- **R8** — dois novos pontos: "o termo prescricional vai estar definido pelo **comando
  exequendo**" (6.14) e "observar se a dedução dos 6% consta ou não do **comando exequendo**"
  (6.13.6). Somam **cinco** no capítulo 6.
- **Regra 6 do plano** — duas divergências registradas e não resolvidas: a base da
  insalubridade (§ 5.1.1) e a dedução dos 6% do vale-transporte (§ 7.6).

---

## 9. Pendências abertas

| # | Pendência | Bloqueia |
|---|---|---|
| **P14** | **Base do adicional de insalubridade sem árbitro.** Súmula 228/TST (salário básico) **suspensa** por liminar do STF na Rcl 6266; Súmula 46 do TRT-3 fixa o **salário mínimo**. Conflito federal × regional, com suspensão liminar | Cálculo de insalubridade; vira variante |
| **P15** | **Cumulação de insalubridade e periculosidade não é tratada.** Os itens são autônomos; nenhum menciona cumulação, opção ou o art. 193, § 2º, da CLT | Casos com os dois adicionais deferidos |
| **P16** | **"Salário por semana ÷ 30 × 7"** reduz em vez de mensalizar. Duas ocorrências; atribuída ao MTE | Seguro-desemprego de horista/semanalista |
| **P17** | **Quatro práticas de arredondamento**, nenhuma enunciada | Agrava a P10 do bloco 3 |
| **P18** | **Critério de contagem de RSR não declarado** no exemplo do item 6.10, e uma linha em que RSR + dias úteis excede os dias do mês | Reflexos em RSR |
| **P19** | **O item 6.15 é cronologia normativa, não fórmula.** Dez normas entre 1986 e 1996, com índices (IPC, URP, IRSM, FAS, FAZ, IPC-r, FRS) que **não estão** nas tabelas do item 18 extraídas no bloco 1 | Diferenças salariais anteriores a 1996 |

**P19 é a que abre trabalho novo.** O bloco 1 extraiu as séries do item 18 — salário mínimo,
INSS, IRRF, URV, BTN, Ufir, Selic. Nenhuma delas cobre IPC, URP, IRSM, FAS, FAZ ou IPC-r. O
item 6.15 depende de séries que o corpus não tem.

---

## 10. Estado do capítulo 6

Integralmente extraído. O que o capítulo entrega ao motor, somando os blocos 3 e 4:

| Camada | Conteúdo |
|---|---|
| **Vocabulário** | O que é principal, correção, juros, base de cálculo, habitualidade, reflexo — e as duas acepções de "refletir" |
| **Regras de contagem** | Doze avos por dias corridos × mês civil; fração de 15 dias; anos completos do aviso; fração de 6 meses na indenização por tempo de serviço; meses nos 36 do seguro-desemprego |
| **Fórmulas** | Trinta e poucas, todas com proveniência |
| **Regras de composição** | O que entra em cada base, o que é excluído, e as assimetrias — periculosidade integra HE e não integra sobreaviso; adicional noturno integra HE e não o inverso |
| **Regras de precedência** | Cinco pontos em que o manual se subordina expressamente ao comando exequendo |
| **Divergências registradas** | Feriado na 12×36; base da insalubridade; dedução dos 6% do vale-transporte |

O próximo bloco é o **capítulo 7 — atualização monetária e juros**, p. 83 em diante, marcado
pela triagem como **Fase 4 obrigatória**: materialmente superado pela ADC 58, pela EC
113/2021, pela Lei 14.905/2024 e pela EC 136/2025. É o primeiro bloco em que
`00-base-normativa.md` **tem** o que dizer.
