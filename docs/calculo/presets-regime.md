# Presets de regime temporal

**Bloco 6.** A camada que decide **qual regra** se aplica a cada competência —
distinta da camada que decide **quanto vale** um parâmetro.

Fonte de verdade executável:
[`tabelas-normativas/regimes-temporais-catalogo.json`](tabelas-normativas/regimes-temporais-catalogo.json)
e [`tabelas-normativas/camada-regime-temporal-schema.json`](tabelas-normativas/camada-regime-temporal-schema.json).
Este documento é a leitura humana deles. Divergiram, vale o JSON.

**26 regimes. Catorze eixos de corte distintos.**

> **Esta é a v1.1.** A validação adversarial derrubou uma data inventada, quatro
> eixos apresentados como declarados quando eram inferência, e a afirmação de que
> o título era "o eixo mais frequente". Ver § 10.

---

## 1. A distinção que governa tudo

| | **Preset de regime** | **Parâmetro negociável** |
|---|---|---|
| Pergunta | Qual regra vale nesta competência? | Quanto vale esta constante? |
| Natureza | Escolha **jurídica** do usuário, ou cadeia determinada pela data | Resolvido por instrumento coletivo, título ou default legal |
| Negociável por sindicato | **Não** | Sim — é a definição |
| Chave | (regime, fatos do caso) — e os fatos variam por eixo | (parametro, categoria, competencia) |
| Quando é avaliado | **Antes** (R22) | Depois, e só se o regime permitir |
| Catálogo | `regimes-temporais-catalogo.json` | `camada-norma-coletiva-catalogo.json` |

**O regime decide se o parâmetro é sequer consultado.** Um contrato de 2015 sob a
corrente ultrativa nunca consulta a redação nova do art. 71, § 4º — e, portanto,
nunca consulta os parâmetros que só existem sob ela. O resolvedor devolve
`consultado: false` com o motivo, em vez de consultar e descartar: consultar e
descartar deixaria, na memória de cálculo, rastro de uma consulta que não houve.

### Não confundir com os presets de atualização

`01-plano-extracao.md` já tem um catálogo de presets — `TRAB-ADC58-LEI14905`,
`TRAB-FAZENDA`, `CIVEL-CC-TEMA1368`, `TRIB-FED-REPETICAO` e outros. Aqueles
respondem **como se atualiza** um valor já apurado: cadeias de correção e juros.
Estes respondem **qual regra de apuração** vale na competência. São famílias
distintas.

O único cruzamento: `TRAB-INTERTEMP-TEMPUS` e `TRAB-INTERTEMP-ULTRATIVO`, nomeados
em `02-base-normativa-verbas.md` § 1, pertencem a **esta** família. Eram os dois
únicos presets do repositório **sem catálogo** — a lacuna que o bloco 5 registrou
e este bloco fecha.

---

## 2. O eixo de corte não é o mesmo entre regimes

É o achado central da varredura, e o erro que esta camada existe para impedir.

> A OJ 394 corta pela **data da hora extra trabalhada**.
> A prescrição intercorrente, pela **data da determinação judicial**.
> A multa do art. 467, pela **data da sentença**.
> O divisor do bancário, por um **estado processual**.

Modelar como se fosse um eixo só não produz um erro barulhento. Produz um
resultado **plausível** com a conta inteira no regime errado.

### Os catorze eixos declarados

| Eixo | Regimes | Exemplo |
|---|---:|---|
| `competencia-do-fato` | 5 | OJ 394 / Tema 9 — a data da hora extra |
| `conteudo-do-titulo` | 2 + 3 alternativos | JAM; limite de 05/10/88 |
| `data-de-admissao` | 1 | eletricitários antes da Lei 12.740/2012 |
| `data-da-sentenca` | 1 | multa do art. 467 |
| `data-da-dispensa` | 1 | seguro-desemprego |
| `inicio-do-aviso` | 1 | aviso proporcional |
| `ciencia-da-lesao` | 1 | prescrição do FGTS |
| `determinacao-judicial-na-execucao` | 1 | prescrição intercorrente |
| `fato-gerador` | 1 | GILRAT |
| `data-do-calculo` | 1 | faixas de INSS em jan/2010 |
| `efetivo-pagamento` | 0 primários | governa a **aritmética** da conversão URV, não a seleção do regime |
| `estado-processual` | componente | modulação do IRR-849 |
| `decisao-de-merito-no-processo` | componente | modulação do IRR-849 |
| `data-base-da-categoria` | componente | planos econômicos |

