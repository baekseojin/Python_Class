# 1. 전역변수 함수에서 다시 정의하여 사용하는 방법

gun = 10

def checkpoint(soldier): # 경계근무
	global gun # 전역변수에 있는 값을 핸들링(가져옴)
	gun = gun - soldier
	print(f'[함수 내] 남은 총 : {gun}')
	
print(f"전체 총 : {gun}")

checkpoint(2) # 2명이 경계 근무 나감

print(f"남은 총 : {gun}")

# 2. 함수 인자로써 전역변수 값을 입력받아 수행 후 결과로 반환하는 방법

# gun = 10

# def checkpoint_ret(gun, soldier):
# 	gun = gun - soldier
# 	print(f"[함수 내] 남은 총 : {gun}")
# 	return gun 

# print(f"전체 총 : {gun}")

# gun = checkpoint_ret(gun, 2)

# print(f"남은 총 : {gun}")