from fastapi import FastAPI
from fastapi.responses import JSONResponse

from computer.computerDAO import ComputerDAO

app = FastAPI()
cDAO = ComputerDAO()


@app.get("/computer.get")
def computerGet(page):
    r = cDAO.get(page)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(r, headers=h)


@app.get("/computer.reg")
def computerReg(name, what, ip, condition):
    r = cDAO.reg(name, what, ip, condition)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(r, headers=h)
