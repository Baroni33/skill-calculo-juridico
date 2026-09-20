# Inventário consolidado de parâmetros negociáveis

**Bloco 5 — versão 2.0.** Substitui a v1, que estava bloqueada pela ausência de
`02-base-normativa-verbas.md`. O arquivo chegou; as tarefas 2 e 4 foram executadas.

Pontos do cálculo de verbas que **norma coletiva, acordo individual ou definição
contratual podem alterar**. Sem este inventário o motor de verbas não pode ser
escrito: cada fórmula extraída nos blocos 02 a 04 tem constantes que não são
constantes.

Fonte de verdade executável: [`tabelas-normativas/camada-norma-coletiva-catalogo.json`](tabelas-normativas/camada-norma-coletiva-catalogo.json).
Este documento é a leitura humana dele. Divergiram, vale o JSON — é o que o
validador lê.

**32 parâmetros.** A v1 dizia "17 parâmetros + 1 derivado"; a contagem já estava
errada naquela versão (o catálogo tinha 19 + 1) e está corrigida aqui e no JSON.

---

## 1. Como ler

| Campo | Significado |
|---|---|
| `id` | Chave estável, usada pela camada de resolução |
| **verba(s)** | O que muda de valor se o parâmetro mudar |
| **default legal** | Valor aplicado quando não há instrumento coletivo (R14) |
| **fonte** | De onde vem o default |
| **tipo** | `substituicao-de-valor` · `alteracao-de-composicao` · `chave-de-variante` |
| **alteração** | `apenas-elevacao` (R18) · `qualquer` · `derivado` |
| **derivado-de** | Quando o valor não é negociado, mas calculado de outro (§ 5) |
| **`fundamento_611b`** | Inciso do art. 611-B que sustenta a classificação (§ 3) |
| **`classificacao_provisoria`** | `true` enquanto nenhum inciso fornecido alcançar |

**Os três tipos:**

- **`substituicao-de-valor`** — troca um número. O adicional de 50% vira 80%. A
  fórmula não muda; muda o operando.
- **`alteracao-de-composicao`** — uma verba passa a integrar, ou deixa de integrar,
  uma base de cálculo. A fórmula muda de argumentos.
- **`chave-de-variante`** — seleciona **qual regra já implementada** se aplica. As
  7ª e 8ª horas do bancário são normais ou extras. Nada de novo se calcula;
  escolhe-se o caminho.

---

## 2. Como a consolidação foi feita

Três fontes, sem duplicação:

| Fonte | Marcas de origem |
|---|---:|
| Varredura dos blocos 02, 03 e 04 (tarefa 1) | 18 |
| Dúvidas da varredura, resolvidas pelo art. 611-B | 5 |
| § 10 de `02-base-normativa-verbas.md` (13 linhas → 15 parâmetros) | 15 |
| § 18 de `02a-adendo-lacunas-verbas.md` | 3 |
| **Total de marcas** | **41** |
| − sobreposição varredura × § 10 | −7 |
| − sobreposição dúvidas × § 10 | −2 |
| **Parâmetros distintos** | **32** |

A repartição em "novos" e "já cobertos" foi deliberadamente omitida: ela depende de
qual fonte se considera primeira, e qualquer ordem que se escolha é arbitrária. O que
não é arbitrário são as 41 marcas, as 9 sobreposições e os 32 distintos — e é isso
que o JSON permite recontar.

Cada parâmetro carrega `origem_consolidacao` com a lista das fontes em que apareceu.
É por ele que a tabela acima se reproduz. O teste
`test_consolidacao_nao_duplicou_parametros` verifica o essencial — ids únicos e as três
famílias de origem presentes —, não os totais; esses se recontam do JSON.

As 13 linhas do § 10 renderam 15 parâmetros porque duas se desdobram:

- **"7ª e 8ª horas em turno"** → `pn.jornada.turno-ininterrupto` (se o regime é turno
  de revezamento) e `pn.turno.setima-e-oitava-horas` (que natureza essas horas têm).
  São decisões independentes: o ACT Gasmig enquadra e, ainda assim, nega as extras.
