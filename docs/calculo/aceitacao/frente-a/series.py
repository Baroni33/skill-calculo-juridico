# -*- coding: utf-8 -*-
"""Camada (B) — series de valores mensais.

A skill `indices-judiciais` e explicita: "esta skill NAO carrega serie — e o
ponto inteiro dela". Os CSV de docs/calculo/extracao/trabalhista/ abrem com o
cabecalho "# OUT_OF_SCOPE — serie de valores, nao entra na skill" e existem
"como evidencia de conferencia, NAO como fonte de consulta".

Consequencia: este provedor nasce QUASE VAZIO. So entram aqui valores que uma
skill (ou a propria fixture) declarou LITERALMENTE, com a fonte ao lado.
Nada e interpolado, nada e deduzido, nada vem da web.

Pedir uma competencia ausente levanta SerieAusente — e isso e resultado, nao
defeito.
"""

from decimal import Decimal
from aritmetica import D


class SerieAusente(Exception):
    """A competencia pedida nao existe em fonte alguma lida por este motor."""

    def __init__(self, indexador, competencia, procurado_em):
        self.indexador = indexador
        self.competencia = competencia
        self.procurado_em = procurado_em
        super().__init__(
            "serie ausente: %s de %s — procurado em: %s"
            % (indexador, competencia, "; ".join(procurado_em))
        )


# Onde se procurou antes de concluir que o valor nao existe. Escopo declarado.
ESCOPO_DE_BUSCA = [
    "skills/calculo-judicial-core/SKILL.md",
    "skills/calculo-judicial-atualizacao/SKILL.md + os 10 references/",
    "skills/indices-judiciais/SKILL.md + references/catalogo-de-indices.md",
    "skills/calculo-trabalhista-liquidacao/SKILL.md + references/",
    "docs/calculo/tabelas-normativas/*.json (ponteiro declarado das skills)",
    "docs/calculo/00-base-normativa.md (ponteiro declarado das skills)",
    "tests/fixtures/calculo/*.json",
]


# ---------------------------------------------------------------------------
# Os UNICOS valores de indice com fonte literal no escopo lido.
# Cada um traz (valor_percentual_str, fonte).
# ---------------------------------------------------------------------------
VALORES_LITERAIS = {
    ("IPCA-E/IBGE", "2021-11"): (
        "1.17",
        "Manual CJF 4.2.1, NOTA 5, pagina_pdf 50 — via references/civel-federal.md S7 "
        "e tributario-federal.md S8; repetido na propria fixture",
    ),
    ("INPC/IBGE", "2021-11"): (
        "0.84",
        "Manual CJF 4.3.1, NOTA 5, pagina_pdf 59 — via references/tributario-federal.md S8",
    ),
    ("TR", "2021-11"): (
        "0.00",
        "Manual CJF 4.7.2, NOTA 2, pagina_pdf 79 — via references/tributario-federal.md S8",
    ),
    ("SELIC", "2025-08"): (
        "1.16",
        "references/civel-federal.md S3 — 'a Selic de ago/2025 (1,16%) e computada em set/2025'",
    ),
    ("TAXA-LEGAL", "2025-09"): (
        "1.305984",
        "references/civel-federal.md S3 — 'a taxa legal de set/2025 (1,305984%) e computada em out/2025'",
    ),
}

# Juros de dez/2021 da consolidacao: valor unico nos cinco ramos (R-08-12).
JUROS_DEZ_2021_PCT = D("0.4412")

# Pares publicados da taxa legal — fixture de aceite 1 da skill indices-judiciais.
# Variante INPC (deflator INPC), pendencias.md SS 2 e 3.
PARES_TAXA_LEGAL_INPC = [
    # (competencia, fator_selic_m, fator_deflator_m-1, taxa_legal_esperada)
    ("2025-09", "1.01164156", "0.9979", "1.377047"),
    ("2026-05", "1.01090058", "1.0081", "0.277807"),
]


def indice_mensal(indexador, competencia):
    """Valor percentual do indexador na competencia. Levanta SerieAusente."""
    chave = (indexador, competencia)
    if chave in VALORES_LITERAIS:
        return D(VALORES_LITERAIS[chave][0])
    raise SerieAusente(indexador, competencia, ESCOPO_DE_BUSCA)


def fonte_do_valor(indexador, competencia):
    return VALORES_LITERAIS[(indexador, competencia)][1]


def cobertura(indexador):
    """R2/contrato de serie: cobertura e DERIVADA, nao metadado."""
    comps = sorted(c for (i, c) in VALORES_LITERAIS if i == indexador)
    return (comps[0], comps[-1]) if comps else None
