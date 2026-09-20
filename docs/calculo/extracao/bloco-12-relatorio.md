# Bloco 12 — relatório

Consolidação da base de conhecimento. **Não é extração:** é incorporar aos documentos
normativos decisões e achados que estavam espalhados pelos relatórios de bloco.

---

## 1. Entregas

| Tarefa | Estado |
|---|---|
| 1 — item "i" da modulação, duas situações | **Feita** — `00-base-normativa.md` § 1.1 |
| 2 — resolver o atrito marcado no 11B | **Feita** — `bloco-11b-amortizacao.md` § 9.1 |
| 3 — dois presets novos | **Feita** — `pr.adc58-item-i` e `pr.imputacao`, + 8 testes |
| 4 — invariantes R23 e R4-EXCEÇÃO | **Feitas** — `00-base-normativa.md` § 7 |
| 5 — `armadilhas-comparador.md` | **Criado** — 10 armadilhas, 4 reconferidas |
| 6 — destino dos caps. 8, 12, 14 e 16 | **Feita** — **zero páginas sem decisão** |
| 7 — pendências | **Feita** — `pendencias.md` § 20 |

**212 testes OK** (eram 204; +8 dos regimes novos).

---

## 2. O que mudou nos documentos normativos

### 2.1 `00-base-normativa.md`

**§ 1.1, nova** — o item "i" da modulação da ADC 58 tem **duas situações**, e a distinção
decide se o critério do STF alcança o que já foi pago:

| | i.1 — pagamento consolidado | i.2 — execução questionada |
|---|---|---|
| **Quando** | pago sem questionamento, ou trânsito em julgado | execução após o início dos debates da ADC 58, com questionamento expresso |
| **Recalcula o pago?** | **não** | **sim** |
| **Índices do STF incidem sobre** | só o que falta pagar | inclusive o já pago |

Com o recorte de alcance dentro de i.1: protege **pagamento** e **incontroverso liberado**;
**não** protege **depósito recursal** nem a **parte controversa** do depósito em garantia.

**R4 ganhou exceção nomeada, gravada dentro do invariante** — não em nota:

> **R4-EXCEÇÃO** — juros **compostos** de 27/02/1987 a 03/03/1991, por força do DL 2.322/87.
> Três registros independentes: quadro geral do TRT-3 (p. 89), quadro da Fazenda (p. 92) e a
> cadeia do CJF. **Quem ler só "juros de mora sempre simples" erra quatro anos.**

**R10 ganhou o lastro que lhe faltava**, e mudou de natureza — ver § 3.

**R23, nova** — descarregar antes de aplicar juros, com a anomalia de localização do
fundamento registrada.

**E uma nota de orientação:** R14–R22 não estão neste arquivo (vivem em
`parametros-negociaveis.md` e `presets-regime.md`). O salto de R13 para R23 é de localização,
não de numeração.

### 2.2 `presets-regime.md` e o catálogo

Dois regimes novos — **28 no total**:

- **`pr.adc58-item-i`** — eixo composto: estado processual ⊕ questionamento expresso ⊕
  **natureza do depósito**. **Tem default** (i.1, que é a regra).
- **`pr.imputacao`** — proporcional × art. 354 do CC. **Sem default.**

---

## 3. O achado que a consolidação produziu, e que nenhum bloco tinha

Os blocos 11B e 11C entregaram peças; juntá-las mudou a leitura de uma invariante.

**R10 dizia:** cível e trabalhista tratam imputação por regras diferentes, não unificáveis.
Estava escrita **sem a regra trabalhista extraída** — o próprio enunciado do 11B apontou isso.

**O 11B extraiu a regra** e o que apareceu não foi uma segunda norma:

| | |
|---|---|
| `art. 354` · `354 do C` · `artigo 354` — **471 páginas** | **0** |
| `proporcional` — no segmento que a aplica | **101** |

> **Não são duas normas concorrentes. São uma norma — o art. 354 do CC — contra um costume de
> liquidação sem base declarada.**

Isso não torna R10 falsa: torna-a **mais forte, e de outra espécie**. A não-unificabilidade
não vem de duas regras disputando o mesmo caso; vem de os dois lados serem **objetos de
naturezas diferentes**.

