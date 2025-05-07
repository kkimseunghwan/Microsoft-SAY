
#Selenium
#   = Python HTML 파싱 하이브러리
#   = 웹 브라우저 매크로 라이브러리
#   -> 사용하고자 하는 웹브라우저에 맞는 드라이버를 따로 설치했'었'어야함
#       (지금은 알아서 됨)


from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news.naver.com/")

news = driver.find_elements(By.CSS_SELECTOR, ".cnf_news")
for n in news:
    print(n.text)