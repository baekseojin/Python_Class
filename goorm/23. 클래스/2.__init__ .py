class Unit:
    def __init__(self, name, hp, damage): # __init__ : 객체가 생성될 때 자동으로 호출
        self.name = name # self : 객체 자기 자신
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.". format(self.name))
        print("체력 {}, 공격력 {}\n".format(self.hp, self.damage))

# self : 메소드를 정의할 때 처음 전달 값은 반드시 self를 넣는다
# 메소드 내에서 self.변수 와 같은 형태로 멤버변수를 저장한다

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
