# Rodada 21 — mapa de lacunas e rodada exploratória com dado real (2026-11-15)

⚠️ **EXPLORATÓRIO.** Autorizado pelo pesquisador ("vamos rodar novas com dados
reais"). Nenhum número daqui entra em `paper/projeto/`. Consequência declarada:
o desenho de calendário **já foi cruzado com o desfecho do pós-lei**; a frase do
projeto que diz o contrário (`05-metodologia.tex`, último parágrafo) deixou de
ser verdadeira e precisa de decisão do pesquisador.

Reproduzir: `make exploratorio-calendario` (scripts `exploratorio/20`, `21`, `22`).
Dados em `projeto-pesquisa/data/` (cópia local, fora do git).

## 1. O que a máquina local supriu
| lacuna | estado | como |
|---|---|---|
| SINASC CE 2005–2014 e 2023–2024 | ✅ suprida | FTP do DATASUS; painel município × mês 2005–2024, 2,53 milhões de nascimentos, peso ausente 0,04% |
| SINASC RN 2005–2024 | ✅ suprida | idem; painel CE + RN |
| Censo Agro 2006, aeronave (SIDRA 1008) | ✅ refeito | CE: 36 estabelecimentos em 7 municípios (Limoeiro 18, Quixeré 9, Aiuaba 5, Jaguaruana 1, Mauriti 1, Quiterianópolis 1, Quixeramobim 1). RN: 5 em 2 (Januário Cicco 4, São Miguel 1) — **nenhum na Chapada potiguar** |
| Banana familiar, Censo Agro 2017 (SIDRA 6955) | ✅ suprida | CE: 152 municípios com banana; RN: 86. ⚠️ fração familiar por **área** sob sigilo em 68/152 (CE) e 64/86 (RN): o limiar só é operável por **estabelecimento** |
| Lei 1.511/2010 de Limoeiro | ✅ conferida | ver `conferencia-local-fontes.md` |
| Dossiê Abrasco, frequência de voos | ✅ conferido | idem |

Dois defeitos do `02_clean_births.py` apareceram e foram corrigidos: extensão
`.DBC` em maiúsculas no FTP (2005–2006, 2010–2012) e `CODMUNRES` de 7 dígitos em 2005.

## 2. O que continua faltando
| lacuna | por que importa | rota |
|---|---|---|
| **Chuva municipal por ano** (quadra chuvosa) | controle `θ_k` da equação principal; sem ela o exploratório abaixo não separa lei de chuva | FUNCEME (sem rota de dados documentada; pedido formal), EMPARN para o RN, ou grade CHIRPS |
| **Voos por município e mês** (`A_m` e estação medidos) | hoje `A_m` é o Censo 2006 e a estação é fev–mai por hipótese | LAI ao MAPA (IN 2/2008) e à ADAGRI — minutas prontas, **não protocoladas** |
| Aeronave depois de 2006 | Missão Velha (1.129 ha de banana, 20% familiar) e Russas (564 ha, 23% familiar) são banana empresarial **sem** aeronave em 2006; o relato de "duas aplicações por ano" é do Cariri | mesma LAI |
| Voos no RN | sem isso não se sabe se o RN é "sem avião" ou "com avião e sem lei" | LAI ao MAPA cobre os dois estados |
| Ação civil pública de 2011 (15ª Vara Federal) | diz se os voos pararam antes da lei | consulta processual JFCE — não tentada |
| Calzada et al., versão publicada | paywall | acesso institucional |
| Goodman-Bacon 2021; de Chaisemartin e D'Haultfœuille 2020, texto integral | seção 3.3 | Estágio 2.5 |
| Leis municipais de outros estados | uma reportagem | Estágio 2.5 |
| Óbito fetal 2005–2014, 2023–2024 | teste de seleção | FTP (DOFET), mesmo procedimento |

## 3. Exploratório A — Ceará, diferença tripla de calendário
Especificação do projeto sem os termos de chuva. `A_m` = Censo 2006; comparação =
banana (≥ 10 estab.) sem aeronave e fração familiar de estabelecimentos ≥ 0,5
(74 municípios); estação fev–mai; referência 2007–2011; 2012 e 2019 fora.

| especificação | tratados | β alta, pós (g) | β alta, seca (g) | β intermediária, pós (g) |
|---|---|---|---|---|
| 7 municípios do Censo 2006 | 7 | −21,3 | −18,4 | −72,6 |
| Limoeiro + Quixeré | 2 | +26,2 | −45,9 | −39,3 |
| aeronave fora da Chapada | 5 | −39,8 | −7,3 | −85,8 |
| referência 2008–2010 | 7 | −26,6 | −23,9 | −79,5 |
| pós sem 2020–2021 | 7 | −13,0 | −18,0 | −62,8 |
| limiar familiar 0,75 | 7 | −14,5 | −11,8 | −69,9 |
| **falso**: banana familiar × sem banana | 74 × 32 | −4,8 | +0,7 | +1,3 |

Inferência por permutação (tratados falsos sorteados entre os de comparação, 999
sorteios): 7 municípios, p = 0,24, placebos em [−38, +30], **efeito mínimo
detectável ≈ 49 g**; Chapada, p = 0,42, placebos em [−72, +67], **≈ 99 g**.
Estudo de evento 2005–2010 (base 2011): entre −13 e +32 g, sem padrão.

Leitura:
1. **Nada se distingue de ruído.** Sinal oposto entre a Chapada (+26) e os cinco
   de fora (−40).
2. **O poder é o problema previsto.** O efeito detectável (49–99 g) é média sobre
   todos os nascimentos do município; o análogo equatoriano dá ~80 g só para quem
   mora a ≤ 150 m. O efeito em intenção de tratar plausível é uma fração pequena disso.
3. **Sinal de alerta:** as coortes intermediárias dão −73 g, mais que as de
   exposição alta, puxadas pelos cinco municípios pequenos de fora da Chapada. Não
   é dose-resposta; é hiato sazonal instável, possivelmente chuva. Aiuaba,
   Quiterianópolis, Quixeramobim e Mauriti somam 8 estabelecimentos com aeronave e
   quase nenhuma banana: classificá-los como tratados é o mesmo erro de diluição
   da flag 7, agora no desenho novo.
4. **No período de seca** a Chapada dá −46 g (hiato fechando), compatível com
   voos suspensos **ou** com a seca alterando a sazonalidade — o projeto já
   declara que não distingue.
5. O tratamento falso passa (−5 g, erro-padrão 5).

## 4. Exploratório B — Chapada: CE × RN
| comparação | n comp. | β alta, pós (g) | β alta, seca (g) |
|---|---|---|---|
| Limoeiro + Quixeré × Chapada potiguar (7) | 7 | +14,7 | −58,4 |
| × Vale do Açu, banana (4) | 4 | +62,9 | −13,2 |
| × os dois grupos (11) | 11 | +24,0 | −49,4 |
| idem, sem Mossoró | 10 | +44,3 | −32,1 |
| × metade maior do RN (84) | 84 | +27,6 | −38,2 |

Permutação com 2 tratados falsos entre municípios potiguares: p = 0,52, placebos
em [−105, +73], efeito mínimo detectável ≈ 129 g.

Leitura: o sinal é positivo (o previsto pela hipótese) em todas as comparações com
o RN e coincide com o da Chapada contra a banana familiar cearense (+26), mas
**dois municípios tratados não sustentam inferência**: a distribuição placebo
é três a quatro vezes maior que o coeficiente.

## 5. Fundamentos de avaliação de política: o que cada grupo de comparação compra
- **Banana familiar cearense (principal).** Mesma lei, mesmos programas estaduais,
  mesma cultura; difere em escala, renda e irrigação. Identifica se o hiato sazonal
  teria evoluído igual em sequeiro e irrigado — a hipótese mais frágil, porque a
  seca atinge os dois de modo diferente.
- **Vizinhos potiguares.** Mesmo aquífero, clima, seca, mercado e empresas; não
  têm a lei. Em diferença simples seria fraco (tudo que é estadual muda junto). Na
  **diferença tripla**, município × ano absorve os choques estaduais; resta a
  hipótese sobre o hiato sazonal, mais crível entre irrigados vizinhos. Riscos:
  (i) vazamento — serviço aéreo migrando para o RN após 2019 infla a estimativa;
  (ii) deriva e aquífero partilhados atenuam; (iii) cultura diferente (Mossoró é
  melão: 7.600 ha contra 32 de banana) — Upanema (850 ha) e o Vale do Açu são os
  pares por cultura.
- **Os dois juntos** triangulam: erram por motivos diferentes. Concordância de
  sinal vale mais que qualquer um sozinho; aqui concordam em sinal para a Chapada
  e nenhum tem precisão.
- **O que nenhum resolve:** poucos tratados. A alavanca continua sendo medir os
  voos (quem, onde, quando) e, se possível, descer abaixo do município
  (setor censitário, distância ao bananal), que é onde o análogo equatoriano acha efeito.

## 6. Decisões que isto devolve ao pesquisador
1. O parágrafo do projeto "sem que a exposição sazonal tenha sido cruzada com os
   desfechos" precisa mudar ou a rodada precisa ser declarada.
2. O `A_m` provisório deve ser os 7 do Censo 2006 ou só a Chapada (Limoeiro +
   Quixeré)? Os dados mostram que são populações diferentes.
3. O RN entra no projeto como segunda comparação do desenho principal (hoje é só
   análise secundária)?
4. Teto de 80 g (ver `conferencia-local-fontes.md`).
