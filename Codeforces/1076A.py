n = int(input())
s = list(input())
maxi = []
maxi.append([0,s[0]])
maxi.append(-1)
for i in range(1,n):
    if s[i] > maxi[0][1]:
        maxi[0] = [i,s[i]]
    if s[i-1] > s[i]:
        if maxi[1] == -1:
            maxi[1] = i-1
ans1 = s.copy()
ans2 = s.copy()
ans1.pop(maxi[0][0])
ans2.pop(maxi[1])
ans1 = ''.join(ans1)
ans2 = ''.join(ans2)
print(ans1 if ans1 < ans2 else ans2 )
