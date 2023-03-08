import requests
import json

link = "https://api-ba-firebase-default-rtdb.firebaseio.com/"

# CREATE
'''
dados = {
    "img": "https://pig.png",
    "status": "nao lido"
}
requisicao = requests.post(f'{link}/Imagens.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)
'''

# GET AND PATCH: ESPECIFICAR
req =  requests.get(f'{link}/Imagens/.json')
print(req)

# transforma o bd json em dict python
dic_req = req.json()

# adicionar as chaves numa lista
list_keys = []

# adiciona as keys do json de imagens a list_keys
for items in dic_req.keys():
    #print(items)
    list_keys.append(items)


for item_id in dic_req:
    image = dic_req[item_id]['img']
    status = dic_req[item_id]['status']
    if status == "nao lido":
        dados = {"status": "lido"}
        requisicao = requests.patch(f'{link}/Imagens/{item_id}/.json', data=json.dumps(dados))
        print(image)
    

    


# function to listen
# take the first unread

