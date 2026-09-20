# Domínio e invariantes

Espinha consolidada. Modelo, vocabulário, as invariantes **R1 a R24** e a regra de
precedência. É o arquivo que os outros pressupõem.

> **R24 nasceu no bloco 16** (§ 2.9), com a correção da premissa nacional × regional. As
> invariantes não são numeradas por ordem de importância, e sim por ordem de descoberta.

Fontes: `../00-base-normativa.md` § 7, `../presets-regime.md` § 5,
`../parametros-negociaveis.md`, e os vereditos do bloco 14.

---

## 1. O modelo em uma página

Um cálculo se resolve em **três camadas, nesta ordem**. Inverter a ordem produz número
plausível com a conta inteira no regime errado.

```
1. REGIME TEMPORAL      qual REGRA vale nesta competência?        R19–R22
2. PARÂMETRO            quanto VALE o que a regra manda aplicar?  R14–R18
3. APURAÇÃO             a conta                                   R1–R13, R23
```

**A camada 1 decide se a camada 2 é sequer consultada.** Sob `pr.in-itinere` na variante
`suprimidas`, o parâmetro `pn.in-itinere.prefixacao` **não existe** — não é que valha zero.

### 1.1 Vocabulário

| Termo | Significado exato |
|---|---|
| **competência** | o mês a que a parcela se refere. Unidade da apuração |
| **corte** | data + **eixo** a partir da qual muda a regra. Ver `00-calendario-de-cortes.md` |
| **eixo de corte** | **qual fato do processo** se compara com a data do corte |
| **regime** | escolha jurídica sobre *qual regra aplicar*. Não é negociável por sindicato |
| **parâmetro** | valor resolvido por `(parâmetro, categoria, competência)` |
| **cadeia temporal** | sequência de segmentos `período → regra`, sem lacuna nem sobreposição |
| **englobamento** | segmento cujo índice cobre **correção e juros** (SELIC, taxa legal) |
| **regra** (A) | muda quando muda a lei ou a jurisprudência |
| **série** (B) | muda quando o governo publica portaria. **Dado externo, não regra** |

**A distinção (A) × (B) é operacional, não acadêmica.** Uma tabela de IRRF desatualizada é
série a atualizar; uma alíquota mudada por emenda é regra a bifurcar.

---

## 2. As invariantes

Violadas, produzem **erro material**. Devem ser impedidas **na composição**, não detectadas no
resultado.

### 2.1 Cadeia e cobertura

**R1 — Exclusividade de englobamento.** Segmento cujo `engloba` cobre correção e juros não
admite outro do mesmo componente no mesmo intervalo. **Vale para SELIC e para a taxa legal.**

> **SELIC e taxa legal ENGLOBAM correção monetária e juros.** Aplicar correção monetária
> **junto** com qualquer das duas é **erro material**, não escolha de critério: conta a
> inflação duas vezes. Vale para todo segmento cujo `engloba` cubra os dois componentes.

**R2 — Cobertura sem lacuna nem sobreposição.** A união dos segmentos cobre da parcela mais
antiga até a data-base.

> **Exaustividade se declara, não se presume.** Ramos condicionados só esgotam o domínio se a
> cadeia o declarar em `dominio_condicoes`. Sem a declaração, o universo "nenhuma condição se
> aplica" continua sendo cobrado. O conserto que presumia exaustividade **escondia 25 anos de
> lacuna** — `bloco-09-relatorio.md` § 2.

**R3 — Tipo do indexador na virada.** Nominal (Ufir, BTN, OTN, ORTN) reflete a inflação do mês
**anterior**; percentual (INPC, IPCA, IGP) reflete a do **próprio** mês. Trocar entre tipos sem
ajustar a defasagem **desloca o cálculo em um mês**.

### 2.2 Juros e capitalização

**R4 — Capitalização.** Juros de mora, SELIC e taxa legal: **sempre simples**.

