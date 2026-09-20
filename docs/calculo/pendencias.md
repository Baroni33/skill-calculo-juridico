# Pendências

Consolidado em 18/09/2026. Três origens: a seção 9 de `00-base-normativa.md`,
lacunas descobertas na montagem desta base, e observações sobre o código do SaaS.

---

## 1. Pendências normativas (seção 9 da base normativa)

| # | Pendência | Tipo | Bloqueia |
|---|---|---|---|
| N1 | Classificação da Gasmig como Fazenda Pública ou não | Determinação jurídica do cliente | Tamanho do catálogo |
| N2 | Tabela Única do CSJT — contrato de integração | Integração | Motor trabalhista |
| N3 | Efeito da EC 136/2025 na Justiça do Trabalho | Aguarda consolidação TST/CSJT | Ramo FP trabalhista |
| N4 | ADI 7873 | Aguarda julgamento | Estabilidade do ramo FP |

**N1 é a de maior impacto.** Se a Gasmig não for Fazenda Pública, somem do escopo:
o ramo FP das três jurisdições, precatório, EC 113/136 e a consolidação de dez/2021.
Não é pesquisa — é pergunta ao jurídico do cliente, ou leitura de como os juízes vêm
decidindo nos processos existentes.

### Instabilidades registradas, não resolvidas

Divergência não se resolve, se registra (regra 6 do plano):

- **TJ-SP, 2ª Câmara de Direito Público** (AI 3001155-79.2026.8.26.0000) mantém a SELIC
  para débitos não submetidos à fase de precatório, aplicando a EC 136 apenas após a
  expedição do requisitório — contra CJF Res. 990/2026 e STJ REsp 2.236.270/SP.
- **Fazenda Pública estadual e municipal:** a EC 136/2025 menciona apenas "Fazenda
  Pública federal". Requisitórios estaduais e municipais ficam sem a regra antiga
  (revogada) e sem a nova (que não os alcança). Vácuo normativo.
- **Juros TRD na fase pré-judicial trabalhista:** parte da doutrina sustenta
  incompatibilidade com a própria ADC 58, que declarou a TR inconstitucional para
  débitos trabalhistas. Expor como variante (`TRAB-ADC58-SEM-TRD`), não como default.

---

## 2. Taxa legal — ausência de par de validação IPCA-15

**Status: aberta. Afeta a cobertura de teste de `scripts/calculo/valida_taxa_legal.py`.**

A fórmula é a mesma nos dois casos:

```
TL_m = (Fator_Selic_m / Fator_Deflator_{m-1} - 1) × 100
```

O que muda é o deflator:

| Variante | Deflator | Fundamento | Par de validação |
|---|---|---|---|
| Regra geral | IPCA-15 | Res. CMN 5.171/2024 | **nenhum** |
| Previdenciária | INPC | Manual CJF 990/2026, item 4.3.2, Nota 3 | dois, seção 4 |

Os dois pares publicados na seção 4 da base normativa — set/2025 = 1,377047% e
mai/2026 = 0,277807% — vêm da tabela de **taxa legal previdenciária** do Manual CJF,
cuja coluna é `Fator INPC`. São do caso INPC, e estão registrados como tal em
`PARES_VALIDACAO_INPC`.

**Consequência:** a variante IPCA-15, que é a regra geral e a de maior uso, está
implementada mas **sem verificação contra valor publicado**. A aritmética é
compartilhada e está coberta pelos pares INPC; o que falta é a confirmação de que a
série correta alimenta `fator_deflator` na regra geral.

**Como fechar:** o Banco Central divulga mensalmente a taxa legal, o Fator Selic e o
Fator IPCA (seção 4). A Calculadora do Cidadão do BCB tem módulo de taxa legal e serve
como oráculo. Extrair dois meses e acrescentar `PARES_VALIDACAO_IPCA15`.

---

## 3. Truncamento, não arredondamento — decidido, registrar

**Status: fechada, registrada aqui porque a base normativa não a explicitava.**

R12 exige "critério de truncamento definido e consistente por etapa", mas não dizia
qual. Os dois pares de validação resolvem a questão empiricamente:

| Competência | Razão exata | Truncado | Half-up | Manual |
|---|---|---|---|---|
| Set/2025 | 1,3770478004 | **1,377047** ✓ | 1,377048 ✗ | 1,377047 |
| Mai/2026 | 0,2778077572 | **0,277807** ✓ | 0,277808 ✗ | 0,277807 |

Arredondamento half-up erra o último dígito **nos dois casos**. Só truncamento fecha.

Corroborado pelo texto do próprio Manual CJF (`manual_de_calculos_2026.pdf`,
pagina_pdf 53): *"são inerentes ao critério de truncamento de casas decimais aplicado
em cada etapa do cálculo"*.

Implementado como `ROUND_DOWN` em `valida_taxa_legal.py`, com teste negativo que falha
se alguém trocar por half-up.

---

## 4. Observações sobre `CalculosService.cs` no repositório do SaaS

**Status: nota para a Fase 5 (build do motor). SEM AÇÃO AGORA.**

Arquivo: `Plataforma-SaaS-Jus/saas/saas/backend/src/Services/CalculosService.cs`.
Repositório distinto deste; nada foi alterado lá. Registrado para que a portabilidade
do motor não herde os defeitos.

O que há de bom: o backend usa `decimal` em toda parte — **zero ocorrências de `double`
ou `float`** em `src/`. A base para R12 já existe.

Três violações observadas no cálculo de taxa legal (linhas ~127-137):

```csharp
var ipca  = Valor(series, Indice.IPCA,  mesAno) / 100m;
var selic = Valor(series, Indice.SELIC, mesAno) / 100m;
var taxaLegal = Math.Max(0m, selic - ipca);          // (a) e (b)
...
var baseParaJuros = acumulado + jurosAcumulado;
jurosAcumulado = Math.Round(jurosAcumulado + baseParaJuros * taxaLegal, 2);  // (c)
```

| # | Invariante | Observação |
|---|---|---|
| (a) | **R11** | Subtração literal de percentuais. É exatamente o erro que a seção 4 antecipa: ~0,003 p.p./mês, acumulativo. A operação é razão entre fatores. |
| (b) | **R11** | Usa o IPCA do mês corrente. A norma exige o IPCA-15 do mês **anterior** (`m-1`). |
| (c) | **R4** | `baseParaJuros` inclui `jurosAcumulado`, capitalizando. Juros de mora, SELIC e taxa legal são sempre simples. |
| (d) | **R12** | Todo `Math.Round(x, 2)` sem `MidpointRounding`. O default do .NET é *banker's rounding*; a norma exige truncamento. |

