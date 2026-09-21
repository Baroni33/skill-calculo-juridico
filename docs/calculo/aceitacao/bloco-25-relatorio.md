# Bloco 25 — a regra foi morar com quem a consome

**Estado: fechado, depois da validação adversarial e das seis correções que ela cobrou.**
Os **32 `.json` de regra** e **4 validadores** migraram por **consumo**, a guarda de **1024
caracteres** na `description` passou a existir, o veredito de **`RG10`** foi dado, e a afirmação
de que **nenhuma série migrou** — publicada por este bloco — **era falsa e foi corrigida**.

> **Registro datado. Não se atualiza.** Estado corrente em
> [`../consolidado/00-numeros.md`](../consolidado/00-numeros.md).

---

## 1. O diagnóstico: não havia arquivo misto, e a separação já estava declarada

**A pergunta de entrada era *"quais arquivos misturam regra e série?"*. A resposta foi: nenhum.**

A separação **(A) semântica** × **(B) série** não precisou ser feita — ela já existia, **gravada
no próprio artefato** desde o bloco 1, no campo `categoria: "A-semantica"`. Nove arquivos de
regra o carregam. As séries de valor sempre viveram em `.csv` separados, marcados `OUT_OF_SCOPE`
no cabeçalho, e o `README` do diretório de tabelas já dizia, na seção *"O que não entra"*:
*"Séries de valores mensais"*.

**Consequência para o desenho da migração:** não houve arquivo a partir. A operação foi de
**endereço**, não de **conteúdo** — e por isso o `git` registra **renomeação**, não reescrita. É
o que permite auditar a migração com `git log --follow` em vez de ler 32 diffs.

---

## 2. A migração, e o critério foi CONSUMO

**Quem lê o arquivo decide onde o arquivo mora.** Não o assunto, não o nome, não a família de
schema.

| O que | Para onde | Quem consome |
|---|---|---|
| as cadeias `cjf.*` e `trab.hist.*`, `cadeias-manifesto.json` e `indexadores-tipo-catalogo.json` | `calculo-judicial-atualizacao/regras/` | `valida_cobertura.py`, `valida_cadeias.py`, as `references/` de atualização |
| `regimes-temporais-catalogo.json` + `camada-regime-temporal-schema.json` | `calculo-judicial-core/regras/` | `valida_regimes.py` |
| `camada-norma-coletiva-*` e os 6 `trt3-18.*` | `calculo-trabalhista-liquidacao/regras/` | `valida_parametros.py`, as `references/` de liquidação |

**`indexadores-tipo-catalogo.json` tem UM dono**, e a regra que o fixou vale para o futuro:
**o dono é a skill onde mora o validador que o lê.** `indices-judiciais` e
`calculo-judicial-core` **apontam** para ele; nenhuma guarda cópia. Duas cópias de um catálogo
divergem — é o defeito que o bloco 23 pagou para aprender.

### A contagem do trabalho de ponteiro, com escopo declarado

> **Esta medição não existia.** O bloco afirmou em conversa *"113 ocorrências em 54 arquivos"* e
> **não a registrou em lugar nenhum**. Ela **não é reafirmada aqui**: não há como reconstruir o
> escopo que a produziu. O que segue foi **medido agora**, com o escopo escrito antes.

| | |
|---|---|
| **O que se contou** | ocorrências da string `tabelas-normativas/` |
| **Escopo** | `README.md` da raiz, `docs/`, `skills/`, `scripts/` — extensões `.md`, `.json`, `.py` |
| **Ferramenta** | `git grep -c`, contra `HEAD` e contra a árvore de trabalho |
| **Antes (`HEAD`, pré-migração)** | **158** ocorrências em **80** arquivos |
| **Depois (fechamento do bloco 25, já com as correções)** | **82** ocorrências em **44** arquivos |

**As 82 que ficam não são dívida.** São, quase todas, **registro datado** — relatório de bloco e
documento de extração que citam o endereço que o artefato tinha no dia em que foram escritos — e
o diretório **continua existindo**, agora guardando só o `README.md`, que é o contrato de campo e
o histórico das decisões. O que **não** pode ficar é ponteiro **navegacional** para lá; esses
foram corrigidos, e a guarda que os pega está descrita em § 8.

---

## 3. Os validadores promovidos — 4 de 21

A classificação dos 21 `.py` foi feita no **bloco 24**, que mandou classificar e **não mover**.
Este bloco moveu, e só os que a classificação dava como limpos ou híbridos resolvíveis:

