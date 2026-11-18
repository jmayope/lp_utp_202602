print("Nivel de Masa Muscular")
genero = input("Ingrese el género (M,F): ")
porcentaje = float(input("Ingrese porcentaje de masa muscular: "))

if genero in ('M', 'F'):
    if genero == 'F':
        resultado = "Bajo" if porcentaje < 24 else "Normal" if porcentaje <= 30 else "Alto"
    else:
        resultado = "Bajo" if porcentaje < 34 else "Normal" if porcentaje <= 40 else "Alto"
    print("Nivel de Masa Muscular: ", resultado)
else:
    print("Genero invalido")