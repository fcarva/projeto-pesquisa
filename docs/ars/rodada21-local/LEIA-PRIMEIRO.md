# Rodada 21 — pipeline ARS completo, rodando localmente

Escrito em 2026-11-16, na sessão em nuvem, para ser lido pelo Claude Code na
máquina do pesquisador. A sessão em nuvem não alcança o computador: este
arquivo é a passagem de bastão.

## Por que rodar localmente
A rodada 20 (`docs/ars/pipeline-rodada20/`) correu em contêiner remoto, com
três limites que a máquina local não tem:

1. **Rede filtrada.** Fontes que o proxy bloqueou ou que só abriram em parte.
2. **Sem os dados.** Os microdados e painéis não estavam no contêiner.
3. **Contexto resumido várias vezes.** Decisões antigas chegaram por resumo.

## O que rechecar (o que a rodada 20 deixou conferido só em parte)
| item | estado na rodada 20 | o que fazer localmente |
|---|---|---|
| Lei municipal 1.511/2010 de Limoeiro do Norte | texto integral bloqueado pelo proxy | abrir `camaralimoeirodonorte.ce.gov.br/leis/581`, ler o artigo de revogação, guardar em `docs/legislacao/` |
| Calzada, Gisbert e Moscoso (2023, JAERE) | cifras conferidas no manuscrito de março de 2023, não na versão publicada | conferir na versão da revista: ~80 g, até 150 m, 3 meses ou mais |
| Seção 3.3: Baker et al. 2026; Callaway e Sant'Anna 2021; Goodman-Bacon 2021; de Chaisemartin e D'Haultfœuille 2020 | conferidos por resumo | conferir no texto integral cada afirmação atribuída |
| Ortiz-Villavicencio e Sant'Anna (arXiv 2505.09942) | lidos resumo e trechos da v3 | ler inteiro; ver se o pacote R dos autores serve a um desenho de coortes dentro do município |
| Callaway, Goodman-Bacon e Sant'Anna 2024 | só o resumo | texto integral; ver se há versão publicada em periódico |
| Suspensão dos voos na seca; ação civil pública de 2011 | imprensa e parte interessada | buscar os autos e fontes primárias |
| Sigatoka-amarela, ~2 aplicações aéreas por ano | um produtor, uma reportagem | buscar fonte técnica (Embrapa, ADAGRI) |
| Proibições municipais em outros estados | uma reportagem (Agência Pública, 2019) | conferir ao menos duas das leis citadas |
| Contagens do Censo Agropecuário 2006 (aeronave por município) | conferidas na nuvem | refazer a partir da tabela SIDRA 1008 |

**Atualização de 2026-11-16:** parte desta tabela já foi rechecada na nuvem.
Ler `rechecagem-nuvem.md` antes de começar: a Lei 1.511/2010 foi conferida
na fonte primária, e há um achado que contradiz o texto do projeto sobre a
frequência de aplicações aéreas (seis a oito por ano na Chapada, não duas).

Regra: o que não abrir fica escrito como "não conferido", com o motivo.

## Ordem de trabalho
1. **Preparar.** `git pull` no ramo `claude/gifted-maxwell-ryr7yk`; instalar o
   plugin (comandos no `CLAUDE.md`, seção "Plugin ARS"); `make projeto` para
   confirmar que compila com 15 páginas textuais.
2. **Conferir o bastão.** Ler `docs/ars/pipeline-rodada20/passport.yaml`, o
   ledger ao lado dele, `stage4.5_final_integrity_report_v7.md` e
   `stage6/registro_do_processo.md`. O reconhecimento final do Estágio 6 da
   rodada 20 ainda não foi dado pelo pesquisador: perguntar antes de abrir a 21.
3. **Rodada 21 em modo completo.** Passport e ledger novos em
   `docs/ars/rodada21-local/`. Entrada no Estágio 2.5 (integridade) sobre
   `paper/projeto/` como está, com a tabela acima como lista mínima; depois
   Estágio 3 (painel de cinco pareceristas), 4, 3', 4.5 e 6. Cada ponto de
   decisão é perguntado ao pesquisador e registrado no ledger nas palavras dele.
4. **Provas em R, só com dado simulado.** Gerador do painel do desenho
   principal com efeito plantado; bateria fixa: recuperação, tamanho do teste
   com poucos tratados, poder, falhas plantadas, sensibilidades. O cálculo de
   `scripts/estimate/14_mde_calendario.py` é anterior à exposição em grupos e
   precisa ser refeito. Todo script novo entra no `Makefile`.
5. **Laço autônomo.** Só sobre o simulado, com gerador e métrica travados,
   `data/` bloqueada por regra de permissão, um commit por experimento em ramo
   separado, limite de rodadas.

## O que não muda sem o pesquisador
- Projeto: só o Ensaio 1, até 15 páginas textuais, **sem estimativa própria**.
- Nada de rodar especificações sobre o desfecho real nesta rodada: o plano de
  análise é escrito e ratificado com o orientador antes.
- Estratégia de identificação e estimador principal são decisão do pesquisador.
- Nunca commitar `data/` nem microdado. Nunca inventar referência.

## Pedido para colar no Claude Code local
> Leia `CLAUDE.md` e `docs/ars/rodada21-local/LEIA-PRIMEIRO.md`. Faça a
> conferência do bastão da rodada 20 e me pergunte o que ela deixou em aberto.
> Depois rode o pipeline do Academic Research Skills em modo completo sobre
> `paper/projeto/`, entrando no Estágio 2.5, com a lista de rechecagem do
> arquivo como mínimo. Siga o protocolo do plugin à risca: ledger, passport e
> ponto de decisão a cada estágio. Não rode nada sobre dados reais.
