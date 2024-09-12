from fastapi import APIRouter, Request, Form, UploadFile, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from database import get_db
from models import Team, User
import os
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

## 다른 사람 메인페이지도 추가해보자.

##유저 생성 페이지
# 유저 생성 페이지 라우트
@router.get("/user/create")
async def create_user_page(request: Request, db: AsyncSession = Depends(get_db)):
    # DB에서 팀 목록을 조회
    result = await db.execute(select(Team))
    teams = result.scalars().all()
    return templates.TemplateResponse("create_user.html", {"request": request, "teams": teams})

@router.post("/user/create")
async def create_user(
    request: Request,
    u_name: str = Form(...),
    u_nickname: str = Form(...),
    u_email: str = Form(None),
    u_git: str = Form(None),
    u_html: UploadFile = Form(None),
    u_css: UploadFile = Form(None),
    photo: UploadFile = Form(None),
    t_id: int = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # 이메일 중복 체크
    result = await db.execute(select(User).filter_by(u_email=u_email))
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        # 이미 존재하는 이메일인 경우 에러 반환
        teams = (await db.execute(select(Team))).scalars().all()
        return templates.TemplateResponse("create_user.html", {
            "request": request,
            "teams": teams,
            "error": "이미 존재하는 이메일입니다."
        })

    # 파일 저장 및 DB 저장 로직
    if u_html:
        # 이메일을 기반으로 파일 이름 생성
        html_filename = f'{u_email}.html'
        file_path_html = f'static/resume_html/{html_filename}'
        with open(file_path_html, 'wb') as f:
            f.write(await u_html.read())
    
    if u_css:
        # 이메일을 기반으로 파일 이름 생성
        css_filename = f'{u_email}.css'
        file_path_css = f'static/css/resume_css/{css_filename}'
        with open(file_path_css, 'wb') as f:
            f.write(await u_css.read())
    
    if photo:
        # 파일의 확장자를 추출하여 이메일 기반 파일 이름 생성
        _, photo_ext = os.path.splitext(photo.filename)
        photo_filename = f'{u_email}{photo_ext}'
        file_path_photo = f'static/images/user_photos/{photo_filename}'
        with open(file_path_photo, 'wb') as f:
            f.write(await photo.read())

    # DB에 유저 정보 저장 로직 추가
    new_user = User(
        u_name=u_name,
        u_nickname=u_nickname,
        u_email=u_email,
        u_git=u_git,
        t_id=t_id,
        u_html= 'resume_html/' + html_filename if u_html else None,
        u_css= 'css/resume_css/' + css_filename if u_css else None,
        u_image= 'images/user_photos/' + photo_filename if photo else None
    )

    db.add(new_user)
    await db.commit()  # 트랜잭션 커밋
    await db.refresh(new_user)

    # 처리가 끝나면 홈으로 리다이렉트
    return RedirectResponse(url="/", status_code=303)
