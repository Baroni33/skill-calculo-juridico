# -*- coding: utf-8 -*-
"""Bloco 18, tarefa 1 — gera as quatro cadeias de FGTS (item 4.8) e de
cadernetas de poupança (item 4.9) do Manual CJF, Res. 990/2026.

Nenhum `float`: os percentuais são strings literais do manual e nada é somado
aqui. Toda escrita declara `encoding='utf-8'` (R12).

Descoberta pelo validador: `valida_cadeias.py` reconhece cadeia por
`tipo == "cadeia-temporal"`, logo estes quatro arquivos entram na contagem
automaticamente.
"""
import json
from pathlib import Path

DEST = Path(__file__).resolve().parents[2] / "docs" / "calculo" / "tabelas-normativas"

CAT = ("tabelas-normativas/indexadores-tipo-catalogo.json — o valor sai da fonte; "
       "sem fonte, indeterminado (bloco 17, tarefa 1)")
NAO_IND = ("segmentos de juros-mora cuja regra é percentual legal fixo (1% a.m., 6% a.a., "
           "TRD, poupança) e não índice. 21 segmentos, em 6 cadeias. Sem índice, R3 não tem "
           "o que verificar.")
NOM = "item 4.1.2.4, letra a, pagina_pdf 42 — nomeado LITERALMENTE na lista de exemplos"
PCT_IPC = ("D8-C21 — bloco-08-jf-detalhe.md linha 416, literal: "
           "'O IPC/IBGE é índice percentual'")
SELIC_F = ("D8-C22 — bloco-08-jf-detalhe.md linha 421, literal: 'Selic não é índice de "
           "inflação'; e R1 (00-base-normativa.md § 7), que a trata como englobante de "
           "correção e juros")
LEGAL_F = ("R1 (00-base-normativa.md § 7) — taxa legal engloba correção e juros. R11: é "
           "DERIVADA por razão entre fatores, não índice de preços publicado. O item 4.1.2.4 "
           "não a alcança: ela é posterior ao manual que o contém e não reflete inflação de "
           "mês algum.")
TR_PQ = ("Rebaixada no bloco 17 (P17-02): nenhum dos dois manuais a classifica, e o critério "
         "material do item 4.1.2.4 — 'refletem a inflação do próprio mês' — não alcança taxa "
         "apurada prospectivamente (art. 12, I, da Lei n. 8.177/1991).")

IND = {
    "UPC": (
        "Unidade Padrão de Capital. NÃO está na lista do item 4.1.2.4 e nenhuma outra fonte do "
        "corpus a classifica. O item 2.4.4.1 (pagina_pdf 35) apenas EXPANDE A SIGLA — 'Unidade "
        "Padrão de Capital (UPC)' —, o que é rotulagem e não classificação. Aparece só na cadeia "
        "da poupança."
    ),
    "LBC": (
        "Letra do Banco Central. NÃO está na lista do item 4.1.2.4; nenhuma fonte do corpus a "
        "classifica. Aparece só nas cadeias de FGTS e poupança."
    ),
    "LBC – 0,5%": (
        "Mesma razão da LBC, e o rótulo do manual já embute uma dedução de 0,5% cuja natureza "
        "(juros descontados? desconto do índice?) a tabela não declara."
    ),
    "LFT – 0,5%": (
        "Letra Financeira do Tesouro. NÃO está na lista do item 4.1.2.4; nenhuma fonte do corpus "
        "a classifica. O rótulo embute uma dedução de 0,5% não explicada pela tabela."
    ),
    "TRD": (
        "Taxa Referencial Diária. Segue a TR, rebaixada a 'indeterminado' no bloco 17 (P17-02): "
        "taxa apurada prospectivamente, fora do critério material do item 4.1.2.4. Nenhuma fonte "
        "do corpus classifica a TRD por si."
    ),
    "IPC": (
        "Rótulo NU, sem emissor, nas linhas de mar./1986–jan./1987 e maio/1989–mar./1990 de "
        "4.8.1.1. D8-C21 sustenta o 'IPC/IBGE', não o 'IPC' sem qualificação — e o próprio manual "
        "usa DOIS IPC de emissores distintos (IPC/IBGE no tronco comum e IPC/FGV no item 4.5.1.1). "
        "A tabela gêmea da poupança (4.9.1.1) escreve 'IPC/IBGE' nos MESMOS meses; identificar os "
        "dois rótulos seria a dedução proibida, e é a mesma classe de erro que o bloco 8 registrou "
        "ao trocar IPC/FGV por IPC/IBGE."
    ),
}


def seg(inicio, fim, **kw):
    d = {"inicio": inicio, "fim": fim}
    d.update(kw)
    return d


