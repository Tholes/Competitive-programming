from sys import stdin
n = int(stdin.readline())
numeros = [int(x) for x in stdin.readline().split()]
numeros.sort()
dia = 1
contador = 0
for i in numeros:
    if i >= dia:
        dia += 1
        contador += 1

print(contador)