import sys
N= int(sys.stdin.readline())
queu = []

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order =='push':
        value = word[1]
        queu.append(value)

    elif order =='pop':
        if len(queu) == 0:
            print(-1)
        else:
            print(queu.pop(0))

    elif order =='size':
        print(len(queu))

    elif order =='empty':
        if len(queu)==0:
            print(1)
        else:
            print(0)
        
    elif order =='front':
        if len(queu)== 0:
            print(-1)
        else:
            print(queu[0])

    elif order =='back':
        if len(queu)== 0:
            print(-1)
        else:
            print(queu[-1])
