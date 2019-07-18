from sys import stdin
lineas = stdin.readlines()
def fun(date, month):
    if date==7 and month ==1:
        return 'Happy Birthday To Shipu.'
    elif date == 29 and month == 4:
        return "Happy Birthday To Dipu Sir."
    elif date == 30 and month == 5:
        return "Happy Birthday To Fahad vai."
    elif date == 21 and month == 6:
        return "Happy Birthday To Sufian."
    elif date == 11 and month == 12:
        return "Happy Birthday To Alim."
    else:
        return "This is an ordinary day."

for line in lineas:
    line = [int(x) for x in line.split()]
    print(fun(line[0],line[1]))
