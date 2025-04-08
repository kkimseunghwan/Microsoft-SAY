

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
import time


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

# 1
def insertCompany():
    company = ConsoleMainMenu.getRegCompanyInfo()
    result = cDAO.registration(company)
    ConsoleMainMenu.showResult(result)

# 2
def insertSnack():
    snack = ConsoleMainMenu.getRegSnackInfo()
    result = sDAO.registration(snack)
    ConsoleMainMenu.showResult(result)

# 3
def selectCompanyALL():
    companies = CompanyDAO.selectALL()
    ConsoleMainMenu.showCompanyInfo(companies)

# 4
def selectSnackALL():
    snacks = SnackDAO.selectALL() 
    ConsoleMainMenu.showSnacksInfo(snacks)

# 5
def selectCompanyPage():
    allPage = cDAO.getAllPageCount()
    targetPage = ConsoleMainMenu.getSelectPage(allPage)
    companies = cDAO.getCompanyTargetPage(targetPage) 
    ConsoleMainMenu.showCompanyInfo(companies)

# 6
def selectSnackPage():
    allPage = sDAO.getAllPageCount()
    targetPage = ConsoleMainMenu.getSelectPage(allPage)
    snacks = sDAO.getSnackTargetPage(targetPage)
    ConsoleMainMenu.showSnacksInfo(snacks)

# 7
def selectCompanySearch():
    searchTxt = ConsoleMainMenu.showSearchMenu()
    allPage = cDAO.getAllPageCount(searchTxt)
    if allPage == 0:
        raise LookupError("검색한 값이 없음")
    targetPage = ConsoleMainMenu.getSelectPage(allPage)
    companies = cDAO.getCompanyTargetPage(targetPage, searchTxt)
    ConsoleMainMenu.showCompanyInfo(companies)

# 8
def selectSnackSearch():
    searchTxt = ConsoleMainMenu.showSearchMenu()
    allPage = sDAO.getAllPageCount(searchTxt)
    if allPage == 0:
        raise LookupError("검색한 값이 없음")
    targetPage = ConsoleMainMenu.getSelectPage(allPage)
    snacks = sDAO.getSnackTargetPage(targetPage, searchTxt)
    ConsoleMainMenu.showSnacksInfo(snacks)

# (비효율 ver.)
#9 - 1 > JOIN 사용 
def selectFullInformation():
    searchTxt = ConsoleMainMenu.showSearchMenu()
    allPage = sDAO.getAllPageCount(searchTxt)
    if allPage == 0:
        raise LookupError("검색한 값이 없음")
    targetPage = ConsoleMainMenu.getSelectPage(allPage)
    start = time.time()
    snackInfo = sDAO.getSnackInformation(targetPage, searchTxt)
    ConsoleMainMenu.showSnacksInfo2(snackInfo)
    end = time.time()
    print("동작 시간", end - start)

# 9 - 2 : 딕셔너리로 데이터 조회
def selectFullInformation():
    searchTxt = ConsoleMainMenu.showSearchMenu()
    allPage = sDAO.getAllPageCount(searchTxt)
    if allPage == 0:
        raise LookupError("검색한 값이 없음")
    targetPage = ConsoleMainMenu.getSelectPage(allPage)
    start = time.time()
    snacks = sDAO.getSnackTargetPage(targetPage, searchTxt)
    companyDict = cDAO.getCompanyDictData()
    ConsoleMainMenu.showSnacksInfoVer2(snacks, companyDict)
    end = time.time()
    print("동작 시간", end - start)
# JOIN보다 시간이 오래 걸림. << 이 방법은 아닌듯 - 폐기
#   >>> 아 DB서버에서 데이터를 불러오는 시간을 신경쓴다면 더 느리겠네.
# Snack과 Company의 데이터를 따로따로 가지고 와서 작업 한다면,
# 데이터를 불러오는 시간으로 인해서, 시간이 오래 걸릴 수 있음
# > 그렇다고 대용량 데이터 연산을 서버에서 진행하게 한다? -> 메모리 터짐
# =>> 그럼?????

