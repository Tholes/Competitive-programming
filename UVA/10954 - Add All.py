import heapq
from sys import stdin, stdout
n = int(stdin.readline())
while n !=0:
    cantidad = [int(x) for x in stdin.readline().split()]

    heapq.heapify(cantidad)
    suma = 0
    
    while len(cantidad) > 1:
        ultima = heapq.heappop(cantidad) + heapq.heappop(cantidad)
        suma += ultima
        heapq.heappush(cantidad,ultima)

    stdout.write(str(suma) + "\n") 
    n = int(stdin.readline())