from pymongo import MongoClient

# OracleDB
#   SQL이라는 별개의 언어로 제어
#   테이블?

# MongoDB
#   JS라는 PL로 제어 : Python과 비슷
#   JS의 배열 : [] : Python의 Listr
#   JS의 객체 : {} : Python의 Dict
#   => Pymongo : MongoDB 명령어 거의 그대로 쓰게 해줌.

# 연결
con = MongoClient("195.168.9.139") # 서버주소
db = con.Hwan # DB연결. => con.DB명

# 데이터 확보
name = input("이름 : ")
price = int(input("가격 : "))

# 명령어 서버로 전송 + 원격실행 + 결과받기
result = db.Apr14_snack.insert_one({"s_name": name, "s_price": price})

if result.acknowledged:
    price("성공")

con.close()