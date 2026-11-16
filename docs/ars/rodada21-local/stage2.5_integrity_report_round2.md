# Relatório de Verificação de Integridade Acadêmica — rodada 21, Estágio 2.5, verificação 2

Agente: `integrity_verification_agent` (ARS v3.24.2). Data: 2026-11-16.
Objeto: `paper/projeto/` (projeto_v8 = v7 + rodada de correção 1; alterações locais não
commitadas, vistas por `git diff -- paper`), PDF de 30 páginas gerado às 00:30:49, depois da
última edição dos `.tex` (00:30:44). O agente não editou o manuscrito, não rodou script de
análise e não tocou em `data/`. Não viu a rodada 1 ser feita; julgou o texto como está.

## Modo de verificação
Mode 1 (pré-revisão), reverificação após correção (2ª de até 3 rodadas). Escopo do protocolo:
itens corrigidos, mais a checagem C2 inteira (a correção mexeu em escopo e em regra de decisão),
mais as entradas novas e alteradas da bibliografia, mais o checklist dos 7 modos.

## Veredito
**FAIL** — 0 SERIOUS, 2 MEDIUM, 6 MINOR, mais notas.

As duas falhas graves da rodada 1 deixaram de existir: o texto não afirma mais o contrário do
que ocorreu, e "teto" e "único relato" sumiram de todo o projeto. Não há MAJOR_DISTORTION nem
referência fabricada. O FAIL vem de dois MEDIUM, ambos de correção curta:

1. IL-MEDIUM-1 ficou **parcial** de propósito (três fatos ainda sem fonte); os dados
   bibliográficos pedidos estão abaixo, prontos para virar entrada.
2. IL2-MEDIUM-1, **novo, criado pela correção**: a regra de decisão, que o texto declara
   inalterável, ficou sem limiar definido quando "teto de 80 g" virou "intervalo de 80 a 150 g".

Fora do veredito: o checklist dos 7 modos continua em **bloqueio** por Modos 3 e 6 SUSPECTED,
agora só pela regra formal (ver seção própria).

## Destino dos 12 achados da rodada 1

