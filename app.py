from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, soy Franco Narvaez. Bienvenido a mi aplicación Flask. Deseo que tengas un gran día."