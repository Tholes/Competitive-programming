from sys import stdin, stdout
mediaAq = []
lines = stdin.readlines()
for line in lines:  
    n = int(line)
    mediaAq.append(n)
    mediaAq.sort()
    if len(mediaAq) % 2 == 1:
        stdout.write(str(mediaAq[(int(len(mediaAq)/2))])+"\n")
    else:
        a = mediaAq[int(len(mediaAq)/2)-1] + mediaAq[(int(len(mediaAq)/2))] 
        a /= 2
        stdout.write(str(int(a))+"\n")