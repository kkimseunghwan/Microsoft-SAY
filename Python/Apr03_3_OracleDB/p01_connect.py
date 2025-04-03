
# 컴퓨터 통신
#   실시간 Socket : 내 의지랑 상관없이
#   안실시간 HTTP : 내가 요청 -> 응답

# DB서버 - Python 프로그램 :
#   안실시간
#   근데 HTTP 통신은 아님.
#   DB메이커 종류는 다양함
#       그 다양한 메이커들간의 표준화된 통신은 없음
#       통신방식이 다 다름.

# Python 입장에서 그 다양한 통신 방식들을 다 만들어 놓을 수가 없음
#   => 없음 => 직접 만들어야 하는데, 

# Python 공식으로는 없지만, 각 DB메이커에서 만들어준게 있으니, 그거 쓰면댐
#       cx_Oracle.py를 썼음 (옛날 이야기-왜씀?) : cx_Oracle.py + instantClient 필요 
#       oracledb.py (최신꺼) : instantClient가 따로 없어도 되는데,
#                               구버전 OracleDB는 지원이 안되서  instantClient가 따로 필요

#######################################################
# Python은 남의거 잘쓰자 -> 중앙제어시스템 : pip
# 시작 - CMD
#   pip install oracledb
#   => 설치
#######################################################

from oracledb import connect, init_oracle_client

# init_oracle_client() # 내장된 instantClient 부르기
# init_oracle_client(lib_dir="instantClient폴더경로") # 구버전 OracleDB라면

try:
    init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")

    # DB 서버 연결 : connect
    # sqlplus로 접속할 때 쓰는 그 형식 (아이디/비번@주소:포트/SID) 입력
    # sqlplus aistudy/1234@195.168.9.116:1521/xe
    con = connect("Hwan/1234@195.168.9.116:1521/xe") 

    print(con)
except Exception as e:
    print("에러메세지:", e)
finally:
    con.close()