def ind_seg(inicio, fim, indexador, tipo, fonte, **kw):
    """Segmento de correção monetária, com a regra do tipo_indexador do bloco 17."""
    d = {"inicio": inicio, "fim": fim, "indexador": indexador, "tipo_indexador": tipo}
    if tipo == "indeterminado":
        d["tipo_indexador_fonte"] = None
        d["tipo_indexador_por_que"] = fonte
        d["tipo_indexador_pendencia"] = "P18-01"
    else:
        d["tipo_indexador_fonte"] = fonte
    d["engloba"] = ["correcao-monetaria"]
    d["componente"] = "correcao-monetaria"
    d.update(kw)
    return d


# --------------------------------------------------------------- 4.8.1.1
fgts_cm = {
    "id": "cjf.fgts.correcao-monetaria",
    "titulo": "Correção monetária — FGTS (critérios das contas fundiárias, JAM)",
    "tipo": "cadeia-temporal",
    "tipo_acao": "fgts",
    "componente": "correcao-monetaria",
    "fonte": {
        "documento": "manual_de_calculos_2026.pdf",
        "norma": "Resolução CJF n. 990/2026",
        "item": "4.8.1.1",
        "pagina_pdf": 82,
    },
    "criterio_declarado": {
        "literal": (
            "Se não houver decisão judicial em contrário, os valores apurados deverão ser "
            "corrigidos com base nos critérios adotados para as contas fundiárias (Juros e "
            "Atualização Monetária — JAM), com os indexadores seguintes."
        ),
        "item": "4.8",
        "pagina_pdf": 81,
        "sigla": "JAM — Juros e Atualização Monetária",
        "NOTA_DO_EXTRATOR": (
            "JAM é o NOME DO CRITÉRIO, não um indexador de segmento: os indexadores são os da "
            "tabela 4.8.1.1. Não confundir com a tabela JAM da CEF do item 6.14 do Manual TRT-3 "
            "(regime pr.fgts-indice-jam), que é outro manual, outra fonte e outro eixo — lá o "
            "eixo é o conteúdo do título, e a tabela 'já computa juros de 3% ao ano'."
        ),
    },
    "escapes_declarados": [
        {
            "n": 1,
            "texto": (
                "Se o título judicial determinar a aplicação de juros e a correção dos valores "
                "devidos como dívida comum (ex.: REsp. n. 630.372) e não havendo previsão de "
                "índice na sentença, aplicam-se os indexadores previstos para condenações em "
                "geral (Seção 4.2 deste capítulo)."
            ),
            "pagina_pdf": 81,
            "efeito": (
                "EIXO DE CONTEÚDO DO TÍTULO — o título manda para cjf.condenatorias-gerais.*, e "
                "esta cadeia inteira deixa de valer."
            ),
        },
        {
            "n": 2,
            "texto": (
                "Se o título judicial determinar a correção e juros pelos critérios fundiários "
                "somente até a data do saque integral (ex.: REsp n. 694.365; AgRg no REsp n. "
                "622.298), devem ser aplicados, a contar do saque integral e se não houver "
                "previsão de índice na sentença, os indexadores previstos para condenações em "
                "geral (Seção 4.2 deste capítulo)."
            ),
            "pagina_pdf": 81,
            "efeito": (
                "EIXO DE CORTE POR SAQUE INTEGRAL — D8-C12. NÃO é competência nem data de "
                "sentença: é um fato do contrato de trabalho. Nenhuma outra cadeia do manual usa "
                "este eixo, e nenhuma tabela o mostra."
            ),
        },
    ],
    "notas": [
        {
            "n": 1,
            "texto": (
                "Expurgos inflacionários. Para ações de FGTS que discutem os expurgos "
                "inflacionários, somente incluir os períodos definidos pelo julgado."
            ),
            "pagina_pdf": 82,
        },
        {
            "n": 2,
            "texto": (
                "Expurgos inflacionários. Se a ação de revisão dos saldos do FGTS não discutir os "
                "expurgos inflacionários (ex.: juros progressivos), a liquidação deve incluir os "
                "expurgos inflacionários reconhecidos pelo STJ em casos de FGTS: 42,72% em "
                "jan./1989 e 44,80% em abr./1990."
            ),
            "pagina_pdf": 82,
            "PENDENCIA_ABERTA": (
                "N-5 / D8-C13 — SUBSTITUI OU ACRESCE? O manual não diz. No capítulo 4 geral a "
                "operação é declarada ('Expurgo, em substituição ao BTN', e o item 4.1.2.1 manda "
                "'descontando o BTN ou outro índice utilizado, evitando bis in idem'). Aqui a nota "
                "apenas manda INCLUIR os percentuais sobre linhas que já trazem indexador — "
                "'LFT – 0,5%' em jan./1989 e 'BTN' em abr./1990 —, e a tabela não menciona expurgo "
                "algum. NÃO RESOLVIDA: os percentuais NÃO foram gravados como segmento, porque "
                "gravá-los exigiria escolher entre substituir e somar."
            ),
            "bifurcacao_contraintuitiva": (
                "D8-C14 — a NOTA 1 RESTRINGE quem DISCUTE expurgos aos períodos definidos pelo "
                "julgado; a NOTA 2 dá os dois expurgos POR PADRÃO a quem NÃO discute. Quem discute "
                "pode receber menos do que quem não discute. Não é erro formal; é o que está "
                "escrito."
            ),
            "contraste_com_o_capitulo_4_geral": {
                "1989-01": "42,72% nos dois — mesmo percentual",
                "1989-02": "10,14% no capítulo 4 geral; o FGTS NÃO o tem",
                "1990-04": "44,80% só no FGTS; o capítulo 4 geral não o tem",
            },
        },
    ],
    "segmentos": [
        ind_seg("1967-01", "1986-02", "ORTN", "nominal", NOM, pagina_pdf=82),
        ind_seg("1986-03", "1987-01", "IPC", "indeterminado", IND["IPC"], pagina_pdf=82,
                divergencia_de_rotulo=("4.9.1.1 escreve 'IPC/IBGE' nos mesmos meses; 4.8.1.1 "
                                       "escreve 'IPC'. Registrado, não harmonizado.")),
        ind_seg("1987-02", "1987-02", "LBC", "indeterminado", IND["LBC"], pagina_pdf=82,
                observacao=("Segmento de UM MÊS. A poupança funde fev./1987 no bloco "
                            "fev./1987–jun./1987.")),
        ind_seg("1987-03", "1987-06", "OTN", "nominal", NOM, pagina_pdf=82,
                DIVERGENCIA_FGTS_x_POUPANCA=(
                    "D8-C15 — nestes quatro meses o FGTS usa OTN e a poupança usa LBC (4.9.1.1, "
                    "pagina_pdf 85). NENHUMA DAS DUAS TABELAS TRAZ FUNDAMENTO LEGAL PARA A "
                    "DIVERGÊNCIA, e o manual não a explica. NÃO HARMONIZADO.")),
        ind_seg("1987-07", "1987-09", "LBC – 0,5%", "indeterminado", IND["LBC – 0,5%"],
                pagina_pdf=82),
        ind_seg("1987-10", "1988-12", "OTN", "nominal", NOM, pagina_pdf=82),
        ind_seg("1989-01", "1989-04", "LFT – 0,5%", "indeterminado", IND["LFT – 0,5%"],
                pagina_pdf=82,
                expurgo_pendente=("A NOTA 2 manda incluir 42,72% em jan./1989 SOBRE esta linha. "
                                  "Substitui ou acresce? Não declarado — N-5, aberta.")),
        ind_seg("1989-05", "1990-03", "IPC", "indeterminado", IND["IPC"], pagina_pdf=82),
        ind_seg("1990-04", "1991-01", "BTN", "nominal", NOM, pagina_pdf=82,
                expurgo_pendente=("A NOTA 2 manda incluir 44,80% em abr./1990 SOBRE esta linha. "
                                  "Substitui ou acresce? Não declarado — N-5, aberta.")),
        ind_seg("1991-02", "1993-04", "TRD", "indeterminado", IND["TRD"], pagina_pdf=82),
        ind_seg("1993-05", "2026-06", "TR", "indeterminado", TR_PQ, pagina_pdf=82,
                ponta_materializada="fim — o manual escreve 'A partir de maio/1993'"),
    ],
    "jurisdicao": "justica-federal",
    "janela_de_analise": {
        "inicio": "1967-01",
        "fim": "2026-06",
        "por_que": (
            "A primeira linha da tabela 4.8.1.1 é 'De jan./1967 a fev./1986' — início DECLARADO, "
            "sem materialização, ao contrário das demais cadeias do capítulo 4. A última é "
            "'A partir de maio/1993'; o fim 2026-06 é a data-base dos exemplos do próprio manual "
            "(item 4.2.1.1, pagina_pdf 52)."
        ),
        "marcador": "ponta_materializada",
    },
    "DIVERGENCIAS_COM_A_POUPANCA": {
        "D8-C15": (
            "Dezesseis anos e quatro meses de divergência. (a) maio/1967 a jun./1983: FGTS ORTN × "
            "poupança UPC; (b) mar. a jun./1987: FGTS OTN × poupança LBC. NENHUMA DAS DUAS TABELAS "
            "TRAZ FUNDAMENTO LEGAL PARA A DIVERGÊNCIA — a de 4.8.1.1 sequer tem coluna de "
            "observações — e o manual não a explica. Não harmonizada."
        ),
        "rotulo_do_IPC": (
            "mar./1986–jan./1987 e maio/1989–mar./1990: o FGTS escreve 'IPC'; a poupança escreve "
            "'IPC/IBGE'. Mesmos meses, rótulos diferentes."
        ),
        "fev_1987": (
            "O FGTS abre um segmento de UM mês (fev./1987, LBC); a poupança o funde no bloco "
            "fev./1987–jun./1987. É o único mês em que as duas concordam entre fev. e jun./1987."
        ),
    },
    "NAO_E_A_CADEIA_DO_ITEM_2_4_4_1": (
        "O item 2.4.4.1 (pagina_pdf 35–36) trata do FGTS como DÍVIDA FISCAL — o débito do "
        "empregador PARA COM o Fundo — e usa outro critério: o 'coeficiente da remuneração das "
        "contas vinculadas (JCM)', com ORTN até set./1983, depois UPC e 'os índices básicos de "
        "atualização dos saldos da poupança'; conversão em BTNF em 1º/11/1989; multiplicação por "
        "126,8621 em 1º/2/1991; TRD de fev./1991 a maio/2000; TR a partir de maio/2000. SÃO "
        "CADEIAS DISTINTAS: sujeito distinto (Fundo credor × titular da conta credor), sigla "
        "distinta (JCM × JAM), capítulo distinto, e até o corte da ORTN difere — set./1983 em "
        "2.4.4.1, fev./1986 em 4.8.1.1, jun./1983 na poupança. O corte de maio/2000 (D8-C8: 'De "
        "fev./1991 a maio/2000' × 'A partir de maio/2000', sem regra de desempate) é do item "
        "2.4.4.1 e NÃO alcança esta cadeia."
    ),
    "tipo_indexador_catalogo": CAT,
}

