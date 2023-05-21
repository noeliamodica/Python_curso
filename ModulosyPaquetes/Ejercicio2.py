import datetime
import time
import os

def clear_screen():
    # Limpiar la pantalla de la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def display_time():
    while True:
        # Obtener la hora actual
        now = datetime.datetime.now()

        # Formatear la hora, minutos y segundos
        time_str = now.strftime("%H:%M:%S")

        # Imprimir el tiempo en la pantalla
        print(time_str)

        # Esperar un segundo antes de actualizar la hora
        time.sleep(1)

        # Limpiar la pantalla antes de imprimir la siguiente hora
        clear_screen()

# Ejecutar el reloj
display_time()
