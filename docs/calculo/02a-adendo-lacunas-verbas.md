# Adendo à base normativa de verbas — lacunas fechadas

**Pesquisado 19/09/2026.** Fecha os seis pontos da seção 11 de `02-base-normativa-verbas.md`.
Anexar como seções 13 a 18 daquele documento, substituindo a seção 11.

---

## 13. OJ 394 da SDI-1 — REVERTIDA

**Este é o achado que mais muda a Fase 4, e corrige um erro do plano de extração.**

A OJ 394, vigente desde 2010, dizia que a majoração do repouso semanal remunerado decorrente da integração das horas extras habituais **não** repercutia no cálculo das férias, da gratificação natalina, do aviso prévio e do FGTS, sob pena de caracterização de *bis in idem*.

**Foi revertida.** No julgamento do IncJulgRREmbRep-10169-57.2013.5.05.0024 (**Tema Repetitivo 9**), o Tribunal Pleno do TST, Rel. Min. Amaury Rodrigues Pinto Junior, aprovou tese contrária, em **20/03/2023**. Nova redação:

> I — A majoração do valor do repouso semanal remunerado, decorrente da integração das horas extras habituais, deve repercutir no cálculo, efetuado pelo empregador, das demais parcelas que têm como base de cálculo o salário, não se cogitando de *bis in idem* por sua incidência no cálculo das férias, da gratificação natalina, do aviso prévio e do FGTS.
>
> II — O item I será aplicado às horas extras trabalhadas a partir de 20.03.2023.

### Consequências

**1. O caso difícil nº 6 da lista de validação da Fase 3 está errado e precisa ser reescrito.** Ele afirmava que o reflexo de HE no RSR não repercute em férias, 13º, aviso e FGTS. Isso deixou de valer para horas extras trabalhadas a partir de 20/03/2023.

Redação corrigida do caso difícil:

> A espinha registra que o reflexo do RSR majorado por horas extras habituais **não** repercute em férias, 13º, aviso e FGTS para horas extras trabalhadas até 19/03/2023 (OJ 394, redação de 2010), e **repercute** para horas extras trabalhadas a partir de 20/03/2023 (Tema Repetitivo 9)?

**2. É uma cadeia temporal, não uma regra fixa.** Entra em `tabelas-normativas/` com `tipo: cadeia-temporal`:

| Período da hora extra trabalhada | Reflexo do RSR majorado em férias, 13º, aviso e FGTS |
|---|---|
| Até 19/03/2023 | Não |
| A partir de 20/03/2023 | Sim |

**3. A modulação é pela data do trabalho, não pela data do ajuizamento nem do julgamento.** O corte é por competência da hora extra. Um mesmo processo, com período contratual atravessando 20/03/2023, tem os dois regimes.

**4. A tese menciona também as contribuições previdenciárias** como parcela alcançada, o que amplia o efeito para além das quatro verbas nomeadas no verbete.

---

## 14. Multas dos arts. 467 e 477 da CLT

### Art. 477, § 6º — alteração da Reforma

Redação original: o prazo tratava apenas do **pagamento** das parcelas constantes do instrumento de rescisão ou recibo de quitação.

Redação da Lei 13.467/2017: o prazo de dez dias contados do término do contrato passou a alcançar também **a entrega dos documentos** que comprovem a comunicação da extinção contratual aos órgãos competentes — guias de FGTS e seguro-desemprego, entre outros.

**Efeito prático:** a entrega tardia dos documentos, ainda que as verbas tenham sido pagas no prazo, enseja a multa do § 8º. O TST já decidiu nesse sentido, reconhecendo transcendência jurídica pela novidade da redação.

**A Súmula 48 do TRT-3 foi superada.** Ela dizia que a aplicação da multa do § 8º estava restrita à falta de pagamento das verbas no prazo do § 6º — interpretação restritiva construída sobre a redação antiga. Como o manual é do TRT-3, verificar se ele a invoca: se invocar, é item de Fase 4.

**Prazo unificado:** dez dias corridos para todas as modalidades de desligamento — sem justa causa, com justa causa, pedido de demissão, término de contrato determinado, aviso trabalhado ou indenizado. A Reforma eliminou a distinção de prazos que existia antes.

**Valor da multa em favor do empregado:** equivalente a um salário do empregado. A multa administrativa de 160 BTN por trabalhador é inexequível na prática, porque o BTN foi extinto.

**Excludente:** não se aplica quando comprovadamente o trabalhador der causa à mora. Exige prova documental.

### Teses vinculantes do TST

