import requests
import json
from flask import Flask, Blueprint

pokemon_search = Blueprint('pokemon_search', __name__)

@pokemon_search.route('/<pokemon>')
def fetch_pokemon(pokemon):

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    data = response.json()

    pokemon_data = json.dumps(data)
    return(data)