# Bloco 18 — fechar as lacunas de consolidação

**Estado: fechado.** FGTS e poupança consolidados e com `reference`, descoberta por conteúdo com
manifesto, ponteiros com teste que impede o retorno.

| | Antes | Depois |
|---|---|---|
| Cadeias | 11 | **15** |
| Testes | 253 | **267** |
| `valida_cadeias.py` | R1 15 · R2 1 · R3 25 | **R1 15 · R2 1** · R3 **46** |
| `valida_bloco_tabelas.py` | `15 ok, 0 erros` | **`15 ok, 0 erros`**, exit 0 |
| `references/` | 8 | **10** |

---

## 1. A varredura — não eram duas, são dez

**O enunciado mandava varrer antes de concluir.** A matriz `item × JSON × consolidado` cobre os
capítulos 2 e 4 e vive em [`02-atualizacao-detalhe.md` § 5.0](../consolidado/02-atualizacao-detalhe.md).

**Escopo declarado:** as 93 páginas do PDF para o sumário numerado; releitura **integral** das
`pagina_pdf` **22–39** e **41–87**; cruzamento com `ls tabelas-normativas/*.json` e busca em
`consolidado/` por `JAM`, `poupan`, `UPC`, `LBC`, `LFT`, `FGTS`, `compensatóri`, `desapropria`.

**Oito cadeias tabuladas sem JSON, além das duas do enunciado** — `P18-02`, registradas e **não
geradas**:

| Item | O que é |
|---|---|
| **4.5.2** · **4.5.3** | juros de mora e **compensatórios** da desapropriação **direta** |
| **4.6.1.1** · **4.6.2** · **4.6.3** | **a desapropriação indireta inteira** — e 4.6.1.1 é **idêntica** a 4.5.1.1 |
| **2.3.2.2** · **2.4.2.2.2** | juros da dívida fiscal e da contribuição previdenciária — exigem `base_incidencia` (`D8-C5`) |
| **2.4.4.1** | **FGTS fiscal, critério `JCM`** — **outra cadeia**, outro sujeito, outra sigla |

> **O FGTS aparece duas vezes no manual, com critérios diferentes.** `JAM` no 4.8 e `JCM` no
> 2.4.4.1, e o corte da ORTN difere nos três lugares (set/1983 × fev/1986 × jun/1983). **O corte
> de maio/2000 é do 2.4.4.1 e não alcança o 4.8.**

### E uma que parecia lacuna e não é

**4.7.1 — correção das ações trabalhistas.** O manual **não tem tabela**: traz lista de leis e a
NOTA 2 **delega** — *"utilizar a tabela de coeficientes trabalhistas expedida pelo TST"*.

> **Mesmo desenho do `P9-02`.** A cadeia vive numa **série**, não numa regra. **Afirmá-la ausente
> seria afirmar ausência de algo que a fonte nunca prometeu.**

---

## 2. O que a consolidação trouxe

**Quatro cadeias novas:** `cjf.fgts.correcao-monetaria` (11 segmentos), `cjf.fgts.juros-mora` (3),
`cjf.poupanca.correcao-monetaria` (12), `cjf.poupanca.juros-mora` (3).

**R1 e R2 não se moveram** — as cadeias novas são perfeitamente contíguas. **R3 subiu de 25 para
46**, e a composição importa: **19 são `R3-INDETERMINADO`** — a pendência ficando visível — e
**duas são R3 cheias, do manual**, ambas na poupança: `1986-03` ORTN→IPC/IBGE e `1990-04`
IPC/IBGE→BTN, **sem `aplicacao`**. **Não harmonizadas.**

### Quatro achados que o bloco 8 não tinha

1. **O calendário de juros de FGTS e poupança é outro.** Vão de Selic **direto a taxa legal em
   set/2024** — **um ano antes das demais**, **sem corte de dez/2021 nem de set/2025**, e **sem
   citar o ARE 1.557.312**. Quem aplicar aqui o calendário das condenatórias gerais **erra**;
2. **A fórmula `D4` tem mais um domicílio.** 4.8.3 e 4.9.3 usam o eixo da **competência da
   parcela**, que o bloco 8 dava **só à dívida fiscal**;
3. **A divergência FGTS × poupança inclui o rótulo do IPC** em duas janelas — a poupança escreve
   `IPC/IBGE` nos mesmos meses em que o FGTS escreve `IPC` nu;
4. **A NOTA 3 de 4.9.1.1 é cadeia paralela** — BTNF/TRD para cruzados novos bloqueados — **que
   nenhuma tabela mostra**. É o padrão *"a regra vive só no item"*, terceira vez no corpus.

