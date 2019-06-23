from sys import stdin
d1,d2,d3 = map(int,input().split())
print(min(d1,d2+d3)+min(d2+d1,d3)+ min(d3+d1,d2))