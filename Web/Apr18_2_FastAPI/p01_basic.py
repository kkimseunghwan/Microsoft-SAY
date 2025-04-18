# flask : 자체 WAS기능 포함 -> 단독 실행 가능
#           전달값 딱히 가리지는 않음
# fastAPI : 따로 WAS가 필요함, 
#           전달 값 기본적으로 JSON으로 응답함.

# flask =둘이 비슷비슷함= fastAPI 

# 시작 - CMD
#   pip install fastapi
#   pip install uvicorn[standard] #->따로 WAS가 필요함


from fastapi import FastAPI
from requests import get
import uvicorn

# 실행 명령어(코드 폴더 위치에서.) : uvicorn (파일명):app --host=0.0.0.0 --port=5678 --reload
app = FastAPI()

# 이렇게 하면 돌아가긴 하는데, 말을 잘 안들어처머금
# if __name__ == "__main__":
#     uvicorn.run 
# =>> 실행 명령어 uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload


# 클래식 스타일
#       back-end에서 HTML/CSS를 완성시켜서 응답 => 앞에 Flask 예제에서 했던 방식.

# 신형 스타일
#       back-end에서 '데이터'만 전달 + HTML/CSS는 따로 존재 (<< 이게 React 스타일)
#                     (JSON)

# http://195.168.9.139:1234/te.st/ <= 접속 가능?
@app.get("/te.st")
def test():
    print("SUCCESS")
    d = {
        "name":"마이쮸", 
        "price": 500,
    }
    return d
