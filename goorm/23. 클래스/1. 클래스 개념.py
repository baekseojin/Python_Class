# def __init__ : 인스턴트화를 실시할 때 반드시 처음에 호출되는 특수한 함수 

class human: # 클래스 이름 정의
    def __init__(self, height, age): # 클래스가 처음 호출될 때 실행될 method, self는 객체 자기 자신을 의미한다. 메서드를 정의할때 처음 전달값은 반드시 self를 넣는다 
        self.height = height
        self.age = age
    
    def how_old(self):
        print(self.age, "살 입니다.")

    def how_tall(self):
        print(self.height, "cm 입니다.")

Seunghyun = human(180, 31) # 인스턴스 생성

Seunghyun.height

Seunghyun.how_old()

Seunghyun.how_tall()

print(Seunghyun.height)



