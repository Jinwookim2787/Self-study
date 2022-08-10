n , m = map(int, input().split())

count=0

while True:
    if n%m==0:
        n=n//m
        count+=1
    
    else:
        n-=1
        count+=1
    
    if n==1:
        break

print(count)