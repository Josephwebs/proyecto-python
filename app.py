def login(username, password):
# Lógica ficticia de autenticación
    if username == "admin" and password == "1234":
        return "Autenticación exitosa"
    else:
        return "Credenciales incorrectas"

if __name__ == "__main__":
# Simulación de login
    print(login("admin", "1234"))