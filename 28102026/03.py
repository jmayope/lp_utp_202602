print("Estado de Salud")
genero = input("Ingrese el género (M,F): ")
agua = float(input("Rango optimo de agua: "))
musculo = float(input("Rango optimo muscular: "))

if genero in ('M', 'F'):
    if genero == 'F':
        resultado_agua = "Alto" if agua < 49 else "Moderado" if agua < 52 else "Normal" if agua < 58 else "Buena"
        resultado_muscular = "Alto" if musculo < 32 else "Moderado" if musculo < 34 else "Normal" if musculo < 38 else "Buena"
    if genero == 'M':
        resultado_agua = "Alto" if agua < 55 else "Moderado" if agua < 57 else "Normal" if agua < 63 else "Buena"
        resultado_muscular = "Alto" if musculo < 42 else "Moderado" if musculo < 42 else "Normal" if musculo < 46 else "Buena"
    print("Resultado agua: ", resultado_agua)
    print("Resultado muscular: ", resultado_muscular)
else:
    print("Genero invalido")