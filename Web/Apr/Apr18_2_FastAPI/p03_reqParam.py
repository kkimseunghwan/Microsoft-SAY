from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# 클래식 웹 스타일 : back-end에서 html/css를 완성시켜서 응답
# 신형 웹 스타일 : back-end에서 데이터만(XML, JSON) + html/css 따로 존재(react)

# =>> 실행 명령어 uvicorn p03_reqParam:app --host=0.0.0.0 --port=5678 --reload

# http://IP주소:1234/calculate.do?x=10&y=5
# http://195.168.9.139:5678/calculate.do?x=10&y=2
# GET 방식
@app.get("/calculate.do")
def calculate_do(x:int, y:int):
    
    html = '<html><head><meta charset="utf-8"></head><body>'
    html += '<table border="1">'
    html += "<tr><td>%d + %d = %d</td></tr>" % (x, y, x + y)
    html += "<tr><td>%d - %d = %d</td></tr>" % (x, y, x - y)
    html += "<tr><td>%d x %d = %d</td></tr>" % (x, y, x * y)
    html += "<tr><td>%d / %d = %d</td></tr>" % (x, y, x / y)
    html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html) # HTMLResponse(html) html 실행

# Post 방식
#      pip install python-multipart # 파일 업로드 때 필요
# http://IP주소:1234/gugudan.show
# start, end는 내부적으로 전달되어옴
@app.post("/gugudan.show")
def gugudan_show(start:int=Form(), end:int=Form()):
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    for dan in range(start, end+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%d단</th></tr>" % dan
        for i in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (dan, i, dan*i)
        html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)