n,m = map(int,input().split())
square = [int(i) for i in input().split()]
ans = 1e9
for i in range(1,n+1):
    ans = min(ans, square.count(i))
print(ans)