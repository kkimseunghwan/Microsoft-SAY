
from Company import Company
from DB_Set.DBManager import DBManager


class CompanyDAO:
    # 등록하기
    def registration(company):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"INSERT INTO APR07_COMPANY VALUES('{company.name}', '{company.addr}', '{company.ceo}', {company.emp})"
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "-- INSERT OK --"
            else:
                return "-- INSERT ERROR --"
            
        except Exception as e:
            print("ERROR", e)
            return "-- INSERT ERROR --"
        finally:
            DBManager.closeConCur(con, cur)

    # 조회하기
    def SelectALL():
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