# a = int(input("Ingrese el angulo a del triangulo"))
# b = int(input("Ingrese el angulo b del triangulo"))

# if a == b:
#     print("Es un triangulo isoseles")
# else:
#     print("NO es un triangulo isoceles")

def AreaTriangulo():
    base = int(input("Ingrese la base del triangulo"))
    altura = int(input("Ingrese la altura del triangulo"))

    area = (base * altura)/2
    print(area)
AreaTriangulo()