- **"Base de cálculo da periculosidade"** → `pn.periculosidade.base` e
  `pn.periculosidade.percentual`. Base e percentual negociam-se separadamente.

---

## 3. A âncora da classificação: art. 611-B da CLT

A pergunta "o artigo diz *no mínimo*?" foi abandonada. Não é assim que se decide.
A âncora é o **art. 611-B da CLT**, rol taxativo do que não pode ser objeto de
convenção ou acordo coletivo **na forma de supressão ou redução**.

```
parâmetro alcançado por INCISO do art. 611-B   →  apenas-elevacao
parâmetro coberto pelo PARÁGRAFO ÚNICO          →  qualquer
demais                                          →  qualquer (Tema 1046/STF)
```

O parágrafo único é o que fecha o raciocínio: regras sobre **duração do trabalho e
intervalos** *não* são normas de saúde, higiene e segurança para este fim. Por isso
jornada, compensação, banco de horas, turno, sobreaviso e prontidão são negociáveis
em qualquer direção — inclusive para baixo.

### 3.1 De onde vem esta classificação

**Atenção, e isto não é detalhe:** o teor dos incisos abaixo, o número de trinta
incisos e a ressalva do § 3.3 vieram de **instrução direta do usuário deste bloco**.
**Não estão no corpus.** Quem auditar o inventário contra os arquivos do repositório
não vai encontrar o art. 611-B — vai encontrar esta declaração, e o bloco
`classificacao_611b.ORIGEM_DESTE_BLOCO` do catálogo, que diz o mesmo.

O corpus tem uma linha só: `02-base-normativa-verbas.md` § 2 *cita* o art. 611-B, sem
transcrever inciso algum.

Registrar a origem é o que separa "recebi um fundamento e o apliquei" de "inventei um
fundamento". O primeiro é legítimo; o segundo é o que este inventário existe para
evitar. Há teste prendendo a declaração —
`test_a_origem_da_classificacao_611b_e_declarada`.

Três incisos foram fornecidos:

| Inciso | Matéria | Parâmetros alcançados |
|---|---|---|
| **VI** | remuneração do trabalho noturno superior à do diurno | `pn.noturno.adicional`, `pn.he.adicional-noturna` |
| **XVII** | normas de saúde, higiene e segurança do trabalho | nenhum diretamente — ver § 3.3 |
| **XVIII** | adicional para atividades penosas, insalubres ou perigosas | `pn.insalubridade.base`, `pn.insalubridade.percentual`, `pn.periculosidade.base`, `pn.periculosidade.percentual` |

### 3.2 LACUNA declarada: 27 incisos não lidos

O art. 611-B tem trinta incisos — **número recebido por instrução, não lido**. O texto
integral não está no repositório; foi procurado, e está ausente também dos dois PDFs.
A regra do bloco — *não pesquise norma na web; se faltar fundamento, é pendência* —
impede a única outra saída.

Recitar trinta incisos de memória e apresentá-los como conferidos seria exatamente o
tipo de invenção que este inventário existe para evitar.

A consequência é mecânica, não decorativa: os **16 parâmetros** que nenhum dos três
incisos alcança receberam `fundamento_611b: "nao-mapeado"` e
`classificacao_provisoria: true`. O validador exige a correspondência nos dois
sentidos — provisório sem lacuna, ou lacuna sem provisório, quebra.

| `fundamento_611b` | Parâmetros | `alteracao` |
|---|---:|---|
| `inciso-VI` | 2 | apenas-elevacao |
| `inciso-XVIII` | 4 | apenas-elevacao |
| `paragrafo-unico` | 9 | qualquer |
| `derivado-nao-se-negocia` | 1 | derivado |
| `nao-mapeado` | **16** | provisória |

### 3.3 Ressalva do inciso XVII

Há decisão do TST aplicando o inciso XVII para invalidar cláusula sobre **jornada**
quando a extensão configura risco à saúde, com ressalva expressa de que o parágrafo
único não a salva. **O corte não é absoluto.**

