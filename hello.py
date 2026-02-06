import requests   # type: ignore
import json
url = "https://dragonball-api.com/api/characters/1"

re = requests.get(url)
data = re.json()
# print(json.dumps((data),indent=4))
# print(len(data))

# for i,_ in data.items():
#     print(data[f"{i}"]," : ",data["ki"])

for i in data['transformations']:
    print(i['ki'])