Também ausente: a distinção IPCA-E / IPCA (a enum tem ambos, mas a cadeia não bifurca
por fase), e o marco inicial dos juros trabalhistas usa `DataCitacao` — R7 exige
**ajuizamento** no trabalhista.

**Recomendação para a Fase 5:** o motor nasce em `src/Domain/Calculo/`, ao lado de
`Domain/Pareceres/` e `Domain/Sla/`, não evolui de `CalculosService`. O serviço atual
é POC e está acoplado a repositório e EF.

---

## 5. Versionamento de séries de referência — ausente no SaaS

**Status: aberta. Bloqueia R13.**

`IndicesSyncService` faz upsert destrutivo sobre `IndicesMonetarios`:

```csharp
if (existente != null) { existente.Valor = valor; }
```

Sem histórico, sem versão, sem data de coleta. R13 exige que toda conta grave a
**versão das séries consumidas**. Hoje, uma série revisada pelo órgão emissor altera
silenciosamente cálculos já emitidos — e uma conta não pode ser reproduzida.

O contrato definido em `skills/indices-judiciais/` precisa suportar leitura por versão,
não só por competência. O backend também não tem migrations EF (só `db/Dockerfile`);
o schema vem de seed.

---

## 6. Fixture 2 — dígito final do método detalhado

**Status: verificação pendente, baixo risco.**

Em `fixture-02-fazenda-publica-jun2026.json`, o total pelo método detalhado consta como
R$ 5.218,27. A camada de texto do PDF trunca o valor em `R$ 5.218,2` (pagina_pdf 52).
O dígito foi derivado por aritmética: 3.412,64 + 1.805,63 = 5.218,27, consistente com a
divergência de R$ 0,01 que o manual declara na pagina_pdf 53.

Confirmar visualmente antes de tratar como transcrição literal. O valor esperado da
fixture (R$ 5.218,28, método resumido) não depende disso.

---

## 7. Schema das tabelas normativas — duas famílias, um diretório

**Status: aberta. Bloqueia a Fase 3.**

O schema canônico de `01-plano-extracao.md` descreve cadeia período → indexador, com
`segmentos`, `engloba` e `aplicacao`. O bloco 1 produziu seis tabelas de outra natureza
— matriz de incidência, estrutura de faixa, enquadramento por atividade, critério de
contagem — que não têm linha do tempo de indexador e que `valida_cobertura.py` não
alcança.

Foram gravadas com shape próprio, marcado `categoria: "A-semantica"`, **sem forçar o
schema canônico**. Duas saídas aparentes: um campo `tipo` discriminando as famílias
dentro do mesmo schema, ou dois diretórios. Decidir antes que a Fase 5 leia daqui.

Detalhe em `tabelas-normativas/README.md`.

---

## 8. Calendários do Manual TRT-3 são defeituosos

**Status: fechada como constatação; abre trabalho na Fase 4.**

O item 18.14 (p. 460–466) imprime treze meses com menos dias do que têm. Conferido na
imagem da página, não só na camada de texto:

- **Setembro de 2009**: a célula de sábado da primeira semana traz **7** onde deveria
  estar **5**; o dia 5 não aparece em lugar nenhum.
- **Março de 2017**: a coluna inteira de segunda-feira está vazia — faltam 6, 13, 20 e
  27 — e os demais dias aparecem deslocados uma coluna à direita.

Outros onze meses perdem um ou dois dias. A extração é fiel ao impresso: `dia_da_semana`
reproduz a coluna do original e por isso diverge do calendário real em 42 dias.

**Consequência:** o calendário do manual não serve para contar dias úteis nem feriados.
As contagens de RSR do item 18.13 dependem de calendário e de feriados; confrontá-las
com um calendário independente é trabalho da Fase 4. Até lá, não derivar dias úteis de
`serie-18.14-calendarios.csv`.

---

## 9. Método de conversão da URV

**Status: parcialmente fechada no bloco 2. Resta o arredondamento.**

O item 18.10 (p. 453–455) traz as cotações diárias da URV em CR$ e nada mais. O método
**não estava no capítulo de critérios matemáticos** (p. 9–17), como se supunha, mas no
item 6.1, página 18:

> "os salários dos recibos de março/94 a junho/94 estão expressos em URV, sendo necessária,
> para o cálculo, a conversão para cruzeiros reais, multiplicando-se a expressão em URV
> pelo valor nominal da URV **do dia do pagamento**."

```
valor_em_CR$ = valor_em_URV × URV(dia_do_pagamento)
```

**Fechado:** direção da operação e data-base.
**Aberto:** critério de arredondamento, que o manual não declara.

Não confundir com a conversão inversa, CR$ → URV, de março/1994 (MP 434/94 e Lei 8880/94),
que se faz por divisão e média aritmética de quatro meses (p. 81).

Detalhe em `extracao/trabalhista/bloco-02-criterios.md`, § 7.
Registrado em `tabelas-normativas/trt3-18.10-urv-conversao.json`.

---

## 9-A. Critério de arredondamento: as duas fontes primárias divergem

**Status: aberta. Bloqueia o núcleo aritmético de `calculo-judicial-core`.**

O § 3 acima fixou truncamento a partir do Manual CJF, e isso continua certo **para a taxa
legal**. O bloco 2 mostrou que o problema é maior: o Manual TRT-3 **arredonda**.

| Operação (TRT-3, item 5.3, p. 17) | Exato | Publicado | Truncado |
|---|---|---|---|
| 25 / 60 | 0,41666… | **0,42** | 0,41 |
| 10 / 60 | 0,16666… | **0,17** | 0,16 |
| 5 × 4,285714 | 21,428570 | **21,43** | 21,42 |
| 180,00 × 4,285714 | 771,428520 | **771,43** | 771,42 |

Quatro exemplos, nenhum compatível com truncamento. Não é acidente de um caso.

R12 exige "critério de truncamento definido e consistente por etapa". **Um critério global
único contraria uma das duas fontes.** Decidir se o critério é atributo da jurisdição, do
tipo de operação, ou de ambos — antes de escrever o núcleo aritmético.

Detalhe em `extracao/trabalhista/bloco-02-relatorio.md`, § 4.

---

## 9-B. Regra do índice negativo é ambígua

**Status: aberta. Interage com R5.**

Manual TRT-3, item 5.3, p. 16:

> "Se houver um Índice com sinal negativo em algum mês, basta dividir o total acumulado até
> o referido mês pelo número índice que apresentou a variação negativa."

