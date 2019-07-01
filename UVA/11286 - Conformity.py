def transformada(materias):
    materias = materias.split()
    materias.sort()
    laMateria =""
    for i in materias:
        laMateria +=  i
    return laMateria
n = int(input())
popular = {}
while n != 0:
    laMas = 1
    for i in range(n):
        materias = input()
        materias = transformada(materias)
        
        if materias not in popular:
            popular[materias] = 1
        else:
            popular[materias] += 1
            if popular[materias] > laMas:
                laMas = popular[materias]
    if laMas == 1:
        print(len(popular))
    else:
        cantidad = 0

        for j, k in popular.items():
            if laMas == k:
                cantidad += 1
        
        print(laMas*cantidad)    
    popular.clear()    
    n = int(input())  