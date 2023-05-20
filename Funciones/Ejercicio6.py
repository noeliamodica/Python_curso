def separar(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    pares.sort()
    impares.sort()
    return pares, impares

# Ejemplo de uso
lista = [6, 5, 2, 1, 7]
pares, impares = separar(lista)
print("Números pares:", pares)
print("Números impares:", impares)