A regra só produz redução se o número índice for construído com o **valor absoluto** do
percentual (−0,23% → 1,0023, e dividir). Construído pela fórmula geral do próprio manual
(`i = p/100 + 1`, −0,23% → 0,9977), **dividir aumentaria** o acumulado.

O manual não diz qual construção usar e **não traz exemplo numérico com índice negativo**.
Sem oráculo. Não foi inferido.

---

## 11. A data do Manual TRT-3 está errada no corpus

**Status: aberta. Decisão do usuário.**

`fontes.md` e `00-base-normativa.md` § 10 registram **julho/2016**. A capa do PDF não traz
data, e o conteúdo vai até **19/12/2016** (acórdão do IRR-849, p. 38–39), com tabelas de
2017 e calendários até 2020. O documento é, no mínimo, de **2017**.

Não é detalhe bibliográfico: muda o que se pode afirmar sobre a defasagem. **O manual não é
anterior ao IRR-849 — ele o transcreve.** Continua anterior à Lei 13.467/2017.

`fontes.md` recebeu nota com a evidência. `00-base-normativa.md` **não foi tocado**: é fonte
de verdade do usuário. Decidir se corrige lá.

---

## 12. Não há base normativa contra a qual confrontar as verbas trabalhistas

**Status: FECHADA em 19/09/2026.** `docs/calculo/02-base-normativa-verbas.md` chegou ao
repositório, com o adendo `02a-adendo-lacunas-verbas.md`. Cobre marco temporal, Tema 1046,
horas in itinere, intervalo intrajornada, base da insalubridade, cumulação, base da
periculosidade, Súmula 124, turno de revezamento e os parâmetros negociáveis do ACT Gasmig.

O que a base **não** cobriu está registrado na § 17 abaixo — são os seis pontos que ela
própria declara como não pesquisados.

O texto original da pendência segue, para registro do que estava em aberto:

`00-base-normativa.md` cobre correção monetária, juros, Fazenda Pública, invariantes R1–R13
e fixtures. **Não tem uma linha sobre aviso-prévio, 13º salário, férias, RSR ou horas
extras.**

A regra de extração manda marcar toda afirmação do manual que a base contradiga. No bloco 3
não houve a quem apontar: os únicos dois pontos de contato — R8 e a regra 6 do plano —
**confirmam** o manual em vez de conflitar.

A Fase 4 do capítulo 6 precisa de um corpo normativo sobre verbas, centrado na **Lei
13.467/2017**, que hoje não existe no repositório. Os nove pontos de impacto estão
identificados em `extracao/trabalhista/bloco-03-verbas.md` § 8, mas o **conteúdo novo de
cada dispositivo não foi verificado**.

---

## 15. Camada de norma coletiva — lacunas residuais

**A pendência original desta seção está FECHADA.** `docs/calculo/02-base-normativa-verbas.md`
chegou ao repositório, foi lido integralmente, e desbloqueou as tarefas 2 e 4 do bloco 5: o
inventário está consolidado em **32 parâmetros** e a fixture do ACT Gasmig é real. O `skip`
do caso 6 saiu da suíte. Hoje são 199 testes no repositório, nenhum pulado.

O que a chegada do arquivo deixou aberto:

### 15.1 Texto integral do art. 611-B da CLT — **a maior**

O artigo tem trinta incisos e é a **âncora da classificação** de todo o inventário: inciso
→ `apenas-elevacao`; parágrafo único (duração do trabalho e intervalos) → `qualquer`;
demais → `qualquer` sob o Tema 1046/STF.

**Só três incisos foram fornecidos** — VI (trabalho noturno), XVII (saúde, higiene e
segurança) e XVIII (atividades penosas, insalubres ou perigosas) — **por instrução direta do
usuário, não pelo corpus**. O texto integral não está no repositório: o art. 611-B aparece
apenas *citado* em `02-base-normativa-verbas.md` § 2, sem transcrever inciso algum, e está
ausente dos dois PDFs. Não foi pesquisado na web, conforme a regra do bloco. O número de
trinta incisos também veio por instrução.

Quem auditar o catálogo contra o corpus **não vai achar o art. 611-B**. A origem está
declarada em `classificacao_611b.ORIGEM_DESTE_BLOCO` e há teste prendendo a declaração.

**Efeito medido:** 16 dos 32 parâmetros carregam `fundamento_611b: "nao-mapeado"` e
`classificacao_provisoria: true`. O validador exige a correspondência nos dois sentidos, e
`Catalogo.provisorios()` lista quais são. Um documento reclassifica metade do inventário.

**Ressalva já registrada:** há decisão do TST aplicando o inciso XVII para invalidar cláusula
sobre jornada quando a extensão configura risco à saúde, com ressalva expressa de que o
parágrafo único não a salva. O corte não é absoluto. Isso é mérito, não cálculo — o motor
aplica a cláusula e registra; a nulidade é do juízo. Marcado como `ressalva_611b_xvii`.

**Sub-pendência:** a decisão foi recebida por instrução, **sem órgão, processo nem data**.
Enquanto a referência faltar, a marca sinaliza um risco que não se pode citar.

### 15.2 Dados do ACT Gasmig 2025/2027

O ACT integral continua fora do repositório; o que existe é a leitura que a base normativa
faz dele.

| # | O que falta | Efeito |
|---|---|---|
| a | **Intervalos de competência das três faixas de HE** (80% / 75% / 60% "por período") | O parâmetro de maior uso do ACT resolve pelo **default legal de 50%**, contra 60–80% reais |
| b | Percentual da HE noturna (a forma é conhecida: percentual direto sobre a hora diurna) | `derivacao.sobrescrevivel` não é exercitado com dado real |
| c | **Mês-base** do ACT | `vigencia` com as duas pontas nulas — o instrumento vale para qualquer competência consultada. Conservador, mas incorreto no mundo |
| d | Identificador real de categoria | `gasmig-sitramico` é **rótulo desta extração**, não do documento |
| e | Cláusula **2.1.1** e a categoria que ela estende | R17 não é exercitada com dado real; `categoria: null` não alcança ninguém |
| f | **Gratificação de sala de controle** | A expressão não aparece em lugar nenhum do documento. Não se sabe se é parâmetro, verba autônoma ou natureza de verba |
| g | **Contribuição negocial** — a § 7 registra que o ACT 2025/2027 usa o adicional de periculosidade como base da contribuição | Percentual e destinação desconhecidos. É desconto, não verba a apurar; provável parâmetro de uma camada de descontos que ainda não existe |
| h | **Sábado como dia de repouso** — a § 8 manda "registrar como ponto a confirmar" | O ACT mantém o sábado como dia útil remunerado, e isso interage com `pn.jornada.sabado-como-rsr` e com a escolha da variante de RSR do item **18.13** do manual. Nenhuma cláusula foi cadastrada: a base diz expressamente que a leitura definitiva depende do ACT e das normas internas |

