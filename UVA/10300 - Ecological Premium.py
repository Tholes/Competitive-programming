n = int(input())
for i in range(n):
    granjeros = int(input())
    suma = 0
    for i in range(granjeros):
        corral, animales, medioAmbiente = map(int,input().split())
        suma += corral*medioAmbiente
    print(suma)