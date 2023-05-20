def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError("Imposible añadir elementos duplicados => {}".format(el))
        else:
            lista.append(el)
    except ValueError as error:
        print("Error:", error)

# Ejemplo de uso
elementos = [1, 5, -2]
agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")

print(elementos)
