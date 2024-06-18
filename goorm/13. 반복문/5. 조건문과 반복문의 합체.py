marks = [90, 25, 67,45, 80]
number2 = 0
ocount = xcount = 0 # 변수 동시에 초기화 하는법

for mark in marks: # mark는 초기값이 0이 되어서 차례로 탐색한다, marks의 값 하나씩 탐색
	number2 += 1 # 학생의 번호를 나타내기 위해서 
	print(mark)
	if mark >= 60: 
		ocount+=1;
		print(f'{number2}번 학생은 {mark}점으로 합격입니다.')
	else:
		xcount+=1;
		print(f"{number2}번 학생은 {mark}점으로 불합격입니다.")
		
print(f'합격자 수는 {ocount}명 입니다.')
print(f'불합격자 수는 {xcount}명 입니다.')