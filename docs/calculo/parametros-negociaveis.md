# Parâmetros negociáveis — inventário

Pontos do cálculo de verbas que **norma coletiva, acordo individual ou definição contratual
podem alterar**. Sem este inventário o motor de verbas não pode ser escrito: cada fórmula
extraída nos blocos 02 a 04 tem constantes que não são constantes.

> ## ⚠ Inventário parcial — falta a seção 10 de `02-base-normativa-verbas.md`
>
> A Tarefa 2 deste bloco mandava cruzar a varredura com **os 13 parâmetros da seção 10 de
> `02-base-normativa-verbas.md`**. **Esse arquivo não está no repositório.** Só chegou o
> adendo `02a-adendo-lacunas-verbas.md`, que se declara complemento dele
> ("Fecha os seis pontos da seção 11 de `02-base-normativa-verbas.md`").
>
> O que está abaixo é **a varredura própria dos blocos 02, 03 e 04, mais os três parâmetros
> da seção 18 do adendo**. A unificação com os 13 da seção 10 **não foi feita** — não posso
> nem somá-los nem deduplicá-los sem vê-los.
>
> O inventário está estruturado para que essa fusão seja mecânica: cada parâmetro tem `id`,
> verba afetada, fonte e o texto literal que sustenta a classificação. Ver
> `extracao/bloco-05-relatorio.md` § 1.

---

## 1. Como ler

Cada parâmetro tem:

| Campo | Significado |
|---|---|
| `id` | Chave estável, usada pela camada de resolução |
| **verba(s)** | O que muda de valor se o parâmetro mudar |
| **default legal** | Valor aplicado quando não há instrumento coletivo (R14) |
| **fonte** | De onde vem o default |
| **tipo** | `substituicao-de-valor` · `alteracao-de-composicao` · `chave-de-variante` |
| **alteração** | `apenas-elevacao` (há piso legal, R18) ou `qualquer` |
| **derivado-de** | Quando o valor não é negociado diretamente, mas calculado de outro |

**Os três tipos:**

- **`substituicao-de-valor`** — troca um número. O adicional de 50% vira 80%. A fórmula não
  muda; muda o operando.
- **`alteracao-de-composicao`** — uma verba passa a integrar, ou deixa de integrar, uma base
  de cálculo. A fórmula muda de argumentos.
- **`chave-de-variante`** — seleciona **qual regra já implementada** se aplica. As 7ª e 8ª
  horas do bancário são normais ou extras. Nada de novo se calcula; escolhe-se o caminho.

---

## 2. Inventário

### 2.1 Horas extras e jornada

#### `pn.he.adicional`