**Consequência de modelagem, e é ela que importa:** um motor não pode *derivar* o critério
proporcional do corpus, porque o corpus não o fundamenta. Tem de **oferecê-lo como escolha**,
com o fundamento declarado como o que é. Daí `pr.imputacao` sem default.

### 3.1 O quinto caso de R20-EXCEÇÃO é de espécie nova

**Correção de premissa do enunciado:** ele dizia "terceiro caso". O catálogo já tinha
**quatro** `sem_default`, e `presets-regime.md` § 9 registra que uma versão anterior dizia
"três" e foi corrigida. `pr.imputacao` é o **quinto**.

E a distinção que o enunciado fez está certa, e é o ponto:

| Casos 1 a 4 | Caso 5 |
|---|---|
| o corpus **deixa a questão aberta** — acórdãos nos dois sentidos, ou eixo não declarado | a **prática não tem norma e a norma não tem prática** |

Nos quatro primeiros, dar default seria escolher entre correntes. No quinto, seria decidir se
a prática predominante **tem autoridade** — questão de outra ordem.

### 3.2 A direção do delta, que o enunciado mandou registrar

```
amplitude = min(abatimento, principal, juros) × índice_residual × pct_juros_residual
```

**Juros primeiro produz saldo maior, logo dívida maior.** O critério proporcional **favorece o
devedor**; o art. 354 **favorece o credor**. Amplitude medida: até **23,83%** do saldo.

Sem a direção, o número não diz a quem a escolha favorece — e é exatamente isso que impede o
motor de arbitrar. Gravado no catálogo e coberto por teste.

---

## 4. O atrito do 11B: dissolvido, não harmonizado

O 11B marcou como maior atrito do projeto o conflito entre o rateio proporcional e a
modulação. **A Tarefa 1 o dissolve, e a forma da dissolução importa:**

**Não é que o manual esteja certo e a modulação errada, nem o contrário.** É que o método do
manual **se aplica ou não conforme um fato processual que o cálculo não conhece**:

- em **i.1** não há o que ratear — o pago sai da conta, e **recompor o bruto até a data do
  pagamento antes de deduzir é justamente o que a modulação veda**;
- em **i.2** o rateio se aplica, e **a proporção mudar porque os juros mudaram é o
  comportamento correto**, não um defeito.

Conflito **condicional**, não estrutural. E por isso vira preset, não correção.

---

## 5. `armadilhas-comparador.md` — por que existe

**Um perito que usa o manual reproduz os erros do manual.** O comparador precisa reconhecer o
número errado e nomear a causa, em vez de apenas acusar diferença.

Dez armadilhas catalogadas com `pagina_pdf`, valor impresso, valor correto e **assinatura
detectável**. As quatro de maior impacto foram **reconferidas contra o PDF nesta
consolidação**:

| | Verificação | Resultado |
|---|---|---|
| A1 — FGTS em dobro | `21.476,22` × `17.673,59`, excesso `3.802,63` | confere |
| A2 — P10D-01 | `55.236,01` **não existe em nenhuma das 471 páginas** | confere |
| A3 — P11B-01 | `976,82 + 384,69 = 1.361,51` contra `1.360,52` | confere |
| A4 — linha copiada | `125,11` ocorre **só na p. 261** | confere |

**E a reconferência corrigiu uma página:** A1 estava registrado na 296; a linha do defeito está
na **297**. Erro que a verificação por script pega e a leitura não.

O arquivo separa **defeitos do manual** (§ 1 e 2) de **deltas de método** (§ 3) e de
**comportamentos que não são defeito** (§ 4) — precisão plena, ausência de regra de
arredondamento, mês comercial com contagem inclusiva. **O limiar de alarme do comparador não
deve ser o centavo.**

---

## 6. Zero páginas sem decisão

| | Páginas |
|---|---|
| Cobertas | 409 |
| Não cobertas **com decisão registrada** | **54** |
| Não cobertas **sem decisão** | **0** |

