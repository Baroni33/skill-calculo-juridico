#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Camada de presets de regime temporal — validador e resolvedor.

Decide QUAL REGRA se aplica a cada competência. É camada distinta da que decide
QUANTO VALE um parâmetro (`valida_parametros.py`), e é avaliada ANTES dela: o
regime decide se um parâmetro é sequer consultado (R22).

Três coisas que este módulo existe para impedir:

1. **Eixo único.** O corpus tem catorze eixos de corte distintos, e apenas dois
   são de competência ou fato. A multa do art. 467 corta pela data da SENTENÇA;
   a prescrição intercorrente, pela data da DETERMINAÇÃO JUDICIAL; o divisor do
   bancário, por um ESTADO PROCESSUAL. Tratar tudo como competência é o erro
   central que a camada previne.

2. **Default inventado.** Onde o corpus manda não resolver, não há default. O
   resultado é `calculavel: False` — não um palpite plausível.

3. **Competência que atravessa o corte.** O corte de 11/11/2017 parte novembro
   de 2017 ao meio. Uma competência mensal não sabe de que lado está. O
   resolvedor recusa em vez de escolher.

Sem floats (R12). Leitura sempre com `encoding='utf-8'`.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# BLOCO 25 — script DE SKILL, e por isso o catálogo viaja com ele. `regras/` é
# irmão de `scripts/` dentro da skill. O caminho anterior apontava para `docs/`,
# que a instalação NÃO copia: o script quebrava no instante em que a skill saía
# do repositório. Nada além do caminho mudou.
SKILL = Path(__file__).resolve().parents[1]
CATALOGO_PADRAO = SKILL / "regras" / "regimes-temporais-catalogo.json"


class ErroDeDados(Exception):
    """Defeito de cadastro. Quebra em vez de silenciar."""


class RegimesNaoAvaliados(Exception):
    """R22 — parâmetro consultado antes da avaliação dos regimes."""


# --------------------------------------------------------------------------
# Datas: o corpus mistura granularidades
# --------------------------------------------------------------------------

