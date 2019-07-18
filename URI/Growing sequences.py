n = int(input())
respuesta = ""
while n != 0:
        for i in range(1,n+1):
                if i != n:
                        respuesta += repr(i) + " "
                else: 
                        respuesta += repr(i)
        respuesta +=  "\n"
        n = int(input())
respuesta.rsplit("\n")        
print(respuesta[:-1])
