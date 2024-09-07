respuesta = input("¿Desea ingresar datos? (si/no): ")

contador = 0
acum = 0

while respuesta.lower() == "si":
    nombre = input("Ingrese el nombre del alumno: ")
    carrera = input("Ingrese la carrera: ")
    calif1 = int(input("Ingrese la calificación 1: "))
    calif2 = int(input("Ingrese la calificación 2: "))
    calif3 = int(input("Ingrese la calificación 3: "))
    proyecto = int(input("Ingrese la calificación del proyecto final: "))

    promedio_parcial = (calif1 + calif2 + calif3) / 3
    print(f"Promedio de parciales: {promedio_parcial:.2f}")

    calif_final = (promedio_parcial + proyecto) / 2

    if calif_final < 80 and proyecto > 50:
        print("Presenta Extraordinario")

    print(f"Calificación final: {calif_final:.2f}")

    contador += 1
    acum += calif_final

    respuesta = input("¿Desea ingresar más datos? (si/no): ")

if contador > 0:
    promedio_alumnos = acum / contador
    print(f"Promedio de los alumnos ingresados: {promedio_alumnos:.2f}")
