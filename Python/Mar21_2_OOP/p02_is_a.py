
# 상속

# 아래 문장 중 말이 되는 것.
#   Dog is a Cat = X
#   Father is a Son = X
#   Man is a Woman = X
#   Taxi is a Car = O 
#   => OOP가 말하는 상속을 쓸 수 있음

# 쇼핑몰을 만들자#
#   Pen is a product => OOP가 말하는 상속을 쓸 수 있음

####################
# 다른언어] 생성자는 상속을 안시킴.
# Python] 보통 생성자에서 멤버 변수를 정하는데,  
#           => 멤버 변수 상속을 안시키는?
#           => 생성자도 상속됨.

# 제품명 : 삼성123
# 가격이 50만원
# 상품을 만들고 정보를 출력

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print("제품명 : %s" % self.name)
        print("가격 : %d" % self.price)

# 상속
# Pen is a Product
#   => OOP가 말하는 상속(확장) 개념 사용 가능
#   Product의 멤버들(멤버변수, 메도스)이 Pen에도 전달됨.
#   (+) 펜은 색깔이 추가로 필요

class Pen(Product): # Product로 부터 상속 받은 Pen클래스
    
    # 생성자 Overriding이 아님.
    def __init__(self, name, price, color):
        super().__init__(name, price) # printInfo()의 __init__ 호출 => 이름, 가격 세팅.
        self.color = color

    def printInfo(self):
        # printInfo를 상속 받았는데, 이름/가격 출력 기능만 있음 
        # 색낄도 출력되게
        # ovverriding : 상속받은 메소디 기능 바꾸기
        #   +> 바꾸기보다는 추가 형태로 많이.

        super().printInfo() #Product의 printInfo()호출 -> 이름, 가격 출력  
        print("펜은 %s색" % self.color) # 차기 기능 정의

        
    pass # 아무것도 없을 때, Product로부터 멤버들을 받아옴.

####################

a = Product("삼성123", 500000)
a.printInfo()

pen = Pen("모나미153", 1500, "빨강")
pen.printInfo()


