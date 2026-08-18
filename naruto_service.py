# onde vamos fazer as chamadas a api
import requests
def busca_dados(url):
    
    try:
        response = requests.get(url)
        
        # se vier com algum status de erro (400 Bad Request, 401 Unatorizeded, 403 Forbidden 404 Not Found 500 Internal Server Error) vai lancar um erro HttpError
        # para pegar esse erro e mandar uma mensagem mais clara podemos usar requests.exceptions.HttpError
        response.raise_for_status()
        
        dados = response.json()
        
        return dados
    # tem como colocar outar excepts mas por enquanto essa esta boa 
    except requests.exceptions.HTTPError as erro:
        print(f'Status da conexao {response.status_code}')
        print(f'Houve um erro de HTTP {erro}')
        
        

personagens = busca_dados('https://dattebayo-api.onrender.com/characters')


