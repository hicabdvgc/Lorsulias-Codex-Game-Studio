from runtime_context import *
W=WORK;B=BASH
F=W/"Studio's fixture";H=F/'.codex/hooks';H.mkdir(parents=True,exist_ok=True)
for n in ['hook-lib.sh','validate-assets.sh']:shutil.copyfile(T/'.codex/hooks'/n,H/n)
for p,content in {'res_lib/good.json':'{"id":"BEACON-01","count":2}',"assets/data/keeper's data.json":'{"ok":true}','res_lib/bad.json':'{"id":}','res_lib/nan.json':'{"v":NaN}','outside.json':'broken','res_lib/media.txt':'unparsed'}.items():
 q=F/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(content,encoding='utf-8')
(F/'nested dir').mkdir(exist_ok=True);(F/'res_lib/folder.json').mkdir(exist_ok=True)
env=os.environ.copy();env['LORSULIA_HOOK_PYTHON']=sys.executable.replace('\\','/');env['MSYS_NO_PATHCONV']='1'
results=[]
def run(label,payload,expected,code=0,cwd=F,missing=False,launcher=None):
 e=env.copy()
 if missing:e['PATH']=str(Path(BASH).parent.parent/'usr/bin');e['LORSULIA_HOOK_PYTHON']='Z:/absent/python.exe'
 args=[B,str(H/'validate-assets.sh').replace('\\','/')]
 if launcher:args=['powershell.exe','-NoProfile','-Command',launcher]
 r=subprocess.run(args,input=payload if isinstance(payload,str) else json.dumps(payload),text=True,capture_output=True,cwd=cwd,env=e,timeout=30)
 combined=r.stdout+r.stderr;ok=r.returncode==code and (expected in combined if expected else not combined.strip())
 results.append(dict(case=label,passed=ok,exit=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if not ok:print('FAIL',label,r.returncode,combined[:300])
def event(p,cwd=F):return dict(hook_event_name='PostToolUse',tool_name='apply_patch',cwd=str(cwd),tool_input={'path':p})
run('valid prepared JSON',event('res_lib/good.json'),'JSON SYNTAX OK')
run('data JSON apostrophe',event("assets/data/keeper's data.json"),'JSON SYNTAX OK')
run('invalid JSON',event('res_lib/bad.json'),'INVALID JSON')
run('strict nonfinite JSON',event('res_lib/nan.json'),'INVALID JSON')
run('irrelevant extension',event('res_lib/media.txt'),'')
run('outside roots',event('outside.json'),'')
run('outside project',event(str(W/'outside.json')),'')
run('deleted file',event('res_lib/deleted.json'),'ABSENT')
run('directory path',event('res_lib/folder.json'),'NOT ASSESSED')
run('malformed event','{','NOT ASSESSED')
run('nonobject event','[]','NOT ASSESSED')
run('irrelevant event',{**event('res_lib/good.json'),'hook_event_name':'PreToolUse'},'')
run('irrelevant tool',{**event('res_lib/good.json'),'tool_name':'Bash'},'')
run('malformed tool_input',{**event('res_lib/good.json'),'tool_input':None},'NOT ASSESSED',1)
run('unextractable input',{**event('res_lib/good.json'),'tool_input':{'command':'echo no patch'}},'NOT ASSESSED')
run('nested relative launch',event('../res_lib/good.json',F/'nested dir'),'JSON SYNTAX OK',cwd=F/'nested dir')
run('absolute Windows path',event(str(F/'res_lib/good.json')),'JSON SYNTAX OK')
msys='/'+str(F)[0].lower()+str(F)[2:].replace('\\','/')+'/res_lib/good.json'
run('MSYS path',event(msys),'JSON SYNTAX OK')
run('outside cwd',event('res_lib/good.json',W),'NOT ASSESSED',1)
run('missing runtime',event('res_lib/good.json'),'NOT ASSESSED',missing=True)
patch='*** Begin Patch\n*** Update File: res_lib/good.json\n+$(touch SHOULD_NOT_EXIST)\n*** Move to: assets/data/keeper\'s data.json\n*** End Patch'
run('patch text treated as data',{**event('res_lib/good.json'),'tool_input':{'command':patch}},'JSON SYNTAX OK')
hooks=json.loads((T/'.codex/hooks.json').read_text(encoding='utf-8'))
handler=next(h for group in hooks['hooks']['PostToolUse'] for h in group['hooks'] if 'validate-assets.sh' in h.get('command',''))
shutil.copyfile(T/'.codex/hooks.json',F/'.codex/hooks.json')
launcher=handler['commandWindows']
# Stored command includes its PowerShell executable; run exactly through cmd.exe's command parser.
r=subprocess.run(launcher,input=json.dumps(event('../res_lib/good.json',F/'nested dir')),text=True,capture_output=True,cwd=F/'nested dir',env=env,timeout=30)
results.append(dict(case='registered Windows launcher nested launch',passed=r.returncode==0 and 'JSON SYNTAX OK' in r.stdout,exit=r.returncode,stdout=r.stdout,stderr=r.stderr))
assert not (F/'SHOULD_NOT_EXIST').exists()
assert not (F/'production').exists()

(W/'runtime-results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print('Asset cases',len(results),'passed',sum(x['passed'] for x in results))
