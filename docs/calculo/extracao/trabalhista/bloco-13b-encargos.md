# Bloco 13B — capítulo 8: encargos e despesas processuais

Manual TRT-3, pp. 100 a 106. **Offset de paginação zero.**

Fecha a assimetria aberta desde o bloco 8: as custas do manual federal estavam extraídas e o
lado trabalhista não.

---

## 1. Correções de premissa do enunciado

Três, todas minhas:

| Premissa | Realidade |
|---|---|
| "o sumário lista `8.2.1`" | **Não lista.** O sumário traz só 8.1/8.2/8.3/8.4. O `8.2.1` existe **no corpo**, p. 101, com título mais longo: *"Apuração do valor das custas de execução **sobre o cálculo de liquidação**"*. A forma curta que citei veio do meu próprio `mapa-de-cobertura.md`, não do manual |
| "o cap. 1 do CJF está em `bloco-08-jf.md`" | Está em **`bloco-08-jf-detalhe.md` § 1**. No `bloco-08-jf.md` a palavra "custas" ocorre **uma vez**, na tabela OUT_OF_SCOPE |
| "as faixas do art. 85, § 3º, do CPC estão em `02-base-normativa-verbas.md` § 10" | **§ 10 é "Inventário inicial de parâmetros negociáveis".** Ver § 5 |

---

## 2. P10-18 — resolvida em parte, e a causa era outra

O bloco 10 registrou que a base das custas de execução do cap. 11 divergia da do cap. 9
(151,56 contra 151,39) e atribuiu a divergência a **bruto × líquido**. O capítulo 8 permite
fechar o diagnóstico, e **a causa é outra**.

### 2.1 O capítulo 8 enuncia — mas por exclusão

Item 8.2.1, literal:

> "Da base de cálculo das CE será excluída apenas a parcela de custas processuais (custas da
> fase de conhecimento)"

> "Nenhuma outra verba deverá ser excluída da base, nem mesmo imprensa oficial e honorários"

**Define o que SAI, nunca o que ENTRA, nem em que estado.** Busca dirigida: `bruto` e
`líquido` têm **zero ocorrências** nos itens 8.2 e 8.2.1.

Logo **não decide** entre as duas versões. Mas **confirma que honorários entram na base**, o
que sustenta o achado do bloco 10 de que eles entram brutos.

### 2.2 A causa real: o juro Selic sobre a cota-reclamante

Refeito em `Decimal` sobre a `pagina_pdf` 280:

```
líquido 28.416,25 + INSS recte 606,12 + INSS recda 1.290,44 = 30.312,81
bruto   28.987,08 +                     INSS recda 1.290,44 = 30.277,52
                                                     delta  =      35,29
                                          606,12 − 570,83   =      35,29   ✓
```

**`bruto ≡ líquido + INSS recte SEM Selic`.** O rótulo do cap. 9 (`"(Vr. Bruto do recte + INSS
recda) x 0,5%"`, `pagina_pdf` 132) **ignora esse juro**, e só coincide quando o INSS não o
carrega — que é o caso nas três ocorrências do cap. 9 (pp. 132, 137, 163, todas verificadas).

**Reclassificado de divergência normativa para defeito de rótulo — D13B-06.** E o `151,39`
**não é impresso em nenhuma das 471 páginas**: era valor derivado da análise do bloco 10.

### 2.3 Invariante promovida de exemplo

**R8-CE-01** — a base das custas de execução é o **total do cálculo antes da própria linha de
CE**. Fecha exato na `pagina_pdf` 163: `4.502,08 → 22,51 → total 4.524,59`.

Regra que só existe na aritmética. Promovida com marcação de origem.

---

## 3. O que o capítulo 8 traz

Encargos extraídos com base, alíquota, responsabilidade, momento e fundamento — detalhe no
JSON de extração. Fundamentos declarados: **arts. 789, 790 e 790-A da CLT**, com as alterações
da **Lei 10.537/02**, e a **IN GP/CR/VCR n. 001/02 do TRT-3**.

**Honorários periciais:** atualizados por **IPCA-E** (Res. 66/10 do CSJT) e **sem juros**, por
serem despesa processual — fundamento no art. 407 do CC e na OJ 198.

