t = int(input())
for i in range(t):
    n = int(input())
    numbers = [int(i) for i in input().split()]
    dice = {}
    m = 0
    for i in numbers:
        if i in dice:
            dice[i] += 1
        else:
            dice[i] = 1
        m = max(m, dice[i])
    tam = len(dice) - 1
    if tam < m:
        m -= 1
        tam += 1
    print(min(m,tam)) 
    
        
