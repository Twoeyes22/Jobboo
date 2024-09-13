from typing import Optional
import logging
from fastapi import Depends, Query, Request, APIRouter, Form, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from fastapi.templating import Jinja2Templates
from models import Team
from src.main.goo.repository.TeamRepository import TeamRepository
from src.main.goo.model.UploadFileDTO import UploadFileDTO, FileType
import urllib.parse

# 로거 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 데이터베이스 의존성을 주입하는 함수
async def get_team_repository(db: AsyncSession = Depends(get_db)) -> TeamRepository:
    return TeamRepository(db)

@router.get("/team_create", response_class=HTMLResponse, name="create_team")
async def create_team_form(request: Request):
    return templates.TemplateResponse("team/create_team.html", {"request": request})

@router.post("/team_create", name="create_team")
async def create_team(
    t_name: str = Form(...),
    t_intro: Optional[str] = Form(None),
    t_descript: Optional[str] = Form(None),
    t_git: Optional[str] = Form(None),
    t_logo: Optional[UploadFile] = File(None),
    repo: TeamRepository = Depends(get_team_repository)
):
    # 팀 생성 로직
    try:
        team = Team(
            t_name=t_name,
            t_intro=t_intro,
            t_descript=t_descript,
            t_git=t_git,
            t_logo=t_logo.filename if t_logo else None
        )
        await repo.create_team(team)
        # 성공 후 index 페이지로 리다이렉션
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        logging.error("팀 생성 중 오류 발생: %s", str(e))
        raise HTTPException(status_code=500, detail="팀 생성 중 오류 발생")



    

@router.post("/team/check-name", name="check_team_name")
async def check_team_name(request: Request, repo: TeamRepository = Depends(get_team_repository)):
    body = await request.json()  # Parse the JSON body
    name = body.get("name")  # Extract the 'name' key from the JSON

    if not name:
        raise HTTPException(status_code=422, detail="팀 이름을 입력해야 합니다.")

    logging.info(f"Checking team name: {name}")
    existing_team = await repo.get_team_by_name(name)
    
    if existing_team:
        return {"exists": True}
    
    return { "exists" : False }












    

# @router.post("/upload")
# async def upload_file(file: UploadFile):
#     try:
#         file_dto = await UploadFileDTO.create_upload_file_dto(UPLOAD_DIR, file, FileType.IMAGE)
#         return {"message": "파일 업로드 완료", "data": file_dto}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="파일 업로드 중 오류 발생")
