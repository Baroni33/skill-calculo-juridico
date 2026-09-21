# Literais que ficaram na extração

**Insumo, não errata.** O bloco 18 registrou que, para escrever `fgts.md` e `poupanca.md`, foi
preciso **buscar no JSON literais que o consolidado apenas parafraseia**. Este arquivo varre o
consolidado atrás do mesmo padrão e **lista** o que encontrou. **Não corrige tudo** — a decisão
sobre uma nova passada na espinha é de outro bloco.

**Só o que é `BLOQUEIA` foi corrigido neste bloco.** São **dois achados**, e a correção está em
[`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) § 5.2-A e em
[`02-atualizacao.md`](02-atualizacao.md) § 5.

> **O bloco 20 reauditou os dez `ENFRAQUECE` um a um, com teste concreto de resultado, e promoveu
> UM: `L12`** — § 5 deste arquivo. A § 6 acrescenta uma varredura de **outro tipo**: entidade
> ausente.
>
> **A validação adversarial do mesmo bloco mexeu em mais três pontos**, e eles estão nas §§ 5.2,
> 5.3 e 6.4: **`L3` virou `DÚVIDA`** (a absolvição invocava um *default* que não existe); **`L7`
> teve o destino do seu ponteiro preenchido** e segue `ENFRAQUECE`; e **`A17` subiu a
> `BLOQUEIA`** — não era achado da § 2, e o critério de termo o fizera escapar das duas peneiras.

---

## 1. Escopo da varredura — a negativa exige universo declarado

*"O literal não está no consolidado"* é afirmação de ausência. O universo em que se buscou:

| Dimensão | Escopo |
|---|---|
| **Onde se procurou a paráfrase** | os **treze** arquivos de `docs/calculo/consolidado/` — `00-calendario-de-cortes`, `00-validacao-casos`, `01-dominio-e-invariantes`, `02-atualizacao`, `02-atualizacao-detalhe`, `03-verbas`, `04-descontos`, `04-descontos-detalhe`, `05-imputacao`, `06-encargos`, `07-leitura-do-corpus`, `08-nacional-e-regional`, `09-ordem-de-calculo`. **Os treze são o universo desta busca, e não o do diretório**, que hoje tem **15**: ficam de fora **este arquivo** e **`00-numeros.md`** — o primeiro porque é o produto da busca, o segundo porque é **gerado** e só contém contagem. **Universo contado antes de declarado, e reconferido no bloco 20** |
| **De onde vieram os literais candidatos** | os **32 arquivos `.json`** de `../tabelas-normativas/` (o diretório tem 32 `.json` mais o `README.md`) — **a unidade é ARQUIVO**; dizia-se *"os 36 JSON"*, e **36 é a contagem de rótulos de indexador** (35 distintos mais `(segmento sem indexador)`), unidade diferente, e a troca de uma pela outra declarava um universo que não existiu nem antes (27) nem depois (32) do bloco 19. **A conclusão da varredura foi reconferida e não muda** —, nos campos que carregam texto de fonte: `texto`, `regra_literal`, `cabecalho_literal`, `termo_inicial`, `observacao`, `aplicacao_literal`, `literal`, `regra` e os campos `NOTA*` — **146 strings** com mais de 60 caracteres |
| **Também lido** | `../extracao/justica-federal/bloco-08-jf.md`, `bloco-08-jf-detalhe.md`, `bloco-08-relatorio.md` e `../extracao/bloco-18-relatorio.md` |
| **Critério mecânico de ausência** | nenhuma janela de **8 palavras** do literal (normalizado: minúsculas, sem acento, sem pontuação) ocorre na concatenação dos treze arquivos. **115 das 146** passaram nesse filtro |
| **Curadoria depois do filtro** | das 115, a maioria é **comentário de projeto** (`observacao` sobre decisão de extração), não regra de fonte. Ficaram os achados abaixo, cada um reconferido por busca literal dirigida |
| **Fora do escopo** | `skills/` — as `reference` **são** o consumidor que descobriu o problema, não o lugar onde a espinha deveria estar; e `docs/calculo/00-base-normativa.md`, que é fonte de verdade do usuário e não se altera |

**O que NÃO conta como achado**, e por quê: literal cujo conteúdo já está na espinha sob outras
palavras **com item e página citados** — aí o literal é cor, não conteúdo, e o lastro existe.
Exemplos verificados e **descartados**: o multiplicador de jan/1989 (`6,17` / `6,92`, presente em
`02-atualizacao.md` e no detalhe); a NOTA 1 dos expurgos do FGTS (*"períodos definidos pelo
julgado"*, presente); os termos iniciais da desapropriação (Súmulas 69 e 75, presentes com a
bifurcação direta × indireta); o atalho de `0,9240%` da Fazenda trabalhista (presente); as
situações de **falência** e **intervenção/liquidação** (presentes).

---

## 2. Os achados

**Treze.** Uma linha por achado na tabela; o que exige argumento vem depois dela.

| # | Regra | Paráfrase | Literal | O que se perde | Classe |
|---|---|---|---|---|---|
| **L1** | Juros de **servidores(as) e empregados(as) públicos(as)** antes de jul/2009 | **nenhuma** | 4.2.2 NOTA 3, `pagina_pdf` **55** — `cjf.condenatorias-gerais.juros-mora.json` | 1% a.m. até jul/2001 e **0,5% a.m. de ago/2001 a jun/2009**, onde a espinha manda **Selic** | **BLOQUEIA** |
| **L2** | **Termo inicial da correção** das remunerações de servidores e empregados públicos | **nenhuma** | 4.2.1.1 NOTA 3, `pagina_pdf` **49** — `cjf.condenatorias-gerais.correcao-monetaria.json` | o eixo é o **mês da competência, não o de pagamento**; sem a regra o implementador não tem default declarado | **BLOQUEIA** |
| **L3** | Os **70% da Selic** incidem *"independentemente da data de vencimento do principal ou do termo inicial dos juros de mora"* | fórmula sim (detalhe § 5.3.3, via 4.9.2); **a cláusula de eixo, não** | 4.2.2 NOTA 4, `pagina_pdf` **55** | a regra que **neutraliza o eixo** — quem condicionar ao vencimento erra, e não há no consolidado o que o desminta | **DÚVIDA** (bloco 20; era ENFRAQUECE — ver § 5.2) |
| **L4** | Definição de índice **percentual**, segunda metade | `01-dominio-e-invariantes.md` **R3** | item 4.1.2.4, `pagina_pdf` **42** — `indexadores-tipo-catalogo.json`, `fonte.literal` | *"e terão **aplicação prática no mês (ou dia) seguinte à data da divulgação**"* — R3 enuncia a **defasagem de referência** e cala sobre a **de publicação**; some também o **IGP-M** da lista de exemplos | ENFRAQUECE |
| **L5** | **R1** — a Selic engloba, e o IPCA-E sai | R1, em 9 dos 13 arquivos | 4.2.1.1 NOTA 2, `pagina_pdf` **49** | R1 aparece como **invariante do projeto**; o literal a põe como **regra escrita da fonte**, com item e página. Sem ele, R1 não é citável | ENFRAQUECE |
| **L6** | As **quatro notas de 4.8.3 e 4.9.3** (FGTS e poupança) | detalhe § 5.3.4 — `N-7` e a alínea *b* | `cjf.fgts.juros-mora.json` e `cjf.poupanca.juros-mora.json`, `notas[]`, `pagina_pdf` **83** e **86–87** | os **precedentes** (REsp 897.043, 1.102.552, 466.732) e a NOTA 4, que **remete a taxa legal à Nota 7 de 4.2.2** — é a origem de `aplicacao: mes-posterior-a-competencia` nessas duas cadeias | ENFRAQUECE |
| **L7** | **Juros remuneratórios da poupança** — 4.9.2, regra-base | o eixo sim (detalhe § 5.3.3); **a regra, não** | `cjf.poupanca.juros-mora.json`, `JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA.regra`, `pagina_pdf` **86** | **0,5% a.m.** e **6% a.a. ou fração *pro rata* para cruzados novos bloqueados**, com os cinco fundamentos — um **componente de valor** que incide **concomitantemente** aos moratórios | ENFRAQUECE |
| **L8** | Os remuneratórios da poupança são **capitalizados mensalmente** | `02-atualizacao.md` § 8: *"capitalização mensal só em juros remuneratórios"* | 4.9.2 NOTA 1, `pagina_pdf` **86** | os **cinco precedentes** que sustentam a exceção a **R4**. A regra está; o lastro, não | ENFRAQUECE |
| **L9** | Sentença que manda aplicar os índices da poupança **sem fixar termo final** | **nenhuma** | 4.9.1.1 NOTA 1, `pagina_pdf` **85** | *"o cômputo deve-se dar **até o efetivo pagamento**"* — regra de integração de sentença omissa; sem ela a conta não tem fecho declarado | ENFRAQUECE |
| **L10** | **Fundamentos legais** das observações linha a linha da poupança | detalhe § 5.3.3 traz as observações **sem fundamento** | `cjf.poupanca.correcao-monetaria.json`, `segmentos[].observacao` | os decretos e leis: **art. 6º da Lei 8.024/1990** (mar/1990), **§ único do art. 13 da Lei 8.177/1991** (jan/1991), **§ 2º do art. 7º da Lei 8.660/1993** (abr/1993), **§§ 1º e 2º do art. 16 da Lei 9.069/1995** (jun/1994) e o *pro rata* da ORTN em fev/1986 | ENFRAQUECE |
| **L11** | **`D8-C21`** — a classificação do IPC/IBGE | invocado em `01-dominio` § R3 e no detalhe § 6 **pelo rótulo** | `bloco-08-jf-detalhe.md` **linha 416** e `indexadores-tipo-catalogo.json`, `apoio_no_corpus.D8-C21.literal` | *"O IPC/IBGE é índice percentual, e o item 4.1.2.4 diz que percentuais 'refletem a inflação do próprio mês de competência'"* — o **raciocínio** que separa fonte de dedução. Citado de segunda mão | ENFRAQUECE |
| **L12** | **Termo inicial dos juros**, literal, das cadeias do CJF | `01-dominio` § 2.4, **R7**, em tabela de três linhas | `termo_inicial` de `cjf.condenatorias-gerais.juros-mora`, `cjf.fgts.juros-mora`, `cjf.poupanca.juros-mora` e `cjf.trabalhista.juros-mora` | (a) a cláusula ***"salvo determinação judicial em outro sentido"***, que torna o termo **sobrescrevível pela sentença** — e **D2 tem o termo inicial como operando**; (b) o CJF escreve *"**notificação inicial** (Súmula 224 do STF)"* para o trabalhista, onde R7 escreve *"ajuizamento"* | **BLOQUEIA** (bloco 20; era ENFRAQUECE — ver § 5) |
| **L13** | Cabeçalho de 4.2.1.1 | — | `cabecalho_literal`: *"Caso não haja decisão judicial em contrário, utilizar os seguintes indexadores"* | a **supletividade** de toda a tabela. O consolidado já trata a decisão judicial como soberana em vários pontos; o literal só confirma | COSMÉTICO |

### 2.1 Por que L1 e L2 são `BLOQUEIA`, e os demais não

**O teste é o do enunciado: *quem lê só a espinha consegue implementar?***

**L1 e L2 falham o teste no pior modo — o silencioso.** A palavra **`servidor`** não ocorre
**nenhuma vez** nos treze arquivos do consolidado (busca literal, sensível e insensível a
maiúsculas; `empregados(as) públicos(as)` idem). A espinha descreve a cadeia de 4.2.2 como
**Selic de jan/2003 a jun/2009 sem condição**, e a bifurcação de jul/2009 como **Fazenda ×
não-Fazenda**. O manual tem **um terceiro recorte** — *créditos referentes a servidores e
empregados públicos* — que **desce a taxa a 0,5% a.m. em oito anos de competências** e que a
espinha não menciona. Quem implementar pela espinha **não vê que falta nada**: a cadeia parece
completa e contígua, e **R1/R2/R3 passam**. É exatamente a falha que nenhum validador pega.

**L3 e L12 chegam perto e não são.** Nos dois, o comportamento correto é o que um implementador
já faria por default — não condicionar (L3), usar o termo inicial da jurisdição (L12). Perde-se
o **lastro**, não o resultado. **ENFRAQUECE.**

> **O bloco 20 refutou a metade `L12` deste parágrafo, e a razão é exatamente o *default*.** *"Usar
> o termo inicial da jurisdição"* **é** o comportamento errado aqui: a jurisdição da cadeia é a
> **Justiça Federal**, e o único termo inicial trabalhista da espinha é o da **Justiça do
> Trabalho**. O *default* não coincide com a fonte — ele **diverge dela por um mês**. **§ 5.**
>
> **E a metade `L3` caiu por outro motivo: o *default* invocado NÃO EXISTE.** Nada no repositório
> declara que a ausência de `aplicacao` significa *"competência"* — o validador trata a ausência
> como **violação**, e o detalhe § 5.3 chama de **defeito** as viradas sem o campo. `L3` foi
> **reclassificado como `DÚVIDA`**. **§ 5.2.**

**L7 e L8 chegam perto por outro lado.** A espinha **declara** que 4.8.2 e 4.9.2 ficaram fora das
cadeias e **diz onde estão** (*"Registrados no JSON, fora dos segmentos"*, detalhe § 5.3.2).
**Ponteiro declarado não é lacuna escondida** — é a mesma solução da ressalva de cobertura de
`00-calendario-de-cortes.md` § 1 para `CH-01`–`CH-05`. **ENFRAQUECE.**

> **Ressalva do bloco 20, e ela vale para `L7`:** a frase citada acima é da § 5.3.2 e fala de
> **4.8.2 (FGTS)**. Para **4.9.2** o ponteiro existia e **o destino não tinha a regra**. Foi
> preenchido; `L7` segue `ENFRAQUECE` **pela razão certa**. **§ 5.3.**

---

## 3. O que foi corrigido neste bloco

**Só L1 e L2.** Entraram em [`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) como
**§ 5.2-A**, com os dois literais, item e `pagina_pdf`, e um ponteiro de uma linha na espinha
[`02-atualizacao.md`](02-atualizacao.md) § 5.

