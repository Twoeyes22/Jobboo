from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Team
from database import get_db

# 라우터 객체 생성
router = APIRouter()

# Jinja2 템플릿 엔진 설정
templates = Jinja2Templates(directory="templates")


# 팀원 정보를 담은 리스트, DB를 사용해보자!
team_members = [
    {"name": "Seoyeon", "image": "Seoyeon.jpg", "resume": "Seoyeon.html"},
    {"name": "Minwoo", "image": "minwoo.png", "resume": "minwoo.html"},
    {"name": "Hongjip", "image": "Hongjip.jpg", "resume": "Hongjip.html"},
    {"name": "Gwangjin", "image": "Gwangjin.jpg", "resume": "Gwangjin.html"},
    {"name": "Boyeong", "image": "Boyeong.jpg", "resume": "Boyeong.html"},
    {"name": "Jiman", "image": "Jiman.jpg", "resume": "Jiman.html"},
    {"name": "Goo", "image": "Goo.jpg", "resume": "Goo.html"}
]

# 홈페이지 라우트
@router.get("/")
async def home(request: Request):
    # index.html 템플릿을 렌더링하고, 팀원 정보를 전달
    return templates.TemplateResponse("index.html", {"request": request, "team_members": team_members})

# 개별 이력서 페이지 라우트
@router.get("/resume/{member_name}")
async def resume(request: Request, member_name: str):
    # 해당 팀원의 이력서 HTML 파일을 렌더링
    return templates.TemplateResponse(f"resume/{member_name}.html", {"request": request})

@router.get("/user/{user_id}")
async def team_info(user_id: int, db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.u_id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()  # 유저 정보가 없으면 None 반환
    
    if user is None:
        return {"error": "User not found"}

    return {
        "u_nickname": user.u_nickname,
        "u_id": user.u_id,
        "u_name": user.u_name,
        "u_email": user.u_email,
        "u_git": user.u_git
    }