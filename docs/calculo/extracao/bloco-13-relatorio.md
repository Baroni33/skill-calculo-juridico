# Bloco 13 — relatório

**Último bloco de extração.** Segmento B do capítulo 10, capítulos 8, 12 e 14, e varredura
dirigida do capítulo 16.

**Os dois PDFs fecham em 100%.**

---

## 1. Entregas

| Parte | Escopo | Estado |
|---|---|---|
| A | Cap. 10, segmento B (pp. 223–237) | **Feita** — `bloco-13a-descontos-proporcionais.md` |
| B | Cap. 8 (pp. 100–106) | **Feita** — `bloco-13b-encargos.md` |
| C | Cap. 12 (pp. 299–302) | **Feita** — `bloco-13c-sindical-precatorios.md` |
| D | Cap. 14 (pp. 304–306) | **Feita** — idem |
| E | Cap. 16 (pp. 310–336) | **Feita** — `bloco-13e-capitulo16.md` |
| — | Detalhe consolidado das três frentes | `bloco-13a-descontos-proporcionais-detalhe.md` |
| — | Mapa de cobertura final | **100%, conferido por script** |

**212 testes OK.** Cinco armadilhas novas em `armadilhas-comparador.md` (10 → 15).

---

## 2. O mapa fecha — e a contagem final

| Manual | Páginas | Cobertas | Pré-textuais com decisão | **Sem decisão** |
|---|---|---|---|---|
| TRT-3 (julho/2016) | 471 | **463** | 8 | **0** |
| CJF (Res. 990/2026) | 93 | **83** | 10 | **0** |
| **total** | **564** | **546** | **18** | **0** |

**Nenhuma página sem destino registrado.**

### 2.1 Duas ressalvas de natureza, para que o número não engane

**O capítulo 16 foi coberto por varredura dirigida, não por extração integral.** As 27 páginas
foram lidas e cruzadas; o que não é regra de cálculo — endereçamento, fecho, pedido de prazo —
**foi deliberadamente não extraído**. É decisão registrada, não lacuna.

**E o manual federal nunca teve "93 páginas integrais".** Desde o bloco 8 ele era assim
descrito. Os **capítulos ocupam 80 páginas**; 13 são pré-textuais, das quais **3 têm conteúdo
normativo** — a Apresentação (critérios da Lei 14.905/2024) e a Resolução 990/2026. Essas três
**estão cobertas**; a imprecisão era de contagem, não de leitura. Corrigida no mapa.

---

## 3. Sete premissas do enunciado caíram

Recorde da série, e todas eram minhas.

| Premissa | Realidade |
|---|---|
| "a regra de arredondamento do NMP nunca é declarada" (blocos 11B e 11C) | **Está declarada**, pp. 226 e 230, com o artigo transcrito. Ver § 4 |
| "percentual pleno de IR no saldo contra `0,9091`" (P11B-03) | **`0,9091` não é percentual de IR — é o IPIR.** Erro meu de leitura de rótulo |
| "16.4.11 está na `pagina_pdf` 335" (bloco 12) | **Está em 333–334** |
| "16.4.7 é caso de fundamentar só na minuta" (bloco 12) | **Falso.** O cap. 6, p. 77, enuncia a regra com o texto **íntegro** da OJ 54 — melhor que a minuta |
| "a p. 328 é o único lugar com `anatocismo`" (bloco 12) | **Parcial.** Ocorre nas pp. 16, 90, 328 e 335. Exclusiva é a **aplicação à amortização** |
| "o sumário lista `8.2.1`" | Não lista. O item existe no corpo, com título mais longo |
| "as faixas do art. 85, § 3º, do CPC estão em `02-base` § 10" | **§ 10 é outra coisa.** As faixas **não existem no repositório** — nova pendência P8-F4-02 |

Somam-se às cinco do bloco 11C e às duas do 12. **A regra que as apanha é sempre a mesma:
exigir a busca que sustenta a afirmação, inclusive quando a afirmação é minha.**

---

## 4. P11B-02 — a pendência que se fecha corrigindo um erro meu

