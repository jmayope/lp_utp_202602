import math

class Icosaedro:
    def __init__(self, arista):
        self.arista = arista

    def obtener_area(self):
        return 5 * math.sqrt(3) * math.pow(self.arista, 2)

    def obtener_volumen(self):
        return (5/12)*(3*math.sqrt(5))*math.pow(self.arista,3)

# Programa Principal
arista = float(input("Ingrese arista: "))
icosaedro = Icosaedro(arista)
print(f"Area de Icosaedro: {icosaedro.obtener_area()}")
print(f"Volumen de Icosaedro: {icosaedro.obtener_volumen()}")
