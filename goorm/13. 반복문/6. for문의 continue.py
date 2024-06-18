marks = [90, 25, 67, 45, 80]
number = 0;
#****** continue, break 알기
for mark in marks:
	number += 1
	if mark <= 60: 
		continue # 만나는 순간 for문으로 간다 != break은 for문을 빠져나간다
	print(f"{number}번 학생 합격입니다 !")