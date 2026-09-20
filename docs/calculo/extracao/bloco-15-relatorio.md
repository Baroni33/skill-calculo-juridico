# Bloco 15 — Fase 4: consolidação em espinha e detalhe

**Estado: fechado.** Treze blocos de extração e os 50 vereditos do confronto normativo viraram
**onze arquivos** em [`docs/calculo/consolidado/`](../consolidado/). Nenhuma skill escrita — a
skill é o bloco 16.

**A consolidação não extraiu nada.** Tudo o que está lá já estava no corpus extraído. O que
mudou é o endereço: passou a haver **um lugar por assunto**, com a espinha do que o motor
precisa e o detalhe de onde está a evidência.

---

## 1. O que foi produzido

| Arquivo | Linhas | Papel |
|---|---|---|
| `00-calendario-de-cortes.md` | 296 | **Chave primária.** Um par `(data, eixo)` por corte |
| `00-validacao-casos.md` | 177 | Os 33 casos difíceis contra a espinha — critério de aceite |
| `01-dominio-e-invariantes.md` | 316 | R1–R23, as três camadas, `dominio_condicoes` |
| `02-atualizacao.md` + `-detalhe.md` | 491 + 196 | Cadeias período → indexador, as duas jurisdições |
| `03-verbas.md` | 501 | Verbas trabalhistas, base de cálculo, a subjanela da MP 808 |
| `04-descontos.md` + `-detalhe.md` | 499 + 137 | INSS, IRRF, RRA, rateio sob pagamento parcial |
| `05-imputacao.md` | 283 | Amortização, rateio, *descarregar*, item "i" da ADC 58 |
| `06-encargos.md` | 442 | Honorários, custas, sindical, precatórios |
| `07-leitura-do-corpus.md` | 203 | Os dez padrões de como este manual se lê |

**Limite de 500 linhas na espinha.** Dois arquivos o estouraram e ganharam companheiro de
detalhe. `03-verbas.md` fechou em **501** — uma linha acima, registrada e não maquiada.

---

## 2. O achado que corrigiu a instrução do próprio bloco

O enunciado mandava implementar **por data**. O bloco 14 dizia o mesmo: *"não são 40 cortes
distintos — são poucas datas, cada uma atingindo muitos pontos."*

**Está incompleto, e a diferença é material.**

**Dezoito pontos compartilham 11/11/2017. E cortam por três eixos diferentes:**

| Eixo | Pontos |
|---|---|
| **competência do fato gerador** | dezesseis |
| **data de propositura da ação** | `C8-01` — honorários sucumbenciais |
| **modalidade do acordo** — não é eixo temporal | `F7-06` — acordo extrajudicial |

Dois processos ajuizados no mesmo dia, com parcelas da mesma competência, **recebem respostas
diferentes**. Um motor que aplique "11/11/2017" uniformemente erra os honorários de toda ação
proposta antes da data com parcelas posteriores.

> **A chave não é a data. É o par `(data, eixo)`.**

---

## 3. A regra que governou a aplicação dos vereditos

**32 dos 50 vereditos são `BIFURCADO`** — e a razão é estrutural, não estatística:

> A **Res. 225/2025 do TST** cancelou 36 enunciados e **declarou, em cada inciso, a data em que
> o verbete perdeu eficácia**. `a partir de` ocorre **27 vezes** no ato.
>
> **O TST não revogou: declarou que os verbetes já haviam perdido eficácia no passado.**

Nem a Reforma, nem a ADC 58, nem a Res. 225/2025 revogaram com efeito *ex nunc*. **Todas
cortaram no tempo.** Daí a regra de aplicação:

**AS DUAS versões entram, com o corte e o eixo. Nunca a nova no lugar da antiga.** Competência
anterior ao corte usa a antiga.

**Consequência de arquitetura:** o motor não pode ter *uma* tabela de regras vigentes. Precisa
de **cadeia temporal por ponto** — como já tem para índices.

---

## 4. Tarefa 0 — as oito correções

| | O que era | O que ficou |
|---|---|---|
| **a** | `01-plano-extracao.md` chamava a consolidação de Fase 3 e o confronto de Fase 4 | **Invertido:** confronto = **Fase 3**, consolidação = **Fase 4**. As marcas `marcar para Fase 4` nos blocos de extração ficam como estão — são registro histórico, e reescrevê-las apagaria a ordem real do trabalho. Ressalva em `confronto-normativo/README.md` |
| **b** | *"A Rcl 6.275 foi cassada"* | Sujeito e objeto invertidos — **a Rcl cassou**, não foi cassada |
| **c** | § 1 sem o Tema 23 | Reescrito com o **Tema 23 do TST** como tese vinculante |
| **d** | art. 58 *"§§ 2º e 3º alterados"* | **§ 2º alterado, § 3º revogado** |
| **e** | `pr.intertemporal` **sem default** | Ganhou default `tempus-regit-actum`, fundado no Tema 23 |
| **f** | C17 pressupunha a ausência de default | Reescrito — passou a perguntar se a espinha registra a regra fixada |
| **g** | EC 113/2021 *"apenas federal"* | **Falso.** O texto diz *"independentemente de sua natureza"* |
| **h** | `F1`–`F9` × `F1`–`F7` colidindo | Renumerados `B03-F*` / `B04-F*` |