*Origem: instrução, como o resto do § 3.1. Não há no corpus órgão, processo nem data,
e não foram pesquisados. A marca `ressalva_611b_xvii` sinaliza, hoje, um risco cuja
fonte não se pode citar numa memória de cálculo — obter a referência é pendência.*

Isso é mérito, não cálculo. O motor aplica a cláusula e registra; a nulidade é do
juízo. Os parâmetros de duração do trabalho carregam `ressalva_611b_xvii: true` para
que a memória de cálculo sinalize o ponto — sem que a classificação mude. O teste
`test_ressalva_do_inciso_XVII_nao_muda_o_calculo` prende essa separação.

---

## 4. As dúvidas da v1, resolvidas

| Dúvida da v1 | Resolução | Fundamento |
|---|---|---|
| Periculosidade — percentual | **apenas-elevacao** | inciso XVIII |
| Periculosidade — base de cálculo | **apenas-elevacao** | inciso XVIII |
| Insalubridade — percentual | **apenas-elevacao** | inciso XVIII |
| Insalubridade — base de cálculo | **apenas-elevacao** | inciso XVIII |
| Sobreaviso 1/3 e prontidão 2/3 | **qualquer** | parágrafo único — duração do trabalho |
| Dedução dos 6% do vale-transporte | **qualquer**, com `sustentacao_fraca` | Tema 1046 |
| Natureza da ajuda-alimentação | instância de `pn.composicao.natureza-de-verba` (§ 10) | Tema 1046 |
| Nº de passagens · 22 dias úteis | **continua fora** — defaults probatórios | — |

As dúvidas não estão numeradas de propósito: a v1 deste documento e o
`bloco-05-relatorio.md` § 4 as agrupavam de formas diferentes (um contava
periculosidade e insalubridade como quatro; o outro, como duas), e qualquer numeração
aqui conflitaria com uma das duas. Os nomes são inequívocos; os números não eram.

As quatro primeiras caem pelo mesmo motivo, e o motivo não é a redação: é a vedação
de reduzir. A ausência de "no mínimo" no texto do artigo é irrelevante.

**Uma dúvida nova, não resolvida:** a *gratificação de sala de controle*, citada no
enunciado, **não aparece em `02-base-normativa-verbas.md`**. A § 12, pendência 3,
fala genericamente em "IP 10.5 (PCCR) e demais Instruções de Pessoal referenciadas
no ACT — definem gratificações que integram base", sem nomeá-las. Não sei se é
parâmetro negociável, verba autônoma, ou instância de
`pn.composicao.natureza-de-verba`. Fica no relatório como dúvida, não no inventário
como palpite.

---

## 5. Parâmetros derivados

**Todo parâmetro que decorra de outro entra como derivado com a fórmula, nunca como
valor cadastrável.** O tratamento dado ao divisor na v1 foi generalizado: o campo
`derivacao` agora é geral, e `Catalogo.valida()` recusa `derivado_de` sem
`derivacao.formula`.

Por que não aceitar o derivado avulso: permitir o cadastro de jornada de 44h *com*
divisor 200 cria um par inconsistente que nenhuma validação posterior pega.

### 5.1 Derivado puro — `pn.jornada.divisor`

```
jornada_diária × 30                       (CLT art. 64)
(jornada_semanal ÷ dias_úteis) × 30       (Súmula 431/TST)
```

`sobrescrevivel: false`. Cláusula que fixe o divisor diretamente é **defeito de
cadastro**, não negociação. No ACT Gasmig a jornada de 40h faz o divisor cair para
200 sem que exista cláusula alguma sobre divisor — é o que
`test_act_gasmig_jornada_de_40h_implica_divisor_200` demonstra.

### 5.2 Derivado sobrescrevível — `pn.he.adicional-noturna`

```
((1 + noturno/100) × (1 + extraordinária/100) − 1) × 100
(1,20 × 1,50 − 1) × 100 = 80
```

`sobrescrevivel: true`. É o único. O ACT Gasmig fixa o adicional de HE noturna
**diretamente sobre a hora diurna**, em vez de compor os dois — § 10. Quando o
instrumento crava o valor, ele vence a derivação e a proveniência aponta a cláusula.

