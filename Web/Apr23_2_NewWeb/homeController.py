
from product.productDAO import ProductDAO
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from requests import get
import uvicorn

# 실행 명령어(코드 폴더 위치에서.) : 
# # =>> uvicorn p01_basic:app --host=0.0.0.0 --port=5678 --reload

app = FastAPI()
pDAO = ProductDAO()


# RESTful
# DB에 직접 접속x
# back-end
# front-end
# 그 결과를 XML/JSON으로 


# http://195.168.9.139:1234/te.st/ <= 접속 가능
@app.get("/product.get")
def snackGet():
    resBody = pDAO.getAll()
    # 결과를 외부에서도 사용 가능하게 하려면?
    # Access-Control-Allow-Origin 이라는 헤더를 세팅하면 사용 가능함
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/product.reg")
def productReg(p_name:str, p_price:int):
    resBody = pDAO.reg(p_name, p_price)
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/product.delete")
def productDel(price_min:int, price_max:int):
    resBody = pDAO.delete(price_min, price_max)
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)