# --------------------------------------------------------------- 4.8.3 / 4.9.3
NOTA_SELIC = {
    "n": 1,
    "texto": (
        "A taxa Selic (Sistema Especial de Liquidação e Custódia): a) deve ser capitalizada de "
        "forma simples, sendo vedada sua incidência cumulada com os juros de mora e com a "
        "correção monetária; b) deve ser aplicada a partir do mês seguinte ao de competência da "
        "parcela devida até o mês anterior ao pagamento, e 1% no mês do pagamento."
    ),
    "ATRITO_N_7": (
        "A alínea 'a' veda a cumulação 'com os juros de mora' — e a tabela que ela qualifica É de "
        "juros de mora. BOILERPLATE AUTORREFERENTE, copiado da seção de correção monetária. "
        "Repete-se em 4.2.2 NOTA 1 a), 4.6.2, 4.8.3 e 4.9.3. Registrado, não corrigido."
    ),
    "aplicacao_e_a_D4": (
        "A alínea 'b' é a fórmula D4 do bloco 8 — eixo na COMPETÊNCIA DA PARCELA —, que o bloco 8 "
        "atribuía só à dívida fiscal (itens 2.3.1.2 e 2.4.2.2.2). FGTS e poupança a usam também. "
        "Não é a D2 das condenatórias, que ancora no termo inicial dos juros."
    ),
}


