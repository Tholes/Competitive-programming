from sys import stdin
x,y = map(int,stdin.readline().split())
while x != 0:
    menor = min(x,y)
    mayor = max(x,y)
    if menor == 1:
        res = mayor
    elif menor == 2:
        res = 4* int(mayor/4) + 2 * min(2,mayor % 4)
    else:
        res = (x*y+1)/2
    print(repr(int(res)) +" knights may be placed on a "+ repr(x) +" row "+ repr(y) +" column board.")
    x,y = map(int,stdin.readline().split())