**Nada mais foi promovido.** Onze achados continuam `ENFRAQUECE` e um é `COSMÉTICO`; nenhum
deles foi reescrito para justificar trabalho. **A lista é o produto.**

**No bloco 20, `L12` saiu dessa conta** — § 5 —, e a **validação adversarial** do mesmo bloco
mexeu em mais duas linhas: **`L3` foi reclassificado como `DÚVIDA`** (§ 5.2 — a absolvição se
apoiava num *default* inexistente) e **`L7` teve o destino do ponteiro preenchido** (§ 5.3),
seguindo `ENFRAQUECE`. **Saldo dos treze achados da § 2: três `BLOQUEIA`, oito `ENFRAQUECE`,
uma `DÚVIDA`, um `COSMÉTICO`.**

**E um achado fora da § 2 subiu a `BLOQUEIA`: `A17`** — os três regimes de atualização de
depósito —, que a § 6.4 havia descartado por critério de termo e que **escapara das duas
peneiras**. Corrigido em [`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) **§ 11**, com
ponteiro em [`02-atualizacao.md`](02-atualizacao.md) **§ 2-A**.

---

## 4. O padrão, e o que ele sugere

**Onze dos treze achados estão nas cadeias do CJF**, e **oito** deles em notas de item — não em
tabela. É a terceira vez que o corpus mostra o mesmo desenho: **a regra vive no item, e a tabela
não a exibe** (o `N-8`, a NOTA 3 de 4.9.1.1 e agora isto).

**A consequência de desenho é clara e fica registrada, não resolvida:** o schema
`cadeia-temporal` grava `notas[]` com `pagina_pdf`, e **a espinha consolidada não tem um lugar
equivalente**. Ela consolida **segmentos** com fidelidade e **notas** por paráfrase. Enquanto for
assim, toda nota de item é candidata a este arquivo.

> **Isto é observação, não proposta.** Se a espinha precisa de uma seção de notas literais por
> cadeia é decisão de outro bloco — e passa por saber quanto ela cresceria.

---

## 5. Bloco 20 — a reauditoria dos dez `ENFRAQUECE`

**O teste aplicado, e ele é único:** existe **sujeito, período e verba** para os quais a conta
feita **só com a espinha** dá número diferente da conta feita **com o extraído**? Sem esse caso
construído, **fica `ENFRAQUECE`** — e dizer isso é a resposta, não a sua ausência.

| # | Espinha | Extraído (item · `pagina_pdf`) | Muda resultado? |
|---|---|---|---|
| **L3** | detalhe § 5.3 delimita **D2** a *"não-Fazenda; e Fazenda jan/03–jun/09"*; o segmento `2012-05..2021-11` da Fazenda não herda `aplicacao` de ninguém | 4.2.2 NOTA 4 · **55**: os 70% da Selic *"incidirão independentemente da data de vencimento do principal ou do termo inicial dos juros de mora"* | **DÚVIDA — reclassificado no bloco 20**; ver § 5.2 |
| **L4** | **R3**: nominal reflete **M−1**, percentual reflete **M** | 4.1.2.4 · **42**: *"e terão aplicação prática no mês (ou dia) seguinte à data da divulgação"*; e o **IGP-M** nos exemplos | **não** — é defasagem de **publicação**, não de referência: numa conta retrospectiva todo índice já está divulgado. Onde há deslocamento real, o `aplicacao` da própria cadeia manda (**D1**–**D4**), e está na espinha. **`IGP-M` não é rótulo de segmento algum** |
| **L5** | **R1**, em 9 dos 13 arquivos | 4.2.1.1 NOTA 2 · **49** | **não** — a regra é idêntica; muda o **estatuto** (invariante do projeto × regra escrita). Lastro |
| **L6** | detalhe § 5.3.4 (`N-7`, alínea *b*) e § 5.3: *"a taxa legal segue **D1**"*, sem condição | `notas[]` de 4.8.3 e 4.9.3 · **83** e **86–87**: REsp 897.043, 1.102.552, 466.732 e a NOTA 4 (*"a taxa legal observará as mesmas orientações da Nota 7 do item 4.2.2"*) | **não** — a NOTA 4 é **remissão**, e o destino já está na espinha como D1. Os três REsp são lastro |
| **L7** | detalhe § 5.3.3 traz agora a **regra-base de 4.9.2, literal, com item e `pagina_pdf` 86** | `cjf.poupanca.juros-mora.json`, `JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA.regra` · **86**: 0,5% a.m.; 6% a.a. ou fração *pro rata* para **cruzados novos bloqueados** | **não** — **mas só depois do conserto do bloco 20; ver § 5.3** |
| **L8** | `02-atualizacao.md` § 8: *"capitalização mensal só em juros remuneratórios"* | 4.9.2 NOTA 1 · **86**, cinco precedentes | **não** — a exceção a **R4** está enunciada; faltam os acórdãos |
| **L9** | **R2** (cobertura até a data-base) e **R8** | 4.9.1.1 NOTA 1 · **85**: sentença omissa quanto ao termo final → *"o cômputo deve-se dar até o efetivo pagamento"* | **não** — o default da espinha **é** correr até a data-base do cálculo, que é o mesmo número. A regra integra a sentença; não desloca a conta |
| **L10** | detalhe § 5.3.3 traz as observações linha a linha **sem fundamento**, e **abreviadas** | `segmentos[].observacao` de `cjf.poupanca.correcao-monetaria.json`: Lei 8.024/1990 art. 6º, Lei 8.177/1991 art. 13 § único, Lei 8.660/1993 art. 7º § 2º, Lei 9.069/1995 art. 16 §§ 1º–2º | **não** — e **a abreviação foi testada**: a espinha corta *"desde **o último crédito efetuado**"* das janelas *pro rata* de jan/1991, abr/1993 e jun/1994. Esse é o **ancoradouro** da fração, e ele **está na espinha por outro caminho** — a NOTA 2 do aniversário (*"em cada aniversário, os índices relativos à data-base da conta"*), § 5.3.3. Mesma fração, mesmo número |
| **L11** | `D8-C21` invocado **pelo rótulo** em `01-dominio` § R3 e no detalhe § 6 | `bloco-08-jf-detalhe.md` linha 416 e `indexadores-tipo-catalogo.json`, `apoio_no_corpus.D8-C21.literal` | **não** — `IPC/IBGE` é `percentual` com ou sem o raciocínio transcrito |
| **L12** | **R7** (`01-dominio` § 2.4): Trabalhista → **ajuizamento** (CLT 883; Súmula 200/TST). **Nenhum** termo inicial próprio para `cjf.trabalhista.juros-mora` | `termo_inicial` de `cjf.trabalhista.juros-mora.json`, 4.7.2 · **78**: *"a partir da **notificação inicial** (Súmula n. 224 do STF), salvo determinação judicial em outro sentido"* | **SIM** — ver abaixo |

### 5.1 `L12` — o único promovido, e a evidência

**O caso.** Ação trabalhista na **Justiça Federal** (item 4.7.2), juros **1,0% a.m. simples**.
Reclamação **ajuizada em 10/03/1995**, **notificação inicial em 05/04/1995**. Pela espinha os
juros correm de **março/1995**; pelo literal, de **abril/1995**. **Um mês de juros sobre todo o
principal, e nenhum validador o pega** — R1, R2 e R3 passam nos dois cenários.

> **Correção de qualificador — bloco 20.** A primeira redação dizia *"ramo empresa pública ou
> prestador de serviços"*. **O número está certo e o qualificador era anacrônico:** o segmento
> aplicável em 1995 é o `1991-04..2001-07`, **sem `condicao`** — tronco. A bifurcação por devedor
> só nasce em **2001-08**. Em 1995 **não há ramo**, e a taxa de 1,0% a.m. simples vale para todos.

**E a falha é do mesmo desenho de `L1`: silenciosa.** A espinha **não escreve** termo inicial para
esta cadeia; quem precisa de um vai a **R7**, cuja única linha trabalhista é a da **Justiça do
Trabalho**. *"Usar o termo inicial da jurisdição"* — o argumento com que a § 2.1 absolveu `L12` —
**é justamente o que produz o erro**, porque a jurisdição da cadeia é federal e a linha que o
implementador encontra é celetista.

**A metade (a) de `L12` não foi promovida.** A cláusula *"salvo determinação judicial em outro
sentido"* é **R8** (título > escolha > default), enunciada na espinha. Lastro, não resultado.

**Correção:** [`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) **§ 5.2-B**, com os dois
literais, item e `pagina_pdf`, e ponteiro de um parágrafo em
[`02-atualizacao.md`](02-atualizacao.md) § 5. **R7 não foi tocada** — as duas regras ficam lado a
lado, e **a divergência entre fontes não se harmoniza**.