| ID | Destino | Texto atual (arquivo:linha) | Observação |
|---|---|---|---|
| IL-SERIOUS-1 | **RESOLVIDO** na exigência do portão | `05-metodologia.tex:303-310`: "Duas rodadas exploratórias antecedem o plano, e nenhuma é reportada aqui. [...] A de novembro estimou o desenho de calendário sobre os nascimentos de 2005 a 2024, com classificação e estação provisórias e sem a chuva: a exposição sazonal já foi cruzada com o desfecho do pós-lei." Compromissos de ordem reescritos: `05:171` ("Antes da análise confirmatória"), `05:248` ("Nenhum critério usa o desfecho do pós-lei"), `05:293-295` ("Para a regra de decisão, o efeito mínimo detectável [...]"), `05:299-301` ("antes da análise confirmatória"), `08-cronograma.tex:20` ("escrito antes da análise confirmatória") | Varredura de todas as seções, apêndices, quadros e resumo (fonte e PDF): não resta nenhuma frase que prometa plano "antes de qualquer contato/cruzamento com o desfecho" nem que negue o contato. A única ocorrência de "antes de qualquer" é `06-dados.tex:41` ("refeitas antes de qualquer uso"), sobre água e satélite. `04-objetivos.tex:16` ("só com dados anteriores à lei") e `projeto.tex:94`, `01:92-93`, `07:30` ("de antemão") são compromissos de desenho, não negação. A redação é fiel ao `mapa-de-lacunas-e-exploratorio.md` no que diz (2005–2024; Censo 2006 e fev–mai provisórios; sem chuva). O que ela **não** diz está em IL2-MEDIUM-1 e IL2-MINOR-2. Conferido pelas datas do git: o período de referência (commit `96dc402`) e o Quadro 2 (`df25151`) são anteriores aos scripts exploratórios (arquivos de 15/11, 23:23–23:45, hora local), o que sustenta "fixado de antemão". |
| IL-SERIOUS-2 | **RESOLVIDO** | `03-referencial.tex:32-40`; `01-introducao.tex:56-58` ("pelos relatos disponíveis"); `02-contexto.tex:37-40`; `05:248-249` ("tomado como referência"); `07-ameacas.tex:33-34` | Nenhuma sobra de "teto" nem de "único relato" (fonte e PDF, inclusive apêndices e quadros). Conferido por mim: Dossiê Abrasco 2015, p. 69 ("realizada de seis a oito vezes por ano, em áreas de cerca de 2.950 hectares") e p. 152 ("Como eram realizadas no mínimo seis pulverizações durante a quadra chuvosa"), no PDF do ICICT/Fiocruz. Calzada et al., manuscrito de 03/2023: "may range from 20 applications (cycles) per year per plantation to almost one application per week" (sustenta "vinte ou mais ciclos por ano"); "the gradients between 150 and 2500 meters from the nearest plantation are quite similar" (sustenta a frase de `03:35-36`); "between 80 and 150 grams" no resumo, na introdução e na conclusão. Resíduos: IL2-MINOR-1 (de que depende o intervalo) e IL2-MEDIUM-1 (regra de decisão). |
| IL-MEDIUM-1 | **PARCIAL** | Com fonte agora: `01:75` (`stf2025adi7794`), `02:20-21` (`lavor2019antes`), `apendices.tex:27` (`sindag2021plataforma`). **Sem fonte**: `02:66-69` (notícia de proibição e ação civil pública de 2011), `05:139-140` ("em 2011 já havia notícia de proibição"), `05:200` ("autos da ação civil pública de 2011"), `apendices.tex:133`; seca de 2012–2017 em `projeto.tex:91`, `05:23`, `apendices.tex:134` | As três fontes novas sustentam o uso (ver "Bibliografia"). `lavor2019antes` sustenta a unanimidade: "aprovou o projeto de lei 18/2015 sem nenhum voto contrário" e "a aprovação por unanimidade". Os três fatos restantes são verdadeiros e continuam sem citação; a nota do Apêndice D ("provêm de fontes secundárias") admite, mas não substitui. Dados para as entradas: seção "Três fontes pedidas". |
| IL-MINOR-1 | RESOLVIDO | `../referencias.bib:106` | "No prelo na American Economic Review". Página da AEA reaberta: "American Economic Review (Forthcoming)"; o DOI 10.1257/aer.20240137 segue 404 no Crossref. |
| IL-MINOR-2 | RESOLVIDO | `03:35-36` | Redação sugerida adotada; confere com a seção 4.2 do manuscrito. |
| IL-MINOR-3 | **PARCIAL** | `05:227` | Entrou "a versão binária da comparação"; não entrou "sob as hipóteses do Corolário 1" (dois grupos, dois períodos, tendências paralelas no tratamento observado). Resíduo MINOR. |
| IL-MINOR-4 | RESOLVIDO | `05:248` | "Nenhum critério usa o desfecho do pós-lei". |
| IL-MINOR-5 | RESOLVIDO | `08:38` | "Revisão final do ensaio"; a frase "tem cronograma próprio" foi cortada junto. |
| IL-MINOR-6 | RESOLVIDO | `01:72`; `apendices.tex:139` | "julgou constitucional a vedação"; "caput e § 1º do art. 28-B". |
| IL-MINOR-7 | RESOLVIDO, com resíduo | `03:76-79` | "cinco foram conferidas, com datas de 2009 a 2017, mas não a vigência". Resíduo: IL2-MINOR-3. |
| IL-MINOR-8 | RESOLVIDO | `referencias-projeto.bib:14`, `150`, `230`, `308` | (a) v3 confere (arXiv: v3 de 18/07/2025). (b) "versão 3, de 2026" confere (v3 de 30/04/2026). (c) "segunda apuração" retirado; o ano 2012 ficou e a citação sai "(IBGE, 2012)" — o metadado da tabela 1008 só diz "Censo Agropecuário", período 2006; nota, não achado. (d) Autoria trocada; a página credita "Coordenadoria de Imprensa do Governo do Ceará". Resíduo de caixa: IL2-MINOR-5. |
| IL-MINOR-9 | RESOLVIDO | `05:95-96` | "cujo início de gestação cai nos anos de seca". Nota: para os nascidos no fim de 2018 o início cai em 2018; a frase é aproximada. |

## Achados novos

### MEDIUM (corrigir)

