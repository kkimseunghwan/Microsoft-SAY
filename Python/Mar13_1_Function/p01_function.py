# 함수

# 숫자 하나 넣으면
# 홀수인지 판별해서 결과를 출력해주는 함수

from time import sleep


def printIsOdd(num): 
    print(num%2 == 1)


# 1) 콘솔 창에 출력만 하고 살거임?
# 2) 출력"만" 할건가?


# 숫자를 하나 넣으면
# 홀수인지 "판별"해주는 함수

# return 값
#   값을 되돌려주고 함수가 끝남. 함수 내 return 아래 부분은 실행되지 않음.
# (정의)
# def 함수명(변수명, 변수명,  ...):
#   함수내용
#   함수내용
#   ...
#   return 값 <- 값 반환

def getIsOdd(num):
    isEven = num%2 == 1
    return isEven

# 숫자를 하나 넣으면
# x2 한 결과를 구해주는 함수

def getDouble(num):
    return num*2


# 숫자 2개 넣으면 합, 차, 곱, 나누기 값을 구해주는 함수
def getCalculate(num1, num2):
    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    d = num1 / num2
    return a, b, c, d # Tuple - 튜플의 문법 괄호는 제외해도됨.

# 어떤 함수의 결과가 여러개(return이 여러개)는 불가능.
# => collection 하나로 반환하면 가능


# 언제 쓰는건지? : 최종결과물에서 어디쓰냐 체감되면 됨.


####################

# 함수 호출 (다른 언어의 main 같은 느낌?)

aa, bb, cc, dd = getCalculate(20, 30)
print(aa, type(aa))

# sum 호출해서 출력
print(getCalculate(20, 30))

num = 10
printIsOdd(5)
printIsOdd(6)

b = getDouble(2)
sleep(b)

a = getIsOdd(5)
print(a)
