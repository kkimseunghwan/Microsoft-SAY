from pymongo import ASCENDING, DESCENDING, MongoClient

# 연결
con = MongoClient("195.168.9.139") # 서버주소
db = con.Hwan # DB연결. => con.DB명

# snack = db.Apr14_snack.find() # 전체 조회

# 정렬
# ASCENDING:오름차순, DESCENDING:내림차순
snack = db.Apr14_snack.find().sort([("s_price", DESCENDING), ("s_name", ASCENDING)])  

print(type(snack))
for s in snack:
    print(s)

con.close()