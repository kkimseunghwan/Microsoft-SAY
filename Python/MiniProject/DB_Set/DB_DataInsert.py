
# 원티드 사이트 크롤링
# 자격요건이랑 우대사항 분석하고 통계

# https://www.wanted.co.kr/company/26218?category_id=518&duty_ids=all
# https://www.wanted.co.kr/company/{기업의 고유 식별 번호}?category_id={말 그대로 회사 카테고리}&duty_ids=all (<- 얜 뭐지?)

# 카테고리
# 518 - 개발
#   /872 - 서버 개발자
# 이런 형식

# 채용 공고 페이지
# https://www.wanted.co.kr/wd/177802
# https://www.wanted.co.kr/wd/{공고 페이지 식별 번호}





# 네이버 검색 API 예제 - 블로그 검색

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
from json import loads
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from oracledb import connect, init_oracle_client

###############

q = '방검조끼'
q = quote(q) # (URL인코딩)

#request header
h = {"X-Naver-Client-ID":"sJ78Ve7Q9XT62bDLXBii",
     "X-Naver-Client-Secret":"wu2TMBQ_BV"}

hc = HTTPSConnection("openapi.naver.com") # 컴퓨터 주소랑, 있다면 포트까지 (주소:포트)형식

init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")

# DB 서버 연결 : connect
con = connect("seong/137@195.168.9.116:1521/xe") 
print("SUCCESS", con)


try:
    for start in range(500, 1001, 100):
     hc.request("GET", f"/v1/search/shop.json?query={q}&display=100&start={start}", headers=h) # 남은 주소 다 # /폴더/파일?변수명=값?변수명...
     resBody = hc.getresponse().read().decode()

     # JSON 파싱
     data = loads(resBody)
     i = 0
     for item in data.get('items', []):
          clean_title = item['title'].replace('<b>', '').replace('</b>', '')
          sql = f"INSERT INTO SPV VALUES({int(item['productId'])}, '{clean_title}', {int(item['lprice'])}, '{item['maker']}', '{item['link']}', {start + i})"
          cur = con.cursor()
          cur.execute(sql)
          con.commit()
          
          sql = f"INSERT INTO COMPANY VALUES({start + i}, {int(item['productId'])}, '{item['mallName']}')"
          cur = con.cursor()
          cur.execute(sql)
          con.commit()
          i += 1
except Exception as e:
   print(e)
finally:
     hc.close()
     cur.close()
     con.close()