_RE_DATA = re.compile(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$")


@dataclass(frozen=True, order=True)
class Data:
    """Data de granularidade variável: ano, competência ou dia.

    O corpus dá cortes ao dia (11/11/2017, 20/03/2023, 05/09/2001) e fatos em
    competência mensal. Comparar os dois sem cuidado produz erro silencioso de
    um mês — por isso a granularidade é preservada, não normalizada.
    """

    ano: int
    mes: int | None = None
    dia: int | None = None

    @staticmethod
    def de(texto: str | None) -> "Data | None":
        if texto is None:
            return None
        if isinstance(texto, Data):
            return texto
        m = _RE_DATA.match(str(texto).strip())
        if not m:
            raise ErroDeDados(f"data inválida: {texto!r}")
        ano, mes, dia = m.groups()
        d = Data(int(ano), int(mes) if mes else None, int(dia) if dia else None)
        if d.mes is not None and not 1 <= d.mes <= 12:
            raise ErroDeDados(f"mês inválido: {texto!r}")
        if d.dia is not None and not 1 <= d.dia <= 31:
            raise ErroDeDados(f"dia inválido: {texto!r}")
        return d

    @property
    def tem_dia(self) -> bool:
        return self.dia is not None

    def _limites(self) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
        """Primeiro e último instante que esta data pode representar."""
        mes_ini, mes_fim = (self.mes, self.mes) if self.mes else (1, 12)
        dia_ini, dia_fim = (self.dia, self.dia) if self.dia else (1, 31)
        return (self.ano, mes_ini, dia_ini), (self.ano, mes_fim, dia_fim)

    def antes_de(self, outra: "Data") -> bool:
        """Todo o intervalo desta data é anterior ao início da outra."""
        return self._limites()[1] < outra._limites()[0]

    def desde(self, outra: "Data") -> bool:
        """Todo o intervalo desta data é igual ou posterior ao da outra."""
        return self._limites()[0] >= outra._limites()[0]

    def atravessa(self, corte: "Data") -> bool:
        """A data é grossa demais para saber de que lado do corte está.

        Competência 2017-11 contra o corte 2017-11-11: parte do mês está de um
        lado e parte do outro. Escolher um lado é inventar.
        """
        return not self.antes_de(corte) and not self.desde(corte)

    def __str__(self) -> str:
        p = [f"{self.ano:04d}"]
        if self.mes is not None:
            p.append(f"{self.mes:02d}")
        if self.dia is not None:
            p.append(f"{self.dia:02d}")
        return "-".join(p)


# --------------------------------------------------------------------------
# Vocabulário
# --------------------------------------------------------------------------

EIXOS_DECLARADOS = {
    "competencia-do-fato",
    "data-de-admissao",
    "conteudo-do-titulo",
    "data-da-sentenca",
    "data-da-dispensa",
    "inicio-do-aviso",
    "ciencia-da-lesao",
    "determinacao-judicial-na-execucao",
    "estado-processual",
    "decisao-de-merito-no-processo",
    "fato-gerador",
    "data-do-calculo",
    "efetivo-pagamento",
    "data-base-da-categoria",
    # Bloco 12 — item "i" da modulação da ADC 58. Nenhum dos dois sai do
    # cálculo: o primeiro é evento do processo, o segundo é qualificação do
    # depósito, e é ele que decide o alcance da proteção dentro de i.1.
    "evento-questionamento-expresso",
    "natureza-do-deposito",
}

# `sem-eixo-temporal` não é um eixo ausente — é a constatação de que a escolha
# NÃO VARIA NO TEMPO. `pr.imputacao` escolhe entre o critério proporcional do
# Manual TRT-3 e o art. 354 do CC, e a escolha vale para o cálculo inteiro,
# qualquer que seja a competência. Distinguir isso de "NAO-DECLARADO" importa:
# lá falta informação, aqui não há o que faltar.
EIXOS_ESPECIAIS = {
    "meta", "herdado", "composto", "NAO-DECLARADO", "sem-eixo-temporal",
}

# Três estados, não dois. Um booleano forçaria a apresentar como DECLARADO o
# que é INFERÊNCIA — e apresentar inferência como declaração é o erro que este
# módulo existe para não cometer.
ORIGENS_DO_EIXO = {"declarado", "inferido", "herdado", "nao-declarado"}
EIXOS = EIXOS_DECLARADOS | EIXOS_ESPECIAIS

# Eixos que se resolvem lendo uma data dos fatos. Os demais dependem de
# condição processual, documental ou de escolha, e não de comparação de datas.
EIXO_PARA_FATO = {
    "competencia-do-fato": "competencia",
    "data-de-admissao": "admissao",
    "data-da-sentenca": "sentenca",
    "data-da-dispensa": "dispensa",
    "inicio-do-aviso": "inicio_do_aviso",
    "ciencia-da-lesao": "ciencia_da_lesao",
    "determinacao-judicial-na-execucao": "determinacao_judicial",
    "fato-gerador": "fato_gerador",
    "data-do-calculo": "data_do_calculo",
    "efetivo-pagamento": "efetivo_pagamento",
}

NATUREZAS = {"cadeia-temporal", "divergencia-interpretativa"}
ESCOPOS = {"apuracao", "encargos", "liquidacao-execucao"}

ORIGEM_USUARIO = "escolha-do-usuario"
ORIGEM_DEFAULT = "default"
ORIGEM_DATA = "determinada-pela-data"

MOTIVO_SEM_DEFAULT = "sem-default-e-sem-escolha"
MOTIVO_EIXO_NAO_DECLARADO = "eixo-nao-declarado-no-corpus"
MOTIVO_ATRAVESSA = "competencia-atravessa-o-corte"
MOTIVO_FATO_AUSENTE = "fato-do-eixo-nao-informado"
MOTIVO_ANTERIOR_A_ADMISSAO = "regime-posterior-a-admissao-sob-ultratividade"
MOTIVO_BLOQUEADO = "regime-bloqueado-por-falta-de-serie"


def _le_json(caminho: str | Path) -> dict:
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------
# Catálogo
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Variante:
    id: str
    fundamento: str
    fonte: str = ""
    vigencia: dict = field(default_factory=dict)
    condicao: str | None = None
    efeito: dict = field(default_factory=dict)
    eixo_efetivo: str | None = None
    preset: str | None = None

    @property
    def de(self) -> Data | None:
        return Data.de(self.vigencia.get("de"))

    @property
    def ate(self) -> Data | None:
        return Data.de(self.vigencia.get("ate"))

    @property
    def datada(self) -> bool:
        return bool(self.vigencia)


@dataclass(frozen=True)
class Regime:
    id: str
    nome: str
    natureza: str
    eixo: str
    eixo_origem: str
    variantes: tuple[Variante, ...]
    corte: Data | None = None
    default: str | None = None
    sem_default: bool = False
    herda_de: str | None = None
    eixos_componentes: tuple[str, ...] = ()
    depende_de: tuple[str, ...] = ()
    afeta_parametros: tuple[str, ...] = ()
    afeta_verbas: tuple[str, ...] = ()
    escopo: str = "apuracao"
    meta_regime: bool = False
    bloqueado: bool = False
    bruto: dict = field(default_factory=dict, repr=False)

    @property
    def eixo_declarado(self) -> bool:
        return self.eixo_origem == "declarado"

    @property
    def eixo_inferido(self) -> bool:
        """O corpus sustenta o eixo para uma pergunta vizinha, não para esta.

        Resolve como o declarado; o que muda é o rastro. Quem lê a memória de
        cálculo precisa ver que ali houve um passo de raciocínio.
        """
        return self.eixo_origem == "inferido"

    def variante(self, vid: str) -> Variante:
        for v in self.variantes:
            if v.id == vid:
                return v
        raise ErroDeDados(f"{self.id}: variante desconhecida {vid!r}")

    @property
    def alcanca_todos_os_parametros(self) -> bool:
        return "TODOS" in self.afeta_parametros


class CatalogoRegimes:
    def __init__(self, dados: dict) -> None:
        self.dados = dados
        self.regimes: dict[str, Regime] = {}
        for r in dados.get("regimes", []):
            if r["id"] in self.regimes:
                raise ErroDeDados(f"regime duplicado: {r['id']}")
            self.regimes[r["id"]] = Regime(
                id=r["id"],
                nome=r["nome"],
                natureza=r["natureza"],
                eixo=r["eixo"],
                eixo_origem=r.get(
                    "eixo_origem",
                    "declarado" if r.get("eixo_declarado", True) else "nao-declarado",
                ),
                variantes=tuple(
                    Variante(
                        id=v["id"],
                        fundamento=v["fundamento"],
                        fonte=v.get("fonte", ""),
                        vigencia=v.get("vigencia") or {},
                        condicao=v.get("condicao"),
                        efeito=v.get("efeito") or {},
                        eixo_efetivo=v.get("eixo_efetivo"),
                        preset=v.get("preset"),
                    )
                    for v in r["variantes"]
                ),
                corte=Data.de(r.get("corte")),
                default=r.get("default"),
                sem_default=bool(r.get("sem_default", False)),
                herda_de=r.get("herda_de"),
                eixos_componentes=tuple(r.get("eixos_componentes", ())),
                depende_de=tuple(r.get("depende_de", ())),
                afeta_parametros=tuple(r.get("afeta_parametros", ())),
                afeta_verbas=tuple(r.get("afeta_verbas", ())),
                escopo=r.get("escopo", "apuracao"),
                meta_regime=bool(r.get("meta_regime", False)),
                bloqueado=bool(r.get("bloqueado", False)),
                bruto=r,
            )

    @classmethod
    def de_arquivo(cls, caminho: str | Path = CATALOGO_PADRAO) -> "CatalogoRegimes":
        return cls(_le_json(caminho))

    def __getitem__(self, rid: str) -> Regime:
        try:
            return self.regimes[rid]
        except KeyError:
            raise ErroDeDados(f"regime desconhecido: {rid!r}") from None

    def __contains__(self, rid: str) -> bool:
        return rid in self.regimes

    # ---------------------------------------------------------------- valida
    def valida(self) -> list[str]:
        p: list[str] = []
        for r in self.regimes.values():
            if r.natureza not in NATUREZAS:
                p.append(f"{r.id}: natureza inválida {r.natureza!r}")
            if r.eixo not in EIXOS:
                p.append(f"{r.id}: eixo inválido {r.eixo!r}")
            if r.escopo not in ESCOPOS:
                p.append(f"{r.id}: escopo inválido {r.escopo!r}")
            if not r.variantes:
                p.append(f"{r.id}: sem variantes")

            if r.eixo_origem not in ORIGENS_DO_EIXO:
                p.append(f"{r.id}: eixo_origem inválido {r.eixo_origem!r}")
            # Os dois estados que o eixo fixa: NAO-DECLARADO e herdado.
            for eixo_especial, origem in (("NAO-DECLARADO", "nao-declarado"),
                                          ("herdado", "herdado")):
                if (r.eixo == eixo_especial) != (r.eixo_origem == origem):
                    p.append(
                        f"{r.id}: eixo {r.eixo!r} e origem {r.eixo_origem!r} "
                        f"não combinam"
                    )
            if not r.bruto.get("fonte_do_eixo"):
                p.append(f"{r.id}: todo regime declara de onde vem o eixo, ou o que falta")
            # Inferência sem justificativa é declaração disfarçada.
            if r.eixo_inferido and not r.bruto.get("justificativa_da_inferencia"):
                p.append(f"{r.id}: eixo inferido exige justificativa_da_inferencia")
            if not r.eixo_inferido and r.bruto.get("justificativa_da_inferencia"):
                p.append(f"{r.id}: justificativa_da_inferencia sem eixo_origem=inferido")

            # herança
            if r.eixo == "herdado" and not r.herda_de:
                p.append(f"{r.id}: eixo herdado exige herda_de")
            if r.herda_de and r.herda_de not in self.regimes:
                p.append(f"{r.id}: herda_de aponta regime inexistente {r.herda_de!r}")
            if r.herda_de and r.eixo != "herdado":
                p.append(f"{r.id}: herda_de exige eixo=herdado")

            if r.eixo == "composto" and len(r.eixos_componentes) < 2:
                p.append(f"{r.id}: eixo composto exige ao menos dois eixos_componentes")
            for e in r.eixos_componentes:
                if e not in EIXOS_DECLARADOS:
                    p.append(f"{r.id}: eixo componente inválido {e!r}")

            # default
            if r.sem_default and r.default:
                p.append(f"{r.id}: sem_default=true não admite default")
            if r.sem_default and not r.bruto.get("por_que_sem_default"):
                p.append(f"{r.id}: sem_default exige por_que_sem_default")
            if r.default and r.default not in {v.id for v in r.variantes}:
                p.append(f"{r.id}: default {r.default!r} não é variante")
            if r.default and not r.bruto.get("default_justificativa"):
                p.append(f"{r.id}: default exige default_justificativa")
            # Divergência interpretativa é escolha: ou tem default, ou declara
            # por que não pode ter. Cadeia temporal a data resolve.
            if r.natureza == "divergencia-interpretativa" and not (
                r.default or r.sem_default
            ):
                p.append(f"{r.id}: divergência exige default ou sem_default declarado")

            # fundamento por variante — é o que separa preset de palpite
            for v in r.variantes:
                if not v.fundamento:
                    p.append(f"{r.id}/{v.id}: variante sem fundamento")
                if not (v.datada or v.condicao) and r.natureza == "cadeia-temporal":
                    if len(r.variantes) > 1:
                        p.append(f"{r.id}/{v.id}: cadeia temporal exige vigencia ou condicao")
                # Condição em prosa documenta; quem resolve é a vigência. Um
                # eixo de data sem vigência cadastrada cai no default sem que
                # ninguém perceba — foi assim que o eletricitário quebrou.
                if (
                    r.natureza == "cadeia-temporal"
                    and len(r.variantes) > 1
                    and (r.eixo in EIXO_PARA_FATO
                         or (r.eixo == "herdado" and r.herda_de))
                    and not v.datada
                ):
                    p.append(
                        f"{r.id}/{v.id}: eixo de data exige vigencia, não só condicao"
                    )
                if v.de and v.ate and not v.de.antes_de(v.ate) and v.de != v.ate:
                    if v.ate._limites()[1] < v.de._limites()[0]:
                        p.append(f"{r.id}/{v.id}: vigência invertida")

            if r.bloqueado and not r.bruto.get("por_que_bloqueado"):
                p.append(f"{r.id}: bloqueado exige por_que_bloqueado")
        return p

    # ------------------------------------------------------------- consultas
    def provisorios(self) -> list[Regime]:
        """Regimes que NÃO PODEM ser aplicados: o corpus não declara o eixo.

        Distinto dos herdados: aqueles têm um mecanismo de eixo (a herança) e
        passam a ser aplicáveis assim que o regime-pai for escolhido. Estes não
        têm mecanismo algum — falta o dado.
        """
        return [r for r in self.regimes.values() if r.eixo == "NAO-DECLARADO"]

    def inferidos(self) -> list[Regime]:
        """Regimes que resolvem, mas cujo eixo é raciocínio e não leitura."""
        return [r for r in self.regimes.values() if r.eixo_inferido]

    def herdados(self) -> list[Regime]:
        """Regimes cujo eixo depende de uma escolha jurídica ainda não feita."""
        return [r for r in self.regimes.values() if r.eixo == "herdado"]

    def por_eixo(self, eixo: str) -> list[Regime]:
        return [r for r in self.regimes.values() if r.eixo == eixo]

    def que_alcancam(self, parametro: str) -> list[Regime]:
        return [
            r
            for r in self.regimes.values()
            if parametro in r.afeta_parametros or r.alcanca_todos_os_parametros
        ]

    def eixos_em_uso(self) -> dict[str, int]:
        c: dict[str, int] = {}
        for r in self.regimes.values():
            c[r.eixo] = c.get(r.eixo, 0) + 1
            for e in r.eixos_componentes:
                c[e] = c.get(e, 0) + 1
        return dict(sorted(c.items()))


# --------------------------------------------------------------------------
# Fatos do caso
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Fatos:
    """As datas e estados de que os catorze eixos precisam.

    Nenhum campo é obrigatório: um caso real raramente conhece todos. Eixo cujo
    fato não foi informado devolve `calculavel: False` com o motivo — nunca um
    default silencioso.
    """

    competencia: str | None = None
    admissao: str | None = None
    dispensa: str | None = None
    sentenca: str | None = None
    inicio_do_aviso: str | None = None
    ciencia_da_lesao: str | None = None
    determinacao_judicial: str | None = None
    fato_gerador: str | None = None
    data_do_calculo: str | None = None
    efetivo_pagamento: str | None = None
    data_base_da_categoria: str | None = None
    # estados processuais e documentais
    transitado_em_julgado: bool = False
    em_liquidacao: bool = False
    decisao_de_merito_no_processo: str | None = None
    titulo: dict = field(default_factory=dict)

    def data_de(self, eixo: str) -> Data | None:
        campo = EIXO_PARA_FATO.get(eixo)
        if campo is None:
            return None
        return Data.de(getattr(self, campo))


@dataclass(frozen=True)
class Escolha:
    variante: str
    justificativa: str = ""


# --------------------------------------------------------------------------
# Resolução
# --------------------------------------------------------------------------


@dataclass
class ResolucaoRegime:
    regime: str
    variante: str | None
    eixo_efetivo: str
    origem: str | None
    calculavel: bool
    consultado: bool = True
    eixo_inferido: bool = False
    motivo: str | None = None
    data_aplicada: str | None = None
    efeito: dict = field(default_factory=dict)
    fundamento: str = ""
    divergencias: list[dict] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)

    def registro(self) -> dict:
        """R19 — o que a memória de cálculo grava desta competência."""
        return {
            "regime": self.regime,
            "variante": self.variante,
            "eixo": self.eixo_efetivo,
            "eixo_inferido": self.eixo_inferido,
            "data_aplicada": self.data_aplicada,
            "origem": self.origem,
            "calculavel": self.calculavel,
            "consultado": self.consultado,
            "motivo": self.motivo,
            "fundamento": self.fundamento,
            "divergencias": list(self.divergencias),
        }


