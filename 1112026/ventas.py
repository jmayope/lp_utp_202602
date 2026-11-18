def venta_mayor():
    print("Venta Mayor: ", max(ventas))

def venta_menor():
    print("Venta Menor: ", min(ventas))

def total():
    print("Total Ventas: ", sum(ventas))

def promedio():
    print("Promedio Ventas: ", sum(ventas)/(len(ventas)))

ventas = [1220,900,1234,543]
venta_mayor()
venta_menor()
total()
promedio()