# Bloco 11A — relatório

Capítulo 10 do Manual do TRT-3, pp. 209–277. Varredura estrutural completa e extração do
primeiro segmento. Produto em `bloco-11a-imputacao.md` e `bloco-11a-imputacao-detalhe.md`.

---

## 1. Entregas

| Tarefa | Estado |
|---|---|
| **Tarefa 0** — varredura estrutural antes de extrair | **Feita.** Quatro operações, não duas. § 2 |
| **Tarefa 1** — extrair só o primeiro segmento | **Feita.** Item 10.1, 41.471 caracteres |
| Aritmética em `Decimal` | **Feita** — 39 contas reproduzem, 14 não |
| Regras dentro de exemplo, promovidas à espinha | **Feita** — 12 estruturais, 12 incidentais |
| Releitura adversarial, tabular inclusive | **Feita** — 11 rótulos conferidos contra a operação |
| Verificação de citação literal por script | **Feita** |
| Notas contra as linhas que qualificam | **Feita** — 8 notas, 1 com atrito |
| Marcação para Fase 4 (ADC 58) | **Feita** — § 7 |
| Mapa de cobertura atualizado | **Feito** — **78,1%**, com as duas categorias separadas |

---

## 2. Tarefa 0 — a varredura mudou o desenho do bloco

O capítulo declara sua própria divisão na p. 209: "dois tipos de atualização". **A declaração
não serve para dividir o trabalho.** Medido por script:

| Seg. | Operação | pp. | Caracteres |
|---|---|---|---|
| A | 10.1 — sem amortização | 209–223 (parcial) | 41.471 |
| B | 10.2 — descontos proporcionais | 223–236 | 41.228 |
| **C** | **10.3 — amortização, RRA (art. 12-A)** | **237–265** | **89.290** |
| D | 10.3 — amortização, art. 12-B | 266–277 | 33.694 |

**A numeração impressa para em 10.3.2.1, na página 239.** As 38 páginas seguintes — 55% do
capítulo — não têm numeração: são `Exemplo 1` a `Exemplo 6`. Dividir pelo sumário ou pela
numeração perderia mais da metade.

O corte C/D tem fundamento no texto, não na contagem: os Exemplos 5 e 6 tratam de
**rendimentos do ano-calendário e de entidades de previdência** — art. 12-B —, contra o
regime do art. 12-A dos Exemplos 1 a 4. É a mesma separação que o item 10.2 faz entre 10.2.1
e 10.2.2.

**Recomendação para o 11B: ir ao segmento C, não ao B.** A ordem documental colocaria os
descontos proporcionais antes da amortização, mas é a amortização que o produto precisa e é
ela que responde a R10.

### 2.1 Uma premissa do enunciado caiu

O enunciado fixava o corte em "pare na 222". **O item 10.1 não termina na p. 222:** o título
`10.2` está no **offset 2.658 da p. 223**, que tem 3.258 caracteres.

Parar em 222 partiria a 4ª hipótese no meio do Passo 5, deixando de fora os Passos 6 e 7, o
demonstrativo do art. 12-A, o quadro A–K e o RESUMO GERAL. **E o achado mais grave do
segmento está exatamente nesse trecho** (§ 4.1), assim como a única ocorrência da palavra
`levantamento` em todo o segmento A.

O extrator leu o trecho e registrou a divergência em vez de obedecer ao corte. Foi a decisão
certa. É a terceira vez na série que uma premissa do enunciado — não do manual — não resiste
à verificação, e a regra que a apanha é sempre a mesma: **registrar a busca que sustenta a
afirmação**.

---

## 3. O que o segmento A respondeu

### 3.1 A ordem das operações altera o resultado? Não. Mas a pergunta certa é outra

```
manual : (4.066,41 × 1,02538895) × (1 + 31,266667%) = 5.473,36
inversa: (4.066,41 + 4.066,41 × 31,266667%) × 1,02538895 = 5.473,36
                                                   delta = 0,00
```

Distributividade. **A ordem entre correção e juros é indiferente.**

**A base não é.** Três decisões de base, medidas:

