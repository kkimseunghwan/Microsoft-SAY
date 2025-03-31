
# JSON 파싱

# 원래 오리지널 : AJAX : (Asynchronous JavaScript And XML)
# JS에서 쓰려고 만들어진게, => XML
# XML : 데이터를 HTML모양으로 표현해 놓은거
# JS에서 쓸건데 굳이 HTML모양이여야 하나?
#   => JS에서 쓸거면 JS모양으로 하는게 편하지 않을까?
#       => XML 후속 >> JSON

# JSON : (JavaScript Object Notation)
# XML후속
#   JS배열 : [ 1, 4, 34, 45] : Python List ??
#   JS객체 : 
#       class 만들고...
#       {멤버변수명:값, 멤버변수명:값} : Python Dict 
#       <- 저 형태로 데이터를 만들어보자 => JSON
# 모든 면에서 XML보다 상위호환
#   -> 용량 측면에서 좋음
#   => 현 시점의 대부분은 JSON이 주력
# 근데 가독성은 XML이 더 나아서
#   - XML은 각종 설정 파일에 쓰임


# [ 실시간 날씨 데이터 받아와서 출력하기. ]
# => openweathermap.org

# API Call
# =>> https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=&units=metric&lang=kr

# 1) HTTP 통신걸어서 받아와서 콘솔 출력

from http.client import HTTPConnection
from json import loads

hc = HTTPConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q=seoul&appid=&units=metric&lang=kr")
resbody = hc.getresponse().read()
# print(resbody.decode())
hc.close()

# Json 파싱
# Json의 import loads
weatherData = loads(resbody) # loads는 기존의 JSON을 -> Python 컬렉션으로 변경해줌.
print(weatherData, type(weatherData)) # => dict

# 날씨
print("날씨", weatherData["weather"][0]["description"])
print("온도", weatherData["main"]["temp"])
print("습도", weatherData["main"]["humidity"])

####################