Sobre (a): as três faixas **não foram cadastradas** porque três cláusulas do mesmo parâmetro
sem `vigencia_propria` se sobrepõem, e sobreposição no mesmo instrumento é defeito de
cadastro. A ordem no documento é *descendente*, o que é incomum numa progressão temporal e
reforça que as datas não podem ser supostas.

Sobre (f): a § 12, pendência 3, fala genericamente em "IP 10.5 (PCCR) e demais Instruções de
Pessoal referenciadas no ACT — definem gratificações que integram base", sem nomeá-las.

### 15.3 Duas divergências entre o enunciado do bloco 5 e o documento

Registradas em `tests/fixtures/calculo/instrumentos-act-gasmig.json`:

1. O enunciado aponta a **§ 3** como fonte dos valores do ACT. A § 3 é *Horas in itinere*.
   Os **valores** estão nas **§§ 8, 9 e, principalmente, na coluna "Observação" da tabela da
   § 10**; as §§ 7 e 12 trazem contexto, não valores. Sem efeito prático — foram
   localizados —, mas registrado.
2. A **cláusula 2.1.1** é citada no enunciado e **não aparece** no documento.

### 15.5 Direito intertemporal — duas correntes, e por que NÃO entraram no inventário

`02-base-normativa-verbas.md` § 1 traz a divergência sobre a aplicação da Lei 13.467/2017
(vigência 11/11/2017) aos contratos em curso, com **acórdãos do TST nos dois sentidos,
inclusive dentro do mesmo tema**, e a instrução literal **"Não resolver — expor como
preset"**:

| Preset | Corrente | Efeito |
|---|---|---|
| `TRAB-INTERTEMP-TEMPUS` | `tempus regit actum` | corte em 11/11/2017; o contrato se divide — regra antiga até 10/11, nova a partir de 11/11 |
| `TRAB-INTERTEMP-ULTRATIVO` | ultratividade da lei do contrato | regra da data de admissão por toda a duração do contrato |

> **FECHADA pelo bloco 6.** A camada de presets de regime temporal existe:
> `docs/calculo/presets-regime.md`, `tabelas-normativas/regimes-temporais-catalogo.json`
> e `scripts/calculo/valida_regimes.py`. Os dois presets são as variantes de
> `pr.intertemporal`, cada uma com o **eixo efetivo** declarado — `tempus regit
> actum` lê a competência; a ultratividade lê a data de admissão. O regime tem
> `sem_default: true`, de modo que a ausência de escolha bloqueia o cálculo em vez
> de produzir um número. Ver `pendencias.md` § 19 para o que o bloco 6 deixou aberto.

**Isto não é parâmetro negociável e por isso não entrou em
`camada-norma-coletiva-catalogo.json`.** Nenhum sindicato negocia qual corrente de direito
intertemporal se aplica: a escolha é do operador do cálculo, não de um instrumento
coletivo. Metê-la no catálogo dos 32 seria erro de categoria — e o catálogo passaria a
misturar duas camadas com chaves de resolução diferentes (`(parametro, categoria,
competencia)` não tem onde encaixar um preset de cálculo).

**Mas a lacuna é real e é grande.** A própria base diz que, tendo a Gasmig contratos
anteriores a 11/11/2017 gerando passivo, **a escolha move o resultado em praticamente todos
os pontos daquela seção**. Falta uma **camada de presets de cálculo**, irmã da camada de
norma coletiva, com a mesma disciplina: duas variantes registradas, nenhuma arbitrada,
proveniência na memória de cálculo. Enquanto ela não existir, os dois presets não têm onde
morar e nenhum ponto do motor sabe qual regra aplicar antes de 11/11/2017.

É pendência de **modelagem**, não de dado — não depende de nenhum documento chegar.

### 15.4 Lastro removido por falta de fonte

Os percentuais de insalubridade **por grau** (leve 10% / máximo 40%) saíram do catálogo. Não
estão em lugar nenhum do corpus, e a citação que os sustentava não correspondia a texto real.
O único percentual que o corpus traz é o grau médio, 20%. Reintroduzir só com a fonte.

Detalhamento em `extracao/bloco-05-relatorio.md` §§ 1, 1-A e 7, e em
`parametros-negociaveis.md` §§ 3 e 9.2.

---

## 16. Escopo não decidido

- **Modelos de petição** (págs. 310–336 do manual trabalhista): decidir escopo antes de
  gastar extração (Fase 2). Podem ficar inteiramente fora.
- **Encargos processuais**: provisoriamente em `calculo-trabalhista-liquidacao`, mas as
  faixas de honorários são do CPC art. 85, § 3º, não da CLT, e valem nos três ramos.
  Provável separação na Fase 5.
- **Triagem das págs. 46–471 do manual trabalhista**: as págs. 1–45 foram lidas
  integralmente; o restante vem do índice e de amostragem das aberturas. Tratar como
  hipótese a confirmar na extração. As fronteiras de 83 e 373 foram verificadas e
  conferem. **As págs. 373–471 foram confirmadas na extração do bloco 1**, com quatro
  desvios de paginação em relação ao índice do escopo — ver
  `extracao/trabalhista/bloco-01-tabelas.md`, seção 2.
- **Dois quadros sem numeração 18.x** foram encontrados e extraídos em arquivos próprios:
  MOEDAS/PARIDADES (p. 381) e alíquotas por código FPAS, Anexo I da IN/RFB 1238/2012
  (p. 449). Decidir se entram no escopo do módulo.

---

## 14. Correção de registro: a pendência P7 do bloco 3 era um erro de extração

**Status: fechada. Registrada porque o erro foi meu, não do manual.**

O relatório do bloco 3 abriu a pendência **P7** afirmando que "não existe item 6.12 na
numeração impressa — salta de 6.11 (p. 59) para 6.13 (p. 67)".

**O item 6.12 existe: `6.12. Comissões`, páginas 65 a 67.** O levantamento de títulos usava
um padrão que exigia espaço logo após o número (`6.12 `), e o original imprime o ponto
(`6.12.`). O item escapou da varredura, e o bloco 3 parou na p. 54, de modo que nenhuma
leitura posterior o recuperou.

