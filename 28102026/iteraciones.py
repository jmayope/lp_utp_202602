
# suma = 0
# numeros = []
# for i in range(1,6):
#     monto = float(input("Ingresar monto: "))
#     numeros.append(monto)

# print("El total es: ", sum(numeros))
# print("El mínimo es: ", min(numeros))
# print("El máximo es: ", max(numeros))

# otros_numeros = []
# for i in range(1,11):
#     otros_numeros.append(i)

# print(";".join([str(x) for x in otros_numeros]))
# print(";".join([str(x) for x in otros_numeros[::-1]]))

# multiplos = []
# for i in range(1000, 5001):
#     if i % 7 == 0 :
#         multiplos.append(i)

# print("Cantidad: ", len(multiplos))
# print("Suma: ", sum(multiplos))

# signo = -1;
# numeros = []
# for i in range (10, 0, -1):
#     signo = -1 if i % 2 == 0 else 1
#     numeros.append(signo*i**2)

# print(numeros)
    
# [print((i**2)*(-1)**(i+1), end=";") for i in range(10,0,-1)]

# numeros = []
# for i in range(1,7):
#     numero = float(input("Ingrese número: "))
#     numeros.append(numero)

# print("Suma: ", sum(numeros))
# print("Promedio: ", sum(numeros)/len(numeros))
# print("Mínimo: ", min(numeros))
# print("Máximo: ", max(numeros))

# numeros_pares = []
# sw = True
# entrada = input("Ingrese el número inicial (por defecto 1): ")
# numero_inicial = int(entrada) if entrada else 1
# contador = numero_inicial

# while sw:
#     if contador % 2 == 0:
#         numeros_pares.append(contador)
#     contador = contador + 1
#     if len(numeros_pares) == 15:
#         sw = False

# print(";".join([str(x) for x in numeros_pares]))
# print(";".join([str(x) for x in numeros_pares[::-1]]))

# multiplos = []
# for i in range(200, 1001):
#     if i % 9 == 0 :
#         multiplos.append(i)

# print("Cantidad: ", len(multiplos))
# print("Suma: ", sum(multiplos))
# print("Mínimo: ", min(multiplos))
# print("Máximo: ", max(multiplos))
# print("Promedio: ", sum(multiplos)/len(multiplos))

# [print((i**3)*(-1)**(i), end=";") for i in range(11,4,-1)]

# numero = int(input("Ingrese un número: "))
# factorial = 1
# for i in range(numero, 0, -1):
#     factorial = factorial * i

# print("Factorial: ", factorial)

# numero = int(input("Ingrese un número: "))
# divisores = 0
# resultado = "Es primo"
# for i in range(numero, 0, -1):
#     if numero % i == 0:
#         divisores += 1

# if divisores > 2:
#     resultado = "No es primo"

# print("El número ", resultado)

# numero = int(input("Ingrese un número: "))
# es_par = numero % 2 == 0
# resultado = 1
# for i in range(numero, 0, -1):
#     if es_par:
#         resultado = resultado * (i if i % 2 == 0 else 1)
#     else:
#         resultado = resultado * (i if i % 2 != 0 else 1)

# print("Factorial doble: ", resultado)

numero = int(input("Ingrese un número: "))
divisores = []

for i in range(2, numero + 1):
    if i % i == 0:
        divisores.append(i)

print("Cantidad: ", len(divisores))
print("Suma: ", sum(divisores))
print(";".join([str(x) for x in divisores]))