lista = [1,2,3]
entero = 2
cadena = "Hola que tal"
Logico = True
def tipoEntero():
   print("Soy un numero entero")

def tipoLista():
   print("Soy una lista")

def tipoLogico():
   print("Soy un valor logico")

def tipoCadena():
   print("Soy una cadena")

elemeto = type(input("Ingrese un elemento"))

if elemeto == (type(entero)):
   tipoEntero()
elif elemeto == (type(lista)):
   tipoLista()
elif elemeto == (type(Logico)):
   tipoLogico()
elif elemeto == (type(cadena)):
   tipoCadena()










