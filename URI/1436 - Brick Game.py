n = int(input())
for i in range(1,n+1):
    numeros = list(map(int,input().split()))
    numeros.pop(0)
    numeros.sort()
    print("Case "+ repr(i)+":",end=" ")
    print(numeros[int(len(numeros)/2)])