Não era detalhe de inventário: o 6.12 é o **"tópico comissões"** para o qual os itens 6.4
(p. 29) e 6.6.2 (p. 37) remetem, e que o bloco 3 declarou estar fora do recorte — duas
vezes. Traz a regra mais desenvolvida do capítulo sobre base de cálculo de horas extras.

Extraído em `extracao/trabalhista/bloco-04-verbas2.md` § 6. Ver também
`bloco-04-relatorio.md` § 1.

**Segunda correção:** os itens 6.1 a 6.6 terminam na **p. 55**, não na 54 — os passos finais
do exemplo de supressão de horas extras (6.6.8) ficam na página seguinte. O fecho está em
`bloco-04-verbas2-detalhe.md` § 1.


---

## 17. O que a base normativa de verbas declara NÃO ter pesquisado

**Status: aberta.** `02-base-normativa-verbas.md` § 11 faz o registro honesto das próprias
lacunas. Todos eram pontos marcados nos blocos 03 e 04, e **nenhum foi fechado pelo bloco 5**
— o bloco 5 trata da camada de norma coletiva, não destes.

| # | Ponto | Por que importa |
|---|---|---|
| 1 | Multa do art. 477, § 8º — alterações da Reforma | Verba rescisória frequente |
| 2 | Prescrição intercorrente, art. 11-A (novo na Reforma) | Afeta liquidação, não apuração |
| 3 | Estado atual das Súmulas 264 e 340 do TST | Base de HE e apuração do valor-hora |
| 4 | Multa do art. 467 — alterações | Verbas incontroversas |
| 5 | Adicional de transferência | Marcado no bloco 04 |
| 6 | **Efeito da Reforma sobre reflexos e OJ 394 da SDI-1** | Caso difícil nº 6 da lista de validação |

**O item 6 é o de maior prioridade**, por declaração da própria base: a OJ 394 está na lista
de casos difíceis da Fase 3 e ainda não foi confrontada com o estado atual.

Nota sobre o item 3: o bloco 3 registrou, e depois corrigiu, uma afirmação falsa de que a
**Súmula 264** trazia regra desenvolvida — ver o relatório do bloco 3. O estado atual dos
dois verbetes continua por confirmar.

Nota sobre o item 5: o adicional de transferência **entrou** no inventário de parâmetros
negociáveis (`pn.transferencia.adicional` e `pn.transferencia.base`, vindos da § 18 do
adendo), mas isso cobre só a negociabilidade — o efeito da Reforma sobre o instituto segue
não pesquisado.

---

## 18. Pendências de dados sobre a Gasmig e seus instrumentos

**Status: aberta.** Consolidação da § 12 de `02-base-normativa-verbas.md`. Sem estes dados a
camada de norma coletiva funciona, mas resolve contra uma fixture parcial e um rótulo de
categoria inventado para esta extração.

| # | Dado | Efeito no motor |
|---|---|---|
| 1 | **Série histórica de ACTs** de todos os sindicatos que representam empregados da Gasmig, desde pelo menos 2012 | Sem a série, competências anteriores a 2025 caem no default legal. SITRAMICO/MG é o sindicato-base por atividade-fim; **SAEMG e Senge-MG negociam instrumentos paralelos** — é exatamente a hipótese de conflito normativo que o resolvedor detecta e não arbitra. Só o ACT 2025/2027 do SITRAMICO foi obtido |
| 2 | **Mapa de categoria por sindicato** | É a chave de resolução. Enquanto faltar, `gasmig-sitramico` é rótulo desta extração (§ 15.2 d) |
| 3 | **IP 10.5 (PCCR) e demais Instruções de Pessoal** referenciadas no ACT | Definem gratificações que integram base — provável origem da gratificação de sala de controle (§ 15.2 f) |
| 4 | **Existência de empregados enquadrados como eletricitários** contratados antes da Lei 12.740/2012 | Aciona a variante do `pn.periculosidade.base` sustentada na Súmula 191, II (§ 7 da base). Sem saber se existem, a variante fica cadastrada e nunca usada |


---

## 19. Camada de regime temporal — lacunas do bloco 6

**Status: aberta.** A camada existe (`presets-regime.md`, 26 regimes, catorze eixos
de corte). O que falta é fundamento, não modelagem.

### 19.1 Eixo de corte não declarado — a maior

**Dezesseis marcas de Fase 4** — nove em `bloco-03-verbas.md` § 8, sete em
`bloco-04-verbas2.md` § 12 — trazem a data de corte sem declarar qual data governa.
(Uma exceção: a F6 do bloco 03, gorjetas, é da Lei 13.419/2017, não da 13.467.)

Cinco regimes ficaram **inaplicáveis** por falta de eixo, e outros cinco resolvem
com eixo **inferido** — o corpus sustenta o eixo para uma pergunta vizinha, não
para a seleção da variante. Os cinco inaplicáveis:

| Regime | Corte | O que falta |
|---|---|---|
| `pr.tema1046-validade-clausula` | 02/06/2022 | se cláusula anterior se julga pelo Tema 1046 ou pelos Temas 357/762 |
| `pr.insalubridade-base-sumula228` | abril/2018 | se a cassação da Súmula 228 alcança competências pretéritas |
| `pr.he-adicional-cf88` | 05/10/1988 | o eixo, **e** a disjunção 20% × 25% |
| `pr.multa477-documentos` | 11/11/2017 | o eixo (presumível data da rescisão; o texto não diz) |
| `pr.sumula17-salario-profissional` | 2003 | o eixo e o alcance da restauração |

As marcas F de `bloco-03-verbas.md` § 8 e `bloco-04-verbas2.md` § 12 herdam o eixo
de `pr.intertemporal`. **Todo o corte de 11/11/2017 está parado nesse único ponto
de decisão jurídica.**

Supor o eixo é a forma mais silenciosa de errar: o resultado sai plausível e a
conta inteira fica no regime errado.

### 19.2 Tema 1046 — governa os 32 parâmetros negociáveis

`pr.tema1046-validade-clausula` tem `afeta_parametros: ["TODOS"]`. Ele decide se uma
cláusula que limita direito **vale** — logo, governa a resolução do catálogo de
parâmetros inteiro. Enquanto o eixo faltar, nenhum parâmetro é consultável sem que o
bloqueio fique registrado. É a maior dependência entre as duas camadas.

### 19.3 Prescrição quinquenal e bienal — ausente do corpus

