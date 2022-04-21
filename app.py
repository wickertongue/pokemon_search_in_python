from flask import Flask
from homepage import home

app = Flask(__name__)

app.register_blueprint(home)