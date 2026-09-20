#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera `docs/calculo/consolidado/00-numeros.md` a partir do ESTADO REAL.

POR QUE ESTE SCRIPT EXISTE
--------------------------
O bloco 19 publicou *"R1 e R2 não se moveram"* em quatro arquivos depois de R1
ter ido a 21. O bloco 18 deixou *"14 ok, 10 erros"* num runbook depois de os
erros sumirem. O bloco 17 deixou *"97 de 97 segmentos"* depois de virarem 126.

O padrão é o mesmo, e é estrutural: **número de resultado digitado é cópia sem
dono, e cópia sem dono envelhece em silêncio.** Número de resultado passa a ter
UM dono — este script — e os demais arquivos apontam para o artefato que ele
escreve, em vez de repetir o valor.

O QUE É "NÚMERO DE RESULTADO", E O QUE NÃO É
--------------------------------------------
  RESULTADO  — sai de contar o repositório ou de executar um validador. Muda
               sozinho quando qualquer outro arquivo muda. **Mora aqui.**
  CONTEÚDO NORMATIVO — 42,72% em jan./1989, 0,5% a.m., art. 457, `pagina_pdf`
               42. É o DADO. Não é contado, não é gerado, e este script não o
               toca.
  RELATÓRIO DE BLOCO — "o bloco 18 fechou com 15 cadeias". Registro datado.
               Relatório que se atualiza sozinho deixa de ser registro.

TRÊS EXIGÊNCIAS DE DESENHO, E COMO CADA UMA FOI ATENDIDA
---------------------------------------------------------
1. **Cabeçalho que se declare gerado.** A primeira linha do arquivo diz que ele
   é gerado e dá o comando que o regenera. Quem editar à mão é avisado de que
   será sobrescrito.

2. **Sem timestamp automático.** `Date.now()` em arquivo versionado produz diff
   a cada rodada e polui o histórico — o ruído passa a esconder a mudança real.
   Data só entra por `--data AAAA-MM-DD`, explícita, de quem roda.

3. **Determinístico.** Toda iteração é sobre coleção ORDENADA; nenhuma depende
   de ordem de `dict` vinda de I/O, de `set`, nem de hash. Duas rodadas seguidas
   sem mudança no repositório produzem bytes idênticos.
   `test_numeros.py::TestDeterminismo` prova isso rodando o gerador duas vezes.

POR QUE EXECUTAR OS VALIDADORES EM SUBPROCESSO, E NÃO REIMPLEMENTAR A CONTA
---------------------------------------------------------------------------
R1/R2/R3 e o placar de `valida_bloco_tabelas.py` PODERIAM ser recalculados aqui
importando `valida_cobertura`. Seria uma segunda implementação da mesma conta —
e duas implementações divergem: é exatamente o defeito que esta tarefa conserta,
só que em código em vez de em prosa. O número publicado tem de ser **o que o
validador imprime**, não um valor parecido. Por isso: subprocesso, e parse da
saída com `_exige()`, que ABORTA se o formato mudar. Gerador que falha alto é
melhor que gerador que publica silêncio.

`valida_cadeias.py` roda com `--sem-atualizar-manifesto`: gerar um relatório não
pode ter efeito colateral sobre o dado que o relatório descreve.

A RECURSÃO, E COMO ELA É CORTADA
---------------------------------
O gerador roda a suíte (`unittest discover`). A suíte contém `test_numeros.py`,
que roda o gerador. Sem corte, isso não termina. O corte é a variável de
ambiente `GERA_NUMEROS_EM_CURSO`: o gerador a exporta para o subprocesso da
suíte, e `test_numeros.py` PULA a regeneração quando a vê. A profundidade fica
em dois, e nenhum dos dois lados precisa saber o nome do outro teste.

