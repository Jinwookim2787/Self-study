a = [1,2,3,2,45,2,5]

# 열거하기 위한 방법.
#1 range를 이용한 방법 <- 리스트 조회 작업과 전체길이 조회 하여 루프 처리 하는 형태라는 것이 단점

for i in range(len(a)):
    print("(",i,",",a[i],")",end =' ')
print("\n")
#2 더 깔끔하게 처리하는 방법 <- 인덱스를 위한 변수를 별도로 관리 해줘야 하는 것이 단점

i = 0
for v in a:
    print(i, v, end =' ')
    i+=1
print("\n")
#3 이 책에서 추천하는 방법. enumerate

for i, v in enumerate(a):
    print(i, v, end =' ')
print("\n")