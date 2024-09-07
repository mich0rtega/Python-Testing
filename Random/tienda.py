subtotal = 0
total = 0
precio = 0
descuento = 0
iva = 0
compra = 0
cantidad = 0
ventas = 0
respuesta = ""

while True:
    precio = float(input("Ingresa el precio del artículo: "))
    cantidad = int(input("Ingresa la cantidad del producto: "))
    
    subtotal = precio * cantidad

    if cantidad > 5:
        descuento = subtotal * 0.10
    else:
        descuento = subtotal * 0.05

    iva = subtotal * 0.16

    total = subtotal - descuento + iva

    print("Subtotal:", subtotal)
    print("IVA:", iva)
    print("Descuento:", descuento)
    print("Total:", total)

    respuesta = input("¿Quieres agregar una nueva venta? (Si/No): ").lower()
    if respuesta == "no":
        break

    ventas += 1

print("Cantidad de ventas que se realizaron:", ventas)
print("Total de ventas es de: $", total)
