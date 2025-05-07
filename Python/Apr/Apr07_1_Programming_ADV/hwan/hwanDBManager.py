


from oracledb import connect


class HwanDB:
    
    def connectDBServer(url):
        con = connect(url)
        cur = con.cursor()
        return con, cur
    
    def closeConCur(con, cur):
        cur.close()
        con.close()
        