# Bloco 19 — classificação de índices e fechamento das cadeias

**Estado: fechado.** R3 ganhou a terceira classe, os 36 rótulos foram mapeados um a um, cinco das
oito cadeias de `P18-02` foram geradas, e o calendário de FGTS e poupança entrou como **eixo
próprio**, não como exceção em nota.

| | Antes | Depois |
|---|---|---|
| Cadeias | 15 | **20** |
| Segmentos | 126 | **156** |
| Testes | 267 | **311** |
| `valida_cadeias.py` | R1 **15** · R2 1 · R3 25 | **R1 21 · R2 1 · R3 62** |
| `valida_bloco_tabelas.py` | `15 ok, 0 erros` | **`15 ok, 0 erros`**, exit 0 |

**Distribuição de `tipo_indexador` nos 156 segmentos:** `percentual` 39 · `nao-indexador` 46 ·
**`indeterminado` 32** · `nominal` 31 · **`janela-deslocada` 8**.

---

## 1. Três classes — e um erro de categoria que caiu junto

A dicotomia nominal/percentual do item 4.1.2.4 **é insuficiente, e os dois índices mais usados
hoje ficam fora dela**. A classificação veio **verificada em fonte, fora do agente**:

| classe | defasagem | quem |
|---|---|---|
| `nominal` | reflete **M−1** | ORTN, OTN, BTN, Ufir |
| `percentual` | reflete **M** | INPC, INPC/IBGE, IGP-DI, IPC/IBGE, **Selic** |
| **`janela-deslocada`** | **metade de M−1, metade de M** | **IPCA-E/IBGE, IPCA-15/IBGE** |
| `indeterminado` | **sem regra de conversão declarada** | 15 rótulos |

**O IPCA-15 difere do IPCA no período de coleta** — do dia 16 do mês anterior ao 15 do mês de
referência. **E o IPCA-E mensal das tabelas judiciais é o IPCA-15.**

### `englobante` era um fato de R1 dentro do campo de R3

Os segmentos **já têm o campo `engloba`** — é o que R1 lê. Marcar a SELIC como `englobante` em
`tipo_indexador` **a deixava cega para R3**: nunca entrava em comparação de defasagem, embora
tenha defasagem.

> **`englobante` foi retirado do vocabulário.** O englobamento não se perdeu — **mudou de campo,
> para o que já existia**.

**Oito violações R3 novas saíram daí**, e são achado, não regressão: duas `Selic → IPCA-15/IBGE`
em set/2025, cinco `Selic → taxa-legal` indeterminadas, e uma `Ufir → IPCA-E/IBGE` que era
indeterminada e virou **confirmada**.

### A TR: `indeterminado` por RAZÃO, não por ausência de fonte

**São coisas diferentes, e se fecham de formas diferentes.** A TR é divulgada **para período
entre datas de aniversário** (17/02 a 17/03), **não para mês calendário**, **e é prefixada**.

> **Não se fecha esperando fonte.** A fonte chegou, e **diz que não cabe**. Campo próprio
> (`tipo_indexador_razao`), **mutuamente excludente** com `tipo_indexador_pendencia` — o schema
> rejeita o par.

**A `TRD` não herdou a razão da TR** — a fonte do BCB nomeia TBF, Redutor-R e TR, **não a TRD**.
E o bloco **desfez** a herança que o bloco 18 tinha feito (*"segue a TR"*).

---

## 2. O mapeamento — 36 rótulos, um a um

**Levantados do repositório, não da tabela.** **32 ficaram `indeterminado`**, por duas razões que
não se confundem:

| Razão | Quantos | Fecha quando |
|---|---|---|
| **sem fonte** | 12 rótulos | a fonte chegar — `P17-01`, `P18-01`, `P19-01`, `P19-02` |
| **fonte diz que não cabe** | 2 — TR e remuneração básica da poupança | **nunca, esperando fonte** |
| **segmento composto** | 2 — `P17-03` | quando o segmento for partido |

### As três deduções que não aconteceram

- **`BTNF`** — o item 4.1.2.4 nomeia o **BTN**. *"Herdar 'nominal' do BTN porque o nome é quase o
  mesmo é a dedução proibida"*, e ficou `indeterminado` (`P19-02`);
