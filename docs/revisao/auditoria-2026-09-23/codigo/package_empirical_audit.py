"""Package only reviewable reports, aggregate outputs, logs and code; no data panels."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, zipfile
import pandas as pd
import numpy as np
import scipy

B=Path(__file__).resolve().parents[1];O=B/'outputs';W=B/'work/empirical'
R=Path('C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa')
clone=B/'work/projeto-pesquisa'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

patch=subprocess.check_output(['git','-C',str(clone),'diff','--no-ext-diff','--','scripts/estimate/10_spt_pretrend.py']).decode('utf-8')
test=clone/'tests/test_pretrend_window.py';lines=test.read_text(encoding='utf-8').splitlines(keepends=True)
patch+='diff --git a/tests/test_pretrend_window.py b/tests/test_pretrend_window.py\nnew file mode 100644\n--- /dev/null\n+++ b/tests/test_pretrend_window.py\n@@ -0,0 +1,%d @@\n'%len(lines)
patch+=''.join('+'+x for x in lines)
(O/'correcao-placebos-pre-periodo.patch').write_text(patch,encoding='utf-8',newline='\n')

input_audit=json.loads((O/'integridade-paineis-agregados.json').read_text(encoding='utf-8'))
source_checks={name:{'sha256_before':v['sha256'],'sha256_after':sha(R/'data/processed'/name)} for name,v in input_audit['files'].items()}
assert all(v['sha256_before']==v['sha256_after'] for v in source_checks.values())
assert '276 passed' in (W/'full-tests-after.log').read_text(encoding='utf-8-sig')
scripts=['audita_paineis_local.py','audit_existing_results.py','empirical_audit.py','check_empirical_outputs.py','compare_versions.py','check_replication_env.R','run_original_contdid.R','run_original_sensitivity.R','package_empirical_audit.py']
commands=[
    'python -B work/audita_paineis_local.py',
    'python -B work/audit_existing_results.py',
    'python -B work/empirical_audit.py',
    'python -B work/check_empirical_outputs.py',
    'python -B SOURCE/scripts/estimate/04_robustness.py --painel PANEL --desfecho peso_medio --out-dir work/empirical/robustness-peso-original',
    'python -B SOURCE/scripts/estimate/09_holm.py --painel PANEL --out-dir work/empirical/holm-original',
    'python -B SOURCE/scripts/estimate/10_spt_pretrend.py --painel PANEL --out-dir work/empirical/spt-original',
    'Rscript --vanilla work/run_original_contdid.R --painel PANEL --desfecho peso_medio --d-zero 4 --saida work/empirical/cgs-peso-d4-original',
    'Rscript --vanilla work/run_original_contdid.R --painel PANEL --desfecho taxa_obito_fetal --d-zero 4 --saida work/empirical/cgs-fetal-d4-original',
    'AUDIT_R_TARGET=07_honestdid.R; Rscript --vanilla work/run_original_sensitivity.R --painel PANEL --saida work/empirical/honest-original',
    'AUDIT_R_TARGET=08_synthdid.R; Rscript --vanilla work/run_original_sensitivity.R --painel PANEL --saida work/empirical/synth-original',
    'python -B work/projeto-pesquisa/scripts/estimate/10_spt_pretrend.py --painel PANEL --out-dir work/empirical/spt-corrected',
    'python -B work/projeto-pesquisa/scripts/estimate/10_spt_pretrend.py --painel PANEL --desfecho taxa_obito_fetal --out-dir work/empirical/spt-corrected',
    'python -B -m pytest tests/test_data_prep.py tests/test_pretrend_window.py -q --disable-warnings --maxfail=3 --basetemp WORKSPACE/work/placebo-tests-complete',
]
manifest={
 'created_utc':datetime.now(timezone.utc).isoformat(),
 'source_repository':str(R),'source_HEAD':'4ab2c93971fa64d03393405428f6518950c9dada',
 'audited_clone_HEAD':'8d3a31ea2680e530d4ea3cee6134531be0d853fe',
 'SOURCE':str(R),'PANEL':str(R/'data/processed/painel_ensaio1.parquet'), 'WORKSPACE':str(B),
 'original_data_unchanged_sha256':source_checks,
 'python':sys.version,'numpy':np.__version__,'pandas':pd.__version__,'scipy':scipy.__version__,
 'R':{'version':'4.6.1','path':'C:/Program Files/R/R-4.6.1/bin/Rscript.exe',
      'library':str(R/'renv/library/windows/R-4.6/x86_64-w64-mingw32'),
      'contdid':'0.1.1','contdid_sha':'5cfec81a82fc8cfeffb6b7b822a0eded5deafc91',
      'ptetools':'1.0.2','ptetools_sha':'bda4aa51fae7721d34f2e5111ecff8e130d8babe',
      'npiv':'0.1.3','HonestDiD':'0.2.8','HonestDiD_sha':'6813f02ed38f0b63bdca6915604b2eac90491303',
      'synthdid':'0.0.9','synthdid_sha':'70c1ce3eac58e28c30b67435ca377bb48baa9b8a'},
 'seed':20190613,'original_python_bootstrap_repetitions':2000,'original_contdid_biters':1000,
 'new_inference_status':'exploratory audit diagnostics, not retrospective preregistration',
 'commands_readable_templates':commands,
 'powershell_environment_note':'Set AUDIT_R_TARGET with $env:AUDIT_R_TARGET; commands execute from WORKSPACE except pytest from work/projeto-pesquisa. Use python -B and Rscript --vanilla.',
 'tests':{'original_regressions':'2 expected failures when outcomes outside pre-window are perturbed','patched_regressions':'2 passed','full_suite':'276 passed, 2 warnings in 70.37s','diff_check':'passed'},
 'limitations':['No causal identification is established by numeric reproduction.',
  'Fetal curve estimates and standard errors reproduced; historical bootstrap critical values did not.',
  'Raw individual health records were not reprocessed.',
  'SIH coverage must be resolved before replacing absent cells with zero.',
  'Scripts use the user-provided local path; original data and R library are required for reruns.'],
 'patch_sha256':sha(O/'correcao-placebos-pre-periodo.patch'),
 'report_sha256':{p.name:sha(p) for p in O.glob('*.md')},
}
(O/'manifesto-reproducao-empirica.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

selected=[p for p in O.iterdir() if p.is_file() and p.suffix in ['.md','.json','.patch']]
selected += [B/'work'/s for s in scripts]
selected += [p for p in W.rglob('*') if p.is_file() and p.suffix in ['.csv','.json','.log']]
selected += [p for p in (B/'work/adendo_identificacao').glob('*') if p.is_file() and p.suffix in ['.csv','.json']]
selected += [clone/'scripts/estimate/10_spt_pretrend.py',clone/'scripts/estimate/04_robustness.py',test]
assert all(p.suffix.lower() not in ['.parquet','.dbc','.dbf'] for p in selected)
zip_path=O/'auditoria-completa-com-paineis-2026-09-23.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(set(selected)):
        z.write(p,arcname=p.relative_to(B).as_posix())
with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    count=len(z.namelist())
print(json.dumps({'archive':str(zip_path),'files':count,'bytes':zip_path.stat().st_size,'sha256':sha(zip_path)},indent=2))
