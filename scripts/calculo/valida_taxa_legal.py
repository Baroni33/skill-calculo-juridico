"""Taxa legal — razão entre fatores, nunca subtração de percentuais.

    TL_m = (Fator_Selic_m / Fator_Deflator_{m-1} - 1) × 100

Fonte: Resolução CMN n. 5.171, de 29/08/2024, que regulamenta o art. 406 do CC na
redação da Lei 14.905/2024. Ver docs/calculo/00-base-normativa.md, seção 4.

Três pontos em que implementações erram, todos cobertos aqui:

R11 — A lei e o acórdão do TST descrevem "SELIC deduzido o IPCA". Isso é descrição
      do EFEITO. A operação é RAZÃO entre fatores. A subtração literal produz número
      errado, com divergência de ~0,003 p.p./mês, que acumula.

R12 — Aritmética decimal. Nenhum float. O resultado é TRUNCADO a seis decimais, não
      arredondado: os dois pares de validação do Manual CJF só fecham com
      truncamento (half-up erra o último dígito em ambos).

R6  — Piso zero. Resultado negativo vira zero no mês de referência
      (CC art. 406, § 3º), nunca negativo.

O deflator é PARÂMETRO, não constante:
  - IPCA-15 → regra geral (Res. CMN 5.171)
  - INPC    → variante previdenciária (Manual CJF, Res. 990/2026, item 4.3.2, Nota 3)

Os dois pares de validação da seção 4 da base normativa são do caso INPC. O caso
IPCA-15 está sem par de validação publicado — ver docs/calculo/pendencias.md.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_DOWN, localcontext
from enum import Enum
from typing import Any, Sequence

__all__ = [
    "Deflator",
    "SEIS_DECIMAIS",
    "taxa_legal",
    "taxa_legal_por_subtracao",
    "PARES_VALIDACAO_INPC",
    "verifica_pares_validacao",
    "carrega_fatores",
]

SEIS_DECIMAIS = Decimal("0.000001")

# Precisão interna folgada: a divisão precisa de muito mais dígitos do que os seis
# que sobrevivem ao truncamento, sob pena de o último dígito virar ruído.
_PRECISAO_INTERNA = 40


class Deflator(str, Enum):
    """Índice deduzido na razão. Muda por ramo, não por preferência."""

    IPCA15 = "IPCA-15"
    INPC = "INPC"

    @property
    def fundamento(self) -> str:
        return {
            Deflator.IPCA15: "Res. CMN 5.171/2024 — regra geral",
            Deflator.INPC: "Manual CJF, Res. 990/2026, item 4.3.2, Nota 3 — previdenciário",
        }[self]


def _para_decimal(valor: Any, nome: str) -> Decimal:
    """Converte para Decimal recusando float explicitamente (R12).

    `float` é recusado em vez de convertido: aceitá-lo silenciosamente já teria
    perdido precisão antes da chamada, e o erro ficaria invisível.
    """
    if isinstance(valor, float):
        raise TypeError(
            f"{nome}: float é proibido (R12 — aritmética decimal). "
            f"Use Decimal('{valor!r}') ou a string do valor."
        )
    if isinstance(valor, Decimal):
        return valor
    if isinstance(valor, (int, str)):
        return Decimal(valor)
    raise TypeError(f"{nome}: esperado Decimal, int ou str; veio {type(valor).__name__}")


def taxa_legal(
    fator_selic: Any,
    fator_deflator: Any,
    deflator: Deflator = Deflator.IPCA15,
) -> Decimal:
    """Taxa legal do mês, em pontos percentuais, truncada a seis decimais.

    `fator_deflator` é o fator do MÊS ANTERIOR ao de referência.
    Retorna Decimal com exatamente seis casas; nunca negativo.
    """
    selic = _para_decimal(fator_selic, "fator_selic")
    defl = _para_decimal(fator_deflator, "fator_deflator")

    if defl <= 0:
        raise ValueError(f"fator do deflator ({deflator.value}) deve ser positivo, veio {defl}")
    if selic <= 0:
        raise ValueError(f"fator da Selic deve ser positivo, veio {selic}")

    with localcontext() as ctx:
        ctx.prec = _PRECISAO_INTERNA
        exato = (selic / defl - 1) * 100

    if exato <= 0:
        return Decimal("0").quantize(SEIS_DECIMAIS)  # R6 — piso zero

    return exato.quantize(SEIS_DECIMAIS, rounding=ROUND_DOWN)  # R12 — truncamento


def taxa_legal_por_subtracao(fator_selic: Any, fator_deflator: Any) -> Decimal:
    """Implementação ERRADA, preservada para os testes negativos.

    Reproduz a subtração literal de percentuais que R11 proíbe. Existe para que a
    suíte demonstre a divergência, não para ser chamada em produção.
    """
    selic = _para_decimal(fator_selic, "fator_selic")
    defl = _para_decimal(fator_deflator, "fator_deflator")
    with localcontext() as ctx:
        ctx.prec = _PRECISAO_INTERNA
        return ((selic - defl) * 100).quantize(SEIS_DECIMAIS, rounding=ROUND_DOWN)


# --------------------------------------------------------------------------
# Pares de validação — seção 4 da base normativa
# --------------------------------------------------------------------------
#
# Conferidos contra a tabela de taxa legal PREVIDENCIÁRIA do Manual CJF
# (Res. 990/2026). Deflator: INPC.

PARES_VALIDACAO_INPC: tuple[dict[str, Any], ...] = (
    {
        "competencia": "2025-09",
        "rotulo": "Set/2025",
        "fator_selic": Decimal("1.01164156"),
        "fator_deflator": Decimal("0.9979"),
        "esperado": Decimal("1.377047"),
        "subtracao_erronea": Decimal("1.374156"),
    },
    {
        "competencia": "2026-05",
        "rotulo": "Mai/2026",
        "fator_selic": Decimal("1.01090058"),
        "fator_deflator": Decimal("1.0081"),
        "esperado": Decimal("0.277807"),
        "subtracao_erronea": Decimal("0.280058"),
    },
)


def verifica_pares_validacao() -> list[str]:
    """Roda os pares publicados. Retorna lista de falhas; vazia = tudo certo."""
    falhas: list[str] = []
    for par in PARES_VALIDACAO_INPC:
        obtido = taxa_legal(par["fator_selic"], par["fator_deflator"], Deflator.INPC)
        if obtido != par["esperado"]:
            falhas.append(
                f"{par['rotulo']}: esperado {par['esperado']}%, obtido {obtido}%"
            )
    return falhas


def carrega_fatores(caminho: str) -> list[dict[str, Any]]:
    """Lê fatores mensais de um JSON, com `encoding='utf-8'` explícito.

    Windows assume cp1252 e corrompe acentuação silenciosamente.
    Valores numéricos são lidos como str e convertidos em Decimal — `json.load`
    produziria float, proibido por R12.
    """
    with open(caminho, "r", encoding="utf-8") as fh:
        dados = json.load(fh, parse_float=Decimal)
    registros = dados.get("fatores", dados) if isinstance(dados, dict) else dados
    return list(registros)


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Calcula a taxa legal e/ou roda os pares de validação publicados."
    )
    parser.add_argument("--selic", help="fator da Selic do mês de referência")
    parser.add_argument("--deflator", help="fator do deflator do mês ANTERIOR")
    parser.add_argument(
        "--indice",
        choices=[d.value for d in Deflator],
        default=Deflator.IPCA15.value,
        help="índice deduzido (padrão: IPCA-15)",
    )
    parser.add_argument(
        "--validar", action="store_true", help="roda os pares de validação (INPC)"
    )
    args = parser.parse_args(argv)

    if args.validar:
        falhas = verifica_pares_validacao()
        if falhas:
            for f in falhas:
                print(f"FALHA {f}")
            return 1
        for par in PARES_VALIDACAO_INPC:
            print(f"OK {par['rotulo']}: {par['esperado']}% (deflator INPC)")
        return 0

    if not args.selic or not args.deflator:
        parser.error("informe --selic e --deflator, ou use --validar")

    resultado = taxa_legal(args.selic, args.deflator, Deflator(args.indice))
    print(f"{resultado}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
