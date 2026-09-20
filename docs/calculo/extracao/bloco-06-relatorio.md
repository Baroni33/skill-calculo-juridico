# Bloco 6 — relatório

Camada de presets de regime temporal. **Não é extração de PDF**: é varredura do
que já está no repositório, mais modelagem.

Fecha a pendência de modelagem que o bloco 5 abriu: os presets
`TRAB-INTERTEMP-TEMPUS` e `TRAB-INTERTEMP-ULTRATIVO` estavam nomeados em
`02-base-normativa-verbas.md` § 1 **sem camada onde morar**.

Nenhuma skill escrita.

| Tarefa | Situação |
|---|---|
| 1 — Inventário de regimes | **Feita** — 26 regimes, 14 eixos |
| 2 — Schema | **Feito** — `camada-regime-temporal-schema.json` |
| 3 — Invariantes R19 a R22 | **Feitas**, mais uma exceção que o corpus impôs |
| 4 — Validador e fixtures | **Feitos** — 76 testes do bloco, 199 no repositório |

---

## 1. O achado central: o eixo de corte não é único

O enunciado já avisava — *"a OJ 394 corta pela data da hora extra trabalhada; a
prescrição intercorrente, pela data da determinação judicial. Modelar como se
fosse um só eixo é erro."* A varredura mostrou que o problema é **maior** do que
dois eixos.

**Catorze eixos declarados no corpus. Dois deles são de competência ou fato.**

| Eixo | Regimes | Onde |
|---|---:|---|
| `competencia-do-fato` | 5 | OJ 394/Tema 9 · divisor CF/88 · INSS sobre aviso · PNS · conversão URV |
| `conteudo-do-titulo` | 2 próprios + 3 alternativos | JAM · limite de 05/10/88 · e como eixo alternativo em três outros |
| `data-de-admissao` | 1 | eletricitários pré-Lei 12.740/2012 |
| `data-da-sentenca` | 1 | multa do art. 467 |
| `data-da-dispensa` | 1 | seguro-desemprego |
| `inicio-do-aviso` | 1 | aviso proporcional |
| `ciencia-da-lesao` | 1 | prescrição do FGTS |
| `determinacao-judicial-na-execucao` | 1 | prescrição intercorrente |
| `fato-gerador` | 1 | GILRAT |
| `data-do-calculo` | 1 | faixas de INSS em jan/2010 |
| `efetivo-pagamento` | 0 primários | a **aritmética** da conversão URV — outra pergunta |
| `estado-processual` | componente | modulação do IRR-849 |
| `decisao-de-merito-no-processo` | componente | modulação do IRR-849 |
| `data-base-da-categoria` | componente | planos econômicos |

### A conclusão que muda a modelagem

**Dos catorze eixos, apenas dois são de competência ou fato.** Os outros doze são
processuais, documentais ou contratuais.

E, contado pela mesma régua dos dois lados — primários, componentes e alternativos
—, o **conteúdo do título comparece tanto quanto a competência**. A precedência R8
não é exceção rara no corpus. Três regimes declaram a
competência como eixo principal *e* o título como eixo alternativo, sempre com a
mesma fórmula: *"salvo se nos autos constar entendimento contrário"*, *"o termo
prescricional vai estar definido pelo comando exequendo"*.

> A primeira redação deste relatório dizia que o título era **o eixo mais
> frequente**. Era efeito de contar o título de um jeito — primários mais
> alternativos mais componentes — e a competência de outro, só primários. Contados
> igualmente, empatam. A validação adversarial pegou, e a afirmação forte saiu.

Dois regimes negam eixos rivais **nominalmente**, e isso é raro o bastante para
merecer registro:

- OJ 394 / Tema 9 — *"pela data do trabalho, **não** pela data do ajuizamento nem
  do julgamento"*;
- GILRAT — *"é o **fato gerador** que manda, **não** a data do cálculo nem a do
  ajuizamento"*.

Um regime usa um eixo que nenhum outro usa e que contraria a intuição inteira:
`pr.faixas-inss-jan2010` depende da **data em que o cálculo foi feito**. Em janeiro
de 2010 o manual traz **duas portarias simultaneamente vigentes** para a mesma
competência. É o caso que prova, sozinho, que o eixo não pode ser único.

