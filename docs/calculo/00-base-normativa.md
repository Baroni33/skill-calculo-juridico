# Base normativa — cálculo judicial (cível, trabalhista, tributário federal)

**Status:** pesquisado e validado contra fontes primárias e acórdãos. Data da pesquisa: 18/09/2026.
**Uso:** fonte de verdade para o motor de cálculo. Prevalece sobre o conteúdo dos manuais em PDF quando houver conflito, porque os manuais têm datas de corte diferentes.
**Não contém:** séries de valores mensais dos índices (manutenção separada).

---

## 1. Trabalhista — devedor privado

Fonte: STF, ADC 58 e ADC 59 — TST, SDI-1, E-ED-RR-713-03.2010.5.04.0029, Rel. Min. Alexandre Agra Belmonte, j. 17/10/2024, DEJT 25/10/2024.

| Fase | Correção monetária | Juros de mora |
|---|---|---|
| Pré-judicial | IPCA-E | art. 39, *caput*, Lei 8.177/1991 (TRD) |
| Ajuizamento até 29/08/2024 | SELIC (engloba ambos) | — |
| A partir de 30/08/2024 | IPCA | Taxa legal (CC art. 406, § único) |

**Atenção:** IPCA-**E** na fase pré-judicial; IPCA (sem E) a partir de 30/08/2024. A distinção é do dispositivo do acórdão. Muitas fontes secundárias escrevem IPCA nos dois lugares — estão erradas.

**Marco inicial dos juros: AJUIZAMENTO**, não citação. Difere do cível.

Regras acessórias do dispositivo:
- Ressalvados os valores eventualmente pagos, nos termos da primeira parte do item "i" da modulação do STF.
- Vedada a dedução ou compensação de eventuais diferenças pelo critério de cálculo anterior.
- Taxa legal admite resultado zero (CC art. 406, § 3º).

**Divergência doutrinária registrada:** parte da doutrina sustenta que aplicar juros pela TRD na fase pré-judicial é incompatível com a própria ADC 58, que declarou a TR inconstitucional para débitos trabalhistas. Expor como variante no catálogo de critérios, não como default.

### 1.1 O item "i" da modulação tem DUAS situações

> **ORIGEM DESTA SUBSEÇÃO.** Conteúdo de **pesquisa jurisprudencial externa ao corpus**,
> trazido pelo enunciado do bloco 12 e conferido em **fontes secundárias que reproduzem a
> fundamentação**. **O inteiro teor dos três precedentes não foi lido.** Declarado nos mesmos
> termos em que se declarou a origem do art. 611-B da CLT no bloco 5. Confirmar contra o
> inteiro teor antes de usar em produção.

Precedentes citados:

| Órgão | Relator | Publicação |
|---|---|---|
| TST, 6ª Turma, ED-RR | Min. Kátia Magalhães Arruda | DEJT 17/03/2023 |
| TST, 7ª Turma, Ag-RR | Min. Cláudio Mascarenhas Brandão | DEJT 17/03/2023 |
| TST, SDI-1, E-Ag-RR | Min. Hugo Carlos Scheuermann | DEJT 10/03/2023 |

A ressalva de valores pagos **não é incondicional**. O TST distingue duas situações, e a
diferença entre elas decide se o critério do STF alcança ou não o que já foi pago.

#### Situação i.1 — pagamento consolidado (regra)

Valores pagos ao exequente **sem qualquer questionamento**, ou objeto de **trânsito em
julgado**.

- **não** são recalculados pelos critérios das ADCs 58 e 59 para dedução ou compensação;
- na atualização, **desconsidera-se o que já foi pago** pelos parâmetros anteriores;
- os índices do STF incidem **apenas sobre o montante que ainda falta pagar**;
- valores depositados judicialmente **e já levantados** seguem esta regra e **não entram na
  conta de liquidação atualizada**.

**Recorte do alcance dentro de i.1:**

| Alcança | Não alcança |
|---|---|
| depósito com **finalidade de pagamento** | **depósito recursal** |
| **valor incontroverso liberado** ao reclamante (pagamento consolidado) | a **parte controversa** do depósito em garantia |

#### Situação i.2 — execução questionada (exceção)

Execução instaurada **após o início dos debates da ADC 58**, havendo **questionamento
expresso de qualquer das partes** sobre a necessidade de observar o posicionamento do STF.

- a atualização leva em conta os novos índices **inclusive sobre os valores já pagos**;
- o TST trata esta hipótese como **exceção ao item "i"**.

