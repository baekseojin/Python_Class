oddnumber = [1,3,5,7,9]
cafes = ['star', 'bene', 'yoger', 'friends']
A = [1,5,'A','CC','B']
listInList = [[1,3,5,7,9], cafes, oddnumber, 1, 3, 'Abc']

# 중간고사 **
a = oddnumber[1:5] # 1,2,3,4번째 요소
b = cafes[1:] # 1번째 요소부터 끝까지
c = A[:2] # 0번째 요소부터 1번째 요소까지
d = listInList[0][1:4] # 리스트 내 리스트 접근, 0번째 리스트에서 1번째 요소부터 3번째 요소까지

print(a) # 3 5 7 9
print(b) # bene yoger friends
print(c) # 1 5  
print(d) # 3 5 7

