# Bloco 22 — Fase 6: aceitação

**Este bloco não corrigiu, não consolidou e não escreveu skill. Mediu.**

> **A skill não é o entregável. O código que um agente constrói lendo a skill é.** Este foi o
> único ponto do projeto onde isso se testou.

---

## Placar

```
bateram: 0   divergiram: 0   BLOQUEADAS por dado ausente: 4   de 4
```

**Nenhuma fixture produziu número errado.** As quatro **pararam antes de produzir número**.

| Fixture | Esperado | Obtido | Onde parou |
|---|---|---|---|
| **01** FP jun/2022 | 3.484,95 | — | série ausente: **IPCA-E de 2020-01** |
| **02** FP jun/2026 | 5.218,28 / 5.218,27 | — | idem — **e os dois métodos nunca são definidos** |
| **03** não-FP jun/2026 | 5.772,95 | — | série ausente: **IPCA-E de 2002-01** |
| **04** precatório | 4.435,07 / 4.435,04 | — | série ausente: **INPC de 2016-01**; e `pr.imputacao` sem default |

---

## A montagem

**Duas frentes, contextos separados, sem contato.**

**Frente A — implementador.** Recebeu **só** `skills/` e `tests/fixtures/calculo/`. **Proibido** abrir
`extracao/`, `consolidado/` ou relatório de bloco, salvo ponteiro que a própria skill declarasse.
Instrução: **parar e registrar** ao faltar informação, **não inventar**.

**Frente B — avaliador.** Recebeu skills, fixtures e o código da Frente A. **Podia** ler o
consolidado e a extração — precisa deles para julgar **omissão**. **Não podia** abrir o registro
de lacunas da Frente A antes de escrever o próprio julgamento.

**A Frente B declara ter seguido a ordem**, e a comparação das duas listas independentes é o
instrumento mais informativo do bloco.

---

## 1. O que a skill entregou

**E é substancial.** A Frente A implementou, só com o que as skills dizem:

- **as cinco cadeias de arredondamento de R12** — truncamento em 6 para fator, 2 para moeda,
  half-up para grandeza física, e o **NMP de três ramos**, acertando a faixa `x,y50`–`x,y54`
  onde ele difere de `ROUND_HALF_UP`;
- **R11 — o ponto mais forte.** A taxa legal por **razão entre fatores** bate nos dois pares
  publicados, e o código **demonstra ativamente** que a subtração de percentuais diverge;
- **R12 verificado por AST: zero literais `float`** em todo o motor;
- **R1 na composição**, exercitado mês a mês sobre as cadeias reais de 1964 a 2026, nos dois
  ramos de devedor: **zero cumulações**;
- **R2** acusando **só as duas sobreposições do original** — jan/1989, que o manual justifica, e
  mar/1990, que ele não justifica;
- **R5** chamado de dentro da correção, logo **por parcela**, como o invariante exige;
- e o motor **recusando arbitrar `pr.imputacao`** — a pendência chegou como pendência.

> **A skill ensinou a aritmética.** O que ela não deu foi **com o que calcular** e **em que
> ordem**.

---

## 2. O que a skill não disse e era necessário

**Duas causas independentes bloqueiam as quatro fixtures.** Qualquer uma sozinha já bastaria.

### (a) A camada (B) não existe no escopo lido

As skills publicam **cinco valores de índice ao todo**. **A fixture 1 sozinha precisa de 23 meses
de IPCA-E.**

**E a skill declara isso** — `indices-judiciais` diz literalmente *"esta skill não carrega série —
é o ponto inteiro dela"*, e `civel-federal.md` repete. **A limitação é honesta.**

> **O defeito não é a limitação: é a contradição.** O mesmo conjunto que declara não ter série
> **apresenta as fixtures como critério de aceite**. As duas afirmações não podem ser verdadeiras
> ao mesmo tempo.

### (b) "Método resumido" e "método detalhado" nunca são definidos

**É o achado que nenhuma das duas frentes esperava, e o mais grave.**

As fixtures **2** e **4** asseveram divergência **entre os dois métodos** — R$ 0,01 e R$ 0,03,
com `divergencia_e_assercao: true`. **Sem o procedimento de cada um, o motor produz um número,
não dois.**

> **Isto é inalcançável mesmo com todas as séries.** A asserção que o projeto trata como o melhor
> teste do pacote **não é executável a partir da skill**.

### As duas listas, feitas em separado

| | Itens | Comuns |
|---|---|---|
| **Frente A** | 14 | **9 fatos** |
| **Frente B** | 15 | |

**As duas elegem o mesmo #1 e o mesmo #2, na mesma ordem.** Convergência independente sobre o que
mais falta.

**Duas convergências valem mais que as outras**, por serem sutis: o conflito entre as **6 casas de
truncamento** que R12 manda e os **10 decimais publicados** no gabarito da fixture 3; e a redação
*"divergem do corpus"* do core.

**Cinco achados só da Frente A** — o melhor: **R1 "impedido na composição" está na prosa, não no
schema**; as cadeias cadastradas **se sobrepõem de fato** entre 2003 e 2009. **Seis só da
Frente B.**

### Outras lacunas que valem nome

- **a Fazenda entre jul/2009 e nov/2021 fica sem fórmula de `aplicacao`** — nem D1 nem D2;
- **"mensalizada" nunca é definido aritmeticamente**;
- **R3 dá a classe `janela-deslocada` e não dá a régua de ajuste** de nenhum dos três pares de
  virada.

---

## 3. O que a skill disse e estava errado

**É a categoria que mais importa. Lacuna declarada é honesta; regra errada não é.**

### A classificação de IPCA-E e IPCA-15 se contradiz entre skills