### 5.3 Ordem de avaliação

Derivados resolvem-se **depois** das suas entradas. Uma cláusula que mova
`pn.jornada.semanal` move o divisor sem tocá-lo.

---

## 6. Conflito normativo × defeito de cadastro

A distinção entrou no schema, seção `conflito_versus_defeito_de_cadastro`.

| | Conflito normativo | Defeito de cadastro |
|---|---|---|
| **Quando** | dois **instrumentos** com cláusula para a mesma tripla | duas cláusulas do **mesmo** instrumento com vigência sobreposta |
| **Natureza** | situação do mundo — sindicatos distintos | erro de quem cadastrou ou de quem leu |
| **Tratamento** | `cobertura = "conflito"`, lista completa dos candidatos | `ErroDeDados` — quebra |
| **Heurística** | **nenhuma** — nem o mais recente, nem o mais favorável | — |
| **Resultado** | `valor = null`, `calculavel = false` | exceção |

Tratar defeito de cadastro como conflito faria o motor devolver "conflito" para um
instrumento mal digitado, e alguém passaria o dia procurando o segundo sindicato que
não existe.

---

## 7. Decisões de comportamento (aprovadas)

**R18 rejeita sem corrigir.** Cláusula abaixo do piso legal é rejeitada e registrada;
o resolvedor devolve o default com `sem-cobertura-coletiva`. Corrigir silenciosamente
para o piso esconderia defeito do instrumento cadastrado ou erro de leitura.

**Título judicial não é barrado pelo piso.** R16 põe o título acima de tudo. Título
que fixe adicional abaixo do piso é aplicado, com a divergência registrada. Aplicar
a lei contra o título é competência do juízo, não do motor.

---

## 8. O inventário

Legenda de `alteracao`: **↑** apenas-elevacao · **↔** qualquer · **ƒ** derivado.
`611-B`: **VI** · **XVIII** · **¶** parágrafo único · **—** não mapeado (provisório).

### 8.1 Jornada e horas extras

| id | nome | default legal | fonte | tipo | 611-B | alt |
|---|---|---|---|---|---|---|
| `pn.he.adicional` | Adicional de HE diurnas | 50 | CF art. 7º, XVI | substituição | — | ↑ |
| `pn.he.adicional-domingos-feriados` | Adicional de HE em domingos e feriados | 50 | CF art. 7º, XVI | substituição | — | ↑ |
| `pn.he.adicional-noturna` | Adicional de HE noturna | 80 | CLT art. 73 + CF art. 7º, XVI | substituição | VI | ↑ ƒ* |
| `pn.he.regime-de-compensacao` | Regime de compensação | sem-compensacao-limite-diario | CF art. 7º, XIII | variante | ¶ | ↔ |
| `pn.he.banco-de-horas` | Banco de horas | sem-banco | CLT art. 59 | variante | ¶ | ↔ |
| `pn.jornada.semanal` | Duração semanal | 44 | CF art. 7º, XIII | substituição | ¶ | ↔ |
| `pn.jornada.divisor` | Divisor do salário-hora | 220 | CLT art. 64; Súm. 431; IRR-849 | substituição | ƒ | ƒ |
| `pn.jornada.sabado-como-rsr` | Sábado como RSR (bancário) | sabado-nao-e-rsr | IRR-849, tese do sábado; Súm. 124 em redação anterior† | variante | ¶ | ↔ |
| `pn.jornada.turno-ininterrupto` | Enquadramento em turno de revezamento | nao-enquadrado | CF art. 7º, XIV; Súm. 423; OJ 396 | variante | ¶ | ↔ |
| `pn.turno.setima-e-oitava-horas` | Natureza da 7ª e 8ª horas em turno | extras | CF art. 7º, XIV; Súm. 423 | variante | ¶ | ↔ |
| `pn.bancario.enquadramento-224` | Gratificação de função ≥ 1/3 | sem-gratificacao-7a-e-8a-sao-extras | Súm. 102, II, III, IV, VI e VII* | variante | ¶ | ↔ |
| `pn.sobreaviso.fator` | Fator do sobreaviso | 1/3 | CLT art. 244, § 2º; Súm. 229 | substituição | ¶ | ↔ |
| `pn.prontidao.fator` | Fator da prontidão | 2/3 | CLT art. 244, § 3º | substituição | ¶ | ↔ |
| `pn.in-itinere.prefixacao` | Prefixação de horas in itinere | apuracao-real | CLT art. 58, § 2º (revogado em 11/11/2017) | variante | — | ↔ |

