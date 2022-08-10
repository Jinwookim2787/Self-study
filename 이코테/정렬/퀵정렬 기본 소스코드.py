a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(a, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left<=right:
        while left <= end and a[left] <=a[pivot]:
            left+=1
        while right> start and a[right]>=a[pivot]:
            right-=1
        if left > right:
            a[right], a[pivot] = a[pivot], a[right]
        else:
            a[left], a[right] = a[right], a[left]
        
    quick_sort(a, start, right-1)
    quick_sort(a, right+1, end)

quick_sort(a, 0, len(a)-1)
print(a)