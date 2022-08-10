# n, m = map(int, input().split())

# a = []
# for i in range(n):
#     a.append([])
#     for j in range(m):
#        a[i].append(0)

# for i in range(n):
#     s = list(map(int, input().split()))
#     a[i]=s



# result=[]
# for i in range(n):
#     list1=[]
#     for j in range(m):
#         list1.append(a[i][j])
#     result.append(min(list1))

# print(max(result))


n, m = map(int, input().split())

result = []
for i in range(n):
    temp = map(int, input().split())
    result.append(min(temp))

print(result)
print(max(result))









