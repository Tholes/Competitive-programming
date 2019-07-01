from sys import stdin, stdout
def verificador(numerador,divisor):
    numerador = str(numerador)
    divisor = str(divisor)
    cantidad = [0 for i in range(10)]
    if len(divisor) == 4 or len(numerador)== 4:
        if len(divisor) != len(numerador):
            cantidad[0] = 1
        else: 
            return False
    for j in numerador:
        if cantidad[int(j)] == 1 :
            return False
        else:
            cantidad[int(j)] = 1

    for j in divisor:
        if cantidad[int(j)] == 1 :
            return False
        else:
            cantidad[int(j)] = 1
    return True

lines = stdin.readlines()
for i,line in enumerate(lines):
    if int(line) == 0:
        break
    else:
        if i != 0:
            print()
    numero = int(line)
    este = False
    contador = 0
    for j in range(1234,98765):
        numerador = j * numero
        if numerador > 99999:
            break
        else:
            este = verificador(numerador,j)
            if este:
                contador += 1 
                if len(str(j)) == 4:
                    print(repr(numerador)+ " / 0"+repr(j)+" = "+repr(numero))
                else:
                    print(repr(numerador)+ " / "+repr(j)+" = "+repr(numero))
    if contador == 0:
        print("There are no solutions for "+repr(numero)+".")