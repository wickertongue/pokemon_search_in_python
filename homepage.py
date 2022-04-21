from flask import Flask, Blueprint, render_template, request, redirect, url_for, json
import requests

home = Blueprint('home', __name__)

@home.route('/', methods = ['GET', 'POST'])
def return_home():
    if request.method == "POST":
        searched_pokemon = request.form["searchedPokemon"]
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{searched_pokemon}")
        data = response.json()

        # pokemon_data = json.dumps(data)
        return render_template('homepage.html', found_pokemon = data)
        # return redirect(url_for('pokemon', searched_pokemon = searched_pokemon))
    else: 
        # do something
        return render_template('homepage.html')


# def fetch_pokemon(pokemon):

#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
#     data = response.json()

#     pokemon_data = json.dumps(data)
#     return(data)