from sys import stdin
n,t = [int(x) for x in stdin.readline().split()]
celdas = []
celdas.append(0)
celdas = [int(x) for x in stdin.readline().split()]
flag = False
acum = 0
while acum != t and acum < n:
    if acum == t:
        flag = True 
        break 
    acum += celdas[acum-1] 
    if acum == t:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")