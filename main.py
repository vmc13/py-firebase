import requests
import json

link = "https://api-ba-firebase-default-rtdb.firebaseio.com/"

# CREATE
#dados = {
#    "img": "https://sheep.png"
#}
#requisicao = requests.post(f'{link}/Imagens.json', #data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

# PATCH

# GET
#req =  requests.get(f'{link}/Imagens.json')
#print(req)
#print(req.text)

# ESPECIFICAR
req =  requests.get(f'{link}/Imagens/.json')
print(req)
dic_req = req.json()
for id_venda in dic_req:
    image = dic_req[id_venda]['img']
    print(f'IMAGE: {image}')