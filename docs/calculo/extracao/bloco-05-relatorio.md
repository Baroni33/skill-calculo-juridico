# Bloco 5 — relatório

Inventário de parâmetros negociáveis e schema da camada de norma coletiva. **Não é extração
de PDF**: é varredura do que já está no repositório, mais modelagem.

Nenhuma skill escrita.

**Versão 2.** A v1 parou nas tarefas 2 e 4 porque `02-base-normativa-verbas.md` não
estava no repositório. O arquivo chegou e as duas foram executadas.

| Tarefa | Situação |
|---|---|
| 1 — Varredura dos blocos 02, 03 e 04 | **Feita** |
| 2 — Consolidação com a § 10 de `02-base-normativa-verbas.md` | **Feita** — 32 parâmetros |
| 3 — Schema da camada | **Feito** — schema v2.0 |
| 4 — Fixture do ACT Gasmig | **Feita** — real e parcial |
| 5 — `valida_parametros.py` + testes | **Feita** — 123 testes, **nenhum skip** |

---

## 1. O desbloqueio, e o que ele custou

A v1 deste relatório abria com um bloqueio: `docs/calculo/02-base-normativa-verbas.md`
não existia no repositório. Procurado em todo o projeto, em `Downloads/Plataforma-SaaS-Jus/`,
na raiz de `Downloads` e nos zips recentes. As tarefas 2 e 4 dependiam dele por inteiro.

**O arquivo chegou.** 206 linhas, lido integralmente. As tarefas 2 e 4 estão feitas e o
`skip` do caso 6 saiu da suíte.

O que a v1 fez em vez de parar continua valendo como método: tarefas 1, 3 e 5 foram feitas
por inteiro, e onde a dependência era real a lacuna ficou **visível e estruturada** — aviso
no topo do inventário, `completude.parcial: true` no catálogo, fixture com `status:
"bloqueada"` e `clausulas: []`, teste pulado com a razão impressa. Nada foi inventado, e a
fusão saiu mecânica quando o arquivo apareceu, exatamente como o roteiro previa.

### O que o arquivo trouxe além do esperado

| § | Conteúdo | Efeito aqui |
|---|---|---|
| **1** | **Direito intertemporal — duas correntes do TST e dois presets nomeados** | **Não virou parâmetro** (não é negociável) e abriu pendência de modelagem — ver abaixo |
| 5 | **A Súmula 228 foi cassada pela Rcl 6.275 em abril de 2018**, definitivamente | O catálogo dizia "suspensa". A variante `salario-basico` de `pn.insalubridade.base` **foi removida** |
| 4 | Duas alterações no intervalo intrajornada pela Lei 13.467/2017 | Confirma o achado do bloco 04, que estava marcado como a conferir |
| 6 | TST Tema Repetitivo 17 (IRR-239-55.2011.5.02.0319, 26/09/2019) — cumulação vedada | Fecha ponto aberto do bloco 04 |
| 8 | Súmula 124 revista em 26/06/2017, Res. 219/2017 — 180/220 | Sustenta `pn.jornada.sabado-como-rsr` |
| 9 | Regime de turno do ACT Gasmig, com a previsão expressa sobre 7ª e 8ª horas | Fecha a **pendência D1** e alimenta a fixture |
| 10 | A tabela de 13 parâmetros | A tarefa 2 |
| 12 | SITRAMICO/MG é o sindicato-base; SAEMG e Senge-MG negociam em paralelo | Partes da fixture; pendência de mapa de categorias |

### O achado que não coube no inventário: direito intertemporal

A § 1 traz a divergência sobre a aplicação da Lei 13.467/2017 aos contratos em curso, com
acórdãos do TST nos dois sentidos **dentro do mesmo tema**, e a instrução literal **"Não
resolver — expor como preset"**, com dois presets nomeados: `TRAB-INTERTEMP-TEMPUS` (corte em
11/11/2017, contrato dividido) e `TRAB-INTERTEMP-ULTRATIVO` (regra da admissão por todo o
contrato).

**Não entrou no catálogo dos 32, e a razão é de categoria, não de rigor.** Nenhum sindicato
negocia qual corrente de direito intertemporal se aplica — a escolha é do operador do
cálculo. A chave de resolução desta camada, `(parametro, categoria, competencia)`, não tem
onde encaixar um preset de cálculo. Enfiá-lo ali faria o catálogo misturar duas camadas.

