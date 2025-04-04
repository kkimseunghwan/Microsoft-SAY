
# 이름이 모나피123, 색 빨, 가격 500원

# 1), 2) => 멤버 변수를 따로 안하고, 생성자에서 결정 짓는 형태로 많이들 작업
class Pen:
    # 1)어차피 외부에서 추가할 수 있음 => 밖에다 쓰는게 무슨 의미가..
    # name = None
    # color = None
    # price = None

    # 2) Python은 overloading이 불가능하니 생성자는 하나만 가능
    # => 펜 만들려면 이름, 색, 가격 써야함.
    # 생성자에서 결정 짓는 형태로 많이들 작업
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __del__(self):
        print(self, "ㅃㅇ")

    def printInfo(self):
        print(self.name)
        print(self.color)
        print(self.price)
        pass

####################

# Garbage Collection : GC
#   메모리 자동 정리 시스템.
#   stack : 프로그램 종료 시 자동으로 정리됨.
#   heap : 자동정리x, 개발자가 직접 정리 해야 하는 영역.
#   GC : heap 영역을 자동으로 정리해줌.
#       => 그 자동 정리를 언제 해주는데?
#           => 그 번지를 더 이상 사용하지 못하게 되는 시점 
#           => 그 번지를 가리키던 변수가 더 이상 안가리키게 되면
#   => Python은 정리는 어떻게든 다 됨. 프로그램 종료시 정리 댐


# destructor (소멸자)
#   객체가 없어질 때 뭔가 작업을 진행.
#   => 얘로 확인 가능.

myPen = Pen("모나미123", "Red", 500)
myPen.printInfo()
Pen.printInfo(myPen)

print("-----")

myP = Pen("모나미153", "Blue", 1000)
myP.printInfo()
Pen.printInfo(myP)
del myP

# myPen 과 속성이 같은 펜. x
# => p를 p3로도 부르게 하자. o
p3 = myPen # 동일한 하나의 객체를 가리키는 myPen과 동일한 주소값이 p3 스택 영역에 저장
p3.printInfo()

myPen.price = 300
myPen.printInfo()

p3.printInfo() # 얘도 price 값이 300으로 바뀜.

print("-----")

# 1TB 데이터를 16GB짜리 램으로 분석 => 되겠냐?