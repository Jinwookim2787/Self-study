n = int(input())

a=[]
for i in range(n):
    temp= input().split()
    a.append((temp[0],temp[1]))

a = sorted(a, key = lambda student: student[1])

for student in a:
    print(student[0], end = ' ')