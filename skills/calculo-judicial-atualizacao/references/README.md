# references/ — variantes por jurisdição

**Fase do pipeline:** Fase 5. **Escrito no bloco 16.**

## Propósito

Um arquivo por variante de cadeia. O agente carrega **apenas** o arquivo da jurisdição em
questão — essa é a razão de a pasta existir em vez de um único documento grande.

---

## RENOMEADO NO BLOCO 16 — e por quê

A divisão anterior separava por **qualidade do devedor** (`trabalhista-privado` ×
`trabalhista-fazenda`) e por **precedente** (`civel-cc-tema1368` × `civel-mg-cgj`). A nova separa
por **alcance da norma: NACIONAL × REGIONAL**.

| Nome antigo | Nome novo | O que motivou |
|---|---|---|
| `trabalhista-privado.md` + `trabalhista-fazenda.md` | **`trabalhista-nacional.md`** | privado e Fazenda são **dois ramos da mesma cadeia nacional**, com os mesmos cortes de 1987, 1991, 2009 e 2021. Separá-los duplicava a `R4-EXCEÇÃO`, as quatro réguas de defasagem e a Tabela Única do CSJT em dois arquivos |
| *(não existia)* | **`trabalhista-regional-trt3.md`** | os verbetes do TRT-3 que o manual invoca **não tinham casa**. Estavam implícitos na aritmética, que é **nacional** |
| `civel-cc-tema1368.md` | **`civel-cc-nacional.md`** | o Tema 1368 é **um** dos fundamentos, não o recorte. O recorte é *o que vale em qualquer estado* |
| `civel-mg-cgj.md` | **`civel-regional-tjmg.md`** | simetria com o trabalhista: o nome passa a declarar **alcance**, não sigla de órgão |
| `tributario-federal.md` | **inalterado** | — |
| `previdenciario.md` | **inalterado** | — |

### A razão de fundo — a premissa corrigida

> **Origem declarada: EXTERNA AO CORPUS** — enunciado do bloco 16, não conferido nesta fase.

A atualização monetária trabalhista é **NACIONAL** desde a **Res. CSJT 8/2005**, que unificou as
**24 tabelas** dos TRTs; hoje vale a **Res. CSJT 380/2024**, com duas tabelas — débitos comuns e
Fazenda Pública, esta referenciada ao **Manual do CJF**. O **PJe-Calc** é o sistema de toda a
Justiça do Trabalho.

O projeto vinha tratando o manual do TRT-3 como *fonte de prática regional*. **Está errado:** é
**fonte procedimental de uma região que aplica norma nacional**. Sua **aritmética não é prática
regional divergente** — regional são **os verbetes que ele invoca**.

> **A separação nacional/regional nos nomes não é organização estética. É o que permite cadastrar
> outra região sem tocar no motor:** o arquivo regional é **entrada de catálogo**, resolvida pela
> chave `(regra, tribunal, competência)`; o arquivo nacional é o **default**. Acrescentar o TRT-9
> ou o TJ-SP é acrescentar linhas, não refatorar.

Fonte da classificação: `docs/calculo/consolidado/08-nacional-e-regional.md`;
`consolidado/01-dominio-e-invariantes.md` § 2.9 (**R24**).

---

## Os dez arquivos

**Eram seis até o bloco 16. O bloco 17 acrescentou dois**, e a razão está na § "Limitação da
própria divisão", abaixo. **O bloco 18 acrescentou outros dois** — `fgts.md` e `poupanca.md` —,
que eram a **primeira linha** da tabela "o que a varredura achou e não foi criado" e só puderam
ser escritos **depois de consolidados** (§ "O que o bloco 18 fechou").

