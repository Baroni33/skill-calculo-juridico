# skill-calculo-juridico

**Base de conhecimento e skills para cálculo judicial brasileiro** — trabalhista e cível, com
ramos tributário federal e previdenciário. Repositório **separado** do SaaS: aqui ficam a
extração normativa, as tabelas de regra e as skills; lá fica o produto.

> **O motor é de produto, não de cliente.** Nenhuma skill cita nome de cliente, nem assume UF,
> tribunal ou polo processual. Onde há variante regional, ela entra por **cadastro**, sob a
> chave `(regra, tribunal, competência)`.

**A skill não é o entregável. O código que um agente constrói lendo a skill é.**

---

## Instalação

**As skills são *model-invoked*: disparam pela `description` do frontmatter, lida no startup.**
**Não há comando de invocação nem instalador** — o modelo decide carregar quando a conversa bate
com o gatilho.

### Via plugin — dois comandos

```
/plugin marketplace add Baroni33/skill-calculo-juridico
/plugin install calculo-judicial-br
```

O manifesto vive em [`.claude-plugin/`](.claude-plugin/) — `marketplace.json` e `plugin.json`.

> **O repositório é PRIVADO.** O acesso do marketplace a repositório privado depende da
> credencial de git da máquina. **Não foi testado** — se falhar, use a instalação manual.

### Manual — copiar quatro pastas

```
skills/calculo-judicial-core/           ->  .claude/skills/
skills/calculo-judicial-atualizacao/
skills/calculo-trabalhista-liquidacao/
skills/indices-judiciais/
```

Para uso global, `~/.claude/skills/`; para um projeto só, `.claude/skills/` na raiz dele.
**Copie a pasta inteira** — cada skill tem `references/` que o `SKILL.md` aponta.

**O que NÃO copiar:**

| | Por quê |
|---|---|
| **`docs/`** | é a **base de conhecimento**, não skill. As skills apontam para ela quando precisam; copiá-la para `.claude/skills/` não faz nada |
| **`scripts/`** | são **ferramentas de pipeline** — validam o repositório, não o cálculo de ninguém |
| **`tests/`** · **`skills/00-cobertura-casos.md`** | verificação e artefato de auditoria |

> **Uma armadilha para a decisão seguinte, registrada aqui porque é fácil de
> pisar.** O bloco 24 classificou os `.py` entre **ferramenta de pipeline** e
> **script de skill**, e deixou a decisão de promover algum para depois.
> **`valida_regimes.py` e `valida_parametros.py` leem o catálogo em
> `docs/calculo/tabelas-normativas/`** — se forem promovidos, **a instrução
> acima de não copiar `docs/` já os quebra**. Ou o catálogo viaja junto, ou o
> caminho vira argumento obrigatório. **`valida_taxa_legal.py` não tem esse
> problema:** é autocontido, e é por isso que é o caso declarado.


### A linguagem do motor e a do script não são a mesma

**O motor-alvo é C#** — backend do produto, com `System.Decimal` nativo. **A skill não pressupõe
C#**: exige **aritmética decimal exata, com ponto flutuante binário proibido no caminho de
cálculo**. O tipo concreto é escolha do implementador.

> **Os scripts de skill permanecem em Python**, e isso é deliberado: eles rodam **no ambiente do
> agente**, para verificar a implementação — **não no produto**. `valida_taxa_legal.py` é o caso
> central, e implementa **R11**.

**Script executado pela skill não entra no contexto — só a saída.**

---

## As duas fontes primárias

**Nenhum PDF é versionado aqui** — os dois vivem fora do repositório, referenciados por caminho
em [`docs/calculo/fontes.md`](docs/calculo/fontes.md).

| Manual | Emissor | Edição |
|---|---|---|
| **Cálculos da Justiça do Trabalho** | TRT-3, Secretaria de Cálculos Judiciais | rótulo **julho/2016** — **ver a ressalva** |
| **Procedimentos para os Cálculos na Justiça Federal** | Conselho da Justiça Federal | **Resolução CJF 990/2026** — edição vigente |

### O manual trabalhista não é o que o rótulo diz — e está materialmente defasado

**A capa não traz data alguma.** O rótulo *"2016"* vem da base do projeto, e **o conteúdo é
posterior**: transcreve acórdão publicado em **19/12/2016**, traz salário mínimo de 2017, tabelas
de IRRF e de contribuição previdenciária de 2017, e calendários até 2020. **É, no mínimo, de
2017.**