| | |
|---|---|
| **Nome** | Adicional de horas extras |
| **Verbas** | Horas extras · intervalo intrajornada suprimido · intervalo interjornada · intervalos especiais (arts. 72, 229, 253, 298, 384) · horas *in itinere* |
| **Default legal** | **50%** |
| **Fonte** | CF art. 7º; CLT art. 444 |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` — piso de 50% |

> "Adicional **superior a 50%** se houver **norma infralegal mais favorável ao empregado** —
> CLT art. 444" (bloco 03, § 6.4; manual 6.6.4, p. 39).

**O valor pode ser plural.** O manual trata a hipótese diretamente:

> "No caso da CCT prever **dois ou mais adicionais** (exemplo: 50% p/ as duas primeiras horas
> extras e 80% para as demais), os cálculos também devem ser feitos separadamente, em colunas
> próprias […] para **viabilizar o cálculo das médias**" (manual 6.6.4, p. 39).

Não é um segundo parâmetro: é o **mesmo** parâmetro com valor em faixas por posição na
jornada. A exigência de colunas separadas tem razão substantiva — *médias físicas por
adicional distinto não podem ser fundidas*, e é isso que alimenta os reflexos em 13º, férias
e aviso.

**Atenção:** a hora extra **noturna** de 80% **não é** um valor deste parâmetro. É o produto
`1,20 × 1,50 = 1,80` — derivado de `pn.he.adicional` e `pn.noturno.adicional`.

#### `pn.he.regime-de-compensacao`

| | |
|---|---|
| **Nome** | Regime de compensação de jornada |
| **Verbas** | Horas extras |
| **Default legal** | Sem compensação — extras acima da **8ª (ou 6ª) diária** |
| **Fonte** | CF art. 7º, XIII |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> "Havendo **compensação de horários mediante acordo ou CCT** (CF, art. 7º, XIII), serão HE
> aquelas laboradas além da **44ª semanal**" (manual 6.6.5, p. 40).

Seleciona entre duas apurações já descritas no corpus — diária e semanal. Note a interação
com a regra da comparação: quando o título defere "excedentes da 8ª diária **ou** da 44ª
semanal", apuram-se as duas e adota-se a maior (bloco 03, § 6.5.2). São coisas distintas —
aqui é **qual regime rege**, lá é **qual resultado prevalece**.

#### `pn.jornada.semanal`

| | |
|---|---|
| **Nome** | Duração semanal do trabalho |
| **Verbas** | Todas as que usam divisor |
| **Default legal** | **44 horas** |
| **Fonte** | CF art. 7º, XIII |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `qualquer` — redução é lícita e comum |

#### `pn.jornada.divisor` — **DERIVADO**

| | |
|---|---|
| **Nome** | Divisor do salário-hora |
| **Derivado de** | `pn.jornada.semanal` e da jornada diária |
| **Default legal** | 220 (8h/44h) · 200 (40h) · 180 (6h) · 150 (5h) · 120 (4h) · 210 (7h e 12×36) · **240 antes da CF/88** |
| **Fonte** | CLT art. 64; Súmula 431/TST; IRR-849, teses 3, 5 e 6 |
| **Tipo** | `substituicao-de-valor` (derivado) |
| **Alteração** | não se negocia diretamente |

> IRR-849, tese 3: o divisor sai da regra geral do **art. 64 da CLT** — jornada normal × 30.
> Tese 6: havendo **redução da duração semanal**, o divisor vem da **Súmula 431** —
> `30 × (horas semanais ÷ dias úteis)`.

**Não é parâmetro próprio, e registrar como tal seria erro.** Uma CCT que reduza a jornada
para 40h move o divisor para 200 por consequência, não por cláusula. O motor deve **derivar**,
não aceitar divisor avulso — sob pena de aceitar um par (jornada, divisor) inconsistente.

A exceção é o divisor **210** da 12×36, que vem da OJ 23 das Turmas do TRT-3 e não da fórmula
do art. 64 — é atribuído ao regime, não derivado da jornada.

#### `pn.jornada.sabado-como-rsr`

| | |
|---|---|
| **Nome** | Sábado como dia de repouso remunerado (bancário) |
| **Verbas** | Horas extras de bancário |
| **Default legal** | Sábado **não** é RSR |
| **Fonte** | Súmula 124, I/TST |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> Súmula 124, I: "se houver **ajuste individual expresso ou coletivo** no sentido de
> considerar o sábado como dia de descanso remunerado" — divisor 150 (6h) ou 200 (8h).

> **Duas correntes, as duas registradas:**
>
> | Corrente | Efeito |
> |---|---|
> | **Súmula 124, I** (2012) | Ajuste coletivo sobre o sábado **altera** o divisor: 150 / 200 |
> | **IRR-849, tese 4** (2016) | "A inclusão do sábado como RSR **não altera o divisor**, por não haver redução do número de horas semanais, trabalhadas e de repouso" |
>
> O IRR-849 é de observância obrigatória e **esvazia na prática** os divisores 150 e 200,
> mas o manual registra que a Súmula 124 não foi revista. Ver bloco 03, P12.
>
> A modulação do IRR importa: aplica-se às sentenças "transitadas em julgado, **ainda em fase
> de liquidação, desde que silentes quanto ao divisor**".

#### `pn.jornada.turno-ininterrupto`

| | |
|---|---|
| **Nome** | Enquadramento em turno ininterrupto de revezamento |
| **Verbas** | Horas extras |
| **Default legal** | Não enquadrado |
| **Efeito** | Extras acima da **6ª diária**, divisor **180** |
| **Fonte** | OJ 396/SDI-I/TST; Súmulas 2 e 38 do TRT-3 (manual 6.6.3, p. 37) |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> **Lacuna de fundamento.** O corpus estabelece o **efeito** do enquadramento, mas **não
> contém** a autorização constitucional para a elevação da jornada do turno por negociação
> coletiva (CF art. 7º, XIV, parte final). Não pesquisei fora do corpus. Pendência **D1**.

#### `pn.bancario.enquadramento-224`

| | |
|---|---|
| **Nome** | Gratificação de função do bancário ≥ 1/3 do salário |
| **Verbas** | Horas extras de bancário — 7ª e 8ª horas |
| **Default legal** | Sem gratificação: 7ª e 8ª horas são **extras** |
| **Efeito** | Com gratificação ≥ 1/3 (art. 224, § 2º): **já remuneradas**, não são extras |
| **Fonte** | Súmula 102, II, III, IV, VI e VII/TST |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> Texto do índice do manual: "A gratificação de função de bancários, incluída no § 2º do art.
> 224, **não inferior a 1/3 do salário já remunera a 7ª e 8ª horas**, enquanto a gratificação
> igual ou superior a 1/3 recebida pelo **caixa**, mesmo que caixa executivo, apenas remunera
> a maior responsabilidade do cargo e **não** as duas horas extras além da sexta."

> **Sustentação fraca, registrada como tal.** A regra aparece **apenas na linha de índice** do
> item 6.6.1; o manual não a desenvolve em item próprio. É um dos verbetes ◆ da pendência P13
> do bloco 3. A classificação é segura; a proveniência é magra.

#### `pn.rsr.dias`

| | |
|---|---|
| **Nome** | Número de dias de repouso semanal remunerado |
| **Verbas** | RSR · reflexo de HE no RSR · reflexo do adicional noturno no RSR · reflexo de comissões no RSR |
| **Default legal** | Um por semana, preferencialmente ao domingo |
| **Fonte** | CLT art. 67; Lei 605/49 |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` — a tese fala em **ampliação** |

