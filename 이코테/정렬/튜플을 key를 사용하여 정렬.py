a = [('좋은하루', 0),
    ('niceday', 1), 
    ('좋은하루', 5), 
    ('good_morning', 3), 
    ('niceday',5)]

a.sort(key= lambda x: x[1])
print(a)