> **R4-EXCEÇÃO — juros COMPOSTOS de 27/02/1987 a 03/03/1991**, por força do **DL 2.322/87,
> art. 3º**. Não é defeito de transcrição: está no quadro geral do TRT-3 (`pagina_pdf` 89),
> repetido no da Fazenda (92) e **confirmado de forma independente pela cadeia do CJF**. O
> manual dá a mecânica: *"1,0% ao mês, c/ taxa capitalizada. Ex.: 3 meses = 3,03%"*.
>
> **Gravado dentro do invariante, não em nota:** quem ler só "sempre simples" **erra quatro
> anos** de qualquer conta que atravesse o período.

**R23 — Descarregar antes de aplicar juros.** Antes de aplicar juros sobre saldo remanescente,
**os juros já contidos nesse saldo devem ser excluídos**. Aplicar juros sobre saldo que já os
contém produz **anatocismo**.

> **Anomalia de localização do fundamento.** O manual **executa** a operação em todo o capítulo
> 10 e a nomeia apenas *"descarregar"* — palavra com **uma única ocorrência** nas 471 páginas
> — **sem fundamentá-la**: `anatocismo` tem **zero ocorrências no capítulo 10 inteiro**.
>
> Quem a nomeia é uma **minuta de petição do capítulo 16** (`pagina_pdf` 328), que abre com a
> **mesma frase** do item 10.3.1 e acrescenta: *"não incidindo juros sobre juros (anatocismo),
> vedada por Lei"*.
>
> **São duas regras anti-anatocismo distintas, que o manual nunca reúne:** (1) juros acumulam
> por **soma**, nunca por multiplicação — `pagina_pdf` 16, **única invocação da Súmula 121 do
> STF** no manual; (2) o **descarregar**, `pagina_pdf` 237.
>
> Efeito medido: no Exemplo 5 do capítulo 10, não descarregar produziria **+R$ 30.452,43**.

### 2.3 Pisos e sinal

**R5 — Piso nominal.** Índices negativos **entram no cálculo**, mas **nenhuma parcela do
principal fica abaixo do valor nominal**. O piso é **por parcela**, não sobre o total. Fonte:
REsp 1.265.580; Manual CJF item 4.1.2.2.

> **A instrução do manual TRT-3 de "dividir pelo índice negativo" é redação defeituosa e NÃO se
> implementa.** Está registrada como defeito do original — `pendencias.md` § 9-B, onde a regra
> do índice negativo foi classificada como **ambígua**. O que se implementa é R5: o índice
> negativo entra, e o piso nominal segura a parcela.

**R6 — Piso zero da taxa legal.** Resultado negativo vira **zero**, nunca negativo.

### 2.4 Termo inicial e jurisdição

**R7 — Termo inicial dos juros não é intercambiável entre jurisdições.**

| Jurisdição | Termo inicial |
|---|---|
| Trabalhista | **ajuizamento** |
| Cível | citação, salvo Súmulas 54 e 362 do STJ |
| Repetição de indébito | trânsito em julgado |

**R9 — Fazenda Pública é atributo do processo**, não configuração de sistema nem cadastro da
empresa. A mesma parte pode receber classificações distintas em processos distintos.

> **E o manual não resolve quem é Fazenda Pública.** Cap. 8 (`pagina_pdf` 102) isenta os entes
> *"que não explorem atividade econômica"*; cap. 14 (306) isenta a administração *"direta e
> indireta"* — **sem a ressalva**. **Dois testes incompatíveis para a mesma pergunta.**
> `economia mista` → **zero ocorrências nas 471 páginas**. Pendência 1 da § 9 da base
> **não se fecha pelo manual**.

### 2.5 Precedência e pagamento

**R8 — Precedência.** **Título judicial > escolha do usuário > default da jurisdição.** Toda
divergência entre níveis fica **registrada**.

**R10 — Pagamentos parciais.**

| Jurisdição | Regra |
|---|---|
| **Cível** | imputação pelo **art. 354 do CC** — juros primeiro |
| **Trabalhista** | **proporcional** — `(B/D)×E` para o principal, `(C/D)×E` para os juros |