**A consequência muda a leitura:** ele **não é anterior ao IRR-849** — ele o transcreve e comenta.
**Continua anterior à Lei 13.467/2017**, cuja vigência é 11/11/2017.

**E está materialmente defasado em quatro frentes**, todas com destino registrado no confronto
normativo:

| Frente | O que mudou depois |
|---|---|
| **correção monetária** | ADC 58, Lei 14.905/2024, EC 113/2021 e EC 136/2025 |
| **juros** | taxa legal desde set/2024; Selic única desde dez/2021 |
| **honorários** | art. 791-A da CLT — a sucumbência **passa a existir** na Justiça do Trabalho |
| **contribuição sindical** | torna-se **facultativa** |

> **`docs/calculo/00-base-normativa.md` prevalece sobre os dois manuais** sempre que houver
> conflito.

---

## Estado

**Extração completa.** As **564 páginas** dos dois manuais têm **destino registrado** — cobertas,
ou com a razão de não terem sido, página a página. Ver
[`docs/calculo/extracao/mapa-de-cobertura.md`](docs/calculo/extracao/mapa-de-cobertura.md).

**Confronto normativo fechado.** Cada regra extraída recebeu veredito contra a base — `VIGENTE`,
`SUPERADO`, `BIFURCADO`, `INAPLICÁVEL` ou `SEM FONTE`. **Dois terços são `BIFURCADO`**, e a razão
é estrutural: nem a Reforma, nem a ADC 58, nem a Res. 225/2025 do TST revogaram com efeito
*ex nunc* — **todas cortaram no tempo**.

> **Consequência de arquitetura:** o motor **não pode ter uma tabela de regras vigentes**.
> Precisa de **cadeia temporal por ponto**. Um `SUPERADO` mal lido apaga o período anterior ao
> corte — e a maioria das contas atravessa o corte.

**Consolidação e skills construídas.** Quatro skills, com `references/` divididas entre
**nacional** e **regional**.

> **Toda contagem — cadeias, segmentos, testes, violações, arquivos — vive em
> [`docs/calculo/consolidado/00-numeros.md`](docs/calculo/consolidado/00-numeros.md), gerado por
> script.** Nenhum outro arquivo publica número de resultado. Número de **conteúdo normativo**
> (42,72% em jan./1989, `art. 457`, `pagina_pdf` 42) **não é resultado, é o dado**, e fica onde
> está. Número em **relatório de bloco** é registro datado e **não se atualiza**.

**A regra nasceu de três reincidências**, e vale citá-las porque são o exemplo que a ensina: o
bloco 19 publicou *"R1 e R2 não se moveram"* em **quatro arquivos** depois de R1 ter ido a 21; o
bloco 18 deixou *"14 ok, 10 erros"* num runbook depois de os erros sumirem; o bloco 17 deixou
*"97 de 97 segmentos"* depois de virarem 126.

> **Número digitado em quatro lugares envelhece em quatro lugares.**

---

## Por onde começar

**Nesta ordem.** Pular etapa produz número plausível com a conta inteira no regime errado.

| # | Leia | Por quê |
|---|---|---|
| **1** | [`docs/calculo/00-base-normativa.md`](docs/calculo/00-base-normativa.md) | **Prevalece sobre os manuais.** Regras vigentes e as invariantes R1–R24 |
| **2** | [`02-base-normativa-verbas.md`](docs/calculo/02-base-normativa-verbas.md) e [`02a-adendo-lacunas-verbas.md`](docs/calculo/02a-adendo-lacunas-verbas.md) | o que cada verba é — e o que **falta** saber sobre ela |
| **3** | [`consolidado/00-calendario-de-cortes.md`](docs/calculo/consolidado/00-calendario-de-cortes.md) | **A chave primária.** Um par `(data, eixo)` por corte |
| **4** | [`consolidado/`](docs/calculo/consolidado/) | espinha por assunto, com o detalhe ao lado |
| **5** | [`skills/`](skills/) | o que um agente lê para construir o motor |

### A chave não é a data — é o par `(data, eixo)`

**Dezoito pontos compartilham 11/11/2017, e cortam por três eixos diferentes:** competência do
fato gerador, **data de propositura da ação** e **modalidade do acordo**.

> Dois processos ajuizados no mesmo dia, com parcelas da mesma competência, **recebem respostas
> diferentes**. Quem aplicar a data uniformemente erra os honorários de toda ação proposta antes
> dela com parcelas posteriores — e vice-versa.

---

## Estrutura

