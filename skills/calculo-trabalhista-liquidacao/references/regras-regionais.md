# As quinze regras regionais — tribunal, efeito e fallback nacional

> **Convenção de rótulo.** `RG1`–`RG15` são as **regras regionais** deste arquivo.
> `R1`–`R24`, sem o `G`, são as **invariantes** de `calculo-judicial-core`. **São
> namespaces diferentes** — `RG14` é a posição da SEE/TRT-4 sobre RSR; `R14` é a
> invariante de ausência de norma coletiva. Confundi-los aplica a regra errada.

Fonte: `docs/calculo/consolidado/08-nacional-e-regional.md` §§ 3–7.

**São quinze, não três.** O enunciado original nomeava Súmula 15, Súmula 46 e OJ 23. O consolidado
invoca **nove verbetes regionais nominados** (`R1`–`R9`) mais **seis fontes regionais
não-verbete** (`R10`–`R15`), de **três** tribunais: **TRT-3**, **TRT-4** e **TJMG**.

**Cada linha está marcada com o tribunal.** A coluna do fallback é o que o motor usa quando o
tribunal da causa **não tem variante cadastrada** — `R24`.

---

## 1. A correção de premissa que torna esta tabela pequena

> **Origem declarada: EXTERNA AO CORPUS.** Vem do **enunciado do bloco 16**, que a declara
> verificada em fonte externa. **Não tem lastro em nenhum arquivo do repositório**, e **não foi
> conferida**.

A atualização monetária trabalhista é **NACIONAL** desde a **Res. CSJT 8/2005**, que unificou as
**24 tabelas** dos TRTs; hoje vale a **Res. CSJT 380/2024**, com duas tabelas — débitos comuns e
Fazenda Pública, esta referenciada ao **Manual do CJF**. O **PJe-Calc** é o sistema de toda a
Justiça do Trabalho.

**Duas consequências de arquitetura:**

- **(d)** A **aritmética do manual do TRT-3** — divisores, RSR, arredondamento, ordem INSS→IR,
  reconstrução de bruto, hora centesimal — **NÃO é prática regional divergente**. É **procedimento
  de uma região que aplica norma nacional**. Regional são **os verbetes que ele invoca**.
- **(e)** A **Tabela Única do CSJT** deixa de ser *"integração desejável"* e passa a ser **a
  dependência que torna o motor nacional**.

**Critérios de classificação aplicados:** **NACIONAL** = lei federal, CF, súmula/OJ/tese do TST,
STF, STJ, resolução CSJT/CNJ/CJF, IN da Receita. **REGIONAL** = súmula, OJ ou tese prevalecente de
**um** TRT ou TJ (art. 896, § 6º, CLT). **DÚVIDA** = usado sem hesitação — **não se presume
tribunal, não se presume vigência**.

**Escopo da busca, declarado.** Varredura 1: os **11 arquivos** de `docs/calculo/consolidado/`,
`grep -rn -i`, com os termos `TRT-3`, `TRT3`, `TRT 3`, `TJMG`, `CGJ`, `tese prevalecente`, `896`,
`regional`, `Súmula 15`, `Súmula 46`, `OJ 23`, `TRT-`, mais os regex `TRT-?[0-9]+`,
`SEE/TRT-[0-9]`, `TJ[A-Z]{2}`, `Provimento`, `001/02|001/2002`, `OJ 348`, `IRR-849`, `Súmula 431`.
Varredura 2: **repositório inteiro** (`--include=*.md --include=*.json`) para `tese prevalecente`,
`TJP [0-9]`, `art. 896, § 6`. Varredura 3, dirigida: `jurisprudencia-indice.md` (158 verbetes,
seções 17.5 a 17.8) e `02-base-normativa-verbas.md`.

**Resultados de ausência, com escopo:** `tese prevalecente` e `art. 896, § 6º` → **zero em todo o
repositório**; `regional` como palavra → **uma única ocorrência no consolidado** (é o próprio
corpus chamando a IN 001/02 de *"IN regional"*); **nenhum TJ estadual além do TJMG** aparece no
consolidado. **A busca é exaustiva sobre o TEXTO DO CONSOLIDADO, não sobre o universo de verbetes
regionais existentes** — o `jurisprudencia-indice.md` cataloga **24 verbetes regionais** no
capítulo 17 do manual (15 súmulas do TRT-3, 3 OJs de Turmas, 2 TJPs e 4 Provimentos), dos quais o
consolidado só invoca os listados abaixo.

