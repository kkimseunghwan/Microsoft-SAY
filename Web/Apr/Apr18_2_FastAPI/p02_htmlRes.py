
from fastapi import FastAPI
from requests import get
import uvicorn

# 실행 명령어(코드 폴더 위치에서.) : uvicorn (파일명):app --host=0.0.0.0 --port=5678 --reload
app = FastAPI()

# http://195.168.9.139:1234/te.st/ <= 접속 가능?
@app.get("/te.st")
def test():
    print("SUCCESS")