**Dos catorze, apenas dois são de competência ou fato** — `competencia-do-fato` e
`fato-gerador`. Os outros doze são processuais, documentais ou contratuais.

Contado pela mesma régua dos dois lados — primários, componentes e alternativos —,
`conteudo-do-titulo` comparece **tanto quanto** `competencia-do-fato`. A precedência
R8 não é, portanto, uma exceção rara no corpus.

> A v1 deste documento dizia que o título era "o eixo **mais frequente**". Era efeito
> de contar o título de um jeito e a competência de outro. Contados igualmente,
> empatam. A afirmação forte saiu.

### Quatro valores especiais de `eixo`

- **`meta`** — o eixo é o próprio objeto da escolha. Só `pr.intertemporal`.
- **`herdado`** — sem eixo próprio; usa o eixo efetivo do regime-pai. Três regimes.
- **`composto`** — mais de um eixo simultâneo; não se resolve por data. Dois.
- **`NAO-DECLARADO`** — o corpus não diz qual data governa. **Inaplicável.** Cinco.

### E quatro estados de `eixo_origem`

Campo separado, e a distinção veio da validação adversarial.

| estado | o que significa | resolve? | quantos |
|---|---|---:|---:|
| `declarado` | o corpus diz qual data governa **a seleção da variante** | sim | 13 |
| `inferido` | o corpus sustenta o eixo para uma pergunta **vizinha** | sim, **com rastro** | 5 |
| `herdado` | o eixo é delegado ao regime-pai | após a escolha do pai | 3 |
| `nao-declarado` | nada | **não** | 5 |

A v1 tinha um booleano, `eixo_declarado`. Ele forçava a escolha entre mentir e
bloquear: regimes em que o corpus sustenta o eixo para outra pergunta — o piso
salarial, a tabela do seguro-desemprego, qual moeda vigia — apareciam como
**declarados** sem sê-lo.

O que separa `declarado` de `inferido` **não é o resultado** — os dois resolvem. É o
rastro: a resolução de um eixo inferido marca `eixo_inferido: true` e carrega a
justificativa, de modo que quem lê a memória de cálculo vê que ali houve um passo de
raciocínio, não uma leitura.

---

## 3. O meta-regime: direito intertemporal

`02-base-normativa-verbas.md` § 1 traz duas correntes do TST, **com acórdãos nos
dois sentidos dentro do mesmo tema**, e a instrução literal: **"Não resolver —
expor como preset."**

| Preset | Corrente | Eixo efetivo |
|---|---|---|
| `TRAB-INTERTEMP-TEMPUS` | `tempus regit actum` — o contrato se divide em 11/11/2017 | `competencia-do-fato` |
| `TRAB-INTERTEMP-ULTRATIVO` | ultratividade — regra da admissão por todo o contrato | `data-de-admissao` |

É o único regime cujo **eixo é o próprio objeto da escolha**. Escolher a corrente
não é escolher um valor: é escolher **qual data o motor vai ler** em todos os
regimes que dele herdam.

### Sem default, e por quê

`pr.intertemporal` tem `sem_default: true`. Atribuir-lhe um default seria arbitrar
a divergência que a base manda não arbitrar.

A consequência é dura e é correta: **sem escolha explícita, os regimes dependentes
não calculam.** O silêncio vira bloqueio visível, não um número plausível. É a
**R20-EXCECAO**, e vale para quatro regimes — este, o Tema 1046, o adicional de HE
pré-CF/88 e a Súmula 17.

### A interação que o enunciado mandou modelar

Mesmo contrato, mesma competência, duas correntes:

| | contrato admitido em 2015, competência 2024-05 |
|---|---|
| `tempus regit actum` | eixo = competência → **redação da Reforma**: só o período suprimido, natureza indenizatória, sem reflexos |
| `ultratividade` | eixo = admissão → **redação anterior**: intervalo integral, natureza salarial, com reflexos |

Sob ultratividade, **a regra nova nunca é consultada para esse contrato** — em
nenhuma competência, nem em 2026. E o reverso importa tanto quanto: sob *tempus*,
uma única conta usa dois regimes, e é por isso que a **R19 exige o registro por
competência**, não uma vez por processo.

---

## 4. Granularidade: a competência que atravessa o corte

O corpus dá cortes ao **dia** — 11/11/2017, 20/03/2023, 05/09/2001. O motor indexa
por **competência mensal**. Novembro de 2017 fica dos dois lados.

O resolvedor **recusa**:

```
competência 2017-11, corte 2017-11-11
  → calculavel: false
  → motivo: "competencia-atravessa-o-corte"
  → aviso: informe a data com precisão de dia
```

Qualquer convenção — o mês inteiro entra, o mês inteiro sai — inventaria meio mês
de cálculo sem deixar rastro. A recusa é visível; a convenção, não.

Com precisão de dia, resolve: 19/03/2023 → sem repercussão; 20/03/2023 → com
repercussão. O ponto não é daquele corte: `bloco-01-tabelas.md` já registrava o
mesmo fenômeno nas tabelas de jun/99, jun/00 e jun/11, que mudam no meio do mês.

---

## 5. Invariantes R19 a R22

**R19 — registro por competência.** Todo cálculo grava qual preset foi aplicado a
**cada competência**. Não basta gravar a escolha uma vez: sob *tempus regit actum*
a mesma conta usa regimes diferentes em meses diferentes. Deriva da R13.

**R20 — default marca a conta.** Regime sem escolha explícita usa o default e
registra `origem: "default"`. A marca não é decorativa: é o que permite a alguém
revisar o que ninguém decidiu.

**R20-EXCECAO — onde não há default.** Regime com `sem_default` não tem default.
Sem escolha, `calculavel: false`.

**R21 — divergir exige justificativa.** Escolher contra o default sem justificar é
**rejeitado** — `ErroDeDados`, não aviso. É a mesma disciplina que a R8 aplica ao
título judicial.

**R22 — regime antes de parâmetro.** `parametro_consultavel()` levanta
`RegimesNaoAvaliados` se chamado sem uma avaliação. É impedimento na composição,
não detecção no resultado — a mesma filosofia da R1 à R13.

---

## 6. O catálogo

`✓` eixo declarado no corpus · `✗` não declarado · `⇢` herdado · `⊕` composto.

### 6.1 Meta

| id | eixo | corte | variantes |
|---|---|---|---|
| `pr.intertemporal` | ✓ meta | 11/11/2017 | tempus regit actum · ultratividade |

### 6.2 Eixo declarado — competência do fato

| id | corte | variantes |
|---|---|---|
| `pr.oj394-reflexo-rsr` | 20/03/2023 | sem repercussão · com repercussão |
| `pr.divisor-cf88` | 05/10/1988 | divisor 240 · divisor 220 |
| `pr.inss-aviso-indenizado` | jan/2009 | sem incidência · com incidência |
| `pr.piso-nacional-salarios` ⟨inferido⟩ | 09/1987–07/1989 | PNS · salário mínimo |

### 6.3 Eixo declarado — outros eixos

| id | eixo | corte | variantes |
|---|---|---|---|
| `pr.multa467-base` | data da sentença | 05/09/2001 | dobro dos salários · 50% do incontroverso |
| `pr.periculosidade-eletricitarios` | data de admissão | Lei 12.740/2012* | totalidade das parcelas · salário-base |

\* O corpus não dá a data ao dia. Ver § 8.4.
| `pr.aviso-proporcional` | início do aviso | 13/10/2011 | 30 dias · proporcional |
| `pr.fgts-prescricao` | ciência da lesão | 13/11/2014 | transição · quinquenal |
| `pr.seguro-desemprego-regime` | data da dispensa ⟨inferido⟩ | 28/02/2015 | regime simples · três variáveis |
| `pr.urv-conversao` | competência ⟨inferido⟩ | 01/03/1994 | CR$ · URV · R$ |
| `pr.gilrat-fato-gerador` | fato gerador | 31/12/2009 | sem FAP · Dec. 6.957/2009 |
| `pr.faixas-inss-jan2010` | **data do cálculo** | jan/2010 | Portaria 350/09 · 333/10 |
| `pr.fgts-indice-jam` | conteúdo do título | — | JAM · sem JAM |
| `pr.indenizacao-tempo-servico-cf88` | conteúdo do título ⟨inferido⟩ | 05/10/1988 | limitada · sem limite |

### 6.4 Eixo herdado do intertemporal

| id | corte | variantes |
|---|---|---|
| `pr.intrajornada-71-4` | 11/11/2017 | redação anterior · redação da Reforma |
| `pr.in-itinere` | 11/11/2017 | devidas · suprimidas |
| `pr.art384-quinze-minutos` | 11/11/2017 | devido · revogado |

### 6.5 Eixo composto

