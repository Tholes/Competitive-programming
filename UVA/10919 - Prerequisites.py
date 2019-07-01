requerimientos = list(map(int,input().split()))
while requerimientos[0] != 0:
    materias = list(map(int,input().split()))
    materia = {}
    for i in range(requerimientos[0]):
        materia[materias[i]] = 0
    contador = 0
    pasa = True
    for i in range(requerimientos[1]):  
        if pasa:     
            candidato = list(map(int,input().split()))        
            for j in range(2,len(candidato)):

                if candidato[j] in materia:
                    contador += 1
                    
        else:
            input()
        if contador < candidato[1]:
            pasa = False
        contador = 0
    if pasa:
        print("yes")
    else: 
        print("no")

    requerimientos = list(map(int,input().split()))