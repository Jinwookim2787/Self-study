#거슬러 줘야할 돈을 차례대로 구하기
n = int(input("돈:  "))

a = 0
while True:
    if n>=500:
        a+=1
        if n-500*a<500:
            break
    else:
        a=0
        break

b=0
while True:
    if n-500*a>=100:
        b+=1
        if n-500*a-100*b<100:
            break
    else:
        b=0
        break

c=0
while True:
    if n-500*a-100*b>=50:
        c+=1
        if n-500*a-100*b-50*c<50:
            break
    else:
        c=0
        break

d=0
while True:
    if n-500*a-100*b-50*c>=10:
        d+=1
        if n-500*a-100*b-50*c-10*d<10:
            break
    else:
        d=0
        break

print('동전의 개수',a+b+c+d)
print('500',a, '100=',b, '50=',c, '10=', d )