#### Consequência para o motor

**O conflito entre o rateio proporcional do Manual TRT-3 e a modulação é condicional, não
estrutural** — ver `extracao/trabalhista/bloco-11b-amortizacao.md` § 9, que o marcara como o
maior atrito do projeto:

- **em i.1 o rateio não se aplica ao valor pago.** Não há o que ratear: o pago sai da conta e
  o critério novo incide só sobre o residual. **O método do manual — recompor o bruto até a
  data do pagamento antes de deduzir — é exatamente o que a modulação veda nesta situação;**
- **em i.2 o rateio se aplica**, sobre valores recalculados pelo critério novo. A proporção
  mudar porque os juros mudaram **é o comportamento correto**, não um defeito.

A escolha entre i.1 e i.2 **não é derivável do cálculo**: depende de estado processual e de
evento (houve questionamento expresso?). Entra como preset — `pr.adc58-item-i`, em
`presets-regime.md`.

---

## 2. Trabalhista — devedor Fazenda Pública

Ramo ressalvado expressamente pela ADC 58.

| Período | Correção | Juros |
|---|---|---|
| Até nov/2021 | IPCA-E | Lei 11.960/2009 |
| A partir de dez/2021 | SELIC (engloba ambos) | — |

Fonte: TST, 2ª Turma, ata da 17ª sessão ordinária de 2026 (RR 131300-14.2010.5.21.0006).

**Pendência:** efeito da EC 136/2025 sobre a Justiça do Trabalho não consolidado pelo TST nem pelo CSJT. Ver seção 5.

---

## 3. Cível — Código Civil (aplicável ao TJMG e em geral)

| Período | Correção monetária | Juros de mora |
|---|---|---|
| Até dez/2002 | Tabela CGJ/TJMG (em MG) | 0,5% simples (CC/1916, arts. 1.062–1.064) |
| Jan/2003 a 29/08/2024 | SELIC (engloba ambos) | — |
| A partir de 30/08/2024 | IPCA (CC art. 389, § único) | Taxa legal (CC art. 406, § 1º) |

**Fonte do trecho central — STJ, Tema 1368**, Corte Especial, j. 15/10/2025, REsp 2.199.164/PR e REsp 2.070.882/RS, Rel. Min. Ricardo Villas Bôas Cueva; acórdão publicado em 20/10/2025:

> O art. 406 do Código Civil de 2002, antes da entrada em vigor da Lei n° 14.905/2024, deve ser interpretado no sentido de que é a SELIC a taxa de juros de mora aplicável às dívidas de natureza civil, por ser esta a taxa em vigor para a atualização monetária e a mora no pagamento de impostos devidos à Fazenda Nacional.

A SELIC engloba simultaneamente correção monetária e juros moratórios, **vedada sua cumulação com outros índices inflacionários**.

Precedentes referenciados: EREsp 727.842/SP; Temas 99, 112 e 113 dos repetitivos da 1ª Seção; REsp 1.795.982/SP; RE 1.558.191/SP (STF, 2ª Turma, j. 12/09/2025).

**Supersessão importante:** até outubro de 2025 a jurisprudência majoritária do TJMG para o período anterior à Lei 14.905 era tabela da CGJ mais juros de 1% ao mês. O Tema 1368 é vinculante e substitui essa prática. O TJMG já publicou o tema no seu portal de precedentes qualificados.

**Quando a tabela CGJ/TJMG ainda se aplica:** períodos anteriores a 2003; processos cujo título fixou expressamente aquele critério; processos com trânsito em julgado sob o regime anterior.

### Termos iniciais no cível

| Situação | Correção monetária | Juros |
|---|---|---|
| Regra geral | — | Citação (CPC) |
| Responsabilidade extracontratual | — | Evento danoso (Súmula 54/STJ) |
| Ato ilícito | Efetivo prejuízo (Súmula 43/STJ) | — |
| Dano moral | Arbitramento (Súmula 362/STJ) | — |

---

## 4. Taxa legal — metodologia

Fonte: Resolução CMN n. 5.171, de 29/08/2024 (DOU 30/08/2024, Edição 168, Seção 1, p. 259-260). Vigência imediata. Regulamenta o art. 406 do CC na redação da Lei 14.905/2024.

### Fórmula

```
TL_m = (Fator_Selic_m / Fator_IPCA15_{m-1} - 1) × 100
```