| Validador | Para onde | Por quê |
|---|---|---|
| `valida_taxa_legal.py` | `calculo-judicial-atualizacao/scripts/` | autocontido: `argparse`, sem `RAIZ`, R11 sobre um par que o usuário passa |
| `valida_cobertura.py` | `calculo-judicial-atualizacao/scripts/` | recebe a tabela como caminho arbitrário; R1/R2/R3 sobre conjuntos de segmentos |
| `valida_regimes.py` | `calculo-judicial-core/scripts/` | resolvedor; o `CATALOGO_PADRAO` passou a apontar para `regras/`, irmã |
| `valida_parametros.py` | `calculo-trabalhista-liquidacao/scripts/` | idem |

**Os outros 17 continuam em `scripts/calculo/`**, e a razão é a mesma que os classificou:
aferem **o repositório**, não uma implementação. `valida_cadeias.py` valida *as cadeias deste
repositório*; `test_numeros.py` e `test_ponteiros.py` vigiam o repositório contra si mesmo;
`gera_numeros.py` **escreve** em `docs/`.

### O ponteiro único, e por que ele existe

`scripts/calculo/caminhos_de_skill.py`. **Nove ferramentas de pipeline precisavam do caminho
novo.** Cravá-lo nove vezes seria tomar a decisão nove vezes e envelhecê-la nove vezes. O módulo
também põe os `scripts/` das skills no `sys.path`, que é o que deixa `test_valida_regimes.py` e
as irmãs seguirem fazendo `from valida_regimes import …` sem saber onde o arquivo foi parar.

### A instalação foi verificada fora do repositório, e o método está escrito

> **Também isto não tinha registro.** O bloco afirmou *"copiei as quatro pastas para fora e rodei
> lá"* sem dizer o quê nem o que observou. **Refeito e escrito:**

```
cp -r skills/{calculo-judicial-core,calculo-judicial-atualizacao,\
              calculo-trabalhista-liquidacao,indices-judiciais}  <dir fora do repo>/
```

**68 arquivos**, `__pycache__` removido, **sem `docs/` e sem `scripts/calculo/`**. Rodando de
dentro desse diretório:

| Comando | Resultado |
|---|---|
| `calculo-judicial-core/scripts/valida_regimes.py` | **exit 0** — *"consistência interna: OK"* |
| `calculo-trabalhista-liquidacao/scripts/valida_parametros.py --catalogo-ok` | **exit 0** — 32 parâmetros, 16 provisórios |
| `calculo-judicial-atualizacao/scripts/valida_taxa_legal.py --help` | `usage:` completo |
| `calculo-judicial-atualizacao/scripts/valida_cobertura.py <regra>` | **exit 1 — e é o resultado certo**: são as violações `R3-INDETERMINADO` pré-existentes (`P19-01`, taxa legal sem fonte). Rodou, leu a regra ao lado, e acusou o que tinha de acusar |

> **Um achado da verificação, e ele não é da skill:** `valida_cobertura.py` imprime `→` e quebra
> em console `cp1252`. Com `PYTHONIOENCODING=utf-8` roda limpo. É ambiente, não empacotamento —
> **registrado, não consertado neste bloco.**

### O resíduo, contado

**28 ocorrências de `scripts/calculo/` sobrevivem em 11 arquivos das quatro pastas**, e **não são
o defeito M2**. São referências deliberadas a **ferramenta de pipeline** que nunca foi promovida
— `test_metodos.py`, `test_aceite_nivel1.py`, `valida_cadeias.py` —, citadas como *"teste DO
repositório"*. O que M2 pegou foi outra coisa: ponteiro para os **quatro que mudaram de lugar**,
em campo legível por máquina. Esses estão em § 6.

---

## 4. A guarda de 1024 caracteres

A `description` do `SKILL.md` é o que decide se a skill **carrega**. Acima de um limite, a
plataforma a trunca ou a rejeita, e o sintoma é silencioso.

A guarda vive em `test_ponteiros.py`, classe `TestManifestoDePlugin`, e cobra **duas** coisas,
porque uma sozinha passa por vacuidade:

1. **nenhuma das quatro passa de 1024** caracteres;
2. **a leitura é multilinha** — o parse tem de enxergar o valor dobrado do YAML. Uma guarda que
   lesse só a primeira linha aprovaria qualquer `description`, por maior que fosse.