```
docs/calculo/
  00-base-normativa.md         fonte de verdade — prevalece sobre os PDFs
  fontes.md                    onde estão os manuais, e os offsets de paginação
  pendencias.md                o que está em aberto e o que bloqueia
  extracao/trabalhista/        um arquivo por bloco de páginas
  extracao/justica-federal/    passada única
  tabelas-normativas/          JSON de regra — cadeias temporais, catálogos, manifesto
  confronto-normativo/         os vereditos, um por regra
  consolidado/                 espinha + detalhe — é daqui que a skill se escreve
skills/
  calculo-judicial-core/           domínio, invariantes, aritmética, comparador
  calculo-judicial-atualizacao/    cadeias período→indexador, references/ por jurisdição
  calculo-trabalhista-liquidacao/  verbas, descontos, encargos
  indices-judiciais/               semântica dos índices e contrato de séries
scripts/calculo/             validadores determinísticos
tests/fixtures/calculo/      fixtures de aceite
```

**Cada pasta tem `README.md`** com propósito, o que entra e o que não entra.

---

## O que bloqueia produção hoje

**Nenhuma destas se fecha inventando dado.** Estão abertas porque fechá-las exigiria **escolher
onde a fonte não escolhe**.

| Pendência | Por que está aberta |
|---|---|
| **`P18-02` — três cadeias do CJF** | juros de mora da desapropriação **direta** e **indireta**, e juros da contribuição previdenciária. **A tabela das três nunca foi extraída linha a linha** — gerá-las exigiria reconstruir a **estrutura**, pior que inventar um valor |
| **índices `indeterminado` sem fonte** | doze rótulos. O item 4.1.2.4 do CJF nomeia **sete** índices, e **lista exemplificativa não autoriza estender por semelhança de nome**. Virada com ponta indeterminada **bloqueia** sob `R3-INDETERMINADO` |
| **taxa legal — `P19-01`** | **não espera fonte, espera decisão.** A fórmula compõe um `percentual` (Selic) com um `janela-deslocada` (IPCA-15), e **a tricotomia de R3 não tem resultado para essa composição** |
| **dois bloqueios aritméticos — pp. 266 e 269** | deltas de **10,00 exatos** e **2.036,51 com índice sem origem**. **Nenhum é arredondamento**, e o segundo propaga |
| **`pr.imputacao` sem default** | o critério proporcional é **aplicado 101 vezes e fundamentado zero**; `art. 354 do CC` tem **zero ocorrências em 471 páginas**. **Não são duas normas concorrentes — é uma norma contra um costume de liquidação sem base declarada.** Arbitrar seria o motor **tomar posição jurídica**. Amplitude medida: **até 23,83%** do saldo |
| **§ 7 de `00-base-normativa.md`** | enuncia R3 com uma lista que a fonte não sustenta. **É fonte de verdade do usuário** — divergência **declarada**, correção **fora do agente** |

### Dependências externas — dado que o repositório não tem

| O que falta | O que trava |
|---|---|
| **Tabela Única do CSJT** | a cadeia trabalhista **anterior a março de 1991**. O cap. 7 do manual **delega** a ela — é **série**, não regra (`P9-02`). **É também a dependência que torna o motor nacional** |
| **séries históricas de normas coletivas** | `pr.planos-economicos` — dez planos, 1986–1996 — fica **bloqueado por falta de série** |
| **faixas do art. 85, § 3º, do CPC** | a **regra estrutural** está fechada com fonte primária; **os valores não estão transcritos**. Sem eles, não se calcula honorário por faixa |

---

## Cobertura regional — o que alcança hoje

**Quinze fontes regionais, de três tribunais:** **TRT-3** (treze), **TRT-4** (uma — a posição da
SEE sobre RSR em comissões) e **TJMG** (uma — a tabela da CGJ). São **nove verbetes** e **seis
fontes não-verbete**, entre elas a IN que fixa **todas as custas de execução** do TRT-3.

> **Outra região exige CADASTRO, não refatoração.** A chave `(regra, tribunal, competência)` já
> existe, e o **fallback nacional está identificado para catorze das quinze**.

**E a premissa que cai junto:** a atualização monetária trabalhista é **nacional** desde a
Res. CSJT 8/2005 — hoje Res. CSJT 380/2024, com o **PJe-Calc** como sistema de toda a Justiça do
Trabalho.

> **O manual do TRT-3 é fonte procedimental de uma região que aplica norma nacional.** Sua
> **aritmética não é prática regional divergente** — regional são **os verbetes que ele invoca**.

