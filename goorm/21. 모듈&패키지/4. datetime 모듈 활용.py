import datetime as dt

print('오늘 =', dt.datetime.now()) # 현재시간을 구한다

hundred = dt.timedelta(days = 100) # 100일 경과시간
plus100day = dt.datetime.now() + hundred # 현재 시간에서 100일 경과시간을 더함
print('100일 후 =', plus100day)

minus100day = dt.datetime.now() - hundred # 현재 시간에서 100일 경과시간을 뺌
print('100일 전 =', minus100day)

aday = dt.timedelta(days=1)
tomorrow = dt.datetime.now()+ aday
print('하루 뒤 =', tomorrow)


import time
seconds = time.time()
print('에폭 이후의 시간 = ', seconds)

# 1970.1.1.0시 0분 0초, UTC