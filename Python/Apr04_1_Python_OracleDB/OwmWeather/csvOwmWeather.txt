
# https://api.openweathermap.org/data/2.5/weather?lat=37.5693582&lon=126.9858652&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr

from datetime import datetime
from json import loads
from oracledb import connect, init_oracle_client
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

init_oracle_client(lib_dir = "C:\Hwan\Oracle DB\instantclient_23_7")
con = connect("Hwan/1234@195.168.9.116:1521/xe")
cur = con.cursor() # DB작업 매니저 겸 "결과" -> FOR 문 안에 넣야댐

sql = "SELECT * FROM OWM_WEATHER"
cur.execute(sql)

f = open("C:\\Hwan\\TestData\\owmWeather.csv", "a", encoding='utf-8')
for date, desc, temp, feels_like, humi in cur:
    date = datetime.strftime(date, "%Y,%m,%d,%H")
    f.write("%s,%s,%.2f,%.2f,%d\n" % (date, desc, temp, feels_like, humi))

f.close()
cur.close()
con.close()





