def nuevaPalabra(palabra):
    x = list()
    for i in palabra:
        x.append(i)
    x.sort()
    nuevaPa = ""
    for i in x:
        nuevaPa += i
    return nuevaPa
    

noAnagramas = list()
linea = input()
diccionario = ""
while linea != "#": 
    diccionario += " "+ linea
    linea = input()

diccionario = list(diccionario.split())
for i in range(len(diccionario)):
        palabra1 = nuevaPalabra(diccionario[i].lower())
        parecidas = 0
        for j in range(len(diccionario)):
            palabra2 = nuevaPalabra(diccionario[j].lower())
            if palabra1 == palabra2:
                parecidas += 1
        if parecidas == 1:
            noAnagramas.append(diccionario[i])

noAnagramas.sort()
for i in noAnagramas:
    print(i)

