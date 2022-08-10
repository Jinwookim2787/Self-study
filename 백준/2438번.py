n = int(input())
a = list(map(int, input().split()))

count=0
cnt=1
for i in a:
    for j in range(2,1001):
        if i==1:
            continue
        if i%j==0:
            cnt+=1
            if cnt>2:
                count+=1
                break
          
           


print(n-count)