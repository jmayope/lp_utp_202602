print("Indice de Masa Corporal (IMC)")
peso = float(input("Ingrese peso: "))
altura = float(input("Ingrese altura: "))
genero = input("Ingrese Genero (M, F): ")

if genero in ('M','F'):    
    imc = peso / altura
    resultado = "Normal"
    if genero == 'M':
        resultado = "Normal" if imc <= 24.9 else "Sobrepeso" if imc <= 29.9 else "Obseo" if imc <= 39.9 else "Obseidad Morbida"
    else:
        resultado = "Peso Bajo" if imc <= 18.5 else "Ideal" if imc <= 24.9 else "Sobrepeso" if imc <= 29.9 else "Obesidad" if imc <= 34.9 else "Obseidad Severa" if imc <= 39.9 else "Obesidad Morbida"
    print("IMC: ", resultado)
else:
    print("genero inválido")
    