| Decisão | Efeito |
|---|---|
| Juros sobre o nominal em vez do corrigido | **−32,28 (−2,48%)** |
| Idem, no exemplo com vincendos | **−106,49 (−3,15%)** |
| Deduzir INSS antes dos juros na base de IR | **−285,83** |

**Os juros incidem sobre o principal corrigido.** É a decisão mais consequente do item.

### 3.2 Os dois critérios de juros, e a regra que o manual enuncia

O manual oferece dois critérios e declara que são idênticos — **conferido ao centavo:
1.303,71 pelos dois**. E enuncia a exceção:

> "na hipótese do cálculo envolver juros vincendos, **o segundo critério torna-se
> obrigatório**"

É regra enunciada, não inferida. Rara neste capítulo.

---

## 4. Defeitos do original

### 4.1 Uma linha copiada de outro exemplo, com a multa junto

O mais grave, e está no trecho da p. 223 que a fronteira errada teria cortado.

A coluna F do quadro A–K, rotulada `Total recolhido a ser recolhido em junho/15`, traz
**956,19** e **8.912,54**, mas `C + D + E` dá **831,08** e **7.744,33**.

Rastreio no manual inteiro: `956,19` e `8.912,54` ocorrem em **duas páginas apenas, 223 e
261**. Na p. 261 o quadro tem dez colunas e inclui `Multa (0,33% ao dia limitada a 20%)`, com
125,11 e 1.168,21 — que ocorrem **só na 261**. E:

```
831,08   + 125,11   = 956,19     (125,11   = 625,56   × 20%)
7.744,33 + 1.168,21 = 8.912,54   (1.168,21 = 5.841,04 × 20%)
```

**A linha foi copiada da p. 261 sem remover a multa.** As letras das colunas foram remapeadas
("col. G × Selic" na 223 contra "col. F × Selic" na 261); os números, não. E a p. 220 declara
literalmente *"Aplicação apenas dos Juros Selic, sem a inclusão da multa"*, com a coluna E
vindo 0,00.

Verificado por mim, não apenas pelo extrator.

### 4.2 Remissão cruzada errada

A p. 209 manda calcular os juros "nos percentuais estudados no tópico **7.3**". **O 7.3 é
"Aplicação do IPCA-E".** Juros de mora são o **7.6**. Conferido no sumário impresso.

Achado meu na releitura — o extrator não o reportou.

### 4.3 Resíduos de versão anterior

`2.731,80`, `4.417,32`, `248,63` e o índice `1,023071044` ocorrem **apenas nas pp. 215–216**
e em nenhum outro ponto do manual. Um rótulo anuncia `(2.731,80 × 110,70%)` e produz
3.135,81, que é `2.832,71 × 110,70%`.

---

## 5. O padrão de precisão se confirma fora do capítulo 11

O bloco 10 estabeleceu que a aritmética do manual é encadeada em precisão plena e que os
números impressos com duas casas não são os operandos. **10.1 se comporta igual**, por quatro
provas independentes:

- somando parcelas arredondadas dá 3.386,11; em precisão plena, 3.386,10 — que é o impresso;
- índices declarados e grafados divergem: `1,02538895` × `1,025388925`; `1,039177731` ×
  `1,03917731`; percentual `0,81777777` quando a razão é `0,8177740422`;
- **nove somas de coluna** divergem dos totais impressos em 0,01–0,02;
- `arredond` → **0 ocorrências** nas pp. 209–223.

**Não é peculiaridade de um capítulo: é o comportamento do manual.** O motor tem de encadear
em precisão plena e arredondar só na apresentação.

### 5.1 O que não reproduziu, e a distinção que importa

Das 14 contas que não fecham, a classificação separa três naturezas:

| Natureza | Casos |
|---|---|
| **Resíduo de versão anterior** | 2.731,80 · 4.417,32 · 248,63 · 1,023071044 — rastreados, ocorrem só nas pp. 215–216 |
| **Regra oculta** | **2.820,40 e 5.109,98** (p. 215), delta 0,44 — **nenhuma via declarada fecha**. Pendência P11A-02 |
| **Arredondamento da planilha** | 15.375,82, +0,01 sobre todas as variantes, repetido duas vezes — sugere regra não-HALF_UP na origem |