---

## 2. A tabela

| # | Verbete / fonte | **Tribunal** | O que muda no resultado | Onde | **Fallback nacional** |
|---|---|---|---|---|---|
| **RG1** | **Súmula 15** — execução, depósito em dinheiro: a responsabilidade do executado **não cessa com o depósito** | **TRT-3** | dedução na **data do levantamento** (depósito em garantia) × **data do depósito** (para pagamento) — muda o principal deduzido e **a existência de diferença a apurar** | `05-imputacao.md` § 5; `02-atualizacao.md` § 12 (`P9-04`) | **ADC 58, item "i"** e **CC arts. 352–355**; na falta, o critério do **cap. 14, p. 306, letra "c"** — dedução na **data do pagamento**, salvo determinação do juízo |
| **RG2** | **Súmula 46** — base do adicional de insalubridade é o **salário mínimo**, salvo critério mais vantajoso | **TRT-3** | troca a base do adicional: mínimo × salário contratual/piso — altera o adicional **e todos os reflexos** | `03-verbas.md` § 5.9 e § 10 | **Súmula 228/TST** (cassada, MC na ADPF 151/STF) + **SV 4/STF** — **o conflito fica aberto, não resolvido aqui** |
| **RG3** | **OJ 23 das Turmas** — jornada 12×36, **divisor 210** | **TRT-3** | divisor do salário-hora na 12×36: **210 × 220** — muda o valor de **toda** hora extra e **todo** adicional calculado sobre hora | `03-verbas.md` § 5.6 | **IRR-849 do TST, tese 3** (divisor decorre da jornada; horas **remuneradas**) + **Súmula 431/TST** + **art. 64 da CLT** |
| **RG4** | **Súmula 24** — contribuições devidas a **terceiros**: incompetência da JT para executar | **TRT-3** | tira as contribuições de terceiros da conta (`R-07-16`) — **reduz o total de INSS executado** | `04-descontos.md` § 2.1 | **art. 114, VIII, da CF** + **Súmula 368, I, do TST** (competência limitada às contribuições do art. 195, I, "a", e II) |
| **RG5** | **Súmula 45** — fato gerador da contribuição até **04/03/2009** é o **pagamento** (regime de caixa) | **TRT-3** | escolhe o regime de apuração do INSS antes de 05/03/2009 — **caixa × competência**; muda alíquota, teto e atualização | `04-descontos.md` §§ 2.2 e 2.4 (`F7-11 VIGENTE`) | **art. 43, § 2º, da Lei 8.212/91** (MP 449/2008 → Lei 11.941/2009) e **Súmula 368, III, do TST** — o corte de **05/03/2009 é nacional e SOBREVIVE ao verbete** |
| **RG6** | **TJP 4** — Tese Jurídica Prevalecente: a **cota-parte patronal** **não integra** a base dos honorários advocatícios | **TRT-3** | exclui **R$ 18.574,26** da base no exemplo da p. 106 — **reduz os honorários** | `06-encargos.md` §§ 1 e 5.2 | **art. 791-A da CLT** (*"valor que resultar da liquidação da sentença"*) e **art. 85, §§ 2º a 5º, do CPC** para a Fazenda |
| **RG7** | **Súmula 39** — art. 384 da CLT (15 min da mulher) — **cancelada** pela **RA 123/2025**, perda de eficácia **a partir de 11/11/2017** | **TRT-3** | enquanto viva, **criava parcela** (15 min extras diários); cancelada, **não há parcela** | `03-verbas.md` § 2 (`B04-F6`) | **art. 384 revogado** pela Lei 13.467/2017 + **STF Tema 528** + **TST Tema 63**, **delimitados ao período anterior** |
| **RG8** | **Súmula 48** — prazo do art. 477 — **superada e cancelada** no portal do TRT-3; **o manual não a invoca** (zero em 471 páginas) | **TRT-3** | **nenhuma, hoje**: o prazo foi unificado em **10 dias corridos** | `03-verbas.md` § 5.11 | **art. 477, § 6º, da CLT** (Lei 13.467/2017) + **Teses 71 e 139 do TST** |
| **RG9** | **Súmulas 2 e 38** — turno ininterrupto de revezamento, horas além da 6ª, **divisor 180** | **TRT-3** | divisor do turno de revezamento | `03-verbas.md` § 5.6 | **OJ 396 da SDI-1/TST** (citada no mesmo parágrafo) + **art. 7º, XIV, da CF** — **o fallback já está ao lado do verbete, o que torna a substituição barata**. **Ver `D3`: a Súmula 38 não consta do índice** |
| **RG10** | **Tabela CGJ/TJMG** — correção monetária cível em Minas | **TJMG** (Corregedoria-Geral) | índice de correção do crédito cível para períodos **anteriores a jan/2003** | `02-atualizacao.md` §§ 1 e 4 | **STJ, Tema 1368** (Corte Especial, 15/10/2025, REsp 2.199.164/PR e REsp 2.070.882/RS), **vinculante** — § 3 abaixo |
| **RG11** | **IN GP/CR/VCR 001/2002 do TRT-3** — arts. 2º e 6º e **Anexo II** (14 rubricas C-1 a C-14, emolumentos E-1 a E-8, teto R$ 1.915,38, CE de 0,5% até R$ 638,46) | **TRT-3** | fixa **TODOS os valores** de custas de execução e emolumentos — nominais de 2002, **sem atualização monetária** | `06-encargos.md` §§ 1, 2.1 e 3 | **CLT arts. 789-A e 789-B** (a CLT dá as rubricas e os valores do art. 789-A; a IN regulamenta) + **IN 20/2002 do TST**. **Fora do TRT-3 há OUTRA IN regional, e os valores do Anexo II não valem** |
| **RG12** | **Acórdão TRT-3, AP 0001624-31.2012.5.03.0010** — sentença que defere reflexo em RSR **não autoriza incluir feriados** | **TRT-3** | **limite de coisa julgada**: impede inclusão de feriados no reflexo | `03-verbas.md` § 5.5 | **CLT art. 67 + Lei 605/49** e **art. 879, § 1º, da CLT** — **a distinção RSR × feriado é NACIONAL; o acórdão só a ilustra** |
| **RG13** | **Três ementas do TRT-3 sobre juros na falência**, *"duas delas divergentes entre si"* | **TRT-3** | se os juros **param na decretação da falência** | `02-atualizacao.md` § 2.2 | **art. 124 da Lei 11.101/05** + **Súmula 388/TST** (esta só quanto às multas dos arts. 467 e 477) |
| **RG14** | **SEE/TRT-4** — RSR sobre comissões **integram** a base das HE variáveis (Súmula 264) | **TRT-4** | inclui ou exclui o RSR da base da HE do **comissionista** | `03-verbas.md` § 5.10 | **Súmula 264/TST** + **Súmula 340/TST** + **OJs 235 e 397** — **a divergência é registrada, não arbitrada** |
| **RG15** | **Tabela própria do TRT-3 até outubro/2005** | **TRT-3** | índices de correção do débito trabalhista **até out/2005** | `02-atualizacao.md` § 6 | **Tabela Única do CSJT** (Res. 8/2005) a partir de **nov/2005**; **antes disso NÃO HÁ fallback nacional no corpus** — lacuna `P9-02` |

