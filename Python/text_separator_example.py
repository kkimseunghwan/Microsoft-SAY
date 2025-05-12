from bs4 import BeautifulSoup

# 예시 HTML
html = """
<dd>
    <span>경기</span>
    <span>용인시</span>
    <span>수지구</span>
    <span>신수로 767</span>
    <span>분당수지유타워 A동 1411호</span>
</dd>
"""

soup = BeautifulSoup(html, 'html.parser')
dd = soup.find('dd')

# separator 없이 텍스트 추출
print("separator 없이 추출:")
print(dd.get_text())
print("\nseparator=' '로 추출:")
print(dd.get_text(separator=" "))
print("\nseparator='\\n'로 추출:")
print(dd.get_text(separator="\n"))
print("\nseparator='|'로 추출:")
print(dd.get_text(separator="|")) 