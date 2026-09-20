# Descontos legais — INSS e IRRF

Fonte: `docs/calculo/consolidado/04-descontos.md` e `04-descontos-detalhe.md` (capítulo 9 do
Manual TRT-3, pp. 107–208, e o item 10.2). **Offset de paginação zero** — número impresso =
página do PDF.

**As FAIXAS não moram aqui.** São série **(B)**, capítulo 18, e vivem em `skills/indices-judiciais/`.
O que vive aqui é **regra (A)**: quem desconta, sobre o quê, em que ordem, sob qual regime.

> **Por que a distinção é operacional:** uma série (B) desatualizada é **defeito de cobertura** —
> recarrega-se. Uma regra (A) superada é **defeito de correção** — **inverte o resultado**.

---

## 1. As regras de abertura — item 9.1, p. 107, `VIGENTE`

Literais: *"Devem ser deduzidos do crédito do reclamante [...] **ainda que o comando sentencial
seja omisso**, conforme Súmula 401/TST"*; *"**O desconto previdenciário precede sempre ao desconto
do IR**"*; *"As bases de cálculo dos descontos previdenciários e fiscais são **diferentes**"*; as
duas cotas deduzem-se do crédito do reclamante (**OJ 363 da SDI-1**), *"**exceto se for acordado
que o valor devido é líquido**"*; a cota patronal *"**é calculada com base no crédito trabalhista,
mas dele não é dedutível e não tem teto máximo**"*.

| ID | Regra |
|---|---|
| `R-07-01` | **ordem: INSS antes de IR, sempre.** A base do IR é o **líquido de INSS** (9.3.6, p. 185; art. 74 do Dec. 3000/99 — **endereço morto**, § 6) |
| `R-07-02` | **assimetria das cotas:** a do empregado deduz, tem teto e totaliza; a do empregador **não deduz e não tem teto** |
| `R-07-03` | **o acordo de valor líquido inverte o ônus** — única exceção declarada |
| `R-07-16` | **contribuições de terceiros ficam fora** (Súmula 24 do TRT-3 — regional `R4`; item 9.2.2, p. 108) |
| `R-07-21` | **no INSS pergunta-se *a verba é salarial?*; no IR, *a lei isenta?*** Usar o mesmo teste nos dois é **erro de método, e o manual o diz expressamente** |
| `R-07-22` | **deduções ≠ verbas não tributáveis:** deduções são **da pessoa do contribuinte**; não tributáveis têm **previsão legal de isenção** |

---

## 2. INSS

### 2.1 Fato gerador — o corte de 05/03/2009

| Competência da parcela | Fato gerador | Regime |
|---|---|---|
| até **04/03/2009** | pagamento do crédito ao reclamante | **caixa** |
| a partir de **05/03/2009** | prestação do serviço | **competência** |

`R-07-04` — **o eixo é a competência da PARCELA**, não a do processo, do ajuizamento ou do
pagamento: **um contrato que atravesse 05/03/2009 tem os dois regimes na mesma conta.**

`R-07-05` — **três marcos temporais distintos dentro do regime de competência** (cisão do Pleno,
p. 118): **atualização monetária** desde a prestação, sobre reclamante **e** reclamada; **juros de
mora** desde a prestação, **só** sobre a reclamada; **multa** só a partir do **exaurimento do
prazo de citação para pagamento**, **só** sobre a reclamada, *"não incide retroativamente à
prestação de serviços [...] observado o limite legal de 20%"*. · `R-07-12` — *"Não há incidência
de multa sobre os juros."* · `R-07-06` — **precedência (R8):** *"o calculista deverá observar
estritamente as decisões existentes nos autos"*; a Súmula 45 é o **default, não o teto**.

**Divergência transcrita, não harmonizada** (p. 129): *"há decisões determinando que a multa
incida também desde a efetiva prestação de serviços. Nesta hipótese, deverá ser observado o
contido na decisão."* — `P7-05` e `P7-06`. · `R-07-07` — **determinação de apurar o período
contratual muda tudo:** os acréscimos incidem desde a prestação **durante todo o período de
apuração**.

