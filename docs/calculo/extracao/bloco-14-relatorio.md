# Bloco 14 — relatório

**Fase 4: confronto normativo.** Esta fase não consolida — **audita**. Cada ponto marcado nos
blocos de extração recebeu um veredito contra a norma vigente em **setembro de 2026**.

Produto em `confronto-normativo/00-inventario.md`, `01-vereditos.md`, `02-efeito-extracao.md`
e `03-suspeitas-base.md`.

---

## 1. Entregas

| Tarefa | Estado |
|---|---|
| 1 — inventário das marcações | **Feito** — 45 marcas, contra 28 anunciadas |
| 2 — veredito, um a um | **Feito** — **50 vereditos**, zero `SEM FONTE` |
| 3 — o que o confronto revelou sobre a base | **Feito** — **19 suspeitas** |
| 4 — efeito sobre o já extraído | **Feito** — 63 arquivos, cortes agrupados |
| Releitura adversarial do resultado | **Feita** — achou **9 pontos sem veredito** |

---

## 2. Tarefa 1 — o inventário achou um buraco de 17 marcas

| | Marcas |
|---|---|
| Anunciado nos relatórios | **28** |
| Encontrado na varredura | **45** |
| **Nunca contadas** | **17** |

**Nenhum documento jamais declarou um total.** Existem três contagens parciais — 16 nos
blocos 3 e 4, 12 no bloco 7 — corretas quando escritas e **nunca somadas**. As outras 17
entraram em formatos que nenhuma contagem varreu: `status_norma` em JSON de cadeia (5), campo
`situacao` do índice de jurisprudência (6), e marcações em prosa nos blocos 11 e 13 (6).

**Mesmo mecanismo que o mapa de cobertura pegou na extração:** ninguém deixou de marcar —
ninguém somou.

### 2.1 Colisão de identificadores, com dano já ocorrido

`F1`–`F9` no bloco 03 e `F1`–`F7` no bloco 04 são **pontos diferentes com os mesmos rótulos**.
O dano é verificável: o bloco 04 escreve *"mesma raiz do F1 do bloco 3"* e *"mesma raiz do F3
do bloco 3"* — remissões que, lidas isoladamente, apontam para horas *in itinere*.

E `F6` ilustra o risco: no bloco 03 são **gorjetas**, da **Lei 13.419/2017**; no bloco 04 é o
**art. 384 da CLT**, revogado pela **13.467/2017**. Normas diferentes, anos diferentes.

Renumerados para `B03-F*` e `B04-F*` **no inventário**. Corrigir os arquivos de origem é do
bloco 15.

---

## 3. Tarefa 2 — o resultado, e o que ele diz sobre arquitetura

| Veredito | Nº |
|---|---|
| `BIFURCADO` | **32** |
| `VIGENTE` | 9 |
| `SUPERADO` | 8 |
| `INAPLICÁVEL` | 1 |
| `SEM FONTE` | **0** |
| **total** | **50** |

*(50 vereditos para 45 marcas: alguns pontos do inventário se desdobraram — a Súmula 437, por
exemplo, rendeu veredito item a item.)*

### 3.1 Dois terços são BIFURCADO, e não é acaso

**Nem a Reforma, nem a ADC 58, nem a Resolução 225/2025 do TST revogaram com efeito
*ex nunc*. Todas cortaram no tempo.**

> **Consequência de arquitetura:** o motor não pode ter *uma* tabela de regras vigentes. Tem de
> ter **cadeia temporal por ponto**, como já tem para índices. Um `SUPERADO` mal lido apaga o
> período anterior ao corte — e a maioria das contas do produto atravessa o corte.

### 3.2 O achado que reorganiza a fase

**TST, Resolução 225/2025** (Pleno, 30/06/2025, DEJT 4253) — **li o texto integral**. Cancelou
27 súmulas, 8 OJs e 1 precedente normativo. Entre elas **90, 228, 423 e 437**.

**Mas o decisivo é *como* cancelou.** Cada inciso declara perda de eficácia **a partir de data
pretérita** — `a partir de` ocorre **27 vezes** no ato:

| Verbete | Texto literal |
|---|---|
| **90** | "cancelada por perda de eficácia **a partir de 11/11/2017**, pela Lei 13.467/2017" |
| **228** | "considerando a decisão da **Rcl 6266**, a partir da publicação em **18/04/2018**" |
| **423** | "considerando a decisão do ARE 1.121.633, a partir da publicação da ata em **14/06/2022**" |
| **437** | "**a partir de 11/11/2017**, pela Lei 13.467/2017" |

**O TST não revogou — declarou que os verbetes já haviam perdido eficácia no passado.** Isso é
estrutura de **cadeia temporal**, não de supersessão. Quem ler "cancelada" e apagar o verbete
erra todo o período anterior ao corte.

### 3.3 O que decide o eixo de 17 pontos

**TST, Tema 23** (IncJulgRREmbRep-528-80.2018.5.14.0004, Pleno, 25/11/2024, 15×10, transitado
em julgado):

> "A Lei nº 13.467/2017 possui aplicação imediata aos contratos de trabalho em curso, passando
> a regular os direitos decorrentes de lei cujos fatos geradores tenham se efetivado a partir
> de sua vigência."

**Modulação pedida e negada por unanimidade** nos embargos (20/05/2025). O eixo é a
**competência do fato gerador** — não a admissão, não o ajuizamento.

### 3.4 A subjanela que quase todos esquecem

**MP 808/2017, vigente de 14/11/2017 a 22/04/2018.** Nela, "abonos" **não** constava da
exclusão do art. 457, § 2º; gratificação de função integrava o § 1º; prêmios eram os
concedidos **até duas vezes ao ano**; a 12×36 exigia norma coletiva.

**Afeta cinco pontos.** É a variante mais fácil de perder: uma janela de cinco meses **dentro**
do período pós-Reforma, com texto diferente dos dois lados.

---

## 4. A releitura adversarial achou nove pontos sem veredito

O enunciado exigiu *"um segundo passe procurando ponto marcado sem veredito"*. Ele achou
**nove**: `JR-01`, `JR-05`, `AM-01`, `AM-03` e os cinco `CH-*`.

**E um deles rendeu achado positivo.** A **Súmula 124 do TST** — divisor do bancário, que
sustenta o preset `pr.sumula124-divisor-bancario` — **não está na lista de canceladas da
Res. 225/2025**. Conferido por script contra os 27 incisos. **Sobreviveu ao expurgo**, e
permanece na redação da Res. 219/2017.

Os cinco `CH-*` receberam `BIFURCADO`, não `SUPERADO`: o `status_norma: superado` gravado nos
JSON **está certo quanto ao futuro e incompleto quanto ao passado**. O segmento continua sendo
a regra das competências que cobre — é a razão de a cadeia histórica existir.

---

## 5. Tarefa 4 — os cortes se agrupam em poucas datas

**63 arquivos** com conteúdo afetado. Mas o número que importa é outro:

| Data de corte | Pontos |
|---|---|
| **2017-11-11** | **17** |
| 2018-04-18 · 2018-09-01 · 2018-11-23 · 2020-03-01 · 2020-11-06 · 2020-12-18 · 2021-03-15 … | 1 cada |

**Não são 40 cortes distintos — são poucas datas, cada uma atingindo muitos pontos.**

Isso só apareceu depois de normalizar: **o mesmo corte vinha grafado de três formas** nas três
auditorias (`11/11/2017`, `2017-11-11`, e prosa com ressalva). O agrupamento estava escondido
pelo formato.

**Implementar por data, não por ponto** reduz o trabalho do bloco 15 a uma fração — e impede
que dois pontos da mesma data recebam fronteiras diferentes.

---

## 6. Tarefa 3 — 19 suspeitas, das quais três pesam

**A maioria não é erro de mérito — é desatualização de rastro.** A base acertou o direito e não
registrou o ato formal posterior.

**Três são de outra ordem:**

**A que muda arquitetura.** `02-base-normativa-verbas.md` § 1 trata o direito intertemporal
como divergência aberta — *"duas correntes, não resolver, expor como preset"* — e é a base do
`pr.intertemporal` **sem default**. **O Tema 23 resolveu com força vinculante**, e a Corrente B
é a posição dos dez vencidos. **Não resolvi a divergência: registrei que ela deixou de ser
simétrica.** A decisão é do bloco 15.

**As duas que são erro de fato e mudam resultado:**

- **o art. 58, § 2º, da CLT não foi revogado.** Teve redação alterada; revogado foi o **§ 3º**.
  A base cita o dispositivo errado como fonte de um parâmetro negociável. Verificado por mim;
