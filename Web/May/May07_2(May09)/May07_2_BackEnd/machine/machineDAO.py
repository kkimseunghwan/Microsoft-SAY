from datetime import datetime
from math import ceil
from kwon.kwonDBManager import KwonDBManager


class MachineDAO:
    def __init__(self):
        self.machinePerPage = 10
        self.setAllMachineCount()

    def setAllMachineCount(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

            sql = "select count(*) from may07_deepracer_machine "

            cur.execute(sql)
            for c in cur:
                self.allMachineCount = c[0]
        except:
            pass
        finally:
            KwonDBManager.closeConCur(con, cur)

    def get(self, page, search):
        try:
            machineCount = self.allMachineCount
            if search != "":
                machineCount = self.getSearchMachineCount(search)
            search = "%" + search + "%"
            pageCount = ceil(machineCount / self.machinePerPage)

            page = int(page)
            start = (page - 1) * self.machinePerPage + 1
            end = page * self.machinePerPage

            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, dm_no, dm_color, dm_status, dm_check_date "
            sql += "    FROM ( "
            sql += "        SELECT * "
            sql += "        FROM may07_deepracer_machine "
            sql += "        where dm_color like '%s' " % search
            sql += "        ORDER BY DM_CHECK_DATE desc "
            sql += "    )"
            sql += ") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)

            cur.execute(sql)
            machines = []
            for _, no, color, status, checkDate in cur:
                m = {
                    "no": no,
                    "color": color,
                    "status": status,
                    "checkDate": datetime.strftime(checkDate, "%Y/%m/%d %H:%M"),
                }
                machines.append(m)
            result = {"pageCount": pageCount, "machines": machines}
            return result
        except:
            return {"result": "조회 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getDetail(self, no):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

            sql = "SELECT * "
            sql += "FROM may07_deepracer_machine "
            sql += "where dm_no = %s" % no

            cur.execute(sql)
            for no, color, status, checkDate in cur:
                m = {
                    "no": no,
                    "color": color,
                    "status": status,
                    "checkDate": datetime.strftime(checkDate, "%Y/%m/%d %H:%M"),
                }
            return m
        except:
            return {"result": "조회 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getSearchMachineCount(self, searchTxt):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

            searchTxt = "%" + searchTxt + "%"

            sql = "SELECT count(*) "
            sql += "FROM may07_deepracer_machine "
            sql += "where dm_color like '%s'" % searchTxt

            cur.execute(sql)
            for r in cur:
                return r[0]
            return -1
        except:
            return -1
        finally:
            KwonDBManager.closeConCur(con, cur)

    def reg(self, color, status):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

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
