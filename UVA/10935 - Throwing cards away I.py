def proceso(n):
    sacadas = ""
    cartas = [(i+1) for i in range(n)]
    for i in range(n-1):
        sacadas += " "+repr(cartas.pop(0)) + ","
        cartas.append(cartas.pop(0))       
    print("Discarded cards:"+ sacadas[:-1])
    print("Remaining card: "+repr(cartas.pop(0)))

n = int(input())
while n != 0:
    proceso(n)
    n = int(input())