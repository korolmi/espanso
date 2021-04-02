import sys, yaml, subprocess

confFile = "default" if len(sys.argv)==2 else sys.argv[1]
command = sys.argv[1] if len(sys.argv)==2 else sys.argv[2]

res = subprocess.run(["espanso", "path"], capture_output=True)
configFile = f'{res.stdout.decode("utf-8").split("Config:")[1].strip().split()[0]}/{confFile}.yml'

# parse vonfig file
with open(configFile) as f:
    triggers = yaml.safe_load(f)
    
# find trigger
for t in triggers["matches"]:
    if t["trigger"]==command:
        break
else: # command not found
    print(f"Command {command} not found in config file {configFile}")
    

# print brief help
print(f'Command `{command}`:\n')
if "doc" in t:
    if isinstance(t["doc"], list):
        for ln in t["doc"]:
            print(f"* {ln}")
    else:
        print(f"  {t['doc']}\n")
else:
    print(f'There is no doc, replace: {t["replace"]}')

print("\n")