- **a EC 113/2021 alcança toda Fazenda Pública**, não só a federal — *"independentemente de sua
  natureza"*. A restrição a "federal" é da **EC 136/2025**. **Erro meu**, em `bloco-13c` § 7.

### 6.1 A única correção que fiz, e por quê

O enunciado proíbe corrigir a base. **Corrigi apenas `bloco-13c` § 7** — documento **meu de
extração**, não a base, e cujo erro era meu: retroprojetei em quatro anos a restrição da
EC 136/2025, lendo *"a nova redação do art. 3º"* do enunciado do bloco 13 como se fosse a
redação original. **O enunciado estava certo; eu li errado.**

Consequência material: para Fazenda estadual ou municipal, **entre dez/2021 e set/2025 vale a
Selic única da EC 113/2021**. A afirmação errada a teria excluído.

---

## 7. Sobre a numeração das fases

`01-plano-extracao.md` chama **esta** etapa de "Fase 4" e a consolidação de "Fase 3". **A ordem
está invertida no documento** — o confronto vem antes, e é o que impede a consolidação de fundir
conteúdo invertido.

**Registrado, não corrigido**, conforme o enunciado. Correção no bloco 15.

---

## 8. Limites declarados

**Planalto, DOU, Receita Federal e `portal.stf.jus.br` recusaram acesso automatizado durante
toda a sessão** — socket fechado ou HTTP 403. Consequências honestas:

- **a modulação da ADC 58 continua sem transcrição literal**;
- o de-para RIR/99 → RIR/2018 não foi feito;
- quatro pontos do capítulo 9 repousam em fonte secundária, **uma delas com erro de data
  flagrante, documentado**;
- **nenhum inteiro teor** de Rcl 6.275, Rcl 6.266 ou Rcl 53.157 foi lido.

**Os canais que funcionaram**, e que valem para as próximas fases: **`portal.trt3.jus.br`** —
que hospeda acórdãos do STF —, **`stj.jus.br`** e **`juslaboris.tst.jus.br`**.

### 8.1 Um alerta operacional que vale registrar

**As fichas de tema do TST não servem como fonte.**

- a ficha do **Tema 9** traz a tese firmada e **omite a modulação** — li o PDF. Quem consultar
  só ela conclui `SUPERADO` onde o correto é `BIFURCADO`;
- a ficha do **Tema 23** está com *"Tese Firmada"* **em branco** e situação *"Afetado"* —
  cache anterior ao julgamento de 25/11/2024.

Os **acórdãos publicados** supriram, com texto primário completo.

---

## 9. O que a Fase 5 recebe

**Decidir, com evidência na mesa:**

1. **`pr.intertemporal` continua sem default?** O Tema 23 é vinculante. Se ganhar default, os
   17 pontos de 11/11/2017 destravam — e `R20-EXCECAO` cai de cinco para quatro casos;
2. **corrigir a colisão `F*`** nos arquivos de origem;
3. **os dois erros de fato** — art. 58 § 2º e, já corrigido, a EC 113;
4. **registrar os cancelamentos da Res. 225/2025** na base, **com as datas de perda de
   eficácia**, não como simples revogação;
5. **implementar os cortes por data**, não por ponto.

**Não decidir:** as variantes registradas em `01-vereditos.md` § E. São correntes com
fundamento dos dois lados, e resolvê-las é do juízo, não do motor.

---

## 10. Lição de método

O bloco 13 fechou com *"a negativa é a afirmação mais perigosa que um extrator faz"*. Esta fase
mostra a forma que ela toma quando o objeto é jurisprudência:

> **"Cancelada" é uma negativa — e quase nunca significa "nunca valeu".**

A Resolução 225/2025 cancelou 36 enunciados e **declarou, 27 vezes, a data em que cada um
deixou de valer**. Um confronto que registrasse apenas "Súmula 437: cancelada" estaria correto
e produziria cálculo errado para todo fato anterior a 11/11/2017.

**O veredito `BIFURCADO` existe para isso**, e foi o resultado de dois terços dos pontos. A
tentação de simplificar para `SUPERADO` é forte porque a fonte oficial usa a palavra
"cancelada" — **e é precisamente aí que a fonte oficial engana.**
