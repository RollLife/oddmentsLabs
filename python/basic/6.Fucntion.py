"""
본 로직은 나도코딩 함수 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""


# def (함수 선언)
# 함수는 특정 부분의 연산이나 작업들을 미리 정의 해두고 호출할때 해당 작업을 실행 할 수 있게 해준다.


def open_account():  # 함수 정의
    print("새로운 계좌가 생성되었습니다.")


open_account()  # 함수 호출


# 전달값과 반환값

def deposit(balance, money):  # 잔액과 입금된 돈을 전달받음
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
    return balance + money  # 잔액과 입금된 돈을 합쳐서 현재 통장에 있는 돈을 반환함


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = 0  # 잔액
balance = deposit(balance, 1000)  # 함수 호출 및 전달값과 반환값을 전달 받음
print(balance)

# balance = withdraw(balance, 2000)  # 출금 불가능
# balance = withdraw(balance, 500)  # 출금

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 기본값(default)
def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 {2}" \
          .format(name, age, main_lang))


# 현재 이 값에 경우는 서로 다른 언어, 다른 사람, 공통정이 없는 사람들에 대한 분류
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):  # 기본값 정의
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 {2}" \
          .format(name, age, main_lang))


# 다른 인자값에 미리 기본값이 선언이 되어있다면 굳이 지정하지 않아도된다. 물론 지정해도 상관은 없다.
profile("유재석")
profile("김태호")


# 키워드 값 (keyword)

def profile(name, age, main_lang):
    print(name, age, main_lang)


# 함수에서 선언된 매개변수의 값이 있다면 이렇게 키워드값을 선언해서 작성을 해준다면 순서가 뒤죽박죽이어도 함수를 선언하여 사용할 수 있다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", name="김태호", age=25)

