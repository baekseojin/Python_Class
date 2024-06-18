# evennumbers = [2, 4, 6, 8, 10]
# oddnumbers = [1, 3, 5, 7, 9]

# numbers = evennumbers + oddnumbers
# print(numbers)
# print(numbers * 4)

# numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

# numbers[4:5] = [80] # 10 -> 80
# print(numbers)

# numbers[2:6] = "hello" 
# print(numbers)
# # 2 4 'h' 'e' 'l' 'l' 'o' 3 5 7 9 

# numbers[2:3] = ['a','b','c'] 
# print(numbers) 
# # 2 4 'a' 'b' 'c' e l l o 3 5 7 9 
# # 슬라이싱은 리스트 안 값을 문자로 대입

# numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
# print(numbers)
# # 인덱스는 리스트 형태 유지하며 대입
# # 2 4 a b c e l l [a,b,c] 3 5 7 9

# numbers[:] = [1]
# print(numbers)

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

#값만 삭제
numbers[3] = "" # 2 4 6 "" 10 1 3 5 7 9  
print(numbers)

a = "goorm"

#공간까지 삭제
del numbers[4]
print(numbers)

numbers[1:3] = ['a', 'b', 'c']
# del numbers[1:3]
print(numbers)

# del numbers[:5]
# print(numbers)

#객체 자체를 삭제
del a