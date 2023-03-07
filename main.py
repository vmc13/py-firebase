import requests
import json

link = "https://api-ba-firebase-default-rtdb.firebaseio.com/"

# CREATE
#dados = {
#    "img": "https://pig.png",
#    "status": "nao lido"
#}
#requisicao = requests.post(f'{link}/Imagens.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

# ESPECIFICAR
req =  requests.get(f'{link}/Imagens/.json')
print(req)

dic_req = req.json()

for item_id in dic_req:
    image = dic_req[item_id]['img']
    status = dic_req[item_id]['status']
    if status == "nao lido":
        print(image)
        dados = {"status": "lido"}
        requisicao = requests.patch(f'{link}/Imagens/-NPxvFyXxMmXvHw27-mo/.json', data=json.dumps(dados))

# função para escutar
# printar só a primeira da fila da não lida