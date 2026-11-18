def insertar_en(index, item):
    equipos.insert(index, item)

def eliminar(item):
    equipos.remove(item)

def cantidad():
    print("Cantidad de equipos: ", len(equipos))

def mostrar():
    print("Equipos: ", equipos)

equipos = ["Computadora", "Proyector", "Impresora", "Router", "Switch"]
insertar_en(2,"Servidor")
mostrar()
cantidad()
eliminar("Impresora")
mostrar()
cantidad()
mostrar()