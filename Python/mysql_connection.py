import mysql.connector

def connect_to_mysql():
    try:
        # MySQL 연결 설정
        connection = mysql.connector.connect(
            host="localhost",      # MySQL 서버 주소
            port=3306,            # MySQL 포트 번호
            user="your_username",  # MySQL 사용자 이름
            password="your_password",  # MySQL 비밀번호
            database="your_database"   # 사용할 데이터베이스 이름
        )
        
        if connection.is_connected():
            print("MySQL 데이터베이스에 성공적으로 연결되었습니다.")
            return connection
            
    except mysql.connector.Error as error:
        print(f"MySQL 연결 중 오류 발생: {error}")
        return None

def close_connection(connection):
    if connection is not None and connection.is_connected():
        connection.close()
        print("MySQL 연결이 종료되었습니다.")

# 사용 예시
if __name__ == "__main__":
    # 데이터베이스 연결
    conn = connect_to_mysql()
    
    if conn is not None:
        try:
            # 커서 생성
            cursor = conn.cursor()
            
            # SQL 쿼리 실행 예시
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"MySQL 버전: {version[0]}")
            
        except mysql.connector.Error as error:
            print(f"쿼리 실행 중 오류 발생: {error}")
            
        finally:
            # 커서와 연결 종료
            cursor.close()
            close_connection(conn) 