def _nao_calculavel(regime: Regime, eixo: str, motivo: str, **kw) -> ResolucaoRegime:
    return ResolucaoRegime(
        regime=regime.id,
        variante=None,
        eixo_efetivo=eixo,
        origem=None,
        calculavel=False,
        motivo=motivo,
        **kw,
    )


def _eixo_efetivo(
    regime: Regime,
    fatos: Fatos,
    escolhas: dict[str, Escolha],
    catalogo: CatalogoRegimes,
) -> tuple[str, ResolucaoRegime | None]:
    """Resolve o eixo, seguindo a herança quando houver.

    A herança é o mecanismo da interação com o intertemporal: sob a corrente
    ultrativa o eixo vira a data de admissão, e regimes posteriores a ela deixam
    de ser consultados.
    """
    if regime.eixo != "herdado":
        return regime.eixo, None

    pai = catalogo[regime.herda_de]
    r_pai = resolve_regime(pai.id, fatos, escolhas, catalogo)
    if not r_pai.calculavel:
        return "herdado", _nao_calculavel(
            regime,
            "herdado",
            r_pai.motivo or MOTIVO_SEM_DEFAULT,
            avisos=[
                f"o eixo depende de {pai.id}, que não resolveu: "
                f"{r_pai.motivo}. Nenhum ponto do motor sabe qual regra aplicar "
                f"antes de {regime.corte} enquanto essa escolha não for feita."
            ],
        )
    variante_pai = pai.variante(r_pai.variante)
    return variante_pai.eixo_efetivo or "competencia-do-fato", None


