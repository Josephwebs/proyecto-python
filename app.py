import getpass

# Diccionario de usuarios (username: password)
usuarios = {
    "admin": "1234",
    "usuario1": "abcd",
    "usuario2": "xyz123"
}

# Diccionario para almacenar los intentos fallidos
intentos_fallidos = {}

def login(username, password):
    # Verifica si el usuario está bloqueado
    if intentos_fallidos.get(username, 0) >= 3:
        return "Usuario bloqueado. Contacta con el administrador."

    # Verifica si las credenciales son correctas
    if usuarios.get(username) == password:
        intentos_fallidos[username] = 0  # Reinicia los intentos fallidos
        return "Autenticación exitosa"
    else:
        # Aumenta el contador de intentos fallidos
        intentos_fallidos[username] = intentos_fallidos.get(username, 0) + 1
        return f"Credenciales incorrectas. Intento {intentos_fallidos[username]}/3"

def registrar_usuario(username, password):
    # Verifica si el usuario ya existe
    if username in usuarios:
        return "El nombre de usuario ya existe. Intenta con otro nombre."
    else:
        usuarios[username] = password
        return "Usuario registrado exitosamente"

def menu():
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
    return input("Selecciona una opción: ")

if __name__ == "__main__":
    while True:
        opcion = menu()
        
        if opcion == "1":
            username = input("Nombre de usuario: ")
            password = getpass.getpass("Contraseña: ")  # Oculta la contraseña en la consola
            print(login(username, password))
        
        elif opcion == "2":
            username = input("Nombre de usuario para registrar: ")
            password = getpass.getpass("Contraseña: ")
            confirm_password = getpass.getpass("Confirma la contraseña: ")

            if password == confirm_password:
                print(registrar_usuario(username, password))
            else:
                print("Las contraseñas no coinciden. Inténtalo de nuevo.")

        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
