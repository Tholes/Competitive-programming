def strong(x,y,n):
    contador = 0
    for i in range(n):
        if x[i] == y[i]:
            contador += 1            
    return contador

def weak(x,y):
    cantidadP = [0 for i in range(9)]
    suma = 0
    for i in range(len(y)):
        cantidadP[y[i]-1] += 1
    for i in range(9):
        suma += min(cantidadP[i], x[i])
    return suma

game = 1
n = int(input())
while n != 0:
    secretCode = list(map(int,input().split()))
    cantidadCode = [0 for i in range(9)]
    for i in range(n):
        cantidadCode[secretCode[i]-1] += 1

    guess = list(map(int,input().split()))
    print("Game "+repr(game)+":")
    while guess[0] != 0:
        strongs = strong(secretCode,guess,n)
        weaks = weak(cantidadCode,guess) - strongs

        print("    ("+repr(strongs)+","+repr(weaks)+")")
        guess = list(map(int,input().split()))
    game += 1
    n = int(input())