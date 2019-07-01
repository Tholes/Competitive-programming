n = int(input())
for i in range(n):
    cantidad = int(input())
    x = list(map(int,input().split()))
    menor = 99
    mayor = 0
    suma = 0
    for i in x:
        suma += i
        if i > mayor:
            mayor = i
        if i< menor:
            menor = i
    suma /= cantidad
    print(int((abs(suma - mayor)+abs(suma-menor))*2))