
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

# 서울시 실시간 미세먼지 데이터를 저장하는 프로그럄

#

from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# 1) HTTP 통신 여부 확인
# 2) 파싱
# 3) 파일에에
hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "//xml/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
hc.close()

now = datetime.today()
now = datetime.strftime(now, "%Y,%m,%d,%H")
f = open("C:\\Hwan\\workspace\\TestData.SeoulDust.csv", "a", encoding="utf-8")


for i in fromstring(resBody).iter("row"):
    print(i.find("MSRRGN_NM").text)