> **R10 está fundamentada, e por razão mais forte que a suposta.** A regra trabalhista **não
> tem fundamento normativo declarado**: `art. 354` tem **zero ocorrências nas 471 páginas**,
> enquanto `proporcional` ocorre **101 vezes** só no segmento que a aplica.
>
> **Não são duas normas concorrentes — são uma norma contra um costume de liquidação sem base
> declarada.** Por isso a escolha entra como preset `pr.imputacao`, **sem default**.
>
> **Amplitude: até 23,83% do saldo.** Direção: **juros primeiro produz dívida maior** — o
> art. 354 favorece o **credor**, o critério proporcional favorece o **devedor**.
>
> **E sob a ADC 58 o conflito é condicional, não estrutural** — ver `05-imputacao.md` § 4.

### 2.6 Aritmética

**R11 — Taxa legal calcula-se por razão entre fatores**, nunca por subtração de percentuais.
Seis decimais, IPCA-15 do mês anterior.

**R12 — Aritmética decimal.** **Nenhum float.** Critério de truncamento definido e consistente
por etapa.

> **O critério é POR ETAPA, não global. Cinco cadeias convivem, e não são intercambiáveis:**
>
> | Etapa | Critério | Casas | Fonte |
> |---|---|---|---|
> | Fator de índice e taxa legal | **truncamento** | 6 | CJF 4.2.1.1, Nota 6 |
> | Grandeza física (hora centesimal, nº de HE) | **half-up** | 2 | TRT-3, item 5.3 |
> | Valor monetário intermediário e final | **truncamento** | 2 | CJF |
> | **NMP** (nº de meses do RRA) | **3 ramos** — IN 1500/14, art. 45, § único | 1 | TRT-3, pp. 226 e 230 |
> | Cadeias do capítulo 6 | **4 práticas não enunciadas** | — | armadilha |
>
> **A regra do NMP não é half-up:** 2ª casa `<5` mantém, `>5` sobe, **`=5` manda olhar a 3ª
> casa** (0–4 mantém, 5–9 sobe). Difere de `ROUND_HALF_UP` na faixa `x,y50` a `x,y54`.
>
> **E a cadeia interna roda em precisão plena** — os impressos com 2 casas **não são os
> operandos**. O truncamento é só na **emissão**, e **valor exibido nunca realimenta cálculo**,
> mesmo que parte dos exemplos do manual o faça.
>
> **Mês comercial:** `1/30` é dízima. Usar `Decimal(1)/Decimal(30)`, nunca o truncamento
> impresso — o manual grafa `0,0333%` na regra e `0,03333%` no exemplo, duas linhas abaixo.
>
> **Consequência: as colunas impressas do manual não somam os totais impressos**, por 0,01 a
> 0,02. **O limiar de alarme do comparador não deve ser o centavo.**

**R13 — Reprodutibilidade.** Toda conta grava: preset aplicado, *overrides* com justificativa,
versão do conjunto normativo, versão das séries consumidas.

### 2.7 Norma coletiva — R14 a R18

Vivem em `../parametros-negociaveis.md`. Em resumo: o parâmetro resolve-se por
`(parâmetro, categoria, competência)`; **a norma coletiva é atributo do contrato**, não da
empresa; **ausência de norma não é erro** — é resolução pelo legal; **conflito normativo e
defeito de cadastro são coisas distintas**; e **R18 rejeita sem corrigir**.

**Art. 611-B da CLT decide a direção:** parâmetro alcançado por **inciso** → só `apenas-elevacao`;
coberto pelo **parágrafo único** (duração do trabalho e intervalos) → `qualquer`; demais →
`qualquer`, sob o **Tema 1046**.

> **27 dos 30 incisos do art. 611-B não estão no corpus** — 16 parâmetros seguem com
> `classificacao_provisoria: true`.

**A âncora é o art. 611-B, não a presença de "no mínimo" no texto de cada artigo.** Inciso que
alcança o parâmetro → `apenas-elevacao` (insalubridade, periculosidade); parágrafo único —
duração do trabalho e intervalos, que **expressamente não são** normas de saúde para esse fim
→ `qualquer`; demais → `qualquer`, sob o **Tema 1046**.

#### Ausência de norma coletiva não é erro

