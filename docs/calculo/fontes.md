# Fontes — corpus primário

Os dois manuais em PDF **permanecem fora deste repositório**, no diretório de trabalho
do SaaS jurídico. Referência por caminho absoluto. Nenhum PDF é versionado aqui.

`00-base-normativa.md` prevalece sobre ambos sempre que houver conflito: os manuais
têm datas de corte diferentes e o trabalhista está materialmente defasado.

## Manual de Cálculos da Justiça do Trabalho — TRT-3

| Campo | Valor |
|---|---|
| Caminho | `C:\Users\Rafaela\Downloads\Plataforma-SaaS-Jus\manual-de-calculo-trabalhista_2016-1.pdf` |
| Emissor | TRT-3, Secretaria de Cálculos Judiciais |
| Data | julho/2016 |
| Páginas (PDF) | 471 |
| Camada de texto | extraível, UTF-8 |
| **Offset de paginação** | **0** |

A página 1 do PDF traz o rótulo impresso "1". Verificado em p.1, p.48 e p.471 —
`pagina_pdf` e número impresso coincidem em todo o documento.

## Manual de Orientação de Procedimentos para os Cálculos na Justiça Federal — CJF

| Campo | Valor |
|---|---|
| Caminho | `C:\Users\Rafaela\Downloads\Plataforma-SaaS-Jus\manual_de_calculos_2026.pdf` |
| Emissor | Conselho da Justiça Federal |
| Norma | Resolução CJF n. 990/2026 |
| Páginas (PDF) | 93 |
| Camada de texto | extraível, UTF-8 |
| **Offset de paginação** | **1** |

A página 1 do PDF é folha em branco (zero caracteres extraídos). A página 2 do PDF
traz o rótulo impresso "1". Relação constante:

```
numero_impresso = pagina_pdf - 1
```

Verificado em p.2 → "1", p.20 → "19", p.93 → "92". O offset é constante do início ao
fim, não apenas na abertura.

## Regra de proveniência

A triagem do corpus em `01-plano-extracao.md` usa **índice de PDF**, não numeração
impressa. Toda extração grava `documento`, `pagina_pdf` e item numerado
(regra 3 das "Regras de trabalho para os agentes").

Grave sempre `pagina_pdf`. Onde o número impresso for útil ao leitor humano, grave-o
como campo adicional — nunca no lugar de `pagina_pdf`.

## Extração

`pdftotext` não está instalado no ambiente de referência; a extração foi feita com
`pdf-tool`. A saída em disco é UTF-8 válida.

Toda leitura de arquivo declara `encoding='utf-8'` explicitamente. Windows assume
cp1252 e corrompe acentuação silenciosamente. A mojibake observada em terminal é
renderização do console, não corrupção do arquivo — não "corrija" o arquivo por causa
dela.
