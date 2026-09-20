"""Testes de valida_bloco_tabelas.py — resolução da faixa de páginas.

O defeito que estes testes trancam: a proveniência era conferida contra uma
constante única do bloco 1 (`range(373, 472)`), enquanto a varredura pegava
TODOS os `serie-*.csv` do diretório. Uma série vinda de outro bloco — 9.2.11,
p178-179 — caía no mesmo diretório e tinha as linhas acusadas de erro de
extração. Falso erro permanente treina quem lê o relatório a ignorá-lo.

A faixa agora se resolve POR ARQUIVO: cabeçalho do próprio CSV, ou contrato de
páginas do item. Os testes cobrem as três saídas possíveis — conforme, fora da
faixa (erro de verdade, que tem de continuar erro) e faixa não declarada (não
verificável, que não pode virar silêncio).

Nenhum float (R12); `encoding='utf-8'` explícito em toda leitura e escrita.
"""

from __future__ import annotations

import json
import pathlib
import tempfile
import unittest

import valida_bloco_tabelas as vbt

CABECALHO_BLOCO_1 = (
    "# OUT_OF_SCOPE — série de valores, não entra na skill.\n"
    "# documento=manual-de-calculo-trabalhista_2016-1.pdf "
    "emissor=TRT-3, Secretaria de Cálculos Judiciais, julho/2016 offset_paginacao=0\n"
)

CABECALHO_OUTRO_BLOCO = (
    "# OUT_OF_SCOPE — serie; manutencao separada\n"
    "# documento=manual-de-calculo-trabalhista_2016-1.pdf item=9.2.11 "
    "tabela='TABELA PRATICA DE ACRESCIMOS LEGAIS - TABELA I' pagina_pdf=178-179\n"
)

JSON_18_1_MINIMO = {
    "parcelas": [
        {"parcela": "aviso prévio indenizado", "paginas_pdf": [373]},
    ]
}


