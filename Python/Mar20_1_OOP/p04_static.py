
# static member variable : 스태틱 멤버 변수
#   메모리의 static 영역에 만들어지고 
#   메모리를 아낄 수 있는데,
#   Python은 알.빠.노 임
#   Python도 static member variable 가 있기는 있는데,
#   극적인 메모리 아끼는 효과가 나지 않음 : 사실상 없는 취급


# static method : 스태틱 메소드

# 지역변수 : 그 함수에서 쓰고 버릴 임시 변수
# 파라메터 : 그 함수에서 길행하는데 필요한 재료. (매개변수)
# 멤버변수 : 객체의 속성

# 멤버 변수가 없음. -> 저장할게 없음.

class Calculator:
    # 잘못된 접근! x,y는 객체의 속성이 아님
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    
    # Static Method : 객체를 만들지 않고도 사용할 수 있는 메소드.
    # 메소드 파라메터에 self를 뺴면 구현 가능.

    # x, y => 계산기가 덧셈(액션)을 하기 위한 재료이므로, 파라메터로 사용
    @staticmethod # 스태틱 메소드 선언 (안해도됨. 가독성) +(저거 없으면 빨간줄 찍어주는 툴이 존재 - 작동은됨)
    def PrintSum(x, y):
        print("%d + %d = %d" % (x, y, x + y))

####################


# static 메소드 호출
# 클래스명. 메소드명(...)
Calculator.PrintSum(1, 2)

# 일반 메소드 호출
# 변수명.메소드명(...)
# c = Calculator()
# c.PrintSum(1, 2)


# 변수는 언제 만드는건지?
#   => 데이터 임시 저장할 때. 

# 객체는 언제 만드는건지? 왜 만드는건지?
#   => 데이터를 실생활스럽게 임시 저장해야 할 때

# 그 상황이 아니라면, 안만들어야



