# Limitações declaradas — por extenso

Companheiro de [`../SKILL.md`](../SKILL.md), seção **Limitações declaradas**, que traz as sete
em tabela. Aqui está cada uma com a busca que a sustenta, os operandos e a pendência.

> **Movido da espinha no bloco 16, pelo limite de 500 linhas. Nenhuma limitação foi removida da
> skill** — as **sete que bloqueiam a conta** continuam nomeadas lá, com a consequência de cada
> uma. As de nº **8 a 10** existem só aqui, e a espinha declara isso.

---

**Não é rodapé. É o que impede usar a skill fora do que ela sustenta.**

**1 — A cobertura de súmulas regionais é de **TRT-3, TRT-4 e TJMG** — e só esses três.** São **quinze regras regionais
catalogadas** (9 verbetes + 6 fontes não-verbete) de **três** tribunais: TRT-3, TRT-4 e TJMG. **Outras
regiões exigem cadastro de súmulas, não refatoração** — a chave `(regra, tribunal, competência)` já existe e
o fallback nacional está identificado para catorze das quinze. **Silêncio do tribunal não é adesão ao
verbete de outro tribunal** (R24).

**2 — Os dois bloqueios aritméticos das pp. 266 e 269 seguem abertos.** Deltas de **10,00 exatos**
(`P11B-01`) e **2.036,51** (`P10D-01`). **Nenhum é arredondamento.** Para fechar o primeiro seria preciso
`H = 1.350,52`, que **não resulta de operação alguma do exemplo** (`373,70 / 3.184,55 = 11,735%`, não os
12,08% da Selic). O segundo propaga: J `138.448,90 → 140.485,41`; IR `4.162,83 → 4.468,30`.

**3 — `pr.imputacao` não tem default, e a razão não é indecisão.** **Aplicado 101 vezes, fundamentado
zero.** Buscas com escopo declarado: `art. 354`, `354 do C` e `artigo 354` → **0 ocorrências em 471
páginas**; `354`, `imputa`, `Código Civil`, `Súmula` e `anatocismo` → **0 cada no segmento que aplica a
regra**; `proporcional` → **101** no mesmo segmento. **Não são duas normas concorrentes: são uma norma — o
art. 354 do CC — contra um costume de liquidação sem base declarada.** Amplitude medida: **até 23,83%** do
saldo. **Juros primeiro produz saldo maior: o art. 354 favorece o CREDOR; o proporcional favorece o
DEVEDOR.** **Escolher um default seria o motor tomar posição jurídica.** `P11B-07`, aberta.

> **Armadilha de previsão, dentro desta limitação:** o Exemplo 5 tem **quase o dobro** da participação de
> juros do Exemplo 1 e amplitude percentual **menor**, porque ali o limitante é o **abatimento**, não os
> juros. **Qual das três grandezas limita muda de caso para caso.**

**4 — As faixas do art. 85, § 3º, do CPC e a série histórica de normas coletivas são DADOS EXTERNOS.** Das
faixas, a regra estrutural está fechada com fonte primária (`P8-F4-02`): a unidade é o **salário-mínimo**;
as faixas são **progressivas** (art. 85, § 5º); a data do salário-mínimo é a do **§ 4º, IV — sentença
líquida ou decisão de liquidação, não o ajuizamento**; e **o percentual é entrada arbitrada, não saída
calculada**. **Os VALORES numéricos continuam não transcritos no repositório** — busca refeita sobre
`docs/**/*.md` com `duzentos` e `salários-mínimos`: **duas ocorrências, ambas metalinguísticas**. Na mesma
família, os índices dos **dez planos econômicos de 1986 a 1996 não estão nas tabelas do item 18** (`P19`), e
`pr.planos-economicos` fica **bloqueado por falta de série**.

**5 — A base das custas de execução é definida SÓ POR EXCLUSÃO — `P13B-01`.** O item 8.2.1 diz o que **sai**
(apenas as custas do conhecimento) e que *"nenhuma outra verba deverá ser excluída, nem mesmo imprensa
oficial e honorários, salvo determinação judicial contrária"*. **Nunca diz o que ENTRA, nem em que estado.**
Busca com escopo declarado: `bruto` e `líquido` → **zero ocorrências nos itens 8.2 e 8.2.1**; nas pp.
100–106 as ocorrências existem, mas são **todas sobre honorários advocatícios e IR de peritos**. **O eixo
bruto × líquido simplesmente não é endereçado. Resolver seria inventar.**

