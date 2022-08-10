a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(a):

    if len(a) <= 1:
        return a
    
    pivot = a[0]
    tail  = a[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x> pivot]
    
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
print(quick_sort(a))

l = [0, 3, 1, 2, 4]
print(quick_sort(l))
