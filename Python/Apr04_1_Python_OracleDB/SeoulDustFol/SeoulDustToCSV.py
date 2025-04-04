

'''

    # 권역별 미세 + 초미세의 평균
    # 수치가 높은 순서대로 정렬
    sql = f"SELECT SD_MSRRGN_NM, AVG(SD_PM10 + SD_PM25) FROM SeoulDustLive GROUP BY SD_MSRRGN_NM ORDER BY AVG(SD_PM10 + SD_PM25) DESC"
    cur.execute(sql)

    for rrgn, pm in cur:
        print(rrgn,"\t" ,pm)
'''

from datetime import datetime
from oracledb import connect, init_oracle_client

# 평균가 조회
try:
    init_oracle_client(lib_dir = "C:\Hwan\Oracle DB\instantclient_23_7")
    con = connect("Hwan/1234@195.168.9.116:1521/xe")
    cur = con.cursor() # DB작업 매니저 겸 결과

    sql = f"SELECT * FROM SeoulDustLive"
    cur.execute(sql) # 결과가 cur
    
    f = open("C:\\Hwan\\TestData\\seoulDust.csv", "a", encoding='utf-8')
    for date, msrrgn_nm, msrstr_nm, pm10, pm25, index_nm in cur:
        date = datetime.strftime(date, "%Y,%m,%d,%H")
        f.write("%s,%s,%s,%d,%d,%s\n" % (date, msrrgn_nm, msrstr_nm, pm10, pm25, index_nm))


except Exception as e:
    print("에러에러", e)
finally:
    f.close()
    cur.close()
    con.close()

