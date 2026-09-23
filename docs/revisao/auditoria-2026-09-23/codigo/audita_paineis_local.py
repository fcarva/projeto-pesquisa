import sys
sys.dont_write_bytecode = True
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import pandas as pd

ROOT = Path('C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa')
OUT = Path(__file__).resolve().parents[1] / 'outputs'
DATA = ROOT/'data/processed'
KEY = ['cod_ibge6','ano','mes']

def native(v):
    if isinstance(v, dict): return {str(k):native(x) for k,x in v.items()}
    if isinstance(v, (list,tuple)): return [native(x) for x in v]
    if isinstance(v,np.generic): v=v.item()
    if isinstance(v,float) and not np.isfinite(v): return None
    if isinstance(v,(pd.Timestamp,datetime)): return v.isoformat()
    return v

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def load(name):
    df=pd.read_parquet(DATA/name)
    if 'cod_ibge6' in df: df['cod_ibge6']=df.cod_ibge6.astype(str)
    return df

def overview(name,df):
    key=[x for x in KEY if x in df]
    if 'cultura' in df: key.append('cultura')
    out={'file':name,'sha256':sha(DATA/name),'bytes':(DATA/name).stat().st_size,
      'mtime_utc':datetime.fromtimestamp((DATA/name).stat().st_mtime,timezone.utc).isoformat(),
      'rows':len(df),'columns':df.columns.tolist(),'key':key,
      'duplicate_key_rows':int(df.duplicated(key,keep=False).sum()) if key else None,
      'municipalities':int(df.cod_ibge6.nunique()) if 'cod_ibge6' in df else None,
      'sources':df.fonte.value_counts(dropna=False).to_dict() if 'fonte' in df else None,
      'missing':df.isna().sum().to_dict()}
    if 'ano' in df:
        yearly=[]
        for y,g in df.groupby('ano'):
            e={'year':y,'rows':len(g),'municipalities':g.cod_ibge6.nunique(),
               'missing':g.isna().sum().to_dict()}
            if 'mes' in g: e['months']=sorted(g.mes.unique().tolist())
            e['sources']=g.fonte.value_counts(dropna=False).to_dict() if 'fonte' in g else None
            e['count_totals']={c:g[c].sum(min_count=1) for c in g if c.startswith(('n_','sinan_n_')) and pd.api.types.is_numeric_dtype(g[c])}
            for c in ['peso_medio','taxa_obito_fetal','taxa_obito_fetal_22sem']:
                if c in g: e[c]={'mean':g[c].mean(),'zero_cells':int(g[c].eq(0).sum()),'nonmissing':int(g[c].notna().sum())}
            yearly.append(e)
        out['yearly']=yearly
    return out

def compare(a,b,key=KEY,cols=None):
    if a.duplicated(key).any() or b.duplicated(key).any(): return {'error':'duplicate_keys'}
    aa=a.set_index(key);bb=b.set_index(key)
    out={'left_only_keys':len(aa.index.difference(bb.index)),'right_only_keys':len(bb.index.difference(aa.index))}
    common=aa.index.intersection(bb.index);aa=aa.loc[common];bb=bb.loc[common]
    out['common_keys']=len(common);out['columns']={}
    for c in (cols or sorted(set(aa)&set(bb))):
        x,y=aa[c],bb[c]
        both=x.notna()&y.notna();missing_diff=x.isna()^y.isna()
        if pd.api.types.is_numeric_dtype(x) and pd.api.types.is_numeric_dtype(y):
            delta=(x[both].astype(float)-y[both].astype(float)).abs()
            neq=~np.isclose(x[both].astype(float),y[both].astype(float),rtol=1e-10,atol=1e-10)
            n=int(neq.sum());maximum=delta.max() if len(delta) else None
        else:
            n=int((x[both].astype(str)!=y[both].astype(str)).sum());maximum=None
        out['columns'][c]={'both_present':int(both.sum()),'different_values':n,'missing_disagreement':int(missing_diff.sum()),'max_abs_difference':maximum}
    return out

