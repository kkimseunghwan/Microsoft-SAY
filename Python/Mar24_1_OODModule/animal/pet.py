
from os import name


class Dog:
    def __init__(self, name):
        self.name = name

    def printInfo(self):
        print(self.name)

# import 해온 class, 여기에 class 이름 중복되면?
# A에서 받아온 class, B에서 받아온 class 이름 중복되려면?
# => 패키지명 / 모듈명이 아예 생략되는 3번으로 해결불가
# => 1, 2도 필요함.

d = Dog("만득이")
d.printInfo()