**6 — A classificação como Fazenda Pública tem DOIS TESTES INCOMPATÍVEIS no mesmo manual, e NÃO É MATÉRIA DE
CÁLCULO.** Cap. 8, p. 102: isentos os entes *"que não explorem atividade econômica"*. Cap. 14, p. 306:
isentos os órgãos da administração *"direta e indireta"*, **sem a ressalva**. **Para um ente da indireta que
explore atividade econômica, os dois capítulos dão respostas opostas.** `economia mista` → **zero
ocorrências nas 471 páginas**; a única equiparação nominada é a **ECT**, e só *"para efeito de execução e do
DL 779/1969"*. **É pergunta ao jurídico do usuário do módulo.** Se a resposta for negativa, somem do escopo
o ramo Fazenda Pública, precatório, ECs 113 e 136 e a consolidação de dez/2021. **Os dois ramos ficam
registrados. Não harmonizo.**

**7 — Pontos que repousam em FONTE SECUNDÁRIA:**

| Ponto | Estado |
|---|---|
| **desdobramento i.1 × i.2 do item "i" da ADC 58** | `portal.stf.jus.br` em **HTTP 403**; modulação **sem transcrição literal verificada**; **inteiro teor dos três precedentes do TST não lido**. **Confirmar antes de produção** |
| **Tema 833 do STF** — sustenta a alíquota única até 02/2020 | STF em 403; **confiança médio-alta**. **Alta** para a regra, a data e o método da **EC 103/2019**, cujo texto foi conferido |
| **percentuais da transição da Lei 14.973/2024** | **lei não lida**; secundária comprovadamente ruidosa (uma fonte trazia *"até 31 de janeiro de 2025"* onde deveria ler-se **dezembro**). **NÃO USAR SEM LER A LEI** |
| **ADI 5766 sem modulação** · **aditamentos de set/2025 do Tema 935** · **literalidade da Súmula 362/TST** | só secundária; acórdãos **não lidos** · PDF da Res. 198/2015 retornou **HTTP 500** |
| **`F7-08`** (IN 1.500/2014) · **`F7-12`** (PLR) · **`F7-06`** (arts. 855-C a 855-E) · art. 457, §§ 3º e 4º | **sem conferência artigo a artigo**; confiança média, **baixa** nos §§ 3º e 4º do art. 457 |
| **premissa da nacionalidade trabalhista** (Res. CSJT 8/2005 e 380/2024, PJe-Calc) | **externa ao corpus**, do enunciado do bloco 16, **não conferida** |
| **cassação da Súmula 228** — Rcl **6.275** × Rcl **6266** (`E14-03`) | mesma data, reclamação diferente. **Nenhum inteiro teor lido** |

**8 — Endereços normativos quebrados; o de-para NÃO foi levantado.** O **Dec. 3.000/1999** foi revogado pelo
**Dec. 9.580/2018** (`F7-07`, `SUPERADO` por **veículo normativo**, não por regra material — as **leis** que
ele consolidava seguem vigentes e reconsolidadas). **Todas as remissões do cap. 9.3 a artigos do RIR/99
estão mortas como ENDEREÇO** — inclusive o **art. 74** (`R-07-01`, ordem INSS→IR) e o **art. 56**
(fundamento do IR proporcional ao valor pago). O de-para artigo a artigo **não foi feito** (Planalto
inacessível). Na mesma família: o **destino individual dos códigos 2909, 1708, 1889 e 5936** tem **confiança
nula** — as fontes tratam da substituição **em bloco**.

**9 — Divergências registradas e NÃO harmonizadas — as duas correntes entram, com fundamento:**

