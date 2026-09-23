# Continuação local — de onde a sessão remota parou

*2026-09-22. Passagem de bastão da sessão remota `session_01FvxuFoRvMtVrRRYhTKWYrL`
(branch `claude/exciting-noether-17cl74`, último commit `9b562c9`) para o
Claude Code na máquina do pesquisador. Quem abrir uma sessão nova começa por
aqui, depois `docs/ars/13-rota1-calzada-januzzi-censo.md` §6.*

**Por que local:** a sessão remota não alcança SIDRA, DATASUS, servicodados,
Planalto nem Crossref (403 no proxy). O código dos passos 2–4 está pronto e
testado sem rede; só falta a rede.

---

## 1. Retomar (10 min)

```powershell
cd C:\Users\DELL\Documents\projeto-pesquisa\projeto-pesquisa
git fetch origin
git switch claude/exciting-noether-17cl74
git pull origin claude/exciting-noether-17cl74
pip install -r requirements.txt      # openpyxl é novo
python -m pytest tests/ -q           # esperado: 294 passed (3 exigem requirements-geo.txt)
```

Puxar a conversa inteira em vez de só o código: `claude --teleport
session_01FvxuFoRvMtVrRRYhTKWYrL` (exige árvore git limpa e a mesma branch).
Se a versão instalada não tiver teleport, abra `claude` na branch e peça para
ler este arquivo.

⚠️ **Windows:** se `make` não existir, os comandos abaixo trazem o equivalente
em Python puro — o `Makefile` é só a ordem.

## 2. Gate da Rota 1 — o passo que decide (≈1 h, quase tudo download)

```powershell
make fronteira VIZINHO=24
```
Sem `make`, na ordem:
```powershell
python scripts/data_prep/01_check_dose_variation.py --fonte sidra --ufs 23 24
python scripts/data_prep/02_clean_births.py --fonte ftp --ufs 23 24   # o espelho do pysus caiu (doc 15 §6)
python scripts/data_prep/15_censo_demografico.py --ufs 23 24 --verificar-dicionario
python scripts/data_prep/14_gate_fronteira.py --vizinho 24 `
  --pam data/processed/pam_ce_muni_cultura_media__sidra__uf23-24.parquet `
  --painel data/processed/nascimentos_ce_muni_mes__uf23-24.parquet
```

Ler `data/processed/gate_fronteira__uf23-24.csv`:

| G1 (aeronave no vizinho, Censo Agro 2006) | leitura | próximo |
|---|---|---|
| ✘ | o RN não tinha pulverização aérea a perder — confirma o SINDAG | repetir com `VIZINHO=22` (PI) e `26` (PE) |
| ✔ | a Rota 1 é viável no RN | G2 (melão) e G3 (registro) decidem o resto |
| ausente | tabela 1008 não respondeu | rodar `13_censo_agro_equipamento.py --uf 24` isolado e ver o erro |

⚠️ **Não montar painel nem estimar a fronteira** depois do gate: é mudança de
identificação, e passa pelo orientador (CLAUDE.md).

## 3. Resolver 17 × 19 no decil superior (15 min)

