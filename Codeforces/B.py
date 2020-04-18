n = int(input())
for i in range(n):
    a,b,p = map(int,input().split())
    s = input()
    tamS = len(s)
    ans = tamS - 1 
    acu = 0
    for i in range(tamS-2,-1,-1):
        if i == tamS - 2 or s[i] != s[i+1]:
            acu += a if s[i] == 'A' else b
            
        if acu <= p:
            ans = i
        else:
            break   

    print(ans + 1)

            