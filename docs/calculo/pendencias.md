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
do caso 6 saiu da suíte, e **nenhum teste do repositório é pulado**. A contagem da suíte não se
escreve aqui: `consolidado/00-numeros.md` § 5.

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
| **D15-03** | **Registrar os cancelamentos da Res. 225/2025 com as datas de perda de eficácia**, não como revogação simples. São 27 súmulas com data pretérita declarada |
| **D15-04** | **Implementar os cortes por data, não por ponto** — 17 pontos compartilham 11/11/2017 |
| **D15-05** | **Inverter a numeração das fases** em `01-plano-extracao.md`: o confronto vem antes da consolidação |

**D15-01 e D15-02 saíram desta tabela — foram decididas. Ver § 22.2.1.**

### 22.2.1 DECIDIDAS no bloco 15 — referência 2026-09-20

| # | Decisão |
|---|---|
| **D15-01** — *"`pr.intertemporal` continua sem default?"* | **DECIDIDA: ganhou default.** É `tempus-regit-actum`, eixo na **competência do fato gerador**, por força do **Tema 23 do TST** (IRR, Pleno, 25/11/2024, 15×10, transitado, modulação negada por unanimidade). A **ultratividade** — a Corrente B da base, posição dos dez vencidos — permanece como variante aplicável **mediante justificativa** (R21) ou a título que a tenha adotado expressamente (R8). Consequências: **o corte de 11/11/2017 destravou** e **`R20-EXCECAO` caiu de cinco para quatro casos** (`presets-regime.md` § 3, § 7.4 e § 8.1; `consolidado/05-imputacao.md` § 3, que já trata `pr.imputacao` como o **quarto**) |
| **D15-02** — colisão `F1`–`F9` × `F1`–`F7` | **DECIDIDA: prefixo por bloco**, `B03-` e `B04-`. Aplicado nas **espinhas** (`bloco-03-verbas.md` § 8, `bloco-04-verbas2.md` § 12) e nos **detalhes**. **Ressalva do bloco 14:** seguia **não aplicada nos dois relatórios** — `bloco-03-relatorio.md` e `bloco-04-relatorio.md` —, onde `F1` significava "base de cálculo" num e "horas *in itinere*" no outro. Os dois relatórios foram renumerados em **2026-09-20**, cada um com a nota `> **RENUMERADO NO BLOCO 15.**` no topo |

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

---

## 23. Bloco 17 — o tipo do indexador (R3) sem fonte

**Status: aberta.** O campo passou a existir: `tipo_indexador` em **97 segmentos** de **11
cadeias**, catálogo único em `tabelas-normativas/indexadores-tipo-catalogo.json`, invariante
R3 cobrada por `scripts/calculo/valida_cobertura.py`. O que não existe é **fonte para metade
do catálogo**.

**A fonte é estreita e exemplificativa.** O item 4.1.2.4 do Manual CJF (`pagina_pdf` 42)
nomeia **quatro** nominais — Ufir, BTN, OTN, ORTN — e **três** percentuais — INPC, IGP-DI,
IGP-M — todos sob "Ex.:". Lista exemplificativa **não autoriza extensão por semelhança de
nome**: `tipo` sai da fonte, nunca de dedução. O que falta fica `indeterminado`.

### 23.1 P17-01 — nove índices sem classificação em fonte alguma

| Índice | Onde aparece | Por que não foi classificado |
|---|---|---|
| **IPCA-E/IBGE** | condenatórias, desapropriação direta (2001-01..2021-11) | **Não está na lista.** O item 4.1.2.4 **não nomeia sequer "IPCA"**. Chamá-lo percentual "porque IPCA é percentual" é a dedução proibida — duas vezes |
| **IPCA-15/IBGE** | condenatórias (2024-09..), desapropriação (2025-09..) | Mesma razão. É a **prévia de 15 dias**, índice distinto dos outros dois |
| **IPCA série especial** | condenatórias e repetição, dez/1991 | Zero ocorrências do nome em janela de classificação, em todo o corpus |
| **IPC/FGV** | desapropriação direta, mar–dez/1991 | **D8-C21 sustenta o IPC/IBGE, não o IPC/FGV.** Emissor distinto, índice distinto. Herdar do homônimo é a mesma classe de erro que o bloco 8 cometeu ao trocar um pelo outro em 78 segmentos |
| **IPC-R** | previdenciário, 1994-07..1995-06 | Não está na lista |
| **IRSM** | previdenciário, 1993-01..1994-02 | Não está na lista |
| **MVR** | `serie-18.11-otn-btn-mvr.csv` | Não está na lista, e **nenhuma cadeia do repositório o consome** |
| **`Ufir → Selic (bifurcado por fato gerador)`** | dívida fiscal, 1992-01..2026-06 | **P17-03**, abaixo — é segmento composto, não índice |
| **`NAO-DECLARADO-PELO-MANUAL`** | correção trabalhista, 1942-11..2009-06 | O índice em si não é declarado. É a **P9-02**, não novidade deste bloco |

**IPC-R e IRSM tinham quase-fonte, e ela não servia.** `previdenciario.md` escrevia *"INPC,
IRSM, IPC-R, IGP-DI são percentuais"* — **sem item, sem `pagina_pdf`, sem nada**. Documento
derivado, e o que ele derivava era exatamente a dedução por nome. **Não foi usada como fonte.**

> **Corrigido ainda no bloco 17**, junto com as demais propagações que a validação adversarial
> achou: `indices-judiciais/SKILL.md`, `calculo-judicial-atualizacao/SKILL.md`,
> `calculo-judicial-core/SKILL.md`, `civel-federal.md`, `consolidado/01-dominio-e-invariantes.md`
> e `consolidado/02-atualizacao.md` afirmavam *"percentual (INPC, **IPCA**, IGP)"* **citando o
> item 4.1.2.4 — que não nomeia IPCA**.
>
> **Permanece divergente, e não foi corrigida:** a **§ 7 de `00-base-normativa.md`** enuncia R3
> com a mesma lista. **É fonte de verdade do usuário**, e este bloco não altera conteúdo
> normativo. Mesmo caso em `03-casos-dificeis.md`.

**Escopo da busca, declarado:** varredura de `docs/`, `skills/`, `scripts/` e `tests/` em
`.md`, `.json`, `.csv` e `.py`, tomando toda linha que contenha o nome do índice e, na janela
de ±3 linhas, qualquer de *nominal*, *nominais*, *percentual*, *percentuais*. Nenhuma
ocorrência atribui tipo com citação de fonte primária.

**Como fechar:** o item 4.1.2.4 é a única regra do gênero nos dois manuais. Fecha-se com o
ato de instituição de cada índice — ou com decisão do usuário de que a extensão da lista é
admissível e sob que critério. **Não se fecha lendo os PDFs de novo.**

### 23.2 P17-02 — a TR foi REBAIXADA de `percentual` para `indeterminado`

`trab.hist.correcao-monetaria.json` gravava `tipo_indexador: "percentual"` para a
TR e para a "remuneração básica da caderneta de poupança (TR)", **com a inferência declarada
no próprio JSON** e detalhada em `bloco-09-cadeias-historicas.md` § 3.3 e
`bloco-09-relatorio.md` § 5.3. O critério era **formal**: *"a TR não é unidade monetária, logo
é percentual"*.

**O bloco 17 rebaixa para `indeterminado`,** e o fundamento do rebaixamento está nos próprios
textos que criaram o rótulo:

- *"**Nenhum dos dois manuais classifica a TR**"* — `bloco-09-relatorio.md` § 5.3, literal;
- o critério **material** do item 4.1.2.4 — *"refletem a inflação do próprio mês"* — **não se
  aplica**: a TR não é índice de preços, é taxa apurada **prospectivamente** (art. 12, I, da
  Lei 8.177/91);
- **inferência declarada não é fonte.** A regra deste bloco não admite exceção por honestidade
  da inferência: *"índice cuja classificação não esteja sustentada em fonte fica como
  `tipo: indeterminado`"*.

**O que se perde:** um rótulo que nunca teve lastro. **O que se ganha:** a virada para a TR
passa a aparecer no validador, como `R3-INDETERMINADO`, em vez de passar limpa.

**Alcança também** `serie-18.15-tabela-unica-trabalhista.csv`, cuja base é a TR.

### 23.3 P17-03 — segmento composto na dívida fiscal

`cjf.divida-fiscal.correcao-monetaria.json`, `1992-01..2026-06`, grava um **único** segmento
com `indexador: "Ufir → Selic (bifurcado por fato gerador)"`. São **dois** indexadores, de
tipos diferentes — Ufir é `nominal`, Selic é `percentual` — num registro só. Nenhum rótulo
único os representa, e escolher um deles seria inventar.

**A correção é partir o segmento pelo eixo `data-do-fato-gerador`**, não classificá-lo. Isso
é mudança de modelagem da cadeia, e não foi feita aqui: este bloco corrige o campo `tipo`, não
o recorte dos segmentos. Enquanto isso, fica `indeterminado` — e, como a dívida fiscal não
tem outra virada, o validador não acusa nada ali.

### 23.4 O que o validador passou a ver — 25 achados, todos do manual

`python scripts/calculo/valida_cadeias.py` sobre as 11 cadeias:

| Regra | Achados | O que são |
|---|---|---|
| **R3** (virada confirmada, sem `aplicacao`) | **12** | Três viradas × quatro cadeias do CJF: `OTN→IPC/IBGE` (jan/1989), `IPC/IBGE→BTN` (mar/1989), `BTN→IPC/IBGE` (mar/1990) |
| **R3-INDETERMINADO** | **13** | Viradas com ponta sem classificação — P17-01 e P17-02 |

**As 12 confirmadas corroboram D8-C21.** O manual explica a colisão de **jan/1989** pelo
argumento dos nominais (item 2.3.1.3, R-08-04) — mas OTN→IPC/IBGE **não é** nominal→nominal, é
nominal→**percentual**, e o argumento não a alcança. É exatamente o que D8-C21 já dizia sobre
mar/1990, agora medido por script e estendido a jan/1989. **Nenhuma foi harmonizada**: são do
manual, e a regra do projeto é registrar.

**A defasagem do expurgo não está declarada em lugar nenhum.** Se as três viradas exigem ou
não ajuste, o manual não diz; ele nem sequer as reconhece como viradas de tipo. Enquanto
`aplicacao` não for preenchido com fundamento, elas permanecem acusadas — e devem permanecer.

### 23.5 Onde a fonte não bastou, em uma linha

**15 dos 97 segmentos**, e **10 dos 27 indexadores nomeados** (mais o **MVR**, que só existe
em série CSV), ficaram `indeterminado`. A
proporção não é defeito da extração: é o tamanho real da lacuna que R3 vinha escondendo por
não ter campo onde aparecer.

---

## 24. Bloco 18 — FGTS (item 4.8) e poupança (item 4.9) do Manual CJF

Consolidados em `consolidado/02-atualizacao.md` § 5 e `02-atualizacao-detalhe.md` §§ 5.0 e
5.3.2–5.3.5. Quatro JSON novos em `tabelas-normativas/`: `cjf.fgts.correcao-monetaria` (11
segmentos), `cjf.fgts.juros-mora` (3), `cjf.poupanca.correcao-monetaria` (12) e
`cjf.poupanca.juros-mora` (3). Gerador: `scripts/calculo/gera_cadeias_bloco18.py`.

### 24.1 `N-5` / `D8-C13` — continua ABERTA, e não se resolve aqui

Item 4.8.1.1, NOTA 2, `pagina_pdf` 82: *"a liquidação deve incluir os expurgos inflacionários
reconhecidos pelo STJ em casos de FGTS: **42,72% em jan./1989 e 44,80% em abr./1990**"*.

**Substitui ou acresce? O manual não diz.** No capítulo 4 geral a operação é declarada — *"Expurgo,
em substituição ao BTN"*, e o item 4.1.2.1 manda *"descontando o BTN ou outro índice utilizado,
evitando bis in idem"*. No FGTS a nota apenas manda **incluir**, sobre linhas que **já trazem
indexador** (`LFT – 0,5%` em jan/1989; `BTN` em abr/1990), e a tabela **não menciona expurgo algum**.

**Consequência de modelagem:** os dois percentuais **não foram gravados como segmento**. Gravá-los
exigiria escolher entre substituir e somar — o que é resolver a pendência por dedução.

E o conjunto do FGTS **não é o do capítulo 4**: lá são 42,72% (jan/1989) e **10,14%** (fev/1989);
aqui, 42,72% (jan/1989) e **44,80%** (abr/1990). **`D8-C14`** acrescenta a bifurcação contraintuitiva:
quem **discute** expurgos só recebe *"os períodos definidos pelo julgado"* (NOTA 1); quem **não
discute** recebe os dois por padrão (NOTA 2).

### 24.2 `P18-01` — sete rótulos de indexador sem classificação em fonte alguma

| Rótulo | Onde | Por que `indeterminado` |
|---|---|---|
| **`JAM`** | 4.8, `pagina_pdf` 81 | **não é indexador** — é o nome do critério (*"Juros e Atualização Monetária"*). Registrado porque circula como se fosse |
| **`UPC`** | poupança, 1967-05..1983-06 | não está no item 4.1.2.4. O item 2.4.4.1 só **expande a sigla** — rotulagem, não classificação |
| **`LBC`** | FGTS 1987-02; poupança 1987-02..1987-06 | não está no item 4.1.2.4; nada no corpus |
| **`LBC – 0,5%`** | ambas, 1987-07..1987-09 | idem, e o rótulo embute um redutor de 0,5% não explicado |
| **`LFT – 0,5%`** | ambas, 1989-01..1989-04 | idem. É a linha do expurgo de 42,72% (`N-5`) |
| **`TRD`** | ambas, 1991-02..1993-04 | **NÃO segue a TR** — a herança foi desfeita no bloco 19 (§ 25.3): a fonte do BCB nomeia TBF, Redutor-R e TR, **não** a TRD. As únicas ocorrências no corpus são o texto `nao-indexador` de segmentos de **juros**, que não classifica a TRD como índice de correção |
| **`IPC`** (nu) | FGTS, duas janelas | `D8-C21` sustenta o **`IPC/IBGE`**, não o `IPC` sem emissor — e o manual usa **dois** IPC (IBGE e FGV, item 4.5.1.1). A poupança escreve `IPC/IBGE` nos **mesmos meses** |

**Escopo da busca de ausência declarado** em `tabelas-normativas/indexadores-tipo-catalogo.json`,
chave `ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_18`: árvores `docs/`, `skills/`, `scripts/`, `tests/`;
extensões `.md`, `.json`, `.csv`, `.py`; critério = linha com o termo **e** vocabulário de tipo.
Mais a releitura integral do PDF nas `pagina_pdf` **81–87** e **35–36**. **Zero ocorrências
classificatórias.**

**Efeito medido:** **19 violações `R3-INDETERMINADO`** novas. Não são defeito do manual nem da
modelagem — são esta pendência tornada visível. Classificar por dedução as faria sumir, **e a dedução
passaria limpa**.