**Não há regra geral de prescrição trabalhista em lugar nenhum dos arquivos
varridos.** O art. 7º, XXIX, da CF aparece só obliquamente: OJ 415 e o "período
imprescrito", Súmula 206, Súmula 362 do FGTS, OJ 83. **Nenhum eixo de ajuizamento é
declarado em ponto algum.**

É desconfortável: o eixo mais usado na prática trabalhista — a data do ajuizamento,
que fixa o marco quinquenal — é justamente o que o corpus não tem. Não foi suposto.

### 19.4 Demais

| # | Pendência | Efeito |
|---|---|---|
| a | Séries dos planos econômicos — IPC, URP, IRSM, FAS, FAZ, IPC-r, FRS | `pr.planos-economicos` está `bloqueado`: regime sem série. É a P19 do bloco 04 |
| b | Contribuição sindical antes e depois da Reforma | Capítulo 12 do manual (p. 299–302), fora dos blocos 1–4. Regime real, não modelado |
| c | Critério de arredondamento da conversão URV (P2 do bloco 02) | `pr.urv-conversao` resolve o regime, não a aritmética |
| d | Sete dúvidas de concorrência não sustentada | `extracao/bloco-06-relatorio.md` § 6 — OJ 16 das Turmas, Memo. Circular 10/2011 × NT 184/12, Súmula 146/OJ 93, rol de feriados, Lei 8.923/94, três redações da Súmula 362, Tema Repetitivo 17 |

### 19.5 A data que o corpus não tem

`pr.periculosidade-eletricitarios` corta pela Lei 12.740/2012, e o corpus diz só
isso — **sem dia e sem mês**. A data não foi suposta: o corte é `2012`, e admissão
ocorrida em 2012 **não resolve**. Obter a data exata da lei fecha o vão.

### 19.6 Um cuidado herdado do bloco 5

O bloco 5 removeu a variante `salario-basico` de `pn.insalubridade.base`. Foi
correto **como parâmetro** — não é mais opção negociável. Mas se a cassação da
Súmula 228 não retroage, competências anteriores a abril/2018 podem segui-la, e
então ela precisa voltar **como variante de regime**. É o que a § 19.1 impede
decidir.


---

## 20. Capítulo 10 e consolidação — blocos 11A a 12

**Status: parcialmente fechada.** A amortização está extraída e R10 respondida; sobram
dois bloqueios aritméticos e uma pendência de fundamento.

### 20.1 FECHADAS pelo bloco 12

| # | O que era | Como fechou |
|---|---|---|
| **R10 sem lastro** | A invariante afirmava que cível e trabalhista tratam imputação por regras não unificáveis, **sem a regra trabalhista extraída** | O bloco 11B extraiu: é **proporcional**, item 10.3.1 letra F. E **sem fundamento normativo** — `art. 354` tem zero ocorrências nas 471 páginas. R10 gravada em `00-base-normativa.md` § 7 |
| **Atrito rateio × modulação** (11B § 9) | Marcado como "maior atrito do projeto" | **Condicional, não estrutural.** O item "i" tem duas situações — `00-base-normativa.md` § 1.1. Em i.1 não há o que ratear; em i.2 o rateio se aplica sobre valores recalculados |
| **R23 sem invariante** | O "descarregar" era praticado e não normatizado | **R23** criada, com a anomalia de localização registrada: quem a fundamenta é a minuta da p. 328, capítulo 16 |
| **R4 sem exceção nomeada** | "Juros de mora sempre simples" — e há quatro anos de juros compostos | **R4-EXCEÇÃO** gravada **dentro** do invariante: DL 2.322/87, de 27/02/1987 a 03/03/1991 |
| **Páginas sem decisão** | 14 pp. (caps. 8, 12, 14) + 27 pp. (cap. 16) sem destino | **Zero.** Todas ao bloco 13. O cap. 16 reclassificado para **fonte normativa** |
| **P11B-05** gross-up invertido | Suspeita de regra oculta | Fecha exato com o denominador correto; não reaparece no segmento D. **Defeito de publicação da fórmula**, catalogado em `armadilhas-comparador.md` A7 |
| **Pendência herdada do 11A** (delta 0,44) | Regra usada e não declarada | **Não reaparece** no segmento C nem no D. O único delta próximo (0,45) dissolve-se com os operandos reais |

### 20.2 BLOQUEIOS — abertos, e não contornados

| # | Onde | Erro | Por que é bloqueio |
|---|---|---|---|
| **P11B-01** | `pagina_pdf` 266, Ex. 4 | total `43.077,24` contra `43.088,23` | Coluna K erra **10,00 exatos**; para fechar seria preciso um H que não sai de operação alguma. Dois desvios independentes na mesma linha |
| **P10D-01** | `pagina_pdf` 269 e 271, Ex. 5 letra I | total `154.874,90` contra `156.911,41`, delta de `2.036,51` na linha | Índice implícito `1,00257222` **sem origem**; `55.236,01` não existe em nenhuma das 471 páginas — não é cópia, não é transposição |

Ambos em `armadilhas-comparador.md`, §§ A3 e A2.

### 20.3 Regras ocultas — usadas e não declaradas

| # | O que |
|---|---|
| **P11B-02** | Arredondamento do **NMP**: `17,16303 → 17,2` e `10,788 → 10,8`. Uma casa, half-up — **inferido**. No segmento D nem a nota sobre "regra de arredondamento" existe |
| **P11B-03** | Percentual **pleno** de IR no saldo contra `0,9091` no levantamento, no mesmo exemplo |
| **P11B-04** | Base de IR do saldo: bruto **com** juros no Ex. 1, principal **sem** juros nos Ex. 2–4. No segmento D a divergência é **instanciada com causa declarada** (OJ 400), não resolvida |

### 20.4 Fundamento ausente — a que mais pesa

**P11B-07 — o critério proporcional não tem fundamento normativo declarado.** Aplicado 101
vezes no segmento e fundamentado zero. Entrou como preset `pr.imputacao`, **sem default** —
quinto caso de `R20-EXCECAO`, e o único em que o problema não é o corpus deixar a questão
aberta, mas **a prática não ter norma e a norma não ter prática**.

**P10D-04 — a obrigatoriedade do critério alternativo da letra C não tem lastro
demonstrativo.** A moldura declara que sob juros vincendos o segundo critério "é obrigatório",
e o manual atravessa 69 páginas sem um caso em que o primeiro erre. Pior: o critério 1 é
**inexecutável a partir do publicado** (nenhum exemplo informa data de ajuizamento nem
percentual acumulado), e sob a única reconstrução possível os dois dão **delta 0,00**.

### 20.5 Demais pendências abertas dos blocos 11A a 11C

