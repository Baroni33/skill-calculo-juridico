# Bloco 11B — relatório

Capítulo 10, segmento C — item 10.3, amortização de valor pago sob o art. 12-A.
pp. 237 (offset 681) a 266 (offset 2141). Produto em `bloco-11b-amortizacao.md` e
`bloco-11b-amortizacao-detalhe.md`.

---

## 1. Entregas

| Item | Estado |
|---|---|
| Moldura das pp. 237–239 como gabarito | **Feita** — roteiro A–H, J |
| Cada exemplo contra a moldura | **Feito** — 5 exemplos |
| Consolidação enunciado × exemplo × inconsistência | **Feita** — 14 divergências |
| **Ordem de imputação** | **Respondida: proporcional, sem fundamento** |
| **Data de referência** | **Respondida: levantamento** |
| Valor pago atualizado ou nominal | **Respondida: nominal** |
| Bruto ou líquido | **Respondida: depende do subitem** |
| Relação com art. 12-A e RRA | **Respondida: dois NM distintos** |
| Os seis exemplos concordam? | **Não** — 14 divergências |
| Medição contra a linha de base do 11A | **Feita** — § 3 |
| Pendência herdada (0,44) | **Não reaparece** — § 5 |
| Aritmética em `Decimal` | **Feita** — 168 linhas, 139 exatas |
| Releitura adversarial, tabular inclusive | **Feita** — 28 defeitos |
| Verificação literal por script | **Feita** |
| Notas contra as linhas que qualificam | **Feita** |
| Marcação Fase 4 / ADC 58 | **Feita** — § 6 |
| Mapa de cobertura | **Atualizado — 84,5%** |

---

## 2. A resposta a R10

**A imputação é proporcional.** Letra F de 10.3.1 (`pagina_pdf` 237), repetida como letra G
em 10.3.2.1 (239):

> "separar no saldo remanescente o principal dos juros, através de **proporção** em relação ao
> total do cálculo"

Confirmada nos cinco exemplos, fechando exato (`F.1 + F.2 = E`).

### 2.1 O achado que muda a natureza de R10

**Não há fundamento jurídico nenhum.** Varredura que sustenta:

| Termo | Escopo | Ocorrências |
|---|---|---|
| `art. 354` · `354 do C` · `artigo 354` | **PDF inteiro** | **0** |
| `354`, `imputa`, `Código Civil`, `Súmula`, `anatocismo` | segmento C | **0** cada |
| `proporcional` | segmento C | **101** |

**Aplicada 101 vezes, fundamentada zero.** A única justificativa é aritmética — evitar
anatocismo, "descarregar" o saldo (palavra que ocorre **uma vez** em todo o manual).

Isto **fundamenta R10 por razão mais forte do que a esperada.** A invariante supunha duas
regras distintas, cada uma com seu fundamento. O que há é **uma norma (art. 354 do CC) contra
um costume de liquidação sem base declarada**. Não são regras concorrentes: são coisas de
naturezas diferentes.

**Consequência de modelagem:** o critério proporcional **não pode entrar como regra derivada
do corpus**. Tem de ser preset de regime, com o fundamento declarado como *"prática do manual
do TRT-3, sem norma citada"*. Pendência **P11B-07**.

---

## 3. Quanto custa — e é a decisão mais cara já medida

Variando **só** a ordem de imputação, em `Decimal`:

**Exemplo 1** (juros residuais de 55,17%):

| Ordem | Δ % |
|---|---|
| Proporcional (manual) | — |
| Juros primeiro (art. 354) | **+10,58%** |
| Principal primeiro | −13,25% |

**Amplitude: 23,83% do saldo — R$ 9.918,92.**

**EXEMPLO de 10.3.1** (juros residuais de 1,13%): amplitude de **0,25%**.

O efeito escala com `tempo residual × participação dos juros no bruto na data da amortização`.

Reproduzi o **+10,58% de forma independente**, por caminho próprio — bate na terceira casa.
(Meu saldo-base difere do do extrator porque omiti duas deduções menores do exemplo, o que
desloca o lado "principal primeiro"; a ordem de grandeza e o sinal são os mesmos.)

**Contra os deltas do 11A** — −2,48%, −3,15%, −R$ 285,83 — a ordem de imputação é, com folga,
a decisão mais cara do corpus extraído até aqui.

### 3.1 Onde a amortização entra na linha de base

O 11A entregou `principal corrigido → juros sobre o corrigido → descontos`.

**A amortização não acrescenta um passo no fim: parte a linha do tempo em duas.** Tudo é
trazido à data do levantamento, rateado ali, e só então levado ao marco final. É exatamente
por isso que o rateio custa 23,83% — ele decide a composição do saldo que renderá juros por
todo o período residual.

E o passo zero, "descarregar", é o que impede anatocismo: **um motor que aplique juros sobre
um saldo que já os contém produz juros sobre juros.**

---

## 4. BLOQUEIO — reportado, não contornado

**P11B-01**, `pagina_pdf` 266, Exemplo 4.

```
coluna H, declarada (D + G):  976,82 + 384,69 = 1.361,51   impresso 1.360,52   Δ −0,99
coluna K, declarada (F + H + J), com os impressos: 5.181,98  impresso 5.171,98   Δ −10,00
```

Para fechar K seria preciso `H = 1.350,52`, que não resulta de operação alguma do exemplo.
**Dois desvios independentes, de ordens de grandeza diferentes, na mesma linha** — e o
segundo, exatamente 10,00, não é absorvível por arredondamento.

