import sys
sys.dont_write_bytecode = True
import json, importlib.util, math, hashlib
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import norm, t as student

SRC=Path('C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa')
D=SRC/'data/processed'
OUT=Path(__file__).resolve().parent/'adendo_identificacao'
OUT.mkdir(exist_ok=True)
def module(name):
    spec=importlib.util.spec_from_file_location(name.replace('.','_'), SRC/'scripts/estimate'/name)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
m13=module('13_mde_desenhos.py'); m14=module('14_mde_calendario.py')
p=pd.read_parquet(D/'painel_ensaio1.parquet')
p['cod_ibge6']=p.cod_ibge6.astype(str)
units=p[['cod_ibge6','dose','dose_ha','aptidao_gaez']].drop_duplicates().set_index('cod_ibge6')
cut=units.aptidao_gaez.quantile(.75)
positive=set(units.index[units.dose>0]); zero=set(units.index[units.dose==0]); zero4=set(units.index[(units.dose==0)&(units.aptidao_gaez<=cut)])
top=set(units[units.dose_ha>0].nlargest(math.ceil(len(positive)*.1),'dose_ha').index)
def collapsed(data, outcome='peso_medio',post_start=2019*12+9,excluded_years=(),weighted=False,annual=False):
    x=data.copy(); x['tm']=x.ano*12+x.mes-1
    x=x[~x.ano.isin(excluded_years)]
    x['phase']=np.where(x.tm<=2018*12+11,'pre',np.where(x.tm>=post_start,'post','transition'))
    x=x[x.phase!='transition'].dropna(subset=[outcome])
    if weighted:
        x['sum']=x[outcome]*x.n_peso_valido
        z=x.groupby(['cod_ibge6','phase']).agg(sum=('sum','sum'),n=('n_peso_valido','sum'))
        z['y']=z['sum']/z.n
        z=z.y.unstack()
    elif annual:
        z=x.groupby(['cod_ibge6','phase','ano'])[outcome].mean().groupby(['cod_ibge6','phase']).mean().unstack()
    else: z=x.groupby(['cod_ibge6','phase'])[outcome].mean().unstack()
    z['dy']=z.post-z.pre
    return z.dropna()
def contrast(z,T,C,label):
    a=z.loc[sorted(T),'dy']; b=z.loc[sorted(C),'dy']; estimate=a.mean()-b.mean()
    v1=a.var(ddof=1)/len(a); v0=b.var(ddof=1)/len(b); se=np.sqrt(v1+v0)
    df=(v1+v0)**2/(v1**2/(len(a)-1)+v0**2/(len(b)-1))
    return dict(label=label,n_t=len(a),n_c=len(b),estimate=estimate,change_t=a.mean(),change_c=b.mean(),se_welch=se,df_welch=df,ci_normal_low=estimate-1.96*se,ci_normal_high=estimate+1.96*se,ci_welch_low=estimate-student.ppf(.975,df)*se,ci_welch_high=estimate+student.ppf(.975,df)*se)
rows=[]
for post,label,exc,weighted,annual in [(2019*12+9,'oct2019',(),False,False),(2019*12,'jan2019',(),False,False),(2019*12,'jan2019_year_means',(),False,True),(2019*12+9,'oct2019_no2020_21',(2020,2021),False,False),(2019*12+9,'oct2019_baby_weighted',(),True,False)]:
    z=collapsed(p,post_start=post,excluded_years=exc,weighted=weighted,annual=annual)
    for T,C,name in [(positive,zero,'positive_zero1'),(positive,zero4,'positive_zero4'),(top,zero4,'top_zero4')]: rows.append(contrast(z,T,C,label+'_'+name))
contrasts=pd.DataFrame(rows); contrasts.to_csv(OUT/'contrasts.csv',index=False)
summaries=[]
for f in sorted(D.glob('cgs_curva_*.csv')):
    q=pd.read_csv(f)
    summaries.append(dict(file=f.name,n=len(q),mean_est=q.estimativa.mean(),min_est=q.estimativa.min(),max_est=q.estimativa.max(),significant_negative=int((q.ic_sup<0).sum()),significant_positive=int((q.ic_inf>0).sum()),min_dose_significant=float(q.loc[q.ic_sup<0,'dose'].min()),max_dose_significant=float(q.loc[q.ic_sup<0,'dose'].max()),critical=q.valor_critico.iloc[0],unique_crit=q.valor_critico.nunique()))