| id | eixos | variantes |
|---|---|---|
| `pr.sumula124-divisor-bancario` | decisão de mérito no processo ⊕ estado processual ⊕ conteúdo do título | regime novo · regime preservado · transitado e silente |
| `pr.planos-economicos` ⟨inferido⟩ | competência ⊕ data-base da categoria | **bloqueado** — sem série |

### 6.6 Eixo NÃO declarado — inaplicáveis

| id | corte | o que falta |
|---|---|---|
| `pr.tema1046-validade-clausula` | 02/06/2022 | se cláusula anterior se julga pelo Tema 1046 ou pelos Temas 357/762 |
| `pr.insalubridade-base-sumula228` | abril/2018 | se a cassação da Súmula 228 alcança competências pretéritas |
| `pr.he-adicional-cf88` | 05/10/1988 | o eixo, **e** a disjunção 20% × 25% |
| `pr.multa477-documentos` | 11/11/2017 | o eixo (presumível data da rescisão; o texto não diz) |
| `pr.sumula17-salario-profissional` | 2003 | o eixo e o alcance da restauração |

### 6.7 Fora do motor de verbas

| id | eixo | por quê |
|---|---|---|
| `pr.prescricao-intercorrente` | determinação judicial na execução | `02a` § 15: *"é regra de liquidação e execução, não de apuração… Entra como marcador no processo, não no motor de verbas."* Está no catálogo para que o marcador exista e seja registrado, não para alterar apuração |

---

## 7. Três regimes que merecem nota

### `pr.oj394-reflexo-rsr` — o único com eixo negado nominalmente

`02a` § 13 não só declara o eixo: **nega dois rivais**. *"A modulação é pela data
do trabalho, não pela data do ajuizamento nem do julgamento."*

E corrige duas coisas já escritas no repositório:

- o **caso difícil nº 6** da lista de validação da Fase 3 está errado e precisa ser
  reescrito;
- o **bloco 03 § 8** listou a OJ 394 entre os pontos "não marcados, porque não
  mudam". Está desmentido.

É cadeia temporal: **ninguém escolhe**. A data decide, e a origem registrada é
`determinada-pela-data`.

### `pr.intrajornada-71-4` — duas mudanças, não uma

| | até 10/11/2017 | a partir de 11/11/2017 |
|---|---|---|
| **extensão** | intervalo **integral** | apenas o período **suprimido** |
| **natureza** | **salarial**, com reflexos | **indenizatória**, sem reflexos |

Tratar como uma mudança só é erro: a extensão muda o número de horas; a natureza
arrasta toda a cadeia de reflexos — 13º, férias + 1/3, aviso, FGTS, RSR.

Lacuna registrada: a Lei 8.923, de 27/07/1994, **acrescentou** o § 4º. Antes dela
não havia consequência pecuniária — um terceiro regime que o corpus não enuncia.
Não foi cadastrado.

### `pr.sumula124-divisor-bancario` — o que prova a tese

Três eixos simultâneos, **nenhum deles a competência**:

1. houve decisão de mérito de Turma do TST ou da SBDI-1 entre 27/09/2012 e
   21/11/2016 **neste processo**?
2. a sentença transitou em julgado e está **em liquidação**?
3. o título é **silente quanto ao divisor**?

A mesma competência, no mesmo processo, resolve-se por um estado processual e pelo
conteúdo do título. Um eixo único não modela isto.

---

## 8. Lacunas

### 8.1 Eixo não declarado — a maior

Quinze pontos do corpus e **dezesseis marcas de Fase 4** trazem a data de corte sem
declarar o eixo. As marcas F (`bloco-03-verbas.md` § 8, F1–F9; `bloco-04-verbas2.md`
§ 12, F1–F7) herdam o eixo de `pr.intertemporal` — que não está arbitrado. **Todo o
corte de 11/11/2017 está parado nesse único ponto.**

Supor o eixo é a forma mais silenciosa de errar. A regra do bloco — não pesquisar,
declarar a pendência — vale aqui com força redobrada.

### 8.2 O Tema 1046 é o maior achado fora da lista dos seis

Ele decide a **validade de qualquer cláusula coletiva** — logo, governa a resolução
dos 32 parâmetros negociáveis inteiros (`afeta_parametros: ["TODOS"]`). O corpus
registra o julgamento e que ele *revisou* os Temas 357 e 762, mas **não diz** se
cláusula anterior a 02/06/2022 se julga por ele ou pelo regime revisado.

Consequência testada: enquanto o eixo faltar, nenhum parâmetro negociável é
consultável sem que o bloqueio fique registrado.

### 8.3 A variante do salário básico, e um cuidado

