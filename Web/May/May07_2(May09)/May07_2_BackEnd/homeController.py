from fastapi import FastAPI
from fastapi.responses import JSONResponse

from machine.machineDAO import MachineDAO

app = FastAPI()
mDAO = MachineDAO()


@app.get("/machine.get")
def machineGet(page, search):
    result = mDAO.get(page, search)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/machine.get.detail")
def machineGetDetail(no):
    result = mDAO.getDetail(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/machine.reg")
def machineReg(color, status):
    result = mDAO.reg(color, status)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)