### 2.2 Os três regimes de atualização da contribuição — item 9.2.7, p. 129

| Caso | Regime | Atualização |
|---|---|---|
| **a)** parcelas até 04/03/09 | caixa | **mesmos índices do crédito do reclamante** até o pagamento; daí, acréscimos legais previdenciários |
| **b)** parcelas desde 05/03/09 | competência | art. 35 da Lei 8.212/91 — **Selic** + multa de **0,33%/dia, limitada a 20%** |
| **c)** parcelas nos dois períodos | ambos | **os dois critérios na mesma conta** |

> **`F7-04` — `SUPERADO`.** A expressão *"atualmente a TR"* (p. 129) **morreu com a ADC 58**
> (18/12/2020). **A remissão de MÉTODO sobrevive intacta** — *"mesmos índices de atualização do
> crédito do reclamante"* — e passa a apontar para a cadeia nova de
> `skills/calculo-judicial-atualizacao/`. Alcança também as pp. **138, 148, 149 e 155**.

### 2.3 Cota do empregado — item 9.2.7.1, pp. 128–130

```
SC_novo(m)      = SC_contrato(m) + BaseSalarialOriginal(m)      ← valor ORIGINAL, sem correção
alíquota(m)     = f(SC_novo(m), tabela_salário_contribuição(época))
INSS_devido(m)  = SC_novo(m) × alíquota(m)   , limitado ao teto da época
Dif_INSS(m)     = INSS_devido(m) − INSS_recolhido_contrato(m)
Se SC_contrato(m) já atingiu o limite máximo  ⇒  Dif_INSS(m) = 0
```

`R-07-08` — base legal: art. 20 da Lei 8.212/91; art. 276, § 4º, do Dec. 3048/99; Súmula 368, III,
do TST; Súmula 45 do TRT-3. · `R-07-09` — **salário de contribuição** = o valor sobre o qual a
executada descontou na época própria, **mês a mês**. · `R-07-10` — **a base é o valor ORIGINAL,
antes da correção**; a correção entra depois, **sobre a contribuição apurada, não sobre a base**.
· `R-07-11` — **bloqueio do mês pelo teto**. · `R-07-13` — **memória segregada** (principal,
juros, multa): o 9.2.7.3 depende disso para reatualizar sem refazer mês a mês.

**`P7-07`:** sem o salário de contribuição nos autos, o manual recompõe *"presumindo que a
reclamada efetuou o recolhimento corretamente"* (p. 158) — **presunção declarada, não dado**. ·
**`P7-04`:** o 13º como base autônoma **não tem enunciado**; existe só em planilha.

### 2.4 `F7-01` — alíquota única × progressiva, o ponto de maior impacto do capítulo

**Bifurcação em 01/03/2020** — as duas versões em
[`cortes-e-bifurcacoes.md`](cortes-e-bifurcacoes.md) § 3.

**Método antigo, literal** (p. 130, passo 3): *"[...] **estabelecer uma nova alíquota** e apurar a
contribuição social devida, respeitando o teto máximo de contribuição da época."* **Confirmado
pela aritmética** — uma alíquota, o total inteiro: p. 131 → `951,99 × 9,00% = 85,68`; p. 133 →
`1.085,60 × 8,00% = 86,85`; p. 135 → `1.675,98 × 11,00% = 184,36`. **E não muda por período dentro
do manual**: mesmo critério em exemplos de 2008, 2009 e 2013/14.

> **O período anterior está POSITIVAMENTE CONFIRMADO, não presumido.** O STF, no **Tema 833**
> (RE 852.796, 14/05/2021), declarou constitucional a expressão *"de forma não cumulativa"* do
> art. 20. **Não é sobrevivência por omissão — é validade declarada por precedente vinculante.**
> **Ressalva:** a tese do Tema 833 é **secundária** (STF em HTTP 403), confiança médio-alta.

