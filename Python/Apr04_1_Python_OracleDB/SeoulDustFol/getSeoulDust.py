
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

# 서울 미세먼지 정보를 받아와서 DB에 저장하기...

# 파일로 저장? - 굳이?
# 바로 DB에다가 저장.
# 테이블은 미리 만들자.

from oracledb import connect, init_oracle_client
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
hc.close()

init_oracle_client(lib_dir = "C:\Hwan\Oracle DB\instantclient_23_7")
con = connect("Hwan/1234@195.168.9.116:1521/xe")
cur = con.cursor() # DB작업 매니저 겸 "결과" -> FOR 문 안에 넣야댐

for i in fromstring(resBody).iter("row"):
    SD_DATE = i.find("MSRDT").text
    SD_MSRRGN_NM = i.find("MSRRGN_NM").text
    SD_MSRSTE_NM = i.find("MSRSTE_NM").text
    SD_PM10 = i.find("PM10").text
    SD_PM25 = i.find("PM25").text
    SD_IDEX_NM = i.find("IDEX_NM").text

    sql = f"INSERT INTO SeoulDustLive VALUES("
    sql += f"to_date('{SD_DATE}', 'YYYYMMDDHH24MI'), "
    sql += f"'{SD_MSRRGN_NM}', "
    sql += f"'{SD_MSRSTE_NM}', "
    sql += f"{SD_PM10}, "
    sql += f"{SD_PM25}, "
    sql += f"'{SD_IDEX_NM}')"
    cur.execute(sql)
    print("INSERT")


con.commit()



cur.close()
con.close()





