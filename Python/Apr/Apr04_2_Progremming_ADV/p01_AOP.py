
# 프로그래밍 패러다임
# Procedural Programming
#       절차지향 프로그래밍
#       순서대로 잘 써서 결과를 내자

# OOP
# Object Oriented Programming
#      객체지향 프로그래밍
#      실생활을 표현해서 유지보사 쉽게 하자 (컴퓨터 성능이 올라갔으니 -> 유지보수를 중심으로..)

# AOP
# Aspect Oriented Programming
#       관점지향 프로그래밍
#       OOP를 다른 관점에서 보자.
#       메소드들에 공통된 부분이 보ㅇ일텐데,
#       공통된 부분을 따로 메소드 정리

## OOP ##
# 홍길동, 30살인 사람 
# 정보 출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print("%s, %d살 사람" % (self.name, self.age))

    def ready(self):
        print("씻고, 옷입고")
        print("나가서 엘베타고 내려가")

    def goSchool(self):
        self.ready() 
        print("벼스타고 학교로..")

    def goPark(self):
        self.ready()
        print("자전타고 공원으로..")

    def goMart(self):
        self.ready() 
        print("걸어서 마트로..")

h = Person("홍길동", 30)
h.printInfo()
h.goMart()
h.goPark()
h.goSchool()


