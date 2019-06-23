from sys import stdin
n = int(stdin.readline())
paisaje = stdin.readlines()
subidas = []
suma = 0
for i in paisaje:
	for j,k in enumerate(i):
		if k == '\\':
			subidas.append(j)
		elif k == '/':
			if len(subidas):
				suma += j - subidas.pop()
		
	print(suma)
	suma = 0
	subidas.clear()