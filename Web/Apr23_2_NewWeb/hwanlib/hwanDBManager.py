


from oracledb import connect, init_oracle_client


class HwanDB:
    
    def connectDBServer(url):
        init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")
        con = connect(url)
        cur = con.cursor()
        return con, cur
    
    def closeConCur(con, cur):
        cur.close()
        con.close()
        