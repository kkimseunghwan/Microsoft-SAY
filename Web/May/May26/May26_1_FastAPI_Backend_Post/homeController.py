from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from calculator.calculator import Calculator
from photo.photoManager import PhotoManager

app = FastAPI()
pm = PhotoManager()

@app.post("/calculate")
def calculate(x: int = Form(), y: int = Form()):
    # 클라이언트 주소와 동일한 주소만 허용
    h = {
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Credentials": "true"
        }
    return JSONResponse(Calculator.calculate(x, y), headers=h)


@app.post("/photo.upload")
async def photoUpload(photo: UploadFile, title: str = Form()):
    r = await PhotoManager.upload(photo, title)

    h = {
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Credentials": "true"
        }
    return JSONResponse(r, headers=h)


@app.get("/photo.get")
def photoGet(photo):
    return pm.getFile(photo)

