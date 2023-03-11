import requests
import json

link = "https://api-ba-firebase-default-rtdb.firebaseio.com/"

# GET AND PATCH FOR ESPECIFIC PATHS
req =  requests.get(f'{link}/Imagens/.json') # bd em json
print(req)

# transforma o bd json em dict python
dic_req = req.json()

# lista com todas as chaves
all_keys = []

# adiciona as keys do json de imagens a all_keys
for items in dic_req.keys():
    all_keys.append(items)

# lista de keys com status nao lido
unseen_keys = []

for item in all_keys:
    if dic_req[item]["status"] == "nao lido":
        unseen_keys.append(item)


image = dic_req[unseen_keys[0]]['img'] # get image link
status = dic_req[unseen_keys[0]]['status'] # get image status
if status == "nao lido":
        dados = {"status": "lido"}
        requisicao = requests.patch(f'{link}/Imagens/{unseen_keys[0]}/.json', data=json.dumps(dados)) # change image status
        print(image)
