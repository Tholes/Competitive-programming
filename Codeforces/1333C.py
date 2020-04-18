n = int(input())
number = [int(i) for i in input().split()]
found = {}
count = total = 0

for i in number:
    if i != 0:
        count += 1
        aux = i - total
        if aux != 0:
            count += 1

        if aux not in found:
            found[aux] = count