> **IRR-849, tese 1, decidida por unanimidade:** "O número de dias de repouso semanal
> remunerado **pode ser ampliado por convenção ou acordo coletivo de trabalho**, como
> decorrência do exercício da **autonomia sindical**."

Este parâmetro alimenta o denominador do critério técnico do reflexo em RSR
(`valor × nº_RSR / dias_úteis`) e, por consequência, quatro verbas.

> **Interação com `pn.jornada.sabado-como-rsr`, e é sutil.** Ampliar o número de dias de RSR
> (tese 1) **é** possível; mas fazê-lo **não altera o divisor** (tese 4). São duas
> consequências separadas do mesmo fato negocial.

#### `pn.rsr.feriados-no-reflexo`

| | |
|---|---|
| **Nome** | Inclusão dos feriados no reflexo de HE sobre o RSR |
| **Verbas** | Reflexo de horas extras no RSR |
| **Default legal** | **Não** — "RSR não se confunde com feriados" |
| **Fonte** | Manual 6.6.6.1, p. 43 |
| **Tipo** | `alteracao-de-composicao` |
| **Alteração** | `apenas-elevacao` — a norma precisa **favorecer** o empregado |

> "Os feriados apenas serão incluídos **quando a sentença determinar ou existir disposição em
> norma coletiva que favoreça o empregado**, visto que RSR não se confunde com feriados."

Limite de coisa julgada, do acórdão transcrito (TRT-3, AP 0001624-31.2012.5.03.0010):
sentença que defere reflexo em RSR "não pode ser interpretada extensivamente para contemplar
a inclusão também dos feriados".

#### `pn.feriado-12x36.criterio`

| | |
|---|---|
| **Nome** | Critério de cálculo do feriado laborado em jornada 12×36 |
| **Verbas** | Feriado trabalhado sem folga compensatória |
| **Default legal** | **Nenhum** — divergência não resolvida |
| **Fonte** | Manual 6.5, p. 34–35 |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> **Duas correntes, transcritas pelo manual sem escolha:**
>
> | Variante | Cálculo |
> |---|---|
> | `salario-dia-dobrado` | `remuneração_mensal / 30 × 2` — TRT-3, 9ª Turma, AP 0001138-58.2012.5.03.0103 |
> | `salario-hora-com-100` | `salário-hora × horas laboradas × 2` — TRT-3, 3ª Turma, AP 0001215-11.2012.5.03.0057 |

