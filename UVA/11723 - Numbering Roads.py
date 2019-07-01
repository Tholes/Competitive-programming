street, name = map(int,input().split())
caso = 0
while street != 0 and name != 0:
    caso += 1
    sufijos = 0
    verdad = False
    if street <= name:
        print("Case "+repr(caso)+": "+repr(sufijos))
    else:
        necesarios = 0
        for i in range(2,28):
            necesarios = name*i
            sufijos += 1
            if necesarios >= street:
                verdad = True
                break
        if verdad:
            print("Case "+repr(caso)+": "+repr(sufijos))
        else:
            print("Case "+repr(caso)+": impossible")
    
    street, name = map(int,input().split())