| ID | Local | O que o texto diz | Problema | Fonte | Correção sugerida |
|---|---|---|---|---|---|
| IL2-MEDIUM-1 | `05-metodologia.tex:248-252` × Quadro 2 (`05:264-267`) × `apendices.tex:60` × `05:301-303` × `05:293-295` | "O efeito plausível é o intervalo do análogo equatoriano, tomado como referência, multiplicado pela fração de nascimentos exposta, para uma grade de valores fixada no plano de análise; decide o valor central da grade." O Quadro 2 decide por "Efeito detectável ≤ plausível". O Apêndice B diz "grade de frações". E `05:301-303`: a ratificação "pode alterar esses parâmetros, mas não o período de referência nem a regra de decisão". | (1) **A regra ficou indeterminada.** Com teto único (v7), "valor central da grade de frações" definia um número. Com intervalo de 80 a 150 g, "plausível" é uma faixa, e o texto não diz qual ponto dela entra na comparação (piso, ponto médio, teto) nem se a grade é só de frações ("grade de frações", Apêndice B) ou também de efeitos ("grade de valores", Seção 5.7). Uma regra declarada inalterável não pode ter o limiar em aberto. (2) **A escolha em aberto será feita com resultado à vista, e o texto não diz isso.** A rodada de novembro já calculou efeito mínimo detectável por permutação sobre o coeficiente do pós-lei, em três configurações, e o comparou com a regra do Quadro 2. O texto declara que "a exposição sazonal já foi cruzada com o desfecho do pós-lei" e conclui "Por isso municípios tratados e estação serão fixados pela medição dos voos"; a grade e o seu valor central, que decidem entre a linha 1 e a linha 2 do quadro, não entram nessa conclusão. | `docs/ars/rodada21-local/mapa-de-lacunas-e-exploratorio.md` §3–4 (efeito mínimo detectável por permutação); `docs/ars/rodada21-local/fundamentos-avaliacao-de-politica.md` §1, linha "Poder e efeito mínimo detectável" (comparação com o Quadro 2). Não li os registros de execução. | Decisão do pesquisador sobre o número; o portão pede só que a regra feche. Duas frases bastam: (a) fixar no próprio projeto o ponto do intervalo que decide (por exemplo, o piso de 80 g, que é a estimativa da especificação principal do artigo, ou o ponto médio) e dizer que a grade é de frações, igualando Seção 5.7 e Apêndice B; (b) acrescentar à divulgação que a rodada de novembro incluiu cálculo de poder com o desfecho do pós-lei, e que por isso a grade é fixada aqui ou por critério externo ao desfecho. Gravidade: julgamento meu, entre MINOR e MEDIUM; classifico MEDIUM porque incide sobre o único compromisso que o texto declara imune à ratificação. |
| IL-MEDIUM-1 (resíduo) | ver tabela de destino | — | Três fatos verdadeiros, que sustentam decisões de desenho (sensibilidade 2008–2010, pedido dos autos, janela da seca), sem entrada na lista de referências. | seção "Três fontes pedidas" | Criar as três entradas e citar em `02:66-69`, `05:23` (ou `projeto.tex:91` não: resumo não leva citação), `apendices.tex:133-134`. |

### MINOR (recomendado agora; obrigatório no Estágio 4.5)