> **Total: 15 itens REGIONAIS** — **9 verbetes** (`R1`–`R9`) e **6 fontes regionais não-verbete**:
> uma tabela de corregedoria (`R10`), uma instrução normativa (`R11`), dois conjuntos de acórdãos
> (`R12`, `R13`), uma posição de órgão fracionário de outro TRT (`R14`) e uma tabela
> administrativa histórica (`R15`).

**Desta skill, tocam diretamente a apuração:** `RG1`, `RG2`, `RG3`, `RG4`, `RG5`, `RG6`, `RG7`, `RG8`,
`R9`, `R11`, `RG12` e `R14`. **`R10`, `RG13` e `RG15` são de atualização** — vivem em
`skills/calculo-judicial-atualizacao/references/`, e estão aqui só para a contagem fechar.

---

## 3. Quando o tribunal não tem súmula cadastrada — `R24`

**Cai no fallback nacional da última coluna, e isso é RESOLUÇÃO, não erro.** Três consequências e
uma vedação:

1. **A resolução é total, nunca parcial.** Para cada uma das quinze existe fallback nacional
   identificado — **exceto `RG15`**, onde o corpus **não tem** fonte nacional para o período.
   **Esta é a única regra da lista que não resolve por fallback**, e permanece **`P9-02`**,
   pendência aberta.
