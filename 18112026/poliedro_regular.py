import math

class PoliedroRegular:
    def __init__(self, arista, vertices):
        self.arista = arista
        self.vertices = vertices

    def obtener_area_superficie_exterior(self):
        if self.arista == 12 and self.vertices == 8:
            return 6 * self.arista ** 2
        elif self.arista == 6:
            return math.sqrt(3) * self.arista ** 2
        elif self.arista == 30 and self.vertices == 30:
            return 3 * math.sqrt(25 + 10 * math.sqrt(5)) * self.arista ** 2
        elif self.arista == 30 and self.vertices == 12:
            return 5 * math.sqrt(3) * self.arista ** 2
        elif self.arista == 12 and self.vertices == 6:
            return 2 * math.sqrt(3) * self.arista ** 2
        else:
            return "No es un Poliedro Regular"

    def obtener_volumen(self):
        if self.arista == 12 and self.vertices == 8:
            return self.arista ** 3
        elif self.arista == 6:
            (math.sqrt(2)/12) * self.arista ** 3
        elif self.arista == 30 and self.vertices == 30:
            return math.sqrt((15 + 7 * math.sqrt(5))/4) * self.arista ** 3
        elif self.arista == 30 and self.vertices == 12:
            return (5 * math.sqrt(3 + math.sqrt(5))/12)  * self.arista ** 3
        elif self.arista == 12 and self.vertices == 6:
            return (math.sqrt(2)/3) * self.arista ** 3
        else:
            return "No es un Poliedro Regular"

    def obtener_radio_esfera_circunscrita(self):
        if self.arista == 12 and self.vertices == 8:
            return (math.sqrt(3)/2)*self.arista
        elif self.arista == 6:
            return (math.sqrt(6)/4) * self.arista
        elif self.arista == 30 and self.vertices == 30:
            return (math.sqrt(15)+math.sqrt(3)/4) * self.arista
        elif self.arista == 30 and self.vertices == 12:
            return (math.sqrt(10 + 2 * math.sqrt(5))/4) * self.arista
        elif self.arista == 12 and self.vertices == 6:
            return (math.sqrt(2)/2) * self.arista
        else:
            return "No es un Poliedro Regular"

    def obtener_radio_esfera_inscrita(self):
        if self.arista == 12 and self.vertices == 8:
            return (1/2)*self.arista
        elif self.arista == 6:
            return (math.sqrt(6)/12) * self.arista
        elif self.arista == 30 and self.vertices == 30:
            return math.sqrt((250 + 110 * math.sqrt(5))/20) * self.arista
        elif self.arista == 30 and self.vertices == 12:
            return math.sqrt((42 + 18 * math.sqrt(5))/12) * self.arista
        elif self.arista == 12 and self.vertices == 6:
            return (math.sqrt(6)/6) * self.arista
        else:
            return "No es un Poliedro Regular"