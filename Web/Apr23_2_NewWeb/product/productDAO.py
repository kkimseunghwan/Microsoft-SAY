
from hwanlib.hwanDBManager import HwanDB


class ProductDAO():
    def getAll(self):
        try:
            # 아이디/비번@주소:포트/SID
            con, cur= HwanDB.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            print("성공")
            # 전체 조회
            sql = "SELECT * FROM APR23_PRODUCT"
            cur.execute(sql)

            products = []
            # 콘솔 출력
            for p_name, p_price in cur:
                s = {"name":p_name, "price":p_price}
                products.append(s)
                print(s)
            
            return products
            
        except Exception as e:
            print("에러에러", e)
        finally:
            HwanDB.closeConCur(con, cur)
            print("종료")


    def reg(self, name, price):
        try:
            # 아이디/비번@주소:포트/SID
            con, cur= HwanDB.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            print("성공")
            # 데이터 입력
            sql = f"INSERT INTO APR23_PRODUCT VALUES('{name}', {price})"
            cur.execute(sql)

            # 콘솔 출력
            if cur.rowcount == 1:
                print("성공")
                con.commit()

            return {"result": name + " 등록 성공"}
        except Exception as e:
            print("에러에러", e)
            return {"result": name + " 등록 실패"}
        finally:
            HwanDB.closeConCur(con, cur)
            print("종료")

    def delete(self, price_min, price_max):
        try:
            # 아이디/비번@주소:포트/SID
            con, cur= HwanDB.connectDBServer("Hwan/1234@195.168.9.116:1521/xe")
            print("성공")
            # 데이터 삭제
            sql = f"DELETE FROM APR23_PRODUCT "
            sql += f"WHERE {price_min} < P_PRICE and P_PRICE < {price_max}"
            cur.execute(sql)

            # 콘솔 출력
            if cur.rowcount:
                print("성공")
                con.commit()

            return {"result":"삭제 성공"}
        except Exception as e:
            print("에러에러", e)
            return {"result":"삭제 실패"}
        finally:
            HwanDB.closeConCur(con, cur)
            print("종료")


    