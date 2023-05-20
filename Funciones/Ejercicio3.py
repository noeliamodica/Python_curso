def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Ejemplo de uso
numeros = [(5, 10), (10, 5), (5, 5)]

for a, b in numeros:
    resultado = relacion(a, b)
    print(f"La relación entre {a} y {b} es: {resultado}")