---

## 2. O meta-regime, e a exceção que o corpus impôs

`pr.intertemporal` é o único cujo **eixo é o próprio objeto da escolha**. Escolher
a corrente não é escolher um valor: é escolher **qual data o motor lê** em todos os
regimes que dele herdam.

| Preset | Eixo efetivo |
|---|---|
| `TRAB-INTERTEMP-TEMPUS` | `competencia-do-fato` |
| `TRAB-INTERTEMP-ULTRATIVO` | `data-de-admissao` |

### R20-EXCECAO — uma invariante que o enunciado não pediu

A R20 diz: *regime sem escolha explícita usa o default e marca a conta*. Mas o
corpus manda literalmente **"Não resolver — expor como preset"**. Dar um default a
`pr.intertemporal` seria arbitrar a divergência que a base proíbe arbitrar.

Então: `sem_default: true`, e **sem escolha explícita o regime não calcula**. O
bloqueio se propaga aos três regimes que dele herdam.

Isso não é rigor decorativo. É a diferença entre um cálculo que diz *"falta uma
decisão jurídica"* e um que devolve um número plausível construído sobre um
palpite. Vale para quatro regimes: este, o Tema 1046, o adicional de HE pré-CF/88
(onde o corpus nem resolve a disjunção 20% × 25%) e a Súmula 17.

### A interação, modelada explicitamente

O enunciado pediu: *"sob a corrente ultrativa, regimes posteriores à admissão podem
nunca ser consultados. Modele essa dependência explicitamente."*

Mesmo contrato — admissão 02/03/2015 —, mesma competência — 2024-05:

| corrente | eixo efetivo | variante do intrajornada | efeito |
|---|---|---|---|
| `tempus regit actum` | competência | redação da Reforma | período suprimido · indenizatória · sem reflexos |
| `ultratividade` | admissão | redação anterior | integral · salarial · com reflexos |

Sob ultratividade a regra nova **nunca é consultada para esse contrato**, em
nenhuma competência. Testado em 2016, 2019, 2024 e 2026.

E o mecanismo vai além de devolver a variante antiga: quando o regime **suprime a
verba** — horas *in itinere* a partir de 11/11/2017 —, `parametro_consultavel()`
devolve `False` com o motivo, e `pn.in-itinere.prefixacao` **não chega a ser
consultado**. Consultar e descartar deixaria, na memória de cálculo, rastro de uma
consulta que não houve.

---

## 3. A granularidade, que não estava no enunciado

O corpus dá cortes ao **dia**: 11/11/2017, 20/03/2023, 05/09/2001, 13/11/2014. O
motor indexa por **competência mensal**.

**Novembro de 2017 fica dos dois lados do corte.**

O resolvedor recusa: `calculavel: false`, motivo `competencia-atravessa-o-corte`,
com o aviso de que falta precisão de dia. Com a data ao dia, resolve — 19/03/2023
sem repercussão, 20/03/2023 com.

Qualquer convenção plausível — o mês inteiro entra, o mês inteiro sai, metade
proporcional — inventaria meio mês de cálculo sem deixar rastro. A recusa é
visível; a convenção, não.

O ponto não é daquele corte específico. `bloco-01-tabelas.md` já registrava o mesmo
fenômeno nas tabelas de jun/99, jun/00 e jun/11, cujos rótulos do original são
"precisos ao dia" enquanto a checagem trabalha em competência mensal. Era
granularidade, e não foi resolvido lá; aqui virou mecanismo.

---

## 4. Duas naturezas de regime

A varredura mostrou que "preset" cobre duas coisas diferentes, e tratá-las igual
seria erro:

| | `cadeia-temporal` | `divergencia-interpretativa` |
|---|---|---|
| Quem decide | **a data** | **o usuário** |
| Pode escolher o contrário? | **Não** | Sim, com justificativa |
| Origem registrada | `determinada-pela-data` | `escolha-do-usuario` ou `default` |
| Exemplo | OJ 394 / Tema 9 | corrente intertemporal; índice JAM |

Ninguém escolhe aplicar a OJ 394 a uma hora extra de 2024 — a tese modulou pela
data, e ponto. Já a corrente intertemporal é escolha jurídica pura. Marcar as duas
como "preset do usuário" daria ao operador um botão que ele não tem o direito de
apertar.

