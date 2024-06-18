print("Hello world 0")
print("Hello world 9")
print("Hello world 18")
print("Hello world 27")
print("Hello world 36")
print("Hello world 45")
print("Hello world 54")
print("Hello world 63")
print("Hello world 72")
print("Hello world 81")

# ***** 시험
for i in range(0, 10):
	print("Hello world {}".format(i*9))
	
'''
for i in range(0, 82, 9):
	print("Hello world {}".format(i))
'''

# range(시작값, 마지막값, 증감값)
# 시작값과 증감값 생략 가능
# 시작값을 생략하면 0, 증감값을 생략하면 1
# 마지막값 - 1, (0,10) => 0~9까지