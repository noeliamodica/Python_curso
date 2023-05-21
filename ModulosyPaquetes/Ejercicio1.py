def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None
