def cal(x, op, y):
    ans = 0
	if op == '+':
		print(f'{x} + {y} = {x+y}')
	elif op == '-':
		print(f'{x} - {y} = {x-y}')
	elif op == 'x':
		print(f'{x} * {y} = {x*y}')
	elif op == '/':
		print(f'{x} / {y} = {x/y}')
		
# ************ 시험 *******************
a = input().split(" ") # split을 통해서 a가 리스트 형태로 반환, ['5', '+', '6'] 리스트
# *********** 시험 ********************

x = int(a[0]); op=a[1]; y = eval(a[2]) # int, eval : 숫자 가능

cal(x, op, y)