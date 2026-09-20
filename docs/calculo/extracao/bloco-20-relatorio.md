# Bloco 20 — fechar a espinha contra o extraído

**Estado: fechado.** Quatro `BLOQUEIA` de conteúdo achados e corrigidos, um enum que desligava
checagem, e os números de resultado passaram a ter **um dono só**.

> **Este relatório é registro datado.** Os números abaixo valem para o fechamento do bloco 20 e
> **não se atualizam**. O estado corrente vive em
> [`../consolidado/00-numeros.md`](../consolidado/00-numeros.md), **gerado por script**.

| | Antes | No fechamento |
|---|---|---|
| Testes | 311 | **342** |
| R1 · R2 · R3 | 21 · 1 · 62 | **21 · 1 · 63** |
| `BLOQUEIA` em `10-literais` | 2 | **4** |
| Arquivos de `consolidado/` | 14 | **15** |

---

## 1. Quatro `BLOQUEIA`, e três deles na mesma cadeia

O bloco 19 achou **um** `BLOQUEIA` de conteúdo, **por acaso**: os juros de servidores e
empregados públicos. O bloco 20 foi procurar de propósito, e achou **três**.

### `L12` — o termo inicial não é o ajuizamento

`cjf.trabalhista.juros-mora`, item 4.7.2, `pagina_pdf` 78, literal:

> *"Os juros são contados a partir da **notificação inicial (Súmula n. 224 do STF)**, salvo
> determinação judicial em outro sentido."*

**A espinha dava `ajuizamento`**, por R7 — que é a linha da **Justiça do Trabalho**, e esta
cadeia é **federal**.

**O caso que prova:** ação ajuizada em 10/03/1995, notificada em 05/04/1995, segmento a 1,0% a.m.
simples. **Um mês de juros sobre todo o principal** — e **R1, R2 e R3 passam nos dois cenários**.
É a falha silenciosa.

> **O argumento que absolvia `L12` no bloco 19 — *"usar o termo inicial da jurisdição"* — é o que
> produz o erro.** A jurisdição da cadeia é federal; R7 só tem linha trabalhista para a JT.

### `estatutário` — a cláusula que EXCLUI um sujeito

A Tarefa 2 buscou **entidade que sumiu**, não paráfrase. Achou o escopo inteiro do cap. 4.7:

> *"contratos regidos pela CLT anteriores à promulgação da vigente Constituição Federal"*,
> **excluindo servidores sob regime estatutário** — `pagina_pdf` 77.

> **É o mesmo mecanismo de `servidor`, e na mesma cadeia em que `L12` caiu.** `escopo_restrito` é
> **campo único em todo o corpus** — nenhuma outra cadeia restringe sujeito. **E cláusula de
> exclusão sumida faz a cadeia parecer aplicável a todo mundo.**

### `A17` — o `BLOQUEIA` que escapou das duas peneiras

Os **três regimes de atualização de depósito** — judicial = **poupança, TR + 0,5%**; recursal =
**FGTS, TR + 3% a.a.**; crédito = **art. 39** (`pagina_pdf` 329) — **não existiam em arquivo
nenhum do consolidado**.

**Foi classificado como *"lacuna de regra, não de entidade"*** porque o *termo* `depósito
recursal` estava lá. **O fato era verdadeiro; a consequência não.**

> **O efeito da classificação foi tirá-lo das duas verificações:** não entrou na reauditoria dos
> dez (que cobria `L1`–`L13`) nem na varredura de entidade (excluído pelo critério do termo).
> **São três taxas diferentes, e a dedução do depósito é passo do cálculo. Muda o número.**

### E os nove que ficaram

**Não foram promovidos, e a disciplina importa.** O teste era concreto: *existe caso — sujeito,
período, verba — em que a conta só com a espinha dá número diferente?* Para nove deles, **não se
conseguiu construir o caso**, e dizer isso é a resposta certa.

