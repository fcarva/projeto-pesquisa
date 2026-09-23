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
python -m pytest tests/ -q           # esperado: 261 passed (3 exigem requirements-geo.txt)
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

## 4. Crossref antes de qualquer `.bib` (30 min)

Procedimento de `docs/referencias-verificadas.md` §7 para: Calzada, Gisbert &
Moscoso (2023); Negi & Negi (2025); Sasaki & Wang (2024); Rull & Ritz (2003);
Borusyak, Hull & Jaravel (2022, 2025); Goldsmith-Pinkham, Sorkin & Swift
(2020). Só depois entram no `.bib`.

## 5. Leituras que mudam o texto

- **Calzada et al. (2023) inteiro** — como mediram exposição, o calendário de
  fumigação, a magnitude por trimestre. Só o resumo foi lido.
- **Camacho & Mejía** — texto completo, pendência antiga.
- **Calendário de pulverização da banana no CE** — condição para a hipótese
  sazonal (§6 do doc 13). Sem ele, a hipótese não se escreve.

## 6. LAI — fora do Claude Code

- **ADAGRI (Pedido C):** checklist de `docs/legislacao/lai-adagri-minuta.md`
  §3 (art. 66 verbatim no Planalto; lei de criação da ADAGRI; objeto das
  Portarias 814/2022, 2/2024, 16/2025) → protocolar no Ceará Transparente.
- **SEMACE (Pedidos A/B):** `docs/legislacao/lai-semace-minuta.md`.

## 7. Para a reunião com o orientador (não decidir sozinho)

1. Parâmetro da fronteira: ATT sobre um grupo mal identificado × ITT de
   fronteira.
2. Adendo à proveniência do piso de 15 g via Calzada — **o valor não muda**.
3. Pré-especificar, para o próximo ciclo, a hipótese sazonal
   (dose × pós × 1º trimestre no pico) e a de cauda (eCIC).
4. Melão como subpergunta, condicionado ao G2.

## 8. Opcional, baixa prioridade

- Fases 3–6 do ARS (`/ars-plan` etc.).
- Censo 2010 (pré-ban) no script 15.
- Fração de nascimentos expostos por setor censitário.
- Bucket R2 do healthbR: a listagem com a chave pública do autor foi negada
  pelo controle de permissões da sessão remota. Valor esperado baixo — o
  SINASC não está lá. Só se o pesquisador decidir.
