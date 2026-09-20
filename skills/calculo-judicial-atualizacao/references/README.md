# references/ — variantes por jurisdição

**Fase do pipeline:** Fase 5. **Escrito no bloco 16.**

## Propósito

Um arquivo por variante de cadeia. O agente carrega **apenas** o arquivo da jurisdição em
questão — essa é a razão de a pasta existir em vez de um único documento grande.

---

## RENOMEADO NO BLOCO 16 — e por quê

A divisão anterior separava por **qualidade do devedor** (`trabalhista-privado` ×
`trabalhista-fazenda`) e por **precedente** (`civel-cc-tema1368` × `civel-mg-cgj`). A nova separa
por **alcance da norma: NACIONAL × REGIONAL**.

| Nome antigo | Nome novo | O que motivou |
|---|---|---|
| `trabalhista-privado.md` + `trabalhista-fazenda.md` | **`trabalhista-nacional.md`** | privado e Fazenda são **dois ramos da mesma cadeia nacional**, com os mesmos cortes de 1987, 1991, 2009 e 2021. Separá-los duplicava a `R4-EXCEÇÃO`, as quatro réguas de defasagem e a Tabela Única do CSJT em dois arquivos |
| *(não existia)* | **`trabalhista-regional-trt3.md`** | os verbetes do TRT-3 que o manual invoca **não tinham casa**. Estavam implícitos na aritmética, que é **nacional** |
| `civel-cc-tema1368.md` | **`civel-cc-nacional.md`** | o Tema 1368 é **um** dos fundamentos, não o recorte. O recorte é *o que vale em qualquer estado* |
| `civel-mg-cgj.md` | **`civel-regional-tjmg.md`** | simetria com o trabalhista: o nome passa a declarar **alcance**, não sigla de órgão |
| `tributario-federal.md` | **inalterado** | — |
| `previdenciario.md` | **inalterado** | — |

### A razão de fundo — a premissa corrigida

> **Origem declarada: EXTERNA AO CORPUS** — enunciado do bloco 16, não conferido nesta fase.

A atualização monetária trabalhista é **NACIONAL** desde a **Res. CSJT 8/2005**, que unificou as
**24 tabelas** dos TRTs; hoje vale a **Res. CSJT 380/2024**, com duas tabelas — débitos comuns e
Fazenda Pública, esta referenciada ao **Manual do CJF**. O **PJe-Calc** é o sistema de toda a
Justiça do Trabalho.

O projeto vinha tratando o manual do TRT-3 como *fonte de prática regional*. **Está errado:** é
**fonte procedimental de uma região que aplica norma nacional**. Sua **aritmética não é prática
regional divergente** — regional são **os verbetes que ele invoca**.

> **A separação nacional/regional nos nomes não é organização estética. É o que permite cadastrar
> outra região sem tocar no motor:** o arquivo regional é **entrada de catálogo**, resolvida pela
> chave `(regra, tribunal, competência)`; o arquivo nacional é o **default**. Acrescentar o TRT-9
> ou o TJ-SP é acrescentar linhas, não refatorar.

Fonte da classificação: `docs/calculo/consolidado/08-nacional-e-regional.md`;
`consolidado/01-dominio-e-invariantes.md` § 2.9 (**R24**).

---

## Os seis arquivos

| Arquivo | Cobre |
|---|---|
| **`trabalhista-nacional.md`** | cadeia nacional — regime vigente (ADC 58/59 + Lei 14.905/2024), Fazenda Pública, cadeias históricas `CH-01`–`CH-05`, **Tabela Única do CSJT**, `R4-EXCEÇÃO`, as quatro réguas de defasagem, `cjf.trabalhista.juros-mora` |
| **`trabalhista-regional-trt3.md`** | os verbetes regionais que o manual invoca — **R1** Súmula 15 (data da dedução), **R13** juros na falência, **R15** tabela própria até out/2005 — com o **fallback nacional** de cada um; as outras doze regras regionais em tabela, com ponteiro; **R24** e a chave de resolução |
| **`civel-cc-nacional.md`** | STJ **Tema 1368**; SELIC de jan/2003 a 29/08/2024; **IPCA + taxa legal** a partir de 30/08/2024; termos iniciais (Súmulas 43, 54 e 362 do STJ); metodologia da taxa legal |
| **`civel-regional-tjmg.md`** | tabela da **CGJ/TJMG** — períodos pré-2003 e as **três hipóteses de sobrevida**; o que acontece fora de MG |
| **`tributario-federal.md`** | repetição de indébito e dívida fiscal; **e mais**, por falta de arquivo próprio: condenatórias gerais, **desapropriação com os juros compensatórios**, ECs 113/136 e precatório |
| **`previdenciario.md`** | cadeia de benefícios do CJF (15 segmentos) e a **taxa legal com deflator INPC** |

---

## O que não entra

- Regra **sem fundamento normativo citado**;
- Cadeia que contradiga `docs/calculo/00-base-normativa.md`;
- **Séries de valores mensais** — dado (B), contrato em `skills/indices-judiciais/`;
- **Invariantes e aritmética** — `skills/calculo-judicial-core/`;
- **Segmento solto exposto ao usuário.** O usuário escolhe preset; o motor compõe segmentos.

---

## Nota sobre `previdenciario.md` — confirmada

A taxa legal previdenciária usa **INPC** como deflator, **não IPCA-15**. Mesma fórmula, deflator
diferente. Fonte: Manual CJF, Res. 990/2026, item **4.3.2, Nota 3**.

**E a consequência que a nota antiga já antecipava está confirmada:** os **dois pares de
validação aritmética** da § 4 da base normativa (set/2025 = 1,377047% e mai/2026 = 0,277807%) são
**deste caso, não do caso geral** — a coluna do manual é `Fator INPC`. **A variante IPCA-15, que é
a regra geral e a de maior uso, segue sem par de validação contra valor publicado.** Pendência
aberta: `docs/calculo/pendencias.md` § 2.

---

## Limitação da própria divisão

**Duas cadeias federais não são tributárias nem previdenciárias e não têm arquivo:**
condenatórias gerais e desapropriação (direta e indireta, com os **juros compensatórios**, que
são **cadeia autônoma** com corte em **ago./2017** que nenhuma tabela mostra). Ficam em
`tributario-federal.md` §§ 5 e 7, **sinalizadas no topo daquele arquivo**. Candidato a sétimo
arquivo: `federal-condenatorias-desapropriacao.md`.

## Estado

**Os seis arquivos estão escritos.** `SKILL.md` escrito no mesmo bloco.
