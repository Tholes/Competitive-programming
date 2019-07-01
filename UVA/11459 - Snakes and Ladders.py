casos = int(input()) 
for i in range(casos):  
    jugadores, sol, tiradas = map(int,input().split())

    token = [1 for i in range(jugadores)]
    continuar = True
    snakesOrLadders = {}
    for i in range(sol):
            inicio, fin = map(int,input().split())
            snakesOrLadders[inicio] = fin

    for i in range(tiradas):
        if continuar:
            token[i % jugadores] += int(input())
            
            if token[i % jugadores] in snakesOrLadders:
                token[i % jugadores] = snakesOrLadders[token[i % jugadores]]

            if token[i % jugadores] >= 100:
                token[i % jugadores] = 100
                continuar = False

        else:
            input()
    for i in range(len(token)):
        print("Position of player "+ repr(i+1)+" is "+repr(token[i])+".")
