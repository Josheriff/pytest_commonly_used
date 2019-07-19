import requests
import json

def get_pokemons_number(requests):
    pokemon_list_request = requests.get('https://pokeapi.co/api/v2/pokemon')
    pokemon_list = pokemon_list_request.json()
    pokemons_number = pokemon_list['count']

    return pokemons_number