Competência **sem instrumento cadastrado** resolve pelo **default legal** e marca a conta como
**`sem cobertura coletiva`** — R14. Não bloqueia, não erra: registra.

> **Exceção, e é a que quebra a regra geral:** verba **exclusivamente convencional** — como a
> **ajuda-alimentação** — **não tem default legal**. Sem instrumento, ela **não existe**, e a
> conta não a apura. A diferença entre "vale o legal" e "não existe" é a diferença entre um
> número e uma linha ausente.

#### Divisor é derivado, não parâmetro

**O divisor decorre da jornada** — art. 64 da CLT e tese 3 do IRR-849. **Não pode ser cadastrado
avulso**, sob pena de admitir o par inconsistente `(jornada 44h, divisor 200)`.

Corolário: **o 210 da 12×36 é atributo do regime de jornada**, não valor negociável. Quem o
cadastrar como parâmetro cria a possibilidade de uma 12×36 com divisor de 44 horas.

> Foi por isso que a variante `enquadrado-sexta-diaria-divisor-180` **foi removida** no bloco 5:
> embutia um derivado. Há teste que impede a reintrodução —
> `test_nenhuma_variante_embute_um_derivado`.

#### A norma coletiva é atributo do CONTRATO

Não do processo, nem da empresa — **R17**. **Dois empregados da mesma empresa, no mesmo
processo, podem resolver o mesmo parâmetro de formas diferentes**, se pertencerem a categorias
com instrumentos distintos.

### 2.8 Regime temporal — R19 a R22

**R19 — registro por competência.** Toda conta grava **qual preset foi aplicado a cada
competência**. Sob *tempus regit actum* a mesma conta usa regimes diferentes em meses
diferentes.

**R20 — default marca a conta.** Regime sem escolha explícita usa o default e registra
`origem: "default"`.

**R20-EXCEÇÃO — onde não há default.** Regime com `sem_default` **não calcula sem escolha**.

> **Quatro casos**, desde o bloco 15: `pr.tema1046-validade-clausula`, `pr.he-adicional-cf88`,
> `pr.sumula17-salario-profissional` e `pr.imputacao`.
>
> **`pr.intertemporal` SAIU da lista.** O **Tema 23 do TST** (IRR, Pleno, 25/11/2024, 15 × 10,
> transitado, **modulação pedida e negada por unanimidade**) fixou tese vinculante: *tempus
> regit actum*, eixo na **competência do fato gerador**. O regime ganhou default; a
> **ultratividade é posição vencida**, aplicável só a título que a tenha adotado
> **expressamente** — e então prevalece por **R8**.
>
> **E os quatro restantes não são todos da mesma espécie.** Em três, o corpus deixa a questão
> aberta. Em **`pr.imputacao`**, o problema é de outra ordem: **a prática não tem norma e a
> norma não tem prática.** Dar default ali seria decidir se a prática predominante *tem
> autoridade*.

**R21 — divergir exige justificativa.** Escolher contra o default sem justificar é
**rejeitado** — `ErroDeDados`, não aviso.

**R22 — regime antes de parâmetro.** `parametro_consultavel()` levanta `RegimesNaoAvaliados` se
chamado sem avaliação prévia.

### 2.9 Jurisdição regional — R24

**A premissa que o projeto carregava estava errada, e a correção é estrutural.**

A atualização monetária trabalhista é **nacional** desde a **Res. CSJT 8/2005**, que unificou as
24 tabelas dos TRTs; hoje vale a **Res. CSJT 380/2024**, com duas tabelas — débitos comuns e
Fazenda Pública, esta referenciada ao Manual do CJF. O **PJe-Calc** é o sistema de toda a Justiça
do Trabalho. *(Origem: enunciado do bloco 16, **externa ao corpus** — ver
[`08-nacional-e-regional.md`](08-nacional-e-regional.md).)*

**Consequência:** o manual do TRT-3 é **fonte procedimental de uma região que aplica norma
nacional**. **Sua aritmética não é prática regional divergente.** O que nele é regional são os
**verbetes que ele invoca**.

**R24 — ausência de súmula regional não é erro.** Competência **sem verbete regional cadastrado
para o tribunal** resolve pela **regra nacional** e marca a conta como **`sem cobertura
regional`**. Não bloqueia, não erra: registra.

