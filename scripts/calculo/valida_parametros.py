"""Camada de resolução de parâmetros negociáveis por norma coletiva.

Resolve a tripla `(parametro, categoria, competencia)` num valor com proveniência.

Invariantes sustentadas, todas verificadas em `test_valida_parametros.py`:

  R14 — Ausência de norma coletiva cadastrada NÃO é erro. É fallback para o default
        legal, com a conta marcada `sem-cobertura-coletiva` naquele parâmetro.
  R15 — Toda resolução devolve proveniência, inclusive quando a origem é o default.
  R16 — Precedência: título judicial > norma coletiva > escolha do usuário > default.
        Divergência entre níveis é registrada, nunca silenciada.
  R17 — Norma coletiva é atributo do contrato: a chave usa categoria e competência,
        não processo nem empresa.
  R18 — Parâmetro com piso legal rejeita valor negociado inferior. Rejeita e reporta;
        não corrige para o piso.

Contrato completo em `docs/calculo/tabelas-normativas/camada-norma-coletiva-schema.json`.
Catálogo em `camada-norma-coletiva-catalogo.json`.

Aritmética decimal, nenhum float (R12). `encoding='utf-8'` explícito em toda leitura.

Uso:
    python valida_parametros.py --catalogo-ok
    python valida_parametros.py pn.he.adicional alfa-producao 2025-06 <instrumentos.json>
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Iterable

RAIZ = Path(__file__).resolve().parents[2]
CATALOGO_PADRAO = RAIZ / "docs" / "calculo" / "tabelas-normativas" / "camada-norma-coletiva-catalogo.json"

__all__ = [
    "Catalogo",
    "Instrumentos",
    "Resolucao",
    "ErroDeDados",
    "competencia_para_indice",
    "resolve",
]


class ErroDeDados(Exception):
    """Defeito no cadastro — não é ausência de cobertura, é dado malformado."""


# --------------------------------------------------------------------------
# Competência
# --------------------------------------------------------------------------

_RE_COMPETENCIA = re.compile(r"^(\d{4})-(\d{2})$")


def competencia_para_indice(competencia: str) -> int:
    """`YYYY-MM` em índice inteiro de meses, para comparação exata."""
    if not isinstance(competencia, str):
        raise ErroDeDados(
            f"competência deve ser str 'YYYY-MM', veio {type(competencia).__name__}"
        )
    m = _RE_COMPETENCIA.match(competencia.strip())
    if not m:
        raise ErroDeDados(f"competência malformada: {competencia!r} (esperado 'YYYY-MM')")
    ano, mes = int(m.group(1)), int(m.group(2))
    if not 1 <= mes <= 12:
        raise ErroDeDados(f"mês fora de 1..12 em {competencia!r}")
    return ano * 12 + (mes - 1)


def _dentro(competencia: str, inicio: str | None, fim: str | None) -> bool:
    """Intervalo fechado. `None` em qualquer ponta significa aberto daquele lado."""
    alvo = competencia_para_indice(competencia)
    if inicio is not None and alvo < competencia_para_indice(inicio):
        return False
    if fim is not None and alvo > competencia_para_indice(fim):
        return False
    return True


def _para_decimal(valor: Any, onde: str) -> Decimal:
    if isinstance(valor, float):
        raise ErroDeDados(f"{onde}: float é proibido (R12 — aritmética decimal)")
    try:
        return Decimal(str(valor))
    except InvalidOperation as exc:
        raise ErroDeDados(f"{onde}: valor não é decimal: {valor!r}") from exc


def _le_json(caminho: str | Path) -> dict:
    """`encoding='utf-8'` explícito: Windows assume cp1252 e corrompe acentuação."""
    with open(caminho, "r", encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# Catálogo
# --------------------------------------------------------------------------

_FORMAS = {"percentual", "monetario", "inteiro", "variante", "tabela"}
_TIPOS = {"substituicao-de-valor", "alteracao-de-composicao", "chave-de-variante"}
_ALTERACOES = {"apenas-elevacao", "qualquer", "derivado"}


@dataclass(frozen=True)
class Parametro:
    id: str
    nome: str
    tipo: str
    forma: str
    alteracao: str
    default_legal: Any
    piso_legal: Any
    fonte_default: str
    verbas: tuple[str, ...] = ()
    variantes: tuple[str, ...] = ()
    sem_default: bool = False
    derivado_de: tuple[str, ...] = ()
    bruto: dict = field(default_factory=dict, repr=False)

    @property
    def comparavel(self) -> bool:
        """Piso só é verificável quando o valor é numérico."""
        return self.forma in ("percentual", "monetario", "inteiro")


class Catalogo:
    def __init__(self, dados: dict) -> None:
        self.dados = dados
        self.parametros: dict[str, Parametro] = {}
        for p in dados.get("parametros", []):
            self.parametros[p["id"]] = Parametro(
                id=p["id"],
                nome=p.get("nome", p["id"]),
                tipo=p["tipo"],
                forma=p["forma"],
                alteracao=p["alteracao"],
                default_legal=p.get("default_legal"),
                piso_legal=p.get("piso_legal"),
                fonte_default=p.get("fonte_default", ""),
                verbas=tuple(p.get("verbas", ())),
                variantes=tuple(p.get("variantes", ())),
                sem_default=bool(p.get("sem_default", False)),
                derivado_de=tuple(p.get("derivado_de", ())),
                bruto=p,
            )

    @classmethod
    def de_arquivo(cls, caminho: str | Path = CATALOGO_PADRAO) -> "Catalogo":
        return cls(_le_json(caminho))

    def __getitem__(self, pid: str) -> Parametro:
        if pid not in self.parametros:
            raise ErroDeDados(f"parâmetro desconhecido no catálogo: {pid!r}")
        return self.parametros[pid]

    def valida(self) -> list[str]:
        """Consistência interna do catálogo. Devolve a lista de problemas."""
        problemas: list[str] = []
        for p in self.parametros.values():
            if p.tipo not in _TIPOS:
                problemas.append(f"{p.id}: tipo inválido {p.tipo!r}")
            if p.forma not in _FORMAS:
                problemas.append(f"{p.id}: forma inválida {p.forma!r}")
            if p.alteracao not in _ALTERACOES:
                problemas.append(f"{p.id}: alteracao inválida {p.alteracao!r}")
            if p.sem_default and p.default_legal is not None:
                problemas.append(f"{p.id}: sem_default mas tem default_legal")
            if not p.sem_default and p.default_legal is None and p.alteracao != "derivado":
                problemas.append(f"{p.id}: sem default_legal e sem sem_default")
            if p.forma == "variante":
                if not p.variantes:
                    problemas.append(f"{p.id}: forma variante sem lista de variantes")
                elif p.default_legal is not None and p.default_legal not in p.variantes:
                    problemas.append(
                        f"{p.id}: default {p.default_legal!r} fora das variantes"
                    )
            if p.alteracao == "apenas-elevacao" and p.piso_legal is None:
                problemas.append(f"{p.id}: apenas-elevacao sem piso_legal (R18)")
            if p.derivado_de and p.alteracao != "derivado":
                problemas.append(f"{p.id}: derivado_de sem alteracao=derivado")
        return problemas


# --------------------------------------------------------------------------
# Instrumentos
# --------------------------------------------------------------------------

@dataclass
class Clausula:
    instrumento: str
    clausula: str
    parametro: str
    valor: Any
    forma: str
    vigencia: tuple[str | None, str | None]
    texto: str
    por_extensao: bool = False


class Instrumentos:
    def __init__(self, *fontes: dict) -> None:
        self.instrumentos: list[dict] = []
        for f in fontes:
            self.instrumentos.extend(f.get("instrumentos", []))

    @classmethod
    def de_arquivos(cls, *caminhos: str | Path) -> "Instrumentos":
        return cls(*(_le_json(c) for c in caminhos))

    def _alcanca(self, inst: dict, categoria: str) -> tuple[bool, bool]:
        """Devolve (alcança, por_extensao)."""
        if categoria in (inst.get("categorias_abrangidas") or []):
            return True, False
        for ext in inst.get("categorias_por_extensao") or []:
            if ext.get("categoria") == categoria:
                return True, True
        return False, False

    def candidatas(self, parametro: str, categoria: str, competencia: str) -> list[Clausula]:
        """Cláusulas aplicáveis à tripla. Sem escolher entre elas."""
        achadas: list[Clausula] = []
        for inst in self.instrumentos:
            alcanca, por_extensao = self._alcanca(inst, categoria)
            if not alcanca:
                continue
            vig = inst.get("vigencia") or {}
            # Vigência do instrumento com ponta desconhecida não filtra: cadastro
            # incompleto não deve ser confundido com vigência aberta de verdade.
            if vig.get("inicio") is not None or vig.get("fim") is not None:
                if not _dentro(competencia, vig.get("inicio"), vig.get("fim")):
                    continue
            for cl in inst.get("clausulas") or []:
                if cl.get("parametro") != parametro:
                    continue
                vp = cl.get("vigencia_propria") or {}
                if vp:
                    if not _dentro(competencia, vp.get("inicio"), vp.get("fim")):
                        continue
                achadas.append(
                    Clausula(
                        instrumento=inst["id"],
                        clausula=cl.get("clausula", "?"),
                        parametro=parametro,
                        valor=cl.get("valor"),
                        forma=cl.get("forma", ""),
                        vigencia=(
                            vp.get("inicio") if vp else vig.get("inicio"),
                            vp.get("fim") if vp else vig.get("fim"),
                        ),
                        texto=cl.get("texto", ""),
                        por_extensao=por_extensao,
                    )
                )
        return achadas


# --------------------------------------------------------------------------
# Resolução
# --------------------------------------------------------------------------

ORIGEM_TITULO = "titulo-judicial"
ORIGEM_COLETIVA = "norma-coletiva"
ORIGEM_USUARIO = "escolha-do-usuario"
ORIGEM_DEFAULT = "default-legal"

COBERTURA_COM = "com-cobertura-coletiva"
COBERTURA_SEM = "sem-cobertura-coletiva"
COBERTURA_SEM_DEFAULT = "sem-default-legal"
COBERTURA_CONFLITO = "conflito"
COBERTURA_REJEITADO = "rejeitado-por-piso-legal"


@dataclass
class Resolucao:
    parametro: str
    categoria: str
    competencia: str
    valor: Any
    forma: str
    origem: str
    cobertura: str
    proveniencia: dict
    divergencias: list[dict] = field(default_factory=list)
    conflitos: list[dict] = field(default_factory=list)
    rejeicoes: list[dict] = field(default_factory=list)

    @property
    def tem_cobertura(self) -> bool:
        return self.cobertura == COBERTURA_COM

    @property
    def calculavel(self) -> bool:
        return self.cobertura not in (COBERTURA_SEM_DEFAULT, COBERTURA_CONFLITO)

    def __str__(self) -> str:
        p = self.proveniencia
        onde = p.get("instrumento") or p.get("fonte") or "—"
        return (
            f"{self.parametro} [{self.categoria} {self.competencia}] = {self.valor!r} "
            f"({self.origem}, {self.cobertura}) ← {onde}"
        )


def _viola_piso(param: Parametro, valor: Any) -> bool:
    """R18 — só tem sentido em parâmetro numérico com piso declarado."""
    if param.alteracao != "apenas-elevacao" or param.piso_legal is None:
        return False
    if not param.comparavel:
        # Piso em variante ou tabela não é comparável por número. Não rejeita
        # silenciosamente: quem chama recebe a informação pela cobertura.
        return False
    return _para_decimal(valor, param.id) < _para_decimal(param.piso_legal, param.id)


def resolve(
    parametro: str,
    categoria: str,
    competencia: str,
    instrumentos: Instrumentos | None = None,
    catalogo: Catalogo | None = None,
    titulo_judicial: Any = None,
    escolha_usuario: Any = None,
) -> Resolucao:
    """Resolve a tripla. Nunca lança por ausência de cobertura (R14)."""
    catalogo = catalogo or Catalogo.de_arquivo()
    param = catalogo[parametro]
    competencia_para_indice(competencia)  # valida a forma

    divergencias: list[dict] = []
    rejeicoes: list[dict] = []

    candidatas = (
        instrumentos.candidatas(parametro, categoria, competencia) if instrumentos else []
    )

    # Cláusulas abaixo do piso saem do jogo, mas ficam registradas (R18).
    validas: list[Clausula] = []
    for c in candidatas:
        if _viola_piso(param, c.valor):
            rejeicoes.append(
                {
                    "instrumento": c.instrumento,
                    "clausula": c.clausula,
                    "valor_negociado": c.valor,
                    "piso_legal": param.piso_legal,
                    "motivo": "valor negociado inferior ao piso legal (R18)",
                }
            )
        else:
            validas.append(c)

    # Conflito: mais de um instrumento com cláusula aplicável (R16 — não resolver).
    por_instrumento = {c.instrumento for c in validas}
    if len(por_instrumento) > 1:
        return Resolucao(
            parametro=parametro,
            categoria=categoria,
            competencia=competencia,
            valor=None,
            forma=param.forma,
            origem=ORIGEM_COLETIVA,
            cobertura=COBERTURA_CONFLITO,
            proveniencia={"fonte": "múltiplos instrumentos aplicáveis"},
            conflitos=[
                {
                    "instrumento": c.instrumento,
                    "clausula": c.clausula,
                    "valor": c.valor,
                    "vigencia": c.vigencia,
                    "por_extensao": c.por_extensao,
                }
                for c in validas
            ],
            rejeicoes=rejeicoes,
        )

    # Duas cláusulas do MESMO instrumento para a mesma competência é defeito de cadastro.
    if len(validas) > 1:
        raise ErroDeDados(
            f"{parametro}: instrumento {validas[0].instrumento} tem "
            f"{len(validas)} cláusulas sobrepostas em {competencia} "
            f"({', '.join(c.clausula for c in validas)})"
        )

    coletiva = validas[0] if validas else None

    # Precedência R16: título > coletiva > usuário > default.
    niveis: list[tuple[str, Any]] = []
    if titulo_judicial is not None:
        niveis.append((ORIGEM_TITULO, titulo_judicial))
    if coletiva is not None:
        niveis.append((ORIGEM_COLETIVA, coletiva.valor))
    if escolha_usuario is not None:
        niveis.append((ORIGEM_USUARIO, escolha_usuario))
    if not param.sem_default:
        niveis.append((ORIGEM_DEFAULT, param.default_legal))

    if not niveis:
        return Resolucao(
            parametro=parametro,
            categoria=categoria,
            competencia=competencia,
            valor=None,
            forma=param.forma,
            origem=ORIGEM_DEFAULT,
            cobertura=COBERTURA_SEM_DEFAULT,
            proveniencia={
                "fonte": param.fonte_default or "sem default legal",
                "observacao": "parâmetro sem default legal; sem instrumento, a verba "
                "fica pendente de dado — não é erro (R14)",
            },
            rejeicoes=rejeicoes,
        )

    origem, valor = niveis[0]

    # Toda discordância entre níveis é registrada, não silenciada (R16).
    for outra_origem, outro_valor in niveis[1:]:
        if str(outro_valor) != str(valor):
            divergencias.append(
                {
                    "nivel_aplicado": origem,
                    "valor_aplicado": valor,
                    "nivel_divergente": outra_origem,
                    "valor_divergente": outro_valor,
                }
            )

    if origem == ORIGEM_COLETIVA and coletiva is not None:
        proveniencia = {
            "instrumento": coletiva.instrumento,
            "clausula": coletiva.clausula,
            "vigencia": coletiva.vigencia,
            "texto": coletiva.texto,
            "por_extensao": coletiva.por_extensao,
        }
        cobertura = COBERTURA_COM
    else:
        proveniencia = {"fonte": param.fonte_default}
        if origem == ORIGEM_TITULO:
            proveniencia = {"fonte": "determinação do título judicial"}
        elif origem == ORIGEM_USUARIO:
            proveniencia = {"fonte": "override do usuário"}
        cobertura = COBERTURA_COM if coletiva is not None else COBERTURA_SEM

    # Piso vale para qualquer origem que não seja o título (R16 × R18).
    if origem != ORIGEM_TITULO and _viola_piso(param, valor):
        rejeicoes.append(
            {
                "origem": origem,
                "valor": valor,
                "piso_legal": param.piso_legal,
                "motivo": "valor inferior ao piso legal (R18)",
            }
        )
        return Resolucao(
            parametro=parametro,
            categoria=categoria,
            competencia=competencia,
            valor=None,
            forma=param.forma,
            origem=origem,
            cobertura=COBERTURA_REJEITADO,
            proveniencia=proveniencia,
            divergencias=divergencias,
            rejeicoes=rejeicoes,
        )

    return Resolucao(
        parametro=parametro,
        categoria=categoria,
        competencia=competencia,
        valor=valor,
        forma=param.forma,
        origem=origem,
        cobertura=cobertura,
        proveniencia=proveniencia,
        divergencias=divergencias,
        rejeicoes=rejeicoes,
    )


def resolve_serie(
    parametro: str,
    categoria: str,
    competencias: Iterable[str],
    **kwargs,
) -> list[Resolucao]:
    """Resolve a mesma tripla ao longo de várias competências.

    É o caminho de uso real: um contrato atravessa vigências, e cada competência
    pode cair num instrumento diferente — ou em nenhum.
    """
    return [resolve(parametro, categoria, c, **kwargs) for c in competencias]


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if "--catalogo-ok" in argv:
        cat = Catalogo.de_arquivo()
        problemas = cat.valida()
        print(f"catálogo: {len(cat.parametros)} parâmetros")
        for p in problemas:
            print(f"  PROBLEMA: {p}")
        if not problemas:
            print("  consistência interna: OK")
        return 1 if problemas else 0

    if len(argv) < 4:
        print(__doc__)
        return 2

    parametro, categoria, competencia, *arquivos = argv
    r = resolve(
        parametro,
        categoria,
        competencia,
        instrumentos=Instrumentos.de_arquivos(*arquivos),
    )
    print(r)
    for d in r.divergencias:
        print(f"  divergência: {d}")
    for c in r.conflitos:
        print(f"  conflito: {c}")
    for x in r.rejeicoes:
        print(f"  rejeição: {x}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