### 24.3 `P18-02` — eram oito cadeias tabuladas sem JSON; **são TRÊS**

> **ATUALIZADO NA TAREFA 3 DO BLOCO 19.** Das oito, **cinco foram geradas**: 4.5.3 e 4.6.3
> (`cjf.desapropriacao-{direta,indireta}.juros-compensatorios`, 3 segmentos cada), **4.6.1.1**
> (`cjf.desapropriacao-indireta.correcao-monetaria`, 11, **derivada** da direta), **2.3.2.2**
> (`cjf.divida-fiscal.juros-mora`, 8, **com `base_incidencia`**) e **2.4.4.1**
> (`cjf.fgts-divida-fiscal.correcao-monetaria`, 5, critério **`JCM`**). **Seguem ausentes 4.5.2,
> 4.6.2 e 2.4.2.2.2**, e por **falta de fonte extraída**, não de schema — `02-atualizacao-detalhe.md`
> § 5.3.6. **O quadro abaixo é o do bloco 18 e fica como registro do estado anterior.**

A varredura `item × JSON × consolidado` dos caps. 2 e 4 (detalhe § 5.0) mostrou que FGTS e poupança
**não eram as únicas**:

| Item | Cadeia | Observação |
|---|---|---|
| **4.5.2** | juros de mora — desapropriação **direta** | 5 linhas; em prosa no detalhe § 5.3.1 |
| **4.5.3** | juros **compensatórios** — direta | recuperada em prosa pelo bloco 15; **segue sem JSON** |
| **4.6.1.1** | correção — desapropriação **indireta** | **idêntica à de 4.5.1.1**, inclusive no IPC/FGV |
| **4.6.2** | juros de mora — indireta | fecha em **dez/2021**; a gêmea 4.5.2 fecha em **nov/2021** |
| **4.6.3** | juros compensatórios — indireta | carrega o `N-10` (remete a *"item 4.5.2"*, da direta) |
| **2.3.2.2** | juros — dívida fiscal | exige `base_incidencia` — `D8-C5`: a base alterna **quatro vezes** |
| **2.4.2.2.2** | juros — contribuição previdenciária | idem |
| **2.4.4.1** | **FGTS fiscal**, critério **`JCM`** | **não é** a cadeia de 4.8: outro sujeito, outra sigla, outro capítulo. Lista, não tabela. `D8-C8` em aberto |

**Não geradas neste bloco**, por escopo e porque três delas exigem decisão de modelagem que não cabe
tomar de passagem. **Registradas, não silenciadas.**

**O que a tarefa 3 do bloco 19 decidiu sobre cada bloqueio herdado:**

| Bloqueio do bloco 18 | Veredito da tarefa 3 |
|---|---|
| *"2.3.2.2 e 2.4.2.2.2 precisam do campo `base_incidencia`"* | **RESOLVIDO para 2.3.2.2.** O campo é de **segmento**, é **ortogonal** a período/indexador/englobamento, e `Segmento.de_dict` ignora campos que não conhece — **R1, R2 e R3 seguem exatas e o validador não mudou**. 2.4.2.2.2 continua bloqueada, mas **por fonte** |
| *"2.4.4.1 é lista, não tabela, com o `D8-C8` em aberto"* | **GERADA assim mesmo.** Lista com períodos datados **é** cadeia; o `D8-C8` entrou como **sobreposição real de 2000-05**, que o validador agora acusa — era exatamente o que o bloco 8 dizia que a checagem *"não pega, porque estão em tabelas diferentes"* |
| 4.5.2, 4.6.2 e 2.4.2.2.2 | **BLOQUEADAS, com escopo declarado.** A tabela das três **nunca foi extraída linha a linha**. Gerar exigiria **reconstruir a estrutura** — pior do que inventar um valor. Razão gravada em `BLOQUEADAS`, de `scripts/calculo/gera_cadeias_bloco19.py`, e conferida por teste |

**`P19-02` — um rótulo novo sem classificação em fonte alguma.** **`BTNF`**, trazido pela cadeia do
FGTS fiscal (item 2.4.4.1, `pagina_pdf` 35). O item 4.1.2.4 nomeia o **BTN**, não o BTNF; herdar
*"nominal"* do quase-homônimo é a dedução que o bloco 17 proibiu, e é a mesma classe de erro de
`IPC` × `IPC/IBGE`. Entrou no catálogo como **`indeterminado`, sem fonte**. Entrou junto o rótulo
**composto** `UPC → índices básicos de atualização dos saldos da poupança`, que **não é rótulo novo
de índice**: é **segmento composto** (`P17-03`), porque o manual lista os dois indexadores e **não
data a fronteira** entre eles. **A cura é partir o segmento, não classificá-lo.**

**E uma que parecia lacuna e não é: `4.7.1`.** O manual **não tem** tabela de correção monetária
trabalhista — só lista de leis, e a NOTA 2 **delega**: *"utilizar a tabela de coeficientes
trabalhistas expedida pelo Tribunal Superior do Trabalho"*. Mesmo desenho do `P9-02`: a cadeia vive
numa **série**, não numa regra. Afirmá-la ausente seria afirmar ausência do que a fonte nunca
prometeu.

### 24.4 Baselines dos validadores, atualizados

`scripts/calculo/valida_cadeias.py` descobre cadeia por `tipo == "cadeia-temporal"`; os quatro
arquivos entraram sem alteração de código.

| | antes (bloco 17) | **depois (bloco 18)** |
|---|---|---|
| cadeias | 11 | **15** |
| **R1** | **15** | **15** — *inalterado* |
| **R2** | **1** | **1** — *inalterado* |
| **R3** | 25 | **46** (+21: **19** `R3-INDETERMINADO` + **2** `R3` cheia) |

**R1 e R2 não se moveram porque as duas cadeias novas de correção são perfeitamente contíguas** —
fim e início nunca caem no mesmo mês, ao contrário do tronco comum do capítulo 4 (jan/1989, mar/1990).

**As 2 `R3` cheias são do manual**, ambas em `cjf.poupanca.correcao-monetaria`: `1986-03` ORTN
(nominal) → IPC/IBGE (percentual) e `1990-04` IPC/IBGE (percentual) → BTN (nominal), **sem `aplicacao`
declarada**. Mesmo padrão já registrado em § 23.4. **Não harmonizadas.**

---

## 25. Bloco 19 — a terceira classe de indexador, e o erro de categoria do `englobante`

**Fonte externa ao corpus, declarada como tal.** A classificação que abre este bloco **não foi
extraída** do material deste repositório: veio do enunciado, verificada fora do agente, e está
gravada em `indexadores-tipo-catalogo.json` sob a chave `FONTE_EXTERNA_AO_CORPUS`. Duas
afirmações a compõem — do **IBGE**, que o **IPCA-15** difere do IPCA apenas no **período de
coleta** (do dia 16 de M−1 ao dia 15 de M) e que **o IPCA-E mensal das tabelas judiciais é o
IPCA-15**; e do **BCB**, que **TBF, Redutor-R e TR** são divulgados para **período entre datas
de aniversário**, não para mês calendário, e que **a TR é prefixada**. **Nenhuma busca na web
foi feita.** A § 7 de `00-base-normativa.md` **não foi alterada**.

### 25.1 `janela-deslocada` — a terceira classe COM DEFASAGEM

`nominal` reflete **M−1**, `percentual` reflete **M**, e **`janela-deslocada` reflete metade de
M−1 e metade de M**. São **três pares** de virada, não um, e a regra em `valida_cobertura.py`
**não os enumera**: exige que os dois lados estejam em `TIPOS_COM_DEFASAGEM` e sejam diferentes.

