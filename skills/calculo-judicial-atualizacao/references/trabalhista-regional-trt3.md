# Trabalhista — o que é REGIONAL (TRT-3), e o fallback nacional

**Este arquivo existe para separar o que vincula uma região do que vale no país inteiro.** A
cadeia de indexador e juros é **nacional** — está em `trabalhista-nacional.md`. Aqui ficam os
**verbetes e fontes regionais que o manual do TRT-3 invoca** e que, mudando de tribunal, **mudam
o resultado**.

**Fonte:** `docs/calculo/consolidado/08-nacional-e-regional.md` §§ 2, 3, 4, 5, 6 e 7;
`01-dominio-e-invariantes.md` § 2.9 (**R24**).

---

## 1. A premissa corrigida, e o que ela reclassifica

> **Origem declarada: EXTERNA AO CORPUS** — enunciado do bloco 16.

O projeto vinha tratando o manual do TRT-3 como **fonte de prática regional**. **Está errado.**
O manual é **fonte procedimental de uma região que aplica norma nacional**. O próprio corpus já
dizia isso sem tirar a consequência: o TRT-3 **delega o encadeamento inteiro à Tabela Única do
CSJT**.

**Diretriz (d) — o que NÃO é regional, embora venha do manual do TRT-3:**

| Regra | Fonte que sustenta a classificação nacional |
|---|---|
| ordem **INSS antes de IR**, base do IR = líquido de INSS | art. 74 do Dec. 3000/99; IN RFB 1.500/2014 |
| assimetria das cotas empregado/empregador | arts. 20 e 22 da Lei 8.212/91 |
| base do INSS = valor **original**, correção depois; bloqueio pelo teto | art. 20 da Lei 8.212/91; art. 276, § 4º, do Dec. 3048/99 |
| **NMP** do RRA e seu arredondamento (três ramos) | IN RFB 1500/2014, art. 45, § único |
| **divisores** 220/200/180/150/120 e o 240 pré-CF/88 | Súmula 431/TST; **IRR-849/TST**; art. 64 da CLT; CF/88 |
| **RSR e feriados** | CLT art. 67; Lei 605/49; Súmula 146/TST |
| hora centesimal; ficção `×1,142857`; `×4,285714` | art. 73, § 1º, da CLT; Súmula 60/TST; OJ 97 |
| **termo inicial dos juros = ajuizamento**, salvo vincendas | **CLT art. 883; Súmula 200/TST** |
| **`aplicacao` = 1º dia do mês subsequente à prestação** | **Súmula 381/TST** |
| reconstrução do bruto antes do rateio; **R23** descarregar antes dos juros | regra de conta, sem veículo regional |
| **arredondamento** half-up em grandeza física, 2 casas | classificado NACIONAL **pelo enunciado do bloco 16**; o corpus registra `P10 · P17` — cadeia **não declarada**, quatro práticas distintas |

**As duas últimas linhas das cadeias `trt3.hist.*` são nacionais** — ver
`trabalhista-nacional.md` § 1(c). **O prefixo `trt3.` mente sobre o alcance.**

---

## 2. As regras REGIONAIS que tocam ESTA skill

Três das quinze. As outras doze são de apuração de verbas, descontos ou encargos — ficam
listadas na § 3 com ponteiro, **não desenvolvidas aqui**.

### `R1` — **Súmula 15 do TRT-3** · execução, depósito em dinheiro, atualização e juros

**Tribunal:** TRT-3. **Onde:** `consolidado/05-imputacao.md` § 5; `02-atualizacao.md` § 12
(`P9-04`); `07-leitura-do-corpus.md` § 4.

**O que muda no resultado:** a **data da dedução** — **levantamento** (depósito em garantia) ×
**depósito** (depósito para pagamento). Muda o principal deduzido e **a existência de diferença a
apurar**.

**Fallback nacional:** **ADC 58, item "i"** (`05-imputacao.md` § 4) e **CC arts. 352–355**; na
falta, o critério do **cap. 14, p. 306, letra "c"**: dedução **na data do pagamento**, salvo
determinação do juízo.

