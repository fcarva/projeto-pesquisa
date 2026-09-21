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
| `main.tex` | esqueleto; ✅ **compila** |
| `secoes/01-introducao.tex` | ✅ **escrita** — fórmula de Head |
| `secoes/02-background.tex` | ✅ escrita |
| `secoes/03-teoria.tex` | ✅ escrita |
| `secoes/04-identificacao.tex` | ✅ escrita — é o que a banca defende |
| `referencias.bib` | ✅ **40 entradas, todas com DOI conferido** |
| §5 Dados e descritivas | ⬜ espera aquisição |
| §6 Resultados | ⬜ **fora do alvo da qualificação** |

```
latexmk -pdf -interaction=nonstopmode paper/main.tex
```

## ✅ Estado da compilação (2026-08-25)

**Compila.** 21 páginas, 20 referências impressas, **zero** *undefined citation*,
**zero** *undefined reference*, **zero** *overfull box*.

As duas advertências que este arquivo carregava caíram na mesma sessão:

- ~~"o `.tex` nunca foi compilado"~~ — havia MiKTeX na máquina do pesquisador.
  A previsão de que a tabela larga de ameaças (§4.8) pediria `\resizebox` ou
  `landscape` **não se confirmou**: ela cabe.
- ~~"nenhuma referência conferida contra DOI/Crossref"~~ — ver abaixo.

⚠️ **Uma armadilha encontrada e resolvida, para quem for editar:** o marcador
`⚠️` (U+26A0) quebra a compilação se aparecer em **texto composto** — em
comentário `%` é inofensivo. No texto, usar `\textbf{[a conferir]}`.

## ✅ Referências: o `.bib` existe, e como ele foi montado

`api.crossref.org` responde na máquina do pesquisador — o bloqueio registrado em
`docs/lacunas-de-dados.md` era do **proxy da sessão remota**, não do projeto.

Os campos do `.bib` **não foram digitados**: um script consultou o Crossref por
DOI e gerou cada registro a partir da resposta, de modo que erro de transcrição
é impossível por construção. **40 de 40 DOIs resolveram.**

O log completo — correções encontradas, o que não foi achado, e as lacunas de
depósito — está em `docs/referencias-verificadas.md`. O essencial:

- ⚠️ **Frank & Sudarshan é de 2024, não 2025** (AER 114(10):3007–3040). O
  material de projeto trazia o ano errado.
- ⚠️ **Marx-Stoelting et al. (2025) não foi encontrada** no Crossref. **Não
  entra no `.bib` e não é citada.**
- ⚠️ **DOI conferido autoriza a citação, não a afirmação sobre o achado.** Duas
  atribuições da primeira redação da introdução iam além do que o *abstract*
  sustenta e foram corrigidas — ver §5 do log.

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

## O que a §1 promete, e por que a promessa é estreita

A introdução segue a fórmula de Head (hook → pergunta → antecedentes → *value
added* → roadmap), e o hook é o assassinato de Zé Maria do Tomé — pelo mundo
real, nunca pela literatura, como Bellemare exige.

⚠️ **O pecado capital é o *bait-and-switch*: prometer na introdução o que o corpo
não entrega.** Como esta etapa não inclui resultado, a §1.3 **declara isso ao
leitor** num quadro próprio: o que se entrega é um **desenho**, e a ausência de
resultado é deliberada. Nenhuma frase da introdução anuncia achado.

⚠️ **Duas afirmações do hook e do *value added* estão marcadas `[a conferir]` em
nota de rodapé**, porque não têm fonte primária conferida: as circunstâncias do
assassinato (data e número de disparos — o material de projeto diz 25 tiros, sem
fonte) e a alegação de que projetos semelhantes tramitam em outros estados.

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
- **Nenhuma referência entra no `.bib` sem DOI resolvido no Crossref.** O
  procedimento está na §7 de `docs/referencias-verificadas.md`. Se o DOI não
  resolve, a referência não entra.
- **Afirmação sobre achado alheio exige conferir o *abstract*, não só o DOI.**
- `paper/figures/` e `paper/tables/` recebem saída dos scripts, não arte feita à
  mão.