**R24 — ausência de súmula regional não é erro.** Resolve pela regra nacional e marca a conta
`sem cobertura regional`. Mesma forma da R14: **o dado não existe, não a regra**.

---

## Validadores

```
python -m unittest discover -s scripts/calculo -p "test_*.py"
python scripts/calculo/gera_numeros.py             # regenera 00-numeros.md
python scripts/calculo/gera_numeros.py --verifica  # falha se divergir do estado real
python scripts/calculo/valida_cadeias.py           # R1, R2, R3 sobre as cadeias reais
python scripts/calculo/valida_bloco_tabelas.py     # exit 0 = sem erro de extração
python scripts/calculo/valida_parametros.py --catalogo-ok
```

| Script | Verifica |
|---|---|
| `valida_cobertura.py` | **R1** englobamento concorrente · **R2** lacuna e sobreposição · **R3** virada entre classes de indexador |
| `valida_cadeias.py` | as cadeias reais, com **manifesto assimétrico** — cresce sozinho, **só encolhe por edição deliberada** |
| `valida_taxa_legal.py` | **R6** piso zero · **R11** razão, não subtração · **R12** decimal e truncamento |
| `valida_bloco_tabelas.py` | contagem contra o PDF, faixas, vigências, proveniência |
| `valida_parametros.py` | camada de norma coletiva — **R14 a R18**, precedência, conflito, piso legal |
| `test_ponteiros.py` | **ponteiro morto**, com ledger que distingue narrativa histórica |
| `test_numeros.py` | **número de resultado digitado** fora de `00-numeros.md` |

**`valida_bloco_tabelas.py` separa erro de extração de divergência do original**, e só sai com
código não-zero no primeiro. **Divergência é resultado esperado do trabalho:** o manual tem erros
de digitação e calendários com dias faltando, e eles ficam **registrados, não corrigidos**.

---

## Três regras que economizam retrabalho

**Truncamento, nunca arredondamento.** Os dois pares de validação do Manual CJF só fecham com
truncamento; half-up erra o último dígito em ambos. **E o critério é POR ETAPA, não global** —
cinco cadeias de arredondamento convivem, e a do NMP **não é half-up**.

**`encoding='utf-8'` explícito em toda leitura.** Windows assume cp1252 e corrompe acentuação
silenciosamente. A mojibake no terminal é renderização do console, **não corrupção do arquivo**.

**Afirmação de ausência exige escopo declarado — e contado.** *"Zero ocorrências no segmento"* e
*"zero ocorrências em 471 páginas"* são afirmações diferentes, **e só a segunda sustenta uma
negativa sobre o manual**. Escopo declarado **errado** é pior que escopo não declarado, porque
**parece auditado**.

---

## Histórico — o que cada bloco descobriu

> **Registro datado.** Os números aqui valem para o fechamento de cada bloco e **não se
> atualizam** — um registro que se atualiza sozinho deixa de ser registro. Estado corrente em
> [`00-numeros.md`](docs/calculo/consolidado/00-numeros.md).

Fases 0 e 1 fechadas (contrato de saída e triagem).

**Fase 2 encerrada no bloco 13.** Os dois manuais estão extraídos, com destino registrado
em todas as 564 páginas.

**Fase 3 (confronto normativo) encerrada no bloco 14** — ver
[`docs/calculo/confronto-normativo/`](docs/calculo/confronto-normativo/). **50 vereditos,
zero `SEM FONTE`**, e **32 deles `BIFURCADO`**: nem a Reforma, nem a ADC 58, nem a
**Resolução 225/2025 do TST** revogaram com efeito *ex nunc* — todas cortaram no tempo.

> **Consequência de arquitetura:** o motor não pode ter *uma* tabela de regras vigentes. Precisa
> de **cadeia temporal por ponto**, como já tem para índices. Um `SUPERADO` mal lido apaga o
> período anterior ao corte — e a maioria das contas atravessa o corte.

**Fase 4 (consolidação) encerrada no bloco 15** — ver
[`docs/calculo/consolidado/`](docs/calculo/consolidado/) e
[`docs/calculo/extracao/bloco-15-relatorio.md`](docs/calculo/extracao/bloco-15-relatorio.md).
Treze blocos de extração e os 50 vereditos viraram **onze arquivos**, espinha e detalhe. Os
**33 casos difíceis** foram o critério de aceite: **31 respondidos, 2 parciais por ponteiro
ausente, zero não respondidos**.

