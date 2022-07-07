from flask import Flask, Blueprint, render_template, request
import requests

home = Blueprint('home', __name__)

@home.route('/', methods = ['GET', 'POST'])
def return_home():
    if request.method == "POST":
        search_term = request.form["searchedPokemon"]

        # get all pokemon, turn it into json, return only results array which contains pokemon data
        all_pokemon = (requests.get("https://pokeapi.co/api/v2/pokemon/?limit=2000").json())["results"]

        # TODO: Can the below be done better? Tidier? More modular?
        # Is it slow given it pulls all this data when the user hits enter?
        def get_pokemon_url(search_term):
            for pokemon in all_pokemon:
                if (pokemon['name'].find(search_term) >= 0):
                    found_pokemon_url = pokemon['url']
                    return found_pokemon_url

        data = requests.get(get_pokemon_url(search_term)).json()

        return render_template('homepage.html', found_pokemon = data, all_pokemon = all_pokemon)
    else: 
        # do something
        return render_template('homepage.html')