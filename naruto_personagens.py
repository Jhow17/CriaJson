class Personagem():
    def __init__(self, id, name, birthdate, sex , debut_manga, debut_anime, better_jutsu, clan, rank):
        self.id = id
        self.nome = name
        self.birthdate = birthdate
        self.sexo = sex
        self.debut_manga = debut_manga
        self.debut_anime = debut_anime
        self.melhor_jutsu = better_jutsu
        self.clan = clan
        self.rank = rank
        
    
    def resumo_personagem(self):
        print( f'O personagem {self.nome} pertence ao cla {self.clan} e apareceu pela primeira vez no anime no episodio {self.debut_anime}')
    
    
    
    def to_dict(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Data de nascimento": self.birthdate,
            "Sexo": self.sexo,
            "Debut no manga": self.debut_manga,
            "Debut no anime": self.debut_anime,
            "Melhor jutsu": self.melhor_jutsu,
            "Rank": self.rank
        }

    # ultimo_rank = list(personagem.get('rank').get('ninjaRank').keys())[-1]
    def __str__(self):
        return (
        f"ID: {self.id}\n"
        f"Nome: {self.nome}\n"
        f"Data de nascimento: {self.birthdate}\n"
        f"Sexo: {self.sexo}\n"
        f"Debut no mangá: {self.debut_manga}\n"
        f"Debut no anime: {self.debut_anime}\n"
        f"Melhor jutsu: {self.melhor_jutsu}\n"
        f"Clã: {self.clan}\n"
        f"Rank: {self.rank}"
    )