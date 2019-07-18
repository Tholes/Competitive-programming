def insertionSort(x):
        contador = 0
        for i in range(len(x)):
                k = i
                for j in range(i-1,0-1,-1):
                        
                        if x[k] < x[j]:
                                Aux = x[k]
                                x[k] = x[j]
                                x[j] = Aux
                                k -= 1
                                contador += 1
                        else:  
                                break

        print("Optimal train swapping takes "+repr(contador)+" swaps.")

n = int(input())
for i in range(n):
        nada = input()
        x = list(map(int, input().split()))
        insertionSort(x)
   