t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    numbers = [int(i) for i in input().split()]
    numbers.sort(reverse = True)
    acu = ans = 0 
  
    for i in range(n):
        acu += numbers[i] 
        if acu / (i+1) < x:
            break
        else:
            ans = i+1
    print(ans)