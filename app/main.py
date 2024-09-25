from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import pages
from database import engine
from models import Base
from src.main.goo.controller.TeamController import router as team_router



# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 정적 파일(CSS, JS, 이미지 등)을 서비스하기 위한 설정
# "/static" URL 경로로 "app/static" 디렉토리의 파일들을 제공
static_files = StaticFiles(directory="static")
app.mount("/static", static_files, name="static")
app.state.static = static_files

# Jinja2 템플릿 엔진 설정, "app/templates" 디렉토리에서 템플릿을 찾음
templates = Jinja2Templates(directory="templates")

# pages 모듈에서 정의한 라우터를 애플리케이션에 포함
app.include_router(pages.router)
# 240911 goo - Team 라우터 추가
app.include_router(team_router)


@app.on_event("startup")
async def startup():
    # 비동기 컨텍스트 매니저를 사용하여 데이터베이스 엔진에 연결
    async with engine.begin() as conn:
        # Base.metadata.create_all() 메서드를 사용하여 모든 정의된 테이블 생성
        # run_sync()는 동기 메서드를 비동기 컨텍스트에서 실행하기 위해 사용
        await conn.run_sync(Base.metadata.create_all)