names=['painel_ensaio1.parquet','painel_ensaio1__simulado.parquet',
'nascimentos_ce_muni_mes.parquet','obitos_fetais_ce_muni_mes.parquet',
'intoxicacao_ce_muni_mes.parquet','sinan_iexo_ce_muni_mes.parquet',
'pam_ce_muni_cultura_media__sidra.parquet','gaez_aptidao_muni.parquet',
'populacao_ce_muni_ano.parquet']
frames={n:load(n) for n in names}
result={'audited_at':datetime.now(timezone.utc).isoformat(),'source_root':str(ROOT),
'head':'4ab2c93971fa64d03393405428f6518950c9dada',
'files':{n:overview(n,f) for n,f in frames.items()},'comparisons':{}}
panel=frames[names[0]]
spec=importlib.util.spec_from_file_location('audited_panel',ROOT/'scripts/build_panel/05_build_panel.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
with contextlib.redirect_stdout(io.StringIO()) as capture:
    rebuilt=module.monta_painel(frames[names[6]],'Banana (cacho)',frames[names[2]],
      frames[names[3]],frames[names[4]],sinan=frames[names[5]],
      populacao=module.carrega_populacao(DATA,'real'),gaez=module.carrega_gaez(DATA),
      bans=module.carrega_bans_municipais(ROOT/'docs/legislacao/bans-municipais-ce.csv'))
rebuilt['fonte']='real'
result['rebuild_messages']=capture.getvalue()
result['comparisons']['stored_vs_rebuilt']=compare(panel,rebuilt)
result['rebuilt_shape']=rebuilt.shape
result['rebuilt_extra_columns']=sorted(set(rebuilt)-set(panel))
result['stored_extra_columns']=sorted(set(panel)-set(rebuilt))
result['comparisons']['stored_vs_rebuilt_by_year']={str(y):compare(g,rebuilt[rebuilt.ano==y]) for y,g in panel.groupby('ano')}
result['comparisons']['stored_vs_simulated']=compare(panel,frames[names[1]],cols=['peso_medio','n_nascimentos','taxa_obito_fetal','dose','aptidao_gaez','sinan_n_agricola','n_acidental'])
for file in DATA.glob('nascimentos_ce_muni_mes__uf*.parquet'):
    f=load(file.name);f=f[f.cod_ibge6.str.startswith('23')]
    result['files'][file.name]=overview(file.name,load(file.name))
    result['comparisons'][f'SINASC_canonical_vs_{file.name}']=compare(frames[names[2]],f)

fetal=frames[names[3]]
birth=frames[names[2]]
cohort=fetal[['cod_ibge6','ano','mes','n_nascimentos','n_obito_fetal','coorte_registrada','taxa_obito_fetal','sem_denominador']].merge(birth[KEY+['n_nascimentos']],on=KEY,how='outer',suffixes=('_fetal','_sinasc'),indicator=True)
result['fetal_denominator']={'key_merge':cohort['_merge'].value_counts().to_dict(),
'nasc_different':int((cohort.n_nascimentos_fetal.ne(cohort.n_nascimentos_sinasc)&cohort.n_nascimentos_fetal.notna()&cohort.n_nascimentos_sinasc.notna()).sum()),
'sem_denominador_true':int(fetal.sem_denominador.sum()),
'rate_one_cells':int(fetal.taxa_obito_fetal.eq(1).sum()),
'years_fetal':sorted(fetal.ano.unique().tolist()),'years_birth':sorted(birth.ano.unique().tolist()),
'cohort_identity_failures':int((fetal.coorte_registrada!=fetal.n_nascimentos+fetal.n_obito_fetal).sum()),
'rate_identity_failures':int((~np.isclose(fetal.taxa_obito_fetal,fetal.n_obito_fetal/fetal.coorte_registrada,equal_nan=True)).sum())}
raws=list((ROOT/'data/raw').rglob('DOFET*'))
result['raw_fetal_inventory']=[{'relative_path':str(p.relative_to(ROOT)), 'bytes':p.stat().st_size,'sha256':sha(p)} for p in raws if p.is_file()]
result['code_hashes']={str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'scripts/build_panel/05_build_panel.py',ROOT/'scripts/data_prep/03_clean_fetal_deaths.py',ROOT/'CLAUDE.md',ROOT/'docs/legislacao/bans-municipais-ce.csv']}

mu=panel.drop_duplicates('cod_ibge6');cut=mu.aptidao_gaez.quantile(.75)
result['panel_design']={'zero_count':int(mu.dose.eq(0).sum()),'positive_count':int(mu.dose.gt(0).sum()),
'gaez_p75':cut,'definition4_controls':int((mu.dose.eq(0)&mu.aptidao_gaez.le(cut)).sum()),
'gaez_missing_municipalities':int(mu.aptidao_gaez.isna().sum()),
'dose_time_varying_municipalities':int(panel.groupby('cod_ibge6').dose.nunique().gt(1).sum()),
'cultures':panel.cultura_ancora.value_counts().to_dict()}
OUT.mkdir(exist_ok=True)
dest=OUT/'integridade-paineis-agregados.json'
dest.write_text(json.dumps(native(result),ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
changed={c:v for c,v in result['comparisons']['stored_vs_rebuilt']['columns'].items() if v['different_values'] or v['missing_disagreement']}
print(json.dumps(native({'json':str(dest),'changed_columns':changed,'design':result['panel_design'],'fetal':result['fetal_denominator']}),ensure_ascii=False,indent=2))
