n = int(input()) # 4 입력 

print(' ' * (n-1) + '*')

for i in range(n-2):
	print(' ' *(n-2-i) + '*' + ' '*(i*2+1) + '*')
	
print('*' * (n*2-1))