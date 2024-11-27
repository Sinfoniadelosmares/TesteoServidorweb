import requests

# URL base de la API
url_base = "https://testeoservidorweb.onrender.com/usuarios"

# 1. Crear un Usuario (POST)
def crear_usuario(nombre, edad):
    data = {
        "nombre": nombre,
        "edad": edad
    }
    response = requests.post(url_base, json=data)
    
    # Verificar si la respuesta es válida y si es JSON
    if response.status_code == 201:
        try:
            print("Crear Usuario:", response.json())
        except ValueError:
            print("La respuesta no es un JSON válido.")
    else:
        print(f"Error {response.status_code}: {response.text}")

# 2. Obtener Todos los Usuarios (GET)
def obtener_usuarios():
    response = requests.get(url_base)
    print("Obtener Todos los Usuarios:", response.json())

# 3. Obtener un Usuario por ID (GET)
def obtener_usuario(id):
    response = requests.get(f"{url_base}/{id}")
    print(f"Obtener Usuario {id}:", response.json())

# 4. Actualizar un Usuario (PUT)
def actualizar_usuario(id, nombre, edad):
    data = {
        "nombre": nombre,
        "edad": edad
    }
    response = requests.put(f"{url_base}/{id}", json=data)
    print(f"Actualizar Usuario {id}:", response.json())

# 5. Eliminar un Usuario (DELETE)
def eliminar_usuario(id):
    response = requests.delete(f"{url_base}/{id}")
    print(f"Eliminar Usuario {id}:", response.json())

# Función para obtener el nombre del usuario por su ID
def Longitudname(id):
    # Hacer una solicitud GET a la URL
    response = requests.get(f"{url_base}/longitud/{id}")
    
    # Asegurarse de que la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el JSON de la respuesta
        data = response.json()
        
        # Extraer el campo "mensaje" del JSON
        if "mensaje" in data:
            return data["mensaje"]
        else:
            return "El campo 'mensaje' no está presente en la respuesta."
    else:
        return f"Error: No se pudo obtener el usuario. Código de estado: {response.status_code}"

# Nueva función para enviar un mensaje
def enviarmensaje(id, mensaje):
    # Obtener el nombre del usuario usando Longitudname
    mensaje_usuario = Longitudname(id)
    
    # Verificar si obtuvimos el nombre del usuario
    if "Error" in mensaje_usuario:
        print(mensaje_usuario)  # Imprimir el error si no se obtuvo el nombre
        return
    
    # Crear un mensaje con el nombre del usuario
    mensaje_completo = f"{mensaje}, {mensaje_usuario}!"
    
    # Enviar el mensaje a la API (se asume que tienes un endpoint para ello)
    data = {
        "mensaje": mensaje_completo
    }
    response = requests.post(f"{url_base}/mensaje", json=data)
    
    # Mostrar la respuesta de la API
    print("Mensaje Enviado:", response.json())

# Probar cada operación
if __name__ == "__main__":
    # Crear un nuevo usuario
    crear_usuario("Juan", 25)

    # Obtener todos los usuarios
    obtener_usuarios()

    # Obtener un usuario específico por ID
    obtener_usuario(1)

    # Actualizar el usuario con ID 1
    actualizar_usuario(1, "Juan Actualizado", 26)

    # Obtener el usuario actualizado
    obtener_usuario(1)

    # Enviar un mensaje al usuario con ID 1
    enviarmensaje(1, "Hola")

    # Eliminar el usuario con ID 1
    eliminar_usuario(1)

    # Intentar obtener el usuario eliminado
    obtener_usuario(1)