> Instrução do manual: na ausência de parâmetros no comando sentencial, analisar o pedido
> inicial, como a reclamada pagava os feriados durante o contrato e a **previsão em
> instrumento coletivo**.
>
> O manual **desautoriza o próprio critério** proposto: "constitui apenas um critério de
> cálculo, visto que ainda **não há consenso jurisprudencial** acerca da matéria".

### 2.2 Adicionais

#### `pn.insalubridade.base`

| | |
|---|---|
| **Nome** | Base de cálculo do adicional de insalubridade |
| **Verbas** | Adicional de insalubridade e todos os seus reflexos |
| **Default legal** | **Salário mínimo** |
| **Fonte** | Súmula 46 do TRT-3 (RA 224/2015); CLT art. 192 |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `apenas-elevacao` — "critério **mais vantajoso**" |

> Súmula 46 do TRT-3: "A base de cálculo do adicional de insalubridade é o **salário
> mínimo**, enquanto não sobrevier lei dispondo de forma diversa, **salvo critério mais
> vantajoso para o trabalhador estabelecido em norma coletiva, condição mais benéfica ou em
> outra norma autônoma aplicável**."
>
> Conclusão operacional do manual: "exceto disposição mais benéfica **específica** em
> instrumento coletivo". A palavra *específica* é operacional — cláusula genérica de
> melhoria não basta.

> **Ponto de maior instabilidade do capítulo 6.** Variantes que o motor precisa carregar:
>
> | Variante | Fonte | Situação |
> |---|---|---|
> | `salario-minimo` | Súmula 46 do TRT-3 | **default** |
> | `salario-basico` | Súmula 228/TST, Res. 148/2008 | **eficácia suspensa** por liminar do STF na Rcl 6266 |
> | `piso-nacional-de-salarios` | DL 2351/87 | só de 09/87 a 07/89 |
> | `salario-profissional` | Súmula 17/TST, restaurada pela Res. 121/03 | hipótese específica |
> | `base-convencional` | Norma coletiva mais vantajosa | Súmula 46, parte final |
>
> A vigência da Súmula 46 após 2018 é a pendência 3 da seção 19 do adendo.

#### `pn.insalubridade.percentual`

| | |
|---|---|
| **Nome** | Percentual do adicional de insalubridade |
| **Verbas** | Adicional de insalubridade e reflexos |
| **Default legal** | **10, 20 ou 40%**, conforme o grau apurado |
| **Fonte** | CLT art. 192 |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` |

> "É apurado à razão de 10, 20, 40% **ou outro percentual previsto em norma infralegal mais
> favorável ao empregado**" (manual 6.11.1, p. 59).

O **grau** (leve, médio, máximo) não é negociável — decorre de perícia. O que a norma pode
elevar é o **percentual associado ao grau**.

#### `pn.noturno.adicional`

| | |
|---|---|
| **Nome** | Adicional noturno |
| **Verbas** | Adicional noturno · hora extra noturna (produto) · reflexos |
| **Default legal** | **20%** urbano · **25%** rural |
| **Fonte** | CLT art. 73; CF art. 7º, IX |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` — "**no mínimo**" |

> "Corresponde ao acréscimo de **no mínimo 20%** sobre o valor da hora diurna" (manual
> 6.11.4, p. 61). Para o rural, "a hora efetivamente trabalhada em horário noturno é
> acrescida de **25% no mínimo**" (6.11.4.3, p. 63).

**O piso é por categoria**, não único. A ficção legal da hora noturna (fator 1,142857143) é
regra de contagem, **não parâmetro negociável** — e não se aplica a rurais nem a portuários.

#### `pn.transferencia.adicional`

