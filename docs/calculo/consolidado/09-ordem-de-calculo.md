# Ordem de cálculo, ponta a ponta

**Este arquivo existe porque a ordem não está em lugar nenhum do corpus.** O manual **ensina
cada operação e nunca as encadeia**. O Procedimento das duas skills é **composição declarada**
— não é citação (`../extracao/bloco-16-relatorio.md` § 6).

Aqui a composição fica **visível, atribuída e contestável**: cada passo traz **de onde veio a
sua posição** e **quanto custa errá-la**, quando isso foi medido.

> **Nota de nome — e ela é um caso da própria regra deste bloco.** O enunciado pediu
> `08-ordem-de-calculo.md`. O número **08 já estava ocupado** por
> [`08-nacional-e-regional.md`](08-nacional-e-regional.md), criado no bloco 16. Duas coisas
> distintas reivindicaram o mesmo identificador porque o identificador carregava **ordem de
> criação** como se fosse **semântica**. Resolvido pelo próximo livre: **`09-`**. O prefixo é
> de arquivo, não de conteúdo — mesma armadilha que `01-dominio-e-invariantes.md` § 2.9
> registra para as cadeias `trab.hist.*`, que são nacionais apesar do prefixo.

---

## 1. A afirmação central é uma negativa — e esta é a busca que a sustenta

> **O corpus não enuncia, em nenhum ponto, a ordem de cálculo do começo ao fim.**

**Escopo da busca:** os **74 arquivos `.md` de `docs/calculo/`** — consolidado, extração,
confronto normativo, armadilhas, pendências, presets e base normativa. Comando: `grep -ric`,
case-insensitive, recursivo, `--include=*.md`.

| Termo buscado | Ocorrências | Onde, e o que são |
|---|---|---|
| `ordem de cálculo` | **3** | `06-encargos.md` § 9 (título desta espinha) e `bloco-16-relatorio.md` (2×, o registro da lacuna) |
| `ordem do cálculo` | **0** | — |
| `sequência de cálculo` | **2** | `06-encargos.md` (uma linha sobre gratuidade) e `bloco-13a-...-detalhe.md` (uma asserção de cap. 16) |
| `ponta a ponta` | **2** | **ambas** em `bloco-16-relatorio.md`, e **ambas afirmando a ausência** |
| `fluxo de cálculo` · `etapas do cálculo` · `ordem geral` | **0** cada | — |
| `passo a passo` | **1** | `01-plano-extracao.md`, sobre o método de extração, não sobre a conta |
| `ordem das operações` | **5** | todas sobre **correção × juros** dentro do item 10.1 — escopo de uma operação |
| `roteiro` | **35**, em 10 arquivos | **todos internos a uma única operação**: o roteiro do INSS (9.2.x), a moldura A–J de 10.3.1/10.3.2, o do gross-up e o do 12-A/12-B |

**E a busca pela categoria que a extração já usava para isto:** o rótulo
`ordem-de-operacoes` do inventário de asserções tem **8 ocorrências**, todas em
`bloco-13a-descontos-proporcionais-detalhe.md`, `pagina_pdf` **314 a 335** — capítulo 16,
minutas. **As oito são locais**: teto da multa diária medido depois da correção (330),
decomposição do saldo na amortização (328), refazer os descontos na reatualização (323),
gross-up (325), juros decrescentes (329), reatualização do INSS com Selic (315), Fazenda em
duas etapas (335), tabelas de época no INSS (314). **Nenhuma encadeia dois blocos do cálculo.**

> **O que a busca NÃO cobre, declarado:** o **PDF do manual não está no repositório**. A
> varredura incide sobre a extração dele, não sobre o original. Um enunciado de ordem global
> que a extração tenha deixado passar **não seria visto por esta busca**. O que se afirma é:
> **em 74 arquivos de extração e consolidação, ninguém registrou tal enunciado — e o bloco 16
> registrou expressamente o contrário.**

---

## 2. Os três rótulos

| Rótulo | Significado |
|---|---|
| **`FONTE`** | o corpus **enuncia** este passo **nesta posição**. Vem com item e `pagina_pdf` |
| **`DERIVADO`** | a posição **decorre de invariante**. Vem com a invariante |
| **`COMPOSIÇÃO`** | **ninguém enuncia esta posição.** É escolha deste projeto |