| ID | Local | Problema | Fonte | Sugestão |
|---|---|---|---|---|
| IL2-MINOR-1 | `03-referencial.tex:32-33` | "déficit de 80 a 150 gramas, **conforme o limiar de intensidade**". O artigo não atribui o intervalo ao limiar. Conclusão do manuscrito: "a birth weight deficit of between 80 and 150 grams, with an impact that depends on the number of months of exposure to pesticides during gestation". A variação de limiar (seção 6.4) dá: 3 galões, sem efeito significante; 4 galões, 80 g; 5 galões, 104,3 g. O extremo superior vem de outras especificações (por exemplo, 157,1 g para exposição no primeiro trimestre, em outra seção). MINOR_DISTORTION. | Calzada et al., manuscrito de 03/2023, resumo, seções 5, 6.4 e 7 | "déficit de 80 a 150 gramas, conforme a especificação" ou "conforme a duração e o momento da exposição"; se quiser manter o limiar, dizer "de 80 gramas na especificação principal a 104 com limiar mais alto". Pequeno também: `03:37` "O valor serve de referência" depois de um intervalo ("O intervalo serve..."). |
| IL2-MINOR-2 | `05-metodologia.tex:303-310` | Divulgação fiel, mas incompleta em três pontos. (a) A rodada de novembro não foi só a especificação principal: incluiu a comparação Ceará × Rio Grande do Norte, variantes de limiar familiar (0,5 e 0,75), de grupo tratado (7 municípios e 2), de referência (2008–2010), sem 2020–2021, tratamento falso, e um estudo de evento com bases 2018 e 2014, diferentes da base 2011 do projeto (script `23_leads_lags_exploratorio.py`, posterior ao documento do mapa, que só lista os scripts 20–22). (b) Dos parâmetros que o texto deixa para o plano (`05:299-300`), o **limiar de agricultura familiar** e os **contrastes de falsificação** já foram variados com o desfecho à vista; o "Por isso" de `05:308` só cobre municípios tratados e estação. (c) O corte removeu a informação de que havia um plano versionado para a forma reduzida em setembro de 2026 (`docs/pre-especificacao.md`, fechado em 21/09/2026) e de que a rodada de setembro levou a desviar dele; "Duas rodadas exploratórias antecedem o plano" sugere que não havia plano, e a frase final "São planos em repositório" ficou sem antecedente no plural. | `mapa-de-lacunas-e-exploratorio.md` §3–4; `fundamentos-avaliacao-de-politica.md` §1–2; cabeçalho do script 23 (só o cabeçalho foi lido); `docs/pre-especificacao.md:3` | Uma frase: "A de novembro variou também o limiar de agricultura familiar, o grupo tratado e a base do estudo de evento, e incluiu a comparação com o Rio Grande do Norte; por isso esses parâmetros são fixados no plano por critério que não usa o desfecho." E repor: "O plano da forma reduzida, versionado em setembro de 2026, foi revisto depois da primeira." |
| IL2-MINOR-3 | `03-referencial.tex:76-79` | "Há proibições municipais em outros estados \cite{lavor2019antes}; cinco foram conferidas, com datas de 2009 a 2017, mas não a vigência". A reportagem citada não dá número nem data de lei (dá os municípios num mapa). O leitor não tem como saber quais cinco nem onde foram conferidas; a conferência foi do verificador da rodada 1, e as fontes não estão na lista. | relatório da rodada 1, IL-MINOR-7 (não reconferi as cinco leis nesta rodada) | Nomear em nota os cinco municípios e leis (Nova Venécia/ES, Lei 3.121/2011; Vila Valério/ES, Lei 550/2011; Boa Esperança/ES, Lei 1.649/2017; Luz/MG, Lei 1.764/2009; Campo Magro/PR, Lei 1.011/2017) ou dizer "conferidas no texto das leis" e citar ao menos uma fonte primária. |
| IL2-MINOR-4 | `02-contexto.tex:37-39`; `07-ameacas.tex:33-34`; `referencias-projeto.bib` (`carneiro2015dossie`) | Citação de livro de 624 páginas sem página, para afirmação pontual. E o relato é de estudo de 2011, em pretérito ("eram realizadas"), anterior à seca; o texto o põe ao lado de um relato de 2021 sem datar. | Dossiê Abrasco 2015, p. 69 e 152 (conferidas) | `\cite[p.~69, 152]{carneiro2015dossie}`; "em estudo de 2011". Na entrada, acrescentar ISBN 978-85-9876-880-9 e URL do Arca/Fiocruz é opcional. |
| IL2-MINOR-5 | `referencias-projeto.bib:230` e entrada `stf2025adi7794`; PDF p. 6 | Caixa inconsistente entre entradas novas e antigas: na mesma página saem "(BRASIL. Supremo Tribunal Federal, 2025)" e "(Brasil. Supremo Tribunal Federal, 2023)"; na lista, "CEARÁ. Governo do Estado" ao lado de "Ceará" e "Ceará. Assembleia Legislativa". | `projeto.bbl:78`, `87`, `147-198` | Uniformizar (a NBR 6023 pede a jurisdição em maiúsculas: mudar as antigas, não as novas). |
| IL-MINOR-3 (resíduo) | `05:227` | ver tabela de destino | Denteh e Kédagni, arXiv v3 | Acrescentar "e sob as hipóteses do Corolário 1". |

### Notas (não contam no veredito)
- `02:20-21`: `lavor2019antes` sustenta a unanimidade, não a data; a reportagem diz que o projeto foi votado antes do recesso e sancionado em 9 de janeiro. A data de 18/12/2018 foi conferida na rodada 1 em outra fonte. Sem ação obrigatória.
- Cortes conferidos: a frase-roteiro do fim da introdução e a fusão das duas linhas do cronograma não removeram conteúdo (as duas linhas tinham os mesmos bimestres). "Se o prazo apertar, a prioridade é: medição, desenho principal, análises secundárias" era uma regra de prioridade assumida de antemão; o corte não cria erro, mas retira um compromisso. A frase sobre o insumo do segundo ensaio continua em `03:19-22`; "tem cronograma próprio" saiu, e a linha "Início do segundo ensaio" segue no quadro, sem contradição.
- `sindag2021plataforma` sustenta "envio eletrônico só a partir de 2021": a matéria noticia o lançamento, em 16/06/2021, do módulo do Sipeagro para "envio digital dos relatórios das operações em campo" e diz que até então o envio vinha "apenas alimentando um arquivo com informações nunca processadas". A palavra "mensais" e a palavra "papel" não estão na matéria.
- Calzada et al., versão tipografada do JAERE: UNVERIFIABLE_ACCESS, como na rodada 1 (não reaberta).

## Bibliografia: entradas novas e alteradas

