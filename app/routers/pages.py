from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# 라우터 객체 생성
router = APIRouter()

# Jinja2 템플릿 엔진 설정
templates = Jinja2Templates(directory="templates")

# 팀원 정보를 담은 리스트, 실제 프로젝트에서는 데이터베이스에서 가져올 수 있음
team_members = [
    {"name": "Seoyeon", "image": "Seoyeon.jpg", "resume": "Seoyeon.html"},
    {"name": "Minwoo", "image": "Minwoo.png", "resume": "Minwoo.html"},
    {"name": "Hongjip", "image": "Hongjip.jpg", "resume": "Hongjip.html"},
    {"name": "Gwangjin", "image": "Gwangjin.jpg", "resume": "Gwangjin.html"},
    {"name": "Boyeong", "image": "Boyeong.jpg", "resume": "Boyeong.html"},
    {"name": "Jiman", "image": "Jiman.jpg", "resume": "Jiman.html"},
    {"name": "Goo", "image": "Goo.jpg", "resume": "Goo.html"}
    # ... 다른 팀원들 추가
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