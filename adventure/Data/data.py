import json

with open('data.json') as f:
    data = json.load(f)

for room in data['rooms']:
    print(room)