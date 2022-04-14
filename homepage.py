from flask import Flask, Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def return_home():
    return "<h1>Pokemon Search!</h1>"