| # | Sobre | Por que as duas ficam |
|---|---|---|
| **`F7-03`** | **juros na base do IR** — OJ 400 da SDI-1 × **Tema 808 do STF** | o Tema 808 **não revogou** a OJ 400, e a OJ **não foi cancelada**: um decidiu um recorte, a outra afirma a regra geral. **Eixo MATERIAL**, não temporal, **sem corte de efeitos** (modulação pedida e recusada). **Preset sem default**, como `pr.imputacao`. Conflito interno correlato, `P7-02`: a matriz 18.1 marca juros como tributáveis; o item 9.3.3 exclui em duas hipóteses |
| **V-01** · **V-05** | base da insalubridade · MP 808 | SV 4 (salário mínimo) × **Rcl 53.157** (parâmetro anterior preservado) — o recorte da exceção não está em precedente qualificado · aplicar o texto no período em que vigeu × ignorar a subjanela, que caducou **sem** decreto legislativo |
| **V-06** | Súmula 85 (IV e VI), OJ 388 e Súmula 60, II — **não canceladas** apesar do conflito | verbete vigente vincula até cancelamento formal × o cancelamento é **declaratório, não constitutivo** (art. 177, I, do RITST, invocado nos próprios considerandos) |
| **V-07 · V-08 · V-09** | Súmula 291 e o art. 8º, § 2º · período aquisitivo **a cavaleiro** de 11/11/2017 no tempo parcial (**três leituras; nenhuma regra legal nem precedente vinculante**) · feriado em 12×36 pós-Reforma | nenhuma arbitrada. **Não infiro** |
| **V-11 · V-12 · V-13** | ADI 5766: afasta a fixação × fixa sob condição suspensiva (art. 98, § 3º, CPC) · autorização sindical **individual** ou por assembleia · art. 20 da Lei 8.212/91 **sobrestado** × tacitamente revogado | as duas primeiras **não mudam o líquido do reclamante**; a terceira **não muda número algum** — muda a fundamentação do laudo |
| **P13B-04** · **P9 · P11 · P16 · P18** | juros sobre honorários periciais · divergências **internas** do manual | **quatro acórdãos em cada sentido** · registradas nos blocos, **não harmonizadas** |
| — | **data da dedução: TRÊS posições no mesmo manual** | cap. 10 (**levantamento**, em todos os exemplos, **sem fundamento**: `Súmula` e `16.4.11` têm zero ocorrências no segmento) × cap. 16, item 16.4.11 (**duas teses**, separadas pela finalidade do depósito, **Súmula 15 do TRT-3**) × cap. 14, p. 306 (**pagamento**, *"salvo determinação do juízo"*). `P11B-06` · `P13C-01` |
| — | **E14-05**, suspeita registrada e **não corrigida** | *"pela média dos últimos doze meses"* **não está no art. 457, § 1º**, nem antes nem depois da Reforma — a média de doze meses estava no § 8º da Lei 13.419 e referia-se a **gorjetas**. **Fundamento frágil; veredito inalterado** |

**10 — Pendências que esta skill NÃO resolve — viram limitação, nunca regra:**

| ID | O que está aberto |
|---|---|
| `P10D-08` | **migração de regime tributário (12-A ↔ 12-B) no mesmo cálculo** — caso único (Ex. 5), **sem disciplina em todo o manual**: `migra*`, `transição` e `dois regimes` → **0 nas 471 páginas** |
| `P10D-05` · `P10D-04` | a **alternativa da letra I de 10.3.2** não tem exemplo em lugar nenhum do cap. 10 · a **obrigatoriedade do critério alternativo da letra C**, *declarada e não demonstrada*: `obrigatór*`, `porque` e `razão` → **0 nas pp. 266–277** |
| `P13A-03` · `P13A-02` | **falta a regra de escolha da base do IR com/sem juros** no item 10.2 — `OJ 400` → **0 nas pp. 223–237** · **os dois rateios do cap. 10 sem fundamento** |
| `P7-01` | ordem de imputação do **recolhimento parcial**: um padrão e **duas alternativas sem critério**, convivendo com uma **segunda ordem, proporcional entre rubricas**, em 9.2.7.3-A |
| `P7-05` · `P7-06` · `P7-07` | **qual** prazo de citação inicia a multa, nunca definido · **multa sobre a cota do reclamante** aplicada nos exemplos **sem enunciado** · ausência do salário de contribuição suprida por **presunção declarada** (*"presumindo que a reclamada efetuou o recolhimento corretamente"*) |
| `P7-04` · `P7-08` · `P7-09` | 13º como base autônoma no INSS **sem enunciado** (só planilha) · honorários advocatícios **não aparecem como dedução em lugar nenhum do cap. 9** · sem regra de **segregação anual** do RRA |
| `P8` · `P10` · `P17` | duas constantes para 30/7 — **4,285714** (item 5.3) × **4,2857** (IRR-849), **tensão entre duas fontes nacionais** · **cadeia de arredondamento do cap. 6 não declarada**, quatro práticas distintas |
| `P13` · `P16` | verbetes sem regra desenvolvida: Súmulas 24, 102, 109, 118, 199 e 370, OJ 235 — **`D2`: só a 24 tem tribunal declarado** · conversão do seguro-desemprego (*"salário por semana ÷ 30 × 7"* **reduz** em vez de mensalizar), e a nota do MTE é **`SEM FONTE` verificada**: pendência, **não regra** |
| `D1` · `D3` · `D4` · `D6` | `OJ 348` é da SDI-1 do TST ou do TRT-3? · **Súmula 38 não consta do índice** — `R9` vale com segurança só para a Súmula 2 · o **FGTS a depositar** na base dos honorários **não tem veículo declarado** · **vigência da Súmula 46** após a cassação da Súmula 228 |
| — | o art. 791-A fala em *"valor que resultar da liquidação"*; **nada no corpus confirma que o FGTS a depositar sobreviva na base** · **responsabilidade e momento das custas do conhecimento não são enunciados** no item 8.1 · **teto do art. 789 não é declarado** · **D15-02**: colisão `F1`–`F9` (bloco 03) × `F1`–`F7` (bloco 04), **ainda aberta nos dois relatórios de origem** |

---
