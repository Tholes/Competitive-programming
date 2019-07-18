from sys import stdin

n = int(stdin.readline())
cantidad = {}
suma = 0
for i in range(0,64+1):
        suma = 2**i
        cantidad[i] = suma/12000
for i in range(n):
        b = int(stdin.readline())   
        print(repr(int(cantidad[b]))+" kg")