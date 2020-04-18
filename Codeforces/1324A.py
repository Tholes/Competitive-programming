t = int(input())
for i in range(t):
    n = int(input())
    
    blocks = [int(i) for i in input().split()]
    mod = blocks[0] % 2
    ans = False 
    for j in blocks:
        if mod != (j % 2):
            ans = True
            break
    if ans:
        print("NO")
    else:
        print("YES")

    