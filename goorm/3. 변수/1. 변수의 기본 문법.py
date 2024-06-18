x=10
y=5

print(x+y)

title = "python"
print("Title is " + title)

a = b = c = 10
print(a,b,c) # 10 10 10 출력

x, y = (5, 10)
print(x,y)

name, age, address = "백서진", 17, "부산 강서구 가락대로"
print(name, age, address)

'''출력 결과
15
Title is python
10 10 10
5 10
백서진 17 부산 강서구 가락대로
'''

# 새로 깨달은 것
# 한 번에 값을 집어 넣을 수 있다
# -> a=b=c=10 | a, b = (1, 2) | a, b = "안녕", "hello"  