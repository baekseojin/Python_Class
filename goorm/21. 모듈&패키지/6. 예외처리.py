''' 
<% 
  %>  <=  웹페이지에서 자바코드를 연동할 때 사용
'''

try:
	print("나누기 전용 계산기입니다.")
	num1 = int(input("첫 번째 숫자를 입력하세요 : "))
	num2 = int(input("두 번째 숫자를 입력하세요 : "))
	if num1 >= 10 or num2 >= 10:
		raise ValueError # 강제로 에러 발생시킨다 
	print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
	print("에러! 잘못된 값을 입력하였습니다. ")