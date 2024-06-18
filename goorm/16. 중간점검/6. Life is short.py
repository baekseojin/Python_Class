import random

luckynum = random.sample(range(1, 45), 6)
# print(sorted(luckynum))

while True:
	bonus = random.sample(range(1, 45), 1)
	if bonus not in luckynum:
		print(f'행운번호 : {sorted(luckynum)} 보너스번호{bonus}')
		import sys # break
		sys.exit()