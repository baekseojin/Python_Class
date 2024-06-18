# def palindrome(string):
# 	a = list(reversed(string))
# 	return string == a 
	
# str = list(input('문장을 입력하세요 : '))
# palindrome(str)

# 파이썬식 코드짜기 
# def palindrome(string):
# 	return string == string[::-1] # 뒤에서부터 앞으로 와서, reverse와 같은 뜻 

# string = input()
# print(palindrome(string))


# a = [1,2,3,4,5,6]
# print(a[::-1]) [a:b]


# str = [1,2,3,4]
# a = str[1:3]
# b = str[-1:-5:-1]
# print(str[-1:-5:-1])
# print(str[0:5:1])

# print(a)
# print(b)

# C식 코드짜기
# word = input()

# is_palindrome = True
# for i in range(len(word) // 2):
# 	if word[i] != word[-1 -i]:
# 		is_palindrome = False
# 		break

str = [1,2,3,4,5,6]
print(str[-1:-5:-1])