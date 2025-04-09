
from oracledb import init_oracle_client

from oracledb import connect

class DBManager:
    @staticmethod
    def connectDBServer(url):
        init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")
        con = connect(url)
        cur = con.cursor()
        return con, cur
    
    @staticmethod
    def closeConCur(con, cur):
        cur.close()
        con.close()
        