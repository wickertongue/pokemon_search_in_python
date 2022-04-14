from flask import Flask, Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def return_home():
    return render_template('homepage.html')