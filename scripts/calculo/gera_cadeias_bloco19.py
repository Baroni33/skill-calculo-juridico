# -*- coding: utf-8 -*-
"""Bloco 19, tarefa 3 — gera as cadeias de `P18-02` que a fonte extraída basta
para sustentar.

`P18-02` arrolou OITO cadeias tabuladas do Manual CJF (Res. 990/2026) sem JSON:
4.5.2, 4.5.3, 4.6.1.1, 4.6.2, 4.6.3, 2.3.2.2, 2.4.2.2.2 e 2.4.4.1.
**Cinco são geradas aqui. Três permanecem bloqueadas por falta de fonte
EXTRAÍDA**, e o porquê de cada uma está em `BLOQUEADAS`, abaixo — a ausência
fica no arquivo que o validador lê, não na prosa.

Disciplina desta tarefa, e ela é a mesma do bloco 18:
  * **nenhum `float`** — percentuais e taxas são strings literais do manual, e
    nada é somado aqui (R12);
  * **`encoding='utf-8'` explícito** em toda escrita e leitura;
  * **todo segmento sai da fonte extraída**, com `fundamento` e `pagina_pdf`.
    Onde a extração não trouxe a taxa, o campo vai `null` com
    `taxa_nao_extraida` — **não se inventa valor**;
  * **nada é harmonizado**: `N-6`, `N-10`, `D8-C8` e `D8-C25` entram como estão.

Descoberta pelo validador: `valida_cadeias.py` reconhece cadeia por
`tipo == "cadeia-temporal"`, logo estes arquivos entram na contagem e no
manifesto automaticamente.
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DEST = Path(__file__).resolve().parents[2] / "docs" / "calculo" / "tabelas-normativas"

CAT = ("tabelas-normativas/indexadores-tipo-catalogo.json — o valor sai da fonte; "
       "sem fonte, indeterminado (bloco 17, tarefa 1)")

JANELA_FIM = "2026-06"
JANELA_POR_QUE_FIM = ("2026-06 é a data-base dos exemplos do próprio manual "
                      "(item 4.2.1.1, pagina_pdf 52).")

# ---------------------------------------------------------------------------
# Textos de `tipo_indexador_fonte` reaproveitados
# ---------------------------------------------------------------------------
NAO_IND_JUROS = ("segmentos de juros cuja regra é percentual legal fixo (1% a.m., "
                 "6% a.a., TRD, poupança) e não índice. Sem índice, R3 não tem o que "
                 "verificar.")
NAO_IND_COMPENSATORIOS = (
    "segmento de JUROS COMPENSATÓRIOS: a regra do manual é percentual de juros, não "
    "índice de correção. Sem índice, R3 não tem o que verificar. O que falta neste "
    "segmento é o VALOR da taxa, e falta de valor não é falta de classe — ver "
    "'taxa_nao_extraida'."
)
NOM = "item 4.1.2.4, letra a, pagina_pdf 42 — nomeado LITERALMENTE na lista de exemplos"

TRD_POR_QUE = (
    "Taxa Referencial Diária. A fonte externa do bloco 19 nomeia TBF, Redutor-R e TR — e "
    "NÃO nomeia a TRD. Estender a razão da TR à TRD por semelhança de nome é a dedução "
    "proibida. Continua SEM FONTE, logo P18-01."
)
TR_FONTE = ("FONTE EXTERNA AO CORPUS (BCB, verificada fora do agente) — TBF, Redutor-R "
            "e TR são divulgados para PERÍODO ENTRE DATAS DE ANIVERSÁRIO, não para mês "
            "calendário (17/02 a 17/03, 03/05 a 03/06, 05/10 a 05/11); e a TR é "
            "PREFIXADA, com variação divulgada para o mês seguinte.")
TR_RAZAO = "período entre datas de aniversário e prefixação"
TR_FECHAMENTO = ("NÃO se fecha esperando fonte. A fonte chegou, e o que ela diz é que a TR "
                 "não cabe em mês calendário — logo não há classe a atribuir. Fecharia só "
                 "se a modelagem ganhar classe para período entre datas de aniversário, ou "
                 "se a cadeia declarar a conversão para competência em 'aplicacao'.")
BTNF_POR_QUE = (
    "Bônus do Tesouro Nacional Fiscal. RÓTULO NOVO no repositório, trazido pelo item "
    "2.4.4.1 (pagina_pdf 35) e pela NOTA 3 do item 4.9.1.1 (pagina_pdf 85). NÃO está na "
    "lista do item 4.1.2.4 — que nomeia o BTN, não o BTNF — e nenhuma fonte do corpus o "
    "classifica. Herdar 'nominal' do BTN 'porque o nome é quase o mesmo' é exatamente a "
    "dedução que o bloco 17 proibiu, e é a mesma classe de erro de 'IPC' × 'IPC/IBGE' e de "
    "'IPC/IBGE' × 'IPC/FGV'. SEM FONTE, logo pendência."
)
COMPOSTO_POR_QUE = (
    "SEGMENTO COMPOSTO: um único registro guarda DOIS indexadores — a UPC e 'os índices "
    "básicos de atualização dos saldos da poupança' —, e o item 2.4.4.1 NÃO DATA a "
    "fronteira entre eles. Um rótulo só não os representa, e escolher um dos dois, ou "
    "arbitrar a data de virada, seria inventar. A correção é partir o segmento quando a "
    "fonte der a data, não classificá-lo. Mesmo desenho de 'Ufir → Selic (bifurcado por "
    "fato gerador)' (P17-03)."
)

PONTA_INICIO_SEM_MES = ("inicio — o manual não dá início; a ponta é materialização de "
                        "janela para permitir a checagem de R1/R2, não afirmação da "
                        "fonte (mesmo desenho de P8-07)")


# ===========================================================================
# 1. Desapropriação INDIRETA — correção monetária (item 4.6.1.1)
#    DERIVADA em tempo de geração da cadeia da DIRETA. Ver DECISAO_1.
# ===========================================================================
def cadeia_indireta_correcao() -> dict:
    origem = DEST / "cjf.desapropriacao-direta.correcao-monetaria.json"
    direta = json.loads(origem.read_text(encoding="utf-8"))

    segmentos = []
    for s in direta["segmentos"]:
        novo = dict(s)
        # A tabela é a MESMA; o que muda é a página em que ela está impressa.
        novo["pagina_pdf"] = 73
        segmentos.append(novo)

    return {
        "id": "cjf.desapropriacao-indireta.correcao-monetaria",
        "titulo": "Correção monetária — desapropriações indiretas",
        "tipo": "cadeia-temporal",
        "tipo_acao": "desapropriacao-indireta",
        "componente": "correcao-monetaria",
        "fonte": {
            "documento": "manual_de_calculos_2026.pdf",
            "norma": "Resolução CJF n. 990/2026",
            "item": "4.6.1.1",
            "pagina_pdf": 72,
        },
        "termo_inicial": (
            "A correção monetária é contada a partir da data do laudo de avaliação "
            "(Súmula n. 75 do TFR)."
        ),
        "IDENTICA_A_4_5_1_1": (
            "A tabela de 4.6.1.1 (pagina_pdf 72–73) é IDÊNTICA à de 4.5.1.1 (pagina_pdf "
            "66), INCLUSIVE no IPC/FGV de mar. a dez./1991 — índice que nenhuma outra "
            "cadeia do manual usa. Afirmação da extração: bloco-08-jf-detalhe.md § 3.1, "
            "literal 'são idênticas'. O que muda entre direta e indireta é o TERMO "
            "INICIAL e os JUROS, não a linha do tempo da correção."
        ),
        "DERIVADA_DE": {
            "arquivo": "cjf.desapropriacao-direta.correcao-monetaria.json",
            "como": (
                "Os segmentos são LIDOS do arquivo da direta em tempo de geração por "
                "scripts/calculo/gera_cadeias_bloco19.py e reescritos com pagina_pdf 73. "
                "É a mitigação do único argumento que havia a favor de uma cadeia só: "
                "conteúdo idêntico duplicado à mão diverge; conteúdo idêntico DERIVADO "
                "não tem como divergir sem que o gerador seja reexecutado."
            ),
            "FUNDAMENTO_AUSENTE_E_PRE_EXISTENTE": (
                "OITO DOS ONZE SEGMENTOS NÃO TÊM O CAMPO 'fundamento', e ISSO É "
                "PRÉ-EXISTENTE, DO BLOCO 8: eles são derivados de "
                "cjf.desapropriacao-direta.correcao-monetaria.json, onde os mesmos oito "
                "já estavam assim. NÃO foram convertidos para 'fundamento: null' com "
                "razão, ao contrário das cadeias NOVAS deste bloco (ver "
                "declara_fundamento_ausente em gera_cadeias_bloco19.py), por duas razões: "
                "consertar aqui seria assumir defeito alheio como se fosse deste bloco, e "
                "faria o DERIVADO divergir da ORIGEM — que é justamente o que este campo "
                "existe para impedir. Fecha junto com a direta, num bloco que a revisite."
            ),
        },
        "DECISAO_1_DUAS_CADEIAS_E_NAO_UMA_COM_DOIS_ESCOPOS": (
            "DECIDIDO: DUAS cadeias. (a) O eixo que separa direta de indireta é a "
            "MODALIDADE da desapropriação, e modalidade não é eixo da linha do tempo: o "
            "que ela muda é o TERMO INICIAL, campo de CADEIA, e 'condicao' / "
            "'dominio_condicoes' são campos de SEGMENTO. Usar 'condicao' para carregar "
            "modalidade obrigaria a repetir a condição nos 11 segmentos para exprimir "
            "que ela não muda nenhum deles, e ainda assim não alcançaria o termo inicial, "
            "que é onde a diferença mora (D8-C10). (b) As gêmeas divergem FORA da "
            "correção: os juros de mora fecham em nov/2021 (4.5.2) e dez/2021 (4.6.2), e "
            "4.6.3 carrega o N-10. Uma cadeia 'desapropriação' seria verdadeira para a "
            "correção e falsa para as outras duas. (c) Regra do bloco 17 — o "
            "IDENTIFICADOR IDENTIFICA: 'cjf.desapropriacao-direta.*' já existe e o "
            "manifesto trata perda de id como regressão; renomeá-lo para abrigar as duas "
            "modalidades custaria uma regressão declarada para ganhar uma ambiguidade. "
            "O custo da decisão — duplicação — é pago por 'DERIVADA_DE'."
        ),
        "notas": [
            {
                "n": 2,
                "texto": (
                    "Consolidação em dez./2021: o crédito será consolidado com base no mês "
                    "de dez./2021 pelos critérios até então aplicáveis, considerando o "
                    "IPCA-E de nov./2021 (1,17%) e os juros de dez./2021 (0,4412%); sobre o "
                    "valor consolidado, sem exclusão de qualquer parcela, incidirá a taxa "
                    "Selic a partir de jan./2022 (competência dez./2021)."
                ),
                "pagina_pdf": 74,
                "efeito": (
                    "A desapropriação INDIRETA é um dos CINCO lugares que consolidam em "
                    "dez./2021. Verificado por varredura: '0,4412' ocorre nas pagina_pdf "
                    "50, 59, 67, 74 e 79. A primeira redação do bloco 8 listava quatro "
                    "lugares, e as duas desapropriações ficaram de fora."
                ),
            },
        ],
        "N_12_AUSENCIA_ASSIMETRICA": (
            "O item 4.5.1 traz NOTA com o termo inicial da correção (pagina_pdf 66); o "
            "item 4.6.1 NÃO tem nota equivalente (pagina_pdf 72). O termo inicial gravado "
            "acima vem do bullet 'Súmula n. 75 do TFR a partir do laudo de avaliação' "
            "(bloco-08-jf-detalhe.md § 3.1). Assimetria registrada, não harmonizada."
        ),
        "DEFEITOS_DO_ORIGINAL": {
            "D8-D26": ("'Parágrafo Único' (4.5.1.1, pagina_pdf 66) × 'parágrafo único' "
                       "(4.6.1.1, pagina_pdf 73) em tabelas GÊMEAS."),
            "D8-D29": ("'relativos a valores' × 'relativos aos valores' (pagina_pdf 67 e "
                       "74) em notas que deveriam ser idênticas."),
            "D8-D30": "Espaço antes da pontuação em 4.6.1 (pagina_pdf 72), resíduo de hyperlink.",
        },
        "jurisdicao": "justica-federal",
        "janela_de_analise": dict(direta["janela_de_analise"]),
        "tipo_indexador_catalogo": CAT,
        "segmentos": segmentos,
    }


# ===========================================================================
# 2. Dívida fiscal — JUROS DE MORA (item 2.3.2.2), com `base_incidencia`
# ===========================================================================
def _juros_fiscal(inicio, fim, taxa, base, pagina, **extra) -> dict:
    seg = {
        "inicio": inicio,
        "fim": fim,
        "taxa": taxa,
        "capitalizacao": "simples",
        "base_incidencia": base,
        "tipo_indexador": "nao-indexador",
        "tipo_indexador_fonte": NAO_IND_JUROS,
        "engloba": ["juros-mora"],
        "componente": "juros-mora",
        "pagina_pdf": pagina,
    }
    seg.update(extra)
    return seg


def cadeia_divida_fiscal_juros() -> dict:
    segmentos = [
        _juros_fiscal(
            "1964-07", "1968-04", "1%",
            "valor-base trimestral do débito cor/mon.", 26,
            base_literal=("Juros simples, incidentes sobre o valor-base trimestral do "
                          "débito cor/mon."),
            observacao="O manual escreve 'De jul./1964 a abr./1968'.",
        ),
        _juros_fiscal(
            "1968-05", "1979-09", "1%",
            "valor originário", 26,
            base_literal="Juros simples, incidentes sobre o valor originário do débito.",
        ),
        _juros_fiscal(
            "1979-10", "1979-12", "1%",
            "valor do débito cor/mon.", 26,
            base_literal="Juros simples, incidentes sobre o valor do débito cor/mon.",
        ),
        _juros_fiscal(
            "1980-01", "1982-12", "1%",
            "valor originário", 26,
            base_literal=("Juros simples, incidentes sobre o valor originário do débito, "
                          "contados do dia seguinte ao do vencimento."),
        ),
        _juros_fiscal(
            "1983-01", "1991-01", "1%",
            "valor do débito cor/mon.", 26,
            base_literal="Juros simples, incidentes sobre o valor do débito cor/mon.",
        ),
        _juros_fiscal(
            "1991-02", "1992-01", "Equivalente à TRD.",
            None, 26,
            fundamento="Art. 30 da Lei n. 8.218/1991.",
            observacao=("O manual escreve 'De fev./1991 a 2/1/1992'. O fim é DIA 2 de "
                        "janeiro de 1992; o schema indexa por competência, e 1992-01 "
                        "entra inteiro."),
            CORTE_INTRAMENSAL=("A fronteira do manual é 2/1/1992 ÷ 3/1/1992, DENTRO de "
                               "1992-01. O segmento seguinte também abre em 1992-01. A "
                               "sobreposição de um mês que o validador vai acusar é do "
                               "CORTE POR DIA numa modelagem por mês — registrada, não "
                               "harmonizada."),
            N_1=("ATRITO. A tabela de correção de 2.3.1.2 fecha a janela sem correção em "
                 "dez./1991 e remete 'vide item 2.3.2.2'; esta tabela estende a TRD até "
                 "2/1/1992. Para 1º e 2 de janeiro de 1992 a correção já iniciou a Ufir "
                 "e os juros ainda aplicam a TRD. CONTRADIZ. Não harmonizado."),
        ),
        _juros_fiscal(
            "1992-01", "1992-01", None,
            None, 26,
            observacao=("De 3/1/1992 a 31/1/1992: 'Não há aplicação de juros de mora, por "
                        "falta de previsão legal.'"),
            D8_C6=("UM MÊS SEM JUROS POR FALTA DE LEI — 3 a 31 de janeiro de 1992. "
                   "DECLARADO pelo manual, não inferido. 'taxa: null' aqui NÃO é dado "
                   "faltante: é a regra."),
        ),
        _juros_fiscal(
            "1992-02", JANELA_FIM, "1%, bifurcado por fato gerador (Selic/TMMCTN)",
            "valor do débito cor/mon.", 26,
            base_literal="Juros simples, incidentes sobre o valor do débito cor/mon.",
            eixo_declarado="data-do-fato-gerador",
            POR_QUE_NAO_E_CONDICAO=(
                "A bifurcação Selic/TMMCTN por data do fato gerador está DENTRO desta "
                "linha, e a tabela de 2.3.2.2 NÃO a desdobra em linhas próprias — quem a "
                "desdobra é a tabela de CORREÇÃO, 2.3.1.2, e é lá que o campo 'condicao' e "
                "o 'dominio_condicoes' vivem. Gravar 'condicao' aqui criaria um ramo sem "
                "gêmeo e abriria lacuna no universo incondicional; declarar "
                "'dominio_condicoes' para fechá-la seria afirmar exaustividade de um "
                "domínio que ESTA tabela não enumera. O eixo fica nomeado em campo próprio."
            ),
            regra_literal=("A partir de fev./1992: 1%, bifurcado por fato gerador "
                           "(Selic/TMMCTN). Juros simples, incidentes sobre o valor do "
                           "débito cor/mon."),
            aplicacao=("a partir do mês seguinte ao da competência da parcela devida até o "
                       "mês anterior ao pagamento, e 1% no mês do pagamento"),
            aplicacao_formula="D4",
            ponta_materializada="fim — o manual escreve 'A partir de fev./1992'",
        ),
    ]
    return {
        "id": "cjf.divida-fiscal.juros-mora",
        "titulo": "Juros de mora — dívidas fiscais da Fazenda Nacional",
        "tipo": "cadeia-temporal",
        "tipo_acao": "divida-fiscal",
        "componente": "juros-mora",
        "fonte": {
            "documento": "manual_de_calculos_2026.pdf",
            "norma": "Resolução CJF n. 990/2026",
            "item": "2.3.2.2",
            "pagina_pdf": 26,
        },
        "DECISAO_4_BASE_INCIDENCIA": (
            "O CAMPO É NOVO E O SCHEMA O ACOMODA SEM ALTERAÇÃO DE CÓDIGO. 'base_incidencia' "
            "é campo de SEGMENTO e diz sobre QUE VALOR a taxa incide — originário × "
            "corrigido ('cor/mon.') —, dimensão ortogonal a período, indexador e "
            "englobamento. `Segmento.de_dict` lê uma lista fechada de campos e ignora os "
            "demais, de modo que R1, R2 e R3 seguem exatas e o dado fica gravado para quem "
            "calcula. NÃO se criou campo no validador: R1/R2/R3 não têm o que fazer com a "
            "base, e acrescentá-lo ao dataclass sem regra que o consuma seria cerimônia. "
            "D8-C5: a base alterna QUATRO vezes — trimestral cor/mon. → originário → "
            "cor/mon. → originário → cor/mon. — e SÓ a dívida fiscal a exercita."
        ),
        "D8_C7_COR_MON_NUNCA_DEFINIDA": (
            "A abreviação 'cor/mon.' aparece TREZE vezes no manual (pagina_pdf 26, 32, 33, "
            "91 e 92) e NUNCA é definida. Transcrita como está; a leitura 'valor corrigido "
            "monetariamente' é a óbvia e NÃO foi gravada como se fosse do manual."
        ),
        "N_2_ASSIMETRIA": (
            "O item 2.4.2.2.2 (juros da contribuição previdenciária) traz, no mesmo período "
            "e com o mesmo fundamento, a ressalva '(sem a incidência de qualquer outro "
            "fator de correção monetária)' (pagina_pdf 33); esta tabela NÃO a traz "
            "(pagina_pdf 25–26). Duas tabelas irmãs, um cuidado só numa delas. Registrado."
        ),
        "aplicacao": {
            "formula": "D4",
            "literal": ("devem ser aplicadas a partir do mês seguinte ao da competência da "
                        "parcela devida até o mês anterior ao pagamento, e 1% no mês do "
                        "pagamento"),
            "pagina_pdf": 27,
        },
        "jurisdicao": "justica-federal",
        "janela_de_analise": {
            "inicio": "1964-07",
            "fim": JANELA_FIM,
            "por_que": ("A tabela 2.3.2.2 abre com 'De jul./1964' — mês DECLARADO, ao "
                        "contrário das cadeias de correção, que abrem com 'De 1964' sem "
                        "mês — e fecha com 'A partir de fev./1992'. " + JANELA_POR_QUE_FIM),
            "marcador": "ponta_materializada",
        },
        "SEM_CONDICAO_E_SEM_DOMINIO_CONDICOES": (
            "Esta cadeia NÃO usa 'condicao' nem 'dominio_condicoes', ao contrário da gêmea "
            "de correção (2.3.1.2). O eixo 'data-do-fato-gerador' aparece DENTRO de uma "
            "única linha — 'A partir de fev./1992: 1%, bifurcado por fato gerador "
            "(Selic/TMMCTN)' — e a tabela de 2.3.2.2 não a desdobra. Marcar o segmento com "
            "'condicao' criaria um ramo sem gêmeo e abriria lacuna de R2 no universo "
            "incondicional; declarar 'dominio_condicoes' para fechá-la seria afirmar "
            "exaustividade de um domínio que esta tabela não enumera. O eixo fica em "
            "'eixo_declarado', campo de registro, que não muda a aritmética de cobertura."
        ),
        "tipo_indexador_catalogo": CAT,
        "segmentos": segmentos,
    }


# ===========================================================================
# 3. FGTS na DÍVIDA FISCAL — item 2.4.4.1, critério JCM
# ===========================================================================
def cadeia_fgts_fiscal() -> dict:
    segmentos = [
        {
            "inicio": "1964-01",
            "fim": "1983-09",
            "indexador": "ORTN",
            "tipo_indexador": "nominal",
            "tipo_indexador_fonte": NOM,
            "engloba": ["correcao-monetaria"],
            "componente": "correcao-monetaria",
            "pagina_pdf": 35,
            "ponta_materializada": PONTA_INICIO_SEM_MES,
            "observacao": ("O item 2.4.4.1 dá a ORTN 'até set./1983' e NÃO dá início. "
                           "D8-C8-bis: o corte da ORTN difere nos TRÊS lugares em que ela "
                           "abre cadeia — set./1983 aqui, fev./1986 em 4.8.1.1 (FGTS "
                           "fundiário) e jun./1983 na poupança (4.9.1.1)."),
        },
        {
            "inicio": "1983-10",
            "fim": "1989-10",
            "indexador": "UPC → índices básicos de atualização dos saldos da poupança",
            "tipo_indexador": "indeterminado",
            "tipo_indexador_fonte": None,
            "tipo_indexador_por_que": COMPOSTO_POR_QUE,
            "tipo_indexador_pendencia": "P17-03",
            "engloba": ["correcao-monetaria"],
            "componente": "correcao-monetaria",
            "pagina_pdf": 35,
            "regra_literal": ("Unidade Padrão de Capital (UPC) e os índices básicos de "
                              "atualização dos saldos da poupança."),
            "observacao": ("O item lista os dois indexadores em sequência e NÃO DATA a "
                           "fronteira entre eles. O fim 1989-10 vem da linha seguinte "
                           "('conversão em BTNF em 1º/11/1989'), não deste segmento."),
        },
        {
            "inicio": "1989-11",
            "fim": "1991-01",
            "indexador": "BTNF",
            "tipo_indexador": "indeterminado",
            "tipo_indexador_fonte": None,
            "tipo_indexador_por_que": BTNF_POR_QUE,
            "tipo_indexador_pendencia": "P19-02",
            "engloba": ["correcao-monetaria"],
            "componente": "correcao-monetaria",
            "pagina_pdf": 35,
            "fundamento": "Item 2.4.4.1 do Manual CJF, Res. 990/2026.",
            "regra_literal": ("O valor do débito deve ser convertido em BTNF, em "
                              "1º/11/1989, aplicando-se juros mensais de 1% simples e "
                              "multa de 20%."),
            "multiplicador_transicao": {
                "valor": "126,8621",
                "quando": "1991-02",
                "texto": ("Os valores convertidos em BTN deverão ser convertidos em "
                          "cruzeiros, em 1º/2/1991, com a multiplicação por 126,8621."),
            },
        },
        {
            "inicio": "1991-02",
            "fim": "2000-05",
            "indexador": "TRD",
            "tipo_indexador": "indeterminado",
            "tipo_indexador_fonte": None,
            "tipo_indexador_por_que": TRD_POR_QUE,
            "tipo_indexador_pendencia": "P18-01",
            "engloba": ["correcao-monetaria"],
            "componente": "correcao-monetaria",
            "pagina_pdf": 35,
            "observacao": "O manual escreve 'De fev./1991 a maio/2000'.",
            "D8_C8": ("MAIO/2000 PERTENCE A DOIS INTERVALOS. 'De fev./1991 a maio/2000' e "
                      "'A partir de maio/2000', SEM REGRA DE DESEMPATE. E o item 2.4.4.2 "
                      "usa fronteira DIFERENTE para o mesmo tema — 'Nov./1989 a abr./2000' "
                      "e 'A partir de maio/2000'. A sobreposição de 2000-05 que o "
                      "validador acusa É DO MANUAL. Não harmonizada — P8-08."),
        },
        {
            "inicio": "2000-05",
            "fim": JANELA_FIM,
            "indexador": "TR",
            "tipo_indexador": "indeterminado",
            "tipo_indexador_fonte": TR_FONTE,
            "tipo_indexador_razao": TR_RAZAO,
            "tipo_indexador_fechamento": TR_FECHAMENTO,
            "engloba": ["correcao-monetaria"],
            "componente": "correcao-monetaria",
            "pagina_pdf": 35,
            "ponta_materializada": "fim — o manual escreve 'A partir de maio/2000'",
            "observacao": "Ver D8-C8 no segmento anterior: maio/2000 está nos dois.",
        },
    ]
    return {
        "id": "cjf.fgts-divida-fiscal.correcao-monetaria",
        "titulo": ("Correção monetária — FGTS como DÍVIDA FISCAL (débito do empregador "
                   "para com o Fundo), critério JCM"),
        "tipo": "cadeia-temporal",
        "tipo_acao": "fgts-divida-fiscal",
        "componente": "correcao-monetaria",
        "criterio": "JCM",
        "criterio_literal": ("coeficiente da remuneração das contas vinculadas (JCM). Como "
                             "'JAM', 'JCM' é NOME DE CRITÉRIO, não rótulo de indexador: os "
                             "indexadores são os dos segmentos. Por isso ele vive neste "
                             "campo e NÃO no campo 'indexador' de segmento algum."),
        "fonte": {
            "documento": "manual_de_calculos_2026.pdf",
            "norma": "Resolução CJF n. 990/2026",
            "item": "2.4.4.1",
            "pagina_pdf": 35,
        },
        "DECISAO_5_NAO_E_A_CADEIA_DO_ITEM_4_8": (
            "SÃO CADEIAS DISTINTAS, e o id precisa dizê-lo sem depender de quem o lê: "
            "'cjf.fgts-divida-fiscal.correcao-monetaria' × 'cjf.fgts.correcao-monetaria'. "
            "Sujeito distinto (o FUNDO é credor aqui; o TITULAR DA CONTA é credor lá), "
            "capítulo distinto (2 × 4), critério distinto (JCM × JAM) e até o corte da "
            "ORTN distinto (set./1983 × fev./1986; e jun./1983 na poupança). Regra do "
            "bloco 17 aplicada: o IDENTIFICADOR IDENTIFICA — 'fgts-divida-fiscal' diz QUAL "
            "cadeia é — e O ESCOPO SE DECLARA EM CAMPO — 'criterio: JCM', 'tipo_acao' e "
            "'ESCOPO'. A sigla do critério NÃO entrou no id: sigla é rótulo, e rótulo muda."
        ),
        "ESCOPO": (
            "Débito do EMPREGADOR para com o FGTS, cobrado como dívida fiscal (capítulo 2). "
            "NÃO alcança o crédito do trabalhador contra o Fundo, que é o item 4.8 e a "
            "cadeia 'cjf.fgts.correcao-monetaria'."
        ),
        "O_CORTE_DE_MAIO_2000_E_DESTA_CADEIA": (
            "D8-C8 é DESTE item e NÃO ALCANÇA o item 4.8. A cadeia de 4.8.1.1 não tem corte "
            "em maio/2000: ela vai de TRD (fev./1991–abr./1993) para TR (maio/1993 em "
            "diante) e não volta a cortar."
        ),
        "REGRA_TRIMESTRAL": {
            "literal": ("índices mensais de correção de forma trimestral, multiplicados pela "
                        "taxa de juros pro rata para o trimestre (1,0075, ou seja, a taxa "
                        "mínima, aplicada para a capitalização de 3% ao ano)"),
            "pagina_pdf": 35,
            "efeito": ("Regra de APLICAÇÃO da cadeia inteira, não de um segmento: os índices "
                       "mensais dos segmentos acima são aplicados TRIMESTRALMENTE, com o "
                       "fator 1,0075 por trimestre. Gravada em campo de cadeia porque não "
                       "corta a linha do tempo."),
        },
        "SERIE_EXTERNA": (
            "'tabelas de atualização mensalmente publicadas pela Caixa Econômica Federal' "
            "(pagina_pdf 35) — dado (B), fora do escopo das cadeias. Ver bloco-08-jf-"
            "detalhe.md § 8, chave 'fiscal.tabelas_fgts_cef'."
        ),
        "jurisdicao": "justica-federal",
        "janela_de_analise": {
            "inicio": "1964-01",
            "fim": JANELA_FIM,
            "por_que": ("O item 2.4.4.1 é LISTA, não tabela, e NÃO declara início: a "
                        "primeira regra datada é 'ORTN até set./1983'. 1964-01 é "
                        "materialização de janela para permitir a checagem de R1/R2, no "
                        "mesmo desenho de P8-07, e NÃO afirmação do manual. "
                        + JANELA_POR_QUE_FIM),
            "marcador": "ponta_materializada",
        },
        "tipo_indexador_catalogo": CAT,
        "segmentos": segmentos,
    }


# ===========================================================================
# 4 e 5. Juros COMPENSATÓRIOS — itens 4.5.3 (direta) e 4.6.3 (indireta)
# ===========================================================================
CORTE_INTRAMENSAL_1997 = (
    "A fronteira do manual é 10/6/1997 ÷ 11/6/1997, DENTRO de 1997-06. O schema indexa por "
    "competência, e 1997-06 entra nos dois segmentos. A sobreposição que o validador acusa "
    "é do CORTE POR DIA numa modelagem por mês — registrada, não harmonizada. Escolher um "
    "dos dois meses seria harmonizar."
)

TAXA_NAO_EXTRAIDA = (
    "A TAXA DESTA LINHA NÃO ESTÁ NA FONTE EXTRAÍDA. O corpus registra desta tabela os "
    "PERÍODOS ('Até 10/6/1997' e 'De 11/6/1997 a nov./2021'), o FUNDAMENTO (MP n. "
    "1.577/1997 e sucessivas, com a ADI n. 2332 nas observações) e os TRÊS CORTES — e NÃO "
    "registra o percentual de cada linha. Gravar um número aqui seria inventar dado. O "
    "segmento entra com o que a fonte dá e o buraco fica VISÍVEL AO VALIDADOR, que é a "
    "razão de existir desta tarefa: prosa não é lida pelo validador, e 'taxa: null' é."
)


def _cadeia_compensatorios(modalidade: str) -> dict:
    direta = modalidade == "direta"
    item = "4.5.3" if direta else "4.6.3"
    pagina = 69 if direta else 76
    termo = (
        "Os juros compensatórios são contados a partir da data da IMISSÃO DA POSSE "
        "(Súmula n. 69 do STJ), certificada no mandado."
        if direta else
        "Os juros compensatórios são contados a partir da data da EFETIVA OCUPAÇÃO do "
        "imóvel (Súmula n. 69 do STJ)."
    )
    remissao = "item 4.5.2" if direta else "item 4.5.2"  # N-10: a indireta remete à direta

    def base(extra: dict) -> dict:
        seg = {
            "tipo_indexador": "nao-indexador",
            "tipo_indexador_fonte": NAO_IND_COMPENSATORIOS,
            "capitalizacao": "simples",
            "componente": "juros-compensatorios",
            "pagina_pdf": pagina,
        }
        seg.update(extra)
        return seg

    segmentos = [
        base({
            "inicio": "1964-01",
            "fim": "1997-06",
            "taxa": None,
            "taxa_nao_extraida": TAXA_NAO_EXTRAIDA,
            "engloba": ["juros-compensatorios"],
            "observacao": "O manual escreve 'Até 10/6/1997'.",
            "ponta_materializada": PONTA_INICIO_SEM_MES,
            "CORTE_INTRAMENSAL": CORTE_INTRAMENSAL_1997,
        }),
        base({
            "inicio": "1997-06",
            "fim": "2021-11",
            "taxa": None,
            "taxa_nao_extraida": TAXA_NAO_EXTRAIDA,
            "engloba": ["juros-compensatorios"],
            "fundamento": ("MP n. 1.577/1997 e sucessivas; ADI n. 2332 citada nas "
                           "observações da tabela."),
            "observacao": "O manual escreve 'De 11/6/1997 a nov./2021'.",
            "CORTE_INTRAMENSAL": CORTE_INTRAMENSAL_1997,
            "D8_D17": ("'(ADI n. 2332)' sem ponto de milhar nesta página; a pagina_pdf 70 "
                       "grafa 'ADI n. 2.332'. Transcrito como está."),
        }),
        base({
            "inicio": "2021-12",
            "fim": JANELA_FIM,
            "taxa": None,
            "engloba": [],
            "regra_literal": (
                f"Já incluídos na SELIC aplicada aos juros de mora ({remissao})."
            ),
            "fundamento": "Art. 3º da EC n. 113/2021, por via dos juros de mora.",
            "absorvido_por": (
                "cjf.desapropriacao-direta.juros-mora" if direta
                else "cjf.desapropriacao-indireta.juros-mora"
            ),
            "absorvido_por_nota": (
                "A cadeia de juros de mora de 4.5.2/4.6.2 NÃO EXISTE no repositório — "
                "segue em P18-02, e o porquê está em 'BLOQUEADAS' de "
                "scripts/calculo/gera_cadeias_bloco19.py. O ponteiro nomeia o destino, "
                "não afirma que o arquivo existe."
            ),
            "D8_C11": (
                "A PARTIR DE DEZ./2021 O REGIME AUTÔNOMO ACABA. Não há taxa adicional: os "
                "compensatórios estão 'já incluídos na SELIC aplicada aos juros de mora'. "
                "'taxa: null' aqui NÃO é dado faltante — é a regra. Somar compensatórios à "
                "Selic depois de dez./2021 é dupla contagem, R1 aplicada a esta cadeia."
            ),
            "LINHAS_DEZ_2021_EM_DIANTE": (
                "A extração registra que o manual traz DUAS linhas de dez./2021 em diante "
                "('nas duas linhas', N-10 e D8-C11) com a MESMA observação, e NÃO "
                "transcreve onde uma termina e a outra começa. Gravadas como UM segmento "
                "porque o conteúdo das duas é idêntico; arbitrar a fronteira — set./2025 é "
                "o palpite óbvio, e palpite óbvio é palpite — seria inventar dado. Por "
                "isso esta cadeia tem TRÊS segmentos, e a varredura do bloco 18 contou "
                "QUATRO LINHAS."
            ),
            "ponta_materializada": "fim — o manual escreve 'De dez./2021' em diante",
            "observacao": ("N-7: a NOTA 1, 'a', do item 4.2.2 — 'vedada sua incidência "
                           "cumulada com os juros de mora' — é boilerplate copiado da "
                           "seção de correção e repete-se em 4.6.2. Registrado."),
        }),
    ]

    cadeia = {
        "id": f"cjf.desapropriacao-{modalidade}.juros-compensatorios",
        "titulo": f"Juros compensatórios — desapropriações {modalidade}s",
        "tipo": "cadeia-temporal",
        "tipo_acao": f"desapropriacao-{modalidade}",
        "componente": "juros-compensatorios",
        "fonte": {
            "documento": "manual_de_calculos_2026.pdf",
            "norma": "Resolução CJF n. 990/2026",
            "item": item,
            "pagina_pdf": pagina,
        },
        "termo_inicial": termo,
        "D8_C10_TERMO_INICIAL_BIFURCA_POR_MODALIDADE": (
            "MESMA SÚMULA, DOIS MARCOS. Direta: imissão da posse, certificada no mandado. "
            "Indireta: efetiva ocupação do imóvel. Ambos por Súmula n. 69 do STJ. NÃO é "
            "defeito — não há imissão na desapropriação indireta —, mas é bifurcação, e o "
            "eixo é a MODALIDADE, não uma data. Sem o atributo modalidade não há termo "
            "inicial. É por isso que são duas cadeias, e não uma com dois escopos: ver "
            "DECISAO_1 em cjf.desapropriacao-indireta.correcao-monetaria.json."
        ),
        "TERCEIRA_CADEIA_AUTONOMA": (
            "Os juros compensatórios são cadeia PRÓPRIA, além da correção (4.5.1.1/4.6.1.1) "
            "e dos juros de mora (4.5.2/4.6.2). Quem tratar a desapropriação só pela linha "
            "de correção monetária perde esta inteira — foi o que aconteceu no bloco 15."
        ),
        "DECISAO_2_O_CORTE_DE_AGO_2017_NAO_E_TABULAVEL": {
            "veredito": "NÃO É TABULÁVEL. Não virou segmento, e a razão está gravada aqui.",
            "onde_vive": "item 4.5.4 (TDAs complementares), pagina_pdf 70",
            "literal": (
                "A conversão em TDAs complementares deverá ser efetuada com base na data da "
                "respectiva conta de atualização. A conta de atualização deverá abranger a "
                "correção monetária com base nos índices referidos no item 4.5.1, desde a "
                "data do laudo, além de juros de mora [...] e de juros compensatórios [...] "
                "até julho de 2017, e, a partir agosto de 2017, em percentual correspondente "
                "ao fixado para os TDAs depositados como oferta inicial (art. 5, § 9º, da "
                "Lei n. 8.629/1993, com alterações da Lei n. 13.465/2017)."
            ),
            "por_que_nao_e_segmento": (
                "A taxa deste regime é 'o percentual fixado para os TDAs depositados como "
                "OFERTA INICIAL' — um valor fixado NO PROCESSO, caso a caso, no ato de "
                "oferta. Não é índice publicado, não é série, não é percentual legal: é "
                "PARÂMETRO DO CASO. Gravá-lo como segmento exigiria um valor que não existe "
                "em fonte alguma, para nenhum caso em geral; e gravá-lo com 'taxa: null' "
                "sobre o intervalo 2017-08..2021-11 SOBRESCREVERIA a linha 'De 11/6/1997 a "
                "nov./2021' que a tabela declara — trocando um fato do manual por uma regra "
                "de outro item. O corte fica em campo de cadeia, com o literal, e quem "
                "calcula PERGUNTA o percentual (R21) e REGISTRA a resposta (R19)."
            ),
            "D8_C25": (
                "O corte de ago./2017 vive SÓ no item 4.5.4 e NENHUMA TABELA O MOSTRA. É o "
                "padrão do § 1 de 07-leitura-do-corpus.md — regra que vive fora da tabela — "
                "aplicado a uma cadeia inteira."
            ),
            "NOTA_1_do_4_5_4": (
                "Havendo imissão prévia, os compensatórios incidem 'sobre a diferença entre "
                "o valor fixado na sentença e o preço ofertado em juízo'. É regra de BASE, "
                "não de taxa — e por isso também não é segmento."
            ),
            "D8_D21": "'art. 5, § 9º' sem ordinal na pagina_pdf 70; a nota logo abaixo grafa 'art. 5º, § 9º'.",
            "D8_D22": "'a partir agosto de 2017' — falta a preposição. Transcrito como está.",
        },
        "DECISAO_3_N_6_A_CONTRADICAO_DE_UM_MES": {
            "veredito": (
                "GRAVADO O QUE A TABELA DIZ: o regime autônomo encerra em NOV./2021. A "
                "contradição fica registrada; NÃO se escolhe lado."
            ),
            "texto_do_manual": ("'Até dez. 2021, os juros compensatórios incidem:' "
                                "(pagina_pdf 69)"),
            "tabela_do_manual": "encerra o regime autônomo em nov./2021",
            "por_que_a_tabela": (
                "Esta é uma CADEIA, e cadeia é a tabela: os segmentos transcrevem linhas. O "
                "texto de abertura é enunciado da seção, não linha. Gravar 'dez./2021' "
                "criaria sobreposição com a linha seguinte que o manual NÃO tem, e seria "
                "resolver N-6 por escolha. A leitura alternativa fica aqui, legível, e a "
                "conta que atravesse dez./2021 grava qual aplicou (R19)."
            ),
            "consequencia": ("DEZ./2021 FICA SEM REGIME COERENTE — e é justamente o mês da "
                             "consolidação da EC 113/2021. Fundamento idêntico nas duas "
                             "cadeias gêmeas."),
            "pendencia": "P8-09 — aberta, NÃO harmonizada.",
            "D8_D23": ("'Até dez. 2021' está fora do padrão 'dez./2021' do manual E em "
                       "conflito com a linha de nov./2021."),
        },
        "VEDACAO_DE_JUROS_COMPOSTOS": {
            "literal": "vedado o cálculo de juros compostos",
            "fundamento": "art. 5º, § 9º, da Lei n. 8.629/1993",
            "pagina_pdf": 71,
            "contraste": (
                "O MESMO manual PRESCREVE capitalização composta em cjf.trabalhista.juros-"
                "mora — 'De mar./1987 a mar./1991 | 1,0% – composta', art. 3º do DL n. "
                "2.322/1987 (pagina_pdf 78, D8-C18, a R4-EXCEÇÃO do projeto). Proíbe num "
                "item e prescreve no outro. AQUI VALE A VEDAÇÃO."
            ),
        },
        "R_08_19_PRECATORIO_COMPLEMENTAR": (
            "NÃO cabem juros compensatórios em precatório complementar — NOTA 7 do item 5.2, "
            "pagina_pdf 90: 'a compensação pela perda da posse se resolve com a consolidação "
            "do montante devido ao expropriado'. Mas 'devem ser incluídos os juros vencidos "
            "antes da apresentação da requisição, e não computados no montante requisitado'."
        ),
        "jurisdicao": "justica-federal",
        "janela_de_analise": {
            "inicio": "1964-01",
            "fim": JANELA_FIM,
            "por_que": (
                "A tabela abre com 'Até 10/6/1997' e NÃO declara início — os compensatórios "
                "correm da imissão da posse / efetiva ocupação, que é fato do caso, não data "
                "do manual. 1964-01 é materialização de janela, alinhada à cadeia de correção "
                "gêmea, e NÃO afirmação da fonte. " + JANELA_POR_QUE_FIM
            ),
            "marcador": "ponta_materializada",
        },
        "tipo_indexador_catalogo": CAT,
        "segmentos": segmentos,
    }

    if not direta:
        cadeia["N_10_REMISSAO_ERRADA"] = (
            "As linhas de dez./2021 em diante de 4.6.3 remetem ao 'item 4.5.2' — que é a "
            "desapropriação DIRETA (pagina_pdf 76, DUAS ocorrências, D8-D15). A remissão foi "
            "TRANSCRITA COMO ESTÁ no campo 'regra_literal' do terceiro segmento; o campo "
            "'absorvido_por' nomeia 4.6.2, que é o item de juros de mora desta própria "
            "cadeia. LEITURA DECLARADA, não correção do original: o defeito fica catalogado "
            "e o texto não se altera."
        )
        cadeia["D8_D16"] = (
            "'este ponto reconhecida a constitucionalidade' — falta o 'n'; o gêmeo 4.5.3 "
            "grafa 'neste ponto' (pagina_pdf 76). Transcrito como está."
        )
        cadeia["SOBREPOSICAO_DE_DEZ_2021_NA_INDIRETA"] = (
            "Achado que NÃO é desta cadeia, e fica o ponteiro: nos JUROS DE MORA da indireta "
            "(4.6.2) a linha da poupança fecha em 'dez./2021' e a da Selic abre em 'De "
            "dez./2021' (pagina_pdf 74–75), enquanto a gêmea direta (4.5.2) fecha em "
            "'nov./2021' com fundamento idêntico. A checagem automática não a pega porque as "
            "linhas estão em tabelas diferentes — e porque nenhuma das duas tabelas virou "
            "cadeia (P18-02)."
        )
        cadeia["DERIVADA_DE"] = {
            "arquivo": "cjf.desapropriacao-direta.juros-compensatorios.json",
            "como": (
                "Esta cadeia e a da direta saem da MESMA função geradora "
                "(_cadeia_compensatorios de scripts/calculo/gera_cadeias_bloco19.py), pela "
                "mesma razão de DERIVADA_DE em cjf.desapropriacao-indireta.correcao-"
                "monetaria.json: conteúdo idêntico duplicado à mão diverge; conteúdo "
                "idêntico DERIVADO não tem como divergir sem que o gerador seja "
                "reexecutado. O que NÃO é derivado, e por isso está gravado à parte, é o "
                "termo inicial (D8-C10), o N-10, o D8-D16 e a sobreposição de dez./2021."
            ),
            "RESSALVA_DE_ORIGEM": (
                "TRÊS BLOCOS DESTA CADEIA SÃO HERDADOS DA DIRETA E NÃO TÊM FONTE PRÓPRIA "
                "NA 4.6.3. A extração não os atribui à indireta, e que a 4.6.3 tenha o "
                "mesmo enunciado é INFERÊNCIA DO GERADOR, não transcrição. O conteúdo fica "
                "— é a melhor leitura disponível —, mas fica DECLARADO como herdado: "
                "(1) DECISAO_3_N_6_A_CONTRADICAO_DE_UM_MES — a extração atribui o N-6 SÓ à "
                "4.5.3, e a pagina_pdf 69 citada no 'texto_do_manual' é da DIRETA "
                "(bloco-08-jf-detalhe.md:365). Não se verificou que a 4.6.3 traga o mesmo "
                "texto de abertura; 'Fundamento idêntico nas duas cadeias gêmeas' é "
                "inferência. (2) DECISAO_2_O_CORTE_DE_AGO_2017_NAO_E_TABULAVEL — o item "
                "4.5.4 e a pagina_pdf 70 são da DIRETA; não há item equivalente extraído "
                "no capítulo 4.6. (3) VEDACAO_DE_JUROS_COMPOSTOS — a pagina_pdf 71 é do "
                "capítulo 4.5. ESTE MESMO ARQUIVO declara o N-10 e a SOBREPOSICAO_DE_DEZ_"
                "2021_NA_INDIRETA, isto é, REGISTRA QUE DIRETA E INDIRETA DIVERGEM EM "
                "DATAS — razão a mais para não importar os três blocos em silêncio. "
                "Fechar esta ressalva exige extrair 4.6.3 e 4.6.4 linha a linha."
            ),
        }
        herdado = (
            "HERDADO DA DIRETA — não tem fonte própria extraída na 4.6.3. "
            "Ver DERIVADA_DE.RESSALVA_DE_ORIGEM nesta cadeia. "
        )
        cadeia["DECISAO_3_N_6_A_CONTRADICAO_DE_UM_MES"]["ORIGEM"] = herdado + (
            "O N-6 é atribuído pela extração SÓ à 4.5.3 e a pagina_pdf 69 é da DIRETA "
            "(bloco-08-jf-detalhe.md:365). Que a 4.6.3 traga o mesmo texto de abertura — e "
            "portanto que o 'Fundamento idêntico nas duas cadeias gêmeas' da 'consequencia' "
            "valha aqui — é INFERÊNCIA, não transcrição."
        )
        cadeia["DECISAO_2_O_CORTE_DE_AGO_2017_NAO_E_TABULAVEL"]["ORIGEM"] = herdado + (
            "O 'onde_vive' — item 4.5.4, pagina_pdf 70 — é item da DIRETA. Nenhum item "
            "equivalente do capítulo 4.6 foi extraído. Que o regime de TDAs complementares "
            "alcance a indireta é INFERÊNCIA."
        )
        cadeia["VEDACAO_DE_JUROS_COMPOSTOS"]["ORIGEM"] = herdado + (
            "A pagina_pdf 71 é do capítulo 4.5. A vedação do art. 5º, § 9º, da Lei n. "
            "8.629/1993 é de direito material e não se limita à modalidade — mas o LUGAR de "
            "onde ela foi lida é o capítulo da direta, e é isso que fica declarado."
        )
    return cadeia


# ===========================================================================
# O que a fonte NÃO bastou para gerar — e a delegação de 4.7.1
# ===========================================================================
BLOQUEADAS = {
    "4.5.2 e 4.6.2 — juros de mora das desapropriações": {
        "veredito": "NÃO GERADAS. Seguem em P18-02.",
        "por_que": (
            "A tabela NÃO FOI EXTRAÍDA LINHA A LINHA, e o corpus o declara duas vezes, com "
            "escopo: skills/calculo-judicial-atualizacao/references/desapropriacao.md § 3 "
            "('A tabela de 4.5.2/4.6.2 não foi extraída linha a linha para "
            "tabelas-normativas/ [...] Não infiro os segmentos ausentes') e § 10, item 4. O "
            "que o corpus tem são QUATRO MARCAS soltas — o eixo de corte 26/9/1999 ÷ "
            "27/9/1999 (que é CONDIÇÃO por data da sentença, não fronteira de período), a "
            "fórmula da poupança a partir de maio/2012 POR COMPETÊNCIA, a Selic de dez./2021 "
            "e a taxa legal de set./2025 — e a informação de que a tabela tem CINCO LINHAS. "
            "Nenhuma taxa anterior a maio/2012 está registrada, e o mapeamento das cinco "
            "linhas sobre as marcas é reconstrução, não transcrição: sobram duas linhas para "
            "dois ramos de condição cujos períodos ninguém transcreveu. Gerar isto seria "
            "inventar a ESTRUTURA, que é pior do que inventar um valor."
        ),
        "o_que_falta_da_fonte": ("a tabela de 4.5.2 (pagina_pdf 68) e a de 4.6.2 "
                                 "(pagina_pdf 75), linha a linha, com período e taxa."),
    },
    "2.4.2.2.2 — juros da contribuição previdenciária": {
        "veredito": "NÃO GERADA. Segue em P18-02.",
        "por_que": (
            "A fonte extraída NÃO TRAZ A TABELA. O § 2.3 de bloco-08-jf-detalhe.md trata do "
            "item 2.4.2 e o que registra é da CORREÇÃO (a janela fev–mar/1997 sem correção) e "
            "da base dos juros sobre MULTAS (item 2.4.1, DL n. 2.323/1987). Do item "
            "2.4.2.2.2 o corpus tem UMA ÚNICA frase, o atrito N-2: a ressalva '(sem a "
            "incidência de qualquer outro fator de correção monetária)', pagina_pdf 33 — uma "
            "observação de uma linha, sem os períodos, sem as taxas e sem as bases. "
            "'É quase igual à do IR' é afirmação sobre a CORREÇÃO e vem com exceção "
            "declarada; estendê-la aos JUROS e copiar 2.3.2.2 seria herança por analogia — a "
            "mesma dedução que o bloco 17 proibiu, agravada porque N-2 REGISTRA que as duas "
            "tabelas irmãs NÃO são idênticas."
        ),
        "o_que_falta_da_fonte": ("a tabela de 2.4.2.2.2 (pagina_pdf 32–33), linha a linha, "
                                 "com período, taxa e base de incidência."),
        "NAO_E_FALTA_DE_CAMPO": (
            "P18-02 dizia que 2.3.2.2 e 2.4.2.2.2 'exigem base_incidencia', campo que as "
            "cadeias não tinham. ESSA PARTE ESTÁ RESOLVIDA: o campo existe e está em uso em "
            "cjf.divida-fiscal.juros-mora. O que bloqueia 2.4.2.2.2 é FONTE, não schema."
        ),
    },
    "4.7.1 — correção das ações trabalhistas na JF": {
        "veredito": "NÃO É LACUNA E NUNCA FOI. NÃO ENTRA EM P18-02.",
        "por_que": (
            "O manual NÃO TEM tabela de correção monetária trabalhista. O item traz lista de "
            "leis e a NOTA 2 DELEGA, literal: 'deve-se utilizar a tabela de coeficientes "
            "trabalhistas expedida pelo Tribunal Superior do Trabalho' (pagina_pdf 77). "
            "REGISTRA-SE A DELEGAÇÃO, NÃO A AUSÊNCIA: afirmar 'falta a cadeia' seria afirmar "
            "ausência de algo que a fonte nunca prometeu. A cadeia vive numa SÉRIE (dado B), "
            "não numa regra — mesmo desenho do P9-02. Os JUROS de 4.7.2, esses sim, existem "
            "e estão em cjf.trabalhista.juros-mora."
        ),
        "onde_ja_estava_registrado": ("02-atualizacao-detalhe.md § 5.0, linha 4.7.1; "
                                      "pendencias.md § 24.3, parágrafo final."),
    },
}


FUNDAMENTO_NAO_EXTRAIDO = (
    "O FUNDAMENTO DESTA LINHA NÃO ESTÁ NA FONTE EXTRAÍDA. A tabela do manual traz o "
    "período e o critério; a coluna de fundamento legal, quando existe, não foi "
    "transcrita linha a linha para esta linha em particular. 'fundamento: null' aqui é "
    "AUSÊNCIA DECLARADA, não campo esquecido — mesmo desenho de 'taxa' + "
    "'taxa_nao_extraida'. Herdar o fundamento da linha vizinha seria dedução por "
    "proximidade. Fecha quando a linha for extraída com a sua coluna de fundamento."
)


def declara_fundamento_ausente(cadeia: dict) -> dict:
    """§ 5.3.6: 'onde a fonte não trouxe, o campo fica null COM A RAZÃO'.

    O critério foi cumprido em 'taxa' e não em 'fundamento', que simplesmente
    SUMIA do segmento — ausência sem razão, indistinguível de esquecimento.
    Aqui ele passa a valer também para 'fundamento', e SÓ NAS CADEIAS NOVAS
    DESTE BLOCO. A indireta de correção fica de fora DE PROPÓSITO: os 8
    segmentos dela sem fundamento são DERIVADOS da direta, que é do bloco 8 —
    são PRÉ-EXISTENTES, e consertá-los aqui seria (a) assumir defeito alheio
    como próprio e (b) fazer o derivado divergir da origem, que é exatamente o
    que 'DERIVADA_DE' existe para impedir.
    """
    for seg in cadeia["segmentos"]:
        if "fundamento" not in seg:
            seg["fundamento"] = None
            seg["fundamento_nao_extraido"] = FUNDAMENTO_NAO_EXTRAIDO
    return cadeia


def main() -> int:
    cadeias = [
        cadeia_indireta_correcao(),
        declara_fundamento_ausente(cadeia_divida_fiscal_juros()),
        declara_fundamento_ausente(cadeia_fgts_fiscal()),
        declara_fundamento_ausente(_cadeia_compensatorios("direta")),
        declara_fundamento_ausente(_cadeia_compensatorios("indireta")),
    ]
    for obj in cadeias:
        destino = DEST / f"{obj['id']}.json"
        destino.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
        print(f"escrito: {destino.name} — {len(obj['segmentos'])} segmentos")

    print("\nNÃO GERADAS (fonte insuficiente ou inexistente):")
    for chave, v in BLOQUEADAS.items():
        print(f"  {chave}: {v['veredito']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
