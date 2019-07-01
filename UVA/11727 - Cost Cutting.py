n = int(input())
for i in range(1,n+1):
    x = list(map(int,input().split()))
    x.sort()
    print("Case "+repr((i))+": " + repr(x[1]))