n = int(input())
for i in range(n):
        notas = list(map(int, input().split()))
        promedio = (sum(notas)-notas[0])/notas[0]
        estudiantesMaquinas = []
        for j in range(1,len(notas)):
                if promedio < notas[j]:
                        estudiantesMaquinas.append(notas[j])
        print("{0:.3f}".format(len(estudiantesMaquinas)/notas[0] * 100),end="")
        print("%")