### `tipo_indexador` — sete novos `indeterminado`

Por fonte: **ORTN, OTN, BTN** `nominal`; **IPC/IBGE** `percentual` (D8-C21); **Selic** e **taxa
legal** `englobante`. **`JAM`, `UPC`, `LBC`, `LBC–0,5%`, `LFT–0,5%`, `TRD` e o `IPC` nu** ficaram
**`indeterminado`** (`P18-01`).

> **O `IPC` nu merece nota.** `D8-C21` sustenta o **`IPC/IBGE`**, e o manual usa **dois** IPC —
> IBGE e FGV. Classificar o `IPC` nu por herança do irmão seria a dedução proibida. **Catálogo
> com 35 rótulos, 17 indeterminados.**

**`D8-C13` / `N-5` fica aberta:** os expurgos do FGTS **não viraram segmento**, porque gravá-los
exigiria **escolher entre substituir e somar** — e o manual não diz. O capítulo 4 geral diz *"em
substituição"*; o do FGTS, nada.

---

## 3. Descoberta por conteúdo, e um manifesto que não envelhece

**(a) já estava feito no bloco 17** e foi **confirmado, não refeito**: as quatro cadeias novas
entraram sozinhas na contagem — **é a prova de que a descoberta lê `tipo`, não o nome**.

**(b) o manifesto:** `docs/calculo/tabelas-normativas/cadeias-manifesto.json`.

> **Manifesto que precisa de edição manual a cada cadeia nova envelhece igual à constante que
> veio substituir.** Este é **assimétrico**: `valida_cadeias.py` **grava sozinho** a cadeia nova e
> avisa; **nunca remove nem baixa contagem**. Só o encolhimento exige edição deliberada.
>
> **Cadeia a mais é crescimento normal. Cadeia a menos é regressão.**

**A chave é o campo `id`, não o nome do arquivo** — indexar por nome repetiria o erro do bloco 17
com o sinal trocado: renomear acusaria ausência. E guarda **`segmentos` por cadeia**, não o total
agregado, onde uma cadeia que encolhe some por compensação com outra que cresce.

**Verificado ponta a ponta:** removendo `cjf.poupanca.juros-mora.json`, o validador sai com
**exit 1 nomeando a cadeia**, e três testes caem.

**As duas guardas** viraram `confere_manifesto()` + piso por cadeia. **Nenhum número cravado
sobrou** — trocar `11` por `15` reintroduziria o defeito em quatro meses.

**(c) a varredura dos oito scripts achou mais um defeito real:**
`valida_bloco_tabelas.py` fazia `DIR_SERIE.glob("serie-*.csv")`. **Renomear um CSV o tirava da
conferência de proveniência em silêncio, com o resumo ainda dizendo "0 erros".** Agora
`glob("*.csv")` — **quem decide conferibilidade é o cabeçalho declarado**, e o inconferível sai
em `NÃO VERIFICÁVEL`.

**Os demais são legítimos, e a razão é uma só:** nomes cravados que são **abertos direto** somem
com `FileNotFoundError` — **falham alto**. `extrai_bloco_01.py` é extrator de **um** documento
fixo, e suas contagens são reconferidas contra o PDF. `gera_cadeias_bloco18.py` deriva o nome
**do `id`** — conteúdo → nome, **direção certa**.

> **O teste não é "usa nome de arquivo?". É: se alguém renomear, o script falha alto ou fica em
> silêncio?** Silêncio é o defeito.

---

## 4. Ponteiros — e o ledger que pegou quem o escreveu

**21 alvos inexistentes, e nenhum era ponteiro morto de verdade:** 2 PDFs do corpus (externos,
declarados em `fontes.md`), 7 arquivos de página extraída (insumo efêmero, citado como proveniência), 7 nomes
históricos, 4 moldes de nomenclatura. **Os `trt3.*` restantes são todos narrativa — o bloco 17
fechou os reais.**

**Um achado inesperado, corrigido:** o detalhe do bloco 13A apontava, na linha 447, para o
detalhe do bloco 8 **com o sufixo em caixa alta**, em prosa nua — nome quase certo, alvo
inexistente.

### Como `test_ponteiros.py` distingue narrativa histórica

**Ledger declarado e autolimpante, chaveado pelo par `(alvo, arquivo)`** — não pelo alvo solto.

Duas alternativas foram rejeitadas, com razão: **heurística de contexto** erra dos dois lados, e
**falso positivo faz ignorarem o validador**; **marcação no texto** é auto-atribuída por quem
escreve o erro.

