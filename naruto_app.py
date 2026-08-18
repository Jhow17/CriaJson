from naruto_service import busca_dados
from naruto_personagens import Personagem
import random
import json

def cria_personagens(url):
    url_base  = f'https://dattebayo-api.onrender.com{url}'
    
    dados = busca_dados (url_base)
    dados_personagens = dados['characters'][:10]

    
    # nao conhecia o json.dumps mas agora que eu coneci ele eu descobri que ele so funciona 
    # com dicionarios eu poderia ter criado so um dicionario normal ao inves de criar uma classe
    
    with open('personagens.json', 'w') as file:
            for personagem in dados_personagens:
                tam_jutsu = len(personagem['jutsu']) - 1
                index_jutsu = random.randint(0, tam_jutsu)
                
                try:
                    ultimo_rank = list(personagem['rank']['ninjaRank'].keys())[-1]
                except AttributeError as erro:
                    ultimo_rank = "Part I"
                except KeyError as erro:
                    ultimo_rank = "Part I"
                try:
                    rank = personagem.get('rank').get('ninjaRank').get(ultimo_rank)
                except:
                    rank = 'Genin'
                personagem_instanciado = Personagem(personagem['id'], personagem['name'], personagem['personal']['birthdate'], personagem['personal']['sex'], personagem['debut']['manga'], personagem['debut']['anime'], personagem['jutsu'][index_jutsu], personagem.get('personal').get('clan'),rank)
                
                json.dump(personagem_instanciado.to_dict(),file)
    


if __name__ == '__main__':     
    cria_personagens('/characters')