def _escolhe_por_data(regime: Regime, data: Data) -> tuple[Variante | None, str | None]:
    """Cadeia temporal: a data seleciona a variante. Ninguém escolhe."""
    if regime.corte and data.atravessa(regime.corte):
        return None, MOTIVO_ATRAVESSA
    candidatas = [
        v
        for v in regime.variantes
        if v.datada
        and (v.de is None or data.desde(v.de))
        and (v.ate is None or data.antes_de(v.ate) or _mesmo_periodo(data, v.ate))
    ]
    if len(candidatas) == 1:
        return candidatas[0], None
    if not candidatas:
        return None, "nenhuma-variante-cobre-a-data"
    return None, "variantes-sobrepostas-na-data"


def _mesmo_periodo(data: Data, limite: Data) -> bool:
    """A data cabe inteira dentro do período que o limite fecha."""
    return data._limites()[1] <= limite._limites()[1]


def resolve_regime(
    regime_id: str,
    fatos: Fatos,
    escolhas: dict[str, Escolha] | None = None,
    catalogo: CatalogoRegimes | None = None,
) -> ResolucaoRegime:
    """Resolve um regime para um conjunto de fatos.

    A ordem importa: eixo primeiro, escolha depois, data por último. Um regime
    cujo eixo não se resolve não tem como ser escolhido nem datado.
    """
    catalogo = catalogo or CatalogoRegimes.de_arquivo()
    escolhas = escolhas or {}
    r = catalogo[regime_id]
    res = _resolve(r, fatos, escolhas, catalogo)
    if r.eixo_inferido:
        res.eixo_inferido = True
        res.avisos.append(
            "eixo INFERIDO: " + r.bruto.get("justificativa_da_inferencia", "")
        )
    return res


