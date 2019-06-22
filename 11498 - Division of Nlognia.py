n = int(input())
while n!=0:
    origenX, origenY = map(int,input().split())
    for i in range(n):
        puntoX, puntoY = map(int,input().split())
        if puntoX > origenX and puntoY > origenY:
            print("NE")
        elif puntoX > origenX and puntoY< origenY:
            print("SE")
        elif puntoX < origenX and puntoY<origenY:
            print("SO")
        elif puntoX < origenX and puntoY > origenY:
            print("NO")
        else:
            print("divisa")
    n=int(input())