**Recebem a classe nova: `IPCA-E/IBGE` e `IPCA-15/IBGE`** — e **só** eles. A identificação entre
os dois é **da própria fonte externa**, não de semelhança de nome, e está declarada no catálogo.

### 25.2 `englobante` era um fato de R1 dentro do campo de R3 — RETIRADO

Os segmentos **sempre tiveram `engloba`**, e é ele que R1 lê. Marcar a SELIC como `englobante`
em `tipo_indexador` **a deixava cega para R3**: ela saltava toda comparação de defasagem, por
desvio explícito no validador, embora tenha defasagem. **`engloba` não foi tocado.**

| Índice | Era | É | Por quê |
|---|---|---|---|
| **SELIC** | `englobante` | **`percentual`** | A tabela externa classifica a *SELIC acumulada* como percentual. `D8-C22` (*"Selic não é índice de inflação"*) segue verdadeiro — mas *"não é índice de inflação"* **não é** *"não tem defasagem"*, e era essa a confusão |
| **taxa legal** | `englobante` | **`indeterminado`** (`P19-01`) | **A fonte externa não a alcança.** `percentual` por analogia com a SELIC é a dedução proibida, e a analogia é frágil por fonte: R11 registra a taxa legal como **derivada** por razão entre fatores, não índice publicado |

> **`P19-01` — a taxa legal não tem classificação de tipo em fonte alguma.** Escopo da busca de
> ausência em `ESCOPO_DA_BUSCA_DE_AUSENCIA_BLOCO_19`. Fecha quando chegar fonte que a alcance.

**Achado colateral, registrado e NÃO harmonizado:** dos cinco segmentos de taxa legal, **dois**
declaram `engloba: ["correcao-monetaria", "juros-mora"]` e **três** declaram só
`["juros-mora"]`. O rótulo `englobante` encobria a assimetria, porque dizia *"engloba"* onde o
`engloba` não englobava. Harmonizar exige fonte que diga qual gravação está certa, e ela não foi
localizada. Há teste que trava a contagem em três.

### 25.3 `tipo_indexador_razao` — razão NÃO é pendência

**A TR fica `indeterminado` com RAZÃO REGISTRADA** — *"período entre datas de aniversário e
prefixação"* —, **não por ausência de fonte**. Carregava `tipo_indexador_pendencia: "P17-02"`,
que afirma *"não há fonte"*; **agora há fonte, e ela diz que a TR não cabe em mês calendário**.
Manter `P17-02` passou a ser afirmação falsa sobre o estado do conhecimento.

| | campo | afirma | como fecha |
|---|---|---|---|
| **sem fonte** | `tipo_indexador_pendencia` | nenhuma fonte classifica | **quando a fonte chegar** — `P17-01`, `P18-01`, `P19-01` |
| **fonte diz que não cabe** | `tipo_indexador_razao` | há fonte, e ela diz que não cabe | **NÃO se fecha esperando fonte** |

Os dois são **mutuamente excludentes** — `Segmento.de_dict` rejeita o par —, e **os dois
bloqueiam** a virada sob `R3-INDETERMINADO`, porque o efeito sobre o cálculo é o mesmo. O que
muda é a mensagem, e é ela que diz a quem audita se vale a pena esperar. Recebem razão: **`TR`**
e **`remuneração básica da caderneta de poupança (TR)`** — esta por **rotulagem do próprio
manual**, que já escreve `(TR)` no rótulo, e não por semelhança de nome. **`TRD` NÃO recebe**: a
fonte do BCB nomeia TBF, Redutor-R e TR, e **não** a TRD; segue `P18-01`.

### 25.4 O mapeamento um a um — 36 rótulos nas 20 cadeias

Levantados **do repositório** (campo `indexador` de todo arquivo com
`tipo == "cadeia-temporal"` — **156 segmentos em 20 cadeias**), não da tabela. Tabela completa,
com fonte e razão de cada um, em `indexadores-tipo-catalogo.json`; contagens recomputadas por
`test_valida_cobertura.py::TestMapeamentoBloco19`.

> **Eram 34 rótulos em 15 cadeias na tarefa 2; são 36 em 20 desde a tarefa 3.** Os dois rótulos
> novos são **`BTNF`** e **`UPC → índices básicos de atualização dos saldos da poupança`**, ambos
> **`indeterminado`**, ambos de `cjf.fgts-divida-fiscal.correcao-monetaria`.

| classe | quantos | quais |
|---|---|---|
| `nominal` | **4** | ORTN, OTN, BTN, Ufir |
| `percentual` | **5** | INPC, INPC/IBGE, IGP-DI, IPC/IBGE, **Selic** |
| **`janela-deslocada`** | **2** | **IPCA-E/IBGE, IPCA-15/IBGE** |
| `nao-indexador` | **8** | as 6 moedas, a conversão em URV e `(segmento sem indexador)` |
| `indeterminado` | **17** | abaixo |
| `englobante` | **0** | retirado |

**Os 17 `indeterminado`, por razão:** **13 sem fonte** — `P17-01` (IPCA série especial, IPC/FGV,
IPC-R, IRSM), `P18-01` (IPC, UPC, LBC, LBC – 0,5%, LFT – 0,5%, TRD), `P19-01` (taxa-legal),
**`P19-02` (BTNF)**, `P9-02` (NAO-DECLARADO-PELO-MANUAL); **2 com razão** (TR e remuneração
básica da poupança); **2 segmentos compostos**, `P17-03` (`Ufir → Selic (bifurcado por fato
gerador)` e **`UPC → índices básicos de atualização dos saldos da poupança`**), **não
classificados** — e a reclassificação da SELIC **agrava** o defeito do primeiro, porque agora os
dois índices embutidos são de classes **com defasagem**, isto é, o registro esconde uma virada
dentro de si.

> **`BTNF` é o rótulo em que a herança por nome seria mais tentadora — e por isso ele está aqui
> nomeado.** `BTN` é `nominal` por nomeação literal do item 4.1.2.4, letra a; **`BTNF` não é
> nomeado por fonte alguma**, nem pelo manual nem pela tabela externa. Classificá-lo como
> `nominal` *"porque é BTN Fiscal"* é exatamente a dedução por nome parecido que o bloco 17
> proibiu. Segue `indeterminado`, sob `P19-02`.

**Decisões explícitas, uma a uma:**

- **`IPCA série especial`** — **permanece `indeterminado`**. A fonte externa alcança IPCA-15 e
  IPCA-E e **não** diz que a série especial seja um ou outro; **o manual a grava como segmento
  próprio**, e identificá-la por semelhança de nome é a dedução proibida;
- **`INPC` × `INPC/IBGE`** — **mesmo índice**, e a costura já estava declarada desde o bloco 17
  (`identificacao_declarada`): é **rotulagem**, porque **não existe INPC de outro emissor**;
- **o `IPC` nu** — **permanece `indeterminado`, com a ambiguidade registrada** no campo. O
  manual usa **dois** IPC, de emissores distintos, e `D8-C21` sustenta **só o IPC/IBGE**;
- **`Ufir → Selic (bifurcado por fato gerador)`** — **não classificado**, segue `P17-03`;
- **`NAO-DECLARADO-PELO-MANUAL`** — segue `P9-02`;
- **`TRD`, `LBC – 0,5%`, `LFT – 0,5%`, `UPC`, `IPC-R`, `IRSM`, `IPC/FGV`** — **nenhum é
  alcançado pela fonte externa**; seguem `indeterminado` **sem fonte**, como estavam.

