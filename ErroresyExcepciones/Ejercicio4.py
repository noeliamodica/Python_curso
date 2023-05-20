try:
    resultado = 15 + "20"
except TypeError:
    mensaje = "Error: Tipo de datos incompatible. No se puede realizar la operación entre un número y una cadena de texto."
    print(mensaje)
