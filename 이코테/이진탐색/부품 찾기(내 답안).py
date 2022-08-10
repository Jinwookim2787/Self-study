n = int(input())
data = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

for i in range(m):
    if want[i] in data:
        print('yes', end = ' ')
    else:
        print('no', end =' ')