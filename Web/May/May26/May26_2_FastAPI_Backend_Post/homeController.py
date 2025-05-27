from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from weather.weatherManager import WeatherManager

app = FastAPI()
wm = WeatherManager()

# icon:UploadFile => param 순서 상 "파일"이 첫 번째 순서로 있어야 함. 
@app.post("/weather.reg")
async def weatherReg(icon:UploadFile, desc:str=Form(), temp:float=Form()):    
    return await wm.weatherReg(icon, desc, temp)



@app.get("/weather.icon.get")
def weatherIconGet(icon):
    return wm.getIcon(icon)
    