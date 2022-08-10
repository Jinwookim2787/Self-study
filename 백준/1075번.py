n = int(input())
f = int(input())

n=n-(n%100)

for i in range(100):
    if n%f != 0:
        n+=i
        
    else:
        print(n)
        if n%100==0:
            print('00')
        elif n%100<10:    
            print('0','n%100')
        else:
            print(n%100)
        break
    

