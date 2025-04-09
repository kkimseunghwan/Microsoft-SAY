

from ConsoleScreen import ConsoleScreen
from DAO.SPVDAO import SPVDAO
from DAO.CompanyDAO import CompanyDAO


if __name__ == "__main__":
    cDAO = CompanyDAO()
    sDAO = SPVDAO()

    while True:
        menu = int(input("계속 하기 : "))
        if menu == 1:
            # 1. 회사 검색.
            companyName = ConsoleScreen.setCompanyName()
            companies = cDAO.searchCompanyName(companyName)
            ConsoleScreen.printCompanyList(companies)

            # 원하는 회사에 대응하는 제품 검색, 출력
            companyName = ConsoleScreen.setCompanyName()
            spvs = sDAO.getDataByCompanyName(companyName)
            ConsoleScreen.printSPVInfo(spvs)




