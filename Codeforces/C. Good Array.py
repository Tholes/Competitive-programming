from sys import stdin
tam = int(stdin.readline())
array = [int(x) for x in stdin.readline().split()]
suma = sum(array)
test = sorted(array)[-2:]
ans = []
for i,c in enumerate(array):
    if c != test[1]:
        if suma - c == 2*test[1]:
            ans.append(i+1)
    else:
        if suma - c == 2*test[0]:
            ans.append(i+1)

print(len(ans))
print(*ans)