**`L3` virou `DÚVIDA`** — ver § 4.

---

## 2. A varredura de entidade — o método vale mais que a lista

**Duas etapas, derivadas do texto extraído:** diferença de vocabulário sobre **linha-gatilho**
(`NOTA`, `Para as ações`, `no caso de`, `salvo`, `exceto`, `quando`, `hipótese`…) — 2.507 tokens
distintos, 792 ausentes —, mais captura de **sintagma nominal** após `Para ações de`, `créditos
referentes a`, `não se aplica a`. Da união, **123 termos testados um a um**.

**Escopo contado, não estimado:** 69 arquivos em `extracao/` (48 `.md` + 21 `.csv`), 32 `.json`,
contra os arquivos de `consolidado/`.

**E a normalização importou:** a primeira passada não colapsava hífen e acusou `aviso-prévio`
como ausente.

**O filtro do ruído teve três motivos declarados** — *outro nome* (`trintenária` → "30 anos";
`astreintes` → "multa diária" + art. 412), *fora de escopo com ponteiro declarado*, e *prosa*
(`marítimo`, `motorista`, `urbano` são rótulos de **CNAE**). **A validação adversarial amostrou
onze descartes e confirmou os onze.**

---

## 3. O enum não era um valor — era a ausência de um

`englobante` caiu no bloco 19 por **duplicar campo e desligar checagem**. A Tarefa 3 varreu **24
vocabulários** atrás do mesmo padrão e achou um caso **em outra forma**:

```python
if seguinte.aplicacao: continue      # qualquer string não-vazia desligava R3
```

**`aplicacao` era teste de *truthiness*.** E o campo guarda também **prosa transcrita que não
declara defasagem alguma** — em `cjf.condenatorias-gerais.correcao-monetaria` é a regra de **qual
valor** do IPCA-E usar em jan./2001.

> **Conteúdo de outro tipo desligando R3 é a assinatura exata do `englobante`.**

### E o conserto errou na primeira tentativa — a auditoria pegou

O domínio foi fechado em **dois** tokens. **Mas o consolidado declara quatro fórmulas** (D1–D4), e
**D2, D3 e D4 estavam gravadas como prosa**. Fechar em dois fez o critério ser **a grafia, não o
conteúdo** — e **uma das duas violações apresentadas como "do manual" era falso positivo de
modelagem**: `cjf.repeticao-indebito.correcao-monetaria`, cujo `aplicacao` **é o D3 do próprio
componente**, não prosa alheia.

**Corrigido:** D2, D3 e D4 tokenizadas, com a prosa preservada em `aplicacao_literal`. **A
violação de `repeticao-indebito` desapareceu; a de jan/2001 permanece, como devia** — aquela diz
**qual valor**, não **quando**.

**Seis outros valores auditados ficaram `LEGÍTIMO`**, cada um com a razão verificada no código —
inclusive `nao-indexador`, cuja isenção foi testada removendo a guarda.

**E um buraco latente virou teste:** um valor novo em `TIPOS_DE_INDEXADOR` fora de
`TIPOS_COM_DEFASAGEM` caía no fim da função **sem violação e sem `R3-INDETERMINADO`**. Agora o
domínio é **partição declarada**, e o *fall-through* **levanta `ValueError` em vez de silenciar**.

---

## 4. Pendências com caminho de fechamento

**A separação agora é legível por script:** `tipo_indexador_razao` ocorre **exatamente** nos
segmentos da família TR; `tipo_indexador_pendencia` nos demais; **nunca juntos**.

| Grupo | O que fecha |
|---|---|
| **`indeterminado-sem-fonte`** | a fonte, quando aparecer |
| **`indeterminado-por-natureza`** — TR | **nada.** A fonte apareceu e **disse que não cabe** |

### Três dos doze já trazem o ato de instituição no próprio `fundamento`

