

from p02_Guest import Guest


class ConsoleScreen:
    @staticmethod
    def GetGuestInfo():
        name = input("이름 : ")
        height = input("키 : ")
        weight = input("몸무게 : ")

        # Guest 객체로 리턴
        return Guest(name, height, weight)
    
    @staticmethod
    def tellResult(guest):
        print("%s씨의 BMI는 %.2f" % (guest.name, guest.BMI))
        print("%s 입니다" % guest.result)
    