### 5.2 `L3` — a absolvição caiu, porque a razão dela **não existe**

**O que estava escrito:** *"o default de uma `cadeia-temporal` já é a competência. Não condicionar
é o comportamento que a espinha produz."*

**Esse default não está declarado em lugar nenhum, e o repositório diz o contrário em dois
lugares:**

1. **`skills/calculo-judicial-atualizacao/scripts/valida_cobertura.py` trata `aplicacao` ausente como VIOLAÇÃO**, não como
   default: *"Ausente o campo, não há ajuste declarado — e declarar é o requisito"*. A mensagem da
   violação é literalmente *"sem ajuste de defasagem declarado em `aplicacao`"*. Se a ausência
   significasse *"competência"*, R3 não teria o que acusar — e acusa;
2. **[`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) § 5.3** descreve **duas viradas** da
   poupança e do FGTS como **defeito justamente por estarem sem `aplicacao`**. Defeito e default
   são incompatíveis: não se chama de falta o que o sistema entrega por padrão.

**Reclassificado: `DÚVIDA`.** Não `ENFRAQUECE` — porque a razão que sustentava a absolvição é
falsa — e não `BLOQUEIA` — porque **não foi construído** o caso com sujeito, período e verba em
que a conta diverge, e a § 5 diz que sem esse caso não se promove. **O que a `DÚVIDA` registra é
que ninguém sabe qual é o comportamento certo**, e é essa a lacuna.

**O que falta para decidir, nominalmente:**

| # | Pergunta | Quem responde |
|---|---|---|
| 1 | O que a espinha manda fazer quando `aplicacao` **falta**? Hoje: **nada** — nem regra, nem default enunciado, e o validador acusa | **decisão de modelagem**, não leitura de fonte. Se houver default, ele tem de ser **escrito** e R3 tem de deixar de acusar; se não houver, todo segmento sem `aplicacao` é pendência |
| 2 | O segmento `2012-05..2021-11` da Fazenda (70% da Selic) tem defasagem própria? | **fonte** — o item 4.2.2 e suas notas. A NOTA 4 é **negativa** (diz do que *não* depende) e **não** diz quando o índice incide |
| 3 | Construído o caso com as duas leituras, a conta diverge? | **teste**, depois de 1 e 2 |

> **Não se inventa um default.** Se a espinha não declara o que acontece quando `aplicacao` falta,
> **isso é a lacuna**, e é ela que fica registrada aqui. **A § 2.1 continua como estava** — é o
> registro do que se pensou à época —, e este parágrafo é o que a refuta na metade `L3`, como o da
> § 5.1 faz na metade `L12`.

### 5.3 `L7` — o ponteiro existia e **não alcançava**

**A absolvição dizia:** *"a espinha não silencia: ela aponta"*. **O ponteiro existe; o destino não
tinha a regra.** [`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) § 5.3.3 trazia **só a
NOTA 2** de 4.9.2 — contas abertas a partir de **maio/2012** — e a nota dos **cruzados novos**
*da correção* (NOTA 3 de 4.9.1.1). **A regra-base do 4.9.2 — 0,5% a.m., e 6% a.a. ou fração *pro
rata* para cruzados novos bloqueados — não estava em ponto nenhum da espinha.** O caso que a
própria seção nomeia, **conta bloqueada em 1990**, chegava ao destino e **não encontrava taxa**.

