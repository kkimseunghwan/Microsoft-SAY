
from hwanlib.hwanDBManager import HwanDB


class SnackDAO():
    def getAll(self):
        try:
            # 아이디/비번@주소:포트/SID
            con, cur= HwanDB.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            print("성공")
            # 전체 조회
            sql = "SELECT * FROM APR23_PRODUCT"
            cur.execute(sql)

            snacks = []
            # 콘솔 출력
            for p_name, p_price in cur:
                s = {"name":p_name, "price":p_price}
                snacks.append(s)
                print(s)
            
            return snacks
            
        except Exception as e:
            print("에러에러", e)
        finally:
            HwanDB.closeConCur(con, cur)
            print("종료")
