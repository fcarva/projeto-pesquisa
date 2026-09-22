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

Saída: `data/processed/holm_confirmatorios.csv`
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
    """
    m = len(ps)
    idx = np.argsort(ps)
    ajustados = np.empty(m, dtype=float)
    corrente = 0.0
    for k, i in enumerate(idx):
        val = (m - k) * ps[i]
        corrente = max(corrente, val)
        ajustados[i] = min(1.0, corrente)
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

def imprime(res: pd.DataFrame) -> None:
    barra = "=" * 84
    print(barra)
    print("E8 — CORREÇÃO DE HOLM SOBRE A FAMÍLIA CONFIRMATÓRIA")
    print(barra)
    print("A §6 da pré-especificação declara DUAS hipóteses e manda corrigir por")
    print("Holm. São estas, com a direção que ela fixou antes de qualquer dado:")
    print()
    for _, r in res.iterrows():
        print(f"  H{int(r['n'])}: {r['hipotese']}")
        print(f"      desfecho = {r['desfecho']}  |  β = {r['beta']:+.5f}")
    print("-" * 84)

    invertidos = res[res["sinal_bate"] == False]  # noqa: E712
    if len(invertidos):
        print("⚠️  SINAL CONTRÁRIO AO PRÉ-ESPECIFICADO")
        for _, r in invertidos.iterrows():
            esperado = "positivo" if r["direcao"] > 0 else "negativo"
            print(f"    H{int(r['n'])} ({r['desfecho']}): previa-se {esperado}, "
                  f"observou-se {r['beta']:+.5f}")
        print("    O teste unilateral na direção prevista NÃO PODE rejeitar aqui —")
        print("    por construção, não por falta de poder. É por isso que a coluna")
        print("    bilateral vai junto: ela é a que ainda diz alguma coisa.")
        print("-" * 84)

    print("p BRUTO e p AJUSTADO POR HOLM — os três procedimentos")
    print()
    print(f"  {'hipótese':<26} {'procedimento':<18} {'p bruto':>9} {'p Holm':>9}")
    print("  " + "-" * 66)
    for _, r in res.iterrows():
        tag = f"H{int(r['n'])} {r['desfecho'][:20]}"
        for proc, bruto, aj in [
            ("unilateral (§6)", r["p_uni"], r["p_uni_holm"]),
            ("bilateral aleat.", r["p_rnd"], r["p_rnd_holm"]),
            ("wild cluster", r["p_wcb"], r["p_wcb_holm"]),
        ]:
            print(f"  {tag:<26} {proc:<18} {bruto:>9.4f} {aj:>9.4f}")
            tag = ""
    print("-" * 84)

    algum = (res[["p_uni_holm", "p_rnd_holm", "p_wcb_holm"]] < 0.05).any().any()
    if algum:
        print("⚠️  ALGUMA HIPÓTESE SOBREVIVE A HOLM A 5%. Conferir antes de escrever:")
        print("    o gate do MDE da §5 continua valendo, e é independente deste.")
    else:
        print("✔  Nenhuma hipótese confirmatória rejeita a 5%, nem antes nem depois")
        print("   de Holm. A correção não muda a conclusão — e o valor de tê-la")
        print("   rodado é que isso agora é fato verificado, não expectativa.")
    print(barra)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    _saida_utf8()

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--painel", type=Path, default=PAINEL)
    parser.add_argument("--corte-pre", default="2018-12")
    parser.add_argument("--corte-pos", default="2019-10")
    parser.add_argument("--n-boot", type=int, default=N_BOOT)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if not args.painel.exists():
        print(f"✘ painel não encontrado: {args.painel}")
        return 1

    painel = pd.read_parquet(args.painel)
    ya, ma = (int(x) for x in args.corte_pre.split("-"))
    yb, mb = (int(x) for x in args.corte_pos.split("-"))
    t_pre, t_pos = ya * 12 + ma - 1, yb * 12 + mb - 1

    linhas = []
    for h in CONFIRMATORIOS:
        if h["desfecho"] not in painel.columns:
            print(f"⚠️ desfecho ausente no painel, pulando: {h['desfecho']}")
            continue
        dados = primeira_diferenca(painel, h["desfecho"], t_pre, t_pos)
        beta = estima(dados)
        wcb = wild_cluster_bootstrap(dados, args.n_boot, args.seed)
        rnd = inferencia_aleatorizacao(dados, args.n_boot, args.seed)
        p_uni = p_unilateral(dados, h["direcao"], args.n_boot, args.seed)

        linhas.append({
            "n": h["n"],
            "desfecho": h["desfecho"],
            "exposicao": h["exposicao"],
            "hipotese": h["hipotese"],
            "direcao": h["direcao"],
            "beta": beta,
            "sinal_bate": bool(np.sign(beta) == h["direcao"]) if not np.isnan(beta) else False,
            "ep_ingenuo": erro_padrao_ingenuo(dados),
            "p_uni": p_uni,
            "p_rnd": rnd["p"],
            "p_wcb": wcb["p"],
            "n_municipios": len(dados),
        })

    if not linhas:
        print("✘ nenhuma hipótese confirmatória pôde ser estimada.")
        return 1

    res = pd.DataFrame(linhas)
    for col in ("p_uni", "p_rnd", "p_wcb"):
        res[f"{col}_holm"] = holm(res[col].tolist()) if len(res) > 1 else res[col]

    if len(res) < len(CONFIRMATORIOS):
        print(f"⚠️ Holm aplicado a {len(res)} de {len(CONFIRMATORIOS)} hipóteses —")
        print("   a família está INCOMPLETA e a correção é otimista. Não reportar")
        print("   como se fosse a família inteira.")

    imprime(res)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "holm_confirmatorios.csv"
    res.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
