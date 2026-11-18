def ver():
    print("Productos registradas: ", productos)

def cantidad():
    print("Cantidad de Productos: ", len(productos))

def eliminar(index):
    productos.pop(index)

def ordenar():
    productos.sort()

productos = ["Laptop", "Mouse", "Monitor", "Teclado"]

nuevo_producto = input("Ingresar nuevo producto: ")
productos.append(nuevo_producto)
ver()
cantidad()
ver()
index_producto = int(input("Ingresar posición de producto: "))
if index_producto <= len(productos):
    eliminar(index_producto)
    ver()
else:
    print("No existe el producto en esa posición")

ordenar()
ver()