**E a frase que sustentava o argumento é de outro item.** *"Registrados no JSON, fora dos
segmentos"* está na § 5.3.2 e é dita de **4.8.2 (FGTS)** — juros progressivos da Súmula 154/STJ —,
**não de 4.9.2**.

**Duas saídas, e a escolhida foi a primeira:** ou o ponteiro passa a alcançar, ou `L7` sobe de
classe. **A regra-base entrou na § 5.3.3, literal, com item e `pagina_pdf` 86**, junto da NOTA 1
(capitalização mensal, exceção a **R4**). Com o destino preenchido, `ponteiro declarado ≠ lacuna
escondida` volta a valer, e **`L7` segue `ENFRAQUECE`** — agora pela razão certa.

---

## 6. Varredura de **entidade ausente** — a busca que achou `servidor` por acaso

**A busca da § 1 é por paráfrase.** `L1` não foi achado por ela: foi achado **procurando um
sujeito que havia sumido**. Esta seção mecaniza essa outra busca.

### 6.1 Escopo — **contado**, não rotulado

| Dimensão | Escopo |
|---|---|
| **Onde se procurou a ausência** | os **15** arquivos `.md` de `docs/calculo/consolidado/` — os treze da § 1, **mais este** e **mais [`00-numeros.md`](00-numeros.md)**. *Eram 14 quando esta seção foi escrita; `00-numeros.md` nasceu no mesmo bloco, **contado e reconferido no bloco 20**. A conclusão não muda: `00-numeros.md` é **gerado** e só contém contagem, de modo que nenhum termo de sujeito, regime ou hipótese poderia aparecer ali.* |
| **De onde vieram os termos** | `docs/calculo/extracao/` — **69 arquivos**: **48** `.md` e **21** `.csv` — e os **32** `.json` de `../tabelas-normativas/`. **A unidade é ARQUIVO, e foi contada com `os.walk`** |
| **Normalização** | minúsculas, sem acento, **pontuação e hífen colapsados em espaço** nos dois lados. Sem isso `aviso-prévio` conta como ausente, e **contou**, na primeira passada — falso positivo corrigido |
| **Como os termos foram derivados** | **do texto extraído**, em duas etapas: (1) diferença de vocabulário — todo token de ≥ 5 letras que ocorre em **linha-gatilho** do extraído e **em nenhum** arquivo do consolidado; gatilhos: `NOTA`, `Para as ações`, `no caso de`, `tratando-se de`, `salvo`, `exceto`, `quando`, `hipótese`, `aplica-se`, `não se aplica`, `relativas a`, `referentes a`, `para fins`; (2) **sintagma nominal** capturado por regex depois de `Para ações de`, `créditos referentes a`, `tratando-se de`, `não se aplica a`, `aplica-se apenas a`, `salvo`, `exceto`, `no caso de`, `devidos a` |
| **Quantos foram testados** | a etapa (1) deu **2 507** tokens distintos em linha-gatilho, dos quais **792** ausentes do consolidado; a etapa (2) deu os sintagmas. Da união saiu a **lista de sondagem curada de 123 termos de sujeito, regime e hipótese**, cada um conferido um a um |

