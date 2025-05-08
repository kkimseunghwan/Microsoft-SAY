#   uvicorn homeController:app --host=0.0.0.0 --port=8888 --reload
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from oracledb import connect, init_oracle_client
import datetime

app = FastAPI()

# 실행 명령어(코드 폴더 위치에서.) : uvicorn (파일명):app --host=0.0.0.0 --port=5678 --reload
@app.get("/machine.reg")
def machineReg(color, status):
    r = {"color": color, "status": status}
    s = {"결과" : "실패"}
    h = {"Access-Control-Allow-Origin": "*"}

    con = connect("Hwan/1234@195.168.9.116:1521/XE")

    sql = "insert into may07_deepracer_machine values(may07_deepracer_machine_seq.NEXTVAL, '%s', '%s', SYSDATE)" % (r["color"], r["status"])
    
    cur = con.cursor()

    cur.execute(sql)

    if cur.rowcount == 1:
        con.commit()
        s["결과"] = "성공"
    
    cur.close()
    con.close()
    return JSONResponse(s, headers=h)



@app.get("/machine.sel")
def machineSel():
    h = {"Access-Control-Allow-Origin": "*"}

    con = connect("Hwan/1234@195.168.9.116:1521/XE")

    sql = "select * from may07_deepracer_machine"
        
    cur = con.cursor() 
    cur.execute(sql)

    result = []

    for no, color, status, date in cur:
        result.append( {
            "no":no,
            "color": color, 
            "status": status,
            "check_date":date.strftime("%Y-%m-%d %H:%M:%S")
        })
        
    cur.close()
    con.close()

    print(result)
    return JSONResponse(content=result, headers=h)



@app.get("/machine.del")
def machineDel(number):
    h = {"Access-Control-Allow-Origin": "*"}
    s = {"결과" : "실패"}
    con = connect("Hwan/1234@195.168.9.116:1521/XE")

    sql = "DELETE FROM may07_deepracer_machine "
    sql += f"WHERE DM_NO = {number}" # 특정 단어 포함된 요소 삭제
        
    cur = con.cursor()
    cur.execute(sql)
    if cur.rowcount:
        print("삭제 성공")
        s["결과"] = "성공"
        con.commit()
        
    cur.close()
    con.close()
    
    return JSONResponse(s, headers=h)



@app.get("/machine.upd")
def machineUpd(number, color, status):
    h = {"Access-Control-Allow-Origin": "*"}
    s = {"결과" : "실패"}
    con = connect("Hwan/1234@195.168.9.116:1521/XE")

    sql = f"UPDATE may07_deepracer_machine SET DM_COLOR = '{color}', DM_STATUS='{status}', DM_CHECK_DATE = SYSDATE WHERE DM_NO = {number};"
        
    cur = con.cursor()
    cur.execute(sql)
    if cur.rowcount:
        print("업데이트 성공")
        s["결과"] = "성공"
        con.commit()
        
    cur.close()
    con.close()
    
    return JSONResponse(s, headers=h)