def cadeia_juros(ident, titulo, tipo_acao, item, pag_tabela, notas_extra, janela_ini,
                 janela_por_que):
    return {
        "id": ident,
        "titulo": titulo,
        "tipo": "cadeia-temporal",
        "tipo_acao": tipo_acao,
        "componente": "juros-mora",
        "fonte": {
            "documento": "manual_de_calculos_2026.pdf",
            "norma": "Resolução CJF n. 990/2026",
            "item": item,
            "pagina_pdf": pag_tabela,
        },
        "termo_inicial": ("Os juros são contados a partir da citação, salvo determinação judicial "
                          "em outro sentido."),
        "notas": [NOTA_SELIC] + notas_extra,
        "segmentos": [
            seg(janela_ini, "2002-12", taxa="0,5% ao mês", capitalizacao="simples",
                engloba=["juros-mora"],
                fundamento="Arts. 1.062, 1.063 e 1.064 do antigo Código Civil.",
                pagina_pdf=pag_tabela, componente="juros-mora",
                ponta_materializada="inicio — o manual escreve 'Até dez./2002', sem data inicial",
                tipo_indexador="nao-indexador", tipo_indexador_fonte=NAO_IND),
            seg("2003-01", "2024-08", indexador="Selic", tipo_indexador="englobante",
                tipo_indexador_fonte=SELIC_F, capitalizacao="simples",
                engloba=["correcao-monetaria", "juros-mora"],
                aplicacao=("a partir do mês seguinte ao de competência da parcela devida até o mês "
                           "anterior ao pagamento, e 1% no mês do pagamento"),
                fundamento="Art. 406 da Lei n. 10.406/2002 – Código Civil.",
                pagina_pdf=pag_tabela, componente="juros-mora"),
            seg("2024-09", "2026-06", indexador="taxa-legal", tipo_indexador="englobante",
                tipo_indexador_fonte=LEGAL_F, capitalizacao="simples",
                engloba=["correcao-monetaria", "juros-mora"],
                formula="SELIC, com dedução do IPCA-15",
                aplicacao="mes-posterior-a-competencia",
                aplicacao_fonte=("NOTA 4 do item: 'A taxa legal observará as mesmas orientações "
                                 "estabelecidas na Nota 7 do item 4.2.2' — e a Nota 7 "
                                 "(pagina_pdf 56) manda aplicá-la no mês posterior ao de sua "
                                 "competência (fórmula D1, R-08-11)."),
                fundamento=("Art. 406 da Lei n. 10.406/2002 – Código Civil (redação dada pela Lei "
                            "n. 14.905/2024) e Resolução CMN n. 5.171/2024."),
                pagina_pdf=pag_tabela, componente="juros-mora",
                ponta_materializada="fim — o manual escreve 'A partir de set./2024'"),
        ],
        "jurisdicao": "justica-federal",
        "janela_de_analise": {"inicio": janela_ini, "fim": "2026-06", "por_que": janela_por_que,
                              "marcador": "ponta_materializada"},
        "ACHADO_O_CALENDARIO_E_OUTRO": (
            "Esta cadeia NÃO tem o corte de dez./2021 da EC 113/2021 nem o de set./2025 da EC "
            "136/2025. Vai direto de Selic (desde jan./2003) para TAXA LEGAL EM SET./2024 — um ano "
            "antes de todas as demais cadeias do manual —, com fundamento exclusivo no art. 406 do "
            "Código Civil na redação da Lei n. 14.905/2024 e na Resolução CMN n. 5.171/2024, SEM "
            "citar o ARE 1.557.312/SP (Tema 1.419 do STF), que todas as outras citam. Consequência "
            "verificada: FGTS e poupança NÃO estão entre os cinco lugares que consolidam em "
            "dez./2021 — '0,4412' ocorre nas pagina_pdf 50, 59, 67, 74 e 79, e nenhuma delas é 83 "
            "ou 86. Transcrito como está, não harmonizado."
        ),
        "tipo_indexador_catalogo": CAT,
    }