---

## 5. O validador

`scripts/calculo/valida_regimes.py` e `test_valida_regimes.py`.

```
Ran 199 tests in 0.236s
OK
```

199 é a suíte inteira — 123 dos blocos anteriores mais **76 deste bloco**. Nenhum
skip.

### Os cinco cenários pedidos

| Cenário | Situação |
|---|---|
| Contrato atravessando 11/11/2017 nas duas correntes | ✓ — 5 testes, mais os casos c1–c6 da fixture |
| HE antes e depois de 20/03/2023, com e sem reflexo do RSR | ✓ — 8 testes |
| Intrajornada nas duas redações, aferindo extensão **e** natureza | ✓ — 5 testes, um por dimensão |
| Contrato de 2015 sob ultratividade nunca consulta a regra nova | ✓ — 4 testes, quatro competências |
| Eixos distintos resolvendo a mesma competência | ✓ — 6 testes; a fixture c10 tem quatro eixos e quatro datas |

Mais 48 testes de catálogo, granularidade de datas, origem do eixo, invariantes
R19–R22, separação entre as camadas e higiene aritmética.

### Dois bugs que os testes pegaram, e onze que a validação adversarial pegou

**Variante com condição em prosa e sem vigência.** Seis variantes de três regimes
— eletricitários, prescrição do FGTS, prescrição intercorrente — descreviam a
condição em texto (`"admissao < corte"`) sem cadastrar a janela de vigência. O
resolvedor não achava variante e **caía no default em silêncio**. Corrigido nos
dados, e o validador ganhou a regra: *eixo de data exige vigência, não só condição*.
É exatamente a classe de erro que a camada existe para impedir, e ela apareceu
dentro da própria camada.

**Contagem de datas distintas.** O teste do cenário 5 afirma quatro datas
diferentes numa competência. Passava com três, porque um dos quatro regimes
falhava — a asserção de contagem é o que revelou.

### O que a validação adversarial derrubou

Foi o achado mais útil do bloco, e foi contra mim.

**Uma data inventada.** `pr.periculosidade-eletricitarios` cortava em `2012-12-08`.
O corpus diz apenas *"eletricitários contratados antes da Lei 12.740/2012"* — sem
dia, sem mês. A data é historicamente a da publicação da lei e **ainda assim é
invenção**, porque não está em arquivo nenhum do repositório. O corte passou a
`2012`, com janelas `até 2011` e `a partir de 2013`: **admissão ocorrida em 2012
não resolve.** A fronteira ficou grossa porque o corpus a deixou grossa.

**Quatro eixos apresentados como declarados quando eram inferência.** O piso
nacional de salários, o regime do seguro-desemprego, a conversão URV e o limite de
05/10/88. Em todos, o corpus sustenta o eixo para uma pergunta **vizinha** — qual
piso vigia, em que tabela enquadrar, por quanto se converte — e **não** declara a
regra de seleção da variante. No caso da URV o erro era mais fino: as citações
declaram a **aritmética** da conversão, não qual regime monetário vale.

Isso obrigou a uma mudança de modelagem, não só de dados. O booleano
`eixo_declarado` forçava a escolher entre mentir e bloquear. Virou `eixo_origem`
com quatro estados — `declarado` (13), `inferido` (5), `herdado` (3),
`nao-declarado` (5). O inferido **resolve**; o que muda é o rastro: a resolução
marca `eixo_inferido: true` e carrega a justificativa.

**Seis números e citações.** A R20-EXCECAO nomeava três regimes quando são quatro;
"quinze pontos do corpus" não era enumerável nem derivável e saiu; as dezesseis
marcas F não são "todas" da Lei 13.467/2017 — a F6 do bloco 03 é da Lei
13.419/2017; a ressalva das marcas F estava citada entre aspas como se fosse uma
frase só, e são duas diferentes; os planos econômicos tinham "treze regimes
sucessivos", número que não vem de lugar nenhum — o corpus conta "dez normas" numa
pendência e tem dezesseis linhas na tabela, e **nenhum** número foi adotado; mais
oito imprecisões de citação.

