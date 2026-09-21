"""Gerador one-shot não pode estragar o que a curadoria escreveu depois dele.

**O DEFEITO QUE ESTE ARQUIVO EXISTE PARA IMPEDIR, e ele já aconteceu.**
`gera_cadeias_bloco19.py` regravava 4 das 20 cadeias e desfazia a tokenização de
`aplicacao` do bloco 23 — três testes caíam. `extrai_bloco_01.py` apagava 20
linhas de proveniência de R3 em 6 `serie-*.csv`. `migra_bloco19_tipos.py`
afirmava idempotência no próprio cabeçalho e reescrevia uma cadeia.

**Nenhum dos três era testado.** É o mesmo argumento do bloco 17 que fundou
`test_ponteiros.py`: *o que se corrige sem teste volta.*

O QUE SE COBRA AQUI, E POR QUE ASSIM
--------------------------------------
Duas coisas, e as duas são necessárias:

  1. **RODAR o gerador não muda byte nenhum do repositório.** É a asserção
     direta, e é a que morde. Roda de verdade — subprocesso, `argv` vazio — e
     compara a árvore antes e depois. Se a guarda sumir, o arquivo muda e o
     teste falha;

  2. **a guarda DETECTA divergência plantada.** Prova contra vacuidade: uma
     guarda que nunca recusa passa no item 1 por não fazer nada. Aqui se planta
     a divergência num diretório temporário e se exige a recusa, com o código
     de saída certo.

**Por que não "rodar o gerador e depois a suíte inteira"?** Porque o enunciado
do defeito era *"regrava e 3 testes caem"* — mas a suíte leva ~28s, e um teste
que dispara a suíte de dentro da suíte é recursão a se evitar. **Byte igual é
condição mais forte:** se nenhum arquivo muda, nenhum teste pode passar a
falhar. O item 1 implica o enunciado e não depende de qual teste é.

`extrai_bloco_01.py` depende do **PDF do TRT-3, que vive fora do repositório**
(`docs/calculo/fontes.md`). Sem ele o teste **pula com a razão escrita** — não
finge que passou.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SCRIPTS = RAIZ / "scripts" / "calculo"
sys.path.insert(0, str(SCRIPTS))

import caminhos_de_skill  # noqa: E402
import escrita_curada  # noqa: E402

#: As árvores que um gerador pode tocar. `extrai_bloco_01.py` escreve nas duas.
VIGIADAS = (
    caminhos_de_skill.REGRAS_ATUALIZACAO,
    caminhos_de_skill.REGRAS_LIQUIDACAO,
    RAIZ / "docs" / "calculo" / "extracao" / "trabalhista",
)


def impressao_digital() -> dict[str, str]:
    """Caminho → sha256 de cada arquivo das árvores vigiadas."""
    estado: dict[str, str] = {}
    for base in VIGIADAS:
        for p in sorted(base.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                estado[p.relative_to(RAIZ).as_posix()] = hashlib.sha256(
                    p.read_bytes()).hexdigest()
    return estado


def roda(script: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        cwd=str(RAIZ),
    )


class TestGeradorNaoEstragaArtefatoCurado(unittest.TestCase):

    def _nao_mexeu(self, script: str, *args: str,
                   permitir_pular: bool = False) -> None:
        antes = impressao_digital()
        r = roda(script, *args)
        depois = impressao_digital()
        if permitir_pular and r.returncode != 0 and "PyMuPDF" in (r.stdout + r.stderr):
            self.skipTest(
                f"{script} depende do PDF do TRT-3 e de PyMuPDF, que vivem fora "
                "do repositório (docs/calculo/fontes.md). Não se finge que passou."
            )
        mudados = sorted(
            k for k in set(antes) | set(depois) if antes.get(k) != depois.get(k)
        )
        self.assertEqual(
            mudados, [],
            f"{script} alterou artefato ao ser re-rodado. A guarda de "
            "escrita_curada.grava_lote deixou de valer — e é exatamente por "
            "aqui que a tokenização do bloco 23 se perdia.",
        )
        self.assertIn(r.returncode, (0, escrita_curada.EXIT_RECUSA), r.stderr[-2000:])

    def test_gera_cadeias_bloco18_nao_mexe(self):
        self._nao_mexeu("gera_cadeias_bloco18.py")

    def test_gera_cadeias_bloco19_nao_mexe(self):
        """O caso do enunciado: era ele que desfazia a tokenização."""
        self._nao_mexeu("gera_cadeias_bloco19.py")

    def test_migra_bloco19_tipos_nao_mexe(self):
        self._nao_mexeu("migra_bloco19_tipos.py")

    def test_extrai_bloco_01_nao_mexe(self):
        """**Escopo reduzido de propósito, e o custo foi medido.** Rodar o
        extrator inteiro leva **~150 s** — mais de cinco vezes a suíte toda, que
        roda em ~28 s. Suíte que demora é suíte que se deixa de rodar, e
        validador ignorado é pior que validador ausente. As três seções aqui —
        `18.10`, `18.11`, `18.12` — são **três dos seis CSV que o extrator
        danificava**, e cobrem as duas famílias de escrita (`grava_csv` e as
        linhas de proveniência de R3). Custam **~4 s**. O que fica de fora é
        mais do mesmo caminho de código, não outro caminho.
        """
        self._nao_mexeu("extrai_bloco_01.py", "18.10", "18.11", "18.12",
                        permitir_pular=True)


class TestGuardaDetectaDivergenciaPlantada(unittest.TestCase):
    """Prova contra vacuidade: guarda que nunca recusa passa na classe acima."""

    def test_identico_nao_escreve_e_inexistente_escreve(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            igual = raiz / "igual.json"
            igual.write_text("{}\n", encoding="utf-8")
            marca = igual.stat().st_mtime_ns
            novo = raiz / "sub" / "novo.json"
            estados = escrita_curada.grava_lote(
                [(igual, "{}\n"), (novo, "[]\n")])
            self.assertEqual(estados[igual], "nada-a-fazer")
            self.assertEqual(estados[novo], "criado")
            self.assertEqual(igual.stat().st_mtime_ns, marca, "tocou sem precisar")
            self.assertEqual(novo.read_text(encoding="utf-8"), "[]\n")

    def test_divergente_recusa_o_lote_inteiro_e_nada_e_escrito(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d)
            curado = raiz / "curado.json"
            curado.write_text('{"aplicacao_literal": "a partir do mês seguinte"}\n',
                              encoding="utf-8")
            inocente = raiz / "inocente.json"
            with self.assertRaises(escrita_curada.ArtefatoCurado) as ctx:
                escrita_curada.grava_lote(
                    [(inocente, "[]\n"), (curado, "{}\n")])
            self.assertEqual(ctx.exception.divergentes, [curado])
            # ATÔMICO: o inocente do mesmo lote também NÃO foi escrito.
            self.assertFalse(inocente.exists(), "o lote não foi atômico")
            self.assertIn("aplicacao_literal", curado.read_text(encoding="utf-8"))

    def test_forcar_sobrescreve_e_diz_que_sobrescreveu(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            alvo = Path(d) / "x.json"
            alvo.write_text("velho\n", encoding="utf-8")
            estados = escrita_curada.grava_lote([(alvo, "novo\n")], forcar=True)
            self.assertEqual(estados[alvo], "sobrescrito")
            self.assertEqual(alvo.read_text(encoding="utf-8"), "novo\n")

    def test_a_mensagem_de_recusa_diz_o_que_fazer(self):
        erro = escrita_curada.ArtefatoCurado([RAIZ / "docs" / "x.json"])
        msg = escrita_curada.explica_recusa(erro, RAIZ, "gera_cadeias_bloco19.py")
        self.assertIn("--forcar", msg)
        self.assertIn("docs/x.json", msg)
        self.assertIn("Nada foi escrito", msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