Escrevi em dois blocos que *"a regra de arredondamento do NMP nunca é declarada"* e a tratei
como inferência (1 casa, half-up). **Ela é declarada, duas vezes**, nas pp. 226 e 230 — no
único segmento do capítulo 10 que eu ainda não extraíra:

> "deverá ser observada a regra de arredondamento prevista no **parágrafo único do 45 da
> Instrução Normativa 1500/14**"

E **não é half-up.** É regra de três ramos: 2ª casa `<5` mantém · `>5` sobe · **`=5` manda
olhar a 3ª casa** (0–4 mantém, 5–9 sobe). **Difere de `ROUND_HALF_UP` na faixa `x,y50` a
`x,y54`.**

Vai para a espinha como **regra literal**. E é lição de método: **afirmei uma negativa sobre um
trecho que ainda não tinha lido.** A varredura que a sustentava cobria só o que eu extraíra.

---

## 5. O que o bloco acrescentou de substantivo

### 5.1 Um defeito grave que propaga para dentro de um segmento já extraído

A fórmula fechada do bruto levantado, pp. 227 e 231, tem o **colchete fechado cedo demais**.
Lida à risca dá `318.618,21`; com o colchete correto dá **`322.389,94`** — exatamente o
impresso, delta **0,00**.

**O próprio manual publica a forma correta duas páginas depois** (10.2.2.1, p. 233). E **a
versão errada propaga para as pp. 244 e 250**, já no segmento C. Armadilha **A11**.

Nuance que importa ao comparador: **com `INSS = 0` as duas leituras coincidem** — e os
exemplos do art. 12-B usam `INSS = 0,00`, logo não exercitam o defeito.

### 5.2 P10-18 reclassificada: a causa era outra

O bloco 10 registrou divergência entre a base das custas do cap. 9 e a do cap. 11, atribuída a
bruto × líquido. **A causa é o juro Selic sobre a cota-reclamante:**

```
606,12 − 570,83 = 35,29     e     30.312,81 − 30.277,52 = 35,29
```

`bruto ≡ líquido + INSS recte SEM Selic`. **Deixa de ser divergência normativa e vira defeito
de rótulo** (A12). E o `151,39` **não é impresso em nenhuma das 471 páginas** — era valor
derivado da análise.

### 5.3 O manual se contradiz sobre quem é Fazenda Pública

| Onde | Teste de isenção das custas de execução |
|---|---|
| **Cap. 8, p. 102** | entes públicos **"que não explorem atividade econômica"** (art. 790-A) |
| **Cap. 14, p. 306** | administração **"direta e indireta"**, inclusive fundações e autarquias — **sem a ressalva** |

Para um ente da administração indireta que explore atividade econômica, **os dois capítulos
dão respostas opostas**.

**Consequência registrada: o manual não pode ser fonte para resolver a pendência 1 da § 9 da
base normativa.** `economia mista` tem **zero ocorrências nas 471 páginas**; a única
equiparação nominada é a ECT, e só *"para efeito de execução e do DL 779/1969"*.

**Não resolvi a classificação** — não é matéria de cálculo. A condicional fica nos dois ramos.

### 5.4 Uma terceira posição sobre a data da dedução

O cap. 14, p. 306, letra "c", manda *"amortizar com observância da **data do pagamento** e não
da data do levantamento"*. São **três posições no mesmo manual**:

| Onde | Data |
|---|---|
| Cap. 10 | **levantamento**, em todos os exemplos, sem fundamento citado |
| Cap. 16, item 16.4.11 | **duas teses**, separadas pela **finalidade do depósito** |
| Cap. 14, p. 306 | **pagamento**, "salvo determinação do juízo" |

**E o critério do 16.4.11 é exatamente o eixo do preset `pr.adc58-item-i`** — a *natureza do
depósito*, aferida pelo código da guia ("código 02" = pagamento) e pela cronologia (precedeu
os embargos = garantia). **O eixo não foi invenção da modelagem: é o que o manual usa.**

### 5.5 O capítulo 16, reavaliado com números

