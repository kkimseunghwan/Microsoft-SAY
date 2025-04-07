
from datetime import datetime
from Snack import Snack
from DB_Set.DBManager import DBManager


class SnackDAO:
    # 등록하기
    def registration(snack):
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"INSERT INTO APR07_SNACK VALUES(APR07_SNACK_SEQ.nextval, '{snack.name}', to_date('{snack.exp}', 'YYYYMMDD'), {snack.price}, {snack.weight}, '{snack.c_name}')"
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
    # 얜 그냥 연습용, 실전에서 이러면 컴터 터짐
    # 
    def SelectALL():
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
    def GetAllSnackCount():
        try:
            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT COUNT(*) FROM APR07_SNACK"
            cur.execute(sql) # 매니저 겸 출력값 저장.
            
            for count in cur:
                if count[0]//3 < count[0]/3:
                    return count[0]//3 + 1
                else:
                    return count[0]//3
            
        except Exception as e:
            print("ERROR", e)
            return None
        finally:
            DBManager.closeConCur(con, cur)


    ####
    def GetSnackTargetPage(targetPage, allPage):
        try:
            if targetPage > allPage:
                return None
            
            startPage = targetPage*2 + (targetPage-2)
            endPage = startPage + 2

            con, cur = DBManager.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM (SELECT rownum AS RN, S_NAME, S_EXP, S_PRICE, S_WEIGHT, S_C_NAME FROM (SELECT S_NAME, S_EXP, S_PRICE, S_WEIGHT, S_C_NAME FROM APR07_SNACK ORDER BY S_NAME, S_PRICE)) "
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

    