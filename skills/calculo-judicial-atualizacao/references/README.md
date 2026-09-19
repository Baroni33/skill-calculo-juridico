# references/ — variantes por jurisdição

**Fase do pipeline:** Fase 5.

## Propósito

Um arquivo por variante de cadeia. O agente carrega **apenas** o arquivo da
jurisdição em questão — essa é a razão de a pasta existir em vez de um único
documento grande.

## Arquivos previstos

| Arquivo | Cobre |
|---|---|
| `trabalhista-privado.md` | ADC 58/59 + Lei 14.905/2024; devedor privado |
| `trabalhista-fazenda.md` | ramo ressalvado pela ADC 58; IPCA-E até nov/2021, SELIC após |
| `civel-cc-tema1368.md` | STJ Tema 1368; SELIC até 29/08/2024, IPCA + taxa legal após |
| `civel-mg-cgj.md` | tabela CGJ/TJMG — só períodos pré-2003 e títulos que a fixaram |
| `tributario-federal.md` | repetição de indébito e dívida ativa |
| `previdenciario.md` | INPC e taxa legal com dedução do **INPC** |

## O que não entra

- Regra sem fundamento normativo citado.
- Cadeia que contradiga `docs/calculo/00-base-normativa.md`.

## Nota sobre `previdenciario.md`

A taxa legal previdenciária usa **INPC** como deflator, não IPCA-15. Mesma fórmula,
deflator diferente. Fonte: Manual CJF, Res. 990/2026, item 4.3.2, Nota 3. Os dois
pares de validação aritmética da seção 4 da base normativa são **deste caso**, não
do caso geral. Ver `docs/calculo/pendencias.md`.

## Estado

Vazio.
