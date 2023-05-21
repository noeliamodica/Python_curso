def modificar(lista):
    # Crear una copia de la lista original
    nueva_lista = lista.copy()

    # Borrar los elementos duplicados
    nueva_lista = list(set(nueva_lista))

    # Ordenar la lista de mayor a menor
    nueva_lista.sort(reverse=True)

    # Eliminar todos los números impares
    nueva_lista = [num for num in nueva_lista if num % 2 == 0]

    # Realizar una suma de todos los números que quedan
    suma = sum(nueva_lista)

    # Añadir la suma como primer elemento de la lista
    nueva_lista.insert(0, suma)

    # Devolver la lista modificada
    return nueva_lista

# Ejemplo de uso
lista = [5, 3, 2, 5, 8, 2, 9, 1, 8]
nueva_lista = modificar(lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))
