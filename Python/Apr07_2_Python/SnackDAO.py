
from datetime import datetime
from math import ceil, floor
from Snack import Snack
from DB_Set.DBManager import DBManager

# 변수 만드는 이유 = 데이터 임시저장
# 객체 만드는 이유 = 데이터를 실생활스럽게 wjwkd
#   멤버변수가 없음
class SnackDAO:
    # 생성자.
    def __init__(self):
        self.setAllSnackCount()
        self.snackPerPage = 3

    # 등록하기
    def registration(self, snack):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"INSERT INTO APR07_SNACK VALUES(APR07_SNACK_SEQ.nextval, '{snack.name}', to_date('{snack.exp}', 'YYYYMMDD'), {snack.price}, {snack.weight}, '{snack.c_name}')"
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                self.allSnackCount += 1
                return "-- INSERT OK --"
            else:
                return "-- INSERT ERROR --"
            
        except Exception as e:
            print("ERROR", e)
            return "-- INSERT ERROR --"
        finally:
            DBManager.closeConCur(con, cur)

    # 조회하기
    # 얜 그냥 연습용, 실전에서 이러면 컴터 터짐
    # 
    def selectALL():
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM APR07_SNACK ORDER BY s_name, s_price"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            snacks = []
            for no, name, exp, price, weight, c_name in cur:
                snacks.append(Snack(no, name, exp.strftime("%Y%m%d"), price, weight, c_name))

            return snacks
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)


    ## 과자 데이터 전체 개수 구하기 ##
    def setAllSnackCount(self):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT COUNT(*) FROM APR07_SNACK"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            for count in cur:
               self.allSnackCount = count[0]
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)
    
    def getAllPageCount(self, searchTxt=None):
        if searchTxt:
            snackCount = self.getSearchSnackCount(searchTxt) 
        else:
            snackCount = self.allSnackCount
            
            
        return ceil(snackCount / self.snackPerPage)
        


    ####
    def getSnackTargetPage(self,targetPage, searchTxt=""):
        try:
            targetPage = int(targetPage)
            startPage = (targetPage-1) * self.snackPerPage + 1
            endPage = targetPage * self.snackPerPage

            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM ("
            sql += f"SELECT rownum AS RN, S_NAME, S_EXP, S_PRICE, S_WEIGHT, S_C_NAME FROM ("
            sql += f"SELECT S_NAME, S_EXP, S_PRICE, S_WEIGHT, S_C_NAME FROM APR07_SNACK WHERE S_NAME LIKE '%{searchTxt}%' ORDER BY S_NAME, S_PRICE)) "
            sql += f"WHERE RN >= {startPage} AND RN <= {endPage}"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            snacks = []
            for no, name, exp, price, weight, c_name in cur:
                snacks.append(Snack(no, name, exp.strftime("%Y%m%d"), price, weight, c_name))

            return snacks
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)


        ####
    def getSnackInformation(self,targetPage, searchTxt=""):
        try:
            targetPage = int(targetPage)
            startPage = (targetPage-1) * self.snackPerPage + 1
            endPage = targetPage * self.snackPerPage

            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM ("
            sql += f"SELECT rownum AS RN, S_NAME, S_EXP, S_PRICE, S_WEIGHT, S_C_NAME, C_ADDR, C_CEO, C_EMP FROM ("
            sql += f"SELECT * FROM APR07_SNACK s, APR07_COMPANY c WHERE s.S_C_NAME = c.C_NAME AND S_NAME LIKE '%{searchTxt}%' ORDER BY S_NAME, S_PRICE)) "
            sql += f"WHERE RN >= {startPage} AND RN <= {endPage}"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            info = []
            for s_no, s_name, s_exp, s_price, s_weight, s_c_name, c_addr, c_ceo, c_emp in cur:
                info.append(Snack(s_no, s_name, s_exp.strftime("%Y%m%d"), s_price, s_weight, s_c_name).SnackInfo(c_addr, c_ceo, c_emp))

            return info
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)



    def getSearchSnackCount(self, searchTxt):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT COUNT(*) FROM APR07_SNACK WHERE S_NAME LIKE '%{searchTxt}%'"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            for count in cur:
               return count[0]
                        
        except Exception as e:
            print("ERROR", e)
            return -1
        finally:
            DBManager.closeConCur(con, cur)

    