**Só a segunda é preocupante**, porque implica regra que o manual usa e não declara.

---

## 6. Invariante R10 — o segmento A não a fundamenta nem a derruba

R10 afirma que cível e trabalhista tratam imputação por regras não unificáveis, e o enunciado
observou corretamente que a afirmação foi escrita sem a regra trabalhista extraída.

**O segmento A não toca a questão**, por definição: 10.1 é a operação *sem* valor pago.
Buscas que sustentam, nas pp. 209–223: `amortiza` → 3 ocorrências, `valor pago` → 3, **todas
na p. 209 e todas na declaração da divisão do capítulo**, anunciando a operação do segmento C
sem executá-la.

O que o segmento A entrega é a **linha de base**: `principal corrigido → juros sobre o
corrigido → descontos`, com a ordem correção/juros indiferente. **Qualquer regra de imputação
do segmento C será uma alteração sobre esta base, e é contra ela que o efeito se mede.**

**Um indício já colhido, registrado como indício.** Os seis exemplos do segmento C dizem *"o
reclamante **levantou** a quantia de R$ …"*, não "pagou". Isso converge com o item 16.4.11 e a
Súmula 15 do TRT-3 — deduzir na data do **levantamento** —, mas **não é conclusão**: exige o
texto de 10.3. Vai como ponto obrigatório do 11B.

---

## 7. Marcação para a Fase 4 — ADC 58

A modulação ressalva valores pagos e veda dedução ou compensação de diferenças apuradas pelo
critério anterior. O manual é de 2016 e opera sob TR + 1% ao mês.

**No segmento A a marcação é geral, não pontual.** Busca rodada sobre as pp. 209–223:

| Termo | Ocorrências |
|---|---|
| `compensa` | **0** |
| `dedução de diferenças` | **0** |
| `ADC 58` | **0** |
| `IPCA` | **0** |

Não há regra de dedução ou compensação em 10.1 — logo não há conflito específico a marcar.
**O conflito, se existir, está no segmento C**, onde há valor pago e dedução. Marcado como
ponto obrigatório do 11B.

---

## 8. Pendências

Sete, listadas em `bloco-11a-imputacao.md` § 9. As que pesam:

- **P11A-02** — 2.820,40 e 5.109,98 não reproduzem por via declarada alguma. Regra oculta;
- **P11A-04** — dois valores simultâneos do mesmo INSS (649,83 para deduzir, 906,64 para
  recolher), sem critério declarado;
- **P11A-05** — o método agregado de juros vincendos de 10.1 diverge em procedimento do
  método linha a linha do cap. 7, e só coincide sob acréscimo uniforme. O manual não adverte.

---

## 9. Cobertura

**78,1% do PDF**, conferido por script — contra 74,9% ao fim do bloco 10. O mapa agora separa
o que o enunciado pediu que fosse separado:

| | Páginas |
|---|---|
| Cobertas | **368** |
| Não cobertas **com decisão registrada** | **81** |
| Não cobertas **sem decisão** | **14** |

As 81 com decisão são o restante do capítulo 10 (54 pp., blocos 11B–11D) e o capítulo 16
(27 pp., varredura dirigida, P10-C16). **As 14 sem decisão são os capítulos 8, 12 e 14** — e
continuam sem destino atribuído.

---

## 10. Lição de método

O bloco 10 fechou com a observação de que cobertura declarada não é cobertura verificada.
Este bloco acrescenta a versão fina do mesmo problema:

> **Fronteira de segmento não é fronteira de página.** O enunciado, o sumário e a numeração
> impressa concordavam em dizer que 10.1 terminava na p. 222. Os três estavam errados, e o
> erro escondia o achado mais grave do segmento.

A varredura estrutural antes de extrair — Tarefa 0 — foi o que evitou isso. Vale como padrão:
**medir o capítulo antes de dividi-lo**, e medir do texto, não do índice.
