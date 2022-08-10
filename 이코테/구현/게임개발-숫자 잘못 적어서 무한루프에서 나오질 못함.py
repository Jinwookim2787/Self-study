n, m = map(int, input().split())

d=[[0]*m for _ in range(n)]
x, y ,direction = map(int, input().split())
d[x][y]=1

a=[]
for i in range(n):
    a.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1 #d이게 왜 1이지?
turn=0

while True:
    turn_left()
    nx= x+dx[direction]
    ny= y+dy[direction]
    if d[nx][ny]==0 and a[nx][ny]==0:
        d[nx][ny]=1 #주의
        x=nx
        y=ny
        count+=1
        turn=0   #주의
        continue #주의
    else:
        turn+=1
    
    if turn==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if a[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn=0

print(count)
    

    
    
    
    
    
  