class BaseProveniencia(unittest.TestCase):
    """Monta um diretório de séries de mentira e aponta o validador para ele."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.dir_serie = pathlib.Path(self._tmp.name) / "extracao"
        self.dir_semantica = pathlib.Path(self._tmp.name) / "tabelas-normativas"
        self.dir_serie.mkdir()
        self.dir_semantica.mkdir()
        with open(
            self.dir_semantica / "trt3-18.1-incidencia-parcelas.json",
            "w",
            encoding="utf-8",
        ) as fh:
            json.dump(JSON_18_1_MINIMO, fh, ensure_ascii=False)

        self._serie_original = vbt.DIR_SERIE
        self._semantica_original = vbt.DIR_SEMANTICA
        vbt.DIR_SERIE = self.dir_serie
        vbt.DIR_SEMANTICA = self.dir_semantica
        self.addCleanup(self._restaura)

    def _restaura(self) -> None:
        vbt.DIR_SERIE = self._serie_original
        vbt.DIR_SEMANTICA = self._semantica_original
        self._tmp.cleanup()

    def escreve(self, nome: str, cabecalho: str, linhas: list[str]) -> None:
        corpo = cabecalho + "pagina_pdf,item,valor\n" + "".join(l + "\n" for l in linhas)
        with open(self.dir_serie / nome, "w", encoding="utf-8", newline="") as fh:
            fh.write(corpo)

    def roda(self) -> vbt.Relatorio:
        rel = vbt.Relatorio()
        vbt.valida_proveniencia(rel)
        return rel


class TestCsvDeOutroBlocoNoMesmoDiretorio(BaseProveniencia):
    """O caso que causou o defeito."""

    def test_serie_de_outro_bloco_nao_e_erro_de_extracao(self):
        self.escreve(
            "serie-18.6-irrf-plr.csv", CABECALHO_BLOCO_1,
            ["389,18.6,1", "389,18.6,2"],
        )
        self.escreve(
            "serie-9.2.11-ufir-juros-ate-dez79.csv", CABECALHO_OUTRO_BLOCO,
            ["178,9.2.11,1", "179,9.2.11,2"],
        )
        rel = self.roda()
        self.assertEqual(rel.erros, [])
        self.assertEqual(rel.nao_verificado, [])
        self.assertEqual(len(rel.ok), 1)
        self.assertIn("cabeçalho do próprio arquivo", rel.ok[0])
        self.assertIn("contrato de páginas do item", rel.ok[0])

    def test_faixa_do_outro_bloco_sai_do_cabecalho_e_nao_de_constante(self):
        self.escreve(
            "serie-9.2.11-ufir-juros-ate-dez79.csv", CABECALHO_OUTRO_BLOCO,
            ["178,9.2.11,1"],
        )
        caminho = self.dir_serie / "serie-9.2.11-ufir-juros-ate-dez79.csv"
        faixa, origem = vbt.faixa_declarada(caminho, vbt.le_csv(caminho.name))
        self.assertEqual(faixa, (178, 179))
        self.assertEqual(origem, "cabeçalho do próprio arquivo")


class TestErroDeVerdadeContinuaErro(BaseProveniencia):
    """Remover o falso erro não pode ter removido o verdadeiro."""

    def test_linha_do_bloco_1_fora_do_contrato_do_item(self):
        self.escreve(
            "serie-18.6-irrf-plr.csv", CABECALHO_BLOCO_1,
            ["389,18.6,1", "455,18.6,2"],
        )
        rel = self.roda()
        self.assertEqual(len(rel.erros), 1)
        self.assertIn("serie-18.6-irrf-plr.csv:3", rel.erros[0])
        self.assertIn("fora de 389-389", rel.erros[0])

    def test_linha_de_outro_bloco_fora_da_faixa_do_proprio_cabecalho(self):
        self.escreve(
            "serie-9.2.11-ufir-juros-ate-dez79.csv", CABECALHO_OUTRO_BLOCO,
            ["178,9.2.11,1", "999,9.2.11,2"],
        )
        rel = self.roda()
        self.assertEqual(len(rel.erros), 1)
        self.assertIn("fora de 178-179", rel.erros[0])

    def test_pagina_ou_item_ausente_continua_erro(self):
        self.escreve(
            "serie-18.6-irrf-plr.csv", CABECALHO_BLOCO_1,
            [",18.6,1", "389,,2"],
        )
        rel = self.roda()
        self.assertEqual(len(rel.erros), 1)
        self.assertIn("1 linhas sem pagina_pdf e 1 sem item", rel.erros[0])

    def test_json_18_1_fora_da_faixa_do_item(self):
        self.escreve("serie-18.6-irrf-plr.csv", CABECALHO_BLOCO_1, ["389,18.6,1"])
        with open(
            self.dir_semantica / "trt3-18.1-incidencia-parcelas.json",
            "w",
            encoding="utf-8",
        ) as fh:
            json.dump({"parcelas": [{"parcela": "x", "paginas_pdf": [178]}]}, fh)
        rel = self.roda()
        self.assertEqual(len(rel.erros), 1)
        self.assertIn("fora de 373-380", rel.erros[0])


class TestFaixaNaoDeclarada(BaseProveniencia):
    """Sem faixa declarada o arquivo não é conferível — e isso tem de aparecer."""

    def test_arquivo_sem_faixa_nao_vira_erro_nem_silencio(self):
        self.escreve(
            "serie-99.9-desconhecida.csv",
            "# documento=outro.pdf\n",
            ["1234,99.9,1"],
        )
        rel = self.roda()
        self.assertEqual(rel.erros, [])
        self.assertEqual(len(rel.nao_verificado), 1)
        self.assertIn("serie-99.9-desconhecida.csv", rel.nao_verificado[0])
        self.assertIn("sem faixa de páginas declarada", rel.nao_verificado[0])


class TestDescobertaNaoDependeDoPrefixo(BaseProveniencia):
    """A varredura de proveniência filtrava por `serie-*.csv`. Era a mesma
    classe de defeito do bloco 17: renomear o arquivo tirava-o da conferência
    EM SILÊNCIO, com o resumo ainda dizendo '0 erros'."""

    def test_csv_sem_o_prefixo_serie_continua_sendo_conferido(self):
        self.escreve(
            "18.6-irrf-plr-SEM-PREFIXO.csv", CABECALHO_BLOCO_1,
            ["389,18.6,1", "455,18.6,2"],
        )
        rel = self.roda()
        self.assertEqual(len(rel.erros), 1, "o arquivo renomeado saiu da varredura")
        self.assertIn("18.6-irrf-plr-SEM-PREFIXO.csv:3", rel.erros[0])


class TestContratoDePaginas(unittest.TestCase):
    """Garantias sobre o contrato, lidas do módulo real."""

    def test_nenhuma_constante_de_faixa_do_bloco_sobrou(self):
        self.assertFalse(
            hasattr(vbt, "PAGINAS_DO_BLOCO"),
            "a faixa tem de se resolver por arquivo; constante de bloco foi o defeito",
        )

    def test_itens_do_bloco_1_cobrem_373_a_470_sem_buraco(self):
        faixas = sorted(vbt.FAIXAS_DE_PAGINA.values())
        self.assertEqual(faixas[0][0], 373)
        self.assertEqual(max(f[1] for f in faixas), 470)
        for (_, fim_ant), (ini, _) in zip(faixas, faixas[1:]):
            self.assertLessEqual(ini, fim_ant + 1)


if __name__ == "__main__":
    unittest.main()
