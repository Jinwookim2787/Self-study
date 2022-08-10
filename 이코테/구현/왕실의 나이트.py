#현재 나이트의 좌표
n = input() 
y=ord(n[0])-96#가로
x=int(n[1])#세로

print('x=',x,'y=',y)

count=0

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, -2, -2, 2, 2]
print(len(dx))

for i in range(len(dx)):
    nx= x + dx[i]
    ny= y + dy[i]
    if nx>0 and ny>0 and nx<8 and ny<8:
        count+=1

print(count)   


