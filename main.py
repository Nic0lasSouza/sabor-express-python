from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    '''
    Endpoint que exibe uma mensagem incrivel no mundo da programação!
    '''
    return {'Hello' : 'World'}
@app.get('/api/restaurantes/')
def get_restaurante(restaurante: str = Query(None)): #exibir informações especificar de um restaurante
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante =[]
        for item in dados_json:
            if item['Company'] == restaurante: # verificar se o nome que esta passando esta dentro de company
                dados_restaurante.append({
                        "item": item['Item'],
                        "price": item['price'],
                        "description": item['description']
                    }) #adiciona os nomes dos restaurantes e seus dados
        return {'Restaurante':restaurante,'Cardapio': dados_restaurante}
    else:
        return{'Erro':f'{response.status_code} - {response.text}'}
