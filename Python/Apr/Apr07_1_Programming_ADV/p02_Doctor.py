from oracledb import connect, init_oracle_client

from Apr07_1_Programming_ADV.hwan.hwanDBManager import HwanDB

class DoctorC:

    # BMI 계산
    @staticmethod
    def calculBMI(guest):
        guest.height = float(guest.height)
        guest.weight = float(guest.weight)

        guest.BMI = guest.weight/((guest.height/100)**2)
        
    
    @staticmethod
    def GetResult(guest):
        if guest.BMI >= 39: guest.result = "고도 비만"
        elif guest.BMI >= 37: guest.result = "중도 비만"
        elif guest.BMI >= 30: guest.result = "경도 비만"
        elif guest.BMI >= 24: guest.result = "과체중"
        elif guest.BMI >= 10: guest.result = "정상"
        else: guest.result = "저체중"

        DoctorC.DAO(guest)

        

    @staticmethod
    def DAO(guest):
        init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")
        con = connect("Hwan/1234@195.168.9.116:1521/xe")

        sql = f"INSERT INTO APR07_BMI VALUES('{guest.name}', {guest.height}, {guest.weight}, {guest.BMI}, '{guest.result}')"
        print(sql)

        cur = con.cursor()
        cur.execute(sql)
        if cur.rowcount == 1:
            print("등록 완료")
            con.commit()

        HwanDB.closeConCur(con, cur)
