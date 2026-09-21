# Aceite em dois níveis — o que a skill sustenta e o que o sistema sustenta

**Carregue este arquivo antes de tratar as fixtures de `tests/fixtures/calculo/` como critério de
aceite de um implementador que só tem as skills.** Elas não são — e a razão está declarada abaixo.

---

## 1. A contradição que este arquivo resolve

O conjunto **declara não carregar série de índices** — `skills/indices-judiciais/SKILL.md` diz
literalmente *"esta skill não carrega série — é o ponto inteiro dela"*, e
`skills/calculo-judicial-atualizacao/references/civel-federal.md` repete — **e ao mesmo tempo
apresentava as quatro fixtures do CJF como critério de aceite**. A **fixture 1 sozinha consome 23
meses de IPCA-E**; as skills publicam **cinco valores de índice ao todo**.

> **As duas afirmações não podem ser verdadeiras ao mesmo tempo.**

**A resolução não é popular série. É declarar o nível.** A série segue sendo dependência externa,
por desenho; o que muda é **de quem** as fixtures são critério de aceite.

---

## 2. Os dois níveis

| | O que é | Executável |
|---|---|---|
| **NÍVEL 1** | os **invariantes e a aritmética**: **R11** pelos dois pares publicados, **R12 verificável** — zero ponto flutuante binário no caminho de cálculo, pelo método que a linguagem permitir (`linguagem-alvo-e-aritmetica.md` § 1.2) —, **R1 na composição**, as **cinco cadeias de arredondamento** e o **NMP de três ramos** | **só com a skill** |
| **NÍVEL 2** | as **quatro fixtures do CJF** de `tests/fixtures/calculo/` | **exige série carregada** |

**O NÍVEL 1 não é lista idealizada — é o que um implementador de fato acertou lendo só as skills,
sem série nenhuma.** O inventário está em `docs/calculo/aceitacao/bloco-22-relatorio.md` § 1.

> **O código que o produziu — `docs/calculo/aceitacao/frente-a/` — é artefato datado do bloco 22 e
> evidência da aceitação. NÃO é o exemplo de aceite, e não é modelo a seguir.** O exemplo é a
> **tabela de entrada e saída esperada, em dado**: `tests/fixtures/calculo/`, mais o procedimento
> em `metodos-resumido-e-detalhado.md`. Implementação de uma linguagem que vira modelo é âncora
> para a próxima — ver `linguagem-alvo-e-aritmetica.md` § 3.

### 2.1 A consequência

> **O NÍVEL 1 é o critério de aceite DA SKILL. O NÍVEL 2 é critério de aceite do SISTEMA** — do
> motor com a camada (B) plugada —, **não da skill.**

---

## 3. Onde o NÍVEL 1 vive, e por que ali

**`scripts/calculo/test_aceite_nivel1.py`** — teste executável, no mesmo diretório da suíte que o
repositório roda inteira (`python -m unittest discover -s scripts/calculo -p "test_*.py"`).

> **Ele é Python, e permanece Python — mesmo que o motor não seja.** Script de skill roda no
> ambiente do **AGENTE**, para verificar a implementação; **não roda no produto**. A linguagem do
> script de verificação é **independente** da linguagem do motor. O mesmo vale para
> `valida_taxa_legal.py`, que implementa **R11** e pode ser executado pela skill sem que exista
> motor nenhum. Ver `linguagem-alvo-e-aritmetica.md` § 2.

**Por que ali e não nos outros dois candidatos:**

- **não em `tests/fixtures/calculo/`**, porque aquele diretório é **dado**, não código: um arquivo
  a mais ali seria prosa que ninguém roda, e **critério de aceite que ninguém roda envelhece** —
  foi exatamente o que aconteceu com a afirmação que este bloco veio corrigir;
- **não só numa seção de skill**, pela mesma razão. A seção existe (`## Fixtures de aceite` da
  espinha), e **aponta** para o teste; ela declara, o teste verifica;
- **em `scripts/calculo/`**, porque é o único lugar do repositório onde algo **roda em toda
  varredura** e já contém os validadores de R1, R2, R3, R6, R11 e R12 que o NÍVEL 1 invoca.

**O teste não é motor de cálculo** — a restrição de `scripts/calculo/README.md` segue valendo. Ele
afere **aritmética normativa e invariante sobre cadeia**, ancorado em **número publicado pelo
corpus** em cada asserção; não liquida condenação e não consulta série.

**Ele também guarda a própria declaração:** uma classe do teste falha se
`tests/fixtures/calculo/README.md` ou as duas `SKILL.md` deixarem de declarar o bloqueio do
NÍVEL 2. A correção deste bloco não pode regredir em silêncio.

---

## 4. As quatro fixtures — NÍVEL 2, com o bloqueio nomeado

| Fixture | Cobre | O que falta para rodar |
|---|---|---|
| `fixture-01-fazenda-publica-jun2022` | Fazenda, antes da virada de 2024 | **IPCA-E a partir de 2020-01** — 23 meses |
| `fixture-02-fazenda-publica-jun2026` | Fazenda, regime atual | idem, até jun/2026 |
| `fixture-03-nao-fazenda-publica-jun2026` | não-Fazenda, regime atual | **IPCA-E a partir de 2002-01** |
| `fixture-04-precatorio-complementar` | precatório, com exclusão de compensatórios | **INPC a partir de 2016-01**; e `pr.imputacao` **sem default** (`R20-EXCEÇÃO`) |

**As fixtures 2 e 4 divergem entre o método RESUMIDO e o DETALHADO do próprio manual** — R$ 0,01 e
R$ 0,03, com `divergencia_e_assercao: true`. **Não divergem do corpus.** Motor que produz **um**
número só **não passa**, e motor que produz **dois números iguais FALHA**. Os dois procedimentos
estão em `skills/calculo-judicial-atualizacao/references/metodos-resumido-e-detalhado.md`.

### 4.1 Requisito registrado, **não implementado**

> **O bloco de aceitação deve poder rodar contra implementação em QUALQUER linguagem.**

**O que o bloco 22 testou — composição e invariantes — já é agnóstico, e a aceitação não se
refaz.** O que acopla hoje é **o modo de invocação**: `docs/calculo/aceitacao/frente-a/runner.py`
importa os módulos Python diretamente. Um harness que atravesse uma fronteira neutra — processo,
arquivo ou serviço — é **requisito do aceite futuro**, aqui **registrado e não implementado**.

**A entrada e a saída esperada já estão em dado** (`tests/fixtures/calculo/`); é o suficiente para
que o requisito seja cumprível sem reescrever critério nenhum.

---

## 5. Ponteiros

| Assunto | Onde |
|---|---|
| O que a skill entregou sem série — a definição do NÍVEL 1 | `docs/calculo/aceitacao/bloco-22-relatorio.md` § 1 |
| O teste do NÍVEL 1 | `scripts/calculo/test_aceite_nivel1.py` |
| **O par asserido das fixtures 2 e 4 — entrada e saída esperada, em dado** | `tests/fixtures/calculo/` (`divergencia_e_assercao: true`) |
| Linguagem-alvo, verificabilidade de R12, e por que a implementação de referência não é modelo | `linguagem-alvo-e-aritmetica.md` |
| Artefato datado do bloco 22 — **evidência, não modelo** (inclui `runner.py`) | `docs/calculo/aceitacao/frente-a/` |
| Os dois métodos, procedimento executável | `metodos-resumido-e-detalhado.md` |
| Contrato de série — a camada (B) | `skills/indices-judiciais/` |
