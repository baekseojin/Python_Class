#  구글 드라이브 마운트
from google.colab import drive
drive.mount('/content/gdrive')

# fp : file pointer의 약자
fp = open('/content/gdrive/MyDrive/지역평균기온.txt', 'r', encoding = 'utf-8')

data = fp.read()
data

data2 = fp.readline()
data2

fp.close()

print(data)

# 알아놓기 (시험)
# readline() : 파일의 첫 번째 줄을 읽어 출력
# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴
# read() : 파일의 내용 전체를 문자열로 리턴