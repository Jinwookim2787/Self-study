n = int(input())

datas = []
for i in range(n):
    datas.append(list(input()))

for i in range(n-1):    
    for j in range(len(datas[i])):
        if datas[i][j] != datas[i+1][j]:
            datas[i][j]='?'
            datas[i+1][j]='?'
            if datas[i-1][j]!=datas[i][j]:
                datas[i-1][j]=datas[i][j]
            
x = datas[n-1]
y = ''.join(x)
print(y)
     
    

