

from oracledb import connect, init_oracle_client

# init_oracle_client() # 내장된 instantClient 부르기
# init_oracle_client(lib_dir="instantClient폴더경로") # 구버전 OracleDB라면

try:
    init_oracle_client(lib_dir="C:\Hwan\Oracle DB\instantclient_23_7")

    # DB 서버 연결 : connect
    # sqlplus로 접속할 때 쓰는 그 형식 (아이디/비번@주소:포트/SID) 입력
    # sqlplus aistudy/1234@195.168.9.116:1521/xe
    con = connect("Hwan/1234@195.168.9.116:1521/xe") 
    print("SUCCESS", con)

    # 데이터 확보 부분
    # DB에 데이터를 간편하게 등록할 수 있는 기능을 만들어보자.
    P_NAME = input("상품의 이름 : ")
    P_PRICE = int(input("상품의 가격 : "))
    
    # INSERT
    # 확보한 데이터를 db에 넣자
    # SQL 문을 str로 작성 (";" 빼고)
    sql = f"INSERT INTO PRODUCT VALUES('{P_NAME}', {P_PRICE})"
    print(sql)

    # DB관련 작업을 총괄 해주는 매니저 겸 결과이기도 함
    cur = con.cursor()

    # execute
    # sql을 DB서버로 전송
    # 전송한 sql을 원격 실행
    # 실행 결과를 받아오고
    cur.execute(sql)

    # 실행 결과
    #   CUD : 데이터 몇 개가 영향받았나 (Update Rows) 
    #   R   : 데이터 (SELECT : 조회)

    # => cur 자체가 결과
    if cur.rowcount: 
        print("등록 성공")
        con.commit()
    
    # 바로 DB서버에 반영x
    # 체크해보고 -> 댔다 -> Commit
    # 체크해보고 -> ㅈ댔다 -> Rollback


    # table?, user? 
    # -> DBA 역할 -> 프로그램에서 테이블 만드는게 아님


except Exception as e:
    print("에러메세지:", e)
finally:
    cur.close()
    con.close()






