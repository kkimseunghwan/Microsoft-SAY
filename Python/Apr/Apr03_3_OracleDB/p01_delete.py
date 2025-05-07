

from oracledb import connect, init_oracle_client

try:
    init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")
    con = connect("Hwan/1234@195.168.9.116:1521/xe") 
    print("SUCCESS", con)

    P_NAME = input("삭제 이름 : ")
    sql = "DELETE FROM PRODUCT "
    sql += f"WHERE P_NAME LIKE '%{P_NAME}%'" # 특정 단어 포함된 요소 삭제
    
    cur = con.cursor()
    cur.execute(sql)
    if cur.rowcount:
        print("삭제 성공")
        con.commit()

except Exception as e:
    print("에러메세지:", e)
finally:
    cur.close()
    con.close()






