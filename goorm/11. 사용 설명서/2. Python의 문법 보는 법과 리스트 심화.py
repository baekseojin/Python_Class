# al = ['A', 'B', 'C', 'D']
# # arr1 = list() 리스트 선언 이렇게도 가능하다
# # arr1 = ['a', 'b', 'c', 'd']
# # print(arr1)
# print(len(al)) # *********************8al 자체가 list 니까 list의 길이 = 4 가 나온다 시험에 나올 가능성 up!!!
# al.append('E') # 추가
# print(al) #['A', 'B', 'C', 'D', 'E']
# del(al[0]) 
# print(al) #['B', 'C', 'D', 'E']
# del(al[1]) # C를 삭제하고 싶으면 al[1] -> A를 이미 삭제했기 때문에 1칸씩 줄어듬
# print(al) #['B', 'D', 'E']

test = ['Aaa', 'Bbb', 'Ccc', 'Ddd']
# del(test[1][0]) # 2번째 객체의 첫번째 글자인 B를 삭제 # 문자열은 수정, 순서변경, 삭제 안된다. 
print(test[1][0]) 