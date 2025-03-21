
# 어벤져스
#   본명
#   나이
#   공격하기
#   출력하기

class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def attack(self):
        print("공격")

    def printInfo(self):
        print(self.name)
        print(self.age)

class Human:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def eat(self):
        print("냠")

    def printInfo(self):
        print(self.name)
        print(self.address)
        

# 로 부터 상속받는 아이언맨   # Ironma is a Avengers
# 아이언맨은 사람임           # Ironman is a Human
# 다중 상속 : 여러 클래스로부터 상속
#   대부분의 프로그래밍 언어] 멤버의 이름이 같으면? ㅈㄴ애매함.
#   Python] 얜 가능
#   - 가능은 한데, 어지러움은 인간의 몫
#   - 상속한 멤버의 이름이 중복될 경우 : 먼저 상속한걸로
class IronMan(Avengers, Human):
    pass
####################

i = IronMan("토니", 40)
i.attack()
i.eat()
i.printInfo()
