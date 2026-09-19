# Bloco 5 — relatório

Inventário de parâmetros negociáveis e schema da camada de norma coletiva. **Não é extração
de PDF**: é varredura do que já está no repositório, mais modelagem.

Nenhuma skill escrita.

| Tarefa | Situação |
|---|---|
| 1 — Varredura dos blocos 02, 03 e 04 | **Feita** |
| 2 — Consolidação com a seção 10 de `02-base-normativa-verbas.md` | **BLOQUEADA** |
| 3 — Schema da camada | **Feito** |
| 4 — Fixture do ACT Gasmig | **BLOQUEADA** |
| 5 — `valida_parametros.py` + testes | **Feita**, menos o teste dependente da Tarefa 4 |

---

## 1. O bloqueio

> ### `docs/calculo/02-base-normativa-verbas.md` não existe no repositório.

O enunciado manda lê-lo e depende dele em duas tarefas. Procurei em todo o repositório, em
`Downloads/Plataforma-SaaS-Jus/`, na raiz de `Downloads` e nos zips recentes. **Não está em
lugar nenhum.**

O que chegou foi apenas o adendo, e ele próprio se declara complemento do que falta:

> "Fecha os seis pontos da **seção 11 de `02-base-normativa-verbas.md`**. Anexar como seções
> 13 a 18 daquele documento, substituindo a seção 11."
> — `02a-adendo-lacunas-verbas.md`, linha 3

### O que cada tarefa perdeu

| Tarefa | Depende de | Efeito |
|---|---|---|
| **2** | "seção 10 de `02-base-normativa-verbas.md` (**13 parâmetros**)" | Não posso somar nem deduplicar 13 itens que não vejo |
| **4** | "os parâmetros do ACT Gasmig 2025/2027 que estão descritos na **seção 3**" | Não tenho **nenhum** valor de cláusula: nem os três percentuais de HE, nem a jornada, nem a gratificação de sala de controle |
| **5**, teste 6 | Fixture da Tarefa 4 | Sem os percentuais, não há o que conferir |

O enunciado é explícito: **"Não invente cláusulas que não estejam no documento."** Não
inventei.

### O que fiz em vez de parar

Tarefas 1, 3 e 5 não dependem do arquivo ausente e foram feitas por inteiro. Onde a
dependência era real, a lacuna ficou **visível e estruturada**, não contornada:

- `parametros-negociaveis.md` abre com o aviso e diz quantos parâmetros faltam.
- O catálogo tem `completude.parcial: true` e nomeia o que falta.
- A fixture do Gasmig existe, mas com `status: "bloqueada"`, `clausulas: []`, e uma lista
  `parametros_esperados_nao_cadastrados` que diz, item a item, o que o escopo prometia e o
  que falta para preencher.
- O teste do caso 6 existe e **é pulado com a razão impressa**, de modo que a lacuna aparece
  na saída da suíte em vez de sumir.

### Como desbloquear

1. Colocar `02-base-normativa-verbas.md` em `docs/calculo/`.
2. Cruzar a seção 10 com o inventário — cada parâmetro tem `id`, verba, fonte e o texto
   literal que o sustenta, então a fusão é mecânica.
3. Transcrever as cláusulas da seção 3 em `instrumentos-act-gasmig-parcial.json`.
4. Reescrever `test_cadeia_temporal_act_gasmig_PENDENTE` com as três faixas reais. O teste
   já **falha de propósito** se alguém preencher a fixture e esquecer de reescrevê-lo.

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

- **`apenas-elevacao`** (9): têm piso legal e ativam a R18 — HE, HE do comissionista,
  noturno, transferência, insalubridade (base e percentual), dias de RSR, feriados no
  reflexo, aviso proporcional.
- **`qualquer`** (8): jornada semanal, compensação, sábado, turno, bancário art. 224,
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
| **4** (por maioria) | "A inclusão do sábado como RSR **não altera o divisor**, por não haver redução do número de horas semanais, trabalhadas e de repouso" |

São **duas consequências separadas do mesmo fato negocial**. Ampliar o RSR muda o numerador
do reflexo (`valor × nº_RSR / dias_úteis`), que alcança quatro verbas. Não muda o divisor do
salário-hora.

