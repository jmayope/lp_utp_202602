import math

class ZonaEsferica:
    def __init__(self, radio_menor, radio_mayor, altura):
        self.radio_menor = radio_menor
        self.radio_mayor = radio_mayor
        self.altura = altura

    def obtener_area(self):
        return 2 * math.pi * self.radio_mayor * self.altura

    def obtener_volumen(self):
        return (1/6) * math.pi * self.altura * (self.altura ** 2 + 3 * self.radio_mayor ** 2 + 3 * self.radio_menor ** 2)

#Programa principal
radio_menor = float(input("Ingrese radio menor: "))
radio_mayor = float(input("Ingrese radio mayor: "))
altura = float(input("Ingrese altura: "))

zona_esferica = ZonaEsferica(radio_menor, radio_mayor, altura)

print(f"Area: {zona_esferica.obtener_area()}")
print(f"Volumen: {zona_esferica.obtener_volumen()}")