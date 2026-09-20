# Bloco 17 — correções estruturais antes da aceitação

**Estado: fechado.** Seis correções aplicadas, nenhuma de conteúdo normativo. **253 testes OK**,
três validadores nos números prometidos, nenhuma `SKILL.md` acima de 500 linhas.

| Verificação | Antes | Depois |
|---|---|---|
| `valida_bloco_tabelas.py` | `14 ok, 31 div, 1 n/v, **10 erros**` | **`15 ok, 31 div, 1 n/v, 0 erros`**, exit 0 |
| `valida_cadeias.py` | 11 cadeias · R1 15 · R2 1 | **11 · 15 · 1** · **R3: 25** (novo) |
| Suíte | 214 testes | **253** |
| Segmentos com `tipo_indexador` | **0 de 97** | **97 de 97** |

---

## 1. O campo `tipo` — e os dez que ficaram `indeterminado`

**R3 era letra morta.** O campo não existia em série nenhuma, e a virada entre tipos sem ajuste
de defasagem **desloca o cálculo em um mês sem produzir sintoma**.

**A fonte é estreita, e foi respeitada.** O item 4.1.2.4 do Manual CJF (`pagina_pdf` 42) nomeia
**Ufir, BTN, OTN, ORTN** como nominais e **INPC, IGP-DI, IGP-M** como percentuais — **e mais
nada**. As listas são exemplificativas, *"o que **não** autoriza estendê-las por semelhança de
nome"*.

| Classe | Quantos | Quais |
|---|---|---|
| **nominal** | 4 | ORTN, OTN, BTN, Ufir — **nomeados na fonte** |
| **percentual** | 3 | INPC, IGP-DI (fonte) e IPC/IBGE (**D8-C21**) |
| **englobante** | 2 | Selic, taxa legal — *"Selic não é índice de inflação"* (D8-C22) |
| **nao-indexador** | 9 | moedas, paridades, conversão em URV |
| **`indeterminado`** | **10** | IPCA, IPCA-E, IPCA-15, IPCA série especial, IPC/FGV, IPC-R, IRSM, MVR, **TR**, remuneração básica da poupança |

> **Dez de vinte e oito é resultado correto, não falha.** Classificar o IPCA-E como percentual
> *"porque IPCA soa percentual"* é exatamente a dedução que a tarefa proibia.

**A TR foi rebaixada.** Era `percentual` por critério **formal** — *"não é unidade monetária,
logo é percentual"* —, mas o critério **material** do item (*"refletem a inflação do próprio
mês"*) **não a alcança**: é taxa apurada **prospectivamente**. `bloco-09-relatorio.md` § 5.3 é
literal: *"nenhum dos dois manuais classifica a TR"*. **Inferência declarada não é fonte.**

**Decisão de formato:** manifesto sidecar `indexadores-tipo-catalogo.json`, não coluna nos CSV.
Três razões: um CSV tem **três** indexadores na mesma coluna; uma coluna repetiria o valor 5.104
vezes num deles; e a fonte é objeto estruturado que não cabe em célula. **Zero bytes de dado
alterados** — a integridade byte a byte dos CSV é a evidência de conferência.

**`indeterminado` numa ponta BLOQUEIA**, sob `R3-INDETERMINADO`. Passar converteria *"não se
sabe"* em *"está certo"*, e num validador cuja razão de existir é que **o erro de R3 não tem
sintoma**, o silêncio é o pior resultado. **13 viradas passaram a ser acusadas.**

---

## 2. Identificadores — e a regra de projeto que faltava

### A varredura achou mais do que o enunciado supunha

`trt3.hist.*` eram quatro. Mas **`trt3.trabalhista.*` são outras sete** — IRRF, INSS, GILRAT,
URV, RSR, incidência de parcelas, contribuição previdenciária. **Lei federal, com prefixo de
TRT.** O campo `fundamento` registra o manual do TRT-3 como **documento de origem**, não como
escopo.

**11 ids, 67 ocorrências, 23 arquivos, 4 arquivos renomeados.** Verificação: **zero resíduos,
zero remissões com sentido alterado**.

### E a renomeação mesmo assim errou — a primeira vez

Troquei `trt3.hist.trabalhista.correcao-monetaria` por `trab.hist.**privado**.correcao-monetaria`.
**A cadeia declara `dominio_condicoes: {devedor: [fazenda-publica, nao-fazenda-publica]}`** e tem
segmento com `condicao: {devedor: fazenda-publica}`. **`privado` afirma uma restrição que a
cadeia não tem** — e, existindo uma irmã `trab.hist.fazenda-publica.juros-mora`, induzia a
concluir que esta excluía a Fazenda.

