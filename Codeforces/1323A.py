t = int(input())
for j in range(t):
    n = int(input())
    conjunto = [int(i) for i in input().split()]
    par = [] 
    impar = []
    for i in range(n):
        if conjunto[i] % 2 == 0:
            par.append([conjunto[i], i+1])
            break
        else:
            impar.append([conjunto[i], i+1])
            if len(impar) == 2:
                break
    if len(par) == 1:
        print(1)
        print(par[0][1])
    elif len(impar) == 2:
        print(2)
        print(impar[0][1], impar[1][1])
    else:
        print(-1)
