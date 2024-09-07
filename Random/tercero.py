lista = []


def llenado(lista):
    if lista == []:  
        print("La lista está vacía.Ingrese palabras o frases")
        while True:
            entrada = input("Ingresa una palabra o frase (o 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            lista.append(entrada)
    return lista


lista = llenado(lista)


print("La lista final es:", lista)

