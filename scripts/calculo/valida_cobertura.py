"""Validador das invariantes R1, R2 e R3 sobre conjuntos de segmentos.

R1 — Exclusividade de englobamento. Segmento cujo `engloba` cobre um componente
     não admite outro segmento do mesmo componente no mesmo intervalo. Vale para
     SELIC e taxa legal. Impede contar inflação duas vezes.

R2 — Cobertura sem lacuna nem sobreposição. A união dos segmentos cobre da parcela
     mais antiga até a data-base.

R3 — Tipo do indexador na virada. Nominal reflete a inflação do mês ANTERIOR;
     percentual, a do PRÓPRIO mês (Manual CJF, item 4.1.2.4, `pagina_pdf` 42).
     Virar de um tipo para o outro sem ajustar a defasagem desloca o cálculo em
     um mês — e nada mais o detecta.

Fonte: docs/calculo/00-base-normativa.md, seção 7.

Aritmética em competências `YYYY-MM`. Nenhum float em caminho algum (R12).

Segmentos que diferem em `condicao` vivem em universos separados: as tabelas
normativas bifurcam por qualidade do devedor, data da sentença e data do fato
gerador. Comparar ramos distintos produziria falso positivo de sobreposição.

**Tronco e ramo.** Segmento SEM `condicao` vale para todos os ramos. As cadeias
reais são incondicionais por décadas e só então bifurcam — a do CJF para ações
condenatórias é comum de 1964 a nov./2021 e só aí separa Fazenda de não-Fazenda.
Tratar o tronco como universo à parte faria cada ramo aparecer com décadas de
lacuna. Aqui a cobertura de cada ramo é avaliada como **tronco ∪ ramo**.

**Exaustividade não se presume.** A primeira versão desta correção deixava de
cobrar o universo incondicional sempre que houvesse ramo — e com isso escondia
lacuna real: tronco até 2000 mais um único ramo `devedor=fazenda-publica` de
2001 em diante passava como íntegro, embora não houvesse segmento algum para o
devedor privado depois de 2000. Trocar falso positivo por falso negativo, num
validador de cobertura, é o pior negócio possível.

O conjunto de `condicao` observado vem dos dados, não de um domínio declarado,
e portanto não se sabe se esgota os casos. Quem sabe é a cadeia. Por isso o
domínio de cada eixo é **declarável**, via `dominio_condicoes`:

* eixo declarado — cada valor do domínio vira um universo, inclusive os que
  nenhum segmento menciona. Valor sem ramo é avaliado só contra o tronco, e a
  lacuna aparece;
* eixo não declarado — o universo incondicional continua sendo cobrado, como o
  caso "nenhuma condição se aplica". Pode gerar ruído em cadeia realmente
  exaustiva; o remédio é declarar o domínio, não silenciar a checagem.

**R3 — o tipo do indexador na virada.** Cada segmento declara `tipo_indexador`,
com os cinco valores do catálogo `docs/calculo/tabelas-normativas/
indexadores-tipo-catalogo.json`:

* `nominal` e `percentual` — as duas letras do item 4.1.2.4. Medem meses
  diferentes: a virada entre elas exige ajuste de defasagem;
* `englobante` — SELIC e taxa legal. **Não entram em R3.** O item 4.1.2.4 fala
  em "refletir a inflação", e `bloco-08-jf-detalhe.md` (D8-C22) é literal: *"Selic
  não é índice de inflação"*. Quem governa a convivência delas é R1, não R3;
* `nao-indexador` — padrão monetário, conversão de moeda, juros em percentual
  legal. Sem índice não há defasagem a alinhar;
* `indeterminado` — o conceito se aplica e **nenhuma fonte o classifica**.

**Virada com ponta `indeterminado` BLOQUEIA** — vira violação, sob a regra
`R3-INDETERMINADO`. Não é a mesma coisa que uma virada confirmada, e por isso
tem rótulo próprio; mas passar seria converter "não se sabe" em "está certo".
É a troca de falso positivo por falso negativo que a nota sobre exaustividade,
logo acima, já condena uma vez. Num validador cuja razão de existir é que o erro
de R3 não tem sintoma, o silêncio é o pior resultado possível.

**O que salva a virada** é `aplicacao` não-vazio no segmento que ENTRA. É o campo
onde as cadeias declaram quando o índice incide em relação à competência
(`mes-posterior-a-competencia`, `primeiro-dia-do-mes-subsequente-a-prestacao`).
Ausente o campo, não há ajuste declarado — e declarar é o requisito.

Segmentos consecutivos com o **mesmo `indexador`** não são virada e não são
examinados: trocar o fundamento ou a condição não muda a régua de defasagem.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Mapping, Iterable, Sequence

__all__ = [
    "Segmento",
    "Violacao",
    "TIPOS_DE_INDEXADOR",
    "TIPOS_COM_DEFASAGEM",
    "competencia_para_indice",
    "indice_para_competencia",
    "valida_cobertura",
    "carrega_segmentos",
]


# --------------------------------------------------------------------------
# Tipos de indexador (R3)
# --------------------------------------------------------------------------
# Domínio fechado, espelho de `valores_de_tipo` em
# docs/calculo/tabelas-normativas/indexadores-tipo-catalogo.json.
TIPOS_DE_INDEXADOR: frozenset[str] = frozenset(
    {"nominal", "percentual", "englobante", "nao-indexador", "indeterminado"}
)

#: Os dois tipos cuja troca move a defasagem em um mês — item 4.1.2.4, letras a e b.
TIPOS_COM_DEFASAGEM: frozenset[str] = frozenset({"nominal", "percentual"})


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
    indexador: str = ""
    tipo_indexador: str = ""
    aplicacao: str = ""

    @staticmethod
    def de_dict(d: dict[str, Any], indice: int = 0) -> "Segmento":
        faltando = [c for c in ("inicio", "fim", "componente") if c not in d]
        if faltando:
            raise ValueError(f"segmento #{indice} sem campo(s) obrigatório(s): {', '.join(faltando)}")
        condicao = d.get("condicao") or {}
        if not isinstance(condicao, dict):
            raise ValueError(f"segmento #{indice}: 'condicao' deve ser objeto")
        tipo = str(d.get("tipo_indexador") or "")
        if tipo and tipo not in TIPOS_DE_INDEXADOR:
            raise ValueError(
                f"segmento #{indice}: 'tipo_indexador' inválido {tipo!r} — "
                f"valores do catálogo: {', '.join(sorted(TIPOS_DE_INDEXADOR))}"
            )
        seg = Segmento(
            inicio=d["inicio"],
            fim=d["fim"],
            componente=d["componente"],
            engloba=tuple(d.get("engloba") or ()),
            condicao=tuple(sorted((str(k), str(v)) for k, v in condicao.items())),
            id=str(d.get("id") or d.get("indexador") or f"segmento[{indice}]"),
            indexador=str(d.get("indexador") or ""),
            tipo_indexador=tipo,
            aplicacao=str(d.get("aplicacao") or "").strip(),
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
            return (
                "OK — cobertura íntegra, sem englobamento concorrente e sem virada "
                "de tipo de indexador desacompanhada de ajuste de defasagem."
            )
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


def _valida_r3(
    componente: str,
    condicao_txt: str,
    provedores: Sequence[Segmento],
) -> list[Violacao]:
    """R3 sobre um universo já resolvido (tronco ∪ ramo), em ordem cronológica.

    Examina pares CONSECUTIVOS. Um par só é virada quando os dois segmentos
    nomeiam indexadores diferentes; trocar fundamento, condição ou página não
    move a régua de defasagem.
    """
    violacoes: list[Violacao] = []
    ordenados = sorted(
        provedores,
        key=lambda s: (competencia_para_indice(s.inicio), competencia_para_indice(s.fim)),
    )
    for anterior, seguinte in zip(ordenados, ordenados[1:]):
        ta, tb = anterior.tipo_indexador, seguinte.tipo_indexador

        # Sem o campo em alguma das pontas não há o que comparar. Não se
        # inventa tipo, e tampouco se acusa quem ainda não o declara.
        if not ta or not tb:
            continue

        # Mesmo indexador dos dois lados: não é virada.
        if anterior.indexador and anterior.indexador == seguinte.indexador:
            continue

        # Fora do alcance de R3: sem índice, ou índice que não é de inflação.
        if "nao-indexador" in (ta, tb) or "englobante" in (ta, tb):
            continue

        janela = (seguinte.inicio, seguinte.fim)

        if "indeterminado" in (ta, tb):
            violacoes.append(Violacao(
                regra="R3-INDETERMINADO",
                componente=componente,
                condicao=condicao_txt,
                inicio=janela[0],
                fim=janela[1],
                segmentos=[anterior.id, seguinte.id],
                mensagem=(
                    f"virada de indexador com tipo indeterminado em uma das pontas "
                    f"({anterior.id}={ta} → {seguinte.id}={tb}) — R3 NÃO PODE SER "
                    f"VERIFICADA; classificação sem fonte é pendência, não aprovação"
                ),
            ))
            continue

        if ta in TIPOS_COM_DEFASAGEM and tb in TIPOS_COM_DEFASAGEM and ta != tb:
            if seguinte.aplicacao:
                continue
            violacoes.append(Violacao(
                regra="R3",
                componente=componente,
                condicao=condicao_txt,
                inicio=janela[0],
                fim=janela[1],
                segmentos=[anterior.id, seguinte.id],
                mensagem=(
                    f"virada {ta} → {tb} sem ajuste de defasagem declarado em "
                    f"'aplicacao' — desloca o cálculo em um mês (item 4.1.2.4, "
                    f"pagina_pdf 42)"
                ),
            ))
    return violacoes


def valida_cobertura(
    segmentos: Iterable[Any],
    inicio: str | None = None,
    fim: str | None = None,
    componentes: Sequence[str] | None = None,
    dominio_condicoes: Mapping[str, Sequence[str]] | None = None,
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

    SEM_CONDICAO: tuple[tuple[str, str], ...] = ()

    for componente in componentes:
        fornecem = [s for s in normalizados if s.fornece(componente)]
        if not fornecem:
            continue

        # Universos deste componente. Ramos com condição distinta não concorrem
        # entre si; o tronco incondicional entra em todos eles.
        tronco = [s for s in fornecem if s.condicao == SEM_CONDICAO]
        condicoes = []
        for s in fornecem:
            if s.condicao != SEM_CONDICAO and s.condicao not in condicoes:
                condicoes.append(s.condicao)

        universos = [
            (c, tronco + [s for s in fornecem if s.condicao == c])
            for c in condicoes
        ]

        # Valor de domínio declarado que nenhum segmento cobre é universo
        # legítimo: só o tronco o atende, e a lacuna precisa aparecer.
        dominios = dominio_condicoes or {}
        eixos = {k for c in condicoes for k, _ in c}
        declarados = {e for e in eixos if e in dominios}
        for eixo in sorted(declarados):
            vistos = {v for c in condicoes for k, v in c if k == eixo}
            for valor in dominios[eixo]:
                if valor not in vistos:
                    universos.append((((eixo, valor),), list(tronco)))

        # Exaustivo só quando TODO eixo em uso tem domínio declarado. Fora
        # disso o caso "nenhuma condição se aplica" continua sendo cobrado.
        exaustivo = bool(eixos) and eixos == declarados
        if not condicoes or not exaustivo:
            universos.insert(0, (SEM_CONDICAO, list(tronco)))

        for condicao, provedores in universos:
            condicao_txt = (
                "(sem condição)" if condicao == SEM_CONDICAO
                else ", ".join(f"{k}={v}" for k, v in condicao)
            )

            # A janela vem de TODOS os segmentos que fornecem o componente, não
            # só dos deste universo: um universo pode estar vazio — é justamente
            # o caso do ramo declarado no domínio que nenhum segmento cobre — e
            # ainda assim precisa ser cobrado na janela dos demais.
            jan_ini = competencia_para_indice(inicio) if inicio else min(
                competencia_para_indice(s.inicio) for s in fornecem
            )
            jan_fim = competencia_para_indice(fim) if fim else max(
                competencia_para_indice(s.fim) for s in fornecem
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

            relatorio.violacoes.extend(_valida_r3(componente, condicao_txt, provedores))

    # Colisão entre dois segmentos do TRONCO é um fato só. Como o tronco entra
    # em todo ramo, ela reapareceria uma vez por ramo e inflaria a contagem.
    # Aqui vira uma violação, rotulada "(tronco)".
    _sem_cond = {s.id for s in normalizados if s.condicao == ()}
    _vistas: set[tuple] = set()
    _unicas = []
    for v in relatorio.violacoes:
        if v.segmentos and all(x in _sem_cond for x in v.segmentos):
            chave = (v.regra, v.componente, v.inicio, v.fim, tuple(v.segmentos))
            if chave in _vistas:
                continue
            _vistas.add(chave)
            v.condicao = "(tronco)"
        _unicas.append(v)
    relatorio.violacoes = _unicas

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

    parser = argparse.ArgumentParser(description="Valida R1, R2 e R3 de uma tabela normativa.")
    parser.add_argument("tabela", help="caminho do JSON da tabela normativa")
    parser.add_argument("--inicio", help="competência inicial exigida (YYYY-MM)")
    parser.add_argument("--fim", help="competência final exigida (YYYY-MM), tipicamente a data-base")
    args = parser.parse_args(argv)

    relatorio = valida_cobertura(carrega_segmentos(args.tabela), args.inicio, args.fim)
    print(relatorio)
    return 0 if relatorio.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
