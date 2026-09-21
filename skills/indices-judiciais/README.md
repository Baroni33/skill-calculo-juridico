# skill: indices-judiciais

**Fase do pipeline:** Fase 5 — Build das skills.
**Eixo de mudança:** mensal.

## Propósito

Semântica de aplicação dos índices e **contrato** com a tabela de séries mantida
à parte. É a skill de maior frequência de mudança e a que menos contém dados.

## O que entra

- Semântica de cada indexador: o que é, o que mede, quem divulga, quando.
- **`tipo`** — o campo que não pode faltar (R3), hoje com **cinco** valores:
  `nominal` (mês anterior), `percentual` (próprio mês), `janela-deslocada`
  (metade de cada, desde o bloco 19), `indeterminado` e `nao-indexador`.
  Trocar entre classes sem ajustar a defasagem desloca o cálculo em um mês.
  **QUAL classe cabe a cada índice sai de
  `skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json`, nunca de
  semelhança de nome** — e não se copia para cá.
- Contrato de consumo da tabela de séries: formato, chave, granularidade,
  versionamento.
- Fontes de divulgação: BCB/SGS (série 29541 = Fator da Taxa Selic mensal para
  cálculo da Taxa Legal), IBGE, Calculadora do Cidadão do BCB como oráculo de teste.

## O que não entra

- **Séries de valores mensais** (regra 4 do plano). Este é o ponto inteiro da
  skill: ela descreve o contrato, não carrega o dado.
- Cadeias período→indexador — vão para `calculo-judicial-atualizacao`.

## Requisito de versionamento

R13 exige que toda conta grave a **versão das séries consumidas**. Uma série
revisada pelo órgão emissor não pode alterar silenciosamente um cálculo já emitido.
O contrato definido aqui precisa suportar leitura por versão, não só por competência.

Ver `docs/calculo/pendencias.md` — o SaaS hoje não tem essa infraestrutura.

## Estado

Vazio.

## Esta skill NÃO tem `regras/` — BLOCO 25

**E é deliberado.** O bloco 25 levou cada família de regra para dentro da skill que a
consome, e `indexadores-tipo-catalogo.json` tinha três candidatos — este entre eles, por
ser semântica de índice. **Ficou com `calculo-judicial-atualizacao`:** é lá que mora
`valida_cobertura.py`, o validador de **R3** que lê o catálogo, e é lá que estão as
cadeias que o citam no campo `tipo_indexador_catalogo`.

**Um dono só, e ponteiro dos outros.** Esta skill aponta para
`skills/calculo-judicial-atualizacao/regras/indexadores-tipo-catalogo.json` e **não guarda
cópia** — a skill de menor conteúdo de dado não fica com o dado. Copiar produziria a
divergência que `test_classes_de_indice.py` já pegou uma vez, quando IPCA-E e IPCA-15
viraram `janela-deslocada` no catálogo e duas skills seguiram publicando `indeterminado`.