**Propaga ao total.** O `TOTAL DO CÁLCULO EM 31/05/16 = 43.077,24` — que eu usara como marca
de fronteira do segmento — deveria ser **43.088,23**.

Conferido por mim, além do extrator.

---

## 5. A pendência herdada não se repetiu

O 11A deixou `2.820,40` e `5.109,98` com delta 0,44 sem via declarada, e o enunciado mandou
tratar como bloqueio se o padrão reaparecesse.

**Não reapareceu.** O único delta próximo (0,45, `pagina_pdf` 251) **dissolve-se**: o operando
real é `34.611,2499`, não o `34.611,21` impresso, combinado com a digitação `46.893,02` onde
o valor é `46.893,92`. Com os operandos reais fecha **exata** em 25.293,98. Classe:
arredondamento + digitação.

Varridos os 29 deltas não-nulos do segmento — nenhum com magnitude inexplicada daquela ordem.

**Mas surgiram duas regras ocultas novas:** o arredondamento do NMP (P11B-02) e o percentual
pleno de IR no saldo contra `0,9091` no levantamento (P11B-03).

---

## 6. Fase 4 — aqui o conflito com a ADC 58 é real

No segmento A a marcação fora geral. **Aqui é específica**, porque o segmento C *é* a operação
que a modulação disciplina:

- a modulação **ressalva valores pagos** e **veda dedução ou compensação de diferenças
  apuradas pelo critério anterior** — e todo o segmento é dedução de valor pago;
- o rateio proporcional distribui o pagamento entre principal e juros **calculados por TR +
  1% ao mês**. Recalculados os juros pelo critério novo, **a proporção muda e o saldo muda**;
- a ressalva convive mal com um método que **recompõe** o bruto até a data do pagamento antes
  de deduzir.

Busca no segmento: `ADC`, `IPCA`, `EC 113`, `compensa` → **0 ocorrências** cada, como esperado
de um texto de 2016.

**Marcado, não harmonizado.** É o maior atrito identificado entre o corpus e a base vigente.

---

## 7. Achados que não estavam no pedido

**A moldura tem defeitos próprios.** Não existe letra `I` em 10.3.1 (a sequência é A–H, J),
mas o EXEMPLO rotula sua linha final como `Demonstração item " I "` e a descreve como
`(l + m)` — **letras que não existem** no demonstrativo. E 10.3.2.1 tem **duas letras `O`** e
nenhuma `P`, embora os Exemplos 1 e 2 rotulem o resumo como "P".

**A hipótese que o manual declara obrigatória não tem exemplo no segmento.** A letra C traz um
critério alternativo com a observação *"quando há juros vincendos (...) o segundo é
obrigatório"*. **Nenhum dos cinco exemplos o usa** — quem o exercita são os Exemplos 5 e 6, no
segmento D.

**E o corte C/D parte essa hipótese.** Varredura de `^1[01]\.\d[\.\d]*` nas pp. 240–300:
nenhum heading numerado depois de `10.3.2.1`; a única ocorrência é uma remissão a "10.2" no
meio do texto da p. 249. Os seis exemplos ficam pendurados no mesmo subitem, que só termina
na p. 277.

**Registrado, não resolvido por conta própria** — a regra "limite de conteúdo vence limite de
página" recomendaria fundir C e D, mas isso altera a divisão fixada no 11A. Fica como decisão
para o 11D, com a informação na mesa. Pendência **P11B-08**.

**Defeito do tipo p.223 — linha copiada de outro exemplo.** O RESUMO GERAL do Exemplo 2
(`pagina_pdf` 254) imprime `Nº de meses RRA: 11,10` e `8,90`, que são **os do Exemplo 1**; o
Exemplo 2 apurou 10,8 e 9,2. O padrão que apareceu na p. 223 do segmento A repete-se aqui.

---

## 8. Cobertura

**84,5% do PDF**, contra 78,1% ao fim do 11A.

| | Páginas |
|---|---|
| Cobertas | **398** |
| Não cobertas **com decisão registrada** | **51** |
| Não cobertas **sem decisão** | **14** |

O capítulo 10 tem **45 das 69 páginas cobertas**. As 24 restantes são o segmento B (13 pp.,
bloco 11C) e o D (11 pp., bloco 11D).

**Os capítulos 8, 12 e 14 seguem sem destino** — mantidos visíveis, não classificados por
conta própria, conforme o enunciado.

---

## 9. Pendências

Oito, em `bloco-11b-amortizacao.md` § 10. As que bloqueiam ou decidem:

- **P11B-01** — o bloqueio da p. 266, com delta de 10,00 não absorvível;
- **P11B-07** — o critério proporcional **sem fundamento normativo**: decide como R10 entra no
  motor;
- **P11B-08** — o corte C/D parte a hipótese que a moldura declara obrigatória;
- **P11B-06** — o segmento adota a dedução na data do levantamento sem citar a Súmula 15 nem o
  16.4.11, que reconhece **duas** teses.

---

## 10. Lição de método

O 11A fechou com "fronteira de segmento não é fronteira de página". Este bloco mostra o
custo de não perguntar pelo fundamento:

> **A regra mais consequente do capítulo — a que move o saldo em 23,83% — é aplicada 101 vezes
> e fundamentada zero vezes.** Só se descobre isso procurando o fundamento de propósito. Uma
> extração que registrasse "imputação proporcional, item 10.3.1, p. 237" estaria correta e
> seria inútil: perderia que o manual não tem autoridade para a regra que ensina.

A pergunta "com que fundamento?" que o enunciado anexou a cada item foi o que produziu o
achado. Vale como padrão para os blocos seguintes.
