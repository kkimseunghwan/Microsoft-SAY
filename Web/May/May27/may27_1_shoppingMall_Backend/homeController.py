from unittest import result
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from product import productDAO

app = FastAPI()
pDAO = productDAO()

@app.post("/product.reg")
def productReg(name:str=Form(), price:int=Form(), desc:str=Form()):

    return pDAO.reg(name, price, desc)
