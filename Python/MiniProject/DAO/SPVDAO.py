

from DB_Set.DBManager import DBManager
from DTO.SPV import SPV


class SPVDAO:
    
    def getDataByCompanyName(self, companyName):
        try:
            con, cur = DBManager.connectDBServer("seong/137@195.168.9.116:1521/xe")
            sql = f"SELECT * FROM SPV WHERE M_C_NO IN (SELECT C_NO FROM COMPANY WHERE C_NAME = '{companyName}')"
            cur.execute(sql)
            spvs = []
            for m_no, m_name, m_price, m_maker, c_link, m_c_no in cur:
                spvs.append(SPV(m_no, m_name, m_price, m_maker, c_link, m_c_no))

            return spvs
        except Exception as e:
            print("ERROR", e)
        finally:
            DBManager.closeConCur(con, cur)

