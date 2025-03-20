# constructor (생성자)
#    핸드폰 객체가 만들어질 때, 뭔가 작업을 하고 싶음.
#    메소드 

# destructor (소멸자)
#   객체가 없어질 때 뭔가 작업을 진행.


# 핸그폰 표현

class Phone:
    model = None
    maker = None
    cost = None

    # 기본 생성자 (default constructor)
    #   클래스에 생성자 작업을 해놓지 않으면,
    #   Python이 자동으로 생성자를 만들어서 씀.
    def __init__(self): # 객체가 만들어질 때, 해당 메소드 자동 호출됨
        print("핸드폰 입고됨.")
        pass

    def __del__(self): # 소멸자
        print("객체 삭제됨")
        pass

    def printInfo(self):
        print(self.model)
        print(self.maker)
        print(self.cost)

class Computer:
    cpu = None
    ram = None
    hdd = None

    # Python은 overloading이 불가능
    # 생성자 여러개 만들어 놓고 => 필요한거 갖다 쓰기 불가능.
    # => 파이썬 생성자는 하나만 가능
    def __init__(self, c, r, hdd):
        self.cpu = c # c값을 받아와서 멤버변수 cpu에 할당
        self.ram = r
        self.hdd = hdd # 
        pass

    def printInfo(self):
        print(self.cpu, self.ram, self.hdd)

    def TEST(self):
        print("asd")


#########################

# 객체 생성
# 변수명 = 클래스명()
#           생성자 메소드를 호출하는 셈.

myPhone = Phone() # 객체 생성과 동시에, __init__ 메소드 자동 실행.
myPhone.model = "S22"
myPhone.maker = "SAMSUNG"
myPhone.cost = 100
myPhone.printInfo()
Phone.printInfo(myPhone)

# 객체를 만들 때, 클래스의 멤버 변수 값을 설정
c = Computer("i5-1234", 16, 500)
c.printInfo()
Computer.printInfo(c)

c2 = Computer("i7-7890", 32)