**A consolidação corrigiu a própria instrução que a governava.** "Implementar por data" está
incompleto: **dezoito pontos compartilham 11/11/2017 e cortam por três eixos diferentes** —
competência do fato gerador, data de propositura da ação e modalidade do acordo.

> **A chave não é a data. É o par `(data, eixo)`.**

Duas decisões do bloco 15 mudam o motor: **`pr.intertemporal` ganhou default** — `tempus regit
actum`, fundado no **Tema 23 do TST** (Pleno, 25/11/2024, 15 × 10, transitado, modulação negada
por unanimidade), com `R20-EXCEÇÃO` caindo de cinco casos para **quatro**; e a numeração das
fases em `01-plano-extracao.md`, que estava invertida, foi corrigida — **o confronto vem antes
da consolidação**.

**Fase 5 (build das skills) encerrada no bloco 16** — ver
[`skills/`](skills/) e
[`docs/calculo/extracao/bloco-16-relatorio.md`](docs/calculo/extracao/bloco-16-relatorio.md).
**Quatro skills**, todas abaixo de 500 linhas, com `references/` divididas entre **nacional** e
**regional**. Os **33 casos difíceis** fecham em **33 COBERTO, zero perdido na transposição**.

**Uma premissa do projeto caiu, e é estrutural.** A atualização monetária trabalhista é
**nacional** desde a Res. CSJT 8/2005 (hoje Res. CSJT 380/2024, com o PJe-Calc como sistema de
toda a Justiça do Trabalho). **O manual do TRT-3 é fonte procedimental de uma região que aplica
norma nacional — sua aritmética não é prática regional divergente.** Regional são os verbetes que
ele invoca, e **são quinze, de três tribunais** (TRT-3, TRT-4, TJMG), não três.

> **As cadeias históricas trabalhistas são NACIONAIS, e o prefixo dizia o contrário.** Chamavam-se
> `trt3.hist.*`, e um motor que resolvesse cadeia por prefixo de tribunal **não acharia cadeia
> nenhuma para TRT-1, TRT-2 ou TRT-15**. **Renomeadas para `trab.hist.*` no bloco 17**, junto com
> sete `trt3.trabalhista.*` que são IRRF, INSS, GILRAT, URV e RSR — lei federal.

Daí a invariante nova: **R24 — ausência de súmula regional não é erro.** Resolve pela regra
nacional e marca a conta `sem cobertura regional`. Chave: `(regra, tribunal, competência)`.

**Bloco 17 — correções estruturais antes da aceitação** — ver
[`docs/calculo/extracao/bloco-17-relatorio.md`](docs/calculo/extracao/bloco-17-relatorio.md).

**R3 deixou de ser letra morta.** O campo `tipo_indexador` não existia em série nenhuma; passou
a estar em **todos os segmentos de todas as cadeias** — 97 no bloco 17; quantos hoje, em
[`00-numeros.md`](docs/calculo/consolidado/00-numeros.md) —, e o
validador bloqueia a virada entre tipos sem ajuste de defasagem. **Dez dos vinte e oito indexadores ficaram `indeterminado`** — a fonte nomeia sete, e
estender por semelhança de nome era a dedução proibida. **A TR foi rebaixada:** era `percentual`
por inferência formal, e **inferência declarada não é fonte**.

**A ordem de cálculo ponta a ponta virou artefato próprio** —
[`09-ordem-de-calculo.md`](docs/calculo/consolidado/09-ordem-de-calculo.md), **19 passos com
`FONTE` / `DERIVADO` / `COMPOSIÇÃO` declarados**. O corpus ensina cada operação e **nunca as
encadeia**; a ordem é composição deste projeto, e agora é contestável em vez de diluída.

> **Regra de projeto nova:** o identificador identifica; **o escopo se declara em campo**. Nunca
> pelo prefixo do id nem pelo nome do arquivo. As cadeias `trt3.hist.*` viraram `trab.hist.*` — e
> a descoberta por prefixo em `valida_cadeias.py`, que fazia o validador cair de 11 cadeias para
> 7 **em silêncio**, passou a ser por conteúdo.

**Bloco 18 — lacunas de consolidação** — ver
[`docs/calculo/extracao/bloco-18-relatorio.md`](docs/calculo/extracao/bloco-18-relatorio.md).

**FGTS e poupança tinham cadeia própria no cap. 4 do CJF e nunca haviam sido consolidados.** A
varredura que o precedia mostrou que **não eram duas: são dez** — inclusive **a desapropriação
indireta inteira** e um **segundo FGTS**, o fiscal do item 2.4.4.1, com critério `JCM` em vez de
`JAM`. As oito restantes ficam registradas como `P18-02`.