O QUE NÃO ENTRA NESTE ARQUIVO, E POR QUÊ
-----------------------------------------
**Pendências abertas por família.** `docs/calculo/pendencias.md` não é contável
por script com confiança: a numeração das seções é heterogênea (`9-A`, `9-B`,
sem 10, 13 fora de ordem), "aberta" e "fechada" aparecem em prosa e em tabela,
uma mesma seção mistura fechadas e abertas (`§ 20.1` FECHADAS dentro do bloco
11A-12), e sub-pendências são tanto `### 15.1` quanto linha de tabela. Qualquer
regex daria um número com aparência de exatidão e sem lastro. **Número inventado
é pior que número ausente**, e a § 9 deste arquivo diz isso em vez de contar.

Aritmética inteira em toda parte. Nenhum `float` (R12). `encoding='utf-8'`
explícito em toda leitura e escrita.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SCRIPTS = RAIZ / "scripts" / "calculo"
TABELAS = RAIZ / "docs" / "calculo" / "tabelas-normativas"
CONSOLIDADO = RAIZ / "docs" / "calculo" / "consolidado"
SKILLS = RAIZ / "skills"
DESTINO = CONSOLIDADO / "00-numeros.md"

COMANDO = "python scripts/calculo/gera_numeros.py"
MARCA_RECURSAO = "GERA_NUMEROS_EM_CURSO"

LIMITE_SKILL = 500


# --------------------------------------------------------------------------
# Execução de subprocesso e parse defensivo
# --------------------------------------------------------------------------

def _roda(argv: list[str]) -> str:
    """Roda um script do repositório e devolve stdout+stderr como texto.

    `encoding='utf-8'` explícito: o console do Windows é cp1252 e engasga com
    travessão, que a saída dos validadores usa.
    """
    ambiente = dict(os.environ)
    ambiente["PYTHONIOENCODING"] = "utf-8"
    ambiente[MARCA_RECURSAO] = "1"
    proc = subprocess.run(
        [sys.executable, *argv],
        cwd=str(RAIZ),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=ambiente,
    )
    return (proc.stdout or "") + (proc.stderr or "")


def _exige(padrao: str, texto: str, o_que: str) -> re.Match:
    """Parse que ABORTA se o formato mudar.

    Um gerador que não acha o que procura e publica zero é pior que um gerador
    que morre: o zero vira número digitado com cara de medido.
    """
    m = re.search(padrao, texto)
    if m is None:
        raise SystemExit(
            f"gera_numeros: não achei {o_que} na saída do validador.\n"
            f"  padrão: {padrao}\n"
            f"  O FORMATO DA SAÍDA MUDOU — conserte este parse; não publique "
            f"número sem lastro.\n--- saída ---\n{texto[-2000:]}"
        )
    return m


# --------------------------------------------------------------------------
# Contagens do repositório
# --------------------------------------------------------------------------

