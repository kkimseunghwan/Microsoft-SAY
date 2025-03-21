
# 상속 연습

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print("제품명 : %s" % self.name)
        print("가격 : %d만원" % self.price)


# 신발
# 제품명 : 조던123
# 가격 : 10000
# 사이즈 : 250

class Shoes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def printInfo(self):
        super().printInfo()
        print("사이즈 : %d" % self.size)

# 컴퓨터
# 제품명 : 매직스테이션123, 가격 200만, cpu, ram, hdd, 

class Computer(Product):
    def __init__(self, name, price, cpu, ram, hdd):
        super().__init__(name, price)
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    
    def printInfo(self):
        super().printInfo()
        print("cpu : %s" % self.cpu)
        print("ram : %dgb" % self.ram)
        print("hdd : %dgb" % self.hdd)

# 노트북
# Gram123, 가격, cpu, ram, hdd, 무게 3Kg
class Notebook(Computer):
    def __init__(self, name, price, cpu, ram, hdd, weight):
        super().__init__(name, price, cpu, ram, hdd)
        self.weight = weight
    
    def printInfo(self):
        super().printInfo()
        print("무게 : %dKg" % self.weight)
        

####################

s = Shoes("조던123", 10, 250)
s.printInfo()

print("-----")

c = Computer("매직스테이션123", 200, "i5-1234", 16, 500)
c.printInfo()

print("-----")

n = Notebook("그램123", 250, "i7-4567", 32, 250, 3)
n.printInfo()

print("-----")


# class dog: 정의 시, 상속을 지정해주지 않으면
# class dog(object): object 로부터 상속을 받게됨 <= 기본으로 자동 상속됨. 