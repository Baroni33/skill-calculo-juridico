"""Validador das invariantes R1 e R2 sobre conjuntos de segmentos.

R1 — Exclusividade de englobamento. Segmento cujo `engloba` cobre um componente
     não admite outro segmento do mesmo componente no mesmo intervalo. Vale para
     SELIC e taxa legal. Impede contar inflação duas vezes.

R2 — Cobertura sem lacuna nem sobreposição. A união dos segmentos cobre da parcela
     mais antiga até a data-base.

Fonte: docs/calculo/00-base-normativa.md, seção 7.

Aritmética em competências `YYYY-MM`. Nenhum float em caminho algum (R12).

Segmentos que diferem em `condicao` vivem em universos separados: as tabelas
normativas bifurcam por qualidade do devedor, data da sentença e data do fato
gerador. Comparar ramos distintos produziria falso positivo de sobreposição.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Iterable, Sequence

__all__ = [
    "Segmento",
    "Violacao",
    "competencia_para_indice",
    "indice_para_competencia",
    "valida_cobertura",
    "carrega_segmentos",
]


# --------------------------------------------------------------------------
# Aritmética de competência
# --------------------------------------------------------------------------

def competencia_para_indice(competencia: str) -> int:
    """Converte `YYYY-MM` em um índice inteiro de meses, para aritmética exata."""
    if not isinstance(competencia, str):
        raise TypeError(f"competência deve ser str 'YYYY-MM', veio {type(competencia).__name__}")
    partes = competencia.strip().split("-")
    if len(partes) != 2:
        raise ValueError(f"competência malformada: {competencia!r} (esperado 'YYYY-MM')")
    ano_txt, mes_txt = partes
    if len(ano_txt) != 4 or len(mes_txt) != 2 or not ano_txt.isdigit() or not mes_txt.isdigit():
        raise ValueError(f"competência malformada: {competencia!r} (esperado 'YYYY-MM')")
    ano, mes = int(ano_txt), int(mes_txt)
    if not 1 <= mes <= 12:
        raise ValueError(f"mês fora de 1..12 em {competencia!r}")
    return ano * 12 + (mes - 1)


def indice_para_competencia(indice: int) -> str:
    ano, mes = divmod(indice, 12)
    return f"{ano:04d}-{mes + 1:02d}"


# --------------------------------------------------------------------------
# Modelo
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Segmento:
    """Intervalo fechado [inicio, fim] em competências, para um componente."""

    inicio: str
    fim: str
    componente: str
    engloba: tuple[str, ...] = ()
    condicao: tuple[tuple[str, str], ...] = ()
    id: str = ""

    @staticmethod
    def de_dict(d: dict[str, Any], indice: int = 0) -> "Segmento":
        faltando = [c for c in ("inicio", "fim", "componente") if c not in d]
        if faltando:
            raise ValueError(f"segmento #{indice} sem campo(s) obrigatório(s): {', '.join(faltando)}")
        condicao = d.get("condicao") or {}
        if not isinstance(condicao, dict):
            raise ValueError(f"segmento #{indice}: 'condicao' deve ser objeto")
        seg = Segmento(
            inicio=d["inicio"],
            fim=d["fim"],
            componente=d["componente"],
            engloba=tuple(d.get("engloba") or ()),
            condicao=tuple(sorted((str(k), str(v)) for k, v in condicao.items())),
            id=str(d.get("id") or d.get("indexador") or f"segmento[{indice}]"),
        )
        if competencia_para_indice(seg.inicio) > competencia_para_indice(seg.fim):
            raise ValueError(f"{seg.id}: início {seg.inicio} posterior ao fim {seg.fim}")
        return seg

    def fornece(self, componente: str) -> bool:
        """Verdadeiro se o segmento entrega este componente, próprio ou englobado."""
        return self.componente == componente or componente in self.engloba

    def por_englobamento(self, componente: str) -> bool:
        """Verdadeiro se o segmento ENGLOBA este componente.

        Basta o componente constar de `engloba`. Não importa se coincide com o
        `componente` próprio do segmento: a SELIC declara-se como correção
        monetária E engloba correção e juros, e é justamente contra ela que R1
        precisa disparar quando outro segmento do mesmo componente concorre.
        """
        return componente in self.engloba

    @property
    def condicao_legivel(self) -> str:
        if not self.condicao:
            return "(sem condição)"
        return ", ".join(f"{k}={v}" for k, v in self.condicao)


@dataclass
class Violacao:
    regra: str
    componente: str
    condicao: str
    inicio: str
    fim: str
    segmentos: list[str]
    mensagem: str

    def __str__(self) -> str:
        janela = self.inicio if self.inicio == self.fim else f"{self.inicio}..{self.fim}"
        envolvidos = ", ".join(self.segmentos) if self.segmentos else "nenhum"
        return (
            f"[{self.regra}] {self.componente} | {self.condicao} | {janela}: "
            f"{self.mensagem} (segmentos: {envolvidos})"
        )


@dataclass
class Relatorio:
    violacoes: list[Violacao] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.violacoes

    def __bool__(self) -> bool:
        return self.ok

    def por_regra(self, regra: str) -> list[Violacao]:
        return [v for v in self.violacoes if v.regra == regra]

    def __str__(self) -> str:
        if self.ok:
            return "OK — cobertura íntegra, sem englobamento concorrente."
        return "\n".join(str(v) for v in self.violacoes)


# --------------------------------------------------------------------------
# Validação
# --------------------------------------------------------------------------

def _agrupa_intervalos(meses: Sequence[int]) -> list[tuple[int, int]]:
    """Colapsa meses consecutivos em intervalos, para relatório legível."""
    if not meses:
        return []
    ordenados = sorted(meses)
    faixas: list[tuple[int, int]] = []
    ini = ant = ordenados[0]
    for m in ordenados[1:]:
        if m == ant + 1:
            ant = m
            continue
        faixas.append((ini, ant))
        ini = ant = m
    faixas.append((ini, ant))
    return faixas


def valida_cobertura(
    segmentos: Iterable[Any],
    inicio: str | None = None,
    fim: str | None = None,
    componentes: Sequence[str] | None = None,
) -> Relatorio:
    """Verifica R1 e R2 sobre um conjunto de segmentos.

    `inicio`/`fim` delimitam a janela exigida — tipicamente da parcela mais antiga
    até a data-base. Omitidos, a janela é inferida da extensão dos próprios
    segmentos, o que ainda detecta lacunas internas mas não lacunas nas bordas.
    """
    normalizados: list[Segmento] = []
    for i, s in enumerate(segmentos):
        normalizados.append(s if isinstance(s, Segmento) else Segmento.de_dict(s, i))

    relatorio = Relatorio()
    if not normalizados:
        return relatorio

    if componentes is None:
        achados: list[str] = []
        for s in normalizados:
            for c in (s.componente, *s.engloba):
                if c not in achados:
                    achados.append(c)
        componentes = achados

    # Ramos com condição distinta não concorrem entre si.
    ramos: dict[tuple[tuple[str, str], ...], list[Segmento]] = {}
    for s in normalizados:
        ramos.setdefault(s.condicao, []).append(s)

    for condicao, do_ramo in ramos.items():
        condicao_txt = do_ramo[0].condicao_legivel
        for componente in componentes:
            provedores = [s for s in do_ramo if s.fornece(componente)]
            if not provedores:
                continue

            jan_ini = competencia_para_indice(inicio) if inicio else min(
                competencia_para_indice(s.inicio) for s in provedores
            )
            jan_fim = competencia_para_indice(fim) if fim else max(
                competencia_para_indice(s.fim) for s in provedores
            )

            lacunas: list[int] = []
            sobreposicoes: dict[tuple[str, ...], list[int]] = {}
            englobamentos: dict[tuple[str, ...], list[int]] = {}

            for mes in range(jan_ini, jan_fim + 1):
                ativos = [
                    s for s in provedores
                    if competencia_para_indice(s.inicio) <= mes <= competencia_para_indice(s.fim)
                ]
                if not ativos:
                    lacunas.append(mes)
                elif len(ativos) > 1:
                    chave = tuple(sorted(s.id for s in ativos))
                    if any(s.por_englobamento(componente) for s in ativos):
                        englobamentos.setdefault(chave, []).append(mes)
                    else:
                        sobreposicoes.setdefault(chave, []).append(mes)

            for ini, fim_ in _agrupa_intervalos(lacunas):
                relatorio.violacoes.append(Violacao(
                    regra="R2",
                    componente=componente,
                    condicao=condicao_txt,
                    inicio=indice_para_competencia(ini),
                    fim=indice_para_competencia(fim_),
                    segmentos=[],
                    mensagem="lacuna de cobertura — nenhum segmento fornece o componente",
                ))

            for chave, meses in sobreposicoes.items():
                for ini, fim_ in _agrupa_intervalos(meses):
                    relatorio.violacoes.append(Violacao(
                        regra="R2",
                        componente=componente,
                        condicao=condicao_txt,
                        inicio=indice_para_competencia(ini),
                        fim=indice_para_competencia(fim_),
                        segmentos=list(chave),
                        mensagem="sobreposição — mais de um segmento fornece o componente",
                    ))

            for chave, meses in englobamentos.items():
                for ini, fim_ in _agrupa_intervalos(meses):
                    relatorio.violacoes.append(Violacao(
                        regra="R1",
                        componente=componente,
                        condicao=condicao_txt,
                        inicio=indice_para_competencia(ini),
                        fim=indice_para_competencia(fim_),
                        segmentos=list(chave),
                        mensagem=(
                            "englobamento concorrente — segmento que engloba o componente "
                            "coexiste com outro que o fornece"
                        ),
                    ))

    relatorio.violacoes.sort(key=lambda v: (v.componente, v.condicao, v.inicio, v.regra))
    return relatorio


def carrega_segmentos(caminho: str) -> list[Segmento]:
    """Lê segmentos de uma tabela normativa em JSON.

    `encoding='utf-8'` explícito: Windows assume cp1252 e corrompe acentuação
    silenciosamente.
    """
    with open(caminho, "r", encoding="utf-8") as fh:
        dados = json.load(fh)
    brutos = dados.get("segmentos", dados) if isinstance(dados, dict) else dados
    return [Segmento.de_dict(s, i) for i, s in enumerate(brutos)]


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Valida R1 e R2 de uma tabela normativa.")
    parser.add_argument("tabela", help="caminho do JSON da tabela normativa")
    parser.add_argument("--inicio", help="competência inicial exigida (YYYY-MM)")
    parser.add_argument("--fim", help="competência final exigida (YYYY-MM), tipicamente a data-base")
    args = parser.parse_args(argv)

    relatorio = valida_cobertura(carrega_segmentos(args.tabela), args.inicio, args.fim)
    print(relatorio)
    return 0 if relatorio.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
