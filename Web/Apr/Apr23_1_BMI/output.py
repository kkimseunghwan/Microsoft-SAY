

# from fileinput import filename
from uuid import uuid4
from exceptiongroup import catch
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

# http://195.168.9.139:8888
app = FastAPI()

# =>> 실행 명령어 uvicorn output:app --host=0.0.0.0 --port=8888 --reload

@app.post("/bmi.sign.up")
async def create_file(
        profile:UploadFile, 
        name:str=Form(), 
        height:int=Form(),
        weight:int=Form()):
    folder = "./image_profile/"

    content = await profile.read() # 파일 내용 다 불러오면, 그 때 read
    fileN = profile.filename # 사용자가 업로드한 파일명 : OOO.png
    type = fileN[-4:] # .png
    fileN = fileN.replace(type, "")
    fileN = fileN + str(uuid4()) + type # 

    f = open(folder + fileN, "wb") # b : binary (파일 쓸 때)
    f.write(content)
    f.close()

    BMI = weight/((height/100)**2) # 값 계산 후, 객체의 속성을 추가 할 수 있음

    if BMI >= 39: result = "고도 비만"
    elif BMI >= 37: result = "중도 비만"
    elif BMI >= 30: result = "경도 비만"
    elif BMI >= 24: result = "과체중"
    elif BMI >= 10: result = "정상"
    else: result = "저체중"
    
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>결과</h1>"
    html += "<img src=\"file.get?fname=%s\">" % fileN
    html += "<h2>이름 : %s</h2>" % name
    html += "<h2>키 : %s</h2>" % height
    html += "<h2>몸무게 : %s</h2>" % weight
    html += "<h2>BMI : %s</h2>" % BMI
    html += "<h2>결과 : %s</h2>" % result
    html += "</body></html>"

    return HTMLResponse(html)

# => ~~~~~/file.get?fname=새asdasd.png
@app.get("/file.get")
async def fileGet(fname):
    folder = "./imageee/"
    return FileResponse(folder + fname, filename=fname)