def cadeias() -> list[dict]:
    """Toda cadeia temporal, em ordem de `id`. Reconhecida pelo CAMPO `tipo`.

    Nunca pelo nome do arquivo — a renomeação `trt3.hist.*` → `trab.hist.*` do
    bloco 17 derrubou a descoberta por prefixo de 11 para 7 em silêncio.
    """
    achadas: list[dict] = []
    for caminho in sorted(TABELAS.glob("*.json")):
        try:
            dados = json.loads(caminho.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            continue
        if dados.get("tipo") != "cadeia-temporal":
            continue
        if not isinstance(dados.get("segmentos"), list):
            continue
        achadas.append(
            {
                "id": dados.get("id") or caminho.stem,
                "arquivo": caminho.name,
                "componente": dados.get("componente", "—"),
                "segmentos": dados["segmentos"],
            }
        )
    achadas.sort(key=lambda c: c["id"])
    return achadas


def distribuicao_de_tipo(todas: list[dict]) -> list[tuple[str, int]]:
    """Ordenada por contagem desc., e por nome para desempatar. Determinismo."""
    conta: collections.Counter = collections.Counter()
    for cadeia in todas:
        for seg in cadeia["segmentos"]:
            conta[seg.get("tipo_indexador", "(campo ausente)")] += 1
    return sorted(conta.items(), key=lambda par: (-par[1], par[0]))


def rotulos(todas: list[dict]) -> list[str]:
    """Rótulos DISTINTOS de indexador. Segmento sem `indexador` não tem rótulo —
    é o caso de `taxa` pura e de `padrao-monetario`; não se inventa um.

    `indexador: null` conta como SEM rótulo, igual a campo ausente: o dado diz
    'não há índice aqui', e tratar `None` como rótulo criaria um rótulo que
    ninguém escreveu.
    """
    vistos = set()
    for cadeia in todas:
        for seg in cadeia["segmentos"]:
            rotulo = seg.get("indexador")
            if isinstance(rotulo, str) and rotulo:
                vistos.add(rotulo)
    return sorted(vistos)


def segmentos_sem_indexador(todas: list[dict]) -> int:
    return sum(
        1
        for c in todas
        for s in c["segmentos"]
        if not isinstance(s.get("indexador"), str) or not s.get("indexador")
    )


def arquivos_de_teste() -> list[tuple[str, int]]:
    """(nome, quantos `def test_`). Ordenado por nome."""
    fora = []
    for caminho in sorted(SCRIPTS.glob("test_*.py")):
        texto = caminho.read_text(encoding="utf-8")
        fora.append((caminho.name, len(re.findall(r"^\s*def test_", texto, re.M))))
    return fora


def skills_md() -> list[tuple[str, int]]:
    """(caminho relativo, linhas) de cada SKILL.md. O limite de 500 é o que a
    contagem torna verificável — declarar o limite sem medi-lo é promessa."""
    fora = []
    for caminho in sorted(SKILLS.glob("*/SKILL.md")):
        linhas = len(caminho.read_text(encoding="utf-8").splitlines())
        fora.append((caminho.relative_to(RAIZ).as_posix(), linhas))
    return fora


def conta_arquivos() -> list[tuple[str, int]]:
    """Inventário de artefatos. Cada linha declara O QUE conta, não só quanto."""
    refs = sorted(SKILLS.glob("*/references/*.md"))
    return [
        ("`docs/calculo/consolidado/` — arquivos `.md`",
         len(sorted(CONSOLIDADO.glob("*.md")))),
        ("`skills/` — arquivos `.md`, em toda a árvore",
         len(sorted(SKILLS.rglob("*.md")))),
        ("`skills/*/SKILL.md` — skills publicadas",
         len(sorted(SKILLS.glob("*/SKILL.md")))),
        ("`skills/*/references/*.md`", len(refs)),
        ("`docs/calculo/tabelas-normativas/*.json` — todos",
         len(sorted(TABELAS.glob("*.json")))),
    ]


# --------------------------------------------------------------------------
# Validadores
# --------------------------------------------------------------------------

def placar_cadeias() -> dict:
    saida = _roda(["scripts/calculo/valida_cadeias.py", "--sem-atualizar-manifesto"])
    m = _exige(
        r"(\d+) cadeias \| R1: (\d+) violações \| R2: (\d+) violações \| "
        r"R3: (\d+) violações",
        saida,
        "a linha de fecho de valida_cadeias.py",
    )
    # A composição de R3 não está na linha de fecho: vem de contar as linhas de
    # violação. `[R3]` é virada CONFIRMADA; `[R3-INDETERMINADO]` é virada que
    # NÃO PODE ser verificada porque uma das pontas não tem tipo em fonte. As
    # duas somam o R3 do fecho, e a soma é conferida logo abaixo — se um dia
    # surgir uma terceira marca, o gerador para em vez de publicar conta que
    # não fecha.
    confirmadas = len(re.findall(r"^\s*\[R3\]", saida, re.M))
    indeterminadas = len(re.findall(r"^\s*\[R3-INDETERMINADO\]", saida, re.M))
    total_r3 = int(m.group(4))
    if confirmadas + indeterminadas != total_r3:
        raise SystemExit(
            f"gera_numeros: a composição de R3 não fecha — "
            f"{confirmadas} confirmadas + {indeterminadas} indeterminadas "
            f"!= {total_r3} do fecho. Apareceu marca de R3 que este parse não "
            f"conhece; conserte antes de publicar."
        )
    return {
        "cadeias": int(m.group(1)),
        "r1": int(m.group(2)),
        "r2": int(m.group(3)),
        "r3": total_r3,
        "r3_confirmadas": confirmadas,
        "r3_indeterminadas": indeterminadas,
    }


def placar_tabelas() -> dict:
    saida = _roda(["scripts/calculo/valida_bloco_tabelas.py"])
    m = _exige(
        r"resumo: (\d+) ok, (\d+) divergências, (\d+) não verificados, (\d+) erros",
        saida,
        "a linha de resumo de valida_bloco_tabelas.py",
    )
    return {
        "ok": int(m.group(1)),
        "divergencias": int(m.group(2)),
        "nao_verificados": int(m.group(3)),
        "erros": int(m.group(4)),
    }


def placar_testes() -> dict:
    saida = _roda(["-m", "unittest", "discover", "-s", "scripts/calculo",
                   "-p", "test_*.py"])
    m = _exige(r"Ran (\d+) tests?", saida, "a linha 'Ran N tests' da suíte")
    return {
        "executados": int(m.group(1)),
        "resultado": "OK" if re.search(r"^OK", saida, re.M) else "FALHOU",
    }


# --------------------------------------------------------------------------
# Escrita
# --------------------------------------------------------------------------

def monta(data: str | None = None) -> str:
    todas = cadeias()
    total_segmentos = sum(len(c["segmentos"]) for c in todas)
    tipos = distribuicao_de_tipo(todas)
    labels = rotulos(todas)
    testes = arquivos_de_teste()
    total_def_test = sum(n for _, n in testes)
    skills = skills_md()
    inventario = conta_arquivos()

    cad = placar_cadeias()
    tab = placar_tabelas()
    sui = placar_testes()

    L: list[str] = []
    a = L.append

    a("<!-- ARQUIVO GERADO. NÃO EDITE À MÃO: será sobrescrito. -->")
    a(f"<!-- Regenere com: {COMANDO} -->")
    a("")
    a("# Números do repositório — **gerado por script**")
    a("")
    a("> **Este arquivo é gerado a partir do estado real, não digitado.**")
    a(">")
    a(f"> ```")
    a(f"> {COMANDO}")
    a("> ```")
    a(">")
    a("> Toda contagem abaixo sai de **contar o repositório** ou de **executar o")
    a("> validador**. Nenhuma é transcrita de outro arquivo.")
    a(">")
    a("> **Este é o único lugar do repositório onde número de RESULTADO é")
    a("> publicado.** Os demais arquivos apontam para cá. Número de **conteúdo")
    a("> normativo** — 42,72% em jan./1989, 0,5% a.m., `pagina_pdf` 42 — não é")
    a("> resultado, é o dado, e continua onde sempre esteve. Número em")
    a("> **relatório de bloco** é registro datado e **não** se atualiza: um")
    a("> relatório que se atualiza sozinho deixa de ser registro.")
    a(">")
    a("> **Sem timestamp automático**, de propósito: data gerada produziria diff")
    a("> a cada rodada e o ruído esconderia a mudança real. Se precisar de data,")
    a(f"> passe `--data AAAA-MM-DD`.")
    if data:
        a(">")
        a(f"> **Estado de referência declarado: {data}.**")
    a("")
    a("---")
    a("")

    # § 1
    a("## 1. Cadeias temporais")
    a("")
    a("Contado dos `.json` de `docs/calculo/tabelas-normativas/` com")
    a("`tipo == \"cadeia-temporal\"` — **pelo campo, nunca pelo nome do arquivo**.")
    a("")
    a(f"| cadeias | **{len(todas)}** |")
    a("|---|---|")
    a(f"| segmentos | **{total_segmentos}** |")
    a(f"| rótulos de indexador **nomeados**, distintos | **{len(labels)}** |")
    a(f"| segmentos sem rótulo utilizável | **{segmentos_sem_indexador(todas)}** |")
    a(f"| rótulos **na convenção do catálogo** | **{len(labels) + 1}** |")
    a("")
    a("Segmento sem rótulo utilizável é `taxa` pura, `padrao-monetario`, ou o")
    a("único com `indexador: null` — `taxa` e moeda não têm índice a classificar,")
    a("e `null` é o dado dizendo isso, não um rótulo que alguém escreveu.")
    a("")
    a("**As duas últimas linhas não se contradizem, e a diferença é declarada:**")
    a("`indexadores-tipo-catalogo.json` conta `(segmento sem indexador)` **como um")
    a("rótulo** da classe `nao-indexador`, porque para ele a pergunta é *\"que")
    a("classe de R3 se aplica?\"* e *\"nenhuma\"* é resposta. A primeira linha conta")
    a("só o que tem **nome**. A convenção do catálogo é a que a `§ 25.4` de")
    a("`../pendencias.md` usa; mantida aqui para não criar um terceiro número.")
    a("")
    a("### 1.1 Segmentos por cadeia")
    a("")
    a("Publicado por cadeia porque as `references/` descrevem cadeias uma a uma:")
    a("é contra esta tabela que se confere cada menção.")
    a("")
    a("| cadeia (`id`) | componente | segmentos |")
    a("|---|---|---|")
    for c in todas:
        a(f"| `{c['id']}` | {c['componente']} | {len(c['segmentos'])} |")
    a("")

    # § 2
    a("## 2. Distribuição de `tipo_indexador`")
    a("")
    a("Sobre os segmentos das cadeias acima. `indeterminado` **bloqueia R3** — não")
    a("é neutro nem é aprovação.")
    a("")
    a("| `tipo_indexador` | segmentos |")
    a("|---|---|")
    for nome, quantos in tipos:
        a(f"| `{nome}` | {quantos} |")
    a(f"| **total** | **{total_segmentos}** |")
    a("")

    # § 3
    a("## 3. Invariantes R1 · R2 · R3")
    a("")
    a("**Executando** `valida_cadeias.py --sem-atualizar-manifesto`. Gerar")
    a("relatório não pode alterar o dado que o relatório descreve.")
    a("")
    a("| | violações |")
    a("|---|---|")
    a(f"| **R1** — englobamento concorrente | **{cad['r1']}** |")
    a(f"| **R2** — lacuna de cobertura do componente próprio | **{cad['r2']}** |")
    a(f"| **R3** — virada de tipo sem ajuste de defasagem | **{cad['r3']}** |")
    a("")
    a("**Composição de R3**, contada das linhas de violação:")
    a("")
    a("| | violações | o que significa |")
    a("|---|---|---|")
    a(f"| `[R3]` — **confirmada** | **{cad['r3_confirmadas']}** | as duas pontas "
      "têm tipo em fonte, e a virada não declara ajuste |")
    a(f"| `[R3-INDETERMINADO]` | **{cad['r3_indeterminadas']}** | uma das pontas "
      "não tem tipo em fonte — **R3 não pôde ser verificada**; é pendência, "
      "não aprovação |")
    a(f"| **soma** | **{cad['r3']}** | confere com o fecho do validador |")
    a("")
    a("> **Toda violação acima é do MANUAL, transcrita como está.** Nenhuma foi")
    a("> harmonizada. A leitura de cada uma está nos relatórios dos blocos 8 e 9.")
    a("")

    # § 4
    a("## 4. `valida_bloco_tabelas.py`")
    a("")
    a("**Executando.** Divergência é resultado esperado do trabalho — é defeito")
    a("do original, registrado e não consertado. **Só `erros` é defeito nosso**,")
    a("e só `erros` faz o validador sair não-zero.")
    a("")
    a("| | |")
    a("|---|---|")
    a(f"| ok | **{tab['ok']}** |")
    a(f"| divergências (do original) | **{tab['divergencias']}** |")
    a(f"| não verificados mecanicamente | **{tab['nao_verificados']}** |")
    a(f"| **erros (da extração)** | **{tab['erros']}** |")
    a("")

    # § 5
    a("## 5. Testes")
    a("")
    a("Duas contagens, e elas respondem coisas diferentes: `def test_` é o que")
    a("**está escrito**; `Ran N` é o que **rodou**. Divergirem é sinal — teste")
    a("não coletado, arquivo fora do padrão de descoberta, erro de importação.")
    a("")
    a("| arquivo | `def test_` |")
    a("|---|---|")
    for nome, quantos in testes:
        a(f"| `scripts/calculo/{nome}` | {quantos} |")
    a(f"| **total escrito** | **{total_def_test}** |")
    a("")
    a(f"**Executados:** `python -m unittest discover -s scripts/calculo "
      f"-p \"test_*.py\"` → **{sui['executados']} testes, {sui['resultado']}**.")
    a("")

    # § 6
    a("## 6. Arquivos")
    a("")
    a("| o que se conta | quantos |")
    a("|---|---|")
    for descricao, quantos in inventario:
        a(f"| {descricao} | **{quantos}** |")
    a("")

    # § 7
    a("## 7. Linhas das `SKILL.md` — o limite de 500 é verificável")
    a("")
    a("O limite existe para que a skill caiba na leitura de entrada; declará-lo")
    a("sem medi-lo seria promessa. Aqui ele é **medido**, e")
    a("`test_numeros.py` faz dele **teste**.")
    a("")
    a(f"| `SKILL.md` | linhas | limite {LIMITE_SKILL} |")
    a("|---|---|---|")
    for caminho, linhas in skills:
        folga = LIMITE_SKILL - linhas
        marca = f"cabe, folga de {folga}" if folga >= 0 else f"**ESTOUROU em {-folga}**"
        a(f"| `{caminho}` | {linhas} | {marca} |")
    a("")

    # § 8
    a("## 8. O que este arquivo NÃO conta, e por quê")
    a("")
    a("**Pendências abertas, por família.** `docs/calculo/pendencias.md` **não é**")
    a("**contável por script com confiança**, e o motivo não é preguiça de regex:")
    a("")
    a("- a numeração das seções é heterogênea — há `9-A` e `9-B`, não há `10`, e a")
    a("  `14` vem depois da `16`. Ordem de seção não é ordem de pendência;")
    a("- *aberta* e *fechada* aparecem ora em prosa, ora em linha de tabela, ora")
    a("  no título da subseção (`### 20.1 FECHADAS pelo bloco 12`) — e uma mesma")
    a("  seção mistura as duas coisas;")
    a("- sub-pendência é tanto `### 15.1` quanto linha de tabela sem título")
    a("  próprio. Não há unidade contável estável.")
    a("")
    a("Qualquer regex produziria um número com **aparência de exatidão e sem**")
    a("**lastro** — e número inventado é pior que número ausente, porque o")
    a("primeiro é usado. **Enquanto a pendência não tiver campo, a contagem fica")
    a("fora daqui.** Para saber o que está aberto, leia `../pendencias.md`.")
    a("")
    a("> O caminho para tornar isso contável já está proposto na `§ 26.1` de")
    a("> `../pendencias.md`: **campo, não prosa**. Quando existir, esta seção vira")
    a("> tabela.")
    a("")
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Gera docs/calculo/consolidado/00-numeros.md do estado real."
    )
    parser.add_argument(
        "--data",
        default=None,
        help="Data de referência, AAAA-MM-DD. NÃO é automática de propósito: "
             "timestamp gerado polui o diff de todo commit.",
    )
    parser.add_argument(
        "--verifica",
        action="store_true",
        help="Não escreve; sai 1 se o arquivo em disco divergir do gerado.",
    )
    args = parser.parse_args(argv)

    if args.data is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.data):
        raise SystemExit("gera_numeros: --data exige o formato AAAA-MM-DD.")

    conteudo = monta(args.data)

    if args.verifica:
        atual = DESTINO.read_text(encoding="utf-8") if DESTINO.exists() else ""
        if atual == conteudo:
            print(f"em dia: {DESTINO.relative_to(RAIZ).as_posix()}")
            return 0
        print(
            f"DESATUALIZADO: {DESTINO.relative_to(RAIZ).as_posix()} não "
            f"corresponde ao estado real. Rode `{COMANDO}`."
        )
        return 1

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(conteudo, encoding="utf-8")
    print(f"escrito: {DESTINO.relative_to(RAIZ).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
