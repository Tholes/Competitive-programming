from sys import stdin
x = [ i for i in stdin.readline().split()]
x.sort()
if x[0] == x[2]:
    print(0)
elif ((int(x[0][0])+ 2) == (int(x[1][0]) + 1) == int(x[2][0])) and (x[0][1] == x[1][1] == x[2][1]) : 
    print(0)
elif x[0][1] == x[1][1] and int(x[1][0]) -  int(x[0][0]) <= 2:
    print(1)
elif x[0][1] == x[2][1] and int(x[2][0]) - int( x[0][0]) <= 2:
    print(1)
elif x[2][1] == x[1][1] and int(x[2][0]) -  int(x[1][0]) <= 2:
    print(1)
else:
    print(2)