O que falta é uma **camada de presets de cálculo**, irmã desta, com a mesma disciplina: as
duas correntes registradas como variantes, nenhuma arbitrada, proveniência na memória. É
pendência de **modelagem**, não de dado — não depende de documento algum chegar. E é grande:
a própria base diz que, com contratos anteriores a 11/11/2017 gerando passivo, **a escolha
move o resultado em praticamente todos os pontos daquela seção**.

Registrada em `pendencias.md` § 15.5. A primeira redação deste relatório simplesmente pulou
a § 1 na tabela acima — foi a validação adversarial que pegou.

### Duas divergências entre o enunciado e o documento

Registradas, não contornadas — ambas estão na própria fixture.

1. **"A seção 3 do arquivo traz os valores"** — a § 3 é *Horas in itinere* e não traz valor
   algum do ACT. Os **valores** estão nas **§§ 8, 9 e, principalmente, na coluna
   "Observação" da tabela da § 10**; as §§ 7 e 12 trazem contexto — base da periculosidade,
   sindicatos —, não valores de cláusula. Efeito prático nenhum: foram localizados e
   transcritos. Fica registrado para que ninguém procure na § 3.
2. **A cláusula 2.1.1**, que o enunciado do bloco 5 aponta como a que estende o ACT a
   categorias cujo sindicato não negociou, **não aparece** no documento. A categoria estendida
   ficou `null` — assim não alcança ninguém, que é o comportamento correto enquanto o dado
   falta.

E uma ausência: **"gratificação de sala de controle" não existe em nenhum lugar do
documento**. A § 12, pendência 3, fala genericamente em "IP 10.5 (PCCR) e demais Instruções
de Pessoal referenciadas no ACT — definem gratificações que integram base", sem nomeá-las.
Continua como dúvida — § 4.

---

## 1-A. A âncora do art. 611-B da CLT

A v1 deixou seis dúvidas abertas porque procurava a expressão "no mínimo" no texto de cada
artigo. **Não é assim que se decide.** A âncora é o art. 611-B da CLT, rol taxativo do que
não pode ser objeto de convenção ou acordo coletivo **na forma de supressão ou redução**.

> ### De onde vem este fundamento
>
> **Instrução direta do usuário deste bloco. Não do corpus.**
>
> O corpus tem uma linha: `02-base-normativa-verbas.md` § 2 *cita* o art. 611-B, sem
> transcrever inciso algum. O teor dos incisos VI, XVII e XVIII, o número de trinta incisos
> e a ressalva do inciso XVII abaixo foram todos **fornecidos**, não conferidos.
>
> Isso é legítimo — receber um fundamento e aplicá-lo não é inventá-lo. Mas quem auditar o
> catálogo contra os arquivos do repositório **não vai achar o art. 611-B**, e precisa saber
> por quê antes de concluir que houve invenção. Está declarado em
> `classificacao_611b.ORIGEM_DESTE_BLOCO`, e há teste prendendo a declaração.
>
> A primeira redação desta seção dizia "conferidos no texto". Era falso quanto à forma, e
> foi corrigido pela validação adversarial.

```
parâmetro alcançado por INCISO do art. 611-B   →  apenas-elevacao
parâmetro coberto pelo PARÁGRAFO ÚNICO          →  qualquer
demais                                          →  qualquer (Tema 1046/STF)
```

O parágrafo único é o que fecha o raciocínio: **duração do trabalho e intervalos não são
normas de saúde, higiene e segurança para este fim**. Jornada, compensação, banco de horas,
turno, sobreaviso e prontidão passam a ser negociáveis em qualquer direção.

### Mapeamento inciso → parâmetro

| Inciso | Matéria | Parâmetros | Classificação |
|---|---|---|---|
| **VI** | remuneração do trabalho noturno superior à do diurno | `pn.noturno.adicional`, `pn.he.adicional-noturna` | **apenas-elevacao** |
| **XVII** | normas de saúde, higiene e segurança | nenhum diretamente — ver ressalva | — |
| **XVIII** | adicional para atividades penosas, insalubres ou perigosas | `pn.insalubridade.base`, `pn.insalubridade.percentual`, `pn.periculosidade.base`, `pn.periculosidade.percentual` | **apenas-elevacao** |
| **¶ único** | duração do trabalho e intervalos | `pn.jornada.semanal`, `pn.jornada.divisor`ᵈ, `pn.jornada.sabado-como-rsr`, `pn.jornada.turno-ininterrupto`, `pn.turno.setima-e-oitava-horas`, `pn.he.regime-de-compensacao`, `pn.he.banco-de-horas`, `pn.bancario.enquadramento-224`, `pn.sobreaviso.fator`, `pn.prontidao.fator` | **qualquer** |

