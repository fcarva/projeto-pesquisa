"""E15 — A dose classifica bem? Sensibilidade, especificidade, VPP e o limite.

POR QUE ESTE SCRIPT EXISTE
--------------------------

A flag 7 do `CLAUDE.md` diz que a dose por área plantada atribui tratamento alto
a municípios sem pulverização aérea, e que isso atenua o ATT por construção. Até
aqui isso era **afirmação qualitativa** com duas ilustrações (17 de 19 sem
aeronave; 27 das 36 aeronaves no decil).

Este script transforma a afirmação em **três métricas padrão** e em **um limite
reportável**. Nenhuma delas exige dado novo: saem do confronto entre a dose
(PAM) e a medida direta (Censo Agro 2006, script 13), que o projeto já tem.

O QUE A LITERATURA DIZ SOBRE ESTA CONFIGURAÇÃO
----------------------------------------------

> Rull, R. P. & Ritz, B. (2003). *Historical pesticide exposure in California
> using pesticide use reports and land-use surveys: an assessment of
> misclassification error and bias.* **Environmental Health Perspectives**
> 111(13): 1582–1589. PMID 14527836.

Eles simulam exatamente a troca que este projeto faz — usar **proximidade a
cultura** no lugar de **registro de aplicação** — e o achado é:

> *se a misclassificação é não-diferencial e a **prevalência de exposição é
> baixa**, **pequenas reduções de especificidade** produzem **reduções
> substanciais** na estimativa de risco.*

⚠️ **As duas condições valem aqui, e com folga.** A prevalência do tratamento
verdadeiro é ~3,8% dos municípios (7 de 184 com aeronave em 2006), e a
especificidade da classificação por decil de dose não é alta o bastante para
compensar isso. O resultado previsto pela literatura é atenuação substancial —
não marginal.

⚠️ E o número que decide não é a especificidade: é o **VPP** (valor preditivo
positivo), porque é ele que diz que fração do grupo "tratado" estava de fato
tratada. Com prevalência baixa, especificidade de 90% ainda produz VPP perto de
10% — e é esse o mecanismo que Rull & Ritz descrevem.

O LIMITE
--------

O λ que o Corolário 5 de Denteh & Kédagni (arXiv:2207.11890) pede é exatamente
`P(ε=1|D=1) + P(ε=1|D=0)`, isto é, `(1 - VPP) + taxa de falso negativo`. Este
script o calcula e aplica:

    min{ θ/(1-λ), θ } ≤ ATT ≤ max{ θ/(1-λ), θ }

⚠️ **TRÊS RESSALVAS, E SÃO SÉRIAS — leia antes de usar o número.**

1. São **limites de estimativa pontual**, não intervalos de confiança.
   Inferência sobre eles exige *intersection bounds* (Chernozhukov, Lee & Rosen).
2. O Corolário 5 exige misclassificação **não-diferencial**. Aqui ela
   provavelmente **não** é: ter aeronave correlaciona com porte do
   estabelecimento, que correlaciona com desfecho perinatal. Sob erro
   diferencial, a Proposição 1 do mesmo artigo diz que o **sinal pode inverter**,
   e o limite abaixo não vale.
3. "Ter aeronave em 2006" **não é** "ser tratado em 2019". O dado é de treze
   anos antes, conta estabelecimentos e não voos, e prestador sediado num
   município pulveriza lavoura do vizinho. O λ daqui é **teto**, não medida.

Por isso o script imprime uma **faixa** de λ, não um λ.

Uso:
    python scripts/estimate/12_erro_de_classificacao.py                # números da §5.4
    python scripts/estimate/12_erro_de_classificacao.py --theta -21.85
    python scripts/estimate/12_erro_de_classificacao.py \
        --censo data/processed/censo_agro_equipamento_ce.csv \
        --dose  data/processed/pam_ce_muni_cultura_media__sidra.parquet

Saída: `data/processed/erro_classificacao_dose.csv` (gitignored).
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"

# MDE do desenho (§6 do paper). O limite só é informativo contra ele.
MDE_G = 33.4

# Números da §5.4 do paper, usados quando não há artefatos. ⚠️ Fonte: Censo
# Agropecuário 2006, tabela SIDRA 1008, rodado pelo script 13 em 2026-09-22.
PUBLICADOS = {
    "n_municipios": 184,
    "municipios_com_aeronave": 7,
    "municipios_decil_com_aeronave": 2,   # Limoeiro do Norte (18) e Quixeré (9)
}
# ✅ Divergência 17 × 19 RESOLVIDA em 2026-09-22, contra os artefatos: a banana
# tem 169 municípios com área positiva, e o decil da convenção do Gate 1 é
# sobre os positivos — 169/10 ≈ 17. O 19 vinha do denominador errado (184
# municípios do CE, ceil = 19), que não é o corte que a pré-especificação usa.
# Com 17: 2 com aeronave (Limoeiro 18, Quixeré 9), 15 sem, VPP 11,8%.
TAMANHOS_DECIL = (17,)

# Coeficientes já reportados na §6 do paper, em gramas.
COEFICIENTES_PAPER = {
    "synthdid": -20.16,
    "controle_sintetico": -34.64,
    "did_simples": -21.85,
}


def metricas_classificacao(n_municipios: int, com_aeronave: int,
                           tamanho_decil: int, decil_com_aeronave: int) -> dict:
    """Matriz de confusão da dose contra a medida direta de método.

    `D = 1` é "está no decil superior da dose"; `D* = 1` é "tinha aeronave".
    """
    if decil_com_aeronave > min(com_aeronave, tamanho_decil):
        raise ValueError("decil_com_aeronave não pode exceder com_aeronave nem o decil")
    if tamanho_decil >= n_municipios or com_aeronave >= n_municipios:
        raise ValueError("decil e com_aeronave têm de ser menores que n_municipios")

    vp = decil_com_aeronave
    fp = tamanho_decil - vp
    fn = com_aeronave - vp
    vn = n_municipios - tamanho_decil - fn

    sensibilidade = vp / com_aeronave
    especificidade = vn / (n_municipios - com_aeronave)
    vpp = vp / tamanho_decil
    # λ do Corolário 5: P(ε=1|D=1) + P(ε=1|D=0).
    lambda_ = (1 - vpp) + fn / (n_municipios - tamanho_decil)
    return {
        "tamanho_decil": tamanho_decil,
        "vp": vp, "fp": fp, "fn": fn, "vn": vn,
        "prevalencia": com_aeronave / n_municipios,
        "sensibilidade": sensibilidade,
        "especificidade": especificidade,
        "vpp": vpp,
        "lambda_teto": lambda_,
    }


# O parquet agregado do script 01 chama a coluna `area_ha_media` — a média da
# janela pré-ban. Só o formato longo, ano a ano, tem `area_ha`. Aceitar os dois
# evita depender de qual dos dois arquivos chega pelo `--pam`; o que não pode
# é falhar com KeyError cru, que foi exatamente o que escondeu esta divergência
# (os testes usavam `area_ha`, o script 01 grava `area_ha_media`).
COLUNAS_DE_AREA = ("area_ha_media", "area_ha")


def coluna_de_area(df: pd.DataFrame) -> str:
    for col in COLUNAS_DE_AREA:
        if col in df.columns:
            return col
    raise KeyError(
        f"PAM sem coluna de área: esperava uma de {COLUNAS_DE_AREA}, "
        f"veio {list(df.columns)}"
    )


def metricas_de_artefatos(censo_csv: Path, dose_parquet: Path, cultura: str,
                         tamanho_decil: int | None = None) -> dict:
    """Recalcula as métricas a partir dos artefatos, em vez dos números da §5.4.

    `censo_csv` sai do script 13 (`censo_agro_equipamento_ce.csv`) e traz
    `cod_ibge6` e `aeronave`; `dose_parquet` sai do script 01
    (`pam_ce_muni_cultura_media__*.parquet`) e traz `cod_ibge`, `cultura`,
    `area_ha_media`.

    ⚠️ O decil é calculado sobre os municípios com área POSITIVA da cultura —
    que é a convenção do Gate 1 (169 para a banana), não sobre os 184. É
    justamente essa escolha que gera a divergência 17 vs 19 no repositório, e
    deixá-la explícita aqui é o ponto.
    """
    censo = pd.read_csv(censo_csv, dtype={"cod_ibge6": str})
    dose = pd.read_parquet(dose_parquet)
    dose["cod_ibge"] = dose["cod_ibge"].astype(str).str[:6]
    dose = dose[dose["cultura"].str.contains(cultura, case=False, na=False)]
    col_area = coluna_de_area(dose)
    dose = dose[dose[col_area] > 0]
    if dose.empty:
        raise ValueError(f"nenhum município com área positiva de {cultura!r}")

    n_positivos = dose["cod_ibge"].nunique()
    k = tamanho_decil or max(1, round(n_positivos / 10))
    decil = set(dose.nlargest(k, col_area)["cod_ibge"])

    com_aeronave = set(censo.loc[censo["aeronave"] > 0, "cod_ibge6"])
    n_municipios = censo["cod_ibge6"].nunique()
    return metricas_classificacao(
        n_municipios=n_municipios,
        com_aeronave=len(com_aeronave),
        tamanho_decil=len(decil),
        decil_com_aeronave=len(decil & com_aeronave),
    )


def limite_corolario5(theta: float, lambda_: float) -> tuple[float, float]:
    """Limites do ATT sob misclassificação não-diferencial (Corolário 5).

    ⚠️ `lambda_ >= 1` não tem limite: o corolário exige λ < 1, e λ = 1 significa
    que a classificação não carrega informação alguma. Levanta em vez de
    devolver infinito, porque um infinito silencioso viraria número em tabela.
    """
    if not 0 <= lambda_ < 1:
        raise ValueError(f"λ tem de estar em [0, 1); recebido {lambda_:.3f}")
    escalado = theta / (1 - lambda_)
    return (min(escalado, theta), max(escalado, theta))


def tabela_limites(theta: float, lambdas, rotulo: str) -> pd.DataFrame:
    linhas = []
    for lam in lambdas:
        inf, sup = limite_corolario5(theta, lam)
        linhas.append({
            "estimador": rotulo, "theta_g": theta, "lambda": lam,
            "limite_inferior_g": inf, "limite_superior_g": sup,
            # O que decide se o limite é informativo: ele ultrapassa o MDE?
            "excede_mde": abs(min(inf, sup)) > MDE_G,
        })
    return pd.DataFrame(linhas)


def imprime(metricas: list[dict], limites: pd.DataFrame) -> None:
    barra = "=" * 84
    print(barra)
    print("ERRO DE CLASSIFICAÇÃO DA DOSE — a flag 7, medida")
    print(barra)
    print("  A dose ('decil superior') contra a medida direta ('tinha aeronave'):")
    print()
    print(f"  {'decil':>6} {'sens.':>8} {'espec.':>8} {'VPP':>8} {'λ teto':>8}")
    for m in metricas:
        print(f"  {m['tamanho_decil']:>6} {m['sensibilidade']:>7.1%} "
              f"{m['especificidade']:>7.1%} {m['vpp']:>7.1%} {m['lambda_teto']:>8.3f}")
    print()
    print(f"  prevalência do tratamento verdadeiro: {metricas[0]['prevalencia']:.1%}")
    print()
    print("  ⚠️ O número que decide é o VPP, não a especificidade: com prevalência")
    print("     baixa, especificidade de ~90% ainda deixa ~9 de cada 10 municípios")
    print("     'tratados' sem tratamento a perder. É o mecanismo de Rull & Ritz")
    print("     (2003): prevalência baixa + especificidade imperfeita = atenuação")
    print("     SUBSTANCIAL, não marginal.")
    print(barra)
    print("  LIMITES DO ATT (Corolário 5, Denteh & Kédagni) — pontuais, não IC:")
    print()
    for est in limites["estimador"].unique():
        sub = limites[limites["estimador"] == est]
        print(f"  {est}:")
        for _, r in sub.iterrows():
            marca = "→ excede o MDE" if r["excede_mde"] else ""
            print(f"    λ={r['lambda']:.2f}  [{r['limite_inferior_g']:8.1f}; "
                  f"{r['limite_superior_g']:7.1f}] g  {marca}")
    print()
    print(f"  MDE do desenho: {MDE_G} g.")
    print("  ⚠️ NÃO vale sob erro diferencial — e há razão para crer que o erro")
    print("     aqui é diferencial (aeronave correlaciona com porte, porte com")
    print("     desfecho). Sob erro diferencial o SINAL pode inverter.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--theta", type=float, action="append", default=None,
                   help="Coeficiente em gramas. Repetível. Omitir usa os da §6.")
    p.add_argument("--lambdas", type=float, nargs="+",
                   default=[0.3, 0.5, 0.7],
                   help="Faixa de λ a reportar. O teto medido entra sempre.")
    p.add_argument("--censo", type=Path, default=None,
                   help="CSV do script 13. Com --dose, recalcula em vez de usar a §5.4.")
    p.add_argument("--dose", type=Path, default=None,
                   help="Parquet do script 01. Exige --censo.")
    p.add_argument("--cultura", default="banana",
                   help="Cultura-âncora para o decil (padrão: banana).")
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if (args.censo is None) != (args.dose is None):
        print("[erro] --censo e --dose andam juntos.")
        return 1
    if args.censo is not None:
        fonte = "artefatos"
        metricas = [metricas_de_artefatos(args.censo, args.dose, args.cultura)]
    else:
        # ⚠️ Sem artefatos, os números da §5.4. As DUAS leituras do decil
        # entram, porque o repositório reporta 17 e 19 e a divergência não
        # pode ser resolvida escolhendo em silêncio.
        fonte = "publicados"
        metricas = [
            metricas_classificacao(
                PUBLICADOS["n_municipios"], PUBLICADOS["municipios_com_aeronave"],
                tamanho, PUBLICADOS["municipios_decil_com_aeronave"],
            )
            for tamanho in TAMANHOS_DECIL
        ]

    # O teto medido é informativo justamente por ser absurdo — mostra que λ
    # ingênuo não serve, e que a faixa tem de ser argumentada.
    lambdas = sorted(set(args.lambdas))
    coeficientes = ({f"theta_{i}": t for i, t in enumerate(args.theta)}
                    if args.theta else COEFICIENTES_PAPER)
    limites = pd.concat(
        [tabela_limites(theta, lambdas, rotulo) for rotulo, theta in coeficientes.items()],
        ignore_index=True,
    )

    imprime(metricas, limites)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "erro_classificacao_dose.csv"
    saida = limites.copy()
    for m in metricas:
        saida[f"lambda_teto_decil{m['tamanho_decil']}"] = m["lambda_teto"]
        saida[f"vpp_decil{m['tamanho_decil']}"] = m["vpp"]
    saida["fonte"] = fonte
    saida["extraido_em"] = date.today().isoformat()
    saida.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
