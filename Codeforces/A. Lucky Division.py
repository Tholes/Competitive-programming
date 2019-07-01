from sys import stdin,stdout
luckyNumbers = {4:4,7:7,44:44,47:47,74:74,77:77,444:444,447:447,474:474,477:477,744:744,747:747,774:774,777:777}
numero = int(stdin.readline())
if numero in luckyNumbers:
    print("YES")
else:
    flag = True
    for i,j in luckyNumbers.items():
        if numero % i == 0:
            print("YES")    
            flag = False
            break
    if flag:
        print("NO")