input()
chests = map(int,input().split())
keys = map(int, input().split())
chestsOdd = 0
chestsEven = 0
keyOdd = 0
keyEven = 0
for i in chests:
    if i % 2 == 0: 
        chestsEven += 1
    else: 
        chestsOdd += 1
for i in keys:
    if i % 2 == 0: 
        keyEven += 1
    else: 
        keyOdd += 1
print(min(chestsEven,keyOdd)+ min(chestsOdd,keyEven))