n = int(input())
contador = 0
while n != 0:
        for i in range(n):
                nota = list(map(int,input().split()))
                letras = ["A","B","C","D","E"]
                for j in range(5):
                        
                        if nota[j] <= 127:
                                contador += 1
                                cual = j

                if contador == 1:
                        print(letras[cual])
                else: 
                        print("*")
                contador = 0
                                                      
        n = int(input())
                        