**Medição no fechamento, uma a uma:** **794** (atualização), **802** (core), **870**
(liquidação), **890** (índices). A docstring do teste dizia *"entre 797 e 893"* e **nenhum dos
dois extremos era uma medição** — a faixa nem continha o menor dos quatro. Corrigido: agora
publica os quatro números.

**Os quatro `SKILL.md` seguem abaixo de 500 linhas:** 496, 495, 496, 499.

---

## 5. `RG10` — o veredito

**O PDF foi lido, as quatro páginas inteiras.** O registro completo está em
[`../pendencias.md`](../pendencias.md) **§ 28.2**, com o escopo contado antes de declarado: 63
linhas-ano, **742 fatores** de 7 casas, **zero** células com rótulo de índice e **zero** marcos
de corte datados dentro da grade.

> **SÉRIE DE VALORES — categoria (B), `OUT_OF_SCOPE`. Não é cadeia. NÃO MIGRA.**

A frase que decide é operacional, não de título, e está na p. 4: *"multiplica-se o valor
histórico pelo fator correspondente à data de origem"*. **Um número por mês, para multiplicar.**
A hipótese *"composição de seis índices, logo cadeia"* caiu **por ausência de datas de
fronteira**, não por interpretação.

**Os 742 fatores foram convertidos em `Decimal` apenas para contar e validar forma. Nenhum foi
gravado.** Povoar série é exatamente o que este bloco existe para impedir.

---

## 6. As correções da validação adversarial

### G1 — o README proclamava um absoluto, e uma série tinha migrado

**O defeito não foi o arquivo ter viajado. Foi proclamar `A SÉRIE DE VALOR NÃO MIGROU` sem
varrer as 32 regras atrás de série.** A varredura não existia. **Agora existe, e achou.**

| | |
|---|---|
| **O que se procurou** | qualquer objeto JSON com **duas ou mais chaves na forma `AAAA-MM`** |
| **Escopo, contado antes** | os **32 `.json`** de `skills/*/regras/` — os mesmos 32 que migraram |
| **Como** | `json.load` com `encoding='utf-8'`, percurso em profundidade de dicts e listas |
| **Casaram** | **3 objetos**, em 3 arquivos |

| Onde | O quê | Veredito |
|---|---|---|
| `trab.hist.fazenda-publica.juros-mora.json` | **15** percentuais de juros, jun/12–ago/13 | **fica, reclassificado** |
| `cjf.previdenciario.correcao-monetaria.json` § `segmentos[8]` | **4** percentuais de conversão em URV, mar–jun/94 | **fica, e a dúvida tem dono** |
| `cjf.fgts.correcao-monetaria.json` § `notas[1]` | 3 chaves de competência cujo **valor é frase** | **não é série** — é o contraste narrado da pendência `N-5` |

**A DECISÃO: OS DOIS FICAM, E O RÓTULO É QUE ESTAVA ERRADO.**

O teste que este projeto usa para separar as camadas é *"série (B) muda quando o governo publica
portaria"*. **Nenhum destes dezenove números pode mudar** — e isso não é conveniência, é o que a
norma diz:

* **os quinze da fazenda pública** existem porque a meta anual da Selic ficou igual ou inferior a
  8,5% (art. 12, II, `b`, da Lei 8.177/91, incluído pela MP 567/12), e **isso só ocorreu de
  jun/12 a ago/13**. O conjunto **fechou em set/13**. E o `atalho_do_manual` do próprio arquivo
  **não os dispensa**: ele vale sob a condição de uso que declara — *data final de atualização
  posterior a 31/08/13* —, e **cálculo que termine dentro da janela não tem outra resposta senão
  os quinze**. Mandá-los para `docs/` deixaria a regra **incompleta no motor instalado**;
* **os quatro da URV** não são índice, e o segmento já o dizia antes da auditoria:
  `tipo_indexador: "nao-indexador"`, porque conversão de padrão monetário é **operação**, não
  medida de inflação de mês nenhum. E o item 4.2.3.1 do Manual CJF **não enuncia fórmula:
  enumera os quatro**. Não há regra a extrair além dos números. Sem eles a cadeia diria *que*
  converte e não *como*. Conjunto igualmente fechado: encerrado pela implantação do real em
  01/07/1994.

**O que mudou, então:**