# 통신 한번으로 데이터를 전달받아 시간을 절약하려면? 
#   서버에서 모든 연산 후, 전달해줘야하고
#       => 메모리 터짐
# 서버에서 연산하는게 부담스러우면? 
#   데이터를 따로따로 받아와서 조건에 대한 출력을 진행하게 하고
#       => 최적화 박음
# 흠

# 시작할 때, 한번 들고와서 가지고 있으면 안되나? <= 이러면 맨 처음만 데이터 받는 시간 걸리니까
# INSERT로 값 입력하면 DB에 적용시키고, 추가한 값은 객체 형식으로 리스트에 넣기 > 메모리 터지려나?
#   아 근데 페이지 형식으로 조회 하는거는 정렬, 추가 연산이 필요해서 안될 것 같기도 하다


## 정답 ##
# 1) JOIN 시키지 말고
# 과자"만" 조회
# -> Python으로 과자의 회사이름을 통한 회사 정보를 조회 해와서
#       붙이는 형식
# N+1 문제?

# 2) JOIN은 시키는데, 전체 말고 필요한 부분만 JOIN해서 연산을 줄이기.






# 10
def exit_loop():
    raise StopIteration("루프 종료")

command = {
    '1':insertCompany,
    '2':insertSnack,
    '3':selectCompanyALL,
    '4':selectSnackALL,
    '5':selectCompanyPage,
    '6':selectSnackPage,
    '7':selectCompanySearch,
    '8':selectSnackSearch,
    '9':selectFullInformation,
    '10':exit_loop
}

if __name__ == "__main__":
    sDAO = SnackDAO()
    cDAO = CompanyDAO()
    
    while True:
        ConsoleMainMenu.showMainMenu()
        menu = ConsoleMainMenu.getMainMenu()
        try:
            if menu in command:
                command[menu]()
        except LookupError as e:
            print(e)
            continue
        except StopIteration as e:
            print(e)
            break

            
    


'''
if __name__ == "__main__":
    sDAO = SnackDAO()
    cDAO = CompanyDAO()
    
    while True:
        ConsoleMainMenu.showMainMenu()
        menu = ConsoleMainMenu.getMainMenu()
        
        if menu == '1': # 회사 입력
            company = ConsoleMainMenu.getRegCompanyInfo()
            result = cDAO.registration(company)
            ConsoleMainMenu.showResult(result)
        elif menu == '2': # 과자 입력
            snack = ConsoleMainMenu.getRegSnackInfo()
            result = sDAO.registration(snack)
            ConsoleMainMenu.showResult(result)
        elif menu == '3': # 회사 전체 조회
            companies = CompanyDAO.selectALL()
            ConsoleMainMenu.showCompanyInfo(companies)
        elif menu == '4': # 과자 전체 조회
            snacks = SnackDAO.selectALL()
            ConsoleMainMenu.showSnacksInfo(snacks)
        elif menu == '5': # 회사 조회
            allPage = cDAO.getAllPageCount()
            targetPage = ConsoleMainMenu.getSelectPage(allPage)
            companies = cDAO.getCompanyTargetPage(targetPage) 
            ConsoleMainMenu.showCompanyInfo(companies) 
        elif menu == '6': # 과자 조회
            allPage = sDAO.getAllPageCount()
            targetPage = ConsoleMainMenu.getSelectPage(allPage)
            snacks = sDAO.getSnackTargetPage(targetPage)
            ConsoleMainMenu.showSnacksInfo(snacks)
        elif menu == '7': # 회사 선택 검색
            searchTxt = ConsoleMainMenu.showSearchMenu()
            allPage = cDAO.getAllPageCount(searchTxt)

            targetPage = ConsoleMainMenu.getSelectPage(allPage)
            companies = cDAO.getCompanyTargetPage(targetPage, searchTxt)
            ConsoleMainMenu.showCompanyInfo(companies)
        elif menu == '8': # 과자 선택 검색
            searchTxt = ConsoleMainMenu.showSearchMenu()
            allPage = sDAO.getAllPageCount(searchTxt)

            targetPage = ConsoleMainMenu.getSelectPage(allPage)
            snacks = sDAO.getSnackTargetPage(targetPage, searchTxt)
            ConsoleMainMenu.showSnacksInfo(snacks)
            
        if menu == '10':
            break
    
    exit()
'''


