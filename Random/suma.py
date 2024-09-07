acum_suma = 0
contador = 0

num = int(input("Ingrese un número: "))

while num != 0:
    if 5 <= num <= 10:
        acum_suma += num
        contador += 1

    if acum_suma == 15:
        print("Se usó el número 5")
    elif acum_suma == 21:
        print("Se usó el número 6")
    elif acum_suma == 28:
        print("Se usó el número 7")
    elif acum_suma == 36:
        print("Se usó el número 8")
    elif acum_suma == 45:
        print("Se usó el número 9")
    elif acum_suma == 55:
        print("Se usó el número 10")

    print("Sumatoria actual: ", acum_suma)
    num = int(input("Ingrese un número entre 5 y 10: "))

print("La sumatoria total es: ", acum_suma)
print("Un total de: ", contador, " sumas.")