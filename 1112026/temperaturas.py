def mayor():
    print("Temperatura mayor: ", max(temperaturas))

def menor():
    print("Temperatura menor: ", min(temperaturas))

def suma():
    print("Suma de Temperaturas: ", sum(temperaturas))

def promedio():
    print("Promedio de Temperaturas: ", sum(temperaturas)/len(temperaturas))

temperaturas = [25.5, 27.0, 24.8, 28.2, 26.4, 29.1, 27.8]
mayor()
menor()
suma()
promedio()