### 4.1 O default do Tema 23 quebrou treze testes — e todos estavam certos

**Tema 23 do TST** — IRR, Pleno, **25/11/2024**, placar **15 × 10**, transitado, **modulação
negada por unanimidade**: a Reforma *"regula os direitos decorrentes de lei cujos fatos
geradores tenham se efetivado a partir de sua vigência"*. Eixo: **competência do fato gerador**.

Com o default, **R21 passou a rejeitar a escolha da ultratividade sem justificativa** — que era
exatamente o comportamento pedido. Três testes foram reescritos para afirmar a regra nova em
vez de a antiga:

- `test_escolha_intertemporal_nao_exige_justificativa` → **`..._agora_EXIGE_justificativa`**;
- `test_sem_escolha_nao_calcula` → **`..._resolve_pelo_default_e_marca_a_conta`**, mais um teste
  novo confirmando que **o mecanismo de bloqueio continua existindo**;
- `test_R22_regime_bloqueado_bloqueia_o_parametro` → **`..._mas_por_outra_razão`**: o parâmetro
  segue bloqueado, agora **por mérito** — a verba não existe — e não por modelagem.

**`R20-EXCEÇÃO` caiu de cinco casos para quatro.** Confirmado por `valida_regimes.py`.

**214 testes OK** (28 + 71 + 86 + 29).

---

## 5. Tarefa 4 — os 33 casos difíceis

**O critério de aceite.** Resultado em [`00-validacao-casos.md`](../consolidado/00-validacao-casos.md):

| | Casos |
|---|---|
| **Respondido** | **31** |
| **Parcial** | **2** — `C31` e `C33`, **ponteiro ausente**, não perda de informação |
| **Não respondido** | **0** |

**Sem esta tarefa, seis casos teriam passado como respondidos por aproximação.** A varredura
pegou quatro lacunas reais e as fechou: C1 (R1 implicava em vez de afirmar), C3 (faltava a
instrução defeituosa do manual), C11 (tabela de arredondamento aproximada) e C23/C25/C26 (a
camada de parâmetros estava resumida demais).

**Duas pendências atravessam casos e não podem ser fechadas por consolidação nenhuma:** a base
das custas de execução, que o item 8.2.1 define **só por exclusão**, e a classificação da
devedora como Fazenda Pública, em que o manual se autocontradiz. **Registrar a pendência é a
resposta certa.** Uma espinha que as "resolvesse" estaria inventando.

---

## 6. Validação adversarial — o que ela pegou

**Segundo passe**, procurando: regra que existia em dois blocos e sumiu na fusão; bifurcação
aplicada como substituição; veredito não refletido na espinha; afirmação sem respaldo.

### 6.1 Três achados graves

**G1 — uma cadeia inteira se perdeu.** Os **juros compensatórios da desapropriação** são
cadeia autônoma, além da correção e dos juros de mora. A fusão manteve só a linha de correção
monetária. Sumiram: o corte de **ago./2017** (os compensatórios passam ao percentual dos TDAs
de oferta inicial — regra que **nenhuma tabela mostra**, vive só no item 4.5.4), os dois termos
iniciais da Súmula 69 do STJ, e a contradição de um mês entre as cadeias gêmeas (**N-6**:
o texto diz "até dez. 2021", a tabela encerra em nov./2021).

**Agravante:** o caso **C21** estava marcado *"Respondido"* apontando para um arquivo que **não
continha a afirmação**. Recuperado em `02-atualizacao-detalhe.md` § 5.4.

**G2 — o capítulo 10 tem duas molduras, e a espinha registrou uma.** O item 10.3.2 (pp.
239–241) **não** repete a moldura de 10.3.1: vai de A a O/P e **tem letra I**. O rateio ali é a
letra **G**, não F. A espinha dizia *"não existe letra I"* sobre o capítulo inteiro — e depois,
no mesmo arquivo, falava da *"alternativa da letra I"*. **Contradição interna.** A afirmação
vale **só para 10.3.1**. Recuperada a tabela de correspondência em `05-imputacao.md` § 2.2.

**G3 — a renumeração da Tarefa 0(h) reintroduziu o dano que curava.** A substituição foi cega e
reescreveu **remissões cruzadas**: *"mesma raiz do F1 **do bloco 3**"* virou `B04-F1`, que é
horas *in itinere* — o alvo errado. **Pior que antes:** o rótulo parece bem-formado, então o
leitor não desconfia. Duas ocorrências corrigidas para `B03-F1` e `B03-F3`.