`IPCA série especial` → **Lei 8.383/1991, art. 2º, § 2º** · `IRSM` → **Lei 8.542/1992, art. 9º,
§ 2º** · `IPC-R` → **Lei 8.880/1994, art. 20, § 6º**. **Falta só o texto.**

Cinco rótulos dependem de ato **que o repositório não nomeia**; dois fecham por **norma do
emissor**; o **`IPC` nu não é problema de classe, é de emissor** — só o CJF resolve.

### E um muda de natureza

**`taxa-legal` não espera fonte — espera decisão.** A varredura achou o que ninguém tinha
procurado: os segmentos carregam `formula: "SELIC, com dedução do IPCA-15"`, e a NOTA 4 remete à
**Nota 7 do item 4.2.2**, `pagina_pdf` 56.

> **A fórmula compõe um `percentual` (Selic) com um `janela-deslocada` (IPCA-15) — composição
> para a qual a tricotomia não tem resultado.** E o item 4.1.2.4-b prende o "mês seguinte" à
> **divulgação**, enquanto a Nota 7 prende à **competência**. **`P19-01` deixa de ser pendência
> de fonte e passa a decisão de modelagem.**

### Os quatro de `P17-03` e as taxas `null`

| | Natureza | O que falta |
|---|---|---|
| **`Ufir → Selic`** | **modelagem** — **partir resolve**: o `regra_literal` **data as quatro viradas** | escolher entre três opções com custo declarado |
| **`UPC → índices básicos`** | **extração** — **e a fronteira é justamente o que a fonte não declara** | releitura das `pagina_pdf` 35–36 |
| **as duas `taxa: null`** | **extração pura** | a coluna de percentual das tabelas 4.5.3 (`pagina_pdf` 69) e 4.6.3 (76) |

**Achado colateral: um terceiro indexador escondido** — **`TMMCTN`**, jan–mar/1995, dentro do
segmento composto e **ausente do catálogo**.

**E o atalho óbvio foi testado e falha:** a poupança encerra a UPC em `1983-06` e o segmento
composto começa em `1983-10`. **A terceira `taxa: null` não é o mesmo buraco** — ali o `null` é a
regra (`D8-C11`).

---

## 5. Número de resultado passou a ter um dono

**Três reincidências motivaram a regra:** o bloco 19 publicou *"R1 e R2 não se moveram"* em
**quatro arquivos** depois de R1 ter ido a 21; o bloco 18 deixou *"14 ok, 10 erros"* num runbook
depois de os erros sumirem; o bloco 17 deixou *"97 de 97 segmentos"* depois de virarem 126.

> **Número digitado em quatro lugares envelhece em quatro lugares.**

**`00-numeros.md` é gerado por `gera_numeros.py`**, que **conta o repositório e executa os
validadores**. Três exigências de desenho, todas testadas: **cabeçalho que se declara gerado**;
**sem timestamp automático** — data gerada produz diff a cada rodada e o ruído esconde a mudança
real; e **determinístico**, confirmado por SHA-256 idêntico em três rodadas.

**E `--verifica` falha se o arquivo divergir do estado real** — porque **gerado e esquecido também
envelhece**.

### A distinção que faz a tarefa funcionar

| | O que fazer |
|---|---|
| **resultado** — *"342 testes"*, *"20 cadeias"* | **ponteiro** |
| **conteúdo normativo** — *"42,72%"*, *"art. 457"*, `pagina_pdf 42` | **não tocar: é o dado** |
| **relatório de bloco** | **não tocar: registro datado.** Um relatório que se atualiza sozinho deixa de ser registro |

**Treze números substituídos — seis já estavam defasados, sete estavam certos e eram cópia sem
dono.** **Vinte e uma menções agregadas não foram substituídas** e sim **marcadas como registro
datado**: narrativa histórica, ponta de variação, ou a própria pendência.

### O detector mediu antes de decidir

