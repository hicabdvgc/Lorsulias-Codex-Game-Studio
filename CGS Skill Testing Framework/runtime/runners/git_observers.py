from pathlib import Path
import os,sys,json,subprocess,shutil,hashlib
from runtime_context import *
W=WORK;P=sys.executable;B=BASH;D=W/"Observer's studio space";D.mkdir(exist_ok=True)
for rel in ['.codex/hooks/hook-lib.sh','.codex/hooks/git-command-check.py','.codex/hooks/validate-commit.sh','.codex/hooks/validate-push.sh','.codex/hooks/detect-gaps.sh','.codex/scripts/artifact-check.py','.codex/scripts/artifact-check.sh']:
 dst=D/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(T/rel,dst)
(D/'nested dir').mkdir(exist_ok=True);(D/'docs').mkdir(exist_ok=True);(D/'docs/technical-preferences.md').write_text('- **Engine**: [TO BE CONFIGURED]\n- **Project / Code Roots**: [TO BE CONFIGURED]\n',encoding='utf-8')
ENV=dict(os.environ);ENV.update(LORSULIA_HOOK_PYTHON=P,PYTHONPATH=os.environ.get('PYTHONPATH', ''),GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull,GIT_TERMINAL_PROMPT='0')
for k in ['GIT_DIR','GIT_WORK_TREE','GIT_INDEX_FILE']:ENV.pop(k,None)
results=[]
def run(name,argv,code,contains='',payload=None,cwd=None,env=None):
 r=subprocess.run(argv,input=payload,text=True,encoding='utf-8',errors='replace',capture_output=True,cwd=cwd or D/'nested dir',env=env or ENV,timeout=40)
 ok=r.returncode==code and contains in r.stdout+r.stderr
 results.append(dict(name=name,passed=ok,exit=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if not ok:print('FAIL',name,r.returncode,(r.stdout+r.stderr)[:600])
 return r
catalog=D/'.codex/docs/workflow-catalog.yaml';catalog.parent.mkdir(parents=True,exist_ok=True)
base='''phases:
  conceptualization:
    steps:
    - id: manual
      completion: Real human work
    - id: concept
      completion: Author concept
      artifact:
        path: docs/input.md
'''
catalog.write_text(base,encoding='utf-8')
(D/'docs/input.md').unlink(missing_ok=True)
art=[B,str(D/'.codex/scripts/artifact-check.sh')]
run('artifact absent/manual',art,1,'NO_CHECK')
(D/'docs/input.md').write_text('   \n',encoding='utf-8');run('artifact empty',art,1,'EMPTY')
(D/'docs/input.md').write_text('actual fixture',encoding='utf-8');run('artifact present nested nonGit',art,0,'PRESENT')
run('artifact explicit Windows root',[*art,'--root',str(D),'--phase','conceptualization'],0,'PRESENT')
run('artifact unknown phase',art+['--phase','production'],2,'unknown phase')
run('artifact unknown flag',art+['--tier','solo'],2,'unrecognized arguments')
for name,text in [('empty',''),('bad yaml','phases: ['),('duplicate key',base+'phases: {}\n'),('duplicate ID',base.replace('id: concept','id: manual')),('bad artifact',base.replace('path: docs/input.md','pattern: docs/*.md')),('outside root',base.replace('docs/input.md','../outside.md')),('zero steps','phases:\n  conceptualization:\n    steps: []\n')]:
 catalog.write_text(text,encoding='utf-8');run('artifact '+name,art,2)
catalog.write_text(base,encoding='utf-8')
no_yaml=dict(ENV);no_yaml.pop('PYTHONPATH');no_yaml['LORSULIA_HOOK_PYTHON']=python_without_packages();run('artifact missing PyYAML',art,2,'PyYAML unavailable',env=no_yaml)
no_runtime=dict(ENV);no_runtime['LORSULIA_HOOK_PYTHON']='Z:/absent/python.exe';no_runtime['PATH']=str(Path(BASH).parent.parent/'usr/bin');run('artifact missing Python',art,2,'Working Python',env=no_runtime)
run('gap explicit', [B,str(D/'.codex/hooks/detect-gaps.sh')],0,'TO BE CONFIGURED')
run('gap unknown args', [B,str(D/'.codex/hooks/detect-gaps.sh'),'--auto'],2,'no arguments')
# Actual isolated Git repository, no user configuration or production remote.
def git(*args):
 r=subprocess.run(['git','-C',str(D),*args],capture_output=True,text=True,env=ENV);assert r.returncode==0,(args,r.stderr);return r.stdout
if not (D/'.git').exists():
 git('init','-b','fixture');git('config','user.name','Studio Test Fixture');git('config','user.email','fixture@example.invalid');git('config','core.autocrlf','false')
 git('add','.');git('commit','-m','fixture baseline')
def hook(name,command,code=0,contains='',mode='commit',cwd=None,payload=None,env=None):
 event={'hook_event_name':'PreToolUse','tool_name':'Bash','cwd':str(cwd or D),'tool_input':{'command':command}}
 return run(name,[B,str(D/f'.codex/hooks/validate-{mode}.sh')],code,contains,payload=json.dumps(event) if payload is None else payload,env=env)
f=D/"res_lib/actor's stats.json";f.parent.mkdir(exist_ok=True);f.write_text('{"hp":3}',encoding='utf-8');git('add','--',str(f));f.write_text('{broken',encoding='utf-8')
hook('valid staged invalid worktree','git commit -m "data"',0,'1 resource JSON')
f.write_text('{broken',encoding='utf-8');git('add','--',str(f));f.write_text('{"hp":3}',encoding='utf-8');hook('invalid staged valid worktree','git commit -m "data"',2,'staged JSON is invalid')
f.write_text('{"hp":3}',encoding='utf-8');git('add','--',str(f));git('commit','-m','valid fixture')
git('mv',str(f),str(f.with_name('renamed stats.json')));hook('renamed staged JSON','git commit --no-edit',0,'1 resource JSON');git('commit','-m','rename fixture')
git('rm','--',str(f.with_name('renamed stats.json')));hook('deleted resource','git commit -m delete',0,'0 resource JSON')
hook('nested git C', 'git -C ".." commit -m "data"',0,'Staged observation',cwd=D/'nested dir')
hook('absolute Windows git C','git -C "'+str(D)+'" commit -m "data"',0,'Staged observation')
hook('apostrophe message','git commit -m "player\'s data"',0,'Staged observation')
hook('non Git cwd','git commit -m data',1,'NOT ASSESSED',cwd=W)
hook('irrelevant shell','echo unrelated')
hook('irrelevant event','ignored',payload=json.dumps({'hook_event_name':'PostToolUse','tool_name':'apply_patch'}))
hook('bad JSON','ignored',1,'NOT ASSESSED',payload='{')
hook('bad input shape','ignored',1,'JSON object',payload='[]')
hook('bad command type','ignored',1,'must be text',payload=json.dumps({'tool_name':'Bash','tool_input':{'command':[]}}))
hook('missing cwd','ignored',1,'cwd is required',payload=json.dumps({'tool_name':'Bash','tool_input':{'command':'git commit'}}))
for cmd in ['git commit -am all','git commit --only res_lib/data.json','git commit -- path.json','git -c key=value commit','cd x && git commit -m y','git commit -m x; echo payload','git commit -m "$(touch SENTINEL)"']:
 hook('unsupported command '+cmd,cmd,0,'NOT ASSESSED')
assert not (D/'SENTINEL').exists()
hook('push context','git push origin fixture',0,'Tests/build checks were NOT RUN',mode='push')
hook('push force','git push --force origin fixture',2,'force-push',mode='push')
hook('push lease','git push --force-with-lease=refs/heads/fixture origin fixture',2,'force-push',mode='push')
hook('missing runtime','git commit',1,'working Python',env=no_runtime)
# Actual Windows registry launcher in a nested fixture, direct invocation rather than native hook dispatch.
config=json.loads((T/'.codex/hooks.json').read_text());launcher=next(h['commandWindows'] for h in config['hooks']['PreToolUse'][0]['hooks'] if 'validate-commit.sh' in h['commandWindows']); ps=launcher.split(' -Command "',1)[1][:-1]
event={'tool_name':'Bash','cwd':str(D),'tool_input':{'command':'git commit -m fixture'}}
run('Windows launcher nested/apostrophe',['powershell.exe','-NoProfile','-NonInteractive','-Command',ps],0,'Staged observation',payload=json.dumps(event))
# Verify observer read-only effects across repeated actual calls.
def snap():return {str(p.relative_to(D)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file()}
before=snap();hook('read-only repeat','git commit -m fixture');run('artifact read-only repeat',art,0);after=snap();results.append(dict(name='observers preserve fixture bytes including Git index',passed=before==after))
(W/'runtime-checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print('Runtime checks:',len(results),'passed:',sum(x['passed'] for x in results))