\* derivado **sobrescrevível** — § 5.2.

### 8.2 RSR e feriados

| id | nome | default legal | fonte | tipo | 611-B | alt |
|---|---|---|---|---|---|---|
| `pn.rsr.dias` | Dias de RSR | 1 | CLT art. 67; Lei 605/49 | substituição | — | ↑ |
| `pn.rsr.feriados-no-reflexo` | Feriados no reflexo de HE sobre o RSR | apenas-rsr | manual 6.6.6.1, p. 43 | composição | — | ↑ |
| `pn.feriado-12x36.criterio` | Critério do feriado laborado em 12×36 | **sem default** | divergência jurisprudencial não resolvida | variante | — | ↔ |

### 8.3 Adicionais de risco

| id | nome | default legal | fonte | tipo | 611-B | alt |
|---|---|---|---|---|---|---|
| `pn.insalubridade.base` | Base da insalubridade | salario-minimo | CLT art. 192; SV 4; **Rcl 6.275** | variante | XVIII | ↑ |
| `pn.insalubridade.percentual` | Percentual da insalubridade | 20 | CLT art. 192 | substituição | XVIII | ↑ |

† A Súmula 124 na **redação vigente** (Res. 219/2017, § 8 da base normativa) trata só
dos divisores 180/220 e **não menciona o sábado**. Quem trata do sábado é a tese do
IRR-849 e a redação anterior da súmula. A primeira versão desta tabela apontava a
redação nova — corrigido.

‡ A tabela por grau de insalubridade (leve 10 / médio 20 / máximo 40) **foi removida**
do catálogo: os percentuais de grau leve e máximo não estão em lugar nenhum do corpus,
e a citação que os sustentava não correspondia a nenhum texto real. O único percentual
que o corpus traz é o grau médio, 20%. Reintroduzir só com a fonte.
| `pn.periculosidade.base` | Base da periculosidade | salario-base | CLT art. 193; Súm. 191 | variante | XVIII | ↑ |
| `pn.periculosidade.percentual` | Percentual da periculosidade | 30 | CLT art. 193 | substituição | XVIII | ↑ |
| `pn.noturno.adicional` | Adicional noturno | 20 | CLT art. 73; CF art. 7º, IX | substituição | VI | ↑ |

**Correção do catálogo anterior:** a variante `salario-basico` de
`pn.insalubridade.base` **foi removida**. A v1 registrava a SV 4 como "suspensa" pela
Rcl 6.275. `02-base-normativa-verbas.md` § 5 mostra que a **Súmula** foi **cassada
definitivamente em abril de 2018**. A variante não existe mais.

### 8.4 Transferência e comissões

| id | nome | default legal | fonte | tipo | 611-B | alt |
|---|---|---|---|---|---|---|
| `pn.transferencia.adicional` | Adicional de transferência | 25 | CLT art. 469, § 3º | substituição | — | ↑ |
| `pn.transferencia.base` | Base do adicional de transferência | **sem default** | art. 469, § 3º — "salários que percebia naquela localidade" | variante | — | ↔ |
| `pn.comissionista.adicional-he` | Adicional de HE do comissionista | 50 | Súmula 340/TST | substituição | — | ↑ |
| `pn.comissoes.periodo-da-media` | Período da média de comissões | 12 | CLT art. 142, § 3º; OJ 181 | substituição | — | ↔ |
| `pn.comissoes.forma-de-correcao` | Correção monetária da média | indices-debitos-trabalhistas | OJ 181/SDI-I | variante | — | ↔ |

