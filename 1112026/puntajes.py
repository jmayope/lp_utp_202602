def contador_puntaje(puntaje):
    print(f"Cantidad de veces de puntaje ({puntaje}) : ", puntajes.count(puntaje))

def posicion_de(puntaje):
    resultado =  f"La posición de {puntaje} es: {puntajes.index(puntaje) + 1}" if puntajes.index(puntaje) != -1 else f"No se encontro el puntaje."
    print(resultado)

def eliminar_ultimo():
    puntajes.pop()

def mostrar():
    print("Puntajes: ", puntajes)

puntajes = [350, 420, 500, 420, 610, 420, 750]

contador_puntaje(420)
posicion_de(610)
eliminar_ultimo()
mostrar()
