from fastapi import APIRouter, Request, Depends, HTTPException, Form, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, PlainTextResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from database import get_db
from models import Team, User
import os
import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request, db: AsyncSession = Depends(get_db)):
    # 모든 팀 정보 조회
    result = await db.execute(select(Team))
    teams = result.scalars().all()

    # 첫 번째 팀의 정보와 멤버 조회 (기본값)
    if teams:
        first_team = teams[0]
        users_result = await db.execute(
            select(User).filter(User.t_id == first_team.t_id)
        )
        team_members = users_result.scalars().all()
    else:
        first_team = None
        team_members = []

    return templates.TemplateResponse("index.html", {
        "request": request,
        "teams": teams,
        "current_team": first_team,
        "team_members": team_members
    })

@router.get("/api/user/{user_id}")
async def user_info(user_id: int, db: AsyncSession = Depends(get_db)):
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

@router.get("/team/{team_id}")
async def team_page(request: Request, team_id: int, db: AsyncSession = Depends(get_db)):
    # 모든 팀 정보 조회
    all_teams_result = await db.execute(select(Team))
    all_teams = all_teams_result.scalars().all()

    # 특정 팀 정보 조회
    team_result = await db.execute(select(Team).filter(Team.t_id == team_id))
    team = team_result.scalar_one_or_none()

    if team:
        # 해당 팀의 멤버 정보 조회
        users_result = await db.execute(select(User).filter(User.t_id == team_id))
        team_members = users_result.scalars().all()
    else:
        team_members = []

    return templates.TemplateResponse("index.html", {
        "request": request,
        "teams": all_teams,
        "current_team": team,
        "team_members": team_members
    })

@router.get("/resume/{user_id}")
async def resume(request: Request, user_id: int, db: AsyncSession = Depends(get_db)):
    # 특정 사용자 정보 조회
    user_result = await db.execute(select(User).filter(User.u_id == user_id))
    user = user_result.scalar_one_or_none()

    if user and user.u_html:
        try:
            # StaticFiles 인스턴스를 통해 파일 경로 얻기
            file_info = request.app.state.static.lookup_path(user.u_html)
            
            if file_info:
                file_path, _ = file_info  # 튜플 언패킹
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                return HTMLResponse(content=content)
            else:
                raise FileNotFoundError(f"File info not found for path: {user.u_html}")
        except Exception as e:
            timestamp = datetime.datetime.now().isoformat()
            error_info = {
                "timestamp": timestamp,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "user_html_path": user.u_html,
                "file_info": str(file_info) if 'file_info' in locals() else "Not available"
            }
            return templates.TemplateResponse("404.html", {"request": request, "error_info": error_info}, status_code=404)
    elif user:
        return templates.TemplateResponse("404.html", {"request": request, "message": "Resume HTML not set for this user"}, status_code=404)
    else:
        return templates.TemplateResponse("404.html", {"request": request, "message": "User not found"}, status_code=404)
    
    
    
    
    

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

