def binary_search(a, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if a[mid] == target:
            return mid
        elif a[mid]> target:
            end = mid -1 
        else:
            start = mid +1
    return None

n= int(input())
a= list(map(int, input().split()))
a.sort()
m= int(input())
x= list(map(int, input().split()))

for i in x:
    result = binary_search(a, i, 0, n-1)
    if result!= None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')