| | |
|---|---|
| **Nome** | Adicional de transferência |
| **Verbas** | Adicional de transferência e reflexos |
| **Default legal** | **25%** |
| **Fonte** | CLT art. 469, § 3º |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` — "**nunca inferior a**" |

> Art. 469, § 3º: pagamento suplementar "**nunca inferior a 25%** dos salários que o
> empregado percebia naquela localidade, **enquanto durar essa situação**".

Origem: seção 18 do adendo `02a`. Confirmado no corpus — a mesma expressão aparece na lista
do MTE reproduzida no manual (6.13.4, p. 70).

**Salário-condição**: devido enquanto durar a transferência. Não se projeta após o retorno.

#### `pn.transferencia.base`

| | |
|---|---|
| **Nome** | Base de cálculo do adicional de transferência |
| **Verbas** | Adicional de transferência |
| **Default legal** | **Divergente** — não há default pacificado |
| **Fonte** | CLT art. 469, § 3º — "salários que o empregado percebia naquela localidade" |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> Variantes: `salario-base` × `remuneracao`. O adendo registra que **o próprio TRT-3 já
> decidiu pela remuneração**. Registrar como variante, não resolver (adendo `02a`, § 17).

Origem: seção 18 do adendo.

### 2.3 Comissões

#### `pn.comissionista.adicional-he`

| | |
|---|---|
| **Nome** | Adicional de hora extra do comissionista |
| **Verbas** | Horas extras de comissionista (só o adicional é devido) |
| **Default legal** | **50%** |
| **Fonte** | Súmula 340/TST |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` — "**no mínimo**" |

> Súmula 340: "tem direito ao adicional de, **no mínimo, 50%** pelo trabalho em horas extras,
> calculado sobre o valor-hora das comissões recebidas no mês, considerando-se como divisor
> o número de horas **efetivamente trabalhadas**" (adendo `02a`, § 16).

Origem: seção 18 do adendo.

> **Não confundir com `pn.he.adicional`.** São dois parâmetros porque incidem sobre bases e
> divisores diferentes — aqui o divisor é o número de horas efetivamente trabalhadas, não
> 220. Uma CCT pode elevar um e não o outro.

#### `pn.comissoes.periodo-da-media`

| | |
|---|---|
| **Nome** | Período de apuração da média de comissões |
| **Verbas** | Reflexo de comissões em férias · 13º · aviso-prévio · verbas rescisórias |
| **Default legal** | **12 meses** anteriores à concessão |
| **Fonte** | CLT art. 142, § 3º; OJ 181/SDI-I/TST |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | **`qualquer`** |

> O manual repete a ressalva em três itens:
>
> - 6.2, p. 23: "alguns documentos coletivos de trabalho […] estabelecem **prazo inferior**
>   para apuração da média";
> - 6.4, p. 29: "alguns instrumentos normativos estabelecem um **intervalo menor** para a
>   apuração da média";
> - 6.12, p. 67: "algumas normas coletivas […] estabelecem **prazo inferior** para apuração
>   da média".

> **A classificação como `qualquer`, e não `apenas-elevacao`, é deliberada.** O manual fala
> em prazo **inferior**, e prazo menor não é necessariamente mais favorável: depende de as
> comissões estarem subindo ou caindo no período. Não há piso a defender aqui.

#### `pn.comissoes.forma-de-correcao`

| | |
|---|---|
| **Nome** | Forma de correção monetária das comissões para a média |
| **Verbas** | Mesmas do anterior |
| **Default legal** | Correção monetária pelos índices de débitos trabalhistas |
| **Fonte** | OJ 181/SDI-I/TST |
| **Tipo** | `chave-de-variante` |
| **Alteração** | `qualquer` |

> "alguns documentos coletivos de trabalho **fixam a forma de correção das comissões**"
> (manual 6.2, p. 23; repetido em 6.12, p. 67).

### 2.4 Demais verbas

#### `pn.aviso.proporcionalidade`

| | |
|---|---|
| **Nome** | Tabela de proporcionalidade do aviso-prévio |
| **Verbas** | Aviso-prévio · projeção sobre doze avos de férias e 13º · reflexos |
| **Default legal** | `30 + 3 × anos_completos`, teto de **90 dias** |
| **Fonte** | Lei 12.506/11; Nota Técnica 184/12/CGRT/SRT/MTE |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `apenas-elevacao` |