ᵈ o divisor é derivado; não se negocia nem para cima nem para baixo.

### LACUNA: 27 dos 30 incisos não foram lidos

**O texto integral do art. 611-B não está no corpus.** Verificado: aparece *citado* em
`02-base-normativa-verbas.md` § 2, e está ausente dos dois PDFs (busca direta no texto
extraído). O próprio número de trinta incisos veio por instrução. A regra do bloco — *não pesquise norma na web; se faltar fundamento, é pendência*
— impede a única outra saída.

Recitar trinta incisos de memória e apresentá-los como conferidos seria exatamente o tipo de
invenção que este inventário existe para evitar.

A lacuna não ficou como nota de rodapé. Virou mecanismo:

- campo `fundamento_611b` em cada parâmetro, com `"nao-mapeado"` onde nenhum inciso
  conferido alcança;
- campo `classificacao_provisoria`, que o validador **exige** ser `true` exatamente nesses
  casos e `false` nos demais — a inconsistência quebra;
- bloco `classificacao_611b.LACUNA` no topo do catálogo, dizendo quantos incisos faltam e
  por quê.

**16 dos 32 parâmetros estão com classificação provisória.** Quando os 27 incisos forem
lidos, o trabalho é reclassificá-los — e a lista de quais é gerada por
`Catalogo.provisorios()`.

### A ressalva do inciso XVII

Há decisão do TST aplicando o inciso XVII para invalidar cláusula sobre **jornada** quando a
extensão configura risco à saúde, **com ressalva expressa de que o parágrafo único não a
salva**. O corte não é absoluto.

Recebida por instrução, **sem órgão, processo nem data**, e não pesquisada. Hoje a marca
`ressalva_611b_xvii` sinaliza um risco cuja fonte não se pode citar numa memória de cálculo.
Obter a referência é pendência.

Isso é mérito, não cálculo. **O motor aplica a cláusula e registra; a nulidade é do juízo.**
Os parâmetros de duração do trabalho carregam `ressalva_611b_xvii: true` para que a memória
de cálculo sinalize o ponto, sem que a classificação mude. Há teste prendendo essa separação
— `test_ressalva_do_inciso_XVII_nao_muda_o_calculo` afirma que todo parâmetro com a ressalva
continua `qualquer`.

É o mesmo princípio que governa `pn.turno.setima-e-oitava-horas = normais` no ACT Gasmig, o
ponto de maior litígio do instrumento: o motor calcula como o ACT manda e registra a
divergência com o default legal.

---

## 2. Tarefa 1 — varredura

Percorri `bloco-02-criterios.md`, `bloco-03-verbas.md` e `bloco-04-verbas2.md` com dois
passes: um atrás das expressões de ressalva e de piso, outro atrás dos parâmetros numéricos
e estruturais que a primeira varredura não pega por vocabulário.

**Resultado: 17 parâmetros + 1 derivado + 6 dúvidas.** Inventário completo em
`docs/calculo/parametros-negociaveis.md`.

### Distribuição

| Bloco | Parâmetros |
|---|---|
| `bloco-02-criterios.md` | **0** |
| `bloco-03-verbas.md` | 9 |
| `bloco-04-verbas2.md` | 6 |
| `02a-adendo-lacunas-verbas.md`, § 18 | 3 (todos incorporados, sem duplicar) |

> **O bloco 02 não contribuiu com parâmetro algum, e isso é o esperado.** Ele trata de
> princípios de liquidação e aritmética, não de verbas. O que ele dá é a **moldura de
> precedência** — R8, título judicial sobre o manual — que a R16 desta camada estende para
> quatro níveis.

### Por tipo

| Tipo | Quantos | Exemplos |
|---|---|---|
| `substituicao-de-valor` | 10 | adicional de HE, adicional noturno, dias de RSR, valor da ajuda-alimentação |
| `chave-de-variante` | 6 | base da insalubridade, sábado como RSR, turno de revezamento, critério do feriado na 12×36 |
| `alteracao-de-composicao` | 1 | feriados no reflexo de HE sobre o RSR |

> **`alteracao-de-composicao` ficou com um só ocupante, e vale explicar por quê.** A maioria
> das mudanças de composição que o capítulo 6 admite vem de **lei** (a Reforma retirando
> prêmios e abonos do art. 457), não de negociação. O que a norma coletiva move, no corpus
> que tenho, é quase sempre **quanto** ou **qual regra**. Se a seção 10 do arquivo ausente
> trouxer mais casos de composição, é aí que vão entrar.