`test_numeros.py` procura **vocabulário de resultado agregado** e **deliberadamente não procura**
`N segmentos` nem `N violações` soltos: **com eles, 64 pares em 15 arquivos; sem eles, 21 em 6**,
e as diferenças eram quase todas legítimas.

> **Ledger de 64 ninguém mantém, e validador ignorado é pior que validador ausente.** O custo
> aceito está escrito no arquivo: um agregado escrito como *"156 segmentos"* nu passa.

**A chave do ledger é o fragmento casado, não a linha inteira** — linha inteira orfanaria a cada
reflow de parágrafo, e autolimpante tem de morder **o fato**, não a formatação.

---

## 6. O que a validação adversarial pegou

**Três `GRAVE`, e os três eram de razão, não de resultado:**

- **`L3` foi absolvido por um *default* que não existe.** A justificativa dizia *"o default de uma
  cadeia-temporal já é a competência"* — e o repositório diz **o contrário**: `aplicacao` ausente é
  tratado como **violação**. **Reclassificado como `DÚVIDA`**, com as três perguntas que faltam.
  **Nenhum default foi inventado**;
- **`A17`** — § 1;
- **o domínio de `aplicacao`** — § 3.

**Cinco `MÉDIA`**, das quais duas são o próprio bloco cometendo o que veio consertar: *"111
arquivos varridos"* **não era nenhum dos três universos reais**, e *"Catorze arquivos"* no README
**escapou do detector por estar por extenso** — duas linhas abaixo de uma edição da mesma tarefa.

**E números de resultado envelhecidos em `.json`**, fora do alcance do detector, que **não
mencionava `.json` no escopo**. **Estendido**, depois de medir: 39 arquivos, **8 achados, todos
num só**.

### O que a auditoria confirmou íntegro

- **`L12` se sustenta** — literal conferido, caso construído procede, e a metade não promovida
  (*"salvo determinação judicial"*) **é R8, corretamente absolvida**;
- **`estatutário` se sustenta** — `escopo_restrito` é campo único no corpus, e **a varredura
  refeita por método próprio não achou mais nada**: 60 fragmentos, 58 deles rótulos de CNAE;
- **o diagnóstico do `aplicacao` está certo** — *"não era um valor, era a ausência de enum"*;
- **o incidente do `git checkout` não deixou perda detectável** — três hunks, todos os
  entregáveis das Tarefas 1–5 presentes, nenhum link quebrado;
- **`00-numeros.md` confere item a item**, e **nenhum número de conteúdo normativo foi tocado**,
  nem relatório de bloco reescrito.

---

## 7. O que continua aberto

| Aberto | Natureza |
|---|---|
| **`L3`** | **dúvida declarada.** Falta saber o que a espinha faz quando `aplicacao` está ausente |
| **nove `ENFRAQUECE`** | não promovidos por **não se conseguir construir o caso**. Insumo |
| **`P19-01` — taxa legal** | **decisão de modelagem**, não espera fonte: a fórmula compõe duas classes |
| **`P17-03`** | um é modelagem (partir resolve), outro é extração — **e a fronteira é o que falta** |
| **as duas `taxa: null`** | **extração pura** — duas colunas de duas tabelas |
| **`TMMCTN`** | terceiro indexador escondido num segmento composto, fora do catálogo |
| **pendências por família** | **ficaram fora de `00-numeros.md`, com o porquê escrito:** numeração heterogênea, *aberta/fechada* ora em prosa ora em título. **Não é contável com lastro, e não se inventou** |

> **O padrão que este bloco fecha:** o bloco 19 achou um `BLOQUEIA` **por acaso**. O bloco 20
> procurou de propósito e achou **três** — e **dois deles na mesma cadeia**. A busca certa não é
> por paráfrase: **é por entidade que sumiu**, e a mais perigosa é a **cláusula que exclui um
> sujeito**, porque a ausência dela faz a regra parecer aplicável a todo mundo.