**Corrigido para `trab.hist.correcao-monetaria`**, neutro. O escopo está no campo — que é
precisamente a regra que este bloco veio estabelecer, aplicada contra o próprio bloco.

### O mesmo defeito, do lado do código

`valida_cadeias.py` descobria cadeia por `p.name.startswith(("cjf.", "trt3.hist."))`. **A
renomeação o fez cair de 11 cadeias para 7 — em silêncio, seguindo a imprimir "OK" sobre as sete
restantes.** Passou a reconhecer por `tipo == "cadeia-temporal"`.

**Dois testes falharam, e estavam certos:** as guardas de `tipo_indexador` filtravam pelo mesmo
prefixo e teriam aprovado quatro cadeias que não inspecionavam.

### A regra, registrada em `01-plano-extracao.md`

> **O identificador identifica. O escopo se declara em campo.** A aplicação é decidida por
> `jurisdicao`, `tribunal`, `competencia` — **nunca pelo prefixo do id nem pelo nome do arquivo**.

**É a terceira vez que ambiguidade de etiqueta morde o projeto:** `F1`–`F9` × `F1`–`F7` no bloco
15; a renumeração `B03`/`B04` **cega**, que reescreveu *"mesma raiz do F1 do bloco 3"* como
`B04-F1`; e `RG8` contra a invariante `R8` no bloco 16.

**Decisão assimétrica, declarada:** `trt3-18.*.json` **não** foi renomeado. O **id** é `trab.*`;
o **nome do arquivo** registra proveniência, como `bloco-08-jf.md`. São coisas diferentes, e
ambas estão declaradas.

---

## 3. References — e a lacuna que a varredura achou

Criados `civel-federal.md` (371) e `desapropriacao.md` (403). `tributario-federal.md` caiu de
432 para 376 e perdeu o **aviso de escopo do topo**, que existia só por causa da lacuna.

**A varredura (c) achou uma lacuna real, e não a preenchi:** **FGTS (item 4.8, índice JAM) e
poupança (item 4.9)** do cap. 4 do CJF têm **cadeia própria e eixos que nenhuma outra usa** —
corte por **saque integral** (`D8-C12`), corte por **data de abertura da conta** (`D8-C16`), e os
expurgos do FGTS que **não dizem se substituem ou acrescem** (`D8-C13`).

> **Razão de não criar:** **zero ocorrências de `JAM` no consolidado**, e nenhuma das sete
> cadeias extraídas é FGTS ou poupança. **Consolidar vem antes de escrever `reference`.**

---

## 4. O validador com saída limpa

Os dez erros eram de **escopo**: `PAGINAS_DO_BLOCO = range(373, 472)` é constante do bloco 1, mas
a verificação de proveniência varria **todos** os CSV do diretório — e uma série da p. 178 caía no
mesmo lugar.

**A proveniência já estava no arquivo — só não estava sendo lida.** Os CSV declaram
`pagina_pdf=` no cabeçalho. Resolução por arquivo, com fallback no contrato de páginas do item, e
**`NÃO VERIFICÁVEL` quando falta as duas — nunca erro, nunca silêncio**.

> **`ok` subiu de 14 para 15, e isso não é ampliação de alcance:** a linha de proveniência só é
> emitida quando a checagem passa. Antes ela errava e não emitia OK nenhum. **As 10.732 linhas
> conferidas são as mesmas.**

Teste acrescentado que cobre exatamente o defeito — **CSV de outro bloco no mesmo diretório** —,
mais o negativo que impede virar maquiagem, e um que **falha se alguém reintroduzir a constante**.

---

## 5. A ordem de cálculo, visível e contestável

`09-ordem-de-calculo.md` — **19 passos: 8 `FONTE`, 8 `DERIVADO`, 3 `COMPOSIÇÃO`**.

> **Nota de nome:** o enunciado pediu `08-`, mas `08-nacional-e-regional.md` existe desde o bloco
> 16. Usei `09-`. **A colisão é, ela própria, um caso da regra da § 2.**

**Custo medido em 4 dos 19 passos.** Não descarregar: **+R$ 30.452,43**. Ordem de imputação: até
**23,83%**. Juros sobre o nominal: **−2,48%** (−3,15% com vincendos). INSS antes dos juros na base
de IR: **−R$ 285,83**. E a ordem entre correção e juros: **delta `0,00`** — distributividade; **o
que altera é a base**. *"Não medido"* nos outros quinze é resposta registrada, não omissão.

**O documento aplica a própria regra contra si**, que é o teste decisivo: o passo 15 é
`COMPOSIÇÃO` embora o conteúdo seja literal, *"porque o item 10.1 faz isso na aritmética mas não o
enuncia"*; e a § 4.1 **recusa** usar o item 9.1 como fonte de posição e rebaixa o passo 6.

