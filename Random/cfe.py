total_pagar = 0
gasto_luz = 0
basico = 0
intermedio = 0
suma = 0

tarifaB = 0.987
tarifaI = 1.203

print("Calculadora de Pago de Luz")
gasto_luz = float(input("¿Cuánto gastaste de luz en KWH? "))

if gasto_luz >= 150:
    basico = 150 * tarifaB
    intermedio = (gasto_luz - 150) * 1.203
else:
    basico = gasto_luz * tarifaB
    intermedio = 0

suma = basico + intermedio
iva = suma * 0.16
fact_periodo = suma + iva
total_pagar = suma + iva + 12.56

print("El total a pagar por la luz es:", total_pagar)
