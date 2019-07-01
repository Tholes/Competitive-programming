n = int(input())
for i in range(n):  
    x,y = map(int,input().split())   
    if x >= y and ((x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 ==1)):
        p1 = (x+y)/2
        p2 = x - p1
        print(repr(int(p1))+" "+repr(int(p2)))
    else:
        print("impossible")