> **Divergência jurisprudencial registrada, não resolvida:** há quatro acórdãos em cada
> sentido sobre a incidência de juros nos honorários periciais. **Duas variantes com
> fundamento próprio.**

---

## 4. O achado mais pesado: o manual se contradiz sobre Fazenda Pública

**D13B-02.** Duas isenções incompatíveis para a **mesma pergunta** — quem é isento das custas
de execução:

| Onde | Teste |
|---|---|
| **Cap. 8, `pagina_pdf` 102, item 4** | "São isentos (...) os entes públicos das 3 esferas, inclusive autarquias e fundações, **que não explorem atividade econômica**, o Ministério Público do Trabalho e os beneficiários da Justiça Gratuita (art. 790-A, CLT)" |
| **Cap. 14, `pagina_pdf` 306, letra "e"** | "Custas execução: Estão isentos os órgãos públicos das três esferas da administração pública **direta e indireta**, inclusive fundações e autarquias" |

**O cap. 14 omite a cláusula da atividade econômica e acrescenta "indireta"** — que abrange
sociedade de economia mista.

Para um ente da administração indireta **que explore atividade econômica**, os dois capítulos
dão respostas opostas.

### 4.1 Consequência registrada

**O manual não pode ser fonte para resolver a pendência 1 da § 9 de `00-base-normativa.md`**
— a classificação de sociedade de economia mista como Fazenda Pública.

Busca que sustenta: **`economia mista` tem zero ocorrências nas 471 páginas.** A única
equiparação nominada no cap. 14 é a **ECT**, e só *"para efeito de execução e do DL
779/1969"*.

**Não resolvi a classificação** — não é matéria de cálculo. A condicional fica registrada nos
dois ramos.

---

## 5. Fase 4 — honorários sucumbenciais, e uma lacuna que eu não sabia que existia

O manual é de 2016 e **não pode conhecer o art. 791-A da CLT**, criado pela Lei 13.467/2017.
Marcado, não harmonizado.

**Mas a marcação não tem contra o que ser confrontada.** As faixas do art. 85, § 3º, do CPC
**não existem em lugar nenhum do repositório**. Busca em toda a árvore `docs/` por
`200 salários`, `1.000 salários`, `2.000 salários`, `20.000 salários`, `100.000 salários`:
**zero ocorrências**.

O que existe é apenas a **regra de progressividade**, em `bloco-08-jf.md`, **R-08-21** — sem
os valores.

Nova pendência: **P8-F4-02**.

---

## 6. Cruzamento com o capítulo 1 do manual federal

Feito contra `bloco-08-jf-detalhe.md` § 1 e `bloco-08-jf.md` § 7. Diferenças de critério
entre as duas jurisdições registradas no detalhe, **sem harmonizar**.

---

## 7. Defeitos

Vinte catalogados, com assinatura detectável. Os que vão para `armadilhas-comparador.md`:

- **`(15% s/ 277.338,69)`** na `pagina_pdf` 106 quando a base é `277.338,39`. Provado: 15% de
  277.338,69 daria 41.600,80, e o impresso é **41.600,76** — que é 15% de 277.338,39;
- **teto rural de 2011** impresso `10.867,51` contra `10.867,32` pelo fecho da própria tabela
  — **delta 0,19**, fora do padrão de 0,01 dos demais anos;
- **faixa de 2013 com sobreposição** em `3.255,47` e **buraco de R$ 2,01**;
- **faixa de 2014** com `6.89.754,21` malformado.

---

## 8. Pendências

| # | Pendência |
|---|---|
| **P13B-01** | A base das custas de execução é definida **por exclusão**; o estado (bruto ou líquido) não é declarado |
| **P13B-02** | **Contradição cap. 8 × cap. 14** sobre a isenção de entes públicos. O manual não resolve a pendência 1 da § 9 |
| **P8-F4-02** | As **faixas do art. 85, § 3º, do CPC não existem no repositório** — só a regra de progressividade |
| **P13B-04** | Juros sobre honorários periciais: quatro acórdãos em cada sentido, duas variantes |
| **P10-18** | **Fechada em parte** — a causa é o juro Selic sobre a cota-reclamante (D13B-06), não bruto × líquido. Resta o estado da base |
