



from pymongo import MongoClient

con = MongoClient("195.168.9.139") # 서버주소
print(con)
db = con.Hwan # DB연결. => con.DB명
print(db)
con.close()