> Nota Técnica 184/12, item 7: "As cláusulas pactuadas em acordos ou convenções coletivas
> acerca de aviso prévio proporcional **continuam válidas, desde que respeitada a
> proporcionalidade mínima prevista na Lei 12.506/11**."

**Parâmetro de alto alavancamento.** Um dia a mais de projeção pode valer **1/12 inteiro** de
férias e de 13º — o manual demonstra o efeito em três itens (bloco 03, §§ 2.3, 3.5 e 4).
O piso da R18 aqui não é um número, é **uma tabela inteira**: cada ponto da curva negociada
tem de ser ≥ o ponto correspondente da legal.

#### `pn.ajuda-alimentacao.valor`

| | |
|---|---|
| **Nome** | Valor unitário da ajuda-alimentação |
| **Verbas** | Ajuda-alimentação e indenização substitutiva |
| **Default legal** | **NÃO EXISTE** |
| **Fonte** | Exclusivamente convencional |
| **Tipo** | `substituicao-de-valor` |
| **Alteração** | `qualquer` |

> O manual identifica a origem na própria planilha: a coluna do exemplo é rotulada "Vr.
> Unitário ajuda alimentação, **conforme CCT**" (bloco 04, detalhe § 12; manual 6.13.7,
> p. 75).

> ### Este parâmetro quebra o padrão da R14, e o schema precisa suportar isso
>
> R14 diz que a ausência de norma coletiva cadastrada **não é erro** — é *fallback* para o
> default legal. **Aqui não há default legal para onde cair.** Sem instrumento, a verba é
> **incalculável**, não calculável-com-marcação.
>
> O schema trata isso com `default_legal: null` e `sem_default: true`, e a resolução devolve
> `cobertura: "sem-default-legal"` em vez de um valor. É diferente de erro: a conta pode
> prosseguir nas demais verbas e esta fica pendente de dado.

---

## 3. Parâmetros identificados mas **não classificados** — vão ao relatório, não ao inventário

A regra do bloco: parâmetro que não consiga classificar com segurança vira dúvida, não
palpite. Estes seis estão em `extracao/bloco-05-relatorio.md` § 4:

| Candidato | Por que não entrou |
|---|---|
| Adicional de periculosidade — 30% | O manual escreve "**devido na base de 30%**", sem "no mínimo" nem "nunca inferior". Não pude confirmar pelo corpus que é piso elevável |
| Sobreaviso — 1/3 · Prontidão — 2/3 | "à razão de", sem expressão de piso. Mesma razão |
| Dedução dos 6% do vale-transporte | A divergência que o manual registra é sobre o **comando exequendo**, não sobre norma coletiva |
| Natureza da ajuda-alimentação (salarial × indenizatória) | O manual a faz depender de **reconhecimento judicial**, não de cláusula |
| Nº de passagens/dia e média de 22 dias úteis | São *defaults probatórios* na ausência de documento, não parâmetros negociáveis |
| Gratificação de sala de controle (ACT Gasmig) | Citada na Tarefa 4; **não tenho o documento**. Não sei se é parâmetro ou verba autônoma |

---

## 4. Cobertura da varredura

| Origem | Parâmetros |
|---|---|
| Varredura própria dos blocos 02, 03 e 04 | **15** |
| Seção 18 de `02a-adendo-lacunas-verbas.md` | **3** — todos incorporados (`pn.transferencia.adicional`, `pn.transferencia.base`, `pn.comissionista.adicional-he`) |
| **Seção 10 de `02-base-normativa-verbas.md`** | **13 — NÃO INCORPORADOS, arquivo ausente** |
| Derivados (não são parâmetros próprios) | 1 — `pn.jornada.divisor` |
| Dúvidas, fora do inventário | 6 |

**Total no inventário: 17 parâmetros + 1 derivado.**

O bloco 02 (`bloco-02-criterios.md`) **não contribuiu com parâmetro algum**, e isso é
esperado: ele trata de princípios da liquidação e aritmética, não de verbas. O que ele
contribui é a **moldura de precedência** — R8, título judicial sobre o manual — que a
invariante R16 desta camada estende.
