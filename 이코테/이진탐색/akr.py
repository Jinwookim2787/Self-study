def mm(a,target, start, end):    
    mid = (start+end)//2
    return sum(a[mid+1:])-a[mid]


n , m = map(int, input().split())
a= list(map(int, input().split()))
a.sort()

result = mm(a, m, 0, n-1)
print(result)