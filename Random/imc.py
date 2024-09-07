peso = 0
altura = 0
imc = 0

print("Calculadora de IMC (Índice de Masa Corporal)")
peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu estatura (metros): "))

imc = peso / (altura ** 2)

print("Tu IMC es de:", imc)

if imc < 18.50:
    print("Tienes bajo peso")
elif 18.50 <= imc <= 24.99:
    print("Tienes un peso normal")
elif 25 <= imc <= 29.99:
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")