**O que a etapa (1) mostra sobre si mesma, e por que a curadoria é obrigatória:** dos 792
ausentes, a esmagadora maioria são **rótulos de CNAE** das duas séries de grau de risco
(`fabricacao`, `atacadista`, `terraplenagem`, `galinaceos`…) e **verbo de prosa de relatório**
(`apontou`, `deixando`, `verifiquei`). **Ausência mecânica não é perda**; o filtro é declarado
abaixo.

### 6.2 Os três motivos de descarte, e quantos caíram em cada

| Motivo | Exemplos verificados |
|---|---|
| **o consolidado usa outro nome** | `trintenária` → *"30 anos do termo inicial"* (`03-verbas.md` § 4.1) · `astreintes` → *"multa diária"* + teto do art. 412 do CC (`03-verbas.md`, `09-ordem-de-calculo.md`) · `empregadora` → **Fazenda subsidiária**, que tem seção própria e ramo vazio declarado (`02-atualizacao.md` § 3.3, `P9-01`) · `sentença proferida até 26/9/1999` → *"condição por data da sentença"* (detalhe § 5.3.6) · `expropriado` → `R-08-19`, precatório complementar (detalhe § 5.3.1) · `aviso previo` → `aviso-prévio`, **artefato de normalização** |
| **matéria fora do escopo, ou sob ponteiro declarado** | as parcelas de `trt3-18.1-incidencia-parcelas.json` — `gestante`, `licença-prêmio`, `salário-maternidade`, `auxílio-doença`, `habitação`, `aeronauta`, `inspetor`, `optante`/`não optante`, `empregado doméstico`: o consolidado remete à tabela **pelo arquivo**, com a contagem de parcelas × colunas (`04-descontos.md` § de ponteiros). **A unidade consolidada é a tabela, não a linha** · `SIMPLES NACIONAL` e `microempresa` → `SIMPLES` está em `04-descontos-detalhe.md`, `R-07-15` · `massa falida` → `02-atualizacao.md` § 2.2 e armadilha `A21`, com ponteiro |
| **palavra de prosa, não entidade** | `marítimo`, `militar`, `motorista`, `leiloeiro`, `urbano`, `temporário` — todos vindos das séries de **CNAE** · `custódia` e `tesouro` — expansão das siglas **Selic** e **LFT** · `delegado` — particípio de *"delegar ao TST"* · `exequente`, `exequenda`, `substituído`, `trabalhador`, `privilégio`, `transitados` — prosa forense |