### 6.2 Onze achados médios

Os que mudam número ou leitura: `F7-05` estava fora da tabela dos pontos de 11/11/2017 (daí
"dezessete" onde são **dezoito**); `F7-06` estava listado como afetado pela MP 808 **sem
respaldo no veredito**; o calendário afirmava cobrir os 32 cortes e **não cobria** `CH-01`–`CH-05`
nem `AM-03`, que vivem nas cadeias de `02-atualizacao.md`; faltava a data de **dez/2021** da EC
113/2021; o placar de casos somava **dois não-casos** aos parciais; e três trechos de
`presets-regime.md` ainda diziam que `pr.intertemporal` não tinha default, um deles afirmando
que *"todo o corte de 11/11/2017 está parado nesse único ponto"*.

Mais: `A9`, `A10` e o ID de `A4` não tinham reflexo na espinha; a **Súmula 454 do TST** funda
`R-07-19` e ficou só na observação metodológica; e uma negativa de `06-encargos.md` estava **sem
escopo declarado** — corrigida para dizer *"escopo não registrado na extração"*, que é honesto,
em vez de inventar "471 páginas".

**Um achado não se confirmou e não foi editado:** `P13B-02` × `D13B-02` não é inconsistência —
são famílias distintas (pendência × divergência) sobre o mesmo assunto, e a origem usa as duas
deliberadamente.

### 6.3 O que a auditoria confirmou íntegro

Isto também é resultado, e é a maior parte.

- **Nenhum dos 50 vereditos está ausente** da espinha. Os dez de menor frequência foram
  conferidos um a um e têm **tratamento substantivo**, não só ponteiro;
- **Nenhuma bifurcação virou substituição.** Os 32 têm as duas versões explícitas, quase sempre
  em tabela de duas colunas datadas. **Zero ocorrências** do padrão de alarme — "passou a ser X"
  sem dizer o que era antes, tabela de uma coluna, "superado" onde o veredito é `BIFURCADO`;
- **Res. 225/2025 tratada como cadeia temporal** em três arquivos independentes e convergentes;
- **EC 113/2021:** a espinha **não** repete a falsidade — refuta-a explicitamente e tira a
  consequência material (Fazenda estadual e municipal sob Selic única entre dez/2021 e set/2025);
- **Regras promovidas de exemplo** sobreviveram: mês comercial com contagem inclusiva, precisão
  plena encadeada, base da multa do art. 467, o NMP em três ramos;
- **Exceções nomeadas** preservadas: `R4-EXCEÇÃO` gravada **dentro** do invariante, a verba
  exclusivamente convencional que *"não existe"* em vez de valer zero, o ramo Fazenda subsidiária
  **declarado e deliberadamente vazio**;
- **Escopo declarado** em 25 das 26 negativas verificadas, e **nada resolvido por inferência**.

---

## 7. O que continua aberto

**Não foi fechado, e não deveria ter sido:**

| Aberto | Natureza |
|---|---|
| **dois bloqueios aritméticos** — pp. 266 e 269 | deltas de **10,00 exatos** e **2.036,51**. Nenhum é arredondamento |
| **`pr.imputacao` sem default** | o critério proporcional é aplicado **101 vezes e fundamentado zero**; `art. 354` → **0 em 471 páginas**. Escolher seria o motor tomar posição jurídica |
| **modulação da ADC 58, item "i"** | origem secundária declarada; o STF recusou acesso automatizado em 100% das tentativas |
| **cadeia trabalhista anterior a 03/1991** | o cap. 7 delega à Tabela Única do CSJT. O tronco do CJF cobre o período, **mas o corpus não faz essa remissão** — usá-lo seria ponte inventada |
| **de-para RIR/99 → RIR/2018** | Planalto inacessível; toda remissão a "art. X do RIR/99" segue endereço quebrado |
| **classificação como Fazenda Pública** | dois testes incompatíveis no mesmo manual. **Não é matéria de cálculo** — é pergunta ao jurídico |
| **`D15-02` nos dois relatórios** | resolvida nas espinhas e nos detalhes; os relatórios foram alcançados nesta passagem |

---

## 8. Para o bloco 16

A skill se escreve **do `00-calendario-de-cortes.md` para fora**, não do domínio para dentro:
é o calendário que impõe a arquitetura de cadeia temporal por ponto.

**Dois ponteiros a fechar**, ambos de consolidação e nenhum de pesquisa: nomear as fixtures 2 e
4 e seus deltas esperados (C31), e reunir as dependências externas numa tabela única com "dado
→ papel → consequência da ausência" (C33).

> **Um veredito inventado é pior que uma pendência declarada.** Vale para a skill também.
