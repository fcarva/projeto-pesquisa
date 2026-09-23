"""Read-only reanalysis of supplied municipal panels, with explicit estimands.

All new tests are audit diagnostics, not preregistered confirmatory results.
No source files are changed. No individual health records are exported.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import importlib.util
import json
import numpy as np
import pandas as pd
from scipy import stats

BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa')
OUT=BASE/'work/empirical'
OUT.mkdir(exist_ok=True)

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

rb=module('rb',REPO/'scripts/estimate/04_robustness.py')
sys.path.insert(0,str(REPO/'scripts/estimate'))
sp=module('sp',REPO/'scripts/estimate/10_spt_pretrend.py')
df=pd.read_parquet(REPO/'data/processed/painel_ensaio1.parquet')
df['t']=df.ano*12+df.mes-1
mun=df.drop_duplicates('cod_ibge6')
cut=mun.aptidao_gaez.quantile(.75)
suspect=set(mun.loc[mun.dose.eq(0)&mun.aptidao_gaez.gt(cut),'cod_ibge6'])
PRE=2018*12+11;POST=2019*12+9

def describe(d,with_resampling=False):
    y1=d.loc[d.dose.gt(0),'dy'].to_numpy();y0=d.loc[d.dose.eq(0),'dy'].to_numpy()
    n1,n0=len(y1),len(y0)
    assert n1>1 and n0>1 and np.isfinite(y1).all() and np.isfinite(y0).all()
    a=y1.var(ddof=1)/n1;b=y0.var(ddof=1)/n0
    se=np.sqrt(a+b);dof=(a+b)**2/(a*a/(n1-1)+b*b/(n0-1))
    estimate=y1.mean()-y0.mean();t=estimate/se
    crit=stats.t.ppf(.975,dof)
    row=dict(n_positive=n1,n_zero=n0,estimate=estimate,se_welch=se,df_welch=dof,
        ci95_welch_low=estimate-crit*se,ci95_welch_high=estimate+crit*se,
        p_two_sided_welch=2*stats.t.sf(abs(t),dof),
        p_weight_increase_welch=stats.t.sf(t,dof),
        p_fetal_decrease_welch=stats.t.cdf(t,dof),
        variance_share_controls=b/(a+b),ols_slope=rb.estima(d),
        change_positive=y1.mean(),change_zero=y0.mean())
    if with_resampling:
        r=rb.inferencia_nivel(d,n_boot=2000,seed=rb.SEED)
        row.update({f'original_method_{k}':v for k,v in r.items()})
    return row

def holm_fixed(ps):
    ps=np.asarray(ps,float)
    assert np.isfinite(ps).all() and np.logical_and(ps>=0,ps<=1).all()
    order=np.argsort(ps); adj=np.minimum(1,np.maximum.accumulate((len(ps)-np.arange(len(ps)))*ps[order]))
    out=np.empty(len(ps));out[order]=adj;return out

levels=[];placebos=[];jack=[]
for y in ['peso_medio','taxa_obito_fetal']:
    for zero in [1,4]:
        sample=df if zero==1 else df[~df.cod_ibge6.isin(suspect)]
        d=rb.primeira_diferenca(sample,y,PRE,POST)
        levels.append(dict(outcome=y,zero_definition=zero,**describe(d,True)))
        for code in d.loc[d.dose.eq(0),'cod_ibge6']:
            jack.append(dict(outcome=y,zero_definition=zero,omitted_control=str(code),
                estimate=rb.nivel(d[d.cod_ibge6.ne(code)])))
        true_pre=sample[sample.t.between(2015*12,PRE)]
        for a,b in sp.placebos(2015*12,PRE,POST-PRE,12):
            for kind,p in [('original_includes_2019_2022',sample),('corrected_pre_only',true_pre)]:
                d=rb.primeira_diferenca(p,y,a,b)
                n_post=int(p.t.ge(b).groupby(p.t).any().sum())
                n_after=int(p.loc[p.t.ge(b),'t'].ge(2019*12).sum())
                placebos.append(dict(outcome=y,zero_definition=zero,kind=kind,
                    pre_end=sp._rotulo(a),post_start=sp._rotulo(b),
                    post_end=sp._rotulo(int(p.t.max())),post_months=n_post,
                    post_cells_after_policy=n_after,**describe(d)))

lev=pd.DataFrame(levels)
for zero in [1,4]:
    ix=lev.index[lev.zero_definition.eq(zero)]
    lev.loc[ix,'p_two_sided_welch_holm_family2']=holm_fixed(lev.loc[ix,'p_two_sided_welch'])
    ps=[lev.loc[i,'p_weight_increase_welch' if lev.loc[i,'outcome']=='peso_medio' else 'p_fetal_decrease_welch'] for i in ix]
    lev.loc[ix,'p_directional_welch_holm_family2']=holm_fixed(ps)
lev.to_csv(OUT/'level-audit.csv',index=False)
pl=pd.DataFrame(placebos)
for (y,zero,kind),g in pl.groupby(['outcome','zero_definition','kind']):
    pl.loc[g.index,'p_two_sided_welch_holm_family3']=holm_fixed(g.p_two_sided_welch)
pl.to_csv(OUT/'placebo-leakage-audit.csv',index=False)
pd.DataFrame(jack).to_csv(OUT/'control-jackknife.csv',index=False)
print(lev[['outcome','zero_definition','estimate','ci95_welch_low','ci95_welch_high','p_two_sided_welch','p_two_sided_welch_holm_family2','p_directional_welch_holm_family2','variance_share_controls']].to_string(index=False))
print(pl[pl.outcome.eq('peso_medio')&pl.zero_definition.eq(4)][['kind','pre_end','post_start','post_end','post_months','estimate','ols_slope','p_two_sided_welch','p_two_sided_welch_holm_family3']].to_string(index=False))
