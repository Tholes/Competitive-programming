n = int(input())
dinero=0
for i in range(n):
    y = list(input().split())
    if y[0] == "donate":
        dinero += int(y[1])
    else:
        print(dinero)