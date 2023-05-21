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
