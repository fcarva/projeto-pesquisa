# Integridade dos painéis fornecidos

Auditoria de 23/09/2026. Diretório-fonte: `C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa`. Os dados originais foram apenas lidos. Este adendo substitui a limitação de disponibilidade de dados da primeira rodada de auditoria, sem apagar seu histórico.

## O painel numérico é reproduzível

O arquivo `painel_ensaio1.parquet` tem SHA-256 `08b8fd390756fe6d8960e2e61c731fa9c97515ded21dc708affbb8d4c1973f1e`, 17.664 linhas, 86 colunas, 184 municípios e 96 meses, de janeiro/2015 a dezembro/2022. Não há chaves município–ano–mês duplicadas. A grade está completa, mas alguns desfechos estão ausentes: grade balanceada não equivale a desfecho observado em todas as células.

Reconstruí o painel em memória com a função `monta_painel` e os componentes atuais. As chaves e **todos os valores numéricos compartilhados** coincidem, com tolerância relativa e absoluta de 1e−10. Os timestamps mais recentes de alguns componentes não demonstram desatualização numérica do painel.

A reconstrução tem 87 colunas: acrescenta `ban_municipal_revogado_em`, ausente no arquivo salvo, e atualiza `ban_municipal_confianca` em 96 linhas. São diferenças de metadados legislativos. Não afetam as estimações aqui reproduzidas, que não condicionam nesses campos, mas a ausência da data de revogação pode afetar rotinas futuras que classifiquem vigência de bans municipais. Não se deve confundir a existência histórica da lei com sua vigência em 2015–2018.

## Componentes, cobertura e fontes

| Componente atual | Linhas | Proveniência gravada | Verificação principal |
|---|---:|---|---|
| SINASC CE | 17.654 | pysus | Todos os valores numéricos coincidem com o recorte CE das três aquisições FTP interestaduais |
| SIM fetal | 17.655 | dofet | Cobertura declarada 2015–2022; identidades de denominador e taxa conferem |
| SIH intoxicação | 46 | ftp | Saída esparsa, inadequada como painel de incidência sem tratamento dos meses sem evento |
| SINAN | 4.382 | ftp | Integração produz 17.664 células de taxas, inclusive zeros |
| PAM média municipal × cultura | 3.312 | arquivo SIDRA | Dose fixa no tempo; 169 positivos e 15 zeros |
| GAEZ | 184 | arquivo de aptidão | Nenhum município sem aptidão; definição 4 deixa 14 controles |
| População municipal anual | 1.472 | sidra | Denominadores presentes; permanece a mudança de origem em 2022 |

A concordância entre SINASC por pysus e por FTP foi verificada nos recortes CE dos arquivos CE+PI, CE+RN e CE+PE. Mudam os rótulos de transporte (`fonte`), não os valores numéricos. Isso sustenta a consistência entre aquisições da mesma fonte; não é validação externa independente da qualidade de registro do SINASC.

O painel simulado existe separadamente, com rótulo `simulado`, e não foi usado nas estimações. Suas chaves municipais não coincidem com as reais. A reconstrução numérica a partir dos componentes reais não revelou mistura de simulação no painel analisado. Isso não torna suficiente, em geral, o rótulo global `fonte=real`: o código ainda perde a proveniência individual das fontes durante o join.

## SIH: o canal não está operacional no painel atual

As taxas SIH de intoxicação têm **46 células observadas e 17.618 ausentes**, ou 99,74% da grade ausente. No contraste pré até dezembro/2018 e pós desde outubro/2019, restam **três municípios de dose positiva e nenhum controle** com observação nos dois períodos. Logo, esse painel não permite o DiD proposto para o canal SIH.

A causa no código é identificável: `prepara_internacoes` conserva apenas internações que casam alguma família de CID; `colapsa_muni_mes` agrega somente as células remanescentes; o join do painel não completa as contagens para as células sem evento. Na taxa acidental, 45 das 46 células observadas já são zero para essa família, pois entraram por outro CID; isso é distinto de completar a grade inteira.

Localizei os **96 arquivos RDCE mensais esperados para 2015–2022**, todos não vazios. Sua presença permite avançar na reconstrução da cobertura, mas não prova por si só a completude por data de internação: os arquivos são por competência e podem envolver defasagem de faturamento e recortes de residência. A correção deve primeiro registrar a cobertura das entradas e o calendário de referência, depois distinguir zero observado de ausência de cobertura. **Não preenchi todos os ausentes com zero nem estimei um efeito SIH a partir dessa suposição.**

O SINAN tem a grade de taxas preenchida, com 706 células de contagem agrícola positiva. Ele continua sujeito a notificação, classificação e cobertura; a existência de zeros não prova a ausência de intoxicações nem valida o mecanismo aéreo→terrestre.

## SIM e células pequenas

Há dez células sem peso médio/nascimentos e nove sem taxa fetal no painel. Uma célula de 2016 tem um óbito fetal, nenhum nascimento no denominador integrado, `sem_denominador=True` e taxa fetal igual a 1. A identidade `óbito/(nascidos vivos+óbitos)` confere aritmeticamente, mas esse caso merece verificação de cobertura e sensibilidade da média municipal. Não é, sozinho, prova de erro de registro ou motivo para exclusão automática.

As séries SINASC e SIM usadas aqui terminam em 2022, e há inventário DOFET para 2015–2022. Assim, o risco anteriormente demonstrado por exemplo sintético — preencher óbitos como zero em anos sem fonte, ao estender nascimentos até 2024 — **não foi observado nesta reprodução 2015–2022**. O código ainda precisa do controle de cobertura antes de uma extensão temporal.

## Rastreabilidade

Os detalhes, SHA-256, faltantes por ano e comparações de colunas estão em [integridade-paineis-agregados.json](integridade-paineis-agregados.json). A viabilidade por desfecho e o inventário SIH estão em [reproducao-empirica-diagnosticos.json](reproducao-empirica-diagnosticos.json). O script `work/audita_paineis_local.py` e os verificadores complementares acompanham o pacote de reprodução.

Esta etapa verifica os arquivos agregados fornecidos e sua integração; não refaz a limpeza de cada registro individual de todas as bases. A existência de painéis consistentes resolve a questão de reprodução numérica, mas não a medição da aplicação aérea efetivamente ocorrida antes e depois da lei.
