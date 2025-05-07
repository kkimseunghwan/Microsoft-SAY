
# https://api.openweathermap.org/data/2.5/weather?lat=37.5693582&lon=126.9858652&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr

from datetime import datetime
from json import loads
from oracledb import connect, init_oracle_client
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?lat=37.5693582&lon=126.9858652&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = hc.getresponse().read()
weatherData = loads(resBody)

hc.close()

init_oracle_client(lib_dir = "C:\Hwan\Oracle DB\instantclient_23_7")
con = connect("Hwan/1234@195.168.9.116:1521/xe")
cur = con.cursor() # DB작업 매니저 겸 "결과" -> FOR 문 안에 넣야댐

desc = weatherData["weather"][0]["description"]
temp = weatherData["main"]["temp"]
feels_like = weatherData["main"]["feels_like"]
humi = weatherData["main"]["humidity"]


sql = "INSERT INTO OWM_WEATHER VALUES(SYSDATE, '%s', %.2f, %.2f, %d)" % (desc, temp, feels_like, humi)
cur.execute(sql)

con.commit()
cur.close()
con.close()