fgts_jm = cadeia_juros(
    "cjf.fgts.juros-mora", "Juros de mora — FGTS", "fgts", "4.8.3", 83,
    [
        {"n": 2, "texto": ("Os juros remuneratórios e moratórios incidem concomitantemente, ou "
                           "seja, não são reciprocamente excludentes (REsp n. 897.043)."),
         "pagina_pdf": 83},
        {"n": 3, "texto": ("No caso de juros moratórios pela taxa Selic, não deve incidir "
                           "concomitantemente a correção monetária, já contemplada, mas tão "
                           "somente deverão incidir os juros remuneratórios respectivos. A Selic "
                           "incidirá sobre o principal acrescido dos juros remuneratórios (REsp n. "
                           "1.102.552)."),
         "pagina_pdf": 83,
         "efeito": ("É a R1 dita pela fonte: a Selic engloba a correção; o que sobra por fora são "
                    "os juros REMUNERATÓRIOS do item 4.8.2, não a correção monetária.")},
        {"n": 4, "texto": ("A taxa legal observará as mesmas orientações estabelecidas na Nota 7 "
                           "do item 4.2.2."), "pagina_pdf": 83},
    ],
    "1967-01",
    ("A tabela 4.8.3 abre com 'Até dez./2002', sem início. A ponta foi materializada em 1967-01, "
     "mesma abertura da cadeia de correção gêmea (4.8.1.1), para permitir a checagem de R1/R2. O "
     "fim 2026-06 é a data-base dos exemplos do manual."),
)
fgts_jm["JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA"] = {
    "item": "4.8.2",
    "pagina_pdf": 82,
    "regra": (
        "3% ao ano (Lei n. 5.705/1971 e art. 13 da Lei n. 8.036/1990); 3%, 4%, 5% ou 6%, "
        "progressivos, para contas existentes em 22/9/1971 (art. 4º da Lei n. 5.107/1986, art. 13, "
        "§ 3º, da Lei n. 8.036/1990 e Súmula n. 154 do STJ); 6% ao ano para os casos enquadrados "
        "no art. 1º da Lei n. 8.678/1993 e durante o prazo previsto nesse dispositivo."
    ),
    "POR_QUE_NAO_VIROU_CADEIA": (
        "O eixo NÃO É COMPETÊNCIA: é a EXISTÊNCIA DA CONTA EM 22/9/1971 (juros progressivos) ou o "
        "enquadramento no art. 1º da Lei n. 8.678/1993. O schema cadeia-temporal indexa por "
        "competência e não expressa este eixo."
    ),
    "D8_D18": (
        "'art. 4º da Lei n. 5.107/1986' — a Lei n. 5.107 é de 13 DE SETEMBRO DE 1966, como o "
        "próprio item 4.8.1 a data uma página antes (pagina_pdf 81). DEFEITO DO ORIGINAL, "
        "TRANSCRITO COMO ESTÁ, não corrigido."
    ),
}

