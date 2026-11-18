import math

class Prisma:
    def __init__(self, vertices, ancho, largo, altura, lado = None):
        self.vertices = vertices
        self.ancho = ancho
        self.largo = largo
        self.altura = altura
        self.lado = lado

    def obtener_tipo(self):
        if self.vertices == 8:
            if self.lado is None:
                return "Prisma Rectangular"
            else:
                return "Cubo"
        elif self.vertices == 6:
            return "Prisma Triangular"
        elif self.vertices == 10:
            return f"Prisma cuya base es un poligono de {self.vertices} lados"
        else:
            return "No es un prisma"

    def obtener_area_lateral(self):
        if self.vertices == 8:
            if self.lado is None:
                return 2 * (self.ancho * self.largo ) * self.altura
            else:
                return 4 * self.largo ** 2
        elif self.vertices == 6:
            return (self.vertices / 2) * self.lado * self.altura
        elif self.vertices == 10:
            return (self.vertices / 2) * self.lado * self.altura
        else:
            return "No es un prisma"

    def obtener_area_total(self, area_base = 1):
        if self.vertices == 8:
            if self.lado is None:
                return 2 * (self.ancho + self.largo)*self.altura + 2 * self.ancho * self.largo
            else:
                return 6 * self.lado ** 2
        elif self.vertices == 6:
            return (self.vertices / 2) * self.lado * self.altura + 2 * area_base
        elif self.vertices == 10:
            return (self.vertices / 2) * self.lado * self.altura * 2 * area_base
        else:
            return "No es un prisma"

    def obtener_volument_total(self, area_base = 1):
        if self.vertices == 8:
            if self.lado is None:
                return self.ancho * self.largo * self.altura
            else:
                return self.lado ** 3
        elif self.vertices == 6:
            return area_base *  self.altura
        elif self.vertices == 10:
            return area_base *  self.altura
        else:
            return "No es un prisma"