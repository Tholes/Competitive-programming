reversas = {"A": "A", "B":0, "C":0, "D":0, "E": "3", "F":0, "G":0,
            "H":"H", "I":"I", "J":"L", "K":0, "L":"J", "M":"M",
            "N":0,"O":"O","P":0,"Q":0,"R":0,"S":"2","T":"T","U":"U",
            "V":"V", "W":"W","X":"X","Y":"Y","Z":"5","1":"1","2":"S",
            "3":"E","4":0,"5":"Z", "6":0, "7":0, "8":"8", "9":0}

def palindromes(x):
    mitad1 = x[0:(int(len(x)/2)+1)]
    mitad2 = x[-(int(len(x)/2))-1::]
    mitad2= ''.join(reversed(mitad2))  
    if mitad1 == mitad2:
        return True
    else:
        return False

def mirrored(x):
    mitad1 = x[0:(int(len(x)/2)+1)]
    mitad2 = x[-(int(len(x)/2))-1::]
    mitad2= ''.join(reversed(mitad2))
    mitad = int(len(x)/2)+1
    for i in range(mitad):
        if reversas[mitad1[i]] != mitad2[i]:
            return False
    return True
while True:
    try:
        x = input()
        pal = palindromes(x)
        mir = mirrored(x)
        if not pal and not mir:
            print(x+" -- is not a palindrome.")
        elif pal and not mir:
            print(x+" -- is a regular palindrome.")
        elif not pal and mir:
            print(x+" -- is a mirrored string.")
        elif  pal and  mir:
            print(x+" -- is a mirrored palindrome.")
        print()
    except EOFError:
            break