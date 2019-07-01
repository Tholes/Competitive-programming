n = int(input())
contenedor = {}
contenedor[n] = n
while True: 
    n += 1
      
    while n % 10 == 0:
        n /= 10
        
    if n in contenedor:
        break
    contenedor[n] = n
    
print(len(contenedor))