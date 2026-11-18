import math

class Ortoedro:
    def __init__(self, ancho, largo, altura):
        self.ancho = ancho
        self.largo = largo
        self.altura = altura

    def obtener_diagonal_mayor(self):
        return math.sqrt(math.pow(self.ancho,2)+math.pow(self.largo,2)+math.pow(self.altura,2))

    def obtener_area(self):
        return 2 * (self.ancho * self.largo + self.ancho * self.altura + self.largo * self.altura)

    def obtener_volumen(self):
        return self.ancho * self.largo * self.altura

# Programa Principal

ancho = float(input("Ingrese ancho: "))
largo = float(input("Ingrese largo: "))
altura = float(input("Ingrese altura: "))

ortoedro = Ortoedro(ancho, largo, altura)
print(f"Diagonal Mayor: {ortoedro.obtener_diagonal_mayor()}")
print(f"Area: {ortoedro.obtener_area()}")
print(f"Volumen: {ortoedro.obtener_volumen()}")
