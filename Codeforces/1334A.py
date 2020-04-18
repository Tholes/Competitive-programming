t = int(input())
for i in range(t):
    n = int(input())
    antX,antY = map(int,input().split())
    ans = True
    if antY > antX:
        ans = False
    for j in range(n-1):
        x,y = map(int,input().split())
        if y > x:
            ans = False
        elif x < antX or y < antY:
            ans = False
        elif abs(y-antY) > abs(antX-x):
            ans = False
        antY = y
        antX = x

    print('YES' if ans else 'NO')
 