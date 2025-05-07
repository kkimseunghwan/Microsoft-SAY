from http.client import HTTPSConnection

from bs4 import BeautifulSoup


con = HTTPSConnection("news.daum.net")
con.request("GET", "/")
rb = con.getresponse().read()
con.close()

cafeData = BeautifulSoup(rb, "html.parser", from_encoding="utf-8")
snsTxts = cafeData.select("desc_txt")
for s in snsTxts:
    print(s)

newsData = BeautifulSoup(rb, "html.parser", from_encoding="utf-8")
for n in newsData.select(".list_newsheadline2 .tit_txt"):
    print(n)