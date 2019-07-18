from sys import stdin
n,t,c = [int(i) for i in stdin.readline().split()]
prisioneros = [int(i) for i in stdin.readline().split()]
count = 0
ans = 0
for i in prisioneros:
    if i <= t:
        count += 1
    else:
        count = 0
    if count >=c:
        ans += 1
print(ans)