import sys

def descomponer_numero(numero):
    numero_str = str(numero)
    longitud = len(numero_str)
    descomposicion = []

    for i in range(longitud):
        ceros = "0" * (longitud - i - 1)
        digito = int(numero_str[i])
        descompuesto = str(digito) + ceros
        descomposicion.append(descompuesto)

    return descomposicion

def mostrar_instrucciones():
    print("Uso: python descomposicion.py [numero]")
    print("Donde [numero] es un número entero positivo.")

# Obtener el argumento del número
if len(sys.argv) > 1:
    try:
        numero = int(sys.argv[1])
        if numero >= 0:
            resultado = descomponer_numero(numero)
            for linea in resultado:
                print(linea)
        else:
            print("Error: El número debe ser positivo.")
    except ValueError:
        print("Error: El argumento no es un número válido.")
else:
    mostrar_instrucciones()
