# 빅데이터 분석용 데이터
# AI 학습용 데이터
# 어디서 구하나
#   1) 발로 뛰어서
#   2) 웹 데이터
#       XML
#       JSON
#       근데 못구하면? -> 웹사이트에서 긁어오기
#   3번)

# Web Crawlinfing(Scraping)
#   좁은의미 : HTML파싱
#   넓은 이미 : 어쩃든 웹에서 가져오면/

# 근데
#   XML : 데이터를 HTML DOM객체 모양으로 표현해놓은거
#   JSON : 데이터를 JavaScript객체 모양으로 표현해놓은거
#   HTML : 웹사이트 만들때 쓰는 디자인 언어
#       -> 파싱 난이도가 극악임
#       -> 거기서 데이터를 긁어가? 법적문제

# https://sd-beanmouse.duckdns.org
#
# HTTP 통신 걸어서 응답내용 콘솔에

# beautifulsoup
#   pip install bs4
from http.client import HTTPSConnection

from bs4 import BeautifulSoup


con = HTTPSConnection("sd-beanmouse.duckdns.org")
con.request("GET", "/")
rb = con.getresponse().read()
con.close()

# 받아온거, 내장html파서이름, 그 사이트 뭘로 인코딩
cafeData = BeautifulSoup(rb, "html.parser", from_encoding="utf-8")
snsTxts = cafeData.select(".txtTd") # css선택자
for s in snsTxts:
    print(s.text)