O TST editou precedentes vinculantes sobre as duas multas:

- **Tema 71** — a multa do art. 477, § 8º, é devida quando a justa causa é revertida em juízo: reconhece-se, nesse caso, a mora patronal.
- **Tema 139** — as multas dos arts. 467 e 477, § 8º, aplicam-se na hipótese de recuperação judicial, diversamente do que ocorre em caso de falência.

**Pendência:** o inteiro teor e a numeração completa dos temas vinculantes sobre as duas multas não foi obtido. As fontes indicam um conjunto maior de teses. Confirmar antes de implementar.

### Art. 467

Sanciona o empregador que não quita as **verbas rescisórias incontroversas** na primeira audiência. Gatilho e base distintos do art. 477: o 467 depende de disputa judicial e de incontrovérsia; o 477 depende só do decurso do prazo.

**Para o motor:** são duas verbas independentes, com condições de incidência diferentes. Não unificar.

---

## 15. Prescrição intercorrente — art. 11-A da CLT

Dispositivo incluído pela Lei 13.467/2017:

> Art. 11-A. Ocorre a prescrição intercorrente no processo do trabalho no prazo de dois anos.
> § 1º A fluência do prazo prescricional intercorrente inicia-se quando o exequente deixa de cumprir determinação judicial no curso da execução.
> § 2º A declaração da prescrição intercorrente pode ser requerida ou declarada de ofício em qualquer grau de jurisdição.

**Contexto anterior:** conflito entre a Súmula 327 do STF ("o direito trabalhista admite a prescrição intercorrente") e a Súmula 114 do TST ("é inaplicável na Justiça do Trabalho a prescrição intercorrente"). O art. 11-A positivou a primeira.

**Marco inicial — IN 41/2018 do TST, art. 2º:** o fluxo da prescrição intercorrente conta-se a partir do descumprimento da determinação judicial a que alude o § 1º do art. 11-A, **desde que a determinação tenha sido feita após 11/11/2017**.

Consequência: execução iniciada antes da Reforma, com intimação para atos executórios anterior a 11/11/2017, não sofre a prescrição intercorrente do art. 11-A. Há jurisprudência firme nesse sentido.

**Exigência procedimental:** a prescrição só deve ser reconhecida após **expressa intimação** do exequente para cumprimento de determinação judicial no curso da execução. Corregedoria-Geral da Justiça do Trabalho, Recomendação 03/GCGJT, de 24/07/2018.

**Critério material do TST:** trata-se da omissão reiterada do exequente que abandona de fato a execução por prazo superior a dois anos, deixando de praticar, por exclusiva omissão sua, atos que tornem fisicamente possível a continuidade. Não basta a demora.

**Alteração correlata — art. 878 da CLT:** a Reforma restringiu o impulso oficial. A execução passou a ser promovida pelas partes, permitida a execução de ofício pelo juiz apenas quando as partes não estiverem representadas por advogado. É o que torna a prescrição intercorrente operacional.

**Para o módulo:** é regra de liquidação e execução, não de apuração. Afeta o que pode ser cobrado, não como se calcula. Entra como marcador no processo, não no motor de verbas.

---

## 16. Súmulas 264 e 340 — ambas vigentes, sem alteração

Nenhuma das duas foi alterada pela Reforma nem posteriormente.

### Súmula 264 — base de cálculo da hora suplementar

A remuneração do serviço suplementar é composta do **valor da hora normal, integrado por parcelas de natureza salarial**, acrescido do adicional.

Define **o que entra** na base. Prêmios pagos com habitualidade e natureza salarial integram o cálculo das horas extras.

### Súmula 340 — comissionista

> O empregado, sujeito a controle de horário, remunerado à base de comissões, tem direito ao adicional de, no mínimo, 50% pelo trabalho em horas extras, calculado sobre o valor-hora das comissões recebidas no mês, considerando-se como divisor **o número de horas efetivamente trabalhadas**.

Define **como se apura o valor-hora** da parte variável, e usa divisor diferente — horas efetivamente trabalhadas, não 220.

**A distinção entre as duas é a que o bloco 04 havia perdido.** A 264 amplia o que entra na base; a 340 fixa o método de apuração da parte variável. Confirmado: são complementares, não alternativas.

### Verbetes correlatos

- **OJ 397 da SDI-1 — comissionista misto.** Remuneração com parte fixa e parte variável: sobre a **parte fixa**, horas simples acrescidas do adicional; sobre a **parte variável**, somente o adicional, aplicando-se a Súmula 340.
- **OJ 235 da SDI-1 — remuneração por produção.** O empregado remunerado por produção tem direito somente ao adicional de hora extra, porque a hora simples já está remunerada pela produção.

