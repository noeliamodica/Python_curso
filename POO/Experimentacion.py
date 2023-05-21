
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y."
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X."
        else:
            if self.x > 0 and self.y > 0:
                return "El punto está en el primer cuadrante."
            elif self.x < 0 and self.y > 0:
                return "El punto está en el segundo cuadrante."
            elif self.x < 0 and self.y < 0:
                return "El punto está en el tercer cuadrante."
            else:
                return "El punto está en el cuarto cuadrante."

    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return Punto(vector_x, vector_y)

    def distancia(self, otro_punto):
        distancia_x = otro_punto.x - self.x
        distancia_y = otro_punto.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return distancia


class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

# Ejemplo de uso
punto1 = Punto(3, 5)
punto2 = Punto(-2, -7)
print(punto1)
print(punto2)
print(punto1.cuadrante())
print(punto2.cuadrante())
vector_resultante = punto1.vector(punto2)
print(vector_resultante)
distancia = punto1.distancia(punto2)
print("La distancia entre los puntos es:", distancia)

rectangulo = Rectangulo(punto1, punto2)
print("Base:", rectangulo.base())
print("Altura:", rectangulo.altura())
print("Área:", rectangulo.area())


# Creación de los puntos A, B, C y D
punto_A = Punto(2, 3)
punto_B = Punto(5, 5)
punto_C = Punto(-3, -1)
punto_D = Punto(0, 0)

# Impresión de los puntos por pantalla
print("Punto A:", punto_A)
print("Punto B:", punto_B)
print("Punto C:", punto_C)
print("Punto D:", punto_D)

# Consulta de los cuadrantes de los puntos A, C y D
print("Cuadrante del punto A:", punto_A.cuadrante())
print("Cuadrante del punto C:", punto_C.cuadrante())
print("Cuadrante del punto D:", punto_D.cuadrante())

# Consulta de los vectores AB y BA
vector_AB = punto_A.vector(punto_B)
vector_BA = punto_B.vector(punto_A)
print("Vector AB:", vector_AB)
print("Vector BA:", vector_BA)

# (Optativo) Consulta de la distancia entre los puntos A y B, y B y A
distancia_AB = punto_A.distancia(punto_B)
distancia_BA = punto_B.distancia(punto_A)
print("Distancia entre los puntos A y B:", distancia_AB)
print("Distancia entre los puntos B y A:", distancia_BA)

# (Optativo) Determinar el punto más lejano al origen (0,0)
distancia_A = punto_A.distancia(Punto(0, 0))
distancia_B = punto_B.distancia(Punto(0, 0))
distancia_C = punto_C.distancia(Punto(0, 0))

if distancia_A > distancia_B and distancia_A > distancia_C:
    print("El punto A está más lejos del origen.")
elif distancia_B > distancia_A and distancia_B > distancia_C:
    print("El punto B está más lejos del origen.")
elif distancia_C > distancia_A and distancia_C > distancia_B:
    print("El punto C está más lejos del origen.")
else:
    print("Dos o más puntos tienen la misma distancia al origen.")

# Creación del rectángulo utilizando los puntos A y B
rectangulo_AB = Rectangulo(punto_A, punto_B)

# Consulta de la base, altura y área del rectángulo
print("Base del rectángulo AB:", rectangulo_AB.base())
print("Altura del rectángulo AB:", rectangulo_AB.altura())
print("Área del rectángulo AB:", rectangulo_AB.area())
