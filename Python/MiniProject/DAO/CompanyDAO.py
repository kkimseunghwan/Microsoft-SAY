
from DB_Set.DBManager import DBManager
from DTO.Company import Company

class CompanyDAO:
    
    def searchCompanyName(self, companyName):
        try:
            con, cur = DBManager.connectDBServer("seong/137@195.168.9.116:1521/xe")
            sql = f"SELECT DISTINCT C_NAME FROM COMPANY WHERE C_NAME LIKE '%{companyName}%'"
            cur.execute(sql)
            companies = []
            for c_name in cur:
                companies.append(c_name[0])

            return companies
        except Exception as e:
            print("ERROR", e)
        finally:
            DBManager.closeConCur(con, cur)