def _resolve(
    r: Regime,
    fatos: Fatos,
    escolhas: dict[str, Escolha],
    catalogo: CatalogoRegimes,
) -> ResolucaoRegime:
    if r.bloqueado:
        return _nao_calculavel(
            r, r.eixo, MOTIVO_BLOQUEADO,
            avisos=[r.bruto.get("por_que_bloqueado", "")],
        )

    eixo, falha = _eixo_efetivo(r, fatos, escolhas, catalogo)
    if falha is not None:
        return falha

    if eixo == "NAO-DECLARADO":
        return _nao_calculavel(
            r, eixo, MOTIVO_EIXO_NAO_DECLARADO,
            avisos=[
                "O corpus dá a data de corte mas não diz qual data governa. "
                "Supor o eixo faz o resultado sair plausível com a conta inteira "
                "no regime errado."
            ],
        )

    # --- escolha explícita do usuário (R21)
    escolha = escolhas.get(r.id)
    if escolha is not None:
        v = r.variante(escolha.variante)
        div: list[dict] = []
        if r.default and escolha.variante != r.default:
            if not escolha.justificativa:
                raise ErroDeDados(
                    f"{r.id}: escolha {escolha.variante!r} diverge do default "
                    f"{r.default!r} sem justificativa (R21)"
                )
            div.append(
                {
                    "nivel_divergente": ORIGEM_DEFAULT,
                    "valor_do_default": r.default,
                    "valor_aplicado": escolha.variante,
                    "justificativa": escolha.justificativa,
                }
            )
        return ResolucaoRegime(
            regime=r.id, variante=v.id, eixo_efetivo=eixo,
            origem=ORIGEM_USUARIO, calculavel=True, efeito=dict(v.efeito),
            fundamento=v.fundamento, divergencias=div,
        )

    # --- meta-regime sem escolha: R20-EXCECAO
    if r.sem_default:
        return _nao_calculavel(
            r, eixo, MOTIVO_SEM_DEFAULT,
            avisos=[r.bruto.get("por_que_sem_default", "")],
        )

    # --- cadeia temporal: a data decide
    if r.natureza == "cadeia-temporal":
        data = fatos.data_de(eixo)
        if data is None:
            if r.default:
                v = r.variante(r.default)
                return ResolucaoRegime(
                    regime=r.id, variante=v.id, eixo_efetivo=eixo,
                    origem=ORIGEM_DEFAULT, calculavel=True, efeito=dict(v.efeito),
                    fundamento=v.fundamento,
                    avisos=[f"R20: sem o fato do eixo {eixo!r}, aplicou o default"],
                )
            return _nao_calculavel(r, eixo, MOTIVO_FATO_AUSENTE)

        v, motivo = _escolhe_por_data(r, data)
        if v is None:
            if motivo == MOTIVO_ATRAVESSA:
                return _nao_calculavel(
                    r, eixo, motivo, data_aplicada=str(data),
                    avisos=[
                        f"o corte de {r.corte} parte a competência {data} ao meio; "
                        f"informe a data com precisão de dia"
                    ],
                )
            if r.default:
                vd = r.variante(r.default)
                return ResolucaoRegime(
                    regime=r.id, variante=vd.id, eixo_efetivo=eixo,
                    origem=ORIGEM_DEFAULT, calculavel=True, data_aplicada=str(data),
                    efeito=dict(vd.efeito), fundamento=vd.fundamento,
                    avisos=[f"R20: {motivo}; aplicou o default"],
                )
            return _nao_calculavel(r, eixo, motivo or "indeterminado",
                                   data_aplicada=str(data))
        return ResolucaoRegime(
            regime=r.id, variante=v.id, eixo_efetivo=eixo, origem=ORIGEM_DATA,
            calculavel=True, data_aplicada=str(data), efeito=dict(v.efeito),
            fundamento=v.fundamento,
        )

    # --- divergência interpretativa sem escolha: R20
    vd = r.variante(r.default)
    return ResolucaoRegime(
        regime=r.id, variante=vd.id, eixo_efetivo=eixo, origem=ORIGEM_DEFAULT,
        calculavel=True, efeito=dict(vd.efeito), fundamento=vd.fundamento,
        avisos=["R20: sem escolha explícita, aplicou o default e marcou a conta"],
    )