| Chave | Metadados | Uso no texto | Veredito |
|---|---|---|---|
| `carneiro2015dossie` | Conferidos na ficha catalográfica (PDF do ICICT/Fiocruz e registro do Arca): organização de Fernando Ferreira Carneiro, Lia Giraldo da Silva Augusto, Raquel Maria Rigotto, Karen Friedrich e André Campos Búrigo; Rio de Janeiro: EPSJV; São Paulo: Expressão Popular, 2015; 624 p. | `02:39`, `07:34`: seis a oito por ano; ao menos seis na quadra chuvosa. Sustentado (p. 69 e 152). | VERIFIED; IL2-MINOR-4 |
| `sindag2021plataforma` | Título e data (17/06/2021) conferidos na página, aberta por mim. | `apendices.tex:27`. Sustentado (nota acima). | VERIFIED |
| `stf2025adi7794` | Título e data conferidos na página: "12/03/2025 21:00"; ADI 7794, PSOL, distribuída ao ministro Luiz Fux, contra a Lei estadual 19.135/2024. | `01:75`. Sustentado. | VERIFIED; IL2-MINOR-5 |
| `callaway2024continuous` | NBER WP 32117 + "No prelo na AER". | — | VERIFIED |
| `ortiz2025triple` | arXiv:2505.09942, v3 (18/07/2025). | — | VERIFIED |
| `denteh2022misclassification` | arXiv:2207.11890, v1 de 25/07/2022, v3 de 30/04/2026. | `05:233` | VERIFIED |
| `ibge2006censoagro` | Título sem "segunda apuração"; ano 2012 mantido (nota). | — | VERIFIED com nota |
| `ceara2018nascer` | Autoria "CEARÁ. Governo do Estado"; página do HGCC credita a Coordenadoria de Imprensa do Governo do Ceará; 26/03/2018. | `apendices.tex:136` | VERIFIED; IL2-MINOR-5 |

Citações indefinidas: nenhuma. 54 chaves citadas, 54 itens no `.bbl`, zero "??" no PDF, sem
aviso de citação no `.log`.

## Três fontes pedidas (dados conferidos nesta rodada)

**1. Nota de proibição, 11/03/2011.**
- Original: BRASIL. Secretaria de Direitos Humanos da Presidência da República. *Pulverização de agrotóxicos com aeronaves está proibida na região da Chapada do Apodi, no Ceará*. Brasília, 11 mar. 2011. **URL original não localizada** (o sítio da SDH de 2011 não está no ar; não achei cópia arquivada).
- Reprodução lida: SINAIT (Sindicato Nacional dos Auditores Fiscais do Trabalho). *Agrotóxicos – Pulverizar com aeronaves está proibido na Chapada do Apodi*. 15 mar. 2011. URL: `https://www.sinait.org.br/noticia/2874/agrotoxicospulverizar-com-aeronaves-esta-proibido-na-chapada-do-apodi`. A página transcreve a nota sob "11-3-2011 – Sec. Especial de Direitos Humanos"; trecho: "As empresas produtoras de frutas instaladas na região da Chapada de Apodi, no Ceará, estão proibidas de utilizar aeronaves para pulverizar os pomares com agrotóxicos. Este é um dos principais resultados da missão da Comissão Nacional de Combate à Violência no Campo".
- **Como abri:** o servidor do SINAIT devolveu 504 e tempo esgotado ao acesso direto nesta sessão; li o texto pelo extrato do serviço de busca (variante `?print` da mesma URL). Título, data e trecho vêm desse extrato. Reabrir no navegador antes de gravar a data de acesso.
- Corroboração independente, aberta pelo mesmo serviço: FIOCRUZ. Mapa de Conflitos Envolvendo Injustiça Ambiental e Saúde no Brasil. *Uso indiscriminado de agrotóxicos contamina recursos hídricos e causa câncer em trabalhadores e moradores do Vale do Jaguaribe* (ficha "CE"; atualizada em maio de 2023). URL: `https://mapadeconflitos.ensp.fiocruz.br/conflito/ce-uso-indiscriminado-de-agrotoxicos-contamina-recursos-hidricos-e-e-a-provavel-razao-da-forte-incidencia-de-cancer-em-populacoes-trabalhadoras-e-moradoras-do-vale-do-jaguaribe`. Diz: "Em março de 2011, a Secretaria de Direitos Humanos da Presidência da República (SDH/PR) anunciou a proibição da pulverização aérea na Chapada do Apodi." A ficha cita outra reprodução (Combate Racismo Ambiental, 12 mar. 2011), que não abri.
- Sugestão de entrada: citar a reprodução do SINAIT como fonte consultada, com "apud" à SDH no título ou na nota. Nenhuma das fontes mostra ato normativo, o que o texto já diz (`02:68-69`).