> **E uma que parecia lacuna e não é:** a correção trabalhista do 4.7.1 **não tem tabela** — o
> manual delega ao TST. **Afirmá-la ausente seria afirmar ausência de algo que a fonte nunca
> prometeu.**

**Ao fim do bloco 18: 15 cadeias, 267 testes** *(registro datado — o estado de hoje está em
[`00-numeros.md`](docs/calculo/consolidado/00-numeros.md))*. A contagem deixou de ser constante e passou a ser **manifesto
assimétrico**: cresce sozinho quando aparece cadeia nova, e **só encolhe por edição deliberada** —
porque cadeia a mais é crescimento e **cadeia a menos é regressão**. E entrou
`test_ponteiros.py`, com *ledger* que distingue ponteiro morto de narrativa histórica pelo par
`(alvo, arquivo)`.

**Bloco 19 — classificação de índices** — ver
[`docs/calculo/extracao/bloco-19-relatorio.md`](docs/calculo/extracao/bloco-19-relatorio.md).

**A dicotomia nominal/percentual do manual é insuficiente, e os dois índices mais usados hoje
ficam fora dela.** R3 ganhou **`janela-deslocada`** — IPCA-15 e IPCA-E refletem **metade de M−1 e
metade de M**, porque o período de coleta vai do dia 16 do mês anterior ao 15 do mês de
referência. E **`englobante` foi retirado**: era um fato de R1 dentro do campo de R3, e deixava a
SELIC **cega para defasagem**. O englobamento não se perdeu — mudou para o campo `engloba`, que já
existia.

**Ao fim do bloco 19: 20 cadeias, 156 segmentos, 311 testes** *(registro datado — ver
[`00-numeros.md`](docs/calculo/consolidado/00-numeros.md))*. Dos 36 rótulos de indexador, **32 segmentos seguem
`indeterminado`** — e a distinção que o bloco introduziu é entre *"sem fonte"* e *"a fonte diz que
não cabe"*: **a TR é divulgada para período entre datas de aniversário, não para mês calendário**.
Essa **não se fecha esperando fonte**.

> **`indeterminado` continua sendo a resposta correta onde falta fonte, e continua bloqueando.**
> Foi o que impediu `BTNF` de herdar do `BTN`, a taxa legal de herdar da SELIC, e o `IPC` nu de
> herdar do irmão.

**Bloco 20 — fechar a espinha contra o extraído** — ver
[`docs/calculo/extracao/bloco-20-relatorio.md`](docs/calculo/extracao/bloco-20-relatorio.md).

**O bloco 19 achou um `BLOQUEIA` de conteúdo por acaso; o bloco 20 procurou de propósito e achou
três** — e **dois na mesma cadeia**. A busca certa não é por paráfrase: **é por entidade que
sumiu**. E a mais perigosa é a **cláusula que exclui um sujeito**, porque a ausência dela faz a
regra parecer aplicável a todo mundo: a cadeia trabalhista do CJF alcança **só contratos
celetistas anteriores à Constituição** e **exclui servidores estatutários por escrito**. O termo
inicial dos juros ali é a **notificação inicial**, não o ajuizamento — **um mês sobre todo o
principal**, com R1, R2 e R3 passando nos dois cenários.

> **E o `englobante` tinha um irmão.** `aplicacao` era teste de *truthiness*: **qualquer prosa
> desligava R3**. Fechar o domínio revelou que o conserto também erra — fechá-lo em dois tokens
> quando o corpus declara **quatro** fórmulas faz o critério ser **a grafia, não o conteúdo**.

