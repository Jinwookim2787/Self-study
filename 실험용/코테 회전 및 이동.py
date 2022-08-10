scores  = [3,2,1,0,1,2,3]
sur_val = [0]*26

survey = list(input().split(','))
choices= list(map(int,input().split(',')))


print(survey)
print(choices)
print(survey[1][2])
# for i in range(len(survey)):
#     if choices[i] == 4 :
#         pass
#     if choices[i]>4 : 
#         sur_val[ord[survey[i][1]]]
