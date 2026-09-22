# Referências conferidas contra Crossref

*2026-08-25. Log da conferência que destravou o `.bib`. **40 de 40 DOIs
resolvidos**; uma referência do material de projeto **não** foi encontrada.*

⚠️ Este documento existe porque o `CLAUDE.md` proíbe inventar referência, e
porque até esta sessão **nenhuma** citação do projeto tinha sido conferida. O
`paper/referencias.bib` é a saída; este arquivo é a prova de trabalho.

---

## 0. O que mudou, e por quê

`docs/lacunas-de-dados.md` §1 classificava a conferência bibliográfica como
**classe E — fora de alcance**, com a observação de que `api.crossref.org`,
`doi.org`, `api.semanticscholar.org` e `pubmed` respondiam **000**.

Isso era verdade **da sessão remota**, não do projeto. Rodando na máquina do
pesquisador, `api.crossref.org` responde normalmente. A classe E, no que diz
respeito a bibliografia, **está resolvida** — e o que a bloqueava era o proxy da
sessão, não o acesso do pesquisador.

**Consequência prática:** as §2, §3 e §4 do `paper/` foram escritas citando *em
prosa, sem `\cite`*, precisamente porque o `.bib` não podia ser montado com
honestidade. Essa restrição caiu.

---

## 1. Método, e por que ele não admite erro de digitação

Os campos do `.bib` **não foram digitados**. Um script consultou
`api.crossref.org/works/<DOI>` para cada entrada e gerou o registro BibTeX a
partir da resposta — autor, título, periódico, volume, número, páginas e ano.
Erro de transcrição é, por construção, impossível; o que pode restar é DOI
errado, e é isso que a lista abaixo confere.

Onde o Crossref responde, o Crossref manda. Onde ele **não** deposita um campo,
o campo fica **ausente** no `.bib` — não preenchido de memória. Ver §4.

---

## 2. Correções encontradas

Cinco divergências entre o material de projeto e o registro oficial. A primeira
é a que mais importa, porque um ano errado numa referência de 2024 citada como
2025 é o tipo de erro que um parecerista encontra.

| Referência | O que o projeto dizia | O que o registro diz |
|---|---|---|
| **Frank & Sudarshan**, vultures/Índia | "AER (2025), *(confirmar volume/DOI)*" | ⚠️ **2024**, AER **114(10):3007–3040**, doi `10.1257/aer.20230016` |
| **Callaway, Goodman-Bacon & Sant'Anna**, AEA P&P | "*(confirmar autoria/entrada)*" | ✅ confirmado: os três autores, *Event Studies with a Continuous Treatment*, **114:601–605** |
| **Roth, Sant'Anna, Bilinski & Poe** | "*(confirmar páginas)*" | ✅ **235(2):2218–2244** |
| **Rambachan & Roth** | "*(confirmar)*" | ✅ **90(5):2555–2591** |
| **Sorensen Montoya**, nitrato | sem DOI, só URL ScienceDirect | ✅ doi `10.1016/j.jeem.2025.103197`, JEEM **133**:103197 |

---

## 3. ⚠️ A que NÃO foi encontrada

**Marx-Stoelting et al. (2025), *Comment on "The economic impacts of ecosystem
disruptions"*, Science (Technical Comment).**

Busca bibliográfica no Crossref **não retorna** este comentário técnico. O
`10.1126/science.adg0344` (o artigo original do Frank) resolve normalmente, então
não é bloqueio de editora — é que o registro do comentário não aparece na busca.

**Situação:** continua **não verificada**, e portanto **não entra no `.bib`** nem
é citada no texto. `docs/estado-da-arte.md` [N2b] a apresenta como a crítica de
identificação que a banca vai reproduzir (falácia ecológica, erro de medida na
exposição, confundidores maternos) — argumento útil e que **não depende** da
citação existir. O texto pode fazer o argumento sem atribuí-lo.

**Próximo passo:** conferir direto no site da *Science* (busca por comentários
técnicos ao artigo) ou pelo PubMed. Não foi feito aqui.

---

## 4. ⚠️ Lacunas de depósito — não são lacunas de conferência

Alguns editores não depositam todos os campos. Onde falta abaixo, falta **no
registro oficial**:

| Entrada | Campo ausente no depósito |
|---|---|
| Weitzman (1974), *Prices vs. Quantities* | só a **primeira página** (477) |
| Larsen et al. (2017), *Nature Communications* | sem página (o artigo tem número, não faixa) |
| Reynier & Rubin (2025), *PNAS* | sem página |
| Frank (2024), *Science* | sem página |
| Böcker et al., ERAE | ⚠️ registro é o de **advance access (2019)**: sem volume, número ou páginas. O material de projeto informa 47(2):371–402 (2020) — plausível, mas **não conferível pelo Crossref**. A entrada carrega `note` dizendo isso |

Nenhuma delas impede a citação: o DOI identifica o trabalho.

---

## 5. Achados de conferência dos resultados citados

Além do DOI, os *abstracts* depositados foram lidos para conferir o que o texto
atribui a cada trabalho. Duas atribuições da primeira redação da introdução
**estavam além do que a fonte sustenta** e foram corrigidas:

| Atribuição | Situação |
|---|---|
| DRS: "o efeito desaparece onde a água de consumo não vem do rio" | ⚠️ **não** consta do *abstract*. Trocado pelo que consta: identificação por direção do fluxo dentro da bacia, deterioração a jusante, e **+5%** de mortalidade infantil na especificação preferida |
| Reynier & Rubin: "redução de 23 a 32 gramas" | ✅ **CONFERE — corrigido em 2026-09-22.** A ressalva anterior dizia que a magnitude "vem do material de projeto, não do *abstract*". A primeira metade era falsa e a segunda é irrelevante: o texto completo (PMC11761964, Discussão) traz **verbatim** *"reduced average birthweight by 23 to 32 g at the average level of glyphosate exposure"*. O PNAS publica *Significance* no lugar do resumo numérico, e foi isso que a verificação por *abstract* não alcançou. Estimativa central: **29,8 g** à intensidade média de 2012. ⚠️ E o decil inferior perde **75 g** contra **6 g** no superior — é daí que vem o "doze vezes" |
| Larsen et al.: efeito só na cauda superior | ✅ confere — **5 a 9%**, apenas acima do percentil 95 |
| Frank (2024): inseticida ↑, mortalidade infantil ↑ | ✅ confere — **+31,1%** de inseticida, **+7,9%** de mortalidade infantil |
| Camacho & Mejía (2017) | ⚠️ **sem *abstract* depositado**. A descrição no texto se apoia no título, e uma nota de rodapé declara isso. Conferir contra o texto integral |

**A regra que isso estabelece:** DOI conferido autoriza a **citação**; não
autoriza a **afirmação sobre o achado**. São duas conferências distintas, e a
segunda depende de *abstract* ou texto integral.

---

## 6. O que entrou no `.bib`

40 entradas, todas com DOI resolvido em 2026-08-25. Blocos:

- **Antecedentes diretos** — Dias-Rocha-Soares; Reynier & Rubin; Camacho &
  Mejía; Larsen et al.; Frank; Frank & Sudarshan; Sorensen Montoya.
- **Teoria e instrumento** — Weitzman; Coase; Helfand & House; Lichtenberg,
  Parker & Zilberman; Skevas et al.; Fernandez-Cornejo et al.; Roth (2002);
  Böcker et al.; Finger; Voica & Schmitz; Chatzimichael et al.
- **Método DiD** — Callaway, Goodman-Bacon & Sant'Anna (WP e AEA P&P); Callaway
  & Sant'Anna; Goodman-Bacon; de Chaisemartin & D'Haultfœuille; Sun & Abraham;
  Borusyak et al.; Sant'Anna & Zhao; Roth et al.; Rambachan & Roth;
  Arkhangelsky et al.; Baker et al.
- **Inferência com poucos clusters** — Conley & Taber; Cameron, Gelbach &
  Miller; Canay, Santos & Shaikh.
- **Idioma ag-econ e contexto** — Henningsen et al.; Bravo-Ureta et al.;
  Bustos et al.; Greenstone & Hanna; Keiser & Shapiro; Shirangi et al.;
  Rocha & Rigotto.

**Citadas no documento atual: 20.** As demais estão no `.bib` para as seções que
ainda não existem; `natbib` só imprime o que se cita.

---

## 7. Como repetir a conferência

Uma entrada nova só entra no `.bib` depois de:

```bash
curl -s "https://api.crossref.org/works/<DOI>" | python -m json.tool | head -40
```

Se o DOI não resolve, a referência **não entra**. Se resolve mas o campo falta,
o campo fica vazio e a lacuna vai para a §4 deste arquivo.