### 8.5 Composição, férias, rescisão e parcelas convencionais

| id | nome | default legal | fonte | tipo | 611-B | alt |
|---|---|---|---|---|---|---|
| `pn.composicao.natureza-de-verba` | Verba integra ou não a base | natureza-legal | CLT arts. 457 e 458 | composição | — | ↔ |
| `pn.ferias.particao` | Períodos de fracionamento das férias | 2 | CLT art. 134 | substituição | — | ↔ |
| `pn.aviso.proporcionalidade` | Tabela do aviso-prévio | 30 + 3 × anos, teto 90 | Lei 12.506/11; NT 184/12 | substituição | — | ↑ |
| `pn.ajuda-alimentacao.valor` | Valor da ajuda-alimentação | **sem default** | parcela exclusivamente convencional | substituição | — | ↔ |
| `pn.vale-transporte.deducao-6pct` | Dedução dos 6% no VT | com-deducao-6pct | Dec. 95.247/87, arts. 9º e 12 | variante | — | ↔ |

`pn.vale-transporte.deducao-6pct` carrega `sustentacao_fraca: true`: a divergência que
o manual registra é governada pelo **título**, não por norma coletiva. Entrou porque
nada impede que um instrumento disponha sobre a dedução — mas o caso de uso provável
não é esse.

**Não são parâmetros** e ficaram deliberadamente de fora: o número de passagens
diárias e a base de 22 dias úteis do vale-transporte. São *defaults probatórios* — o
que se presume quando a prova falha —, não cláusulas negociáveis.

---

## 9. O que o ACT Gasmig preenche

Fixture: [`tests/fixtures/calculo/instrumentos-act-gasmig.json`](../../tests/fixtures/calculo/instrumentos-act-gasmig.json).
**Real e parcial.** Todos os valores vêm de `02-base-normativa-verbas.md`. Nenhum foi
inventado.

| parâmetro | valor Gasmig | default legal |
|---|---|---|
| `pn.jornada.semanal` | **40** | 44 |
| `pn.jornada.divisor` | *(derivado → 200)* | 220 |
| `pn.he.adicional-domingos-feriados` | **100** | 50 |
| `pn.jornada.turno-ininterrupto` | **enquadrado** (6h + 7ª/8ª; módulos 6×4 e 21×14; média 36h) | não enquadrado |

A variante chamava-se `enquadrado-sexta-diaria-divisor-180`. O nome embutia uma
consequência de **divisor** que (a) é parâmetro derivado e não pode viver dentro de
uma variante, e (b) contradiz o corpus no caso concreto — a § 8 diz que 40 horas
semanais implicam divisor **200**, e a Gasmig tem 40h. Os 180 valem para a jornada de
6 horas do manual 6.6.3, não para todo turno enquadrado. Corrigido, e há teste
(`test_nenhuma_variante_embute_um_derivado`) impedindo a recaída.
| `pn.turno.setima-e-oitava-horas` | **normais** | extras |
| `pn.ferias.particao` | **3** | 2 |
| `pn.he.banco-de-horas` | **banco-convencional** (quitação trimestral) | sem banco |

`pn.turno.setima-e-oitava-horas = normais` é o **ponto de maior litígio do ACT**, e é
exatamente onde a ressalva do inciso XVII (§ 3.3) pode incidir. O motor aplica a
cláusula e registra a divergência com o default. A nulidade é do juízo.

### 9.1 O que ficou sem valor completo

| parâmetro | o que se sabe | o que falta |
|---|---|---|
| `pn.he.adicional` | 80% / 75% / 60% "por período" | **os intervalos de competência de cada faixa** |
| `pn.he.adicional-noturna` | percentual direto sobre a hora diurna | o percentual |
| *gratificação de sala de controle* | nada — a expressão não está no documento | tudo |
| *contribuição negocial* | a § 7 diz que o ACT usa o adicional de periculosidade como base | percentual, destinação, direito de oposição — e uma **camada de descontos**, que não existe |
| `pn.jornada.sabado-como-rsr` | o ACT mantém o sábado como dia útil remunerado | a confirmação: a § 8 manda "registrar como ponto a confirmar, não como conclusão" |