**Um teste frouxo.** `test_o_eixo_dominante_nao_e_a_competencia` usava
`assertGreaterEqual` e contava os dois lados com réguas diferentes — "provava" a
dominância por construção. Foi reescrito com régua simétrica e afirma o que a
contagem sustenta.

**O que resistiu:** as demais doze datas de corte, conferidas uma a uma no corpus;
todos os números estruturais; e as quatro afirmações negativas — inclusive a do § 7.

### A fixture

`tests/fixtures/calculo/regimes-casos.json`, **declaradamente sintética**. Doze
casos, três perfis de contrato. Os **fundamentos e as datas de corte são reais**, do
corpus; os fatos do caso, não.

O caso que mais importa é o **c10**: competência 2015-06, quatro regimes, quatro
eixos, quatro datas — dispensa em 01/2015, sentença em 06/2001, aviso iniciado em
09/2011, ciência da lesão em 13/11/2014. Quatro respostas diferentes, e o teste
afirma que as quatro datas aplicadas são distintas. **Com um eixo só, seriam quatro
respostas erradas de uma vez.**

---

## 6. Dúvidas — candidatos que não viraram regime

A regra do bloco: ponto que sugere concorrência mas não a sustenta vai para o
relatório como dúvida.

| # | Candidato | O que falta |
|---|---|---|
| **D1** | **OJ 16 das Turmas do TRT-3** (07/10/2009), cancelada por contrariar a OJ 394 em 09/06/2010 | Sugere uma cadeia de **três** trechos onde `pr.oj394-reflexo-rsr` tem dois: cascata até 09/06/2010, sem cascata até 19/03/2023, cascata de novo. O corpus não declara se o primeiro trecho é regime aplicável ou história regional |
| **D2** | **Memo. Circular 10/2011 × Nota Técnica 184/2012** sobre o acréscimo do aviso proporcional | Duas leituras administrativas sucessivas. Falta a data de eficácia da NT e o eixo: avisos iniciados entre out/2011 e 2012 seguem qual? |
| **D3** | **Súmula 146 e a OJ 93 da SDI-1** (30/05/97) sobre o dobro do feriado | Falta declarar se a redação antiga governa competências anteriores, ou se a súmula atual retroage |
| **D4** | **Rol de feriados** — Lei 10.607/2002, Lei 9.093/1994, Lei 6.802/80 | O rol é dado como vigente; o corpus não diz o que vale antes de 19/12/2002 nem como se apura o rol municipal por competência. Carnaval: "não há consenso jurisprudencial" |
| **D5** | **Lei 8.923, de 27/07/1994**, que acrescentou o § 4º do art. 71 | Terceiro regime do intrajornada: antes dela não havia consequência pecuniária. O corpus não o enuncia como regime. Registrado dentro de `pr.intrajornada-71-4`, campo `lacuna_anterior` |
| **D6** | **Três redações da Súmula 362** (Res. 90/1999, 121/2003, 198/2015) | O manual reproduz as duas anteriores "para liquidação de processos antigos", sem dizer por qual eixo se escolhe entre elas |
| **D7** | **Tema Repetitivo 17** (cumulação de adicionais) | O corpus trata como regra única e vinculante, **sem modulação declarada**. Só haveria concorrência se houvesse período anterior com jurisprudência permissiva — e o corpus não afirma isso |

Nenhuma virou regime. Todas estão aqui.

### Dois pontos fora do recorte, com ponteiro

- **Contribuição sindical antes e depois da Reforma.** Está no **capítulo 12** do
  manual (p. 299–302), fora dos blocos 1–4. `00-base-normativa.md` registra que o
  manual "não serve como fonte normativa" para esse capítulo. É regime real e não
  foi modelado porque o corpus extraído não o alcança.
- **Modulação da ADC 58** — ressalva dos valores pagos e vedação de dedução. É
  capítulo 7 (atualização e juros), e `bloco-02-criterios.md` registra que "a
  interação não está no manual".

---

## 7. A lacuna estrutural: prescrição quinquenal e bienal

**Não há regra geral de prescrição trabalhista em lugar nenhum do corpus varrido.**