**Quatro divergências entre as duas composições das skills**, achadas e registradas — entre elas
o core **não ter passo de encargos**, e o cabeçalho da liquidação dizer *"antes de atualizar"*
enquanto o passo 7 exige atualizar até o levantamento. E **uma lacuna comum às duas**, corrigida:
nenhuma enunciava que **`pr.adc58-item-i` precede `pr.imputacao`**.

---

## 6. Validação adversarial — três graves, e a primeira era minha

**G1 — a renomeação inverteu o sentido** (§ 2 acima). **Exatamente a classe que o enunciado
mandava procurar**, cometida pela correção que a combatia.

**G2 — a dedução por nome sobrevivia em seis arquivos**, e **um deles foi criado neste bloco**.
Cinco espinhas afirmavam *"percentual (INPC, **IPCA**, IGP)"* **citando o item 4.1.2.4 — que não
nomeia IPCA**; e `civel-federal.md` classificava **IPCA-E e IPCA-15** como percentuais, os dois
primeiros da tabela de indeterminados. `indices-judiciais/SKILL.md` **se contradizia dentro do
mesmo arquivo**: percentual na § 2, indeterminado na § 5.

> **Permanece divergente e NÃO foi corrigida:** a **§ 7 de `00-base-normativa.md`** enuncia R3 com
> a mesma lista. **É fonte de verdade do usuário, e este bloco não altera conteúdo normativo.**
> Registrada em `pendencias.md` § 23.

**G3 — ponteiros mortos para os ids extintos em 14 arquivos**, dois deles artefatos deste bloco:
o catálogo novo apontava para `trt3.hist.*.json`, e `09-ordem-de-calculo.md` também. Corrigidos
**exceto onde o nome antigo é a narrativa** — `01-plano-extracao.md`, os dois validadores e o
relatório do bloco 16 **devem** usá-lo, porque descrevem a renomeação.

**Três médias corrigidas:** a TR ainda descrita como `percentual` em dois textos; o runbook da
`indices-judiciais` publicando `10 erros` **quando a própria § 5 já dizia que tinham sumido**; e
`pendencias.md` citando como literal uma frase que a correção já tinha mudado.

### O que a auditoria confirmou íntegro

- **97 de 97 segmentos com `tipo_indexador`, zero ausências** — e, o mais importante, **nenhum
  dos 37 classificados traz índice fora do conjunto sustentado em fonte**;
- **os 8 `FONTE` se verificam um a um.** *"O desconto previdenciário precede sempre ao desconto do
  IR"* é enunciado **de posição**, não só de operação. **Nenhum `FONTE` é composição disfarçada**;
- **a § 1 de `09-ordem-de-calculo.md` é modelo de afirmação de ausência** — escopo (74 `.md`),
  comando, oito termos com contagem, e a ressalva de que o PDF não está no repositório;
- **os seis deltas batem exatamente** com `armadilhas-comparador.md` § 3;
- **TRT-4 de volta nos quatro lugares**, com as quinze regras de três tribunais tabeladas;
- **zero menções a cliente, UF suposta ou polo processual** nas skills.

**Uma média não foi corrigida, e a razão está registrada:** `references/README.md` diz que o
conteúdo *"mudou de lugar, não de teor"*. O `git diff` mostra **7 linhas verbatim de 81** — os
arquivos foram **reescritos e expandidos**. **A norma sobreviveu** (conferida item a item), mas a
asserção sobre o método convida a pular a conferência que o teor exigia.

---

## 7. Para o próximo bloco

| Aberto | Natureza |
|---|---|
| **FGTS (JAM) e poupança do cap. 4 do CJF** | **cadeia própria, nunca consolidada.** Consolidar antes de escrever `reference` |
| **`P17-01` — nove índices sem classificação** | **não se fecha relendo os PDFs.** Exige o ato de instituição de cada índice, ou decisão de estender a lista do 4.1.2.4 |
| **`P17-03` — `Ufir → Selic` é segmento composto** | dois indexadores de tipos diferentes num registro só. A correção é **partir o segmento**, não classificá-lo |
| **a defasagem do expurgo** | as 12 viradas R3 confirmadas seguem acusadas — **e devem seguir** — enquanto `aplicacao` não for preenchido com fundamento |
| **`00-base-normativa.md` § 7 × o catálogo** | divergência declarada. **É fonte de verdade do usuário** |

> **Um veredito inventado é pior que uma pendência declarada.** Foi o que sustentou `indeterminado`
> em dez índices, e o que impediu de forçar `nominal`/`percentual` por semelhança de nome.
