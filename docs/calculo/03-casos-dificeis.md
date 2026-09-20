# Casos difíceis — validação da espinha consolidada

**Substitui** a lista provisória da Fase 3 do `01-plano-extracao.md`, escrita antes da
extração e com o caso 6 errado.

**Como usar:** a espinha consolidada deve responder a cada caso abaixo. Resposta ausente
ou errada é perda de informação na consolidação, não lacuna do corpus. Os casos marcados
`[NOVO]` vieram da extração e valem mais que os originais, porque foram encontrados, não
antecipados.

---

## Grupo 1 — Cumulação e composição

### C1 — Englobamento
A espinha deixa claro que SELIC e taxa legal englobam correção monetária e juros, e que
aplicar correção junto é erro material? (R1)

### C2 — Taxa legal é razão, não subtração `[NOVO]`
A espinha registra que a taxa legal se calcula por `(Fator_Selic / Fator_IPCA15 − 1) × 100`,
seis decimais, com IPCA-15 do mês anterior — e não por subtração de percentuais, que é a
descrição legal do efeito? (R11)

Validação: set/2025 INPC → 1,377047% pela razão, 1,374156% pela subtração.

### C3 — Deflação e piso nominal
Índices negativos entram no cálculo, mas nenhuma parcela do principal fica abaixo do valor
nominal? E a instrução do manual TRT-3 de "dividir pelo índice negativo" está registrada
como redação defeituosa, não implementada? (R5)

### C4 — Nominal contra percentual na virada `[NOVO]`
A espinha registra que índice nominal (Ufir, BTN, OTN, ORTN) reflete a inflação do mês
anterior e percentual (INPC, IPCA, IGP) a do próprio mês, e que trocar entre tipos sem
ajustar a defasagem desloca o cálculo em um mês? (R3)

---

## Grupo 2 — Ordem de operações e imputação

### C5 — Imputação proporcional sem norma `[NOVO — o mais importante do conjunto]`
A espinha registra que:
- o critério trabalhista de imputação é **proporcional** (letra F/G do item 10.3);
- ele é aplicado 101 vezes no capítulo 10 e **fundamentado zero vezes**;
- `art. 354` tem **zero ocorrências em 471 páginas**;
- portanto entra como **preset sem default**, nunca como regra derivada do corpus;
- a variante é o art. 354 do Código Civil aplicado subsidiariamente.

E registra a direção do delta: juros primeiro produz saldo maior, logo dívida maior. O
critério proporcional favorece o devedor; o art. 354 favorece o credor.

Amplitude medida: até 23,83% do saldo.

### C6 — Descarregar antes de aplicar juros `[NOVO]`
A espinha registra que, antes de aplicar juros sobre saldo remanescente, os juros já
contidos nesse saldo devem ser excluídos, sob pena de anatocismo? (R23)

E registra que o manual executa a operação no capítulo 10 sem a fundamentar, e que quem a
nomeia como anatocismo é a minuta da p.328?

### C7 — A amortização parte a linha do tempo `[NOVO]`
A espinha registra que a amortização não é um passo a mais no fim: tudo é trazido à data
do levantamento, rateado ali, e só então levado ao marco final — e que é por isso que o
rateio custa até 23,83%, porque decide a composição do saldo que rende juros pelo período
residual inteiro?

### C8 — Base contra ordem `[NOVO]`
A espinha registra que a ordem das operações **não** altera o resultado (distributividade,
delta 0,00), mas a **base** altera?

Deltas medidos:
- juros sobre nominal em vez de corrigido: −2,48%; com vincendos, −3,15%
- INSS antes dos juros na base de IR: −R$ 285,83

### C9 — Amplitude da imputação tem forma fechada `[NOVO]`
`amplitude = min(abatimento, principal, juros) × índice_residual × pct_juros_residual`

A espinha registra que qual das três grandezas limita **muda por caso** — o Exemplo 5 tem
quase o dobro da participação de juros do Exemplo 1 e amplitude percentual menor, porque
ali o limitante é o abatimento?

