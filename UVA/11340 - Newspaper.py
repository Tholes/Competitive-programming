casos = int(input())
for i in range(casos):
    n = int(input())
    pagadas = {}
    cantidad = 0
    for j in range(n):
        letra, valor = input().split()
        pagadas[letra] = int(valor)
    n = int(input())
    candidatos = ""
    for j in range(n):
        candidatos += input()
    
    for letra, valor in pagadas.items():
        cantidad += candidatos.count(letra) * valor
    cantidad = round(cantidad/100,2)
    cantidad = "{0:.2f}".format(cantidad)
    print(cantidad + "$")