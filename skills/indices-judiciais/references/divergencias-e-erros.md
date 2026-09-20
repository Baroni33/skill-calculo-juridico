# As 31 divergências, e o que foram os 10 erros

Companheiro de [`../SKILL.md`](../SKILL.md), § Limitações declaradas, item 5. **Movido da
espinha no bloco 19, pelo limite de 500 linhas** — nada foi removido.

**Bloco 23:** recebeu também as **armadilhas 8 e 9** da espinha, pela mesma razão de limite.

---

### As armadilhas 8 e 9 — defeitos do original, não da leitura

**8 — o calendário de 18.14 não serve para contar dias úteis.** **Treze meses impressos com
menos dias do que têm** — conferido na imagem da página. Março de 2017 imprime **27 dias num mês
de 31**, com a coluna inteira de segunda-feira vazia. `dia_da_semana` vem da coluna sob o
cabeçalho do original, **não de cálculo de calendário**, e diverge do real em **42 dias**.

**9 — ruído tipográfico que o validador acusa, e que é do original.** Dígito a mais ou ponto no
lugar da vírgula nos limites de faixa (`De 2.2347,86 até 3.130,51`, `Até 1.1710,78`,
`De 478.78 até 957,56` — **nove ocorrências**, `bloco-01-tabelas.md` § 5.1); e **chamada de nota
de rodapé colada na data** (`04/04/9116`, `Dez/1017`), que faz o validador acusar lacuna de
**1018-01 a 2010-12**. O CSV guarda a **string literal**.

---

### 5. O que as "31 divergências" significam (e o que foram os "10 erros")

**O script separa erro de extração de divergência do original. Divergência é RESULTADO
ESPERADO.** Não apresentar como falha da skill.

**As 31 divergências são o original:** 13 calendários com dias faltando, 9 limites de faixa com
erro de digitação, sobreposições reais de vigência (jan/10 tem **dois quadros vigentes**;
jun/99, jun/00 e jun/11 mudam de tabela **no meio do mês**, e a checagem trabalha em competência
mensal), rótulos com nota de rodapé colada, e a contagem de 18.1 que **não deve** fechar.

**Os 10 erros eram de ESCOPO, não de dado, e estão corrigidos (bloco 17, tarefa 4).** Todos
apontavam para o mesmo arquivo — `serie-9.2.11-ufir-juros-ate-dez79.csv`, linhas 2 a 11,
*"página 178"*. O validador conferia a proveniência contra `PAGINAS_DO_BLOCO =
range(373, 472)`, constante do bloco 1, enquanto varria `DIR_SERIE.glob("serie-*.csv")` —
**todos** os CSV do diretório. Uma série de bloco posterior caiu no mesmo lugar e foi acusada
de estar fora de 373–471. **`bloco-01-tabelas.md` registra "0 erros de extração"**, e o
registro estava certo **para o escopo dele**. **O dado nunca regrediu; o escopo do validador é
que estava estreito.**

**A constante não existe mais.** A faixa se resolve **por arquivo**, em duas origens: o
`pagina_pdf=` declarado no cabeçalho do próprio CSV, ou o item da linha resolvido no contrato
de páginas do bloco. Arquivo sem nenhuma das duas sai como **não verificável**, nunca como erro
e nunca em silêncio. **A saída corrente não é transcrita aqui** — ok, divergências, não
verificados e erros estão em `docs/calculo/consolidado/00-numeros.md` § 4, gerado por script.
**Consequência para o contrato:** proveniência **exige o intervalo de páginas declarado junto
com a série** — validador com intervalo fixo global não escala para múltiplos blocos.
