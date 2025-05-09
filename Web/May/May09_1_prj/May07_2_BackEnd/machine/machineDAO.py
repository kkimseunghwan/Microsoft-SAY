from datetime import datetime
from math import ceil
from kwon.kwonDBManager import KwonDBManager


class MachineDAO:
    def __init__(self):
        self.machinePerPage = 10
        self.setAllMachineCount()

    def setAllMachineCount(self):
        try:
            con, cur = KwonDBManager.makeConCur("Hwan/1234@195.168.9.116:1521/XE")

            sql = "select count(*) from may07_deepracer_machine "

            cur.execute(sql)
            for c in cur:
                self.allMachineCount = c[0]
        except:
            pass
        finally:
            KwonDBManager.closeConCur(con, cur)

    def get(self):
        try:
            machineCount = self.allMachineCount
            pageCount = ceil(machineCount / self.machinePerPage)

            con, cur = KwonDBManager.makeConCur("Hwan/1234@195.168.9.116:1521/XE")

            sql = "select * from may07_deepracer_machine "
            sql += "order by dm_check_date desc"

            cur.execute(sql)
            machines = []
            for no, color, status, checkDate in cur:
                m = {
                    "no": no,
                    "color": color,
                    "status": status,
                    "checkDate": datetime.strftime(checkDate, "%Y/%m/%d %H:%M"),
                }
                machines.append(m)
            result = {
                "pageCount" : pageCount,
                "machines" : machines
            }
            return result
        except:
            return {"result": "조회 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)

    def reg(self, color, status):
        try:
            con, cur = KwonDBManager.makeConCur("Hwan/1234@195.168.9.116:1521/XE")

            sql = "insert into may07_deepracer_machine values( "
            sql += "may07_deepracer_machine_seq.nextval, "
            sql += "'%s', '%s', sysdate) " % (color, status)

            cur.execute(sql)
            if cur.rowcount == 1:
                self.allMachineCount += 1
                con.commit()
                return {"result": color + "색 머신 등록 완료"}
            return {"result": "등록 실패"}
        except:
            return {"result": "등록 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)
