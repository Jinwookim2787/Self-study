n, k = map(int, input().split())
a = [i for i in range(1, n+1)]
result = []
i = k-1

for _ in range(n):
    if len(a) > i:
        x = a[i]
        result.append(x)
        a.pop(i)
        i+=k-1
    elif len(a) <= i:
        i = i % len(a)
        x = a[i]
        result.append(x)
        a.pop(i)
        i+=k-1

print("<", ', '.join(str(i) for i in result), ">", sep = '')