### Por regime de alteração

*Contagem da varredura da v1 — 20 parâmetros, antes da § 10 e antes do art. 611-B. O
inventário consolidado está em `parametros-negociaveis.md` § 8, e a classificação mudou:
sobreaviso, prontidão e vale-transporte entraram; periculosidade e insalubridade viraram
`apenas-elevacao` pelo inciso XVIII.*

- **`apenas-elevacao`** (9): têm piso legal e ativam a R18 — HE, HE do comissionista,
  noturno, transferência, insalubridade (base e percentual), dias de RSR, feriados no
  reflexo, aviso proporcional.
- **`qualquer`** (10): jornada semanal, compensação, sábado, turno, bancário art. 224,
  feriado 12×36, base da transferência, período e forma de correção da média de comissões,
  valor da ajuda-alimentação.

Um caso merece nota: **`pn.comissoes.periodo-da-media` foi classificado como `qualquer`, não
como `apenas-elevacao`**, embora o manual só fale em prazo *inferior*. Prazo menor **não é
necessariamente mais favorável** — depende de as comissões estarem subindo ou caindo no
período. Não há piso a defender.

---

## 3. Três achados da varredura

### 3.1 O divisor não é parâmetro, e tratá-lo como um seria erro

`pn.jornada.divisor` entrou como **derivado**, não como parâmetro próprio.

> IRR-849, tese 3: o divisor sai da regra geral do **art. 64 da CLT** — jornada normal × 30.
> Tese 6: havendo redução da duração semanal, vem da **Súmula 431** —
> `30 × (horas semanais ÷ dias úteis)`.

Uma CCT que reduza a jornada para 40h move o divisor para 200 **por consequência, não por
cláusula**. Se o motor aceitasse divisor avulso, aceitaria o par (jornada 44h, divisor 200) —
inconsistente e indetectável.

A exceção é o **210** da 12×36, que vem da OJ 23 das Turmas do TRT-3 e é atribuído ao regime,
não derivado da fórmula. Está registrado no catálogo.

### 3.2 Um parâmetro sem default legal quebra o padrão da R14

`pn.ajuda-alimentacao.valor` **não tem default legal**. É parcela exclusivamente
convencional — o manual identifica a origem na própria planilha, cuja coluna é rotulada
"Vr. Unitário ajuda alimentação, **conforme CCT**".

R14 diz que ausência de norma coletiva é *fallback* para o default. **Aqui não há para onde
cair.** Sem instrumento, a verba é **incalculável**, não calculável-com-marcação.

O schema trata com `sem_default: true` e a cobertura `sem-default-legal`. Continua não sendo
erro — é dado faltante, e a conta prossegue nas demais verbas. Mas é um terceiro estado, e o
motor precisa distingui-lo dos outros dois. Testado.

### 3.3 Ampliar o RSR é possível; fazê-lo não move o divisor

Duas teses do mesmo acórdão, e é fácil confundi-las:

| Tese | Conteúdo |
|---|---|
| **1** (unânime) | "O número de dias de repouso semanal remunerado **pode ser ampliado** por convenção ou acordo coletivo, como decorrência do exercício da **autonomia sindical**" |
| **4** | "A inclusão do sábado como RSR **não altera o divisor**, por não haver redução do número de horas semanais, trabalhadas e de repouso" |

São **duas consequências separadas do mesmo fato negocial**. Ampliar o RSR muda o numerador
do reflexo (`valor × nº_RSR / dias_úteis`), que alcança quatro verbas. Não muda o divisor do
salário-hora.

Por isso `pn.rsr.dias` e `pn.jornada.sabado-como-rsr` são parâmetros distintos, e o segundo
carrega as **duas correntes** — Súmula 124 (altera o divisor) × IRR-849 tese 4 (não altera) —
registradas, não arbitradas.

---

## 4. Os seis candidatos da v1 — cinco resolvidos, um aberto

A regra do bloco: o que não se classifica com segurança vira dúvida, não palpite. A v1
deixou seis. O art. 611-B resolveu cinco.