| # | Pendência |
|---|---|
| **P11A-02** | `2.820,40` e `5.109,98` (p. 215) não reproduzem por via declarada alguma — delta 0,44 |
| **P11A-04** | Dois valores simultâneos do mesmo INSS: `649,83` para deduzir, `906,64` para recolher |
| **P11A-05** | Método agregado de juros vincendos de 10.1 × método linha a linha do cap. 7 — equivalentes só sob acréscimo uniforme |
| **P11B-06** | O segmento C adota a dedução na data do levantamento **sem citar** a Súmula 15/TRT-3 nem o 16.4.11, que reconhece **duas** teses |
| **P10D-02** | Centavo perdido no rateio do Ex. 6 (`5.057,47` onde o correto é `5.057,48`); o `J` é construído sobre o valor errado |
| **P10D-03** | `11.731,57` × `11.731,37` na mesma página, com a letra B imprimindo o errado |
| **P10D-05** | A alternativa da **letra I** não tem exemplo em lugar nenhum do capítulo 10 |
| **P10D-06** | Os `251,02` rotulados "juros vincendos" no Ex. 6 são juros **vencidos** |
| **P10D-07** | Enquadramento no art. **12-B** é paráfrase: a string não ocorre no segmento |
| **P10D-08** | Migração de regime tributário dentro do mesmo cálculo (Ex. 5) — caso único do manual, sem enunciado |
| **P10-C16** | Varredura dirigida do capítulo 16 — **prioridade alta**, após a reclassificação para fonte normativa |
| **P10-18** | Base das custas de execução: cap. 11 diverge do cap. 9. O cap. 8 é onde a regra deveria estar |

### 20.6 Pendência de origem — declarada

**A subseção § 1.1 de `00-base-normativa.md` vem de pesquisa jurisprudencial externa ao
corpus**, conferida em fontes secundárias que reproduzem a fundamentação. **O inteiro teor dos
três precedentes do TST não foi lido.** Declarado nos mesmos termos do art. 611-B da CLT no
bloco 5.

Confirmar contra o inteiro teor antes de usar em produção — a distinção i.1 × i.2 decide se o
critério do STF alcança ou não valores já pagos, e é o que sustenta o preset
`pr.adc58-item-i`.

---

## 21. Bloco 13 — fechamento da extração

**Status: a extração está encerrada.** Os dois manuais têm destino registrado em todas as
564 páginas. O que resta não se fecha lendo os PDFs.

### 21.1 FECHADAS pelo bloco 13

| # | Como fechou |
|---|---|
| **P11B-02** — arredondamento do NMP | **A regra É declarada**, pp. 226 e 230: *"parágrafo único do 45 da IN 1500/14"*, com o artigo transcrito. **Não é half-up** — três ramos, e `=5` manda olhar a 3ª casa. Difere de `ROUND_HALF_UP` em `x,y50`–`x,y54`. Minha afirmação anterior era negativa não verificada |
| **P11B-03** — percentual pleno × `0,9091` | **Erro meu de leitura.** `0,9091` é o **IPIR**, índice das parcelas passíveis de IR. O contraste não existe |
| **P10D-07** — art. 12-B por paráfrase | **Resolvida.** A string está nas pp. 224 e 233, com hipótese de incidência literal. Sob 12-B **não há NM** |
| **P10-18** — base das custas de execução | **Reclassificada.** A causa é o **juro Selic sobre a cota-reclamante** (35,29), não bruto × líquido. Vira defeito de rótulo — A12. Resta o estado da base, que o cap. 8 define **só por exclusão** |
| **P10-C16** — varredura do cap. 16 | **Feita.** 39 achados, 36 fundamentos cruzados, **seis exclusivos do capítulo 16** |

### 21.2 NOVAS — e a primeira bloqueia uma pendência antiga

| # | Pendência |
|---|---|
| **P13B-02** | **O manual se contradiz sobre Fazenda Pública.** Cap. 8, p. 102: isentos os entes públicos *"que não explorem atividade econômica"* (art. 790-A). Cap. 14, p. 306: isentos os órgãos da administração *"direta e indireta"*, **sem a ressalva**. Dois testes incompatíveis. **Consequência: o manual NÃO pode fechar a pendência 1 da § 9.** `economia mista` = 0 ocorrências nas 471 páginas |
| **P8-F4-02** | **As faixas do art. 85, § 3º, do CPC não existem no repositório.** Busca em toda a árvore `docs/` por `200 salários`, `1.000 salários`, `2.000 salários`, `20.000 salários`, `100.000 salários` → **zero**. Só existe a regra de progressividade (`bloco-08-jf.md`, R-08-21). Sem elas, a marcação de Fase 4 do art. 791-A não tem contra o que ser confrontada |
| **P13A-01** | Fórmula do bruto levantado com **colchete fechado cedo demais**, pp. 227 e 231; **propaga para 244 e 250**. Delta 3.771,73. Armadilha A11 |
| **P13A-02** | O capítulo 10 aplica **dois critérios de rateio** (principal×juros em 10.3; bruto→INSS em 10.2) e **não fundamenta nenhum** |
| **P13A-03** | `OJ 400` ausente do segmento B: a escolha entre base de IR **com** e **sem** juros é bifurcação declarada, **sem regra de escolha** |
| **P13A-05** | Divergência de citação da IN 1500/14: 10.2.2 cita "arts. 26, **44 e 45**"; 9.3.8 cita "arts. 26, **43** e 44". O art. 45 é **inaplicável ao 12-B** |
| **P13C-01** | **Três posições no mesmo manual** sobre a data da dedução: cap. 10 usa **levantamento** sem fundamento; 16.4.11 dá **duas teses** separadas pela finalidade do depósito; cap. 14, p. 306, manda **data do pagamento** |
| **P13E-01** | **IN SRF 15/2001** — fonte declarada da fórmula de *gross-up* — tem **uma única ocorrência em 471 páginas**, no cap. 16. O cap. 10 usa a fórmula em todos os exemplos e nunca diz de onde vem |
| **P13B-04** | Juros sobre honorários periciais: quatro acórdãos em cada sentido. **Duas variantes com fundamento** |

### 21.3 Correções de registro feitas no bloco 13

Afirmações de blocos anteriores que a extração final derrubou, todas minhas:

- **16.4.11 está nas pp. 333–334**, não na 335 (bloco 12);
- **16.4.7 não é caso de "fundamenta só na minuta"** — o cap. 6, p. 77, enuncia a regra com o
  texto **íntegro** da OJ 54, melhor que a minuta (bloco 12);