- **`taxa-legal`** — **não** foi promovida a `percentual` por analogia com a SELIC. R11 a registra
  como **derivada**, e a fonte externa não a alcança (`P19-01`);
- **o `IPC` nu** — `D8-C21` sustenta o **`IPC/IBGE`**, e o manual usa **dois** IPC.

### Três divergências entre a tabela externa e a fonte extraída

**`IGP-DI`** — a tabela externa não o nomeia; **o item 4.1.2.4 o nomeia literalmente**. **Prevalece
a fonte extraída**: fica `percentual`. Idem **`IPC/IBGE`**, por `D8-C21`.

**`IPCA`** — a tabela o classifica, mas **nenhum segmento tem o rótulo `IPCA` nu**. **Linha sem
destinatário** — e era a porta de entrada do derramamento por nome. **`IGP-M`, `TDA` e `JCM`
também não são rótulos de segmento algum.**

---

## 3. Cinco cadeias geradas, três recusadas

| id | item | segmentos |
|---|---|---|
| `cjf.desapropriacao-indireta.correcao-monetaria` | 4.6.1.1 | 11 |
| `cjf.divida-fiscal.juros-mora` | 2.3.2.2 | 8 |
| `cjf.fgts-divida-fiscal.correcao-monetaria` | 2.4.4.1 | 5 |
| `cjf.desapropriacao-direta.juros-compensatorios` | 4.5.3 | 3 |
| `cjf.desapropriacao-indireta.juros-compensatorios` | 4.6.3 | 3 |

### As cinco decisões, cada uma gravada no próprio JSON

1. **Duas cadeias, não uma com dois escopos.** A identidade 4.6.1.1 × 4.5.1.1 **é afirmação da
   fonte**, não inferência. Mas o que **muda** — termo inicial (`D8-C10`) e juros — **está fora da
   linha do tempo**, e `condicao` é campo de *segmento*, não de cadeia. **A duplicação foi paga:**
   os 11 segmentos da indireta são **derivados em tempo de geração** da direta;
2. **O corte de ago./2017 NÃO é tabulável.** A taxa é *"o percentual fixado para os TDAs
   depositados como oferta inicial"* — **valor do caso**. Gravá-la como segmento sobrescreveria a
   linha que a tabela declara;
3. **`N-6`: grava-se a TABELA** (fim em `2021-11`), com o texto *"Até dez. 2021"* ao lado.
   **`P8-09` segue aberta.** E as 4 linhas viraram **3 segmentos** porque a extração não transcreve
   onde a primeira das duas linhas de dez/2021 termina — *"palpite óbvio é palpite"*;
4. **`N-10` transcrito, não corrigido.** A remissão errada ficou no `regra_literal`; o destino
   correto num campo próprio. **Corrigir seria harmonizar**;
5. **`base_incidencia`: campo novo, e o schema o acomoda** — `Segmento.de_dict` lê lista fechada,
   então R1/R2/R3 seguem exatas. **Deixou de ser o bloqueio que o bloco 18 supunha.**

### R1 subiu de 15 para 21, e as seis são do manual

Duas herdadas do tronco na indireta; **três cortes intramensais** (10/6÷11/6/1997 nas duas de
compensatórios; 2/1÷3/1/1992 na dívida fiscal); e uma que é o **`D8-C8`** de maio/2000 — *"a
sobreposição que o bloco 8 dizia que a checagem não pega porque a cadeia não existe"*.

**R2 seguiu em 1.** **R3 foi de 51 para 62.**

### As três que não foram geradas, e a razão é uma só

**4.5.2**, **4.6.2** (juros de mora da desapropriação) e **2.4.2.2.2** (juros previdenciários).

> **A tabela das três nunca foi extraída linha a linha.** De 4.5.2/4.6.2 o corpus tem quatro
> marcas soltas; de 2.4.2.2.2, **uma frase**. **Gerá-las exigiria reconstruir a ESTRUTURA — pior
> do que inventar um valor.**

**`P18-02` encolhe de oito para três.** E **4.7.1 não entra**: registrada a **delegação ao TST**,
não a ausência.