O bloco 5 **removeu** `salario-basico` de `pn.insalubridade.base`, porque a Rcl
6.275 foi cassada definitivamente. Removê-la do catálogo de **parâmetros** foi
correto: não é mais opção negociável.

Mas se a cassação **não retroage**, competências anteriores a abril/2018 podem
seguir o salário básico — e aí ela precisa voltar **como variante de regime**, não
de parâmetro. É exatamente isso que o eixo não declarado impede decidir.

### 8.4 A data que o corpus não tem

`pr.periculosidade-eletricitarios` corta pela **Lei 12.740/2012**, e o corpus diz
exatamente isso: *"eletricitários contratados antes da Lei 12.740/2012"*. **Sem dia,
sem mês.**

A v1 deste catálogo cravou `2012-12-08`. É historicamente a data de publicação da
lei e ainda assim é invenção, porque não está em arquivo nenhum do repositório.

O corte agora é `2012`, e as janelas das variantes são `até 2011` e `a partir de
2013`. A consequência é deliberada e é o ponto: **admissão ocorrida em 2012 não
resolve** — o resolvedor devolve `nenhuma-variante-cobre-a-data`. A fronteira fica
grossa porque o corpus a deixou grossa.

### 8.5 Regime sem série

`pr.planos-economicos` está `bloqueado`. Os índices do período — IPC, URP, IRSM,
FAS, FAZ, IPC-r, FRS — **não estão em nenhuma tabela** do item 18 extraída no bloco
1 (pendência P19 do bloco 04). É regime sem série: não há o que aplicar.

---

## 9. O que a validação adversarial derrubou

Registro do que a v1 afirmava e não sustentava.

| # | Afirmação da v1 | Correção |
|---|---|---|
| 1 | `pr.periculosidade-eletricitarios` cortava em **08/12/2012** | A data ao dia não está no corpus. Corte passou a `2012`, com o vão declarado — § 8.4 |
| 2 | `pr.piso-nacional-salarios` com eixo **declarado** | Uma janela de vigência não é declaração de eixo. Passou a `inferido` |
| 3 | `pr.indenizacao-tempo-servico-cf88` — *"o corte é de competência, mas quem o impõe é o título"* | Essa frase é minha, não do corpus, que nunca nomeia o título. Passou a `inferido` |
| 4 | `pr.urv-conversao` com eixo **efetivo-pagamento** | As citações declaram a **aritmética** da conversão, não a seleção do regime monetário. Eixo passou a competência ⟨inferido⟩, e a aritmética foi para campo próprio |
| 5 | `pr.seguro-desemprego-regime` com eixo **declarado** | As citações governam a tabela e o piso, não a escolha do regime. Passou a `inferido` |
| 6 | `R20-EXCECAO` nomeava **três** regimes | São quatro |
| 7 | *"Quinze pontos do corpus"* sem eixo declarado | Número não enumerado nem derivável. Retirado |
| 8 | As 16 marcas F, *"todas com o corte de 11/11/2017"* | A F6 do bloco 03 é da **Lei 13.419/2017** |
| 9 | Ressalva das marcas F citada entre aspas | Era costura de duas frases diferentes. Desfeita |
| 10 | Planos econômicos: *"treze regimes sucessivos"* | O corpus conta "dez normas"; a tabela tem dezesseis linhas, catorze com norma. Nenhum número foi adotado |
| 11 | *"O título é o eixo mais frequente"* | Contagem assimétrica. Contados igualmente, empatam — § 2 |

Mais oito imprecisões de citação, todas corrigidas no catálogo.

O que **resistiu**: as demais doze datas de corte, conferidas uma a uma; os números
estruturais; as quatro afirmações negativas — inclusive a de que **não há regra
geral de prescrição trabalhista em lugar nenhum do corpus**.

---

## 10. Ver também

- [`tabelas-normativas/regimes-temporais-catalogo.json`](tabelas-normativas/regimes-temporais-catalogo.json) — os 26 regimes
- [`tabelas-normativas/camada-regime-temporal-schema.json`](tabelas-normativas/camada-regime-temporal-schema.json) — o contrato
- [`parametros-negociaveis.md`](parametros-negociaveis.md) — a outra camada, avaliada depois
- [`extracao/bloco-06-relatorio.md`](extracao/bloco-06-relatorio.md) — relatório do bloco
- `scripts/calculo/valida_regimes.py` — validador e resolvedor (76 testes)
- `tests/fixtures/calculo/regimes-casos.json` — doze casos, sintéticos e declarados
