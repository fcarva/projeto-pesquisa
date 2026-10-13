"""E19 — O lado do custo: a banana do Ceará perdeu com o ban? (à la Manuweera et al. 2008)

POR QUE ESTE SCRIPT EXISTE
--------------------------

A pergunta do Ensaio 2 tem dois lados: o que o ban comprou em saúde e o que ele
custou em produção. A literatura de banimentos de agrotóxicos mede o custo de um
jeito simples e replicável: compara o rendimento das culturas no lugar que
proibiu com o de vizinhos que não proibiram, antes e depois.

- Manuweera et al. (2008, *EHP* 116(4):492–495, doi:10.1289/ehp.11029): Sri
  Lanka contra Índia, Paquistão e Bangladesh, 1980–2005. Nenhuma queda de
  rendimento alinhada às proibições de 1995 e 1998.
- Chowdhury et al. (2018, *IJE* 47(1):175–184, doi:10.1093/ije/dyx157):
  Bangladesh, a mesma pergunta, a mesma resposta.
- Lin et al. (2026, *BMJ Glob Health* 11(2):e022329,
  doi:10.1136/bmjgh-2025-022329): Coreia do Sul, regressão de *joinpoint* nos
  rendimentos 2000–2019, nenhuma quebra alinhada às proibições de 2011–2012.

Aqui a unidade é a UF e a cultura é a banana (PAM, tabela 1613, produto 2720). O
Ceará é o único tratado; os comparadores padrão são as outras oito UFs do
Nordeste, que passaram pela mesma seca de 2012–2017.

MÉTODO
------

DiD 2×2 em médias (equivale ao TWFE num painel balanceado com um tratado):

    β = [ȳ_CE(pós) − ȳ_CE(pré)] − [ȳ_C(pós) − ȳ_C(pré)]

com y em log (área colhida, quantidade, rendimento), ȳ_C a média simples dos
comparadores por ano, pré = 2010–2018 e pós = 2019–2024 por padrão. Inferência
por **placebo no espaço**: cada comparador faz o papel de tratado contra os
demais, sem o Ceará, e o p-valor é a posição de |β_CE| na distribuição dos |β|
(Abadie et al. 2010; com um tratado, é o que se pode fazer honestamente). Um
**placebo no tempo** repete a conta só no pré-período, com quebra falsa em 2015.

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não é o efeito causal do ban sobre a economia.** É a forma reduzida estadual
  de um ban que alcança só a banana da Chapada e de onde mais houvesse avião. A
  diluição da flag 7 vale aqui também, e mais forte: a UF inteira é o tratado.
- **Não controla chuva por UF.** A seca de 2012–2017 e sua saída atingiram o
  Nordeste de forma desigual. O script 18 só cobre o Ceará.
- **Não usa o valor da produção.** Ele vem nominal; deflacionar é passo à parte.
- **Não tem modo simulado.**

Uso:
    python scripts/data_prep/19_banana_uf_custo.py
    python scripts/data_prep/19_banana_uf_custo.py --comparadores todas
    python scripts/data_prep/19_banana_uf_custo.py --pre 2012 2018 --pos 2019 2024

Saídas (gitignored):
    data/raw/pam_banana/pam_1613_banana_uf_{ini}_{fim}.json   cache da API do IBGE
    data/processed/banana_uf_painel.csv                        painel UF × ano
    data/processed/banana_uf_did.csv                           β, placebos e p-valor
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
RAW_DIR = RAIZ / "data" / "raw" / "pam_banana"
OUT_DIR = RAIZ / "data" / "processed"

URL = ("https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{periodos}"
       "/variaveis/216|214|112?localidades=N3[all]&classificacao=82[2720]")
VARIAVEIS = {"Área colhida": "area_ha", "Quantidade produzida": "producao_t",
             "Rendimento médio da produção": "rendimento_kg_ha"}
CE = "23"
NORDESTE = ("21", "22", "24", "25", "26", "27", "28", "29")   # sem o Ceará


def tidy_ibge(dados: list) -> pd.DataFrame:
    """JSON da API de agregados v3 → UF × ano × variável. '-' e '...' viram NaN."""
    linhas = []
    for var in dados:
        nome = VARIAVEIS.get(var["variavel"])
        if nome is None:
            continue
        for res in var["resultados"]:
            for s in res["series"]:
                for ano, v in s["serie"].items():
                    linhas.append({"uf": str(s["localidade"]["id"]),
                                   "nome": s["localidade"]["nome"],
                                   "ano": int(ano), "var": nome,
                                   "v": pd.to_numeric(v, errors="coerce")})
    longo = pd.DataFrame(linhas)
    if longo.empty:
        raise ValueError("resposta da API sem séries de banana")
    # unstack, e não pivot_table: o pivot descarta o ano em que tudo veio "-",
    # e um painel que perde linhas em silêncio muda a média dos comparadores.
    return (longo.groupby(["uf", "nome", "ano", "var"])["v"].first().unstack("var")
            .reset_index().rename_axis(columns=None))


def did_um_tratado(painel: pd.DataFrame, y: str, tratado: str, controles,
                   pre: tuple[int, int], pos: tuple[int, int]) -> float:
    """β do DiD 2×2 em médias, com o tratado contra a média simples dos controles."""
    p = painel[painel["uf"].isin([tratado, *controles])].copy()
    p["periodo"] = np.where(p["ano"].between(*pre), "pre",
                            np.where(p["ano"].between(*pos), "pos", None))
    p = p.dropna(subset=["periodo", y])
    trat = p[p["uf"] == tratado].groupby("periodo")[y].mean()
    ctrl = (p[p["uf"] != tratado].groupby(["ano", "periodo"])[y].mean()
            .groupby("periodo").mean())
    if not {"pre", "pos"} <= set(trat.index) or not {"pre", "pos"} <= set(ctrl.index):
        return float("nan")
    return float((trat["pos"] - trat["pre"]) - (ctrl["pos"] - ctrl["pre"]))


def placebo_no_espaco(painel, y, tratado, controles, pre, pos) -> pd.DataFrame:
    """β para o tratado e para cada controle no papel de tratado (sem o tratado real)."""
    linhas = [{"uf": tratado, "beta": did_um_tratado(painel, y, tratado, controles, pre, pos),
               "papel": "tratado"}]
    for c in controles:
        outros = [o for o in controles if o != c]
        linhas.append({"uf": c, "beta": did_um_tratado(painel, y, c, outros, pre, pos),
                       "papel": "placebo"})
    return pd.DataFrame(linhas)


def p_valor_permutacao(betas: pd.DataFrame) -> float:
    """Fração de unidades com |β| ≥ |β do tratado|, contando o próprio tratado."""
    b = betas.dropna(subset=["beta"])
    alvo = abs(b.loc[b["papel"] == "tratado", "beta"].iloc[0])
    return float((b["beta"].abs() >= alvo - 1e-12).mean())


def baixa(url: str, destino: Path, timeout: int = 180) -> Path:
    import requests

    destino.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    destino.write_text(r.text, encoding="utf-8")
    return destino


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--pre", type=int, nargs=2, default=[2010, 2018], metavar=("INI", "FIM"))
    p.add_argument("--pos", type=int, nargs=2, default=[2019, 2024], metavar=("INI", "FIM"))
    p.add_argument("--comparadores", choices=["nordeste", "todas"], default="nordeste")
    p.add_argument("--json", type=Path, default=None, help="resposta da API já baixada")
    p.add_argument("--cache", type=Path, default=RAW_DIR)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    pre, pos = tuple(args.pre), tuple(args.pos)
    if pre[1] >= pos[0] or pre[0] > pre[1] or pos[0] > pos[1]:
        print("ERRO: janelas pré e pós inválidas ou sobrepostas", file=sys.stderr)
        return 1

    ini, fim = pre[0], pos[1]
    fonte = args.json
    if fonte is None:
        fonte = args.cache / f"pam_1613_banana_uf_{ini}_{fim}.json"
        if not fonte.exists():
            periodos = "|".join(str(a) for a in range(ini, fim + 1))
            print(f"baixando PAM banana {ini}–{fim} (API do IBGE) …")
            baixa(URL.format(periodos=periodos), fonte)
    painel = tidy_ibge(json.loads(Path(fonte).read_text(encoding="utf-8")))
    for c in VARIAVEIS.values():
        painel[f"log_{c}"] = np.log(painel[c].where(painel[c] > 0))

    ufs = sorted(painel["uf"].unique())
    if CE not in ufs:
        print("ERRO: o Ceará não está na resposta", file=sys.stderr)
        return 1
    controles = [u for u in (NORDESTE if args.comparadores == "nordeste" else ufs)
                 if u != CE and u in ufs]

    linhas = []
    for c in VARIAVEIS.values():
        y = f"log_{c}"
        b = placebo_no_espaco(painel, y, CE, controles, pre, pos)
        b_tempo = did_um_tratado(painel[painel["ano"] <= pre[1]], y, CE, controles,
                                 (pre[0], 2014), (2015, pre[1]))
        linhas.append({
            "desfecho": c,
            "beta_log": b.loc[b["papel"] == "tratado", "beta"].iloc[0],
            "efeito_pct": 100 * np.expm1(b.loc[b["papel"] == "tratado", "beta"].iloc[0]),
            "p_placebo_espaco": p_valor_permutacao(b),
            "n_unidades": int(b["beta"].notna().sum()),
            "beta_placebo_tempo_2015": b_tempo,
            "placebos": ";".join(f"{u}:{v:.3f}" for u, v in zip(b["uf"], b["beta"])),
        })
    saida = pd.DataFrame(linhas)
    saida.insert(0, "extraido_em", dt.date.today().isoformat())
    saida["pre"], saida["pos"] = f"{pre[0]}-{pre[1]}", f"{pos[0]}-{pos[1]}"
    saida["comparadores"] = ",".join(controles)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    painel.to_csv(args.out_dir / "banana_uf_painel.csv", index=False, encoding="utf-8")
    saida.to_csv(args.out_dir / "banana_uf_did.csv", index=False, encoding="utf-8")

    print(f"\nBanana, Ceará contra {len(controles)} UF(s); pré {pre[0]}–{pre[1]}, pós {pos[0]}–{pos[1]}")
    print(saida[["desfecho", "efeito_pct", "p_placebo_espaco", "n_unidades",
                 "beta_placebo_tempo_2015"]].round(3).to_string(index=False))
    print("\n⚠️ Forma reduzida estadual, sem controle de chuva por UF. Não é o efeito do ban.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
