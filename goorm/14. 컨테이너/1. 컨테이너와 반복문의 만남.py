# members = ['고윤영', '김도건', '김민우', '김준경', '김준일', '마현우', '백서진', '백진암', '변은혜', '서수민', '심효은', '원설아', '이명재', '이상진', '이희성', '정지원']
# i = 0

# while i < len(members):
# 	print(members[i], end=' ')
# 	i+=1

# members.pop() # 마지막 요소 삭제, pop은 인덱스 번호로 삭제
# print(members) # 정지원 삭제

# members.pop(7) # 7번째 요소 삭제 
# print(members) # 백진암 삭제

# members.remove('백서진') #remove는 데이터 값으로 삭제
# print(members) # 백서진 삭제

# members.insert(0, '백서진') # 첫번째에 백서진 추가
# print(members) # 백서진 추가

# print(members.index('이상진')) # 몇 번째 인덱스에 있는지 출력
# # 12

# members.reverse() # 리스트 역순 출력
# print(members)

# # 리스트 원본을 살리면서 역순 출력하는 방법
# print(list(reversed(members)))
# print(members)
	
list = [0,1,2,3,4,5]

list.pop()
print(list)

list.pop(1)  # 인덱스 번호 삭제
print(list)

list.remove(3) # 값 삭제
print(list)
# [0,2,4]

list.insert(2, 5)
print(list)