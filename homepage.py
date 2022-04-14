from flask import Flask, Blueprint, render_template, request

home = Blueprint('home', __name__)

@home.route('/', methods = ['GET', 'POST'])
def return_home():
    return render_template('homepage.html')

@home.route('/post', methods = ['POST'])
def post():
    form_data = request.form
    searched_pokemon = form_data["searchedPokemon"]
    return render_template('response.html', searched_pokemon = searched_pokemon)
