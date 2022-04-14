from flask import Flask
from pokemon_search import pokemon_search
from homepage import home

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(pokemon_search)