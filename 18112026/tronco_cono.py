import math

class TroncoCono:
    def __init__(self, radio_menor, radio_mayor, altura, lado):
        self.radio_menor = radio_menor
        self.radio_mayor = radio_mayor
        self.altura = altura
        self.lado = lado

    def obtener_area_lateral(self):
        return math.pi * (self.radio_mayor + self.radio_menor) * self.lado

    def obtener_area_total(self):
        return math.pi * (self.lado * (self.radio_mayor + self.radio_menor) + self.radio_mayor ** 2 + self.radio_menor ** 2)

    def obtener_volumen(self):
        return (1/3) * math.pi * self.altura * (self.radio_mayor ** 2 + self.radio_menor ** 2 + self.radio_mayor + self.radio_menor)

#Programa Principal
radio_menor = float(input("Ingrese Radio Menor: "))
radio_mayor = float(input("Ingrese Radio Mayor: "))
altura = float(input("Ingrese Altura: "))
lado = float(input("Ingrese Lado: "))

tronco_cono = TroncoCono(radio_menor, radio_mayor, altura, lado)
print(f"Area Lateral: {tronco_cono.obtener_area_lateral()}")
print(f"Area Total: {tronco_cono.obtener_area_total()}")
print(f"Volumen: {tronco_cono.obtener_volumen()}")