

from oracledb import connect, init_oracle_client

try:
    init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")
    con = connect("Hwan/1234@195.168.9.116:1521/xe") 
    print("SUCCESS", con)

    P_NAME = input("업데이트 제품 : ")
    P_PRICE = int(input("변동 가격 : "))

    sql = f"UPDATE PRODUCT SET P_PRICE = {P_PRICE} WHERE P_NAME = '{P_NAME}'"

    cur = con.cursor()
    cur.execute(sql)
    if cur.rowcount:
        print("업데이트 성공")
        con.commit()

except Exception as e:
    print("에러메세지:", e)
finally:
    cur.close()
    con.close()






