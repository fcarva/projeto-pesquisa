# `paper/` — o documento da qualificação

⚠️ **O alvo da qualificação não inclui resultado estimado.** O roteiro
(`docs/ars/04-roteiro-qualificacao.md`) declara: *"documento de projeto
defensável. Identificação fechada, dose verificada, descritivas preliminares,
ameaças mapeadas. **Não** resultado estimado."*

Isso muda como o documento é lido: a seção de identificação está **completa**, e
as de resultado estão **ausentes de propósito** — não por atraso.

## Estrutura

| Arquivo | Estado |
|---|---|
| `main.tex` | esqueleto; compila com o que existe |
| `secoes/02-background.tex` | ✅ **escrita** |
| `secoes/03-teoria.tex` | ✅ **escrita** |
| `secoes/04-identificacao.tex` | ✅ **escrita** — é o que a banca defende |
| §1 Introdução | ⬜ por último, quando as demais fixarem o argumento |
| §5 Dados e descritivas | ⬜ espera aquisição |
| §6 Resultados | ⬜ **fora do alvo da qualificação** |

```
latexmk -pdf -interaction=nonstopmode paper/main.tex
```

⚠️ **O `.tex` nunca foi compilado.** Não há compilador LaTeX nesta sessão e
instalar TeX Live pelo proxy seria desproporcional. Verificado: ambientes
balanceados (`table`, `tabular`, `itemize`, `enumerate`, `quote`, `minipage`),
9 subseções, 12 rótulos. **Não** verificado: que compila. Na primeira compilação,
esperar ajuste de pacote — `natbib` sem `.bib` ainda, e a tabela larga da
§\ref{sub:ameacas} pode pedir `\resizebox` ou `landscape`.

## ⚠️ Duas coisas que o texto corrige em relação ao esboço

**O químico não é o glifosato.** `docs/framework-dissertacao.md` §5.1 é centrado
em glifosato e culturas transgênicas. A tabela do Dossiê ABRASCO reproduzida no
PL 18/2015 mostra outra coisa na Chapada do Apodi: procimidona e carbaril em
23/23, carbofurano em 18/23, fenitrotiona em 16/23 — e **glifosato em 4/23**. É
fungicida e inseticida sobre fruticultura irrigada, não herbicida sobre grão
transgênico. A §2.3 abre com advertência ao leitor por isso, e tira três
consequências metodológicas.

**A autoria da lei.** O esboço atribui a três deputados. O texto oficial da lei e
o PL 18/2015 registram apenas **Renato Roseno** — provavelmente coautoria no
projeto, não na lei sancionada (ver `docs/legislacao/README.md`). O texto **não
nomeia autores** enquanto a tramitação não for conferida.

## O que a §4 carrega, e que só existia em nota

A seção de identificação consolida achados que até agora viviam em
`docs/ars/*.md` e em mensagem de commit — lugar frágil para material que a banca
vai cobrar:

- a distinção `ATT(d|d)` vs. `ATE(d)`/`ACR(d)`, e por que o **Ensaio 2 obriga a
  curva** (decide pela inclinação do dano marginal, não pelo nível);
- ⚠️ que o *event study* de *leads* **não testa** a hipótese forte — fala da
  usual. Confundir os dois é erro comum o bastante para estar escrito;
- a retroprojeção gestacional, e por que a janela é **fixa**: usar a duração
  observada seria endógeno, porque prematuridade é desfecho;
- ⚠️ **a tensão do §4.5** — o estimador que produz a curva opera sobre dois
  períodos, o que torna o pré uma média única de 2015–2018; como essa janela é
  posterior ao marco de notícia (24/02/2015), a contaminação por antecipação
  **não é observável dentro da especificação principal**. Declarada, com três
  mitigações;
- que a contaminação do grupo `d = 0` **desloca o nível** da curva (o estimador
  centra em `mean(dy[dose==0])`) — aritmética, não apresentação;
- o critério de falsificação declarado **antes** de estimar, e o compromisso de
  reportar coeficiente abaixo do MDE como **limite superior**, não como achado;
- ⚠️ a nota de nomenclatura sobre Conley–Taber: construído para tratamento
  **binário**; com tratamento contínuo a adaptação fiel é permutar a dose. A
  lógica é a mesma, o procedimento não.

## Regras que valem aqui

- **Números de resultado não entram.** Onde há número na §4, ele é de **desenho**
  (poder, MDE, aritmética de exposição) e está marcado como tal.
- ⚠️ **Referências não verificadas não entram sem marca.** A §3 se apoia no
  referencial de `docs/framework-dissertacao.md` §4 (Pigou, Coase, Weitzman,
  Helfand & House, Lichtenberg–Parker–Zilberman, Skevas et al., Roth). **Nenhuma
  foi conferida contra DOI/Crossref** — as bases estão inacessíveis
  (`docs/lacunas-de-dados.md` §1, classe E). Por isso a §3 cita **em prosa, sem
  `\\cite`**: o `.bib` só se monta com DOI conferido, e o `CLAUDE.md` proíbe
  inventar referência. Marx-Stoelting et al. (2025) e Larsen et al. (2017)
  seguem na mesma situação.
- `paper/figures/` e `paper/tables/` recebem saída dos scripts, não arte feita à
  mão.