Por isso `pn.rsr.dias` e `pn.jornada.sabado-como-rsr` são parâmetros distintos, e o segundo
carrega as **duas correntes** — Súmula 124 (altera o divisor) × IRR-849 tese 4 (não altera) —
registradas, não arbitradas.

---

## 4. Seis candidatos que **não** viraram parâmetro

A regra do bloco: o que não se classifica com segurança vira dúvida, não palpite.

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

**Pendência D1**, separada: o corpus estabelece o **efeito** do enquadramento em turno
ininterrupto (6ª diária, divisor 180) mas **não contém** a autorização constitucional para
elevação da jornada do turno por negociação (CF art. 7º, XIV, parte final). Não pesquisei
fora do corpus, conforme a regra do bloco.

---

## 5. Tarefa 3 — o schema

Dois arquivos em `docs/calculo/tabelas-normativas/`:

| Arquivo | Conteúdo |
|---|---|
| `camada-norma-coletiva-schema.json` | Contrato da camada: chave, retorno, forma do instrumento, algoritmo, invariantes |
| `camada-norma-coletiva-catalogo.json` | Os 20 parâmetros com default, piso, tipo, variantes e sustentação literal |

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

Testado nos dois sentidos.

---

## 6. Tarefa 5 — validador

`scripts/calculo/valida_parametros.py` e `test_valida_parametros.py`.

```
Ran 101 tests in 0.101s
OK (skipped=1)
```

101 é a suíte inteira do repositório — 52 dos blocos anteriores mais **49 novos**. O único
`skip` é o caso 6, pelo bloqueio.

### Os seis casos pedidos

| # | Caso | Situação |
|---|---|---|
| 1 | Resolução com instrumento vigente | ✓ — 9 testes, incluindo proveniência e extensão |
| 2 | Sem instrumento → fallback + marcação (R14) | ✓ — 4 testes, incluindo o caso sem default legal |
| 3 | Competência anterior ao instrumento mais antigo | ✓ — 5 testes, incluindo bordas inclusivas e série mês a mês |
| 4 | Valor abaixo do piso → rejeição (R18) | ✓ — 7 testes |
| 5 | Dois instrumentos → conflito reportado | ✓ — 5 testes |
| 6 | Cadeia temporal do ACT Gasmig | **pulado** — mecanismo testado com fixture sintética |

Mais 19 testes de catálogo, competência, precedência (R16) e higiene aritmética.

### Duas decisões de comportamento que valem registro

**R18 rejeita, não corrige.** Cláusula de 40% com piso de 50% **não vira 50%**. A resolução
devolve o default, marca `cobertura: sem-cobertura-coletiva` e registra a rejeição. Corrigir
silenciosamente para o piso esconderia um defeito do instrumento cadastrado — ou um erro de
leitura do instrumento.

**O título judicial não é barrado pelo piso.** R16 põe o título acima de tudo; se um título
fixa adicional de 40%, o motor aplica 40% e registra a divergência. Aplicar a lei contra o
título é competência do juízo, não do motor. Testado explicitamente.

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

## 7. Pendências abertas

| # | Pendência | Bloqueia |
|---|---|---|
| **B1** | `02-base-normativa-verbas.md` ausente — 13 parâmetros da seção 10 não incorporados | Tarefa 2; inventário completo |
| **B2** | Mesma ausência — seção 3, cláusulas do ACT Gasmig | Tarefa 4; caso 6 do validador |
| **D1** | Autorização constitucional para elevar a jornada do turno de revezamento por negociação (CF art. 7º, XIV) não está no corpus | Variante do turno |
| **D2** | Seis candidatos não classificados — § 4 | Cobertura do inventário |
| **D3** | Vigência da Súmula 46 do TRT-3 após 2018 (pendência 3 da seção 19 do adendo) | Default de `pn.insalubridade.base` |
| **D4** | Mapa de categorias profissionais e série de ACTs (pendência 4 da seção 19 do adendo) | Alimentar a camada com dados reais |

**B1 e B2 são o mesmo arquivo.** Um único arquivo desbloqueia as duas tarefas e o teste.

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
blocos 03 e 04 registraram como se fosse fixa. **Enquanto os 13 parâmetros da seção 10 não
entrarem, o inventário está incompleto e o motor herdaria a lacuna em silêncio** — razão de
o catálogo declarar `completude.parcial: true`.
