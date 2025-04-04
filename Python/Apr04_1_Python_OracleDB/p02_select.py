
from oracledb import connect, init_oracle_client

try:
    init_oracle_client(lib_dir = "C:\Hwan\Oracle DB\instantclient_23_7")
    con = connect("Hwan/1234@195.168.9.116:1521/xe")
    print("SUCCESS", con)

    sql = f"SELECT * FROM PRODUCT"

    cur = con.cursor() # DB작업 매니저 겸 결과
    cur.execute(sql) # 결과가 cur

    for p_name, p_price in cur:
        print(p_name,"\t",p_price) # 튜플 형태


except Exception as e:
    print("에러에러", e)
finally:
    cur.close()
    con.close()

