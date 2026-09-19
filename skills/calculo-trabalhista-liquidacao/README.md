# skill: calculo-trabalhista-liquidacao

**Fase do pipeline:** Fase 5 — Build das skills.
**Eixo de mudança:** médio.

## Propósito

Apuração de verbas trabalhistas, descontos legais e encargos. É o "o que se deve",
antes de qualquer atualização monetária.

## O que entra

- Estrutura de apuração de verbas: aviso prévio, 13º, férias, RSR, horas extras,
  reflexos.
- Descontos legais: INSS e IRRF — conceitos e estrutura.
- Encargos e despesas processuais (**provisoriamente**, ver abaixo).

## O que não entra

- Correção monetária e juros — vão para `calculo-judicial-atualizacao`.
- Comparador/diff — fica em `calculo-judicial-core`, porque é a mesma operação nas
  três jurisdições.
- Faixas de INSS/IRRF como valores — são série mantida à parte.

## Fronteira instável

**Encargos processuais** estão aqui provisoriamente, mas provavelmente se separam:
as faixas de honorários são do **CPC art. 85, § 3º**, não da CLT, e valem nos três
ramos. Decidir na Fase 5, não antes.

## Armadilhas que esta skill precisa cobrir

- **OJ 394 da SDI-I:** reflexo de horas extras no RSR não repercute em férias, 13º,
  aviso e FGTS.
- O manual do TRT-3 é de 2016. A estrutura de apuração (cap. 6), os critérios
  matemáticos (cap. 5) e a estrutura dos descontos (cap. 9) servem; as faixas e os
  honorários, não. Ver `docs/calculo/confronto-normativo/`.

## Estado

Vazio.
