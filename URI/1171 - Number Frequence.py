n = int(input())
numeros = {}
aux = 0
for i in range(n):
        aux = int(input())
        if aux not in numeros:
                numeros[aux] = 1
        else: 
                numeros[aux] = numeros[aux] + 1

for k,v in sorted(numeros.items()):
        print(repr(k)+" aparece "+ repr(v) +" vez(es)" )