- Seis casas decimais.
- Razão entre a acumulação das Taxas Selic diárias e a taxa de variação do IPCA-15 **relativas ao mês anterior ao de referência**.
- Resultado negativo é considerado igual a zero no mês de referência (CC art. 406, § 3º).
- Regime de **juros simples**, inclusive e especialmente para a acumulação de taxas mensais e para a apuração de juros proporcionais (pro rata).

### NÃO é subtração de percentuais

A lei e o acórdão do TST descrevem "SELIC deduzido o IPCA". Isso é descrição do efeito. A **operação é razão entre fatores**, não subtração. Implementar a subtração literal produz número errado.

Validação aritmética contra a tabela do Manual de Cálculos do CJF (Res. 990/2026), taxa legal previdenciária:

| Competência | Fator Selic | Fator INPC | Manual | Razão | Subtração |
|---|---|---|---|---|---|
| Set/2025 | 1,01164156 | 0,9979 | 1,377047% | **1,377047%** ✓ | 1,374156% ✗ |
| Mai/2026 | 1,01090058 | 1,0081 | 0,277807% | **0,277807%** ✓ | 0,280058% ✗ |

Divergência de ~0,003 p.p./mês. Acumula.

### Divulgação

- Banco Central divulga mensalmente a taxa legal, o Fator Selic_m e o Fator IPCA_m.
- Séries no SGS. Série 29541 = Fator da Taxa Selic mensal para cálculo da Taxa Legal.
- Primeira taxa legal divulgada em 30/08/2024, aplicável aos dias 30 e 31/08/2024. A partir de setembro de 2024, divulgação no primeiro dia útil de cada mês.
- Calculadora do Cidadão do BCB tem módulo de taxa legal — serve como oráculo de teste.

### Variante previdenciária (Justiça Federal)

Mesma metodologia, com **dedução do INPC** em vez do IPCA-15. Fonte: Manual CJF, Res. 990/2026, item 4.3.2, Nota 3.

---

## 5. EC 136/2025 — Fazenda Pública

Promulgada em 09/09/2025. Reescreveu o art. 3º da EC 113/2021.

### Redação anterior (EC 113/2021)

> Nas discussões e nas condenações que envolvam a Fazenda Pública, independentemente de sua natureza e para fins de atualização monetária, de remuneração do capital e de compensação da mora, inclusive do precatório, haverá a incidência, uma única vez, até o efetivo pagamento, do índice da taxa referencial do Sistema Especial de Liquidação e de Custódia (Selic), acumulado mensalmente.

### Redação nova (EC 136/2025)

> Nos requisitórios que envolvam a Fazenda Pública federal, a partir da sua expedição até o efetivo pagamento, a atualização monetária será feita pela variação do Índice Nacional de Preços ao Consumidor Amplo (IPCA), e, para fins de compensação da mora, incidirão juros simples de 2% a.a.

Trava: se a soma da atualização monetária com os juros de mora superar a SELIC no mesmo período, aplica-se a SELIC em substituição.

### Três estreitamentos simultâneos

| Eixo | Antes | Depois |
|---|---|---|
| Objeto | Discussões e condenações | Só requisitórios |
| Ente | Toda Fazenda Pública | Só Fazenda Pública **federal** |
| Período | Do início até o pagamento | Da expedição até o pagamento |

### Regra de incidência (CNJ, Provimento 207/2025)

A partir de setembro de 2025:
- Os precatórios são atualizados pelo IPCA, incidindo esse indexador sobre **principal e juros somados**.
- Os juros de 2% a.a., calculados mensalmente, incidem sobre o **principal, excluídos os juros já apurados**.

Essa assimetria é regra de implementação e não decorre da leitura da emenda. Vai para o motor como especificação.

### Fase pré-requisitório

Vácuo normativo preenchido pelo Código Civil:
- STJ, REsp 2.236.270/SP, Rel. Min. Gurgel de Faria, publicado em 02/03/2026: a nova redação restringe-se exclusivamente aos requisitórios; na fase de conhecimento aplica-se o art. 406 do CC.
- STF, ARE 1.557.312/SP (Tema 1.419).
- CJF, Res. 990/2026: encerra a SELIC na fase pré-requisitório a partir de setembro de 2025; aplica IPCA para correção e taxa legal para juros. Previdenciário mantém INPC e taxa legal com dedução do INPC.

### Instabilidade