> **Divergência entre a tabela do enunciado e a fonte extraída — `IGP-DI`.** A tabela externa
> **não o nomeia**; o **item 4.1.2.4, letra b, o nomeia LITERALMENTE** (*"Ex.: INPC, IGP-DI,
> IGP-M"*), e a transcrição está em `bloco-08-jf.md`. **Prevalece a fonte extraída: permanece
> `percentual`.** Mesmo desenho para o **`IPC/IBGE`**, que a tabela externa não alcança e
> `D8-C21` sustenta. Na direção oposta, a linha **`IPCA` → percentual** da tabela externa
> **não tem destinatário**: nenhum segmento tem rótulo `IPCA` nu. **Registradas, não
> harmonizadas.**

**`IGP-M`, `TDA` e `JCM` não são rótulos de indexador de segmento algum** — ocorrem no corpus
como transcrição do item 4.1.2.4, como objeto de direito material (item 4.5.4) e como nome do
critério do FGTS fiscal (item 2.4.4.1, cadeia ausente, `P18-02`). Escopo da busca declarado no
catálogo. **Nada a mapear.**

### 25.5 Efeito sobre os validadores

| | antes do bloco | depois da Tarefa 2 | **depois da Tarefa 3 — FINAL** |
|---|---|---|---|
| **cadeias** | 15 | 15 | **20** (+5 cadeias novas) |
| **R1** | 15 | 15 — *inalterado* | **21** (+6, todas do MANUAL) |
| **R2** | 1 | 1 — *inalterado* | **1** — *inalterado* |
| **R3** | 46 | 51 (+5 líquido: **8 novas**, **3 fechadas**) | **62** (+11) |

> **A história inteira, não só o número final.** `R3` foi de **46 para 51 na Tarefa 2** e de
> **51 para 62 na Tarefa 3**; `R1` ficou em 15 na Tarefa 2 e foi a **21 na Tarefa 3**. As duas
> etapas têm causas distintas — reclassificação de índice numa, cadeias novas na outra — e
> guardar só o total impediria auditar qualquer das duas.

**As 8 novas da Tarefa 2 são ACHADO, não regressão** — nenhuma cadeia mudou de conteúdo; o campo
que as descrevia é que parou de esconder o fato:

| origem | quantas | quais |
|---|---|---|
| SELIC deixou de saltar R3 | **2** `R3` | `cjf.condenatorias-gerais.correcao-monetaria` (devedor=fazenda-publica, 2025-09) e `cjf.desapropriacao-direta.correcao-monetaria` (2025-09), ambas `Selic → IPCA-15/IBGE` |
| taxa legal deixou de saltar R3 e não tem classe | **5** `R3-INDETERMINADO` | `cjf.condenatorias-gerais.juros-mora` (2024-09 e 2025-09), `cjf.fgts.juros-mora`, `cjf.poupanca.juros-mora`, `cjf.trabalhista.juros-mora` — todas `Selic → taxa-legal` |
| IPCA-E ganhou classe | **1** `R3` | `cjf.desapropriacao-direta.correcao-monetaria`, 2001-01, `Ufir → IPCA-E/IBGE` **sem `aplicacao`** — era indeterminada, virou **confirmada** |

**As 3 fechadas:** `cjf.condenatorias-gerais.correcao-monetaria` 2001-01 `Ufir → IPCA-E`, salva
porque o segmento que **entra** declara `aplicacao` e agora o tipo é conhecido — `indeterminado`
bloqueia mesmo com `aplicacao`, pois sem saber o tipo não se sabe se a defasagem declarada é a
certa; a de desapropriação, que **reabriu como confirmada** e portanto não é fechamento líquido;
e `IPCA-E → IPCA-15` em 2024-09, que **deixou de ser virada** porque os dois são a **mesma
classe** — efeito direto da identificação declarada pela fonte externa.

**As 6 novas de R1 da Tarefa 3 são do MANUAL**, transcritas como estão, e nenhuma vem do
gerador:

| origem | quantas | quais |
|---|---|---|
| herdadas do tronco na indireta | **2** | `cjf.desapropriacao-indireta.correcao-monetaria`, 1989-01 (`IPC/IBGE × OTN`) e 1990-03 (`BTN × IPC/IBGE`) — idênticas às da direta, porque o tronco é o mesmo |
| **cortes intramensais** — o mês da fronteira cai nos dois segmentos | **3** | `cjf.desapropriacao-indireta.juros-compensatorios` 1997-06 (*"até 10/6/1997"* ÷ *"de 11/6/1997"*); `cjf.divida-fiscal.juros-mora` 1992-01 (*"a 2/1/1992"* ÷ *"de 3/1/1992"*); `cjf.divida-fiscal.correcao-monetaria` 1989-01 (OTN ÷ BTN) |
| `D8-C8` de maio/2000 | **1** | `cjf.fgts-divida-fiscal.correcao-monetaria`, 2000-05 (`TRD × TR`) — maio/2000 está nos dois, como o D8-C8 registra |

**`R2` seguiu em 1** nas duas tarefas.

**A suíte cresceu de 267 para 311 ao longo do bloco 19** — **299** depois da Tarefa 2, **310** ao
fim da Tarefa 3. *(Registro datado do bloco 19; não se atualiza.)* O 311º é
`TestMapeamentoBloco19::test_a_contagem_de_segmentos_sem_indexador_bate_com_o_repositorio`, que
guarda a única contagem que sobrou em prosa no catálogo (`(segmento sem indexador)` →
`quantos`), agora que ela saiu do texto replicado para dentro dos segmentos.

> **O placar atual dos validadores e da suíte não é transcrito aqui** — sai de
> `consolidado/00-numeros.md`, §§ 3 a 5, **gerado por script**. Esta seção registra a VARIAÇÃO do
> bloco 19, que é o que ela existe para contar; o estado de hoje tem um dono só.

---

## 26. Bloco 20 — caminho de fechamento das pendências abertas

**Nada é fechado aqui.** Esta seção diz, para cada pendência aberta, **o que exatamente falta,
onde procurar e quem resolve** — e, onde a resposta é *"não dá para fechar com o que há"*, diz
isso. Contagens de resultado (cadeias, testes, violações) não são escritas aqui: ver
*00-numeros.md*, Tarefa 6 do bloco 20.

### 26.1 Os `indeterminado`, recontados — a separação é estrutural

**Escopo contado antes de declarado:** os **32 arquivos `.json`** de `tabelas-normativas/`, campo
`indexador` e `tipo_indexador` de todo segmento de arquivo com `tipo == "cadeia-temporal"`.
**São 32 segmentos `indeterminado`, em 17 rótulos distintos.**

| Grupo | Campo que o marca | Rótulos | Segmentos | Fecha |
|---|---|---|---|---|
| **`indeterminado-sem-fonte`** | `tipo_indexador_pendencia` (`P17-01`, `P18-01`, `P19-01`, `P19-02`) | **12** | **24** | **quando a fonte aparecer** |
| **`indeterminado-por-natureza`** | `tipo_indexador_razao` | **2** — TR e remuneração básica da poupança (TR) | **5** | **nunca, esperando fonte** |
| **segmento composto** (`P17-03`) | `tipo_indexador_pendencia` | **2** | **2** | quando o segmento for partido — § 26.4 |
| **índice não declarado** (`P9-02`) | `tipo_indexador_pendencia` | **1** | **1** | quando o manual nomear o índice |

**Duas divergências de contagem, registradas e não harmonizadas:**

- `extracao/bloco-19-relatorio.md` § 2 diz **12 rótulos sem fonte**; a § 25.4 deste arquivo diz
  **13**. A diferença é `NAO-DECLARADO-PELO-MANUAL`, que **não é "sem fonte de tipo"** — é *"sem
  índice"*, e é a `P9-02`. **12** é a contagem do grupo *sem-fonte*; **13** é a contagem dos
  rótulos que carregam `tipo_indexador_pendencia` fora dos compostos. As duas frases são
  verdadeiras sobre coisas diferentes, e é por isso que colidem;
- o catálogo tem **18** rótulos `indeterminado`, **um a mais** que os 17 dos segmentos: **`JAM`**
  (`P18-01`) está no catálogo e **não é `indexador` de segmento algum**. O catálogo declara o
  porquê — o rótulo circula no corpus como se fosse índice. **Declarado, não removido.**

#### A separação já é legível por script — confirmado, com uma ressalva

`tipo_indexador_razao` ocorre **exatamente** nos 5 segmentos da família TR e em nenhum outro;
`tipo_indexador_pendencia` ocorre nos outros 27; **nunca os dois juntos** — `Segmento.de_dict`
rejeita o par. O predicado *"é `indeterminado-por-natureza`"* é, portanto, uma linha de script:
presença de `tipo_indexador_razao`. **A distinção do enunciado está no dado, não na prosa.**

**A ressalva, e a proposta:** o **subgrupo** — sem-fonte × composto × índice-não-declarado — **não
tem campo**. Só se lê **parseando o ID da pendência** (`P17-03` = composto, `P9-02` = sem índice),
e ID de pendência é string de prosa. **Proposta, não executada:** um mapa
`subgrupo_por_pendencia` em `indexadores-tipo-catalogo.json`, ao lado de `razoes_de_indeterminado`
— que já nomeia os três subgrupos em texto. **Sem campo novo no segmento**: o segmento já carrega
o ID, e duplicar a classificação nele criaria duas verdades para manter.

### 26.2 Os doze — qual fonte fecharia cada um

**Não "uma fonte". A fonte.** Onde a resposta é *"nenhuma"*, está escrito.

| Rótulo | Segs. | **A fonte que fecharia** | Natureza |
|---|---|---|---|
| **`taxa-legal`** | 5 | **Nenhuma.** Art. 406 do CC (red. Lei 14.905/2024) e Res. CMN n. 5.171/2024 dão a **fórmula**, não a classe — e a fórmula compõe duas classes distintas (§ 26.3). **É decisão do projeto**: a tricotomia admite ou não índice **derivado**? | **decisão** |
| **`TRD`** | 3 | **Norma do emissor (BCB)** sobre a apuração da TRD — **a mesma classe de documento que fechou a TR fora do agente**. Se disser *"período entre datas de aniversário"*, fecha como **razão**, não como classe, e a TRD migra de `pendencia` para `razao` | norma do emissor |
| **`IPCA série especial`** | 2 | **Art. 2º, § 2º, da Lei n. 8.383/1991** — **já nomeado no `fundamento` do próprio segmento**; o **texto** do ato não está no corpus. Subsidiariamente, nota metodológica do **IBGE** sobre a série especial de dez./1991 | ato de instituição, **já nomeado** |
| **`IPC/FGV`** | 2 | **Metodologia do emissor (FGV)**. O manual usa o índice e não o classifica; `D8-C21` alcança só o IPC/IBGE | norma do emissor |
| **`IPC`** (nu) | 2 | **Nenhuma fonte de classe — a pergunta não é de classe, é de EMISSOR.** Fecha quem nomeie o emissor do `IPC` do item 4.8.1.1 (`pagina_pdf` 82): errata ou edição nova do **CJF**. Se o emissor for o IBGE, `D8-C21` **já** classifica. **Ninguém no repositório pode declará-lo** | fonte externa (CJF) |
| **`LBC`** | 2 | **Ato de instituição da LBC** e a **resolução do CMN/BACEN** que a pôs como remuneração de FGTS e poupança em 1987. **Nenhum dos dois é citado em lugar algum do corpus** | ato de instituição, **não nomeado** |
| **`LBC – 0,5%`** | 2 | Idem — **e uma segunda pergunta na mesma norma**: a natureza do redutor de 0,5% (juros descontados? redutor do índice?), que a tabela não declara | idem |
| **`LFT – 0,5%`** | 2 | Idem, e a mesma norma responderia o **`N-5` / `D8-C13`** (o expurgo de 42,72% substitui ou acresce) | idem |
| **`BTNF`** | 1 | **Ato de instituição do BTNF.** O corpus **não o nomeia**: o item 2.4.4.1 (`pagina_pdf` 35) e a NOTA 3 de 4.9.1.1 (`pagina_pdf` 85) **usam** o BTNF sem classificá-lo | ato de instituição, **não nomeado** |
| **`UPC`** | 1 | **Ato de instituição da UPC.** O item 2.4.4.1 só **expande a sigla** — rotulagem, não classificação. Não nomeado no corpus | ato de instituição, **não nomeado** |
| **`IRSM`** | 1 | **Art. 9º, § 2º, da Lei n. 8.542/1992** — **já nomeado no `fundamento` do segmento**; texto não extraído | ato de instituição, **já nomeado** |
| **`IPC-R`** | 1 | **Art. 20, § 6º, da Lei n. 8.880/1994** — **já nomeado no `fundamento` do segmento**; texto não extraído | ato de instituição, **já nomeado** |

**O que a coluna da direita muda, e é o ponto desta tarefa:**

- **três** (`IPCA série especial`, `IRSM`, `IPC-R`) já trazem o ato **escrito no próprio segmento**
  — o que falta é o **texto**, e quem o busca sabe exatamente o que pedir;
- **cinco rótulos em quatro normas** (`LBC`, `LBC – 0,5%`, `LFT – 0,5%`, `BTNF`, `UPC`) dependem
  de ato **que o repositório não nomeia**: antes de ler, é preciso **descobrir qual ler**;
- **dois** (`TRD`, `IPC/FGV`) fecham por **norma do emissor**, não por lei;
- **um** (`IPC` nu) **não é problema de classe** e nenhuma fonte de tipo o fecha;
- **um** (`taxa-legal`) **nenhuma fonte fecha — é decisão.** E isso **muda quem resolve**: sai do
  campo da pesquisa documental e entra no de quem desenha o domínio.

> **`indeterminado` continua bloqueando em todos os doze.** Nenhuma linha acima autoriza
> classificar; todas dizem onde procurar.

### 26.3 A varredura do extraído — escopo contado, e o que ela achou

**Escopo contado antes de declarado:** **48 arquivos `.md` e 21 `.csv`** sob
`docs/calculo/extracao/` — **69 arquivos, 1.745.128 bytes** —, mais os **32 `.json`** de
`tabelas-normativas/`. Três critérios, todos com `encoding='utf-8'` explícito:

1. cada um dos doze rótulos em **janela de ±350 caracteres** de *nominal*, *percentual*,
   *reflete*, *defasag*, *mês anterior*, *próprio mês*, *divulga*, *aniversár*, *acumulad*,
   *prefixad*, *período de coleta*;
2. cada rótulo em janela de ±250 caracteres de **ato normativo** — *Lei*, *Decreto-lei*,
   *Decreto*, *Resolução*, *MP*, *Medida Provisória*, *Circular* —, para achar o ato citado num
   `fundamento` sem ninguém ter notado;
3. leitura **campo a campo** dos 32 segmentos `indeterminado`, nos campos que classificam sem
   nomear a classe: `formula`, `aplicacao`, `aplicacao_fonte`, `regra_literal`, `fundamento`,
   `observacao`, `notas`, `base_incidencia`.

> **Resultado: NÃO HÁ fonte no extraído que classifique qualquer um dos doze.** Nos **21 `.csv`**,
> **zero ocorrências** dos doze rótulos. Os acertos dos critérios 1 e 2 são de três espécies,
> nenhuma classificatória: (i) os relatórios dos blocos 17, 18 e 19 **narrando a ausência**;
> (ii) `bloco-04-verbas2.md`, que usa `IPC`, `IPC-r` e `IRSM` como **índice de reajuste salarial**
> — cronologia normativa, nunca classificação; (iii) os próprios campos `tipo_indexador_*`.

#### Um achado, e ele não fecha — **muda a natureza da pendência**

**`taxa-legal`.** Os cinco segmentos carregam `formula: "SELIC, com dedução do IPCA-15"`, e três
carregam `aplicacao: "mes-posterior-a-competencia"` com `aplicacao_fonte` citando a **NOTA 4** do
item — *"A taxa legal observará as mesmas orientações estabelecidas na Nota 7 do item 4.2.2"* — e
a **Nota 7, `pagina_pdf` 56**, fórmula `D1`. **Isto estava no extraído e não chegou ao catálogo**,
cuja entrada de `taxa-legal` não traz nem a fórmula nem a Nota 7.

**E ainda assim não classifica**, por duas razões que se somam:

- a fórmula **compõe** um `percentual` (Selic) com um `janela-deslocada` (IPCA-15). **A tricotomia
  do bloco 19 não tem resultado para essa composição** — e a reclassificação da SELIC, que a
  tornou `percentual`, é o que deixou isso visível;
- o item 4.1.2.4, letra b, prende *"aplicação prática no mês seguinte"* à **DIVULGAÇÃO**; a Nota 7
  prende ao **mês posterior à COMPETÊNCIA**. **Casar as duas é inferência**, e é a dedução que o
  catálogo existe para impedir.

> **Efeito: `P19-01` deixa de ser *"esperando fonte"*.** A fonte que descreve a taxa legal **está
> no corpus, com item e `pagina_pdf`** — e o que ela descreve é um **índice derivado**, objeto que
> a tricotomia não prevê. **`P19-01` é decisão de modelagem**, e a opção está em § 26.4.
> **Próximo passo nomeado, não executado:** levar `formula` e a citação da Nota 7 para a entrada
> `taxa-legal` do catálogo. É **movimentação de dado já extraído**, não classificação.

### 26.4 Os quatro — extração, fonte externa ou decisão de modelagem

| # | Item | Veredito |
|---|---|---|
| 1 | `Ufir → Selic (bifurcado por fato gerador)` | **modelagem** |
| 2 | `UPC → índices básicos de atualização dos saldos da poupança` | **extração — e a fronteira é o que a fonte não declara** |
| 3 e 4 | as duas `taxa: null` dos juros compensatórios | **extração pura** |

#### 1. `Ufir → Selic`, em `cjf.divida-fiscal.correcao-monetaria.json`, `1992-01..2026-06` — MODELAGEM

**A fronteira ESTÁ declarada.** O `regra_literal` do próprio segmento data as viradas dos dois
ramos: *"Para fatos geradores ocorridos: a) Até 31/12/1994: I. Até jan./1997: Ufir; II. A partir
de jan./97: taxa Selic, até o mês anterior ao pagamento; 1% no mês do pagamento. b) A partir de
jan./1995: I. De jan./95 a mar./1995: TMMCTN; II. A partir de abr./1995: taxa Selic até o mês
anterior ao pagamento; 1% no mês do pagamento."* **E o eixo já existe no arquivo:**
`condicao: {"eixo": "data-do-fato-gerador"}`, com `dominio_condicoes` declarado. **Partir
resolve**, e nada precisa ser inventado.

