from sys import stdin, stdout

if __name__ == "__main__":
    write = stdout.write
    names = stdin.readline().strip().split('-')
    for i in names:
        write(i[0])