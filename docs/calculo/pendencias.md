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
do caso 6 saiu da suíte — 123 testes, nenhum pulado.

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

