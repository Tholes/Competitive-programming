n, b = map(int,input().split())
while n != 0:
    bolsa = list(map(int,input().split()))
    disponibles = {}
    for i in range(b):
        disponibles[bolsa[i]] = 1
    for i in range(b):
        bola1 = bolsa[i]
        for j in range(i+1,b):            
            bola2 = bolsa[j]
            Absoluto = abs(bola1-bola2)
            disponibles[Absoluto] = 1
       
    if len(disponibles) == n+1:
        print("Y")
    else:
        print("N")
    n, b = map(int,input().split())