# --------------------------------------------------------------------------
# Avaliação da competência — R19 e R22
# --------------------------------------------------------------------------


@dataclass
class AvaliacaoDeRegimes:
    """Resultado da avaliação de TODOS os regimes numa competência.

    É o portão da R22: `resolve_parametro_sob_regime` só aceita um parâmetro
    depois que isto existe. Consultar parâmetro sem avaliar regime é erro de
    composição, impedido aqui — não detectado depois no resultado.
    """

    competencia: str
    fatos: Fatos
    resolucoes: dict[str, ResolucaoRegime]

    def __getitem__(self, rid: str) -> ResolucaoRegime:
        return self.resolucoes[rid]

    @property
    def calculaveis(self) -> dict[str, ResolucaoRegime]:
        return {k: v for k, v in self.resolucoes.items() if v.calculavel}

    @property
    def bloqueadores(self) -> dict[str, ResolucaoRegime]:
        """Regimes de apuração que impedem calcular esta competência."""
        return {
            k: v
            for k, v in self.resolucoes.items()
            if not v.calculavel and v.consultado
            and self._escopo(k) == "apuracao"
        }

    _catalogo: CatalogoRegimes | None = None

    def _escopo(self, rid: str) -> str:
        return self._catalogo[rid].escopo if self._catalogo else "apuracao"

    def registro(self) -> dict:
        """R19 — o bloco que a memória de cálculo grava para a competência."""
        return {
            "competencia": self.competencia,
            "regimes": [r.registro() for r in self.resolucoes.values()],
        }