# --------------------------------------------------------------- 4.9.1.1
poup_cm = {
    "id": "cjf.poupanca.correcao-monetaria",
    "titulo": "Correção monetária (remuneração básica) — cadernetas de poupança",
    "tipo": "cadeia-temporal",
    "tipo_acao": "caderneta-de-poupanca",
    "componente": "correcao-monetaria",
    "fonte": {
        "documento": "manual_de_calculos_2026.pdf",
        "norma": "Resolução CJF n. 990/2026",
        "item": "4.9.1.1",
        "pagina_pdf": 84,
    },
    "condicao_de_incidencia": {
        "literal": (
            "Havendo decisão judicial determinando a correção monetária dos valores apurados com "
            "base nos critérios adotados para as contas de poupança, aplicam-se os seguintes "
            "indexadores."
        ),
        "pagina_pdf": 84,
        "escape": (
            "Não determinando a decisão judicial a aplicação dos critérios próprios da caderneta "
            "de poupança, os cálculos seguirão, quanto à correção monetária e juros moratórios, as "
            "orientações constantes do item 4.2 (Ações condenatórias em geral) (REsp n. 1.075.627; "
            "Resp n. 754.013; REsp. n. 1.314.478; EDcl no REsp n. 1.355.333), considerando-se como "
            "termo inicial o mês em que o crédito deveria ter sido efetivado na conta."
        ),
        "escape_pagina_pdf": 84,
        "escopo": (
            "Referem-se, ainda, à chamada poupança 'livre', a mais encontrada. Para modalidades "
            "específicas de cadernetas de poupança (v.g. vinculada, programada, a prazo fixo, de "
            "rendimentos crescentes etc.), raramente encontradas, deve-se consultar o juízo sobre "
            "a utilização."
        ),
    },
    "termo_inicial": (
        "NOTA 2: O termo inicial de correção pelos critérios da caderneta de poupança é o dia em "
        "que o crédito deveria ter sido efetivado, aplicando-se, em cada aniversário, os índices "
        "relativos à DATA-BASE DA CONTA."
    ),
    "notas": [
        {"n": 1, "texto": ("Se a sentença determinar a aplicação dos índices próprios da poupança "
                           "a partir de quando era devido o crédito, sem fixar o termo final, o "
                           "cômputo deve-se dar até o efetivo pagamento."), "pagina_pdf": 85},
        {"n": 2, "texto": ("O termo inicial de correção pelos critérios da caderneta de poupança é "
                           "o dia em que o crédito deveria ter sido efetivado, aplicando-se, em "
                           "cada aniversário, os índices relativos à data-base da conta."),
         "pagina_pdf": 85,
         "efeito": ("EIXO DE ANIVERSÁRIO — a competência não é o mês civil, é a DATA-BASE DA "
                    "CONTA. Nenhuma outra cadeia de correção do manual tem este eixo, e o schema "
                    "cadeia-temporal não o expressa: os segmentos abaixo são o mapa período → "
                    "indexador, e a aplicação ao caso passa pelo aniversário da conta.")},
        {"n": 3, "texto": ("Para correção de cruzados novos bloqueados na forma da Lei n. "
                           "8.024/1990 — Plano Collor (conversão da MP n. 168/1990), aplicam-se os "
                           "seguintes índices até a data da conversão: BTNF desde o bloqueio até "
                           "jan./1991; e TRD, de fev./1991 em diante."),
         "pagina_pdf": 85,
         "efeito": ("CADEIA PARALELA NÃO TABULADA, para um subconjunto de saldos (cruzados novos "
                    "bloqueados). Dois trechos — BTNF e TRD — que a tabela de 4.9.1.1 não mostra. "
                    "NÃO gravados como segmentos: são regime alternativo, não trecho desta linha "
                    "do tempo. Mesmo padrão do N-8 (ramo paralelo que só vive em nota).")},
    ],
    "segmentos": [
        ind_seg("1964-01", "1967-04", "ORTN", "nominal", NOM, pagina_pdf=84,
                ponta_materializada="inicio — o manual escreve 'Até abr./1967', sem data inicial"),
        ind_seg("1967-05", "1983-06", "UPC", "indeterminado", IND["UPC"], pagina_pdf=85,
                DIVERGENCIA_FGTS_x_POUPANCA=(
                    "D8-C15 — nestes dezesseis anos e dois meses o FGTS usa ORTN (4.8.1.1, "
                    "pagina_pdf 82) e a poupança usa UPC. Nenhuma das duas tabelas traz fundamento "
                    "legal para a divergência. NÃO HARMONIZADO.")),
        ind_seg("1983-07", "1986-02", "ORTN", "nominal", NOM, pagina_pdf=85,
                observacao=("Fev./1986: ORTN pro rata até 28/2/1986 (art. 4º, parágrafo único, do "
                            "DL n. 2.284/1986 e art. 1º, inciso I, 'a', do Decreto n. "
                            "92.492/1986).")),
        ind_seg("1986-03", "1987-01", "IPC/IBGE", "percentual", PCT_IPC, pagina_pdf=85),
        ind_seg("1987-02", "1987-06", "LBC", "indeterminado", IND["LBC"], pagina_pdf=85,
                DIVERGENCIA_FGTS_x_POUPANCA=(
                    "D8-C15 — de mar. a jun./1987 o FGTS usa OTN e a poupança usa LBC. Fev./1987 "
                    "coincide: o FGTS abre um segmento de um mês só com LBC. NÃO HARMONIZADO.")),
        ind_seg("1987-07", "1987-09", "LBC – 0,5%", "indeterminado", IND["LBC – 0,5%"],
                pagina_pdf=85),
        ind_seg("1987-10", "1988-12", "OTN", "nominal", NOM, pagina_pdf=85),
        ind_seg("1989-01", "1989-04", "LFT – 0,5%", "indeterminado", IND["LFT – 0,5%"],
                pagina_pdf=85),
        ind_seg("1989-05", "1990-03", "IPC/IBGE", "percentual", PCT_IPC, pagina_pdf=85,
                observacao=("Mar./1990: contas com data-base e depósitos efetuados entre 19 e 28/3 "
                            "– BTNF (art. 6º da Lei n. 8.024/1990 – conv. MP n. 168/1990).")),
        ind_seg("1990-04", "1991-01", "BTN", "nominal", NOM, pagina_pdf=85,
                observacao=("Jan./1991: BTNF desde o último crédito efetuado até 31/1/1991 + TRD "
                            "de 1º/2/1991 até a data do crédito (parágrafo único do art. 13 da Lei "
                            "n. 8.177/1991 – conv. MP n. 294/1991).")),
        ind_seg("1991-02", "1993-04", "TRD", "indeterminado", IND["TRD"], pagina_pdf=85,
                observacao=("Abr./1993: TRD desde o último crédito efetuado até 2/5/1993 + TR pro "
                            "rata de 3/5/1993 até a data do crédito (§ 2º do art. 7º da Lei n. "
                            "8.660/1993 – conv. MP n. 319/1993).")),
        ind_seg("1993-05", "2026-06", "TR", "indeterminado", TR_PQ, pagina_pdf=85,
                ponta_materializada="fim — o manual escreve 'A partir de maio/1993'",
                observacao=("Jun./1994: TR pro rata desde o último crédito efetuado até 30/6/1994 "
                            "+ TR pro rata de 1º/7/1994 até a data do crédito (§§ 1º e 2º do art. "
                            "16 da Lei n. 9.069/1995 – conv. MP n. 542/1994).")),
    ],
    "jurisdicao": "justica-federal",
    "janela_de_analise": {
        "inicio": "1964-01",
        "fim": "2026-06",
        "por_que": (
            "A primeira linha é 'Até abr./1967', sem início. 1964-01 MATERIALIZA a ponta pelo ano "
            "da Lei n. 4.380/1964, primeira norma da lista do item 4.9.1 (pagina_pdf 84) — é "
            "materialização declarada, não afirmação do manual. O fim 2026-06 é a data-base dos "
            "exemplos do manual (item 4.2.1.1, pagina_pdf 52)."
        ),
        "marcador": "ponta_materializada",
    },
    "DEFEITOS_DO_ORIGINAL_TRANSCRITOS": {
        "D8-D24": ("'de 31de outubro de 1990' — falta o espaço. Item 4.9.1, pagina_pdf 84. "
                   "Transcrito como está."),
        "D8-D25": ("'REsp n. 1.075.627; Resp n. 754.013; REsp. n. 1.314.478' — três grafias da "
                   "mesma abreviatura na mesma linha. Item 4.9, pagina_pdf 84 (e 'REsp.' em 4.8, "
                   "pagina_pdf 81). Transcrito como está."),
    },
    "tipo_indexador_catalogo": CAT,
}

