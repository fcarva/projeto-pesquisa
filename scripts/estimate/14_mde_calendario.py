"""E18 — O poder do desenho de calendário: MDE do hiato sazonal contra o do nível.

POR QUE ESTE SCRIPT EXISTE
--------------------------

A Fase 1 da rodada 18 do ARS (`docs/ars/18-medida-e-desenho-fase1-escopo.md`
§4.1) mostrou que medir o tratamento pelo método corrige a atenuação, mas não
compra poder no corte transversal. Com os 7 municípios que tinham aplicação
aérea em 2006, o MDE entre municípios fica na ordem de 50 g. O análogo mais
próximo, Calzada et al., identifica pelo **calendário**: bebês cujo 1º
trimestre caiu nos meses de fumigação intensa (a estação chuvosa, quando ataca
a sigatoka). O checkpoint 1 pôs como condição da Fase 2 calcular o MDE desse
desenho. É o que este script faz.

O DESENHO
---------

Diferença tripla dentro do município: coortes de 1º trimestre **nos** meses de
pulverização contra coortes **fora** deles, em municípios com e sem aplicação
aérea, antes e depois do ban. O efeito que ela mede é o **hiato sazonal** que o
ban apagaria onde havia avião. A hipótese de identificação é uma só (Olden &
Møen 2022): sem o ban, o hiato sazonal teria evoluído igual nos dois grupos.

Por que pode ter mais poder que o nível: o hiato é uma diferença **dentro** do
município. Choques e tendências do município inteiro (τ² do script 13, a
heterogeneidade que infla o MDE entre municípios) se cancelam nele. O preço é
que cada lado do hiato usa só parte dos nascimentos.

E por que pode ter menos: se a pulverização for o ano inteiro, sem pico, o
hiato não tem sinal, e o desenho mede zero por construção. O desenho de
calendário **testa o mecanismo sazonal**; não substitui o nível quando esse
mecanismo falha.

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não estima efeito e não olha o pós-ban.** Usa só 2015–2018, dividido em
  metades (2015–16 × 2017–18), como o script 13: a variação placebo do hiato
  entre as metades é o ruído que o desenho precisa vencer.
- **Não escolhe o calendário.** `--meses-pico` é hipótese. O padrão (fevereiro
  a maio, a quadra chuvosa do Ceará) vem da analogia com Calzada et al. e não
  está confirmado para a banana cearense. O calendário certo sai dos
  relatórios mensais do MAPA (Pedido D, `docs/legislacao/`).
- **Não escolhe os tratados.** Padrão: os municípios com aplicação por
  aeronave no Censo Agro 2006 (a lista do script 13). `--tratados` troca a lista
  quando houver medida melhor.

A CONVENÇÃO DA GESTAÇÃO
-----------------------

A mesma do painel (`05_build_panel.py`): janela **fixa** de 9 meses, 1º
trimestre em (−9, −6) relativo ao mês de nascimento. Para a coorte nascida no
mês t, o 1º trimestre são os meses t−9, t−8 e t−7. A exposição da coorte é a
fração desses três meses que cai em `--meses-pico`. "Alta" é ≥ 2/3, "zero" é 0,
e as coortes de 1/3 ficam de fora do hiato. Usar a idade gestacional observada
seria condicionar em desfecho (prematuridade).

Uso:
    python scripts/estimate/14_mde_calendario.py \
        --painel data/processed/nascimentos_ce_muni_mes.parquet \
        --censo data/processed/censo_agro_equipamento_ce.csv
    python scripts/estimate/14_mde_calendario.py --meses-pico 3,4,5,6
    make mde-calendario

Saída (gitignored): `data/processed/mde_calendario.csv`.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"

ANOS_PRE = (2015, 2016, 2017, 2018)
MESES_PICO_PADRAO = (2, 3, 4, 5)       # quadra chuvosa: HIPÓTESE, ver docstring
TRI1_MESES_ANTES = (9, 8, 7)           # 1º trimestre em (−9, −6), como o painel
LIMIAR_ALTA = 2 / 3


def _carrega_script(nome: str, sub: str):
    caminho = RAIZ / "scripts" / sub / nome
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


_mde = _carrega_script("13_mde_desenhos.py", "estimate")
Z_PODER = _mde.Z_PODER
FRACOES_EXPOSTAS = _mde.FRACOES_EXPOSTAS
mde_agrupado = _mde.mde_agrupado
mde_por_unidade = _mde.mde_por_unidade
variacao_placebo = _mde.variacao_placebo
variancia_individual = _mde.variancia_individual
heterogeneidade = _mde.heterogeneidade
com_aeronave = _mde.com_aeronave
_saida_utf8 = _mde._saida_utf8


# --------------------------------------------------------------------------
# Exposição da coorte pelo calendário
# --------------------------------------------------------------------------

def exposicao_tri1(mes_nascimento, meses_pico=MESES_PICO_PADRAO) -> np.ndarray:
    """Fração do 1º trimestre (meses t−9, t−8, t−7) que cai nos meses de pico.

    Só depende do mês do calendário, então vale para qualquer ano.
    """
    m = np.asarray(mes_nascimento, int)
    pico = set(int(x) for x in meses_pico)
    dentro = [np.isin(((m - 1 - k) % 12) + 1, list(pico)) for k in TRI1_MESES_ANTES]
    return np.mean(dentro, axis=0)


def classifica_coortes(mes_nascimento, meses_pico=MESES_PICO_PADRAO) -> np.ndarray:
    """'alta' (≥ 2/3 do 1º trimestre no pico), 'zero' (nada) ou 'parcial'."""
    e = exposicao_tri1(mes_nascimento, meses_pico)
    return np.where(e >= LIMIAR_ALTA - 1e-9, "alta", np.where(e <= 1e-9, "zero", "parcial"))


# --------------------------------------------------------------------------
# O hiato sazonal e sua variação placebo
# --------------------------------------------------------------------------

def variacao_hiato(painel: pd.DataFrame, meses_pico=MESES_PICO_PADRAO,
                   anos_pre=ANOS_PRE) -> pd.DataFrame:
    """Por município: o hiato (alta − zero) em cada metade do pré e a variação.

    Médias ponderadas por `n_peso_valido`. Município sem nascimento válido em
    alguma das quatro caselas (alta/zero × ini/fim) sai: não tem hiato.
    """
    p = _mde._celulas_pre(painel, anos_pre)
    p["coorte"] = classifica_coortes(p["mes"], meses_pico)
    p = p[p["coorte"] != "parcial"]
    p["soma"] = p["peso_medio"] * p["n_peso_valido"]
    g = (p.groupby(["cod_ibge6", "meio", "coorte"])
          .agg(soma=("soma", "sum"), n=("n_peso_valido", "sum"))
          .unstack(["meio", "coorte"]))
    casas = [(m, c) for m in ("ini", "fim") for c in ("alta", "zero")]
    for m, c in casas:
        if ("n", m, c) not in g.columns:
            raise ValueError(f"o pré-período não tem coortes '{c}' na metade '{m}'")
    saida = pd.DataFrame(index=g.index)
    for m, c in casas:
        saida[f"n_{c}_{m}"] = g[("n", m, c)]
        saida[f"media_{c}_{m}"] = g[("soma", m, c)] / g[("n", m, c)]
    saida = saida.replace([np.inf, -np.inf], np.nan).dropna()
    saida = saida[(saida[[f"n_{c}_{m}" for m, c in casas]] > 0).all(axis=1)]
    saida["hiato_ini"] = saida["media_alta_ini"] - saida["media_zero_ini"]
    saida["hiato_fim"] = saida["media_alta_fim"] - saida["media_zero_fim"]
    saida["delta_hiato"] = saida["hiato_fim"] - saida["hiato_ini"]
    return saida


def heterogeneidade_hiato(variacao: pd.DataFrame, sigma2: float) -> float:
    """τ² do hiato: o que sobra da variância depois do ruído das quatro caselas."""
    return max(float(variacao["delta_hiato"].var(ddof=1)) - float(ruido_hiato(variacao, sigma2).mean()), 0.0)


def ruido_hiato(variacao: pd.DataFrame, sigma2: float) -> pd.Series:
    """Variância amostral de Δ-hiato por município: quatro médias, cada uma com σ²/n."""
    return sigma2 * (1 / variacao["n_alta_ini"] + 1 / variacao["n_zero_ini"]
                     + 1 / variacao["n_alta_fim"] + 1 / variacao["n_zero_fim"])


def fracao_alta(painel: pd.DataFrame, meses_pico=MESES_PICO_PADRAO,
                anos_pre=ANOS_PRE) -> float:
    """Fração dos nascimentos do pré-período em coortes de exposição alta."""
    p = _mde._celulas_pre(painel, anos_pre)
    alta = classifica_coortes(p["mes"], meses_pico) == "alta"
    total = float(p["n_peso_valido"].sum())
    return float(p.loc[alta, "n_peso_valido"].sum()) / total if total > 0 else float("nan")


# --------------------------------------------------------------------------
# Os dois desenhos para os mesmos tratados
# --------------------------------------------------------------------------

def compara(painel: pd.DataFrame, tratados, meses_pico=MESES_PICO_PADRAO,
            anos_pre=ANOS_PRE) -> pd.DataFrame:
    """MDE do nível e do calendário, agrupado e por unidade, e o efeito
    individual que cada um exige por fração de nascimentos expostos."""
    tratados = {str(t) for t in tratados}
    sigma2 = variancia_individual(painel, anos_pre)

    niv = variacao_placebo(painel, anos_pre)
    tau2_niv = heterogeneidade(niv, sigma2)
    v_niv = sigma2 * (1 / niv["n_ini"] + 1 / niv["n_fim"]) + tau2_niv

    cal = variacao_hiato(painel, meses_pico, anos_pre)
    tau2_cal = heterogeneidade_hiato(cal, sigma2)
    v_cal = ruido_hiato(cal, sigma2) + tau2_cal

    s = fracao_alta(painel, meses_pico, anos_pre)
    linhas = []
    for desenho, var_df, col, v, tau2 in (
        ("nivel", niv, "delta", v_niv, tau2_niv),
        ("calendario", cal, "delta_hiato", v_cal, tau2_cal),
    ):
        t = var_df.index.isin(tratados)
        g1, g0 = int(t.sum()), int((~t).sum())
        ausentes = sorted(tratados - set(var_df.index))
        agr = mde_agrupado(float(var_df[col].std(ddof=1)), g1, g0)
        uni = mde_por_unidade(v[t], v[~t])
        # O que o desenho mede, em termos do efeito individual δ sobre o bebê
        # exposto no pico, com fração f dos nascimentos do município exposta:
        #   nível: f · s · δ (só as coortes de pico são afetadas, sob a hipótese
        #          sazonal; s = fração de nascimentos nessas coortes)
        #   calendário: f · δ (o hiato é entre coortes de pico e fora dele)
        escala = s if desenho == "nivel" else 1.0
        linha = {"desenho": desenho, "g1": g1, "g0": g0,
                 "tratados_ausentes": ";".join(ausentes),
                 "mde_agrupado_g": agr, "mde_por_unidade_g": uni,
                 "tau_g": math.sqrt(tau2), "fracao_nasc_pico": s,
                 "meses_pico": ",".join(str(m) for m in meses_pico)}
        for f in FRACOES_EXPOSTAS:
            linha[f"delta_minimo_f{int(f * 100):02d}_g"] = (
                uni / (f * escala) if np.isfinite(uni) and f * escala > 0 else float("nan"))
        linhas.append(linha)
    return pd.DataFrame(linhas).assign(sigma_individual_g=math.sqrt(sigma2))


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime(res: pd.DataFrame, tratados) -> None:
    barra = "=" * 88
    print(barra)
    print("E18 — MDE DO DESENHO DE CALENDÁRIO CONTRA O DO NÍVEL (só pré-período)")
    print(barra)
    print(f"tratados: {len(set(tratados))} | meses de pico (HIPÓTESE): {res['meses_pico'].iloc[0]} "
          f"| nascimentos em coortes de pico: {res['fracao_nasc_pico'].iloc[0]:.1%}")
    print(f"σ individual: {res['sigma_individual_g'].iloc[0]:.0f} g")
    print("-" * 88)
    cab = "  {:<11} {:>4} {:>5} {:>11} {:>12} {:>7}   δ mínimo p/ f = " + \
          " / ".join(f"{int(f * 100)}%" for f in FRACOES_EXPOSTAS)
    print(cab.format("desenho", "g1", "g0", "agrupado", "por unidade", "τ"))
    for _, r in res.iterrows():
        deltas = " / ".join(f"{r[f'delta_minimo_f{int(f * 100):02d}_g']:.0f}"
                            for f in FRACOES_EXPOSTAS)
        print(f"  {r['desenho']:<11} {r['g1']:>4} {r['g0']:>5} {r['mde_agrupado_g']:>9.1f} g "
              f"{r['mde_por_unidade_g']:>10.1f} g {r['tau_g']:>5.1f}   {deltas} g")
        if r["tratados_ausentes"]:
            print(f"    ⚠️ tratados sem dado suficiente: {r['tratados_ausentes']}")
    print("-" * 88)
    print("COMO LER")
    print("  • MDE: o menor efeito sobre a média do grupo que o desenho detecta com")
    print("    80% de poder. O do nível é sobre todos os nascimentos; o do calendário,")
    print("    sobre o hiato entre coortes de pico e fora dele.")
    print("  • δ mínimo: o efeito sobre o bebê exposto no pico que o desenho precisa")
    print("    para ter 80% de poder, dada a fração f exposta. É a coluna comparável")
    print("    entre os dois desenhos, e o que se põe contra os 80–150 g de Calzada et al.")
    print("  • Sob a hipótese sazonal. Se a pulverização não tiver pico, o calendário")
    print("    não tem sinal e o δ mínimo dele não se aplica.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--painel", type=Path,
                   default=OUT_DIR / "nascimentos_ce_muni_mes.parquet")
    p.add_argument("--censo", type=Path,
                   default=OUT_DIR / "censo_agro_equipamento_ce.csv")
    p.add_argument("--tratados", default=None,
                   help="códigos IBGE6 separados por vírgula; substitui o Censo 2006")
    p.add_argument("--meses-pico", default=",".join(map(str, MESES_PICO_PADRAO)),
                   help="meses do calendário com pulverização intensa (HIPÓTESE)")
    p.add_argument("--ufs", default="23",
                   help="UFs do universo de controles e da calibração, separadas por "
                        "vírgula. Padrão: só o Ceará, porque o desenho é intraestadual.")
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if not args.painel.exists():
        print(f"[erro] {args.painel} não existe. Rode antes o script 02 (SINASC).")
        return 1
    painel = pd.read_parquet(args.painel)
    painel["cod_ibge6"] = painel["cod_ibge6"].astype(str)
    # ⚠️ O universo é explícito (auditoria de 2026-09-23). O mde_calendario.csv
    # salvo tinha 7 tratados contra 344 controles porque o painel era o CE+RN:
    # o RN entrava como controle e calibrava a variância de um desenho que é do
    # Ceará. Controle de outra UF é outro desenho, e só entra se pedido.
    ufs = tuple(u.strip() for u in args.ufs.split(",") if u.strip())
    fora = sorted(set(painel["cod_ibge6"].str[:2]) - set(ufs))
    if fora:
        print(f"  universo restrito às UFs {', '.join(ufs)}; fora do cálculo: {', '.join(fora)}")
    painel = painel[painel["cod_ibge6"].str[:2].isin(ufs)]
    if painel.empty:
        print(f"[erro] nenhum município das UFs {ufs} no painel.")
        return 1

    if args.tratados:
        tratados = {c.strip() for c in args.tratados.split(",") if c.strip()}
        origem = "lista passada em --tratados"
    elif args.censo.exists():
        censo = pd.read_csv(args.censo, dtype={"cod_ibge6": str, "cod_ibge7": str})
        tratados = com_aeronave(censo)
        origem = f"Censo Agro 2006 ({args.censo.name})"
    else:
        print(f"[erro] sem tratados: {args.censo} não existe e --tratados não foi passado.")
        return 1
    try:
        meses_pico = tuple(int(m) for m in args.meses_pico.split(",") if m.strip())
    except ValueError:
        print(f"[erro] --meses-pico inválido: {args.meses_pico!r}")
        return 1
    if not meses_pico or any(m < 1 or m > 12 for m in meses_pico):
        print(f"[erro] --meses-pico fora de 1..12: {args.meses_pico!r}")
        return 1

    print(f"tratados de: {origem}")
    res = compara(painel, tratados, meses_pico)
    imprime(res, tratados)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "mde_calendario.csv"
    res.assign(origem_tratados=origem, painel=args.painel.name, universo="+".join(ufs),
               extraido_em=date.today().isoformat()).to_csv(destino, index=False,
                                                            encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
