"""E17 — O poder que cada grupo tratado compra: MDE dos desenhos candidatos.

POR QUE ESTE SCRIPT EXISTE
--------------------------

A calibração do script 12 mostrou que a alavanca do Ensaio 1 é o **VPP**, não o
N: no decil de 17 só 2 municípios tinham aplicação aérea, e o sinal esperado ali
não passa de ~9 g contra um MDE de 33,4 g. As saídas que sobem o VPP —
concentrar o grupo tratado onde havia avião (Rota 1, Chapada) ou tratar pelo
método (Rota 3) — fazem o grupo tratado **encolher**. Fica a pergunta que este
script responde: **quanto poder um grupo de 1, 2 ou 7 municípios compra?**

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não estima efeito nenhum e não olha o pós-ban.** Usa só 2015–2018, como o
  cálculo que deu os 33,4 g. Um MDE calculado com dado pós-ban deixaria de ser
  conta de desenho.
- **Não escolhe desenho.** Trocar o grupo de comparação é mudança de
  identificação e passa pelo orientador (`CLAUDE.md`). O script mede o preço de
  cada opção; a decisão não é dele.

MÉTODO — o mesmo do MDE de 33,4 g, mais uma conta que importa com poucos tratados
--------------------------------------------------------------------------------

**Variação placebo por município:** peso médio de 2017–2018 menos o de
2015–2016. No pré-período não há tratamento, então a dispersão dessa variação é
o ruído que o desenho precisa vencer.

Duas contas de MDE, lado a lado:

- **agrupado** — **réplica exata** da conta do script 01, a que deu os 33,4 g:
  `2,8 × DP(variações) × √(1/g₁ + 1/g₀)`, com a variação feita, como lá, de
  **médias simples das médias mensais**. Dá o mesmo peso a todo município e a
  todo mês. Existe para o benchmark bater; não é a melhor conta.
- **por unidade** — médias ponderadas pelos nascimentos com peso válido, e
  cada município entra com a variância que tem:
  `vᵢ = σ²·(1/Nᵢ,ini + 1/Nᵢ,fim) + τ²`, e
  `MDE = 2,8 × √(Σ_T vᵢ/g₁² + Σ_C vⱼ/g₀²)`.
  σ² é a variância individual do peso, estimada da variação mês a mês dentro de
  cada município e meio-período. A sazonalidade entra junto e a infla, então o
  erro é para o lado conservador. τ² é a heterogeneidade real das tendências,
  `Var(Δ) − média do ruído amostral` (o método do script 07).

Com dois tratados, as duas contas divergem, e é essa divergência que importa. A
agrupada pune Limoeiro pelo ruído dos municípios minúsculos e, ao mesmo tempo,
esquece que dois clusters não têm média nenhuma para diluir a heterogeneidade
própria deles. A por unidade faz as duas contas certas.

⚠️ É a aproximação normal. Com 1 ou 2 tratados a inferência do paper seria
Conley–Taber, com a distribuição tirada dos controles. O MDE daqui dá a **ordem
de grandeza**, não o valor crítico.

OS DESENHOS
-----------

| desenho | tratados | controles | VPP (Censo 2006) |
|---|---|---|---|
| `decil17_vs_ce_outros` | decil canônico da banana (17) | os outros municípios do CE | 2/17 — é o benchmark dos 33,4 g |
| `decil17_vs_ce_dose_zero` | idem | CE de dose zero — o grupo dos scripts 07/08 | 2/17 |
| `chapada2_vs_ride_rn` | Limoeiro + Quixeré | RIDE da Chapada, lado potiguar (21) | ~1 |
| `chapada2_vs_rn` | Limoeiro + Quixeré | todo o RN | ~1 |
| `quixere_vs_ride_rn` | só Quixeré | RIDE potiguar | ~1 — para o caso de a revogação de Limoeiro não se confirmar |
| `aeronave_ce_vs_ce_sem` | os 7 do CE com aplicação aérea | CE sem aplicação aérea | ~1 — a Rota 3 dentro do estado |

Os códigos de Limoeiro e Quixeré vêm do Censo Agro 2006 (script 13) e a RIDE
potiguar do script 15; os decis saem do PAM. Nada disso escolhe a
cultura-âncora: `--cultura` continua parâmetro.

Uso:
    python scripts/estimate/13_mde_desenhos.py \
        --painel data/processed/nascimentos_ce_muni_mes__uf23-24.parquet
    make mde-desenhos                     # VIZINHO=24

Saída (gitignored): `data/processed/mde_desenhos.csv`.
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
Z_PODER = 2.8          # 1,96 + 0,84: 80% de poder, 5% bilateral — igual ao script 01
FRACAO_DECIL = 0.10

# Chapada do Apodi, lado cearense: os dois municípios do decil da banana com
# aplicação por aeronave no Censo Agro 2006 (Limoeiro 18 estabelecimentos,
# Quixeré 9). A lei de Limoeiro de 2009 foi revogada em 2010 — ver
# docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md §5.
TRATADOS_CHAPADA = ("230760", "231150")
SO_QUIXERE = ("231150",)

# Calibração do script 12 (Calzada et al. 2023, pelo resumo): efeito individual
# sob exposição alta, e a fração exposta como grade.
EFEITOS_INDIVIDUAIS_G = (80.0, 150.0)
FRACOES_EXPOSTAS = (0.10, 0.25, 0.50)


def _carrega_script(nome: str, sub: str):
    caminho = RAIZ / "scripts" / sub / nome
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _saida_utf8() -> None:
    """Mesmo guarda dos outros scripts: no Windows a saída usa cp1252 e morre
    em ⚠️ depois de o trabalho estar feito."""
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


# --------------------------------------------------------------------------
# O ruído do pré-período
# --------------------------------------------------------------------------

def _celulas_pre(painel: pd.DataFrame, anos_pre=ANOS_PRE) -> pd.DataFrame:
    """Células município × mês do pré-período com peso válido, marcadas por meio."""
    p = painel[painel["ano"].isin(anos_pre)].copy()
    p = p[(p["n_peso_valido"] > 0) & p["peso_medio"].notna()]
    metade = min(anos_pre) + (max(anos_pre) - min(anos_pre)) // 2
    p["meio"] = np.where(p["ano"] <= metade, "ini", "fim")
    p["cod_ibge6"] = p["cod_ibge6"].astype(str)
    return p


def variacao_placebo(painel: pd.DataFrame, anos_pre=ANOS_PRE) -> pd.DataFrame:
    """Por município: nascimentos e peso médio em cada meio, e a variação Δ.

    Duas variações, para as duas contas: `delta`, de médias ponderadas por
    `n_peso_valido` (a média do meio-período é a de todos os bebês dele), para
    o MDE por unidade; e `delta_script01`, de médias simples das médias
    mensais, que é a conta do script 01 e só serve ao benchmark. Município sem
    nascimento válido em um dos meios sai: não tem Δ.
    """
    p = _celulas_pre(painel, anos_pre)
    p["soma"] = p["peso_medio"] * p["n_peso_valido"]
    g = (p.groupby(["cod_ibge6", "meio"])
          .agg(soma=("soma", "sum"), n=("n_peso_valido", "sum"),
               simples=("peso_medio", "mean"))
          .unstack("meio"))
    if ("n", "ini") not in g.columns or ("n", "fim") not in g.columns:
        raise ValueError(f"o painel não cobre as duas metades de {anos_pre}")
    saida = pd.DataFrame({
        "n_ini": g[("n", "ini")],
        "n_fim": g[("n", "fim")],
        "media_ini": g[("soma", "ini")] / g[("n", "ini")],
        "media_fim": g[("soma", "fim")] / g[("n", "fim")],
        # A conta do script 01: média simples das médias mensais. Só serve à
        # coluna agrupada, para o benchmark dos 33,4 g bater.
        "delta_script01": g[("simples", "fim")] - g[("simples", "ini")],
    }).dropna()
    saida["delta"] = saida["media_fim"] - saida["media_ini"]
    return saida


def variancia_individual(painel: pd.DataFrame, anos_pre=ANOS_PRE) -> float:
    """σ² do peso individual, pela variação mês a mês dentro do município.

    Com `m_c` a média da célula e `n_c` os bebês dela, `Σ n_c (m_c − m̄)²`
    dentro de cada município × meio tem esperança `(C − 1)·σ²` se as células
    só diferem por amostragem. A sazonalidade soma variância real e infla σ² —
    o erro vai para o lado de um MDE maior, que é o lado certo de errar.
    """
    p = _celulas_pre(painel, anos_pre)
    chave = ["cod_ibge6", "meio"]
    p["soma"] = p["peso_medio"] * p["n_peso_valido"]
    media = (p.groupby(chave)["soma"].transform("sum")
             / p.groupby(chave)["n_peso_valido"].transform("sum"))
    ss = float((p["n_peso_valido"] * (p["peso_medio"] - media) ** 2).sum())
    gl = int((p.groupby(chave).size() - 1).sum())
    if gl <= 0:
        raise ValueError("pré-período sem células suficientes para estimar σ²")
    return ss / gl


def heterogeneidade(variacao: pd.DataFrame, sigma2: float) -> float:
    """τ²: a variância das tendências que sobra depois do ruído amostral."""
    ruido = sigma2 * (1 / variacao["n_ini"] + 1 / variacao["n_fim"])
    return max(float(variacao["delta"].var(ddof=1)) - float(ruido.mean()), 0.0)


# --------------------------------------------------------------------------
# As duas contas de MDE
# --------------------------------------------------------------------------

def mde_agrupado(sd_g: float, g1: int, g0: int, z: float = Z_PODER) -> float:
    """A conta do script 01 — a que deu os 33,4 g."""
    if g1 <= 0 or g0 <= 0 or not np.isfinite(sd_g):
        return float("nan")
    return z * sd_g * math.sqrt(1 / g1 + 1 / g0)


def mde_por_unidade(v_tratados, v_controles, z: float = Z_PODER) -> float:
    """Cada município com a própria variância: Var(Δ̄_T − Δ̄_C)."""
    v_t, v_c = np.asarray(v_tratados, float), np.asarray(v_controles, float)
    if v_t.size == 0 or v_c.size == 0:
        return float("nan")
    return z * math.sqrt(v_t.sum() / v_t.size ** 2 + v_c.sum() / v_c.size ** 2)


def poder(theta: float, mde: float, z_alfa: float = 1.959964) -> float:
    """Poder bilateral contra um efeito `theta`, dado o MDE (80% por construção)."""
    from statistics import NormalDist
    if not np.isfinite(mde) or mde <= 0:
        return float("nan")
    ep = mde / Z_PODER
    t = abs(theta) / ep
    return NormalDist().cdf(t - z_alfa) + NormalDist().cdf(-t - z_alfa)


# --------------------------------------------------------------------------
# Os grupos
# --------------------------------------------------------------------------

def decil_superior(pam: pd.DataFrame, cultura: str,
                   fracao: float = FRACAO_DECIL) -> set[str]:
    """Decil canônico: `ceil(10%)` dos produtores, por área — o dos scripts 07/08."""
    col = "area_ha_media" if "area_ha_media" in pam.columns else "area_ha"
    bloco = pam[pam["cultura"].str.contains(cultura, case=False, na=False)].copy()
    bloco["cod_ibge6"] = _cod6(bloco)
    positivos = bloco[bloco[col] > 0]
    if positivos.empty:
        raise ValueError(f"nenhum município com área positiva de {cultura!r}")
    k = max(1, math.ceil(positivos["cod_ibge6"].nunique() * fracao))
    return set(positivos.nlargest(k, col)["cod_ibge6"])


def dose_zero(pam: pd.DataFrame, cultura: str, universo: set[str]) -> set[str]:
    """Municípios do universo SEM área da cultura — o grupo de comparação 07/08."""
    col = "area_ha_media" if "area_ha_media" in pam.columns else "area_ha"
    bloco = pam[pam["cultura"].str.contains(cultura, case=False, na=False)].copy()
    bloco["cod_ibge6"] = _cod6(bloco)
    positivos = set(bloco.loc[bloco[col] > 0, "cod_ibge6"])
    return universo - positivos


def _cod6(df: pd.DataFrame) -> pd.Series:
    if "cod_ibge6" in df.columns:
        return df["cod_ibge6"].astype(str).str[:6]
    return df["cod_ibge"].astype(str).str[:6]


def com_aeronave(censo: pd.DataFrame) -> set[str]:
    """Municípios com algum estabelecimento que aplicou por aeronave (2006)."""
    return set(_cod6(censo.loc[censo["aeronave"] > 0]))


def ride_chapada_rn() -> set[str]:
    """A RIDE da Chapada, lado potiguar — delimitação externa, do script 15."""
    censo15 = _carrega_script("15_censo_demografico.py", "data_prep")
    return {str(c)[:6] for c in censo15.RIDE_CHAPADA_RN}


# --------------------------------------------------------------------------
# Um desenho
# --------------------------------------------------------------------------

def avalia_desenho(nome: str, tratados, controles, variacao: pd.DataFrame,
                   sigma2: float, tau2: float, vpp: float, nota: str = "") -> dict:
    """MDE agrupado e por unidade, e o poder contra o sinal calibrado.

    ⚠️ Tratado sem dado no pré-período torna o desenho `ausente`, não menor:
    calcular o MDE de um desenho sem uma das suas unidades tratadas daria
    número para um desenho que não é o proposto. É a mesma classe de erro do
    painel de fronteira que só tinha o Ceará (doc 15 §4.1).
    """
    tratados, controles = set(tratados), set(controles) - set(tratados)
    base = {"desenho": nome, "nota": nota, "vpp": vpp,
            "g1_pedido": len(tratados), "g0_pedido": len(controles)}
    faltam_t = sorted(tratados - set(variacao.index))
    if not tratados or faltam_t:
        return {**base, "veredito": "ausente",
                "motivo": f"tratados sem pré-período no painel: {faltam_t or 'nenhum pedido'}"}
    ctrl = sorted(controles & set(variacao.index))
    if len(ctrl) < 2:
        return {**base, "veredito": "ausente",
                "motivo": f"só {len(ctrl)} controles com pré-período no painel"}

    t = variacao.loc[sorted(tratados)]
    c = variacao.loc[ctrl]
    v = lambda d: sigma2 * (1 / d["n_ini"] + 1 / d["n_fim"]) + tau2
    sd_desenho = float(pd.concat([t["delta_script01"], c["delta_script01"]]).std(ddof=1))
    agrupado = mde_agrupado(sd_desenho, len(t), len(c))
    unidade = mde_por_unidade(v(t), v(c))
    linha = {
        **base, "veredito": "calculado", "motivo": "",
        "g1": len(t), "g0": len(c),
        "nascimentos_ano_tratados": float((t["n_ini"] + t["n_fim"]).sum()
                                          / len(ANOS_PRE)),
        "sd_placebo_g": sd_desenho,
        "mde_agrupado_g": agrupado,
        "mde_por_unidade_g": unidade,
    }
    for f in FRACOES_EXPOSTAS:
        for d in EFEITOS_INDIVIDUAIS_G:
            theta = vpp * f * d
            linha[f"theta_f{f:.2f}_d{d:.0f}"] = theta
            linha[f"poder_f{f:.2f}_d{d:.0f}"] = poder(theta, unidade)
    return linha


def desenhos_padrao(variacao: pd.DataFrame, pam: pd.DataFrame | None,
                    censo: pd.DataFrame | None, cultura: str) -> list[dict]:
    """Os seis desenhos da tabela do docstring, cada um com o que tiver de insumo."""
    ce = {c for c in variacao.index if c.startswith("23")}
    rn = {c for c in variacao.index if c.startswith("24")}
    especs = []
    if pam is not None:
        decil = decil_superior(pam, cultura)
        vpp_decil = (len(decil & com_aeronave(censo)) / len(decil)
                     if censo is not None else 2 / 17)
        especs += [
            ("decil17_vs_ce_outros", decil, ce - decil, vpp_decil,
             "benchmark: a conta que deu os 33,4 g"),
            ("decil17_vs_ce_dose_zero", decil, dose_zero(pam, cultura, ce),
             vpp_decil, "o grupo de comparação dos scripts 07/08 (sem o corte GAEZ)"),
        ]
    ride = ride_chapada_rn()
    especs += [
        ("chapada2_vs_ride_rn", set(TRATADOS_CHAPADA), ride, 1.0,
         "Rota 1 concentrada: os dois da divisa contra a RIDE potiguar"),
        ("chapada2_vs_rn", set(TRATADOS_CHAPADA), rn, 1.0,
         "idem, contra todo o RN"),
        ("quixere_vs_ride_rn", set(SO_QUIXERE), ride, 1.0,
         "se a revogação de Limoeiro (2010) não se confirmar"),
    ]
    if censo is not None:
        # Do Censo, NÃO do painel: um município com aeronave e sem nascimento
        # no painel tem de tornar o desenho `ausente`, não sumir dele.
        aero = {c for c in com_aeronave(censo) if c.startswith("23")}
        especs.append(("aeronave_ce_vs_ce_sem", aero, ce - aero, 1.0,
                       "Rota 3 no estado: tratado pelo método, não pela cultura"))
    return especs


def imprime(resultados: pd.DataFrame, sigma2: float, tau2: float,
            n_unidades: int) -> None:
    barra = "=" * 96
    print(barra)
    print("MDE DOS DESENHOS CANDIDATOS — só pré-período "
          f"({min(ANOS_PRE)}–{max(ANOS_PRE)}), nada estimado")
    print(barra)
    print(f"  σ individual (mês a mês, conservador): {math.sqrt(sigma2):6.0f} g   "
          f"τ (heterogeneidade real): {math.sqrt(tau2):5.1f} g   "
          f"({n_unidades} municípios)")
    print()
    print(f"  {'desenho':<26} {'g1':>3} {'g0':>4} {'nasc/ano T':>10} "
          f"{'MDE agr.':>9} {'MDE unid.':>10} {'poder f.25':>11} {'poder f.50':>11}")
    print(f"  {'':<26} {'':>3} {'':>4} {'':>10} {'':>9} {'':>10} "
          f"{'δ 80–150':>11} {'δ 80–150':>11}")
    for _, r in resultados.iterrows():
        if r["veredito"] != "calculado":
            print(f"  {r['desenho']:<26} ausente — {r['motivo']}")
            continue
        p25 = f"{r['poder_f0.25_d80']:.0%}–{r['poder_f0.25_d150']:.0%}"
        p50 = f"{r['poder_f0.50_d80']:.0%}–{r['poder_f0.50_d150']:.0%}"
        print(f"  {r['desenho']:<26} {r['g1']:>3.0f} {r['g0']:>4.0f} "
              f"{r['nascimentos_ano_tratados']:>10.0f} {r['mde_agrupado_g']:>8.1f}g "
              f"{r['mde_por_unidade_g']:>9.1f}g {p25:>11} {p50:>11}")
    print()
    print("  poder = contra θ = VPP · f · δ, com o MDE por unidade (aprox. normal).")
    print("  ⚠️ Com 1–2 tratados a inferência seria Conley–Taber: isto é ordem de")
    print("     grandeza, não valor crítico. E nada aqui é resultado do ban.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--painel", type=Path,
                   default=OUT_DIR / "nascimentos_ce_muni_mes__uf23-24.parquet",
                   help="Painel de nascimentos município × mês com CE E o vizinho.")
    p.add_argument("--pam", type=Path,
                   default=OUT_DIR / "pam_ce_muni_cultura_media__sidra.parquet")
    p.add_argument("--censo", type=Path,
                   default=OUT_DIR / "censo_agro_equipamento_ce.csv")
    p.add_argument("--cultura", default="banana",
                   help="Cultura do decil de benchmark (padrão: banana).")
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if not args.painel.exists():
        print(f"[erro] {args.painel} não existe. Rode antes o `make fronteira` "
              "(scripts 01 e 02 com --ufs 23 24).")
        return 1
    painel = pd.read_parquet(args.painel)
    painel["cod_ibge6"] = painel["cod_ibge6"].astype(str)
    ufs = sorted(painel["cod_ibge6"].str[:2].unique())
    if "24" not in ufs:
        # ⚠️ A lição do doc 15 §4.1: painel rotulado de fronteira com uma UF só.
        # Os desenhos com controle potiguar sairiam `ausente` um a um, mas o
        # aviso tem de vir antes, e alto.
        print(f"  ⚠️ o painel só tem as UFs {ufs}: os desenhos com o RN saem ausentes.")

    pam = pd.read_parquet(args.pam) if args.pam.exists() else None
    censo = (pd.read_csv(args.censo, dtype={"cod_ibge6": str, "cod_ibge7": str})
             if args.censo.exists() else None)
    if pam is None:
        print(f"  ⚠️ {args.pam} ausente: sem o benchmark do decil.")
    if censo is None:
        print(f"  ⚠️ {args.censo} ausente: sem o desenho da Rota 3 e com VPP do decil = 2/17.")

    variacao = variacao_placebo(painel)
    sigma2 = variancia_individual(painel)
    tau2 = heterogeneidade(variacao, sigma2)

    linhas = [avalia_desenho(nome, t, c, variacao, sigma2, tau2, vpp, nota)
              for nome, t, c, vpp, nota in desenhos_padrao(variacao, pam, censo,
                                                            args.cultura)]
    resultados = pd.DataFrame(linhas)
    imprime(resultados, sigma2, tau2, len(variacao))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "mde_desenhos.csv"
    resultados.assign(sigma_individual_g=math.sqrt(sigma2), tau_g=math.sqrt(tau2),
                      painel=args.painel.name, extraido_em=date.today().isoformat()
                      ).to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