| Onde | O que diz |
|---|---|
| `calculo-judicial-core/SKILL.md` | *"**Dez** indexadores em uso são `indeterminado`* — entre eles **IPCA-E, IPCA-15**…" |
| `references/civel-federal.md` | *"**IPCA-E e IPCA-15 são `indeterminado`**"* |
| `indices-judiciais/SKILL.md` | *"**IPCA-15 e IPCA-E**"* → **`janela-deslocada`** |
| `indexadores-tipo-catalogo.json` | `IPCA-E/IBGE` → **`janela-deslocada`** · `IPCA-15/IBGE` → **`janela-deslocada`** |

**O catálogo é o dado que o validador lê, e diz `janela-deslocada`.** Duas skills ficaram no
estado anterior ao bloco 19. **E "dez" também envelheceu — são 17.**

> **Cai em cima das fixtures 1, 2 e 3**, que são exatamente cadeias de IPCA-E.
>
> **E a Frente A citou os dois lados no mesmo item sem perceber que se contradizem** — o que diz
> algo sobre quanto a contradição é detectável por quem lê de fora.

### "as fixtures 2 e 4 divergem **do corpus**"

**Não divergem do corpus. Divergem entre os dois métodos do próprio manual.**

**A redação induziu defeito real:** o runner da Frente A trata a tolerância como **banda de
aceitação** em vez de **asserir o par**. Um motor que zere a diferença passaria — e **motor que
zera está arredondando errado**.

---

## 4. O que o implementador inventou apesar da instrução de parar

**Três invenções declaradas, e as três estão nomeadas no registro:**

| # | O quê | Executou? |
|---|---|---|
| 1 | `getcontext().prec = 50` — o corpus não declara precisão | sim, transversal |
| 2 | a **ordem interna** da consolidação de dez/2021 | **nunca executou** |
| 3 | a tradução de *"inclusive para o mês de pagamento"* em D1 para lista de competências | **nunca executou** |

**Mais duas sub-declaradas**, que a Frente B achou: generalizar a NOTA 2 à taxa legal, e separar
honorários.

**Nenhum valor de índice foi inventado.** A Frente B conferiu os cinco literais contra as fontes
citadas.

### E o melhor dado do bloco está no que ela NÃO fez

A Frente A registrou **seis pontos em que quase inventou e se conteve**. Dois são caros:

- **não usou a taxa legal de mai/2026** — é da variante INPC, não IPCA-15;
- **não extraiu por álgebra** os 3,548% de Selic da parcela 02/2022 **a partir do gabarito da
  fixture**.

> **A segunda é a prova de que o teste funcionou.** O caminho existia, produziria o número
> esperado, e teria passado despercebido. **O registro mostra a álgebra e a recusa.**

**E houve uma recusa a mais, por escolha:** a Frente A **podia** abrir
`consolidado/09-ordem-de-calculo.md` — é ponteiro declarado — **e não abriu**, registrando a
decisão. Isso pode tê-la deixado sem a ordem ponta a ponta que o arquivo traz.

---

## 5. Os cinco critérios, respondidos

**1 — As quatro batem, com as divergências preservadas?** **Não.** Zero bateram, **zero erraram**,
quatro bloqueadas antes de produzir número. **A pergunta sobre as divergências não chegou a ser
testável** — e o runner as trataria como banda, não como asserção.

**2 — Os invariantes são observados?** **A distinção importa:**

| Invariante | Estado |
|---|---|
| **R1** · **R2** · **R5** · **R11** · **R12** | **implementados e verificados** |
| **R4** | implementado |
| **R4-EXCEÇÃO** | **mecânica presente, fronteira ausente — função morta.** A skill dá o *como*, não o *quando* |
| **R23** | **primitiva correta, não alcançada** — o código não chega lá |
| **R3** | **não implementado, por recusa declarada** — a skill dá a classe e não dá a régua |

**Nenhum foi implementado errado.**

**3 — Quantas lacunas?** **14 pela Frente A, 15 pela Frente B, 9 fatos comuns.**

**4 — As limitações declaradas correspondem?** **Em parte.** A ausência da camada (B) **está
declarada** e foi exatamente o que bloqueou. **A indefinição dos dois métodos não está declarada
em lugar nenhum** — e é o bloqueio que sobrevive mesmo com as séries.

**5 — Alguma pendência virou regra por omissão?** **Não.** `pr.imputacao` chegou como pendência e
o motor **recusou arbitrar**. Os índices `indeterminado` chegaram — ainda que com a classificação
contraditória da § 3.

---

## 6. Por que o resultado foi o que foi

**O teste não mediu o implementador. Mediu a integridade do conjunto de aceite.**

**As fixtures não são reproduzíveis por implementador algum, com skill ou sem.** A camada (B) não
existe no repositório, e os quatro totais só aparecem em `00-base-normativa.md` § 8 — **sempre
como resultado transcrito, nunca com os operandos**.

**Acima disso:** o procedimento dos métodos resumido e detalhado **não é definido em lugar
nenhum**, o que torna inalcançável a asserção que as próprias skills chamam de melhor teste do
pacote.

> **E o implementador se comportou exatamente como as skills pedem:** parou, nomeou o ponto de
> parada, declarou o escopo da busca, e não inventou valor algum.

**O bloco 23 escreve as correções a partir daqui. Nada foi corrigido neste bloco.**

---

## Artefatos

| Arquivo | O que é |
|---|---|
| `frente-a/` | o motor, o runner, o `README.md` e o **registro de lacunas** |
| `frente-b-avaliacao.md` | a avaliação independente, com a comparação das duas listas |
| este arquivo | o relatório do bloco |

**Reprodução:** `python docs/calculo/aceitacao/frente-a/runner.py`
