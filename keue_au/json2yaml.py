import json
import time
import yaml


print(time.time())
with open('icorpus.json') as ic:
    chu = json.load(ic)
print(time.time())
for pinn in chu:
    pinn['台語'] = pinn['台語'].split('\n')
    pinn['華語'] = pinn['華語'].split('\n')
print(time.time())
with open('icorpus.yaml', 'w') as 檔案:
    yaml.dump(chu, 檔案, default_flow_style=False, allow_unicode=True)
print(time.time())
