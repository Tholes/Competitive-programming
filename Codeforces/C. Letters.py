from sys import stdin
x,y = [int(x) for x in stdin.readline().split()]
tamHabitaciones = [int(x) for x in stdin.readline().split()]
consultas = [int(x) for x in stdin.readline().split()]
dormitorio = 0
habitacion = 0
anterior = 0
for i in consultas:
    while i>habitacion:
        anterior = habitacion
        habitacion += tamHabitaciones[dormitorio]
        dormitorio += 1
    print(dormitorio,i-anterior)