> **O que retirar a Súmula 15 apaga não é o critério — é o EIXO DE ESCOLHA.** Há **três posições
> no mesmo manual** sobre a data da dedução, e **só uma é regional**:
>
> | # | Onde | Data | Fundamento | Classificação |
> |---|---|---|---|---|
> | 1 | cap. 10, **todos os exemplos** | **levantamento** | **nenhum** — `Súmula` e `16.4.11` têm **zero ocorrências no segmento** | **NACIONAL** |
> | 2 | cap. 16, item **16.4.11** (pp. 333–334) | **duas teses**, separadas pela finalidade do depósito | **Súmula 15 do TRT-3** | **REGIONAL — é esta** |
> | 3 | cap. 14, p. 306, letra "c" | **pagamento**, *"salvo determinação do juízo"* | — | **NACIONAL** |
>
> As posições 1 e 3 **coincidem em resultado** com os dois ramos da tese regional. O que a
> Súmula 15 fornece é o **`natureza_do_deposito`** do preset `pr.adc58-item-i`.

**Pendência correlata:** `P11B-06` — o segmento C adota a dedução na data do levantamento **sem
citar** a Súmula 15 nem o 16.4.11.

### `R13` — **três ementas do TRT-3 sobre juros na falência**

**Tribunal:** TRT-3. **Onde:** `02-atualizacao.md` § 2.2 (`pagina_pdf` 89).

**O que muda:** **se os juros param na decretação da falência.** O manual transcreve três
ementas, ***"duas delas divergentes entre si"***.

**Fallback nacional:** **art. 124 da Lei 11.101/05** — juros limitados à data da falência
**apenas se houver determinação nos autos** — e **Súmula 388/TST**, esta **só quanto às multas**
dos arts. 467 e 477, § 8º.

> **Divergência registrada, NÃO harmonizada.** As duas correntes entram, com fundamento.
> E a Súmula 388 **decide outro ponto**: INSS, IR e custas **continuam integrando a execução**
> contra a massa (armadilha **A21**, p. 332).

### `R15` — **tabela própria do TRT-3 até outubro/2005**

**Tribunal:** TRT-3. **Onde:** `02-atualizacao.md` § 6.

**O que muda:** os **índices de correção do débito trabalhista até out/2005**.

**Fallback nacional:** **Tabela Única do CSJT** (Res. CSJT 8/2005) **a partir de nov/2005**.
Antes disso — **não há fallback nacional no corpus**.

> **`R15` é a ÚNICA das quinze regras regionais que não resolve por fallback.** É lacuna, ligada
> a **`P9-02`**, e permanece **pendência aberta**. Ver `trabalhista-nacional.md` § 5.

---

## 3. As demais regras regionais — fora do escopo desta skill

Listadas para que ninguém conclua que não existem. **Desenvolvimento em
`consolidado/08-nacional-e-regional.md` § 4**, com o fallback nacional de cada uma na coluna 6.

| # | Verbete / fonte | Tribunal | Skill que as consome |
|---|---|---|---|
| `RG2` | **Súmula 46** — base do adicional de insalubridade é o salário mínimo, salvo critério mais vantajoso | TRT-3 | `calculo-trabalhista-liquidacao` |
| `RG3` | **OJ 23 das Turmas** — 12×36, **divisor 210** | TRT-3 | idem |
| `RG4` | **Súmula 24** — contribuições a **terceiros**: incompetência da JT | TRT-3 | idem |
| `RG5` | **Súmula 45** — fato gerador do INSS até 04/03/2009 é o **pagamento** | TRT-3 | idem |
| `RG6` | **TJP 4** — cota-parte patronal **não integra** a base dos honorários | TRT-3 | idem |
| `RG7` | **Súmula 39** — art. 384 da CLT, **cancelada** pela RA 123/2025, eficácia perdida a partir de **11/11/2017** | TRT-3 | idem |
| `RG8` | **Súmula 48** — prazo do art. 477, **superada e cancelada**; **o manual não a invoca** (zero em 471 páginas) | TRT-3 | idem |
| `RG9` | **Súmulas 2 e 38** — turno de revezamento, **divisor 180** | TRT-3 | idem |
| `RG11` | **IN GP/CR/VCR 001/2002** — custas de execução e emolumentos, **Anexo II**, valores nominais de 2002 **sem atualização** | TRT-3 | `calculo-trabalhista-liquidacao` |
| `RG12` | **AP 0001624-31.2012.5.03.0010** — reflexo em RSR não autoriza incluir feriados | TRT-3 | idem |
| `RG14` | **SEE/TRT-4** — RSR sobre comissões integra a base das HE variáveis | **TRT-4** | idem |
| `RG10` | **Tabela CGJ/TJMG** | **TJMG** | `civel-regional-tjmg.md` |

