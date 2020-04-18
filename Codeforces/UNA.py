for i in range(int(input())):
    n = int(input())
    students = [int(i) for i in input().split()]
    ansR = True
    ansNR = True
    uno = students.index(1)
    for i in range(n-1):
        #print(students[(uno + i)%n], (students[(uno+i+1)%n] - 1))
        if students[(uno + i)%n] != (students[(uno+i+1)%n] - 1):
            ansR = False
            break
    #print("SECOND")
    for i in range(n-1):
        #print(students[(uno - i)%n], (students[(uno-i-1)%n] - 1))
        if students[(uno - i)%n] != (students[(uno-i-1)%n] - 1):
            ansNR = False
            break

    print("YES" if ansR or ansNR else "NO")

