n = int(input())

a=[]
for i in range(n):
    a.append(input().split())

for i in range(n):
    a[i][1]=int(a[i][1])

for i in range(n):
    if i ==n-1:
        break 
    if a[i][1]>a[i+1][1]:
        a[i+1][1], a[i][1] = a[i][1], a[i+1][1]
        a[i+1][0], a[i][0] = a[i][0], a[i+1][0]

for i in range(n):
    print(a[i][0], end = ' ')