| Bloco | Conteúdo | Relatório |
|---|---|---|
| 1 | Tabelas do Manual TRT-3, p. 373–471 | `docs/calculo/extracao/trabalhista/bloco-01-tabelas.md` |
| 2 | Critérios e estrutura do cálculo, p. 9–17 | `docs/calculo/extracao/trabalhista/bloco-02-relatorio.md` |
| 3 | Verbas trabalhistas, itens 6.1 a 6.6, p. 18–55 | `docs/calculo/extracao/trabalhista/bloco-03-relatorio.md` |
| 4 | Verbas trabalhistas, itens 6.7 a 6.15, p. 55–82 | `docs/calculo/extracao/trabalhista/bloco-04-relatorio.md` |
| 5 | Parâmetros negociáveis e camada de norma coletiva | `docs/calculo/extracao/bloco-05-relatorio.md` |
| 6 | Presets de regime temporal | `docs/calculo/extracao/bloco-06-relatorio.md` |
| 7 | Descontos previdenciário e fiscal, cap. 9, p. 107–208 | `docs/calculo/extracao/bloco-07-relatorio.md` |
| 8 | Manual de Cálculos da Justiça Federal, CJF Res. 990/2026, integral | `docs/calculo/extracao/justica-federal/bloco-08-relatorio.md` |
| 9 | Cadeias históricas de atualização trabalhista — TRT-3, cap. 7, p. 83–99, extração dirigida | `docs/calculo/extracao/trabalhista/bloco-09-relatorio.md` |
| 10 | Fechamento trabalhista — cap. 7 residual, 11, 13, 15 e 17 | `docs/calculo/extracao/trabalhista/bloco-10-relatorio.md` |
| 11A | Capítulo 10 — varredura estrutural e item 10.1 (atualização sem amortização) | `docs/calculo/extracao/trabalhista/bloco-11a-relatorio.md` |
| 11B | Capítulo 10, segmento C — amortização de valor pago (art. 12-A) | `docs/calculo/extracao/trabalhista/bloco-11b-relatorio.md` |
| 11C | Capítulo 10, segmento D — vincendos e art. 12-B; **fecha a amortização** | `docs/calculo/extracao/trabalhista/bloco-11c-relatorio.md` |
| 12 | Consolidação da base de conhecimento — presets, invariantes, armadilhas | `docs/calculo/extracao/bloco-12-relatorio.md` |
| 13 | **Fechamento da extração** — cap. 10 seg. B, caps. 8, 12, 14 e varredura do 16 | `docs/calculo/extracao/bloco-13-relatorio.md` |
| 14 | **Fase 3 — confronto normativo.** 50 vereditos, 19 suspeitas sobre a base | `docs/calculo/extracao/bloco-14-relatorio.md` |
| 15 | **Fase 4 — consolidação.** Onze arquivos em espinha e detalhe; os 33 casos difíceis como aceite | `docs/calculo/extracao/bloco-15-relatorio.md` |
| 16 | **Fase 5 — build das skills.** Quatro skills, `references/` nacional × regional, R24 | `docs/calculo/extracao/bloco-16-relatorio.md` |
| 17 | **Correções estruturais.** Campo `tipo` e R3 no validador; ids neutros; ordem de cálculo | `docs/calculo/extracao/bloco-17-relatorio.md` |
| 18 | **Lacunas de consolidação.** FGTS e poupança; manifesto de cadeias; teste de ponteiros | `docs/calculo/extracao/bloco-18-relatorio.md` |
| 19 | **Classificação de índices.** Terceira classe de R3; 36 rótulos mapeados; 5 cadeias novas | `docs/calculo/extracao/bloco-19-relatorio.md` |
| 20 | **Espinha contra o extraído.** Quatro `BLOQUEIA` de conteúdo; `00-numeros.md` gerado | `docs/calculo/extracao/bloco-20-relatorio.md` |

O **Manual de Cálculos da Justiça Federal (CJF, Res. 990/2026) está integralmente extraído** —
**80 páginas de capítulo** mais a Apresentação e a Resolução, sete cadeias temporais em
`tabelas-normativas/`, e é a única fonte do corpus cuja edição está vigente. *(A descrição
"93 páginas integrais", usada até o bloco 12, superestimava: 13 das 93 são pré-textuais, e as
3 com conteúdo normativo estão cobertas. Corrigido no bloco 13.)*

O **bloco 9** acrescenta quatro cadeias históricas trabalhistas (`trab.hist.*`) e corrige o
validador de cobertura: a exaustividade dos ramos condicionados passou a ser **declarada**
(`dominio_condicoes`), não presumida. A primeira versão do conserto escondia lacuna real —
ver `bloco-09-relatorio.md` § 2.

**O artefato que abre a Fase 3 é [`docs/calculo/extracao/mapa-de-cobertura.md`](docs/calculo/extracao/mapa-de-cobertura.md)** —
todo capítulo e item dos dois manuais, com o bloco que o cobriu ou a razão de não ter sido
coberto. **O bloco 13 fechou a extração: os dois PDFs têm destino registrado em todas as 564
páginas.**