Dos **36 fundamentos** cruzados, **a maioria É citada** pelo capítulo técnico. **Seis não
são** — e um deles é a **IN SRF 15/2001**, fonte declarada da fórmula de *gross-up*, com **uma
única ocorrência em 471 páginas**, enquanto "bruto em relação ao líquido" ocorre em 16 páginas,
**15 delas no capítulo 10**.

**A reclassificação para fonte normativa está confirmada — e a lição fica mais estreita e mais
útil do que a que eu escrevera no bloco 12.** Não é que o capítulo 16 seja a fonte do manual.
É que **há operações centrais cuja única fundamentação está fora do capítulo que as executa**.

---

## 6. Aritmética e bloqueios

**Segmento B: tudo fecha em 0,00 em precisão plena.** 44 operações em `Decimal` prec=50. A
cadeia completa de 10.2.1.1 e 10.2.1.2 devolve exatamente `282500.00000000000000000000` —
zero casas residuais.

**Nenhum bloqueio novo.** Os dois padrões dos segmentos C e D — o delta de `10,00 exatos` e o
índice implícito sem origem — **não reaparecem**. Maior delta: **0,66**, com origem
identificada.

**Os dois bloqueios anteriores permanecem abertos:** P11B-01 (p. 266) e P10D-01 (p. 269).

---

## 7. Defeitos catalogados

| Frente | Nº |
|---|---|
| Segmento B | 15 |
| Caps. 8, 12 e 14 | 20 |
| Cap. 16 | 12 |

Cinco promovidos a `armadilhas-comparador.md` — **A11** (colchete da fórmula), **A12** (rótulo
do cap. 9), **A13** (base do percentual de honorários), **A14** (teto rural de 2011), **A15**
(OJ 54 truncada). O arquivo passa de **10 para 15** armadilhas.

**Verificação literal:** 60 citações conferidas por script nos caps. 8/12/14 (**0 falhas**) e
39 no cap. 16 (**0 falhas**).

---

## 8. O que a Fase 3 recebe

**A extração está encerrada.** Os dois manuais têm destino registrado em todas as 564 páginas.

**Aberto, por peso:**

1. **Dois bloqueios aritméticos** — P11B-01 e P10D-01, nenhum absorvível por arredondamento;
2. **P11B-07** — o critério de imputação sem norma, já modelado como preset sem default;
3. **P13B-02** — o manual se contradiz sobre Fazenda Pública; a pendência 1 da § 9 **não pode
   ser fechada por ele**;
4. **P8-F4-02** — as faixas do art. 85, § 3º, do CPC **não existem no repositório**;
5. **P10D-04** — a obrigatoriedade do critério alternativo da letra C, declarada e não
   demonstrada;
6. **P10D-08** — migração de regime tributário sem disciplina em todo o manual;
7. **A origem externa da § 1.1** — o inteiro teor dos três precedentes do TST **não foi lido**.

**Sólido:** 564 páginas com destino · 15 armadilhas com assinatura detectável · 28 regimes ·
212 testes · onze cadeias temporais validadas por R1/R2 · e a disciplina de não harmonizar
mantida em treze blocos.

---

## 9. Lição de método — a que a série inteira sustenta

Cada bloco fechou com uma lição. A do último é a que as reúne:

> **A negativa é a afirmação mais perigosa que um extrator faz, e a mais fácil de fazer sem
> perceber.**

Neste bloco eu errei uma negativa **duas vezes seguidas** — "a regra de arredondamento nunca é
declarada" — porque a varredura que a sustentava cobria **só o que eu já tinha extraído**. A
regra estava nas 13 páginas que faltavam.

O corretivo não é desconfiar mais: é **declarar o escopo da busca junto com o resultado**.
"Zero ocorrências" sem dizer *em quantas páginas* é uma afirmação que não pode ser auditada — e
foi exatamente assim que sete premissas atravessaram três blocos.

**O que funcionou, e vale manter na Fase 3:** exigir a busca ao lado da negativa; reproduzir
toda conta em `Decimal`; e tratar premissa do enunciado com o mesmo ceticismo que se trata
afirmação do manual. Das quatorze premissas derrubadas na série, **nenhuma veio do manual —
todas vieram de quem estava conduzindo a extração.**
