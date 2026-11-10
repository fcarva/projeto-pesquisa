"""Estilo e utilitários comuns das figuras (scripts/figures/).

Não é passo de pipeline: é importado pelos scripts numerados. Um matiz
sequencial para magnitude, tinta neutra para texto, laranja reservado para
"aeronave" e vermelho para "ban/divisa" — as mesmas cores do mapa F01.
"""

from __future__ import annotations

import importlib.util
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PROCESSED = RAIZ / "data" / "processed"
FIG_DIR = RAIZ / "paper" / "figures"

TINTA = "#1a1a1a"
CINZA = "#6b6b6b"
GRADE = "#e3e3e3"
AZUL = "#1f5fa8"        # grupo tratado / dose alta
AZUL_CLARO = "#9cc3e4"  # demais produtores
NEUTRO = "#9a9a9a"      # d = 0 / comparação
LARANJA = "#e07b00"     # aeronave (Censo Agro 2006)
VERMELHO = "#b3261e"    # ban / divisa

UF_CE = "23"


def aplica_estilo():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 8.5,
        "axes.edgecolor": NEUTRO, "axes.linewidth": 0.6,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.titlesize": 10, "axes.titlelocation": "left",
        "axes.labelcolor": TINTA, "text.color": TINTA,
        "xtick.color": CINZA, "ytick.color": CINZA,
        "xtick.major.size": 2.5, "ytick.major.size": 2.5,
        "grid.color": GRADE, "grid.linewidth": 0.6,
        "legend.frameon": False,
    })
    return plt


def carrega_script(relativo: str):
    """Scripts numerados não são importáveis por nome; mesmo padrão dos testes."""
    caminho = RAIZ / "scripts" / relativo
    spec = importlib.util.spec_from_file_location("_" + caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def slug(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-")


def rotulo_unico(culturas, pedido: str) -> str:
    """O rótulo da PAM que casa com `pedido`. Zero ou 2+ casamentos é erro."""
    casam = sorted({c for c in culturas if pedido.lower() in c.lower()})
    if len(casam) != 1:
        raise ValueError(f"--cultura {pedido!r} casa com {casam or 'nenhum rótulo'}; "
                         f"disponíveis: {sorted(set(culturas))}")
    return casam[0]


def pam_real(explicito: Path | None = None) -> Path:
    """PAM município×cultura REAL (script 01). Recusa simulado."""
    candidatos = [explicito] if explicito else [
        PROCESSED / "pam_ce_muni_cultura_media__sidra.parquet",
        PROCESSED / "pam_ce_muni_cultura_media__sidra__uf23-24.parquet"]
    for arq in candidatos:
        if arq.exists():
            if "simulado" in arq.name:
                raise FileNotFoundError(f"{arq.name} é SIMULADO: não vira figura do paper.")
            return arq
    raise FileNotFoundError(
        "PAM real não encontrado em data/processed/. Rode antes:\n"
        "  python scripts/data_prep/01_check_dose_variation.py --fonte sidra --ufs 23 24")


def so_ceara(pam):
    return pam[pam["cod_ibge"].astype(str).str.startswith(UF_CE)].copy()


def decil_superior(pam_ce, rotulo: str) -> set[str]:
    """Mesma conta dos estimadores 07/08, via script 16 (que casa por regex)."""
    f16 = carrega_script("data_prep/16_fronteira_geografica.py")
    return f16.decil_superior(pam_ce, re.escape(rotulo))


def nomes_municipios() -> dict[str, str]:
    """cod7 → nome, da malha em cache (data/geo/). Vazio se não houver malha."""
    arq = RAIZ / "data" / "geo" / "municipalities_2022_simplified.parquet"
    if not arq.exists():
        return {}
    import pandas as pd

    m = pd.read_parquet(arq, columns=["code_muni", "name_muni"])
    return dict(zip(m["code_muni"].astype("int64").astype(str), m["name_muni"]))


def grava(fig, nome: str, out_dir: Path = FIG_DIR, dpi: int = 300) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        destino = out_dir / f"{nome}.{ext}"
        fig.savefig(destino, dpi=dpi)
        print(f"gravado: {destino}")
