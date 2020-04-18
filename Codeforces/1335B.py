letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y','z']
t = int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    ans = []
    while len(ans) < n:
        for j in range(b):
            ans.append(letters[j])

    print(''.join(ans[:n]))      