* `natureza` dizia *"série (B) — percentuais cravados, mês a mês"* e passa a dizer o que o
  conjunto é: **conjunto fechado por norma, exaurido**;
* a chave `serie` virou `percentuais_por_competencia`, com o nome antigo registrado ao lado em
  `chave_anterior` — **para que a busca continue achando o caso**, e não para escondê-lo;
* os dois arquivos carregam `DECISAO_BLOCO_25`, com o argumento inteiro;
* o `README` de `tabelas-normativas/` **deixou de afirmar o absoluto**: publica a varredura, o
  escopo, os três achados e as duas decisões.

**O que este bloco aprendeu:** *"conjunto fechado por norma"* é uma **terceira coisa**, e ela
pertence à regra. Regra e valor continuam sendo coisas diferentes.

### G2 — a dúvida declarada, e agora com dono

Resolvida junto de G1, acima, e gravada no próprio segmento. **O auditor declarou dúvida, não
acusação, e a razão era boa.** A resposta não desfaz o fato que gerou a dúvida — quatro números
indexados por competência dentro de `regras/` —; ela nomeia por que esses quatro **não** são a
coisa que a regra proíbe.

### M1 — oito links mortos, e a guarda que era cega para eles

Os **8** links markdown clicáveis para `tabelas-normativas/` foram corrigidos:
`presets-regime.md` (4), `parametros-negociaveis.md` (3), `consolidado/00-calendario-de-cortes.md`
(1). Quatro deles estavam sob o rótulo **"Fonte de verdade executável"** — o pior lugar possível
para um ponteiro morto.

**E `test_ponteiros.py` passava**, por uma válvula que dizia: *se o nome-base existe em algum
lugar, não é morte, é imprecisão de caminho relativo*. **Ela tem razão de existir** — mas foi
desenhada contra **RENOMEAÇÃO**, e este bloco fez **MUDANÇA DE DIRETÓRIO**. O basename sobrevive
à mudança de diretório, e imuniza todo ponteiro antigo.

> **Não é bug do bloco 25: é a guarda não cobrindo o risco que o bloco 25 criou.** Por isso ela
> foi apertada, e não a operação desfeita.

**O aperto:** o nome-base ainda salva, mas só se **todo diretório citado no alvo for diretório
REAL** de algum arquivo com esse nome. um alvo citado como *consolidado/…* continua salvo, porque o arquivo mora mesmo dentro de um
`consolidado/`; um alvo citado como *tabelas-normativas/…* não, porque esse diretório deixou de
ser diretório do arquivo.
Alvo sem diretório nenhum — o nome do arquivo sozinho entre crases — passa direto: **nome nu não
promete caminho**.

**O custo foi medido antes da decisão, como o bloco 20 estabeleceu:**

| | |
|---|---|
| ponteiros que dependiam **só** da válvula larga | **728** |
| ponteiros que **deixaram de ser imunizados** pelo aperto | **18**, em **11** arquivos |
| deles, **defeito de verdade** | **13** — endereço de artefato que a migração moveu. **Corrigidos**, não excepcionados |
| deles, **falso positivo genuíno** | **5** — abreviação de nome de skill em prosa — *liq*, *core* e *atualizacao* no lugar do nome inteiro do diretório |
| entradas novas de ledger | **5**, classe nova **`registro datado de bloco`** |

**Os 5 falsos positivos foram escritos por extenso**, não excepcionados: custa menos que uma
entrada de ledger e o documento fica melhor. **Custo declarado:** quem quiser abreviar diretório
de skill entre crases terá de tirar as crases ou declarar a exceção. Julgado barato diante de 13
ponteiros mortos que o teste aprovava.

