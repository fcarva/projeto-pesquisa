"""E18 — Chuva mensal por município (CHIRPS): o PRISM que o Ceará não tem

POR QUE ESTE SCRIPT EXISTE
--------------------------

Reynier & Rubin (2025, *PNAS* 122(3):e2413013121) usam o **PRISM** (Oregon State)
para medir a chuva mensal em grade e montar, com erodibilidade e aptidão GAEZ, o
potencial de escoamento do glifosato a montante. O PRISM só cobre os Estados
Unidos contíguos: **não existe PRISM para o Ceará**. O análogo funcional é o
**CHIRPS v2.0** (Funk et al. 2015, *Scientific Data* 2:150066,
doi:10.1038/sdata.2015.66): chuva mensal em grade de 0,05°, estação + satélite,
de 1981 até o presente, cobrindo 50°S–50°N.

No projeto a chuva tem três usos, em ordem de importância
(`docs/ars/20-material-drive-prism-chapada.md` §3):

1. **O pico do calendário deixa de ser hipótese fixa.** O desenho de calendário
   (`scripts/estimate/14_mde_calendario.py`, rotas R3/R4 do doc 19) usa fevereiro
   a maio como pico de aplicação, por analogia com Calzada et al. (2023): a
   fumigação de banana segue a sigatoka, que segue a chuva. Com a chuva medida, o
   pico vira dado por município e ano, e a seca de 2012–2017 deixa de ser
   ressalva verbal.
2. **Confundidor do próprio desfecho.** Rocha & Soares (2015, *J Dev Econ*
   112:72–91, doi:10.1016/j.jdeveco.2014.10.003) mostram, no semiárido e com o
   SINASC, que choque negativo de chuva na gestação reduz peso ao nascer e
   encurta a gestação. Se a chuva de 2019+ difere entre municípios com e sem
   avião, ela entra no hiato do calendário. Camacho & Mejía (2017) controlam
   chuva média mensal pelo mesmo motivo.
3. **Canal-água à la Reynier & Rubin.** Escoamento = chuva × erodibilidade ×
   aptidão. ⏸️ Suspenso junto com o SISAGUA (`17_audita_sisagua.py`).

FONTES
------

- Chuva: CHIRPS v2.0 mensal pelo **IRI Data Library** (Columbia), que recorta a
  caixa do Ceará no servidor e devolve NetCDF. Unidade: mm/mês. Tempo em "months
  since 1960-01-01", calendário 360. É o mesmo produto do servidor da UCSB
  (data.chc.ucsb.edu), sem baixar o globo inteiro.
- Malha: **API de malhas do IBGE** (servicodados.ibge.gov.br, v3), GeoJSON dos
  184 municípios, com verificação TLS normal. Preferida ao `geobr`, que baixa com
  TLS desativado (ver `16_fronteira_geografica.py`).

MÉTODO
------

Média ponderada pela área de interseção célula × município, com peso cos(lat)
para a área da célula. Células sem dado (mar) saem e o peso é renormalizado. O
script **falha** se algum município ficar com menos de 98% da área coberta pela
grade: caixa curta é erro silencioso de borda.

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não muda o pico do script 14.** Ele mede e reporta. Trocar `PICO` ou passar a
  um pico por município é mudança de pré-especificação e passa pelo orientador.
- **Não mede pulverização.** Chuva é deslocador da demanda de fungicida, não
  aplicação. A aplicação aérea medida continua dependendo do Pedido D ao MAPA.
- **Não substitui estação.** CHIRPS suaviza extremos locais; a FUNCEME tem rede
  pluviométrica densa no Ceará e é a validação natural, ainda não feita.
- **Não tem modo simulado.** Chuva simulada não é evidência.

Uso:
    python scripts/data_prep/18_chuva_chirps.py
    python scripts/data_prep/18_chuva_chirps.py --inicio 1991 --fim 2024
    python scripts/data_prep/18_chuva_chirps.py --netcdf caminho.nc --malha malha.json

Saídas (gitignored):
    data/raw/chirps/chirps_ce_{inicio}_{fim}.nc           cache do recorte
    data/raw/chirps/malha_ibge_ce.json                    cache da malha
    data/processed/chuva_chirps_ce_muni_mes.parquet       painel município × mês
    data/processed/chuva_chirps_ce_pico.csv               pico observado por ano
    data/processed/chuva_chirps_ce_proveniencia.json      vintage e URLs
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
RAW_DIR = RAIZ / "data" / "raw" / "chirps"
OUT_DIR = RAIZ / "data" / "processed"

# Caixa do Ceará com folga de ~0,1°: o estado vai de 41,42°W a 37,25°W e de
# 7,86°S a 2,78°S. A checagem de cobertura em `pesos_area` pega caixa curta.
CAIXA = {"x0": -41.55, "x1": -37.15, "y0": -8.05, "y1": -2.65}
RES = 0.05
COBERTURA_MINIMA = 0.98

URL_IRI = (
    "https://iridl.ldeo.columbia.edu/SOURCES/.UCSB/.CHIRPS/.v2p0/.monthly/.global/"
    ".precipitation/X/{x0}/{x1}/RANGEEDGES/Y/{y0}/{y1}/RANGEEDGES/"
    "T/(Jan%20{ini})/(Dec%20{fim})/RANGEEDGES/data.nc"
)
URL_MALHA = (
    "https://servicodados.ibge.gov.br/api/v3/malhas/estados/23"
    "?formato=application/vnd.geo%2Bjson&intrarregiao=municipio&qualidade=intermediaria"
)
URL_NOMES = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/23/municipios"

PICO_PADRAO = (2, 3, 4, 5)          # o PICO do Makefile (mde-calendario)
CLIMA_PADRAO = (1991, 2020)          # normal climatológica da OMM
CHAPADA = {                          # para o resumo impresso; não entra no painel
    "230760": "Limoeiro do Norte",
    "231150": "Quixeré",
    "231180": "Russas",
    "231310": "Tabuleiro do Norte",
    "230070": "Alto Santo",
}


# --------------------------------------------------------------------------
# tempo
# --------------------------------------------------------------------------

def decodifica_tempo_iri(t) -> tuple[np.ndarray, np.ndarray]:
    """'months since 1960-01-01' (calendário 360, ponto no meio do mês) → ano, mês."""
    m = np.floor(np.asarray(t, dtype=float)).astype(int)
    return 1960 + m // 12, m % 12 + 1


# --------------------------------------------------------------------------
# geometria
# --------------------------------------------------------------------------

def pesos_area(xs, ys, poligonos: dict, res: float = RES):
    """Matriz de pesos município × célula, por área de interseção × cos(lat).

    `xs`, `ys` são os centros da grade (1-D). `poligonos` mapeia código →
    geometria shapely em graus. Devolve (W, codigos, cobertura), com W de forma
    (n_muni, len(ys) * len(xs)) na ordem C de (Y, X), e cobertura = fração da área
    do município que caiu dentro da grade.
    """
    from shapely import STRtree, box

    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    gy, gx = np.meshgrid(ys, xs, indexing="ij")
    cy, cx = gy.ravel(), gx.ravel()
    h = res / 2
    celulas = [box(x - h, y - h, x + h, y + h) for x, y in zip(cx, cy)]
    arvore = STRtree(celulas)
    coslat = np.cos(np.deg2rad(cy))

    codigos = sorted(poligonos)
    W = np.zeros((len(codigos), cy.size))
    cobertura = np.zeros(len(codigos))
    for i, cod in enumerate(codigos):
        geo = poligonos[cod]
        idx = arvore.query(geo, predicate="intersects")
        if idx.size == 0:
            continue
        areas = np.array([celulas[j].intersection(geo).area for j in idx])
        W[i, idx] = areas * coslat[idx]
        cobertura[i] = areas.sum() / geo.area if geo.area > 0 else 0.0
    return W, codigos, cobertura


def agrega(P: np.ndarray, W: np.ndarray) -> np.ndarray:
    """P: (n_tempo, n_celulas) com NaN no mar. Devolve (n_tempo, n_muni)."""
    valido = np.isfinite(P)
    soma = np.where(valido, P, 0.0) @ W.T
    peso = valido.astype(float) @ W.T
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(peso > 0, soma / peso, np.nan)


# --------------------------------------------------------------------------
# painel e derivados
# --------------------------------------------------------------------------

def monta_painel(chuva: np.ndarray, anos, meses, codigos) -> pd.DataFrame:
    n_t, n_m = chuva.shape
    return pd.DataFrame({
        "cod_ibge7": np.tile(np.asarray(codigos, dtype=str), n_t),
        "ano": np.repeat(np.asarray(anos, int), n_m),
        "mes": np.repeat(np.asarray(meses, int), n_m),
        "chuva_mm": chuva.ravel(),
    }).assign(cod_ibge6=lambda d: d["cod_ibge7"].str[:6])[
        ["cod_ibge6", "cod_ibge7", "ano", "mes", "chuva_mm"]
    ]


def climatologia(painel: pd.DataFrame, inicio: int, fim: int) -> pd.DataFrame:
    """Acrescenta a normal do município-mês e a anomalia (mm e padronizada).

    A normal usa só os anos em [inicio, fim] que estiverem no painel; se nenhum
    estiver, as colunas saem NaN e o chamador avisa.
    """
    ref = painel[painel["ano"].between(inicio, fim)]
    norm = (ref.groupby(["cod_ibge6", "mes"])["chuva_mm"]
            .agg(clima_mm="mean", clima_dp="std").reset_index())
    out = painel.merge(norm, on=["cod_ibge6", "mes"], how="left")
    out["anomalia_mm"] = out["chuva_mm"] - out["clima_mm"]
    out["anomalia_z"] = out["anomalia_mm"] / out["clima_dp"].replace(0, np.nan)
    return out


def janela_de_pico(painel: pd.DataFrame, largura: int = 4,
                   fixo: tuple[int, ...] = PICO_PADRAO) -> pd.DataFrame:
    """Para cada município-ano, a janela de `largura` meses consecutivos mais
    chuvosa dentro do ano civil, e quanto da chuva anual cai nela e no pico fixo.
    """
    def _um(g: pd.DataFrame) -> pd.Series:
        v = g.set_index("mes")["chuva_mm"].reindex(range(1, 13)).to_numpy()
        total = np.nansum(v)
        somas = [np.nansum(v[i:i + largura]) for i in range(0, 13 - largura)]
        k = int(np.argmax(somas))
        return pd.Series({
            "chuva_anual_mm": total,
            "pico_inicio": k + 1,
            "pico_fim": k + largura,
            "frac_pico_obs": somas[k] / total if total > 0 else np.nan,
            "frac_pico_fixo": np.nansum(v[[m - 1 for m in fixo]]) / total if total > 0 else np.nan,
            "meses_completos": int(np.isfinite(v).sum()),
        })

    return (painel.groupby(["cod_ibge6", "ano"])[["mes", "chuva_mm"]]
            .apply(_um).reset_index())


# --------------------------------------------------------------------------
# E/S
# --------------------------------------------------------------------------

def baixa(url: str, destino: Path, timeout: int = 600) -> Path:
    import requests

    destino.parent.mkdir(parents=True, exist_ok=True)
    parte = destino.with_suffix(destino.suffix + ".parte")
    with requests.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with open(parte, "wb") as f:
            for bloco in r.iter_content(1 << 20):
                f.write(bloco)
    parte.replace(destino)
    return destino


def le_netcdf(caminho: Path):
    import xarray as xr

    ds = xr.open_dataset(caminho, decode_times=False)
    da = ds["precipitation"].transpose("T", "Y", "X")
    unid = da.attrs.get("units", "")
    if unid and unid != "mm/month":
        raise ValueError(f"unidade inesperada no CHIRPS: {unid!r} (esperado mm/month)")
    P = da.to_numpy().astype(float)
    P[P < 0] = np.nan                        # -9999 e afins
    anos, meses = decodifica_tempo_iri(ds["T"].to_numpy())
    return P.reshape(P.shape[0], -1), ds["X"].to_numpy(), ds["Y"].to_numpy(), anos, meses


def le_malha(caminho: Path) -> dict:
    from shapely.geometry import shape
    from shapely.validation import make_valid

    g = json.loads(Path(caminho).read_text(encoding="utf-8"))
    return {str(f["properties"]["codarea"]): make_valid(shape(f["geometry"]))
            for f in g["features"]}


def imprime_resumo(pico: pd.DataFrame, anos_janela=range(2015, 2025)) -> None:
    sub = pico[pico["ano"].isin(list(anos_janela))]
    estado = (sub.groupby("ano")
              .agg(chuva_anual_mm=("chuva_anual_mm", "median"),
                   frac_pico_fixo=("frac_pico_fixo", "median"),
                   frac_pico_obs=("frac_pico_obs", "median"),
                   pico_inicio_moda=("pico_inicio", lambda s: s.mode().iloc[0]),
                   pct_muni_pico_fev=("pico_inicio", lambda s: (s == 2).mean() * 100)))
    print("\nCeará, mediana dos 184 municípios por ano")
    print(estado.round(2).to_string())
    ch = sub[sub["cod_ibge6"].isin(CHAPADA)].assign(
        municipio=lambda d: d["cod_ibge6"].map(CHAPADA))
    if not ch.empty:
        print("\nChapada do Apodi e vizinhos: janela de 4 meses mais chuvosa (início) e fração no pico fixo fev–mai")
        print(ch.pivot(index="ano", columns="municipio", values="pico_inicio").to_string())
        print(ch.pivot(index="ano", columns="municipio", values="frac_pico_fixo").round(2).to_string())


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--inicio", type=int, default=1991)
    p.add_argument("--fim", type=int, default=2024)
    p.add_argument("--clima", type=int, nargs=2, default=list(CLIMA_PADRAO),
                   metavar=("INI", "FIM"), help="anos da normal climatológica")
    p.add_argument("--netcdf", type=Path, default=None, help="recorte CHIRPS local")
    p.add_argument("--malha", type=Path, default=None, help="GeoJSON municipal local")
    p.add_argument("--cache", type=Path, default=RAW_DIR)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if args.inicio > args.fim:
        print("ERRO: --inicio maior que --fim", file=sys.stderr)
        return 1

    prov = {"extraido_em": dt.date.today().isoformat(), "fonte": "CHIRPS v2.0 mensal",
            "caixa": CAIXA, "resolucao_graus": RES}
    nc = args.netcdf
    if nc is None:
        nc = args.cache / f"chirps_ce_{args.inicio}_{args.fim}.nc"
        url = URL_IRI.format(ini=args.inicio, fim=args.fim, **CAIXA)
        prov["url_chuva"] = url
        if not nc.exists():
            print(f"baixando CHIRPS {args.inicio}–{args.fim} (IRI) …")
            baixa(url, nc)
    else:
        prov["url_chuva"] = f"arquivo local: {nc}"
    malha = args.malha
    if malha is None:
        malha = args.cache / "malha_ibge_ce.json"
        prov["url_malha"] = URL_MALHA
        if not malha.exists():
            print("baixando malha municipal (IBGE) …")
            baixa(URL_MALHA, malha)
    else:
        prov["url_malha"] = f"arquivo local: {malha}"

    P, xs, ys, anos, meses = le_netcdf(nc)
    poligonos = le_malha(malha)
    W, codigos, cobertura = pesos_area(xs, ys, poligonos)
    curtos = [c for c, v in zip(codigos, cobertura) if v < COBERTURA_MINIMA]
    if curtos:
        print(f"ERRO: {len(curtos)} município(s) com menos de {COBERTURA_MINIMA:.0%} "
              f"da área dentro da grade (caixa curta?): {curtos[:10]}", file=sys.stderr)
        return 1

    chuva = agrega(P, W)
    painel = climatologia(monta_painel(chuva, anos, meses, codigos), *args.clima)
    if painel["clima_mm"].isna().all():
        print(f"⚠️ nenhum ano da normal {args.clima} está no recorte: anomalias saem NaN")
    faltas = int(painel["chuva_mm"].isna().sum())
    if faltas:
        print(f"⚠️ {faltas} município-mês sem chuva (todas as células NaN)")
    pico = janela_de_pico(painel)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    painel.to_parquet(args.out_dir / "chuva_chirps_ce_muni_mes.parquet", index=False)
    pico.to_csv(args.out_dir / "chuva_chirps_ce_pico.csv", index=False, encoding="utf-8")
    prov.update({"anos": [int(anos.min()), int(anos.max())], "n_meses": int(len(anos)),
                 "n_municipios": len(codigos), "cobertura_minima": float(cobertura.min()),
                 "normal_climatologica": args.clima})
    (args.out_dir / "chuva_chirps_ce_proveniencia.json").write_text(
        json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"painel: {len(codigos)} municípios × {len(anos)} meses "
          f"({anos.min()}–{anos.max()}), cobertura mínima {cobertura.min():.3f}")
    imprime_resumo(pico)
    return 0


if __name__ == "__main__":
    sys.exit(main())
