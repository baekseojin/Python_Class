
def cal(num1, num2, op):
    ans = 0
	if op == '+':
		ans = num1 + num2
	elif op == '-':
		ans = num1 - num2
	elif op == 'x':
		ans = num1 * num2
	elif op == '/':
		ans = num1 / num2
		
	show(num1, num2, op, ans)
	
def numInput():
	data = int(input('숫자를 입력하세요.'))
	return data

def strInput(msg):
	data = input(msg)
	return data

def show(num1, num2, op, ans):
	print(f'{num1} {op} {num2} = {ans}')
	
# if __name__ == '__main__' => 파이썬 파일은 모듈로 쓸 수 있음, 모듈로 사용될 때는 실행이 안된다
if __name__ == '__main__':
	num1 = numInput()
	num2 = numInput()
	op = strInput('연산자를 입력하세요.')
	cal(num1, num2, op)