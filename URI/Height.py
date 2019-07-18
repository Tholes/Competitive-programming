from sys import stdin
n = int(stdin.readline())

for i in range(n):
        stdin.readline()
        resultado =""
        numeros = map(int,stdin.readline().split())       
        comparador = [0 for i in range(231)]
        for i in numeros:
                comparador[i] = comparador[i] + 1
        
        for i in range(20,len(comparador)):
                for j in range(comparador[i]):
                        resultado += repr(i) + " "
                        
        print(resultado[:-1])