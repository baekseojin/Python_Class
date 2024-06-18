# 일반 가격
def price(people):
    print("{0} 명 가격은 {1} 원 입니다.".format(people, people * 10000))

# 조조할인 가격
def price_morning(people):
    print("{0} 명 조조할인 가격은 {1} 원 입니다.".format(people, people * 6000))

# 군인 할인 가격 
def price_soldier(people):
    print("{0} 명 군인 할인 가격은 {1}원 입니다.".format(people, people*4000))

# !!!!!!!!!!!!!!!! 시험문제 !!!!!!!!!!!!!!! 나와요 기억 
 
if __name__ == '__main__': # 내가 모듈이 아니라 main일 경우에 실행하세요, 단독이 아니라 모듈로 들어가면 실행하지 않는다 
    price(30)
    price_soldier(50)
