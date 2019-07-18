from sys import stdin
casos = int(stdin.readline())
difTime= [int(x) for x in stdin.readline().split()]
a,b = [int(x)-1 for x in stdin.readline().split()]
tiempo = 0
contador = 0
for i in range(a,b):
    tiempo += difTime[i]
print(tiempo)