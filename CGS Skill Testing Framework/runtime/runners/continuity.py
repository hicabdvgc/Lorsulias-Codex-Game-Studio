from runtime_context import *
E=WORK
import subprocess, sys, tomllib, importlib.util, copy as cp, uuid
from unittest.mock import patch
PY=sys.executable;BASH=BASH
results=[]
def check(name,ok,detail=''):
 results.append({'name':name,'pass':bool(ok),'detail':str(detail)[:1800]})
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def run(cmd,**kw):return subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30,**kw)
root=E/("Observer's studio space " + uuid.uuid4().hex[:8]);root.mkdir(exist_ok=True)
for directory in ['.codex/hooks','.codex/scripts','.codex/docs']:
 shutil.copytree(T/directory,root/directory,dirs_exist_ok=True)
(root/'docs').mkdir(exist_ok=True);shutil.copy2(T/'docs/technical-preferences.md',root/'docs/technical-preferences.md')
(root/'nested/deeper').mkdir(parents=True,exist_ok=True)
statepath=root/'production/session-state/active.md';statepath.parent.mkdir(parents=True,exist_ok=True)
valid='''# Current task
<!-- STATUS -->
Epic:
Feature: Navigation
Task: Check inputs
<!-- /STATUS -->
<!-- CHECKPOINT -->
Current task: Exercise recovery
Completed: Fixture made
Next step: Inspect actual output
Verification: This is fixture context only
<!-- /CHECKPOINT -->

## Notes
Preserve this narrative, including the apostrophe in user's note.
'''
state=module('state_test',T/'.codex/scripts/session-state.py')
rotate=module('rotate_test',T/'.codex/scripts/rotate_session_state.py')
statepath.write_text(valid,encoding='utf-8')
r=state.read_state(root);check('parser blank field does not consume next field',r['focus']=={'Feature':'Navigation','Task':'Check inputs'},r)
for name,content in [('missing','legacy unstructured notes'),('duplicate',valid+'<!-- STATUS -->'),('reversed',valid.replace('<!-- STATUS -->','<!-- /STATUS -->',1)),('oversized',valid.replace('Current task: Exercise recovery','x'*4097)),('overlap',valid.replace('<!-- /STATUS -->','').replace('<!-- /CHECKPOINT -->','<!-- /STATUS -->\n<!-- /CHECKPOINT -->')),('duplicate-field',valid.replace('Task: Check inputs','Task: Check inputs\nTask: Another'))]:
 statepath.write_text(content,encoding='utf-8');r=state.read_state(root);check('parser '+name,r['status']=='MALFORMED' and not r['focus'],r)
statepath.write_text(valid,encoding='utf-8')
stage=root/'production/stage.txt';stage.write_text('implementation\n',encoding='utf-8')
check('stage canonical',state.read_stage(root)['status']=='VALID')
stage.write_text('Live\nimplementation\n',encoding='utf-8');check('stage legacy retained',state.read_stage(root)['declared']=='Live' and state.read_stage(root)['status']=='MALFORMED')
stage.write_text('implementation\n',encoding='utf-8')
env=os.environ.copy();env['LORSULIA_HOOK_PYTHON']=PY;env['PYTHONPATH']=os.environ.get('PYTHONPATH', '');env['CGS_HOOK_DRY_RUN']='1'
for name,event,extra in [('session-start','SessionStart',{'source':'startup'}),('session-stop','Stop',{'stop_hook_active':False}),('pre-compact','PreCompact',{'trigger':'auto'}),('post-compact','PostCompact',{'trigger':'manual'})]:
 script=root/f'.codex/hooks/{name}.sh';data={'hook_event_name':event,'session_id':"fixture's session",'turn_id':'turn/../id',**extra}
 p=run([BASH,str(script)],cwd=root/'nested/deeper',env=env,input=json.dumps(data))
 try:out=json.loads(p.stdout)
 except ValueError:out={}
 check(name+' valid nested non-Git',p.returncode==0 and bool(out),p.stdout+p.stderr)
 check(name+' dry-run no audit writes',not (root/'production/session-logs').exists())
 if event=='SessionStart':
  ctx=out.get('hookSpecificOutput',{}).get('additionalContext','');check('startup bounded discovery and no narrative', 'Discovery observer exit' in ctx and 'Preserve this narrative' not in ctx,ctx)
  data['source']='compact';p=run([BASH,str(script)],cwd=root,env=env,input=json.dumps(data));out=json.loads(p.stdout);ctx=out['hookSpecificOutput']['additionalContext'];check('compact avoids repeated gap scan','Discovery observer' not in ctx and 'Exercise recovery' in ctx,ctx)
 for label,payload in [('malformed','{'),('irrelevant',json.dumps({'hook_event_name':'PreToolUse'})),('badfield',json.dumps({**data,'session_id':3}))]:
  p=run([BASH,str(script)],cwd=root,env=env,input=payload);check(name+' '+label,p.returncode!=0 and 'NOT ASSESSED' in p.stdout,p.stdout)
 liveenv=env.copy();liveenv.pop('CGS_HOOK_DRY_RUN');p=run([BASH,str(script)],cwd=root,env=liveenv,input=json.dumps(data));check(name+' actual execution',p.returncode==0,p.stdout+p.stderr)
 if event!='SessionStart':
  logs=list((root/'production/session-logs').glob('lifecycle-*.json'));events=[json.loads(x.read_text()) for x in logs]
  check(name+' event audit',any(x['event']==event and x['session_id']=="fixture's session" for x in events),events)
  # Move evidence away so the next dry-run check sees a clean output scope.
  archive=E/'event-evidence';archive.mkdir(exist_ok=True)
  for f in logs:shutil.move(str(f),str(archive/f.name))
  (root/'production/session-logs').rmdir()