---

## 4. O calendário de FGTS e poupança é outro eixo

**Confirmado contra a fonte:** 4.8.3 (`pagina_pdf` 83) e 4.9.3 (86) são a mesma tabela palavra
por palavra — **0,5% até dez/2002 → Selic → taxa legal em set/2024**, fundada só na Lei
14.905/2024, **sem o ARE 1.557.312**, **sem dez/2021 e sem set/2025**.

**Achado que o bloco 18 não tinha: a CORREÇÃO dessas duas cadeias é TR de maio/1993 a jun/2026,
sem corte nenhum.** O calendário próprio vale para **os dois componentes**.

**Registrado como `§ 2-A` de `00-calendario-de-cortes.md`, seção própria e não par.** A razão é
estrutural: **o desenho `(data, eixo)` é um índice positivo, e o núcleo do achado são
ausências** — *"não há corte em dez/2021"* **não tem par que se escreva**.

### O eixo de set/2024 difere — e é o padrão de 11/11/2017

| | Eixo |
|---|---|
| **FGTS e poupança** | `competência da parcela` **pura** — move todo mundo |
| **Condenatórias gerais** | `competência ⊕ natureza do devedor` — **o ramo Fazenda não muda de regime** |

**Mesma data, eixos diferentes.** É o achado estrutural do bloco 15, reencontrado.

### `A16`, e por que o delta não é mensurável

**A série mensal de Selic e taxa legal de set/2024 a ago/2025 é dado (B) fora do repositório.** A
única tabela de taxa legal do manual é a previdenciária de set/2025–jun/2026 — **período e
deflator errados**. **Dizer um número seria inventá-lo.**

**Assinatura estrutural em cinco itens**, toda derivável do que está gravado: janela de
divergência de **exatamente 12 meses**; **sinal determinado** — `taxa legal ≤ Selic`, logo o erro
**superestima**; **consolidação fantasma** de `0,4412%`; qualquer índice ≠ TR na correção
pós-maio/1993; e **citação do ARE 1.557.312**.

### A NOTA 3 de 4.9.1.1 não foi gerada, e não deve

As duas pontas são **o bloqueio e a data da conversão** — **eventos da conta, não competências**.
É regime **alternativo** que convive com a tabela nos mesmos meses: **gravar como segmento
violaria R2**. Vive nas `notas` do JSON, com `pagina_pdf`. **Tratada, não perdida.**

---

## 5. A espinha é mais fina que o dado — treze achados

`10-literais-na-extracao.md`. **Escopo declarado:** 146 literais dos JSON contra os 13 arquivos
do consolidado, filtro mecânico de janela de 8 palavras (115 passaram) mais curadoria. **Cinco
falsos positivos descartados por nome.**

**Dois `BLOQUEIA`, dez `ENFRAQUECE`, um `COSMÉTICO`. Só os dois `BLOQUEIA` foram corrigidos** —
*"nada foi promovido para justificar trabalho"*.

**L1 é o mais grave, e é erro de conteúdo:** os juros de **servidores e empregados públicos**
antes de jul/2009 são **1% até jul/2001 e 0,5% a.m. de ago/2001 a jun/2009** — e **a espinha dava
Selic**. A palavra *"servidor"* **não ocorria nos 13 arquivos do consolidado**. Corrigido no
§ 5.2-A do detalhe, com os dois literais, item e `pagina_pdf`.

---

## 6. Validação adversarial — e o defeito mais irônico do bloco

**Três graves, e a primeira é de método:**

**G1 — o bloco publicou números de meio-caminho como resultado final.** O resultado foi escrito
depois da Tarefa 2 e **nunca reescrito depois da Tarefa 3**, que acrescentou cinco cadeias.
Quatro arquivos afirmavam `15 cadeias | R1: 15 | R3: 51` e *"R1 e R2 não se moveram"* — **R1 tinha
ido a 21**. Corrigido **preservando as duas etapas**, porque *"R3 foi de 46 para 51 na Tarefa 2 e
de 51 para 62 na Tarefa 3"* é o que permite auditar de novo.

