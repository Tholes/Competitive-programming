t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    matriz = [['W' for i in range(m)] for j in range(n)]
    white = n * m
    black = 0
    for j in range(0,n,2):
        for k in range(0,m,2):
            matriz[j][k] = 'B'
            black += 1
            white -= 1

    for j in range(1,n,2):
        for k in range(1,m,2):
            matriz[j][k] = 'B'
            black += 1
            white -= 1
    if black == white + 1:
        for j in range(n):
            print(''.join(matriz[j]))
    else:
        matriz[0][1] = 'B'
        for j in range(n):
            print(''.join(matriz[j]))   
