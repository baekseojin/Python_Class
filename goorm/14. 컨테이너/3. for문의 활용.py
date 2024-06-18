# # end=',' : \n 대신 , 
# # print문 끝나면 항상 \n 실행(python)

# for i in range(5, 11): # 5부터 10까지의 아이템( list의 인덱스 )
#     print(i, end=' ')
		
# # 1부터 100까지
# for i in range(1, 101):
# 		print(i, end=' ') # end=" " : \n 대신 한 칸 띄어서 출력
		
# # 1부터 100까지 짝수만
# for i in range(1, 101):
# 	if i%2==0: 
# 		print(i, end=' ')
		
# 100부터 1까지 홀수만
for i in range(99, 0, -2):
	print(i, end=' ')
print('--'*50)