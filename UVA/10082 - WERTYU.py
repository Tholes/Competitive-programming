from sys import stdin
def nuevaPalabra(line,letras):
    palabra = ""
    for i in line:
        for j,k in enumerate(letras):
            if i == " ":
                palabra += " "
                break
            elif k == i:
                palabra += letras[j-1]
                break

    return palabra
lines = stdin.readlines()
letras= "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
for line in lines:
    print(nuevaPalabra(line,letras))