from runtime_context import *
results=[]
PY=sys.executable
S=WORK
def check(name,passed,detail=''):
    results.append({'name':name,'passed':bool(passed),'detail':detail})
    print(('PASS ' if passed else 'FAIL ')+name+(': '+str(detail) if detail else ''))
env=os.environ.copy();env['LORSULIA_HOOK_PYTHON']=PY;env['CGS_HOOK_DRY_RUN']='1';env['PYTHONUTF8']='1'
for p in (T/'.codex/hooks').glob('*.sh'):
    run=subprocess.run([BASH,'-n',str(p)],capture_output=True,text=True)
    check('Bash syntax '+p.name,run.returncode==0,run.stderr.strip())

def hook(name,payload,cwd=None,custom_env=None,base=T):
    return subprocess.run([BASH,str(base/'.codex/hooks'/name)],input=payload if isinstance(payload,str) else json.dumps(payload),capture_output=True,text=True,encoding='utf-8',cwd=cwd or base,env=custom_env or env,timeout=20)

for command,expected in [('git status',0),('echo "rm -rf build"',0),('git diff --stat',0),('git reset --hard HEAD',2),('git status; git clean -fd',2),('git push --force-with-lease',2),('Remove-Item -LiteralPath build -Recurse -Force',2),('bash -c "git reset --hard"',2),('cat .env',2)]:
    r=hook('validate-command-safety.sh',{'tool_input':{'command':command}})
    check('Command text: '+command,r.returncode==expected,f'rc={r.returncode} {r.stderr.strip()}')

for payload,label in [('{bad','Malformed JSON'),('[]','Non-object JSON')]:
    r=hook('validate-command-safety.sh',payload)
    check(label,r.returncode==0 and 'NOT ASSESSED' in r.stderr and not r.stdout,r.stderr.strip())
missing_env=env.copy();missing_env.pop('LORSULIA_HOOK_PYTHON',None);missing_env['PATH']=str(Path(BASH).parent.parent/'usr/bin')
parser_fixture=S/"Parser fixture's studio"
(parser_fixture/'.codex/hooks').mkdir(parents=True,exist_ok=True)
for p in (T/'.codex/hooks').glob('*.sh'):shutil.copy2(p,parser_fixture/'.codex/hooks'/p.name)
r=hook('validate-command-safety.sh',{'tool_input':{'command':'git status'}},custom_env=missing_env,base=parser_fixture)
check('Missing structured parser visible','NOT ASSESSED' in r.stderr or 'NOT ASSESSED' in r.stdout,r.stdout.strip()+r.stderr.strip())
subprocess.run([PY,'-m','venv','--without-pip',str(parser_fixture/'.venv')],check=True,timeout=60)
r=hook('validate-command-safety.sh',{'tool_input':{'command':'git status'}},custom_env=missing_env,base=parser_fixture)
check('Project virtual environment works without PATH Python',r.returncode==0 and 'NOT ASSESSED' not in r.stderr,r.stderr.strip())
r=hook('validate-command-safety.sh',{'tool_input':{'command':'git reset --hard HEAD'}},custom_env=missing_env,base=parser_fixture)
check('Project virtual environment retains command checks',r.returncode==2,r.stderr.strip())

patch={'tool_input':{'command':'*** Begin Patch\n*** Update File: .agents/skills/skill-test/SKILL.md\n*** End Patch'}}
r=hook('validate-skill-change.sh',patch,cwd=T/'docs')
out=json.loads(r.stdout) if r.stdout else {}
check('Skill patch reminder from nested folder',r.returncode==0 and '$skill-test' in out.get('systemMessage','') and out.get('hookSpecificOutput',{}).get('hookEventName')=='PostToolUse',out)
r=hook('validate-skill-change.sh',{'tool_input':{'path':'docs/FRAMEWORK.md'}})
check('Unrelated patch no reminder',r.returncode==0 and not r.stdout)
r=hook('validate-skill-change.sh',{'tool_input':{'path':r"E:\A folder\Lorsulia's Studio\.agents\skills\example\SKILL.md"}})
check('Windows path patch reminder','example' in r.stdout and r.returncode==0)

# Real filesystem effects stay in an isolated copy with a space and apostrophe.
fixture=S/"Hook fixture's studio"
fixture.mkdir(exist_ok=True)
(fixture/'nested').mkdir(exist_ok=True)
(fixture/'.codex/hooks').mkdir(parents=True,exist_ok=True)
for p in (T/'.codex/hooks').glob('*.sh'):shutil.copy2(p,fixture/'.codex/hooks'/p.name)
write_env=env.copy();write_env.pop('CGS_HOOK_DRY_RUN',None)
log=fixture/'production/session-logs/agent-audit.log'
before=log.read_text() if log.exists() else ''
for name in ['log-agent.sh','log-agent-stop.sh']:
    r=hook(name,{'agent_type':'producer','agent_id':'test-42'},cwd=fixture/'nested',custom_env=write_env,base=fixture)
    check('Lifecycle '+name,r.returncode==0 and json.loads(r.stdout)=={'continue':True},r.stderr.strip())
appended=log.read_text()[len(before):]
check('Audit events at studio root',len(appended.splitlines())==2 and 'started: producer' in appended and 'stopped: producer' in appended and 'id=test-42' in appended and not (fixture/'nested/production').exists(),appended.strip())
before=log.read_bytes()
r=hook('log-agent.sh',{'agent_type':'producer'},cwd=fixture/'nested',base=fixture)
check('Audit dry run no writes',r.returncode==0 and log.read_bytes()==before)

registry=json.loads((T/'.codex/hooks.json').read_text())['hooks']
for event,payload in [('PreToolUse',{'tool_input':{'command':'git status'}}),('PostToolUse',patch),('SubagentStart',{'agent_type':'producer'}),('SubagentStop',{'agent_type':'producer'})]:
    handler=registry[event][0]['hooks'][0]
    ps=handler['commandWindows'].split(' -Command "',1)[1][:-1]
    r=subprocess.run(['powershell.exe','-NoProfile','-NonInteractive','-Command',ps],input=json.dumps(payload),capture_output=True,text=True,encoding='utf-8',cwd=fixture/'nested',env=env,timeout=30)
    check('Registered Windows launcher '+event,r.returncode==0 and 'unavailable' not in (r.stdout+r.stderr),r.stdout.strip()+r.stderr.strip())
    # Unix command tested with Git Bash; native Unix client dispatch is not claimed.
    r=subprocess.run([BASH,'-c',handler['command']],input=json.dumps(payload),capture_output=True,text=True,encoding='utf-8',cwd=fixture/'nested',env=env,timeout=30)
    check('Registered Bash launcher '+event,r.returncode==0,r.stdout.strip()+r.stderr.strip())

(S/'checks.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
print('SUMMARY',sum(r['passed'] for r in results),'/',len(results))
sys.exit(1 if any(not r['passed'] for r in results) else 0)
