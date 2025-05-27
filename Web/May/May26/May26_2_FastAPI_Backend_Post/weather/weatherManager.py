from datetime import datetime
from fastapi.responses import JSONResponse, FileResponse

class WeatherManager:
    def __init__(self):
        self.imagefolder = "./weather/image/"

    def fileNameSet(self, fileName):
        now = datetime.today()
        now = datetime.strftime(now, "%Y%m%d%H%M%S")

        file_type = fileName[-4:]
        fileName = fileName.replace(file_type, "")
        return fileName + "_" + now + file_type
    
    def getIcon(self, icon):
        return FileResponse(self.imagefolder + "/" + icon, filename=icon)

    async def weatherReg(self, icon, desc, temp):
        content = await icon.read()

        fileName = self.fileNameSet(icon.filename)
        f = open(self.imagefolder + "/" + fileName, "wb")
        f.write(content)
        f.close()

        r = {
            "result":"SUCCESS", 
            "desc":desc, 
            "temp":temp,
            "icon": fileName
            }
        # 클라이언트 주소와 동일한 주소만 허용
        h = {
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Credentials": "true"
            }
        

        return JSONResponse(r, headers=h)
    