| Arquivo | Cobre |
|---|---|
| **`trabalhista-nacional.md`** | cadeia nacional — regime vigente (ADC 58/59 + Lei 14.905/2024), Fazenda Pública, cadeias históricas `CH-01`–`CH-05`, **Tabela Única do CSJT**, `R4-EXCEÇÃO`, as quatro réguas de defasagem, `cjf.trabalhista.juros-mora` |
| **`trabalhista-regional-trt3.md`** | os verbetes regionais que o manual invoca — **R1** Súmula 15 (data da dedução), **R13** juros na falência, **R15** tabela própria até out/2005 — com o **fallback nacional** de cada um; as outras doze regras regionais em tabela, com ponteiro; **R24** e a chave de resolução |
| **`civel-cc-nacional.md`** | STJ **Tema 1368**; SELIC de jan/2003 a 29/08/2024; **IPCA + taxa legal** a partir de 30/08/2024; termos iniciais (Súmulas 43, 54 e 362 do STJ); metodologia da taxa legal |
| **`civel-regional-tjmg.md`** | tabela da **CGJ/TJMG** — períodos pré-2003 e as **três hipóteses de sobrevida**; o que acontece fora de MG |
| **`civel-federal.md`** ⟨bloco 17⟩ | **condenatórias em geral** do CJF (item 4.2) — tronco comum, correção (15 segmentos, bifurca em **dez/2021**), **cadeia autônoma de juros** (11 segmentos, bifurca em **jul/2009**), as duas reconvergências em **set/2025**, o ramo paralelo `N-8`, as fórmulas **D1 e D2**, as **fixtures 1 a 3** |
| **`desapropriacao.md`** ⟨bloco 17⟩ | **três cadeias autônomas** — correção (com o **IPC/FGV** exclusivo), juros de mora (eixo na **data da sentença**) e **juros compensatórios** (`D8-C10`, os três cortes, `N-6`, `N-10`, `R-08-19`, honorários de perito) |
| **`fgts.md`** ⟨bloco 18⟩ | **FGTS do cap. 4 do CJF** (item 4.8) — critério **`JAM`**, correção (11 segmentos) e juros de mora (3); **`D8-C12`**, o corte por **saque integral**; **`D8-C13`/`N-5`**, os expurgos que **não dizem se substituem ou acrescem** (**aberta**); `D8-C14`, `D8-C15`, `D8-D18`; e o **FGTS fiscal de 2.4.4.1 (`JCM`), que é OUTRA cadeia** e segue em `P18-02` |
| **`poupanca.md`** ⟨bloco 18⟩ | **cadernetas de poupança** (item 4.9) — correção (12 segmentos) e juros de mora (3); **`D8-C16`/`N-11`**, o corte por **data de abertura da conta**; **UPC** e **LBC**, que só aparecem aqui; a **cadeia paralela da NOTA 3** (cruzados novos bloqueados); as **duas `R3` cheias do manual**; `D8-D19`, `D8-D24`, `D8-D25` |
| **`tributario-federal.md`** | repetição de indébito e dívida fiscal; **e as seções transversais** a todas as cadeias federais: as quatro fórmulas de `aplicacao`, ECs 113/136, precatório e a consolidação de dez/2021 nos cinco lugares |
| **`previdenciario.md`** | cadeia de benefícios do CJF (15 segmentos) e a **taxa legal com deflator INPC** |

> **O nome `civel-federal.md` declara alcance, como os demais.** *Cível federal* é o contencioso
> condenatório da Justiça Federal regido pelo **cap. 4 do Manual CJF**; *cível nacional* é o do
> **Código Civil** (`civel-cc-nacional.md`). **São cadeias diferentes, e o nome é o que impede
> confundi-las.**

---

## O que não entra

- Regra **sem fundamento normativo citado**;
- Cadeia que contradiga `docs/calculo/00-base-normativa.md`;
- **Séries de valores mensais** — dado (B), contrato em `skills/indices-judiciais/`;
- **Invariantes e aritmética** — `skills/calculo-judicial-core/`;
- **Segmento solto exposto ao usuário.** O usuário escolhe preset; o motor compõe segmentos.

---

## Nota sobre `previdenciario.md` — confirmada

