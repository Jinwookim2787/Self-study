h, w = map(int, input().split())

f = []
for i in range(h):
    f.append([])
    for j in range(w):
        f[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if  d== 0:
            f[x + j - 1][y - 1] = 1

        if d == 1:
            
            f[x - 1][y + j - 1] = 1

for i in range(h):
    for j in range(w):
        print(f[j][i], end = ' ')
    print()