t = int(input())
for i in range(t):
    n = int(input())
    quest = [int(i) for i in input().split()]
    ans = False
    end = 0
    for j in range(0,n-2):
        for k in range(j+2,n):
            if quest[j] == quest[k]:
                ans = True
                break
    print("YES" if ans else "NO")
    