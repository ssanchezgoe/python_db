# Creación de una instancia de un objeto Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"