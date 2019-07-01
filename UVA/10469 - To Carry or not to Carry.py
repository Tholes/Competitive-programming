while True:
    try:
        x,y = map(int,input().split())
    except EOFError:
        break
    print(x^y)