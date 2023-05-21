def leer_personas():
    personas = []

    with open("personas.txt", "r", encoding="utf8") as file:
        for line in file:
            line = line.strip()
            if line:
                id, nombre, apellido, nacimiento = line.split(";")
                persona = {
                    "id": id,
                    "nombre": nombre,
                    "apellido": apellido,
                    "nacimiento": nacimiento
                }
                personas.append(persona)

    return personas

def mostrar_personas(personas):
    for persona in personas:
        print("ID: ", persona["id"])
        print("Nombre: ", persona["nombre"])
        print("Apellido: ", persona["apellido"])
        print("Fecha de nacimiento: ", persona["nacimiento"])
        print()

# Leer los datos del archivo y almacenar en la lista personas
personas = leer_personas()

# Mostrar los datos de las personas de forma amigable
mostrar_personas(personas)