> ✅ **Resolvido na sessão remota** (`docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §1): 17 é o grupo dos
> estimadores, e 15 deles não tinham aplicação aérea; 19 é o quantil 0,9 sobre
> os 184. Arquivos corrigidos. Rodar o comando abaixo continua útil para
> confirmar com os artefatos — agora ele também conta o falso negativo no grupo
> de comparação.

Dizem **17**: `paper/secoes/05-dados.tex`, flag 0 do `CLAUDE.md`,
`docs/legislacao/README.md`, `docs/lacunas-de-dados.md`,
`docs/gates-resultados-dados-reais.md`. Dizem **19**: flag 7 do `CLAUDE.md`,
`scripts/data_prep/13_censo_agro_equipamento.py`,
`docs/legislacao/lai-semace-minuta.md`, o teste do script 12. Um dos dois está
errado (ou são cortes diferentes do decil), e o VPP depende disso (11,8% ×
10,5%).

```powershell
python scripts/estimate/12_erro_de_classificacao.py `
  --censo data/processed/censo_agro_equipamento_ce.csv `
  --dose data/processed/pam_ce_muni_cultura_media__sidra.parquet
```
Corrigir o número errado em todos os arquivos acima e em
`docs/auditoria-mensuracao-do-tratamento.md` — no mesmo commit.

## 3-bis. Texto integral da Lei 1.511/2010 de Limoeiro (5 min)

A revogadora da Lei 1.478/2009 foi identificada: a **Lei 1.511, de
26/05/2010**, de política ambiental. A revogação está num artigo do corpo.
Falta lê-la. Abrir o anexo em
`https://www.camaralimoeirodonorte.ce.gov.br/leis/581` e copiar o artigo
revogatório para o bloco RESOLVIDO de `docs/legislacao/README.md`. Depois,
trocar `secundaria` por `primaria` em `fonte_revogacao`, no registro e na
semente do script 08, e rodar os testes. Se o artigo não estiver lá, a flag 0
reabre.

## 3-ter. Parecer de 2026-09-22 — o que rodar (20 min)

> ✅ **Feito pela auditoria de 2026-09-23, no painel real** (doc 20 §1). O
> `nivel` deu −35,33 g com 15 controles e −36,19 g com 14: a premissa do doc 17
> §1 vale. O item 1 abaixo pedia −36,19 g, mas o script rodava com a definição
> 1; agora o `make real` passa `D_ZERO=4`. Os placebos do item 4 estavam
> contaminados pelo pós-ban (corrigido). Os nomes de saída mudaram: levam
> `__<desfecho>__d0-<def>`. O que rodar agora está no §3-sexies.

Resposta completa em `docs/ars/17-resposta-ao-feedback-2026-09-22.md`. O que
precisa de dado real:

```powershell
make real        # ou, só o que mudou:
python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet
python scripts/estimate/10_spt_pretrend.py --painel data/processed/painel_ensaio1.parquet --desfecho peso_medio
python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet `
  --estratos-aptidao 3 --out-dir data/processed/estratos3
```

Ler, nesta ordem:
1. `nivel` em `robustez_inferencia.csv` tem de dar ≈ −36,19 g, o agregado do
   contdid. Se não der, o doc 17 §1 parte de premissa errada: parar e avisar.
2. `nivel_jack_min`/`nivel_jack_max`: se um único controle move o nível para
   perto de zero, o −36 g é esse município.
3. `robustez_perfil_dose.csv`: os terços da dose positiva são planos entre si?
4. `nivel` nos cortes placebo (`spt_pretrend__peso_medio.csv`): quantos
   placebos têm nível do tamanho do real?
5. `ic_inv_baixo`/`ic_inv_alto`: substituem o [−46,45; +57,85] do paper.

Os números entram nos colchetes dos textos propostos do doc 17 §7.

## 3-quater. ARS, rodada 18 — o que só a máquina local faz (≈1 h 45)

A Fase 1 (`docs/ars/18-medida-e-desenho-fase1-escopo.md`) espera confirmação
para abrir a Fase 2. Três passos não dependem dela, e o proxy remoto bloqueia
os três:

1. **IN MAPA nº 2/2008** consolidada (gov.br, aviação agrícola, legislação):
   copiar os arts. 9º–14 e os Anexos I e V para `docs/legislacao/`. Depois,
   passar o checklist de `docs/legislacao/lai-mapa-relatorios-mensais-minuta.md`
   §3 e protocolar o Pedido D no Fala.BR. É o item com relógio mais longo.
2. **Relatórios de gestão da SFA-CE, 2010–2018** (gov.br, acesso à
   informação, prestação de contas): procurar "aviação agrícola". Se houver
   área aplicada por ano, é a série estadual que responde se a aviação cresceu
   depois de 2006.
3. **Calzada et al. (*JAERE*, 2023) inteiro**: de onde veio o calendário de
   fumigação e como definiram "período intensivo" (doc 18 §3.2).

## 3-quinquies. ARS, rodada 18, Fase 2 — o que decide as rotas (≈2 h)

> 🟡 **Estado em 2026-09-23** (doc 20 §§4 e 6). **Item 3 feito** pela auditoria,
> só no Ceará: MDE do calendário de 82,5 g, δ mínimo de 165 g com f = 0,5. A R3
> não tem poder. **Itens 1 e 2 em parte**: nenhuma decisão primária de 2011
> achada, e há indícios de aplicação em Limoeiro em 2018. Continuam valendo.
> **Item 4:** o Pedido D foi corrigido (art. 12, VI; art. 14, III) e espera
> protocolo.

A Fase 2 (`docs/ars/19-medida-e-desenho-fase2-investigacao.md`) terminou com uma
matriz de decisão e um nó: **a pulverização aérea continuou na Chapada depois de
2011?** Em ordem:

1. **Portal da Justiça Federal no Ceará:** a ação civil pública de julho de 2011
   (MPF, MPT, MP estadual × FAPIJA, Del Monte Fresh, Frutacor, Tropical
   Nordeste, Agrícola Famosa). Houve liminar? Sentença?
2. **A matéria da SEDH de 11/03/2011** (reproduzida pelo SINAIT em 15/03/2011):
   quem proibiu, por qual instrumento, com que alcance e por quanto tempo.
3. `make mde-calendario`, e `make mde-calendario PICO=3,4,5,6` como
   sensibilidade. Ler a coluna de δ mínimo contra os 38–89 g de Calzada et al.
4. O artigo da "informação prévia de atuação" na IN 2/2008 (item 6 do Pedido D)
   e o protocolo do Pedido D.

Se os passos 1 e 2 mostrarem que a pulverização parou em 2011, as rotas R2 a R5
perdem o grupo tratado, e a resposta do Ensaio 1 é a R8 (doc 19 §5).

## 3-sexies. Auditoria de 2026-09-23 — o que rodar agora (≈1 h)

A lista está em `docs/ars/20-resposta-a-auditoria-2026-09-23.md` §9:

1. `make real` com o código corrigido.
2. `make mde-desenhos` e `make mde-calendario`.
3. Ler, na ordem:
   - a banda com `ep_m0` da curva de nível (previsão: nenhum ponto exclui o zero);
   - o teste do piso;
   - os placebos corrigidos;
   - a família B de Holm;
   - o SDID e o HonestDiD com 2020–2022 como pós;
   - as linhas de 17×14 e 169×14 do `mde_desenhos.csv`.
4. Cinco minutos sobre os `.dbc` do SINASC: há campo de bairro ou localidade de
   residência preenchido para 230760 e 231150? Se houver, a fração exposta
   deixa de ser grade (doc 20 §6).

## 4. Crossref antes de qualquer `.bib` (30 min)

Procedimento de `docs/referencias-verificadas.md` §7 para: Calzada, Gisbert &
Moscoso (2023); Negi & Negi (2025); Sasaki & Wang (2024); Rull & Ritz (2003);
Borusyak, Hull & Jaravel (2022, 2025); Goldsmith-Pinkham, Sorkin & Swift
(2020); e as marcadas ⬜ na tabela do doc 17 §8 (Helfand 1991 primeiro: o
texto proposto para a §7.2 já a cita). Só depois entram no `.bib`.

## 5. Leituras que mudam o texto

- **Calzada et al. (2023) inteiro** — como mediram exposição, o calendário de
  fumigação, a magnitude por trimestre. Só o resumo foi lido.
- **Camacho & Mejía** — texto completo, pendência antiga.
- **Calendário de pulverização da banana no CE** — condição para a hipótese
  sazonal (§6 do doc 13). Sem ele, a hipótese não se escreve. Os relatórios
  mensais do Pedido D ao MAPA o dariam por município (doc 18 §3.2).

## 6. LAI — fora do Claude Code

- **ADAGRI (Pedido C):** checklist de `docs/legislacao/lai-adagri-minuta.md`
  §3 (art. 66 verbatim no Planalto; lei de criação da ADAGRI; objeto das
  Portarias 814/2022, 2/2024, 16/2025) → protocolar no Ceará Transparente.
- **SEMACE (Pedidos A/B):** `docs/legislacao/lai-semace-minuta.md`.
- **Prefeitura de Limoeiro do Norte (Pedido E, 🆕 2026-09-23):** avisos prévios
  de pulverização aérea exigidos pela Lei 1.511/2010 (art. 214) e pela Lei
  2.054/2018 (art. 153), 2010–2019: `docs/legislacao/lai-limoeiro-avisos-previos-minuta.md`
  → e-SIC municipal. É o único registro que dataria cada aplicação no principal
  tratado.
- **MAPA (Pedido D, 🆕 2026-09-23):** relatórios mensais de aviação agrícola
  com operação no Ceará, 2008–2024 (IN MAPA nº 2/2008, art. 14):
  `docs/legislacao/lai-mapa-relatorios-mensais-minuta.md` → Fala.BR. Pode ser
  o mais valioso dos quatro: é o registro da aplicação feita, não da receita
  nem do cadastro (doc 18 §3.1).

## 7. Para a reunião com o orientador (não decidir sozinho)

1. Parâmetro da fronteira: ATT sobre um grupo mal identificado × ITT de
   fronteira.
2. Adendo à proveniência do piso de 15 g via Calzada — **o valor não muda**.
3. Pré-especificar, para o próximo ciclo, a hipótese sazonal
   (dose × pós × 1º trimestre no pico) e a de cauda (eCIC).
4. Melão como subpergunta, condicionado ao G2.
5. As seis decisões que o parecer de 2026-09-22 abriu (doc 17 §5): estimando
   declarado, GAEZ como instrumento ou construção de controle, janela da dose,
   vintage até 2024, inferência do nível com 15 controles, e o enquadramento do
   Ensaio 2.

## 8. Opcional, baixa prioridade

- Fases 3–6 do ARS (`/ars-plan` etc.).
- Censo 2010 (pré-ban) no script 15.
- Fração de nascimentos expostos por setor censitário.
- Bucket R2 do healthbR: a listagem com a chave pública do autor foi negada
  pelo controle de permissões da sessão remota. Valor esperado baixo — o
  SINASC não está lá. Só se o pesquisador decidir.
