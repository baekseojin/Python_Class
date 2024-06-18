import math 
print(math.ceil(2.2)) # 3, ceil : 올림 
print(math.floor(2.7)) # 2, floor : 내림
print(math.pow(2, 10)) # 1024.0, 제곱 (2의 10제곱)
print(math.pi) # 3.141592~, 파이값 반환

# 파이썬은 객체지향 언어

height = int(input("키를 입력하세요"))
weight = int(input("몸무게를 입력하세요 : "))
print(type(height)) # <class 'int'>

bmi = weight / (height/100)**2

print("당신의 BMI는 다음과 같습니다 : ", bmi)

# 새로 알게 된 점
# ceil : 올림
# floor : 내림
# pi : 파이값 반환
# type(변수) : <class '변수의 자료형'>
