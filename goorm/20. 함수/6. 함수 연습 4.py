# 지역별 데이터
data = {'서울':[81,0.052,0.4] ,
        '부산':[54,0.072,0.4],
        '대구':[55,0.06,0.4],
        '인천':[52,0.06,0.5],
        '광주':[61,0.064,0.5],
        '대전':[71,0.064,0.4],
        '울산':[60,0.068,0.4],
        '경기':[64,0.06,0.4],
        '강원':[62,0.062,0.4],
        '충북':[59,0.067,0.4],
        '충남':[65,0.063,0.4],
        '전북':[65,0.068,0.4],
        '전남':[51,0.062,0.4],
        '세종':[69,0.06,0.5],
        '경북':[57,0.066,0.4],
        '경남':[49,0.074,0.4],
        '제주':[66,0.076,0.3]}

# 미세먼지 등급 판단
def PM10(num):
  if num <= 30: return 'Good!'
  elif num <= 80: return 'normal!'
  elif num <= 150: return 'bad!'
  else: return 'terrible!'

# 오존 등급 판단
def O3(num):
  if num <= 0.03: return 'Good!'
  elif num <= 0.09: return 'normal!'
  elif num <= 0.15: return 'bad!'
  else: return 'terrible!'

# 일산화탄소 등급 판단
def CO(num):
  if num <= 2: return 'Good!'
  elif num <= 9: return 'normal!'
  elif num <= 15: return 'bad!'
  else: return 'terrible!'

# 등급 별 표시
def star(grade):
  if grade == 'Good!': return '****'
  elif grade == 'normal!': return '***'
  elif grade == 'bad!': return '**'
  else: return '*'

# 키와 밸류 를 쌍으로 묶은 것 = item
# 하나씩 뽑아서 리스트로 만들거임

for key, value in data.items():
  lt = [] # 별을 저장할 임시 기억장소 리스트
	
  # PM10(value[0]) # 서울의 81을 들고와서 PM10에 넣어서 별이 반환된다
  
	lt.append(star(PM10(value[0]))) # append() 추가
  lt.append(star(O3(value[1])))
  lt.append(star(CO(value[2])))
  # print(lt)
	
	starlist[key] = lt # 키값마다 lt를 value로 할당
	
	print(starlist)
	print(starlist['부산'])
	
	print(starlist.get('부산시')) # None 반환