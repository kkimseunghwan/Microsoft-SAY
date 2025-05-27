from email.mime import image
from unittest import result
from wsgiref import headers
from fastapi.responses import JSONResponse
from hwan import hwanDBManager

def generate(fileName, mode):
    type = fileName[-4:]
    return fileName


class ProductDAO:

    def __init__(self):
        self.imageFolder = "./product/image/"
    
    async def reg(self, image, name, price, desc):
        r = { "result":"SUCCESS", "name":name, "price":price, "desc":desc }
        h = {
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Credentials": "true"
            }

        try:
            content = await image.read()
            if len(content) > 30*1024*1024:
                raise


            fileName = image.filename
            fileName = generate(fileName)
            f = open(self.imageFolder + "/" + fileName)
            f.write(content)
            f.close()
        except Exception as e:
            r = { "result":"ERROR : " + e }

        try:
            con, cur = hwanDBManager.connect("Hwan/DB주소")
        except:
            pass

        return JSONResponse(r, headers=h)