**Total: 15 regras regionais**, de **três tribunais** — TRT-3, TRT-4 e TJMG. **Nove são verbetes**
(súmula/OJ/TJP) e **seis são fontes não-verbete**: uma tabela de corregedoria, uma instrução
normativa, dois conjuntos de acórdãos, uma posição de órgão fracionário e uma tabela
administrativa histórica.

> **O enunciado original do bloco 16 nomeava três.** São quinze. Contagem em
> `08-nacional-e-regional.md` § 4.

---

## 4. Como o motor resolve — `R24` e a chave `(regra, tribunal, competência)`

**`R24` — ausência de súmula regional NÃO é erro.** Competência sem verbete regional cadastrado
para o tribunal resolve pela **regra nacional** e marca a conta como **`sem cobertura
regional`**. Não bloqueia, não erra: **registra**. É a mesma forma da **R14** (norma coletiva), e
a simetria é deliberada — `sem cobertura coletiva` e `sem cobertura regional` são a mesma espécie
de silêncio: **o dado não existe, não a regra**.

| Componente | O que é |
|---|---|
| **`regra`** | o **ponto de cálculo**, não o verbete: `deducao.data`, `juros.falencia`, `correcao.tabela`, `divisor.12x36`, `insalubridade.base` |
| **`tribunal`** | o TRT ou TJ da causa. **Só entra** onde há variante regional cadastrada; ausente, é **ignorado** — não vira o valor `"nacional"` |
| **`competência`** | necessária porque **verbete regional nasce e morre com data** — a Súmula 39 do TRT-3 foi cancelada **com eficácia retroagida a 11/11/2017** |

**Quatro consequências, e uma vedação:**

1. **A resolução é total, nunca parcial** — há fallback nacional identificado para **14 das 15**.
   A exceção é **`R15`**;
2. **O default NÃO é a regra do TRT-3.** Depois da correção de premissa, **o default é a norma
   nacional**, e o TRT-3 é **uma** entrada da tabela regional, ao lado de TRT-4 e TJMG;
3. **Silêncio do tribunal não é adesão ao verbete de outro tribunal.** Se o TRT-9 não tem súmula
   sobre divisor na 12×36, aplica-se **IRR-849/Súmula 431**, **não** a OJ 23 do TRT-3. Espelha a
   regra dura do índice de jurisprudência: **ausência de notícia não é notícia de vigência**;
4. **`R24` não cria exceção à `R8`.** O **título judicial continua vencendo**: comando exequendo
   expresso (art. 879, § 1º, da CLT) afasta o verbete regional **mesmo dentro da região que o
   editou**. A chave regional entra **dentro do default**, nunca acima do título;
5. **Vedação — a chave NÃO harmoniza divergência.** Onde há duas correntes com fundamento próprio
   e nenhuma arbitrada, a chave **seleciona o eixo, não o resultado**.

---

## 5. As DÚVIDAS — nenhuma resolvida por inferência

São oito em `08-nacional-e-regional.md` § 6. **As que tocam esta skill:**

