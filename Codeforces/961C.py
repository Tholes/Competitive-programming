n = int(input())

def sol(matriz):  
    ans = 0
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0 and matriz[i][j] == '0':
                ans += 1
            elif i % 2 == 1 and j % 2 == 1 and matriz[i][j] == '0':
                ans += 1
            elif i % 2 == 1 and j % 2 == 0 and matriz[i][j] == '1':
                ans += 1
            elif i % 2 == 0 and j % 2 == 1 and matriz[i][j] == '1':
                ans += 1
    print(matriz, ans)
    return ans 

first = []
second = []
third = []
fourth = []

for i in range(n):
    first.append(list(input()))
input()
for i in range(n):
    second.append(list(input()))
input()
for i in range(n):
    third.append(list(input()))
input()
for i in range(n):
    fourth.append(list(input()))

ans = sol(first)
ans += sol(second)
ans += sol(third)
ans += sol(fourth)

print(ans)