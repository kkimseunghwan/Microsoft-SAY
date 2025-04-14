
# 정부사이트
#   data.go.kr
#   data.seoul.go.kr
#   data.gg.go.kr
#   ...
# 포털 사이트가 개발자 센터
# SNS 개발자 센터
# ...


# 네이버 뉴스
# https://developers.naver.com/main/ 로그인

# 네이버 입장에서는 뉴스 데이터를 제3자에게 공개 : 위험
# 로그인해서 신청
#   사용 API : 검색
#   비로그인.. : WEB설정 => 웹사이트 주소 아무거나 하나
#   ClientID : sJ78Ve7Q9XT62bDLXBii
#   ClientSecret : wu2TMBQ_BV

# Documents - 서비스API - 검색 - 뉴스

# https://openapi.naver.com/v1/search/news.xml

# 인터넷 주소 체계
# 프로토콜://서버주소[:포트번호(생략가능)]/폴더/폴더/.../파일?..
# ?param변수명=param값&?param변수명=param값&..

# 인터넷 주서 체계에는 한글을 넣을 수 었음
# ㅋ -> %2D (URL인코딩) 진행 필요

# 서버주소 - 192.1.2.3 일수도 있고, 도메인으로 되어있을 수 있음

# request parameter 
#   클라이언트가 서버에게 전달해주는 정보.

# request Header
#   내부적으로 전달하는 것것


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


# <b> 같은거 없애자 -> 이번만x
# => <b> 같은거 없애주는 library를 만들자

# library vs Framework
#   library :
#   자주 사용되는 기능 따로 정리해놓고
#   필요할 때마다 가져다 쓸 수 있게 하는 것


