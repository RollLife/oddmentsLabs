"""
본 로직은 나도코딩 클래스 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# Class (클래스)
# 스타크래프트

# 마린 : 공격 유닛, 군인. 총을 쓸 수 있으
name = "마린"  # 유닛의 이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {} \n".format(hp, damage))

# 탴크 : 공격 유닛, 탱크, 포를 쓸 수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {}, 공격력 {} \n".format(tank_hp, tank_damage))


def attack(name, loccation, damage):
    """
    유닛이 공격하는 method
    :param name: 유닛 이름
    :param loccation: 공격 위치
    :param damage: 공격할 때 데미지
    :return:
    """
    print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(name, loccation, damage))


attack(name, "1시", damage)  # 마린이 공격
attack(tank_name, "1시", tank_damage)  # 탱크가 공격

# 여기서 탱크가 하나 더 생긴다면?

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("\n{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {}, 공격력 {} \n".format(tank2_hp, tank2_damage))

attack(tank2_name, "1시", tank2_damage)


# 여기서 문제가 생긴다. 게임을 실제로 할때 유닛은 수없이 생기는데 이렇게 일일이 하나씩 만들어야 할까?
# >> 그래서 class가 필요함 (흔히 class를 붕어빵 틀이라고 말한다. 붕어빵은 하나인데 여러개 찍어내는것처럼 말이다.)

class Unit:
    def __init__(self, name, hp, damage):
        # 필요한 값들을 정의
        # init 함수
        # 파이썬에서 생성되는 생성자
        # init 함수에서 생성된 인자만큼 동일한 갯수의 인자들을 던져줘야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)  # self를 제외한 나머지 인자에 값 전달
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# tank = Unit("tank") # 정의된 argument만큼 전달하지 못하기때문에 오류가 발생됨
# marine과 tank는 Unit 클래스의 인스턴스라고 표현함

# >> 똑같은 클래스에서 서로 다른 유닛들을 생성하였음


# init 함수
# 파이썬에서 생성되는 생성자
# init 함수에서 생성된 인자만큼 동일한 갯수의 인자들을 던져줘야함
# marine과 tank는 Unit 클래스의 인스턴스라고 표현함


# 멤버변수
# 클래스 내에서 정의된 변수
# self.name, self.hp 같은 애들이 멤버변수

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))  # 멤버 변수를 외부에서 사용함.

# 레이스가 클로킹함
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True  # 외부에서 clocking이라는 변수를 추가로 할당함

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))


# if wraith1.clocking == True: # Error!
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# >> wraith2에만 확장적으로 clocking이라는 멤버 변수가 추가가 되었지만 wraith1에는 clocking이라는 변수가 없음
# TIP) 어떤 객체에 대해서 확장적으로 변수를 할당할 수 있고, 할당한 객체만 적용이되고 다른 객체에는 적용이 되지않는다.


# 메소드

# 공격 유닛 클래스 생성
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        """
        공격하는 함수
        """
        # self는 자기 자신에 대한 변수
        # name과 damage는 자기자신(Unit 클래스)에 정의되었으니 self.name, self.damage라고 사용이 가능하다.
        # location은 자기자신(Unit 클래스)에 정의되지않았고, 전달받은 변수이기때문에 self.을 사용하지 않고 사용한다.(물론 정의한다면 멤버변수로 사용가능)
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        """
        공격받은 함수
        """
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 50)
firebat1.attack("5시")  # 공격함

# 두번 공격받음
firebat1.damaged(25)
firebat1.damaged(25)


# 상속 (inheritance)
# 물려받음, Unit이라는 클래스에 있는 속성들을 상속 받음

# 메딕 : 의무병 (공격유닛 X)
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 위에서 작성된 코드를 동일하게 동작하되 상속되게끔 작성해본다
class AttackUnit(Unit):  # Unit 클래스를 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # Unit 클래스를 상속했다면 똑같이 인자들도 할당시켜주어야함
        # self.name, self.hp 또한 상속받아서 선언하지 않아도됨
        self.damage = damage  # 상속받은것 이외에 다른 변수를 추가 할당

    def attack(self, location):
        """
        공격하는 함수
        """
        # self는 자기 자신에 대한 변수
        # name과 damage는 자기자신(Unit 클래스)에 정의되었으니 self.name, self.damage라고 사용이 가능하다.
        # location은 자기자신(Unit 클래스)에 정의되지않았고, 전달받은 변수이기때문에 self.을 사용하지 않고 사용한다.(물론 정의한다면 멤버변수로 사용가능)
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        """
        공격받은 함수
        """
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 50)
firebat1.attack("5시")  # 공격함

# 두번 공격받음
firebat1.damaged(25)
firebat1.damaged(25)


# 다중 상속
# 부모 클래스(Unit, ...)를 두개 이상 상속 받는 것
# 부모 클래스(Unit), 자식 클래스(AttackUnit) / Unit -(상속)-> AttackUnit

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # >> AttackUnit, Flyable 두 개의 부모클래스를 상속받음.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkrie = FlyableAttackUnit("발키리", 200, 6, 5)  # 초기화 및 선언
valkrie.fly(valkrie.name, "3시")


# 연산자 오버라이딩 (부모 클래스에서 정의한 메소드 말고 자식 클래스에서 선언한 메소드를 사용하는것)
class Unit:
    def __init__(self, name, hp, speed):  # 기존과 다르게 지상 유닛에 대해서도 이동속도를 추가 시켜준다.
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):  # 유닛이 이동한다는 가정하에 위치와 그에 해당하는 메소드를 생성함
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))


# 부모클래스의 인자가 변경됨에 따라 똑같이 인자를 추가시켜 주어야함.
class AttackUnit(Unit):  # Unit 클래스를 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        """
        공격하는 함수
        """
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        """
        공격받은 함수
        """
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # >> AttackUnit, Flyable 두 개의 부모클래스를 상속받음.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0(이미 flying_speed가 선언되어서)
        Flyable.__init__(self, flying_speed)


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀 크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")  # 지상 유닛 이동
battlecruiser.fly(battlecruiser.name, "9시")  # 공중 유닛 이동


# >> 문제점 : 매번 유닛이 지상유닛일때 move함수, 공중유닛일때 fly함수를 써야하는 단점이 있다.


# 그렇기에 move 함수 하나로 지상유닛 이동과 공중유닛이동을 구현해보겠다.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # move라는 메소드를 이미 갖고 있지만 재 정의 함.
        print("[공중 유닛 이동]")
        self.fly(self.name, location)  # Flyable함수 내에 fly가 선언되어있으므로 그것을 사용하는 것


battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("9시")
