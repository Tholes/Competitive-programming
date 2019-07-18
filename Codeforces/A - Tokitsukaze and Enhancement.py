from sys import stdin
mayor = {0:"A" , 1:"B" , 2:"C" , 3:"D"}
 
 
def div(n):
    if n % 4 == 1:
        return 0
    if n % 4  == 3:
        return 1
    if n % 4 == 2:
        return 2
    if n % 4 == 0:
        return 3
n = int(stdin.readline())
ma = min(div(n),div(n+1), div(n+2))
if ma == div(n):
    print(0,mayor[ma])
elif ma == div(n+1):
    print(1, mayor[ma])
elif ma == div(n+2):
    print(2, mayor[ma])