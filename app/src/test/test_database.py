import pymysql
from dotenv import load_dotenv
import os



# .env 파일 로드
load_dotenv(dotenv_path='.env')

# 데이터베이스 생성 테스트 함수
def test_create_database():
    # 환경 변수에서 DB 정보 가져오기
    db_host = os.getenv('MYSQL_HOST')
    db_user = os.getenv('MYSQL_USER')
    db_password = os.getenv('MYSQL_PASSWORD')
    db_port = int(os.getenv('MYSQL_PORT', 3306))  # 기본 포트 3306
    db_name = os.getenv('MYSQL_DATABASE')  # 기본 DB 이름 설정

    # 데이터베이스 생성 시도
    try:
        connection = pymysql.connect(host=db_host, user=db_user, password=db_password, port=db_port)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        connection.commit()
        cursor.close()
        connection.close()
        assert True  # 데이터베이스 생성이 성공하면 테스트 통과
    except Exception as e:
        assert False, f"Error creating database: {e}"