### C10 — Data de referência da dedução `[NOVO]`
A dedução se dá na data do **levantamento**, não do depósito. A espinha registra que o
capítulo 10 adota essa tese sem citar a Súmula 15/TRT-3, e que o item 16.4.11 reconhece
**duas** teses?

---

## Grupo 3 — Arredondamento e precisão

### C11 — Cinco cadeias de arredondamento `[NOVO]`
A espinha registra o critério **por etapa**, e não um critério global?

| Etapa | Critério | Casas | Fonte |
|---|---|---|---|
| Fator de índice e taxa legal | truncamento | 6 | CJF 4.2.1.1 Nota 6 |
| Grandeza física (hora centesimal, nº de HE) | half-up | 2 | TRT-3 item 5.3 |
| Valor monetário intermediário e final | truncamento | 2 | CJF |
| NMP (nº de meses RRA) | 3 ramos, IN 1500/14 art. 45 § único | 1 | TRT-3 pp.226, 230 |
| Cadeias do capítulo 6 | 4 práticas não enunciadas | — | armadilha |

A regra do NMP **não é half-up**: 2ª casa `<5` mantém, `>5` sobe, `=5` manda olhar a 3ª
casa. Difere de `ROUND_HALF_UP` na faixa `x,y50` a `x,y54`.

### C12 — Precisão plena na cadeia interna `[NOVO]`
A espinha registra que o motor usa precisão plena em toda a cadeia interna e trunca só na
emissão, e que valor exibido nunca realimenta cálculo — mesmo que isso divirja de parte
dos exemplos do manual, que consomem valor exibido?

---

## Grupo 4 — Capitalização

### C13 — Exceção histórica à R4 `[NOVO]`
A espinha registra que juros de mora, SELIC e taxa legal são sempre simples, **salvo** a
capitalização composta por força do DL 2.322/87, de 27/02/1987 a 03/03/1991?

Confirmada independentemente pelos dois manuais. Quem ler só "juros sempre simples" erra
quatro anos.

### C14 — Acumulação por soma, não por produto
A espinha registra que a acumulação de percentuais mensais se faz por somatório, porque a
multiplicação caracterizaria anatocismo, vedado pela Súmula 121 do STF — e que o regime
vem da **lei que institui a taxa**, caso a caso, não de uma regra geral "juros somam,
índices multiplicam"?

---

## Grupo 5 — Regimes temporais

### C15 — OJ 394 `[CORRIGIDO — a versão anterior deste caso estava errada]`
A espinha registra a **bifurcação**, não a regra antiga?

| Hora extra trabalhada | Reflexo do RSR majorado em férias, 13º, aviso, FGTS |
|---|---|
| Até 19/03/2023 | **Não** (OJ 394, redação de 2010) |
| A partir de 20/03/2023 | **Sim** (Tema Repetitivo 9) |

O corte é pela **data em que a hora extra foi trabalhada** — não pelo ajuizamento nem pelo
julgamento. Contrato que atravesse a data tem os dois regimes no mesmo processo.

### C16 — Item "i" da ADC 58, duas situações `[NOVO]`
A espinha registra que o tratamento do valor pago depende de fato processual?

| Situação | Condição | Valor pago |
|---|---|---|
| i.1 | Pago sem questionamento, ou trânsito em julgado | Sai da conta. Critério novo só sobre o residual. **Sem rateio** |
| i.2 | Execução instaurada após início dos debates da ADC 58 **e** questionamento expresso | Entra pelo critério novo. **Rateio se aplica** |

Em i.1, recompor o bruto até a data do pagamento antes de deduzir é o que a modulação
veda. Em i.2, a proporção mudar porque os juros mudaram é o comportamento correto.

A proteção de i.1 alcança depósito com finalidade de pagamento e incontroverso liberado;
**não** alcança depósito recursal nem parte controversa do depósito em garantia.

