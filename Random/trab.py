
total_trabajadores = 0
total_aumento = 0

while True:
    nombre = input("Ingrese su nombre: ")
    horas = float(input("Ingrese horas trabajadas: "))
    sueldo = float(input("Ingrese sueldo por hora: "))

    if horas == 10:
        aumento = sueldo * 0.20
    elif horas == 15:
        aumento = sueldo * 0.30
    elif horas == 20:
        aumento = sueldo * 0.15
    else:
        aumento = sueldo * 0.08

    total_trabajadores += 1
    total_aumento += aumento

    print("Total de trabajadores ingresados:", total_trabajadores)
    print("Aumento:", aumento)

    sueldo_neto = sueldo + aumento
    print("Sueldo neto =", sueldo_neto)

    respuesta = input("Desea ingresar otro trabajador? (si/no): ").lower()
    if respuesta == "no":
        break

print("Total de trabajadores procesados:", total_trabajadores)
print("Total de aumento acumulado:", total_aumento)
