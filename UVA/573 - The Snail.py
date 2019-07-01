altura, subida , bajada , fatiga =  map(int,input().split())
while altura != 0:
    fatiga /= 100
    i = 0
    alturaCaracol = 0
    while True :
        sube = subida - subida*(fatiga*i)
        if sube > 0:
            alturaCaracol += sube
        
        if alturaCaracol > altura:
            i += 1
            print("success on day "+repr(i))
            break       

        alturaCaracol -= bajada           
        i += 1
        if alturaCaracol < 0:
            print("failure on day "+repr(i))
            break
    altura, subida , bajada , fatiga =  map(int,input().split())