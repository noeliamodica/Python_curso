texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Separar el texto en tres partes utilizando el carácter "#"
partes = texto.split("#")

# Obtener las frases de cada parte y eliminar los guiones y las comillas
frase1 = partes[0].replace("-", "").strip()
frase2 = partes[1].replace("-", "").strip()
frase3 = partes[2].replace("-", "").strip()

# Crear una lista con las tres frases
frases = [frase1, frase2, frase3]

# Imprimir las frases transformadas
for frase in frases:
    print(frase)
