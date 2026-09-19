# Confronto normativo

**Fase do pipeline:** Fase 4. **Só trabalhista.**

## Propósito

Cada regra extraída do manual do TRT-3 (2016) é confrontada com
`../00-base-normativa.md` e marcada como **vigente**, **superada** ou **alterada**.

Sem esta fase, a validação adversarial confirma fidelidade ao manual de 2016 e o
motor produz valores errados com aparência de fundamentação. Esse é o risco que
esta pasta existe para eliminar.

## Escopo

Capítulos do manual trabalhista que **não servem como fonte normativa**:

| Cap. | Assunto | Por quê |
|---|---|---|
| 7 | Atualização monetária e juros | ADC 58, EC 113/2021, Lei 14.905/2024 |
| 8 (parte) | Honorários sucumbenciais | Reforma Trabalhista (Lei 13.467/2017) |
| 9 (parte) | Descontos — faixas | faixas de INSS/IRRF superadas |
| 10 | Atualização de débitos | mesmo eixo do cap. 7 |
| 12 | Contribuição sindical | Reforma tornou facultativa |
| 14 | Precatórios | EC 113/2021 e EC 136/2025 |

## O que entra

Um registro por regra, com: texto original, `pagina_pdf`, veredito
(vigente/superada/alterada), norma que a superou, e a regra vigente correspondente
em `00-base-normativa.md`.

## O que não entra

- Veredito sem fundamento normativo citado.
- **Resolução de divergência.** Onde tribunais divergem, ambas as correntes viram
  preset com fundamento (regra 6 do plano). Divergência não se resolve, se registra.

## Estado

Vazio. Depende da Fase 2 do bloco trabalhista.