> **É a mesma forma da R14**, e a simetria é deliberada: `sem cobertura coletiva` e `sem
> cobertura regional` são a mesma espécie de silêncio — **o dado não existe**, não **a regra
> não existe**.

**A chave de resolução tem três componentes:**

```
(regra, tribunal, competência)
```

- **`regra`** identifica o **ponto de cálculo**, não o verbete;
- **`tribunal`** só entra onde há **variante regional cadastrada**. Ausente → fallback nacional;
- **`competência`** é necessária porque **verbete regional nasce e morre com data** — a Súmula 39
  do TRT-3 foi cancelada com eficácia retroagida a 11/11/2017.

**R24 não cria exceção à R8.** O título judicial continua vencendo: comando exequendo expresso
(art. 879, § 1º, da CLT) afasta o verbete regional **mesmo dentro da região que o editou**.

> **São quinze as regras regionais catalogadas, não três** — nove verbetes e seis fontes
> não-verbete, de **três** tribunais (TRT-3, TRT-4, TJMG). O enunciado do bloco 16 nomeava três.
> Contagem e fontes em [`08-nacional-e-regional.md`](08-nacional-e-regional.md).

**Armadilha de nome.** As cadeias `trt3.hist.*` de `tabelas-normativas/` **são NACIONAIS**: seus
fundamentos declarados são CC arts. 1.062–1.063, Lei 8.177/91 art. 39, Súmulas 200 e 381 do TST e
as paridades da moeda — e a correção monetária **delega à Tabela Única do CSJT**. O prefixo é do
arquivo, não da norma. **Um motor que resolva cadeia por prefixo de tribunal não acha cadeia
nenhuma para TRT-1, TRT-2 ou TRT-15.**

---

## 3. A precedência, por extenso

```
título judicial  >  escolha do usuário  >  default da jurisdição
```

**Três consequências que o motor precisa honrar:**

1. **título silente não é título contrário.** Sentença que não diz nada sobre o divisor não
   afasta o IRR-849 — ao contrário: a modulação da Súmula 124 alcança **expressamente** as
   sentenças transitadas e silentes ainda em liquidação;
2. **divergir do default é legítimo, esquecer de justificar não é.** R21 rejeita;
3. **o default marca a conta.** R20 não é decorativo: é o que permite a alguém revisar **o que
   ninguém decidiu**.

---

## 4. O que as invariantes não cobrem — e por que

| Ponto | Por que não vira invariante |
|---|---|
| **imputação proporcional** | não tem norma. Vira **preset sem default** — o motor não arbitra |
| **juros na base do IR** | **duas correntes** — Tema 808 do STF × OJ 400 da SDI-1. Ambas registradas |
| **classificação como Fazenda Pública** | **não é matéria de cálculo**, e o manual se contradiz |
| **data da dedução** | **três posições no mesmo manual** — ver `05-imputacao.md` § 3 |
| **ordem entre correção e juros** | **indiferente** por distributividade, delta 0,00 medido. O que altera é a **base** |

> **A última merece nota:** a pergunta "qual a ordem das operações?" tem resposta *não importa*.
> A pergunta produtiva é **"sobre que base cada uma incide?"** — e aí as diferenças medidas são
> −2,48%, −3,15% e −R$ 285,83.

---

## 5. Ponteiros

| Assunto | Detalhe |
|---|---|
| Cortes e eixos | `00-calendario-de-cortes.md` |
| Cadeias e defasagens | `02-atualizacao.md` |
| Verbas e a bifurcação de 11/11/2017 | `03-verbas.md` |
| INSS, IR, RRA | `04-descontos.md` |
| Amortização, rateio, descarregar, item "i" | `05-imputacao.md` |
| Custas, honorários, multas | `06-encargos.md` |
| **Como este manual se lê** | `07-leitura-do-corpus.md` |
| Defeitos do original | `../armadilhas-comparador.md` |
| Vereditos | `../confronto-normativo/01-vereditos.md` |
| O que está aberto | `../pendencias.md` |