### 6.3 Os achados, classificados

| Termo | Onde ocorre no extraído | Hipótese do que se perdeu | Classe |
|---|---|---|---|
| **`estatutário`** (e o sintagma *"contratos regidos pela CLT anteriores à promulgação da vigente Constituição"*) | `cjf.trabalhista.juros-mora.json`, campo `escopo_restrito`, item 4.7, `pagina_pdf` **77**; `bloco-08-jf-detalhe.md` § 3.4 (`D8-C17`) e `bloco-08-relatorio.md` | **O escopo inteiro do capítulo 4.7.** A espinha apresenta `cjf.trabalhista.juros-mora` como *"a cadeia trabalhista do CJF"*, sem dizer que ela alcança **só contratos celetistas anteriores à promulgação da vigente Constituição Federal** *(**`05/10/1988` é GLOSA**, não literal — ver abaixo)* e que **exclui por escrito servidores(as) estatutários(as)** | **BLOQUEIA** |
| **`contribuição confederativa`** · **`mensalidade de associado`** | `bloco-13a-descontos-proporcionais-detalhe.md` (quadro do cap. 12) e `bloco-13c-sindical-precatorios.md` | A **enumeração** dos institutos sindicais fica incompleta na espinha, que traz sindical e assistencial (`C12-03`, `06-encargos.md` § 7.2). **O próprio extraído diz que as duas são *"nomeada, não calculada"* e *"sem regra de cálculo"*** — nenhuma conta muda | ENFRAQUECE |
| **`conta vinculada`** | `bloco-02-criterios.md` — o FGTS apurado vai *"depositado em conta vinculada"*, e entra **separadamente** no resumo | Destino e **apresentação separada** do FGTS no resumo de cálculo. Afeta a forma do resultado, não seu valor | ENFRAQUECE |
| os **~40 demais** da lista de sondagem | ver § 6.2 | — | RUÍDO |

