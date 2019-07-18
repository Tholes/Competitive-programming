n = int(input())
while n != 0:
        word = input()
        contador = 0
        for i in word:
                if i == "D":
                        contador += 1
                        if contador > 3:
                                contador = 0
                else:
                        contador -=1
                        if contador < -3:
                                contador = 0
        if contador == 0 :
                print("N")
        elif contador == 1 or contador == -3:
                print("L")
        elif contador == 2 or contador == -2:
                print("S")
        elif contador == 3 or contador == -1:
                print("O")
        n = int(input())

