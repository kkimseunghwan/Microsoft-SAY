
from math import ceil
from Company import Company
from DB_Set.DBManager import DBManager


class CompanyDAO:
    # 생성자.
    def __init__(self):
        self.setAllCompanyCount()
        self.companyPerPage = 2

    # 등록하기
    def registration(self, company):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"INSERT INTO APR07_COMPANY VALUES('{company.name}', '{company.addr}', '{company.ceo}', {company.emp})"
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allCompanyCount += 1
                return "-- INSERT OK --"
            else:
                return "-- INSERT ERROR --"
            
        except Exception as e:
            print("ERROR", e)
            return "-- INSERT ERROR --"
        finally:
            DBManager.closeConCur(con, cur)

    # 조회하기
    def selectALL():
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM APR07_COMPANY ORDER BY c_name"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            companies = []
            for name, addr, ceo, emp in cur:
                companies.append(Company(name, addr, ceo, emp))
            
            return companies
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)

    ## 과자 데이터 전체 개수 구하기 ##
    def setAllCompanyCount(self):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT COUNT(*) FROM APR07_COMPANY"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            for count in cur:
               self.allCompanyCount = count[0]
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)
    
    def getAllPageCount(self, searchTxt=None):
        if searchTxt:
            companyCount = self.getSearchCompanyCount(searchTxt)
            pass
        else:
            companyCount = self.allCompanyCount

        return ceil(companyCount / self.companyPerPage)
        
    ## 페이지 검색 ##
    def getCompanyTargetPage(self,targetPage, searchTxt=""):
        try:
            targetPage = int(targetPage)
            startPage = (targetPage-1) * self.companyPerPage + 1
            endPage = targetPage * self.companyPerPage

            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM ("
            sql += f"SELECT rownum AS RN, C_NAME, C_ADDR, C_CEO, C_EMP FROM ("
            sql += f"SELECT * FROM APR07_COMPANY WHERE C_NAME LIKE '%{searchTxt}%' ORDER BY C_NAME)) "
            sql += f"WHERE RN >= {startPage} AND RN <= {endPage}"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            companies = []
            for _, name, addr, ceo, emp in cur:
                companies.append(Company(name, addr, ceo, emp))

            return companies
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)

    def getSearchCompanyCount(self, searchTxt):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT COUNT(*) FROM APR07_COMPANY WHERE C_NAME LIKE '%{searchTxt}%'"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            for count in cur:
               return count[0]
                        
        except Exception as e:
            print("ERROR", e)
            return -1
        finally:
            DBManager.closeConCur(con, cur)


# 어짜피 리스트에 넣는 건 어쩔 수 없는거잖아. 이건 데이터가 많아도 해야되는거임.
# 그럼 회사의 데이터 저장을 리스트가 아니라 딕셔너리로 해서 저장하고
# 과자의 s_c_name을 키로 해서 회사의 데이터를 조회 하면, 개빠르지 않을까?
# 그걸로 출력 시키는거임
# 연결은 대가리 깨지면서 하면 어떻게든 되지 않을까?

    ## 옆동네 Snack 데이터를 위한 딕셔너리 생성 함수 ##
    def getCompanyDictData(self):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM APR07_COMPANY"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            companies = {}
            for name, addr, ceo, emp in cur:
                companies[name] = Company(name, addr, ceo, emp)

            return companies
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)


    ## 옆동네 Snack에 붙어있는 "회사 이름"으로 조회 ###
    def getCompanyForName(self, c_name):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM APR07_COMPANY WHERE c_name = '{c_name}'"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            companies = {}
            for name, addr, ceo, emp in cur:
                companies[name] = Company(name, addr, ceo, emp)

            return companies
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)



