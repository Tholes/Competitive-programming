n = int(input())
for i in range(n):
        aux = input()
        numero1 = int(aux[0])
        numero2 = int(aux[2])
        if aux[1] == aux[1].lower():               
                if numero1 != numero2:
                        print(numero1+numero2)
                else:
                        print(numero1*numero2)
        else:                 
                if numero1 != numero2:
                        print(numero2-numero1)
                else:
                        print(numero1*numero2)