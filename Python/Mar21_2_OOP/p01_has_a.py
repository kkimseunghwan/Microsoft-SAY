
# ** 객체관의 관계
#   has a = 속성
#   Human has a Dog : 반려동물
#   is a

####################
# 이름이 만득이, 나이가 2살인 개.
class Dog:
    def __init__(self, name, age, bug):
        self.name = name
        self.age = age
        self.bug = bug
        pass

    def printInfo(self):
        print("이름이 %s, 나이가 %d살" % (self.name, self.age))
        self.bug.printInfo()

# 정보 출력

# 이름이 홍길동, 집이 인천인 사람
#   이 키우는 2살짜리 만득이라는 개
#       몸에 붙어있는 5mm짜리, 빈대라는 벌레가 출력력
# 정보 출력
class Human:
    def __init__(self, name, house, pet):
        self.name = name
        self.house = house
        self.pet = pet

    def checkBug(self, bug):

        pass

    def printInfo(self):
        print("이름이 %s, 집이 %s인 사람" % (self.name, self.house))
        self.pet.printInfo()
        
class Bug:
    def __init__(self, size, name):
        self.size = size
        self.name = name
    
    def printInfo(self):
        print("몸에 붙어있는 %dmm짜리, %s라는 벌레" % ( self.size, self.name ))

####################

print("-----")

h = Human("홍길동", "인천", Dog("만득이", 2, Bug(5, "빈대")))
h.printInfo()

print("-----")

# h의 이름
print(h.name)

# h가 키우는 개 이름
print(h.pet.name)

# h가 키우는 개 모든정보
h.pet.printInfo()

# h가 키우는 개에 붙어있는 벌레 이름
print(h.pet.bug.name)

# h가 키우는 개의 붙어있는 벌레 모든정보
h.pet.bug.printInfo()


