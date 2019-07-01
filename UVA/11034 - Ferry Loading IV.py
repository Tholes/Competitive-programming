n = int(input())
for i in range(n):
    longFerry , carros = map(int,input().split())
    left = []
    right = []
    for j in range(carros):
        tamaño, direccion = input().split()
        
        if direccion == "left":
            left.append(int(tamaño))
        else:
            right.append(int(tamaño))
    capacidad = 0
    recorridos = 0

    longFerry = longFerry*100

    while len(left) or len(right):
        capacidad = 0
        if len(left):
            while len(left):
                    if capacidad + left[0] <= longFerry:
                        capacidad += left.pop(0)
                    else:                        
                        break
            recorridos += 1
        else:
            recorridos += 1
            
        if len(left) == 0 and len(right)== 0:
            break

        capacidad = 0

        if len(right):
            while len(right):
                if capacidad + right[0] <= longFerry:
                    capacidad += right.pop(0)
                else:
                    
                    break
            recorridos += 1        
        else:
            recorridos += 1

    print(recorridos)
    