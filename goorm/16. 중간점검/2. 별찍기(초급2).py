n = int(input()) # 5 입력

for i in range(1, n+1):
	print(" " *(n-i) + "*" * i)
	
# i=1, 공백 4칸 출력 후 * 1개 출력
# i=2, 공백 3칸 출력 후 * 2개 출력
# i=3, 공백 2칸 출력 후 * 3개 출력
# i=4, 공백 1칸 출력 후 * 4개 출력
# i=5, 공백 0칸 출력 후 * 5개 출력

# while 문

'''
num = int(input())
i = 1
while i<=num:
	print(" " *(num-i) + "*" * i)
	i+=1
'''