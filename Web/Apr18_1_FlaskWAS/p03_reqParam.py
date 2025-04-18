from flask import Flask, request

app = Flask(__name__)

# 인터넷 주소 체계
#   프로토콜://IP주소:포트/지정한주소?변수명=값&변수명=값...

# request parameter : 클라이언트가 WAS로 보내는 정보

# 요청
#   GET방식 
#       주소를 직접 입력, <a>
#       요청param이 주소에 실려서 전달
#   POST방식
#       form을 통해서만 가능
#       요청param이 내부적으로 전달 -> 보안성 높음

# http://IP주소:1234/calculate.do?xxx=10&yyy=5
@app.get("/calculate.do")
def calculate_do():
    x = int(request.args.get("xxx")) # request.args.get("reqParam변수명") -> str
    y = int(request.args.get("yyy"))
    html = '<html><head><meta charset="utf-8"></head><body>'
    html += '<table border="1">'
    html += "<tr><td>%d + %d = %d</td></tr>" % (x, y, x + y)
    html += "<tr><td>%d - %d = %d</td></tr>" % (x, y, x - y)
    html += "<tr><td>%d x %d = %d</td></tr>" % (x, y, x * y)
    html += "<tr><td>%d / %d = %d</td></tr>" % (x, y, x / y)
    html += "</table>"
    html += "</body></html>"
    return html

# http://IP주소:1234/gugudan.show
# start, end는 내부적으로 전달되어옴
@app.post("/gugudan.show")
def gugudan_show():
    s = int(request.form["start"])
    e = int(request.form["end"])
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    for dan in range(s, e+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%d단</th></tr>" % dan
        for i in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (dan, i, dan*i)
        html += "</table>"
    html += "</body></html>"
    return html



if __name__ == "__main__":
    app.run("0.0.0.0", 1234, debug=True)
