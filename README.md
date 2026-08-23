# Aerial Pesticide Spraying as a Negative Externality: Causal Evidence and Instrument Choice from Ceará, Brazil

Master's dissertation (PPGEco/UFES). Two essays evaluating Ceará's 2019 statewide ban on aerial pesticide spraying — *Lei Zé Maria do Tomé*, State Law 16.820/2019.

## Research design

**Essay 1 — Causal impact evaluation.** Effect of the ban on birth outcomes (SINASC) and, as a channel, drinking-water quality (SISAGUA).

**Essay 2 — Instrument choice.** Prohibition vs. taxation vs. buffer zones, under Weitzman (1974) prices-vs-quantities, anchored to the dose–response curve estimated in Essay 1.

## Identification

- **Target parameter:** dose–response ATT — how the ban's effect varies with pre-ban aerial-spraying intensity across municipalities. Treatment is *continuous* (a dose), not binary.
- **Primary estimator:** Callaway, Goodman-Bacon & Sant'Anna (2024) continuous-treatment DiD. The ban is statewide and simultaneous, so identification comes from cross-municipal *dose* variation, not treatment *timing* — staggered-DiD estimators are therefore not the primary tool.
- **Exposure instrument:** FAO-GAEZ agro-climatic suitability, following Reynier & Rubin (2025, *PNAS*) and Dias, Rocha & Soares (2023, *ReStud*).
- **Water channel:** within-watershed upstream/downstream DiD (ANA basins), DRS (2023) template.
- **Robustness:** synthetic DiD (Arkhangelsky et al. 2021); PSM+DiD; small-cluster inference via Conley–Taber (2011) / wild-cluster bootstrap.

## Data

SINASC, SIM (DATASUS); SISAGUA (Ministério da Saúde); PAM (IBGE); FAO-GAEZ; ANA watershed shapefiles; IBAMA pesticide sales. **Individual-level microdata are never committed to this repository.**

## Stack

Python-first (pandas, pyfixest, sidrapy, pysus, geopandas) with R for the continuous-treatment estimator (`contdid` / `did`). The language boundary is file I/O (parquet/CSV) for reproducibility.

## Repository structure

```
tese-agrotoxicos-ceara/
├── data/          # raw / processed / geo — microdata gitignored, never committed
├── notebooks/     # exploratory analysis
├── scripts/       # numbered pipeline: data_prep → build_panel → estimate → figures
├── paper/         # LaTeX manuscript, tables, figures
└── docs/          # legislation (Law 16.820/2019, ADI 6137, Law 19.135/2024, ADI 7794), notes
```

## Reproducibility

`requirements.txt` (Python) + `renv.lock` (R); fixed seeds; documented data vintages. Run `bash setup.sh` to scaffold the tree, `.gitignore`, and environments.

## Key references

Callaway, Goodman-Bacon & Sant'Anna (2024, NBER WP 32117); Dias, Rocha & Soares (2023, *Review of Economic Studies* 90(6):2943–2981); Reynier & Rubin (2025, *PNAS* 122(3):e2413013121); Camacho & Mejía (2017, *Journal of Health Economics* 54); Weitzman (1974, *Review of Economic Studies* 41(4)); Lichtenberg, Parker & Zilberman (1988, *American Journal of Agricultural Economics* 70(4)). Full reading list in `docs/`.

## License

Code: MIT. Text, tables, and figures: © the author, all rights reserved. *(Adjust to your preference before making the repo public.)*
