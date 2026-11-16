# Rechecagem de fontes feita na nuvem (2026-11-16)

Feita por agente de verificação com busca na web, sem acesso de escrita. O
que está aqui **não foi relido por mim na fonte**: a sessão local deve abrir
cada URL antes de alterar o projeto com base nisto.

## Resumo
| item | resultado | o que resta para a máquina local |
|---|---|---|
| Lei municipal 1.511/2010 (Limoeiro do Norte) | **Conferida na fonte primária.** Art. 212: "Fica revogada a Lei nº. 1.478, de 20 de novembro de 2.009." Art. 214 regula a pulverização aérea (1.000 m de povoações e mananciais de captação; 500 m de mananciais, moradias isoladas e animais; aviso de cinco dias). PDF: `camaralimoeirodonorte.ce.gov.br/arquivos/581/Leis_1511_2010_0000001.pdf` (68 p. escaneadas) | Baixar o PDF para `docs/legislacao/`; passar a fonte de `secundaria` a primária no CSV; atualizar a flag 0 do `CLAUDE.md` |
| Calzada et al. (2023, JAERE) | Conteúdo confere no manuscrito de 20/03/2023, no resumo publicado e nos slides do NBER (jul/2023). Texto tipografado atrás de paywall | Abrir a versão da revista com acesso institucional. Nuance: na subamostra de meninos, o 3º trimestre é significativo |
| Seção 3.3: Baker et al.; Callaway e Sant'Anna | Sustentado no texto do arXiv: Baker et al. tratam o caso de uma data de adoção (2×T) com o estimador de Callaway e Sant'Anna e grupo não tratado | Goodman-Bacon (2021) e de Chaisemartin e D'Haultfœuille (2020) não foram reabertos no texto integral |
| Ortiz-Villavicencio e Sant'Anna | Lido inteiro (arXiv v3). Só covariáveis anteriores ao tratamento e fixas no tempo. Pacote `triplediff` (CRAN 0.2.4), função `ddd()`; aborta com covariável que varia no tempo. Cabe no desenho com unidade município × mês do ano, dois períodos; frágil com poucos tratados; tratamento binário, então exposição alta e intermediária pedem rodadas separadas | Testar o pacote no painel simulado antes de prometer a sensibilidade |
| Callaway, Goodman-Bacon e Sant'Anna (contínuo) | Sustentado (arXiv v8). **Aceito na American Economic Review, "forthcoming"**, DOI 10.1257/aer.20240137 ainda sem volume | Atualizar a entrada `callaway2024continuous` quando sair; por ora, nota "no prelo, AER" |
| Ação civil pública de 2011 | Ajuizamento corroborado por nota do MPT-CE de 07/07/2011: 15ª Vara Federal, Limoeiro do Norte; MPF, MP-CE e MPT contra Fapija, Del Monte, Frutacor, Tropical Nordeste e Agrícola Famosa. Sem número de processo nem decisão localizados | Consulta processual na JFCE pelos nomes das partes |
| Suspensão dos voos na seca | Segunda fonte independente: entrevista de Raquel Rigotto ao IHU, 06/10/2016 ("a pulverização aérea não tem acontecido na região em função da seca"). Continua sem registro administrativo | Relatórios mensais do MAPA (pedido de acesso à informação) |

## 🔴 Achado que contradiz o texto atual do projeto
**Frequência de aplicações aéreas.** O projeto diz que "o único relato
disponível para o Ceará" indica aplicações menos frequentes
(`paper/projeto/secoes/03-referencial.tex:36`) e cita duas por ano, de um
produtor do Cariri (`02-contexto.tex:38`).

O agente encontrou fonte acadêmica para a Chapada do Apodi com frequência
maior: Dossiê Abrasco (2015, p. 152–153), citando Rigotto (2011), "a
pulverização aérea, adotada no cultivo da banana, e realizada de seis a oito
vezes por ano", e, citando Marinho, Carneiro e Almeida (2011), "no mínimo seis
pulverizações durante a quadra chuvosa". Há ainda coluna do setor com "média
de, apenas, 3 pulverizações aéreas". A Embrapa (2014, Agropolo
Jaguaribe-Apodi) confirma a sigatoka-amarela, o controle priorizado no período
chuvoso e a via aérea, sem dar número.

Consequências, a decidir pelo pesquisador:
1. "O único relato disponível" não se sustenta e precisa sair.
2. Seis a oito aplicações, concentradas em cerca de quatro meses, enfraquecem
   a leitura dos 80 g de Calzada et al. como teto folgado. A intensidade não
   foi convertida para a unidade daquele artigo (galões por hectare por mês).
3. A favor do desenho: concentração na quadra chuvosa é o pico sazonal de que
   a diferença tripla de calendário depende.

Não alterei `paper/projeto/`: a correção mexe no argumento do teto, que é de
conteúdo, e a sessão local pode estar editando os mesmos arquivos.

## Bloqueios
`journals.uchicago.edu` (403, paywall); `ecodebate.com.br` (403); consulta
processual da JFCE e do TRF5 não tentada.
