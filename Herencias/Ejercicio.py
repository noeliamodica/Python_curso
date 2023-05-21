# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Subclase Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"

# Subclase Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}"

# Subclase Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}"

# Crear objetos de cada subclase y añadirlos a una lista llamada vehiculos
vehiculo1 = Coche("Ford", "Mustang", "Rojo")
vehiculo2 = Moto("Honda", "CBR", 1000)
vehiculo3 = Bicicleta("Specialized", "Epic", "Montaña")

vehiculos = [vehiculo1, vehiculo2, vehiculo3]

# Función catalogar para mostrar los vehículos
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(type(vehiculo).__name__, vehiculo)
    else:
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__, vehiculo)

# Prueba de la función catalogar con diferentes valores de ruedas
catalogar(vehiculos)
print()
catalogar(vehiculos, 0)
print()
catalogar(vehiculos, 2)
print()
catalogar(vehiculos, 4)
