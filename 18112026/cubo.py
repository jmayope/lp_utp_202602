import math

class Cubo:
    def __init__(self, lado):
        self.lado = lado

    def obtener_diagonal_mayor(self):
        return math.sqrt(3) * self.lado

    def obtener_area_lateral(self):
        return 4 * math.pow(self.lado, 2)

    def obtener_area_total(self):
        return 6 * math.pow(self.lado, 2)

    def obtener_volumen(self):
        return self.lado**3

#Programa principal
lado = float(input("Ingresar lado: "))
cubo = Cubo(lado)
print(f"Diagonal Mayor: {cubo.obtener_diagonal_mayor()}")
print(f"Area Lateral: {cubo.obtener_area_lateral()}")
print(f"Area Total: {cubo.obtener_area_total()}")
print(f"Volumen: {cubo.obtener_volumen()}")