### C17 — Intertemporal da Reforma, com regra fixada `[REESCRITO NO BLOCO 15]`
A espinha registra que o **Tema 23 do TST** (IRR, Pleno, 25/11/2024, 15 × 10, transitado,
**modulação pedida e negada por unanimidade**) fixou tese vinculante — `tempus regit
actum`, com eixo na **competência do fato gerador**?

E que a **ultratividade é posição vencida**, aplicável apenas a título que a tenha adotado
**expressamente**, prevalecendo então por R8?

E que, por isso, `pr.intertemporal` **deixou de ser caso de R20-EXCEÇÃO** — que cai de
cinco para quatro?

> **A versão anterior deste caso perguntava o contrário:** se a espinha registrava as duas
> correntes "sem default, porque a base manda não resolver". **A base estava desatualizada.**
> O caso foi reescrito no bloco 15, junto com `02-base-normativa-verbas.md` § 1 e o catálogo
> de regimes.
>
> **A pergunta sobre a interação sobrevive, e continua valendo:** sob a corrente ultrativa —
> quando o título a adote — regimes posteriores à admissão podem **nunca ser consultados**. É
> comportamento modelado e testado.

### C18 — Eixos de corte não são intercambiáveis `[NOVO]`
A espinha registra que os catorze eixos mapeados cortam por coisas diferentes — data do
fato, data do ajuizamento, data da sentença, trânsito em julgado, estado processual,
evento — e que modelar como se fosse um eixo só é erro?

Exemplos: a multa do art. 467 corta pela data da sentença; o divisor do bancário, por
estado processual; a OJ 394, pela data da hora extra trabalhada.

### C19 — Súmula 124, modulação `[NOVO]`
A espinha registra que a ressalva do item II alcança as **sentenças transitadas em julgado
ainda em liquidação, silentes quanto ao divisor** — que é exatamente o caso de uso de
conferência de cálculo?

### C20 — Consolidação em dez/2021
A espinha registra os três valores de fechamento por ramo?

| Ramo | Índice nov/2021 | Juros dez/2021 |
|---|---|---|
| Condenatórias em geral / desapropriação | IPCA-E 1,17% | 0,4412% |
| Previdenciário | INPC 0,84% | 0,4412% |
| Trabalhista (JF) | TR 0,00% | 0,4412% |

### C21 — Desapropriação
A espinha registra que os juros compensatórios passam a estar embutidos na SELIC a partir
de dez/2021, sem taxa adicional?

---

## Grupo 6 — Norma coletiva e parâmetros

### C22 — Precedência
Título judicial > norma coletiva da competência > escolha do usuário > default legal, com
divergência entre níveis registrada? (R8, R16)

### C23 — Ausência de norma coletiva não é erro `[NOVO]`
Competência sem instrumento cadastrado usa o default legal e marca a conta como "sem
cobertura coletiva"? (R14)

E a espinha registra a **exceção**: verba exclusivamente convencional (ajuda-alimentação)
não tem default legal e é **incalculável** sem instrumento — terceiro estado de cobertura?

### C24 — Art. 611-B decide elevação contra alteração `[NOVO]`
A espinha registra que a classificação `apenas-elevacao` / `qualquer` se ancora no art.
611-B da CLT, não na presença de "no mínimo" no texto de cada artigo?

- inciso alcança o parâmetro → `apenas-elevacao` (insalubridade e periculosidade, XVIII;
  noturno, VI)
- parágrafo único (duração do trabalho e intervalos, que **não** são normas de saúde para
  esse fim) → `qualquer`
- demais → `qualquer`, sob o Tema 1046 do STF

### C25 — Divisor é derivado, não parâmetro `[NOVO]`
A espinha registra que o divisor decorre da jornada (art. 64 da CLT; IRR-849 tese 3) e não
pode ser cadastrado avulso, sob pena de admitir o par inconsistente `(jornada 44h, divisor
200)`? E que o 210 da 12×36 é atributo do regime, não do divisor?

