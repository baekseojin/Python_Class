import random

numbers = list()

while len(numbers)<6: # 길이는 0부터 셈 0, 1, 2, 3, 4, 5 (6번)
	number = random.randint(1, 45)
	if number not in numbers: # 중복제거, 만약 number가 numbers에 없으면 추가
		numbers.append(number)
	numbers.sort() # numbers 오름차순 정렬
print(numbers)