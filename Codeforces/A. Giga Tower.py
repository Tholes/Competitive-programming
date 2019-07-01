from sys import stdin 
def ocho(numero):
        prueba = str(numero)
        return prueba.find('8')

n = int(stdin.readline())
contador = 0
flag = True
while flag:
        contador += 1
        n += 1
        if ocho(n) >= 0:
                flag = False
print(contador)
                