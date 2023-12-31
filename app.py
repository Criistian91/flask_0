#Servidor
from flask import Flask, jsonify, request
from markupsafe import escape

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página de inicio
# Si no escribo nada, es escribir unicamente el nombre de dominio y puerto
# Ruta de recursos
@app.route('/')
def index():
    return 'Index'

# Hacer Ping→ ←pong 
@app.route('/ping') # Nombre de la ruta
def ping():
    return jsonify({"message": "pong"})

#Asociamos una funcipon
#Utilizar jsonify para convertir un objeto Python en JSON
# Definir una ruta adicional para /ping
@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
   return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id":id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

# GET todos los recursos
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items de este recurso"})

# POST nuevo recurso
@app.route('/recurso', methods = ['POST'])
def post_recursos():
    print(request.get_json())
    # body es el diccionario
    body = request.get_json()
    name = body()["name"]
    modelo = body()["modelo"]
    # insertar en la BD
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})









































# Ejecutar la aplicacion en el modo debuging
# Controlar nombre y garantizar que el archivo se lanze correctamente
# Dejarlo preparado para un futuro
if __name__ == '__main__':
    print(" 6565 ")
    # True: hacer las pruebas en modo de desarrollo
    app.run(debug=True, port=5200)
