

# 1) 회사등록
# ...
# 10) 종료
# ----------
# 뭐 : 1
# => ...
# 10종료 전 까지 반복


from CompanyDAO import CompanyDAO
from SnackDAO import SnackDAO
from p_View import ConsoleMainMenu


# 아래 코드는 반복문이 돌아가면서, 
# 매 호출마다 DB에 연결 및 연결 해제 작업이 반복됨
# => 이게 맞다고 함.
# =>=> 이유는?

# 학생 1명이 DB계정 1개씩
# => 아님, 개발자 여럿이 DB계정 1개 같이 씀.
# 예) 회의실 예약시스템을 쓰는 모든 직원들은 하나의 계정을 다 같이 사용 중.

# DB계정 1개를 여러명이 같이 쓰게 되는데, 
# 계정 하나를 동시에 쓸 수 있는 사람수는 제한되어있음.
# => 계정하나를 빨리 쓰고 빨리 닫아버려야됨. 
# =>=> 그래야 다른 사람들이 그 계정을 쓸 수 있음

# 연결을 한번 해놓은 상태로 작업 진행 시,
# => 다른 사람이 DB를 사용 못하게 될 수 있음.

# 1. 전체 과자 수 구하는 방법.
# 2. 어디다가 쓸까 -> SnackDAO
#

# 전체 과자 수 구하는 방법
#       SELECT COUNT(*) FROM APR07_SNACK 돌리면 나옴
#       Python - DB 서버간의 통신을 해야 함.
#       통신 횟수를 줄이면 좋은데...
# =>
#       이 프로그램 처음 한번만 구해놓고
#       변동 사항 생기면, 코드에서 수동으로 값을 변경

if __name__ == "__main__":
    while True:
        ConsoleMainMenu.showMainMenu()
        menu = ConsoleMainMenu.getMainMenu()
        
        if menu == '1': # 회사 입력
            company = ConsoleMainMenu.getRegCompanyInfo()
            result = CompanyDAO.registration(company)
            ConsoleMainMenu.showResult(result)
        elif menu == '2': # 과자 입력
            snack = ConsoleMainMenu.getRegSnackInfo()
            result = SnackDAO.registration(snack)
            ConsoleMainMenu.showResult(result)
        elif menu == '3': # 회사 전체 조회
            companies = CompanyDAO.SelectALL()
            ConsoleMainMenu.showCompanyInfo(companies)
            pass
        elif menu == '4': # 과자 전체 조회
            snacks = SnackDAO.SelectALL()
            ConsoleMainMenu.showSnacksInfo(snacks)
            pass
        elif menu == '5': # 회사 조회
            pass
        elif menu == '6': # 과자 조회
            snackAllPage = SnackDAO.GetSnackAllPage()
            targetPage = ConsoleMainMenu.getSelectPage(snackAllPage)
            snacks = SnackDAO.GetSnackTargetPage(int(targetPage), snackAllPage)
            ConsoleMainMenu.showSnacksInfo(snacks)
            
            
            

        if menu == '10':
            break
    
    exit()


