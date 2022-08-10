from bisect import bisect_left, bisect_right

a = [1,2,3,3,3,3,4,4,8,9]

print(bisect_left(a, 4))
print(bisect_right(a,4))