| Candidato da v1 | Resolução | Fundamento |
|---|---|---|
| Periculosidade 30% | **apenas-elevacao** | inciso XVIII |
| Base da periculosidade | **apenas-elevacao** | inciso XVIII |
| Sobreaviso 1/3 · Prontidão 2/3 | **qualquer** — viraram `pn.sobreaviso.fator` e `pn.prontidao.fator` | ¶ único, duração do trabalho |
| Dedução dos 6% do VT | **qualquer** — virou `pn.vale-transporte.deducao-6pct`, com `sustentacao_fraca: true` | Tema 1046 |
| Natureza da ajuda-alimentação | instância de `pn.composicao.natureza-de-verba`, da § 10 | Tema 1046 |
| Nº de passagens · 22 dias úteis | **continua fora** — são defaults probatórios, não cláusulas | — |
| Gratificação de sala de controle | **ABERTA** — a expressão não existe no documento | — |

As quatro primeiras linhas caem por um motivo só, e o motivo **não é a redação do artigo**:
é a vedação de reduzir. A ausência de "no mínimo" no texto é irrelevante — foi o erro de
método da v1.

A tabela abaixo preserva o raciocínio original, para registro do que foi corrigido.

| Candidato | Por que não entrou |
|---|---|
| **Adicional de periculosidade — 30%** | O manual escreve "**devido na base de 30%**". Não há "no mínimo" nem "nunca inferior". Pelo corpus, não consigo afirmar que é piso elevável — e a diferença importa para a R18 |
| **Sobreaviso 1/3 · Prontidão 2/3** | "à razão de 1/3 do salário normal" e "à razão de 2/3". Mesma razão: são proporções fixadas, não pisos declarados |
| **Dedução dos 6% do vale-transporte** | A divergência que o manual registra é sobre o **comando exequendo** — "observar se a dedução consta ou não" —, não sobre norma coletiva. É variante governada pelo título, não pela camada |
| **Natureza da ajuda-alimentação** (salarial × indenizatória) | O manual a faz depender de **reconhecimento judicial**: "quando tem a natureza salarial reconhecida judicialmente". Na prática a CCT costuma estipular, mas o corpus não diz isso |
| **Nº de passagens/dia · média de 22 dias úteis** | São *defaults probatórios* para quando faltam documentos, não parâmetros negociáveis |
| **Gratificação de sala de controle** (ACT Gasmig) | Citada na Tarefa 4. **Não tenho o documento.** Não sei se é parâmetro negociável ou verba autônoma — e a diferença muda onde ela vive no modelo |

Os quatro primeiros têm um padrão comum: **o corpus descreve o valor sem qualificá-lo como
piso**. Classificar como `apenas-elevacao` ativaria a R18 e faria o motor rejeitar cláusulas
que talvez sejam válidas. Classificar como `qualquer` permitiria reduções que talvez sejam
nulas. Nenhum dos dois erros é preferível, então nenhum foi cometido.

~~**Pendência D1**~~ — **FECHADA.** A v1 registrava que o corpus estabelecia o *efeito* do
enquadramento em turno ininterrupto (6ª diária, divisor 180) mas não continha a autorização
constitucional para elevação da jornada por negociação. `02-base-normativa-verbas.md` §§ 9 e
10 trazem o fundamento: **CF art. 7º, XIV, com a Súmula 423/TST e o Tema 1046**. (O corpus
diz "CF art. 7º, XIV"; a expressão "parte final" era acréscimo meu e saiu.)

---

> **Nota sobre a numeração das teses do IRR-849.** Duas numerações circulam no repositório:
> `bloco-03-verbas.md` enumera **seis** teses; `02-base-normativa-verbas.md` § 8 enumera
> **cinco** itens. Esta seção usa a de seis, por citar o bloco 03; o catálogo usa a de cinco,
> por citar a base normativa. Não existe "tese 6" na numeração de cinco. Conferir sempre
> contra a fonte citada na mesma frase.

---

## 5. Tarefa 3 — o schema

Dois arquivos em `docs/calculo/tabelas-normativas/`:

| Arquivo | Conteúdo |
|---|---|
| `camada-norma-coletiva-schema.json` | Contrato da camada: chave, retorno, forma do instrumento, algoritmo, invariantes |
| `camada-norma-coletiva-catalogo.json` | Os **32** parâmetros com default, piso, tipo, variantes, derivação, `fundamento_611b` e sustentação literal |

### A chave, e o que deliberadamente fica de fora dela

`(parametro, categoria, competencia)`.

**O que não entra**, e é a parte que a R17 exige:

- **processo** — norma coletiva não é atributo do processo;
- **empresa** — a mesma empresa tem empregados de categorias distintas;
- **data do cálculo** — manda a competência da parcela, não quando se calcula.

