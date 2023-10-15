import json


info = json.load(open("Ezra/Json-ex/3/random info.json"))
print(info)

info['name'] = 'ezra'
info['age'] = 22
info['city'] = 'RBS'
print(info)

new_info = open("Ezra/Json-ex/3/new info.json", "w")
new_info.write(json.dumps(info))

