from sys import stdin
def ans(x):
    if x  % 2==0:
        return int(x/2)
    else:
        return - x + int((x-1)/2)

casos = int(stdin.readline())
for i in range(casos):
    x,y = map(int,stdin.readline().split())
    print(ans(y) - ans((x-1)))