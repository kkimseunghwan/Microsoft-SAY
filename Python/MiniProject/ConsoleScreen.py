
# View
class ConsoleScreen:

    # 회사 이름 검색 후 리턴
    @staticmethod
    def setCompanyName():
        return input("회사 이름 검색 : ")
    
    # 제품 정보 출력
    @staticmethod
    def printSPVInfo(spvs):
        for data in spvs:
            print(data.m_no, data.m_name, data.m_price, data.m_maker, data.c_link, data.m_c_no)

    # 제품 정보 출력
    @staticmethod
    def printCompanyList(companies):
        print("-- 회사 목록 --")
        for data in companies:
            print(data)
        print("--------")
        

    pass