- **`anatocismo` não é exclusivo do cap. 16** — pp. 16, 90, 328 e 335. Exclusiva é a
  **aplicação do conceito à amortização** (bloco 12);
- **o capítulo técnico do FGTS cita a OJ 302** — cap. 6, p. 79, com transcrição;
- **o manual CJF não tem "93 páginas integrais"** — os capítulos são 80; 13 são pré-textuais,
  das quais 3 têm conteúdo normativo e estão cobertas (bloco 8).

### 21.4 O que permanece aberto e não se fecha por extração

- **P11B-01** e **P10D-01** — os dois bloqueios aritméticos, nenhum absorvível por
  arredondamento;
- **P11B-07** — o critério de imputação sem norma, modelado como `pr.imputacao` sem default;
- **P10D-04** — obrigatoriedade do critério alternativo da letra C, declarada e não
  demonstrada;
- **P10D-08** — migração de regime tributário dentro do mesmo cálculo, sem disciplina em todo
  o manual;
- **§ 20.6** — a origem externa da subseção § 1.1 da base normativa: o inteiro teor dos três
  precedentes do TST **não foi lido**.

---

## 22. Bloco 14 — Fase 4, confronto normativo

**Status: a auditoria está feita.** 50 vereditos, zero `SEM FONTE`. O que resta são decisões
de modelagem, não de pesquisa.

### 22.1 FECHADAS pelo bloco 14

| # | Como fechou |
|---|---|
| **P8-F4-02** — faixas do art. 85, § 3º, do CPC | **Transcritas de fonte primária** (acórdão do STJ). Três consequências: unidade é salário-mínimo; a **data** é a do § 4º, IV — sentença líquida ou decisão de liquidação, **não o ajuizamento**; e o percentual é **entrada arbitrada**, não saída calculada |
| **Súmula 48 do TRT-3** | Confirmada **cancelada** no portal oficial do TRT-3 — o que **não contradiz** o bloco 10: o manual de 2016 não a invoca (zero ocorrências em 471 páginas) e ela existe e foi cancelada. Duas afirmações distintas, ambas verdadeiras |
| **Súmula 124 do TST** | **Sobreviveu** ao expurgo da Res. 225/2025 — conferido contra os 27 incisos. Permanece na redação da Res. 219/2017. `pr.sumula124-divisor-bancario` segue válido |

### 22.2 DECISÕES para o bloco 15 — não são pesquisa

| # | Decisão |
|---|---|
| **D15-01** | **`pr.intertemporal` continua sem default?** O **Tema 23 do TST** (Pleno, 25/11/2024, 15×10, vinculante, modulação negada) fixou *tempus regit actum* com eixo na **competência do fato gerador**. A Corrente B da base é a posição dos dez vencidos. Se ganhar default, **os 17 pontos do corte de 11/11/2017 destravam** e `R20-EXCECAO` cai de cinco para quatro |
| **D15-02** | **Corrigir a colisão `F*`** — `F1`–`F9` do bloco 03 e `F1`–`F7` do bloco 04 são pontos diferentes com os mesmos rótulos, e há remissões cruzadas já ambíguas nos arquivos |
| **D15-03** | **Registrar os cancelamentos da Res. 225/2025 com as datas de perda de eficácia**, não como revogação simples. São 27 súmulas com data pretérita declarada |
| **D15-04** | **Implementar os cortes por data, não por ponto** — 17 pontos compartilham 11/11/2017 |
| **D15-05** | **Inverter a numeração das fases** em `01-plano-extracao.md`: o confronto vem antes da consolidação |

### 22.3 ERROS DE FATO na base — confirmados, não corrigidos

| # | Erro |
|---|---|
| **E14-01** | **O art. 58, § 2º, da CLT NÃO foi revogado** — teve redação alterada. Revogado foi o **§ 3º**. A base cita o dispositivo errado como fonte de um parâmetro negociável (`02-base-normativa-verbas.md` §§ 3 e 10) |
| **E14-02** | **A base invoca como vigentes verbetes cancelados** — Súmulas 90, 423 e 437, canceladas em 30/06/2025 com perda de eficácia pretérita. A **423** é a mais grave: sustenta o turno de revezamento e perdeu eficácia em **14/06/2022** pelo Tema 1046 |
| **E14-03** | **Divergência de atribuição na Súmula 228** — a base atribui a cassação à **Rcl 6.275** (abril/2018); a Res. 225/2025 do TST atribui à **Rcl 6266**, "a partir da publicação em 18/04/2018". Mesma data, reclamação diferente. **Não resolvido** |
| **E14-04** | **Erro de linguagem propagado** — `bloco-05-relatorio.md`, `bloco-06-relatorio.md` e `parametros-negociaveis.md` dizem *"a Rcl 6.275 foi cassada"*. Uma reclamação não é cassada: **a súmula é que foi cassada pela reclamação** |
| **E14-05** | **Atribuição incorreta no manual, reproduzida sem ressalva** — o manual diz que comissões integram *"pela média dos últimos doze meses (art. 457, § 1º)"*. **O art. 457, § 1º não contém essa regra**, nem antes nem depois da Reforma |

**Já corrigido:** a afirmação de que a EC 113/2021 alcançaria "apenas requisitórios federais"
(`bloco-13c` § 7). Era **erro meu de extração**, não da base — a restrição é da EC 136/2025.

### 22.4 As 19 suspeitas, e a natureza delas

Íntegra em `confronto-normativo/03-suspeitas-base.md`. **A maioria não é erro de mérito — é
desatualização de rastro:** a base acertou o direito aplicável e não registrou o ato formal
posterior.

### 22.5 Limites de acesso — valem para as próximas fases

**Recusaram acesso automatizado a sessão inteira:** Planalto, DOU, Receita Federal,
`portal.stf.jus.br`, Legin da Câmara.

**Consequências declaradas:**
- a **modulação da ADC 58 continua sem transcrição literal**;
- o de-para **RIR/99 → RIR/2018** não foi feito;
- **nenhum inteiro teor** de Rcl 6.275, 6.266 ou 53.157 foi lido.

**Canais que funcionaram:** `portal.trt3.jus.br` (hospeda acórdãos do STF), `stj.jus.br`,
`juslaboris.tst.jus.br`.

**E um alerta:** **as fichas de tema do TST não servem como fonte.** A do **Tema 9** omite a
modulação; a do **Tema 23** está com "Tese Firmada" em branco e situação "Afetado", cache
anterior ao julgamento. Usar os **acórdãos publicados**.
