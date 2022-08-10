n , m = map(int, input().split())

a=[]
for i in range(n):
    a.append(int(input()))

d = [10001]*(m+1)

d[1]=m
