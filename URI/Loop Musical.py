n = int(input())
while n != 0:
        numeros = list(map(int,input().split()))
        contador = 0
        for i in range(n):
                if numeros[i] > numeros[(i+1)%n]:
                        if numeros[(i+1)%n] < numeros[(i+2)%n]:
                                contador += 1
                elif numeros[i] < numeros[(i+1)%n]:
                        if numeros[(i+1)%n] > numeros[(i+2)%n]:
                                contador += 1                        
        print(contador)
        n = int(input())