- **ADI 7873** questiona a emenda. Pendente.
- **Divergência:** TJ-SP, 2ª Câmara de Direito Público (AI 3001155-79.2026.8.26.0000), mantém a SELIC para débitos não submetidos à fase de precatório, aplicando a EC 136 apenas após a expedição do requisitório.
- **Fazenda Pública estadual e municipal:** a nova redação menciona apenas "Fazenda Pública federal". Requisitórios estaduais e municipais ficam sem a regra antiga (revogada) e sem a nova (que não os alcança).

---

## 6. Justiça Federal — cadeias do Manual CJF (Res. 990/2026)

### Condenatórias em geral (item 4.2.1.1)

| Período | Devedor Fazenda Pública | Devedor não Fazenda Pública |
|---|---|---|
| Jan/2001 a nov/2021 | IPCA-E | IPCA-E |
| Dez/2021 a ago/2024 | SELIC | IPCA-E |
| Set/2024 a ago/2025 | SELIC | IPCA-15 |
| A partir de set/2025 | IPCA-15 | IPCA-15 |

### Benefícios previdenciários (item 4.3.1.1)

| Período | Correção |
|---|---|
| Set/2006 a nov/2021 | INPC |
| Dez/2021 a ago/2025 | SELIC |
| A partir de set/2025 | INPC |

Juros: SELIC de dez/2021 a ago/2025; taxa legal com dedução do INPC a partir de set/2025.

### Consolidação em dez/2021

Crédito consolidado com base no mês de dez/2021 pelos critérios então aplicáveis. Sobre o valor consolidado, sem exclusão de qualquer parcela, incide a SELIC a partir de jan/2022 (competência dez/2021), nos termos do § 1º do art. 22 da Res. CNJ 303/2019, com redação do art. 6º da Res. CNJ 448/2022. O resultado, chamado "Juros Selic", soma-se integralmente à parcela "Juros até 12/2021".

Valores de fechamento por ramo:

| Ramo | Índice de nov/2021 | Juros de dez/2021 |
|---|---|---|
| Condenatórias em geral / desapropriação | IPCA-E 1,17% | 0,4412% |
| Previdenciário | INPC 0,84% | 0,4412% |
| Trabalhista (JF) | TR 0,00% | 0,4412% |

### Repetição de indébito tributário (item 4.4)

- Jan/1992 a jan/1996: Ufir
- A partir de jan/1996: SELIC (art. 39, § 4º, Lei 9.250/1995)
- Juros: 1% simples até 31/12/1995; SELIC a partir de 1º/01/1996
- Termo inicial dos juros: trânsito em julgado (CTN art. 167, § único)
- A EC 113/2021 não altera o cálculo, que já observa a SELIC desde jan/1996 — desnecessário consolidar em dez/2021

---

## 7. Invariantes do motor

Regras que, violadas, produzem erro material. Devem ser impedidas na composição, não detectadas no resultado.

**R1 — Exclusividade de englobamento.** Segmento cujo `engloba` cobre correção e juros não admite outro segmento do mesmo componente no mesmo intervalo. Vale para SELIC e taxa legal. Impede contar inflação duas vezes.

**R2 — Cobertura sem lacuna nem sobreposição.** A união dos segmentos cobre da parcela mais antiga até a data-base.

**R3 — Tipo do indexador na virada.** Nominal (Ufir, BTN, OTN, ORTN) reflete a inflação do mês anterior; percentual (INPC, IPCA, IGP) reflete a do próprio mês. Trocar entre tipos sem ajustar a defasagem desloca o cálculo em um mês. Fonte: Manual CJF, item 4.1.2.4.

**R4 — Capitalização.** Juros de mora, SELIC e taxa legal: sempre simples. Capitalização mensal só em juros remuneratórios.

> **R4-EXCEÇÃO — juros COMPOSTOS de 27/02/1987 a 03/03/1991.** Por força do **DL 2.322/87,
> art. 3º**. Não é defeito de transcrição: está no quadro geral do Manual TRT-3
> (`pagina_pdf` 89), repetido no quadro da Fazenda (`pagina_pdf` 92) e **confirmado de forma
> independente pela cadeia do Manual CJF** para o mesmo período — três registros, duas
> jurisdições, edições separadas por dez anos. O manual dá inclusive a mecânica:
> *"1,0% ao mês, c/ taxa capitalizada. Ex.: 3 meses = 3,03%"*.
>
> **Gravado dentro do invariante, não em nota de rodapé:** quem ler apenas "juros de mora
> sempre simples" erra quatro anos de qualquer conta que atravesse o período.

