pu = 0
subtotal = 0
descuento = 0
iva = 0
total_pagar = 0
total_pagar_acum = 0
cantidad = 0
ventas = 0
resp = ""

resp = "SI"
total_pagar_acum = 0
ventas = 0

ventas = int(input("¿Cuantas veces quieres realizar el proceso? "))

for i in range(ventas):
    pu = float(input("Precio Unitario: "))
    cantidad = int(input("Cantidad: "))
    
    subtotal = pu * cantidad

    if cantidad > 5:
        descuento = subtotal * 0.10
    else:
        descuento = subtotal * 0.05

    iva = (subtotal - descuento) * 0.16

    total_pagar = subtotal - descuento + iva

    total_pagar_acum += total_pagar

print("El número de ventas que se realizaron fueron:", ventas)
print("Y el total de las ventas es: $", total_pagar_acum)
