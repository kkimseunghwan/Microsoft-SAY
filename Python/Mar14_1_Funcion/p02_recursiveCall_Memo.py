
# 함수 : 소스 정리 차원에서 활용 => 가독성을 위해 => 사람 기준
#   => 연관된 작업을 묶어놓고, 필요할 때 호출해서 사용.
# 컴 입장 : 소스 정리(관심없음) - 느려지기만 할 뿐.

# 함수를 정의한 뒤, 저 밑 어디가서 그 함수를 호출해서 사용하는 형태.

# 함수 호출 : JUMP연산이 일어난다고 함 : 내부적으로 추가적인 시간 소요
'''
def 함수 정의

코드 : line 11
코드 : line 12
코드 : line 13

함수 호출 : => line 9 : 함수가 정의된 곳으로 이동
'''

# 함수 호출에는 물리적인 시간 소요
# 함수의 재귀호출이 여러번 반복될 경우 시간이 매우 오레걸림
# (함수 호출에는 물리적인 시간 소요 <= 이게 정확한 이유인가?)

# 함수를 recursive(재귀적)하게 호출 : 기술명
#   함수 내부에서 자기 자신을 호출해서 반복이 생기게 하는 것.
#   언제? 규칙적인 숫자를 계산할때? (= 개소리)

# 피보나치 수열
# => 첫번째와 두번째 항은 1로 시작되며, 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다
# 1, 1, 2, 3, 5, 8, 13, 21. 34, 55, 89

def Fibonacci(x):
    if x < 3: 
        return 1

    return Fibonacci(x-2) + Fibonacci(x-1)

# 많이 돌리면 에러 발생
# RecursionError: maximum recursion depth exceeded in comparison
# 파이썬 내부적으로 제한이 걸려 있음

# 제한 해제
import sys
sys.setrecursionlimit(10000000) # 돌아는 가게 함.
# Fibonacci(7000000) # 에러는 나지 않음. 컴퓨터 터짐.

# recursive Call : 재귀적 호출
# 단순 계산용으로 쓰면, 연산이 매우 느려짐. => 반복문으로 하면 됨.


# 그럼 이 재귀라는 놈을 언제 어따가 쓸까?
# 그냥 반복문 쓰면 되는거 아님? 메모리 낭비 심하자너



# 예) 회원가입 페이지, 중복되는 ID 입력 시, 진행되지 않게 하고, 제대로된 입력을 받을 때 까지 반복.
# => 여기에 재귀 활용 (?)



# 속도에 약점이 있음
# 속도와 상관없는. 사용자로부터 원하는 입력을 받을때까지 반복
# 사용자가 개빠르게 10억번 반복하겠음?

# BMI 검사프로그램
from math import floor

user_name = {"kim", "kwon", "lee"}

# 아이디 중복 방지.
def getName():
    name = input("이름 : ")
    if name in user_name: 
        print("이미 존재하는 이름입니다.")
        return getName()
    return name

# 잘못된 데이터 입력 방지.
def getHeight():
    h = input("키 : ")
    h = float(h)
    if h > 3: # 똑바로 쓸 때 까지 입력받기.
        return getHeight()
    return h


name = getName()
height = getHeight()
weight = float(input("몸무게 : "))
print("---------------")

# 계산 해놓고 => 변수 저장
# 결과 출력
# 판정도 필요
BMI = weight/(height**2)

print("BMI : %.2f" % (floor(BMI * 100) / 100))

# 소스가 길다 : 프로그램 용량이 커짐 => HDD를 많이 차지
print("%s씨는" % name, end=' ')
if BMI >= 39: print("고도 비만")
elif BMI >= 37: print("중도 비만")
elif BMI >= 30: print("경도 비만")
elif BMI >= 24: print("과체중")
elif BMI >= 10: print("정상")
else: print("저체중")