| Manual | Páginas | Cobertas | Pré-textuais com decisão | Sem decisão |
|---|---|---|---|---|
| TRT-3 (2016) | 471 | **463** | 8 | **0** |
| CJF (Res. 990/2026) | 93 | **83** | 10 | **0** |
| **total** | **564** | **546** | **18** | **0** |

O **bloco 12** consolidou o que estava espalhado pelos relatórios:
[`armadilhas-comparador.md`](docs/calculo/armadilhas-comparador.md) reúne os **defeitos do
manual que um perito reproduz** — **quinze** armadilhas com página, valor impresso, valor
correto e assinatura detectável, mais os deltas de método e os comportamentos que **não** são
defeito
(precisão plena, ausência de regra de arredondamento, mês comercial inclusivo). O limiar de
alarme do comparador não deve ser o centavo.

O **capítulo 10** foi extraído pela série 11A–11C e 13A, dividido **por operação** — as 69
páginas estão cobertas. O **bloco 11B** respondeu a invariante **R10**:

> A imputação de pagamento parcial no trabalhista é **proporcional** — o pagamento abate
> principal e juros na razão em que compõem o bruto (item 10.3.1, letra F, p. 237). **E não
> tem fundamento normativo declarado:** `art. 354` não ocorre em nenhuma das 471 páginas,
> enquanto `proporcional` ocorre 101 vezes só no segmento. R10 fica fundamentada por razão
> mais forte que a suposta — não são duas normas concorrentes, mas **uma norma (art. 354 do
> CC) contra um costume de liquidação sem base declarada**.

Por isso a escolha entra como preset **`pr.imputacao`, sem default** — quinto caso de
`R20-EXCECAO`, e o único em que o problema não é o corpus deixar a questão aberta, mas a
prática não ter norma. **Direção do delta:** juros primeiro produz dívida maior; o critério
proporcional favorece o **devedor**, o art. 354 favorece o **credor**.

A escolha da ordem de imputação move o saldo em até **23,83%** (juros primeiro: +10,58%;
principal primeiro: −13,25%) — **a decisão mais cara já medida no corpus**. O bloco 11C
derivou a forma fechada da amplitude, verificada em três casos:
`min(abatimento, principal, juros) × índice_residual × percentual_juros_residual`.

O **11C** fecha a amortização e acrescenta dois achados de mesma natureza que o de R10: a
hipótese que a moldura declara **obrigatória** (critério alternativo da letra C, sob juros
vincendos) **atravessa o capítulo sem um único exemplo que demonstre sua necessidade** — e nos
dois exemplos que deveriam exercitá-la os dois critérios dão o mesmo número. E o fundamento do
"descarregar" (**R23**, anti-anatocismo) **não está no capítulo que executa a operação**, mas
numa minuta de petição do capítulo 16 (p. 328).

O **bloco 10** fecha a extração trabalhista com o índice de jurisprudência
([`docs/calculo/jurisprudencia-indice.md`](docs/calculo/jurisprudencia-indice.md), 158 verbetes,
dos quais **a base normativa cobre 12**) e 17 regras estruturais que só existiam dentro dos
exemplos do capítulo 11.

**Achado estrutural do bloco 9:** o capítulo 7 do TRT-3 **não traz cadeia período → indexador**.
Ele delega o encadeamento histórico à Tabela Única do CSJT. A cadeia trabalhista anterior a
março de 1991 continua sendo pendência do corpus (**P9-02**).

Do Manual TRT-3, o **capítulo 6 está integralmente extraído**, e agora também o **capítulo 9**
(descontos previdenciário e fiscal, p. 107–208) — o maior do manual, 102 páginas e 47 itens.
Nenhuma skill escrita.

O **bloco 6** acrescentou a camada que decide *qual regra* vale em cada competência,
distinta da que decide *quanto vale* cada parâmetro: 26 regimes e **catorze eixos de
corte distintos** — e apenas dois deles são de competência ou fato. Cinco regimes
ficaram inaplicáveis porque o corpus dá a data de corte sem dizer qual data governa.
Ver `docs/calculo/presets-regime.md` e `docs/calculo/pendencias.md` § 19.

O bloco 5 está **completo em cobertura e provisório em classificação**: os 32 parâmetros
negociáveis estão consolidados e a fixture do ACT Gasmig é real, mas **27 dos 30 incisos do
art. 611-B da CLT não estão no corpus**, o que deixa 16 parâmetros com
`classificacao_provisoria: true`. Ver `docs/calculo/extracao/bloco-05-relatorio.md` §§ 1-A e 7,
e `docs/calculo/pendencias.md` § 15.