**R5 — Piso nominal.** Índices negativos entram no cálculo, mas nenhuma parcela do principal fica abaixo do valor nominal. Fonte: REsp 1.265.580; Manual CJF item 4.1.2.2.

**R6 — Piso zero da taxa legal.** Resultado negativo vira zero, nunca negativo.

**R7 — Termo inicial dos juros não é intercambiável entre jurisdições.** Trabalhista: ajuizamento. Cível: citação, salvo Súmulas 54 e 362 do STJ. Repetição de indébito: trânsito em julgado.

**R8 — Precedência.** Título judicial > escolha do usuário > default da jurisdição. Toda divergência entre níveis fica registrada.

**R9 — Fazenda Pública é atributo do processo**, não configuração de sistema nem cadastro da empresa. A mesma parte pode receber classificações distintas em processos distintos.

**R10 — Pagamentos parciais.** Cível: imputação pelo art. 354 do CC. Trabalhista sob ADC 58: valores pagos são ressalvados e é vedada a dedução ou compensação de diferenças apuradas pelo critério anterior — **com as duas situações da § 1.1**. Regras diferentes, não unificáveis.

> **R10 está FUNDAMENTADA, e por razão mais forte que a suposta.** O bloco 11B extraiu a regra
> trabalhista: a imputação é **proporcional** — o pagamento abate principal e juros na razão em
> que compõem o bruto (Manual TRT-3, item 10.3.1, letra F, `pagina_pdf` 237). E **não tem
> fundamento normativo declarado**: `art. 354` não ocorre em nenhuma das 471 páginas do manual,
> enquanto `proporcional` ocorre 101 vezes só no segmento que a aplica.
>
> Não são duas normas concorrentes: são **uma norma (art. 354 do CC) contra um costume de
> liquidação sem base declarada**. Por isso a escolha entra como preset `pr.imputacao`, **sem
> default** — ver `presets-regime.md`.
>
> **Amplitude medida: até 23,83% do saldo.** Direção: juros primeiro produz saldo **maior**,
> logo dívida maior. O critério proporcional **favorece o devedor**; o art. 354 **favorece o
> credor**.

**R11 — Taxa legal calcula-se por razão entre fatores**, nunca por subtração de percentuais. Seis decimais, IPCA-15 do mês anterior.

**R12 — Aritmética decimal.** Nenhum float. Critério de truncamento definido e consistente por etapa. O Manual CJF registra que diferenças de centavos entre métodos decorrem do truncamento e são desprezíveis — isso só é verdade se o critério for consistente.

**R13 — Reprodutibilidade.** Toda conta grava: preset aplicado, overrides com justificativa, versão do conjunto normativo, versão das séries consumidas.

> **R14 a R22 não estão aqui.** Vivem nas camadas que as usam: **R14–R18** (norma coletiva) em
> `parametros-negociaveis.md`; **R19–R22** (regime temporal) em `presets-regime.md`. O salto de
> R13 para R23 nesta seção é de localização, não de numeração.

**R23 — Descarregar antes de aplicar juros.** Antes de aplicar juros sobre saldo remanescente, os juros já contidos nesse saldo devem ser excluídos. Aplicar juros sobre saldo que já os contém produz **anatocismo**.

> **Anomalia de localização do fundamento, registrada.** O Manual TRT-3 **executa** a operação
> em todo o capítulo 10 e a nomeia apenas como *"descarregar"* (`pagina_pdf` 237, única
> ocorrência da palavra no manual), **sem fundamentá-la**: `anatocismo` → **0 ocorrências** em
> todo o capítulo 10.
>
> Quem a nomeia como anatocismo é uma **minuta de petição do capítulo 16** (`pagina_pdf` 328):
> *"recalculando os juros de mora desde a inicial, não incidindo juros sobre juros
> (anatocismo)"*. A p. 328 abre com a **mesma frase** do item 10.3.1 — a diferença é que lá a
> operação é apenas nomeada, e aqui é qualificada juridicamente.
>
> **Precisão do bloco 13:** `anatocismo` ocorre nas pp. **16, 90, 328 e 335** — não é
> exclusivo do capítulo 16. A p. 16 trata da acumulação da Selic e a p. 90 da Fazenda Pública.
> **Exclusiva do capítulo 16 é a aplicação do conceito à operação de amortização.**
>
> **E são duas regras anti-anatocismo distintas, que o manual nunca reúne:** (1) juros
> acumulam por **soma** de percentuais, nunca por multiplicação — `pagina_pdf` 16, **única**
> invocação da **Súmula 121 do STF** em todo o manual; (2) o **descarregar**, `pagina_pdf` 237.
> A Súmula 121 é citada só para a primeira.
>
> Efeito medido: no Exemplo 5 do capítulo 10, aplicar juros sobre o saldo não descarregado
> produziria **+R$ 30.452,43**.

