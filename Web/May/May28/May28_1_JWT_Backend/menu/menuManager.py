
from datetime import datetime, timedelta
from time import timezone
from fastapi.responses import JSONResponse
import jwt

# JWT (Json Web Token)
#   JSON + 암호화 + 시간제한

# pip install pyjwt

# 현재시간날짜 : datetime.today()
# 현재시간날짜 : datetime.now()
# 현재시간날짜(표준 시간대): datetime.now(timezone.utc)
# 현재시간날짜(표준 시간대) 로 부터 10초 지나서:
#                            datetime.now(timezone.utc) + timedelta(seconds=10)


class MenuManager:
    def __init__(self):
        self.key = "KeyDesu"
        self.jwtAlogrithm = "HS256"

    # 토큰 읽기
    def get(self, token):
        h = { "Access-Control-Allow-Origin": "*" }
        try:
            r = jwt.decode(token, self.key, self.jwtAlogrithm)
            r = { 
                "result":"Last Token", 
                "name":r["name"], 
                "price":r["price"], 
            }
        except:
            pass
        return JSONResponse(r, headers=h)
    
    def rag(self, name, price):
        # exp는 만료 시간
        r = { 
            "result":"SUCCESS", 
            "name":name, 
            "price":price, 
            "exp": datetime.now(timezone.utc) + timedelta(seconds=10)  
        }
        h = { "Access-Control-Allow-Origin": "*" }
        jwtr = jwt.encode(r, self.key, self.jwtAlogrithm)
        return JSONResponse(
            {"menuJWT":jwtr}, 
            headers=h
        ) # JWON 형태로 전달