h, w = map(int, input().split())

a=[]
for i in range(h+1): #세로부터 그리고
  a.append([])
  for j in range(w+1): #가로를 그린다
    a[i].append(0)

n = int(input())
for i in range(n):
  l, d, x, y = map(int, input().split())

  if d == 1: #세로
    try:
      for j in range(l):
        a[x][y]=1
        x+=1
    except IndexError:
      pass

  if d == 0: #가로
    for j in range(l):
      a[x][y]=1
      y+=1
    
for i in range(1, h+1) :
  for j in range(1, w+1) : 
    print(a[i][j], end=' ')
  print()