---

## 8. Fixtures de aceite

Casos com resultado numérico conhecido, do Manual CJF (Res. 990/2026, item 4.2.1.1, Nota 6).

### Fixture 1 — devedor Fazenda Pública, data-base jun/2022

Parcelas: 01/2020 R$ 1.000,00; 02/2020 R$ 1.000,00; 02/2022 R$ 1.000,00. Citação (termo inicial dos juros): 01/2021.

Resultado esperado: **R$ 3.484,95** (principal corrigido R$ 3.275,96; juros até 12/2021 R$ 55,75; juros SELIC R$ 153,24).

### Fixture 2 — mesmo caso, data-base jun/2026

Resultado esperado: **R$ 5.218,28** (principal corrigido R$ 3.412,64; juros R$ 1.805,64).

Diferença de R$ 0,01 entre o método detalhado e o resumido é esperada e decorre do truncamento. Um motor que zera essa diferença está arredondando errado.

### Fixture 3 — devedor não Fazenda Pública, data-base jun/2026

Parcelas: 01/2002 R$ 1.000,00; 08/2024 R$ 1.000,00. Citação: 01/2005.

Resultado esperado: **R$ 5.772,95** (principal corrigido R$ 2.554,45; juros R$ 3.218,50).

### Fixture 4 — precatório complementar (item 5.2.1)

Valor devido em jan/2016: principal R$ 20.000,00; juros R$ 3.000,00; honorários 10%; correção INPC. Pagamento em ago/2018 dentro do prazo constitucional (precatório apresentado em 01/07/2017). Atualização até maio/2020.

Resultado esperado: **R$ 4.435,07** pelo método resumido e **R$ 4.435,04** pelo detalhado.

A divergência de R$ 0,03 é esperada e documentada. É o melhor teste de arredondamento do conjunto.

---

## 9. Pendências abertas

| # | Pendência | Tipo | Bloqueia |
|---|---|---|---|
| 1 | Classificação da Gasmig como Fazenda Pública ou não | Determinação jurídica do cliente | Tamanho do catálogo |
| 2 | Tabela Única do CSJT — contrato de integração | Integração | Motor trabalhista |
| 3 | Efeito da EC 136/2025 na Justiça do Trabalho | Aguarda consolidação TST/CSJT | Ramo FP trabalhista |
| 4 | ADI 7873 | Aguarda julgamento | Estabilidade do ramo FP |

**Pendência 1 é a de maior impacto.** Se a Gasmig não for Fazenda Pública, somem do escopo: o ramo FP das três jurisdições, precatório, EC 113/136 e a consolidação de dez/2021. Não é pesquisa — é pergunta ao jurídico do cliente, ou leitura de como os juízes vêm decidindo nos processos existentes.

---

## 10. Nota sobre os manuais em PDF do repositório

**`manual_de_calculos_2026.pdf`** — Manual de Orientação de Procedimentos para os Cálculos na Justiça Federal, CJF, Res. 990/2026, 93 páginas. Edição vigente. Governa o tributário federal. **Não governa o contencioso cível estadual.**

**`manual-de-calculo-trabalhista_2016-1.pdf`** — Manual de Cálculos da Secretaria de Cálculos Judiciais do TRT-3, julho/2016, 471 páginas. Ainda é a versão publicada pelo TRT-3 como vigente. **Materialmente defasado** quanto a correção monetária, juros, honorários sucumbenciais e contribuição sindical: é anterior à Reforma Trabalhista (Lei 13.467/2017), à ADC 58, à EC 113/2021, à Lei 14.905/2024 e à EC 136/2025.

**Serve para:** estrutura de apuração de verbas (cap. 6), critérios matemáticos (cap. 5), estrutura dos descontos legais (cap. 9), tabelas históricas (cap. 18).

**Não serve como fonte normativa para:** cap. 7 (atualização e juros), cap. 10 (atualização de débitos), cap. 12 (contribuição sindical), cap. 14 (precatórios) e as partes do cap. 8 sobre honorários.

Lacuna conhecida: o item 2.8 do manual do CJF remete a um quadro de multas administrativas "anexado a este manual" que não existe no PDF.