**G2 — `indices-judiciais/SKILL.md` estourou o limite**, em 517. Cortada para **499**, com a § 5
movida para `references/divergencias-e-erros.md`, **com ponteiro**.

**G3 — `englobante` sobreviveu na prosa de um JSON**, e o catálogo **declarava ter corrigido**.
A afirmação era **falsa como escrita**.

### O mais irônico

**Três varreduras declararam escopo de *"os 36 JSON de `tabelas-normativas/`"*. São 32 arquivos.**
36 é a contagem de **rótulos**, não de arquivos — **a unidade foi trocada**.

> **Num projeto cuja regra é *"afirmação de ausência exige escopo declarado"*, escopo declarado
> errado é pior que escopo não declarado — porque parece auditado.**

**As conclusões das três estavam certas.** O universo é que não existiu nem antes (27) nem depois
(32).

### Mais três, que valem pelo padrão

**M3 — a indireta importou três blocos da direta sem declarar**, inclusive `pagina_pdf 69`, que é
da direta. **O mesmo arquivo declara meticulosamente o `N-10`** e registra que as duas divergem em
datas — e ainda assim herdou em silêncio. **Ressalva acrescentada.**

**M4 — o critério prometia `fundamento: null` com razão onde a fonte não trouxesse; 20 segmentos
ficaram sem o campo e sem a razão.** Preenchidos os **13 novos deste bloco**; os **8 da indireta
são pré-existentes do bloco 8 e ficaram declarados como tais** — consertá-los faria o derivado
divergir da origem. **No repositório inteiro são 77 segmentos sem `fundamento`, em 11 cadeias.**

**M6 — uma contagem envelhecida replicada dezenas de vezes.** O texto *"21 segmentos, em 6
cadeias"* é **copiado literalmente para dentro de cada segmento** — são **37 em 10**. A correção
**tirou a contagem de dentro do texto replicado**: no segmento fica só o que não envelhece, e o
número vai para o catálogo, **num lugar só**. **Com teste que recomputa do repositório e falha se
a contagem voltar para dentro do texto** — é o 311º.

### O que a auditoria confirmou íntegro

- **Nenhum índice classificado por dedução ou herança.** Os 36 rótulos das 20 cadeias conferem
  **100%** com o catálogo, zero divergência entre segmento e catálogo;
- **as cinco decisões da Tarefa 3 se sustentam**, com a ressalva M3 — inclusive a negativa do
  FGTS fiscal sobre maio/2000, que é **verificável e verdadeira**, não inferência;
- **o calendário de § 2-A está correto e não há troca em lugar nenhum** — varredura de `2024-09`
  em `skills/` e `consolidado/` não achou contaminação nos dois sentidos;
- **`A16`: a não-mensurabilidade procede** — a via mais óbvia foi testada e não fecha;
- **nenhuma exceção foi acrescentada ao ledger de ponteiros** para acomodar ponteiro morto.

---

## 7. O que continua aberto

| Aberto | Natureza |
|---|---|
| **`P18-02` — três cadeias** | 4.5.2, 4.6.2, 2.4.2.2.2. **A tabela nunca foi extraída linha a linha.** Não é de modelagem |
| **32 segmentos `indeterminado`** | 12 rótulos **sem fonte** (`P17-01`, `P18-01`, `P19-01`, `P19-02`) e 2 **com razão** (TR, poupança) |
| **`P17-03` — dois segmentos compostos** | `Ufir → Selic` e `UPC → índices básicos`. **Partir o segmento**, não classificá-lo |
| **duas taxas `null`** nos compensatórios | **não estão na fonte extraída.** O buraco está declarado num arquivo que o validador lê |
| **`D8-C13` / `N-5`** | os expurgos do FGTS não dizem se substituem ou acrescem |
| **onze `ENFRAQUECE`** da Tarefa 5 | insumo para decidir se a espinha precisa de outra passada. **Não promovidos** |
| **`00-base-normativa.md` § 7** | divergência declarada. **Correção fora do agente** |

> **`indeterminado` continua sendo a resposta correta onde falta fonte, e continua bloqueando.**
> Foi o que impediu `BTNF` de herdar do `BTN`, a taxa legal de herdar da SELIC, e o `IPC` nu de
> herdar do irmão.
