def ver_notas():
    print("Notas registradas: ", notas)

def cantidad_notas():
    print("Cantidad de Notas: ", len(notas))

def min_nota():
    print("Mínima nota: ", min(notas))

def max_nota():
    print("Máxima nota: ", max(notas))

notas = [12,11,13,14]
ver_notas()
nueva_nota = float(input("Ingresar nueva nota: "))
notas.append(nueva_nota)
ver_notas()
cantidad_notas()
min_nota()
max_nota()

