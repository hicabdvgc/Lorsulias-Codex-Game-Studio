from pathlib import Path
import json,sys,subprocess,os
from runtime_context import *
W=WORK;D=W/"Observer's studio space";P=sys.executable
E=dict(os.environ);E.update(PYTHONPATH=os.environ.get('PYTHONPATH', ''),GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull,GIT_TERMINAL_PROMPT='0')
rows=[]
def check(name,args,code,needle='',data=None,env=None):
 r=subprocess.run(args,input=data,text=True,encoding='utf-8',capture_output=True,env=env or E,cwd=D,timeout=30);rows.append(dict(name=name,passed=r.returncode==code and needle in r.stdout+r.stderr,exit=r.returncode,stdout=r.stdout,stderr=r.stderr));return r
script=T/'.codex/hooks/git-command-check.py'
def event(cmd='git commit -m fixture'):return json.dumps({'tool_name':'Bash','cwd':str(D),'tool_input':{'command':cmd}})
no_git=dict(E);no_git['PATH']='';check('Git unavailable',[P,str(script),'commit',str(D)],1,'NOT ASSESSED',event(),no_git)
# The pending command inherits this override. Inspecting a different cleaned context
# would not assess that command; require an explicit unavailable-context result.
check('Git override remains unassessed',[P,str(script),'commit',str(D)],1,'NOT ASSESSED',event(),dict(E,GIT_DIR='Z:/wrong/repository'))
sub=D/'sub studio';(sub/'res_lib').mkdir(parents=True,exist_ok=True);f=sub/'res_lib/test.json';f.write_text('{"x":1}',encoding='utf-8');subprocess.run(['git','add','--','sub studio/res_lib/test.json'],cwd=D,env=E,check=True,capture_output=True)
check('studio nested within Git root',[P,str(script),'commit',str(sub)],0,'1 resource JSON',event())
out=D/'outside.json';out.write_text('{invalid',encoding='utf-8');subprocess.run(['git','add','--','outside.json'],cwd=D,env=E,check=True,capture_output=True)
check('outside declared resource roots ignored',[P,str(script),'commit',str(sub)],0,'1 resource JSON',event())
f.write_text('{"x":NaN}',encoding='utf-8');subprocess.run(['git','add','--','sub studio/res_lib/test.json'],cwd=D,env=E,check=True,capture_output=True)
check('JSON nonstandard NaN blocked',[P,str(script),'commit',str(sub)],2,'non-JSON constant',event())
f.write_bytes(b'\xff\xfeinvalid');subprocess.run(['git','add','--','sub studio/res_lib/test.json'],cwd=D,env=E,check=True,capture_output=True)
check('invalid staged encoding blocked',[P,str(script),'commit',str(sub)],2,'invalid',event())
# Read failure injection is labeled explicitly; Windows ACL changes are unnecessary.
code='''import runpy,sys\nfrom pathlib import Path\nfrom unittest.mock import patch\noriginal=Path.read_bytes\ndef read(p):\n if p.name=="input.md":raise PermissionError("fixture read failure")\n return original(p)\nsys.argv=[sys.argv[1],"--root",sys.argv[2]]\nwith patch.object(Path,"read_bytes",read):runpy.run_path(sys.argv[0],run_name="__main__")\n'''
check('artifact unreadable (injected OSError)',[P,'-c',code,str(T/'.codex/scripts/artifact-check.py'),str(D)],2,'UNREADABLE')
(W/'extra-runtime-checks.json').write_text(json.dumps(rows,indent=2),encoding='utf-8');print('Additional executable cases:',len(rows),'passed:',sum(x['passed'] for x in rows))
for x in rows:
 if not x['passed']:print(x)