**Saldo: um `BLOQUEIA`, dois `ENFRAQUECE`, o resto `RUÍDO`.**

> **E o `BLOQUEIA` é o mesmo mecanismo de `L1`, na mesma cadeia em que `L12` caiu.** `servidor`
> havia sumido do consolidado; `estatutário` também havia — **e é a palavra com que a fonte
> EXCLUI um sujeito**, não a com que o inclui. **Uma cláusula de exclusão desaparecida é tão
> silenciosa quanto um ramo desaparecido**, e é pior: faz a cadeia parecer aplicável a todo
> mundo.

**Corrigido junto com `L12`, em [`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) § 5.2-B**
— os dois literais governam a mesma cadeia, e enunciar o termo inicial sem dizer de quem ele é
seria repetir o defeito.

> **Marcação de glosa — bloco 20.** A data **`05/10/1988`** é **inferência**, não literal: o
> `escopo_restrito` escreve *"anteriores à promulgação da vigente Constituição Federal"*. A glosa
> está **correta** — e numa seção cujo produto é **o literal**, inferência tem de aparecer como
> inferência, ou o leitor a cita como fonte. Marcada aqui e no destino (§ 5.2-B).

### 6.4 `A17` — a ausência vizinha que **era `BLOQUEIA`**, e escapou de duas peneiras

**`A17` — os três regimes de atualização de depósito** (judicial = poupança TR + 0,5% a.m.;
recursal = FGTS TR + 3% a.a.; crédito trabalhista = art. 39 da Lei 8.177/91), `pagina_pdf` **329**,
em `../extracao/trabalhista/bloco-13e-capitulo16.md` § 5 — **não estava no consolidado**.

**A primeira redação desta seção o descartou, e o descarte não se sustentava.** Ela dizia: o termo
`depósito recursal` **ocorre** no consolidado ([`05-imputacao.md`](05-imputacao.md) § 4), logo *"é
lacuna de REGRA, não de entidade"*, e o critério da § 6 é o termo. **O fato é verdadeiro; a
consequência, não.** O termo está lá **qualificando o alcance do item "i" da ADC 58** — não a
atualização do depósito. Os **três regimes** não estavam em arquivo nenhum do consolidado: busca
literal por `TR + 3% a.a.`, `3% ao ano`, `TR +` e `poupança … 0,5%` devolveu **zero**.

**E o descarte fez `A17` escapar das DUAS peneiras:** não entrou na reauditoria dos dez da § 5
(que cobriu `L1`–`L13`) nem na varredura de entidade desta § 6 (excluído pelo critério do termo).
**Regra que não é examinada por peneira alguma não é "insumo registrado" — é lacuna.**

**O teste da § 5 aplicado, e ele passa:** são **três taxas diferentes conforme a natureza do
depósito**, e a **dedução do depósito é passo do cálculo** — passo **11** de
[`09-ordem-de-calculo.md`](09-ordem-de-calculo.md) § 3. Atualizar um depósito **recursal** pela
régua do **crédito** troca **3% a.a.** por **1% a.m.**. **Muda o número, e muda o saldo.**

**Classe: `BLOQUEIA`.** **Corrigido em**
[`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) **§ 11**, com os três regimes, item e
`pagina_pdf` **329** — conferida na extração antes de escrever —, e **ponteiro curto na espinha**,
[`02-atualizacao.md`](02-atualizacao.md) **§ 2-A**. Mesma forma de `L1`, `L2` e `L12`.

> **Não é o mesmo eixo da § 5 de `05-imputacao.md`**, que registra as três posições sobre a
> **data** da dedução. Aquilo é *quando* deduzir; isto é *com que régua* o depósito chega lá.