**Para o salário-de-contribuição há DUAS CAMADAS, e é pior que no IRRF:** os **VALORES** das
faixas mudam todo 1º de janeiro por portaria — **(B)**; a **REGRA** de aplicação mudou por emenda
constitucional em **01/03/2020** — **(A)**. **Uma série de faixas atualizada com a regra antiga
produz número errado.**

### 2.5 Cota patronal — item 9.2.4.1, pp. 109–115

| Situação | Alíquota | Fonte |
|---|---|---|
| Empresas em geral, com vínculo, desde nov/91 | **20% + RAT (1, 2 ou 3%)** | p. 109 |
| Instituições financeiras | **+2,5%** sobre o 20% | Lei 8.212/91, art. 22, § 1º |
| Aposentadoria especial | **+12, 9 ou 6 pontos**, só sobre a remuneração do exposto | p. 109 |
| Sem vínculo: mai/96–fev/00 · mar/00 → · abr/03 → | **15% · 20% · 20% + 11% de retenção** | Dec. 3048/99 art. 201, II · Lei 9.876/99 · p. 110 |
| Empregador doméstico, desde **01/10/15** | **8% + 0,8% (SAT) = 8,8%** | LC 150/15, art. 34 |

`R-07-14` — **o FAP tem eixo próprio, e é um QUARTO eixo temporal:** não é competência nem fato
gerador — é **divulgação + 4 meses** (*"produz efeitos tributários a partir do primeiro dia do
quarto mês subsequente ao de sua divulgação"*), desde **setembro/2007**.

`R-07-15` — **quatro hipóteses em que só se apura a cota do empregado:** SIMPLES; associação
desportiva com clube profissional; entidade beneficente certificada; produtor rural PJ/PF e
agroindústria sob contribuição substitutiva (itens 9.2.4.2 a 9.2.4.5). **Ressalva comum:** desde
**abril/03** as beneficentes descontam **20%** de contribuinte individual — logo, **sem vínculo a
cota do reclamante é 20%, não 11%**.

### 2.6 `R-07-19` — o RAT/SAT sobrevive sempre, e o fundamento está no capítulo 16

*"Mesmo se houver substituição integral da alíquota de 20%"*: o regime substitutivo da desoneração
alcança só os **incisos I e III do art. 22** da Lei 8.212/91, e **o RAT/SAT está no inciso II**.

**Fundamento: Súmula 454 do TST.** Ele **não está no capítulo técnico que executa a operação** (o
cap. 9, item 9.2.10). Está no **cap. 16, item 16.4.3.19, pp. 320–322**, com **3 ocorrências, todas
no cap. 16**. É exatamente o padrão do § 2 de `07-leitura-do-corpus.md`: **o manual pratica no
capítulo técnico e fundamenta na minuta.** Quem extrair só o cap. 9 fica com a regra **sem a
razão**.

---

## 3. Imposto de renda

### 3.1 A inversão de lógica — item 9.3.2, p. 180

Literal: *"Diferentemente do desconto previdenciário, no caso do imposto de renda **é de pouca
valia orientar-se pelo conceito de verba indenizatória ou salarial** [...] **são verbas
não-tributáveis somente aquelas que a lei expressamente mencionar**."*

**Não incide IR** (9.3.4 e 9.3.5): férias integrais + 1/3 não gozadas por necessidade de serviço e
pagas em pecúnia na rescisão, exoneração ou aposentadoria; férias em dobro + 1/3 e proporcionais +
1/3 nas mesmas hipóteses; **abono pecuniário**; **danos morais** (AD PGFN 09/2011).

### 3.2 `F7-03` — juros na base do IR: DUAS CORRENTES, nenhuma resolvida

O manual (p. 181) registra que *"a questão não está resolvida"*. **Continua não estando.**

| | **Corrente A — OJ 400 da SDI-1 do TST** | **Corrente B — Tema 808 do STF** |
|---|---|---|
| Tese | os juros de mora **nunca** integram a base do IR, *"independentemente da natureza jurídica da obrigação inadimplida"* | não incide IR sobre juros de mora **por atraso no pagamento de remuneração por exercício de emprego, cargo ou função** |
| Fundamento | art. 404 do CC/2002; DEJT 02–04/08/2010 | RE 855.091/RS, Plenário, **15/03/2021**; adaptação do STJ no Tema 878 |
| Alcance · estado | **mais amplo** · **não cancelada** | **mais estreito** · vinculante, **modulação pedida e RECUSADA** nos ED (11–18/06/2021) |

> **Por que não se resolve:** o Tema 808 **não revogou** a OJ 400, e a OJ 400 **não foi
> cancelada**. **A área de atrito é o espaço entre os dois** — juros sobre verbas indenizatórias,
> sobre honorários, sobre rescisórias de natureza não remuneratória. **É escolha jurídica do
> usuário do módulo: preset SEM DEFAULT**, como `pr.imputacao`.

**Eixo: não é temporal — é MATERIAL**, a natureza da verba principal sobre a qual os juros
incidem; **sem corte temporal de efeitos**, porque a modulação foi recusada.

**A regra operacional do manual sobrevive** — item 9.3.3, p. 182: os juros *"apenas deverão ser
excluídos da base [...] **se houver decisões nos autos neste sentido ou se pagas no contexto da
rescisão do contrato de trabalho**"*. **Duas portas independentes:** (1) **decisão nos autos**, via
OJ 400; (2) **contexto da rescisão**, por IN RFB 1500/14, art. 62, § 3º, II, "a", e **Solução de
Consulta Interna Cosit 13, de 30/06/2016**, transcrita na p. 181.

`R-07-23` — **a segunda porta é mais larga que "verbas rescisórias":** dirigida ao contexto da
**perda do emprego** — **não alcança pedido de demissão** — e abrange *"além dos juros referentes
às verbas rescisórias em sentido estrito, também os juros relativos às demais verbas trabalhistas
devidas [...] e não adimplidas no curso do contrato"*. · `R-07-24` — **o principal continua
tributado**, *"acrescido de correção monetária"*. · `R-07-25` — **contrato em curso: os juros são
tributáveis**.

**Conflito interno registrado (`P7-02`), não harmonizado:** a matriz 18.1 marca juros como
tributáveis; o item 9.3.3 conclui pela exclusão em duas hipóteses.

### 3.3 Os dois regimes — art. 12-A × art. 12-B

| | **art. 12-A** — RRA | **art. 12-B** — regime geral |
|---|---|---|
| Quando | rendimentos de **anos-calendário anteriores** ao do recebimento | rendimentos do **mesmo ano-calendário** do pagamento |
| Base | `VB × IPIR − INSS` | `VB × IPIR − INSS` |
| Alíquota | tabela do mês do recebimento, sobre base **dividida por NM** | tabela **mensal** sobre a base **integral** |
| Parcela a deduzir | **× NM** | **única, sem multiplicação** |
| **Número de meses** | **dois NM distintos** | **NENHUM** |
| Tributação · código | na fonte, **em separado** · 1889 | junto aos demais · 5936 (**só no cap. 9, p. 207** — ausente do 10.2: `P13A-04`) |

**Hipótese de incidência do 12-B, literal** (pp. 233 e 235, texto idêntico): *"rendimentos
referentes ao ano-calendário do recebimento, rendimentos pagos por entidades de previdência
complementar e liberados ao reclamante até 10/03/15 e rendimentos pagos em cumprimento da decisão
da Justiça do Trabalho e que não se enquadram ao disposto no art. 12-A"*.

`R-07-26` — **havendo os dois, são duas apurações distintas** (p. 190). · `R-07-27` — **marco
inicial do 12-A: 01/01/2010.** · `R-07-28` — **desde 11/03/2015** o 12-A perde a restrição por
tipo de rendimento (MP 670/15 → Lei 13.149/15). · `R-07-34` — **a virada do ano-calendário muda o
regime**: um cálculo do 12-B vira 12-A pela simples passagem do ano (p. 193), **e a regra só
existe em observação de exemplo**.

> **`P10D-08` — permanece aberta.** A **migração de regime dentro do mesmo cálculo** (Exemplo 5) é
> caso único e **não tem disciplina em lugar nenhum**. Buscas nas **471 páginas**: `migra*` → 0;
> `transição` → 0; `dois regimes` → 0. No segmento B: `11/03/15` → 0; `10/03/15` → 2 (pp. 233 e
> 235), **sempre dentro da hipótese do 12-B, nunca como marco de transição**. **Não resolvo por
> inferência.**

### 3.4 O NM — variável, nunca doze

Item 9.3.7.3, p. 188: *"serão considerados **apenas os meses em que foram apurados rendimentos
passíveis de tributação** no cálculo de liquidação."* **O manual nomeia dois erros comuns:** tomar
por base *"o período trabalhado ou o período imprescrito"* — *"tal critério está incorreto"* — e
*"considerar todos os meses constantes no cálculo, mesmo que em determinados meses não sejam
apuradas parcelas passíveis"*.

```
NM              = nº de meses COM rendimento tributável   (+1 por 13º apurado)
faixa           = f(base ÷ NM)   ou   f(base, limites_da_faixa × NM)     ← equivalentes
parcela_deduzir = parcela_deduzir_da_faixa × NM
IR              = base × alíquota − parcela_deduzir
```

`R-07-29` — **o 13º vale um mês, sempre**, *"não importando se proporcional ou integral"*. ·
`R-07-30` — **no 12-A o 13º NÃO é tributado em separado**; é englobado — **o contrário do INSS**. ·
`R-07-31` — **duas deduções, não três:** contribuição previdenciária e pensão alimentícia (art.
12-A, § 3º, I e II, da Lei 7.713/88); **dependente NÃO deduz no RRA**.

**Sob o 12-B não há NM; sob o 12-A há DOIS NM distintos** — o do enquadramento e o da parcela a
deduzir. **O manual anuncia *"dois critérios"* (p. 193) mas só enuncia o primeiro.**

**`P7-08`:** honorários advocatícios **não aparecem como dedução em lugar nenhum do cap. 9**.
**`P7-09`:** não há regra de **segregação anual** do RRA.

**Arredondamento do NMP:** `SKILL.md`, Passo 6 — **três ramos, não é half-up**.

### 3.5 Momento do cálculo — item 9.3.6, pp. 185–186

`R-07-32` — **o IR se recalcula a cada liberação:** *"por ocasião de cada pagamento ao reclamante,
o imposto de renda deverá **sempre ser recalculado**, incidindo apenas sobre o valor efetivamente
disponibilizado, considerando a proporção das parcelas passíveis de tributação"* — **é a ponte
para o rateio de 10.2**. · `R-07-33` — **o IR do cálculo de liquidação é ESTIMATIVA** quando
apurado na data final de atualização (p. 190). · `R-07-35` — **prazo de 15 dias** da retenção para
a fonte pagadora comprovar nos autos.

---

## 4. Rateio sob pagamento parcial — item 10.2

**O manual não distribui os descontos: RECONSTRÓI O BRUTO PRIMEIRO.**

```
1.  do LÍQUIDO levantado, achar o VR. BRUTO LEVANTADO      (fórmula fechada — cuidado com A11)
2.  ratear o INSS:   (VB / TB) × INSS_devido_na_data_do_levantamento
3.  recalcular o IR do zero:   base = VB × IPIR − INSS_proporcional
```

**Literal sobre o INSS** (pp. 227, 232, 234, 236): *"dividir o valor bruto levantado pelo total
bruto devido ao recte na data da amortização e multiplicar pelo valor da contribuição social
devida na data do levantamento"*. Aplica-se a **cota reclamante e cota reclamada**, **dispensada a
reclamada quando o fato gerador é a prestação de serviço**. **O IR não é rateado:** é apurado **de
novo**, pela tabela do **mês do levantamento**.

**Duas razões diferentes no mesmo exemplo.** Nos ramos "sem juros" o manual usa **duas proporções
distintas**: `VB / TB` para **ratear o INSS** e `TBSJ / TBCJ` para **expurgar os juros da base do
IR**. **Não é erro — são objetos diferentes.** Mas é **decisão estrutural que nenhum enunciado
declara**, e um motor que use uma razão só produz número errado num dos dois passos.

**`P11B-04` — a base do IR com e sem juros é bifurcação DECLARADA, quatro vezes no segmento:** o
mesmo levantamento de `282.500,00` produz IR de **`38.425,68`** (com juros) contra **`13.551,75`**
(sem). **É parâmetro do método, não defeito.** **Falta a regra de escolha, e ela não está aqui:**
`OJ 400` tem **zero ocorrências nas pp. 223–237** (`P13A-03`). A regra de escolha é a do § 3.2 —
justamente a que **não se resolve**.

**O cap. 9 delega ao 10.2, e a remissão FUNCIONA** — p. 207, item 9.3.12: *"Imposto de renda
proporcional ao valor pago — O cálculo [...] **será detalhado no item 10.2**."* **O cap. 9 tem o
fundamento; o 10.2 tem a operação.** O fundamento está na p. 186 — art. 12-A § 1º, art. 12-B e
**art. 56 do Dec. 3000/99** (endereço morto). **O item 10.2 nunca o repete.** Registre-se, porque
a remissão cruzada da p. 209 (*"tópico 7.3"* onde deveria ser **7.6**) **não funciona** — `A8`.

---

## 5. Defeitos que o comparador precisa nomear

| ID | Onde | O quê e o efeito |
|---|---|---|
| **A11** | pp. 227, 231 → 244, 250 | **colchete fechado cedo demais**: impresso `{1–[(TB×IPIR–INSS)×ALIQ/TB] + (INSS/TB)}`, correto `{1–[(TB×IPIR–INSS)×ALIQ/TB + (INSS/TB)]}`. **−3.771,73** e **−3.071,48** se seguida à risca. **Fórmula errada, resultado certo** — a forma correta está em 10.2.2.1, p. 233. **Com `INSS = 0` as duas leituras coincidem** |
| **A12** | pp. 132, 280 | o rótulo `"(Vr. Bruto do recte + INSS recda) x 0,5%"` **ignora o juro Selic da cota-reclamante**; base real `líquido + INSS recte COM Selic + INSS recda`. **35,29** na p. 280 |
| **A6 · A7** | pp. 254 · 244 | resumo do Exemplo 2 com o **NM do Exemplo 1** (`11,10`/`8,90` em vez de `10,8`/`9,2`) · **gross-up com sinal invertido**, **−4.100,21** |

**E dois comportamentos que NÃO são defeito:** a aritmética é encadeada em **precisão plena**,
logo **as colunas impressas não somam os totais impressos** por 0,01–0,02; e **não existe regra de
arredondamento monetário no manual** — busca nas **471 páginas**: `arredond` → **5, todas sobre o
número de meses do RRA**; `casas decimais` → **0**; `truncad` → **0**.

**`P11B-03` fecha como erro de leitura:** `0,9091` **não é percentual de IR — é o IPIR** (rótulo
literal, p. 244: *"x 0,9091 (índice parcelas passíveis IR)"*), papel idêntico ao `0,8340` do
segmento B. **O contraste registrado não existe.**

---

## 6. O que este arquivo NÃO consolida, e por quê

| Aberto | Razão |
|---|---|
| **De-para RIR/99 → RIR/2018, artigo a artigo** | Planalto inacessível. **Não foi feito**, e sem ele **toda remissão a "art. X do RIR/99" é endereço quebrado** — inclusive o art. 74 (`R-07-01`) e o art. 56 (§ 4) |
| **Destino dos códigos 2909, 1708, 1889 e 5936** | as fontes tratam da substituição **em bloco**; **confiança nula** código a código |
| **Percentuais da transição da Lei 14.973/2024** | lei **não lida**; secundária comprovadamente ruidosa. **Não usar em produção.** E a Lei 14.784/2023 teve eficácia suspensa por monocrática na **ADI 7633** (abril/2024) — **instabilidade não verificada** que afeta as competências de 2024 |
| **`F7-03`** | **duas correntes vigentes**, Tema 808 × OJ 400. **Não resolvo** |
| **Migração 12-A ↔ 12-B**; **escolha da base do IR com/sem juros** | `P10D-08` (0 disciplina em 471 páginas) e `P13A-03` (`OJ 400` ausente do segmento). **Não infiro** |
| **Fundamento normativo dos dois rateios do cap. 10** | `P13A-02` — `art. 354` tem **0 ocorrências em 471 páginas** |
| **Conferência artigo a artigo da IN 1500/14** · **nota do MTE sobre a base do seguro-desemprego** | a primeira **não foi realizada**, e impede confiança maior em `F7-08`; a segunda é **`SEM FONTE` verificada** — lacuna declarada, **e não é regra** |
| **Honorários sucumbenciais e gratuidade** (`C8-01`, `C8-02`) | são **cadeia de honorários, não desconto legal**. Em [`encargos-processuais.md`](encargos-processuais.md) — **por delimitação, não por omissão** |
| **`P7-01`** | ordem de imputação do **recolhimento parcial**: um padrão e **duas alternativas sem critério**, convivendo com uma **segunda ordem, proporcional entre rubricas**, em 9.2.7.3-A (pp. 152–153 e 143) |
| **`P7-03`** | **diárias**: contradição **interna ao 18.1** — a linha marca `IRRF = sim` acima de 50%; a nota diz que não há limite, e o cap. 9 **concorda com a nota** |
| **`P13A-05`** | divergência de citação da IN 1500/14 entre 10.2.2 (*"arts. 26, 44 e 45"*) e 9.3.8 (*"arts. 26, 43 e 44"*) — **a de 10.2.2 é a errada** |

---

## Passo 6 — o arredondamento do NMP, por extenso

*Movido da espinha no bloco 16, pelo limite de 500 linhas.*

### Passo 6 — o arredondamento do NMP, que **não é half-up**

**A regra É declarada** — pp. **226** e **230**, com o artigo transcrito: *"deverá ser observada a regra de
arredondamento prevista no **parágrafo único do 45 da Instrução Normativa 1500/14**"*. **Três ramos:** 2ª
casa decimal **< 5** mantém a 1ª casa; **> 5** acrescenta uma unidade; **= 5** manda **analisar a 3ª casa**
— 0–4 **mantém**, 5–9 acrescenta.

> **Difere de `ROUND_HALF_UP` na faixa `x,y50` a `x,y54`**, onde half-up **sobe** e a regra do art. 45
> **mantém**. Entra como **regra literal**, não como inferência.

**Limite de verificabilidade, declarado:** os dois NMP dos exemplos (`48,5107` e `44,7478`) **não
discriminam** entre as regras — **nenhum exemplo do manual exercita o ramo `=5`**. **`P13A-05`, não
corrigida:** 10.2.2 cita *"arts. 26, 44 e 45"* da IN 1500/14; 9.3.8, *"arts. 26, 43 e 44"* — **o art. 45 é a
regra de meses do RRA, inaplicável ao art. 12-B**, logo a citação de 10.2.2 é a errada (`D13A-12`).
