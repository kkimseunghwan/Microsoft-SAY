


from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from hwan.StringCleaner import StringCleaner # 라이브러리
from pymongo import MongoClient

###############

q = quote('취업') # (인코딩)

#request header
h = {"X-Naver-Client-ID":"sJ78Ve7Q9XT62bDLXBii",
     "X-Naver-Client-Secret":"wu2TMBQ_BV"}

# API 연결
hc = HTTPSConnection("openapi.naver.com") # 컴퓨터 주소랑, 있다면 포트까지 (주소:포트)형식
hc.request("GET", "/v1/search/news.xml?query="+q, headers=h) # 남은 주소 다 # /폴더/파일?변수명=값?변수명...
resBody = hc.getresponse().read()
hc.close()

# txt 파일
f = open("C:\\Hwan\\TestData\\seoulNews.txt", "a", encoding='utf-8')

# DB 연결
con = MongoClient("195.168.9.139") # 서버주소
db = con.Hwan # DB연결. => con.DB명

# 데이터 처리
for item in fromstring(resBody).iter("item"):
    news = {
        "title": StringCleaner.CleanTXT(item.find("title").text),
        "desc" : StringCleaner.CleanTXT(item.find("description").text)
    }
    print(news)
    print("-----")  
    # txt 저장
    f.write(news["title"] + "\t")
    f.write(news["desc"] + "\n")
    # DB저장 : 명령어 서버로 전송 + 원격실행 + 결과받기
    db.NaverNews.insert_one(news)

f.close()
con.close()