> **Achado colateral desta leitura:** o rótulo `Ufir → Selic` **esconde um terceiro indexador** —
> **`TMMCTN`**, jan. a mar./1995 —, que **não está no catálogo** nem é `indexador` de segmento
> algum. Partir o segmento **cria um rótulo novo**, e ele nasce `indeterminado`.

**As opções, e o que cada uma custa:**

| Opção | Custo |
|---|---|
| **(A)** dois ramos em `condicao`, com valores próprios | Expõe a R3 a virada `nominal → percentual` que hoje está escondida. **Custa uma lacuna de R2** no ramo *"a partir de jan./1995"* antes de 1995-01 — janela **vazia por construção**, porque não há fato gerador ali —, que exige **exceção declarada** |
| **(B)** manter um registro, declarando a composição | Custo zero de validador, e **mantém uma virada de classe escondida dentro de um segmento** — exatamente o que a § 25.4 registra como agravado pela reclassificação da SELIC |
| **(C)** uma cadeia por ramo | Duplicação, do tipo que a `DECISAO_1` da desapropriação indireta já pagou uma vez, e ali **com derivação em tempo de geração**. Aqui os ramos **não são derivados um do outro** |

**Por que o agente não escolhe sozinho:** a opção (A) cria **ramo sem gêmeo**, e o próprio
`gera_cadeias_bloco19.py` registra, em outra cadeia, que isso *"abriria lacuna de R2"*. Escolher
entre **aceitar exceção de R2** e **duplicar cadeia** é decisão de desenho do domínio, com efeito
sobre o validador e sobre quem consome a cadeia — não é leitura de fonte.