**2. Ação civil pública, 07/2011.**
- BRASIL. Ministério Público do Trabalho. Procuradoria Regional do Trabalho da 7ª Região (MPT-CE). *Agrotóxicos no Apodi: MPs pedem à Justiça o fim da pulverização aérea e revisão de licenciamentos ambientais*. Fortaleza, 7 jul. 2011 (a página traz "Escrito por ASCOM em 07 Julho 2011"). URL: `https://www.prt7.mpt.mp.br/informe-se/noticias-do-mpt-ce/534-agrotoxicos-no-apodi-mps-pedem-a-justica-o-fim-da-pulverizacao-aerea-e-revisao-de-licenciamentos-ambientais`.
- **Abri diretamente** (HTTP 200 na URL completa e na curta `.../534-`; título conferido no `<title>`). Conteúdo: MPF, MPT e Ministério Público Estadual, "perante a 15ª Vara da Justiça Federal, em Limoeiro do Norte (CE)", contra a Fapija e "Del Monte Fresh, Fazenda Frutacor, Tropical Nordeste e Agrícola Famosa"; "A ação requer que a Justiça proíba a utilização de agrotóxicos mediante pulverização aérea na Chapada do Apodi" e a revisão das licenças pela Semace. Número do processo e desfecho: não constam.

**3. Seca de 2012–2017.**
- REBELLO, Aiuri. *Seca de 2012 a 2017 no semiárido foi a mais longa na história do Brasil*. UOL Notícias, São Paulo, 3 mar. 2018, 04h00. URL: `https://noticias.uol.com.br/meio-ambiente/ultimas-noticias/redacao/2018/03/03/seca-de-2012-a-2017-no-semiarido-foi-a-mais-longa-da-historia.htm`. Atenção: o título é "na história **do Brasil**"; o endereço é que termina em "da-historia". Trecho: "A seca que castigou o semiárido brasileiro de 2012 a 2017 [...] foi a pior da história já registrada no Brasil, aponta levantamento do Inmet". O texto diz ainda que 2009 foi o último ano acima da média "antes da estiagem que começou em 2012".
- **Como abri:** o UOL devolveu 403 ao acesso direto; li pelo extrato do serviço de busca (conteúdo em cache, obtido em 15/06/2026). Há cópia no Internet Archive de 19/10/2026 (`web.archive.org/web/20261019170109/...`), que não abri.
- Alternativa acadêmica, **com ressalva**: MARENGO, J. A.; ALVES, L. M.; ALVALA, R. C. S.; CUNHA, A. P.; BRITO, S.; MORAES, O. L. L. Climatic characteristics of the 2010-2016 drought in the semiarid Northeast Brazil region. *Anais da Academia Brasileira de Ciências*, v. 90, n. 2, supl. 1, p. 1973–1985, 2018. DOI 10.1590/0001-3765201720170206 (metadados conferidos no Crossref). O período do artigo é 2010–2016; **não sustenta "2012–2017" como escrito**, e só li o registro, não o texto. Para o intervalo que o projeto usa, a fonte que confere é a reportagem com o levantamento do Inmet.

## Fase C — reverificação

C1: nenhum número ou data do texto mudou além dos conferidos acima.

**Número de estimativa própria: nenhum.** Varredura dos `.tex` (padrões de decimal, valor-p,
erro-padrão, intervalo, grama e percentual) e das páginas textuais do PDF. Os únicos números com
unidade são da literatura (23 a 32 g; 80 a 150 g) e de definição (2.500 g; 37 semanas; 150 m).
A divulgação das rodadas exploratórias não traz número.

C2, consistência interna depois da correção:
- Períodos: referência 2007–2011, transição 2012 e 2019, seca 2013–2018 por nascimento, pós de 2020 em diante, sensibilidades 2008–2010 e sem 2020–2021 — coincidem entre a Seção 5, os objetivos e os Apêndices B, C e D.
- O que é confirmatório: uma só hipótese (`04:27`, `05:295-297`, `06:14-16`, Apêndice C), sem conflito com a nova redação. A linha 5 do Quadro 2 (registros não obtidos: Censo 2006 e quadra chuvosa, "declarado exploratório") é a mesma especificação que a rodada de novembro já rodou; o rótulo "exploratório" é coerente com isso.
- Regra de decisão contra "intervalo ... tomado como referência": **inconsistente/indeterminada** — IL2-MEDIUM-1.
- "Duas rodadas exploratórias antecedem o plano" contra a existência de plano versionado em setembro — IL2-MINOR-2 (c).

Páginas: 30 no PDF; textuais numeradas de 5 a 19 (**15 páginas**); Referências começa na **p. 20**
(`projeto.toc` e PDF), apêndices de 25 a 29. A restrição "até 15 páginas textuais" está cumprida, sem folga.

C4: passport com `experiment_intake_declaration` (`no_experiments_declared`, `declared_by`,
`declared_at`); nenhuma das cinco condições de FAIL se verifica (não há manifesto nem frase de
resultado próprio). O que o texto divulga pesa no checklist, abaixo.
"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the
experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