2. **O default NÃO é a regra do TRT-3.** Hoje o motor herdaria do manual mineiro por ser a fonte
   extraída. Depois da correção de premissa, **o default é a norma nacional**, e o TRT-3 é **uma**
   entrada da tabela regional, ao lado de TRT-4 (`RG14`) e TJMG (`RG10`).
3. **Silêncio do tribunal não é adesão ao verbete de outro tribunal.** Se o TRT-9 não tem súmula
   sobre divisor na 12×36, aplica-se **IRR-849 / Súmula 431**, **não** a OJ 23 do TRT-3 — *"as
   três mudam resultado e não valem fora de Minas"*. Espelha a regra dura do
   `jurisprudencia-indice.md` § 1: **ausência de notícia não é notícia de vigência**.
4. **Vedação: a chave NÃO harmoniza divergência.** Onde há duas correntes com fundamento próprio e
   nenhuma arbitrada — `V-05`, `V-06`, `V-07`, `V-09`, `F7-03`, a divergência de base dos
   honorários —, a chave **seleciona o eixo, não o resultado**. **Resolver seria inferir.**

**Precedência, contra `R8`:** a chave regional entra **dentro do default, nunca acima do título**.
Comando exequendo que fixe divisor 220 na 12×36 **afasta a OJ 23 mesmo em Minas**, por art. 879,
§ 1º, da CLT.

**Bifurcação temporal do `R10`, que não é resíduo:** até **dez/2002** vale a Tabela CGJ/TJMG
(REGIONAL); de jan/2003 a 29/08/2024, **SELIC**; a partir de 30/08/2024, **IPCA + taxa legal** —
os dois últimos NACIONAIS. O que a substitui é o **STJ, Tema 1368**, vinculante. **Mas a tabela
sobrevive em três hipóteses:** períodos anteriores a 2003; processos cujo **título** fixou
expressamente aquele critério; processos com **trânsito em julgado** sob o regime anterior — por
**R8** (a invariante de precedência, **não** o verbete `RG8`).

---

## 4. NACIONAL que se confunde com regional — diretriz (d)

**Nada disto é prática regional divergente:**

| Regra | Fonte que sustenta a classificação |
|---|---|
| Ordem **INSS antes de IR**, base do IR = líquido de INSS (`R-07-01`) | art. 74 do Dec. 3000/99; IN RFB 1.500/2014 |
| Assimetria das cotas empregado/empregador (`R-07-02`) | arts. 20 e 22 da Lei 8.212/91 |
| Base do INSS = valor **original** (`R-07-10`), bloqueio pelo teto (`R-07-11`) | art. 20 da Lei 8.212/91; art. 276, § 4º, do Dec. 3048/99 |
| **NMP** do RRA e seu arredondamento — **três ramos** | **IN RFB 1500/2014, art. 45, § único** |
| Regimes do **art. 12-A × 12-B** e tabela de IRRF | Lei 7.713/88; Lei 12.350/2010 |
| **Divisores** 220/200/180/150/120 e o **240 pré-CF/88** | **Súmula 431/TST**, **IRR-849/TST**, art. 64 da CLT, CF/88 |
| **RSR e feriados**, rol e forma de remuneração | CLT art. 67; Lei 605/49; Leis 10.607/02, 6.802/80, 9.093/1994; Súmula 146/TST |
| **Arredondamento** — half-up em grandeza física, 2 casas | classificado NACIONAL **pelo enunciado do bloco 16**; o corpus registra `P10 · P17` — cadeia **não declarada**, quatro práticas distintas |
| Hora centesimal; ficção `×1,142857`; `×4,285714` | art. 73, § 1º, da CLT; Súmula 60/TST; OJ 97 — a tensão `P8` com o `4,2857` do IRR-849 é **entre duas fontes nacionais** |
| Reconstrução do bruto antes do rateio; **`R23` descarregar** | **regra de conta, sem veículo regional**; fundamento no cap. 10 e no 16 |
| Termo inicial dos juros = ajuizamento · `aplicacao` = 1º dia do mês subsequente | CLT art. 883; **Súmulas 200 e 381/TST** |

