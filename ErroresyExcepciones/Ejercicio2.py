lista = [1, 2, 3, 4, 5]

try:
    elemento = lista[10]
except IndexError:
    mensaje = "Error: Índice fuera de rango. El índice solicitado excede el tamaño de la lista."
    print(mensaje)
