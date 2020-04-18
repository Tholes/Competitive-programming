t = int(input())
for i in range(t):
    n = int(input())
    move = [int(i) for i in input().split()]
    compair = [int(i) for i in input().split()]
    backNeg = backPos = False
    ans = True
    for j in range(n):
        if move[j] == compair[j]:
            if move[j] > 0:
                backPos = True
            elif move[j] < 0:
                backNeg = True
            continue
        if move[j] < compair[j]:
            if not backPos:
                ans = False
                break
        if move[j] > compair[j]:
            if not backNeg:
                ans = False
                break
        if move[j] > 0:
            backPos = True
        elif move[j] < 0:
            backNeg = True
    print('YES' if ans else 'NO')



        
