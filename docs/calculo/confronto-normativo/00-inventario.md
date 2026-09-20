# Inventário das marcações de Fase 4

**Tarefa 1 do bloco 14.** A lista completa **antes** de julgar qualquer ponto — porque quem
julga enquanto inventaria para de procurar.

Varredura de `docs/calculo/` inteira por `status_norma`, `marcar para Fase 4`, `superado`,
`confrontar`, `posterior ao manual`, marcas `F*`, e os campos `situacao` do índice de
jurisprudência.

---

## 1. O total, e o buraco

| | Marcas |
|---|---|
| **Anunciado nos relatórios** | **28** |
| **Encontrado na varredura** | **45** |
| **Nunca contadas** | **17** |

**Nenhum documento do projeto jamais declarou um total.** O que existe são contagens parciais,
corretas quando escritas e nunca somadas:

- `pendencias.md` § 19.1 e `presets-regime.md` § 8.1 — *"**Dezesseis** marcas de Fase 4 — nove
  em `bloco-03-verbas.md` § 8, sete em `bloco-04-verbas2.md` § 12"*;
- `bloco-06-relatorio.md`, achado E1 — *"15 pontos do corpus e **16** marcas de Fase 4"*;
- `bloco-07-relatorio.md` — *"Marcas Fase 4 | **Feitas** — 12 marcas"*.

`16 + 12 = 28`. **As outras 17 entraram no corpus em formatos que nenhuma contagem varreu** —
`status_norma` dentro de JSON de cadeia, campo `situacao` do índice de jurisprudência, e
marcações em prosa nos blocos 11 e 13.

**É o mesmo tipo de buraco que o mapa de cobertura pegou na extração:** não é que alguém tenha
deixado de marcar — é que **ninguém somou**.

---

## 2. Colisão de identificadores — achado estrutural

> **`F1` a `F9` existem no bloco 03 e `F1` a `F7` existem no bloco 04. São pontos diferentes
> com os mesmos rótulos.**

E `presets-regime.md` os referencia **sem qualificar o bloco** — cita "F1, F6, F7, F9" em
contexto onde os dois conjuntos são plausíveis.

Exemplo do dano: **`F6` do bloco 03** são *gorjetas*, da **Lei 13.419/2017**; **`F6` do bloco
04** é o *art. 384 da CLT*, revogado pela **Lei 13.467/2017**. Normas diferentes, anos
diferentes, verbas diferentes.

**Neste confronto os IDs passam a ser `B03-F1`…`B03-F9` e `B04-F1`…`B04-F7`.** A renumeração é
do inventário, não dos arquivos de origem — corrigir os arquivos é tarefa do bloco 15.

---

## 3. O inventário

### 3.1 Bloco 03 — verbas, itens 6.1 a 6.6 (9 marcas)

Origem: `extracao/trabalhista/bloco-03-verbas.md` § 8.

| ID | Ponto | Item, `pagina_pdf` | Dispositivo apontado |
|---|---|---|---|
| **B03-F1** | Base de cálculo integra **abonos e prêmios habituais** | 6.1 p. 18; 6.6.6.5 p. 47 | CLT art. 457, §§ 1º e 2º |
| **B03-F2** | **Habitualidade** como teste de integração, com lapso até anual | 6.1, p. 18 | CLT art. 457, § 2º |
| **B03-F3** | **12×36**: feriado laborado pago em dobro, **dois critérios divergentes** | 6.5, pp. 34–35 | CLT art. 59-A, parágrafo único |
| **B03-F4** | **Súmula 85** e compensação de jornada | 6.6.1 p. 36; 6.6.5 p. 40 | CLT art. 59-B — introduzido |
| **B03-F5** | **Minutos residuais** e Súmula 366 | 6.6.5, p. 40 | CLT art. 58, § 1º; art. 4º, § 2º |
| **B03-F6** | **Gorjetas** — Súmula 354 e a vedação de reflexos | 6.6.6.5, p. 48 | CLT art. 457, § 3º — **Lei 13.419/2017** |
| **B03-F7** | **Férias**: regime de concessão e período único | 6.4, pp. 25–27 | CLT art. 134, § 1º |
| **B03-F8** | **Prescrição na supressão de HE** | 6.6.8, p. 53 | CLT art. 11, § 2º — introduzido |
| **B03-F9** | **Tempo parcial**: tabela do art. 130-A | 6.4, p. 30 | CLT arts. 58-A e 130-A |

