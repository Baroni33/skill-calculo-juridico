# references/ — detalhe por ponto de apuração

**Fase do pipeline:** Fase 5. **Escrito no bloco 16.**

## Propósito

`SKILL.md` passou de 500 linhas. Esta pasta existe para que o agente carregue **apenas** o arquivo
do ponto em questão, e não um documento único grande.

**A regra de repartição:** `SKILL.md` fica com o que o motor precisa **em toda conta** — as
camadas, os invariantes que mordem, o procedimento, as armadilhas com efeito de valor, as fixtures
e **as limitações declaradas por inteiro**. Os `references/` ficam com **o detalhe de cada ponto**:
as duas versões de cada bifurcação, a espinha verba a verba, a mecânica dos descontos, as letras
do capítulo 10, os encargos e o catálogo regional.

---

## Os seis arquivos

| Arquivo | Cobre |
|---|---|
| **`cortes-e-bifurcacoes.md`** | **as trinta bifurcações, cada uma com AS DUAS versões, o corte e o eixo** — os quinze pontos de 11/11/2017, os quatro cortes de verbas fora dele, sete nos descontos, três nos encargos e a multa do art. 477; os cancelamentos da Res. 225/2025 como **cadeia temporal**; e os presets que não têm tabela própria |
| **`verbas-catalogo.md`** | verba a verba — base de cálculo, aviso, 13º, férias, RSR, HE (divisores, adicionais, reflexos, dedução da OJ 415, supressão), *in itinere*, sobreaviso, intervalos, adicionais, comissões, gorjetas, multas, seguro-desemprego, FGTS |
| **`descontos-inss-irrf.md`** | fato gerador e o corte de 05/03/2009; três regimes de atualização; cota do empregado e patronal; `F7-01` alíquota única × progressiva; desoneração; `F7-03` juros na base do IR; art. 12-A × 12-B; **NM**; momento do cálculo; o rateio de 10.2 |
| **`imputacao-e-amortizacao.md`** | a linha de base sem amortização e os três deltas de base; **as duas molduras do cap. 10**; o rateio proporcional e sua ausência de fundamento; **`R23` descarregar**; o item "i" da ADC 58; **as três posições sobre a data da dedução** |
| **`encargos-processuais.md`** | custas processuais e de execução (**base por exclusão**, `R8-CE-01`); honorários periciais; honorários advocatícios, faixas do art. 85, § 3º, e gratuidade; **a contradição sobre Fazenda Pública**; contribuição sindical e assistencial; precatórios |
| **`regras-regionais.md`** | **as quinze regras regionais, cada uma marcada com o tribunal**, com o efeito no resultado e o **fallback nacional**; `R24` e a chave `(regra, tribunal, competência)`; o que é NACIONAL e se confunde com regional; **as oito DÚVIDAS** |

---

## Por que `regras-regionais.md` é um arquivo separado

**Não é organização estética.** É o que permite **cadastrar outro tribunal sem tocar em nenhum dos
outros cinco**: o arquivo regional é **entrada de catálogo**, resolvida pela chave
`(regra, tribunal, competência)`; tudo o mais é o **default nacional**. Acrescentar o TRT-9 é
acrescentar linhas, não refatorar.

**A premissa que sustenta isso é EXTERNA AO CORPUS** — enunciado do bloco 16, **não conferida**:
a atualização monetária trabalhista é nacional desde a **Res. CSJT 8/2005**, e **a aritmética do
manual do TRT-3 não é prática regional divergente**. Regional são **os verbetes que ele invoca**.

## Por que `cortes-e-bifurcacoes.md` é um arquivo separado

**É o arquivo que muda quando o Congresso ou o TST mexem na regra.** Os outros cinco mudam quando
muda a compreensão do manual — o que é muito mais raro. Manter as duas versões de cada ponto num
só lugar é o que impede o erro que o projeto inteiro existe para não cometer: **apagar a regra
antiga e destruir o cálculo de todo contrato pré-Reforma.**

---

## O que não entra em nenhum dos seis

- **Regra sem fundamento citado** — vira pendência declarada, nunca regra;
- **Correção monetária e juros** — `skills/calculo-judicial-atualizacao/`. Três das quinze regras
  regionais (`R10`, `R13`, `R15`) vivem lá; aparecem em `regras-regionais.md` **só para a contagem
  fechar**;
- **Séries de valores** — faixas de INSS e IRRF, índices mensais: dado **(B)**,
  `skills/indices-judiciais/`;
- **Invariantes e aritmética decimal** — `skills/calculo-judicial-core/`;
- **Harmonização de divergência.** Onde há duas correntes com fundamento próprio, **as duas
  entram**. Resolver seria inferir;
- **Nome de cliente, UF presumida, tribunal presumido ou polo processual presumido.**

---

## Limitação da própria divisão

**Os encargos processuais estão aqui provisoriamente.** As faixas de honorários são do **CPC art.
85, § 3º**, não da CLT, e valem nos três ramos — o `README.md` da skill já registrava a fronteira
como instável. **Mantidos por ora**, porque separá-los exigiria decidir onde ficam as custas de
execução, cuja base o corpus **define só por exclusão** (`P13B-01`, aberta).

## Estado

**Os seis arquivos estão escritos.** `SKILL.md` escrito no mesmo bloco.
