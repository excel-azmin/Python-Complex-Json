import json

data = {}
with open('data.json') as r:
    data = json.load(r)


for d in data:
    print("\n"+d+" \t: "+str(data[d]["data"]))