


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
        print("7) 회사 검색")
        print("8) 과자 검색")
        print("9) 과자 정보 조회")
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
    def showSearchMenu():
        return input("검색어 : ")

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
        return input("페이지(1 ~ %d) : " % allPage)
    
        
    @staticmethod
    def showCompanyInfo(companies):
        for company in companies:
            print("%s\t%s\t%s\t%d" % (company.name, company.addr, company.ceo, company.emp))

    @staticmethod
    def showSnacksInfo(snacks):
        for snack in snacks:
            print("%d %s  %s  %d  %d  %s" % (snack.no, snack.name, snack.exp, snack.price, snack.weight, snack.c_name))
    
    @staticmethod
    def showSnacksInfo2(snackInfo):
        for snack in snackInfo:
            print("[%d] %s : %d원 %dg\n유통기한 : %s\n%s\n> %s\n> %s\n> %d" % (snack.no, snack.name, snack.price, snack.weight, snack.exp, snack.c_name, snack.c_addr, snack.c_ceo, snack.c_emp))

    # no, name, exp, price, weight, c_name, c_addr, c_ceo, c_emp 
    @staticmethod
    def showSnacksInfoVer2(snacks):
        for snack in snacks:
            print("[%d] %s : %d원(%dg)" % (snack.no, snack.name, snack.price, snack.weight))
            print("유통기한 : %s" % snack.exp)
            print("회사:%s" % snack.c_name)
            #print("> 위치: %s" % companyDict[snack.c_name].addr)
            #print("> 사장: %s" % companyDict[snack.c_name].ceo)
            #print("> 직원: %s" % companyDict[snack.c_name].emp)
            print("> 위치: %s" % snack.c_addr)
            print("> 사장: %s" % snack.c_ceo)
            print("> 직원: %s" % snack.c_emp)

    @staticmethod
    def showResult(result):
        print(result)

    

    






