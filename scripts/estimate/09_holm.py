"""E8 — Correção de Holm sobre a família confirmatória.

A §6 da `docs/pre-especificacao.md` declara duas hipóteses confirmatórias e
manda corrigir a família por **Holm**. Este script é o cumprimento desse
compromisso; até 2026-09-22 ele não existia, e a auditoria
(`docs/auditoria-pre-especificacao.md`, achado 1) registrou a falta.

⚠️ TRÊS COISAS QUE ESTE SCRIPT FAZ QUESTÃO DE NÃO ESCONDER
-----------------------------------------------------------

1. **As hipóteses são DIRECIONAIS.** A §6 não declara "existe efeito"; declara
   `ACR(d) > 0` para o peso e `ACR(d) < 0` para o óbito fetal. A leitura fiel é
   portanto de teste **unilateral**, e é ela que entra na coluna principal.

2. ⚠️ **E o peso tem sinal CONTRÁRIO ao previsto.** Quando isso acontece, o
   unilateral na direção pré-especificada não pode rejeitar — por construção,
   não por falta de poder. Reportar só ele seria esconder a inversão atrás de um
   `p` alto. Por isso o relatório traz unilateral e bilateral lado a lado, e
   grita quando o sinal diverge.

3. ⚠️ **A pré-especificação NÃO diz qual dos três procedimentos de inferência
   alimenta o Holm.** É uma lacuna dela, não uma escolha deste script. Então
   aplica-se Holm aos três, e a tabela inteira é reportada. Se os três
   concordarem, a lacuna não teve consequência — e é o que se espera aqui.

⚠️ DUAS FAMÍLIAS, E A SEGUNDA É PÓS-RESULTADO (auditoria de 2026-09-23)
----------------------------------------------------------------------
A família da §6 é sobre o ACR, e este script a testa pela inclinação OLS de
dy sobre a dose (a forma reduzida do 04). Em 2026-09-22 o alvo principal
passou a ser o nível, o ATT(d|d) agregado, depois de ver a curva (§8 da
pré-especificação). Corrigir a inclinação e dizer que "nenhuma confirmatória
rejeita" deixava o nível sem correção nenhuma: são funcionais diferentes, e
nem o sinal precisa coincidir (doses [0; 0; 0,1; 1] e dy [0; 0; −100; 10]
dão nível −45 e inclinação +35).

- **Família A, `confirmatoria_original`:** a da §6, como foi declarada.
- **Família B, `nivel_pos_resultado`:** as mesmas duas hipóteses sobre o
  nível, com t de Welch, wild bootstrap e permutação. É **adaptativa**: foi
  escolhida depois de ver o resultado, e o CSV diz isso em cada linha. Não é
  confirmatória prospectiva, e não substitui a A.

E um nulo não vira número: `holm([nan, 0,04])` devolvia `[0,08; 0,08]`. Agora
o nulo continua nulo, o teste que falta conta como p = 1 para os outros (o
conservador), e a família sai marcada como incompleta.

Saída: `data/processed/holm_confirmatorios__d0-<def>.csv`
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from importlib import import_module

_rb = import_module("04_robustness")
primeira_diferenca = _rb.primeira_diferenca
estima = _rb.estima
erro_padrao_ingenuo = _rb.erro_padrao_ingenuo
wild_cluster_bootstrap = _rb.wild_cluster_bootstrap
inferencia_aleatorizacao = _rb.inferencia_aleatorizacao
inferencia_nivel = _rb.inferencia_nivel
zeros_suspeitos = _rb.zeros_suspeitos
aplica_d_zero = _rb.aplica_d_zero
_saida_utf8 = _rb._saida_utf8
N_BOOT = _rb.N_BOOT
SEED = _rb.SEED

RAIZ = Path(__file__).resolve().parents[2]
PAINEL = RAIZ / "data" / "processed" / "painel_ensaio1.parquet"
OUT_DIR = RAIZ / "data" / "processed"

# A família confirmatória, verbatim da §6 da pré-especificação.
CONFIRMATORIOS = [
    {
        "n": 1,
        "desfecho": "peso_medio",
        "exposicao": "share_gestacao_pos_ban",
        "direcao": +1,
        "hipotese": "ACR(d) > 0 — remover a exposição aumenta o peso ao nascer",
    },
    {
        "n": 2,
        "desfecho": "taxa_obito_fetal",
        "exposicao": "share_gestacao_pos_ban",
        "direcao": -1,
        "hipotese": "ACR(d) < 0 — o ban reduz o óbito fetal",
    },
]


# --------------------------------------------------------------------------
# Holm
# --------------------------------------------------------------------------

def holm(ps: list[float]) -> list[float]:
    """Holm (1979), step-down. Controla FWER sem supor independência.

    Ordena crescente, multiplica o k-ésimo por (m - k + 1), e impõe
    monotonicidade acumulando o máximo — sem ela um p ajustado poderia ficar
    menor que o anterior, o que não é um p-valor.

    ⚠️ p nulo (teste que não rodou) continua nulo na saída. Para os outros, ele
    conta como p = 1: fica no fim da ordem e m continua sendo o tamanho da
    família inteira. É o ajuste conservador. Até 2026-09-23, `max(0,08, nan)`
    devolvia 0,08, e o teste ausente ganhava p ajustado finito.
    """
    brutos = np.asarray(ps, dtype=float)
    ausente = ~np.isfinite(brutos)
    m = len(brutos)
    idx = np.argsort(np.where(ausente, np.inf, brutos), kind="stable")
    ajustados = np.empty(m, dtype=float)
    corrente = 0.0
    for k, i in enumerate(idx):
        val = (m - k) * (1.0 if ausente[i] else brutos[i])
        corrente = max(corrente, val)
        ajustados[i] = min(1.0, corrente)
    ajustados[ausente] = np.nan
    return [float(x) for x in ajustados]


def p_unilateral(dados: pd.DataFrame, direcao: int,
                 n_perm: int = N_BOOT, seed: int = SEED) -> float:
    """p unilateral por aleatorização, na direção pré-especificada.

    Conta com que frequência a distribuição nula produz efeito ao menos tão
    extremo QUANTO O PREVISTO. Se o ponto observado aponta para o outro lado,
    isto devolve algo acima de 0,5 — e é para devolver mesmo: a evidência é
    contra a hipótese, não a favor.
    """
    rng = np.random.default_rng(seed)
    beta = estima(dados)
    if np.isnan(beta):
        return float("nan")

    base = dados[["dose", "dy"]].copy()
    nulos = np.empty(n_perm)
    for k in range(n_perm):
        emb = base.copy()
        emb["dose"] = rng.permutation(base["dose"].to_numpy())
        nulos[k] = estima(emb)

    validos = nulos[~np.isnan(nulos)]
    if not len(validos):
        return float("nan")
    if direcao > 0:
        return float((validos >= beta).mean())
    return float((validos <= beta).mean())


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

FAMILIAS = {
    "confirmatoria_original": "A — a da §6: inclinação (ACR), como declarada",
    "nivel_pos_resultado": "B — o nível ATT(d|d) agregado; PÓS-RESULTADO, adaptativa",
}
COLUNAS_P = ("p_uni", "p_rnd", "p_wcb", "p_welch")


def imprime(res: pd.DataFrame) -> None:
    barra = "=" * 84
    print(barra)
    print("E8 — CORREÇÃO DE HOLM SOBRE A FAMÍLIA CONFIRMATÓRIA")
    print(barra)
    print("A §6 da pré-especificação declara DUAS hipóteses e manda corrigir por")
    print("Holm. São estas, com a direção que ela fixou antes de qualquer dado:")
    print()
    for _, r in res[res["familia"] == "confirmatoria_original"].iterrows():
        print(f"  H{int(r['n'])}: {r['hipotese']}")
    print()
    print("⚠️ A família B repete as duas sobre o NÍVEL, que virou o alvo principal")
    print("   depois de ver a curva (§8, 2026-09-22). É adaptativa e não substitui a A.")

    for fam, titulo in FAMILIAS.items():
        bloco = res[res["familia"] == fam]
        if bloco.empty:
            continue
        print("-" * 84)
        print(f"FAMÍLIA {titulo}")
        if not bloco["completa"].all():
            print("  ⚠️ FAMÍLIA INCOMPLETA: há teste que não rodou. O p dele fica nulo e")
            print("     conta como 1 para os outros. Não reportar como família inteira.")
        invertidos = bloco[bloco["sinal_bate"] == False]  # noqa: E712
        for _, r in invertidos.iterrows():
            if np.isnan(r["beta"]):
                continue
            esperado = "positivo" if r["direcao"] > 0 else "negativo"
            print(f"  ⚠️ H{int(r['n'])} ({r['desfecho']}): previa-se {esperado}, "
                  f"observou-se {r['beta']:+.5f}. O unilateral na direção prevista")
            print("     NÃO PODE rejeitar aqui, por construção; o bilateral vai junto.")
        print(f"  {'hipótese':<26} {'procedimento':<22} {'p bruto':>9} {'p Holm':>9}")
        print("  " + "-" * 70)
        rotulos = {"p_uni": "unilateral (§6)", "p_rnd": "bilateral permutação",
                   "p_wcb": "bilateral wild", "p_welch": "bilateral t de Welch"}
        for _, r in bloco.iterrows():
            tag = f"H{int(r['n'])} {str(r['desfecho'])[:20]}"
            for col in COLUNAS_P:
                if col == "p_welch" and fam == "confirmatoria_original":
                    continue    # a família A nunca teve t de Welch
                print(f"  {tag:<26} {rotulos[col]:<22} {r[col]:>9.4f} {r[col + '_holm']:>9.4f}")
                tag = ""
        cols_holm = [f"{c}_holm" for c in COLUNAS_P]
        algum = (bloco[cols_holm] < 0.05).any().any()
        if algum:
            print("  ⚠️ ALGUMA HIPÓTESE DESTA FAMÍLIA REJEITA A 5% DEPOIS DE HOLM.")
            print("     Ler o sinal antes de escrever: rejeitar no sentido contrário ao")
            print("     previsto não confirma a hipótese.")
        else:
            print("  ✔ Nenhuma hipótese desta família rejeita a 5% depois de Holm.")
    print(barra)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def _linha_vazia(h: dict, familia: str, estimando: str) -> dict:
    return {"familia": familia, "estimando": estimando, "completa": False,
            "n": h["n"], "desfecho": h["desfecho"], "exposicao": h["exposicao"],
            "hipotese": h["hipotese"], "direcao": h["direcao"], "beta": np.nan,
            "sinal_bate": False, "ep": np.nan, **{c: np.nan for c in COLUNAS_P},
            "n_municipios": 0, "n_controles": 0}


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--painel", type=Path, default=PAINEL)
    parser.add_argument("--corte-pre", default="2018-12")
    parser.add_argument("--corte-pos", default="2019-10")
    parser.add_argument("--d-zero", choices=("1", "4"), default="1",
                        help="construção do d = 0, como no 04 (o `make real` passa D_ZERO)")
    parser.add_argument("--aptidao-p", type=float, default=0.75)
    parser.add_argument("--n-boot", type=int, default=N_BOOT)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if not args.painel.exists():
        print(f"✘ painel não encontrado: {args.painel}")
        return 1

    from scipy.stats import t as dist_t

    painel = pd.read_parquet(args.painel)
    ya, ma = (int(x) for x in args.corte_pre.split("-"))
    yb, mb = (int(x) for x in args.corte_pos.split("-"))
    t_pre, t_pos = ya * 12 + ma - 1, yb * 12 + mb - 1

    suspeitos: set = set()
    if args.d_zero == "4":
        try:
            suspeitos = zeros_suspeitos(painel, args.aptidao_p)
        except ValueError as erro:
            print(f"✘ {erro}")
            return 1

    linhas = []
    for h in CONFIRMATORIOS:
        if h["desfecho"] not in painel.columns:
            print(f"⚠️ desfecho ausente no painel: {h['desfecho']} — p nulo, família incompleta")
            linhas.append(_linha_vazia(h, "confirmatoria_original", "inclinação OLS de dy na dose"))
            linhas.append(_linha_vazia(h, "nivel_pos_resultado", "nível: E[dy|d>0] − E[dy|d=0]"))
            continue
        dados = aplica_d_zero(primeira_diferenca(painel, h["desfecho"], t_pre, t_pos), suspeitos)
        n_ctrl = int((dados["dose"] <= 0).sum())

        # A — a família da §6, como declarada
        beta = estima(dados)
        wcb = wild_cluster_bootstrap(dados, args.n_boot, args.seed)
        rnd = inferencia_aleatorizacao(dados, args.n_boot, args.seed)
        linhas.append({
            "familia": "confirmatoria_original",
            "estimando": "inclinação OLS de dy na dose",
            "completa": True,
            "n": h["n"], "desfecho": h["desfecho"], "exposicao": h["exposicao"],
            "hipotese": h["hipotese"], "direcao": h["direcao"],
            "beta": beta,
            "sinal_bate": bool(np.sign(beta) == h["direcao"]) if not np.isnan(beta) else False,
            "ep": erro_padrao_ingenuo(dados),
            "p_uni": p_unilateral(dados, h["direcao"], args.n_boot, args.seed),
            "p_rnd": rnd["p"], "p_wcb": wcb["p"], "p_welch": np.nan,
            "n_municipios": len(dados), "n_controles": n_ctrl,
        })

        # B — o nível, pós-resultado
        niv = inferencia_nivel(dados, args.n_boot, args.seed)
        t_obs = (niv["nivel"] / niv["ep_welch"]
                 if np.isfinite(niv["ep_welch"]) and niv["ep_welch"] > 0 else np.nan)
        gl = niv["gl_welch"]
        if np.isfinite(t_obs) and np.isfinite(gl):
            p_uni_b = float(dist_t.sf(t_obs, gl) if h["direcao"] > 0 else dist_t.cdf(t_obs, gl))
        else:
            p_uni_b = np.nan
        linhas.append({
            "familia": "nivel_pos_resultado",
            "estimando": "nível: E[dy|d>0] − E[dy|d=0]",
            "completa": bool(np.isfinite(niv["nivel"])),
            "n": h["n"], "desfecho": h["desfecho"], "exposicao": h["exposicao"],
            "hipotese": h["hipotese"].replace("ACR(d)", "ATT(d|d) agregado"),
            "direcao": h["direcao"],
            "beta": niv["nivel"],
            "sinal_bate": (bool(np.sign(niv["nivel"]) == h["direcao"])
                           if np.isfinite(niv["nivel"]) else False),
            "ep": niv["ep_welch"],
            "p_uni": p_uni_b, "p_rnd": niv["p_perm"], "p_wcb": niv["p_wcb"],
            "p_welch": niv["p_welch"],
            "n_municipios": len(dados), "n_controles": n_ctrl,
        })

    res = pd.DataFrame(linhas)
    if res.empty:
        print("✘ nenhuma hipótese confirmatória pôde ser estimada.")
        return 1

    for fam in res["familia"].unique():
        sel = res["familia"] == fam
        for col in COLUNAS_P:
            res.loc[sel, f"{col}_holm"] = holm(res.loc[sel, col].tolist())
        res.loc[sel, "completa"] = bool(res.loc[sel, "completa"].all())
    res["d_zero"] = args.d_zero
    res["corte_pre"], res["corte_pos"] = args.corte_pre, args.corte_pos

    imprime(res)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / f"holm_confirmatorios__d0-{args.d_zero}.csv"
    res.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
