respuesta = input("Desea ingresar al sistema")
acum_precio_venta = 0.0

while respuesta.lower() == "si":
   marca = input("Ingrese la marca")
   origen = input("Ingrese el origen")
   costo = int(input("Ingrese el costo"))

   if origen.lower() == "alemania":
    impuesto_pagar = 0.20
   elif origen.lower() == "japon":
    impuesto_pagar= 0.30
   elif origen.lower() == "italia":
    impuesto_pagar = 0.15
   elif origen.lower() == "usa":
    impuesto_pagar = 0.08

   impuesto_costo = costo * impuesto_pagar
   precio_venta = costo + impuesto_costo

   print(f"El impuesto a pagar es de: {impuesto_pagar}")
   print(f"Precio total: {precio_venta}")
   respuesta = input("Desea ingresar al sistema otra vez?")
   acum_precio_venta += precio_venta
   
print(f"'Monto final: {acum_precio_venta}")
   


