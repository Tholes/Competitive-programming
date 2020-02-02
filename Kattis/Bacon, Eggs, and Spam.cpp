n = int(input())
while n != 0:
    dic = {}
    for i in range(n):
        aux = input().split()
        for i in range(1,len(aux)):
            if(aux[i] in dic):
                dic[aux[i]].append(aux[0])
            else: 
                dic[aux[i]] = [aux[0]]
    for k,v in sorted(dic.items()):
        print(k,' '.join(sorted(dic[k])))

    print()
    n = int(input())