
from snack.snackDAO import SnackDAO
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from requests import get
import uvicorn

# 실행 명령어(코드 폴더 위치에서.) : 
# # =>> uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload

app = FastAPI()

sDAO = SnackDAO()


# http://195.168.9.139:1234/te.st/ <= 접속 가능
@app.get("/snack.get")
def snackGet():
    resBody = sDAO.getAll()
    return resBody