**Armadilha de nome — as cadeias `trab.hist.*` são NACIONAIS.** Os quatro JSON de
`tabelas-normativas/` com esse prefixo têm **conteúdo inteiramente nacional**: CC arts.
1.062–1.063, Lei 8.177/91 art. 39, Súmulas 200 e 381 do TST, paridades da moeda, e a correção
**delega à Tabela Única do CSJT**. **O prefixo é do arquivo de origem, não da norma.** Um motor
que resolva cadeia **por prefixo de tribunal não acha cadeia nenhuma para TRT-1, TRT-2 ou
TRT-15**. Mesmo vício de nome nos `trt3-18.*.json`, cujo conteúdo é **IN RFB, Lei 8.212/91 e Lei
8.880/94**.

---

## 5. As DÚVIDAS — oito, nenhuma resolvida por inferência

| # | Dúvida | O que falta |
|---|---|---|
| **D1** | `OJ 348` em `06-encargos.md` § 5.2: *"OJ 348 e TJP 4 do TRT-3"* — o "do TRT-3" governa **só a TJP 4** ou **as duas**? O índice lista **apenas três** OJs de Turmas do TRT-3 (4, 23 e 29), o que **inclina** para a SDI-1 do TST | ler a `pagina_pdf` 106. **Inclinação não é classificação** |
| **D2** | os verbetes de `P13` — Súmulas 24, 102, 109, 118, 199 e 370, OJ 235. **A Súmula 24 é do TRT-3**; as outras **não têm tribunal declarado**, e o índice tem **numeração colidente** entre 17.1 (TST) e 17.5 (TRT-3) | conferir cada número contra a seção de origem |
| **D3** | **Súmula 38 do TRT-3**: o índice § 17.5 traz 15 súmulas — **2, 5, 10, 11, 15, 23, 24, 25, 27, 28, 29, 39, 45, 46, 50** — e **a 38 não está lá**. Ou é súmula não catalogada, ou é erro de número, ou é de outro tribunal | conferir a p. 37/48. **Enquanto isso, `RG9` vale com segurança só para a Súmula 2** |
| **D4** | `FGTS a depositar` na base dos honorários — o corpus a chama de *"regra do TRT-3 de 2016"* **sem citar verbete** | o veículo (`P8-F4-03`) |
| **D5** | `SEE/TRT-4` — SEE é **órgão fracionário**. Se a posição estiver em súmula ou tese prevalecente, é REGIONAL plena (`R14`); se for jurisprudência **sem verbete editado**, não entra na regra do art. 896, § 6º | o veículo da posição |
| **D6** | **vigência da Súmula 46 do TRT-3** após a cassação da Súmula 228/TST em 2018. **A classificação como REGIONAL é firme; a vigência é a dúvida.** O índice marca o verbete como **`não coberto`**, e a regra dura é explícita: *"verbete não coberto fica `não coberto`, **nunca** `vigente` por omissão"* | consulta ao portal do TRT-3 |
| **D7** | os **Provimentos do TRT-3** — **01/93, 03/91, 04/00** e o **Prov. Conjunto GCR/GVCR n. 3, de 15/12/2015**. **Zero ocorrências de `Provimento` no consolidado** (a única é o **Prov. 207/2025 do CNJ**, nacional). Os quatro são regionais e **procedimentais**, não de cálculo — mas o **04/00 disciplina memória e resumo** do cálculo, e o Conjunto **remete expressamente ao Manual** | decidir se o motor emite memória/resumo, e por regra nacional ou regional |
| **D8** | a **IN 001/02** (`RG11`) foi classificada REGIONAL porque o corpus a chama de *"IN regional"* — **mas não é súmula nem tese do art. 896, § 6º**: é ato administrativo de corregedoria. **A tipologia não tem casa para ela.** Mesmo problema em `RG10` e `R15` | uma terceira etiqueta — sugestão, `REGIONAL-ADMINISTRATIVO` — ou a decisão de que **valores de custas são parâmetro de configuração, não regra** |

---

## 6. O que este arquivo NÃO faz

**Não altera os arquivos do consolidado.** **Não resolve pendência aberta** — `P9-02`, `P9-04`,
`P8`, `P13`, `P8-F4-03` e a vigência da Súmula 46 seguem abertas. **Não renomeia** os JSON
`trab.hist.*` — só registra o achado. **Não classifica** `tabelas-normativas/trt3-18.*.json` nem
os 158 verbetes do `jurisprudencia-indice.md`: **lidos para conferência, não classificados item a
item.** **Não confirma** a premissa da § 1 — ela é externa, e assim está declarada.
