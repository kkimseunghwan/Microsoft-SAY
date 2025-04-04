
# x = int(input())
# y = int(input())
# print("-----")
# print(x/y)



# [ exception ]
# x = 10
# y = 0
# => 오루 Zerodivision 
# 수학에서 나누기 0은 없음
# 사용자는 몰랐음 => 나누기 0 시도하다가 실패
# -> 개발자에게 문의

# exception handling
#   오류가 나지 않게 대비책을 마련해놓자
#   문제 생길만한거를 미리 파악해서 대비책을 마련해놓자
#       java : 처리안해놓으면 에러
#       python : 자유의 언어. 하든 말든 알빠노

#   try:
#       일단 여기를 실행
#   except 예외이름 as 별칭:
#       별칭에 예외 사유가
#       그 문제가 발생하면 여기서 실행
#   except 예외이름:
#       그 문제가 발생하면 여기서 실행
#   ...
#   else:
#       아무 문제도 없었으면 여기가 실행    
#   finally:
#       문제가 있었든 없었든, 무조건 실행행

x = int(input())
y = int(input())

try:
    d = x / y
    print("-----")
    print(d)
    e = [ 54, 123, 3 ]
    print(e[y])
except Exception as e:
    print(e) # 개발하는동안..., 개발종료떄 지우고고
    print("어쨋든 잘못됨")
else:
    print("문제 없음")
finally:
    print("문제 발생여부 상관없이 어쟀든 실행???")

# OOP
#   polymorphism (다형성)
#       상위타입(Animal)변수에 하위타입(Dog)데이터 넣는게 가능.

# a의 자료형? 
a = 10   # int? - X
a = 'ㅋ' # str? - X

# 1) Python은 자료형을 자동으로 지정해준다
# 2) Python은 자료형을 바꾸는 것도 가능하다.

# PYTHON]
#    => 1) Python은 다 객체
#    PYthon 모든 변수의 자료형은 처음부터 : object 타입
#    상위타입(object)변수에 하위타입 (Dog, str, int, ...)
#    -> 다형성을 늘 써왔음

