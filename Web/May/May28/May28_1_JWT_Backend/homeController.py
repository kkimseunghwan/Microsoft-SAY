from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from menu import menuManager
# 데이터를 Back-end에 저장 => 공용 데이터

# 그러면 사용자마다 개별 데이터가 필요할 텐데
#   =>> Session : 데이터를 서버와 사용자의 연결에 저장하는 것.
#                    연결을 끊으면 데이터가 삭제됨
#                    session 유지시간 동안 아무것도 안하고 가만히 있으면 연결이 끊킴
#   =>> cookie : 사용자의 PC에 파일로 저장하는 것.
#                    연결을 끊든 말든, 재부팅을 하든 말든 데이터가 남음 -> 보안상 위험.
#
# cookie: 보안상 위험
# Session: 서버가 바뀌면 관리하기 어려움
# 
# JWT (Json Web Token)
#   JSON + 암호화 + 시간제한

app = FastAPI()
menuM = menuManager()

# uvicorn homeController:app --host=0.0.0.0 --port=1125 --reload
@app.post("/data.post")
def test(name: str=Form(), price: int= Form()):
    return menuM.reg(name, price)