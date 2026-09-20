# Literais que ficaram na extração

**Insumo, não errata.** O bloco 18 registrou que, para escrever `fgts.md` e `poupanca.md`, foi
preciso **buscar no JSON literais que o consolidado apenas parafraseia**. Este arquivo varre o
consolidado atrás do mesmo padrão e **lista** o que encontrou. **Não corrige tudo** — a decisão
sobre uma nova passada na espinha é de outro bloco.

**Só o que é `BLOQUEIA` foi corrigido neste bloco.** São **dois achados**, e a correção está em
[`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) § 5.2-A e em
[`02-atualizacao.md`](02-atualizacao.md) § 5.

---

## 1. Escopo da varredura — a negativa exige universo declarado

*"O literal não está no consolidado"* é afirmação de ausência. O universo em que se buscou:

| Dimensão | Escopo |
|---|---|
| **Onde se procurou a paráfrase** | os **treze** arquivos de `docs/calculo/consolidado/` — `00-calendario-de-cortes`, `00-validacao-casos`, `01-dominio-e-invariantes`, `02-atualizacao`, `02-atualizacao-detalhe`, `03-verbas`, `04-descontos`, `04-descontos-detalhe`, `05-imputacao`, `06-encargos`, `07-leitura-do-corpus`, `08-nacional-e-regional`, `09-ordem-de-calculo` |
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
| **L3** | Os **70% da Selic** incidem *"independentemente da data de vencimento do principal ou do termo inicial dos juros de mora"* | fórmula sim (detalhe § 5.3.3, via 4.9.2); **a cláusula de eixo, não** | 4.2.2 NOTA 4, `pagina_pdf` **55** | a regra que **neutraliza o eixo** — quem condicionar ao vencimento erra, e não há no consolidado o que o desminta | ENFRAQUECE |
| **L4** | Definição de índice **percentual**, segunda metade | `01-dominio-e-invariantes.md` **R3** | item 4.1.2.4, `pagina_pdf` **42** — `indexadores-tipo-catalogo.json`, `fonte.literal` | *"e terão **aplicação prática no mês (ou dia) seguinte à data da divulgação**"* — R3 enuncia a **defasagem de referência** e cala sobre a **de publicação**; some também o **IGP-M** da lista de exemplos | ENFRAQUECE |
| **L5** | **R1** — a Selic engloba, e o IPCA-E sai | R1, em 9 dos 13 arquivos | 4.2.1.1 NOTA 2, `pagina_pdf` **49** | R1 aparece como **invariante do projeto**; o literal a põe como **regra escrita da fonte**, com item e página. Sem ele, R1 não é citável | ENFRAQUECE |
| **L6** | As **quatro notas de 4.8.3 e 4.9.3** (FGTS e poupança) | detalhe § 5.3.4 — `N-7` e a alínea *b* | `cjf.fgts.juros-mora.json` e `cjf.poupanca.juros-mora.json`, `notas[]`, `pagina_pdf` **83** e **86–87** | os **precedentes** (REsp 897.043, 1.102.552, 466.732) e a NOTA 4, que **remete a taxa legal à Nota 7 de 4.2.2** — é a origem de `aplicacao: mes-posterior-a-competencia` nessas duas cadeias | ENFRAQUECE |
| **L7** | **Juros remuneratórios da poupança** — 4.9.2, regra-base | o eixo sim (detalhe § 5.3.3); **a regra, não** | `cjf.poupanca.juros-mora.json`, `JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA.regra`, `pagina_pdf` **86** | **0,5% a.m.** e **6% a.a. ou fração *pro rata* para cruzados novos bloqueados**, com os cinco fundamentos — um **componente de valor** que incide **concomitantemente** aos moratórios | ENFRAQUECE |
| **L8** | Os remuneratórios da poupança são **capitalizados mensalmente** | `02-atualizacao.md` § 8: *"capitalização mensal só em juros remuneratórios"* | 4.9.2 NOTA 1, `pagina_pdf` **86** | os **cinco precedentes** que sustentam a exceção a **R4**. A regra está; o lastro, não | ENFRAQUECE |
| **L9** | Sentença que manda aplicar os índices da poupança **sem fixar termo final** | **nenhuma** | 4.9.1.1 NOTA 1, `pagina_pdf` **85** | *"o cômputo deve-se dar **até o efetivo pagamento**"* — regra de integração de sentença omissa; sem ela a conta não tem fecho declarado | ENFRAQUECE |
| **L10** | **Fundamentos legais** das observações linha a linha da poupança | detalhe § 5.3.3 traz as observações **sem fundamento** | `cjf.poupanca.correcao-monetaria.json`, `segmentos[].observacao` | os decretos e leis: **art. 6º da Lei 8.024/1990** (mar/1990), **§ único do art. 13 da Lei 8.177/1991** (jan/1991), **§ 2º do art. 7º da Lei 8.660/1993** (abr/1993), **§§ 1º e 2º do art. 16 da Lei 9.069/1995** (jun/1994) e o *pro rata* da ORTN em fev/1986 | ENFRAQUECE |
| **L11** | **`D8-C21`** — a classificação do IPC/IBGE | invocado em `01-dominio` § R3 e no detalhe § 6 **pelo rótulo** | `bloco-08-jf-detalhe.md` **linha 416** e `indexadores-tipo-catalogo.json`, `apoio_no_corpus.D8-C21.literal` | *"O IPC/IBGE é índice percentual, e o item 4.1.2.4 diz que percentuais 'refletem a inflação do próprio mês de competência'"* — o **raciocínio** que separa fonte de dedução. Citado de segunda mão | ENFRAQUECE |
| **L12** | **Termo inicial dos juros**, literal, das cadeias do CJF | `01-dominio` § 2.4, **R7**, em tabela de três linhas | `termo_inicial` de `cjf.condenatorias-gerais.juros-mora`, `cjf.fgts.juros-mora`, `cjf.poupanca.juros-mora` e `cjf.trabalhista.juros-mora` | (a) a cláusula ***"salvo determinação judicial em outro sentido"***, que torna o termo **sobrescrevível pela sentença** — e **D2 tem o termo inicial como operando**; (b) o CJF escreve *"**notificação inicial** (Súmula 224 do STF)"* para o trabalhista, onde R7 escreve *"ajuizamento"* | ENFRAQUECE |
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

**L7 e L8 chegam perto por outro lado.** A espinha **declara** que 4.8.2 e 4.9.2 ficaram fora das
cadeias e **diz onde estão** (*"Registrados no JSON, fora dos segmentos"*, detalhe § 5.3.2).
**Ponteiro declarado não é lacuna escondida** — é a mesma solução da ressalva de cobertura de
`00-calendario-de-cortes.md` § 1 para `CH-01`–`CH-05`. **ENFRAQUECE.**

---

## 3. O que foi corrigido neste bloco

**Só L1 e L2.** Entraram em [`02-atualizacao-detalhe.md`](02-atualizacao-detalhe.md) como
**§ 5.2-A**, com os dois literais, item e `pagina_pdf`, e um ponteiro de uma linha na espinha
[`02-atualizacao.md`](02-atualizacao.md) § 5.

**Nada mais foi promovido.** Onze achados continuam `ENFRAQUECE` e um é `COSMÉTICO`; nenhum
deles foi reescrito para justificar trabalho. **A lista é o produto.**

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
