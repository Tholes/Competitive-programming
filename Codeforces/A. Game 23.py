x,y = map(int,input().split())
if x == y:
    print(0)
elif y % x != 0:
    print(-1)
else:
    contador = 0
    while x != y:
        if y % (x*2) == 0:
            x *= 2
            contador += 1
        elif y % (x*3) == 0:
            x *= 3
            contador += 1
        else:
            print(-1)
            break
    if x == y:
        print(contador)