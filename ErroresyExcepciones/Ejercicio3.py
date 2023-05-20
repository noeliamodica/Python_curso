colores = { 'rojo': 'red', 'verde': 'green', 'negro': 'black' }

try:
    color = colores['blanco']
except KeyError:
    mensaje = "Error: Clave no encontrada. La clave solicitada no existe en el diccionario."
    print(mensaje)