Consequência direta, testada: dois empregados da mesma empresa, no mesmo processo, podem
resolver o mesmo parâmetro de formas diferentes.

### As duas situações de abrangência que o enunciado mandou modelar

**Um empregado alcançado por instrumentos de sindicatos distintos.** O resolvedor devolve
**todos** os instrumentos aplicáveis. Havendo mais de um com cláusula para o mesmo parâmetro,
a cobertura é `conflito`, com a lista completa — e **nenhuma heurística**. Nem o mais
recente, nem o mais favorável, nem o mais específico. A escolha é decisão jurídica.

**Um instrumento que se estende a categorias cujo sindicato não negociou.** Campo
`categorias_por_extensao`, com a cláusula que promove a extensão. O retorno marca
`por_extensao: true`.

> A marcação não é enfeite: **a força vinculante de uma extensão é mais discutível que a de
> uma categoria signatária**, e quem lê a memória de cálculo precisa saber por qual das duas
> vias o instrumento chegou até aquele empregado. É a estrutura declarada para a cláusula
> 2.1.1 do ACT Gasmig.

### Uma distinção que o schema faz e que não estava no enunciado

**Conflito normativo × defeito de cadastro.**

- Dois **instrumentos** com cláusula aplicável à mesma tripla → `conflito`, reportado e não
  resolvido. É situação do mundo.
- Duas cláusulas do **mesmo instrumento** com vigência sobreposta → `ErroDeDados`, que
  quebra. Não é conflito normativo: é alguém que cadastrou errado, e silenciar esconderia o
  defeito.

Testado nos dois sentidos. Na v2 a distinção subiu para o schema como seção própria,
`conflito_versus_defeito_de_cadastro`, em vez de viver só no algoritmo.

> Tratar defeito de cadastro como conflito faria o motor devolver "conflito" para um
> instrumento mal digitado, e alguém passaria o dia procurando o segundo sindicato que não
> existe.

### Parâmetros derivados, generalizados

A v1 tratava o divisor como caso único. A v2 fez do tratamento uma regra: **todo parâmetro
que decorra de outro entra como derivado com a fórmula, nunca como valor cadastrável.**
`Catalogo.valida()` recusa `derivado_de` sem `derivacao.formula`.

O motivo é concreto: aceitar o derivado avulso permite cadastrar jornada de 44h **com**
divisor 200, e nenhuma validação posterior pega o par inconsistente.

Duas espécies:

| | `pn.jornada.divisor` | `pn.he.adicional-noturna` |
|---|---|---|
| fórmula | `(jornada_semanal ÷ dias_úteis) × 30` | `((1+not/100)×(1+extra/100) − 1)×100` |
| exemplo | 40h → **200** | 1,20 × 1,50 → **80** |
| `sobrescrevivel` | **false** — cláusula que o fixe é defeito de cadastro | **true** |

O `sobrescrevivel` não é hipótese de laboratório: **o ACT Gasmig fixa o adicional de HE
noturna diretamente sobre a hora diurna**, em vez de compor os dois (§ 10). É o único
parâmetro do catálogo com essa marca.

---

## 6. Tarefa 5 — validador

`scripts/calculo/valida_parametros.py` e `test_valida_parametros.py`.

```
Ran 123 tests in 0.108s
OK
```

123 é a suíte inteira do repositório — 52 dos blocos anteriores mais **71 deste bloco**.
**Nenhum skip.** A v1 tinha 101 testes e um `skip`, o caso 6.

### Os seis casos pedidos

| # | Caso | Situação |
|---|---|---|
| 1 | Resolução com instrumento vigente | ✓ — 8 testes, incluindo proveniência e extensão |
| 2 | Sem instrumento → fallback + marcação (R14) | ✓ — 4 testes, incluindo o caso sem default legal |
| 3 | Competência anterior ao instrumento mais antigo | ✓ — 5 testes, incluindo bordas inclusivas e série mês a mês |
| 4 | Valor abaixo do piso → rejeição (R18) | ✓ — 7 testes |
| 5 | Dois instrumentos → conflito reportado | ✓ — 5 testes |
| 6 | Cadeia temporal do ACT Gasmig | ✓ — mecanismo com fixture sintética, **valores com a fixture real** |

Mais 37 testes de catálogo, competência, precedência (R16), classificação 611-B, derivação,
fixtures e higiene aritmética. Somam 71 no arquivo do bloco 5 — 8+4+5+7+5+5 nos seis casos, mais 37.

### O que o caso 6 conseguiu afirmar, e o que não

