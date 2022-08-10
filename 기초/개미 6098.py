a = [] 
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    s = list(map(int,input().split()))
    a[i] = s

for x in range(10):
    for y in range(10):
        if a[x][y] == 2:
            a[x][y] = 9

            #while a[x][y]==9:
            #    for n in (1,10):
            #        for m in (1,10):
            #            if a[n][m]==0 or 2:
            #                a[n][m]=9
            #            else:
            #                a[n+1][m]=9
                

for i in range(10):
    for j in range(10):
        print(a[i][j], end = ' ')
    print()


