def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

# Ejemplo de uso
numero = 15
limite_inferior = 0
limite_superior = 10
resultado = recortar(numero, limite_inferior, limite_superior)
print("El número recortado es:", resultado)
