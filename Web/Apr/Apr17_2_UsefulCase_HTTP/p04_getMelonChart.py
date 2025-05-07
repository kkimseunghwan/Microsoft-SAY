#   XML : 데이터를 HTML DOM객체 모양으로 표현해놓은거
#   JSON : 데이터를 JavaScript객체 모양으로 표현해놓은거
#   HTML : 웹사이트 만들때 쓰는 디자인 언어
#       -> 파싱 난이도가 극악임
#       -> 거기서 데이터를 긁어가? 법적문제

# 멜론 : 데이터는 주고 싶지 않다, 일반 사용자들 차트나 보게 하고 싶었다.
# 우리 : 차트를 볼 수 있다? -> 데이터 주겠다는거 아닌가? ㄹㅇㅋㅋ

# 1) -> 정식으로 웹브라우저 켜서 접속은 가능함,
# 프로그램 만들어서 GET 방식 요청 날리는건 막아놓은 곳이 많음.
# 2) 
#    전통 스타일 웹 - Back-End에서 HTML을 완성시켜서 제공하는..
#    신형 스타일 웹 - Front-End에서 동적으로 HTML을 실시간으로 만들어내는..(React 등)
#               예) 스크롤 시키서 바닥에 닿으면 다음 페이지 나오는 사이트 
#               => 얜 못가져옴
#    => 매크로(웹 브라우저를 키고, 스크롤 하고, 그 웹브라우저의 데이터를 받는다?)
#       => selenium(웹브라우저 매크로)

#Selenium
#   = Python HTML 파싱 하이브러리
#   = 웹 브라우저 매크로 라이브러리
#   -> 사용하고자 하는 웹브라우저에 맞는 드라이버를 따로 설치했'었'어야함
#       (지금은 알아서 됨)

from http.client import HTTPSConnection
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.melon.com/chart/index.htm")

body = driver.find_element(By.CSS_SELECTOR, "body")
for i in range(5):
    print("end")
    body.send_keys(Keys.END)
    sleep(1)

# JavaScript : 웹사이트의 이벤트
# driver.execute_script("JavaScript 문법")


songs = driver.find_elements(By.CSS_SELECTOR, ".rank01 a")
for i, n in enumerate(songs):
    print(i+1, n.text)