As três faixas de HE **não foram cadastradas**. Três cláusulas do mesmo parâmetro sem
`vigencia_propria` se sobrepõem, e sobreposição no mesmo instrumento é defeito de
cadastro (§ 6). Inventar as datas seria pior — elas determinam qual percentual rege
cada competência, e a ordem no documento é *descendente*, o que é incomum numa
progressão temporal e reforça que a leitura não pode ser suposta.

O preço está medido e é alto: enquanto faltarem, a categoria resolve o adicional de
HE pelo **default legal de 50%**, contra 60% a 80% reais. O teste
`test_act_gasmig_tres_faixas_de_he_declaradas_sem_datas` afirma isso.

A `vigencia` do instrumento tem as duas pontas **nulas**: o rótulo "2025/2027" sugere
o biênio, mas o **mês-base não consta** do documento e não foi suposto.

### 9.2 Duas divergências entre o enunciado e o documento

1. O enunciado aponta a **seção 3** como fonte dos valores. A seção 3 é *Horas in
   itinere* e não traz valor algum do ACT. Os **valores** estão nas **seções 8, 9 e,
   principalmente, na coluna "Observação" da tabela da seção 10**. As seções 7 e 12
   trazem contexto — base da periculosidade, sindicatos —, não valores de cláusula.
2. A **cláusula 2.1.1** (extensão a categorias cujo sindicato não negociou) é citada
   no enunciado do bloco 5, mas **não aparece** em `02-base-normativa-verbas.md`. A
   categoria estendida ficou `null` — assim não alcança ninguém, que é o comportamento
   correto enquanto o dado falta.

Ambas registradas na própria fixture, em `divergencia_de_referencia` e
`categorias_por_extensao`.

---

## 10. Pendências que restam

| # | Pendência | Efeito |
|---|---|---|
| 1 | **27 incisos do art. 611-B** não lidos | 16 parâmetros com classificação provisória |
| 2 | Intervalos das três faixas de HE do ACT | o parâmetro de maior uso resolve 50% em vez de 60–80% |
| 3 | Percentual da HE noturna do ACT | `derivacao.sobrescrevivel` não é exercitado com dado real |
| 4 | Mês-base do ACT | vigência nula — o instrumento vale para qualquer competência |
| 5 | Identificador real de categoria (`gasmig-sitramico` é rótulo desta extração) | a fixture não liga a contrato real |
| 6 | Cláusula 2.1.1 e a categoria estendida | R17 não é exercitada com dado real |
| 7 | Gratificação de sala de controle | dúvida aberta de classificação |
| 8 | ACT integral fora do repositório | o que existe é a leitura que a base normativa faz dele |
| 9 | **Camada de presets de cálculo** — os dois presets de direito intertemporal (`TRAB-INTERTEMP-TEMPUS` × `TRAB-INTERTEMP-ULTRATIVO`) não têm onde morar | nenhum ponto do motor sabe qual regra aplicar antes de 11/11/2017. Não é parâmetro negociável; é pendência de modelagem — `pendencias.md` § 15.5 |
| 10 | **Camada de descontos** — a contribuição negocial do ACT não tem parâmetro | desconto do ACT não modelado |

---

## 11. Ver também

- [`tabelas-normativas/camada-norma-coletiva-schema.json`](tabelas-normativas/camada-norma-coletiva-schema.json) — schema v2.0: R14–R18, derivação, conflito × defeito, 611-B
- [`tabelas-normativas/camada-norma-coletiva-catalogo.json`](tabelas-normativas/camada-norma-coletiva-catalogo.json) — os 32 parâmetros
- [`extracao/bloco-05-relatorio.md`](extracao/bloco-05-relatorio.md) — relatório do bloco
- `scripts/calculo/valida_parametros.py` — validador e resolvedor
- `scripts/calculo/test_valida_parametros.py` — **nenhum skip**; a contagem por arquivo está em
  [`consolidado/00-numeros.md`](consolidado/00-numeros.md) § 5, gerado por script
