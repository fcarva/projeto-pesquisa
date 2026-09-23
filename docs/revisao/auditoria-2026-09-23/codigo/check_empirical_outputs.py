from pathlib import Path
import json, hashlib, re, subprocess
import numpy as np
import pandas as pd

BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa')
W=BASE/'work/empirical';D=REPO/'data/processed'
rows=[]
for folder in ['cgs-peso-d4-original','cgs-fetal-d4-original','holm-original','robustness-peso-original','synth-original','honest-original','spt-original']:
    for p in sorted((W/folder).glob('*.csv')):
        q=D/p.name
        if not q.exists(): continue
        a=pd.read_csv(p);b=pd.read_csv(q)
        info={'file':p.name,'run':folder,'rows_rerun':len(a),'rows_saved':len(b),
            'rerun_only_columns':sorted(set(a)-set(b)), 'saved_only_columns':sorted(set(b)-set(a)),
            'different_columns':{}}
        if len(a)==len(b):
            for c in sorted(set(a)&set(b)):
                if pd.api.types.is_numeric_dtype(a[c]) and pd.api.types.is_numeric_dtype(b[c]):
                    ok=np.isclose(a[c],b[c],rtol=1e-8,atol=1e-10,equal_nan=True)
                    if not ok.all(): info['different_columns'][c]={'count':int((~ok).sum()),'max_abs':float((a[c]-b[c]).abs().max())}
                else:
                    diff=a[c].fillna('<NA>').astype(str).ne(b[c].fillna('<NA>').astype(str))
                    if diff.any(): info['different_columns'][c]={'count':int(diff.sum())}
        rows.append(info)

df=pd.read_parquet(D/'painel_ensaio1.parquet')
df['t']=df.ano*12+df.mes-1
mu=df.drop_duplicates('cod_ibge6');cut=mu.aptidao_gaez.quantile(.75)
exclude=set(mu.loc[mu.dose.eq(0)&mu.aptidao_gaez.gt(cut),'cod_ibge6'])
sub=df[~df.cod_ibge6.isin(exclude)]
channels=[]
for c in ['peso_medio','taxa_baixo_peso','taxa_prematuridade','taxa_obito_fetal','taxa_obito_fetal_22sem','taxa_sih_acidental_100k','taxa_sih_t60_100k','taxa_sinan_agricola_100k','taxa_sinan_agricola_nao_intencional_100k']:
    pre=sub.loc[sub.t.le(2018*12+11)].groupby('cod_ibge6')[c].mean()
    post=sub.loc[sub.t.ge(2019*12+9)].groupby('cod_ibge6')[c].mean()
    dd=pd.DataFrame({'pre':pre,'post':post}).dropna();dd['dy']=dd.post-dd.pre
    dd['dose']=sub.groupby('cod_ibge6').dose.first()
    channels.append({'outcome':c,'nonmissing_cells':int(df[c].notna().sum()),
        'missing_cells':int(df[c].isna().sum()),'zero_cells':int(df[c].eq(0).sum()),
        'paired_positive_d4':int(dd.dose.gt(0).sum()),'paired_controls_d4':int(dd.dose.eq(0).sum())})

raw=list((REPO/'data/raw/sih').rglob('*'))
rd=[p for p in raw if p.is_file() and re.fullmatch(r'RDCE\d{4}\.dbc',p.name,re.I)]
found={p.name.upper() for p in rd};expected={f'RDCE{y%100:02d}{m:02d}.DBC' for y in range(2015,2023) for m in range(1,13)}
inventory={'rd_files':len(rd),'expected_2015_2022':96,'missing_expected':sorted(expected-found),
    'empty_files':[p.name for p in rd if p.stat().st_size==0],
    'processed_sih_rows':len(pd.read_parquet(D/'intoxicacao_ce_muni_mes.parquet'))}
fetal=df[df.sem_denominador.eq(True)]
fetal_info={'cells_flagged':len(fetal),'years':fetal.ano.tolist(),
    'groups':['positive' if x>0 else 'zero' for x in fetal.dose],
    'rates':fetal.taxa_obito_fetal.tolist(),
    'n_fetal':float(fetal.n_obito_fetal.sum())}
version=json.loads((W/'code-comparison.json').read_text())
for r in version:
    p=REPO/r['path'];q=BASE/'work/projeto-pesquisa'/r['path']
    old=subprocess.run(['git','-C',str(BASE/'work/projeto-pesquisa'),'show','HEAD:'+r['path']],capture_output=True)
    r['same_text_normalized_newlines_at_audited_HEAD']=old.returncode==0 and p.read_text(encoding='utf-8-sig')==old.stdout.decode('utf-8-sig').replace('\r\n','\n')

out={'csv_comparisons':rows,'channels':channels,'sih_inventory':inventory,
     'fetal_denominator_flag':fetal_info,'code_version_comparison':version,
     'notes':['CSV equality tolerances rtol=1e-8, atol=1e-10.',
     'Presence of SIH monthly files is not validation of all admission-date coverage or source completeness.']}
def clean(x):
    if isinstance(x,dict): return {k:clean(v) for k,v in x.items()}
    if isinstance(x,list): return [clean(v) for v in x]
    if isinstance(x,float) and not np.isfinite(x): return None
    return x
out=clean(out)
(BASE/'outputs/reproducao-empirica-diagnosticos.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['code_version_comparison']},ensure_ascii=False,indent=2))
