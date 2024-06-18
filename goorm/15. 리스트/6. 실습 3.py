numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

a = "goorm"

# 공간까지 삭제
del numbers[4] # 10과 그 공간을 삭제
print(numbers) # [2, 4, 6, 8, 1, 3, 5, 7, 9]

del numbers[:5] # 0번째 부터 4번째 요소 삭제
print(numbers) # [3, 5, 7, 9]

del a # 객체 자체를 삭제
# print(a) -> 오류

# cf) 파이썬은 인터프린터 언어라 한 줄 한 줄 실행해서 오류가 있더라도 그 줄 전까지는 실행한다