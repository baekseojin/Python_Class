class Unit:
    def __init__(self, name, hp, damage): # self : 객체 자기 자신을 의미 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.". format(self.name))
        print("체력 {}, 공격력 {}\n".format(self.hp, self.damage))

class AttackUnit(Unit):
    def attack(self, location):
        print("{} : {} 방향으로 적을 공격합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))

        self.hp = self.hp - damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)