### Limite de aplicação da Súmula 340

O TST restringiu o alcance: a súmula pressupõe que a sobrejornada **aumente** o ganho variável. Os precedentes que a originaram tratam de vendedores. Em remuneração variável de valor fixo por unidade — motorista remunerado por carga, por exemplo — a hora extra não aumenta a remuneração e **não se aplica a Súmula 340**: a hora extra é devida de forma integral.

**Para o motor:** a aplicação da Súmula 340 depende de um atributo do vínculo — se a sobrejornada aumenta ou não o ganho variável. Não é derivável do tipo de remuneração isoladamente. É variante que o usuário seleciona.

### Divergência em liquidação, registrada

Há divergência sobre se os RSR sobre comissões integram a base de cálculo das horas extras variáveis quando o título determina a apuração pela Súmula 264. A Seção Especializada em Execução do TRT-4 tem entendimento majoritário de que os repousos decorrentes da remuneração variável **integram** a base. Ponto típico de impugnação de cálculo — registrar como variante.

---

## 17. Adicional de transferência

**Art. 469, § 3º, da CLT:** em caso de necessidade de serviço, o empregador pode transferir o empregado para localidade diversa da que resultar do contrato, ficando obrigado a pagamento suplementar **nunca inferior a 25% dos salários que o empregado percebia naquela localidade, enquanto durar essa situação**.

**Não alterado pela Reforma.**

### Requisitos cumulativos

1. **Mudança de domicílio.** Não se considera transferência a simples mudança do local da prestação de serviços sem alteração do domicílio (art. 469, *caput*).
2. **Provisoriedade.** **OJ 113 da SDI-1:** o adicional é devido desde que a transferência seja provisória. O fato de o empregado exercer cargo de confiança ou a existência de previsão contratual de transferência não exclui o direito — o pressuposto legal é a provisoriedade.
3. **Real necessidade de serviço.** A **Súmula 43 do TST** estendeu esse requisito a todo tipo de transferência, inclusive para cargo de confiança.

### Natureza e reflexos

**Salário-condição:** devido enquanto perdurar a transferência, cessando no retorno. Natureza salarial — integra férias, 13º e FGTS enquanto pago.

### Base de cálculo — divergência

O texto legal diz "salários que o empregado percebia naquela localidade". Há decisões calculando sobre o **salário-base** e decisões calculando sobre a **remuneração**, incluindo o TRT-3, que já decidiu pelo cálculo sobre a remuneração nos moldes do § 3º do art. 469.

**Registrar como variante**, não resolver.

### Divergência sobre transferência definitiva

A OJ 113 é o entendimento majoritário: só a transferência provisória gera o adicional. Mas há corrente minoritária sustentando que a provisoriedade do § 3º se refere ao **recebimento** do adicional — salário-condição — e não à natureza da transferência, de modo que a mudança definitiva de domicílio também geraria direito.

O TST reafirma a OJ 113; alguns TRTs resistem. Registrar como variante com o default na OJ 113.

**Ponto de prova relevante para o polo passivo:** há decisões condenando quando o empregador não produz prova da definitividade. O rótulo dado pela empresa não decide; a prova sim.

### Transferência definitiva

Ainda que não gere o adicional, a **Súmula 29 do TST** garante ao menos as despesas com transporte.

---

## 18. Parâmetros negociáveis acrescidos

Somar ao inventário da seção 10:

| Parâmetro | Default legal | Fonte |
|---|---|---|
| Adicional de transferência | 25% | CLT art. 469, § 3º — "nunca inferior", ACT pode elevar |
| Base do adicional de transferência | divergente: salário-base ou remuneração | CLT art. 469, § 3º |
| Adicional de HE do comissionista | 50% | Súmula 340 — "no mínimo", ACT pode elevar |

---

## 19. Pendências remanescentes

| # | Pendência | Tipo |
|---|---|---|
| 1 | Numeração e inteiro teor completos dos temas vinculantes do TST sobre as multas dos arts. 467 e 477 | Pesquisa |
| 2 | Verificar se o manual TRT-3 invoca a Súmula 48 do TRT-3 (multa do art. 477) | Extração |
| 3 | Verificar vigência da Súmula 46 do TRT-3 após a cassação da Súmula 228 do TST em 2018 | Pesquisa |
| 4 | Todas as pendências de dados da seção 12 — série de ACTs, mapa de categorias, IPs, eletricitários | Coleta do cliente |