#### 2. `UPC → índices básicos`, em `cjf.fgts-divida-fiscal.correcao-monetaria.json`, `1983-10..1989-10` — EXTRAÇÃO

O item 2.4.4.1 (`pagina_pdf` 35–36) é **lista, não tabela**, e foi transcrito literalmente:
*"Unidade Padrão de Capital (UPC) e os índices básicos de atualização dos saldos da poupança."*
**Não data a fronteira.**

**O que pedir** — o PDF está fora do repositório: releitura das **`pagina_pdf` 35–36, item
2.4.4.1**, procurando (a) data de virada entre a UPC e os *"índices básicos"*, e (b) **notas do
item**, se houver, já que a extração registra a cadeia como lista sem notas.

> **E o atalho óbvio NÃO funciona — verificado.** A cadeia da poupança (item 4.9.1.1,
> `pagina_pdf` 85) encerra a UPC em **1983-06**; este segmento **começa em 1983-10**. Importar a
> data de lá trocaria a data de uma cadeia pela de outra **e ainda erraria por quatro meses**.
> Registrado para que a tentativa não se repita.

**Se a releitura voltar sem data, é isso a resposta:** **partir exigiria inventar a fronteira**, e
o segmento permanece composto. Não é fonte externa — o documento é o próprio manual.

#### 3 e 4. As duas `taxa: null` dos juros compensatórios — EXTRAÇÃO PURA

`cjf.desapropriacao-direta.juros-compensatorios.json` (item **4.5.3**, `pagina_pdf` **69**) e
`cjf.desapropriacao-indireta.juros-compensatorios.json` (item **4.6.3**, `pagina_pdf` **76**),
primeiras duas linhas de cada: `1964-01..1997-06` e `1997-06..2021-11`, `taxa: null` com
`taxa_nao_extraida`. O corpus registra **período**, **fundamento** (MP n. 1.577/1997 e sucessivas,
com a ADI n. 2332 nas observações) e os **três cortes** — e **não registra a coluna do percentual**.

**O que pedir, nominalmente:**

1. a **coluna de percentual/critério** das duas linhas — *"Até 10/6/1997"* e *"De 11/6/1997 a
   nov./2021"* — da tabela do **item 4.5.3, `pagina_pdf` 69**;