# Fault injection only in the disposable helper proves each wrapper's unavailable-runtime route.
lib=root/'.codex/hooks/hook-lib.sh';orig=lib.read_text();lib.write_text(orig+'\nselect_hook_python() { HOOK_PYTHON_CMD=(); }\n')
for n in ['session-start','session-stop','pre-compact','post-compact']:
 p=run([BASH,str(root/f'.codex/hooks/{n}.sh')],env=env,input='{}');check(n+' unavailable runtime',p.returncode!=0 and 'NOT ASSESSED' in p.stdout,p.stdout)
lib.write_text(orig)

# Exact registered Windows launch command, invoked from a nested path with apostrophe/spaces.
registry=json.loads(read('.codex/hooks.json'))
for event,extra in [('SessionStart',{'source':'compact'}),('Stop',{'stop_hook_active':False}),('PreCompact',{'trigger':'manual'}),('PostCompact',{'trigger':'auto'})]:
 cmd=registry['hooks'][event][0]['hooks'][0]['commandWindows'].split(' -Command "',1)[1][:-1]
 p=run(['powershell.exe','-NoProfile','-NonInteractive','-Command',cmd],cwd=root/'nested/deeper',env=env,input=json.dumps({'hook_event_name':event,**extra}));check(event+' registered Windows launcher',p.returncode==0 and bool(json.loads(p.stdout)),p.stdout+p.stderr)

# Rotation successes, preservation, repeat invocation, appended notes, archive/failure/concurrency.
statepath.write_text(valid,encoding='utf-8');before=statepath.read_bytes();r=rotate.rotate(root,True)
check('rotation dry run preserves source',r['status']=='DRY RUN' and statepath.read_bytes()==before and not Path(r['archive']).exists(),r)
r=rotate.rotate(root);check('rotation archive exact narrative',r['status']=='ROTATED' and Path(r['archive']).read_bytes()==before.split(b'<!-- /CHECKPOINT -->',1)[1],r)
check('rotation keeps exact checkpoint prefix',statepath.read_bytes().split(b'<!-- /CHECKPOINT -->')[0]==before.split(b'<!-- /CHECKPOINT -->')[0])
check('rotation repeated no duplicate',rotate.rotate(root)['status']=='UNCHANGED')
with statepath.open('a',encoding='utf-8') as f:f.write('\nNew note added after rotation.\n')
r=rotate.rotate(root);check('rotation preserves newly appended narrative',r['status']=='ROTATED' and 'New note' in Path(r['archive']).read_text(),r)
statepath.write_text(valid,encoding='utf-8')
with patch.object(rotate.os,'replace',side_effect=OSError('fixture replacement denied')):
 try:rotate.rotate(root);ok=False
 except ValueError as exc:ok='verified archive retained' in str(exc)
check('rotation replacement failure preserves source/archive',ok and statepath.read_bytes()==before)
lock=statepath.with_name('.session-state-rotation.lock');lock.write_text('other operation')
try:rotate.rotate(root);ok=False
except ValueError as exc:ok='lock exists' in str(exc)
check('rotation competing operation',ok and statepath.read_bytes()==before);lock.unlink()
with patch.object(rotate.tempfile,'NamedTemporaryFile',side_effect=OSError('fixture temp unavailable')):
 try:rotate.rotate(root);ok=False
 except ValueError as exc:ok='temp unavailable' in str(exc)
check('rotation unavailable temp preserves source',ok and statepath.read_bytes()==before)
real_fsync=rotate.os.fsync
def concurrent(fd):
 real_fsync(fd);statepath.write_bytes(before+b'\nConcurrent addition\n')
with patch.object(rotate.os,'fsync',side_effect=concurrent):
 try:rotate.rotate(root);ok=False
 except ValueError as exc:ok='changed during' in str(exc)
check('rotation concurrent edit preserved',ok and statepath.read_bytes().endswith(b'Concurrent addition\n'))
statepath.write_text('legacy notes',encoding='utf-8')
try:rotate.rotate(root);ok=False
except ValueError:ok=True
check('rotation legacy refused without data loss',ok and statepath.read_text()=='legacy notes')
statepath.write_text(valid,encoding='utf-8')
p=run([BASH,str(root/'.codex/scripts/rotate-session-state.sh'),'--dry-run'],cwd=root/'nested/deeper',env=env);check('rotation Bash Windows path',p.returncode==0 and json.loads(p.stdout)['status']=='DRY RUN',p.stdout+p.stderr)
(E/'runtime-checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'checks':len(results),'passed':sum(x['pass'] for x in results),'failures':[x for x in results if not x['pass']]},indent=2))