**O ledger não envelhece** porque um segundo teste **falha em exceção órfã** — alvo que passou a
existir, ou menção que sumiu. E `test_a_varredura_enxerga_o_repositorio` impede passar por
vacuidade. **~1,3 s**, sem `pytest`.

> **O ledger pegou o próprio agente que o escreveu.** Ao redigir o `scripts/calculo/README.md`,
> citou um script renomeado pelo nome antigo e o teste acusou — a exceção valia nos três
> relatórios que narram a fusão, **não num README novo**. Episódio registrado no README.

---

## 5. Dedução por nome — busca com escopo declarado

**Escopo:** `docs/`, `skills/`, `scripts/`, `tests/`, em `.md`, `.json`, `.py`, `.csv`. Termos:
`INPC, IPCA, IGP`; e `IPCA-E|IPCA-15|IPC-R|IRSM|IPC/FGV|MVR` a até 60 caracteres de
`percentual`.

**Os seis arquivos do bloco 17 estão limpos.** As ocorrências restantes são de três espécies, e
nenhuma é dedução:

| Onde | O que é |
|---|---|
| `00-base-normativa.md` § 7 · `03-casos-dificeis.md` | **divergência declarada, que este bloco está proibido de alterar** — `pendencias.md` § 23 |
| `01-dominio-e-invariantes.md:79` · `bloco-17-relatorio.md` | **a nota que registra a divergência**, e a narrativa |
| a cadeia das condenatórias gerais · `civel-federal.md:96` | *"O **percentual** a ser utilizado"* — literal do manual sobre **valor**, não classificação |
| `indices-judiciais/SKILL.md` linhas 9, 33, 263, 448 | frases-gatilho, escopo, **a própria anti-heurística** e o rebaixamento da TR |

**`indices-judiciais/SKILL.md` não se contradiz mais.** E uma enumeração obsoleta foi corrigida
no caminho: o Passo 1 dizia *"nominal, percentual ou englobante"* — **são cinco classes**, e a
quarta é a que mais governa o motor.

> **`indeterminado` e `nao-indexador` afirmam coisas diferentes:** *"não se sabe"* × *"não se
> pergunta"*. **Ausência do campo não é nenhum dos dois** — é indistinguível de esquecimento.

---

## 6. O que o consolidado não bastou para escrever

**Seis pontos em que as `reference` tiveram de buscar no JSON ou na extração**, todos declarados
no arquivo onde aparecem. Os dois de maior alcance:

- **os literais das notas de 4.8.3/4.9.3 e dos juros remuneratórios** (4.8.2, 4.9.2) **não estão
  no consolidado** — o § 5.3.4 parafraseia. Vieram dos JSON do mesmo bloco, que trazem
  `pagina_pdf`;
- **as observações linha a linha da tabela da poupança** (ORTN *pro rata* em fev/1986, BTNF de
  19–28/3/1990, jan/1991, abr/1993, jun/1994) aparecem **sem o fundamento legal**; os decretos e
  leis só existem no JSON.

> **É o mesmo padrão que o bloco 18 veio corrigir, um nível acima:** a espinha consolidada é mais
> fina que o dado extraído, e quem escreve a skill descobre isso ao precisar do literal.

**Uma divergência interna não foi harmonizada:** o § 5.3.3 fala em *"dezesseis anos e dois
meses"* para a janela UPC × ORTN e o `D8-C15` totaliza *"dezesseis anos e quatro meses"* somando
os quatro meses de 1987. **Coerentes, mas aplicados a recortes diferentes. Reproduzidos como
estão.**

---

## 7. O que continua aberto

| Aberto | Natureza |
|---|---|
| **`P18-02` — oito cadeias tabuladas sem JSON** | a desapropriação **indireta inteira**, os juros da direta, os juros fiscais e o **FGTS fiscal (`JCM`)** |
| **`P18-01` — sete índices novos sem fonte** | `JAM`, `UPC`, `LBC`, `LBC–0,5%`, `LFT–0,5%`, `TRD`, `IPC` nu. **Não se fecha relendo os PDFs** |
| **`D8-C13` / `N-5`** | os expurgos do FGTS **não dizem se substituem ou acrescem**. Gravá-los exigiria escolher |
| **duas R3 cheias na poupança** | do manual, **sem `aplicacao`**. Seguem acusadas — e devem seguir |
| **`00-base-normativa.md` § 7** | divergência declarada. **Correção fora do agente**, por determinação do enunciado |

> **Afirmar ausência de algo que a fonte nunca prometeu seria tão errado quanto perder o que ela
> promete.** Foi o que separou as dez lacunas reais do 4.7.1.