| Cap. | Destino |
|---|---|
| 8 — encargos e despesas | bloco 13, extração normal |
| 12 — contribuição sindical | bloco 13, **estrutura**, marcado superado pela Reforma |
| 14 — precatórios | bloco 13, **estrutura**, marcado superado pela EC 113/2021 e EC 136/2025 |
| 16 — promoções | bloco 13, varredura dirigida, **reclassificado para FONTE NORMATIVA** |

### 6.1 O capítulo 16 deixou de ser formulário

Três achados forçaram a reclassificação, e o terceiro é decisivo:

- **16.4.11** — imputação na data do **levantamento**, com a **Súmula 15 do TRT-3**. O
  capítulo 10 executa a dedução em 56 páginas e **nunca cita a Súmula 15**;
- **16.4.7** — multa limitada ao principal **corrigido**, art. 412 do CC + OJ 54;
- **p. 328** — **o único lugar do manual** que conecta o "descarregar" ao anatocismo.

**O padrão se repetiu três vezes: o manual pratica no capítulo técnico e fundamenta na
minuta.** Quem extrair só os capítulos técnicos fica com as operações sem as razões.

---

## 7. O que precisou de conserto no código

Os dois regimes novos não couberam no vocabulário fechado do validador, e a recusa foi
correta — o validador fez o que devia.

**Três extensões, todas justificadas:**

- `evento-questionamento-expresso` e `natureza-do-deposito` — eixos genuinamente novos;
  nenhum sai do cálculo;
- `sem-eixo-temporal` — **e esta é conceitual**. `pr.imputacao` não tem eixo temporal porque
  a escolha **não varia no tempo**. Distinguir isso de `NAO-DECLARADO` importa: lá falta
  informação, aqui **não há o que faltar**.

**E uma recusa que respeitei:** o validador rejeitou `corte: "inicio-dos-debates-da-ADC-58"`
porque o campo exige data. **A correção não foi afrouxar o validador — foi gravar `corte:
null`** e pôr o evento em `corte_observacao`. O corpus não dá a data; cravar uma seria
inventá-la. Coberto por teste.

---

## 8. Correções de premissa do enunciado

Duas, ambas registradas:

- **"terceiro caso de R20-EXCEÇÃO"** → é o **quinto**. Já havia quatro no catálogo;
- **A1 na `pagina_pdf` 296** → a linha do defeito está na **297**.

É a quinta vez consecutiva que uma premissa do enunciado não resiste à verificação. A regra
que as apanha continua sendo a mesma: **exigir a busca que sustenta a afirmação, inclusive
quando a afirmação é minha ou sua.**

---

## 9. O que a Fase 3 recebe

**Fechado:** R10 fundamentada · R23 criada · R4 com exceção nomeada · o atrito do 11B
dissolvido · o comparador com catálogo de armadilhas · zero páginas sem decisão · 28 regimes
com 212 testes.

**Aberto, e por ordem de peso:**

1. **Dois bloqueios aritméticos** — P11B-01 (10,00 exatos) e P10D-01 (2.036,51 com índice sem
   origem). Nenhum dos dois é arredondamento;
2. **P11B-07** — o critério proporcional sem norma. Já modelado como preset, mas a questão
   jurídica segue aberta;
3. **P10D-04** — a obrigatoriedade do critério alternativo da letra C, que o manual declara e
   não demonstra;
4. **P10-C16** — varredura dirigida do capítulo 16, agora em prioridade alta;
5. **A origem externa da § 1.1** — o inteiro teor dos três precedentes do TST **não foi
   lido**. Confirmar antes de produção.

---

## 10. Lição de método

Os blocos anteriores fecharam com lições sobre extração. Esta é sobre **consolidação**:

> **Peças corretas e separadas podem esconder uma conclusão que só aparece quando se juntam.**
> O 11B registrou "a regra é proporcional e não tem fundamento". O 11C registrou "o
> fundamento do descarregar está numa minuta". Nenhum dos dois disse que **R10 era de espécie
> diferente do que a invariante supunha** — isso só apareceu ao escrever os dois no mesmo
> documento.

Consolidar não é copiar achados para um lugar comum. É a etapa em que se descobre o que os
achados significam juntos — e vale programá-la, não deixá-la para quando sobrar tempo.