E4 (escopo): "só o Ensaio 1", "até 15 páginas textuais" e "nenhum número de estimativa" respeitadas.
E6 (deriva de força das afirmações na revisão): as alterações enfraqueceram ou qualificaram
("teto" → "referência"; "único relato" → "os relatos divergem"; "antes de qualquer contato" →
"antes da análise confirmatória"); nenhuma afirmação ficou mais forte que a fonte, salvo o
atributo de IL2-MINOR-1.

## Checklist dos 7 modos de falha de pesquisa com IA

Regra aplicada, literal: a declaração é `no_experiments_declared`, resposta do pesquisador "Não
reporta". O protocolo manda: se o texto, ainda assim, apresenta análises de dados como executadas
pelo autor (resultados, parâmetros de execução ou texto de Métodos que as descreve como feitas),
declaração e texto discordam; nenhum dos Modos 1, 3, 5 e 6 é NOT APPLICABLE, e os Modos 3 e 6
ficam SUSPECTED. O texto agora apresenta, e com mais clareza que na v7: "A de setembro de 2026
estimou a forma reduzida estadual e levou a rever seu alvo"; "A de novembro estimou o desenho de
calendário sobre os nascimentos de 2005 a 2024, com classificação e estação provisórias e sem a
chuva" (`05:304-307`); "um levantamento preliminar encontrou uma proibição" (`06:33`);
"Avaliações preliminares [...] indicaram limitações" (`06:40-41`). A regra dispara.

| Modo | Resultado | Pela regra formal ou pelo mérito | Evidência | Bloqueia? |
|---|---|---|---|---|
| 1. Erro de implementação que passa na autorrevisão | CLEAR | mérito | O texto não traz resultado numérico próprio; as perguntas de detecção não têm objeto. Ressalva: não vi registros de execução das rodadas exploratórias. | não |
| 2. Citação alucinada | CLEAR | mérito | 54 de 54 referências existem; as 3 novas e as 5 alteradas foram conferidas nesta rodada. | não |
| 3. Resultado experimental alucinado | **SUSPECTED** | **só pela regra formal** | Declaração "Não reporta" contra quatro frases que apresentam análises próprias como feitas. No mérito, nada a suspeitar: não há número; os únicos resultados narrados são qualitativos ("levou a rever seu alvo", "indicaram limitações", "encontrou uma proibição", esta conferida na fonte primária na rodada 1). | **sim** |
| 4. Atalho | CLEAR | mérito | Não há resultado; o desenho prevê tratamento falso, placebo de composição e estudo de evento. Só sinaliza neste estágio. | não |
| 5. Erro reapresentado como achado novo | CLEAR | mérito | Nenhuma ocorrência de "surpreendente", "inesperado" ou equivalente. | não |
| 6. Fabricação de metodologia | **SUSPECTED** | **só pela regra formal** | Na rodada 1 era substantivo (o texto negava a rodada de novembro). Esse motivo acabou: a Metodologia agora descreve o que o registro do repositório descreve. O que resta é a discordância formal entre declaração e texto, e a divulgação incompleta de IL2-MEDIUM-1 e IL2-MINOR-2, que é omissão, não fabricação. Não vi configuração nem registro de execução, de modo que, mesmo sem a regra, o mais que eu poderia dar no mérito é "sem contradição conhecida". | **sim** |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE | mérito | Seguem abertas as escolhas que a rodada de novembro devolveu (grupo tratado de 7 ou 2 municípios; Rio Grande do Norte como segunda comparação; efeito detectável acima do plausível). A regra de decisão prevê o cenário sem poder, o que pesa contra o travamento. Depende de resposta do pesquisador. | não (aviso; rever no 4.5) |

Condição de bloqueio: qualquer modo SUSPECTED, exceto o 4. Há dois, **ambos apenas pela regra
formal**. O bloqueio não é achado das Fases A–E e não muda o veredito; só o pesquisador o destrava,
por modo: confirmar e voltar ao texto; afastar com justificativa registrada (por exemplo: as
rodadas existem, estão divulgadas no texto e nenhum resultado delas é reportado, que é o sentido de
"Não reporta"); ou revisar a passagem e repetir a checagem. Observação: enquanto o texto divulgar
as rodadas e a declaração seguir `no_experiments_declared`, a regra continuará disparando em
qualquer reverificação; retirar a divulgação para silenciá-la recriaria o IL-SERIOUS-1.

## Não conferido (com o motivo)

