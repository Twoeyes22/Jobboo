from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# DB.env 파일 로드
load_dotenv('app/.env')

# 환경 변수에서 데이터베이스 접속 정보 가져오기
DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
DB_NAME = os.getenv('MYSQL_DATABASE')
DB_HOST = os.getenv('MYSQL_HOST', 'db')  # 기본값으로 'db' 사용

# 비동기 데이터베이스 URL 구성
DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# 비동기 세션 생성
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# 비동기 데이터베이스 세션 제공 함수
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