E que ampliar o RSR por norma coletiva **não move o divisor** — teses 1 e 4 do mesmo
acórdão?

### C26 — Norma coletiva é atributo do contrato `[NOVO]`
Não do processo nem da empresa. Dois empregados da mesma empresa, no mesmo processo, podem
resolver o mesmo parâmetro de formas diferentes? (R17)

---

## Grupo 7 — Leitura do corpus

### C27 — Regra mora no exemplo `[NOVO]`
A espinha adverte que, no manual do TRT-3, a regra de cálculo frequentemente só existe
dentro de exemplo numérico, sem enunciado — confirmado nos capítulos 9, 10, 11 e 16 — e
que quem consultar pelo sumário não encontra o que precisa?

Casos estruturais: o 13º como base autônoma no INSS; o vencimento do IR no dia 20.

### C28 — Fundamento fora do capítulo que executa `[NOVO]`
A espinha adverte que há operações centrais cuja única fundamentação está fora do capítulo
que as executa? Seis casos em 36 fundamentos cruzados, incluindo a IN SRF 15/2001, fonte
declarada do gross-up, com **uma ocorrência em 471 páginas**.

### C29 — Afirmação de ausência exige escopo declarado `[NOVO]`
A espinha registra, como regra de método, que "zero ocorrências no segmento" e "zero
ocorrências em 471 páginas" são afirmações diferentes, e que só a segunda sustenta uma
negativa sobre o manual?

Origem: a negativa sobre a regra de arredondamento do NMP passou por duas rodadas de
validação adversarial porque a busca tinha a forma certa e o escopo errado. A regra estava
nas 13 páginas ainda não extraídas.

---

## Grupo 8 — Defeitos do original

### C30 — O comparador precisa conhecer os erros do manual `[NOVO]`
A espinha aponta para `armadilhas-comparador.md` e registra que um perito que use o manual
reproduz o número errado, e que o motor precisa **reconhecê-lo**, não reproduzi-lo?

Exemplos com assinatura detectável:
- fórmula do bruto levantado com colchete fechado cedo (pp.227, 231) — delta 3.771,73; o
  próprio manual publica a forma correta duas páginas depois, e a errada propaga às pp.244
  e 250
- gross-up com sinal invertido (p.244)
- exemplo 8 (p.297): juros contados duas vezes, 21.476,22 contra 17.673,59
- linha copiada da p.261 para a p.223, com multa embutida
- índice de dez/10 com monotonicidade quebrada
- P11B-01 (p.266): total 43.077,24 contra 43.088,23
- P10D-01 (p.269): total 154.874,90 contra 156.911,41

### C31 — Divergências esperadas não são erros `[NOVO]`
A espinha registra que a divergência de R$ 0,01 da fixture 2 e a de R$ 0,03 da fixture 4
são **documentadas e esperadas**, decorrentes do truncamento, e que um motor que as zere
está arredondando errado?

---

## Grupo 9 — O que o corpus não resolve

### C32 — Classificação como Fazenda Pública `[NOVO]`
A espinha registra que o manual **se contradiz** — capítulo 8, p.102, exclui entes que
explorem atividade econômica; capítulo 14, p.306, diz administração direta e indireta sem
a ressalva — e que `economia mista` tem **zero ocorrências em 471 páginas**?

E que, portanto, a classificação não sai de extração nem de pesquisa: vem do jurídico do
cliente, ou da leitura de como os juízes vêm decidindo nos processos existentes?

### C33 — Dados externos bloqueantes `[NOVO]`
A espinha registra as três dependências que o motor não pode suprir?

| Dado | Papel | Consequência da ausência |
|---|---|---|
| Tabela Única do CSJT | única fonte da cadeia trabalhista anterior a 03/1991 | motor não calcula o período |
| Série histórica de ACTs | parâmetros negociáveis por categoria e competência | cai no default legal, marcado |
| Faixas do art. 85, § 3º, CPC | honorários sucumbenciais | não estão no repositório |
