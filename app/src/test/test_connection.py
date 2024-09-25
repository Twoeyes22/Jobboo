import pymysql
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv(dotenv_path='.env')

# MySQL 연결 테스트 함수
def test_mysql_connection():
    # 환경 변수에서 DB 정보 가져오기
    db_host = os.getenv('MYSQL_HOST')
    db_user = os.getenv('MYSQL_USER')
    db_password = os.getenv('MYSQL_PASSWORD')
    db_port = int(os.getenv('MYSQL_PORT', 3306))  # 기본 포트 3306
    db_name = os.getenv('MYSQL_DATABASE')

    print(db_host)
    print(db_user)
    print(db_password)
    print(db_port)
    print(db_name)

    # MySQL 연결 시도
    try:
        connection = pymysql.connect(host=db_host, user=db_user, password=db_password, port=db_port)
        connection.close()
        assert True  # 연결이 성공하면 테스트 통과
    except Exception as e:
        assert False, f"Error connecting to MySQL: {e}"