pd.DataFrame(summaries).to_csv(OUT/'curves.csv',index=False)
# Fixed design contrasts in the pre-period. Use original functions read-only.
mde_rows=[]; calendar_rows=[]
censo=pd.read_csv(D/'censo_agro_equipamento_ce.csv',dtype={'cod_ibge6':str,'cod_ibge7':str})
aero=m13.com_aeronave(censo)
for filename in ['nascimentos_ce_muni_mes.parquet','nascimentos_ce_muni_mes__uf23-24.parquet']:
    births=pd.read_parquet(D/filename); births['cod_ibge6']=births.cod_ibge6.astype(str)
    for scope in (['all'] if 'uf23' not in filename else ['all','ce_only']):
        b=births if scope=='all' else births[births.cod_ibge6.str.startswith('23')]
        v=m13.variacao_placebo(b); sigma2=m13.variancia_individual(b); tau2=m13.heterogeneidade(v,sigma2)
        ce={x for x in v.index if x.startswith('23')}
        for T,C,name,vpp in [(top,zero4,'top_zero4',2/17),(top,zero,'top_zero1',2/17),(top,ce-top,'top_others',2/17),(positive,zero4,'positive_zero4',7/169),(positive,zero,'positive_zero1',7/169),(aero,ce-aero,'aero_ce_others',1)]:
            r=m13.avalia_desenho(name,T,C,v,sigma2,tau2,vpp)
            r.update(file=filename,scope=scope,sigma=math.sqrt(sigma2),tau=math.sqrt(tau2)); mde_rows.append(r)
        q=m14.compara(b,aero,(2,3,4,5)); q['file']=filename; q['scope']=scope; calendar_rows.append(q)
pd.DataFrame(mde_rows).to_csv(OUT/'mde_recomputed.csv',index=False)
pd.concat(calendar_rows).to_csv(OUT/'calendar_recomputed.csv',index=False)
# Exact simple monthly-mean weighting in a pre-period variance diagnostic,
# distinct from the birth-weighted 'por_unidade' model.
z=collapsed(p[p.ano<=2018],post_start=2017*12) if False else None
x=p[p.ano<=2018].copy(); x['half']=np.where(x.ano<=2016,'early','late')
z=x.groupby(['cod_ibge6','half']).peso_medio.mean().unstack(); z['dy']=z.late-z.early
sameweight=[]
for T,C,name in [(top,zero4,'top_zero4'),(positive,zero4,'positive_zero4'),(positive,zero,'positive_zero1')]:
    r=contrast(z,T,C,name); r['mde80_normal']=2.8*r['se_welch']; sameweight.append(r)
pd.DataFrame(sameweight).to_csv(OUT/'pre_variance_sameweights.csv',index=False)
metadata=dict(source=str(SRC),n_cells=len(p),n_units=p.cod_ibge6.nunique(),years=sorted(p.ano.unique().tolist()),births=int(p.n_nascimentos.sum()),cells_weight_missing=int(p.peso_medio.isna().sum()),gaez_p75=cut,excluded_zero=sorted(zero-zero4),n_t=len(positive),n_zero=len(zero),n_zero4=len(zero4),n_top=len(top),aero=sorted(aero),n_covid_cells=int(p.ano.isin([2020,2021]).sum()))
(OUT/'metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf8')
# Hash inputs, to make provenance reconstructable without copying source data.
inputs=['painel_ensaio1.parquet','nascimentos_ce_muni_mes.parquet','nascimentos_ce_muni_mes__uf23-24.parquet','censo_agro_equipamento_ce.csv','mde_desenhos.csv','mde_calendario.csv','robustez_inferencia.csv','holm_confirmatorios.csv']
(OUT/'input_sha256.json').write_text(json.dumps({n:hashlib.sha256((D/n).read_bytes()).hexdigest() for n in inputs},indent=2),encoding='utf8')
print(json.dumps(metadata,ensure_ascii=False,indent=2))
print(contrasts[['label','n_t','n_c','estimate','se_welch','ci_welch_low','ci_welch_high']].to_string(index=False))
print(pd.DataFrame(summaries).to_string(index=False))
print(pd.DataFrame(mde_rows)[['file','scope','desenho','g1','g0','mde_agrupado_g','mde_por_unidade_g','sigma','tau']].to_string(index=False))
print(pd.concat(calendar_rows)[['file','scope','desenho','g1','g0','mde_agrupado_g','mde_por_unidade_g','delta_minimo_f25_g','delta_minimo_f50_g']].to_string(index=False))
print(pd.DataFrame(sameweight)[['label','estimate','se_welch','mde80_normal']].to_string(index=False))
