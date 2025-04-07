


from datetime import datetime
from Snack import Snack
from Company import Company


class ConsoleMainMenu:

    @staticmethod
    def showMainMenu():
        print("----------")
        print("1) 회사등록")
        print("2) 과자 등록")
        print("3) 회사 전체 조회")
        print("4) 과자 전체 조회")
        print("5) 회사 조회")
        print("6) 과자 조회")
        print("...")
        print("10) 종료")
        print("----------")

    @staticmethod
    def getMainMenu():
        menu = input("뭐 : ")
        return menu
    
    @staticmethod
    def getRegCompanyInfo():
        print("-----")
        name = input("회사 이름 : ")
        addr = input("회사 주소 : ")
        ceo = input("사장 이름 : ")
        emp = input("직원 수 : ")
        return Company(name, addr, ceo, emp)
    
    @staticmethod
    def getRegSnackInfo():
        print("-----")
        name = input("과자 이름 : ")
        exp = input("유통기한 : ")
        price = input("가격 : ")
        weight = input("질량 : ")
        c_name = input("담당 회사 : ")
        return Snack(name, exp, price, weight, c_name)
    
    @staticmethod
    def getSelectPage(allPage):
        print("-----")
        print("전체 페이지 >> %d" % allPage)
        page = input("확인할 페이지 : ")
        return page
    
        
    @staticmethod
    def showCompanyInfo(companies):
        for company in companies:
            print("%s\t%s\t%s\t%d" % (company.name, company.addr, company.ceo, company.emp))

    @staticmethod
    def showSnacksInfo(snacks):
        for snack in snacks:
            print("%d %s  %s  %d  %d  %s" % (snack.no, snack.name, snack.exp, snack.price, snack.weight, snack.c_name))

    @staticmethod
    def showResult(result):
        print(result)

    

    






