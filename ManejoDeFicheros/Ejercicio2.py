import sys

def incrementar_contador(contador):
    contador += 1
    print("Contador incrementado: ", contador)
    return contador

def decrementar_contador(contador):
    contador -= 1
    print("Contador decrementado: ", contador)
    return contador

def mostrar_contador(contador):
    print("Valor del contador: ", contador)

def guardar_contador(contador):
    try:
        with open("contador.txt", "w") as file:
            file.write(str(contador))
            print("Contador guardado en el archivo.")
    except Exception as e:
        print("Error al guardar el contador en el archivo:", e)

def leer_contador():
    try:
        with open("contador.txt", "r") as file:
            contenido = file.read().strip()
            if contenido:
                contador = int(contenido)
            else:
                contador = 0
    except FileNotFoundError:
        contador = 0
    except Exception as e:
        print("Error: Fichero corrupto.")
        sys.exit(1)
    
    return contador

# Leer el contador del archivo
contador = leer_contador()

# Verificar el argumento pasado al script
if len(sys.argv) > 1:
    argumento = sys.argv[1]
    if argumento == "inc":
        contador = incrementar_contador(contador)
    elif argumento == "dec":
        contador = decrementar_contador(contador)
    else:
        print("Argumento inválido. Uso: contador.py [inc|dec]")
        sys.exit(1)
else:
    mostrar_contador(contador)

# Guardar el contador en el archivo
guardar_contador(contador)