2. a mesma coluna da tabela do **item 4.6.3, `pagina_pdf` 76** — **as duas, e não uma**: as
   cadeias divergem em termo inicial (`D8-C10`) e a indireta **não** é derivada da direta aqui;
3. junto, a **coluna de fundamento da PRIMEIRA linha** de cada, hoje `fundamento: null` com
   `fundamento_nao_extraido`.

**Varredura de confirmação, escopo declarado:** `docs/` e `skills/`, extensões `.md`, `.csv` e
`.json`, termo *compensat* com **percentual na janela**. **Nenhum percentual de juros
compensatórios ocorre no repositório inteiro** — o que há é *"0,5% a.m. desde ago/2001"*, que é
**juros de mora de precatório**, e *"vedado o cálculo de juros compostos"* (`pagina_pdf` 71), que
é **capitalização**, não taxa.

**Não é fonte externa** — a fonte é o próprio manual, e ela existe. **Não é modelagem** — o campo
existe e o buraco está visível ao validador, que é o desenho que o bloco 19 escolheu de propósito.

> **Ressalva que evita um pedido errado:** a **terceira** linha de cada cadeia
> (`2021-12..2026-06`) **também** tem `taxa: null`, e **não é o mesmo buraco**. Ali o `null` **é a
> regra** — *"Já incluídos na SELIC aplicada aos juros de mora"* —, e o segmento o declara em
> `D8-C11`. **Pedir percentual para ela é pedir dado que não existe**, e gravá-lo seria dupla
> contagem.

### 26.5 Veredito sobre partir os compostos, e uma correção de registro

| Composto | Partir resolve? |
|---|---|
| **`Ufir → Selic (bifurcado por fato gerador)`** | **SIM.** A fonte declara as quatro viradas e o eixo já está no arquivo. O que falta é **decisão**, não dado |
| **`UPC → índices básicos de atualização dos saldos da poupança`** | **NÃO, com o que há.** **A fronteira é justamente o que a fonte não declara** — partir exigiria **inventar a data** |

> **Os dois vivem sob a mesma `P17-03` e não têm a mesma natureza.** **Proposta, não executada:**
> desdobrar em **`P17-03a`** (modelagem — dívida fiscal) e **`P17-03b`** (fonte não declara a
> fronteira — FGTS fiscal). **Não feito aqui** porque mexer em ID de pendência toca os dois JSON,
> o catálogo e esta seção de uma vez, e a Tarefa 4 do bloco 20 **dá caminho, não fecha**.

**Correção de registro.** A § 24.2 descrevia a `TRD` como *"segue a TR (P17-02)"*. **O bloco 19
desfez essa herança** — a fonte do BCB nomeia TBF, Redutor-R e TR, **não** a TRD (§ 25.3). A
célula foi corrigida; o resto da § 24.2 fica como estava.

---

## 27. Bloco 23 — as duas lacunas que a aceitação da frente A revelou

**Nenhuma das duas é falta de dado externo. As duas são o corpus não dizendo o que fazer**, e
por isso entram aqui em vez de virarem regra.

### 27.1 `P23-01` — a **régua de ajuste** da virada de `R3` não existe

`R3` diz que `nominal` reflete **M−1**, `percentual` reflete **M** e `janela-deslocada` reflete
**metade de cada**, e que trocar de classe **sem ajustar desloca o cálculo em um mês**. **O que
FAZER na virada — repetir o mês, pular, pro-ratizar — não está enunciado.**

**O que existe e não é isso:** o campo `aplicacao`, vocabulário fechado **D1–D4**
(`consolidado/02-atualizacao-detalhe.md` § 5.3). Ele declara **se** a defasagem foi tratada
naquele segmento; **não** qual deslocamento aplicar na fronteira entre dois segmentos de classes
diferentes.

**Busca negativa, escopo contado:** os **15** arquivos de `consolidado/` e as **31** páginas
`.md` de `skills/`, por `defasagem`, `desloca`, `ajustar`, `ajuste`, `na virada`, `um mês`,
`pro rata` e `régua`. Toda ocorrência **enuncia o efeito de não ajustar** ou **descreve D1–D4**;
**nenhuma dá o procedimento**. O próprio corpus registra a indecisão: a `L3` de
`consolidado/10-literais-na-extracao.md` § 5.2 foi reclassificada `DÚVIDA` com a frase *"ninguém
sabe qual é o comportamento certo"*, e a primeira das três perguntas que faltam é **decisão de
modelagem, não leitura de fonte**.

**Fecha com:** decisão de modelagem declarada — não com releitura de PDF. Até lá: ponta
`indeterminado` **bloqueia** sob `R3-INDETERMINADO`; duas pontas com classe diferente viram `[R3]`
**registrada e não consertada**. Quem precisar do número decide a régua, justifica (**R21**) e
grava (**R13**). Declarada em `calculo-judicial-core` (Limitações),
`indices-judiciais/references/catalogo-de-indices.md` (última seção) e `civel-federal.md` § 10.

### 27.2 `P23-02` — `aplicacao` da **Fazenda entre jul/2009 e nov/2021** não é declarada

`civel-federal.md` § 5 atribui **D2** à Fazenda de **jan/2003 a jun/2009** e **D1** à Fazenda **a
partir de dez/2021**. **A janela do meio fica sem fórmula**, e a **fixture 1** (citação em
01/2021) cai exatamente nela.

> **Estender D1 "por ser o que a Fazenda usa depois" é dedução por continuidade de sujeito.** O
> que muda em dez/2021 é a **EC 113/2021**, que reescreve o regime — **o D1 nasce com ela**, e
> antes dela a Fazenda esteve em **D2**. `R-08-09` mede o preço da escolha errada: *a mesma
> Selic, dois números*.

**Conduta declarada:** **bloquear e perguntar**, nunca arbitrar. Registrada em `civel-federal.md`
§§ 5 e 11 (itens 10 e 11 — o item 11 é a **outra** metade do mesmo segmento: *"mensalizada"* sem
definição aritmética).

### 27.3 O que a aceitação mostrou que **já funcionava**, e por quê

Três quase-invenções foram contidas **pela skill, não pela disciplina do implementador** — e o
que as conteve foi sempre a mesma forma: **a conduta proibida está NOMEADA, não deduzível.**

| Quase-invenção | O que a impediu |
|---|---|
| classificar **IPCA-E como percentual** | a frase *"classificar o IPCA-E como percentual porque IPCA soa percentual é a dedução que o bloco 17 removeu"* — **nomeia o erro com o exemplo dele dentro**, e a `REGRA_DESTE_CATALOGO` repete a proibição no dado |
| **interpolar** IPCA-E entre meses conhecidos | *"a conduta padrão diante do buraco é registrar e parar, nunca costurar"*, numa tabela em que **nenhum** dos quatro comportamentos é interpolação |
| buscar série nos **CSV de `extracao/trabalhista/`** | o cabeçalho `# OUT_OF_SCOPE` no próprio arquivo **mais** a frase da skill: existem *"como evidência de conferência, não como fonte de consulta"*. **Duas barreiras, uma delas no dado** |

**O padrão que se replica:** proibição genérica (*"não invente"*) não segura ninguém; **proibição
com o caso concreto ao lado** segurou as três. As duas quase-invenções que a skill **não** cobria
— taxa legal da variante errada e extensão de D1 — eram exatamente aquelas em que **o valor certo
existe no repositório para OUTRO uso**, e nenhuma delas tinha o caso nomeado. Agora têm.