**A classe `registro datado de bloco` é distinta de `narrativa histórica`**, e a distinção é a
que o ledger já fazia em `test_numeros.py`: narrativa **descreve** a mudança (*"era X, virou
Y"*); registro datado apenas **gravou**, no dia em que foi escrito, o endereço de então.

**Prova contra vacuidade:** `test_a_valvula_perdoa_caminho_relativo_e_acusa_mudanca_de_diretorio`
planta os dois casos lado a lado num repositório sintético e exige que o primeiro passe e o
segundo caia. Sem ele, afrouxar a regra de volta não faria barulho.

### M2 — ponteiros dentro das skills para o que a instalação não copia

**A mesma doença, na direção inversa.** Corrigidos, e dois deles eram **campo legível por
máquina**:

| Arquivo | Campo |
|---|---|
| `calculo-judicial-core/regras/camada-regime-temporal-schema.json` | `"validador"` |
| `calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json` | `"ONDE_ISTO_E_CONSUMIDO"` |
| `calculo-judicial-core/references/linguagem-alvo-e-aritmetica.md` | prosa, mais um quadro novo que diz **onde cada validador mora e por quê** |
| `tabelas-normativas/README.md` § Validação | **o pior, porque é o README que este bloco reescreveu.** Virou tabela com os 6 validadores e os caminhos de hoje |
| `presets-regime.md`, `parametros-negociaveis.md` | ponteiros de "Ver também" |

Mais **6 ocorrências em `pendencias.md`** e **1 em `10-literais-na-extracao.md`**, achadas pelo
aperto de M1 — todas em frases no presente, sobre validador vivo.

### M3 e M4 — geradores que sobrescrevem curadoria

**O defeito é de classe, e por isso a correção é de classe.** Quatro geradores *one-shot*
rodaram uma vez e tiveram a saída **curada depois, à mão, por outros blocos**. Nenhum deles sabe
disso, e todos escreviam por cima sem perguntar. **Nenhum era testado.**

| Gerador | O que desfazia |
|---|---|
| `gera_cadeias_bloco19.py` | a **tokenização de `aplicacao`** do bloco 23 em 4 cadeias — 3 testes caíam |
| `gera_cadeias_bloco18.py` | idem, em `cjf.fgts.juros-mora` e `cjf.poupanca.juros-mora` |
| `migra_bloco19_tipos.py` | prosa ampliada de `tipo_indexador_por_que` e `_fechamento` — **e o cabeçalho dele afirmava idempotência** |
| `extrai_bloco_01.py` | **20 linhas de proveniência de R3** em 6 `serie-*.csv` |

> **Não era regressão do bloco 25. Mas o bloco 25 AGRAVOU a consequência:** antes o gerador
> estragava `docs/`; depois da migração estraga o **artefato empacotado**, o que o usuário
> instala.

**A saída escolhida, e as duas que foram descartadas com razão escrita** (em
`scripts/calculo/escrita_curada.py`):

* **`--forcar` obrigatório sempre** — rejeitado: pune o caso inocente. Dois dos quatro arquivos
  de `gera_cadeias_bloco18.py` são reproduzidos hoje byte a byte;
* **gerador idempotente reaplicando a curadoria** — o padrão que o enunciado mandou examinar.
  Rejeitado: põe no gerador o conhecimento de todas as curadorias **futuras**. É a mesma dívida,
  adiada. (E o *"`gera_cadeias_bloco18.py` é idempotente"* do enunciado **não se confirmou na
  medição**: ele também reescrevia dois arquivos.);
* **ESCOLHIDA — conferir antes de escrever.** Idêntico: não escreve. Inexistente: escreve.
  **Divergente: RECUSA, nomeia os arquivos, e sai com código 2.** `--forcar` continua, para o dia
  em que a intenção for mesmo regerar.

**A recusa é ATÔMICA**, e é o ponto que só `grava_lote` cumpre: o lote inteiro é conferido antes
de qualquer escrita. Recusa arquivo a arquivo deixa o diretório meio regerado — que foi
literalmente o que aconteceu durante a **medição** deste bloco, quando `extrai_bloco_01.py`
danificou seis CSV antes de alguém olhar. **`extrai_bloco_01.py` foi convertido** para acumular
em memória e escrever só no fim.

**Código 2, e não 1**, de propósito: `1` é *"o validador achou violação"*, e confundir os dois
faz CI tratar recusa como divergência de norma.

**E ao consertar, o caminho citado nas linhas de proveniência foi atualizado** — as 20 linhas que
o extrator apagaria já apontavam para `tabelas-normativas/`. Agora apontam para
`skills/calculo-judicial-atualizacao/regras/` e `skills/calculo-trabalhista-liquidacao/regras/`,
em **8 `serie-*.csv`**, com escrita em modo binário para não trocar fim de linha.

**O teste novo: `scripts/calculo/test_geradores.py`, 8 testes.** Cobra duas coisas:

1. **rodar o gerador não muda byte nenhum** — subprocesso de verdade, `sha256` das três árvores
   que um gerador pode tocar, antes e depois. **Byte igual é condição mais forte que "a suíte
   continua passando"**: se nenhum arquivo muda, nenhum teste pode passar a falhar — e não
   depende de qual teste é, nem exige disparar a suíte de dentro da suíte;
2. **a guarda detecta divergência plantada**, com o lote atômico e a mensagem de recusa
   conferidos. Sem isso, uma guarda que nunca recusa passaria no item 1 por não fazer nada.

> **Custo medido e declarado:** `extrai_bloco_01.py` inteiro leva **~150 s** — cinco vezes a
> suíte toda. O teste roda **três seções** (`18.10`, `18.11`, `18.12`), que são **três dos seis
> CSV que ele danificava**, em **~4 s**. O que fica de fora é mais do mesmo caminho de código,
> não outro caminho. *Suíte que demora é suíte que se deixa de rodar.*

### L1 e L2

**L1** — a docstring de `test_as_quatro_descriptions_sao_lidas_inteiras` dizia *"entre 797 e
893"*; a medição real é **794, 802, 870, 890**, e a faixa publicada **não continha o menor dos
quatro**. O teste nunca cravou número — só a prosa estava errada, e é o defeito que este
repositório chama de **cópia sem dono**. Corrigida com os quatro números.

**L2** — `indices-judiciais` apontava o catálogo com prefixo `skills/`, **que não existe depois
de instalado**, em `SKILL.md:96` e `:283` e em `references/catalogo-de-indices.md:7` e `:65` —
enquanto o próprio `SKILL.md:71` já usava a forma certa, `calculo-judicial-atualizacao/regras/…`,
que é irmã. **Inconsistente consigo mesmo.** As quatro passaram à forma certa.

---

## 7. O que este bloco deixa como regra para os próximos

1. **Afirmação de ausência exige varredura, e varredura exige escopo contado antes de
   declarado.** Foi por não cumprir isso que o bloco publicou *"a série não migrou"*;
2. **guarda desenhada contra um risco não cobre o risco vizinho.** A válvula de nome-base era
   contra renomeação e ficou cega para mudança de diretório. **Ao mover coisas, pergunte de que
   risco a guarda existente protege**;
3. **gerador one-shot é artefato perigoso enquanto viver no repositório.** Ou tem guarda contra
   sobrescrita, ou é apagado. *"É idempotente"* escrito no cabeçalho **não é idempotência** — em
   dois dos quatro casos a afirmação era falsa;
4. **número quantitativo sem registro não se afirma.** Duas afirmações deste bloco —
   *"113 ocorrências em 54 arquivos"* e *"copiei as quatro pastas e rodei lá"* — **não tinham
   onde ser conferidas**. A primeira não foi reafirmada; a segunda foi **refeita e escrita**.

---

## 8. Verificação do fechamento

| Comando | Resultado |
|---|---|
| `python -m unittest discover -s scripts/calculo -p "test_*.py"` | **421 testes, OK** (3 skips pré-existentes). Eram **412** |
| `python scripts/calculo/gera_numeros.py --verifica` | *"em dia"* |
| `python scripts/calculo/test_ponteiros.py` | **14 testes, OK** — 1 novo |
| `python scripts/calculo/test_numeros.py` | OK |
| `python scripts/calculo/test_geradores.py` | **8 testes, OK** — arquivo novo |
| linhas dos quatro `SKILL.md` | 496 · 495 · 496 · 499 — todos **< 500** |

**Os 9 testes novos:** 8 de `test_geradores.py` e 1 de `test_ponteiros.py`
(`test_a_valvula_perdoa_caminho_relativo_e_acusa_mudanca_de_diretorio`).

**Nenhuma série de índice foi povoada. Nenhum conteúdo normativo foi alterado** — os 15
percentuais da fazenda pública e os 4 da URV estão byte a byte como estavam; o que mudou foi o
rótulo que os classificava e o registro da decisão. **Nenhum ponto flutuante binário entrou em
caminho de cálculo. Nenhuma pesquisa na web.**

---

## 9. Ver também

- [`../tabelas-normativas/README.md`](../tabelas-normativas/README.md) — a migração, a varredura de série e as duas decisões
- [`../pendencias.md`](../pendencias.md) § 28.2 — o veredito de `RG10`, com as 4 páginas lidas
- [`bloco-24-relatorio.md`](bloco-24-relatorio.md) — a classificação dos 21 `.py` que este bloco executou
- [`../consolidado/00-numeros.md`](../consolidado/00-numeros.md) — **o estado corrente.** Os números acima são datados
