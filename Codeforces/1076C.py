from math import sqrt
n = int(input())
for i in range(n):
    d = int(input())
    b =  d
    a = -1
    c = -d
    det = b**2 -4 * a * c

    if det >= 0:
        ans1 = abs((b + sqrt(det))/2*a)
        ans2 = abs((b - sqrt(det))/2*a)
        print('Y', "{0:.9f}".format(ans1), "{0:.9f}".format(ans2))

    else:
        print('N')