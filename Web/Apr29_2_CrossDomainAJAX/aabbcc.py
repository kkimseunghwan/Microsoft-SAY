# 산불로 검색했을 때
# 네이버 뉴스 XML 나오는거
# 콘솔에 출력

# 파싱까지는 x


from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from hwann.StringCleaner import StringCleaner # 라이브러리

###############

q = '산불'
q = quote(q) # (URL인코딩)
print(q)

#request header
h = {"X-Naver-Client-ID":"",
     "X-Naver-Client-Secret":""}

hc = HTTPSConnection("openapi.naver.com") # 컴퓨터 주소랑, 있다면 포트까지 (주소:포트)형식
hc.request("GET", "/v1/search/news.xml?query="+q, headers=h) # 남은 주소 다 # /폴더/파일?변수명=값?변수명...
resBody = hc.getresponse().read()
#print(resBody.decode())
hc.close()

for item in fromstring(resBody).iter("item"):
    print(StringCleaner.DeleteBold(item.find("title").text))
    print(StringCleaner.DeleteBold(item.find("description").text))
    print("-----")