O art. 7º, XXIX, da CF aparece obliquamente — a OJ 415 e o "período imprescrito" do
contrato, a Súmula 206, a Súmula 362 do FGTS, a ressalva de que a indenização da
Súmula 291 não é abrangida, a OJ 83 sobre a contagem a partir do fim do aviso.
Nenhum eixo de **ajuizamento** é declarado em ponto algum.

É a lacuna mais desconfortável do bloco: **o eixo mais usado na prática trabalhista
— a data do ajuizamento, que fixa o marco quinquenal — é justamente o que o corpus
não tem.** Não foi suposto. Está aqui.

---

## 8. Pendências

### Abertas por este bloco

| # | Pendência | Efeito |
|---|---|---|
| **E1** | **Eixo não declarado** em 15 pontos do corpus e 16 marcas de Fase 4 | Cinco regimes inaplicáveis; todo o corte de 11/11/2017 parado em `pr.intertemporal` |
| **E2** | **Tema 1046** — se cláusula anterior a 02/06/2022 se julga por ele ou pelos Temas 357/762 | `afeta_parametros: ["TODOS"]`. Governa a resolução dos 32 parâmetros negociáveis inteiros |
| **E3** | **Prescrição quinquenal/bienal** ausente do corpus — § 7 acima | O eixo mais usado na prática não existe no catálogo |
| **E4** | Alcance temporal da cassação da Súmula 228 | Decide se `salario-basico` volta **como variante de regime** — ver § 9 |
| **E5** | Séries dos planos econômicos (IPC, URP, IRSM, FAS, FAZ, IPC-r, FRS) | `pr.planos-economicos` está `bloqueado`: regime sem série |
| **E6** | Disjunção 20% × 25% do adicional de HE pré-CF/88, e se o cancelamento da Súmula 215 em 1994 retroage | Duas lacunas empilhadas no mesmo regime |
| **E7** | Contribuição sindical — capítulo 12, fora do recorte extraído | Regime real não modelado |
| **E8** | Critério de arredondamento da conversão URV (pendência P2 do bloco 02) | `pr.urv-conversao` resolve o regime, não a aritmética |

### Fechada

| # | Pendência | Como fechou |
|---|---|---|
| **M1** do bloco 5 | "Camada de presets de cálculo não existe — os dois presets de direito intertemporal não têm onde morar" | Esta camada. `TRAB-INTERTEMP-TEMPUS` e `-ULTRATIVO` são variantes de `pr.intertemporal`, com eixo efetivo declarado |

---

## 9. Um cuidado que o bloco 5 deixou

O bloco 5 **removeu** a variante `salario-basico` de `pn.insalubridade.base`, porque
a Súmula 228 foi cassada definitivamente pela Rcl 6.275, em abril de 2018. Removê-la do catálogo de
**parâmetros** foi correto: não é mais opção negociável.

Mas se a cassação **não retroage**, competências anteriores a abril/2018 podem
seguir o salário básico — e aí ela precisa voltar **como variante de regime**, não
de parâmetro. Registrado em `pr.insalubridade-base-sumula228`, campo
`variante_removida.cuidado`, e é exatamente o que o eixo não declarado impede
decidir.

O mesmo raciocínio vale para o Piso Nacional de Salários (09/87–07/89), que **é**
uma variante de regime com eixo declarado e entrou como tal, e para o salário
profissional da Súmula 17, que seria a quarta e ficou sem eixo.

---

## 10. O que esta camada entrega, e o que não

**Entrega:** a resolução de qual regra vale numa competência, com o eixo correto
para cada regime, fundamento por variante, registro por competência, propagação da
escolha intertemporal aos regimes dependentes, e recusa explícita quando o corpus
não sustenta a resolução.

**Não entrega, por decisão:**

- **eixo suposto** — onde o corpus não declara, o regime é inaplicável;
- **default onde o corpus manda não resolver** — quatro regimes sem default;
- **escolha quando a competência atravessa o corte** — recusa com o motivo;
- **mérito** — a validade de uma cláusula, a nulidade de um ajuste, a ocorrência da
  prescrição. O motor aplica o regime e registra; a decisão é do juízo;
- **aritmética** — a camada diz qual regra vale, não calcula a verba.

Com as duas camadas — regime e parâmetro —, o motor sabe **qual regra** aplicar e
**quanto vale** cada constante dela. O que falta, agora, é a terceira: a que
efetivamente apura.
