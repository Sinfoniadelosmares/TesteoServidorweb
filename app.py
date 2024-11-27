from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo (lista de usuarios en memoria)
usuarios = []
@app.route("/")
def index():
    return "Bienvenido ala api"
# Endpoint para crear un usuario
@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    nuevo_usuario = request.get_json()
    print("Datos recibidos para crear usuario:", nuevo_usuario)  # Verifica los datos recibidos
    nuevo_usuario["id"] = len(usuarios) + 1  # Asigna un ID único
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201

# Obtener todos los usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

# Obtener un usuario por ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Actualizar un usuario por ID
@app.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        datos = request.get_json()
        usuario.update(datos)
        return jsonify({"mensaje": "Usuario actualizado exitosamente", "usuario": usuario})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Obtener longitud del nombre del usuario por ID
@app.route("/usuarios/longitud/<int:id>", methods=["GET"])
def Longituddenombre(id):
    # Buscar al usuario por su ID
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        # Crear un mensaje que incluya el nombre del usuario
        return jsonify({"mensaje": f"Hola {usuario['nombre']}, sabías que tu nombre tiene {len(usuario['nombre'])} caracteres? No es curioso?"})
    else:
        # Si el usuario no existe
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Recibir un mensaje
@app.route("/usuarios/mensaje", methods=["POST"])
def recibir_mensaje():
    # Obtener el JSON del cuerpo de la solicitud
    datos = request.get_json()
    
    # Verificar que el mensaje esté presente en los datos enviados
    if "mensaje" in datos:
        mensaje = datos["mensaje"]
        return jsonify({
            "estado": "éxito",
            "mensaje": f"Recibí tu mensaje: {mensaje}"
        }), 200
    else:
        return jsonify({
            "estado": "error",
            "mensaje": "No se envió ningún mensaje"
        }), 400

# Eliminar un usuario por ID
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        usuarios.remove(usuario)
        return jsonify({"mensaje": "Usuario eliminado exitosamente"})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
