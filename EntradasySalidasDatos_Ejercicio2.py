import sys

# Verificar si se proporcionan los argumentos
if len(sys.argv) != 3:
    print("Uso: python tabla.py [filas] [columnas]")
else:
    # Obtener los argumentos de filas y columnas
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    # Validar que los argumentos sean números enteros positivos del 1 al 9
    if 1 <= filas <= 9 and 1 <= columnas <= 9:
        # Iterar sobre las filas
        for i in range(filas):
            # Iterar sobre las columnas
            for j in range(columnas):
                print(" * ", end='')
            print()  # Salto de línea después de cada fila
    else:
        print("Los argumentos deben ser números enteros positivos del 1 al 9.")

