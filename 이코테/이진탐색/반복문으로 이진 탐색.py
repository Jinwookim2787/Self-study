def binary_search(a, target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        if a[mid] == target:
            return mid
        
        elif a[mid] > target:
            end = mid-1
        
        else:
            start = mid+1

    return None

n, target = list(map(int, input().split()))
a = list(map(int, input().split()))

result = binary_search(a, target, 0, n-1)
if result== None:
    print('원소가 존재하지 않습니다')
else:
    print(result+1)