A taxa legal previdenciária usa **INPC** como deflator, **não IPCA-15**. Mesma fórmula, deflator
diferente. Fonte: Manual CJF, Res. 990/2026, item **4.3.2, Nota 3**.

**E a consequência que a nota antiga já antecipava está confirmada:** os **dois pares de
validação aritmética** da § 4 da base normativa (set/2025 = 1,377047% e mai/2026 = 0,277807%) são
**deste caso, não do caso geral** — a coluna do manual é `Fator INPC`. **A variante IPCA-15, que é
a regra geral e a de maior uso, segue sem par de validação contra valor publicado.** Pendência
aberta: `docs/calculo/pendencias.md` § 2.

---

## Limitação da própria divisão — **fechada no bloco 17**

**A lista de seis fixada pelo bloco 16 não fechava o domínio.** Duas cadeias federais não são
tributárias nem previdenciárias e ficaram sem arquivo: **condenatórias em geral** e
**desapropriação** (direta e indireta, com os **juros compensatórios**, que são **cadeia autônoma**
com corte em **ago./2017** que nenhuma tabela mostra). Ambas foram extraídas no **bloco 08**, ambas
têm **cadeia própria**, e ficaram alojadas em `tributario-federal.md` §§ 5 e 7 com aviso no topo.
A lacuna estava registrada em `docs/calculo/extracao/bloco-16-relatorio.md` § 6.

**O bloco 17 criou `civel-federal.md` e `desapropriacao.md`**, migrou o conteúdo **sem alterar
norma** — mudou de lugar, não de teor —, deixou ponteiro explícito em `tributario-federal.md` § 5
e **removeu o aviso do topo**, que existia só por causa da lacuna.

> **O candidato nomeado pelo bloco 16 era um arquivo só** (`federal-condenatorias-desapropriacao.md`).
> **São dois**, porque são **matérias distintas com cadeias distintas**: as condenatórias gerais
> têm **duas** cadeias e bifurcam por devedor; a desapropriação tem **três** e nunca bifurca por
> devedor (`R-08-08`). Juntá-las repetiria o defeito que a divisão existe para evitar.

### O que a varredura do bloco 17 encontrou, e NÃO foi criado

O enunciado autorizou **dois** arquivos. As demais lacunas ficam **listadas, não preenchidas**:

| Matéria | Cadeia própria? | Por que não virou `reference` |
|---|---|---|
| **FGTS do cap. 4 do CJF** (item 4.8, índice **JAM**) e **poupança** (item 4.9, **12 segmentos**) | **sim** — `D8-C12` (eixo por **saque integral**), `D8-C13`, `D8-C14`, `D8-C15`, `D8-C16` | **À época: não estavam no consolidado.** Viviam só em `extracao/justica-federal/bloco-08-jf-detalhe.md` §§ 3.2 e 3.3, e **não haviam sido extraídos como cadeia** para `tabelas-normativas/`. Escrever `reference` exigiria consolidar antes — **e foi o que o bloco 18 fez. FECHADO:** `fgts.md` e `poupanca.md` |
| **Dívida fiscal** | **sim** — bifurca por `data-do-fato-gerador`, **não tem o tronco comum**, tem janela **sem correção** e base de juros que **alterna quatro vezes** | **Tem casa e o nome a cobre:** é tributária. `tributario-federal.md` § 3. **Não é lacuna** |
| **Repetição de indébito** | **sim** — `D3`, termo inicial no **trânsito em julgado**, **não consolida** em dez/2021 | idem — `tributario-federal.md` § 2. **Não é lacuna** |
| **Precatórios / requisitórios** (ECs 113 e 136, `C14-02`, `R-08-17`) | **não é cadeia por jurisdição** — é **regime de fase**, transversal a todas elas | Ficaria duplicado em cada arquivo. **Fica em `tributario-federal.md` §§ 6 e 7 como seção transversal**, referenciada pelos demais |
| **Planos econômicos** (`pr.planos-economicos`) | é **regime temporal**, outra família | **`bloqueado` por falta de série** (P19). `presets-regime.md`; `consolidado/03-verbas.md` § 5.12. **Pendência, não matéria de `reference`** |
| **FGTS trabalhista** (`pr.fgts-indice-jam`, `pr.fgts-prescricao`) | regime temporal, eixo **conteúdo do título** | pertence a `calculo-trabalhista-liquidacao`, não a esta skill |

