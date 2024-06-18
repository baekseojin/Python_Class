# --------------- 리스트 연산 ------------------
evennumbers = [2, 4, 6, 8, 10]
oddnumbers = [1, 3, 5, 7, 9]

numbers = evennumbers + oddnumbers
print(numbers) # [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
print(numbers * 4) # [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, ........ ] numbers 리스트를 4번 출력

# --------------- 리스트 수정 1 ------------------
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4] = 100
print(numbers) # 10 -> 100

numbers[2] = "hello"
print(numbers) # 6 -> hello

numbers[0] = numbers[9] # 인덱스 9를 인덱스 0에 대입
print(numbers) # 2 -> 9

numbers[8] = ['a', 'b', 'c'] # 리스트 전체를 형태 유지하며 대입
print(numbers) # 7 -> ['a', 'b', 'c']

# -------------------- 리스트 수정 2 ----------------------
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4:5] = [80] # 10 -> 80
print(numbers) # [2, 4, 6, 8, 80, 1, 3, 5, 7, 9]

numbers[2:6] = "hello" 
print(numbers) # [2, 4, hello, 3, 5, 7, 9]가 아니라 [2, 4, 'h', 'e', 'l', 'l', 'o', 3, 5, 7, 9]
# 2부터 6까지 hello를 대입한다
# [2, 4, h, e, l, l, o, 3, 5, 7, 9]

numbers[2:3] = ['a','b','c'] 
print(numbers) # [2, 4, 'a', 'b', 'c', 'e', 'l', 'l', 'o' 3, 5, 7, 9]
# 2번째 인덱스, 즉 h에 a,b,c 대입
# [2, 4, 'a', 'b', 'c', 'e', 'l', 'l', 'o', 3, 5, 7, 9] 

numbers[8] = ['a', 'b', 'c'] # 리스트 전체를 형태 유지하며 대입
print(numbers) # [2, 4, 'a', 'b', 'c', 'e', 'l', 'l', ['a', 'b', 'c'], 3, 5, 7, 9]

numbers[:] = [1]
print(numbers) # [1]

# -------------------- 리스트 삭제 1 --------------------
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

# 값만 삭제
numbers[3] = ""
print(numbers) [2, 4, 6, '', 10, 1, 3, 5, 7, 9]

# -------------------- 리스트 삭제 2 --------------------
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

a = "goorm"

#공간까지 삭제
del numbers[4]
print(numbers) # [2, 4, 6, 8, 1, 3, 5, 7, 9]

del numbers[:5]
print(numbers) # [3, 5, 7, 9]

#객체 자체를 삭제
del a