Com os dados reais, cinco testes novos:

| teste | afirma |
|---|---|
| `test_act_gasmig_resolve_os_parametros_cadastrados` | as seis cláusulas resolvem, com proveniência |
| `test_act_gasmig_jornada_de_40h_implica_divisor_200` | o divisor **deriva** e não está cadastrado |
| `test_act_gasmig_setima_e_oitava_horas_e_o_ponto_de_litigio` | a cláusula é aplicada e a divergência com o default é registrada (R16) |
| `test_act_gasmig_he_noturna_e_derivado_sobrescrevivel` | a composição 1,20 × 1,50 = 80 |
| `test_act_gasmig_tres_faixas_de_he_declaradas_sem_datas` | **a lacuna**, e o preço dela |

A cadeia temporal com valores reais **não foi afirmada**, e o motivo está no último teste.
A § 10 dá os três percentuais do ACT — **80% / 75% / 60% "por período"** — e **não dá os
intervalos de competência**. Três cláusulas do mesmo parâmetro sem `vigencia_propria` se
sobrepõem, e sobreposição no mesmo instrumento é defeito de cadastro, que quebra. Inventar
as datas seria pior: elas determinam qual percentual rege cada competência, e a ordem no
documento é **descendente**, o que é incomum numa progressão temporal e reforça que a
leitura não pode ser suposta.

O preço foi medido em vez de escondido: enquanto faltarem, a categoria `gasmig-sitramico`
resolve o adicional de HE pelo **default legal de 50%**, contra os 60% a 80% reais. O teste
afirma esse 50% — para que o dia em que as datas chegarem, ele falhe e alguém o atualize.

### Duas decisões de comportamento que valem registro

**R18 rejeita, não corrige.** Cláusula de 40% com piso de 50% **não vira 50%**. A resolução
devolve o default, marca `cobertura: sem-cobertura-coletiva` e registra a rejeição. Corrigir
silenciosamente para o piso esconderia um defeito do instrumento cadastrado — ou um erro de
leitura do instrumento.

**O título judicial não é barrado pelo piso.** R16 põe o título acima de tudo; se um título
fixa adicional de 40%, o motor aplica 40% e registra a divergência. Aplicar a lei contra o
título é competência do juízo, não do motor. Testado explicitamente.

### A fixture real do ACT Gasmig

`tests/fixtures/calculo/instrumentos-act-gasmig.json` substitui a bloqueada. **Real e
parcial**: todos os valores vêm de `02-base-normativa-verbas.md`, nenhum foi inventado.

Seis cláusulas cadastradas — jornada 40h, HE em domingos e feriados 100%, enquadramento em
turno, 7ª e 8ª horas normais, partição de férias em 3, banco com quitação trimestral. Todas
com `clausula: "não informada"`, porque o documento não dá os números das cláusulas.

Três coisas **não** foram cadastradas, e cada uma diz por quê no próprio arquivo: as três
faixas de HE (faltam as datas), o percentual da HE noturna (falta o número), e a gratificação
de sala de controle (não existe no documento).

A `vigencia` tem as **duas pontas nulas**. O rótulo "2025/2027" sugere o biênio, mas o
mês-base não consta e não foi suposto. O arquivo registra que isso torna o instrumento
aplicável a qualquer competência consultada — **comportamento conservador, mas incorreto no
mundo**, e a ser corrigido assim que o mês-base for conhecido. Dizer isso é melhor que
escolher janeiro.

Pelo mesmo motivo `categorias_abrangidas: ["gasmig-sitramico"]` traz o campo companheiro
`categorias_fonte` com a frase **"RÓTULO DESTA EXTRAÇÃO, não do documento"**. Sem um
identificador a fixture não resolve nada; com um identificador inventado sem aviso, alguém
acreditaria nele.

### O que a fixture sintética exercita

`instrumentos-sinteticos.json`, **declaradamente sintética**, com quatro instrumentos
desenhados para cobrir os caminhos:

- **Alfa** — três faixas temporais do mesmo parâmetro, cobrindo a vigência inteira sem
  lacuna nem sobreposição (testado);
- **Beta** — extensão de categoria, espelhando a estrutura da cláusula 2.1.1;
- **Gama** — janela estreita de conflito com a Alfa, **só** em `alfa-producao`, para que
  `alfa-manutencao` fique livre e possa exercitar a cadeia temporal;
- **Delta** — duas cláusulas abaixo do piso legal, para a R18.

