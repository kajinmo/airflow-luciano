# consumir uma api

import requests
from pydantic import BaseModel

#pydantic > pandera pra esse serviço
#- faz a validação
#- transforma o json num objeto python (desserialização)


class PokemonShema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True #pra falar com a orm

def pegar_pokemon(id: int) -> PokemonShema:
    URL = "https://pokeapi.co/api/v2/pokemon/15"
    response = requests.get(url=URL)
    data = response.json()
    data_pkmn_types = data['types']

    types_list = []
    for types_info in data_pkmn_types:
        types_list.append(types_info['type']['name'])

    name = data['name']
    types = ', '.join(types_list)

    return PokemonShema(name=name, type=types)


if __name__ == "__main__":
    print(pegar_pokemon(1))





