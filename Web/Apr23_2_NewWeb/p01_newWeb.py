

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from requests import get
import uvicorn

# 실행 명령어(코드 폴더 위치에서.) : uvicorn (파일명):app --host=0.0.0.0 --port=5678 --reload
app = FastAPI()
# =>> 실행 명령어 uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload

# HTML + CSS + JS : 웹사이트를 제작 가능
# JS 쓰면 프로그램스러운 기능을 넣을 수는 있는데
# JS가 작업이 불편함 -> 그래서 JS를 기피'했었'음

# 클래식 웹:
#   back-end(Fast-API) : 7
#       프로그램스러운 작업 다 해서
#       HTML + CSS + JS 완성시켜서 응답

#   front-end(JavaScript): 3
#       완성된 웹사이트에 이벤트 같은 효과 부여

# 신형 웹:
#   front-end(JavaScript)
#       프로그램스러운 작업은 다 하자
#       DB 관련 작업은 back-end 쪽 통해서 
#       (= AJAX (XML, JSON 파싱))
#   back-end(Fast-API)
#       DB관련 작업만 진행. 결과를 front-end 쪽에서 쓸 수 있게 (XML, JSON으로 응답)
#   -> 서버에 부담 감소


# http://195.168.9.139:1234/te.st/ <= 접속 가능
@app.get("/xml.test")
def xmlTest():
    xmll = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    xmll += "<snacks>"
    xmll += "<s_name>뺴뺴로</s_name>"
    xmll += "<s_price>1500</s_price>"
    xmll += "</snacks>"
    xmll += "<snacks>"
    xmll += "<s_name>새우깡</s_name>"
    xmll += "<s_price>2000</s_price>"
    xmll += "</snacks>"


    return Response(xmll, media_type="apllication/xml")


@app.get("/json.test")
def jsonTest():
    jsonn = [
        {"s_name":"빼빼로", "s_price":1500},
        {"s_name":"새우깡", "s_price":2000}
    ]

    # 결과를 외부에서도 사용 가능하게 하려면?
    # Access-Control-Allow-Origin 이라는 헤더를 세팅하면 사용 가능함
    ㅗ = {"Access-Control-Allow-Origin" : "1.2.3.4"}
    return JSONResponse(jsonn)
