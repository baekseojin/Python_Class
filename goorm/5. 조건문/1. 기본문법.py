if True:
    print("code1")
    print("code2")
    # 들여쓰기 되어있는 부분이 하나의 블록과 같음
print("code3")

if False:
    print("code1")
    print("code2")
print("code3")

# 성인 미성년자 판별 코드

age = int(input("나이를 입력하세요 : "))

if age > 19:
    print("성인입니다.")
elif age <= 19:
    print("미성년자입니다.") 


''' 출력 결과
code1
code2
code3
code3
if문 결과에 따라 출력
'''