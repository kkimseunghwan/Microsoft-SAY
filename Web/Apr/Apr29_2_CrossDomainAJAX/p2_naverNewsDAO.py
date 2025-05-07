

from http.client import HTTPSConnection
from urllib.parse import quote


# class NaverDAO:
#     def getNews(self, selfTxt):
#         q = quote(selfTxt) # (URL인코딩)

#         #request header
#         h = {"X-Naver-Client-ID":"sJ78Ve7Q9XT62bDLXBii",
#             "X-Naver-Client-Secret":"wu2TMBQ_BV"}

#         hc = HTTPSConnection("openapi.naver.com") # 컴퓨터 주소랑, 있다면 포트까지 (주소:포트)형식
#         hc.request("GET", "/v1/search/news.xml?query="+q, headers=h) # 남은 주소 다 # /폴더/파일?변수명=값?변수명...
#         resBody = hc.getresponse().read()
#         hc.close()

#         #print(resBody.decode())
#         return resBody

from http.client import HTTPSConnection
from urllib.parse import quote

class NaverNewsDAO:
    def getNews(self, searchTxt):
        
        q = "산불"
        q = quote(searchTxt)
        h = {"X-Naver-Client-Id": "sJ78Ve7Q9XT62bDLXBii", 
             "X-Naver-Client-Secret": "wu2TMBQ_BV"}
        hc = HTTPSConnection("openapi.naver.com")
        hc.request("GET", "/v1/search/news.xml?query=" + q, headers=h) # com 뒤로 남은거 다써 => /폴더/파일?변수명=값&...
        rb = hc.getresponse().read()
        # print(resBody.decode())
        hc.close()
        return rb