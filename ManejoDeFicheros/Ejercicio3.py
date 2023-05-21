import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

class Gestor:
    def __init__(self):
        self.personajes = []
        self.cargar_personajes()

    def cargar_personajes(self):
        try:
            with open("personajes.pckl", "rb") as file:
                self.personajes = pickle.load(file)
        except FileNotFoundError:
            self.personajes = []

    def guardar_personajes(self):
        with open("personajes.pckl", "wb") as file:
            pickle.dump(self.personajes, file)

    def agregar_personaje(self, personaje):
        for p in self.personajes:
            if p.nombre == personaje.nombre:
                print("El personaje '{}' ya existe.".format(personaje.nombre))
                return
        self.personajes.append(personaje)
        self.guardar_personajes()
        print("Personaje '{}' agregado correctamente.".format(personaje.nombre))

    def mostrar_personajes(self):
        if len(self.personajes) == 0:
            print("No hay personajes en el gestor.")
        else:
            print("Personajes en el gestor:")
            for personaje in self.personajes:
                print("Nombre: {}".format(personaje.nombre))
                print("Vida: {}".format(personaje.vida))
                print("Ataque: {}".format(personaje.ataque))
                print("Defensa: {}".format(personaje.defensa))
                print("Alcance: {}".format(personaje.alcance))
                print("-------------------------")

    def borrar_personaje(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar_personajes()
                print("Personaje '{}' borrado correctamente.".format(nombre))
                return
        print("El personaje '{}' no existe.".format(nombre))

# Crear los personajes
caballero = Personaje("Caballero", 4, 2, 4, 2)
guerrero = Personaje("Guerrero", 2, 4, 2, 4)
arquero = Personaje("Arquero", 2, 4, 1, 8)

# Crear el gestor
gestor = Gestor()

# Agregar los personajes al gestor
gestor.agregar_personaje(caballero)
gestor
