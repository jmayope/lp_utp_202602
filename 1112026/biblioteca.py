def mostrar():
    print("Lista de Libros: ", libros)

def insertar_libro():
    nuevo_libro = input("Ingrese nuevo libro: ")
    libros.append(nuevo_libro)

def cantidad():
    print("Cantidad de libros:", len(libros))

def ordenar():
    libros.sort()


libros = ["Programación", "Base de Datos", "Redes", "Inteligencia Artificial", "Ciberseguridad"]
mostrar()
insertar_libro()
mostrar()
cantidad()
ordenar()
mostrar()