### 3.2 Bloco 04 — verbas, itens 6.7 a 6.15 (7 marcas)

Origem: `extracao/trabalhista/bloco-04-verbas2.md` § 12.

| ID | Ponto | Item, `pagina_pdf` | Dispositivo apontado |
|---|---|---|---|
| **B04-F1** | **Horas *in itinere*** — item inteiro | 6.7, p. 55 | CLT art. 58, § 2º — **suprimido** |
| **B04-F2** | **Intervalo intrajornada suprimido** — integral, como HE, natureza salarial | 6.10.1, p. 56 | CLT art. 71, § 4º — **duas** alterações |
| **B04-F3** | Base do **seguro-desemprego** pelo art. 457, com prêmios e *in natura* | 6.13.4 | CLT art. 457 |
| **B04-F4** | **Comissões** pela média dos últimos doze meses | 6.12, p. 65 | CLT art. 457, § 1º |
| **B04-F5** | **Adicional noturno em 12×36** — OJ 388 | 6.11.4, p. 62 | CLT art. 59-A — introduzido |
| **B04-F6** | **Súmula 39 do TRT-3** e o art. 384 — 15 min para mulheres | 6.10.1, p. 57 | CLT art. 384 — **revogado** |
| **B04-F7** | **Prescrição do FGTS** e a Súmula 362 | 6.14, p. 79 | CLT art. 11, § 2º — introduzido |

### 3.3 Bloco 07 — descontos, capítulo 9 (12 marcas)

Origem: `extracao/trabalhista/bloco-07-descontos.md` § 13.

| ID | Ponto | `pagina_pdf` | Norma apontada |
|---|---|---|---|
| **F7-01** | Alíquota **única** sobre o total (cota do segurado) | 130, 158 | EC 103/2019 |
| **F7-02** | **Desoneração da folha**, item 9.2.10 inteiro | 176 | Leis 13.670/2018, 14.784/2023, **14.973/2024** |
| **F7-03** | **Juros de mora na base do IR** — "a questão não está resolvida" | 181 | Tema 808 do STF (RE 855091) |
| **F7-04** | "atualmente a TR" como índice do débito trabalhista | 129 | ADC 58/59 e ADIs 5867/6021 |
| **F7-05** | Base = "parcelas de natureza salarial" | 128 | Lei 13.467/2017 |
| **F7-06** | Acordo homologado **sem** o rito de jurisdição voluntária | 153–154, 201 | Lei 13.467/2017, arts. 855-B a 855-E |
| **F7-07** | **RIR/99** (Dec. 3000/99) em todo o item 9.3 | 180, 186, 207 | Dec. 9.580/2018 |
| **F7-08** | **IN/RFB 1500/14** com alterações da 1558/15 | 187–208 | INs posteriores |
| **F7-09** | Tabelas de IRRF e salário-de-contribuição **congeladas em abr/2015** | anexos | Portarias e leis posteriores |
| **F7-10** | Códigos 2909, 1708, 1889, 5936 e a GPS | 153, 196, 207 | eSocial, DCTFWeb, EFD-Reinf |
| **F7-11** | **Súmula 45 do TRT-3**, editada em ago/2015 | 117 | Confirmar redação e vigência |
| **F7-12** | **PLR** — Lei 10.101/00 na redação da 12.832/13 | 199 | Lei 14.020/2020 |

### 3.4 As 17 que nunca foram contadas

**Cinco `status_norma` em cadeias temporais** — `tabelas-normativas/trab.hist.*.json`:

| ID | Cadeia, segmento | `substituido_por` |
|---|---|---|
| **CH-01** | `trabalhista.correcao-monetaria` 1942-11..2009-06 | ADC 58, EC 113/2021 art. 3º, Lei 14.905/2024 |
| **CH-02** | `trabalhista.correcao-monetaria` 2009-07..2016-05 (não-Fazenda) | idem |
| **CH-03** | `trabalhista.correcao-monetaria` 2009-07..2016-05 (Fazenda) | idem |
| **CH-04** | `trabalhista.juros-mora` 1991-04..2016-05 | ADC 58 e 59, EC 113/2021, Lei 14.905/2024, EC 136/2025 |
| **CH-05** | `fazenda-publica.juros-mora` 2009-07..2016-05 | EC 113/2021, art. 3º — Selic única |

*(O `episodio_ipca_e` também carrega `status_norma`, mas é registro histórico, não regra
aplicável — não entra na contagem.)*

**Seis verbetes do índice de jurisprudência** — `jurisprudencia-indice.md`, campo `situacao`:

| ID | Verbete | Situação registrada |
|---|---|---|
| **JR-01** | Súmula 124 do TST | alterado — Res. 219/2017 |
| **JR-02** | Súmula 437 do TST | alterado — item III superado pelo art. 71, § 4º |
| **JR-03** | Súmula 90 do TST | alterado — art. 58, § 2º revogado em 11/11/2017 |
| **JR-04** | OJ 394 da SDI-1 | **superado** — Tema Repetitivo 9 |
| **JR-05** | OJ 300 da SDI-1 | **superado** — valida a TRD, que a ADC 58 declarou inconstitucional |
| **JR-06** | Súmula 228 do TST | **cancelado** — Rcl 6.275, abril/2018 |

**Três marcações de segmento nos blocos 11** — em prosa, nunca inventariadas:

| ID | Onde | Ponto |
|---|---|---|
| **AM-01** | `bloco-11a-imputacao.md` § 10 | Todo o item 10.1 pressupõe o critério pré-ADC 58 — marcação **geral** |
| **AM-02** | `bloco-11b-amortizacao.md` § 9 | O rateio distribui o pagamento entre juros por TR + 1% — **resolvido no bloco 12** como conflito condicional |
| **AM-03** | `bloco-11c-vincendos.md` § 9 | Sob Selic pós-citação a distinção principal/juros **perde objeto** |

**Três marcações do bloco 13:**

| ID | Onde | Ponto |
|---|---|---|
| **B13-01** | `bloco-13b-encargos.md` § 5 | Honorários sucumbenciais — **art. 791-A da CLT** |
| **B13-02** | `bloco-13c-sindical-precatorios.md` § 2 | Contribuição sindical **facultativa** desde a Reforma |
| **B13-03** | `bloco-13c-sindical-precatorios.md` § 4 | Precatórios — **EC 113/2021 e EC 136/2025** |

---

## 4. Sobre a numeração das fases

`01-plano-extracao.md` chama **esta** etapa de "Fase 4" e a consolidação de "Fase 3". **A ordem
está invertida no documento:** o confronto vem antes.

**Registrado, não corrigido** — a correção é do bloco 15, conforme o enunciado.

---

## 5. O que o inventário já decide

**Dois pontos estão fora do escopo de veredito antes de qualquer pesquisa:**

- **AM-02** foi **resolvido no bloco 12**: o conflito entre o rateio e a modulação é
  **condicional**, não estrutural, e virou o preset `pr.adc58-item-i`. Entra no inventário
  para rastreabilidade, com veredito já dado;
- **JR-05** (OJ 300) é **consequência** de F7-04, não ponto autônomo: a OJ valida a TRD do art.
  39 da Lei 8.177/91, que a ADC 58 declarou inconstitucional. Julgar as duas separadamente
  produziria vereditos redundantes.

Os demais **43** vão a veredito em `01-vereditos.md`.
