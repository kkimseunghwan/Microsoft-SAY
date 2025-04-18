

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

# http://195.168.9.139:1234
app = FastAPI()

@app.post("/member.create.account")
def create_account(id:str=Form(), pw:str=Form()): #id:str=Form(), password:str=Form()
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>ID = %s</h1>" % id
    html += "<h1>PW = %s</h1>" % pw
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