| # | Dúvida | O que falta |
|---|---|---|
| **D6** | **vigência da Súmula 46** do TRT-3 — a **classificação como regional é firme; a vigência é a dúvida**, após a cassação da Súmula 228/TST | consulta ao portal do TRT-3. O índice marca o verbete como **`não coberto`**, e a regra dura é explícita: *verbete não coberto fica `não coberto`, **nunca** `vigente` por omissão* |
| **D5** | **`SEE/TRT-4`** — Seção Especializada em Execução é **órgão fracionário**. Se a posição estiver em súmula ou tese prevalecente, é regional plena; se for jurisprudência **sem verbete editado**, não entra na regra do art. 896, § 6º | o **veículo** da posição |
| **D8** | a **IN 001/02** foi classificada REGIONAL porque o corpus a chama de *"IN regional"* — mas **não é súmula nem tese** do art. 896, § 6º: é **ato administrativo de corregedoria**. **A tipologia não tem casa para ela** | uma terceira etiqueta (`REGIONAL-ADMINISTRATIVO`) ou a decisão de que valores de custas são **parâmetro de configuração**, não regra. **Mesmo problema atinge `R10` e `R15`** |
| **D3** | **Súmula 38 do TRT-3** — o índice lista 15 súmulas do TRT-3 (2, 5, 10, 11, 15, 23, 24, 25, 27, 28, 29, 39, 45, 46, 50) e **a 38 não está lá** | conferir a p. 37/48 do manual. Enquanto isso, `R9` vale com segurança **só para a Súmula 2** |
| **D7** | os **Provimentos do TRT-3** (01/93, 03/91, 04/00 e o Prov. Conjunto GCR/GVCR 3, de 15/12/2015). **`Provimento` tem zero ocorrências no consolidado** além do Prov. **207/2025 do CNJ**, que é nacional. Os quatro são regionais e **procedimentais** — mas o **04/00 disciplina memória e resumo do cálculo**, e o Conjunto **remete expressamente ao Manual** | decidir se o motor emite memória/resumo e, em caso positivo, por regra nacional ou regional |

---

## 6. Escopo da busca — declarado

**Varredura 1** — os 11 arquivos de `docs/calculo/consolidado/`, `grep -rn -i`, termos: `TRT-3`,
`TRT3`, `TRT 3`, `TJMG`, `CGJ`, `tese prevalecente`, `896`, `regional`, `Súmula 15`, `Súmula 46`,
`OJ 23`, `TRT-`, mais os regex `TRT-?[0-9]+`, `SEE/TRT-[0-9]`, `TJ[A-Z]{2}`, `Provimento`,
`001/02|001/2002`, `OJ 348`, `IRR-849`, `Súmula 431`.

**Varredura 2** — repositório inteiro (`--include=*.md --include=*.json`): `tese prevalecente`,
`TJP [0-9]`, `art. 896, § 6`.

**Varredura 3 — dirigida:** `jurisprudencia-indice.md` (158 verbetes, seções 17.5 a 17.8) e
`02-base-normativa-verbas.md`.

**Resultados de ausência, com escopo:**

- `tese prevalecente` e `art. 896, § 6º` — **zero ocorrências em todo o repositório**;
- `TRT 3` com espaço e `TRT3` como referência a tribunal — **zero no consolidado**;
- `regional` como palavra — **uma única ocorrência no consolidado**, e é o corpus chamando a
  IN 001/02 de *"IN regional"*;
- **nenhum TJ estadual além do TJMG** aparece no consolidado.

> **A busca é exaustiva sobre o TEXTO DO CONSOLIDADO, não sobre o universo de verbetes regionais
> existentes.** O capítulo 17 do manual cataloga **24 verbetes regionais** — 15 súmulas do TRT-3,
> 3 OJs de Turmas, 2 Teses Prevalecentes e 4 Provimentos —, dos quais o consolidado invoca
> apenas os listados acima.

---

## 7. Cadastrar outra região

**É cadastro, não refatoração.** Para uma nova região basta acrescentar entradas
`(regra, tribunal, competência) → variante`, com:

- o **verbete** e seu texto;
- a **janela de vigência** — data de edição **e** data de perda de eficácia, que pode ser
  **retroativa** (Súmula 39/TRT-3: cancelada em 2025, eficácia perdida em 11/11/2017);
- o **ponto de cálculo** que ela altera;
- o **fallback nacional** já existente, que continua valendo para todos os demais tribunais.

**O motor não muda.** O que muda é a tabela.

---

## 8. Ponteiros

- `docs/calculo/consolidado/08-nacional-e-regional.md` — a classificação completa, os 15 itens
  com fallback, as 8 dúvidas
- `docs/calculo/consolidado/01-dominio-e-invariantes.md` § 2.9 — **R24** e a chave
- `docs/calculo/jurisprudencia-indice.md` §§ 17.5–17.8 — os 24 verbetes regionais do cap. 17
- `references/trabalhista-nacional.md` — a cadeia, que **não** é regional
- `references/civel-regional-tjmg.md` — a outra região catalogada
