lista = [1,8,3,5,7,2,4,6]

# for i in lista:
#     print(i)

# def devuelveString():
#    i = 0
#    while i < len(lista): 
#     print(f"Hay un total de 8 elementos, los cuales son: {lista[i]}")       
#     i +=1
# devuelveString()

# lista.sort()
# print (lista)

# print(len(lista))

i = 0
num_buscar = int(input("Ingrese el num a buscar"))
no_encontro = True

if num_buscar in lista:
    print(f"Encontré el num {num_buscar}")
    no_encontro = False


if no_encontro:
  print(f"No se encontró el num dentro de la lista")