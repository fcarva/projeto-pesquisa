import numpy as np, itertools
rng=np.random.default_rng(0)
M=8; A=np.array([1,1,1,0,0,0,0,0])
season={2,3,4,5}
rows=[]
for m in range(M):
    for y in range(2005,2025):
        for mo in range(1,13):
            t=y*12+(mo-1)            # birth month index
            conc=t-9                 # conception month index (gestation months conc..t-1)
            gest=[conc+k for k in range(9)]
            first6=gest[:6]
            P=sum(((g%12)+1) in season for g in first6)/6
            gy=[g//12 for g in gest]
            ref = min(gy)>=2007 and max(gy)<=2011
            seca= min(gy)>=2012 and max(gy)<=2018
            pos = conc> 2019*12+0    # conceived Feb 2019 or later (fully after 9 Jan 2019)
            rows.append((m,y,mo,t,P,ref,seca,pos))
import pandas as pd
d=pd.DataFrame(rows,columns="m y mo t P ref seca pos".split())
d["A"]=A[d.m]
def rank_check(d,label):
    def dummies(keys):
        g=d.groupby(keys).ngroup().values
        X=np.zeros((len(d),g.max()+1)); X[np.arange(len(d)),g]=1; return X
    FE=np.hstack([dummies(["m","mo"]),dummies(["m","y"]),dummies(["t"])])
    r0=np.linalg.matrix_rank(FE)
    out={}
    for name,v in {"A*Seca":d.A*d.seca,"A*Pos":d.A*d.pos,"A*P":d.A*d.P,"A*P*Seca":d.A*d.P*d.seca,"A*P*Pos":d.A*d.P*d.pos}.items():
        out[name]= np.linalg.matrix_rank(np.hstack([FE,v.values[:,None]]))-r0
    both=np.linalg.matrix_rank(np.hstack([FE,(d.A*d.P*d.seca).values[:,None],(d.A*d.P*d.pos).values[:,None]]))-r0
    print(label,"| extra rank (0=absorbed):",out,"| betaS,beta jointly identified:",both==2, "| n",len(d))
print("P support:",sorted(d.P.round(3).unique()))
rank_check(d,"full panel 2005-2024, periods by gestation, FE by birth year")
d2=d[d.ref|d.seca|d.pos]
rank_check(d2,"only cohorts wholly in ref/seca/pos (transition + 2005-06 dropped)")
print("omitted-category cohorts in full panel (not seca, not pos):", d[(~d.seca)&(~d.pos)&(d.m==0)].groupby("y").size().to_dict())
print("ref cohorts by birth year:", d[d.ref&(d.m==0)].groupby("y").size().to_dict())
print("within-year variation of seca / pos by birth year (m=0):", {y:(g.seca.nunique(),g.pos.nunique()) for y,g in d[d.m==0].groupby("y") if g.seca.nunique()>1 or g.pos.nunique()>1})
print("in dropped sample:", {y:(g.seca.nunique(),g.pos.nunique(),g.ref.nunique()) for y,g in d2[d2.m==0].groupby("y") if g.seca.nunique()>1 or g.pos.nunique()>1 or g.ref.nunique()>1})
# fix A: year FE by conception year, straddling cohorts dropped
d3=d2.copy(); d3["y"]=((d3.t-9)//12)
rank_check(d3,"FIX A: FE by conception year; only ref/seca/pos cohorts")
print("fixA within-year variation:", {y:(g.seca.nunique(),g.pos.nunique()) for y,g in d3[d3.m==0].groupby("y") if g.seca.nunique()>1 or g.pos.nunique()>1})
# fix B: periods defined by birth year (ref 2007-2011, seca 2012-2018, pos: born >= Nov 2019; drop Jan-Oct 2019, 2005-06)
d4=d.copy(); d4["ref"]=d4.y.between(2007,2011); d4["seca"]=d4.y.between(2012,2018)
d4=d4[d4.ref|d4.seca|d4.pos]
rank_check(d4,"FIX B: periods by birth year; 2005-06 and Jan-Oct 2019 dropped")
