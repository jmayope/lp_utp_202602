def nuevo():
    nuevo_registro = input("Ingrese nuevo distrito: ")
    distritos.append(nuevo_registro)

def revertir_orden():
    distritos.sort(reverse=True)

def cantidad():
    print("Cantidad de Distritos: ", len(distritos))

def mostrar():
    print("Distritos: ", distritos)


distritos = ["El Tambo", "Huancayo", "Chilca", "Sapallanga", "Pilcomayo"]
nuevo()
mostrar()
cantidad()
revertir_orden()
mostrar()
