from pathlib import Path
import hashlib, json

root=Path(__file__).resolve().parents[1]
audit=root/'work/projeto-pesquisa'
local=Path('C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa')
rows=[]
for base in ['scripts', 'paper', 'tests']:
    for p in sorted((local/base).rglob('*')):
        if p.is_file() and p.suffix in ['.py', '.R', '.tex', '.bib']:
            rel=p.relative_to(local)
            q=audit/rel
            sha=hashlib.sha256(p.read_bytes()).hexdigest()
            other=hashlib.sha256(q.read_bytes()).hexdigest() if q.exists() else None
            rows.append({'path':rel.as_posix(),'local_sha256':sha,'audited_sha256':other,'same':sha==other})
(root/'work/empirical').mkdir(exist_ok=True)
(root/'work/empirical/code-comparison.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'files':len(rows),'changed':[x['path'] for x in rows if not x['same']]},indent=2))
