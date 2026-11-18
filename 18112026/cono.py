import math

class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def obtener_lado(self):
        return math.sqrt(self.radio ** 2 + self.altura ** 2)

    def obtener_area_lateral(self, lado):
        return math.pi * self.radio * lado

    def obtener_area_total(self, lado):
        return math.pi * self.radio * (lado * self.radio)

    def obtener_volumen(self):
        return (math.pi * self.radio ** 2 * self.altura) / 3

#Programa principal
radio = float(input("Ingresar radio: "))
altura = float(input("Ingresar altura: "))

cono = Cono(radio, altura)
lado = cono.obtener_lado()
print(f"Lado Al cuadrado: {lado ** 2}")
print(f"Area Lateral: {cono.obtener_area_lateral()}")
print(f"Area Total: {cono.obtener_area_total()}")
print(f"Volumen: {cono.obtener_volumen()}")