> A separação entre `alfa-producao` (com conflito) e `alfa-manutencao` (sem) foi uma correção
> de projeto: a primeira versão da fixture dava à Gama uma vigência larga, e a janela de
> conflito engoliu três testes que nada tinham a ver com conflito. O sintoma era útil —
> mostrou que o resolvedor prefere reportar conflito a escolher, que é o comportamento
> desejado.

---

## 7. Pendências

### Fechadas nesta versão

| # | Pendência | Como fechou |
|---|---|---|
| **B1** | § 10 de `02-base-normativa-verbas.md` não incorporada | 13 linhas → 15 parâmetros, consolidados sem duplicação |
| **B2** | Cláusulas do ACT Gasmig | Fixture real com seis cláusulas |
| **D1** | Autorização constitucional para elevar a jornada do turno | CF art. 7º, XIV + Súmula 423 + Tema 1046 (§§ 9 e 10) |
| **D2** | Seis candidatos não classificados | Cinco resolvidos pelo art. 611-B; um segue aberto |

### Abertas

| # | Pendência | Efeito |
|---|---|---|
| **L1** | **27 dos 30 incisos do art. 611-B** não estão no corpus | 16 parâmetros com `classificacao_provisoria: true` |
| **L2** | Intervalos de competência das três faixas de HE do ACT | O parâmetro de maior uso resolve 50% em vez de 60–80% |
| **L3** | Percentual da HE noturna do ACT | `derivacao.sobrescrevivel` não é exercitado com dado real |
| **L4** | Mês-base do ACT | Vigência nula — o instrumento vale para qualquer competência |
| **L5** | Identificador real de categoria | `gasmig-sitramico` é rótulo desta extração |
| **L6** | Cláusula 2.1.1 e a categoria estendida | R17 não é exercitada com dado real |
| **D2'** | Gratificação de sala de controle | Não existe no documento; classificação desconhecida |
| **D3** | Vigência da Súmula 46 do TRT-3 após 2018 (§ 19 do adendo) | Default de `pn.insalubridade.base` |
| **D4** | Mapa de categorias e série de ACTs (§ 19 do adendo; § 12 da base) | Alimentar a camada com dados reais |
| **L7** | Referência da decisão do TST sobre o inciso XVII — órgão, processo, data | A marca `ressalva_611b_xvii` não é citável numa memória de cálculo |
| **L8** | Percentuais de insalubridade por grau (leve 10 / máximo 40) | Removidos do catálogo por falta de lastro; só o grau médio (20%) está no corpus |
| **M1** | **Camada de presets de cálculo** não existe — os dois presets de direito intertemporal não têm onde morar | Nenhum ponto do motor sabe qual regra aplicar antes de 11/11/2017. Pendência de modelagem |
| **M2** | Camada de **descontos** não existe — a contribuição negocial do ACT (base: adicional de periculosidade) não tem parâmetro | Desconto do ACT não modelado |
| **B3** | Os **seis pontos que a § 11 da base declara não ter pesquisado** | `pendencias.md` § 17; o item 6 (OJ 394) é o de maior prioridade por declaração da própria base |
| **B4** | As **quatro pendências de dados da § 12** | `pendencias.md` § 18 |

**L1 é a maior.** Um documento — o texto do art. 611-B — reclassifica metade do inventário.

---

## 8. O que esta camada entrega, e o que não

**Entrega:** a resolução de um parâmetro para uma categoria numa competência, com
proveniência, precedência de quatro níveis, detecção de conflito sem arbitragem e rejeição
de cláusula abaixo do piso.

**Não entrega, por decisão:**

- escolher entre dois instrumentos conflitantes — é decisão jurídica;
- corrigir cláusula abaixo do piso — R18 manda rejeitar e reportar;
- inferir a categoria do empregado — vem do cadastro do contrato;
- séries de índices — manutenção separada, regra 4 de `01-plano-extracao.md`.

Com o inventário e a camada, o motor de verbas passa a ter onde buscar cada constante que os
blocos 03 e 04 registraram como se fosse fixa. Os 13 parâmetros da § 10 entraram; o
inventário está **completo em cobertura** e **provisório em classificação**, e a diferença
entre as duas coisas é o que os campos `fundamento_611b` e `classificacao_provisoria`
existem para carregar.

O que resta não é trabalho de modelagem. São **seis documentos** — o art. 611-B, as datas
das faixas de HE, o percentual da HE noturna, o mês-base do ACT, o mapa de categorias e a
cláusula 2.1.1 — e cada um tem, no arquivo que o espera, o lugar exato onde entra.
