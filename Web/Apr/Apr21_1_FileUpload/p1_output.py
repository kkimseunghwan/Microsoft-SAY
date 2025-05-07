

# from fileinput import filename
from typing import Optional
from uuid import uuid4
from exceptiongroup import catch
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

# http://195.168.9.139:1234
app = FastAPI()


# =>> 실행 명령어 uvicorn p1_output:app --host=0.0.0.0 --port=1234 --reload

# 전기 신호로 온거, 알아서 원상복귀 (디코딩) 시켜서

# 파일업로드

# 1) 인코딩 방식이 바뀌어서 오니
#   => pip install pthon-multipart
# 2) 파일 저장될 폴더 확보 (서버)
#    => 당장 서버를 쓸 수 없는 상황
#   프로젝트 자체를 서버에 업로드 할거고
#   프로젝트에다가 폴더 만들어놓자 + 상대경로 


# 동기식
#   요청을 보내놓고 서버측의 응답이 올 때까지의 시간.
#   동안 멈추는거 (응답없음)

# 비동기식 <- FastAPI
#   요청 보내놓고 서버측의 응답이 올 때까지의 시간동안 안멈추고 멀쩡히 사용 가능



# 비동기식으로 놔두면 파일이 다 불러지지도 않았는데, 다음소스 실행
#   => 동기식으로 바꿔야.. async
@app.post("/file.up")
async def create_file(photo:UploadFile, title:str=Form()):
    folder = "./imageee/"
    content = await photo.read() # 파일 내용 다 불러오면, 그 때 read
    fileN = photo.filename # 사용자가 업로드한 파일명 : OOO.png
    type = fileN[-4:] # .png
    fileN = fileN.replace(type, "")
    fileN = fileN + str(uuid4()) + type # 
    print("시바", fileN)

    # uuid : 네트워크상에서 뭐 구별할 때 쓰는거거
    #   uuid4 : 랜덤하게 uuid값 만드는거

    f = open(folder + fileN, "wb") # b : binary (파일 쓸 때)
    f.write(content)
    f.close()
    
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>제목목 = %s</h1>" % title
    html += "<img src=\"file.get?fname=%s\">" % fileN
    html += "<hr>"
    html += "<a herf=\"file.get?fname=%s\">%s</a>" % (fileN, title)
    html += "</body></html>"

    return HTMLResponse(html)

# => ~~~~~/file.get?fname=새asdasd.png
@app.get("/file.get")
async def fileGet(fname):
    folder = "./imageee/"
    return FileResponse(folder + fname, filename=fname)