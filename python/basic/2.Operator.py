"""
본 로직은 나도코딩 연산자 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# [연산자]

# 연산기호(덧셈, 뺄셈, 곱셈, 나눗셈)
print(1 + 1)  # 2
print(3 - 2)  # 1
print(5 * 2)  # 10
print(6 / 3)  # 2

# **(제곱), %(나머지), //(몫)
print(2 ** 3)  # 제곱 2^3= 8
print(5 % 3)  # 나머지 2
print(10 % 3)  # 나머지1
print(5 // 3)  # 몫 1
print(10 // 3)  # 몫 3

# >, < , >=, <=
print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

# ==
print(3 == 3)  # True | == 같다(등호의 개념)
print(4 == 2)  # False
print(3 + 4 == 7)  # True

# !=
print(1 != 3)  # True | != 같지 않다
print(not (1 != 3))  # False | 1 != 3 => True , not True == False

# and
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

# or
print((3 > 0) or (3 < 5))  # True
print((3 > 0) | (3 < 5))  # True (백 스페이스 밑에 있는 기호를 Shift 누르고 입력하면 된다, 영어로는 pipe)

# multi operator
print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False

# [간단한 수식]

print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
number = 2 + 3 * 4  # 14
print(number)
number = number + 2  # 16
print(number)
number += 2  # 18
print(number)
number -= 2  # 16
print(number)

number %= 5  # 1
print(number)

# [숫자처리함수]

print(abs(-5))  # 5 | 절댓값
print(pow(4, 2))  # 4^2 = 4*4  = 16 | 제곱값을 다음 인자만큼 계산해주는 함수
print(max(5, 12))  # 12 | 주어진 인자중에서 최댓값을 구해주는 함수
print(min(5, 12))  # 5  | 주어진 인자중에서 최솟값을 구해주는 함수
print(round(3.14))  # 3 | 반올림함수
print(round(4.99))  # 5

from math import floor, ceil, sqrt  # 다른 라이브러리에서 함수를 가져옴

print(floor(4.99))  # 4 | 무조건 내림
print(ceil(3.14))  # 4 | 무조건 올림
print(sqrt(16))  # 4 | 제곱근

# [랜덤 함수]

from random import *

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print((random() * 10))  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성

# ---------------------------------------------------------------------------------------
'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
# ----------------------------------------------------------------------------------------

# Answer

from random import randrange

print("오프라인 스터디 모임 날짜는 매월 " + str(randrange(4, 29)) + "일로 선정되었습니다.")
