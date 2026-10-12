from runtime_context import *
D=WORK;static=[]
def check(label,condition,detail=''): static.append(dict(check=label,passed=bool(condition),detail=detail))
def snap(root): return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
# Execute a copied observer with the real shared helper in an isolated non-Git studio.
F=D/"Observer's studio space"; (F/'.codex/scripts').mkdir(parents=True,exist_ok=True);(F/'.codex/hooks').mkdir(parents=True,exist_ok=True)
shutil.copy2(T/'.codex/scripts/story-status.sh',F/'.codex/scripts/story-status.sh');shutil.copy2(T/'.codex/hooks/hook-lib.sh',F/'.codex/hooks/hook-lib.sh')
(F/'production/epics').mkdir(parents=True,exist_ok=True);(F/'nested launch').mkdir(exist_ok=True)
bash=BASH;env=os.environ.copy();env['LORSULIA_HOOK_PYTHON']=sys.executable;env['PYTHONIOENCODING']='utf-8'
results=[]
def run(label,contents,args=None,expected=(),code=0,cwd=None,customenv=None):
 slug='case-'+str(len(results)+1);p=F/'production/epics'/slug;p.mkdir(exist_ok=True)
 for name,content in contents.items():
  fp=p/name
  if isinstance(content,bytes):fp.write_bytes(content)
  else:fp.write_text(content,encoding='utf-8')
 scope=['production/epics/'+slug] if args is None else args(p)
 initial=snap(F)
 r=subprocess.run([bash,(F/'.codex/scripts/story-status.sh').as_posix(),*scope],cwd=cwd or F,env=customenv or env,capture_output=True,text=True,encoding='utf-8')
 output=r.stdout+r.stderr
 ok=r.returncode==code and all(s in output for s in expected) and snap(F)==initial
 results.append({'case':label,'args':scope,'cwd':str(cwd or F),'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'passed':ok,'expected':list(expected),'read_only':snap(F)==initial})
run('all canonical and legacy statuses',{f'story-{i:03}-example.md':f'# Work\nStatus: {s}\n## Context\n' for i,s in enumerate(['Not Started','Ready','In Progress','In Review','Complete','Blocked','Done'],1)},expected=['TODO','IN_PROGRESS','IN_REVIEW','BLOCKED','DONE','COMPLETE     2 of 7'])
run('markdown header forms',{'story-001-a.md':'# A\n**Status:** Ready\n','story-002-b.md':'# B\n> **Status**: In Review\n','story-003-c.md':'# C\n- **Status**: Blocked\n'},expected=['TODO','IN_REVIEW','BLOCKED'])
run('unknown values',{'story-001-a.md':'Status: Not Done\n','story-002-b.md':'Status: Completed\n','story-003-c.md':'Status: Complete someday\n'},expected=['OTHER','COMPLETE     0 of 3'])
run('missing header and body status',{'story-001-a.md':'# A\n## Test Evidence\nStatus: Complete\n'},expected=['NO_STATUS','COMPLETE     0 of 1'])
run('malformed empty status',{'story-001-a.md':'Status: \n'},expected=['MALFORMED'])
run('malformed missing colon',{'story-001-a.md':'Status = Ready\n'},expected=['MALFORMED'])
run('conflicting declarations',{'story-001-a.md':'Status: Ready\nStatus: Complete\n'},expected=['CONFLICT','COMPLETE     0 of 1'])
run('duplicate identical declarations',{'story-001-a.md':'Status: Ready\nStatus: Ready\n'},expected=['MALFORMED'])
run('fenced examples and comments',{'story-001-a.md':'# A\n```md\nStatus: Complete\n## Fake\n```\n<!-- Status: Complete -->\nStatus: Ready\n## Context\nStatus: Complete\n'},expected=['TODO','COMPLETE     0 of 1'])
run('tilde fences',{'story-001-a.md':'~~~md\nStatus: Complete\n~~~\nStatus: Blocked\n'},expected=['BLOCKED'])
run('case and trailing period',{'story-001-a.md':'status: done.\n'},expected=['DONE','COMPLETE     1 of 1'])
run('successful empty scope',{},expected=['EMPTY: discovery succeeded','0 of 0'])
run('missing directory',{},args=lambda p:['production/epics/absent'],code=2,expected=['NOT ASSESSED: discovery'])
run('outside roots',{},args=lambda p:[str(D)],code=2,expected=['NOT ASSESSED: discovery'])
run('file instead of directory',{'story-001-a.md':'Status: Ready'},args=lambda p:[str(p/'story-001-a.md')],code=2,expected=['NOT ASSESSED: discovery'])
run('read error with partial scope',{'story-001-a.md':'Status: Ready\n','story-002-b.md':b'\xff\xfe\xff'},code=2,expected=['NOT ASSESSED:','PARTIAL:','TODO'])
run('Windows absolute path and nested launch',{'story-001-a.md':'Status: Ready\n'},args=lambda p:[str(p)],cwd=F/'nested launch',expected=['TODO'])
run('Windows relative backslashes',{'story-001-a.md':'Status: In Progress\n'},args=lambda p:['production\\epics\\'+p.name],cwd=F/'nested launch',expected=['IN_PROGRESS'])
run('irrelevant filenames',{'README.md':'Status: Complete\n','EPIC.md':'Status: Ready\n'},expected=['EMPTY: discovery succeeded'])
run('invalid argument count',{},args=lambda p:['one','two'],code=2,expected=['Usage:'])
fake=F/'fake bin';fake.mkdir(exist_ok=True)
for n in ['python3','python','py']:(fake/n).write_text('#!/bin/sh\nexit 1\n',encoding='utf-8',newline='\n')
noenv=env.copy();noenv['LORSULIA_HOOK_PYTHON']=str(F/'missing.exe');noenv['PATH']=str(fake)+os.pathsep+env['PATH']
run('unavailable Python',{},code=2,expected=['requires working Python'],customenv=noenv)
run('default scope from nested non-Git launch',{},args=lambda p:[],cwd=F/'nested launch',code=2,expected=['IN_REVIEW','PARTIAL:']) # contains deliberate unreadable fixture
for p in [T/'.codex/scripts/story-status.sh']:
 r=subprocess.run([bash,'-n',str(p)],capture_output=True,text=True);check('bash syntax '+p.name,r.returncode==0,r.stderr)
out={'static':static,'executions':results}
(D/'checks.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print('Static:',sum(r['passed'] for r in static),'/',len(static),'Observer:',sum(r['passed'] for r in results),'/',len(results))
for r in static+results:
 if not r['passed']: print('FAILED',r)