**Escopo declarado da varredura:** os **11 arquivos** de `docs/calculo/consolidado/`, mais
`presets-regime.md`, `pendencias.md` e os dois arquivos do bloco 08, buscando `JAM`, `poupan`,
`FGTS`, `planos econ`, `planos-economicos`, `4.8` e `4.9`. **Fora deste escopo não há afirmação.**

## O que o bloco 18 fechou — **"depois de consolidadas, e não antes"**

A **tarefa 1 do bloco 18** consolidou FGTS e poupança em
`docs/calculo/consolidado/02-atualizacao-detalhe.md` **§§ 5.3.2 a 5.3.5**, gerou as **quatro
cadeias** (`cjf.fgts.*` e `cjf.poupanca.*`) e registrou a **varredura item × JSON × consolidado**
do § 5.0. **A tarefa 2 escreveu as duas `references/` a partir do consolidado — não da extração
bruta**, como os oito anteriores.

**O que continua ABERTO, e não foi resolvido por estes dois arquivos:**

| Pendência | O que é |
|---|---|
| **`N-5` / `D8-C13`** | os expurgos do FGTS (**42,72% em jan/1989 e 44,80% em abr/1990**) **não dizem se substituem ou acrescem**. Os percentuais **não viraram segmento**: gravá-los exigiria escolher. `fgts.md` § 8 |
| **`P18-01`** | sete rótulos (`JAM`, `UPC`, `LBC`, `LBC – 0,5%`, `LFT – 0,5%`, `TRD`, **`IPC` nu**) **sem classificação em fonte alguma** → `indeterminado`. **19 `R3-INDETERMINADO`** |
| **`P18-02`** | eram **oito** cadeias tabuladas sem JSON; **são TRÊS** — **4.5.2**, **4.6.2** e **2.4.2.2.2**. As outras cinco foram geradas no **bloco 19, tarefa 3**: 4.5.3, 4.6.1.1, 4.6.3, 2.3.2.2 e **2.4.4.1** (o **FGTS fiscal**, critério `JCM`, que **não é** a cadeia de 4.8). As três que restam estão bloqueadas por **falta de fonte** — a tabela delas **nunca foi extraída linha a linha** —, não por schema. `02-atualizacao-detalhe.md` § 5.3.6 |
| **`P19-02`** | **`BTNF` sem classificação em fonte alguma** → `indeterminado`. O item 4.1.2.4 nomeia o **BTN**, não o BTNF; herdar do quase-homônimo é a dedução proibida |
| **duas `R3` cheias** | `1986-03` e `1990-04` na poupança, **sem `aplicacao`**. **São do manual — transcritas, não harmonizadas.** `poupanca.md` § 4.2 |

> **`4.7.1` parecia lacuna e não é:** o manual **não tem** tabela de correção trabalhista — ele
> **delega ao TST** (NOTA 2, `pagina_pdf` 77: *"utilizar a tabela de coeficientes trabalhistas
> expedida pelo Tribunal Superior do Trabalho"*). **O que se registra é a DELEGAÇÃO, não a
> ausência**: afirmá-la ausente seria afirmar ausência de algo que a fonte nunca prometeu. A cadeia
> vive numa **série**, não numa regra — desenho do `P9-02`. **Não entra em `P18-02`.**
> `02-atualizacao-detalhe.md` §§ 5.0 e 5.3.6.

## Estado

**Os dez arquivos estão escritos.** Os seis primeiros no bloco 16; `civel-federal.md` e
`desapropriacao.md` no **bloco 17**; **`fgts.md` e `poupanca.md` no bloco 18** — com `SKILL.md` e
este README atualizados em cada bloco.
