n,k = map(int, input().split())
theorems = [int(i) for i in input().split()]
wake = [int(i) for i in input().split()]
acu = 0
for i in range(n):
    if wake[i] == 1:
        acu += theorems[i]
    elif i < k:
        acu += theorems[i]

ans = acu
j = k
ans = acu 

for i in range(n-k):
    if wake[i] == 0:
        acu -= theorems[i]
    if wake[j] == 0:
        acu += theorems[j]
    ans = max(ans,acu)
    j += 1

print(ans)