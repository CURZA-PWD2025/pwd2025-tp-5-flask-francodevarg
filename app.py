from flask import Flask

app = Flask(__name__)

productos = [
    {"id": 1, "descripcion": "Zapatillas 32", "categoria_id": 1},
    {"id": 2, "descripcion": "Remera", "categoria_id": 2},
    {"id": 3, "descripcion": "Zapatillas Nike", "categoria_id": 1},
]

categorias = [
    {"id": 1, "descripcion": "Calzado"},
    {"id": 2, "descripcion": "Ropa"},
]


@app.route("/")
def home():
    return "Hola!!! Bienvenido a mi aplicación Flask. Yo soy Franco Narvaez. Deseo que tengas un gran día."

@app.route('/productos')
def listar_productos():
    productos_str = ""
    for producto in productos:
        productos_str += f"ID: {producto['id']} - Descripción: {producto['descripcion']} <br>"
    return productos_str

@app.route('/categorias')
def listar_categorias():
    categorias_str = ""
    for categoria in categorias:
        categorias_str += f"ID: {categoria['id']} - Descripción: {categoria['descripcion']}<br>"
    return categorias_str

if __name__ == '__main__':
    app.run(debug=True)