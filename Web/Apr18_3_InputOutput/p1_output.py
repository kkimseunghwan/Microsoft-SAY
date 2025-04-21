

from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

# http://195.168.9.139:1234
app = FastAPI()


# =>> 실행 명령어 uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload
# GET vs POST
#   reqParam 요청 파라미터가
#       GET은 ~~~?변수명=값&변수명=값
#           -> 주소에 실려서
#       POST는 내부적으로 

# checkbox : 변수는 하나인데 값이 여러개
#  -> GET방식으로 표현 불가 -> POST 방식으로 써야..

# Form("a") -> Form 안 넣었을 때 기본값.


@app.post("/member.create.account")
def create_account(
            id:str=Form(), 
            pw:str=Form(), 
            gender:str=Form(), 
            adr:str=Form(), 
            hobby:Optional[list[str]]=Form(None),
            comment:str=Form()
        ): #id:str=Form(), password:str=Form()
    comment = comment.replace("\r\n", "<br>")

    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>ID = %s</h1>" % id
    html += "<h1>PW = %s</h1>" % pw
    html += "<h1>성별 = %s</h1>" % gender
    html += "<h1>주소 = %s</h1>" % adr
    for i in hobby:
        html += "<h1>취미 = %s</h1>" % i 
    html += "<h1>자기소개 = %s</h1>" % comment 

    html += "</body></html>"

    return HTMLResponse(html)

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