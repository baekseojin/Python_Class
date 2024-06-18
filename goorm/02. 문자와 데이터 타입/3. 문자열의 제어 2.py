str1 = 'hello world'
str2 = 'HELLO WORLD'
print('hello world'.capitalize()) # 첫 글자를 대문자로 바꿈
print('hello world'.upper()) # 모든 글자를 대문자로 만듦
print(str1.lower()); # str1의 모든 글자를 소문자로 만듦
print('hello world'.__len__())
print(len('hello world')) # 뒤에 있는 객체 요소 갯수 반환
print('Hello world'.replace('world', 'programming')) # 문자를 바꿈, world -> programming

''' 실행결과
Hello world
HELLO WORLD
hello world
11
11
Hello programming
'''

# 깨달은 점
# capitalize : 첫 글자를 대문자
# upper : 모든 글자를 대문자
# lower : 모든 글자를 소문자
# len("문자열") : 문자의 갯수

