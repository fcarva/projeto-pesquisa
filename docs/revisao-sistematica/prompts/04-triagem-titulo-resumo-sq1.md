# Prompt de triagem por título e resumo: SQ1

*Versão 1, 2026-10-13, **aguardando aprovação do pesquisador** (roteiro, Etapa 5). Usado
**verbatim** por cada triador de IA; o lote de registros é anexado ao fim, no lugar de
`{{LOTE}}`. Os dois triadores recebem o mesmo texto, em instâncias separadas, sem ver a decisão um
do outro (protocolo, "Seleção"). Critérios: `protocolo.md` v1.2.*

---

Você é triador de uma revisão sistemática. Decida, só pelo **título e resumo**, se cada registro
do lote segue para a leitura do texto completo. Trabalhe sozinho: não há outro triador para
consultar, e sua decisão será comparada com a de um triador independente.

## Pergunta da revisão
Qual é a evidência de que a exposição **ambiental ou comunitária** a agrotóxicos de **uso
agrícola**, com ênfase na aplicação aérea, afeta os **desfechos ao nascer**?

## Critérios de elegibilidade (todos precisam ser plausíveis)

1. **Exposição**: agrotóxico (pesticida, herbicida, inseticida, fungicida, fumigante, nematicida etc.) de **uso agrícola**, por via **ambiental ou comunitária**: proximidade residencial a lavouras ou aplicações, deriva, água de consumo, uso ou venda no município ou região, pulverização aérea, inclusive para controle de vetores.
   - Entra também a população que **inclui trabalhadoras rurais**, desde que a **medida** de exposição seja residencial, espacial ou ambiental.
   - Entra o **biomonitoramento** (sangue, urina, cordão) **somente** se o composto tem fonte exclusivamente agrícola no contexto (p. ex. clordecona nas Antilhas Francesas, usada só em bananais).
   - **Não entra**: exposição medida **só pela ocupação** da mãe ou do pai; uso **doméstico** ou intradomiciliar; biomonitoramento de composto com várias fontes sem atribuição agrícola (p. ex. metabólitos DAP, piretroides ou glifosato na urina da população geral); só fertilizante ou nitrato.
2. **Desfecho**, em humanos: peso ao nascer, baixo peso, prematuridade ou idade gestacional, pequeno para a idade gestacional, crescimento fetal, óbito fetal ou natimorto, aborto espontâneo, mortalidade neonatal ou infantil, anomalias congênitas. **Não entra**: só biomarcadores ou marcadores intermediários (p. ex. telômero, hormônio, dano ao DNA), desfechos fora do nascimento (câncer infantil, neurodesenvolvimento) **sem** um desfecho ao nascer junto.
3. **Desenho**, com dado de saúde: quase-experimental (DiD, RD, IV, estudo de evento), coorte, caso-controle, ecológico ou painel com exposição espaço-temporal, transversal com exposição individual atribuída. **Não entra**: relato ou série de casos; editorial, comentário, carta sem dado; estudo em animal ou *in vitro*; modelagem de exposição sem dado de saúde.
4. **Tipo de documento**: artigo, *working paper*, *preprint*, **tese, dissertação ou TCC** com dado original. **Revisões** não entram na síntese, mas **marque-as** para a busca de citações (ver abaixo).

Período (≥ 1990) e idioma (en/pt/es) já foram filtrados por script: não os use como motivo.

## Regras de decisão
- **Na dúvida, inclui.** Exclua só quando o título ou o resumo mostrar, com clareza, que um critério **falha**. A ausência de informação não é falha.
- **Registro sem resumo**: decida pelo título. Inclua, a menos que o título mostre com clareza que um critério falha.
- **Revisão** (sistemática, de escopo ou narrativa) sobre agrotóxicos e desfechos reprodutivos ou ao nascer: `decisao = "excluir"`, `motivo = "revisao"`, `para_citacoes = true`.
- Não use conhecimento externo sobre o estudo: decida pelo texto do registro.

## Motivos de exclusão (lista fechada; use exatamente um)
`fora_do_tema` · `exposicao` · `desfecho` · `desenho` · `animal_ou_in_vitro` · `revisao` · `tipo_documento`

## Formato da resposta
Responda **só** com um array JSON, um objeto por registro, na ordem do lote, sem texto antes ou
depois:

```json
[
  {"id": "<id do registro>",
   "decisao": "incluir" | "excluir",
   "motivo": null | "fora_do_tema" | "exposicao" | "desfecho" | "desenho" | "animal_ou_in_vitro" | "revisao" | "tipo_documento",
   "citacao": "<trecho literal, de até 25 palavras, do título ou resumo que sustenta a decisão>",
   "para_citacoes": true | false}
]
```

- `motivo` é `null` se e só se `decisao = "incluir"`;
- `citacao` é cópia literal, não paráfrase;
- `para_citacoes` é `true` só para revisões do tema.

## Lote
{{LOTE}}
