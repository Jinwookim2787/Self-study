n , m = map(int, input().split())

result=0

while True:
    tar = (n//m)*m
    result+=n-tar
    n=tar
    if n<m:
        break
    result += 1
    n//=m

result += n-1
    
print(result)