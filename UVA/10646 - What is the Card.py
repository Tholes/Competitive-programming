cartas = {'A': 10, 'K': 10, 'J':10, 'Q':10, 'T':10}
n = int(input())
for i in range(n):
    y =  0
    baraja = input().split()
    if len(baraja) != 52:
        baraja += input().split()
   
    for j in range(3):
        carta = baraja.pop(0)
        x = carta[0]
        if x in cartas:
            x = cartas[x]
            y += x
        else:
            x = int(x)
            y += x
        for K in range(10 - x):          
            baraja.pop(0)       
    
    print("Case "+repr(i+1)+": "+baraja[y-1])