1. **Nota original da SDH de 11/03/2011** — URL não localizada; lida em reprodução.
2. **Página do SINAIT, acesso direto** — 504 e tempo esgotado nesta sessão; lida por extrato do serviço de busca.
3. **Reportagem do UOL, acesso direto** — 403; lida por extrato em cache do serviço de busca. Cópia do Internet Archive não aberta.
4. **Marengo et al. (2018)** — só metadados (Crossref); texto não lido.
5. **Ação civil pública de 2011** — número, andamento e desfecho: consulta à JFCE/TRF5 não tentada.
6. **Cinco leis municipais de outros estados** (`03:76-79`) — não reconferidas; apoio na rodada 1.
7. **Calzada et al., versão tipografada do JAERE** — não reaberta (403 na rodada 1); conferido o manuscrito de 03/2023. Apêndice online (tabelas A6–A7) não aberto: os valores de 3 e 5 galões vêm do corpo do texto.
8. **Rodada de setembro de 2026** — a frase "estimou a forma reduzida estadual e levou a rever seu alvo, da curva para o nível" não foi conferida contra registro de execução; só confirmei que `docs/pre-especificacao.md` existe e está datado de 21/09/2026.
9. **Scripts `scripts/exploratorio/20–23`, registros de execução e dados** — fora do mandato; do script 23 li só o cabeçalho. O documento de fundamentos remete a uma "seção 7 do mapa de lacunas" que não existe no arquivo atual (vai até a §6).
10. **Referências não tocadas pela correção** — não reverificadas (protocolo de reverificação); valem os resultados e as lacunas da rodada 1.
11. **Rótulo e ano (2012) da tabela SIDRA 1008** — o metadado da API traz só "Censo Agropecuário", 2006.
12. **Originalidade D1 por busca na web e D2** — não executadas (restrição do despacho), como na rodada 1. Os trechos novos são paráfrases com citação.
13. **Semantic Scholar (A0)** — não usado; verificação por arXiv, Crossref, AEA e fonte primária.

## Aviso de limitação da ferramenta

> A checagem de originalidade (Fase D) não usou busca de frases na web nem software de detecção
> de plágio (Turnitin, iThenticate). Vale como triagem preliminar; recomenda-se ferramenta
> profissional antes da entrega formal.

Este relatório verifica as populações registradas acima. Não garante a completude da extração de
afirmações, a verdade do que está nas fontes, nem a correção de análises que não examinei.

## Trilha de auditoria

Abertos diretamente nesta rodada:
`diposit.ub.edu/server/api/core/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/content` (PDF, texto extraído e lido);
`www.icict.fiocruz.br/sites/www.icict.fiocruz.br/files/DossieAbrasco_2015_web.pdf` (PDF, p. 69 e 152 impressas);
`apublica.org/2019/02/antes-do-ceara-8-municipios-ja-haviam-proibido-fumigacao-aerea-de-agrotoxicos/`;
`noticias.stf.jus.br/postsnoticias/partido-questiona-lei-do-ceara-que-autoriza-pulverizacao-de-agrotoxicos-por-drones/`;
`sindag.org.br/setor-ganha-plataforma-digital-para-envio-de-relatorios-ao-mapa`;
`www.prt7.mpt.mp.br/informe-se/noticias-do-mpt-ce/534-agrotoxicos-no-apodi-mps-pedem-a-justica-o-fim-da-pulverizacao-aerea-e-revisao-de-licenciamentos-ambientais`;
`www.hgcc.ce.gov.br/2018/03/26/ceara-lanca-programa-para-reduzir-mortes-maternas-e-neonatais`;
`arxiv.org/abs/2207.11890`; `arxiv.org/abs/2505.09942`;
`www.aeaweb.org/articles?id=10.1257/aer.20240137`; `api.crossref.org/works/10.1257/aer.20240137` (404);
`api.crossref.org/works/10.1590/0001-3765201720170206`;
`servicodados.ibge.gov.br/api/v3/agregados/1008/metadados`.

Lidos por extrato do serviço de busca: `sinait.org.br/noticia/2874/...`; ficha do Mapa de Conflitos
(Fiocruz); `noticias.uol.com.br/.../seca-de-2012-a-2017-no-semiarido-foi-a-mais-longa-da-historia.htm`;
registro do Arca/Fiocruz e ficha catalográfica do Dossiê.

Falharam: `sinait.org.br` (504), `noticias.uol.com.br` (403), `freshfruitportal.com` (410),
`dssbr.ensp.fiocruz.br/.../DossieAbrasco_2015_web.pdf` (404).

Locais: `git diff -- paper`; `projeto.pdf`, `projeto.toc`, `projeto.bbl`, `projeto.blg`, `projeto.log`;
`git log` das seções; datas de arquivo de `scripts/exploratorio/`; `docs/pre-especificacao.md` (linha 3);
os três documentos de `docs/ars/rodada21-local/` e o `passport.yaml`.

Buscas feitas: só títulos, autores citados, DOIs, nomes de órgãos, de municípios e de empresas que
constam de notas públicas. Nenhum nome de pesquisador nem trecho do projeto foi enviado a buscador.
