


from flask import Flask

app = Flask(__name__)

@app.get("/html.test") # 클라이언트로부터 GET 방식 요청 받으면
def html_test(): # 이 함수 자동 실행
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<marquee>ㅋㅋㅋ</marquee>"
    html += "</body></html>"
    print("HTML")
    return html

@app.get("/xy.calculate") # 클라이언트로부터 GET 방식 요청 받으면
def xy_calculate(): # 이 함수 자동 실행
    a = 10
    b = 20
    c = a + b
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>%d + %d = %d</h1>" % (a,b,c)
    html += "</body></html>"
    print("HTML")
    return html

# http://조소:1234/gugudan.show
@app.get("/gugudan.show") # 클라이언트로부터 GET 방식 요청 받으면
def gugudan_show(): # 이 함수 자동 실행
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    for j in range(2, 10):
        html += "<table border=\"1\" style=\"float:left\">"
        html += "<tr><th>%d단</td></th>" % j
        for i in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (j, i,j*i)
        html += "</table>"
    html += "</body></html>"
    print("HTML")
    return html

# http://195.168.9.139:1234/html.test/ <= 접속 가능.

if __name__ == "__main__":
    app.run(
        "0.0.0.0", # 접속 허용 주소. 넣은 주소로만 접속하게 하는? 위에 4개 다 되게 = "0.0.0.0"
        1234,      # 포트번호
        debug=True # 정보 출력
    )

