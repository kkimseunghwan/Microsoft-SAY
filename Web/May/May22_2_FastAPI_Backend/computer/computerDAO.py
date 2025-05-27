from math import ceil
from kwon.kwonDBManager import KwonDBManager


class ComputerDAO:
    def __init__(self):
        self.computerPerPage = 5
        self.allComputerCount = 0
        self.setAllComputerCount()

    def get(self, page):
        try:
            con, cur= KwonDBManager.makeConCur("Hwan/1234@195.168.9.116:1521/xe")

            page = int(page)
            pageCount = ceil(self.allComputerCount / self.computerPerPage)
            start = (page - 1) * self.computerPerPage + 1
            end = page * self.computerPerPage
            
            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, c_no, c_name, c_what, c_ip, c_condition "
            sql += "    FROM ( "
            sql += "        SELECT * "
            sql += "        FROM may22_computer "
            sql += "        ORDER BY c_name, c_ip "
            sql += "    ) "
            sql += ") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)

            computers = []
            for _, no, name, what, ip, cond in cur:
                computers.append(
                    {"no": no, "name": name, "what": what, "ip": ip, "condition": cond}
                )

            return {
                "result": "조회 성공",
                "pageCount": pageCount,
                "computers": computers,
            }
        except:
            return {"result": "조회 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)

    def reg(self, name, what, ip, condition):
        try:
            con, cur= KwonDBManager.makeConCur("Hwan/1234@195.168.9.116:1521/xe")

            sql = "INSERT INTO may22_computer "
            sql += "values(COMPUTER_SEQ.nextval, "
            sql += "'%s', '%s', '%s', '%s')" % (name, what, ip, condition)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allComputerCount += 1
                return {"result": "%s 등록 성공" % name}
            return {"result": "%s 등록 실패" % name}
        except:
            return {"result": "%s 등록 실패" % name}
        finally:
            KwonDBManager.closeConCur(con, cur)

    def setAllComputerCount(self):
        try:
            con, cur= KwonDBManager.makeConCur("Hwan/1234@195.168.9.116:1521/xe")
            #con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.59:1521/xe")
            cur.execute("select count(*) from may22_computer")
            for c in cur:
                self.allComputerCount = c[0]
            for _, no, name, what, ip, cond in cur:
                print(f"no: {no}, name: {name}, what: {what}, ip: {ip}, condition: {cond}")
        except Exception as e:
            print(f"============ Error in setAllComputerCount: {e}")
            pass
        finally:
            KwonDBManager.closeConCur(con, cur)