poup_jm = cadeia_juros(
    "cjf.poupanca.juros-mora", "Juros de mora — cadernetas de poupança",
    "caderneta-de-poupanca", "4.9.3", 86,
    [
        {"n": 2, "texto": ("Os juros remuneratórios e moratórios incidem concomitantemente, ou "
                           "seja, não são reciprocamente excludentes (REsp n. 466.732)."),
         "pagina_pdf": 87},
        {"n": 3, "texto": ("No caso de juros moratórios pela taxa Selic, que também contempla "
                           "correção monetária, não devem incidir concomitantemente com a "
                           "remuneração básica, mas tão somente com os juros remuneratórios "
                           "respectivos. A Selic incidirá sobre o principal acrescido dos juros "
                           "remuneratórios."),
         "pagina_pdf": 87,
         "efeito": ("R1 dita pela fonte, com o nome próprio da poupança: o que a Selic exclui é a "
                    "REMUNERAÇÃO BÁSICA (item 4.9.1), não os juros remuneratórios (item 4.9.2).")},
        {"n": 4, "texto": ("A taxa legal observará as mesmas orientações estabelecidas na Nota 7 "
                           "do item 4.2.2."), "pagina_pdf": 87},
    ],
    "1964-01",
    ("A tabela 4.9.3 abre com 'Até dez./2002', sem início. A ponta foi materializada em 1964-01, "
     "mesma abertura da cadeia de correção gêmea (4.9.1.1), para permitir a checagem de R1/R2. O "
     "fim 2026-06 é a data-base dos exemplos do manual."),
)
poup_jm["JUROS_REMUNERATORIOS_NAO_SAO_ESTA_CADEIA"] = {
    "item": "4.9.2",
    "pagina_pdf": 86,
    "regra": (
        "0,5% ao mês (art. 52 do Decreto n. 24.427/1934; art. 12 do DL n. 2.284/1986; art. 2º da "
        "Lei n. 8.088/1990 e art. 12 da Lei n. 8.177/1991); 6% ao ano ou fração pro rata para "
        "cruzados novos bloqueados (art. 6º da Lei n. 8.024/1990; art. 7º da Lei n. 8.177/1991)."
    ),
    "NOTA_1": (
        "Os juros remuneratórios são CAPITALIZADOS MENSALMENTE, agregando-se ao principal em cada "
        "período a que se referem (REsp n. 780.085; AgRg-Ag n. 1.192.553; AgRg-Ag n. 1.217.521; "
        "AgRg no REsp n. 1.554.66; AgRg no Ag n. 1.098.926). NÃO é juros de mora: a R4 do projeto "
        "não é tocada."
    ),
    "NOTA_2_D8_C16": (
        "Tratando-se de contas ABERTAS A PARTIR DE MAIO/2012 (art. 12 da Lei n. 8.177/1991 com "
        "alterações da MP n. 567/2012, convertida na Lei n. 12.703/2012): 0,5% ao mês, caso a taxa "
        "Selic ao ano seja superior a 8,5%; e 70% da taxa Selic ao ano, mensalizada, nos demais "
        "casos."
    ),
    "POR_QUE_NAO_VIROU_CADEIA": (
        "O eixo NÃO É COMPETÊNCIA: é a DATA DE ABERTURA DA CONTA. O schema cadeia-temporal indexa "
        "por competência e não expressa este eixo. D8-C16 / N-11."
    ),
    "N_11": (
        "Eixo DIFERENTE do usado em 4.5.2 e 4.6.2, que aplicam a MESMA FÓRMULA da poupança (0,5% "
        "a.m. se a Selic anual for superior a 8,5%; senão 70% da Selic ao ano, mensalizada) a "
        "partir de maio/2012 POR COMPETÊNCIA. Mesmo cálculo, eixos diferentes. Registrado, não "
        "harmonizado."
    ),
    "D8_D19": ("'AgRg no REsp n. 1.554.66' — número truncado no original (pagina_pdf 86). "
               "Transcrito como está."),
    "D8_D14_contraste": (
        "4.9.2 grafa corretamente 'Lei n. 12.703/2012'; a gêmea 4.5.2 grafa 'Lei n. 2.703/2012' "
        "(pagina_pdf 68). O defeito é de 4.5.2, e a poupança é a prova."
    ),
}


def main() -> int:
    for obj in (fgts_cm, fgts_jm, poup_cm, poup_jm):
        destino = DEST / f"{obj['id']}.json"
        destino.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
        print(f"escrito: {destino.name} — {len(obj['segmentos'])} segmentos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
