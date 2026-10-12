from runtime_context import *
E=WORK
import importlib.util,sys,subprocess,uuid
from unittest.mock import patch
def mod(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
state=mod('state_extra',T/'.codex/scripts/session-state.py');rot=mod('rot_extra',T/'.codex/scripts/rotate_session_state.py');life=mod('life_extra',T/'.codex/scripts/session_lifecycle.py')
R=E/("Extra observer's fixture "+uuid.uuid4().hex[:8]);R.mkdir();p=R/'production/session-state/active.md';p.parent.mkdir(parents=True)
checks=[]
def ck(n,v,d=''):checks.append({'name':n,'pass':bool(v),'detail':str(d)[:1000]})
ck('absent state is discovery result',state.read_state(R)['status']=='ABSENT')
p.write_bytes(b'\xff');ck('invalid UTF-8 is unreadable',state.read_state(R)['status']=='UNREADABLE')
text='<!-- STATUS -->\nTask: test\n<!-- /STATUS -->\n<!-- CHECKPOINT -->\nNext: inspect\n<!-- /CHECKPOINT -->\n\n## Notes\nKeep exact narrative.\n'
p.write_text(text,encoding='utf-8');original=p.read_bytes()
real_open=Path.open
def failed_archive(path,*args,**kwargs):
 if path.parent.name=='session-logs' and args and args[0]=='xb':raise OSError('fixture archive unavailable')
 return real_open(path,*args,**kwargs)
with patch.object(Path,'open',failed_archive):
 try:rot.rotate(R);ok=False
 except ValueError as exc:ok='archive unavailable' in str(exc)
ck('archive failure leaves source unchanged',ok and p.read_bytes()==original)
with patch.object(life.subprocess,'run',side_effect=OSError('fixture command unavailable')):
 result=life.run(R,'SessionStart',{'hook_event_name':'SessionStart','source':'startup'})
 ck('discovery execution failure explicit','Discovery NOT ASSESSED' in result['hookSpecificOutput']['additionalContext'],result)
with patch.dict(os.environ,{'CGS_HOOK_DRY_RUN':'1'}):
 for i in range(2):result=life.run(R,'Stop',{'hook_event_name':'Stop','stop_hook_active':True})
 ck('repeat Stop never requests continuation',result=={'continue':True})
with patch.object(Path,'mkdir',side_effect=OSError('fixture log unavailable')):
 old=os.environ.pop('CGS_HOOK_DRY_RUN',None)
 try:
  try:life.run(R,'Stop',{'hook_event_name':'Stop'});ok=False
  except OSError as exc:ok='log unavailable' in str(exc)
 finally:
  if old is not None:os.environ['CGS_HOOK_DRY_RUN']=old
 ck('audit write error is an execution error',ok)
shutil.copytree(T/'.codex',R/'.codex',dirs_exist_ok=True);(R/'docs').mkdir(exist_ok=True);shutil.copy2(T/'docs/technical-preferences.md',R/'docs/technical-preferences.md')
env=os.environ.copy();env['LORSULIA_HOOK_PYTHON']=python_without_packages();env['PYTHONDONTWRITEBYTECODE']='1';env.pop('PYTHONPATH',None)
proc=subprocess.run([BASH,str(R/'.codex/hooks/session-start.sh')],cwd=R,input=json.dumps({'hook_event_name':'SessionStart','source':'startup'}),capture_output=True,text=True,encoding='utf-8',env=env,timeout=30)
ck('missing YAML parser actionable','PyYAML' in proc.stdout and ('NOT ASSESSED' in proc.stdout or 'unavailable' in proc.stdout),proc.stdout)
(E/'extra-runtime-checks.json').write_text(json.dumps(checks,indent=2))
print(json.dumps({'checks':len(checks),'passed':sum(c['pass'] for c in checks),'failures':[c for c in checks if not c['pass']]},indent=2))