def avalia_regimes(
    competencia: str,
    fatos: Fatos,
    escolhas: dict[str, Escolha] | None = None,
    catalogo: CatalogoRegimes | None = None,
    escopo: str | None = "apuracao",
) -> AvaliacaoDeRegimes:
    """R22 — avalia os regimes ANTES de qualquer parâmetro."""
    catalogo = catalogo or CatalogoRegimes.de_arquivo()
    fatos = (
        fatos
        if fatos.competencia == competencia
        else Fatos(**{**fatos.__dict__, "competencia": competencia})
    )
    alvo = [
        r for r in catalogo.regimes.values()
        if escopo is None or r.escopo == escopo
    ]
    res = {r.id: resolve_regime(r.id, fatos, escolhas, catalogo) for r in alvo}
    a = AvaliacaoDeRegimes(competencia=competencia, fatos=fatos, resolucoes=res)
    a._catalogo = catalogo
    return a


def parametro_consultavel(
    parametro: str,
    avaliacao: AvaliacaoDeRegimes | None,
    catalogo: CatalogoRegimes | None = None,
) -> tuple[bool, str | None]:
    """R22 — um parâmetro só se consulta sob regimes já avaliados.

    Devolve (consultavel, motivo). O motivo é o que a memória de cálculo grava
    quando o parâmetro não chega a ser consultado — é diferente de consultá-lo e
    descartar o resultado, que deixaria rastro de uma consulta que não houve.
    """
    if avaliacao is None:
        raise RegimesNaoAvaliados(
            f"R22: {parametro} consultado antes da avaliação dos regimes"
        )
    catalogo = catalogo or avaliacao._catalogo or CatalogoRegimes.de_arquivo()
    for r in catalogo.que_alcancam(parametro):
        res = avaliacao.resolucoes.get(r.id)
        if res is None:
            continue
        if not res.calculavel:
            return False, f"{r.id}: {res.motivo}"
        # Regime que suprime a verba suprime o parâmetro junto.
        if res.efeito.get("verba_existe") is False:
            return False, f"{r.id}/{res.variante}: a verba não existe nesta competência"
    return True, None


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    cat = CatalogoRegimes.de_arquivo()
    problemas = cat.valida()

    print(f"catálogo de regimes: {len(cat.regimes)}")
    if "--eixos" in argv:
        for eixo, n in cat.eixos_em_uso().items():
            marca = "" if eixo in EIXOS_DECLARADOS else "   <- especial"
            print(f"  {eixo:38s} {n}{marca}")
    prov = cat.provisorios()
    print(f"  eixo NÃO DECLARADO no corpus (inaplicáveis): {len(prov)}")
    for r in prov:
        print(f"    - {r.id}")
    inf = cat.inferidos()
    print(f"  eixo INFERIDO (resolve, com rastro): {len(inf)}")
    for r in inf:
        print(f"    - {r.id}  ({r.eixo})")
    her = cat.herdados()
    print(f"  eixo herdado (aplicáveis após a escolha intertemporal): {len(her)}")
    for r in her:
        print(f"    - {r.id}  <- {r.herda_de}")
    sem_def = [r.id for r in cat.regimes.values() if r.sem_default]
    print(f"  sem default (corpus manda não resolver): {len(sem_def)}")
    for rid in sem_def:
        print(f"    - {rid}")
    for p in problemas:
        print(f"  PROBLEMA: {p}")
    if not problemas:
        print("  consistência interna: OK")
    return 1 if problemas else 0


if __name__ == "__main__":
    raise SystemExit(main())
