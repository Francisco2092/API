from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.get_json()
    cursor = db.cursor()
    query = "INSERT INTO usuarios (nombre, edad, email) VALUES (%s, %s, %s)"
    values = (data['nombre'], data['edad'], data['email'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Usuario agregado correctamente"})

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    cursor = db.cursor()
    query = "UPDATE usuarios SET edad = %s WHERE id = %s"
    values = (data['edad'], id)
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Usuario actualizado correctamente"})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    cursor = db.cursor()
    query = "DELETE FROM usuarios WHERE id = %s"
    value = (id,)
    cursor.execute(query, value)
    db.commit()
    return jsonify({"message": "Usuario eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