**Regra de aplicação:** o rótulo qualifica **a posição do passo na cadeia**, não o conteúdo do
passo. Um passo cujo *conteúdo* é literal mas cuja *posição* ninguém fixou é **`COMPOSIÇÃO`** —
e o passo 15 é exatamente isso. **Na dúvida, `COMPOSIÇÃO`.**

---

## 3. A ordem composta — dezenove passos

```
 1 classificar     →  2 (data,eixo)  →  3 regime   →  4 adc58   →  5 parâmetro
 6 verbas          →  7 cadeia       →  8 corrigir+juros
[  9 descarregar   → 10 B/C/D        → 11 deduzir  → 12 base-c/desc → 13 ratear → 14 marco final ]
15 descontos       → 16 INSS→IR      → 17 honorários → 18 custas de execução → 19 registrar
```

Os passos **9 a 14** só existem **se houve pagamento, depósito ou acordo** antes do resultado
final. **Eles não são um apêndice no fim:** ver § 4.

| # | Passo | Rótulo | Fonte / invariante | Custo de errar a posição |
|---|---|---|---|---|
| 1 | Classificar jurisdição e se a devedora é Fazenda Pública | **DERIVADO** | **R9**, **R7** (`01-dominio` §§ 2.4) | **não medido** |
| 2 | Fixar o par **`(data, eixo)`** de cada ponto de corte | **DERIVADO** | **R19**; `00-calendario-de-cortes.md` §§ 1–2 | **não medido** |
| 3 | Resolver o **regime temporal** de cada competência | **DERIVADO** | **R22** (`01-dominio` § 2.8) | **não medido** |
| 4 | Avaliar **`pr.adc58-item-i` ANTES de `pr.imputacao`** | **DERIVADO** | **R22**; `05-imputacao.md` § 4 | **não medido** |
| 5 | Resolver **parâmetros**: `(parâmetro, categoria, competência)` e `(regra, tribunal, competência)` | **DERIVADO** | **R22**, **R14–R18**, **R24** | **não medido** |
| 6 | Apurar **verbas e reflexos** | **COMPOSIÇÃO** | — ver § 4.1 | **não medido** |
| 7 | Montar a **cadeia temporal** `período → regra`, sem lacuna nem sobreposição | **DERIVADO** | **R2**, e **R1**/**R3** sobre ela | **não medido** |
| 8 | **Corrigir o principal** e aplicar **juros sobre o CORRIGIDO** | **FONTE** | item **10.1**, `pagina_pdf` **209** | **−2,48%** / **−3,15%**; ordem interna: **0,00** |
| 9 | **Descarregar** — excluir do saldo os juros nele contidos (letra **A**) | **FONTE** | **10.3.1**, letra A, `pagina_pdf` **237**; **R23** | **+R$ 30.452,43** |
| 10 | Atualizar o principal **sem juros** até a amortização (**B**), juros do ajuizamento até ali (**C**), somar (**D**) | **FONTE** | **10.3.1**, `pagina_pdf` **237** | **não medido** |
| 11 | **Deduzir o valor pago, NOMINAL** (**E**) | **FONTE** | **10.3.1**, letra E, `pagina_pdf` **237** | **não medido** |
| 12 | Ramo **com descontos**: a base é o bruto **já reduzido do INSS e IR proporcionais ao levantamento** | **FONTE** | **10.3.2.1**, `pagina_pdf` **239–241** | **não medido** |
| 13 | **Ratear o saldo entre principal e juros** (**F** em 10.3.1, **G** em 10.3.2) | **FONTE** | **10.3.1/10.3.2**, `pagina_pdf` **237**, **239–241** | **até 23,83%** do saldo |
| 14 | Levar ao **marco final** (**G/H → J**) | **FONTE** | **10.3.1**, `pagina_pdf` **237–238** | **não medido** |
| 15 | **Descontos finais sobre o resultado** — depois dos juros, não antes | **COMPOSIÇÃO** | — ver § 4.5 | **−R$ 285,83** |
| 16 | **INSS sempre antes do IR**; base do IR é o **líquido de INSS** | **FONTE** | **9.1**, `pagina_pdf` **107**; **9.3.6**, `pagina_pdf` **185** | **não medido** *(a ordem INSS→IR em si)* |
| 17 | **Honorários advocatícios** sobre o bruto do reclamante + FGTS, **excluída a cota patronal** | **COMPOSIÇÃO** | — ver § 4.6 | **não medido** |
| 18 | **Custas de execução** depois dos honorários: `0,5%` sobre o total **antes da própria linha** | **DERIVADO** | **R8-CE-01**; literal de **8.2.1**, `pagina_pdf` **101** | **não medido** |
| 19 | **Registrar** preset por competência, *overrides*, versões | **DERIVADO** | **R13**, **R19**, **R20**, **R21** | **não medido** |

**Contagem:** 19 passos — **8 `FONTE`**, **8 `DERIVADO`**, **3 `COMPOSIÇÃO`**.
**Custo medido em 4 passos** (8, 9, 13, 15); **não medido em 15**.

> **Os oito `FONTE` concentram-se num só trecho:** sete deles (9 a 14, e o 8) estão no
> **capítulo 10**, e seis dentro da **moldura A–J**. Fora desse trecho, o único `FONTE` é a
> ordem **INSS → IR** do item 9.1. **É esta a forma exata da lacuna:** o corpus é denso em
> ordem *dentro* de cada operação e mudo na ordem *entre* operações.

---

## 4. O raciocínio de posição — por que aqui e não noutro lugar

### 4.1 Passo 6 — verbas: a junção com a atualização não tem fonte

A **única costura lexical** disponível é o item **9.1** (`pagina_pdf` 107): *"Devem ser
deduzidos **do crédito do reclamante**"* — o que pressupõe o crédito apurado, mas **não fixa
posição**: não diz se o crédito entra corrigido, nominal, ou com juros.

Nada no corpus manda apurar verbas **antes** de montar a cadeia. A ordem é escolha deste
projeto, e a razão é de **dependência de dados**, não normativa: a cadeia (passo 7) precisa
conhecer a **competência da parcela mais antiga** para satisfazer **R2**, e isso só existe
depois da apuração.

**Contestação possível:** quem tratar a cadeia como **atributo do processo**, e não do conjunto
de parcelas, pode montá-la antes. **Não muda número** — muda o momento em que uma lacuna de
cobertura aparece. **Não medido.**

### 4.2 Passos 3 e 4 — regime antes de parâmetro, e ADC 58 antes da imputação

**R22 é o que põe o passo 3 antes do 5**, e `parametro_consultavel()` levanta
`RegimesNaoAvaliados` se a ordem for invertida. A razão está em `01-dominio` § 1: **a camada 1
decide se a camada 2 é sequer consultada** — sob `pr.in-itinere` variante `suprimidas`, o
parâmetro `pn.in-itinere.prefixacao` **não existe**, não vale zero.

**O passo 4 é o mesmo argumento aplicado à imputação** (`05-imputacao.md` § 4): em **i.1**
— pagamento consolidado — **o pago sai da conta, e não há o que ratear**. Avaliar
`pr.imputacao` primeiro seria consultar um parâmetro de um ramo que a camada 1 já fechou.

> **Ressalva de origem, e ela não se resolve aqui.** A distinção i.1 × i.2 vem de **pesquisa
> jurisprudencial externa ao corpus**; **o inteiro teor dos três precedentes do TST não foi
> lido** (`05-imputacao.md` § 4, nota final). A **posição** do passo 4 é `DERIVADO` de R22; o
> **conteúdo** do preset continua com a ressalva aberta.

### 4.3 Passos 9 a 14 — a imputação parte a linha do tempo em duas

**Este é o ponto em que a ordem deixa de ser arrumação e vira número.**

A amortização **não é um passo a mais no fim**. Tudo é trazido **até a data do levantamento**,
**rateado ali**, e só então levado ao marco final (`05-imputacao.md` § 2). O demonstrativo tem
**duas pernas**: ajuizamento → levantamento, e levantamento → marco final. **O valor pago é
deduzido NOMINAL** — o que se atualiza é o crédito; nenhuma linha de levantamento tem coluna de
índice preenchida.

**Por que pôr no fim muda o número:** deduzir o pago do total já atualizado até o marco final
aplica ao crédito inteiro o índice e o percentual de juros de **todo** o intervalo, quando parte
dele já havia sido satisfeita. O rateio **F.1/F.2** existe justamente para decidir **quanto do
que sobra é principal** — e só o principal segue rendendo juros do período restante.

```
F.1  principal no saldo = (B / D) × E        F.2  juros no saldo = (C / D) × E
```

**Custo medido:** **até 23,83% do saldo** (Exemplo 1), pela escolha do critério de rateio —
`../armadilhas-comparador.md` § 3.2. **Direção:** juros primeiro produz saldo **maior**; o
art. 354 do CC favorece o **credor**, o critério proporcional favorece o **devedor**.

> **O critério do passo 13 é `FONTE` quanto à POSIÇÃO e SEM NORMA quanto ao CONTEÚDO.** A
> proporcionalidade é aplicada **101 vezes** e fundamentada **zero** — `art. 354` tem **zero
> ocorrências nas 471 páginas** (`05-imputacao.md` § 3). Por isso é **`pr.imputacao`, preset
> sem default** (`R20-EXCEÇÃO`). **Este arquivo não arbitra o critério** — fixa apenas onde ele
> entra.

**E qual letreiro usar:** **são duas molduras**. 10.3.1 vai de A a H e **J**, sem letra I;
10.3.2 vai até **O/P** e **tem** letra I. **Os Exemplos 5 e 6 seguem 10.3.2.** Ler o capítulo
com um letreiro só produz **erro de endereço**, não de valor (`05-imputacao.md` § 2.2).

### 4.4 Passo 9 — descarregar antes de aplicar juros

**R23**, e é o **maior delta de método do corpus**: no Exemplo 5 do capítulo 10, não descarregar
produz **+R$ 30.452,43** (`../armadilhas-comparador.md` § 3.3).

**Por que é o passo 9 e não uma checagem tardia:** a letra **A** da moldura é literalmente a
primeira. Aplicar juros sobre saldo que já os contém produz **anatocismo** — e a operação é
irreversível a jusante, porque depois da letra D principal e juros já estão somados.

> **Anomalia de fundamentação, registrada e não resolvida.** O manual **executa** o
> descarregar em todo o capítulo 10 e **não o fundamenta**: `anatocismo` tem **zero ocorrências
> no capítulo 10 inteiro**. Quem o nomeia é uma **minuta do capítulo 16** (`pagina_pdf` 328).
> A posição é `FONTE`; o fundamento está fora do lugar onde a operação vive
> (`01-dominio` § 2.2).

### 4.5 Passo 15 — a posição dos descontos é `COMPOSIÇÃO`, e tem custo medido

**O que é `FONTE`:** que o INSS precede o IR (passo 16), e que a base do IR é o líquido de INSS.

**O que NÃO é `FONTE`:** que o bloco de descontos venha **depois** dos juros. O item 10.1 **faz
isso na aritmética** do exemplo, mas **não o enuncia**. A prova é a medição inversa: deduzir
INSS **antes** dos juros na base do IR dá **4.824,15 contra 5.109,98 — −R$ 285,83**
(`../armadilhas-comparador.md` § 3.1; `bloco-11a-imputacao.md` § 3, que conclui: *"as três
decisões acima são de base, e duas delas o manual não enuncia"*).

**Por isso `COMPOSIÇÃO`, com custo medido.** É o rótulo que o bloco quer: posição praticada,
não declarada, e com preço conhecido.

> **E há dois momentos de desconto, não um.** No ramo com pagamento parcial, os descontos
> **proporcionais ao levantamento** entram no **passo 12**, dentro da amortização; os descontos
> **sobre o resultado** entram no passo 15. **Em 10.3.2.1 os tributos também são rateados** —
> *"regra estrutural que só existe na aritmética"* (`05-imputacao.md` § 2.1). **E o rateio de
> 10.2 não é o de 10.3:** em 10.3 rateia-se **principal × juros**; em 10.2, **bruto → INSS**.
> Objetos distintos, **e a mesma lacuna: nenhum dispositivo citado para nenhum dos dois**.

### 4.6 Passos 17 e 18 — onde entram os encargos, e a ordem entre eles

**A posição do bloco de encargos depois do resultado é `COMPOSIÇÃO`.** O capítulo 8 diz o que
entra e o que sai da base; **não diz quando a base fica pronta**. A espinha que hoje a enuncia
— `06-encargos.md` § 9 — abre com *"apuração das verbas e descontos"* **como caixa-preta**, e é
essa caixa que os passos 6 a 16 abrem.

**A ordem ENTRE os dois encargos, ao contrário, é `DERIVADO` — e por literal.** O item 8.2.1
(`pagina_pdf` 101) manda excluir da base das custas de execução **apenas** as custas do
conhecimento: *"Nenhuma outra verba deverá ser excluída da base, **nem mesmo imprensa oficial e
honorários**, salvo determinação judicial contrária"*. **Se os honorários entram na base da CE,
os honorários têm de estar calculados antes dela.** Somado a **R8-CE-01** — a base é o total
**antes da própria linha de CE** —, a ordem fica fixada sem escolha.

**O que continua aberto e este arquivo não fecha:** o **estado** em que o crédito entra na base
da CE — bruto ou líquido — **não é endereçado** pelo capítulo 8 (`bruto` e `líquido`: **zero
ocorrências** nos itens 8.2 e 8.2.1). É a pendência **P13B-01**.

**E a gratuidade muda a conta, não a ordem:** os honorários devidos pelo reclamante beneficiário
**não se abatem do seu crédito** (ADI 5766) — **some uma parcela** da cadeia de descontos sobre
o líquido, sem deslocar passo algum.

### 4.7 Passo 8 — a pergunta que não é produtiva

**A ordem entre correção e juros é indiferente.** Distributividade, **delta `0,00` verificado**:

```
manual : (4.066,41 × 1,02538895) × (1 + 31,266667%) = 5.473,36
inversa: (4.066,41 + 4.066,41 × 31,266667%)         = 5.473,36
```

**O que altera é a BASE.** Juros sobre o **nominal** em vez do corrigido: **−2,48%**; com juros
vincendos, **−3,15%**. E **sob juros vincendos o segundo critério do item 10.1 torna-se
obrigatório** — regra enunciada, `pagina_pdf` 209 —, **com a ressalva de que a obrigatoriedade
não tem lastro demonstrativo** e o critério 1 é inexecutável a partir do publicado
(pendência **P10D-04**, `05-imputacao.md` § 1).

---

## 5. Os deltas de método, reunidos

De `../armadilhas-comparador.md` § 3, conferidos linha a linha contra a fonte.

| Decisão de posição / base | Efeito medido | Passo | Bloco |
|---|---|---|---|
| **Não descarregar** (viola **R23**) | **+R$ 30.452,43** — o maior delta de método do corpus | **9** | 11A/11B |
| **Ordem de imputação** (art. 354 × proporcional) | até **23,83%** do saldo (Exemplo 1) | **13** | 11B |
| Juros sobre o **nominal** em vez do corrigido | **−2,48%** | **8** | 11A |
| Idem, em cálculo com **juros vincendos** | **−3,15%** | **8** | 11A |
| Deduzir **INSS antes dos juros** na base de IR | **−R$ 285,83** | **15** | 11A |
| **Ordem entre correção e juros** | **delta `0,00`** — distributividade | **8** | 11A |

> **A última linha é a mais instrutiva do quadro.** A pergunta *"qual a ordem das operações?"*
> tem resposta **não importa**. A pergunta produtiva é **"sobre que base cada uma incide?"** —
> e é aí que estão os −2,48%, os −3,15% e os −R$ 285,83.

**Os outros quinze passos não têm custo medido.** Não é omissão a suprir por inferência: é o
estado da verificação. **"Não medido" é o registro correto** — e é o que distingue uma posição
*escolhida* de uma posição *validada*.

---

## 6. As duas composições atuais — e onde divergem

As skills [`calculo-judicial-core`](../../../skills/calculo-judicial-core/SKILL.md) e
[`calculo-trabalhista-liquidacao`](../../../skills/calculo-trabalhista-liquidacao/SKILL.md)
traziam, até este bloco, **duas ordens escritas em separado**. **Quatro divergências reais:**

| # | Divergência | Qual prevalece |
|---|---|---|
| **D1** | **O core não tem passo de encargos.** Sua sequência termina em `REGISTRAR`; a de liquidação tem `Passo 8 — encargos` | **A de liquidação**, e por `06-encargos.md` § 9. O core é a camada de invariantes, não de apuração — **omissão de escopo, não conflito** |
| **D2** | **Endereço do descarregar.** O core o aloja em `ATUALIZAR` (*"se houve pagamento parcial, descarregar ANTES"*); a liquidação, na imputação (Passo 7, letra A) | **A liquidação.** O descarregar é a **letra A da moldura**, não uma pré-condição da atualização. Mesmo lugar aritmético, endereços diferentes — **sem efeito de valor** |
| **D3** | **Descontos × imputação.** A liquidação numera `Passo 5 — descontos` **antes** do `Passo 7 — imputação`, sugerindo **um** bloco de descontos. São **dois momentos** (§ 4.5) | **Este arquivo.** Em 10.3.2.1 os descontos proporcionais ao levantamento entram **dentro** da amortização; os finais, depois. A numeração linear da skill não comporta os dois |
| **D4** | **Escopo declarado × conteúdo.** O cabeçalho da liquidação anuncia `verbas → descontos → encargos`, *"antes de atualizar"* — mas o Passo 7 **exige atualizar** até a data do levantamento | **Este arquivo.** A própria skill já registra a tensão (*"um caso de fronteira que não é fronteira"*); o que faltava era a ordem onde a perna intermediária aparece |

**Duas diferenças que NÃO são divergência:** o core tem `Passo 0 — CLASSIFICAR` (jurisdição e
Fazenda, **R9**) e a liquidação não — ela já opera dentro de uma jurisdição; e o `Passo 0` da
liquidação, o par `(data, eixo)`, é no core uma nota do `Passo 1`. **Mesma ordem, granularidade
diferente.**

**E uma lacuna comum às duas, corrigida aqui:** **nenhuma** das duas enuncia que
`pr.adc58-item-i` é avaliado **antes** de `pr.imputacao` — o passo 4. Não é divergência entre
elas; é ausência nas duas.

---

## 7. O que este arquivo NÃO faz

- **não arbitra `pr.imputacao`** — segue **sem default**, `R20-EXCEÇÃO`. Fixa a **posição**, não
  o **critério**. Pendência **P11B-07**, aberta;
- **não harmoniza as três posições sobre a data da dedução** — levantamento, depósito ou
  pagamento. Pendências **P11B-06** e **P13C-01** (`05-imputacao.md` § 5);
- **não decide o estado (bruto ou líquido) da base das custas de execução** — **P13B-01**;
- **não fecha a alternativa da letra I de 10.3.2**, sem exemplo em todo o capítulo 10 —
  **P10D-05**;
- **não altera conteúdo normativo.** Nenhum número, corte, eixo ou invariante muda por este
  arquivo. Ele **nomeia posições** e **atribui autoria** a elas;
- **não substitui os dois bloqueios abertos** do capítulo 10 — **P11B-01** (p. 266, delta de
  10,00 exatos) e **P10D-01** (p. 269, delta de 2.036,51). Nenhum é arredondamento.

---

## 8. Ponteiros

| Assunto | Arquivo |
|---|---|
| R1–R24, três camadas, precedência | [`01-dominio-e-invariantes.md`](01-dominio-e-invariantes.md) |
| Cortes e eixos | [`00-calendario-de-cortes.md`](00-calendario-de-cortes.md) |
| Cadeias, defasagens, ADC 58 | [`02-atualizacao.md`](02-atualizacao.md) |
| Verbas e reflexos | [`03-verbas.md`](03-verbas.md) |
| INSS, IR, RRA | [`04-descontos.md`](04-descontos.md) |
| Moldura A–J, rateio, descarregar, item "i" | [`05-imputacao.md`](05-imputacao.md) |
| Honorários, custas, precatórios | [`06-encargos.md`](06-encargos.md) |
| Como o manual se lê | [`07-leitura-do-corpus.md`](07-leitura-do-corpus.md) |
| Nacional × regional, R24 | [`08-nacional-e-regional.md`](08-nacional-e-regional.md) |
| Deltas de método e defeitos do original | [`../armadilhas-comparador.md`](../armadilhas-comparador.md) |
| O registro da lacuna que originou este arquivo | [`../extracao/bloco-16-relatorio.md`](../extracao/bloco-16-relatorio.md) § 6 |
| O que segue aberto | [`../pendencias.md`](../pendencias.md) |
