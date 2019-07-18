while True:
        try:
                a,b = map(int,input().split())
                suma = (b*(b+1)/2) - (a*(a+1)/2) + a
                print(int(suma))
        except EOFError:
                break