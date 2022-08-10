import sys
N= int(sys.stdin.readline())
stack = []

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order =='push':
        value = word[1] #push의 경우에는 두 단어가 입력되기 때문에 word[0]은 명령어 push를 받고 word[1]은 숫자를 받는다.
        stack.append(value)

    elif order =='pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order =='size':
        print(len(stack))

    elif order =='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
        
    elif order =='top':
        if len(stack)== 0:
            print(-1)
        else:
            print(stack[-1])